# Función para leer los productos del archivo productos.txt y cargarlos en un diccionario
def cargar_productos():
    productos = {}
    #El with asegura que el archivo se cierre automáticamente una vez que se termine de usar. r es para leer, read
    with open('productos.txt', 'r') as file:
        for linea in file:
            codigo, nombre, precio = linea.strip().split(';')
            productos[nombre.lower()] = float(precio)  # Guardar el nombre en minúsculas y el precio como float. clave valor
    return productos

# Función para buscar el precio de un producto dado su nombre
def buscar_precio_producto(productos, producto_buscado):
    producto_buscado = producto_buscado.lower()  # Convertimos a minúsculas para evitar problemas
    if producto_buscado in productos:
        return productos[producto_buscado]
    else:
        return None
    

def main():
    # Cargar los productos desde el archivo
    productos = cargar_productos()

    # Solicitar al usuario el nombre del producto que quiere buscar
    producto_buscado = input("Ingrese el nombre del producto: ")

    # Buscar el precio del producto
    precio = buscar_precio_producto(productos, producto_buscado)

    # Mostrar el resultado
    if precio is not None:
        print(f"El precio de {producto_buscado} es: ${precio}")
    else:
        print(f"El producto '{producto_buscado}' no fue encontrado.")



main()    