from data_access.base_data_access import BaseDataAccess
from model.roomtype import RoomType
from model.room import Room

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.4: Verfügbare Zimmer eines Hotels an einem Datum
    def get_rooms_by_hotel(self, hotel_id: int, date_str: str) -> list[Room]:
        sql = """
        SELECT room_id, room_number, price_per_night
        FROM Room
        WHERE hotel_id = ?
          AND room_id NOT IN (
              SELECT room_id
              FROM Booking
              WHERE check_in_date <= ?
                AND check_out_date > ?
          )
        """
        rows = self.fetchall(sql, (hotel_id, date_str, date_str))
        return [
            Room(room_id, room_number, price_per_night)
            for room_id, room_number, price_per_night in rows
        ]

    # User Story 2.1: Alle Raumtypen eines Hotels inklusive Ausstattung
    def get_room_types_by_hotel(self, hotel_id: int) -> list[RoomType]:
        # Basis-Abfrage pro Raumtyp (mit minimalem Preis)
        sql = """
        SELECT
            rt.type_id             AS room_type_id,
            rt.description         AS description,
            rt.max_guests          AS max_guests,
            MIN(r.price_per_night) AS price_per_night
        FROM Room_Type AS rt
        JOIN Room AS r
          ON rt.type_id = r.type_id
        WHERE r.hotel_id = ?
        GROUP BY rt.type_id, rt.description, rt.max_guests
        """
        rows = self.fetchall(sql, (hotel_id,))

        result: list[RoomType] = []
        for rtid, description, max_guests, price in rows:
            # Facilities für diesen Raumtyp ermitteln
            fac_sql = """
            SELECT DISTINCT f.facility_name
            FROM Facilities AS f
            JOIN Room_Facilities AS rf ON f.facility_id = rf.facility_id
            JOIN Room AS r ON rf.room_id = r.room_id
            WHERE r.hotel_id = ? AND r.type_id = ?
            """
            fac_rows = self.fetchall(fac_sql, (hotel_id, rtid))
            facilities = [fr[0] for fr in fac_rows]

            result.append(
                RoomType(
                    rtid,
                    description,        # name
                    max_guests,
                    description,        # description
                    price,
                    facilities
                )
            )

        return result

    # User Story 2.2: Verfügbare Zimmer eines Hotels für einen Zeitraum
    def get_available_rooms_by_hotel_and_dates(
        self, hotel_id: int, check_in: str, check_out: str
    ) -> list[Room]:
        sql = """
        SELECT room_id, room_number, price_per_night
        FROM Room
        WHERE hotel_id = ?
          AND room_id NOT IN (
              SELECT room_id
              FROM Booking
              WHERE NOT (
                  check_out_date <= ?
                  OR check_in_date  >= ?
              )
          )
        """
        rows = self.fetchall(sql, (hotel_id, check_in, check_out))
        return [
            Room(room_id, room_number, price_per_night)
            for room_id, room_number, price_per_night in rows
        ]

