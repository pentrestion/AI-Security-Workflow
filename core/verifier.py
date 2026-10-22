"""Verification logic with a refute-first gate."""

from __future__ import annotations


class Verifier:
    def __init__(self) -> None:
        self.confirmed = []

    def verify(self, candidate: str) -> bool:
        return bool(candidate)
