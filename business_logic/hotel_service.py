from data_access.room_data_access import get_hotels_by_availability

from data_access.hotel_data_access import get_hotels_by_city

from data_access.hotel_data_access import get_hotels_by_city_and_min_stars

from data_access.room_data_access import get_hotels_by_guest_count

def find_hotels_by_city(city: str) -> list:
    return get_hotels_by_city(city)

def find_hotels_by_city_and_min_stars(city: str, min_stars: int) -> list:
    return get_hotels_by_city_and_min_stars(city, min_stars)

def find_hotels_by_guest_count(city: str, guest_count: int) -> list:
    return get_hotels_by_guest_count(city, guest_count)

def find_hotels_by_availability(check_in_date: str, check_out_date: str) -> list:
    return get_hotels_by_availability(check_in_date, check_out_date)

