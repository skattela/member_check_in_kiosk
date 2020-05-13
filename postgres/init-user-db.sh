#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE postgres;
    CREATE USER django_user WITH PASSWORD 'django_user_pw';
    GRANT ALL PRIVILEGES ON DATABASE django_db TO django_user;
EOSQL