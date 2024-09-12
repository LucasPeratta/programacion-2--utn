def main():
    while True:
        num = input("Ingrese un número: ")
        if num.isdigit():
            break
        else:
            print("Error: Debe ingresar un número válido.")
    
    digitos = [int(d) for d in num]
    
    # Buscar el índice que contiene el dígito mayor
    digito_mayor = digitos[0]
    indice_mayor = 0
    
    for i in range(1, len(digitos)):
        if digitos[i] > digito_mayor:
            digito_mayor = digitos[i]
            indice_mayor = i
    
    # Mostrar el índice del dígito mayor
    print(f"El dígito mayor es {digito_mayor} y se encuentra en el índice {indice_mayor}.")

# Llamar a la función principal
main()
