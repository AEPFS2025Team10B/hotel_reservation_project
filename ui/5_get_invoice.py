from business_logic.invoice_manager import find_invoice_by_booking_id
from business_logic.booking_manager import find_booking_by_id
from business_logic.booking_manager import generate_booking_confirmation

from business_logic.booking_manager import find_bookings_by_email

def main():
    print("📄 View Invoice")
    valid = False
    while not valid:
        choice = input("for coach: Do you want to see what happens if you want to load a Invoice of a canceled booking? (y/n)?")
        if choice.lower() == "y":
            print("enter as booking ID: 4")
            valid = True
        elif choice.lower() == "n":
            valid = True
        else:
            print("Please enter either 'y' or 'n'.")

    booking_input = input("Enter the booking ID (or press Enter if you don't know it): ").strip()

    if booking_input == "":
        email = input("Enter your email address to find your bookings: ").strip()
        bookings = find_bookings_by_email(email)

        if not bookings:
            print("❌ No bookings found for this email.")
            return

        print(f"\n📚 Found {len(bookings)} bookings for {email}:")
        print("-" * 50)
        for b in bookings:
            print(f"Booking ID: {b.booking_id} | Hotel: {b.room.hotel.name} | "
                  f"Room: {b.room.number} | Check-in: {b.check_in_date} | Check-out: {b.check_out_date}")
        print("-" * 50)

        try:
            booking_id = int(input("Enter the Booking ID you want to view the invoice for: ").strip())
        except ValueError:
            print("❌ Invalid booking ID.")
            return
    else:
        try:
            booking_id = int(booking_input)
        except ValueError:
            print("❌ Invalid booking ID.")
            return

    booking = find_booking_by_id(booking_id)
    invoice = find_invoice_by_booking_id(booking_id)

    if not booking or not invoice:
        print(f"\n❌ Booking got cancelled, therefore no invoice")
        booking = find_booking_by_id(booking_id)
        print(f"\n Details of cancelled booking: \n {generate_booking_confirmation(booking)}")
        input(f"\nPress Enter to finish")
        return

    # Print confirmation
    print(generate_booking_confirmation(booking))

    # Print invoice
    print("\n🧾 Invoice")
    print("=" * 40)
    print(f"Invoice ID      : {invoice.invoice_id}")
    print(f"Issue Date      : {invoice.issue_date.strftime('%d.%m.%Y')}")
    print(f"Total Amount    : CHF {invoice.total_amount:.2f}")
    print("=" * 40)
    input(f"\nPress Enter to finish")