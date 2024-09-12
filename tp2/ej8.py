# Función para cargar productos desde el archivo productos.txt en un diccionario
def cargar_productos():
    productos = {}
    with open('productos.txt', 'r') as file:
        for linea in file:
            codigo, nombre, precio = linea.strip().split(';')
            productos[codigo] = (nombre, float(precio))  # Guardar nombre y precio usando código como clave
    return productos

# Función para cargar el stock desde el archivo stock.txt
def cargar_stock():
    stock = {}
    with open('stock.txt', 'r') as file:
        for linea in file:
            codigo, stock_minimo, stock_real = linea.strip().split(';')
            stock[codigo] = (int(stock_minimo), int(stock_real))  # Guardar stock mínimo y real usando código como clave
    return stock


# Función para generar el archivo Compras.txt con productos cuyo stock real está por debajo del mínimo
def generar_compras(productos, stock):
    with open('Compras.txt', 'w') as file:
        for codigo, (stock_minimo, stock_real) in stock.items():
            if stock_real < stock_minimo:
                if codigo in productos:
                    nombre, precio = productos[codigo]
                    file.write(f"{codigo};{nombre};{precio};{stock_real}\n")



def main():
    # Cargar productos y stock desde los archivos
    productos = cargar_productos()
    stock = cargar_stock()

    # Generar el archivo Compras.txt
    generar_compras(productos, stock)
    print("El archivo Compras.txt ha sido generado con los productos cuyo stock está por debajo del mínimo.")

main()