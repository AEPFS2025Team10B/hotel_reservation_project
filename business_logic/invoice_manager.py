
from business_logic import booking_manager
from data_access.invoice_data_access import InvoiceDataAccess
from model.invoice import Invoice

invoice_dao = InvoiceDataAccess()

def create_invoice_by_booking_id(booking_id: int) -> Invoice:
    booking = booking_manager.find_booking_by_id(booking_id)
    if not booking:
        raise ValueError(f"No booking found with ID {booking_id}")
    
    total_amount = booking.total_price
    issue_date = booking.check_out_date.strftime("%Y-%m-%d")
    invoice = invoice_dao.create_invoice(booking_id, issue_date, total_amount)
    invoice.booking = booking
    return invoice

def find_invoice_by_booking_id(booking_id: int):
    booking = booking_manager.find_booking_by_id(booking_id)
    if not booking:
        return None

    invoice = invoice_dao.get_invoice_by_booking_id(booking.booking_id)
    if invoice:
        invoice.booking = booking
    return invoice

def delete_invoice_by_booking_id(booking_id: int):
    return invoice_dao.delete_invoice(booking_id)
