from empleado import Empleado

class TesterEmpleado:
    @staticmethod
    def test():
        # Solicitar al usuario que ingrese los datos del empleado
        legajo = int(input("Ingrese el legajo del empleado: "))
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valor_hora = float(input("Ingrese el valor por hora: "))

        # Crear una instancia de Empleado utilizando el constructor
        empleado = Empleado(legajo, horas_trabajadas, valor_hora)

        # Mostrar legajo y sueldo
        print(f"Legajo: {empleado.obtenerLegajo()}")
        print(f"Sueldo: {empleado.obtenerSueldo():.2f}")  # Formato a 2 decimales

# Ejecución de la clase tester
if __name__ == "__main__":
    TesterEmpleado.test()
