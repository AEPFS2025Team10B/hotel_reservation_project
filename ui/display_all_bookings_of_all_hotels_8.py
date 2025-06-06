"""
User Story 8.0: Als Admin des Buchungssystems möchte ich alle Buchungen aller Hotels sehen können,
um eine Übersicht zu erhalten.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from business_logic import booking_manager

def main():
    print("\nAlle Buchungen aller Hotels:")
    print("-----------------------------")

    bookings = booking_manager.get_all_bookings_with_details()

    if not bookings:
        print("Keine Buchungen gefunden.")
        return

    for booking in bookings:
        print(f"Buchungsnummer: {booking['Buchungsnummer']}")
        print(f"Hotel: {booking['Hotelname']}")
        print(f"Gast: {booking['Gastname']}")
        print(f"Zimmer: {booking['Zimmernummer']}")
        print(f"Check-In: {booking['CheckInDatum']}")
        print(f"Check-Out: {booking['CheckOutDatum']}")
        print("-" * 30)

if __name__ == "__main__":
    main()