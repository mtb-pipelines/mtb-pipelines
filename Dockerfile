FROM python:3.10-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.0.0

RUN apt update \
    && apt install --no-install-recommends -y \
            g++ \
            gcc \
            python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# System pip dependencies
RUN pip install --upgrade pip \
    && pip install "poetry>=$POETRY_VERSION"

COPY pyproject.toml poetry.lock /src/

WORKDIR /src

COPY mtbpipe ./mtbpipe
COPY README.md .

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi
