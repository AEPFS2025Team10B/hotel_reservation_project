class RoomType:
    def __init__(
        self,
        room_type_id: int,
        max_guests: int,
        description: str = "No Description",
    ):
        self.__room_type_id = room_type_id
        self.__description = description
        self.__max_guest = max_guests

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

    def __str__(self):
        return (
            f" (max {self.__max_guest} Gäste): {self.__description}\n"
        )