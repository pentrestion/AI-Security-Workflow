"""Frida runtime instrumentation bridge.

This provides the hook layer for dynamic tracing in a disposable VM or sandbox.
"""

from __future__ import annotations


class FridaBridge:
    def __init__(self) -> None:
        self.session = None

    def attach(self, process_name: str) -> None:
        self.process_name = process_name
