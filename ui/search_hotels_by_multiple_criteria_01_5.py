"""
User Story 1.5: Ich möchte Wünsche kombinieren können (z.B. Gästezahl, Sterne, Verfügbarkeit).).
"""
from model.hotel import Hotel
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_hotels_by_multiple_criteria

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
            check_in_date = input("Enter your check-in Date in the Format: YYYY-MM-DD: ")
            check_out_date = input("Enter your check-out Date in the Format: YYYY-MM-DD: ")
            valid = True
        except ValueError:
            print("Please enter a valid date in the format: YYYY-MM-DD")
            return

    hotels = find_hotels_by_multiple_criteria(city, min_stars, guest_count, check_in_date, check_out_date)

    if hotels:
        print(f"\nThese hotels are available for you:\n")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), Address: {hotel.address.street}, {hotel.address.zip_code}, {hotel.address.city}")
        input("\nPress Enter to finish")
    else:
        print(f"\nNo hotels available:\n")
        input("Press Enter to finish")

    return hotels, check_in_date, check_out_date

