
cont=0
suma=0
num=int(input("Ingrese un numero positivo para calcular el promedio (o num negativo para finalizar): "))


while (num >= 0):
    cont+=1
    suma+=num
    num=int(input("Ingrese un numero positivo para calcular el promedio (o num negativo para finalizar): "))



if cont > 0:
    promedio = suma / cont  
    print(f"El promedio es: {promedio} con un total de {cont} ingresos.")
else:
    print("No se ingresaron números positivos.")