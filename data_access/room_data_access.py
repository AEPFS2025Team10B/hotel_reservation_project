import sqlite3

DB_PATH = "database/hotel_reservation_sample.db" 

def get_hotels_by_guest_count(city: str, guest_count: int) -> list:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
    SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
    FROM Hotel
    JOIN Address ON Hotel.address_id = Address.address_id
    JOIN Room ON Hotel.hotel_id = Room.hotel_id
    JOIN Room_Type ON Room.type_id = Room_Type.type_id
    WHERE LOWER(Address.city) = LOWER(?) AND Room_Type.max_guests >= ?
    """
    cursor.execute(query, (city, guest_count))
    result = cursor.fetchall()

    connection.close()
    return result