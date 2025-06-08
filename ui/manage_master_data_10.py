# ui/manage_master_data_10.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import room_manager


# Funktion zur Auswahl eines Zimmers und Preisänderung
def choose_room_and_update_price():
    rooms = room_manager.get_all_rooms_with_facilities()
    print("\nAvailable Rooms:")
    for idx, room in enumerate(rooms, start=1):
        print(f"{idx}. Hotel: {room['hotel_name']} | Room: {room['room_number']} | "
              f"Type: {room['room_type']} | Price: CHF {room['price_per_night']:.2f}")
    try:
        choice = int(input("Select room to update: ")) - 1
        selected_room = rooms[choice]
        new_price = float(input("Enter new price per night (e.g., 120.00): "))
        room_manager.update_room_price(selected_room["room_id"], new_price)
        print(f"✅ Updated Room {selected_room['room_number']} to CHF {new_price:.2f}")
    except (IndexError, ValueError):
        print("❌ Invalid selection or input.")


# Funktion zur Auswahl eines Raumtyps und Aktualisierung von max. Gästen und Beschreibung
def choose_room_type_and_update():
    room_types = room_manager.get_all_room_types()
    print("\nRoom Types:")
    for idx, rt in enumerate(room_types, start=1):
        print(f"{idx}. ID: {rt.room_type_id} | Description: {rt.description} | Max Guests: {rt.max_guests}")
    try:
        choice = int(input("Select room type to update: ")) - 1
        selected = room_types[choice]
        max_guests = int(input("Enter new max guests: "))
        description = input("Enter new description: ")
        room_manager.update_room_type(selected.type_id, max_guests, description)
        print(f"✅ Room type '{selected.description}' updated.")
    except (IndexError, ValueError):
        print("❌ Invalid selection or input.")


# Funktion zur Auswahl einer Einrichtung und Aktualisierung des Namens
def choose_facility_and_update():
    facilities = room_manager.get_all_facilities()
    print("\nFacilities:")
    for idx, f in enumerate(facilities, start=1):
        print(f"{idx}. ID: {f.facility_id} | Name: {f.name}")
    try:
        choice = int(input("Select facility to update: ")) - 1
        selected = facilities[choice]
        new_name = input("Enter new facility name: ")
        room_manager.update_facility(selected.facility_id, new_name)
        print(f"✅ Facility '{selected.name}' renamed to '{new_name}'.")
    except (IndexError, ValueError):
        print("❌ Invalid selection or input.")


# Funktion zur Anzeige aller Raumtypen
def list_room_types():
    print("\nAll Room Types:")
    for rt in room_manager.get_all_room_types():
        print(f"ID: {rt.room_type_id} | Description: {rt.description} | Max Guests: {rt.max_guests}")


# Funktion zur Anzeige aller Einrichtungen
def list_facilities():
    print("\nAll Facilities:")
    for fac in room_manager.get_all_facilities():
        print(f"ID: {fac.facility_id} | Name: {fac.name}")


# Hauptmenü für die Verwaltung der Stammdaten
def main():
    print("\n🛠️  Master Data Management (User Story 10) 🛠️")
    print("1. Update room price")
    print("2. Update room type")
    print("3. Update facility")
    print("4. List all room types")
    print("5. List all facilities")
    print("0. Exit")

    choice = input("Your choice: ")

    if choice == "1":
        choose_room_and_update_price()
    elif choice == "2":
        choose_room_type_and_update()
    elif choice == "3":
        choose_facility_and_update()
    elif choice == "4":
        list_room_types()
    elif choice == "5":
        list_facilities()
    elif choice == "0":
        print("👋 Back to main menu.")
    else:
        print("❌ Invalid input.")


if __name__ == "__main__":
    main()