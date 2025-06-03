# from __future__ import annotations
#
import model
from  import BaseDataAccess
#
#
# class AlbumDataAccess(BaseDataAccess):
#     def __init__(self, db_path: str = None):
#         super().__init__(db_path)
# class AddressDataAccess(BaseDataAccess):
#     det __init__(self, db_path: str = None):
#         super().__init__(db_path)


    # def create_new_album(self, title: str, artist: model.Artist = None) -> model.Album:
    #     sql = """
    #     INSERT INTO Album (Title, ArtistId) VALUES (?, ?)
    #     """
    #     params = (
    #         title,
    #         artist.artist_id if artist else None,
    #     )

            #muss sicher noch angepasst werden
    def create_new_address(self, street: str, city: str, zip: str) -> model.Address:  #State muss eventuell ergänzt werden
        sql = """
        INSERT INTO Address (street, city, zip_code) VALUES (?, ?, ?)
        """
        params = (
            street,
            city,
            zip
        )

         last_row_id, row_count = self.execute(sql, params)
         return model.Address(last_row_id, street, city, zip)

#     def read_album_by_id(self, album_id: int) -> model.Album | None:
#         sql = """
#         SELECT AlbumId, Title FROM Album WHERE AlbumId = ?
#         """
    def read_address_by_id(self, address:id: int) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE address_id = ?
        """
#         params = tuple([album_id])
#         result = self.fetchone(sql, params)
        params = tuple([address_id])
        result = self.fetchone(sql, params)
#         if result:
#             album_id, title = result
#             return model.Album(album_id, title)
        if result:
            address_id, street, city, zip_code = result
            return model.Address(address_id, street, city, zip_code)
#         else:
#             return None
        else:
            return None
#
#     def read_albums_by_artist(self, artist: model.Artist) -> list[model.Album]:
#         sql = """
#         SELECT AlbumId, Title FROM Album WHERE ArtistId = ?
#         """
    def read_address_by_city(self, city: str) -> model.Address | None:
        sql = """
        SELECT address_id, street, city, zip_code FROM Address WHERE city = ?
        """
#         if artist is None:
#             raise ValueError("Artist can not be None")

#
#         params = tuple([artist.artist_id])
#         albums = self.fetchall(sql, params)
#         return [
#             model.Album(album_id, title, artist)
#             for album_id, title in albums
#         ]