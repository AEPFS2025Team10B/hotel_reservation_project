from data_access.base_data_access import BaseDataAccess
from model import Invoice

class InvoiceDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)

    def create_invoice(self, booking_id: int, issue_date: str, total_amount: float) -> Invoice:
        sql = """
            INSERT INTO invoice ( booking_id, issue_date, total_amount)
            VALUES (?, ?, ?)
            """
        new_id, _ = self.execute(sql, (booking_id, issue_date, total_amount))
        invoice = Invoice(new_id, issue_date, total_amount)
        return invoice

    def get_invoice_by_booking_id(self, booking_id: int) -> Invoice:
        sql = """
               SELECT invoice_id, booking_id, issue_date, total_amount
               FROM invoice
               WHERE booking_id = ?
               """
        row = self.fetchone(sql, (booking_id,))
        if row is None:
            return None
        invoice_id, booking_id, issue_date, total_amount = row
        # TODO: check booking constructor to give more attributes.
        return Invoice(invoice_id, issue_date, total_amount)
