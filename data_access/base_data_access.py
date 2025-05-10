import os
import sqlite3

class BaseDataAccess:
    def __init__(self, db_connection_str: str = None):
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE", "database/hotel_reservation_sample.db")
        else:
            self.__db_connection_str = db_connection_str

    def _connect(self):
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()): 
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            result = cur.fetchone()
            cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute(sql, params)
            result = cur.fetchall()
            cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> (int, int):
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
            finally:
                cur.close()
        return cur.lastrowid, cur.rowcount
