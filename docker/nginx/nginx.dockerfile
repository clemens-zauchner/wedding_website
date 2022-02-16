FROM nginx:1.21

ENV IMAGE_USER="nginx"
ENV PROJECT_HOME="/home/${IMAGE_USER}"
ENV PROJECT_STATIC="${PROJECT_HOME}/static"
ENV PROJECT_TMP="${PROJECT_HOME}/tmp"


RUN mkdir -p "${PROJECT_HOME}" && \
    mkdir -p "${PROJECT_STATIC}" && \
    mkdir -p "${PROJECT_TMP}"

RUN rm /etc/nginx/nginx.conf && \
    rm /etc/nginx/conf.d/default.conf

COPY files/nginx-root.conf /etc/nginx/nginx.conf
COPY files/nginx-site.conf /etc/nginx/sites-enabled/nginx-site.conf

# USER "${IMAGE_USER}"
# RUN chown -R "${IMAGE_USER}":"${IMAGE_USER}"

COPY --chmod=0755 files/entrypoint.sh "/usr/bin/entrypoint.sh"

WORKDIR "${PROJECT_HOME}"
ENTRYPOINT [ "entrypoint.sh" ]
CMD ["nginx", "-g", "daemon off;"]
