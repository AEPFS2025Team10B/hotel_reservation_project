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
        if row is None:
            return None
        booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount = row
        # TODO: check booking constructor to give more attributes.
        booking = Booking(booking_id, check_in_date, check_out_date)
        booking.is_cancelled = bool(is_cancelled)
        booking.total_amount = total_amount
        return booking

    def get_booking_relations(self, booking_id: int) -> tuple[int, int] | None:
        sql = """
        SELECT guest_id, room_id
        FROM booking
        WHERE booking_id = ?
        """
        row = self.fetchone(sql, (booking_id,))
        if row:
            return row[0], row[1]  # guest_id, room_id
        return None

    def insert_hotelrecommendation(self, booking_id: int, rating: int, recommendation: str):
        #gibt an, welche Inputs wir gerne hätten
        sql = """
        UPDATE booking 
        SET rating = ?, recommendation = ?
        WHERE booking_id = ?
        """
        self.execute(sql, (rating, recommendation, booking_id))
        # führt das SQL Statement aus

    def display_all_bookings_of_all_hotels(self, booking_id: int) -> Booking | None:
        sql = """"
        SELECT Hotel.name AS hotel_name, Booking.booking_id, Booking.room_id, check_in_date, check_out_date, is_cancelled
        FROM Booking
        JOIN Room ON Booking.room_id = Room.room_id
        JOIN Hotel ON Room.hotel_id = Hotel.hotel_id;
        """
        row = self.fetchone(sql, (booking_id,))
        return Booking