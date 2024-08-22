from config.SQLite_DB import Database

data = "../config/iva_data.db"
db = Database(data)

print(data)

with open('ACTIVIDADES_ECONOMICAS_F883.txt', 'r') as archivo:
    lineas = archivo.readlines()

    print(f'Archivo tiene {len(lineas)} lineas')

global count1

for linea in lineas:
    datos = linea.strip().split(';')

    if len(datos) == 3:
        dato1, dato2, dato3 = datos
        count1 += 1
        # Inserta estos valores en tu base de datos
        query = f"INSERT INTO activities_eco_f833(code, description, description_large) VALUES  (?,?,?)"
        values = (dato1, dato2, dato3)

        db.insertRecord(query, values)


    elif len(datos) == 2:
        dato1, dato2 = datos
        # Asigna valores predeterminados o maneja la situación según tus necesidades
        query = f"INSERT INTO activities_eco_f833(code, description, description_large) VALUES  (?,?,?)"
        values = (dato1, dato2, '   ')

        db.insertRecord(query, values)

    # else:
    # Maneja las líneas con un número incorrecto de datos
    # print(f"Línea incorrecta: {linea}")
