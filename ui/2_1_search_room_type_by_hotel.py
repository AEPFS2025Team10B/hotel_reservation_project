"""
User Story 2.1: Ich möchte alle Raumtypen pro Hotel sehen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.hotel_manager import print_all_hotel_details
from business_logic.hotel_manager import create_detailed_hotel_list

def main():
    print("All Hotels")
    hotels = find_all_hotel_details()

    if hotels:
        print(print_all_hotel_details(hotels))
        valid = False
        while not valid:
            # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
            # jetzt kann er es einfach wieder eingeben.
            try:
                selection = int(input("\nEnter the number of the hotel you want to see the Room Types: ").strip())
                if 1 <= selection <= len(hotels):
                    selected = hotels[selection - 1]
                    detailed_hotels = create_detailed_hotel_list(selected)
                    if not isinstance(detailed_hotels, list):
                        detailed_hotels = [detailed_hotels]
                    print(f"\nRoom Types for:")
                    output = ""
                    for index, hotel in enumerate(detailed_hotels, start=1):
                        output += f"{index}. {hotel.name} ({hotel.stars}★), Address: {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}\n"
                        if hasattr(hotel, 'rooms'):
                            unique_roomtypes = set()
                            for room in hotel.rooms:
                                rt_key = room.roomtype.description
                                if rt_key not in unique_roomtypes:
                                    output += f"  Room Type: {room.roomtype.description}, Max Guests: {room.roomtype.max_guests}\n"
                                    if room.facilities:
                                        for facility in room.facilities:
                                            output += f"    - Facility: {facility.name}\n"
                                    unique_roomtypes.add(rt_key)

                            valid = True
                            print(output)
                        else:
                            print("No room types found for this hotel.")
                            valid = True
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")
    else:
        print("No hotels found.")
        return

    input("Press Enter to finish")

if __name__ == "__main__":
    main()