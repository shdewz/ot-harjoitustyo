from init_db import initialize_database
from db import get_database_connection


def populate():
    initialize_database()

    connection = get_database_connection()
    cursor = connection.cursor()

    relics = [
        """'Scholar Lost in Erudition',
            'Head', 15, 'HP',
            'DEF', 16,
            'CRATE%', 9.0,
            'CDMG%', 14.1,
            'RES%', 8.2""",

        """'Pioneer Diver of Dead Waters',
            'Feet', 15, 'ATK%',
            'DEF', 35,
            'SPD', 4.9,
            'CRATE%', 9.3,
            'RES%', 4.3""",

        """'Scholar Lost in Erudition',
            'Body', 15, 'CRATE%',
            'HP', 120,
            'HP%', 4.3,
            'SPD', 4.9,
            'CDMG%', 7.6""",
    ]

    for relic in relics:
        cursor.execute(f"""
            insert into relics (relic_set, type, level, mainstat,
                                substat1, substat1value,
                                substat2, substat2value,
                                substat3, substat3value,
                                substat4, substat4value
            )
            values ({relic})
        """)

    connection.commit()


if __name__ == "__main__":
    populate()
