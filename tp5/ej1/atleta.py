class Atleta: 
    __max_valor=100
    __min_valor=0

    def __init__(self,nombre:str):
        self.__nombre=nombre
        self.__energia=self.__max_valor
        self.__destreza=0
        self.__entrenamientos=0


    def entrenar(self):
        if self.__energia < 5:
            return (f"{self.__nombre} no puede enttrenar por falta de energia, necesita descansar.")

        else: 
            self.__energia-=5
            self.__entrenamientos+=1

            if self.__entrenamientos==5:
                self.__entrenamientos=0
                self.__destreza+=1
                return (f"Entrenamiento de {self.__nombre} completado con éxito. ¡Destreza mejorada!")

            return (f"Entrenamiento de {self.__nombre} completado con exito")


    def descansar(self):
        if self.__energia==100:
            return (f"{self.__nombre} no necesita descansar, su energia esta al maximo!")

        else:
            self.__energia = min(self.__energia + 20, 100)
            return (f"{self.__nombre} descanso correctamente, y ahora su energia esta en {self.__energia} !!")



    def mismaDestrezaQue(self, otro_atleta) -> bool:
        return self.__destreza == otro_atleta.destreza


    def mayorDestrezaQue(self, otro_atleta) -> bool:
        return self.__destreza > otro_atleta.destreza

    
    def __str__(self):
    return f"Atleta: {self.__nombre}, Energía: {self.__energia}, Destreza: {self.__destreza}, Entrenamientos: {self.__entrenamientos}"
