# behavioral-circuits-viz

> **Causal Visualization of Behavioral Circuits in Language Models**

A research tool for tracing how high-level behaviors (refusal, hallucination)
emerge causally across layers of a language model — with an interactive
Behavior Flow Map visualization.

## Quickstart

```bash
# 1. Clone and install
git clone https://github.com/YOUR_USERNAME/behavioral-circuits-viz.git
cd behavioral-circuits-viz
pip install -e ".[dev]"

# 2. Set up environment
cp .env.example .env   # fill in HF_TOKEN

# 3. Train probes
make probes

# 4. Run causal analysis
make causal

# 5. Launch interactive tool
make app
```

## Pipeline

```
data/ → src/model → src/probes → src/causal → src/visualization → src/tool
```

## Structure

| Directory | Purpose |
|-----------|---------|
| `data/` | Contrastive prompt pairs (JSONL) |
| `src/model/` | TransformerLens model loading + activation extraction |
| `src/probes/` | Layer-wise logistic regression probes |
| `src/causal/` | Activation patching + ablation |
| `src/visualization/` | Behavior Flow Map rendering |
| `src/tool/` | Streamlit interactive interface |
| `experiments/` | Reproducible experiment scripts |
| `configs/` | YAML configs for models and experiments |
| `paper/` | LaTeX source for research paper |

## Citation

```bibtex
@misc{bcv2026,
  title={Causal Visualization of Behavioral Circuits in Language Models},
  author={Lukasz Pindor},
  year={2026}
}
```
