# Hardened Container Image Pipeline

A security-hardened container release pipeline built around a minimal Python
service: multi-stage/non-root/distroless image, Trivy-gated CI, multi-arch
builds with SBOM + cosign signing + build provenance published to GHCR, a
scheduled rebuild with an automatic CVE-issue bot, a Bash + Go compliance
suite checked against the CIS Docker Benchmark, and GitOps deployment to a
local kind cluster via Argo CD with PR-based image promotion.

## Service

A minimal FastAPI app (`app/main.py`) exposing:

- `GET /health` — liveness check
- `GET /version` — current build version

Run locally:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Status

This project is built incrementally, stage by stage. Sections below will be
filled in as each stage lands.

- [x] Minimal FastAPI service
- [ ] Multi-stage, non-root, distroless Dockerfile
- [ ] Bash compliance suite
- [ ] CI: build + Trivy scan gate
- [ ] Multi-arch build, SBOM, cosign signing, build provenance, GHCR publish
- [ ] Go policy checker
- [ ] Scheduled rebuild + CVE issue bot
- [ ] kind + Argo CD GitOps deployment with PR-based promotion
- [ ] CIS Docker Benchmark + OCI manifest write-ups
