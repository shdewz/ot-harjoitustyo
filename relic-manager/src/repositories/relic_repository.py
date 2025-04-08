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
            insert into relics (relic_set, type, level, mainstat,
                                substat1, substat1value,
                                substat2, substat2value,
                                substat3, substat3value,
                                substat4, substat4value
            )
            values (
                    '{relic.relic_set}',
                    '{relic.relic_type}',
                    '{relic.level}',
                    '{relic.mainstat}',
                    '{relic.substats[0][0]}',
                    '{relic.substats[0][1]}',
                    '{relic.substats[1][0]}',
                    '{relic.substats[1][1]}',
                    '{relic.substats[2][0]}',
                    '{relic.substats[2][1]}',
                    '{relic.substats[3][0]}',
                    '{relic.substats[3][1]}'
            )
        """)
        self._connection.commit()
        return relic


relic_repository = RelicRepository(get_database_connection())
