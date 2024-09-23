def main():
    with open('datos.txt', 'r') as archivo:
        lineas = [linea.strip() for linea in archivo]
    print(lineas)


main()
