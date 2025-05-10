import model
from data_access.base_data_access import BaseDataAccess

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_new_guest(
            self,
            first_name: str,
            last_name: str,
            email: str
    ) -> model.Guest:
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if not email:
            raise ValueError("Email is required")

        sql = """
        INSERT INTO Guest (FirstName, LastName, Email)
        VALUES (?, ?, ?)
        """
        params = (first_name, last_name, email)

        last_row_id, row_count = self.execute(sql, params)

        return model.Guest(
            guest_id=last_row_id,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

    def read_guest_by_id(self, guest_id: int) -> model.Guest | None:
        if not guest_id:
            raise ValueError("Guest ID is required")

        sql = """
        SELECT GuestId, FirstName, LastName, Email
        FROM Guest
        WHERE GuestId = ?
        """
        params = (guest_id,)
        result = self.fetchone(sql, params)

        if result:
            guest_id, first_name, last_name, email = result
            return model.Guest(
                guest_id=guest_id,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
        else:
            return None

    def read_guests_by_last_name(self, last_name: str) -> list[model.Guest]:
        if not last_name:
            raise ValueError("Last name is required")

        sql = """
        SELECT GuestId, FirstName, LastName, Email
        FROM Guest
        WHERE LastName = ?
        """
        params = (last_name,)
        rows = self.fetchall(sql, params)

        return [
            model.Guest(
                guest_id=row[0],
                first_name=row[1],
                last_name=row[2],
                email=row[3]
            )
            for row in rows
        ]
