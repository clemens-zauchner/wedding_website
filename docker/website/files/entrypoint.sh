#!/bin/bash

source common.sh

# file_env "DJANGO_SUPERUSER"
# file_env "DJANGO_SUPERUSER_PASSWORD"
# file_env "DJANGO_SECRET_KEY"
# file_env "POSTGRES_USER"
# file_env "POSTGRES_PASSWORD"

echo "Waiting for db.."
python ${PROJECT_CODE}/manage.py check --database default > /dev/null 2> /dev/null
until [ $? -eq 0 ];
do
    echo "Waiting for db.."
    sleep 1
    python ${PROJECT_CODE}/manage.py check --database default > /dev/null 
done
echo "Connected."


/usr/local/bin/python3 ${PROJECT_CODE}/manage.py migrate

/usr/local/bin/python3 ${PROJECT_CODE}/manage.py createsuperuser --noinput --username "${DJANGO_SUPERUSER}" --email "${DJANGO_SUPERUSER_EMAIL}"

/usr/local/bin/python3 ${PROJECT_CODE}/manage.py collectstatic

# /usr/local/bin/python3 ${PROJECT_CODE}/manage.py runserver

/usr/local/bin/uwsgi --ini "${PROJECT_HOME}/uwsgi.ini"
