#!/usr/bin/env python3
"""Legacy hook file retained for compatibility but disabled in repository mode.

This repository is intentionally a plain source repository and does not ship a
Claude Code plugin or agent runtime.
"""

import sys

print("Repository mode: hook enforcement disabled.", file=sys.stderr)
raise SystemExit(0)
