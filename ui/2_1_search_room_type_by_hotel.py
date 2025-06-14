"""
User Story 2.1: Ich möchte alle Raumtypen pro Hotel sehen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_room_types_by_hotel
from common_code.find_hotel_by_list_city import find_hotel_by_list_city
from business_logic.hotel_manager import print_all_hotel_details

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
                    selected_hotel = hotels[selection - 1]
                    print(f"\nRoom Types for {selected_hotel.name}:")

                    room_types = get_room_types_by_hotel(selected_hotel.hotel_id)

                    if room_types:
                        for rt in room_types:
                            print("\n-------------------------------")
                            print(f"→ {rt.name}")
                            print(f"   Description: {rt.description}")
                            print(f"   Max guests: {rt.max_guests}")
                            print(f"   Price per night: CHF {rt.price_per_night:.2f}")
                            print(f"   Facilities: {', '.join(rt.facilities) if rt.facilities else 'None'}")
                            print("\n-------------------------------")

                            valid = True

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