"""
User Story 1.3: Filter hotels in a city by room capacity (one room per booking).
As a guest, I want to search all hotels in a city that have a room for all my guests.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from business_logic.hotel_manager import find_hotels_by_guest_count
from business_logic.hotel_manager import print_all_hotel_details
from model.roomtype import RoomType
from business_logic.hotel_manager import create_detailed_hotel_list
from business_logic.hotel_manager import print_all_hotel_details
from common_code.find_hotel_by_list_city import find_hotel_by_list_city
def main():
    print("Hotel Search by Guest Count")

    guest_count = None
    valid = False
    while not valid:
    # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
    # jetzt kann er es einfach wieder eingeben.
        try:
            guest_count = int(input("How many people should have space in this room? "))
            if guest_count < 1:
            #Der input vom Kunden wird geprüft, ob die Zahl kleiner als 1 ist. Wenn ja, kommt die fehlermeldung zum Zug.
                raise ValueError
                #der Kunde wird darauf hingewiesen, dass er eine ungültige eingabe getätigt hat.

            valid = True
        except ValueError:
            print("Enter a valid number and number must be above 0")
            # der Kunde wird darauf hingewiesen, dass er eine ungültige eingabe getätigt hat.
            continue
            #while-loop wird fortgesetzt, da wir keine gültige eingabe erhalten haben

    hotels = find_hotels_by_guest_count(guest_count)

    if hotels:
        print(f"\nThese hotels have a room for at least {guest_count} guests:\n")
        print(print_all_hotel_details(hotels))
        selected = find_hotel_by_list_city(hotels)

        print(print_all_hotel_details(selected))
        #Die details für das Hotel seiner Wahl werden ausgegeben

        input(f"\nEnter to finish")
    else:
        print(f"\nNo hotels found with rooms for {guest_count} guests.")
        #Der Kunde wird informiert, dass wir keine Zimmer passend zu seiner Gästezahl erfasst haben.
        input(f"\nEnter to finish")
    return hotels