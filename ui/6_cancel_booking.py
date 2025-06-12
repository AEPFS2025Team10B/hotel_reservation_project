
from business_logic import invoice_manager
from business_logic import booking_manager

def main():
    print("Cancel Booking")
    print("")
    print("for Coach: do not cancel bookings 1-3, 5 "
          "the others are good to check 5_get_invoice.py & 4_book_a_room.py")
    print("")
    booking_id = int(input("Please enter the booking id you would like to cancel: "))
    cancelled_booking = booking_manager.cancel_booking_by_id(booking_id)
    print("you have successfully canceled this booking")