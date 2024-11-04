Aquí tienes el código completo, con los tests para la fase de procesamiento ubicados justo después de cada función `main` en cada ejercicio. Estos tests están preparados para ejecutarse con `pytest`.

"""Ejercicio 2.2.1
Descripción: Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_palabra() -> str:
    """
    Solicita al usuario una palabra y la retorna.

    Returns:
        str: La palabra ingresada por el usuario.
    """
    return input("Introduce una palabra: ")

# Fase 2: Procesamiento
def repetir_palabra(palabra: str, repeticiones: int = 10) -> str:
    """
    Genera una cadena con la palabra repetida el número de veces indicado, separada por espacios.

    Args:
        palabra (str): La palabra a repetir.
        repeticiones (int, opcional): Número de veces a repetir la palabra. Por defecto, 10.

    Returns:
        str: Cadena con la palabra repetida y separada por espacios.
    """
    return " ".join([palabra] * repeticiones)

# Fase 3: Salida
def mostrar_repeticiones(cadena_palabras: str) -> None:
    """
    Muestra cada palabra de la cadena separada en líneas individuales.

    Args:
        cadena_palabras (str): Cadena con las palabras repetidas separadas por espacios.
    """
    for palabra in cadena_palabras.split():
        print(palabra)

# Función principal
def main_ejercicio_2_2_1() -> None:
    palabra = obtener_palabra()
    cadena_palabras = repetir_palabra(palabra)
    mostrar_repeticiones(cadena_palabras)

# Test para la fase de procesamiento
def test_repetir_palabra():
    assert repetir_palabra("hola") == "hola hola hola hola hola hola hola hola hola hola"
    assert repetir_palabra("test", 5) == "test test test test test"


"""Ejercicio 2.2.2
Descripción: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_edad() -> int:
    """
    Solicita al usuario su edad y la valida como un número entero positivo.

    Returns:
        int: La edad ingresada por el usuario.
    """
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                edad = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return edad

# Fase 2: Procesamiento
def generar_cadena_años(edad: int) -> str:
    """
    Genera una cadena de años desde 1 hasta la edad dada, separados por espacios.

    Args:
        edad (int): Edad del usuario.

    Returns:
        str: Cadena de años cumplidos separados por espacios.
    """
    return " ".join(str(año) for año in range(1, edad + 1))

# Fase 3: Salida
def mostrar_años_cumplidos(cadena_años: str) -> None:
    """
    Muestra cada año cumplido en una línea individual.

    Args:
        cadena_años (str): Cadena con los años cumplidos separados por espacios.
    """
    for año in cadena_años.split():
        print(año)

# Función principal
def main_ejercicio_2_2_2() -> None:
    edad = obtener_edad()
    cadena_años = generar_cadena_años(edad)
    mostrar_años_cumplidos(cadena_años)

# Test para la fase de procesamiento
def test_generar_cadena_años():
    assert generar_cadena_años(3) == "1 2 3"
    assert generar_cadena_años(5) == "1 2 3 4 5"


