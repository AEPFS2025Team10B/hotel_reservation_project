class Address:
    def __init__(self, address_id:int, street:str, city:str, zip_code:str):
        self.__address_id = address_id
        self.__street = street
        self.__city = city
        self.__zip_code = zip_code

    def __repr__(self):
        return f"Address(id={self.__address_id!r}, street={self.__street!r}, city={self.__city!r}, state={self.__state!r}, zip={self.__zip_code!r})"

    @property
    def address_id(self):
        return self.__address_id

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        if not street:
            raise ValueError("street name and number is required")
        if not isinstance(street, str):
            raise TypeError("street must be a string")
        self.__street = street

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        if not city:
            raise ValueError("city name is required")
        if not isinstance(city, str):
            raise TypeError("city must be a string")
        self.__city = city

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        if not state:
            raise ValueError("state name is required")
        if not isinstance(state, str):
            raise TypeError("state must be a string")
        self.__state = state

    @property
    def zip_code(self):
        return self.__zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        if not zip_code:
            raise ValueError("zip code is required")
        if not isinstance(zip_code, str):
            raise TypeError("zip code must be a string")
        self.__zip_code = zip_code

