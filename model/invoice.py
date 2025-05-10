from datetime import date
class Invoice:
    def __init__(self, invoice_id:int, issue_date:date, total_amount:float):
        self.__invoice_id = invoice_id
        self.__issue_date = issue_date
        self.__total_amount = total_amount

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
        pass

    @property
    def total_amount(self):
        return self.__total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        pass