def esPar(numero):
    if numero % 2 == 0:
        return True

    return False



def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    pares=[numero for numero in lista if esPar(numero)]

    impares=[numero for numero in lista if not esPar(numero)]
    
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    

main()