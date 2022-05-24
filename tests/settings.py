SECRET_KEY = "insecure-key"

INSTALLED_APPS = ["rdtwt", "tests"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

TEST_RUNNER = "rdtwt.runner.PostgresDiscoverRunner"

RDTWT_POSTGRESQL_IMAGE = "postgres:14"
RDTWT_POSTGRESQL_USER = "postgres"
RDTWT_POSTGRESQL_PASSWORD = "postgres"
RDTWT_POSTGRESQL_NAME = "postgres"
