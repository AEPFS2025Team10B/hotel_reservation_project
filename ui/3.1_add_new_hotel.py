"""
User Story 3.1: Als Admin möchte ich neue Hotels zum System hinzufügen.
"""

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import add_new_hotel

def main():
    print("=== Neues Hotel hinzufügen ===")

    # 1) Hotel-Grunddaten
    name = input("Name des Hotels: ").strip()
    if not name:
        print("Name darf nicht leer sein.")
        return

    try:
        stars = int(input("Anzahl Sterne (1–5): ").strip())
        if not (1 <= stars <= 5):
            raise ValueError()
    except ValueError:
        print("Ungültige Sterne-Eingabe. Bitte eine ganze Zahl zwischen 1 und 5.")
        return

    # 2) Adresse in einem Block abfragen
    print("\nAdresse des Hotels:")
    street   = input("  Strasse: ").strip()
    city     = input("  Stadt:   ").strip()
    zip_code = input("  PLZ:     ").strip()

    if not street or not city or not zip_code:
        print("Straße, Stadt und PLZ sind erforderlich.")
        return

    # 3) Anlegen und Bestätigung
    try:
        new_hotel = add_new_hotel(name, stars, street, city, zip_code)
    except Exception as e:
        print(f"Fehler beim Anlegen: {e}")
        return

    print("\n Hotel erfolgreich hinzugefügt:")
    print(f"  – {new_hotel.name} ({new_hotel.stars}★)")
    addr = new_hotel.address
    print(f"  – Adresse: {addr.street}, {addr.city} {addr.zip_code}")

if __name__ == "__main__":
    main()