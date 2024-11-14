# Ejercicio 3.0.1
"""
Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.
"""

def obtener_cadena() -> str:
    """Solicita al usuario una cadena de texto.

    Returns:
        str: La cadena de texto ingresada por el usuario.
    """
    return input("Introduce una cadena de texto: ")

def recorrer_cadena_inversa(cadena: str) -> str:
    """Recorre la cadena en orden inverso y devuelve cada letra en una nueva línea.

    Args:
        cadena: str, la cadena a recorrer.

    Returns:
        str: Una cadena con cada letra en una nueva línea.
    """
    resultado = ""
    i = len(cadena) - 1
    while i >= 0:
        resultado += cadena[i] + "\n"
        i -= 1
    return resultado.strip()

def mostrar_resultado_cadena(resultado: str):
    """Muestra el resultado del recorrido inverso en la salida estándar."""
    print("Recorrido inverso de la cadena:\n" + resultado)

def main_3_0_1():
    cadena = obtener_cadena()
    resultado = recorrer_cadena_inversa(cadena)
    mostrar_resultado_cadena(resultado)

if __name__ == "__main__":
    main_3_0_1()

# Tests para pytest
def test_recorrer_cadena_inversa():
    assert recorrer_cadena_inversa("hola") == "a\nl\no\nh"



# Ejercicio 3.0.2
"""
Dado que `fruta` es una variable de tipo cadena, ¿qué significa `fruta[:]`?

Respuesta:
`fruta[:]` devuelve una nueva cadena que es una copia completa de la original `fruta`. Esto es útil si se necesita una copia de la cadena, aunque en el caso de las cadenas no es común, ya que son inmutables.
"""



# Ejercicio 3.0.3
"""
Tienes este código:

palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
Encapsúlalo en una función llamada cuenta, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos.
"""

def obtener_cadena_y_letra() -> tuple:
    """Solicita al usuario una cadena y una letra para contar.

    Returns:
        tuple: Una tupla con la cadena de texto y la letra.
    """
    cadena = input("Introduce una cadena de texto: ")
    letra = input("Introduce una letra para contar: ")
    return cadena, letra

def cuenta(cadena: str, letra: str) -> int:
    """Cuenta el número de veces que una letra aparece en la cadena.

    Args:
        cadena: str, la cadena en la que buscar.
        letra: str, la letra a contar en la cadena.

    Returns:
        int: Número de ocurrencias de la letra en la cadena.
    """
    contador = 0
    for caracter in cadena:
        if caracter == letra:
            contador += 1
    return contador

def mostrar_resultado_cuenta(contador: int):
    """Muestra el resultado de la cuenta de letras en la salida estándar."""
    print(f"La letra aparece {contador} veces en la cadena.")

def main_3_0_3():
    cadena, letra = obtener_cadena_y_letra()
    contador = cuenta(cadena, letra)
    mostrar_resultado_cuenta(contador)

if __name__ == "__main__":
    main_3_0_3()

# Tests para pytest
def test_cuenta():
    assert cuenta("banana", "a") == 3
    assert cuenta("banana", "b") == 1




# Ejercicio 3.0.4
"""
Usa el método count para contar el número de veces que una letra aparece en "banana".
"""

def obtener_letra() -> str:
    """Solicita al usuario una letra para contar en la palabra 'banana'.

    Returns:
        str: La letra ingresada por el usuario.
    """
    return input("Introduce una letra para contar en 'banana': ")

def cuenta_letras_banana(letra: str) -> int:
    """Cuenta cuántas veces aparece una letra en la palabra 'banana'.

    Args:
        letra: str, la letra a contar en la palabra.

    Returns:
        int: Número de ocurrencias de la letra en "banana".
    """
    palabra = "banana"
    return palabra.count(letra)

def mostrar_resultado_cuenta_banana(contador: int):
    """Muestra el resultado del conteo de letras en 'banana'."""
    print(f"La letra aparece {contador} veces en 'banana'.")

def main_3_0_4():
    letra = obtener_letra()
    contador = cuenta_letras_banana(letra)
    mostrar_resultado_cuenta_banana(contador)

if __name__ == "__main__":
    main_3_0_4()

# Tests para pytest
def test_cuenta_letras_banana():
    assert cuenta_letras_banana("a") == 3
    assert cuenta_letras_banana("b") == 1
    assert cuenta_letras_banana("n") == 2
