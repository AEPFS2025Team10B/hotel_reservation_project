#Hier später Funktionen bzgl:
#Gäste erstellen und lesen

from data_access import GuestDataAccess, BookingDataAccess
from model.guest import Guest
from common_code.age_calculator import calculate_age
import collections


# DAO-Instanzen
guest_dao = GuestDataAccess()
booking_dao = BookingDataAccess()

def add_new_guest(first_name:str, last_name:str, email:str, street: str, city:str, zip:str, nationality: str, birthday) -> Guest:
    from business_logic.address_manager import find_address_id
    address_id = find_address_id(street, city, zip)
    return guest_dao.create_guest(first_name, last_name, email, address_id, birthday, nationality)

def find_guest_by_email(email: str) -> Guest | None:
    return guest_dao.get_guest_by_email(email)

def find_guest_by_id(guest_id:int):
    return guest_dao.get_guest_by_id(guest_id)

def get_guest_demographics():
    all_guests = guest_dao.get_all_guests()
    all_bookings = booking_dao.get_all_bookings()

    age_groups = collections.defaultdict(int)

    nationalities = collections.defaultdict(int)

    guest_booking_counts = collections.defaultdict(int)

    for guest_obj in all_guests:
        # das alter wird berechnet
        if guest_obj.birthday:
            try:
                age = calculate_age(guest_obj.birthday)
                if 0 <= age <= 25: age_groups["0-25"] += 1
                elif 26 <= age <= 35: age_groups["26-35"] += 1
                elif 36 <= age <= 45: age_groups["36-45"] += 1
                elif 46 <= age <= 70: age_groups["46-70"] += 1
                else: age_groups["70+"] += 1
            except ValueError:
                pass
        
        # hier werden die nationalitäten gezählt
        if guest_obj.nationality:
            nationalities[guest_obj.nationality] += 1

    for booking in all_bookings:
        guest_booking_counts[booking.guest_id] += 1

    recurring_guests_count = sum(1 for count in guest_booking_counts.values() if count > 1)

    return {
        "age_groups": dict(age_groups),
        "nationalities": dict(nationalities),
        "recurring_guests": recurring_guests_count
    }