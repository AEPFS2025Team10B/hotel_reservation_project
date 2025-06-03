#Buchungen verwalten, Verfügbarkeit
from data_access import BookingDataAccess
from model.room import Room
from business_logic.guest_manager import find_guest_by_email

# DAO-Instanzen
booking_dao = BookingDataAccess()

def add_new_booking(email: str, selected_room: Room, check_in_date: str, check_out_date: str):
    is_cancelled = 0
    guest_id = find_guest_by_email(email)
    room_id = selected_room.room_id
    total_amount = 10
    booking = booking_dao.insert_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    booking.room_id = room_id
    booking.guest_id = guest_id
    booking.total_amount = total_amount
    return booking