"""
causal_scorer.py
Aggregates patching / ablation results into per-component causal importance scores.
Output feeds directly into visualization/causal_markers.py.
"""


def compute_scores(patching_results: dict) -> dict:
    raise NotImplementedError
