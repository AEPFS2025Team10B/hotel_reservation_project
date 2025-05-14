from __future__ import annotations

from model import Guest
from data_access.base_data_access import BaseDataAccess


class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(self, first_name: str, last_name: str, email: str) -> Guest:
        if first_name is None:
            raise ValueError("First name is required")
        if last_name is None:
            raise ValueError("Last name is required")
        if email is None:
            raise ValueError("Email is required")

        sql = """
        INSERT INTO Guest (FirstName, LastName, Email)
        VALUES (?, ?, ?)
        """
        params = (first_name, last_name, email)
        last_row_id, _ = self.execute(sql, params)

        return Guest(
            guest_id=last_row_id,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

    def read_guest_by_id(self, guest_id: int) -> Guest | None:
        if guest_id is None:
            raise ValueError("Guest ID is required")

        sql = """
        SELECT GuestId, FirstName, LastName, Email
        FROM Guest
        WHERE GuestId = ?
        """
        result = self.fetchone(sql, (guest_id,))
        if result:
            guest_id, first_name, last_name, email = result
            return Guest(guest_id, first_name, last_name, email)
        return None

    def read_guests_by_last_name(self, last_name: str) -> list[Guest]:
        if last_name is None:
            raise ValueError("Last name is required")

        sql = """
        SELECT GuestId, FirstName, LastName, Email
        FROM Guest
        WHERE LastName = ?
        """
        rows = self.fetchall(sql, (last_name,))
        return [
            Guest(guest_id, first_name, last_name, email)
            for guest_id, first_name, last_name, email in rows
        ]