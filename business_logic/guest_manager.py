#Hier später Funktionen bzgl:
#Gäste erstellen und lesen
from data_access import GuestDataAccess
from data_access.Addres_data_access import address_id

# DAO-Instanzen
guest_dao = GuestDataAccess()

def add_new_guest(first_name:str, last_name:str, email:str, street: str, city:str, zip:str) -> Guest:
    address_id = find_address_id(street, city, zip)
    return guest_dao.create_guest(first_name, last_name, email, address_id)

def find_guest_by_email(email:str):
    return guest_dao.get_guest_id_by_email(email)