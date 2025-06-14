import importlib.util
import os
import sys
from logo import print_logo

# Sicherstellen, dass das Hauptverzeichnis im Pfad ist, damit Imports funktionieren
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

UI_PATH = "ui"
SCRIPTS_PATH = "scripts"

def run_story(filename):
    # Check if file exists in ui directory first
    full_path = os.path.join(UI_PATH, filename)
    if not os.path.exists(full_path):
        # If not in ui, try scripts directory
        full_path = os.path.join(SCRIPTS_PATH, filename)
        if not os.path.exists(full_path):
            print(f"Error: File {filename} not found in {UI_PATH} or {SCRIPTS_PATH}")
            return

    spec = importlib.util.spec_from_file_location("module.name", full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "main"):
        module.main()
    else:
        print("No main() function found in", filename)


def main():
    print_logo()

    # User Stories thematisch unterteilt
    sections = [
        ("Hotelsuche", [
            (1, "search_hotels_by_city_01_1.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city)."),
            (2, "search_hotel_stars_01_2.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city) and minimum star count."),
            (3, "search_room_by_guest_count_01_3.py", "As a guest I want to search all hotels in a city that have room for all my guests."),
            (4, "search_hotels_by_availability_01_4.py", "As a guest I want to search all hotels which have available room for my desired stay time."),
            (5, "search_hotels_by_multiple_criteria_01_5.py", "As a guest I want to search hotels by multiple criteria (location, stars, guests, dates)."),
        ]),
        ("Hoteldetails & Zimmerwahl", [
            (6, "search_all_hotel_details_01_6.py", "As a guest I want to see hotel details (name, address, stars)."),
            (7, "2_1_search_room_type_by_hotel.py", "As a guest, I want to see all Room Types of a Hotel"),
            (8, "2_2_search_room_by_date.py", "As a guest, I want to find unoccupied rooms during my travelling time"),
        ]),
        ("Buchung & Nachbetreuung", [
            (12, "4_book_a_room.py", "As a customer I want to book a room"),
            (13, "5_get_invoice.py", "As a customer I want to get invoice"),
            (14, "6_cancel_booking.py", "As a customer I want to cancel booking"),
            (15, "7_price_seasons.py", "As a customer I want to see the price depending on seasons"),
        ]),
        ("Hotelverwaltung (Admin)", [
            (9, "3_1_add_new_hotel.py", "As an admin, i want to be able to add new hotels"),
            (10, "3_2_remove_hotel.py", "As an admin, i want to delte a hotel"),
            (11, "3_3_update_hotel.py", "As an admin, i want to update the details of a hotel"),
            (18, "manage_master_data_10.py", "Als Admin möchte ich Stammdaten anpassen können."),
        ]),
        ("Reporting & Übersicht (Admin)", [
            (16, "display_all_bookings_of_all_hotels_8.py", "As an Admin, I want to see all Bookings of all Hotels"),
            (17, "display_all_rooms_with_facilities_9.py", "Als Admin möchte ich eine Liste der Zimmer mit ihrer Ausstattung sehen."),
        ]),
        ("Empfehlungen & Bewertungen", [
            (19, "2_3_Hotelrecommendation.py", "As a guest I want to leave a recommendation after my stay"),
            (20, "2_4_look_up_hotelrecommendation.py", "As a guest I want to read hotel reviews before booking"),
        ]),
        ("Datenvisualisierung", [
            (21, "data_visualization_2.py", "As an Admin, I want to see a breakdown of guest demographics (e.g., age range, nationality, returning guests)."),
        ]),
        ("Datenbank Verwaltung", [
            (100, "add_example_data.py", "Reset data back to original"),
            #genau genommen, wird die Datenbank komplett gelöscht und dann wieder eingefügt
        ]),
    ]

    # Sektionen anzeigen
    for title, items in sections:
        border = "=" * 40
        print(f"\n{border}")
        print(f"|{title.center(38)}|")
        print(border)
        for idx, fname, desc in items:
            print(f"{idx}. {fname}\n   → {desc}\n")

    # Eingabe und Ausführung
    all_stories = [item for sect in sections for item in sect[1]]
    mapping = {i: fname for i, fname, _ in all_stories}

    try:
        choice = int(input("Enter number to run or 0 to run all: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 0:
        for _, fname, _ in all_stories:
            print(f"\n--- Running {fname} ---")
            run_story(fname)
    else:
        fname = mapping.get(choice)
        if fname:
            print(f"\n--- Running {fname} ---")
            run_story(fname)
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
