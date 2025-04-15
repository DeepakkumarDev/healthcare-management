web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn healthcare.wsgi:application --bind 0.0.0.0:$PORT --log-file -
