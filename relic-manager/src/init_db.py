from db import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists relics;
    """)

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute("""
        create table relics (
            id integer primary key not null,
            relic_set text,
            type text,
            level integer,
            mainstat text,
            substat1 text,
            substat1value real,
            substat2 text,
            substat2value real,
            substat3 text,
            substat3value real,
            substat4 text,
            substat4value real
        );
    """)

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()