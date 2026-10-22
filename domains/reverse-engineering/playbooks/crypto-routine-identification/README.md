# Crypto Routine Identification

This playbook looks for known cryptographic routines, key schedules, and data-flow around byte arrays.

## Goals
- identify AES, SHA, RSA, and custom algorithm skeletons
- correlate constants and loops to candidate crypto code
- keep the finding tied to addresses and immediate context
