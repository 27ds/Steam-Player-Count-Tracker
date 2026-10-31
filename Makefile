.PHONY: build up shell lint format

build:
	docker compose build

up:
	docker compose up -d

up-backend:
	docker compose up -d backend

up-frontend:
	docker compose up -d frontend

down:
	docker compose down

shell:
	docker compose run --rm app bash

lint:
	docker compose run --rm backend ruff check src

format:
	docker compose run --rm backend ruff format src

typecheck:
	docker compose run --rm backend pyrefly check src

check: format lint typecheck
