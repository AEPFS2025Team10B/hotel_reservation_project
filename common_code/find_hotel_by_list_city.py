# find_hotels_by_list_city haben wir implementiert, da wir nicht wollten,
# dass sich unser code bei der user story 1.1 & 1.2 wiederholt.
# Bei uns haben nämlich beide zu einem grossem teil dasselbe UI.
from business_logic.hotel_manager import print_all_hotel_details

def find_hotel_by_list_city(hotels):
    while True:
        try:
            selection = int(input("\nEnter the number of the hotel you'd like to view in more detail: "))
            if 1 <= selection <= len(hotels):
                selected = hotels[selection - 1]
                print("\nYou selected:")
                print(print_all_hotel_details(selected))
                return selected
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
