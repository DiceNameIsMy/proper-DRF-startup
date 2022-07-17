#!/usr/bin/env

docker build --target builder . -f compose/prod/Dockerfile --cache-from proper-drf-startup-builder:latest --tag proper-drf-startup-builder:latest
docker build . -f compose/prod/Dockerfile --cache-from proper-drf-startup-builder:latest --cache-from proper-drf-startup:latest --tag proper-drf-startup:latest
