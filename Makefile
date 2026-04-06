.PHONY: help install data probes causal app test lint clean

help:
	@echo ""
	@echo "  behavioral-circuits-viz"
	@echo "  ─────────────────────────────────────────"
	@echo "  make install   Install dependencies via pip"
	@echo "  make data      Build contrastive pair datasets"
	@echo "  make probes    Train probes on all layers"
	@echo "  make causal    Run activation patching sweep"
	@echo "  make app       Launch Streamlit tool"
	@echo "  make test      Run pytest suite"
	@echo "  make lint      Run ruff linter"
	@echo "  make clean     Remove cached artifacts"
	@echo ""

install:
	pip install -e ".[dev]"

data:
	python experiments/01_baseline_probes.py --config configs/experiment_refusal.yaml

probes:
	python experiments/01_baseline_probes.py --config configs/experiment_refusal.yaml

causal:
	python experiments/02_activation_patching.py --config configs/experiment_refusal.yaml

app:
	streamlit run src/tool/app.py

test:
	pytest tests/ -v --cov=src

lint:
	ruff check src/ experiments/ tests/

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
