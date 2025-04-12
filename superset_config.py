from superset.config import *  # Импорт стандартных настроек
from flask_appbuilder.security.manager import AUTH_LDAP
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из файла .env
load_dotenv()

# Настройки подключения к базе данных
SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{os.getenv('ENV_SUPERSET_DB_USER')}:{os.getenv('ENV_SUPERSET_DB_PASSWORD')}@{os.getenv('ENV_PG_HOST')}:{os.getenv('ENV_PG_PORT')}/{os.getenv('ENV_SUPERSET_DB_NAME')}"


# Тайм-аут сессии
SUPERSET_WEBSERVER_TIMEOUT = 60

# Настройки CORS
ENABLE_CORS = True

# Включение экспериментальных функций
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
}