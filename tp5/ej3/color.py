class Color:
    def __init__(self, rojo: int = 255, verde: int = 255, azul: int = 255):
        self.__establecer_color(rojo, verde, azul)

    def __establecer_color(self, rojo: int, verde: int, azul: int):
        if not (0 <= rojo <= 255):
            raise ValueError("La intensidad del rojo debe estar entre 0 y 255.")
        if not (0 <= verde <= 255):
            raise ValueError("La intensidad del verde debe estar entre 0 y 255.")
        if not (0 <= azul <= 255):
            raise ValueError("La intensidad del azul debe estar entre 0 y 255.")

        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul

    def variar(self, valor: int):
        self.__rojo = max(0, min(self.__rojo + valor, 255))
        self.__verde = max(0, min(self.__verde + valor, 255))
        self.__azul = max(0, min(self.__azul + valor, 255))

   
    def variarRojo(self, valor: int):
        self.__rojo = max(0, min(self.__rojo + valor, 255))

    def variarVerde(self, valor: int):
        self.__verde = max(0, min(self.__verde + valor, 255))

    def variarAzul(self, valor: int):
        self.__azul = max(0, min(self.__azul + valor, 255))

    def establecer_rojo(self,rojo:int):
        self.__rojo=rojo
       
    def establecer_verde(self,verde:int):
        self.__verde=verde

    def establecer_azul(self,azul:int):
        self.__azul=azul

    def copiar(self, otro_color: 'Color'):
        if not isinstance(otro_color, Color):
            raise ValueError("El parámetro debe ser un objeto de la clase Color.")
        self.__rojo = otro_color.obtener_rojo()
        self.__verde = otro_color.obtener_verde()
        self.__azul = otro_color.obtener_azul()

    def obtener_rojo(self):
        return self.__rojo

    def obtener_verde(self):
        return self.__verde

    def obtener_azul(self):
        return self.__azul

    def esRojo(self) -> bool:
        return self.__rojo == 255 and self.__verde == 0 and self.__azul == 0

    def esGris(self) -> bool:
        return self.__rojo == self.__verde == self.__azul

    def esNegro(self) -> bool:
        return self.__rojo == 0 and self.__verde == 0 and self.__azul == 0

    def complemento(self):
        return Color(255 - self.__rojo, 255 - self.__verde, 255 - self.__azul)

    def esIgualQue(self, otro_color) -> bool:
        return (self.__rojo == otro_color.obtener_rojo() and
                self.__verde == otro_color.obtener_verde() and
                self.__azul == otro_color.obtener_azul())
                

    def clonar(self):
        return Color(self.__rojo, self.__verde, self.__azul)

    def __str__(self):
        return f"Color(R: {self.__rojo}, G: {self.__verde}, B: {self.__azul})"