from model.hotel import Hotel
from model.address import Address

from data_access.base_data_access import BaseDataAccess

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    #(Userstory 1.1) Search a Hotel by City 
    def get_hotels_by_city(self, city_name: str) -> list[Hotel]:
        query = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.city, Address.street, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE LOWER(Address.city) = LOWER(?);
        """
        result = self.fetchall(query, (city_name,))
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, city, street, zip_code = row
            address = Address(address_id, city, street, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    #(User Story 1.2) Search a Hotel by City and min star
    def get_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[Hotel]:
        query = """
        SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.city, Address.street, Address.zip_code
        FROM Hotel
        JOIN Address ON Hotel.address_id = Address.address_id
        WHERE LOWER(Address.city) = LOWER(?) AND Hotel.stars >= ?
        """
        result = self.fetchall(query, (city, min_stars))
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, city, street, zip_code = row
            address = Address(address_id, city, street, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels

    #(User Story 1.5) Combined Filter (city, stars, guests, availability)
    def get_hotels_by_multiple_criteria(self, city: str, min_stars: int, guest_count: int, check_in_date: str, check_out_date: str) -> list[Hotel]:
        query = """
        SELECT DISTINCT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.address_id, Address.city, Address.street, Address.zip_code
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
        result = self.fetchall(query, (
            check_in_date,
            check_out_date,
            city,
            min_stars,
            guest_count
        ))
        hotels = []
        for row in result:
            hotel_id, name, stars, address_id, city, street, zip_code = row
            address = Address(address_id, city, street, zip_code)
            hotel = Hotel(hotel_id, name, stars, address)
            hotels.append(hotel)
        return hotels
    # #(User Story 1.6) Get all hotel details
    # def get_all_hotel_details(self) -> list[model.Hotel]:
    #     query = """
    #     SELECT Hotel.hotel_id, Hotel.name, Hotel.stars, Address.city, Address.street
    #     FROM Hotel
    #     JOIN Address ON Hotel.address_id = Address.address_id
    #     """
    #     result = self.fetchall(query)
    #     return [model.Hotel(hotel_id, name, stars, city, street) for hotel_id, name, stars, city, street in result]