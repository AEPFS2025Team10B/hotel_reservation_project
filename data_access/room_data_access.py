from data_access.base_data_access import BaseDataAccess
from model.Hotel import Hotel  # da du Hotel-Objekte zurückgibst

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.3: Hotels mit Zimmern für X Gäste
    def get_hotels_by_guest_count(self, city: str, guest_count: int) -> list[Hotel]:
        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE LOWER(Address.city) = LOWER(?) AND Room_Type.max_guests >= ?
        """
        result = self.fetchall(sql, (city, guest_count))
        return [Hotel(hotel_id, name, stars, city, street) for hotel_id, name, stars, city, street in result]

    # User Story 1.4: Verfügbarkeit nach Zeitraum
    def get_hotels_by_availability(self, check_in_date: str, check_out_date: str) -> list[Hotel]:
        sql = """
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
        result = self.fetchall(sql, (check_in_date, check_out_date))
        return [Hotel(hotel_id, name, stars, city, street) for hotel_id, name, stars, city, street in result]