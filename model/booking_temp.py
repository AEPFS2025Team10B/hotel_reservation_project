from datetime import date
class Booking:
    def __init__(self, booking_id:int, check_in_date:date, check_out_date:date, number_of_guests:int):
        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__number_of_guests = number_of_guests
        self.__is_cancelled = False
        self.__total_price = 0

    def __repr__(self):
        return f"Booking(id={self.__booking_id!r}, check_in_date={self.__check_in_date!r}, check_out_date={self.__check_out_date!r}, number_of_guests={self.__number_of_guests!r}, is_cancelled{self.__is_cancelled!r}, total_price={self.total_price!r})"


    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, check_in_date):
        pass

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, check_out_date):
        pass

    @property
    def number_of_guests(self):
        return self.__number_of_guests

    @number_of_guests.setter
    def number_of_guests(self, number_of_guests):
        pass

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, is_cancelled):
        pass

    @property
    def total_price(self):
        return self.__total_price
    @total_price.setter
    def total_price(self, total_price):
        pass