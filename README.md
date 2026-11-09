# Steam Player Count Tracker
An application designed to track, store, and visualize player count trends for selected Steam games over time.

---
- [Steam Player Count Tracker](#steam-player-count-tracker)
  - [1. Team \& Roles](#1-team--roles)
  - [2. Project Idea \& Architecture Overview](#2-project-idea--architecture-overview)
  - [3. Scope (Project Scope v1.0)](#3-scope-project-scope-v10)
    - [In Scope](#in-scope)
  - [4. Development Process and Community Rules](#4-development-process-and-community-rules)
  - [5. Project structure](#5-project-structure)




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

## 4. Development Process and Community Rules
- **Code review:** Every pull request needs at least one approving review before it is merged into `main`.
- **Branching:** Each issue is worked on in its own branch, named after the issue.
- **Issue planning:** Every issue has a **priority** (3 - high / 2 - medium / 1 - low) and an estimated **size** (XS / S / M / L / XL).
- **Definition of Done:** Before an issue can be set to **Ready**, it needs a Definition of Done (DoD): a short checklist of what must be true for the issue to count as finished.

## 5. Project structure

```text
Steam-Player-Count-Tracker/
├── .github/workflows/       # CI/CD pipelines
│   └── ci.yml               # runs lint, typecheck and build on every push / pull request
├── backend/                 # Backend service (Python, pyproject.toml, Dockerfile, etc.)
│   ├── src/                 # Application source code
│   ├── Dockerfile
│   ├── Makefile             # Shortcut commands for build, run, lint, and typecheck
│   ├── docker-compose.yaml  # Central Docker configuration for orchestration
│   └── pyproject.toml       # Python dependencies and tool settings
├── docs/
│   ├── architecture.md      # System overview: components and how they interact
│   ├── dev_environment.md   # How to set up and run the project locally
│   └── retro.md             # Sprint retrospectives: what went well, what to improve
├── frontend/                # Web-based frontend (package.json, Dockerfile, etc.)
│   ├── src/                 # Frontend source code
│   ├── Dockerfile
│   ├── Makefile             # Shortcut commands for build, run, lint, and typecheck
│   └── docker-compose.yaml  # Docker configuration for the frontend service
├── .dockerignore
├── .editorconfig            # Coding styles & whitespace standardization for editors
├── .env.example             # Template for environment variables; copy to .env (never commit .env)
├── .gitignore
├── README.md                # Project overview, quick start and links to docs
├── config.conf              # Configuration file (e.g., ports, etc.)
└── version
```

