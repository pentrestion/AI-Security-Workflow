# AI-Security-Workflow
An AI-assisted, multi-domain security testing framework for authorized research.

## What This Is
A modular workflow that turns LLMs (ChatGPT, Claude, Gemini, DeepSeek, Grok)
into structured security testers using the four-phase loop:
Scoping → Discovery → Hypothesis/Verification → Reporting.

## Quick Start
1. Clone the repo and configure `.env`.
2. Install requirements: `pip install -r requirements.txt`
3. Run `python core/orchestrator.py init --domain web --name my-target`
4. Fill in the engagement scope and authorization files.
5. Run `discover`, `hypothesis_engine`, `verifier`, and `report`.

## Modules
- `domains/web/` — SQLi, XSS, SSRF, request smuggling (Burp MCP)
- `domains/iot/` — firmware extraction, protocol fuzzing (Ghidra MCP)
- `domains/supply-chain/` — dependency confusion, typosquatting (OSV + AST)
- `domains/network/` — misconfigurations, default creds (Nmap MCP)
- `library-testing/` — component-level source analysis (`/http`, `/socket`, `/crypto`)

## CVE Case Studies
See `cve-reference/` for chained exploit walkthroughs with AI notes.

## Safety
All verification is sandboxed. Refute-first validation suppresses unconfirmed findings.
Authorized testing only.

## Repository Layout
```text
AI-Security-Workflow/
├── README.md
├── LICENSE
├── .env.example
├── requirements.txt
├── core/
├── domains/
├── library-testing/
├── cve-reference/
├── tools/
├── reports/
└── .github/
```

## License
MIT
