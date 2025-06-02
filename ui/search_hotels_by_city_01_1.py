"""
User Story 1.1
Stadtbasierte Hotelsuche
"""
#Import function
from business_logic.hotel_manager import find_hotels_by_city
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
