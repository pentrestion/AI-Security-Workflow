"""JADX bridge for Android APK decompilation."""

from __future__ import annotations


class JADXBridge:
    def __init__(self) -> None:
        self.apk = None

    def load(self, apk_path: str) -> None:
        self.apk = apk_path
