class Room:
    def __init__(self, room_id:int, number:str, price_per_night:float):
        self.__room_id = room_id
        self.__number = number
        self.__price_per_night = price_per_night

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

