from datetime import date
class Booking:
    def __init__(self, booking_id:int, check_in_date:date, check_out_date:date, number_of_guests:int):
        self.booking_id = booking_id
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.number_of_guests = number_of_guests
        self.is_cancelled = False
        self.total_price = 0