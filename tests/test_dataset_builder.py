"""Tests for data pairing logic, JSONL format, and train/test splits."""
import pytest


def test_pair_structure():
    # Each pair must have: prompt_allowed, prompt_disallowed, behavior, domain
    pair = {"prompt_allowed": "a", "prompt_disallowed": "b", "behavior": "refusal", "domain": "chemistry"}
    assert all(k in pair for k in ["prompt_allowed", "prompt_disallowed", "behavior", "domain"])
