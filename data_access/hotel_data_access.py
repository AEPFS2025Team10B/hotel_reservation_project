from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.1: Alle Hotels abrufen
    def get_all_hotels(self) -> list[Hotel]:
        sql = """
        SELECT hotel_id, name, stars
        FROM hotel
        """
        rows = self.fetchall(sql)
        return [Hotel(hid, name, stars, None) for hid, name, stars in rows]

    # User Story 1.2: Hotel-Details nach ID abrufen
    def get_hotel_by_id(self, hotel_id: int) -> Hotel | None:
        sql = """
        SELECT hotel_id, name, stars, address_id
        FROM hotel
        WHERE hotel_id = ?
        """
        row = self.fetchone(sql, (hotel_id,))
        if not row:
            return None
        hid, name, stars, aid = row
        addr_row = self.fetchone(
            "SELECT address_id, street, city, zip_code FROM address WHERE address_id = ?", (aid,)
        )
        address = Address(*addr_row) if addr_row else None
        return Hotel(hid, name, stars, address)

    # User Story 1.3: Hotels in einer Stadt suchen
    def get_hotels_by_city(self, city_name: str) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        WHERE LOWER(a.city) = LOWER(?)
        """
        rows = self.fetchall(sql, (city_name,))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipc in rows:
            addr = Address(aid, street, city, zipc)
            result.append(Hotel(hid, name, stars, addr))
        return result

    # User Story 1.6: Alle Hoteldetails (Name, Adresse, Sterne)
    def get_all_hotel_details(self) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        """
        rows = self.fetchall(sql)
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipc in rows:
            addr = Address(aid, street, city, zipc)
            result.append(Hotel(hid, name, stars, addr))
        return result

    # User Story 3.1.1: Neue Adresse anlegen
    def create_address(self, street: str, city: str, zip_code: str) -> Address:
        sql = """
        INSERT INTO address (street, city, zip_code)
        VALUES (?, ?, ?)
        """
        new_id, _ = self.execute(sql, (street, city, zip_code))
        return Address(new_id, street, city, zip_code)

    # User Story 3.1: Neues Hotel anlegen
    def create_hotel(self, name: str, stars: int, address_id: int) -> Hotel:
        sql = """
        INSERT INTO hotel (name, stars, address_id)
        VALUES (?, ?, ?)
        """
        new_id, _ = self.execute(sql, (name, stars, address_id))
        return self.get_hotel_by_id(new_id)

    # Optional: Update und Delete Methoden
    def update_hotel(self, hotel: Hotel) -> None:
        sql = """
        UPDATE hotel
        SET name = ?, stars = ?, address_id = ?
        WHERE hotel_id = ?
        """
        _, _ = self.execute(
            sql,
            (hotel.name, hotel.stars, hotel.address.address_id, hotel.hotel_id),
        )

    def delete_hotel(self, hotel_id: int) -> None:
        sql = "DELETE FROM hotel WHERE hotel_id = ?"
        _, _ = self.execute(sql, (hotel_id,))
