"""Ejercicio 2.1.1
Descripción: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
"""
#Solución
# Fase 1: Entrada y validación de datos
def obtener_edad():
    """Obtiene y valida la edad ingresada por el usuario."""
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                edad = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return edad

# Fase 2: Procesamiento
def es_mayor_de_edad(edad):
    """Determina si una persona es mayor de edad."""
    return edad >= 18

# Fase 3: Salida
def mostrar_resultado_mayor_edad(mayor_edad):
    """Muestra si el usuario es mayor de edad o no."""
    if mayor_edad:
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")

# Función principal
def main():
    edad = obtener_edad()
    mayor_edad = es_mayor_de_edad(edad)
    mostrar_resultado_mayor_edad(mayor_edad)

if __name__ == "__main__":
    main()

# Test con pytest
def test_es_mayor_de_edad():
    assert es_mayor_de_edad(18) == True
    assert es_mayor_de_edad(17) == False
    assert es_mayor_de_edad(20) == True
    assert es_mayor_de_edad(0) == False




"""Ejercicio 2.1.2
Descripción: Programa que almacene una contraseña, pregunte al usuario por la contraseña e imprima si coincide con la almacenada sin tener en cuenta mayúsculas y minúsculas.
"""
#Solución
# Fase 1: Entrada y validación de datos
def obtener_contrasena():
    """Obtiene la contraseña ingresada por el usuario."""
    return input("Introduce la contraseña: ")

# Fase 2: Procesamiento
def verificar_contrasena(contrasena_almacenada, contrasena_usuario):
    """Verifica si la contraseña coincide, sin considerar mayúsculas/minúsculas."""
    return contrasena_almacenada.lower() == contrasena_usuario.lower()

# Fase 3: Salida
def mostrar_resultado_verificacion(verificacion):
    """Muestra si la contraseña coincide o no."""
    if verificacion:
        print("La contraseña es correcta.")
    else:
        print("La contraseña es incorrecta.")

# Función principal
def main():
    contrasena_almacenada = "contraseñaSegura"
    contrasena_usuario = obtener_contrasena()
    verificacion = verificar_contrasena(contrasena_almacenada, contrasena_usuario)
    mostrar_resultado_verificacion(verificacion)

if __name__ == "__main__":
    main()

# Test con pytest
def test_verificar_contrasena():
    assert verificar_contrasena("contraseñaSegura", "contraseñasegura") == True
    assert verificar_contrasena("Contraseña", "contraseña") == True
    assert verificar_contrasena("Segura", "insegura") == False



"""Ejercicio 2.1.3
Descripción: Programa que pide al usuario dos números y muestra su división. Si el divisor es cero, muestra un error.
"""
#Solución
# Fase 1: Entrada y validación de datos
def obtener_numeros():
    """Obtiene dos números del usuario, asegurando que el divisor no sea cero."""
    dividendo = None
    divisor = None

    while dividendo is None:
        try:
            dividendo = float(input("Introduce el dividendo: "))
        except ValueError:
            print("Por favor, introduce un número válido.")

    while divisor is None:
        try:
            divisor = float(input("Introduce el divisor: "))
            if divisor == 0:
                print("El divisor no puede ser cero.")
                divisor = None
        except ValueError:
            print("Por favor, introduce un número válido.")

    return dividendo, divisor

# Fase 2: Procesamiento
def calcular_division(dividendo, divisor):
    """Calcula la división entre el dividendo y el divisor."""
    return dividendo / divisor

# Fase 3: Salida
def mostrar_resultado_division(resultado):
    """Muestra el resultado de la división."""
    print(f"El resultado de la división es: {resultado}")

# Función principal
def main():
    dividendo, divisor = obtener_numeros()
    resultado = calcular_division(dividendo, divisor)
    mostrar_resultado_division(resultado)

if __name__ == "__main__":
    main()

# Test con pytest
def test_calcular_division():
    assert calcular_division(10, 2) == 5.0
    assert calcular_division(9, 3) == 3.0
    assert calcular_division(5, -1) == -5.0

