
from business_logic import invoice_manager
from business_logic import booking_manager

def main():
    print("Cancel Booking")
    booking_id = int(input("Please enter the booking id you would like to cancel: "))
    cancelled_booking = booking_manager.cancel_booking_by_id(booking_id)
    print("you have successfully canceled this booking")