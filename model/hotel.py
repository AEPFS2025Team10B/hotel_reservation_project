from address import Address
from room import Room
from facility import Facility

class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, city: str, street: str):
        self.__hotel_id = hotel_id
        self.__name = name
        self.__stars = stars
        self.__address = Address
        self.__room  = []
        self.__facility = []

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
        if not name:
            raise TypeError("hotel name is required")
        if not isinstance(name, str):
            raise TypeError("hotel name must be a string")
        self.__name = name

    @property
    def stars(self):
        return self.__stars

    @stars.setter
    def stars(self, stars):
        if stars is None:
            raise TypeError("hotel stars is required")
        if not isinstance(stars, int):
            raise TypeError("hotel stars must be a integer")
        if not (0 <= stars <= 5):
            raise ValueError("Number of stars must be between 0 and 5")
        self.__stars = stars

    @property
    def address(self):
        return self.__address

    @address.setter
    def add_address(self, address: Address):
        self.__address.append(address)

    @property
    def room(self):
        return self.__rooms

    def add_room(self, room: Room):
        self.__room.append(room)

    @property
    def facility(self):
        return self.__facility

    @facility.setter
    def add_facility(self, facility: Facility):
        self.__facility.append(facility)

#for room maybe following would be better:
# def add_room(self, room_id:int, number:str, price_per_night:float):
# room = Room(room:id, number, price_per_night)
# self.__room.append(room)

    # def show_hotel_details(self):
    #     print(f"Hotel Name: {self.__name}, Stars: {self.__stars}, Address: {self.__address}")
    #     for room in self.__room:
    #         print(room.get_room_details())

