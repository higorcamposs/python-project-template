FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY pyproject.toml README.md /app/
RUN pip install -U pip && pip install -e .[dev] || pip install -e .

COPY src/ /app/src/
ENV PYTHONPATH=/app/src

CMD ["python", "-m", "my_project"]
