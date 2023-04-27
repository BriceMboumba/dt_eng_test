FROM mysql:latest
COPY ./db_dteng_schema.sql /docker-entrypoint-initdb.d/