import json
from pathlib import Path


def load_pairs(cfg):
    path = Path(cfg["dataset"]["path"])

    pairs = {}

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            item = json.loads(line)

            # -------------------------------------------------
            # CASE 1: SIMPLE FORMAT (single prompt)
            # {"prompt": "...", "label": "...", "category": "..."}
            # -------------------------------------------------
            if "variant" not in item:
                pid = item.get("category", "unknown")

                pairs.setdefault(pid, {})
                pairs[pid]["single"] = {
                    "prompt": item["prompt"],
                    "label": item["label"],
                    "category": item.get("category", None),
                }

            # -------------------------------------------------
            # CASE 2: PAIR FORMAT (safe/unsafe comparison)
            # {"id", "concept", "pair_id", "variant", ...}
            # -------------------------------------------------
            else:
                pid = item["pair_id"]

                pairs.setdefault(pid, {})
                pairs[pid][item["variant"]] = {
                    "prompt": item["prompt"],
                    "label": item["label"],
                    "concept": item.get("concept"),
                    "risk_level": item.get("risk_level"),
                    "template_id": item.get("template_id"),
                    "seed": item.get("seed"),
                    "id": item.get("id"),
                }

    return pairs