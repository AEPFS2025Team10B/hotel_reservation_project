class RoomType:
    def __init__(
        self,
        room_type_id: int,
        max_guests: int,
        description: str = "No Description",
        name: str = None,
        price_per_night: float = 0.0,
        facilities: list = None
    ):
        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guest = max_guests
        self.__name = name or description
        self.__price_per_night = price_per_night
        self.__facilities = facilities or []

    @property
    def room_type_id(self):
        return self.__room_type_id

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise ValueError("Room Type description must be a string")
        self.__description = description

    @property
    def max_guests(self):
        return self.__max_guest

    @max_guests.setter
    def max_guests(self, max_guests):
        if not max_guests:
            raise ValueError("Room Type max_guest is required")
        if not isinstance(max_guests, int):
            raise ValueError("Room Type max_guest must be an integer")
        self.__max_guest = max_guests

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Room Type name must be a string")
        self.__name = name

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price):
        if not isinstance(price, (int, float)):
            raise ValueError("Room Type price must be a number")
        self.__price_per_night = price

    @property
    def facilities(self):
        return self.__facilities

    @facilities.setter
    def facilities(self, facilities):
        if not isinstance(facilities, list):
            raise ValueError("Room Type facilities must be a list")
        self.__facilities = facilities

    def __str__(self):
        return (
            f" (max {self.__max_guest} Gäste): {self.__description}\n"
        )