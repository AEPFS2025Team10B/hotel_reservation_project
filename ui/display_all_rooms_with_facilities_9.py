# ui/display_all_rooms_with_facilities_9.py

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import room_manager

def main():
    print("\nAlle Zimmer mit Ausstattung:")
    print("----------------------------")

    rooms = room_manager.get_all_rooms_with_facilities()
    # alle Räume werden herausgesucht

    if not rooms:
        print("No rooms found.")
        # dem User wird mitgeteilt, dass keine Räume gefunden werden konnten
        input(f"\nPress Enter to finish")
        return

    for room in rooms:
        # Jeder Raum wir als eigener Block ausgegeben
        print(f"Hotel: {room['hotel_name']}")
        print(f"Zimmernummer: {room['room_number']}")
        print(f"Beschreibung: {room['room_type']}")
        print(f"Maximale Gäste: {room['max_guests']}")
        print(f"Preis pro Nacht: CHF {room['price_per_night']:.2f}")
        print(f"Ausstattung: {room['facilities']}")
        print("-" * 40)
    input(f"\nPress Enter to finish")

if __name__ == "__main__":
    main()
    