numeros = []

# Solicitar números al usuario
num = int(input("Ingresa un número entero positivo (o 0 para finalizar): "))

while num != 0:    
    numeros.append(num)
    num = int(input("Ingresa otro número entero positivo (o 0 para finalizar): "))


# Verificamos si la lista está vacía
if len(numeros) == 0:
    print("No se ingresaron números.")
else:
     if numeros == sorted(numeros):
          print("La secuencia está ordenada de menor a mayor.")
     else:
        print("La secuencia no está ordenada de menor a mayor.")