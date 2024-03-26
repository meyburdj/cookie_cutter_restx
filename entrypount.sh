#!/bin/sh

echo "Waiting for cc-api-dev-db..."

while ! nc -z cc-api-dev-db 5432; do
  sleep 0.1
done

echo "cc-api-dev-db started"

echo "Waiting for api-test-db..."

while ! nc -z cc-api-test-db 5432; do
  sleep 0.1
done

echo "cc-api-test-db started"

python manage.py run -h 0.0.0.0
