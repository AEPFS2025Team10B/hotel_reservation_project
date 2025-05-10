import sqlite3

DB_PATH = "database/hotel_reservation_sample.db" 

#UserStory 1.3
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

# UserStory 1.4
def get_hotels_by_availability(check_in_date: str, check_out_date: str) -> list:
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    query = """
SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
FROM Hotel
JOIN Address ON Hotel.address_id = Address.address_id
JOIN Room ON Hotel.hotel_id = Room.hotel_id
LEFT JOIN Booking ON Room.room_id = Booking.room_id
    AND Booking.is_cancelled = 0
    AND NOT (
        Booking.check_out_date <= ? OR Booking.check_in_date >= ?
    )
WHERE Booking.booking_id IS NULL
"""