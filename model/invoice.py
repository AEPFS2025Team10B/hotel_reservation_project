from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, issue_date: date, total_amount: float):
        self.__invoice_id = invoice_id
        self.issue_date = issue_date
        self.total_amount = total_amount
        self.__booking = None

    def __repr__(self):
        return f"Invoice(id={self.__invoice_id!r}, issue_date={self.__issue_date!r}, total={self.__total_amount!r})"

    @property
    def invoice_id(self):
        return self.__invoice_id

    @property
    def issue_date(self):
        return self.__issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        if not isinstance(issue_date, date):
            raise TypeError("Issue_date must be a datetime.date")
        self.__issue_date = issue_date

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        if not isinstance(total_amount, (int, float)):
            raise TypeError("Total_amount must be a number")
        if total_amount < 0:
            raise ValueError("Total_amount must be non-negative")
        self.__total_amount = total_amount

    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, booking):
        from .booking import Booking
        if not isinstance(booking, Booking):
            raise TypeError("Booking must be a Booking object")
        self.__booking = booking