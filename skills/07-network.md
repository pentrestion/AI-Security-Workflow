---
name: network-testing
phase: attack
tools: [nmap, nikto, enum4linux, nuclei]
intensity_min: active
---

# Network Service Testing

## Parameters
`engagement_token`, `cidr_list`, `port_profile`, `credential_list_ref`,
`max_concurrent`, `destructive` (default false).

## Procedure
1. Validate `cidr_list ⊆ scope_hosts`.
2. Service scan with `port_profile`. Correlate versions against OSV/NVD.
3. For each service: check default credentials **only from `credential_list_ref`**
   (an approved list, not a wordlist attack on production).
4. Run `nuclei` with tags matching discovered technologies; exclude tags marked
   destructive unless explicitly enabled.
5. Flag misconfigurations: anonymous FTP/SMB, open resolvers, unauthenticated
   Redis/Mongo/Elastic, exposed `.git`, TLS 1.0/1.1, expired certs.
6. Each finding must cite the exact probe command and raw response.

## Hard constraints
- No DoS-class probes (`--script dos`, flood modes) under any circumstance.
- No password spraying against production auth endpoints.
- `max_concurrent` is a ceiling, not a target.
