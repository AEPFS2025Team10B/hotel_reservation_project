import model
from data_access.base_data_access import BaseDataAccess

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # (User Story 1.3) Filter hotels in a city by room capacity (guest count)
    def get_hotels_by_guest_count(self, city: str, guest_count: int) -> list[model.Hotel]:
        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE LOWER(Address.city) = LOWER(?) AND Room_Type.max_guests >= ?
        """
        result = self.fetchall(sql, (city, guest_count))
        return [model.Hotel(hotel_id, name, stars, city, street) for hotel_id, name, stars, city, street in result]

    # (User Story 1.4) Filter hotels by room availability in a date range
    def get_hotels_by_availability(self, check_in_date: str, check_out_date: str) -> list[model.Hotel]:
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
        return [model.Hotel(hotel_id, name, stars, city, street) for hotel_id, name, stars, city, street in result]