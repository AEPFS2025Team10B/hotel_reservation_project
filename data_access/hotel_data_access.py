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


def get_hotels_by_multiple_criteria(city:str, min_stars:int, guest_count:int, check_in_date:str, check_out_date:str):
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
    FROM Hotel
    JOIN Address ON Hotel.address_id = Address.address_id
    JOIN Room ON Hotel.hotel_id = Room.hotel_id
    JOIN Room_Type ON Room.type_id = Room_Type.type_id
    LEFT JOIN Booking ON Room.room_id = Booking.room_id
        AND Booking.is_cancelled = 0
        AND NOT (
            Booking.check_out_date <= ? OR Booking.check_in_date >= ?
        )
    WHERE LOWER(Address.city) = LOWER(?)
      AND Hotel.stars >= ?
      AND Room_Type.max_guests >= ?
      AND Booking.booking_id IS NULL
    """

    cursor.execute(query, (
        check_in_date,
        check_out_date,
        city,
        min_stars,
        guest_count
    ))

    result = cursor.fetchall()
    connection.close()
    return result
