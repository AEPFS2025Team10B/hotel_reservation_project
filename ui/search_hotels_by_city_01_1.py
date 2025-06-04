#Bei search_hotels_by_city geht es darum, dass der User nur eine Stadt eingeben kann,
# und dann alle Hotels findet, die es in dieser Stadt gibt.

"""
User Story 1.1
Stadtbasierte Hotelsuche
"""
#Import function
from business_logic.hotel_manager import find_hotels_by_city

#sehr ähnlich wie 1.2, daher in find_hotels_by_list_city aufgebaut, und hier diversifiziert.
from common_ui.find_hotel_by_list_city import find_hotel_by_list_city

def main():
    print(" Hotel Search by City")
    city = input("Enter a city: ").strip()
    hotels = find_hotels_by_city(city)

    if hotels:
        print(f"\nFound hotels in {city}:")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.address}")

        selected = find_hotel_by_list_city(hotels)
        print(f"Hotel-ID for further processing: {selected.hotel_id}")

    else:
        print(f"\nNo hotels found in {city}.")
    return hotels
