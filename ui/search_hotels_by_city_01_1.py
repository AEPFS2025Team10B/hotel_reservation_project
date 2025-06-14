#Bei search_hotels_by_city geht es darum, dass der User nur eine Stadt eingeben kann,
# und dann alle Hotels findet, die es in dieser Stadt gibt.

"""
User Story 1.1
Stadtbasierte Hotelsuche
"""
#Import function
from business_logic.hotel_manager import find_hotels_by_city
from business_logic.hotel_manager import print_all_hotel_details

#sehr ähnlich wie 1.2, daher in find_hotels_by_list_city aufgebaut, und hier diversifiziert.
from common_code.find_hotel_by_list_city import find_hotel_by_list_city

def main():
    print(" Hotel Search by City")
    print(f"\nfor Coach: Enter Zürich or Aarau (no hotel)\n")
    city = input("Enter a city: ").strip()
    hotels = find_hotels_by_city(city)

    if hotels:
        print("\nAvailable hotels:")
        print(print_all_hotel_details(hotels))
        #alle verfügbaren Hotels werden ausgegeben

        selected = find_hotel_by_list_city(hotels)

        print(f"Hotel-ID for further processing: {selected.hotel_id}")
        #die Hotel ID wir für den Kunden ausgegeben. So kann er eitere Informationen einfacher beschaffen.
        input(f"\nPress enter to finish")
    else:
        print(f"\nNo hotels found in {city}.")
        #Der Kunde wird informiert, dass es in dieser Stadt keine erfassten Hotels gibt.

        input(f"\nPress enter to finish")
    return hotels
