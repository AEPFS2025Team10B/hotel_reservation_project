from data_access.hotel_data_access import get_hotels_by_city

def find_hotels_by_city(city: str) -> list:
    return get_hotels_by_city(city)