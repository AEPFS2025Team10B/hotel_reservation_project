class RoomType:
    def __init__(
        self,
        room_type_id: int,
        name: str,
        max_guests: int,
        description: str = "No Description",
        price_per_night: float = 0.0,
        facilities: list[str] = None
    ):
        self.__room_type_id = room_type_id
        self.__name = name
        self.__description = description
        self.__max_guest = max_guests
        self.__price_per_night = price_per_night
        self.__facilities = facilities or []

    @property
    def room_type_id(self):
        return self.__room_type_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Room Type name is required")
        if not isinstance(name, str):
            raise ValueError("Room Type name must be a string")
        self.__name = name

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
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, price):
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Preis muss eine positive Zahl sein.")
        self.__price_per_night = float(price)

    @property
    def facilities(self):
        return self.__facilities

    @facilities.setter
    def facilities(self, facilities_list):
        if not isinstance(facilities_list, list):
            raise ValueError("Facilities must be a list of string.")
        if not all(isinstance(f, str) for f in facilities_list):
            raise ValueError("All facilities must be string.")
        self.__facilities = facilities_list

    def __str__(self):
        return (
            f"{self.__name} (max {self.__max_guest} Gäste): {self.__description}\n"
            f"Preis: CHF {self.__price_per_night:.2f} pro Nacht\n"
            f"Ausstattung: {', '.join(self.__facilities) if self.__facilities else 'Keine'}"
        )