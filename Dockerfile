# Базовый образ Superset
FROM apache/superset:4.1.2

# Устанавливаем зависимости для PostgreSQL
USER root

RUN apt update && apt upgrade -y && apt install -y --no-install-recommends \
    libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade --no-cache-dir pip

RUN pip install --no-cache-dir psycopg2-binary flask-cors flask-ldap3-login apache-superset python-ldap gunicorn

COPY superset_config.py /app/pythonpath/

# Устанавливаем пользователя обратно на non-root для безопасности
USER superset

#Для Development
#CMD ["/bin/sh", "-c", "superset db upgrade && superset init && superset run -p 8088 -h 0.0.0.0"]

#Для PROD
CMD ["/bin/sh", "-c", "superset db upgrade && superset init && gunicorn --bind 0.0.0.0:8088 --workers 3 --timeout 120 'superset.app:create_app()'"]