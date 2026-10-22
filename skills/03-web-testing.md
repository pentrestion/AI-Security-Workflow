---
name: web-testing
phase: attack
tools: [burp-mcp, caido-mcp, ffuf, sqlmap]
playbooks: [sqli, xss, ssrf, idor, request_smuggling, authz]
requires_verification: true
---

# Web Application Testing

## Parameters
`engagement_token`, `base_url`, `auth_context` (`none`|`cookie`|`bearer`),
`credential_ref` (vault path, never inline), `classes` (list of playbooks),
`max_requests_per_endpoint`.

## Procedure per class
1. Load only the playbook(s) named in `classes`.
2. Map endpoints reachable under `auth_context`.
3. Generate candidate payloads from the playbook's mutation grammar.
4. **For each candidate, state the falsifiable prediction first:**
   > "If this endpoint concatenates `id` into SQL, then `id=1'` will produce a
   > distinct error or timing delta > 500ms vs `id=1`."
5. Execute, record the observation, and mark `CONFIRMED` / `REFUTED` / `INCONCLUSIVE`.
6. Only `CONFIRMED` findings advance to verification.

## Hard constraints
- No destructive verbs (`DELETE`, `DROP`, `TRUNCATE`, `UPDATE` without `WHERE`)
  unless `playbook.destructive == true` **and** intensity allows it.
- No credential stuffing against real user accounts.
- Stop a class after `max_requests_per_endpoint` without a signal.

## Anti-hallucination
Every `CONFIRMED` finding must cite a request/response pair from the traffic log
by hash. A finding without a hash is auto-downgraded to `INCONCLUSIVE`.
