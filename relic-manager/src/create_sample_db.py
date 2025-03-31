from init_db import initialize_database
from db import get_database_connection


if __name__ == "__main__":
    initialize_database()

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into relics (relic_set, type, level, mainstat, substat1, substat1value)
        values ('Scholar Lost in Erudition', 'Head', 15, 'ATK%', 'SPD', 7.6)
    """)

    cursor.execute("""
        insert into relics (relic_set, type, level, mainstat, substat1, substat1value)
        values ('Scholar Lost in Erudition', 'Body', 15, 'CDMG', 'SPD', 7.1)
    """)

    connection.commit()
