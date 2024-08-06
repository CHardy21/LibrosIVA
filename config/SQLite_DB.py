import sqlite3

# ===============================================================================================
#  No olvidar al terminar el codigo de este archivo cerrar la conneccion despues de cada llamada.
# ===============================================================================================
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
        # self.conn.commit()
        rows = self.cur.fetchall()
        return rows

    def insertRecord(self, query):
        self.cur.execute(query)
        self.conn.commit()


    def removeRecord(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateRecord(self, item_name, item_price, purchase_date, rid):
        self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ? WHERE rowid = ?",
                         (item_name, item_price, purchase_date, rid))
        self.conn.commit()

    def __del__(self):
        self.conn.close()