from data_access.base_data_access import BaseDataAccess
from model.roomtype import RoomType
from model.room import Room
from model.facility import Facility

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.4: Verfügbare Zimmer eines Hotels an einem Datum
    def get_rooms_by_hotel(self, hotel_id: int, date_str: str) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.max_guests, rt.description,
                   fac.facility_id, fac.facility_name
            FROM Room AS r
            JOIN Room_Type AS rt ON rt.type_id = r.type_id
            JOIN Room_Facilities AS rf ON rf.room_id = r.room_id
            JOIN Facilities AS fac ON fac.facility_id = rf.facility_id
            WHERE r.hotel_id = ?
            AND r.room_id NOT IN (SELECT room_id FROM Booking WHERE check_in_date <= ? AND check_out_date > ?)
        """
        rows = self.fetchall(sql, (hotel_id, date_str, date_str))
        rooms = {}
        for rid, rnr, rpr, rtid, rtmg, rtd, fid, fname in rows:
            if rid not in rooms:
                room = Room(rid, rnr, rpr)
                room.roomtype = RoomType(rtid, rtmg, rtd)
                room.facilities = []
                rooms[rid] = room
            rooms[rid].facilities.append(Facility(fid, fname))
            return list(rooms.values())

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
        SELECT r.room_id, r.room_number, r.price_per_night, rt.type_id, rt.max_guests, rt.description, fac.facility_id, fac.facility_name
            FROM Room AS r
            JOIN Room_Type AS rt ON rt.type_id = r.type_id
            JOIN Room_Facilities AS rf ON rf.room_id = r.room_id
            JOIN Facilities AS fac ON fac.facility_id = rf.facility_id
            WHERE r.hotel_id = ?
            AND r.room_id NOT IN (
              SELECT room_id
              FROM Booking
              WHERE NOT (
                  check_out_date <= ?
                  OR check_in_date  >= ?
              )
          )
        """
        rows = self.fetchall(sql, (hotel_id, check_in, check_out))
        rooms_by_id = {}
        for rid, rnr, rpr, rtid, rtmg, rtd, fid, fname in rows:
            if rid not in rooms_by_id:
                room = Room(rid, rnr, rpr)
                room.roomtype = RoomType(rtid, rtmg, rtd)
                room.facilities = []
                rooms_by_id[rid] = room
            rooms_by_id[rid].facilities.append(Facility(fid, fname))

        return list(rooms_by_id.values())



# User Story 4: Verfügbare Zimmer eines Hotels für einen Zeitraum
    def get_available_rooms_by_hotel_and_dates_2(
        self, hotel_id: int, check_in_date: str, check_out_date: str
    ) -> list[Room]:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, rt.type_id, rt.max_guests, rt.description, fac.facility_id, fac.facility_name
        FROM Room AS r
        JOIN Room_Type AS rt ON rt.type_id = r.type_id
        JOIN Room_Facilities AS rf ON rf.room_id = r.room_id
        JOIN Facilities AS fac ON fac.facility_id = rf.facility_id
        WHERE hotel_id = ?
          AND r.room_id NOT IN (
              SELECT b.room_id
              FROM Booking AS b
              WHERE NOT (
                  b.check_out_date <= ?
                  OR b.check_in_date  >= ?
              )
          )
        """
        rows = self.fetchall(sql, (hotel_id, check_in_date, check_out_date))
        result: list[Room] = []
        for rid, rnr, rpr, rtid, rtmg, rtd, fid, fn in rows:
            room = Room(rid, rnr, rpr)
            room.roomtype = RoomType(rtid, rtmg, rtd)
            room.facility = Facility(fid, fn)
            result.append(room)
        return result

    def get_room_by_id(self, room_id: int) -> Room | None:
        sql = """
        SELECT r.room_id, r.room_number, r.price_per_night, rt.type_id, rt.max_guests, rt.description, fac.facility_id, fac.facility_name
        FROM Room AS r
        JOIN Room_Type AS rt ON rt.type_id = r.type_id
        JOIN Room_Facilities AS rf ON rf.room_id = r.room_id
        JOIN Facilities AS fac ON fac.facility_id = rf.facility_id
        WHERE r.room_id = ?
        """
        row = self.fetchone(sql, (room_id,))
        if row is None:
            return None
            
        rid, rnr, rpr, rtid, rtmg, rtd, fid, fn = row
        room = Room(rid, rnr, rpr)
        room.roomtype = RoomType(rtid, rtmg, rtd)
        room.facility = Facility(fid, fn)
        return room
    
    def get_all_rooms_with_facilities(self):
        sql = """
        SELECT h.name AS hotel_name,
            r.room_number,
            rt.description AS room_type,
            rt.max_guests,
            r.price_per_night,
            GROUP_CONCAT(f.facility_name, ', ') AS facilities,
            r.room_id,
            rt.type_id
        FROM Room r
        JOIN Hotel h ON r.hotel_id = h.hotel_id
        JOIN Room_Type rt ON r.type_id = rt.type_id
        LEFT JOIN Room_Facilities rf ON r.room_id = rf.room_id
        LEFT JOIN Facilities f ON rf.facility_id = f.facility_id
        GROUP BY r.room_id
        ORDER BY h.name, r.room_number
        """
        return self.fetchall(sql)


    def get_room_with_hotel(self, hotel_id: int) -> list[Room]:
        sql = """
            SELECT r.room_id, r.room_number, r.price_per_night,
                   rt.type_id, rt.max_guests, rt.description,
                   fac.facility_id, fac.facility_name
            FROM Room AS r
            JOIN Room_Type AS rt ON rt.type_id = r.type_id
            JOIN Room_Facilities AS rf ON rf.room_id = r.room_id
            JOIN Facilities AS fac ON fac.facility_id = rf.facility_id
            WHERE r.hotel_id = ?
            ORDER BY r.room_id
        """
        rows = self.fetchall(sql, (hotel_id,))

        rooms_by_id = {}
        for rid, rnr, rpr, rtid, rtmg, rtd, fid, fname in rows:
            if rid not in rooms_by_id:
                room = Room(rid, rnr, rpr)
                room.roomtype = RoomType(rtid, rtmg, rtd)
                room.facilities = []
                rooms_by_id[rid] = room
            rooms_by_id[rid].facilities.append(Facility(fid, fname))

        return list(rooms_by_id.values())