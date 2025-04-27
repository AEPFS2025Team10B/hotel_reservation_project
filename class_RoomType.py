class RoomType:
    def __init__(self, room_type_id:int, name:str, description:str, max_guest:int):
        self.room_type_id = room_type_id
        self.name = name
        self.description = description
        self.max_guest = max_guest