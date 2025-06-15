# business_logic/hotel_manager.py

from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess
from data_access.address_data_access import AddressDataAccess

# DAO-Instanzen
hotel_dao = HotelDataAccess()
room_dao  = RoomDataAccess()
address_dao = AddressDataAccess()

# (User Story 1.1) Hotels in einer Stadt durchsuchen
def find_hotels_by_city(city: str):
    return hotel_dao.get_hotels_by_city(city)

# (User Story 1.2) Hotels in einer Stadt mit Mindest-Sterne durchsuchen
def find_hotels_by_city_and_min_stars(city: str, min_stars: int):
    return hotel_dao.get_hotels_by_city_and_min_stars(city, min_stars)

# (User Story 1.3) Hotels mit Zimmern für eine bestimmte Gästeanzahl durchsuchen
def find_hotels_by_guest_count(guest_count: int):
    return hotel_dao.get_hotels_by_guest_count(guest_count)

# (User Story 1.4) Hotels nach Verfügbarkeit im Zeitraum durchsuchen
def find_hotels_by_availability(check_in_date: str, check_out_date: str):
    return hotel_dao.get_hotels_by_availability(check_in_date, check_out_date)

# (User Story 1.5) Hotels nach mehreren Kriterien (Stadt, Sterne, Gäste, Zeitraum) durchsuchen
def find_hotels_by_multiple_criteria(city: str, min_stars: int, guest_count: int, check_in_date: str, check_out_date: str):
    return hotel_dao.get_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)

# (User Story 1.6) Alle Hotel-Details (Name, Adresse, Sterne) abrufen
def find_all_hotel_details():
    return hotel_dao.get_all_hotel_details()

# (User Story 3.1) Admin fügt neues Hotel hinzu
def add_new_hotel(name: str, stars: int, street: str, city: str, zip_code: str):
    # Prüfe ob das Hotel bereits existiert
    if hotel_dao.hotel_exists(name, street, city, zip_code):
        raise ValueError(f"A hotel with the name:'{name}' and address '{street}, {city} {zip_code}' already exists.")
    #Der Fehler kommt nur, wenn Der Name und die Adresse übereinstimmt.
    #Überlegung: Es kann sein das ein hotel denselben namen hat, wie ein anderes,
    # aber es kann nicht die gleiche Adresse haben.
    
    # Wenn nicht, erstelle das neue Hotel
    addr = hotel_dao.create_address(street, city, zip_code)
    hotel = hotel_dao.create_hotel(name, stars, addr.address_id)
    return hotel

# (User Story 3.2) Admin entfernt ein Hotel aus dem System
def remove_hotel(hotel_id: int):
    hotel_dao.delete_hotel(hotel_id)

    
# (User Story 3.3) Admin aktualisiert ein Hotel
def update_hotel(name: str, stars: int, street: str, city: str, zip_code: str, hotel_id: int):
    current = hotel_dao.get_hotel_by_id(hotel_id)
    if current and current.address:
        # Update the address
        current.address.street = street
        current.address.city = city
        current.address.zip_code = zip_code
        address_dao.update_address(current.address)
        
        # Update the hotel
        current.name = name
        current.stars = stars
        hotel_dao.update_hotel(current)
        return current
    return None

def find_hotel_id_by_room_id(room_id: int):
    return hotel_dao.get_hotel_id_by_room_id(room_id)

def find_hotel_by_id_2(hotel_id: int):
    return hotel_dao.get_hotel_by_id_2(hotel_id)

def print_all_hotel_details(hotels):
    # Wenn ein einzelnes Hotel übergeben wurde, mache eine Liste daraus
    if not isinstance(hotels, list):
        hotels = [hotels]
    for index, hotel in enumerate(hotels, start=1):
        print(f"{index}. {hotel.name} ({hotel.stars}★), Address: {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}")

# def print_all_hotel_details_with_room_details(hotels):

def create_detailed_hotel_list(hotels):
    if not isinstance(hotels, list):
        hotels = [hotels]
    for hotel in hotels:
        rooms = room_dao.get_room_with_hotel(hotel.hotel_id)
        hotel.rooms = rooms
    return hotels

def print_detailed_hotel_list(detailed_hotels):
    if not isinstance(detailed_hotels, list):
        detailed_hotels = [detailed_hotels]
    output = ""
    for index, hotel in enumerate(detailed_hotels, start=1):
        output += f"{index}. {hotel.name} ({hotel.stars}★), Address: {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}\n"
        if hasattr(hotel, 'rooms'):
            for room in hotel.rooms:
                output += f"  Room {room.number}: {room.price_per_night} CHF, Type: {room.roomtype.description}, Max Guests: {room.roomtype.max_guests}\n"
                if room.facilities:
                    for facility in room.facilities:
                        output += f"    - Facility: {facility.name}\n"
    return output