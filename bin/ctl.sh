#!/bin/bash
set -e 

export BASE_PATH="$(realpath $(dirname $0)/..)"

DJANGO_PATH="${BASE_PATH}/django_wedding_website"
export CONFIG_PATH="${BASE_PATH}/config"
export DJANGO_CONF_FILE="${CONFIG_PATH}/django.conf"
export DB_CONF_FILE="${CONFIG_PATH}/db.conf"

cd "${BASE_PATH}"

if [ $1 = "build" ]
then
    WEBSITE_PATH="${BASE_PATH}/docker/website/files"
    cp "${DJANGO_PATH}/manage.py" "${WEBSITE_PATH}/." 
    cp -r "${DJANGO_PATH}/wedding/" "${WEBSITE_PATH}/." 
    cp -r "${DJANGO_PATH}/wedding_website/" "${WEBSITE_PATH}/." 
    export DOCKER_BUILDKIT=1
    export COMPOSE_DOCKER_CLI_BUILD=1

fi
export COMPOSE_PROJECT_NAME="wedding"
COMPOSE_PATH="${BASE_PATH}/docker-compose"
COMPOSE_FILE="${COMPOSE_PATH}/docker-compose.yml"


docker-compose -f "${COMPOSE_FILE}" "$@"

if [ $1 = "build" ]
then
    rm "${WEBSITE_PATH}/manage.py"
    rm -rf "${WEBSITE_PATH}/wedding"
    rm -rf "${WEBSITE_PATH}/wedding_website"
fi
