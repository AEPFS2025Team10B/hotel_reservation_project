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
    if booking is None:
        return None
    
    relations = booking_dao.get_booking_relations(booking_id)
    if relations:
        guest_id, room_id = relations
        booking.room = find_room_by_id(room_id)
        booking.guest = find_guest_by_id(guest_id)
    return booking

def add_new_hotelrecommendation(booking_id: int, rating: int, recommendation: str):
    if not (1 <= rating <= 10):
        raise ValueError("Rating must be between 1 and 10")
    if recommendation and len(recommendation) > 500:
        raise ValueError("Recommendation too long")
    booking_dao.insert_hotelrecommendation(booking_id, rating, recommendation)
    #gibt Inputs weiter an booking_data_access.py
    return