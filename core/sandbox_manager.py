"""Sandbox lifecycle manager.

This placeholder manages Docker/gVisor execution for exploit verification.
"""

from __future__ import annotations


class SandboxManager:
    def __init__(self) -> None:
        self.running = False

    def start(self, network_mode: str = "none") -> None:
        self.running = True
        self.network_mode = network_mode
