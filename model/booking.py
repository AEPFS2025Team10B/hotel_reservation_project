from datetime import date

class Booking:
    def __init__(self, booking_id: int, check_in_date: date, check_out_date: date):
        self.__booking_id = booking_id
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__is_cancelled = False
        self.__total_price = 0.0
        self.__guest = None
        self.__room = None
        self.__invoice = None
        self.__rating = None
        self.__recommendation = None

    def __repr__(self):
        return (f"Booking(id={self.__booking_id!r}, check_in={self.__check_in_date!r}, "
                f"check_out={self.__check_out_date!r}, guests={self.__number_of_guests!r}, "
                f"cancelled={self.__is_cancelled!r}, price={self.__total_price!r})")

    @property
    def booking_id(self):
        return self.__booking_id

    @property
    def check_in_date(self):
        return self.__check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        if not isinstance(value, date):
            raise TypeError("check_in_date must be a date")
        self.__check_in_date = value

    @property
    def check_out_date(self):
        return self.__check_out_date

    @check_out_date.setter
    def check_out_date(self, value):
        if not isinstance(value, date):
            raise TypeError("check_out_date must be a date")
        self.__check_out_date = value

    @property
    def is_cancelled(self):
        return self.__is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value):
        if not isinstance(value, bool):
            raise TypeError("is_cancelled must be a boolean")
        self.__is_cancelled = value

    @property
    def total_price(self):
        return self.__total_price

    @total_price.setter
    def total_price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("total_price must be a non-negative number")
        self.__total_price = value

    @property
    def guest(self):
        return self.__guest

    @guest.setter
    def guest(self, value):
        from.guest import Guest
        if not isinstance(value, Guest):
            raise TypeError("guest must be a Guest object")
        self.__guest = value

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        from .room import Room
        if not isinstance(value, Room):
            raise TypeError("room must be a Room object")
        self.__room = value

    @property
    def invoice(self):
        return self.__invoice

    @invoice.setter
    def invoice(self, value):
        if not isinstance(value, Invoice):
            raise TypeError("invoice must be an Invoice object")
        self.__invoice = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int) or 1 <= value <= 10:
            raise ValueError("rating must be number between 1 and 10")