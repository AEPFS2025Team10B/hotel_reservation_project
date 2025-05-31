from tkinter.tix import Select

from data_access.base_data_access import BaseDataAccess
from model.hotel import Hotel
from model.address import Address

class HotelDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.1: Alle Hotels abrupt
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

    # User Story 1.1: Hotels in einer Stadt suchen
    def get_hotels_by_city(self, city: str) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        WHERE LOWER(a.city) = LOWER(?)
        """
        rows = self.fetchall(sql, (city,))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipc in rows: #TODO List comprehension
            address = Address(aid, street, city, zipc)
            hotel = Hotel(hid, name, stars, address)
            result.append(hotel)
        return result

    # User Story 1.2: Hotels in einer Stadt durchsuchen mit mind Anzahl Sternen
    def get_hotels_by_city_and_min_stars(self, city: str, min_stars: int) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars,
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        WHERE LOWER(a.city) = LOWER(?)
        AND h.stars >= ?
        """
        rows = self.fetchall(sql, (city, min_stars,))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipc in rows: #TODO List comprehension
            hotels = Hotel(hid, name, stars)
            hotels.address = Address(aid, street, city, zipc)
            result.append(hotels)
        return result

    # User Story 1.3: Hotels suchen, die Zimmer haben welche meiner Gästeanzahl entsprechen
    def get_hotels_by_guest_count(self, guest_count: int) -> list[Hotel]:
        sql = """
      SELECT h.hotel_id, h.name, h.stars,
             a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        JOIN ROOM AS r ON r.hotel_id = h.hotel_id
        JOIN Room_Type AS rt ON rt.type_id = r.type_id
        WHERE rt.max_guests = ?
        """
        rows = self.fetchall(sql, (guest_count,))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipcode in rows:
            hotels = Hotel(hid, name, stars)
            hotels.address = Address(aid, street, city, zipcode)
            result.append(hotels)
        return result

    # User Story 1.4: Hotels , die während des Aufenthaltes verfügbar sind
    def get_hotels_by_availability(self, check_in_date: str, check_out_date: str) -> list[Hotel]:
        sql = """
        SELECT h.hotel_id, h.name, h.stars, 
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        JOIN room as r ON r.hotel_id = h.hotel_id
        WHERE room_id NOT IN (
              SELECT room_id
              FROM Booking
              WHERE check_in_date <= ?
                AND check_out_date > ?
                AND is_cancelled == 0
          )
        """
        rows = self.fetchall(sql, (check_in_date, check_out_date,))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipcode in rows:
            hotels = Hotel(hid, name, stars)
            hotels.address = Address(aid, street, city, zipcode)
            result.append(hotels)
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

    #User Story 1.5 – Hotels nach mehreren Kriterien suchen
    def get_hotels_by_multiple_criteria(
        self,
        city: str,
        min_stars: int,
        guest_count: int,
        check_in_date: str,
        check_out_date: str
    ) -> list[Hotel]:
        sql = """
        SELECT DISTINCT h.hotel_id, h.name, h.stars,
               a.address_id, a.street, a.city, a.zip_code
        FROM hotel AS h
        JOIN address AS a ON h.address_id = a.address_id
        JOIN room AS r ON r.hotel_id = h.hotel_id
        JOIN room_type AS rt ON rt.type_id = r.type_id
        WHERE LOWER(a.city) = LOWER(?)
          AND h.stars >= ?
          AND rt.max_guests >= ?
          AND r.room_id NOT IN (
              SELECT room_id
              FROM booking
              WHERE check_in_date < ?
                AND check_out_date > ?
                AND is_cancelled = 0
          )
        """
        rows = self.fetchall(sql, (city, min_stars, guest_count, check_out_date, check_in_date))
        result: list[Hotel] = []
        for hid, name, stars, aid, street, city, zipcode in rows:
            hotel = Hotel(hid, name, stars)
            hotel.address = Address(aid, street, city, zipcode)
            result.append(hotel)
        return result
