.PHONY: build up shell lint format

build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

shell:
	docker compose run --rm app bash

lint:
	docker compose run --rm app ruff check src

format:
	docker compose run --rm app ruff format src

typecheck:
	docker compose run --rm app pyrefly check src
