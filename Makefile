.PHONY: up-uk logs-uk down-uk cp-up cp-down
up-uk:
	cd regions/uk && cp -n .env.example .env || true && docker compose up -d --build
logs-uk:
	cd regions/uk && docker compose logs -f --tail=200
down-uk:
	cd regions/uk && docker compose down
cp-up:
	cd controlplane && cp -n .env.example .env || true && docker compose up -d --build
cp-down:
	cd controlplane && docker compose down
