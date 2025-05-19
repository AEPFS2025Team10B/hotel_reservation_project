# business_logic/hotel_manager.py

from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess

# DAO-Instanzen
hotel_dao = HotelDataAccess()
room_dao  = RoomDataAccess()

# (User Story 1.1) Hotels in einer Stadt durchsuchen
def find_hotels_by_city(city: str):
    return hotel_dao.get_hotels_by_city(city)

# (User Story 1.2) Hotels in einer Stadt mit Mindest-Sterne durchsuchen
def find_hotels_by_city_and_min_stars(city: str, min_stars: int):
    return hotel_dao.get_hotels_by_city_and_min_stars(city, min_stars)

# (User Story 1.3) Hotels mit Zimmern für eine bestimmte Gästeanzahl durchsuchen
def find_hotels_by_guest_count(city: str, guest_count: int):
    return room_dao.get_hotels_by_guest_count(city, guest_count)

# (User Story 1.4) Hotels nach Verfügbarkeit im Zeitraum durchsuchen
def find_hotels_by_availability(check_in_date: str, check_out_date: str):
    return room_dao.get_hotels_by_availability(check_in_date, check_out_date)

# (User Story 1.5) Hotels nach mehreren Kriterien (Stadt, Sterne, Gäste, Zeitraum) durchsuchen
def find_hotels_by_multiple_criteria(city: str, min_stars: int, guest_count: int, check_in_date: str, check_out_date: str):
    return hotel_dao.get_hotels_by_multiple_criteria(
        city, min_stars, guest_count, check_in_date, check_out_date
    )

# (User Story 1.6) Alle Hotel-Details (Name, Adresse, Sterne) abrufen
def find_all_hotel_details():
    return hotel_dao.get_all_hotel_details()

# (User Story 3.1) Admin fügt neues Hotel hinzu
def add_new_hotel(name: str, stars: int, street: str, city: str, zip_code: str):
    addr = hotel_dao.create_address(street, city, zip_code)
    hotel = hotel_dao.create_hotel(name, stars, addr.address_id)
    return hotel

# (User Story 3.2) Admin entfernt ein Hotel aus dem System
def remove_hotel(hotel_id: int):
    hotel_dao.delete_hotel(hotel_id)

    
# (User Story 3.3) Admin aktualisiert ein Hotel
def update_hotel(name: str, stars: int, street: str, city: str, zip_code: str, hotel_id: int):
    addr = hotel_dao.update_address(hotel_id, street, city, zip_code)
    current = hotel_dao.get_hotel_by_id(hotel_id)
    current.name  = name
    current.stars = stars
    hotel_dao.update_hotel(current)
    return current