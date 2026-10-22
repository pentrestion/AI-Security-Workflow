"""Model routing for security testing workloads.

This file is intentionally lightweight and meant to be extended with model-choice
logic such as local models, DeepSeek, Gemini, Opus, and GPT-4o routing.
"""

from __future__ import annotations


class ModelRouter:
    """Select an LLM based on task difficulty and cost profile."""

    def __init__(self) -> None:
        self.profiles = {
            "recon": ["ollama:qwen2.5", "deepseek-chat"],
            "planning": ["gemini-2.0-pro", "gpt-4o"],
            "verification": ["claude-opus", "gpt-4o"],
        }

    def select(self, task_type: str) -> str:
        return self.profiles.get(task_type, ["ollama:qwen2.5"])[0]
