# tester_empleado_modificado.py

from empleado import Empleado  # Asegúrate de importar la clase Empleado

class TesterEmpleadoModificado:
    @staticmethod
    def test():
        # Solicitar al usuario que ingrese el legajo del empleado
        legajo = int(input("Ingrese el legajo del empleado: "))
        
        # Crear una instancia de Empleado utilizando solo el legajo
        empleado = Empleado(legajo)

        # Solicitar al usuario que ingrese las horas trabajadas y el valor por hora
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valor_hora = float(input("Ingrese el valor por hora: "))

        # Modificar los atributos utilizando los métodos
        empleado.establecerHorasTrabajadas(horas_trabajadas)
        empleado.establecerValorHora(valor_hora)

        # Mostrar legajo y sueldo
        print(f"Legajo: {empleado.obtenerLegajo()}")
        print(f"Sueldo: {empleado.obtenerSueldo():.2f}")  # Formato a 2 decimales

# Ejecución de la clase tester
if __name__ == "__main__":
    TesterEmpleadoModificado.test()
