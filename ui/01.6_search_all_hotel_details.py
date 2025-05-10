"""
User Story 1.6: Ich möchte Name, Adresse und Anzahl der Sterne jedes Hotels sehen.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details

def main():
    print("All Hotels")
    hotels = find_all_hotel_details()
    for index, hotel in enumerate(hotels, start=1):
        print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.street}, {hotel.city}")
    if hotels:
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.street}, {hotel.city}")
    else:
        print("No hotels found.")