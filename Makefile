.PHONY: up-uk logs-uk down-uk
up-uk:
	cd regions/uk && cp -n .env.example .env || true && docker compose up -d --build
logs-uk:
	cd regions/uk && docker compose logs -f --tail=200
down-uk:
	cd regions/uk && docker compose down
