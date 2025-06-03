#Buchungen verwalten, Verfügbarkeit
from data_access import BookingDataAccess
from model import guest
from model.room import Room
from business_logic.guest_manager import find_guest_by_email
from business_logic.guest_manager import find_guest_by_id
from business_logic.room_manager import find_room_by_id

# DAO-Instanzen
booking_dao = BookingDataAccess()

def add_new_booking(email: str, selected_room: Room, check_in_date: str, check_out_date: str):
    is_cancelled = 0
    guest_id = find_guest_by_email(email)
    guest = find_guest_by_id(guest_id)
    room_id = selected_room.room_id
    total_amount = 10
    booking = booking_dao.insert_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    booking.room = selected_room
    booking.guest = guest
    booking.total_amount = total_amount
    return booking

def find_booking_by_id(booking_id: int):
    booking = booking_dao.get_booking_by_id(booking_id)
    booking.room = customer_room
    booking.guest = guest
    return booking