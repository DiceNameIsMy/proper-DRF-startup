FROM python:3.10.2-slim

# install initial dependencies
RUN apt-get update && \
    apt-get -y install libpq-dev gcc gdal-bin &&  \
    pip install --no-cache --upgrade pip pipenv

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1
ENV APP_HOME=/app/

WORKDIR ${APP_HOME}

# install dependencies
COPY Pipfile Pipfile.lock ${APP_HOME}
RUN pipenv install

# project source is included via volume
