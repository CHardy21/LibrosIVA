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