Aquí tienes la solución de los ejercicios desde el 2.1.4 hasta el 2.1.7, incluyendo la descripción del ejercicio en cada solución como pediste:


"""Ejercicio 2.1.4
Descripción: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_numero_entero():
    """Obtiene un número entero del usuario."""
    numero = None
    while numero is None:
        try:
            numero = int(input("Introduce un número entero: "))
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return numero

# Fase 2: Procesamiento
def es_par(numero):
    """Determina si un número es par."""
    return numero % 2 == 0

# Fase 3: Salida
def mostrar_resultado_paridad(par):
    """Muestra si el número es par o impar."""
    if par:
        print("El número es par.")
    else:
        print("El número es impar.")

# Función principal
def main():
    numero = obtener_numero_entero()
    par = es_par(numero)
    mostrar_resultado_paridad(par)

if __name__ == "__main__":
    main()

# Test con pytest
def test_es_par():
    assert es_par(2) == True
    assert es_par(3) == False
    assert es_par(0) == True
    assert es_par(-4) == True
    assert es_par(-5) == False




"""Ejercicio 2.1.5
Descripción: Para tributar un determinado impuesto se debe ser mayor de 16 años y tener ingresos mensuales iguales o superiores a 1000 €. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre si debe tributar.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_datos_tributo():
    """Obtiene y valida la edad y los ingresos del usuario."""
    edad = None
    ingresos = None

    while edad is None:
        try:
            edad = int(input("Introduce tu edad: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                edad = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")

    while ingresos is None:
        try:
            ingresos = float(input("Introduce tus ingresos mensuales: "))
            if ingresos < 0:
                print("Los ingresos no pueden ser negativos.")
                ingresos = None
        except ValueError:
            print("Por favor, introduce un número válido.")

    return edad, ingresos

# Fase 2: Procesamiento
def debe_tributar(edad, ingresos):
    """Determina si una persona debe tributar."""
    return edad > 16 and ingresos >= 1000

# Fase 3: Salida
def mostrar_resultado_tributo(tributa):
    """Muestra si el usuario debe tributar o no."""
    if tributa:
        print("Debes tributar.")
    else:
        print("No debes tributar.")

# Función principal
def main():
    edad, ingresos = obtener_datos_tributo()
    tributa = debe_tributar(edad, ingresos)
    mostrar_resultado_tributo(tributa)

if __name__ == "__main__":
    main()

# Test con pytest
def test_debe_tributar():
    assert debe_tributar(17, 1000) == True
    assert debe_tributar(16, 1000) == False
    assert debe_tributar(18, 900) == False
    assert debe_tributar(20, 2000) == True





"""Ejercicio 2.1.6
Descripción: Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres 
con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_datos_grupo():
    """Obtiene y valida el nombre y el sexo del usuario."""
    nombre = input("Introduce tu nombre: ")
    sexo = None
    while sexo not in ['M', 'H']:
        sexo = input("Introduce tu sexo (M para mujer, H para hombre): ").upper()
        if sexo not in ['M', 'H']:
            print("Por favor, introduce M o H.")
    return nombre, sexo

# Fase 2: Procesamiento
def determinar_grupo(nombre, sexo):
    """Determina el grupo del usuario en función de su nombre y sexo."""
    if (sexo == 'M' and nombre[0].upper() < 'M') or (sexo == 'H' and nombre[0].upper() > 'N'):
        return 'A'
    else:
        return 'B'

# Fase 3: Salida
def mostrar_resultado_grupo(grupo):
    """Muestra el grupo asignado."""
    print(f"Te corresponde el grupo {grupo}.")

# Función principal
def main():
    nombre, sexo = obtener_datos_grupo()
    grupo = determinar_grupo(nombre, sexo)
    mostrar_resultado_grupo(grupo)

if __name__ == "__main__":
    main()

# Test con pytest
def test_determinar_grupo():
    assert determinar_grupo("Ana", "M") == "A"
    assert determinar_grupo("Maria", "M") == "B"
    assert determinar_grupo("Luis", "H") == "A"
    assert determinar_grupo("Nicolas", "H") == "B"




"""Ejercicio 2.1.7
Descripción: Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde según la renta.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_renta():
    """Obtiene y valida la renta anual del usuario."""
    renta = None
    while renta is None:
        try:
            renta = float(input("Introduce tu renta anual: "))
            if renta < 0:
                print("La renta no puede ser negativa.")
                renta = None
        except ValueError:
            print("Por favor, introduce un número válido.")
    return renta

# Fase 2: Procesamiento
def calcular_tipo_impositivo(renta):
    """Determina el tipo impositivo en función de la renta."""
    if renta < 10000:
        return 5
    elif renta < 20000:
        return 15
    elif renta < 35000:
        return 20
    elif renta < 60000:
        return 30
    else:
        return 45

# Fase 3: Salida
def mostrar_tipo_impositivo(tipo):
    """Muestra el tipo impositivo aplicable."""
    print(f"El tipo impositivo que corresponde es del {tipo}%.")

# Función principal
def main():
    renta = obtener_renta()
    tipo_impositivo = calcular_tipo_impositivo(renta)
    mostrar_tipo_impositivo(tipo_impositivo)

if __name__ == "__main__":
    main()

# Test con pytest
def test_calcular_tipo_impositivo():
    assert calcular_tipo_impositivo(5000) == 5
    assert calcular_tipo_impositivo(15000) == 15
    assert calcular_tipo_impositivo(25000) == 20
    assert calcular_tipo_impositivo(40000) == 30
    assert calcular_tipo_impositivo(75000) == 45





"""Ejercicio 2.1.8
Descripción: En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación 
comienzan en 0.0 y pueden ir aumentando en 0.4, 0.6 o más. A cada puntuación le corresponde un nivel y una cantidad de dinero (2400€ multiplicada 
por la puntuación). Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_puntuacion():
    """Obtiene y valida la puntuación del empleado."""
    puntuacion = None
    while puntuacion is None:
        try:
            puntuacion = float(input("Introduce la puntuación del empleado: "))
            if puntuacion not in [0.0, 0.4, 0.6] and puntuacion < 0.6:
                print("Puntuación no válida. Debe ser 0.0, 0.4, 0.6 o más.")
                puntuacion = None
        except ValueError:
            print("Por favor, introduce un número válido.")
    return puntuacion

# Fase 2: Procesamiento
def determinar_nivel_y_beneficio(puntuacion):
    """Determina el nivel de rendimiento y el beneficio."""
    if puntuacion == 0.0:
        nivel = "Inaceptable"
    elif puntuacion == 0.4:
        nivel = "Aceptable"
    else:
        nivel = "Meritorio"

    beneficio = 2400 * puntuacion
    return nivel, beneficio

# Fase 3: Salida
def mostrar_resultado_nivel_y_beneficio(nivel, beneficio):
    """Muestra el nivel de rendimiento y el beneficio económico."""
    print(f"Nivel de rendimiento: {nivel}")
    print(f"Beneficio: {beneficio}€")

# Función principal
def main():
    puntuacion = obtener_puntuacion()
    nivel, beneficio = determinar_nivel_y_beneficio(puntuacion)
    mostrar_resultado_nivel_y_beneficio(nivel, beneficio)

if __name__ == "__main__":
    main()

# Test con pytest
def test_determinar_nivel_y_beneficio():
    assert determinar_nivel_y_beneficio(0.0) == ("Inaceptable", 0.0)
    assert determinar_nivel_y_beneficio(0.4) == ("Aceptable", 960.0)
    assert determinar_nivel_y_beneficio(0.6) == ("Meritorio", 1440.0)
    assert determinar_nivel_y_beneficio(1.0) == ("Meritorio", 2400.0)





"""Ejercicio 2.1.9
Descripción: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular el precio de entrada. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio. Menores de 4 años entran gratis, de 4 a 18 años pagan 5€ 
y mayores de 18 años pagan 10€.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_edad_cliente():
    """Obtiene y valida la edad del cliente."""
    edad = None
    while edad is None:
        try:
            edad = int(input("Introduce la edad del cliente: "))
            if edad < 0:
                print("La edad no puede ser negativa.")
                edad = None
        except ValueError:
            print("Por favor, introduce un número entero válido.")
    return edad

# Fase 2: Procesamiento
def calcular_precio_entrada(edad):
    """Calcula el precio de entrada en función de la edad del cliente."""
    if edad < 4:
        return 0
    elif edad <= 18:
        return 5
    else:
        return 10

# Fase 3: Salida
def mostrar_precio_entrada(precio):
    """Muestra el precio de la entrada."""
    print(f"El precio de la entrada es: {precio}€")

# Función principal
def main():
    edad = obtener_edad_cliente()
    precio = calcular_precio_entrada(edad)
    mostrar_precio_entrada(precio)

if __name__ == "__main__":
    main()

# Test con pytest
def test_calcular_precio_entrada():
    assert calcular_precio_entrada(3) == 0
    assert calcular_precio_entrada(4) == 5
    assert calcular_precio_entrada(18) == 5
    assert calcular_precio_entrada(19) == 10
    assert calcular_precio_entrada(65) == 10




"""Ejercicio 2.1.10
Descripción: La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas. Los ingredientes vegetarianos son Pimiento y tofu; 
los ingredientes no vegetarianos son Peperoni, Jamón y Salmón. Escribir un programa que pregunte si se quiere una pizza vegetariana 
o no, muestre el menú de ingredientes y permita elegir uno. Al final, muestra si la pizza es vegetariana y todos los ingredientes que lleva.
"""
# Solución
# Fase 1: Entrada y validación de datos
def obtener_tipo_pizza():
    """Obtiene y valida el tipo de pizza que desea el usuario."""
    tipo = None
    while tipo not in ["vegetariana", "no vegetariana"]:
        tipo = input("¿Quieres una pizza vegetariana o no vegetariana? (vegetariana/no vegetariana): ").lower()
        if tipo not in ["vegetariana", "no vegetariana"]:
            print("Por favor, introduce 'vegetariana' o 'no vegetariana'.")
    return tipo

def obtener_ingrediente(tipo_pizza):
    """Muestra el menú de ingredientes y permite elegir uno."""
    if tipo_pizza == "vegetariana":
        ingredientes = ["Pimiento", "Tofu"]
    else:
        ingredientes = ["Peperoni", "Jamón", "Salmón"]

    ingrediente = None
    while ingrediente not in ingredientes:
        print(f"Ingredientes disponibles: {', '.join(ingredientes)}")
        ingrediente = input("Elige un ingrediente: ").capitalize()
        if ingrediente not in ingredientes:
            print("Por favor, elige un ingrediente válido.")
    return ingrediente

# Fase 2: Procesamiento
def preparar_pizza(tipo_pizza, ingrediente):
    """Prepara los ingredientes de la pizza seleccionada."""
    base = ["Mozzarella", "Tomate"]
    return base + [ingrediente], tipo_pizza

# Fase 3: Salida
def mostrar_pizza(ingredientes, tipo_pizza):
    """Muestra la pizza elegida y sus ingredientes."""
    print(f"Pizza {tipo_pizza} con ingredientes: {', '.join(ingredientes)}")

# Función principal
def main():
    tipo_pizza = obtener_tipo_pizza()
    ingrediente = obtener_ingrediente(tipo_pizza)
    ingredientes, tipo_pizza = preparar_pizza(tipo_pizza, ingrediente)
    mostrar_pizza(ingredientes, tipo_pizza)

if __name__ == "__main__":
    main()

# Test con pytest
def test_preparar_pizza():
    assert preparar_pizza("vegetariana", "Pimiento") == (["Mozzarella", "Tomate", "Pimiento"], "vegetariana")
    assert preparar_pizza("vegetariana", "Tofu") == (["Mozzarella", "Tomate", "Tofu"], "vegetariana")
    assert preparar_pizza("no vegetariana", "Peperoni") == (["Mozzarella", "Tomate", "Peperoni"], "no vegetariana")
    assert preparar_pizza("no vegetariana", "Jamón") == (["Mozzarella", "Tomate", "Jamón"], "no vegetariana")

