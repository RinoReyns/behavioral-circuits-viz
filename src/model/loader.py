"""
loader.py
Loads GPT-2 / Pythia / Llama models via TransformerLens.
Reads model registry from configs/model_*.yaml.
"""

from transformer_lens import HookedTransformer
from src.config.config import load_yaml_config


def load_model_config(config_path: str):
    cfg = load_yaml_config(config_path)
    return cfg["model"]


def load_model(experiment_cfg: dict):
    """
    Loads model using:
    experiment.yaml → model.config → model.yaml
    """

    model_config_path = experiment_cfg["model_config"]
    model_cfg = load_model_config(model_config_path)
    hf_repo = model_cfg["hf"]["repo"]

    print(f"\nLoading model: {model_cfg['id']} ({hf_repo})")

    # 4. load TransformerLens model
    model = HookedTransformer.from_pretrained(
        hf_repo,
        device=model_cfg["device"]
    )

    return model, model_cfg
