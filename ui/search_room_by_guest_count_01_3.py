"""
User Story 1.3: Filter hotels in a city by room capacity (one room per booking).
As a guest, I want to search all hotels in a city that have a room for all my guests.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_hotels_by_guest_count

DB_PATH = "database/hotel_reservation_sample.db"
def main():
    print("Hotel Search by Guest Count")

    guest_count = None
    valid = False
    while not valid:
        try:
            guest_count = int(input("How many people should have space in this room? "))
            if guest_count < 1:
                raise ValueError
            print("")
            print("Enter to finish...")  # TODO: Auf verschiednen Files, eventuell so machen, dass man nur 1 mal anpassen muss
            valid = True
        except ValueError:
            print("Enter a valid number and number must be above 0")
            continue

    hotels = find_hotels_by_guest_count(guest_count)

    if hotels:
        print(f"\nThese hotels have a room for at least {guest_count} guests:\n")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")
    else:
        print(f"\nNo hotels found with rooms for {guest_count} guests.")

    return hotels