ancho = int(input("Ingresa el ancho del rectángulo (máximo 40): "))
alto = int(input("Ingresa el alto del rectángulo: "))

while (ancho > 40):
    print("El ancho no puede ser mayor que 40.")
    ancho = int(input("Ingresa el ancho del rectángulo (máximo 40): "))

print(f"Dibujando un rectángulo de {ancho}x{alto}")
for i in range(alto):
    print('*' * ancho)