class Room:
    def __init__(self, room_id: int, number: str, price_per_night: float):
        self.__room_id = room_id
        self.__number = number
        self.__price_per_night = price_per_night
        self.__roomtype = []
        self.__hotel = []
        self.__booking = []

    def __repr__(self):
        return f"Room(id={self.__room_id!r}, number={self.__number!r}, price_per_night={self.__price_per_night!r})"

    @property
    def room_id(self):
        return self.__room_id

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if not number:
            raise ValueError("room number is required")
        if not isinstance(number, str):
            raise TypeError("room number must be a string")
        self.__number = number

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price_per_night):
        if price_per_night is None:
            raise ValueError("price per night is required")
        if not isinstance(price_per_night, float):
            raise TypeError("price per night must be a float")
        if price_per_night <= 0:
            raise ValueError("price per night must be greater than 0")
        self.__price_per_night = price_per_night

    @property
    def roomtype(self):
        return self.__roomtype

    @roomtype.setter
    def roomtype(self, roomtype):
        from .roomtype import RoomType
        if not isinstance(roomtype, RoomType):
            raise TypeError("room type must be a RoomType")
        self.__roomtype = roomtype

    @property
    def hotel(self):
        return self.__hotel

    @hotel.setter
    def hotel(self, hotel):
        from .hotel import Hotel
        if not isinstance(hotel, Hotel):
            raise TypeError("hotel must be a Hotel")
        self.__hotel = hotel

    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, booking):
        from .booking import Booking
        if not isinstance(booking, Booking):
            raise TypeError("booking must be a Booking")
        self.__booking = booking