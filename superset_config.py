from superset.config import *  # Импорт стандартных настроек
from flask_appbuilder.security.manager import AUTH_LDAP
from dotenv import load_dotenv
import os

# ------------------ Загрузка переменных окружения ------------------
load_dotenv()

# ------------------ Подключение к базе данных ------------------
SQLALCHEMY_DATABASE_URI = (
    f"postgresql+psycopg2://{os.getenv('ENV_SUPERSET_DB_USER')}:"
    f"{os.getenv('ENV_SUPERSET_DB_PASSWORD')}@"
    f"{os.getenv('ENV_PG_HOST')}:{os.getenv('ENV_PG_PORT')}/"
    f"{os.getenv('ENV_SUPERSET_DB_NAME')}"
)

# ------------------ CORS ------------------
ENABLE_CORS = True

# ------------------ Безопасность ------------------
WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None

# ------------------ Таймаут веб-сервера ------------------
SUPERSET_WEBSERVER_TIMEOUT = 60

# ------------------ Языковые настройки ------------------
LANGUAGES = {
    "ru": {"flag": "ru", "name": "Русский"},
    "en": {"flag": "us", "name": "English"},
}
BABEL_DEFAULT_LOCALE = "ru"
BABEL_DEFAULT_TIMEZONE = "Europe/Moscow"

# ------------------ Экспериментальные фичи ------------------
FEATURE_FLAGS = {
    "ALERT_REPORTS": True,
    "DASHBOARD_NATIVE_FILTERS": True,
}
