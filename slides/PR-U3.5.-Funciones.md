# U3.5 - Funciones

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Por qué funciones?

* Evitar repetir código (DRY - Don't Repeat Yourself)
* Dividir programas complejos en partes manejables
* Facilitar testing y depuración
* Reutilizar código en múltiples lugares
* Hacer código más legible y mantenible

Note: Las funciones son fundamentales en programación. Imagina copiar-pegar el mismo código 10 veces: si hay un bug, debes arreglarlo 10 veces. Con funciones, lo arreglas una vez. Las funciones son los bloques de construcción de programas grandes.


### ¿Qué es una función?

* Bloque de código reutilizable
* Tiene un nombre descriptivo
* Puede recibir datos (parámetros)
* Puede devolver resultados (return)
* Se ejecuta solo cuando se llama

```python
# Definir función
def saludar(nombre):
    return f'Hola, {nombre}!'

# Llamar función
mensaje = saludar('Ana')
print(mensaje)  # 'Hola, Ana!'
```

Note: Una función es como una mini-máquina: le das input (parámetros), hace algo, y te da output (retorno). La defines una vez con def, la usas muchas veces llamándola por nombre.


### Anatomía de una función

```python
def nombre_funcion(parametro1, parametro2):
    """Documentación de la función (docstring)"""
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado

# def: palabra clave
# nombre_funcion: identificador descriptivo
# (parametro1, parametro2): parámetros (entrada)
# ""docstring"": documentación
# return: devuelve valor (salida)
```

Note: Los componentes esenciales: def inicia definición, nombre debe ser descriptivo (snake_case), paréntesis contienen parámetros, dos puntos inician bloque, docstring documenta, return devuelve resultado.

---

## Definir y Llamar Funciones


### Definir función simple

```python
# Función sin parámetros ni retorno
def saludar():
    print('¡Hola!')

# Función con parámetro, sin retorno
def saludar_persona(nombre):
    print(f'Hola, {nombre}!')

# Función sin parámetros, con retorno
def obtener_pi():
    return 3.14159

# Función completa
def sumar(a, b):
    resultado = a + b
    return resultado
```

Note: Las funciones pueden tener 0+ parámetros y retornar o no retornar valor. Sin return, devuelven None implícitamente. Con return, devuelven el valor especificado. Elige según necesidad.


### Llamar funciones

```python
def multiplicar(a, b):
    return a * b

# Llamada básica
resultado = multiplicar(5, 3)
print(resultado)  # 15

# Usar directamente el resultado
print(multiplicar(10, 2))  # 20

# En expresiones
total = multiplicar(4, 5) + multiplicar(3, 2)
print(total)  # 26

# Llamadas anidadas
print(multiplicar(multiplicar(2, 3), 4))  # 24
```

Note: Llamar una función ejecuta su código. Captura el retorno en variable o úsalo directamente. Puedes llamar funciones dentro de expresiones o como argumentos de otras funciones. Las llamadas anidadas se evalúan de dentro hacia fuera.


### Retorno de valores

```python
# Retorno simple
def cuadrado(x):
    return x ** 2

# Retorno múltiple (tupla)
def dividir(a, b):
    cociente = a // b
    resto = a % b
    return cociente, resto

c, r = dividir(10, 3)  # c=3, r=1

# Retorno condicional
def es_par(numero):
    if numero % 2 == 0:
        return True
    return False

# Sin return explícito (devuelve None)
def imprimir_mensaje():
    print('Hola')
    # return None implícito
```

Note: return detiene la ejecución y devuelve valor. Puedes retornar múltiples valores como tupla y desempaquetar. Puedes tener múltiples returns (diferentes condiciones). Sin return, la función devuelve None.

---

## Parámetros y Argumentos


### Parámetros posicionales

```python
def restar(a, b):
    return a - b

# Orden importa
print(restar(10, 3))   # 7
print(restar(3, 10))   # -7

# Deben pasarse todos
print(restar(5, 2))    # OK
# print(restar(5))     # TypeError: falta 1 argumento
# print(restar(5,2,1)) # TypeError: sobra 1 argumento
```

Note: Los parámetros posicionales se asignan por posición. El orden importa: primer argumento → primer parámetro. Debes pasar exactamente el número correcto de argumentos. Es la forma más común y simple.


### Argumentos con nombre (keyword)

```python
def crear_usuario(nombre, edad, ciudad):
    return {'nombre': nombre, 'edad': edad, 'ciudad': ciudad}

# Posicionales (orden importa)
u1 = crear_usuario('Ana', 25, 'Madrid')

# Con nombre (orden no importa)
u2 = crear_usuario(edad=30, ciudad='Barcelona', nombre='Bob')

# Mixtos (posicionales primero)
u3 = crear_usuario('Carlos', ciudad='Valencia', edad=35)

# Más legible con nombres
u4 = crear_usuario(nombre='Diana', edad=28, ciudad='Sevilla')
```

Note: Los argumentos con nombre (keyword arguments) son más legibles y no dependen del orden. Puedes mezclar posicionales y con nombre, pero posicionales deben ir primero. Úsalos cuando hay muchos parámetros o el significado no es obvio.


### Parámetros con valor por defecto

```python
def saludar(nombre, saludo='Hola'):
    return f'{saludo}, {nombre}!'

# Usa valor por defecto
print(saludar('Ana'))          # 'Hola, Ana!'

# Sobreescribe valor por defecto
print(saludar('Bob', '¿Qué tal?'))     # '¿Qué tal?, Bob!'

# Múltiples valores por defecto
def conectar(host='localhost', port=8080, timeout=30):
    return f'Conectando a {host}:{port} (timeout:{timeout}s)'

print(conectar())                    # Todos por defecto
print(conectar('example.com'))       # Solo host
print(conectar(port=3000))           # Solo port
print(conectar('example.com', timeout=60))  # host y timeout
```

Note: Los parámetros con valores por defecto son opcionales al llamar. Deben ir después de los obligatorios en la definición. Úsalos para configuración común con opciones personalizables. Hacen las funciones más flexibles.


### Parámetros *args

* Captura argumentos posicionales adicionales
* Se recibe como tupla
* Por convención se llama args

```python
def sumar(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar(1, 2, 3))           # 6
print(sumar(10, 20, 30, 40))    # 100
print(sumar())                   # 0

# Con sum()
def sumar_mejorado(*numeros):
    return sum(numeros)

# Mixto con parámetros fijos
def procesar(operacion, *valores):
    print(f'Operación: {operacion}')
    print(f'Valores: {valores}')
```

Note: *args permite número variable de argumentos posicionales. Útil cuando no sabes cuántos argumentos recibirás. Internamente es una tupla. Puedes combinarlo con parámetros fijos (que van antes).


### Parámetros **kwargs

* Captura argumentos con nombre adicionales
* Se recibe como diccionario
* Por convención se llama kwargs

```python
def crear_config(**opciones):
    return opciones

config = crear_config(host='localhost', port=8080, debug=True)
print(config)  # {'host': 'localhost', 'port': 8080, 'debug': True}

# Procesar kwargs
def conectar(**config):
    host = config.get('host', 'localhost')
    port = config.get('port', 8080)
    print(f'Conectando a {host}:{port}')

conectar(host='example.com', port=3000)

# Mixto: fijos, *args, **kwargs
def funcion_completa(fijo, *args, **kwargs):
    print(f'Fijo: {fijo}')
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')
```

Note: **kwargs captura argumentos con nombre en un diccionario. Útil para funciones altamente configurables. Puedes combinar parámetros fijos, *args y **kwargs en ese orden. Muy flexible pero puede ser menos claro.

---

## Scope y Variables


### Scope local vs global

```python
# Variable global
mensaje = 'Global'

def funcion():
    # Variable local
    mensaje = 'Local'
    print(mensaje)  # 'Local'

funcion()
print(mensaje)  # 'Global' (sin cambios)

# Las locales no afectan globales
x = 10
def modificar():
    x = 20  # Crea local x, no modifica global
    print(x)  # 20

modificar()
print(x)  # 10 (sin cambios)
```

Note: Las variables definidas en funciones son locales: solo existen dentro de la función. Las globales existen fuera. Python busca primero en scope local, luego global. Asignar en función crea variable local, no modifica global.


### Keyword global

```python
contador = 0

def incrementar():
    global contador  # Indica que usarás la global
    contador += 1

incrementar()
print(contador)  # 1

incrementar()
print(contador)  # 2

# Sin global causaría error
def incrementar_mal():
    contador += 1  # UnboundLocalError

# Mejor: retornar y reasignar
def incrementar_bien(valor):
    return valor + 1

contador = incrementar_bien(contador)
```

Note: global permite modificar variables globales desde funciones. Generalmente se debe evitar: crea dependencias ocultas y dificulta testing. Mejor: pasar como parámetro y retornar nuevo valor. Usa global solo cuando realmente necesario.


### Keyword nonlocal

```python
def externa():
    x = 10
    
    def interna():
        nonlocal x  # Modifica x de externa()
        x = 20
    
    interna()
    print(x)  # 20 (modificado por interna)

externa()

# Sin nonlocal
def externa2():
    x = 10
    
    def interna2():
        x = 20  # Crea nuevo x local
    
    interna2()
    print(x)  # 10 (sin cambios)

externa2()
```

Note: nonlocal es para funciones anidadas. Permite modificar variables del scope enclosing (función contenedora). Sin nonlocal, se crea variable local. Útil en closures pero también debe usarse con cuidado.

---

## Docstrings


### ¿Qué son los docstrings?

* Documentación de la función
* Primera cadena después de def
* Accesible vía `__doc__`
* Mostrada por help()

```python
def calcular_area(base, altura):
    """
    Calcula el área de un triángulo.
    
    Args:
        base: Base del triángulo
        altura: Altura del triángulo
        
    Returns:
        Área del triángulo
    """
    return (base * altura) / 2

print(calcular_area.__doc__)
help(calcular_area)
```

Note: Los docstrings documentan qué hace la función, qué parámetros toma, qué retorna. Son la documentación oficial de Python. Herramientas las usan para generar documentación HTML. Siempre documenta funciones públicas.


### Formato de docstrings

```python
# Formato Google Style
def dividir(dividendo, divisor):
    """
    Divide dos números.
    
    Args:
        dividendo (float): Número a dividir
        divisor (float): Número por el cual dividir
        
    Returns:
        float: Resultado de la división
        
    Raises:
        ValueError: Si divisor es cero
        
    Example:
        >>> dividir(10, 2)
        5.0
    """
    if divisor == 0:
        raise ValueError('División por cero')
    return dividendo / divisor
```

Note: Hay varios formatos: Google, NumPy, Sphinx. Google Style es popular y legible. Documenta parámetros con tipo, retorno, excepciones, y ejemplos. Los ejemplos se pueden ejecutar con doctest.

---

## Funciones Lambda


### Sintaxis lambda

* Funciones anónimas de una línea
* Sintaxis: `lambda parametros: expresion`
* Retorna resultado de la expresión

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Lambda equivalente
cuadrado_lambda = lambda x: x ** 2

print(cuadrado(5))         # 25
print(cuadrado_lambda(5))  # 25

# Lambda con múltiples parámetros
sumar = lambda a, b: a + b
print(sumar(3, 4))  # 7

# Lambda sin parámetros
obtener_pi = lambda: 3.14159
print(obtener_pi())  # 3.14159
```

Note: Lambda crea funciones pequeñas inline. Solo puede contener una expresión (no statements como if, for). Son funciones reales pero sin nombre. Útiles para funciones simples de uso único.


### Cuándo usar lambda

```python
# Bueno: función simple de una línea
cuadrados = list(map(lambda x: x**2, [1, 2, 3, 4]))

# Bueno: como argumento
numeros = [4, 1, 3, 2]
numeros.sort(key=lambda x: -x)  # Ordenar descendente

# Malo: lambda compleja (mejor función normal)
# compleja = lambda x: x**2 if x > 0 else -x**2

# Malo: lambda con nombre (mejor def)
# calcular = lambda x, y: (x + y) * 2

# Mejor:
def calcular(x, y):
    return (x + y) * 2
```

Note: Lambda es para funciones triviales usadas una vez, típicamente como argumentos de map, filter, sort. Para funciones complejas o reusables, usa def. Lambda con nombre derrota su propósito (anónimo). Si necesitas nombre, usa def.


### Lambda con map, filter, sorted

```python
numeros = [1, 2, 3, 4, 5]

# map: transformar
cuadrados = list(map(lambda x: x**2, numeros))
# [1, 4, 9, 16, 25]

# filter: filtrar
pares = list(filter(lambda x: x % 2 == 0, numeros))
# [2, 4]

# sorted con key
palabras = ['Python', 'es', 'genial']
por_longitud = sorted(palabras, key=lambda p: len(p))
# ['es', 'Python', 'genial']

# Ordenar tuplas por segundo elemento
pares = [(1, 'd'), (2, 'b'), (3, 'a')]
ordenado = sorted(pares, key=lambda x: x[1])
# [(3, 'a'), (2, 'b'), (1, 'd')]
```

Note: Lambda brilla con funciones de alto orden: map, filter, sorted, max, min. Permite transformaciones concisas. Aunque comprensiones suelen ser más pythónicas para map/filter.


