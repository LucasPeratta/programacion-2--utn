char= input("Ingrese un caracter: ")
cantidad= int(input("Ingrese la cantidad de repeticiones: "))
if cantidad < 0:
    print("El número debe ser un número natural (no negativo).")
else:
    # Repetir el carácter N veces y mostrar el resultado
    resultado = char * cantidad
    print(resultado)