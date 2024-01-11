import os
import sys

import django
from django.conf import settings
from django.test.utils import get_runner

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
    django.setup()

    # Smoke tests with actual test runner
    settings.TEST_RUNNER = "rdtwt.runner.PostgresDiscoverRunner"
    postgres_discover_runner = get_runner(settings)
    failures = postgres_discover_runner(verbosity=2).run_tests(["tests.test_smoke"])

    # Tests using standard runner
    settings.TEST_RUNNER = "django.test.runner.DiscoverRunner"
    discover_runner = get_runner(settings=settings)
    failures += discover_runner(verbosity=2).run_tests(
        ["tests.test_postgres_discover_runner"]
    )

    sys.exit(bool(failures))
