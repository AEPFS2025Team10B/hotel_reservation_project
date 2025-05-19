# ui/3.3_update_hotel.py

"""
User Story 3.3: Ich möchte Hotel Infos updaten
"""

import sys
import os
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_all_hotel_details, update_hotel

def ask_date_int(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            val = int(input(prompt).strip())
            if min_val <= val <= max_val:
                return val
        except ValueError:
            pass
        print(f"Bitte eine ganze Zahl von {min_val} bis {max_val} eingeben.")

def main():
    print("__________________________")
    print("|- Update Hotel Details -|")
    print("__________________________")
    hotels = find_all_hotel_details()

    if not hotels:
        print("No Hotel found.")
        return

    # 1) Liste der Hotels anzeigen
    for idx, h in enumerate(hotels, start=1):
        print(f"{idx}. {h.name} ({h.stars}★), {h.address}")

    # 2) Hotel-Auswahl
    sel = ask_date_int("\nNumber of the Hotel you want to update: ", 1, len(hotels))
    hotel = hotels[sel - 1]

    # 3) Neue Werte abfragen
    print(f"\nUpdating '{hotel.name}':")
    new_name = input(f" New name [{hotel.name}]: ").strip() or hotel.name
    new_stars = ask_date_int(f" New stars (1–5) [{hotel.stars}]: ", 1, 5) or hotel.stars

    print("\n New address:")
    street   = input(f"  Street [{hotel.address.street}]: ").strip() or hotel.address.street
    city     = input(f"  City   [{hotel.address.city}]: ").strip() or hotel.address.city
    zip_code = input(f"  ZIP    [{hotel.address.zip_code}]: ").strip() or hotel.address.zip_code

    # 4) Update durchführen
    try:
        update_hotel(new_name, new_stars, street, city, zip_code, hotel.hotel_id)
        print(f"\nHotel '{hotel.name}' wurde erfolgreich aktualisiert.")
    except Exception as e:
        print(f"\nFehler beim Aktualisieren: {e}")

if __name__ == "__main__":
    main()