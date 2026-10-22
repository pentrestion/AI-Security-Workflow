---
name: recon
phase: discovery
tools: [nmap, whatweb, subfinder, burp-mcp]
writes_to: hypothesis_board
intensity_min: passive
---

# Reconnaissance

## Parameters
`engagement_token`, `target_set` (subset of `scope_hosts`), `depth` (1-3),
`timeout_per_host`, `rate_limit_pps`.

## Procedure
1. Validate `target_set ⊆ scope_hosts`. Refuse on any out-of-scope element and
   name it explicitly.
2. Enumerate: DNS, HTTP fingerprints, TLS metadata, exposed services, banners.
3. For each discovered asset, write one `Asset` record with evidence
   (raw tool output, timestamp, tool version).
4. Do **not** form vulnerability hypotheses in this phase. Discovery only.
5. Flag any asset that resolves to infrastructure outside `scope_hosts`
   (CDN, shared hosting, third-party API) as `OUT_OF_SCOPE_LEAKAGE` and stop
   probing it.

## Output schema
```json
{"assets":[{"host":"","port":0,"service":"","banner":"","evidence":"","in_scope":true}]}
```

Rate discipline

Respect rate_limit_pps absolutely. If a target returns 429/503 or connection
resets cluster, halve the rate and log the throttle event.
