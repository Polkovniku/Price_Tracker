FROM mcr.microsoft.com/playwright/python:v1.50.0-jammy

WORKDIR /app

COPY pyproject.toml ./
COPY uv.lock ./
COPY backend/ .
RUN pip install uv && uv sync --frozen && uv run python -m camoufox fetch

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]