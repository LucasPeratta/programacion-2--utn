# Paso 1: Pedir al usuario cuántos valores desea ingresar
cantidad_valores = int(input("¿Cuántos valores deseas ingresar? "))

# Paso 2: Validar que la cantidad de valores sea positiva
while cantidad_valores <= 0:
    print("Por favor, ingresa una cantidad positiva de valores.")
    cantidad_valores = int(input("¿Cuántos valores deseas ingresar? "))

suma_total = 0

# Paso 3: Pedir los valores y calcular la suma
for i in range(cantidad_valores):
    valor = float(input(f"Ingrese el valor {i + 1}: "))  # Pedir cada valor
    suma_total += valor  # Sumar cada valor


promedio = suma_total / cantidad_valores

# Paso 4: Mostrar la suma y el promedio
print(f"La suma de los {cantidad_valores} valores es: {suma_total}")
print(f"El promedio es: {promedio}")