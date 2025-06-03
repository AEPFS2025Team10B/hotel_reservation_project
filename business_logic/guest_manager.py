#Hier später Funktionen bzgl:
#Gäste erstellen und lesen
from data_access import GuestDataAccess

# DAO-Instanzen
guest_dao = GuestDataAccess()

def add_new_guest(first_name:str, last_name:str, email:str):
    return guest_dao.create_guest(first_name, last_name, email)

def find_guest_by_email(email:str):
    return guest_dao.get_guest_by_email(email)