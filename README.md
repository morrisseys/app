# RMY — Multi-Region, Multi-Tenant FastAPI + OpenSearch (Scaffold)

This scaffold includes:
- **controlplane/** (global: regions, tenants, global users — minimal stub)
- **regions/uk/** (first regional stack: app, admin, Postgres, Redis, OpenSearch, Dashboards, Traefik)
- **edge/** Cloudflare Worker stub for region redirects

Key choices:
- **OpenSearch Dashboards is internal-only**, proxied by the app under `/_reporting/*` and embedded via iframe in the Bootstrap UI.
- Traefik terminates TLS (labels are ready, you must set real DNS + ACME email).

## Quick start (locally or on a server with ports 80/443)
1) Copy `regions/uk/.env.example` to `.env` and set values.
2) `docker compose -f regions/uk/docker-compose.yml up -d --build`
3) Point `uk.rmy.app` DNS to the server. Traefik will fetch certs automatically.
4) Visit `https://uk.rmy.app` once DNS/ACME is done.

## Structure
- `regions/uk/app` — FastAPI app (Bootstrap 5), static + templates, includes `/t/{tenant}/reporting` wrapper and `/_reporting/*` reverse proxy
- `regions/uk/dashboards/opensearch_dashboards.yml` — basePath + proxy-auth config
- `regions/uk/traefik/traefik.yml` — ACME (Let's Encrypt) example
- `controlplane/` — minimal API skeleton
- `edge/worker.js` — Cloudflare Worker stub

## Next
- Build out controlplane routing (tenant → region), SSO, tenant registry, owners.
- Flesh out app modules (auth, tenancy middleware, RBAC, entities, recordings).

