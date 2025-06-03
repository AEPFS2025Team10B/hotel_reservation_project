from data_access.base_data_access import BaseDataAccess
from model.booking import Booking

class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def insert_booking(self, guest_id, room_id, check_in_date: str, check_out_date: str, total_amount) -> Booking:
        sql = """
        INSERT INTO booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        new_id, _ = self.execute(sql, (guest_id, room_id, check_in_date, check_out_date, total_amount))
        return Booking(new_id, guest_id, room_id, check_in_date, check_out_date, total_amount)