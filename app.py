""" Main App to run user stories one by one or all at once. """

import importlib.util
import os
import sys

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

    stories = [
        (1, "01.1_search_hotels_by_city_ui.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city)."),
        (2, "01.2_search_hotel_stars.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city) and minimum star count."),
        (3, "01.3_search_room_by_guest_count.py", "As a guest I want to search all hotels in a city that have room for all my guests."),
        (4, "01.4_search_hotels_by_availability.py", "As a guest I want to search all hotels which have available room for my desired stay time."),
        (5, "01.5_search_hotels_by_multiple_criteria.py", "As a guest I want to search hotels by multiple criteria (location, stars, guests, dates)."),
        (6, "01.6_search_all_hotel_details.py", "As a guest I want to see hotel details (name, address, stars)."),
        (7, "2.1_search_room_type_by_hotel.py", "As A guest, I want to see all Room Types of a Hotel")
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
