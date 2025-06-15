#Ähnlich wie 1.1 geht, kann hier der Kunde eine Stadt eingaben und alle Hotels in der Stadt werden angezeigt.
#ZUsätzlich kann der Kunde hier aber noch die Mindestanzahl Sterne filtern.

"""
User Story 1.2: Hotels nach Mindestanzahl Sterne filtern
"""

from business_logic import print_all_hotel_details

# Tell Python to look in the parent folder for business_logic and data_access
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_hotels_by_city_and_min_stars

#sehr ähnlich wie 1.1, daher in find_hotels_by_list_city aufgebaut, und hier diversifiziert.
from common_code.find_hotel_by_list_city import find_hotel_by_list_city

def main():
    print(" Hotel Search by City with Minimum Stars")
    print("for Coach: Enter Zürich or Aarau (no hotel)")

    city = input("Enter city: ").strip()
    min_stars = int(input("Enter minimum stars: "))

    hotels = find_hotels_by_city_and_min_stars(city, min_stars)

    if hotels:
        print(f"\nFound hotels in {city} with at least {min_stars} stars:")
        print("\nAvailable hotels:")
        print(print_all_hotel_details(hotels))
        #Alle hotels werden ausgegeben

        selected = find_hotel_by_list_city(hotels)
        print(f"Hotel-ID for further processing: {selected.hotel_id}")
        # die Hotel ID wir für den Kunden ausgegeben. So kann er eitere Informationen einfacher beschaffen.

        input("Press enter to finish")

    else:
        print(f"\nNo hotels found in {city} with at least {min_stars} stars.")
        input("Press enter to finish")
    return hotels

#Was könnte man besser machen: Es wäre noch gut, dass wenn man eine Stadt eingibt,
# es in dieser Stadt aber kein Hotel hat, bereits unterbrochen wird. Jetzt weis man
# nicht, ob es an der Stadt oder an den sternen liegt.
# Wie: Zuerst prüfen gibt es in der Stadt überhaupt Hotels und nur wenn ja, nach
# der mindestanzahl Sternen fragen