# Anti-Analysis Detection

This playbook finds techniques designed to hinder reverse engineering and automated analysis.

## Goals
- detect `ptrace`, `int3`, `ud2`, timing loops, TLS callbacks, and loader tricks
- reduce false positives by checking the instruction stream and cross-references
