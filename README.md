# Steam Player Count Tracker

A Python app for tracking Steam game player counts.

## Project structure

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


