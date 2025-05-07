"""
User Story 1.1
Stadtbasierte Hotelsuche
"""
#Import function
from business_logic.hotel_service import find_hotels_by_city

def main():
    print(" Hotel Search by City")
    city = input("Enter a city: ").strip()
    hotels = find_hotels_by_city(city)

    if hotels:
        print(f"\nFound hotels in {city}:")
        for index, (hotel_id, name, stars, city, street) in enumerate(hotels, start=1):
            print(f"{index}. {name} ({stars}★), {street}, {city}")

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
        print(f"\nNo hotels found in {city}.")