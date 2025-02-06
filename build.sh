#!/usr/bin/env bash

set -o errexit

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar collectstatic
python manage.py collectstatic --noinput
python manage.py migrate

ls -l $BASE_DIR/staticfiles || echo "No se encuentra la carpeta staticfiles"

# Crear la carpeta media si no existe
mkdir -p media/empresas
chmod 777 media

# Crear superusuario con variables de entorno
echo "from django.contrib.auth import get_user_model
import os
User = get_user_model()
username = os.getenv('DJANGO_SUPERUSER_USERNAME')
email = os.getenv('DJANGO_SUPERUSER_EMAIL')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print('Superusuario creado con éxito')
else:
    print('El superusuario ya existe')" | python manage.py shell
