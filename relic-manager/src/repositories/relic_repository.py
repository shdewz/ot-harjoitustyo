from entities.relic import Relic
from db import get_database_connection


class RelicRepository:
    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        relics = []
        cursor = self._connection.cursor()
        cursor.execute("select * from relics;")
        rows = cursor.fetchall()
        for row in rows:
            relics.append(Relic(
                row["id"],
                row["relic_set"],
                row["type"],
                row["level"],
                row["mainstat"],
                list(map(lambda i: (row[f"substat{i+1}"], row[f"substat{i+1}value"]), range(4)))
            ))

        return relics

    def delete_all(self):
        cursor = self._connection.cursor()
        cursor.execute("delete from relics;")
        self._connection.commit()

    def create(self, relic):
        cursor = self._connection.cursor()
        cursor.execute(f"""
            insert into relics (
                relic_set, type, level, mainstat,
                {",".join(map(lambda i: f"substat{i+1}, substat{i+1}value", range(4)))}
            )
            values (
                    '{relic.relic_set}',
                    '{relic.relic_type}',
                    '{relic.level}',
                    '{relic.mainstat}',
                    {",".join(map(lambda i:
                                  f"'{relic.substats[i][0]}', '{relic.substats[i][1]}'",
                    range(4)))}
            )
        """)
        relic.relic_id = cursor.lastrowid
        self._connection.commit()
        return relic

    def delete(self, relic_id):
        cursor = self._connection.cursor()
        cursor.execute(f"delete from relics where id = {relic_id};")
        self._connection.commit()
        return True


relic_repository = RelicRepository(get_database_connection())
