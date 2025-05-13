#Räume anzeigen, filtern
from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess

#from model.hotel import Hotel

# Optional: Übergib den Pfad als Parameter, falls du später dynamisch arbeitest
hotel_dao = HotelDataAccess()
room_dao = RoomDataAccess()

# (User Story 1.6.1)
def get_available_rooms_by_hotel(hotel_id: int, today: str):
    return room_dao.get_available_rooms_for_hotel(hotel_id, today)

def get_next_available_date_for_hotel(hotel_id: int):
    return room_dao.get_next_available_date_for_hotel(hotel_id)