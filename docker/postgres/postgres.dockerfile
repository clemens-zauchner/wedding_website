FROM postgres:14

COPY files/init-user-db.sh docker-entrypoint-initdb.d/init-user-db.sh
