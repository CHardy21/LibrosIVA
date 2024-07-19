class DB:
    DATABASE = 'iva_dat.db'
    USERNAME = 'root'
    PASSWORD = ''
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def conexion(self):
        pass