class Hotel:
    def __init__(self, hotel_id: int, name: str, stars: int, city: str, street: str):
        self.hotel_id = hotel_id
        self.name = name
        self.stars = stars
        self.city = city
        self.street = street

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

