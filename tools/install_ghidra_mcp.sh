#!/usr/bin/env bash
set -euo pipefail

# Zero-cost route: Ghidra + LaurieWired GhidraMCP
GHIDRA_VERSION="12.1.4"

echo "[*] Install Ghidra ${GHIDRA_VERSION} manually from https://ghidra-sre.org/"
echo "[*] Install uv: https://docs.astral.sh/uv/"
echo "[*] Then install the plugin:"
echo "    pip install git+https://github.com/LaurieWired/GhidraMCP"
echo ""
echo "[*] In Ghidra: File -> Install Extensions -> select GhidraMCP zip"
echo "[*] Restart Ghidra, enable GhidraMCPPlugin in File -> Configure -> Developer"
echo "[*] Start the server: Tools -> GhidraMCP -> Start MCP Server"
echo "[*] Register with Claude Code:"
echo "    claude mcp add ghidra -- uvx ghidra-mcp"
