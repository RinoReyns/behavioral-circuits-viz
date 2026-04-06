"""
loader.py
Loads GPT-2 / Pythia / Llama models via TransformerLens.
Reads model registry from configs/model_*.yaml.
"""
from transformer_lens import HookedTransformer


def load_model(model_name: str) -> HookedTransformer:
    """Load and return a HookedTransformer model by name."""
    return HookedTransformer.from_pretrained(model_name)
