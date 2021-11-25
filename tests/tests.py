from unittest.mock import patch, Mock

from django.test import SimpleTestCase

from rdtwt.runner import PostgresDiscoverRunner


class SettingsStub:
    DATABASES = {
        'default': {
            'HOST': '127.0.0.1'
        }
    }

    def get_host_ip(self):
        return self.DATABASES['default']['HOST']


class PostgresDiscoverRunnerUnitTests(SimpleTestCase):

    @patch('rdtwt.runner.settings', SettingsStub())
    def test_setup_container_set_host_ip_as_database_host(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock
        container_mock.get_container_host_ip.return_value = 'container-host-ip'

        postgres_runner._setup_container()

        container_mock.start.assert_called()
        self.assertEqual(SettingsStub().get_host_ip(), 'container-host-ip')

    def test_teardown_container_stops_postgres_container(self):
        container_mock = Mock()
        postgres_runner = PostgresDiscoverRunner()
        postgres_runner._postgres_container = container_mock

        postgres_runner._teardown_container()

        container_mock.stop.assert_called()
