from address import Address
from booking import Booking
from model import booking


class Guest:
    def __init__(self, guest_id:int, last_name:str, first_name:str, email:str):
        self.__guest_id = guest_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__email = email
        self.__address = Address
        self.__booking = Booking

    def __repr__(self):
        return f"Guest(id={self.__guest_id!r}, last_name={self.__last_name!r}, first_name={self.__first_name!r}, email={self.__email!r})"

    @property
    def guest_id(self):
        return self.__guest_id

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        if not last_name:
            raise ValueError("last name name is required")
        if not isinstance(last_name, str):
            raise TypeError("last name must be a string")
        self.__last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise ValueError("first name is required")
        if not isinstance(first_name, str):
            raise TypeError("first name must be a string")
        self.__first_name = first_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not email:
            raise ValueError("email is required")
        if not isinstance(email, str):
            raise TypeError("email must be a string")
        self.__email = email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, Address):
            raise TypeError("address is required")
        self.__address = address

    @property
    def booking(self):
        return self.__booking
    @booking.setter
    def booking(self, booking):
        if not isinstance(booking, Booking):
            raise TypeError("booking must be a Booking")
        self.__booking = booking

