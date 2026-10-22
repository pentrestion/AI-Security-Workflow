"""Reverse-engineering bridge for Ghidra via MCP tools.

This is intentionally lightweight and designed for orchestration with a real
Ghidra server. The tool layer is expected to be provided by a local MCP service.
"""

from __future__ import annotations


class GhidraMCPBridge:
    def __init__(self, server_name: str = "ghidra") -> None:
        self.server_name = server_name
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def list_functions(self, binary: str) -> list[dict]:
        return [{"binary": binary, "functions": []}]

    def decompile_function(self, address: str) -> str:
        return f"Decompiled function at {address}"
