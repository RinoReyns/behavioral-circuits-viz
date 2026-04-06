"""
activation_extractor.py
Hooks into each layer and stores residual stream activations.
Returns: dict[layer_idx -> tensor of shape (seq_len, d_model)]
"""


def extract_activations(model, tokens) -> dict:
    raise NotImplementedError
