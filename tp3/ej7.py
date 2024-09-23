def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    return sum(1 for letra in palabra if letra in vocales)


def main():
    while True:
        palabra = input("Ingrese una palabra (o `salir` para finalizar): ")

        if palabra == "salir":
            break

        cantidad = contar_vocales(palabra)
        print(f"La palabra {palabra} tiene {cantidad} vocales")
    

main()