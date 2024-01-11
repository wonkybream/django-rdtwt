import os
from unittest import TestCase
from unittest.mock import Mock

import django
from django.conf import settings

from rdtwt.runner import PostgresDiscoverRunner


class PostgresDiscoverRunnerTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
        django.setup()

    def test_setup_container_overwrites_hosts_and_ports_for_all_databases(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock
        container_mock.get_container_host_ip.return_value = "127.0.0.2"
        container_mock.get_exposed_port.return_value = "5433"

        postgres_runner._setup_container()

        container_mock.start.assert_called()
        self.assertEqual(settings.DATABASES["default"]["HOST"], "127.0.0.2")
        self.assertEqual(settings.DATABASES["other"]["HOST"], "127.0.0.2")
        self.assertEqual(settings.DATABASES["default"]["PORT"], "5433")
        self.assertEqual(settings.DATABASES["other"]["PORT"], "5433")

    def test_teardown_container_stops_postgres_container(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock

        postgres_runner._teardown_container()

        container_mock.stop.assert_called()
