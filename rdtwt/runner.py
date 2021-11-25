from django.conf import settings
from django.test.runner import DiscoverRunner
from testcontainers.postgres import PostgresContainer


class PostgresDiscoverRunner(DiscoverRunner):

    _postgres_container: PostgresContainer

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        postgresql_image = getattr(settings, 'RDTWT_POSTGRESQL_IMAGE', 'postgres:latest')
        postgresql_user = getattr(settings, 'RDTWT_POSTGRESQL_USER', None)
        postgresql_password = getattr(settings, 'RDTWT_POSTGRESQL_PASSWORD', None)
        postgresql_name = getattr(settings, 'RDTWT_POSTGRESQL_NAME', None)

        self._postgres_container = PostgresContainer(
            image=postgresql_image,
            user=postgresql_user,
            password=postgresql_password,
            dbname=postgresql_name
        )

    def _setup_container(self):
        self._postgres_container.start()
        settings.DATABASES['default']['HOST'] = self._postgres_container.get_container_host_ip()
        settings.DATABASES['default']['PORT'] = self._postgres_container.get_exposed_port(5432)

    def _teardown_container(self):
        self._postgres_container.stop()

    def setup_databases(self, **kwargs):
        self._setup_container()
        return super().setup_databases(**kwargs)

    def teardown_databases(self, old_config, **kwargs):
        super().teardown_databases(old_config, **kwargs)
        self._teardown_container()
