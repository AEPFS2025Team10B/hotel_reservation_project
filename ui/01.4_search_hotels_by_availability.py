"""
User Story 1.4: Ich möchte Hotels sehen, die während meines Aufenthalts verfügbar sind (Check-in- und Check-out-Datum).
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_hotels_by_availability

def main():
    print(" Hotel Search by Availability")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ").strip()
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ").strip()

    hotels = find_hotels_by_availability(check_in_date, check_out_date)

    if hotels:
        print(f"\nAvailable hotels from {check_in_date} to {check_out_date}:\n")
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★), {hotel.street}, {hotel.city}")
    else:
        print(f"\nNo hotels available in that period.")