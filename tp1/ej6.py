num= int(input("Ingrese un numero entero positivo: "))

while num <= 0:
    print("Por favor, ingresa un número positivo")
    num = int(input("Ingresa un número entero positivo: "))


print("Secuencia de números:")
for i in range(1, num + 1):
    print(i, end=' ')  # 'end' se usa para mostrar los números en la misma línea