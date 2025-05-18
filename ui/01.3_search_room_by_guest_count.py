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
    city = input("Enter city: ").strip()

    try:
        guest_count = int(input("And how many people should have space in this room? "))
    except ValueError:
        print("Enter a valid number.")
        return

    hotels = find_hotels_by_guest_count(city, guest_count)

    if hotels:
        print(f"\nThese hotels in {city} have a room for at least {guest_count} guests:\n")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")
    else:
        print(f"\nNo hotels in {city} found with rooms for {guest_count} guests.")