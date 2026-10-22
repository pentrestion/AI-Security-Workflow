"""Hash-pinning and validation for reverse-engineering targets.

This guarantees that the exact file being analyzed is the same one under test.
"""

from __future__ import annotations

import hashlib
from pathlib import Path


class BinaryHasher:
    def __init__(self) -> None:
        self.pinned = {}

    def sha256(self, path: str) -> str:
        digest = hashlib.sha256()
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        return digest.hexdigest()

    def verify(self, path: str, expected: str) -> bool:
        return self.sha256(path) == expected.lower()

    def pin(self, path: str) -> dict:
        digest = self.sha256(path)
        self.pinned[path] = digest
        return {"path": path, "sha256": digest}
