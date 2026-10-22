"""Skill loader for parameter-gated workflow execution.

This validates YAML frontmatter and required parameters before prompt assembly.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


class Refusal(Exception):
    def __init__(self, reason: str, remediation: str | None = None):
        super().__init__(reason)
        self.reason = reason
        self.remediation = remediation


def parse_frontmatter(path: str) -> dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}
    fm = text[4:end]
    data: dict[str, Any] = {}
    for line in fm.splitlines():
        if not line or line.strip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_token(token: str | None) -> bool:
    if not token:
        return False
    return len(token) >= 12 and token.count("-") >= 1


def load_skill(path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    params = params or {}
    fm = parse_frontmatter(path)
    if not fm:
        raise Refusal("Skill file missing YAML frontmatter", "Add a valid --- block at the top of the skill file.")

    requires = fm.get("requires", [])
    if isinstance(requires, str):
        requires = [requires]
    for key in requires:
        if key not in params:
            raise Refusal(f"missing {key}", f"Supply {key} before invoking the skill.")

    blocks = fm.get("blocks_execution_if", [])
    if isinstance(blocks, str):
        blocks = [blocks]
    for key in blocks:
        if key in params and params.get(key) is True:
            raise Refusal(f"gate failed: {key}", "Resolve the blocking condition before execution.")

    if "engagement_token" in params:
        if not validate_token(params["engagement_token"]):
            raise Refusal("UNAUTHORIZED_SKILL_INVOCATION", "Provide a valid engagement token.")

    return {"name": fm.get("name"), "phase": fm.get("phase"), "frontmatter": fm, "params": params}


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Load and validate a security skill file.")
    parser.add_argument("skill_path", help="Path to a skill markdown file.")
    parser.add_argument("--params", help="JSON object with params to validate")
    args = parser.parse_args()

    params = json.loads(args.params) if args.params else {}
    try:
        result = load_skill(args.skill_path, params)
        print(json.dumps({"status": "OK", "skill": result["name"], "phase": result["phase"]}, indent=2))
    except Refusal as exc:
        print(json.dumps({"status": "BLOCKED", "reason": exc.reason, "remediation": exc.remediation}, indent=2))
        raise SystemExit(2)


if __name__ == "__main__":
    main()
