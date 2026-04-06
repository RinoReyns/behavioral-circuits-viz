"""
ablation.py
Zero-ablation and mean-ablation of attention heads and MLP layers.
Used to identify causally necessary components.
"""


def zero_ablate(model, tokens, component: str, layer: int, head: int = None):
    raise NotImplementedError


def mean_ablate(model, tokens, mean_cache, component: str, layer: int):
    raise NotImplementedError
