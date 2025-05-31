# ui/01.6_search_all_hotel_details.py

"""
User Story 1.6: Ich möchte Name, Adresse und Anzahl der Sterne jedes Hotels sehen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
today = date.today().isoformat()

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_available_rooms_by_hotel, get_next_available_date_for_hotel


def main():
    print("All Hotels")
    hotels = find_all_hotel_details()
    
    if hotels:
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")
        try:
            selection = int(input("\nEnter the number of the hotel you want to see the details: ").strip())
            if 1 <= selection <= len(hotels):
                selected_hotel = hotels[selection - 1]

                print(f"\nDetails for {selected_hotel.name}:")
                print(f"Address: {selected_hotel.address}")
                print(f"Stars: {selected_hotel.stars}")

                available_rooms = get_available_rooms_by_hotel(selected_hotel.hotel_id, today)
                print("\nAvailable rooms today:")
                if available_rooms:
                    for room in available_rooms:
                        print(f" - Room {room.number}, CHF {room.price_per_night:.2f} per night")
                else:
                    print(" No available rooms today.")
                    next_date = get_next_available_date_for_hotel(selected_hotel.hotel_id)
                    if next_date:
                        print(f"\nNext available date for any room: {next_date}")
                    else:
                        print("No future availability found.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("No hotels found.")
        return




if __name__ == "__main__":
    main()