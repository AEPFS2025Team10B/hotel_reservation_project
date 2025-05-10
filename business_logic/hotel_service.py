from data_access.room_data_access import get_hotels_by_availability

from data_access.hotel_data_access import get_hotels_by_city

from data_access.hotel_data_access import get_hotels_by_city_and_min_stars

from data_access.room_data_access import get_hotels_by_guest_count

from data_access.hotel_data_access import get_hotels_by_multiple_criteria

def find_hotels_by_city(city: str) -> list:
    return get_hotels_by_city(city)

def find_hotels_by_city_and_min_stars(city: str, min_stars: int) -> list:
    return get_hotels_by_city_and_min_stars(city, min_stars)

def find_hotels_by_guest_count(city: str, guest_count: int) -> list:
    return get_hotels_by_guest_count(city, guest_count)

def find_hotels_by_availability(check_in_date: str, check_out_date: str) -> list:
    return get_hotels_by_availability(check_in_date, check_out_date)

def find_hotels_by_multiple_criteria(city:str, min_stars:int, guest_count:int, check_in_date:str, check_out_date:str) -> list:
    return get_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)
