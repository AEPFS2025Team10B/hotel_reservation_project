"""
3. Als Gast möchte ich nach meinem Aufenthalt Hotelbewertungen abgeben
"""
#Ziel ist es, dass der User die Buchungs ID eingeben muss, diese dann zuerst abgeglichen wir,
# ob sie überhaupt existiert.
# Danach kann der User seine Bewertung abgeben und es wird gespeichert.

import sys
import os
from datetime import datetime


from data_access.booking_data_access import BookingDataAccess
from business_logic.booking_manager import find_booking_by_id, add_new_hotelrecommendation


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def ask_booking_id():
    valid = False
    while not valid:
        user_input = int(input("Please enter your booking id: "))
        correct_booking_id = find_booking_by_id(user_input)


ask_booking_id()