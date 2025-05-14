class RoomType:
    def __init__(self, room_type_id:int, name:str, max_guest:int, description:str = "No Description"):
        self.__room_type_id = room_type_id
        self.__name = name
        self.__description = description
        self.__max_guest = max_guest

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
    def max_guest(self):
        return self.__max_guest

    @max_guest.setter
    def max_guest(self, max_guest):
        if not max_guest:
            raise ValueError("Room Type max_guest is required")
        if not isinstance(max_guest, int):
            raise ValueError("Room Type max_guest must be a integer")
        self.__max_guest = max_guest
