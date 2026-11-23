.PHONY: backend-build backend-up backend-down backend-lint backend-typecheck frontend-build frontend-up frontend-down

# ===============================================================
# BACKEND
# ===============================================================
backend-build:
	docker compose -f ./backend/docker-compose.yaml build

backend-up:
	docker compose -f ./backend/docker-compose.yaml up -d

backend-down:
	docker compose -f ./backend/docker-compose.yaml down

backend-shell:
	docker compose -f ./backend/docker-compose.yaml run --rm app bash

backend-format:
	docker compose -f ./backend/docker-compose.yaml run --rm app ruff format src
	docker compose -f ./backend/docker-compose.yaml run --rm app ruff format tests

backend-lint:
	docker compose -f ./backend/docker-compose.yaml run --rm app ruff check src --fix
	docker compose -f ./backend/docker-compose.yaml run --rm app ruff check tests --fix

backend-typecheck:
	docker compose -f ./backend/docker-compose.yaml run --rm app pyrefly check src
	docker compose -f ./backend/docker-compose.yaml run --rm app pyrefly check tests

backend-unittest:
	docker compose -f ./backend/docker-compose.yaml run --rm app python -m unittest discover -s tests -v

backend-check: backend-format backend-lint backend-typecheck

# ===============================================================
# FRONTEND
# ===============================================================
frontend-build:
	docker compose -f ./frontend/docker-compose.yaml build

frontend-up:
	docker compose -f ./frontend/docker-compose.yaml up -d

frontend-down:
	docker compose -f ./frontend/docker-compose.yaml down

