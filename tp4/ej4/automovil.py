class Automovil:
     
    def __init__(self, marca, modelo, anio, velocidad_maxima):
        self.marca = marca                  
        self.modelo = modelo                
        self.anio = anio               
        self.velocidad_maxima = velocidad_maxima  
        self.velocidad_actual = 0 


    def establecer_marca(self, marca):
         self.marca= marca

    def establecer_modelo(self, modelo):
         self.modelo= modelo

    def establecer_anio(self, anio):
         self.anio= anio
         
    def establecer_velocidad_maxima(self, velocidad_maxima):
         self.velocidad_maxima= velocidad_maxima
         
    def establecer_velocidad_actual(self, velocidad_actual):
         self.velocidad_actual= velocidad_actual


    def acelerar(self, aumento):
         nueva_velocidad = self.velocidad_actual + aumento
         if nueva_velocidad > self.velocidad_maxima:
             print(f"Se alcanzó la velocidad máxima: {self.velocidad_maxima} km/h")

         else:
            self.velocidad_actual = nueva_velocidad
            print(f"Velocidad actual: {self.velocidad_actual} km/h")    


    def desacelerar(self, decremento):
        nueva_velocidad = self.velocidad_actual - decremento
        
        # Asegurarse de que no baje de cero
        if nueva_velocidad < 0:
            self.velocidad_actual = 0
            print("El automóvil se ha detenido.")
        else:
            self.velocidad_actual = nueva_velocidad
            print(f"Velocidad actual después de desacelerar: {self.velocidad_actual} km/h")


    def frenar_por_completo(self):
        self.establecer_velocidad_actual(0)
        print(f"El auto se ha detenido")


    def obtener_marca(self):
        return self.marca
    
    def obtener_modelo(self):
        return self.modelo
    
    def obtener_anio(self):
        return self.anio
    
    def obtener_velocidad_max(self):
        return self.velocidad_maxima
    
    def obtener_velocidad_actual(self):
        return self.velocidad_actual
    
    def calcular_minutos_a_destino(self,distanciaKm:float):
        if self.velocidad_actual==0:
            print(f"El auto se encuentra detenido")
        else:
           return distanciaKm / self.velocidad_actual * 60