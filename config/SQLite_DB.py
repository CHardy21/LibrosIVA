import sqlite3
# import sys
# import traceback


def error_mng(e):
    print("DB Error: ", e)
    return e


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()

    def selectRecord(self, query):
        with self.conn:
            self.conn.row_factory = sqlite3.Row  # Para obtener los resultados como diccionarios
            self.cur.execute(query)
            # Obtén los nombres de las columnas
            column_names = [description[0] for description in self.cur.description]
            # Construye los diccionarios manualmente
            result = [dict(zip(column_names, row)) for row in self.cur.fetchall()]
            return result

    def searchRecords(self, query, value=''):
        with self.conn:
            self.cur.execute(query, value)
            self.conn.commit()
            rows = self.cur.fetchall()
            return rows

    def fetchRecord(self, query, value):
        with self.conn:
            self.cur.execute(query, value)
            self.conn.commit()
            row = self.cur.fetchone()
            return row

    def fetchRecords(self, query, value):
        with self.conn:
            self.cur.execute(query, value)
            self.conn.commit()
            rows = self.cur.fetchall()
            return rows

    def fetchRecords2(self, query, value=None):
        with self.conn:
            self.cur.execute(query, value)
            self.conn.commit()
            rows = self.cur.fetchall()
            return rows

    def insertRecord(self, query, values):
        with self.conn:
            """
            Ejecuta una consulta SQL para insertar datos en la base de datos.
            Args:
                query (str): Consulta SQL con marcadores de posición (?).
                values (tuple): Tupla de valores a insertar en la consulta.
            Returns:
                None
            """
            try:
                self.cur.execute(query, values)
                self.conn.commit()
                return True
            except sqlite3.Error as e:
                error_mng(e)

    def removeRecord(self, query):
        with self.conn:
            try:
                print(query)
                self.cur.execute(query)
                self.conn.commit()
                print("DB: Registro Eliminado correctamente.")
                return True
            except sqlite3.Error as e:
                error_mng(e)

    def updateRecord(self, query, values):
        with self.conn:
            try:
                print("=> ", query)
                self.cur.execute(query, values)
                self.conn.commit()
                print("Registro Actualizado correctamente.")
                return True
            except sqlite3.Error as e:
                print(f"Error al Actualizar el registro: {e}")
                error_mng(e)
