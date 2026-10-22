#!/usr/bin/env bash
set -euo pipefail

# Official Hex-Rays IDA MCP — requires IDA Pro / Home / Classroom 8.3+
echo "[*] Install uv, then:"
echo "    uvx ida-hcli mcp install"
echo ""
echo "[*] For the community server (IDA 8.3+, IDA Free unsupported):"
echo "    git clone https://github.com/mrexodia/ida-pro-mcp"
echo "    cd ida-pro-mcp && pip install -r requirements.txt"
echo ""
echo "[*] Note: official IDA MCP is free and open source, works headlessly"
echo "    with idalib for pipeline processing, and shares IDBs across agents."
