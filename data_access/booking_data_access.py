from data_access.base_data_access import BaseDataAccess
from model.booking import Booking
from business_logic.room_manager import find_room_by_id
from business_logic.hotel_manager import find_hotel_by_id
from business_logic.hotel_manager import find_hotel_id_by_room_id
from business_logic.hotel_manager import find_hotel_by_id_2


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
        booking.is_cancelled = bool(is_cancelled)
        booking.total_price = total_amount
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
        booking = Booking(booking_id, check_in_date, check_out_date)
        booking.is_cancelled = bool(is_cancelled)
        booking.total_price = total_amount
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

    def get_reviews_by_hotel_name(self, hotel_name: str):
        sql = """
        SELECT b.rating, b.recommendation, g.first_name, g.last_name
        FROM booking AS b
        JOIN room AS r ON b.room_id = r.room_id
        JOIN hotel AS h ON r.hotel_id = h.hotel_id
        JOIN guest AS g ON b.guest_id = g.guest_id
        WHERE h.name = ? AND b.rating IS NOT NULL
        """
        return self.fetchall(sql, (hotel_name,))
    

    def display_all_bookings_of_all_hotels(self) -> list[tuple]:
        sql = """
        SELECT 
            h.name AS hotel_name,
            b.booking_id,
            g.first_name || ' ' || g.last_name AS guest_name,
            r.room_number,
            b.check_in_date,
            b.check_out_date
        FROM booking b
        JOIN guest g ON b.guest_id = g.guest_id
        JOIN room r ON b.room_id = r.room_id
        JOIN hotel h ON r.hotel_id = h.hotel_id
        ORDER BY h.name, b.check_in_date
        """
        return self.fetchall(sql)

    def cancel_booking(self, booking_id: int):
        sql = """
        UPDATE booking 
        SET is_cancelled = 1
        WHERE booking_id = ?
        """
        self.execute(sql, (booking_id,))

    def get_bookings_by_guest_id(self, guest_id: int) -> list[Booking]:
        sql = """
        SELECT booking_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM Booking
        WHERE guest_id = ?
        """
        rows = self.fetchall(sql, (guest_id,))

        bookings = []
        for booking_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount in rows:
            booking = Booking(booking_id, check_in_date, check_out_date)
            booking.is_cancelled = bool(is_cancelled)
            booking.total_amount = total_amount

            room = find_room_by_id(room_id)
            hotel_id = find_hotel_id_by_room_id(room.room_id)
            room.hotel = find_hotel_by_id_2(hotel_id)
            booking.room = room

            bookings.append(booking)
        return bookings

    def get_all_bookings(self) -> list[Booking]:
        sql = """
        SELECT booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount
        FROM booking
        """
        rows = self.fetchall(sql)
        bookings = []
        for row in rows:
            booking_id, guest_id, room_id, check_in_date, check_out_date, is_cancelled, total_amount = row
            booking = Booking(booking_id, check_in_date, check_out_date)
            booking.is_cancelled = bool(is_cancelled)
            booking.total_price = total_amount
            booking.guest_id = guest_id
            booking.room_id = room_id
            bookings.append(booking)
        return bookings