def main():
    lista = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9, 9]
    
    # Usamos un set para obtener los elementos únicos, ya que set hace de la lista un conjunto, y estos no permiten duplicados
    lista_unicos = list(set([elemento for elemento in lista]))

    print(f"Lista original: {lista}")
    print(f"Lista sin duplicados: {lista_unicos}")

main()
