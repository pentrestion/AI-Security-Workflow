"""Memory and ledger modules for findings and false positives."""

from __future__ import annotations


class Memory:
    def __init__(self) -> None:
        self.findings = []
        self.false_positives = []

    def add_finding(self, finding: str) -> None:
        self.findings.append(finding)