"""Ejercicio 2.2.3
Descripción: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero_positivo() -> int:
    """
    Solicita al usuario un número entero positivo y lo valida.

    Returns:
        int: El número entero positivo ingresado por el usuario.
    """
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo.")
                numero = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def generar_cadena_impares(numero: int) -> str:
    """
    Genera una cadena de números impares desde 1 hasta el número dado, separados por comas.

    Args:
        numero (int): Número entero positivo hasta el cual generar impares.

    Returns:
        str: Cadena de números impares separados por comas.
    """
    return ", ".join(str(i) for i in range(1, numero + 1, 2))

# Fase 3: Salida
def mostrar_impares(cadena_impares: str) -> None:
    """
    Muestra los números impares en la cadena, separados por comas.

    Args:
        cadena_impares (str): Cadena de números impares separados por comas.
    """
    print(cadena_impares)

# Función principal
def main_ejercicio_2_2_3() -> None:
    numero = obtener_numero_positivo()
    cadena_impares = generar_cadena_impares(numero)
    mostrar_impares(cadena_impares)

# Test para la fase de procesamiento
def test_generar_cadena_impares():
    assert generar_cadena_impares(5) == "1, 3, 5"
    assert generar_cadena_impares(10) == "1, 3, 5, 7, 9"


"""Ejercicio 2.2.4
Descripción: Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás 
desde ese número hasta cero separados por comas.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero_positivo() -> int:
    """
    Solicita al usuario un número entero positivo y lo valida.

    Returns:
        int: El número entero positivo ingresado por el usuario.
    """
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo.")
                numero = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def generar_cadena_cuenta_atras(numero: int) -> str:
    """
    Genera una cadena con la cuenta atrás desde el número dado hasta cero, separados por comas.

    Args:
        numero (int): Número entero positivo desde el cual iniciar la cuenta atrás.

    Returns:
        str: Cadena de la cuenta atrás separada por comas.
    """
    return ", ".join(str(i) for i in range(numero, -1, -1))

# Fase 3: Salida
def mostrar_cuenta_atras(cadena_cuenta_atras: str) -> None:
    """
    Muestra la cadena de la cuenta atrás separada por comas.

    Args:
        cadena_cuenta_atras (str): Cadena con la cuenta atrás separada por comas.
    """
    print(cadena_cuenta_atras)

# Función principal
def main_ejercicio_2_2_4() -> None:
    numero = obtener_numero_positivo()
    cadena_cuenta_atras = generar_cadena_cuenta_atras(numero)
    mostrar_cuenta_atras(cadena_cuenta_atras)

# Test para la fase de procesamiento
def test_generar_cadena_cuenta_atras():
    assert generar_cadena_cuenta_atras(3) == "3, 2, 1, 0"
    assert generar_cadena_cuenta_atras(5) == "5, 4, 3, 2, 1, 0"




