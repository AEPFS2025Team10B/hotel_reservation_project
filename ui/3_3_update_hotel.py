# ui/3_3_update_hotel.py

"""
User Story 3.3: Ich möchte Hotel Infos updaten
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_all_hotel_details, update_hotel
from business_logic.hotel_manager import print_all_hotel_details

def ask_date_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
        # jetzt kann er es einfach wieder eingeben.
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
        except ValueError:
            pass
        print(f"Please enter a natural number between {min_val} to {max_val}.")

def main():
    print("__________________________")
    print("|- Update Hotel Details -|")
    print("__________________________")
    hotels = find_all_hotel_details()

    if not hotels:
        print("No Hotel found.")
        input(f"\nPress Enter to finish")
        #falls kein Hotel gefunden wird
        return

    # 1) Liste der Hotels anzeigen
    if hotels:
        print(print_all_hotel_details(hotels))

    # 2) Hotel-Auswahl
    sel = ask_date_int("\nNumber of the Hotel you want to update: ", 1, len(hotels))
    hotel = hotels[sel - 1]

    # 3) Neue Werte abfragen
    print(f"\nUpdating '{hotel.name}':")
    new_name = input(f" New name [{hotel.name}]: ").strip() or hotel.name
    #der Neue Name wird erfasst (falls lehr, wird der alte übernommen)

    stars_input = input(f" New stars (1–5) [{hotel.stars}]: ").strip()
    #die neue Anzahl Sterne werden abgefragt
    if stars_input:
        new_stars = int(stars_input)
        #die Sternenzahl wird in einen Integer umgewandelt
    else:
        new_stars = ask_date_int(f" New stars (1–5) [{hotel.stars}]: ", 1, 5)

    print("\n New address:")
    street   = input(f"  Street [{hotel.address.street}]: ").strip() or hotel.address.street
    city     = input(f"  City   [{hotel.address.city}]: ").strip() or hotel.address.city
    zip_code = input(f"  ZIP    [{hotel.address.zip_code}]: ").strip() or hotel.address.zip_code
    #die Neue Adresse wird als Block abgefragt (falls lehr, wird der alte übernommen)

    # 4) Update durchführen
    try:
        update_hotel(new_name, new_stars, street, city, zip_code, hotel.hotel_id)
        print(f"\nHotel '{hotel.name}' got successfully updated.")
    except Exception as e:
        print(f"\nError updating: {e}")

    input(f"\nPress Enter to finish")
if __name__ == "__main__":
    main()