import sqlite3

DB_PATH = "database/hotel_reservation_sample.db"

#(Userstory 1.1) Search a Hotel by City 
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

#(User Story 1.2) Search a Hotel by City and min star 
def get_hotels_by_city_and_min_stars(city: str, min_stars: int) -> list:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
    FROM Hotel
    JOIN Address ON Hotel.address_id = Address.address_id
    WHERE LOWER(Address.city) = LOWER(?) AND Hotel.stars >= ?
    """
    cursor.execute(query, (city, min_stars))
    result = cursor.fetchall()

    connection.close()
    return result

