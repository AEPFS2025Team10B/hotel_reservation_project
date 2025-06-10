"""
User Story 2.2: Ich möchte nur die verfügbaren Zimmer sehen, sofern
ich meinen Aufenthalt (von – bis) spezifiziert habe.
"""

import sys
import os
from datetime import datetime
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_available_rooms_by_hotel_and_dates

DATE_FORMAT = "%Y-%m-%d"

def ask_date(prompt: str) -> str:
    pattern = r"^\d{4}[-./]\d{2}[-./]\d{2}$"
    while True:
        s = input(prompt).strip()
        if not re.match(pattern, s):
            print("Please enter a date in the format: YYYY-MM-DD, YYYY.MM.DD or YYYY/MM/DD.")
            continue
        try:
            parts = re.split(r"[-./]", s)
            date_obj = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            return date_obj.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date. Please enter a valid date.")

def main():
    check_in = ask_date("Check-in (YYYY-MM-DD, . or / also allowed): ")

    while True:
        check_out = ask_date("Check-out (YYYY-MM-DD, . or / also allowed): ")
        if check_out <= check_in:
            print("Check-out date must be after check-in date.")
        else:
            break

    hotels = find_all_hotel_details()
    print(f"\nAvailable room from {check_in} to {check_out} in all hotels:")
    any_available = False

    for hotel in hotels:
        rooms = get_available_rooms_by_hotel_and_dates(hotel.hotel_id, check_in, check_out)
        if rooms:
            any_available = True
            print(f"\n{hotel.name} (Address: {hotel.address.street}, {hotel.address.city}, {hotel.address.zip_code}):")
            for r in rooms:
                print(f" - Room {r.number}, Type: {r.roomtype.description} (max {r.roomtype.max_guests} guests), CHF {r.price_per_night:.2f} per night")

    if not any_available:
        print("No available rooms, in all the hotels in this time period.")

if __name__ == "__main__":
    main()