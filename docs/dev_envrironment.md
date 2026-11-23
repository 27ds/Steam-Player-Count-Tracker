# dev_environment
The development environment is provided by a Docker Compose stack.

## MySQL-Verbindung
Das Backend verbindet sich mit einer extern betriebenen MySQL-Datenbank. Vor dem Start
des Compose-Stacks müssen diese Umgebungsvariablen gesetzt sein:

- `MYSQL_HOST`
- `MYSQL_PORT` (optional, Standard: `3306`)
- `MYSQL_USER`
- `MYSQL_PASSWORD`
- `MYSQL_DATABASE`

Die Tabelle `tracked_games` wird beim ersten API-Aufruf automatisch angelegt.
Zugangsdaten sollten nicht in Dateien eingecheckt werden.

## API-Endpunkte
- `GET /api/get_game/<game_id>` — gespeicherte Daten eines überwachten Spiels
- `POST /api/add_game` — Spiel hinzufügen; JSON-Body: `{"game_id": 730}`
- `DELETE /api/remove_game/<game_id>` — Spiel aus der Überwachung entfernen
- `GET /api/get_count/<game_id>` — aktuelle Spielerzahl eines überwachten Spiels

Der bisherige `GET /game/<game_id>`-Endpunkt bleibt aus Kompatibilitätsgründen verfügbar.

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
