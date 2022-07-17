FROM python:3.10.4-alpine as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apk update

# copy requirements
COPY Pipfile.lock ./

# install dependencies as wheels
RUN pip install --no-cache --upgrade pip pipenv && \
    pipenv requirements > requirements.txt && \
    pip uninstall pipenv -y && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

######

FROM python:3.10.4-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1
ENV APP_HOME=/app

WORKDIR ${APP_HOME}

# Copy wheels and requirements
COPY --from=builder /app/wheels /wheels

# install dependencies
RUN pip install --no-cache /wheels/*

COPY src/ ${APP_HOME}/src

# create user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    # give user permissions to run the application
    chown -R appuser:appgroup $APP_HOME

# change to the app user
USER appuser
