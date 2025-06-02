"""
User Story 2.2: Ich möchte nur die verfügbaren Zimmer sehen, sofern
ich meinen Aufenthalt (von – bis) spezifiziert habe.
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_available_rooms_by_hotel_and_dates

DATE_FORMAT = "%Y-%m-%d"

def ask_date(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        try:
            datetime.strptime(s, DATE_FORMAT)
            return s
        except ValueError:
            print("Bitte ein Datum im Format YYYY-MM-DD eingeben.")

def main():
    check_in  = ask_date("Check-in (YYYY-MM-DD): ")
    check_out = ask_date("Check-out (YYYY-MM-DD): ")

    hotels = find_all_hotel_details()
    print(f"\nVerfügbare Zimmer vom {check_in} bis {check_out} in allen Hotels:")
    any_available = False

    for hotel in hotels:
        rooms = get_available_rooms_by_hotel_and_dates(hotel.hotel_id, check_in, check_out)
        if rooms:
            any_available = True
            print(f"\n{hotel.name} ({hotel.address}):")
            for r in rooms:
                print(f" - Zimmer {r.number}, CHF {r.price_per_night:.2f} pro Nacht")

    if not any_available:
        print("Keine verfügbaren Zimmer in diesem Zeitraum in allen Hotels.")

if __name__ == "__main__":
    main()