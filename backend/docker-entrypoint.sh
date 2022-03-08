#!/bin/sh

echo "Waiting for postgres..."

until pg_isready -h ${POSTGRES_HOST:-db} -p ${POSTGRES_PORT:-5432}; do
    echo "Awaiting Database container on  ${POSTGRES_HOST:-db}:${POSTGRES_PORT:-5432}"
    sleep 1
done

echo "PostgreSQL started"

# PGPASSWORD=djangoproject psql --host db --port 5432 --username=code.djangoproject --dbname=code.djangoproject < tracdb/trac.sql
python manage.py migrate
# python manage.py collectstatic --no-input --clear
python manage.py loaddata ./commons/fixtures/*.xml

echo "************** Create backend superuser ******************"

script="
from django.contrib.auth import get_user_model

username = '$SU_USERNAME';
password = '$SU_PWD';
email = '$SU_EMAIL';

User = get_user_model()

if User.objects.filter(is_superuser=True).count()==0:
    superuser=User.objects.create_user(username, email, password);
    superuser.is_superuser=True;
    superuser.is_staff=True;
    superuser.save();
    print('Superuser',username,'created.');
else:
    print('One or more Superuser already exists, creation skipped.')
"

printf "$script" | python manage.py shell

if [ "$DEBUG" = "True" ]; then
    python -m manage runserver 0.0.0.0:8000
else
    gunicorn -b 0.0.0.0:8000 config.wsgi
fi
