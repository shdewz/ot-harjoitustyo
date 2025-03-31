from entities.relic import Relic
from db import get_database_connection


class RelicRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()
        cursor.execute("select * from relics;")
        rows = cursor.fetchall()

        return list(rows)

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from relics;")
        self._connection.commit()


relic_repository = RelicRepository(get_database_connection())