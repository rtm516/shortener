#!/bin/sh

export FLASK_APP=project/__init__.py

#python manage.py create_db

exec "${@:-python manage.py run -h 0.0.0.0}"