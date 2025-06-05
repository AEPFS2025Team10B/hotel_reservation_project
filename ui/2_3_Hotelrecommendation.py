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
        print(f"Guest: {booking.guest.first_name} {booking.guest.last_name}")
        print(f"Total Amount: {booking.total_amount}")

        correcht = input("Is this youre booking? (Y/N)")

        if correcht.lower() == "y":
            valid = True
        elif correcht.lower() == "n":
            print("Alright, the process has been canceled.")
            return


    ask_booking_id()


if __name__ == "__main__":
    #print(os.getcwd())
    #ask_booking_id()
    main()