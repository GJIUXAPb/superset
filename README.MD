```YAML
version: '3.3'
services:
  superset:
    image: gjiuxapb/superset
    container_name: superset
    restart: always
    environment:
      SUPERSET_ENV: production
      SUPERSET_LOAD_EXAMPLES: "no"
      SUPERSET_SECRET_KEY: ${ENV_SUPERSET_SECRET_KEY}
      ENV_SUPERSET_DB_USER: superset
      ENV_SUPERSET_DB_PASSWORD: ${ENV_SUPERSET_DB_PASSWORD}
      ENV_SUPERSET_DB_NAME: superset
      ENV_PG_HOST: postgres
      ENV_PG_PORT: 5432
      TZ: Europe/Moscow
```