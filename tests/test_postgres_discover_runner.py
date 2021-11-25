from unittest import TestCase
from unittest.mock import patch, Mock

from rdtwt.runner import PostgresDiscoverRunner


class SettingsStub:
    DATABASES = {
        'default': {
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }

    RDTWT_POSTGRESQL_IMAGE = 'postgres:latest'

    def get_host_ip(self):
        return self.DATABASES['default']['HOST']

    def get_bind_port(self):
        return self.DATABASES['default']['PORT']


class PostgresDiscoverRunnerTests(TestCase):

    @patch('rdtwt.runner.settings', SettingsStub())
    def test_setup_container_overwrites_default_database_host(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock
        container_mock.get_container_host_ip.return_value = 'container-ip'

        postgres_runner._setup_container()

        container_mock.start.assert_called()
        self.assertEqual(SettingsStub().get_host_ip(), 'container-ip')

    @patch('rdtwt.runner.settings', SettingsStub())
    def test_setup_container_overwrites_default_database_port(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock
        container_mock.get_exposed_port.return_value = 'bind-port'

        postgres_runner._setup_container()

        container_mock.start.assert_called()
        self.assertEqual(SettingsStub().get_bind_port(), 'bind-port')

    @patch('rdtwt.runner.settings', SettingsStub())
    def test_teardown_container_stops_postgres_container(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock

        postgres_runner._teardown_container()

        container_mock.stop.assert_called()
