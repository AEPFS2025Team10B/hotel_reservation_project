from data_access.base_data_access import BaseDataAccess
from model.address import Address


class AddressDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def get_address_by_id(self, address_id: int) -> Address | None:
        sql = """
        SELECT address_id, street, city, zip_code
        FROM address
        WHERE address_id = ?
        """
        row = self.fetchone(sql, (address_id,))
        if row:
            return Address(*row)
        return None

    def insert_address(self, street: str, city: str, zip_code: str) -> int:
        sql = """
        INSERT INTO address (street, city, zip_code)
        VALUES (?, ?, ?)
        """
        new_id, _ = self.execute(sql, (street, city, zip_code))
        return Address(new_id, street, city, zip_code)

    def update_address(self, address: Address) -> None:
        sql = """
        UPDATE address
        SET street = ?, city = ?, zip_code = ?
        WHERE address_id = ?
        """
        self.execute(sql, (address.street, address.city, address.zip_code, address.address_id))

    def delete_address(self, address_id: int) -> None:
        sql = "DELETE FROM address WHERE address_id = ?"
        self.execute(sql, (address_id,))
