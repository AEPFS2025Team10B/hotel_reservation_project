"""
User Story 2.2: Ich möchte nur die verfügbaren Zimmer sehen, sofern
ich meinen Aufenthalt (von – bis) spezifiziert habe.
"""

import sys
import os
from datetime import datetime
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.room_manager import get_available_rooms_by_hotel_and_dates

DATE_FORMAT = "%Y-%m-%d"
#legt das Datumsformat fest

def ask_date(prompt: str) -> str:
    pattern = r"^\d{4}[-./]\d{2}[-./]\d{2}$"
    while True:
        s = input(prompt).strip()
        if not re.match(pattern, s):
            print("Please enter a date in the format: YYYY-MM-DD, YYYY.MM.DD or YYYY/MM/DD.")
            #Kunde wird darauf hingewiesen, dass er das falsche Datumsformat benutzt hat.
            continue
            #while-loop wird fortgesetzt
        try:
            parts = re.split(r"[-./]", s)
            date_obj = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
            return date_obj.strftime("%Y-%m-%d")
            #Da wir ein gültiges Datum erhalten haben, wird das while-loop beendet
        except ValueError:
            print("Invalid date. Please enter a valid date.")
            #Kunde wird darauf hingewiesen, dass er ein ungültiges Datum eingegeben hat.

def main():
    valid = False
    while not valid:
        choice = input("for coach: Do you want to check when no hotels are available (y/n)?")
        if choice.lower() == "y":
            print("enter as check-in: 2025-10-28 an check-out: 2025-10-31")
            valid = True
        elif choice.lower() == "n":
            valid = True
        else:
            print("Please enter either 'y' or 'n'.")
        # das ganze loop ist dafür da um dem coach zu helfen, den Code auf funktionalität zu prüfen

    check_in = ask_date("Check-in (YYYY-MM-DD, . or / also allowed): ")

    while True:
        check_out = ask_date("Check-out (YYYY-MM-DD, . or / also allowed): ")
        if check_out <= check_in:
            #es wird geprüft, ob die Daten in der richtigen Reihenfolge geschrieben wurden.
            # Das, dass Check-in date auch wirklich kleiner als das Check-out ist.
            print("Check-out date must be after check-in date.")
            #Wenn das Check-out Datum kleiner als das Check-in datum ist, wird oberes statement ausgegeben.
        else:
            break

    hotels = find_all_hotel_details()
    print(f"\nAvailable room from {check_in} to {check_out} in all hotels:")
    any_available = False
    #Zuerst wird gesagt, dass es nichts zur Verfügung hat, danach wird es geprüft und entsprechend angepasst.

    for hotel in hotels:
        rooms = get_available_rooms_by_hotel_and_dates(hotel.hotel_id, check_in, check_out)
        if rooms:
            any_available = True
            #wenn freie Zimmer gefunden wurde, wird any_available auf True gesetzt

            print(f"\n{hotel.name} Address: {hotel.address.street}, {hotel.address.city}, {hotel.address.zip_code}:")
            for room in rooms:

                output = f"  Room {room.number}: {room.price_per_night} CHF, Type: {room.roomtype.description}, Max Guests: {room.roomtype.max_guests}\n"
                #der Output wird jetzt festgelegt.

                if room.facilities:
                    for facility in room.facilities:
                        output += f"    - Facility: {facility.name}\n"

                    print(output)
                    #der Output wird ausgegeben

    if not any_available:
        print("No available rooms, in all the hotels in this time period.")
        #der Kunde wird, darüber informiert, dass es in diesem Zeitrahmen keine freien Zimmer hat.

    input(f"\nPress Enter to finish")

if __name__ == "__main__":
    main()

