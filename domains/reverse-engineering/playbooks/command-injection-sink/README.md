# Command Injection Sink

This playbook locates OS command execution paths reachable from user-controlled input.

## Goals
- find `system`, `popen`, `execve`, and string builder patterns
- confirm data origin and reachability
- verify in emulator and gather syscall evidence
