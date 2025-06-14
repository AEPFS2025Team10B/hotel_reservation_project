"""
User Story 1.5: Ich möchte Wünsche kombinieren können (z.B. Gästezahl, Sterne, Verfügbarkeit).).
"""
from model.hotel import Hotel
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_hotels_by_multiple_criteria
from common_code.find_hotel_by_list_city import find_hotel_by_list_city
from business_logic.hotel_manager import print_all_hotel_details

def main():
    print("Hotel Search by your availability")
    city = None
    min_stars = None
    guest_count = None
    check_in_date = None
    check_out_date = None

    valid = False
    while not valid:
        # while-loop, dass der User nicht immer von vorne beginnen muss, wenn er etwas Ungültiges eingibt,
        # jetzt kann er es einfach wieder eingeben.
        try:
            city = input("Enter a city: ").strip()
            min_stars = int(input("Enter minimum stars: "))
            guest_count = int(input("And how many people should have space in this room? "))
            coach = False
            while not coach:
                choice = input("for coach: Do you want to check when no hotels are available (y/n)?")
                if choice.lower() == "y":
                    print("enter as check-in: 2025-10-28 an check-out: 2025-10-31")
                    coach = True
                elif choice.lower() == "n":
                    coach = True
                else:
                    print("Please enter either 'y' or 'n'.")
                # das ganze loop ist dafür da um dem coach zu helfen, den Code auf funktionalität zu prüfen

            check_in_date = input("Enter your check-in Date in the Format: YYYY-MM-DD: ")
            check_out_date = input("Enter your check-out Date in the Format: YYYY-MM-DD: ")
            valid = True
        except ValueError:
            print("Please enter a valid date in the format: YYYY-MM-DD")
            return

    hotels = find_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)

    if hotels:
        print(f"\nAvailable hotels from {check_in_date} to {check_out_date}:\n")
        #Dem Kunden wird nochmals die Eingabe bestätigt

        print(print_all_hotel_details(hotels))
        selected = find_hotel_by_list_city(hotels)

        print(f"Hotel-ID for further processing: {selected.hotel_id}")
        # die Hotel ID wir für den Kunden ausgegeben. So kann er eitere Informationen einfacher beschaffen.
        input(f"\nPress enter to finish")

    else:
        print(f"\nNo hotels available:\n")
        #Dem Kunden wird mitgeteilt, das es keine verfügbaren Hotels hat.
        input(f"\nPress Enter to finish")

    return hotels, check_in_date, check_out_date

