FROM python:3.14-slim AS base
WORKDIR /app

# Linter / Typecheck (for CI/CD)
FROM base AS ci
RUN pip install --no-cache-dir ".[dev]"
COPY . .

# Runtime App
FROM base AS runtime
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
RUN pip install --no-cache-dir .
COPY . .

# Dev build
FROM runtime AS dev
RUN pip install --no-cache-dir -e ".[dev]"
