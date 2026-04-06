"""
prompt_generator.py
Generates allowed / disallowed prompt variants for a given topic.
Can use rule-based templates or an LLM (Claude API) for paraphrasing.
"""


def generate_pair(topic: str) -> dict:
    raise NotImplementedError
