# RMY — AdminLTE Scaffold (FastAPI + OpenSearch proxied Dashboards)

This scaffold integrates **AdminLTE** for the UI shell and embeds **OpenSearch Dashboards** via an iframe under the same origin.

## Highlights
- AdminLTE assets pulled during image build into `/static/adminlte`
- FastAPI + Jinja templates using AdminLTE `base.html` layout
- Reporting page `/t/{tenant}/reporting` wraps Dashboards iframe
- Dashboards kept **internal-only** and proxied at `/_reporting/*`

## Quick start
1) `cd regions/uk && cp .env.example .env` (set ACME_EMAIL, passwords)
2) `docker compose up -d --build`
3) Point `uk.rmy.app` DNS to the server and visit https://uk.rmy.app
