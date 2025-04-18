from config.SQLite_DB import Database

data = "../iva_data.db"
db = Database(data)

query = """
    CREATE TABLE IF NOT EXISTS sys_opcode (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    code TEXT(2) NOT NULL,
    desc_buy TEXT NOT NULL,
    desc_sell TEXT NOT NULL
    )
    """
result = db.fetchRecord(query)

with open('codigo_operacion.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

    print(f'Archivo tiene {len(lineas)} lineas')

    count1 = 0

    for linea in lineas:
        datos = linea.strip().split(';')
        # print(datos, ' => ', len(datos))

        if len(datos) == 4:
            dato1, dato2, dato3, dato4 = datos
            count1 += 1
            # Inserta estos valores en tu base de datos
            query = f"INSERT INTO sys_opcode (code, desc_buy, desc_sell) VALUES  (?,?,?)"
            values = (dato1, dato2, dato3)

            result = db.insertRecord(query, values)
        elif len(datos) == 3:
            dato1, dato2, dato3 = datos
            count1 += 1
            # Inserta estos valores en tu base de datos
            query = f"INSERT INTO sys_opcode (code, desc_buy, desc_sell) VALUES  (?,?,?)"
            values = (dato1, dato2, dato3)

            result = db.insertRecord(query, values)

        elif len(datos) == 2:
            dato1, dato2, dato3 = datos
            count1 += 1
            # Inserta estos valores en tu base de datos
            query = f"INSERT INTO sys_opcode (code, desc_buy, desc_sell) VALUES  (?,?,?)"
            values = (dato1, dato2, '')

            db.insertRecord(query, values)

        else:
            # Maneja las líneas con un número incorrecto de datos
            print(f"Línea incorrecta: {linea}")
        print('-> ', count1)

    print(f'Se agregaron "{count1}" registros a la DB.')
