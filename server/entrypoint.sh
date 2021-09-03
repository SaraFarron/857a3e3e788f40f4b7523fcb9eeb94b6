#!/bin/sh

celery -A server worker -l info -pool=solo

exec "$@"