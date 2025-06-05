"""
4. Als Gast möchte ich Hotelbewertungen vor der Buchung lesen
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic.hotel_manager import find_all_hotel_details
from business_logic.booking_manager import get_reviews_by_hotel_name

def main():
    print("All Hotels")
    hotels = find_all_hotel_details()
    
    if hotels:
        for index, hotel in enumerate(hotels, start=1):
            print(f"{index}. {hotel.name} ({hotel.stars}★)")
        try:
            selection = int(input("\nPlease enter the number oft the hotel you want to see the recommendations of").strip())
            if 1 <= selection <= len(hotels):
                selected_hotel = hotels[selection - 1]
                print(f"\nRecommendation(s) for {selected_hotel.name}:")
                reviews = get_reviews_by_hotel_name(selected_hotel.name)
                if reviews:
                    for rating, recommendation, first_name, last_name in reviews:
                        print(f"- {rating}/10 von {first_name} {last_name}: '{recommendation}'")
                else:
                    print("There are no Recommendations for this Hotel.")
            else:
                print("Invalid Input. Please try again.")
        except ValueError:
            print("Pleas enter a valid number.")
    else:
        print("no hotels found.")

if __name__ == "__main__":
    main()
