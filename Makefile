.PHONY: backend-build backend-up backend-down backend-lint backend-typecheck frontend-build frontend-up frontend-down

# ===============================================================
# BACKEND
# ===============================================================
backend-build:
	docker compose -f ./backend/docker-compose.yaml build

backend-build-dev:
	docker compose -f ./backend/docker-compose.yaml -f ./backend/docker-compose.dev.yaml build

backend-up:
	docker compose -f ./backend/docker-compose.yaml up -d

backend-down:
	docker compose -f ./backend/docker-compose.yaml down

backend-shell:
	docker compose -f ./backend/docker-compose.yaml run --rm app bash

backend-init_default_games:
	docker compose -f ./backend/docker-compose.yaml run --rm app python src/init_db_for_dev.py

backend-format:
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app ruff format src
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app ruff format tests

backend-lint:
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app ruff check src --fix
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app ruff check tests --fix

backend-typecheck:
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app pyrefly check src
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app pyrefly check tests

backend-unittest-steam_client:
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app python -m unittest tests.test_steam_client -v

backend-unittest-db_client:
	docker compose -f ./backend/docker-compose.yaml run --rm --no-deps app python -m unittest tests.test_db_client -v

backend-check: backend-format backend-lint backend-typecheck

backend-unittest: backend-unittest-steam_client backend-unittest-db_client

# ===============================================================
# FRONTEND
# ===============================================================
frontend-build:
	docker compose -f ./frontend/docker-compose.yaml build

frontend-up:
	docker compose -f ./frontend/docker-compose.yaml up -d

frontend-down:
	docker compose -f ./frontend/docker-compose.yaml down

