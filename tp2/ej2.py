def EsBisiesto(año):
    # Un año es bisiesto si es divisible por 4 y
    # no es divisible por 100, o es divisible por 400
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

def es_fecha_valida(dia, mes, año):
    # Verificamos si el año es bisiesto
    es_bisiesto = EsBisiesto(año)
    
    # Días en cada mes
    dias_por_mes = [31, 29 if es_bisiesto else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verificamos si el mes es válido
    if 1 <= mes <= 12:
        # Verificamos si el día es válido para el mes dado
        return 1 <= dia <= dias_por_mes[mes - 1]
    return False

def main():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes (1-12): "))
    año = int(input("Ingrese el año: "))
    
    if es_fecha_valida(dia, mes, año):
        print(f"La fecha {dia}/{mes}/{año} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{año} no es válida.")

main()
