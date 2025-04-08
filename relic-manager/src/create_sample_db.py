from init_db import initialize_database
from db import get_database_connection


if __name__ == "__main__":
    initialize_database()

    connection = get_database_connection()
    cursor = connection.cursor()

    cursor.execute("""
        insert into relics (relic_set, type, level, mainstat,
                            substat1, substat1value,
                            substat2, substat2value,
                            substat3, substat3value,
                            substat4, substat4value
        )
        values ('Scholar Lost in Erudition',
                'Head', 15, 'ATK',
                'SPD', 7.6,
                'ATK', 81,
                'HP', 65,
                'EHR%', 11.4
        )
    """)

    cursor.execute("""
        insert into relics (relic_set, type, level, mainstat,
                            substat1, substat1value,
                            substat2, substat2value,
                            substat3, substat3value,
                            substat4, substat4value
        )
        values ('Scholar Lost in Erudition',
                'Body', 15, 'CDMG%',
                'SPD', 7.1,
                'ATK', 71,
                'HP', 75,
                'EHR%', 10.4
        )
    """)

    connection.commit()
