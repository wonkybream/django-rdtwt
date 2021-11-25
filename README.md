# django-rdtwt

[![Static analysis](https://github.com/wonkybream/django-rdtwt/actions/workflows/static-analysis.yml/badge.svg?branch=main)](https://github.com/wonkybream/django-rdtwt/actions/workflows/static-analysis.yml)
[![Tests](https://github.com/wonkybream/django-rdtwt/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/wonkybream/django-rdtwt/actions/workflows/tests.yml)

*(Run Django Tests With Testcontainers)*

This targets users who wish to forget setting up a database for tests. There's no manually starting up *Docker compose* or local database with this.

**Note:**

See: [Altering settings at runtime: Django documentation](https://docs.djangoproject.com/en/3.2/topics/settings/#altering-settings-at-runtime)

This test runner changes default database host and port dynamically, because it's quite hard to know database host before-hand in dynamic environments, for example some CI/CD runners.

Still this just works and is quite simple, that's why I haven't spent that much time investigating alternative solutions. 

## Installation

1. Add rdtwt to your INSTALLED_APPS setting like this
    ```python
    INSTALLED_APPS = [
        ...
        'rdtwt',
    ]
    ```

2. Run tests with rdtwt runner,
    ```shell
    python manage.py test --testrunner=rdtwt.runner.PostgresDiscoverRunner
    ```

Though what I really suggest is to put following in your test settings.

```python
# RDTWT SETTINGS
RDTWT_POSTGRESQL_IMAGE = 'postgres:14.1'
TEST_RUNNER = 'rdtwt.runner.PostgresDiscoverRunner'
```

This makes sure that tests run against the PostgreSQL version defined by you. It also adds up to the test confidence, at least they aren't flaky because of database version changing without your knowledge.

**Example:**

Defining all available options.

```python
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# RDTWT SETTINGS
RDTWT_POSTGRESQL_IMAGE = 'postgres:14.1'
TEST_RUNNER = 'rdtwt.runner.PostgresDiscoverRunner'
RDTWT_POSTGRESQL_USER = 'postgres'
RDTWT_POSTGRESQL_PASSWORD = 'postgres'
RDTWT_POSTGRESQL_NAME = 'postgres'
```
