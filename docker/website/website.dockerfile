FROM python:3.8-alpine


ENV IMAGE_USER="wedding"
ENV PROJECT_HOME="/home/${IMAGE_USER}"
ENV PROJECT_CODE="${PROJECT_HOME}/code"
ENV PROJECT_TMP="${PROJECT_HOME}/tmp"
ENV PROJECT_STATIC="${PROJECT_HOME}/static"


RUN mkdir -p "${PROJECT_HOME}" && \
    mkdir -p "${PROJECT_CODE}" && \
    mkdir -p "${PROJECT_TMP}" && \
    mkdir -p "${PROJECT_STATIC}"

COPY files/requirements.txt "${PROJECT_TMP}/requirements.txt"
RUN apk add --update --no-cache build-base linux-headers bash && \
    pip3 install --no-cache-dir -r "${PROJECT_TMP}/requirements.txt" && \
    apk del build-base linux-headers

COPY files/wedding "${PROJECT_CODE}/wedding"
COPY files/wedding_website "${PROJECT_CODE}/wedding_website"
COPY files/manage.py "${PROJECT_CODE}/manage.py"
COPY files/uwsgi.ini "${PROJECT_HOME}/uwsgi.ini"

WORKDIR "${PROJECT_HOME}"
COPY --chmod=0755 files/common.sh "/usr/bin/common.sh"
COPY --chmod=0755 files/entrypoint.sh "/usr/bin/entrypoint.sh"

ENTRYPOINT [ "entrypoint.sh" ]

