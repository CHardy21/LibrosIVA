# Verificar si coneccion esta abierta o cerrada en cada consulta.
Para asegurarte de que la conexión a la base de datos se verifica y se cierra correctamente en cada consulta, puedes utilizar un contexto de administrador (context manager) con la declaración with. Esto garantiza que la conexión se cierre automáticamente después de que se complete el bloque de código, incluso si ocurre una excepción.
```Python
class Database: 
    def __init__(self, db): 
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        ...

    def searchRecords(self, query, value=''):
        with self.conn:
            self.cur.execute(query, value)
            self.conn.commit()
            rows = self.cur.fetchall()
```
* Contexto de administrador (with): \
Al usar with sqlite3.conn('db') as conn:, la conexión se abre al inicio del bloque y se cierra automáticamente al final del bloque, sin importar si el bloque se ejecuta correctamente o si se lanza una excepción.
* Eliminación de conn.close(): \
No necesitas llamar a conn.close() explícitamente, ya que el contexto de administrador se encarga de cerrar la conexión por ti.