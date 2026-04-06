"""
cache_manager.py
Saves and loads activation caches to/from disk.
Format: .pt files keyed by (model_name, prompt_hash, layer).
"""


def save_cache(cache: dict, path: str) -> None:
    raise NotImplementedError


def load_cache(path: str) -> dict:
    raise NotImplementedError
