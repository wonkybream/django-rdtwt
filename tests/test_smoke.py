from django.db import connection
from django.test import TestCase


class PostgresDiscoverRunnerSmokeTests(TestCase):
    def test_connection_to_postgres_container(self):
        connection.cursor().execute("SELECT 1")
