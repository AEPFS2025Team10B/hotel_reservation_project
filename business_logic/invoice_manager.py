
from business_logic import booking_manager
from data_access.invoice_data_access import InvoiceDataAccess
invoice_dao = InvoiceDataAccess()

def create_invoice_by_booking_id(booking_id: int):
    booking = booking_manager.find_booking_by_id(booking_id)
    booking_id = booking.booking_id
    issue_date = booking.check_out_date
    total_amount = booking.total_amount
    invoice = invoice_dao.create_invoice(booking_id, issue_date, total_amount)
    invoice.booking
    return invoice
