def main():
    # Diccionario de ejemplo de palabras y sus definiciones
    diccionario = {
        'apple': 'a fruit',
        'banana': 'another fruit',
        'apricot': 'yet another fruit',
        'berry': 'a small fruit',
        'avocado': 'a green fruit',
    }

    letra = input("Ingrese una letra para filtrar las palabras: ").lower()

    palabras_filtradas = [palabra for palabra in diccionario if palabra.startswith(letra)]

    print(palabras_filtradas)


main()
