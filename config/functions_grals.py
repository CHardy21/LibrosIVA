

def verificar_cuit(cuit: str) -> int:
    # Elimina los guiones si están presentes
    cuit = cuit.replace("-", "")

    # Verifica que el CUIT tenga 11 dígitos
    if len(cuit) != 11:
        return -1  # CUIT inválido

    # Calcula la suma ponderada
    suma_ponderada = 0
    for i, digito in enumerate(cuit[:-1]):
        peso = 2 if i % 2 == 0 else 1
        suma_ponderada += int(digito) * peso

    # Calcula el dígito verificador
    residuo = suma_ponderada % 10
    digito_verificador = 10 - residuo if residuo != 0 else 0

    # Compara el dígito verificador calculado con el proporcionado
    if digito_verificador == int(cuit[-1]):
        return digito_verificador
    else:
        return -1  # CUIT inválido

# Ejemplo de uso
# cuit_ingresado = "20-12345678-9"
# resultado = verificar_cuit(cuit_ingresado)
# if resultado != -1:
#     print(f"El CUIT {cuit_ingresado} es válido.")
# else:
#     print(f"El CUIT {cuit_ingresado} es inválido.")
