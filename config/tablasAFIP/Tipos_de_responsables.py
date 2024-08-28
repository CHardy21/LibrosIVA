from config.SQLite_DB import Database

data = "../iva_data.db"
db = Database(data)

query = """
    CREATE TABLE IF NOT EXISTS sys_type_taxpayer (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    code TEXT(3) NOT NULL,
    description TEXT NOT NULL)
    """
result = db.fetchRecord(query)

with open('Tipos_de_responsables.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()

    print(f'Archivo tiene {len(lineas)} lineas')

    count1 = 0

    for linea in lineas:
        datos = linea.strip().split('\t')
        # print(datos, ' => ', len(datos))

        if len(datos) == 4:
            dato1, dato2, dato3, dato4 = datos
            count1 += 1
            # Inserta estos valores en tu base de datos
            query = f"INSERT INTO sys_type_taxpayer (code, description) VALUES  (?,?)"
            values = (dato1, dato2)

            result = db.insertRecord(query, values)
        elif len(datos) == 3:
            dato1, dato2 = datos
            count1 += 1
            # Inserta estos valores en tu base de datos
            query = f"INSERT INTO sys_type_taxpayer (code, description) VALUES  (?,?)"
            values = (dato1, dato2)

            result = db.insertRecord(query, values)

        elif len(datos) == 2:
            dato1, dato2 = datos
            count1 += 1
            # Asigna valores predeterminados o maneja la situación según tus necesidades
            query = f"INSERT INTO sys_type_taxpayer (code, description) VALUES  (?,?)"
            values = (dato1, dato2)

            db.insertRecord(query, values)

        else:
            # Maneja las líneas con un número incorrecto de datos
            print(f"Línea incorrecta: {linea}")
        print('-> ', count1)

    print(f'Se agregaron "{count1}" registros a la DB.')
