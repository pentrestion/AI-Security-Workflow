"""Builds contextual knowledge for a given engagement.

This module consolidates scope, target metadata, recon data, and playbook context
into a single knowledge bundle that the AI can safely consume.
"""

from __future__ import annotations


class ContextBuilder:
    def __init__(self) -> None:
        self.knowledge = {}

    def build(self, engagement: str, domain: str) -> dict:
        self.knowledge[engagement] = {
            "domain": domain,
            "scope": "Authorized testing only",
            "notes": "Refute-first verification required",
        }
        return self.knowledge[engagement]
