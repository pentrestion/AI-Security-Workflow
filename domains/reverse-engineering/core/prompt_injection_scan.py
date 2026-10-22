"""Prompt injection scanning for reverse engineering targets.

This catches strings that instruct the model to ignore prior constraints or claim
permissions it does not have. It is a guardrail, not a bypass mechanism.
"""

from __future__ import annotations

import re
from pathlib import Path

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"you are now",
    r"system:",
    r"developer:",
    r"override",
    r"act as",
    r"jailbreak",
    r"do not refuse",
]


class PromptInjectionScan:
    def __init__(self) -> None:
        self.flagged = []

    def scan_strings(self, strings_path: str | Path) -> list[str]:
        text = Path(strings_path).read_text(encoding="utf-8", errors="ignore")
        flagged: list[str] = []
        for line in text.splitlines():
            if any(re.search(pattern, line, flags=re.IGNORECASE) for pattern in INJECTION_PATTERNS):
                flagged.append(line)
        self.flagged = flagged
        return flagged
