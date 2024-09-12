# Solicitar al usuario que ingrese un texto
texto = input("Introduce un texto: ")

# Dividir el texto en palabras usando el método split()
palabras = texto.split()

# Inicializar variables para almacenar la palabra más larga y su longitud
palabra_mas_larga = ""
longitud_maxima = 0

# Recorrer las palabras para encontrar la más larga
for palabra in palabras:
    # Verificar la longitud de la palabra actual
    if len(palabra) > longitud_maxima:
        palabra_mas_larga = palabra
        longitud_maxima = len(palabra)

# Mostrar la palabra más larga y su longitud
print("La palabra más larga es:", palabra_mas_larga)
print("La longitud de la palabra más larga es:", longitud_maxima)
