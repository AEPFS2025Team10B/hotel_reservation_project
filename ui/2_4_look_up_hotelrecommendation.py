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
            selection = int(input("\nPlease enter the number of the hotel you want to see the recommendations of: ").strip())
            if 1 <= selection <= len(hotels):
                selected_hotel = hotels[selection - 1]
                print(f"\nRecommendation(s) for {selected_hotel.name}:")
                reviews = get_reviews_by_hotel_name(selected_hotel.name)
                if reviews:
                    # Mittelwert berechnen
                    ratings = [r[0] for r in reviews if r[0] is not None]
                    if ratings:
                        avg_rating = round(sum(ratings) / len(ratings), 1)
                        print(f"Average Rating: {avg_rating}/10\n")
                    else:
                        print("no recommendation jet, for this hotel.\n")
                    # Einzelne Reviews ausgeben
                    for rating, recommendation, first_name, last_name in reviews:
                        rec_text = '' if not recommendation or str(recommendation).lower() == 'none' else recommendation
                        print(f"- {rating}/10 from {first_name} {last_name}: '{rec_text}'")
                else:
                    print("There are no recommendations for this Hotel.")
            else:
                print("Invalid Input. Please try again.")
        except ValueError:
            print("Pleas enter a valid number.")
    else:
        print("no hotels found.")

if __name__ == "__main__":
    main()
