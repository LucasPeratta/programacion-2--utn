def main():
    # Abrimos el archivo y leemos las distancias
    with open('distancias.txt', 'r') as archivo:
        distancias = archivo.readlines()

    # Convertimos las distancias a números enteros
    distancias = [int(distancia.strip()) for distancia in distancias]

    # Calculamos el promedio de las distancias
    promedio = sum(distancias) / len(distancias)

    # Encontramos las distancias mayores al promedio
    distancias_mayores = [distancia for distancia in distancias if distancia > promedio]

    # Mostramos el promedio y las distancias mayores
    #join toma una lista de cadenas y las une, usando un separador especificado (",")
    print(f"La distancia promedio de los viajes es {promedio}")
    print(f"Los viajes con distancia mayor al promedio son: {', '.join(map(str, distancias_mayores))}")

# Llamar a la función principal
main()
