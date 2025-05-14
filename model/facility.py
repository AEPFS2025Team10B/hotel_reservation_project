class Facility:
    def __init__(self, facility_id:int, name:str):
        self.__facility_id = facility_id
        self.__name = name

    @property
    def facility_id(self):
        return self.__facility_id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("facility name is required")
        if not isinstance(name, str):
            raise TypeError("facility name must be a string")
        self.__name = name
