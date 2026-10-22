"""Library testing generic repo graph builder."""

from __future__ import annotations


class RepoGraphBuilder:
    def __init__(self) -> None:
        self.nodes = []

    def build(self, target: str) -> dict:
        return {"target": target, "nodes": []}
