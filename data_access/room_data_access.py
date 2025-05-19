from model.hotel import Hotel
from model.room import Room
from model.roomtype import RoomType
from data_access.base_data_access import BaseDataAccess
from model.address import Address

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # (User Story 1.3) Filter hotels in a city by room capacity (guest count)
    def get_hotels_by_guest_count(self, city: str, guest_count: int) -> list[Hotel]:
        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.city, Address.street, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        JOIN Room ON Hotel.hotel_id = Room.hotel_id
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE LOWER(Address.city) = LOWER(?) AND Room_Type.max_guests >= ?
        """
        result = self.fetchall(sql, (city, guest_count))
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, city, street, zip_code = row
            address = Address(address_id, city, street, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    # (User Story 1.4) Filter hotels by room availability in a date range
    def get_hotels_by_availability(self, check_in_date: str, check_out_date: str) -> list[Hotel]:
        sql = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.city, Address.street, Address.zip_code
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
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, city, street, zip_code = row
            address = Address(address_id, city, street, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels
    
    
    # (User Story 1.6.1) Show available rooms in hotel *today*
    def get_available_rooms_for_hotel(self, hotel_id: int, today: str):
        sql = """
        SELECT Room.room_id, Room.room_number, Room.price_per_night
        FROM Room
        JOIN Room_Type ON Room.type_id = Room_Type.type_id
        WHERE Room.hotel_id = ?
        AND Room.room_id NOT IN (
            SELECT Booking.room_id
            FROM Booking
            WHERE is_cancelled = 0
            AND DATE(?) BETWEEN DATE(check_in_date) AND DATE(check_out_date)
        )
        """
        result = self.fetchall(sql, (hotel_id, today))
        rooms = []
        for row in result:
            room_id, room_number, price_per_night = row
            room = Room(room_id, room_number, price_per_night)
            rooms.append(room)
        return rooms


    # Next available date for any room in hotel
    def get_next_available_date_for_hotel(self, hotel_id: int):
        sql = """
        SELECT MIN(Booking.check_out_date)
        FROM Booking
        JOIN Room ON Booking.room_id = Room.room_id
        WHERE Room.hotel_id = ? AND Booking.is_cancelled = 0
        """
        result = self.fetchone(sql, (hotel_id,))
        return result[0] if result else None

     # (User Story 2.1) Show all Room Types of Hotel

    def get_room_types_by_hotel(self, hotel_id: int) -> list[RoomType]:
        sql = """
        SELECT 
            RT.type_id,
            RT.description,
            RT.max_guests,
            R.price_per_night,
            GROUP_CONCAT(F.facility_name, ', ') AS facilities
        FROM Room R
        JOIN Room_Type RT ON R.type_id = RT.type_id
        LEFT JOIN Room_Facilities RF ON R.room_id = RF.room_id
        LEFT JOIN Facilities F ON RF.facility_id = F.facility_id
        WHERE R.hotel_id = ?
        GROUP BY RT.type_id, R.price_per_night
        ORDER BY RT.description
        """
        result = self.fetchall(sql, (hotel_id,))
        return [
            RoomType(
                room_type_id=type_id,
                name=description,
                max_guest=max_guests,
                description=description,
                price_per_night=price,
                facilities=facilities.split(', ') if facilities else []
            )
            for type_id, description, max_guests, price, facilities in result
        ]