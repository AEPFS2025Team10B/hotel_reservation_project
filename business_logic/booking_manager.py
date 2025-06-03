#Buchungen verwalten, Verfügbarkeit
from data_access import BookingDataAccess
from model.room import Room
from business_logic.guest_manager import find_guest_by_email

# DAO-Instanzen
booking_dao = BookingDataAccess()

def add_new_booking(email: str, selected_room: Room, check_in_date: str, check_out_date: str):
    guest_id = find_guest_by_email(email)
    room_id = selected_room.room_id
    total_amount = 10
    return booking_dao.insert_booking(guest_id, room_id, check_in_date, check_out_date, total_amount)