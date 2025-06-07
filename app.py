""" Main App to run user stories one by one or all at once. """

import importlib.util
import os
import sys
from logo import print_logo
# Sicherstellen, dass das Hauptverzeichnis im Pfad ist, damit Imports funktionieren
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

UI_PATH = "ui"

def run_story(filename):
    full_path = os.path.join(UI_PATH, filename)
    spec = importlib.util.spec_from_file_location("module.name", full_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if hasattr(module, "main"):
        module.main()
    else:
        print("No main() function found in", filename)

def main():
    # User Story 1.1: Stadtbasierte Hotelsuche.
    # User Story 1.2: Hotels nach Mindestanzahl Sterne filtern.
    # User Story 1.3: Hotels mit Zimmern für bestimmte Gästezahl.
    # User Story 1.4: Hotels mit Verfügbarkeit im Zeitraum filtern.
    # User Story 1.5: Kombination von Wünschen (Sterne, Gästezahl, Zeitraum).
    # User Story 1.6: Anzeige von Hoteldetails (Name, Adresse, Sterne).
    # User Story 2.1: Anezige der Raumdetails (Facilities, Beschreibung etc.)
    # User Story 2.2: Ich möchte verfügbare Räume an gewissen Daten anzeigen lassen (Reisezeitraum)
    # User Story 3.1: Als Admin möchte ich ein neues Hotel hinzufügen können.
    # User Story 3.2: Als Admin möchte ich ein Hotel löschen können.
    # User Story 3.3: Als Admin möchte ich die Details eines Hotels ändern können.


    print_logo()
    stories = [
        (1, "search_hotels_by_city_01_1.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city)."),
        (2, "search_hotel_stars_01_2.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city) and minimum star count."),
        (3, "search_room_by_guest_count_01_3.py", "As a guest I want to search all hotels in a city that have room for all my guests."),
        (4, "search_hotels_by_availability_01_4.py", "As a guest I want to search all hotels which have available room for my desired stay time."),
        (5, "search_hotels_by_multiple_criteria_01_5.py", "As a guest I want to search hotels by multiple criteria (location, stars, guests, dates)."),
        (6, "search_all_hotel_details_01_6.py", "As a guest I want to see hotel details (name, address, stars)."),
        (7, "2_1_search_room_type_by_hotel.py", "As a guest, I want to see all Room Types of a Hotel"),
        (8, "2_2_search_room_by_date.py", "As a guest, I want to find unoccupied rooms during my travelling time"),
        (9, "3_1_add_new_hotel.py", "As an admin, i want to be able to add new hotels"),
        (10, "3_2_remove_hotel.py", "As an admin, i want to delte a hotel"),
        (11, "3_3_update_hotel.py", "As an admin, i want to update the details of a hotel"),
        (12, "4_book_a_room.py", "As a customer I want to book a room"),
        (13, "5_get_invoice.py", "As a customer I want to get invoice"),
        (14, "6_cancel_booking.py", "As a customer I want to cancel booking"),
        (17, "display_all_bookings_of_all_hotels_8.py", "As an Admin, I want to see all Bookings of all Hotels"),
        (20, "2_3_Hotelrecommendation.py", "3. As a guest I want to leave a recommendation after my stay"),
        (21, "2_4_look_up_hotelrecommendation.py", "4. As a guest I want to read hotel reviews before booking"),

        ]

    print("\nAvailable User Stories:")
    for idx, fname, doc in stories:
        print(f"{idx}. {fname}\n   → {doc}\n")

    try:
        choice = int(input("Enter number to run or 0 to run all: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 0:
        for _, fname, _ in stories:
            print(f"\n--- Running {fname} ---")
            run_story(fname)
    else:
        match = next((f for i, f, _ in stories if i == choice), None)
        if match:
            print(f"\n--- Running {match} ---")
            run_story(match)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
