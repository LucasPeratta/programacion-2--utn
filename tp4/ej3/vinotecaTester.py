from vinoteca import Vinoteca

class TesterVinoteca:
    @staticmethod
    def test():     
        vinoteca = Vinoteca()

        # Mostrar el estado inicial
        print("Estado inicial:")
        print(vinoteca.mostrar_jugos())
        print(vinoteca.mostrar_blancos())
        print(vinoteca.mostrar_vinos_jovenes())
        print(vinoteca.mostrar_vinos_anejados())
        print()

        # Probar la venta
        cantidad_venta_jugos = int(input("Ingrese la cantidad de jugos a vender: "))
        cantidad_venta_blancos = int(input("Ingrese la cantidad de vinos blancos a vender: "))
        
        print(vinoteca.vender("jugos", cantidad_venta_jugos))
        print(vinoteca.vender("vinos_blancos", cantidad_venta_blancos))

        print(vinoteca.mostrar_jugos())
        print(vinoteca.mostrar_blancos())




# Ejecutar la prueba
TesterVinoteca.test()