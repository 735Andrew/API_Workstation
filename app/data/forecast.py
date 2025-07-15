from app.models import Forecast
from app.data.init import connection, cursor
from typing import Dict

ATTEMPTS = 0


def model_to_dict(data: Forecast) -> dict:
    # Converts a Pydantic model into a dictionary suitable for database queries
    return data.model_dump()


def test_data_create() -> None:
    global ATTEMPTS
    ATTEMPTS += 1

    if ATTEMPTS == 1:
        query = """
            INSERT INTO weather
            (city, temperature)
            VALUES
            ('London', 20),
            ('Paris', 10);
        """

        cursor.execute(query)
        connection.commit()

    return None


def forecast_get() -> str:
    query = """SELECT * FROM weather"""

    cursor.execute(query)
    row = cursor.fetchall()

    return str(row)


def forecast_add(data: Forecast) -> Dict:
    query = """
        INSERT INTO weather
        (city,temperature)
        VALUES
        (%s, %s);
    """

    model_dict = model_to_dict(data)
    params = (
        model_dict["city"],
        model_dict["temperature"],
    )

    try:
        cursor.execute(query, params)
    except Exception:
        raise Exception("Wrong data input")
    finally:
        connection.commit()
    return {"success": "Forecast has been added."}
