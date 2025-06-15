from business_logic import booking_manager

def main():
    print("Cancel Booking")
    print("")
    print(f"for Coach: do only cancel bookings 2-3, 5, you can enter 4 to see "
          "\nwhat happens if the booking is already been cancelled "
          "\nif you want to check other booking ids you have to reload the "
          "\ndatabank in the starting menu (with 100)\n")

    booking_id = int(input("Please enter the booking id you would like to cancel: "))
    #der Kunde muss die Buchungs-ID eingeben
    result = booking_manager.cancel_booking_by_id(booking_id)
    if isinstance(result, str):
        print(result)
    else:
        print("you have successfully canceled this booking")
        #dem Kunden wird bestätigt, das die Stornierung funktioniert hat.
    input(f"\nPress Enter to finish")