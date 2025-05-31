"""
User Story 1.2: Hotels nach Mindestanzahl Sterne filtern
"""

import sys
import os
# Tell Python to look in the parent folder for business_logic and data_access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the correct function
from business_logic.hotel_manager import find_hotels_by_city_and_min_stars
from common_ui.find_hotel_by_list_city import find_hotel_by_list_city

def main():
    print(" Hotel Search by City with Minimum Stars")
    city = input("Enter city: ").strip()
    min_stars = int(input("Enter minimum stars: "))

    hotels = find_hotels_by_city_and_min_stars(city, min_stars)

    if hotels:
        print(f"\nFound hotels in {city} with at least {min_stars} stars:")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")

        selected = find_hotel_by_list_city(hotels)
        print(f"Hotel-ID for further processing: {selected.hotel_id}")


    else:
        print(f"\nNo hotels found in {city} with at least {min_stars} stars.")