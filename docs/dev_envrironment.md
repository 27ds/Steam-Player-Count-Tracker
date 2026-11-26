# dev_environment
The development environment is provided by a Docker Compose stack.

## MySQL-Verbindung
The backend connects to a PostgreSQL database.

The tracked_games table is created automatically on the first API request.
Database credentials must not be committed to the repository.

## API-Endpoint
- `GET /api/get_game/<game_id>` — Returns stored information about a tracked game.
- `POST /api/add_game` — Adds a game to tracking.
- `DELETE /api/remove_game/<game_id>` — Removes a game from tracking.
- `GET /api/get_count/<game_id>` — Returns the current player count


## Linter und Formatter
- Pyrefly
- Ruff

## Docs
- Markdown
- Mermaid

## Git Branch Convention
- feat/
- doc/
- fix/
- test/
- build/
- enh/

## Naming Convention
- Snake Case

