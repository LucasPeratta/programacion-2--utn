def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    inicio = int(input("Ingrese el número de inicio del rango: "))
    fin = int(input("Ingrese el número final del rango: "))

    # Creamos una lista con los números primos dentro del rango
    primos = [num for num in range(inicio, fin + 1) if es_primo(num)]

    # Imprimimos la lista de números primos
    print(f"Números primos entre {inicio} y {fin}: {primos}")

# Llamamos a la función main
if __name__ == '__main__':
    main()
