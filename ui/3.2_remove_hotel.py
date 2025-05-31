"""
User Story 3.2: Ich möchte Hotels aus dem System entfernen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_all_hotel_details, remove_hotel

def main():
    print("___________________")
    print("|- Hotel löschen -|")
    print("___________________")
    hotels = find_all_hotel_details()

    if not hotels:
        print("No Hotel found.")
        return

    for idx, h in enumerate(hotels, start=1):
        print(f"{idx}. {h.name} ({h.stars}★), {h.address}")

    valid = False
    while not valid:
        try:
            sel = int(input("\nNumber of the Hotel you want to remove: ").strip())
            if not (1 <= sel <= len(hotels)):
                print("Invalid Selection.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        hotel = hotels[sel - 1]
        valid = True


    valid = False
    while not valid:
        confirm = input(f"Should the hotel '{hotel.name}' really be deleted? (j/n): ").strip().lower()
        if confirm == 'n':
            print("Cancelled.")
            print("")
            input("Press Enter to finish...")
            break

        elif confirm != 'j':
            print("Cancelled.")
            print("")
            continue


        try:
            remove_hotel(hotel.hotel_id)
            print(f"Hotel '{hotel.name}' was deleted succesfully.")
            input("Press Enter to finish...")
            valid = True
        except Exception as e:
            print(f"Deleting didnt work: {e}")
            valid = True

if __name__ == "__main__":
    main()