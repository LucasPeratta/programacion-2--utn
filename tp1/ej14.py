# Solicitar al usuario que ingrese un texto
texto = input("Introduce un texto: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Inicializar el contador de vocales
contador_vocales = 0

# Contar las vocales en el texto
for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

# Mostrar el resultado
print("La cantidad total de vocales en el texto es:", contador_vocales)
