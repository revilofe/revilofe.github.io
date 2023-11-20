"""
Ejercicio 3.2.3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""

def calcular_precio(fruta: str, kilos: float, precios: dict) -> float:
    """ Calcular el precio total
    """
    if fruta in precios:
        precio_total = precios[fruta] * kilos
        return precio_total
    else:
        return None


def pedir_fruta_kilos() -> tuple:
    """ Solicitar la fruta y la cantidad de kilos al usuario
    """
    try:
        return (
            input("Ingrese el nombre de la fruta: ").strip().title(), 
            float(input("Ingrese la cantidad de kilos: ").strip().replace(',', '.'))
            )
    except Exception:
        print("*Error* cantidad de kilos no válida")


def main():
    # Precios de las frutas
    precios_frutas = {
        'Plátano': 1.35,
        'Manzana': 0.80,
        'Pera': 0.85,
        'Naranja': 0.70
    }

    fruta_elegida, kilos_fruta = pedir_fruta_kilos()

    precio_total_fruta = calcular_precio(fruta_elegida, kilos_fruta, precios_frutas)

    # Mostrar el resultado
    if precio_total_fruta is not None:
        print(f"El precio de {kilos_fruta} kilos de {fruta_elegida} es: {precio_total_fruta:.2f} €")
    else:
        print(f"Lo siento, la fruta {fruta_elegida} no está en la lista de precios.")


if __name__ == '__main__':
    main()