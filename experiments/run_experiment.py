import sys
import json
from pathlib import Path

from src.config.config import load_yaml_config
from src.model.loader import load_model
from src.data.dataset_loader import load_pairs


def run_with_cache(model, prompt):
    tokens = model.to_tokens(prompt, prepend_bos=True)
    _, cache = model.run_with_cache(tokens)
    return cache


def layerwise_diff(cache_safe, cache_unsafe, n_layers):

    diffs = {}

    for layer in range(n_layers):

        safe_act = cache_safe["resid_post", layer]
        unsafe_act = cache_unsafe["resid_post", layer]

        # shape: [batch, seq, d_model] -> [batch, d_model]
        safe_last = safe_act[:, -1, :]
        unsafe_last = unsafe_act[:, -1, :]

        # compute squared L2 distance
        diff = (safe_last - unsafe_last).pow(2).mean().item()

        diffs[f"layer_{layer}"] = diff

    return diffs

def main(config_path):

    cfg = load_yaml_config(config_path)["experiment"]

    # ------------------
    # setup
    # ------------------
    model, model_cfg = load_model(cfg)
    pairs = load_pairs(cfg)

    n_layers = model_cfg["architecture"]["n_layers"]
    results = []

    for pair_id, pair in pairs.items():

        # ----------------------------
        # CASE 1: PAIRED DATA
        # ----------------------------
        if "safe" in pair and "unsafe" in pair:

            safe_prompt = pair["safe"]["prompt"]
            unsafe_prompt = pair["unsafe"]["prompt"]

            cache_safe = run_with_cache(model, safe_prompt)
            cache_unsafe = run_with_cache(model, unsafe_prompt)

            diffs = layerwise_diff(cache_safe, cache_unsafe, n_layers)

            results.append({
                "pair_id": pair_id,
                "type": "paired",
                "layerwise_diff": diffs
            })

        # ----------------------------
        # CASE 2: SINGLE DATA
        # ----------------------------
        elif "single" in pair:

            prompt = pair["single"]["prompt"]
            label = pair["single"]["label"]

            cache = run_with_cache(model, prompt)

            results.append({
                "pair_id": pair_id,
                "type": "single",
                "label": label,
                "activation_norm": {
                    f"layer_{l}": cache["resid_post", l].norm().item()
                    for l in range(n_layers)
                }
            })

        else:
            continue

        print(f"Processed {pair_id}")

        # --------------------------
        # save output
        # --------------------------
    out_path = Path(cfg["output_dir"])
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("Done:", out_path)


if __name__ == "__main__":
    main(sys.argv[1])