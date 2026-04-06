dev:
    uv run uvicorn iiza.main:api --reload --app-dir src

test:
    uv run pytest --cov -s
