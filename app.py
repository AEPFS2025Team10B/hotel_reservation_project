""" Main App to run user stories one by one or all at once. """

import importlib.util
import os

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
    # User Story 1.1: Stadtbasierte Hotelsuche
    # User Story 1.2: Hotels nach Mindestanzahl Sterne filtern
    # User Story 1.3: Hotels nach Gästezahl filtern
    # User Story 1.4: Hotels mit Verfügbarkeit im Zeitraum filtern
    # User Story 1.5: Kombination von Wünschen (Sterne, Gästezahl, Zeitraum)
    # User Story 1.6: Anzeige von Hoteldetails (Name, Adresse, Sterne)

    stories = [
        (1, "01.1_search_hotels_by_city_ui.py", "As a guest, I want to browse all hotels in a city so that I can choose one based on location (city)."),
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