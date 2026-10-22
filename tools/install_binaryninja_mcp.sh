#!/usr/bin/env bash
set -euo pipefail

# Headless Binary Ninja MCP — 180 tools, containerized
echo "[*] Requires Binary Ninja Commercial or Ultimate"
echo "    pip install binaryninja-mcp"
echo "    uvx binaryninja-mcp install-api"
echo "    uvx binaryninja-mcp server <binary>"
