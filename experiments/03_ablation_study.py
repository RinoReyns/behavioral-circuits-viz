"""
03_ablation_study.py
Head-level and MLP-level ablation experiments.
Usage: python experiments/03_ablation_study.py --config configs/experiment_refusal.yaml
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()
