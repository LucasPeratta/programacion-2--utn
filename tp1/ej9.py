A = int(input("Ingresa el valor de A (entero positivo): "))
B = int(input("Ingresa el valor de B (entero positivo): "))
X = int(input("Ingresa el valor de X (entero positivo): "))


while A <= 0 or B <= 0 or X <= 0:
    print("Por favor, ingresa solo valores enteros positivos.")
    A = int(input("Ingresa el valor de A (entero positivo): "))
    B = int(input("Ingresa el valor de B (entero positivo): "))
    X = int(input("Ingresa el valor de X (entero positivo): "))


if A > B:
    A, B = B, A  # Intercambiamos los valores para que A sea el menor y B el mayor


    print(f"Múltiplos de {X} entre {A} y {B}:")
for i in range(A, B + 1):
    if i % X == 0:  # Verificamos si i es múltiplo de X
        print(i, end=' ')  # Mostramos el múltiplo