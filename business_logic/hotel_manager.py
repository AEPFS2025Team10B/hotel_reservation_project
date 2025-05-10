from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess

# Optional: Übergib den Pfad als Parameter, falls du später dynamisch arbeitest
hotel_dao = HotelDataAccess()
room_dao = RoomDataAccess()

# (User Story 1.1)
def find_hotels_by_city(city: str):
    return hotel_dao.get_hotels_by_city(city)

# (User Story 1.2)
def find_hotels_by_city_and_min_stars(city: str, min_stars: int):
    return hotel_dao.get_hotels_by_city_and_min_stars(city, min_stars)

# (User Story 1.3)
def find_hotels_by_guest_count(city: str, guest_count: int):
    return room_dao.get_hotels_by_guest_count(city, guest_count)

# (User Story 1.4)
def find_hotels_by_availability(check_in_date: str, check_out_date: str):
    return room_dao.get_hotels_by_availability(check_in_date, check_out_date)

# (User Story 1.5)
def find_hotels_by_multiple_criteria(city: str, min_stars: int, guest_count: int, check_in_date: str, check_out_date: str):
    return hotel_dao.get_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)

# (User Story 1.6)
def find_all_hotel_details():
    return hotel_dao.get_all_hotel_details()