"""Ejercicio 2.2.5
Descripción: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
capital obtenido en la inversión cada año que dura la inversión.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_datos_inversion() -> tuple:
    """
    Solicita al usuario la cantidad a invertir, el interés anual y el número de años.

    Returns:
        tuple: Cantidad a invertir (float), interés anual (float), número de años (int).
    """
    cantidad = interes = años = -1
    while cantidad <= 0:
        try:
            cantidad = float(input("Introduce la cantidad a invertir: "))
            if cantidad <= 0:
                print("La cantidad debe ser positiva.")
        except ValueError:
            print("Por favor, introduce una cantidad válida.")

    while interes < 0:
        try:
            interes = float(input("Introduce el interés anual (%): "))
            if interes < 0:
                print("El interés debe ser 0 o positivo.")
        except ValueError:
            print("Por favor, introduce un valor de interés válido.")

    while años <= 0:
        try:
            años = int(input("Introduce el número de años: "))
            if años <= 0:
                print("El número de años debe ser positivo.")
        except ValueError:
            print("Por favor, introduce un número de años válido.")

    return cantidad, interes, años

# Fase 2: Procesamiento
def calcular_inversion(cantidad: float, interes: float, años: int) -> str:
    """
    Calcula el capital obtenido año a año durante el periodo de inversión.

    Args:
        cantidad (float): Cantidad a invertir.
        interes (float): Interés anual.
        años (int): Número de años.

    Returns:
        str: Capital acumulado al final de cada año, separado por comas.
    """
    capital = cantidad
    resultado = ""
    for año in range(1, años + 1):
        capital *= 1 + interes / 100
        resultado += f"Año {año}: {capital:.2f}, "
    return resultado.rstrip(", ")

# Fase 3: Salida
def mostrar_inversion(cadena_inversion: str) -> None:
    """
    Muestra el capital obtenido en la inversión año a año.

    Args:
        cadena_inversion (str): Cadena con los resultados de capital por año.
    """
    print(cadena_inversion)

# Función principal
def main_ejercicio_2_2_5() -> None:
    cantidad, interes, años = obtener_datos_inversion()
    cadena_inversion = calcular_inversion(cantidad, interes, años)
    mostrar_inversion(cadena_inversion)

# Test para la fase de procesamiento
def test_calcular_inversion():
    assert calcular_inversion(1000, 5, 3) == "Año 1: 1050.00, Año 2: 1102.50, Año 3: 1157.63"
    assert calcular_inversion(2000, 10, 2) == "Año 1: 2200.00, Año 2: 2420.00"





"""Ejercicio 2.2.6
Descripción: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo de altura igual al número.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_altura_triangulo() -> int:
    """
    Solicita al usuario un número entero positivo que representará la altura del triángulo.

    Returns:
        int: Altura del triángulo ingresada por el usuario.
    """
    altura = -1
    while altura <= 0:
        try:
            altura = int(input("Introduce la altura del triángulo (entero positivo): "))
            if altura <= 0:
                print("La altura debe ser un entero positivo.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return altura

# Fase 2: Procesamiento
def generar_triangulo(altura: int) -> str:
    """
    Genera un triángulo rectángulo de altura dada usando asteriscos.

    Args:
        altura (int): Altura del triángulo.

    Returns:
        str: Triángulo de asteriscos separado por saltos de línea.
    """
    resultado = ""
    for i in range(1, altura + 1):
        resultado += "*" * i + "\n"
    return resultado.strip()

# Fase 3: Salida
def mostrar_triangulo(triangulo: str) -> None:
    """
    Muestra el triángulo de asteriscos en pantalla.

    Args:
        triangulo (str): Triángulo generado como cadena.
    """
    print(triangulo)

# Función principal
def main_ejercicio_2_2_6() -> None:
    altura = obtener_altura_triangulo()
    triangulo = generar_triangulo(altura)
    mostrar_triangulo(triangulo)

# Test para la fase de procesamiento
def test_generar_triangulo():
    assert generar_triangulo(3) == "*\n**\n***"
    assert generar_triangulo(5) == "*\n**\n***\n****\n*****"




"""Ejercicio 2.2.7
Descripción: Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
# Solución
# Fase 2: Procesamiento (no requiere entrada de usuario)
def generar_tabla_multiplicar() -> str:
    """
    Genera las tablas de multiplicar del 1 al 10.

    Returns:
        str: Tablas de multiplicar del 1 al 10, separadas por saltos de línea.
    """
    resultado = ""
    for i in range(1, 11):
        for j in range(1, 11):
            resultado += f"{i} x {j} = {i * j}\n"
        resultado += "\n"  # Añade una línea en blanco entre tablas
    return resultado.strip()

# Fase 3: Salida
def mostrar_tabla_multiplicar(tabla: str) -> None:
    """
    Muestra las tablas de multiplicar del 1 al 10 en pantalla.

    Args:
        tabla (str): Cadena con las tablas de multiplicar.
    """
    print(tabla)

# Función principal
def main_ejercicio_2_2_7() -> None:
    tabla = generar_tabla_multiplicar()
    mostrar_tabla_multiplicar(tabla)

# Test para la fase de procesamiento
def test_generar_tabla_multiplicar():
    expected_output = (
        "1 x 1 = 1\n1 x 2 = 2\n1 x 3 = 3\n1 x 4 = 4\n1 x 5 = 5\n1 x 6 = 6\n"
        "1 x 7 = 7\n1 x 8 = 8\n1 x 9 = 9\n1 x 10 = 10\n\n"
        "2 x 1 = 2\n2 x 2 = 4\n2 x 3 = 6\n2 x 4 = 8\n2 x 5 = 10\n2 x 6 = 12\n"
        "2 x 7 = 14\n2 x 8 = 16\n2 x 9 = 18\n2 x 10 = 20\n"
    )
    assert generar_tabla_multiplicar().startswith(expected_output)


"""Ejercicio 2.2.8
Descripción: Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo de números.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_altura_triangulo() -> int:
    """
    Solicita al usuario un número entero positivo que representará la altura del triángulo.

    Returns:
        int: Altura del triángulo ingresada por el usuario.
    """
    altura = -1
    while altura <= 0:
        try:
            altura = int(input("Introduce la altura del triángulo (entero positivo): "))
            if altura <= 0:
                print("La altura debe ser un entero positivo.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return altura

# Fase 2: Procesamiento
def generar_triangulo_numerico(altura: int) -> str:
    """
    Genera un triángulo numérico de altura dada.

    Args:
        altura (int): Altura del triángulo.

    Returns:
        str: Triángulo numérico separado por saltos de línea.
    """
    resultado = ""
    for i in range(1, altura + 1):
        fila = " ".join(str(num) for num in range(1, 2 * i, 2)[::-1])
        resultado += fila + "\n"
    return resultado.strip()

# Fase 3: Salida
def mostrar_triangulo_numerico(triangulo: str) -> None:
    """
    Muestra el triángulo numérico en pantalla.

    Args:
        triangulo (str): Triángulo generado como cadena.
    """
    print(triangulo)

# Función principal
def main_ejercicio_2_2_8() -> None:
    altura = obtener_altura_triangulo()
    triangulo = generar_triangulo_numerico(altura)
    mostrar_triangulo_numerico(triangulo)

# Test para la fase de procesamiento
def test_generar_triangulo_numerico():
    assert generar_triangulo_numerico(3) == "1\n3 1\n5 3 1"
    assert generar_triangulo_numerico(5) == "1\n3 1\n5 3 1\n7 5 3 1\n9 7 5 3 1"


"""Ejercicio 2.2.9
Descripción: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña 
hasta que introduzca la contraseña correcta.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_contrasena() -> str:
    """
    Solicita la contraseña al usuario y la retorna.

    Returns:
        str: Contraseña ingresada por el usuario.
    """
    return input("Introduce la contraseña: ")

# Fase 2: Procesamiento
def verificar_contrasena(contrasena_correcta: str) -> str:
    """
    Pregunta al usuario por la contraseña hasta que sea correcta.

    Args:
        contrasena_correcta (str): Contraseña almacenada.

    Returns:
        str: Mensaje confirmando el acceso.
    """
    contrasena = ""
    while contrasena != contrasena_correcta:
        contrasena = obtener_contrasena()
        if contrasena != contrasena_correcta:
            print("Contraseña incorrecta. Intenta nuevamente.")
    return "Acceso concedido"

# Fase 3: Salida
def mostrar_resultado(mensaje: str) -> None:
    """
    Muestra el mensaje de resultado en pantalla.

    Args:
        mensaje (str): Mensaje de acceso.
    """
    print(mensaje)

# Función principal
def main_ejercicio_2_2_9() -> None:
    contrasena_correcta = "segura123"
    mensaje = verificar_contrasena(contrasena_correcta)
    mostrar_resultado(mensaje)

# Test para la fase de procesamiento
def test_verificar_contrasena(monkeypatch):
    inputs = iter(["incorrecta", "otra", "segura123"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert verificar_contrasena("segura123") == "Acceso concedido"



"""Ejercicio 2.2.10
Descripción: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero() -> int:
    """
    Solicita al usuario un número entero positivo.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    numero = -1
    while numero <= 0:
        try:
            numero = int(input("Introduce un número entero positivo: "))
            if numero <= 0:
                print("El número debe ser positivo.")
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def es_primo(numero: int) -> bool:
    """
    Determina si un número es primo.

    Args:
        numero (int): Número a verificar.

    Returns:
        bool: True si es primo, False en caso contrario.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Fase 3: Salida
def mostrar_resultado_primo(es_primo: bool) -> None:
    """
    Muestra si el número es primo o no.

    Args:
        es_primo (bool): True si el número es primo, False si no lo es.
    """
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

# Función principal
def main_ejercicio_2_2_10() -> None:
    numero = obtener_numero()
    resultado = es_primo(numero)
    mostrar_resultado_primo(resultado)

# Test para la fase de procesamiento
def test_es_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(13) == True
    assert es_primo(16) == False


"""Ejercicio 2.2.11
Descripción: Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida, 
empezando por la última.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_palabra() -> str:
    """
    Solicita al usuario una palabra y la retorna.

    Returns:
        str: La palabra ingresada por el usuario.
    """
    return input("Introduce una palabra: ")

# Fase 2: Procesamiento
def invertir_palabra(palabra: str) -> str:
    """
    Invierte el orden de las letras en la palabra.

    Args:
        palabra (str): Palabra a invertir.

    Returns:
        str: Palabra invertida.
    """
    resultado = ""
    for letra in palabra:
        resultado = letra + resultado
    return resultado

# Fase 3: Salida
def mostrar_letras_invertidas(palabra_invertida: str) -> None:
    """
    Muestra cada letra de la palabra invertida en una línea.

    Args:
        palabra_invertida (str): Palabra invertida.
    """
    for letra in palabra_invertida:
        print(letra)

# Función principal
def main_ejercicio_2_2_11() -> None:
    palabra = obtener_palabra()
    palabra_invertida = invertir_palabra(palabra)
    mostrar_letras_invertidas(palabra_invertida)

# Test para la fase de procesamiento
def test_invertir_palabra():
    assert invertir_palabra("hola") == "aloh"
    assert invertir_palabra("python") == "nohtyp"


"""Ejercicio 2.2.12
Descripción: Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece 
la letra en la frase.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_frase() -> str:
    """
    Solicita al usuario una frase y la retorna.

    Returns:
        str: Frase ingresada por el usuario.
    """
    return input("Introduce una frase: ")

def obtener_letra() -> str:
    """
    Solicita al usuario una letra y la valida.

    Returns:
        str: Letra ingresada por el usuario.
    """
    letra = ""
    while len(letra) != 1:
        letra = input("Introduce una letra: ")
        if len(letra) != 1:
            print("Por favor, introduce solo una letra.")
    return letra

# Fase 2: Procesamiento
def contar_letra(frase: str, letra: str) -> int:
    """
    Cuenta las ocurrencias de una letra en una frase.

    Args:
        frase (str): Frase en la cual contar la letra.
        letra (str): Letra a contar.

    Returns:
        int: Número de veces que aparece la letra en la frase.
    """
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

# Fase 3: Salida
def mostrar_contador_letra(contador: int) -> None:
    """
    Muestra el número de veces que aparece la letra en la frase.

    Args:
        contador (int): Número de veces que aparece la letra.
    """
    print(f"La letra aparece {contador} veces en la frase.")

# Función principal
def main_ejercicio_2_2_12() -> None:
    frase = obtener_frase()
    letra = obtener_letra()
    contador = contar_letra(frase, letra)
    mostrar_contador_letra(contador)

# Test para la fase de procesamiento
def test_contar_letra():
    assert contar_letra("hola mundo", "o") == 2
    assert contar_letra("python es divertido", "e") == 2
    assert contar_letra("este es un test", "t") == 4




"""Ejercicio 2.2.13
Descripción: Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_texto() -> str:
    """
    Solicita una línea de texto al usuario y la retorna.

    Returns:
        str: Texto ingresado por el usuario.
    """
    return input("Escribe algo (o 'salir' para terminar): ")

# Fase 2 y Fase 3: Procesamiento y Salida
def eco_texto():
    """
    Repite el texto ingresado por el usuario hasta que escriba "salir".
    """
    texto = obtener_texto()
    while texto.lower() != "salir":
        print("Eco:", texto)
        texto = obtener_texto()

# Función principal
def main_ejercicio_2_2_13() -> None:
    eco_texto()

# Este ejercicio no requiere test para la fase de procesamiento, ya que su salida depende de la interacción en tiempo real.




"""Ejercicio 2.2.14
Descripción: Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero() -> int:
    """
    Solicita un número entero al usuario y lo retorna.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero (0 para terminar): "))
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def sumar_hasta_cero() -> int:
    """
    Suma números ingresados por el usuario hasta que se introduce un 0.

    Returns:
        int: Suma de todos los números ingresados.
    """
    suma = 0
    numero = obtener_numero()
    while numero != 0:
        suma += numero
        numero = obtener_numero()
    return suma

# Fase 3: Salida
def mostrar_suma(suma: int) -> None:
    """
    Muestra la suma de todos los números ingresados.

    Args:
        suma (int): Suma de los números.
    """
    print(f"La suma es: {suma}")

# Función principal
def main_ejercicio_2_2_14() -> None:
    suma = sumar_hasta_cero()
    mostrar_suma(suma)

# Test para la fase de procesamiento
def test_sumar_hasta_cero(monkeypatch):
    inputs = iter([5, 10, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert sumar_hasta_cero() == 15




"""Ejercicio 2.2.15
Descripción: Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero() -> int:
    """
    Solicita un número entero al usuario y lo retorna.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero (0 para terminar): "))
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def sumar_positivos_hasta_cero() -> int:
    """
    Suma solo los números positivos ingresados por el usuario hasta que se introduce un 0.

    Returns:
        int: Suma de todos los números positivos ingresados.
    """
    suma = 0
    numero = obtener_numero()
    while numero != 0:
        if numero > 0:
            suma += numero
        numero = obtener_numero()
    return suma

# Fase 3: Salida
def mostrar_suma_positivos(suma: int) -> None:
    """
    Muestra la suma de todos los números positivos ingresados.

    Args:
        suma (int): Suma de los números positivos.
    """
    print(f"La suma de los números positivos es: {suma}")

# Función principal
def main_ejercicio_2_2_15() -> None:
    suma = sumar_positivos_hasta_cero()
    mostrar_suma_positivos(suma)

# Test para la fase de procesamiento
def test_sumar_positivos_hasta_cero(monkeypatch):
    inputs = iter([5, -3, 10, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert sumar_positivos_hasta_cero() == 15



"""Ejercicio 2.2.16
Descripción: Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero_positivo_o_cero() -> int:
    """
    Solicita un número entero positivo o cero al usuario y lo retorna.

    Returns:
        int: Número entero ingresado por el usuario.
    """
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero positivo (0 para terminar): "))
            if numero < 0:
                print("El número debe ser positivo o cero.")
                numero = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def encontrar_mayor_hasta_cero() -> int:
    """
    Encuentra el mayor número ingresado por el usuario hasta que se introduce un 0.

    Returns:
        int: El mayor número ingresado (excluyendo el 0).
    """
    mayor = 0
    numero = obtener_numero_positivo_o_cero()
    while numero != 0:
        if numero > mayor:
            mayor = numero
        numero = obtener_numero_positivo_o_cero()
    return mayor

# Fase 3: Salida
def mostrar_mayor(mayor: int) -> None:
    """
    Muestra el mayor número ingresado.

    Args:
        mayor (int): El mayor número ingresado.
    """
    if mayor > 0:
        print(f"El mayor número ingresado es: {mayor}")
    else:
        print("No se ingresaron números mayores que cero.")

# Función principal
def main_ejercicio_2_2_16() -> None:
    mayor = encontrar_mayor_hasta_cero()
    mostrar_mayor(mayor)

# Test para la fase de procesamiento
def test_encontrar_mayor_hasta_cero(monkeypatch):
    inputs = iter([5, 12, 7, 0])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    assert encontrar_mayor_hasta_cero() == 12




