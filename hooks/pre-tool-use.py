#!/usr/bin/env python3
"""PreToolUse hook for AI-Security-Workflow.

Reads the Claude Code hook event from stdin. Exits 0 to allow, 2 to block
(stderr is shown to the model as feedback), any other code for a non-blocking
error.

Gates enforced:
  - engagement.json must exist before network or destructive commands run
  - network commands are blocked unless the target appears in scope_hosts
    or network_enabled=true is set in .engagement/sandbox.json
  - destructive shell patterns are blocked unconditionally
  - credential-read patterns are blocked unconditionally
  - MCP tools are blocked if the engagement window has expired
"""
from __future__ import annotations

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(os.environ.get("CLAUDE_PROJECT_DIR", ".")).resolve()
ENGAGEMENT_FILE = PROJECT_ROOT / "engagement.json"
SANDBOX_FILE = PROJECT_ROOT / ".engagement" / "sandbox.json"
AUDIT_LOG = PROJECT_ROOT / ".engagement" / "audit.jsonl"

NETWORK_COMMANDS = re.compile(
    r"\b(curl|wget|nc|ncat|netcat|ssh|scp|ftp|telnet|nmap|masscan|"
    r"sqlmap|ffuf|nikto|nuclei|hydra|gobuster|dirb)\b",
    re.IGNORECASE,
)
DESTRUCTIVE_PATTERNS = re.compile(
    r"(rm\s+-rf\s+/|mkfs|dd\s+if=/dev|:\(\)\s*\{|shutdown|reboot|"
    r"DROP\s+TABLE|TRUNCATE\s+TABLE|chmod\s+-R\s+777\s+/)",
    re.IGNORECASE,
)
CREDENTIAL_READ = re.compile(
    r"(cat\s+/etc/shadow|cat\s+.*\.env\b|printenv\s*$|cat\s+.*id_rsa|"
    r"cat\s+.*id_ed25519)",
    re.IGNORECASE,
)


def block(reason: str, code: int = 2) -> None:
    print(f"BLOCKED (pre-tool-use): {reason}", file=sys.stderr)
    sys.exit(code)


def allow(message: str = "") -> None:
    if message:
        print(message)
    sys.exit(0)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        block(f"Malformed JSON at {path}: {exc}")


def audit(event: dict, decision: str, reason: str = "") -> None:
    try:
        AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG.open("a") as fh:
            fh.write(json.dumps({
                "ts": datetime.now(timezone.utc).isoformat(),
                "tool": event.get("tool_name"),
                "decision": decision,
                "reason": reason,
                "input": event.get("tool_input"),
            }) + "\n")
    except OSError:
        pass


def load_engagement() -> dict:
    eng = load_json(ENGAGEMENT_FILE)
    required = ["engagement_id", "authorization_ref", "scope_hosts", "window_end"]
    missing = [k for k in required if not eng.get(k)]
    if missing:
        return {"_bootstrap": True, "_missing": missing}
    return eng


def load_sandbox(eng: dict) -> dict:
    sb = load_json(SANDBOX_FILE)
    if not sb.get("profile"):
        sb["profile"] = eng.get("sandbox_profile", "docker-none")
    if "network_enabled" not in sb:
        sb["network_enabled"] = False
    return sb


def check_window(eng: dict) -> None:
    try:
        end = datetime.fromisoformat(eng["window_end"].replace("Z", "+00:00"))
    except (KeyError, ValueError):
        return
    if datetime.now(timezone.utc) > end:
        block(f"Engagement window expired at {eng['window_end']}")


def check_bash(command: str, eng: dict, sb: dict) -> None:
    if DESTRUCTIVE_PATTERNS.search(command):
        block(f"Destructive pattern: {command[:120]!r}")
    if CREDENTIAL_READ.search(command):
        block(f"Credential-read pattern: {command[:120]!r}")

    if not NETWORK_COMMANDS.search(command):
        return

    if eng.get("_bootstrap"):
        block(
            "Network command with no engagement.json. Create the file first "
            f"(missing: {', '.join(eng['_missing'])})."
        )

    if sb.get("network_enabled"):
        return

    allowlist = [str(h).lower() for h in eng.get("scope_hosts", [])]
    lowered = command.lower()
    if not any(host in lowered for host in allowlist):
        block(
            "Network command targets no in-scope host. Either add the host to "
            "scope_hosts in engagement.json or set network_enabled=true in "
            ".engagement/sandbox.json."
        )


def check_mcp(tool_name: str, eng: dict) -> None:
    if eng.get("_bootstrap"):
        block(
            f"MCP tool {tool_name} invoked with no engagement.json. "
            f"Missing: {', '.join(eng['_missing'])}."
        )
    check_window(eng)


def main() -> None:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        block(f"Invalid hook event: {exc}")

    tool_name = event.get("tool_name", "")
    tool_input = event.get("tool_input") or {}

    eng = load_engagement()
    sb = load_sandbox(eng)

    if tool_name == "Bash":
        check_bash(tool_input.get("command", ""), eng, sb)
    elif tool_name.startswith("mcp__"):
        check_mcp(tool_name, eng)

    audit(event, "allow")
    allow(f"pre-tool-use: allowed {tool_name}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception as exc:
        print(f"BLOCKED (pre-tool-use internal error): {exc}", file=sys.stderr)
        sys.exit(2)
