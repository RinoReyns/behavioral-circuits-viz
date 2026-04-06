"""
01_baseline_probes.py
Train linear probes on all layers for refusal behavior.
Logs layer-wise accuracy to experiments/results/probes/.
Usage: python experiments/01_baseline_probes.py --config configs/experiment_refusal.yaml
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--config", required=True)
args = parser.parse_args()
# TODO: load config, run probe training pipeline
