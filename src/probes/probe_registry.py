"""
probe_registry.py
Tracks trained probes indexed by (model_name, behavior, layer).
Persists to probes/saved/.
"""


def register(probe, model_name: str, behavior: str, layer: int) -> None:
    raise NotImplementedError


def load(model_name: str, behavior: str, layer: int):
    raise NotImplementedError
