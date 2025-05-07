"""
User Story 1.2: Hotels nach Mindestanzahl Sterne filtern
As a guest, I want to filter hotels in a city by minimum star rating.
"""

import sys
import os
# Tell Python to look in the parent folder for business_logic and data_access
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the correct function
from business_logic.hotel_service import find_hotels_by_city_and_min_stars

def main():
    print("🏨 Hotel Search by City with Minimum Stars")
    city = input("Enter city: ").strip()
    min_stars = int(input("Enter minimum stars: "))

    hotels = find_hotels_by_city_and_min_stars(city, min_stars)

    if hotels:
        print(f"\nFound hotels in {city} with at least {min_stars} stars:")
        for index, (hotel_id, name, hotel_stars, city, street) in enumerate(hotels, start=1):
            print(f"{index}. {name} ({hotel_stars}★), {street}, {city}")

        try:
            selection = int(input("\nEnter the number of the hotel you'd like to view in more detail: "))
            if 1 <= selection <= len(hotels):
                selected = hotels[selection - 1]
                print(f"\nYou selected:\n→ {selected[1]} ({selected[2]}★), {selected[4]}, {selected[3]}")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print(f"\nNo hotels found in {city} with at least {min_stars} stars.")