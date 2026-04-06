# Data

## Schema — `pairs/*.jsonl`
Each line is a JSON object:
```json
{
  "prompt_allowed":    "...",   // benign / grounded prompt
  "prompt_disallowed": "...",   // harmful / hallucination-prone prompt
  "behavior":          "refusal | hallucination",
  "domain":            "chemistry | security | ...",
  "source":            "manual | advbench | hh-rlhf | truthfulqa"
}
```

## Sources
- **AdvBench**: Zou et al. 2023 — 500 harmful instruction pairs
- **HH-RLHF**: Anthropic — helpful/harmless dialogue splits
- **TruthfulQA**: Lin et al. 2022 — adversarial truthfulness probing
- **manual**: Hand-crafted pairs for controlled experiments
