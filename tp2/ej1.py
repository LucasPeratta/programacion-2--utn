def reverso(cadena):
    return cadena[::-1]



def es_palindromo(cadena):
    # Convertimos la cadena a minúsculas para evitar diferencias
    cadena = cadena.lower()
    # Invertimos la cadena usando el procedimiento reverso
    cadena_invertida = reverso(cadena)
    # Comparamos la cadena original con la invertida
    return cadena == cadena_invertida


def main():
    texto = input("Ingrese una cadena: ")
    if es_palindromo(texto):
        print(f'"{texto}" es un palíndromo.')
    else:
        print(f'"{texto}" no es un palíndromo.')


main()