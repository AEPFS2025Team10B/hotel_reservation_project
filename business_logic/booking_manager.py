#Buchungen verwalten, Verfügbarkeit
from business_logic import invoice_manager
from data_access import BookingDataAccess
from model.hotel import Hotel
from model.guest import Guest
from business_logic.hotel_manager import find_hotel_by_id
from model.room import Room
from business_logic.guest_manager import find_guest_by_email
from business_logic.guest_manager import find_guest_by_id
from business_logic.room_manager import find_room_by_id
from business_logic.invoice_manager import create_invoice_by_booking_id
from business_logic.room_manager import apply_seasonal_discount
from model.booking import Booking
from datetime import datetime
from business_logic.room_manager import find_room_by_id
from business_logic.hotel_manager import find_hotel_id_by_room_id

# DAO-Instanzen
booking_dao = BookingDataAccess()

def add_new_booking(email: str, selected_room: Room, check_in_date: str, check_out_date: str, selected_hotel: Hotel):
    is_cancelled = 0
    guest = find_guest_by_email(email)
    guest_id = guest.guest_id
    room_id = selected_room.room_id
    check_in = datetime.strptime(check_in_date, "%Y-%m-%d")
    check_out = datetime.strptime(check_out_date, "%Y-%m-%d")
    num_nights = (check_out - check_in).days
    total_amount = num_nights * selected_room.price_per_night
    booking = booking_dao.insert_booking(guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
    booking.room = selected_room
    booking.guest = guest
    booking.room.hotel = selected_hotel
    booking.check_in_date = check_in
    booking.check_out_date = check_out
    booking.total_amount = total_amount
    invoice = create_invoice_by_booking_id(booking.booking_id)
    return generate_booking_confirmation(booking)

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

def get_reviews_by_hotel_name(hotel_name: str):
    return booking_dao.get_reviews_by_hotel_name(hotel_name)


def get_all_bookings_with_details():
    rows = booking_dao.display_all_bookings_of_all_hotels()

    result = []
    for row in rows:
        hotel_name, booking_id, guest_name, room_number, check_in, check_out = row
        result.append({
            "Buchungsnummer": booking_id,
            "Hotelname": hotel_name,
            "Gastname": guest_name,
            "Zimmernummer": room_number,
            "CheckInDatum": check_in,
            "CheckOutDatum": check_out
        })

    return result

def cancel_booking_by_id(booking_id: int):
    booking_dao.cancel_booking(booking_id)
    booking = find_booking_by_id(booking_id)
    invoice_manager.delete_invoice_by_booking_id(booking.booking_id)
    return booking

def generate_booking_confirmation(booking: Booking) -> str:
    lines = []
    lines.append("\n✅ Booking Confirmation")
    lines.append("=" * 40)
    lines.append(f" Booking ID: {booking.booking_id}")
    lines.append(f"👤 Guest: {booking.guest.first_name} {booking.guest.last_name}  |  📧 {booking.guest.email}")
    lines.append(f"🏨 Hotel: {booking.room.hotel.name}, {booking.room.hotel.address}")
    lines.append(f"🛏️ Room Number: {booking.room.number}  |  Type: {booking.room.roomtype.description}")
    lines.append(f"💰 Price per Night: CHF {booking.room.price_per_night:.2f}")
    lines.append(f"📅 Stay: {booking.check_in_date.strftime('%d.%m.%Y')} to {booking.check_out_date.strftime('%d.%m.%Y')}")
    lines.append(f"🌙 Nights: {(booking.check_out_date - booking.check_in_date).days}")
    lines.append(f"💵 Total Amount: CHF {booking.total_amount:.2f}")
    lines.append("=" * 40)
    return "\n".join(lines)

def find_bookings_by_email(email: str) -> list[Booking]:
    guest = find_guest_by_email(email)
    if not guest:
        return f"No Guest found for {email}"
    bookings = booking_dao.get_bookings_by_guest_id(guest.guest_id)
    return bookings