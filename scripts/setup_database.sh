#!/bin/bash
rm tmp/db.sqlite3
.venv/bin/python manage.py makemigrations
.venv/bin/python manage.py migrate
export DJANGO_SUPERUSER_EMAIL=your@email.com
export DJANGO_SUPERUSER_PASSWORD=pwd
.venv/bin/python manage.py createsuperuser --name admin --no-input