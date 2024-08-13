def validar_cuit(cuit):
    # Validaciones mínimas
    if len(cuit) != 11:
        return False

    # Pesos para el cálculo del dígito verificador
    base = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    # Remover guiones
    cuit = cuit.replace("-", "")

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


# Ejemplo de uso
print(validar_cuit("20245092042"))  # Devuelve True o False dependiendo de la validez del CUIT
