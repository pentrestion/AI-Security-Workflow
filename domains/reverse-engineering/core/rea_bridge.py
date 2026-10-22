"""REA (multi-engine reverse engineering orchestrator)."""

from __future__ import annotations


class REABridge:
    def __init__(self) -> None:
        self.engines = []

    def register_engine(self, name: str) -> None:
        self.engines.append(name)
