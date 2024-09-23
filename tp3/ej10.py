def obtenerNombres(estudiantes):
    nombres=[estudiante["nombre_apellido"] for estudiante in estudiantes]
    return nombres

def obtenerAprobados(estudiantes):
    return [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] > 70 and estudiante["nota_parcial2"] > 70]

def obtenerDesaprobados(estudiantes):
    return [estudiante["nombre_apellido"] for estudiante in estudiantes if estudiante["nota_parcial1"] < 60 or estudiante["nota_parcial2"] < 60 ]

def main():
    estudiantes = [
    {'nombre_apellido': 'Pepe Gómez', 'legajo': 101, 'nota_parcial1': 75, 'nota_parcial2': 80, 'nota_final': 85},
    {'nombre_apellido': 'María Pérez', 'legajo': 102, 'nota_parcial1': 90, 'nota_parcial2': 92, 'nota_final': 88},
    {'nombre_apellido': 'Pedro Díaz', 'legajo': 103, 'nota_parcial1': 58, 'nota_parcial2': 65, 'nota_final': 60},
    {'nombre_apellido': 'Ana López', 'legajo': 104, 'nota_parcial1': 45, 'nota_parcial2': 50, 'nota_final': 55}
    ]

    nombres= obtenerNombres(estudiantes)
    aprobados= obtenerAprobados(estudiantes)
    desaprobados= obtenerDesaprobados(estudiantes)

    print("Nombres de todos los estudiantes:", nombres)
    
    print("Estudiantes con promedio superior a 70:", aprobados)
    
    print("Estudiantes con calificaciones inferiores a 60 en al menos un examen:", desaprobados)



main()