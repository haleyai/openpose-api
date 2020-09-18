#!/bin/bash

docker-compose up -d

echo "isort"
docker-compose exec api /bin/sh -c "isort ./**/*.py"

echo "black"
docker-compose exec api black . --exclude env

echo "flake8"
docker-compose exec api flake8 . --exclude ./env

echo "pytest coverage"
docker-compose exec api python3 -m pytest
# docker-compose exec api python3 -m pytest --cov="."
# docker-compose exec api python3 -m pytest --cov="."  --cov-report html


