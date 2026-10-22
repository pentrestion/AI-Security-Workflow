"""IDA MCP bridge placeholder for official or community servers."""

from __future__ import annotations


class IDAMCPBridge:
    def __init__(self, server_name: str = "ida") -> None:
        self.server_name = server_name
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def list_functions(self, binary: str) -> list[dict]:
        return [{"binary": binary, "functions": []}]
