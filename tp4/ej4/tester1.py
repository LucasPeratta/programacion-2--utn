import random
from automovil import Automovil

class Tester:
    @staticmethod
    def test():
        auto = Automovil("Toyota", "Corolla", 2020, 180)

        iteraciones = int(input("Ingrese la cantidad de iteraciones a realizar: "))


        # Realizar las iteraciones
        for i in range(iteraciones):
            print(f"\nIteración {i+1}")
            operacion = random.randint(0, 3)  # Generar un número aleatorio entre 0 y 3
            
            if operacion == 0:
                # Acelerar en 20 km/h
                print("Operación: Acelerar 20 km/h")
                auto.acelerar(20)
            elif operacion == 1:
                # Desacelerar en 15 km/h
                print("Operación: Desacelerar 15 km/h")
                auto.desacelerar(15)
            elif operacion == 2:
                # Frenar por completo
                print("Operación: Frenar por completo")
                auto.frenar_por_completo()
                print("El automóvil se ha detenido.")
            elif operacion == 3:
                # Calcular el tiempo para llegar a 50 km
                print("Operación: Calcular tiempo para llegar a 50 km")
                tiempo = auto.calcular_minutos_a_destino(50)
                if tiempo:
                    print(f"Tiempo estimado para llegar al destino: {tiempo:.2f} minutos")



# Ejecutar la prueba
Tester.test()