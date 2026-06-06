# ECOSYSTEM_HANDOVER.md

> Read this first. Every time. No exceptions.

Last updated: June 2026

---

## Who this is for

Any human contributor, AI agent, or outside helper entering the HyperFocus Zone ecosystem.

---

## What this ecosystem is

HyperFocus Zone is a neurodivergent-first autonomous AI infrastructure platform.

It includes:
- Core backend infrastructure and agent swarm (HyperCode-V2.4)
- A learning and course platform (Hyper-Vibe-Coding-Course)
- A reusable agent SDK (HyperAgent-SDK)
- A public showcase and demos (showcase-web)
- A second brain and knowledge ops system (BROski-Obsidian-Brain-for-HyperFocus-z0ne)
- A creative Web3 + AI product (BROskiPets-LLM-dNFT)

---

## Current status

| Area | Status |
|---|---|
| Core infrastructure | 🟢 Healthy — 41 containers, 55 agents running |
| Observability stack | 🟢 Grafana, Prometheus, Loki, Tempo all up |
| Course platform | 🟡 Live — Stripe revenue loop needs smoke test |
| Agent SDK | 🟢 Published to npm |
| showcase-web | 🟡 Live — 60-second demo section pending |
| BROskiPets | 🟡 Building |

---

## How to work here safely

1. Pick **one repo** — never work across multiple repos in one session
2. Read the repo-level `AGENT-START.md` before starting
3. Check `WHATS_DONE.md` — never suggest or rebuild what's already done
4. Check `CLAUDE.md` where it exists
5. Prove changes before committing — lint → test → build → THEN commit
6. Never touch `.env` files or commit secrets
7. Document what you did at the end of a session

---

## Sacred rules (never break)

- `docker-ce-cli` — NEVER `docker.io` for socket agents
- `from app.X import Y` — NEVER `from backend.app.X`
- `.env` files — NEVER committed to git
- Stripe webhook — rate-limit EXEMPT, always
- Python indent — 4 spaces, NEVER 3, NEVER mixed
- Redis DB 1 = cache, DB 2 = rate limits — NEVER mix
- `npm run dev:frontend` — NOT `npm run dev`
- Bot entrypoint — `python -u -m cogs.bot` — NEVER `python main.py`

---

## Key contacts

- Builder: [@welshDog](https://github.com/welshDog) — Lyndz Williams, Llanelli, South Wales 🏴󠁧󠁢󠁷󠁬󠁳󠁥
- Mission: Neurodivergent-first autonomous AI infrastructure for the world

---

## Mission

> Stop apologising for your brain. Start building.
