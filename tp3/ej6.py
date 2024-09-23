def main():
    diccionario={
        "lucas" : 22,
        "franco" : 29,
        "lautaro" : 23,
        "mateo" : 17,
        "gian" : 17
    }

    mayores=[persona for persona, edad in diccionario.items() if edad >= 18]

    print(mayores)

main()  