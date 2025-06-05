"""
3. Als Gast möchte ich nach meinem Aufenthalt Hotelbewertungen abgeben
"""
#Ziel ist es, dass der User die Buchungs ID eingeben muss, diese dann zuerst abgeglichen wir,
# ob sie überhaupt existiert.
# Danach kann der User seine Bewertung abgeben und es wird gespeichert.

import sys
import os
from datetime import datetime

os.environ["DB_FILE"] = "database/test_hotel_reservation_sample.db"
from business_logic.booking_manager import find_booking_by_id, add_new_hotelrecommendation


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
def main():
    print("\n=== Hotel Recommendation System ===")
    print("Please provide your feedback for your stay.")
    ask_booking_id()

def ask_booking_id():
    valid = False
    while not valid:
        user_input = int(input("Please enter your booking id: "))
        booking = find_booking_by_id(user_input)
        
        if booking is None:
            print("No booking found with this ID. Please try again.")
            continue
            
        print("\nBooking Details:")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Check-in Date: {booking.check_in_date}")
        print(f"Check-out Date: {booking.check_out_date}")
        print(f"Room: {booking.room.number}")
        #print(f"Guest: {booking.guest.first_name} {booking.guest.last_name}")
        #print(f"Total Amount: {booking.total_amount}")

        correct = input("Is this your booking? (Y/N): ")
        if correct.lower() == "y":
            ask_hotelrecommendation(booking)
        elif correct.lower() == "n":
            print("Alright, the process has been canceled.")
            input("Press Enter to Exit")
            quit()

def ask_hotelrecommendation(booking):
    valid = False
    while not valid:
        try:
            rating = int(input("\nPlease enter your rating (1-10): "))
            if 1 <= rating <= 10:
                valid = True
            else:
                print("Invalid input please enter 1 to 10.")
        except ValueError:
            print("Invalid input please enter 1 to 10.")

    valid = False
    while not valid:
        try:
            recommendation = input("\nPlease enter your recommendation(not mandatory): ")
            if recommendation == "" or len(recommendation) <= 500:
                valid = True
            else:
                print("The recommendation can not be longer than 500 characters")
        except Exception as e:
            print(f"Unexpected error: {e}")

    valid = False
    while not valid:
        try:
            add_new_hotelrecommendation(booking.booking_id, rating, recommendation)
            print("Thank you for your feedback!")
            valid = True

        except ValueError as e:
            print(f"Error saving your feedback: {e}")

if __name__ == "__main__":
    #print(os.getcwd())
    #ask_booking_id()
    main()