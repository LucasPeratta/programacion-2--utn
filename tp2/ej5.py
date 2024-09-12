def main():
    alumnos = []
    
    # Cargar la lista de alumnos y sus notas
    while True:
        nombre = input("Ingrese el nombre del alumno (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':           
            break
        
        # Validar que se ingrese una nota
        while True:
            try:
                nota = float(input(f"Ingrese la nota de {nombre}: "))
                alumnos.append({"nombre": nombre, "nota": nota})                
                break
            except ValueError:
                print("Error: Debe ingresar un número válido para la nota.")
        
       
    
    # Mostrar el resultado
    print("\nALUMNOS  PARCIAL  RESULTADO")
    for alumno in alumnos:
        resultado = "Aprobado" if alumno["nota"] >= 40 else "Desaprobado"
        print(f"{alumno['nombre']}  {alumno['nota']}  {resultado}")

# Llamar a la función principal
main()
