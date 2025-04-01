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

    def create(self, relic):
        cursor = self._connection.cursor()
        print(relic)
        cursor.execute(f"""
            insert into relics (relic_set, type, level, mainstat, substat1, substat1value)
            values ('{relic.relic_set}', '{relic.relic_type}', '{relic.level}', '{relic.mainstat}', '{relic.substats[0][0]}', '{relic.substats[0][1]}')
        """)
        self._connection.commit()
        return relic


relic_repository = RelicRepository(get_database_connection())