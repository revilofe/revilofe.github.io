"""
Ejercicio 3.2.4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
"""

#Constante con los nombres de los meses en un diccionario
NOMBRES_MESES = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril', 5: 'mayo', 6: 'junio',
    7: 'julio', 8: 'agosto', 9: 'septiembre', 10: 'octubre', 11: 'noviembre', 12: 'diciembre'
}


def dividir_fecha(fecha: str) -> tuple:
    """ Dividir la fecha en día, mes y año
    """

    partes_fecha = fecha.split('/')
    
    #Obtener día, mes y año como enteros
    if len(partes_fecha) == 3:
        dia = int(partes_fecha[0])
        mes = int(partes_fecha[1])
        anio = int(partes_fecha[2])
    else:
        raise ValueError
    
    #Otra forma de hacer lo mismo:
    #dia, mes, anio = map(int, partes_fecha)

    return dia, mes, anio


def formatear_fecha(fecha: str) -> str:
    """ Formatear la fecha con el nuevo formato
    """
    
    dia, mes, anio = dividir_fecha(fecha)

    #Obtener el nombre del mes
    nombre_mes = NOMBRES_MESES.get(mes, None)

    if nombre_mes == None:
        raise ValueError
    
    return f"{dia} de {nombre_mes} de {anio}"



def main():
    fecha = input("Ingrese la fecha en formato dd/mm/aaaa: ")

    try:
        fecha_formateada = formatear_fecha(fecha)
        print(f"La fecha formateada es: {fecha_formateada}")
    except ValueError:
        print("*Error* la fecha no tiene el formato correcto (dd/mm/aaaa).")


if __name__ == '__main__':
    main()