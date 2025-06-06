"""
User Story 3.1: Als Admin möchte ich neue Hotels zum System hinzufügen.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import add_new_hotel

def main():
    print("=== Add a new hotel ===")

    # 1) Hotel-Grunddaten
    name = input("Name of the hotel: ").strip()
    if not name:
        print("Name can not be empty.")
        return

    try:
        stars = int(input("Number of stars (1–5): ").strip())
        if not (1 <= stars <= 5):
            raise ValueError()
    except ValueError:
        print("Invalid star input. Please enter a number from 1 to 5.")
        return

    # 2) Adresse in einem Block abfragen
    print("\nAddress of the hotel:")
    street   = input("  Street: ").strip()
    city     = input("  City:   ").strip()
    zip_code = input("  Zip:     ").strip()

    if not street or not city or not zip_code:
        print("street, city and zip are valid.")
        return

    # 3) Anlegen und Bestätigung
    try:
        new_hotel = add_new_hotel(name, stars, street, city, zip_code)
    except Exception as e:
        print(f"Error creating entry: {e}")
        return

    print("\n Hotel successfully created:")
    print(f"  – {new_hotel.name} ({new_hotel.stars}★)")
    addr = new_hotel.address
    print(f"  – address: {addr.street}, {addr.city} {addr.zip_code}")

if __name__ == "__main__":
    main()