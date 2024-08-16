import sqlite3
import sys
import traceback


# ===============================================================================================
#  No olvidar al terminar el codigo de este archivo cerrar la conneccion despues de cada llamada.
# ===============================================================================================
def error_mng(e):
    print("DB Error: ", e)
    return e


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        # self.cur.execute(
        #      "CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date)")
        # self.conn.commit()

    def selectRecord(self, query):
        self.conn.row_factory = sqlite3.Row  # Para obtener los resultados como diccionarios
        self.cur.execute(query)
        # Obtén los nombres de las columnas
        column_names = [description[0] for description in self.cur.description]
        # Construye los diccionarios manualmente
        result = [dict(zip(column_names, row)) for row in self.cur.fetchall()]

        return result

    def fetchRecord(self, query):
        self.cur.execute(query)
        self.conn.commit()
        row = self.cur.fetchone()
        return row

    def fetchRecords(self, query):
        self.cur.execute(query)
        self.conn.commit()
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, query, values):
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
            print("Registro insertado correctamente.")
            return True
        except sqlite3.Error as e:
            print(f"Error al insertar el registro: {e}")
            return False, e

    def removeRecord(self, query):
        try:
            print(query)
            self.cur.execute(query)
            self.conn.commit()
            print("DB: Registro Eliminado correctamente.")

        except sqlite3.Error as e:
            # print(f"DB Error: {e}")
            error_mng(e)

    def updateRecord(self, query, values):
        try:
            print("=> ", query)
            self.cur.execute(query, values)
            self.conn.commit()
            print("Registro Actualizado correctamente.")
            return True
        except sqlite3.Error as e:
            print(f"Error al Actualizar el registro: {e}")
            error_mng(e)

    def __del__(self):
        self.conn.close()
