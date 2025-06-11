"""
User Story 1.3: Filter hotels in a city by room capacity (one room per booking).
As a guest, I want to search all hotels in a city that have a room for all my guests.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_hotels_by_guest_count
from model.roomtype import RoomType

def main():
    print("Hotel Search by Guest Count")

    guest_count = None
    valid = False
    while not valid:
    # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
    # jetzt kann er es einfach wieder eingeben.
        try:
            guest_count = int(input("How many people should have space in this room? "))
            if guest_count < 1:
                raise ValueError

            valid = True
        except ValueError:
            print("Enter a valid number and number must be above 0")
            continue

    hotels = find_hotels_by_guest_count(guest_count)

    if hotels:
        print(f"\nThese hotels have a room for at least {guest_count} guests:\n")
        for index, hotel in enumerate(hotels, start=1):
            matching_room = next((r for r in hotel.rooms if r.roomtype and r.roomtype.max_guests >= guest_count), None)
            description = matching_room.roomtype.description if matching_room and matching_room.roomtype else "Unbekannt"
            max_guests = matching_room.roomtype.max_guests if matching_room and matching_room.roomtype else "?"
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}, {description} (Max. Guests: {max_guests})")
            print("")
            input("Enter to finish...")
    else:
        print(f"\nNo hotels found with rooms for {guest_count} guests.")
        print("")
        input("Enter to finish...")

    return hotels