# Paso 1: Pedir al usuario que ingrese los lados del triángulo
lado1= float(input("Ingrese el primer lado del triangulo: "))
lado2= float(input("Ingrese el segundo lado del triangulo: "))
lado3= float(input("Ingrese el tercer lado del triangulo: "))

# Paso 2: Comparar los lados para determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    print("El triangulo es EQUILATERO")

elif lado1==lado2 or lado1==lado3 or lado2==lado3:
     print("El triángulo es Isósceles (dos lados son iguales).")
     
else:
    print("El triángulo es Escaleno (todos los lados son diferentes).")
