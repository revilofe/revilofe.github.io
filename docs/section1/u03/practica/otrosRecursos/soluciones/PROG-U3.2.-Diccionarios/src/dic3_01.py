"""
Ejercicio 3.2.1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

def main():
    # Definir el diccionario de divisas y símbolos
    diccionario_divisas = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}

    # Solicitar al usuario una divisa
    divisa_elegida = input("Ingrese el nombre de la divisa: ").title()

    # Obtener el símbolo de la divisa o mostrar un mensaje de aviso
    if divisa_elegida in diccionario_divisas:
        simbolo_divisa = diccionario_divisas[divisa_elegida]
        print(f"El símbolo de {divisa_elegida} es: {simbolo_divisa}")
    else:
        print(f"Lo siento, la divisa {divisa_elegida} no está en el diccionario.")


if __name__ == '__main__':
    main()