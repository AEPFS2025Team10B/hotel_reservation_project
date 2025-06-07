from business_logic import invoice_manager

def main():
    print("Get invoice")
    booking_id = int(input("Please enter the booking id you would like to get the invoice from: "))
    customer_invoice = invoice_manager.find_invoice_by_booking_id(booking_id)
    print(customer_invoice)