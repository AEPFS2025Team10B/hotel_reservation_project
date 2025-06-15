"""
User Story 3.2: Ich möchte Hotels aus dem System entfernen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_all_hotel_details, remove_hotel
from business_logic.hotel_manager import print_all_hotel_details

def main():
    print("___________________")
    print("|- delete hotel -|")
    print("___________________")
    hotels = find_all_hotel_details()

    if not hotels:
        print("No Hotel found.")
        #falls keine Hotels gefunden wurden
        return

    print(print_all_hotel_details(hotels))

    hotel = None

    valid = False
    while not valid:
        # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
        # jetzt kann er es einfach wieder eingeben.
        try:
            print(f"\n\nfor Coach: do not delete hotel: Les Trois Rois, its good to check user story 3_1_add_new_hotel")
            sel = int(input("\nNumber of the Hotel you want to remove: ").strip())
            if not (1 <= sel <= len(hotels)):
                #Es wird geprüft, ob die eingabe vom User gültig war (grösser oder 1 bis Anzahl Hotels)
                print("Invalid Selection.")
                #wird ausgegeben, vals der Input ungültig war
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        hotel = hotels[sel - 1]
        valid = True


    valid = False
    while not valid:
        confirm = input(f"Should the hotel '{hotel.name}' really be deleted? (y/n): ").strip().lower()
        if confirm == 'n':
            print("Cancelled.")
            #Kunde wird informiert, dass der Vorgang beendet wurde.
            input(f"\nPress Enter to finish")
            break

        elif confirm != 'y':
            print("Cancelled.")
            continue


        try:
            remove_hotel(hotel.hotel_id)
            #Inputs wurden an den Manager weitergegeben

            print(f"Hotel '{hotel.name}' was deleted succesfully.")
            #Info, dass alles funktioniert hat

            input(f"\nPress Enter to finish")
            valid = True

        except Exception as e:
            print(f"Deleting didnt work: {e}")
            #Es wird mitgeteilt, dass der Löschvorgang fehlgeschlagen ist.
            input(f"\nPress Enter to finish")
            valid = True

if __name__ == "__main__":
    main()