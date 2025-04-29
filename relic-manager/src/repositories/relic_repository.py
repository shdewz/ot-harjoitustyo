from entities.relic import Relic
from db import get_database_connection


class RelicRepository:
    """Class responsible for handling database operations for relics
    """

    def __init__(self, connection):
        """Constructor
        
        Args:
            connection: Connection object for the database
        """

        self._connection = connection

    def find_all(self):
        """Returns all relics

        Returns:
            Returns a list of Relic objects
        """

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
        """Deletes all relics from the database
        """

        cursor = self._connection.cursor()
        cursor.execute("delete from relics;")
        self._connection.commit()

    def create(self, relic):
        """Adds a relic to the database

        Args:
            relic: a Relic object to add

        Returns:
            Returns the added Relic object along with its newly created ID
        """

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
        """Removes a specific relic from the database

        Args:
            relic_id: ID of the relic to be removed
        """

        cursor = self._connection.cursor()
        cursor.execute(f"delete from relics where id = {relic_id};")
        self._connection.commit()


relic_repository = RelicRepository(get_database_connection())
