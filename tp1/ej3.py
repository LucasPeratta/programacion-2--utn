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

# Paso 4: Calcular cuántos litros de pintura se necesitan x una mano (1 litro cubre 10 metros cuadrados)
litros_pintura_por_mano = area_final / 10

# Paso 5: Preguntar cuántas manos de pintura se quieren aplicar
manos_pintura = int(input("¿Cuántas manos de pintura deseas aplicar? "))

# Paso 6: Calcular el total de litros de pintura necesarios
litros_totales = litros_pintura_por_mano * manos_pintura

# Paso 7: Mostrar el resultado
print(f"Para {manos_pintura} manos de pintura, se necesitan {litros_totales:.2f} litros de pintura.")

#Por ejemplo, si tienes un número como 17.1987, y lo formateas con :.2f, el resultado será 17.20 (redondeado a 2 decimales).