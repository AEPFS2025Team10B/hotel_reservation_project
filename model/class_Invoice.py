from datetime import date
class Invoice:
    def __init__(self, invoice_id:int, issue_date:date, total_amount:float):
        self.invoice_id = invoice_id
        self.issue_date = issue_date
        self.total_amount = total_amount