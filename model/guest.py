from model.address import Address
from model.booking import Booking
import datetime

class Guest:
    def __init__(self, guest_id:int, last_name:str, first_name:str, email:str, birthday: datetime.date | None, nationality: str):
        self.__guest_id = guest_id
        self.__last_name = last_name
        self.__first_name = first_name
        self.__email = email
        self.__birthday = birthday
        self.__nationality = nationality
        self.__address = None
        self.__booking = []
    def __repr__(self):
        return f"Guest(id={self.__guest_id!r}, last_name={self.__last_name!r}, first_name={self.__first_name!r}, email={self.__email!r}, birthday={self.__birthday!r}, nationality={self.__nationality!r})"

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
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: datetime.date | None):
        self.__birthday = birthday

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality):
        if not nationality:
            raise ValueError("Nationality is required")
        self.__nationality = nationality

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        if not isinstance(address, Address):
            raise TypeError("Address is required")
        self.__address = address

    @property
    def bookings(self):
        return self.__booking

    @bookings.setter
    def bookings(self, bookings):
        if not isinstance(bookings, list):
            raise TypeError("Bookings must be a list of Booking objects")
        if not all(isinstance(b, Booking) for b in bookings):
            raise TypeError("All items in bookings must be of type Booking")
        self.__booking = bookings

