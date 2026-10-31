# Steam Player Count Tracker
An application designed to track, store, and visualize player count trends for selected Steam games over time.

---

## 1. Team & Roles
**Team:** Photonware
* **Product Owner:** Delia
* **Scrum Master / Developer:** Thomas
* **Developer:** Mika
* **Developer:** Catherine

---

## 2. Project Idea & Architecture Overview
The objective of this project is to collect and clearly present historical data regarding the player activity and popularity of selected Steam games.

* **Data Source:** [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API) (Fetches current player counts via API endpoints).
* **Logic:** A background process queries current player numbers at regular intervals for a defined selection of games and processes the data.
* **Data Storage:** Received data points are stored in a database alongside a timestamp.
* **Visualization:** A dashboard/frontend visualizes player count trends across various timeframes (e.g., daily, weekly, or monthly views).

---

## 3. Scope (Project Scope v1.0)

### In Scope
* Automated fetching of current player numbers for a predefined list of Steam games (e.g., top 5–10 selected games).
* Storing history of data points (timestamp, game ID, player count) in a database.
* Simple visualization (e.g., line chart) of the player count trend per game.

---

## Project structure

```text
Steam-Player-Count-Tracker/
├── .github/workflows/       # CI/CD pipelines
├── backend/                 # Backend service (Python, pyproject.toml, Dockerfile, etc.)
│   ├── src/
│   ├── pyproject.toml
│   └── Dockerfile
├── frontend/                # Web-based frontend (package.json, Dockerfile, etc.)
│   ├── src/
│   ├── package.json
│   └── Dockerfile
├── .editorconfig            # Coding styles & whitespace standardization for editors
├── config.conf              # Configuration file (e.g., ports, etc.)
├── docker-compose.yml       # Central Docker configuration for orchestration
├── Makefile                 # Shortcut commands for build, run, lint, and typecheck
├── .gitignore
└── README.md
```

