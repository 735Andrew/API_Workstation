"""Initialize PostgreSQL database"""

from typing import Optional
from time import sleep
import psycopg2 as ps
from config import POSTGRESQL_DATABASE_URL


connection: Optional = None
cursor: Optional = None


def get_db():
    global connection, cursor

    sleep(5)
    connection = ps.connect(POSTGRESQL_DATABASE_URL)
    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS weather
        (
            report_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            city TEXT NOT NULL,
            temperature INT NOT NULL
        );
        """
    )

    connection.commit()


get_db()
