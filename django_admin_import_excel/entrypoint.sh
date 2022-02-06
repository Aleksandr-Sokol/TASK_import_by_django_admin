#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py initadmin
python manage.py collectstatic
exec gunicorn django_admin_import_excel.wsgi:application --bind 0.0.0.0:8000 --reload