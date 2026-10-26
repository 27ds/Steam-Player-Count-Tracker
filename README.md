# Steam Player Count Tracker
An application designed to track, store, and visualize player count trends for selected Steam games over time.

---

## 1. Team & Roles
**Team:** Photonware
* **Product Owner:** Delia
* **Developer:** Mika
* **Developer:** Catherine
* **Developer:** Thomas

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
steam_player_count_tracker/
├── .github/workflows/ci.yml            # CI/CD Pipeline   
├── docs/
│   ├── architecture.md                 # C4, static and dynamic diagrams
│   └── retro.md                        # sprint retrospectives
├── src/steam_player_count_tracker/
│   ├── source/                         # 1. data source (API / sensor)
│   ├── logic/                          # 2. logic
│   ├── storage/                        # 3. storage interface + database
│   ├── output/                         # 4. export / chart
│   ├── config.py                       # 5. reads config file and .env
│   └── main.py
├── tests/                              # pytest tests
├── config.ini                          # configuration (no secrets)
├── .env.example                        # names of the secrets, fake values
├── Dockerfile
├── docker-compose.yaml
├── requirements.txt
└── requirements-dev.txt
```

