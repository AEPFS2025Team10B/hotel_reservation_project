from data_access.base_data_access import BaseDataAccess
from model.roomtype import RoomType
from model.room import Room

class RoomDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 1.4: Verfügbare Zimmer eines Hotels an einem Datum
    def get_rooms_by_hotel(self, hotel_id: int, date_str: str) -> list[Room]:
        sql = """
        SELECT room_id, room_number, price_per_night, roomtype_id, hotel_id
        FROM room
        WHERE hotel_id = ?
          AND room_id NOT IN (
              SELECT room_id
              FROM booking
              WHERE check_in_date <= ?
                AND check_out_date > ?
          )
        """
        rows = self.fetchall(sql, (hotel_id, date_str, date_str))
        return [
            Room(rid, number, price, rt_id, hotel_id)
            for rid, number, price, rt_id, hotel_id in rows
        ]

    # User Story 2.1: Alle Raumtypen eines Hotels
    def get_room_types_by_hotel(self, hotel_id: int) -> list[RoomType]:
        sql = """
        SELECT rt.roomtype_id, rt.name, rt.description, rt.max_guest, rt.price_per_night
        FROM roomtype AS rt
        JOIN room AS r ON rt.roomtype_id = r.roomtype_id
        WHERE r.hotel_id = ?
        """
        rows = self.fetchall(sql, (hotel_id,))
        return [
            RoomType(rtid, name, desc, maxg, price)
            for rtid, name, desc, maxg, price in rows
        ]
