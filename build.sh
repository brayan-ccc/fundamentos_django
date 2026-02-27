#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate

# Crear superuser automáticamente
echo "from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@email.com', 'admin1234')
    print('Superuser creado')
else:
    print('Superuser ya existe')
" | python manage.py shell