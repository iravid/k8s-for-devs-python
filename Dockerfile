FROM python:3.8-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100

RUN pip install poetry==1.0.10
RUN mkdir /app

WORKDIR /app
ADD pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

ADD . /app

EXPOSE 8080
ENTRYPOINT ["gunicorn", "--config", "gunicorn.py", "kubernetes_workshop.app:app"]
