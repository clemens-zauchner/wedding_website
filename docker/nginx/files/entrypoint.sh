#!/bin/bash

set -eu

# /usr/sbin/service nginx start

# certbot certonly \
#     --nginx \
#     --http-01-port 8080 \
#     --non-interactive \
#     --agree-tos \
#     --email "${EVENTMAN_CERTBOT_EMAIL}" \
#     -d "${EVENTMAN_CERTBOT_DOMAINS}"

# # ls /etc/letsencrypt
# # ls /etc/letsencrypt/live/events.it-ps.at/

# rm /etc/nginx/sites-enabled/01-http.conf

# /usr/sbin/service nginx stop

exec "$@"
