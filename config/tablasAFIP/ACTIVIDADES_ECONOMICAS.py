from config.SQLite_DB import Database

datax = "../iva_data.db"
dbx = Database(datax)

query = """
    CREATE TABLE IF NOT EXISTS sys_activities_eco_f833 (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	code TEXT(6) NOT NULL,
	description TEXT NOT NULL,
	description_large TEXT NOT NULL)
    """
result = dbx.fetchRecord(query)

with open('ACTIVIDADES_ECONOMICAS_F883.txt', 'r', encoding='utf-8') as archivo:
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
            query = f"INSERT INTO activities_eco_f833 (code, description, description_large) VALUES  (?,?,?)"
            values = (dato1, dato2, dato3)

            result = dbx.insertRecord(query, values)

        elif len(datos) == 3:
            dato1, dato2 = datos
            # Asigna valores predeterminados o maneja la situación según tus necesidades
            query = f"INSERT INTO activities_eco_f833(code, description, description_large) VALUES  (?,?,?)"
            values = (dato1, dato2, '   ')

            dbx.insertRecord(query, values)

        else:
            # Maneja las líneas con un número incorrecto de datos
            print(f"Línea incorrecta: {linea}")
        print('-> ', count1)

    print(f'Se agregaron "{count1}" registros a la DB.')
