def validate_txt(value, min, max, type):
    validate = False
    if min <= len(value) <= max:
        validate = True
    return validate


# Función para validar el string
def validar_string(s, caracteres):
    if len(s) < 1:
        return False
    caracteres_permitidos = set(caracteres)
    return set(s).issubset(caracteres_permitidos)


def validar_cuit(cuit):
    # Remover guiones
    cuit = cuit.replace("-", "")

    # Validaciones mínimas
    if len(cuit) != 11:
        return False

    # Pesos para el cálculo del dígito verificador
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    # Calcular el dígito verificador
    aux = 0
    for i in range(10):
        aux += int(cuit[i]) * base[i]

    aux = 11 - (aux % 11)
    if aux == 11:
        aux = 0
    if aux == 10:
        aux = 9

    return aux == int(cuit[10])


def validate_codActividad(db, record):
    print(record)
    value = (record,)
    query = "SELECT * FROM sys_activities_eco_f833 WHERE code = ?"
    result = db.fetchRecord(query, value)
    print("DB Valor devuelto: ", result)
    if result:
        print('True')
        return True
    else:
        return False


def validate_condIVA(db, record):
    print(record)
    value = (record,)
    query = "SELECT * FROM tax_status WHERE code = ?"
    result = db.fetchRecord(query, value)
    print("DB Valor devuelto: ", result)
    if result:
        print('True')
        return True
    else:
        return False

def verificar_rango(dato, rango):
    try:
        numero = int(dato)
        if rango[0] < numero < rango[1]:
            return True
        else:
            return False
    except ValueError:
        return False