import string

# Solicitar al usuario que ingrese una oración
oracion = input("Introduce una oración: ")

# a. Número total de caracteres en la oración
num_caracteres = len(oracion)

# b. Cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# Filtrar solo las letras del texto
letras = [caracter for caracter in oracion if caracter.isalpha()]
num_letras = len(letras)

# c. Cantidad de palabras separadas por uno o más espacios
# Dividir la oración en palabras utilizando el método split()
# Este método maneja automáticamente múltiples espacios
palabras = oracion.split()
num_palabras = len(palabras)

# Mostrar los resultados
print("Número total de caracteres en la oración:", num_caracteres)
print("Cantidad total de letras (consonantes y vocales):", num_letras)
print("Cantidad de palabras separadas por uno o más espacios:", num_palabras)
