# 1 litro de pintura sirve para 10m cuadrados
#la habitación tiene sólo una puerta de 0,80 de ancho por 2 mts de alto.

# Paso 1: Pedir al usuario las dimensiones de la habitación
ancho= float(input("Ingrese el ancho de la habitacion: "))
largo= float(input("Ingrese el largo de la habitacion: "))
alto= float(input("Ingrese el alto de la habitacion: "))

# Paso 2: Calcular el área total de las paredes (habitacion rectangular)
area_paredes = 2 * (ancho * alto) + 2 * (largo * alto)

# Paso 3: Restar el área de la puerta (0.80m x 2m)
area_puerta = 0.80 * 2
area_final = area_paredes - area_puerta

# Paso 4: Calcular cuántos litros de pintura se necesitan (1 litro cubre 10 metros cuadrados)
litros_pintura = area_final / 10

# Paso 5: Mostrar el resultado
print(f"Se necesitan {litros_pintura:.2f} litros de pintura para cubrir las paredes de la habitación.")

# :.2f se utiliza para formatear un número decimal (flotante) y mostrarlo con un número específico de decimales
# : : Indica que estamos aplicando un formato específico a la variable.
# .2 : Significa que queremos mostrar 2 decimales después del punto decimal.
# f : Significa que el número es de tipo flotante (es decir, un número con decimales).