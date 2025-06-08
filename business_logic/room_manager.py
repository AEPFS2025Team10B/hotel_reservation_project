from data_access.hotel_data_access import HotelDataAccess
from data_access.room_data_access import RoomDataAccess
from datetime import datetime

#from model.hotel import Hotel

# Optional: Übergib den Pfad als Parameter, falls du später dynamisch arbeitest
hotel_dao = HotelDataAccess()
room_dao  = RoomDataAccess()

# (User Story 1.6.1)
def get_available_rooms_by_hotel(hotel_id: int, today: str):
    return room_dao.get_rooms_by_hotel(hotel_id, today)

def get_next_available_date_for_hotel(hotel_id: int):
    return room_dao.get_next_available_date_for_hotel(hotel_id)

# (User Story 2.1) Show all Room Types of Hotel
def get_room_types_by_hotel(hotel_id: int):
    return room_dao.get_room_types_by_hotel(hotel_id)

# (User Story 2.2) Show available rooms of a hotel for a date range
def get_available_rooms_by_hotel_and_dates(hotel_id: int, check_in: str, check_out: str):
    return room_dao.get_available_rooms_by_hotel_and_dates(hotel_id, check_in, check_out)

# (User Story 4) Show available rooms of a hotel for a date range
def get_available_rooms_by_hotel_and_dates_2(hotel_id: int, check_in_date: str, check_out_date: str):
    return room_dao.get_available_rooms_by_hotel_and_dates_2(hotel_id, check_in_date, check_out_date)

def find_room_by_id(room_id: int):
    return room_dao.get_room_by_id(room_id)


def apply_seasonal_discount(rooms: list, check_in_date_str: str) -> list:
    check_in_date = datetime.strptime(check_in_date_str, "%Y-%m-%d")
    month = check_in_date.month

    if 2 <= month <= 6 or 10 <= month <= 11:
        for room in rooms:
            original_price = room.price_per_night
            room.price_per_night *= 0.9
            print(f"✅ Rabatt angewendet: {original_price:.2f} ➜ {room.price_per_night:.2f}")
    else:
        print("🟦 Kein Rabatt für dieses Datum")

    return rooms

def get_all_rooms_with_facilities():
    rows = room_dao.get_all_rooms_with_facilities()
    result = []
    for row in rows:
        result.append({
            "hotel_name": row[0],
            "room_number": row[1],
            "room_type": row[2],
            "max_guests": row[3],
            "price_per_night": row[4],
            "facilities": row[5] or "Keine"
        })
    return result