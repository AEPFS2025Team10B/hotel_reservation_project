from data_access.base_data_access import BaseDataAccess
from model.guest import Guest

class GuestDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    # User Story 4.1: Neuer Gast anlegen
    def create_guest(self, first_name: str, last_name: str, email: str) -> Guest:
        if not first_name or not last_name:
            raise ValueError("Vor- und Nachname sind erforderlich")
        sql = """
        INSERT INTO guest (first_name, last_name, email)
        VALUES (?, ?, ?)
        """
        new_id, _ = self.execute(sql, (first_name, last_name, email))
        return Guest(new_id, first_name, last_name, email)

    # User Story 2.1 (Teil 2): Gast nach ID lesen
    def get_guest_by_id(self, guest_id: int) -> Guest | None:
        sql = """
        SELECT guest_id, first_name, last_name, email
        FROM guest
        WHERE guest_id = ?
        """
        row = self.fetchone(sql, (guest_id,))
        return Guest(*row) if row else None

    # User Story 4.2: Gäste nach Nachname suchen
    def get_guests_by_last_name(self, last_name: str) -> list[Guest]:
        sql = """
        SELECT guest_id, first_name, last_name, email
        FROM guest
        WHERE LOWER(last_name) = LOWER(?)
        """
        rows = self.fetchall(sql, (last_name,))
        return [Guest(gid, fn, ln, em) for gid, fn, ln, em in rows]

    # User Story 4.3: Gast-Daten aktualisieren
    def update_guest(self, guest: Guest) -> None:
        sql = """
        UPDATE guest
        SET first_name = ?, last_name = ?, email = ?
        WHERE guest_id = ?
        """
        _, _ = self.execute(
            sql, (guest.first_name, guest.last_name, guest.email, guest.guest_id)
        )

    # User Story 4.4: Gast löschen
    def delete_guest(self, guest_id: int) -> None:
        sql = "DELETE FROM guest WHERE guest_id = ?"
        _, _ = self.execute(sql, (guest_id,))