# Authentication Bypass Location

This playbook is used to identify logic that bypasses checks or deserializes untrusted input.

## Goals
- trace auth validation routines
- compare expected and observed control-flow
- validate behavioral mismatch in emulator before reporting
