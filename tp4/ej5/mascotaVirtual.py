class MascotaVirtual:
    __max_valor=100
    __min_valor=0

    def __init__(self,nombre:str):
        self.nombre=nombre
        self.higiene=self.__max_valor
        self.energia=self.__max_valor
        self.diversion=self.__max_valor
        self.dormido=False
        self.cant_actividades_desgaste = 0
        self.esta_vivo=True



    def _verificar_vivo(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede realizar la acción porque ha dejado de existir.")
            return False
        return True

    #comandos
    def comer(self):
        if self._verificar_vivo():
            self.aumentar_estado(20,"energia")        

    def beber(self):
        if self._verificar_vivo():
            self.aumentar_estado(10,"energia")       

    def dormir(self):
        if self._verificar_vivo():
            self.dormido=True
            self.aumentar_estado(20,"energia")        
            self.reducir_estado(10,"diversion")

    def despertar(self):
        if self._verificar_vivo():
            self.dormido=False       

    def jugar(self):
        if self._verificar_vivo():
            self.aumentar_estado(40,"diversion")
            self.reducir_estado(20,"energia")    
            self.reducir_estado(15,"higiene")

    def caminar(self):
        if self._verificar_vivo():
            self.aumentar_estado(20,"diversion")
            self.reducir_estado(10,"energia")    
            self.reducir_estado(8,"higiene")

    def saltar(self):
        if self._verificar_vivo():
            self.aumentar_estado(10,"diversion")
            self.reducir_estado(15,"energia")    
            self.reducir_estado(10,"higiene")

    def baniar(self):
        if self._verificar_vivo():    
            self.aumentar_estado(40,"higiene")
            self.reducir_estado(10,"diversion")
            

    def aumentar_estado(self,valor,estado):
        if estado=="energia":
            self.energia+=valor
            if self.energia > self.__max_valor:
                self.energia = self.__max_valor

        elif estado=="higiene":
            self.higiene+=valor
            if self.higiene > self.__max_valor:
                self.higiene = self.__max_valor

        elif estado=="diversion":
            self.diversion+=valor
            if self.diversion > self.__max_valor:
                self.diversion = self.__max_valor


    def reducir_estado(self,valor,estado):
        if estado=="energia":
            self.energia-=valor
            if self.energia <= self.__min_valor:
                print(f"{self.nombre} ha dejado de existir debido a falta de energía.")
                self.esta_vivo="false"
                return  

        elif estado=="higiene":
            self.higiene-=valor
            if self.higiene < self.__min_valor:
                self.higiene = self.__min_valor

        elif estado=="diversion":
            self.diversion-=valor
            if self.diversion < self.__min_valor:
                self.diversion = self.__min_valor


    #consultas
    def obtener_nombre(self):
        return self.nombre
    
    def obtener_energia(self):
        return self.energia

    def obtener_higiene(self):
        return self.higiene

    def obtener_diversion(self):
        return self.diversion
    
    def esta_dormido(self):
        if self.dormido==True:
            return (f"{self.nombre} esta dormido")
        else:
            return (f"{self.nombre} no esta dormido")


    def esta_vivo(self):
            if self.esta_vivo==True:
                return (f"{self.nombre} esta vivo")
            else:
                return (f"{self.nombre} no esta vivo")
            


    def obtener_humor(self):
        # Contar cuántos estados están dentro de los rangos específicos
        estados = [self.energia, self.diversion, self.higiene]
        
        feliz = sum(1 for x in estados if x > 70)
        alegre = sum(1 for x in estados if 50 <= x <= 70)
        neutral = sum(1 for x in estados if 30 <= x < 50)
        triste = sum(1 for x in estados if 10 <= x < 30)
        muy_triste = sum(1 for x in estados if x < 10)

        # Determinar el humor de la mascota
        if feliz == 3:
            return "Feliz"
        elif alegre >= 2:
            return "Alegre"
        elif neutral >= 2:
            return "Neutral"
        elif triste >= 2:
            return "Triste"
        elif muy_triste >= 2:
            return "Muy Triste"
        else:
            return "Indefinido"