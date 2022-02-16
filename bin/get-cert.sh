#!/bin/bash
set -e 

BASE_PATH="$(realpath $(dirname $0)/..)"

CERT_PATH="${BASE_PATH}/cert"
CERT_VAR_PATH="${CERT_PATH}/var"
CERT_ETC_PATH="${CERT_PATH}/etc"

mkdir -p "${CERT_VAR_PATH}"
mkdir -p "${CERT_ETC_PATH}"


docker run -it --rm --name certbot \
            -p 80:80 \
            -p 443:443 \
            -v "${CERT_VAR_PATH}:/etc/letsencrypt" \
            -v "${CERT_VAR_PATH}:/var/lib/letsencrypt" \
            certbot/certbot certonly

