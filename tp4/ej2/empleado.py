class Empleado:
   
    #constructor
    def __init__(self, legajo: int, horasTrabajadasMes: int = 0, valorHora: float = 0.0 ) :
        self.__legajo= legajo
        self.__horasTrabajadasMes= horasTrabajadasMes
        self.__valorHora= valorHora

    #comandos
    
    def establecerHorasTrabajadas(self, cantHoras: int):
        if cantHoras > 0:
            self.__horasTrabajadasMes = cantHoras

        else:
            print("Las horas trabajadas deben ser un número positivo.")

    def establecerValorHora(self, valorHora: float): 
        if valorHora > 0:
            self.__valorHora = valorHora

        else:
            print("El valor por hora debe ser un número positivo.")

    #consultas
            
    def obtenerLegajo(self) -> int:
        return self.__legajo
    
    def obtenerHorasTrabajadas(self) -> int:
        return self.__horasTrabajadasMes
    
    def obtenerValorHora(self) -> float:
        return self.__valorHora
    
    def obtenerSueldo(self) -> float:
        return self.__horasTrabajadasMes * self.__valorHora

    

