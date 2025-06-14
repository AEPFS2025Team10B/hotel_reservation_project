"""
User Story 1.6: Ich möchte Name, Adresse und Anzahl der Sterne jedes Hotels sehen.
"""

import sys
import os
import subprocess
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_available_rooms_by_hotel
from common_code.get_next_available_date_for_hotel import get_next_available_date_for_hotel
from common_code.find_hotel_by_list_city import find_hotel_by_list_city
from business_logic.hotel_manager import print_all_hotel_details

today = date.today().isoformat()


def main():
    print("All Hotels")
    hotels = find_all_hotel_details()

    if hotels:
        print(print_all_hotel_details(hotels))
        selected = find_hotel_by_list_city(hotels)
        print(f"Hotel-ID for further processing: {selected.hotel_id}")
        input("Press enter to finish")

        # Heute verfügbare Zimmer anzeigen
        available_rooms = get_available_rooms_by_hotel(selected.hotel_id, today)
        print("\nAvailable rooms today:")
        output = ""
        if available_rooms:
            for room in available_rooms:
                output = f"  Room {room.number}: {room.price_per_night} CHF, Type: {room.roomtype.description}, Max Guests: {room.roomtype.max_guests}\n"
                if room.facilities:
                    for facility in room.facilities:
                        output += f"    - Facility: {facility.name}\n"
            print(output)
            coach = False
            while not coach:
                choice = input(
                    "for Coach: Do you want to see what happens if there are currently no rooms available (y/n)?\n"
                    "the databank will get manipulated and you have to reload it again in the starting menu (with 100) ")
                if choice.lower() == "y":
                    # manipulate_data_for_01_6.py wird ausgeführt
                    script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts',
                                               'manipulate_data_for_01_6.py')
                    subprocess.run([sys.executable, script_path])
                    coach = True
                    # man hätte in der datenbank auch ein hotel einfach ausbuchen können, dann wäre aber das nächste frei
                    # Zimmer erst sehr spät angezeigt worden. Oder wir hätten es direkt so hinterlegt, dass sich das datum
                    # automatisch anpasst, dann hätten wir aber überschneidungen verschiedener Buchungen besonders, wenn
                    # wir im Oktober sind.
                elif choice.lower() == "n":
                    coach = True
                else:
                    print("Please enter either 'y' or 'n'.")
        else:
            print(" No available rooms today.")

            # Nächstes verfügbares Datum ermitteln
            next_date = get_next_available_date_for_hotel(selected.hotel_id)
            if next_date:
                print(f"\nNext available date for any room: {next_date}")
            else:
                print("No future availability found.")
                # sollte eigentlich nie kommen
    else:
        print("No hotels found.")

    print("")
    input("Press Enter to finish")
    return hotels


if __name__ == "__main__":
    main()

#was könnte man besser machen?:
#man könnte vielleicht bevor man ein hotel auswählt herausfiltern können,
# welche Hotels gerade keine Freien Zimmer haben.