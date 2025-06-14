"""
User Story 1.4: Ich möchte Hotels sehen, die während meines Aufenthalts verfügbar sind (Check-in- und Check-out-Datum).
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_hotels_by_availability
from business_logic.hotel_manager import print_all_hotel_details
from common_code.find_hotel_by_list_city import find_hotel_by_list_city

def main():
    print(" Hotel Search by Availability")
    valid = False
    while not valid:
        choice = input("for coach: Do you want to check when no hotels are available (y/n)?")
        if choice.lower() == "y":
            print("enter as check-in: 2025-10-28 and check-out: 2025-10-31")
            valid = True
        elif choice.lower() == "n":
            valid = True
        else:
            print("Please enter either 'y' or 'n'.")
        #das ganze loop ist dafür da um dem coach zu helfen, den Code auf funktionalität zu prüfen

    check_in_date = input("Enter check-in date (YYYY-MM-DD): ").strip()
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ").strip()

    hotels = find_hotels_by_availability(check_in_date, check_out_date)

    if hotels:
        print(f"\nAvailable hotels from {check_in_date} to {check_out_date}:\n")
        print(print_all_hotel_details(hotels))
        selected = find_hotel_by_list_city(hotels)
        print(f"Hotel-ID for further processing: {selected.hotel_id}")
        input("Press enter to finish")

    else:
        print(f"\nNo hotels available in that period.")
        print("")
        input("Press enter to finish")

    return hotels, check_in_date, check_out_date