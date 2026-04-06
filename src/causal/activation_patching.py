"""
activation_patching.py
Patches clean activations into corrupt (disallowed) runs layer by layer.
Measures how much each layer's residual stream causally drives behavior.
"""


def patch_layer(model, clean_cache, corrupt_tokens, layer: int) -> float:
    raise NotImplementedError
