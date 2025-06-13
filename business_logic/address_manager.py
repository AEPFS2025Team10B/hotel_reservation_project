from data_access import AddressDataAccess

# DAO-Instanzen
address_dao = AddressDataAccess()

def add_new_address(street:str, city:str, zip:str):
    return address_dao.insert_address(street, city, zip)

def find_address_id(street: str, city: str, zip: str):
    return address_dao.get_address_id(street, city, zip)

def find_address_by_id(address_id:int):
    return address_dao.get_address_by_id(address_id)