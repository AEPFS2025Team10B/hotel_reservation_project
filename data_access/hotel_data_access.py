import sqlite3

DB_PATH = "database/hotel_reservation_sample.db"

def get_hotels_by_city(city_name: str) -> list:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
    FROM Hotel
    JOIN Address ON Hotel.address_id = Address.address_id
    WHERE LOWER(Address.city) = LOWER(?);
    """
    cursor.execute(query, (city_name,))
    result = cursor.fetchall()

    connection.close()
    return result