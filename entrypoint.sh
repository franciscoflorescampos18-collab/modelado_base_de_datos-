#!/bin/sh
set -e

echo ">> Esperando a que la base de datos este lista..."

while ! python -c "
import socket
import os

host = os.environ.get('POSTGRES_HOST', 'db')
port = int(os.environ.get('POSTGRES_PORT', 5432))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    s.close()
except Exception:
    exit(1)
"; do
    echo ">> Base de datos no disponible todavia, reintentando en 2s..."
    sleep 2
done

echo ">> Base de datos lista. Aplicando migraciones..."

python manage.py migrate --noinput

echo ">> Arrancando servidor..."

exec "$@"
