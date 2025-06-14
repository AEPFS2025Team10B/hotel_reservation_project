# find_hotels_by_list_city haben wir implementiert, da wir nicht wollten,
# dass sich unser code bei der user story 1.1 & 1.2 wiederholt.
# Bei uns haben nämlich beide zu einem grossem teil dasselbe UI.
from business_logic.hotel_manager import print_all_hotel_details
from business_logic.hotel_manager import create_detailed_hotel_list
from business_logic.hotel_manager import print_detailed_hotel_list

def find_hotel_by_list_city(hotels):
    while True:
        try:
            selection = int(input("\nEnter the number of the hotel you'd like to view in more detail: "))
            #der Kunde wird gefragt, von welchem Hotel er die Details sehen möchte
            if 1 <= selection <= len(hotels):
                selected = hotels[selection - 1]
                #Die eingabe vom Kunden wird auf ihre Gültigkeit geprüft

                detailed_hotels = create_detailed_hotel_list(selected)
                print("\nYou selected:")
                print(print_detailed_hotel_list(detailed_hotels))
                #Seine Wahl wird ausgegeben
                return selected
            else:
                print("Invalid selection.")
                #Dem Kunden wird mitgeteilt, dass seine Eingabe ungültig ist

        except ValueError:
            print("Please enter a valid number.")
