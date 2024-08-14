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

