def main():
    cantidad = int(input("Ingrese la cantidad de notas que desea cargar: "))
    
    notas = []
    
    # Ingresar las notas y agregarlas a la lista
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota numero {i + 1}: "))
        notas.append(nota)
    
    # Buscar la nota más alta
    indice_mayor=0
    mayor=notas[0]
    for i in range(cantidad):
        if notas[i] > mayor:
            mayor=notas[i]
            indice_mayor=i
    
 
    # Mostrar la nota más alta y su índice
    print(f"La nota más alta es {mayor} y se encuentra en el índice {indice_mayor}.")

# Llamar a la función principal
main()
