class Especie:
    def __init__(self, nombre: str):
        if not isinstance(nombre, str) or not nombre:
            raise ValueError("El nombre científico debe ser una cadena no vacía.")
        
        self.__nombre = nombre  # Nombre científico de la especie
        self.__machos = 0        # Inicialmente, la cantidad de machos es 0
        self.__hembras = 0       # Inicialmente, la cantidad de hembras es 0
        self.__ritmo = 0.0       # Ritmo de crecimiento inicial en 0


    def establecerMachos(self):
        cantidad = -1 
        while cantidad < 0:
            cantidad = int(input("Ingrese la cantidad de machos (no negativo): "))
            if cantidad < 0:
                print("La cantidad de machos no puede ser negativa. Intente de nuevo.")
            
        self.__machos = cantidad  


    def establecerHembras(self):
        cantidad = -1 
        while cantidad < 0:
            cantidad = int(input("Ingrese la cantidad de hembras (no negativo): "))
            if cantidad < 0:
                print("La cantidad de hembras no puede ser negativa. Intente de nuevo.")
            
        self.__hembras = cantidad     


    def actualizarMachos(self, cantidad: int):
        self.__machos += cantidad  # Sumar la cantidad al número de machos
        if self.__machos < 0:
            self.__machos = 0  # Asegurarse de que no sea menor que 0
        else:
            print("La cantidad de machos no puede ser negativa. Intente de nuevo.")
            

    def actualizarHembras(self, cantidad: int):
        self.__hembras += cantidad  # Sumar la cantidad al número de hembras
        if self.__hembras < 0:
            self.__hembras = 0  # Asegurarse de que no sea menor que 0
        else:
            else:
            print("La cantidad de machos no puede ser negativa. Intente de nuevo.")