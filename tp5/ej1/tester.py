class Tester:
    @staticmethod
    def probar_atleta():
        # Crear algunos atletas
        atleta1 = Atleta("Juan")
        atleta2 = Atleta("Ana")
        
        # Probar el estado inicial
        print(atleta1)
        print(atleta2)

        # Probar entrenar
        for i in range(6):  # Entrenar 6 veces
            print(atleta1.entrenar())
            print(f"Energía de {atleta1.nombre}: {atleta1.energia}")
            print(f"Destreza de {atleta1.nombre}: {atleta1.destreza}")

        # Probar descansar
        print(atleta1.descansar())
        print(f"Energía de {atleta1.nombre} tras descansar: {atleta1.energia}")

        # Comparaciones de destreza
        print(f"{atleta1.nombre} tiene la misma destreza que {atleta2.nombre}: {atleta1.mismaDestrezaQue(atleta2)}")
        print(f"{atleta1.nombre} tiene mayor destreza que {atleta2.nombre}: {atleta1.mayorDestrezaQue(atleta2)}")
      

# Ejecutar las pruebas
Tester.probar_atleta()
