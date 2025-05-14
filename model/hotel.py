from address import Address

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, city: str, street: str):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address: list[Address] = []
        self.__rooms = []                  
        self.__facilities = []      

    def __repr__(self):
        return f"Hotel(id={self.__hotel_id!r}, name={self.__name!r})"

    @property
    def hotel_id(self):
        return self.__hotel_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name or not isinstance(name, str):
            raise TypeError("Hotel name must be a non-empty string")
        self.__name = name

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, stars):
        if not isinstance(stars, int) or not (0 <= stars <= 5):
            raise ValueError("Stars must be an integer between 0 and 5")
        self.__stars = stars

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        from .address import Address
        if not isinstance(address, Address):
            raise TypeError("Address must be an Address object")
        self.__address = address

    @property
    def rooms(self):
        return self.__rooms

    def add_room(self, room):
        from .room import Room
        if not isinstance(room, Room):
            raise TypeError("Room must be a Room object")
        self.__rooms.append(room)

    @property
    def facilities(self):
        return self.__facilities

    def add_facility(self, facility):
        from .facility import Facility
        if not isinstance(facility, Facility):
            raise TypeError("Facility must be a Facility object")
        self.__facilities.append(facility)
