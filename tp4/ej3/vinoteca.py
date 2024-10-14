class Vinoteca:
    # Atributo de clase
    __capacidad_maxima=5000

    # Atrinutos de instacia
    def __init__(self):
        self.cant_jugos=Vinoteca.__capacidad_maxima
        self.cant_blancos=Vinoteca.__capacidad_maxima
        self.cant_tintos_jovenes=Vinoteca.__capacidad_maxima
        self.cant_tintos_anejados=Vinoteca.__capacidad_maxima

    
    #comandos

    def reponer(self, seccion):
    # Al reponer, siempre se llena hasta la capacidad máxima
        if seccion == "jugos":
            self.cant_jugos = Vinoteca.__capacidad_maxima
        elif seccion == "vinos_blancos":
            self.cant_blancos = Vinoteca.__capacidad_maxima
        elif seccion == "vinos_tintos_jovenes":
            self.cant_tintos_jovenes = Vinoteca.__capacidad_maxima
        elif seccion == "vinos_tintos_anejados":
            self.cant_tintos_anejados = Vinoteca.__capacidad_maxima
        else:
            return "Sección no válida."
        

    def vender(self, seccion, cantidad):
        if seccion == "jugos":
            disponible = self.cant_jugos
        elif seccion == "vinos_blancos":
            disponible = self.cant_blancos
        elif seccion == "vinos_tintos_jovenes":
            disponible = self.cant_tintos_jovenes
        elif seccion == "vinos_tintos_anejados":
            disponible = self.cant_tintos_anejados
        else:
            return "Sección no válida."
        
        if cantidad > disponible:
            vendido = disponible
            self.actualizar_seccion(seccion, 0)
            return f"Se vendieron {vendido} unidades. No se pudo completar la venta."
        else:
            self.actualizar_seccion(seccion, disponible - cantidad)
            return f"Se vendieron {cantidad} unidades."
        

    def actualizar_seccion(self,seccion, nueva_cantidad):
          if seccion == "jugos":
            self.cant_jugos= nueva_cantidad
          elif seccion == "vinos_blancos":
            self.cant_blancos= nueva_cantidad
          elif seccion == "vinos_tintos_jovenes":
             self.cant_tintos_jovenes= nueva_cantidad
          elif seccion == "vinos_tintos_anejados":
                self.cant_tintos_anejados= nueva_cantidad
          else:
                return "Sección no válida."
          

    #consultas
    def mostrar_jugos(self):
        return   f"Jugos sin alcohol:  {self.cant_jugos}"
    

    def mostrar_blancos(self):
        return   f"Vinos Blancos:  {self.cant_blancos}"
    
    def mostrar_vinos_jovenes(self):
        return   f"Vinos Jovenes:  {self.cant_tintos_jovenes}"
    
    def mostrar_vinos_anejados(self):
        return   f"Vinos Anejados:  {self.cant_tintos_anejados}"
           