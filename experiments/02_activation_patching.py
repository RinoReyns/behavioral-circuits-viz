"""
02_activation_patching.py
Full layer-wise activation patching sweep.
Saves causal importance scores to experiments/results/causal/.
Usage: python experiments/02_activation_patching.py --config configs/experiment_refusal.yaml
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()
