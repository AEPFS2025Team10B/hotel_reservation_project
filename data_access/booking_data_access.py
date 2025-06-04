
from data_access.base_data_access import BaseDataAccess
from model.booking import Booking


class BookingDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def insert_booking(self, guest_id: int, room_id: int, check_in_date: str, check_out_date: str, is_cancelled: int, total_amount: float) -> Booking:
        sql = """
        INSERT INTO booking (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        new_id, _ = self.execute(sql, (guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount))
        booking = Booking(new_id, check_in_date, check_out_date)
        return booking

    def get_booking_by_id(self, booking_id: int) -> Booking | None:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM booking
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        find_guest_by_id(row['guest_id'])
        find_room_by_id(row['room_id'])
        return [Booking(booking_id, check_in_date, check_out_date) for booking_id, check_in_date, check_out_date in row]
    
    def insert_hotelrecommendation(self, rating, recommendation):
        sql = """
        INSERT INTO booking (rating, recommendation)
        VALUES (?, ?)
        """
        