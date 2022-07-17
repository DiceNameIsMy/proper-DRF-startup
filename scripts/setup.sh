#!/usr/bin/env

cp compose/local/.env-sample compose/local/.env
cp compose/prod/.env-sample compose/prod/.env
pipenv install --dev
pipenv run pre-commit install
