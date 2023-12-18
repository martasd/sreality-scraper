FROM python:3.9-slim as builder

RUN pip install poetry==1.3.2

ENV POETRY_VIRTUALENVS_CREATE=1
ENV POETRY_VIRTUALENVS_IN_PROJECT=1
ENV POETRY_NO_INTERACTION=1
ENV POETRY_CACHE_DIR=/tmp/poetry_cache

COPY pyproject.toml poetry.lock ./

RUN --mount=type=cache,target=$POETRY_CACHE_DIR poetry install --without dev --no-root

# ====================================================================================

FROM builder as runner

ENV VIRTUAL_ENV=/.venv
ENV PATH="/.venv/bin:$PATH"

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY app.py app.py
COPY entrypoint.sh entrypoint.sh
COPY migrations migrations
COPY templates templates

RUN chmod u+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
