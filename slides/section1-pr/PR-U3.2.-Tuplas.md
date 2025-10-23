# U3.2 - Tuplas

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las tuplas?

* Colección ordenada e inmutable de elementos
* Se definen con paréntesis ()
* Pueden contener elementos de diferentes tipos
* Similares a listas pero no se pueden modificar
* Más eficientes en memoria que las listas

Note: Las tuplas son como listas inmutables. Una vez creadas, no puedes cambiar, añadir o eliminar elementos. Esta inmutabilidad tiene ventajas: son más rápidas, usan menos memoria, y pueden ser claves de diccionarios.


### Crear tuplas

```python
# Tupla vacía
vacia = ()
otra_vacia = tuple()

# Tupla con elementos
numeros = (1, 2, 3, 4, 5)
mixta = (1, 'dos', 3.0, True)

# Sin paréntesis (tuple packing)
coordenadas = 10, 20

# Tupla de un elemento (nota la coma)
un_elemento = (5,)    # Correcto
no_tupla = (5)        # Esto es solo el número 5

# Desde otra secuencia
lista = [1, 2, 3]
tupla = tuple(lista)
```

Note: Los paréntesis son opcionales para crear tuplas, pero es buena práctica usarlos. La coma es lo que define una tupla, no los paréntesis. Para tupla de un elemento, la coma es obligatoria: (5,) es tupla, (5) es solo número con paréntesis.


### Tuplas vs Listas

```python
# Lista: mutable
lista = [1, 2, 3]
lista[0] = 100  # OK
lista.append(4)  # OK

# Tupla: inmutable
tupla = (1, 2, 3)
# tupla[0] = 100  # TypeError: no se puede modificar
# tupla.append(4)  # AttributeError: no tiene append

# Rendimiento
import sys
print(sys.getsizeof([1, 2, 3]))  # ~80 bytes
print(sys.getsizeof((1, 2, 3)))  # ~64 bytes
```

Note: La principal diferencia es la mutabilidad. Las tuplas son inmutables: no puedes cambiar sus elementos después de crearlas. Son más eficientes en memoria y velocidad. Usa tuplas cuando los datos no deben cambiar: coordenadas, fechas, configuración, etc.

---

## Acceso a Elementos


### Indexación y slicing

* Igual que en listas y cadenas
* Índices comienzan en 0
* Índices negativos desde el final
* Slicing crea nueva tupla

```python
tupla = ('a', 'b', 'c', 'd', 'e')

# Indexación
print(tupla[0])    # 'a'
print(tupla[-1])   # 'e'

# Slicing
print(tupla[1:4])  # ('b', 'c', 'd')
print(tupla[:3])   # ('a', 'b', 'c')
print(tupla[2:])   # ('c', 'd', 'e')
print(tupla[::-1]) # ('e', 'd', 'c', 'b', 'a')
```

Note: La indexación y slicing funcionan idénticamente a listas y cadenas. La única diferencia es que las tuplas resultantes de slicing también son inmutables. [::-1] invierte la tupla.


### Longitud y pertenencia

```python
tupla = ('Python', 'Java', 'C++', 'JavaScript')

# Longitud
print(len(tupla))  # 4

# Pertenencia
print('Python' in tupla)        # True
print('Ruby' in tupla)          # False
print('Ruby' not in tupla)      # True

# Contar ocurrencias
numeros = (1, 2, 3, 2, 4, 2)
print(numeros.count(2))         # 3

# Encontrar índice
print(tupla.index('C++'))       # 2
# tupla.index('Ruby')  # ValueError
```

Note: len(), in, count() e index() funcionan igual que en listas. count() cuenta ocurrencias. index() devuelve el índice de la primera ocurrencia o lanza ValueError si no encuentra.

---

## Inmutabilidad


### No se pueden modificar

```python
tupla = (1, 2, 3)

# Intentar modificar causa error
# tupla[0] = 100  # TypeError
# tupla.append(4)  # AttributeError
# del tupla[0]     # TypeError

# Pero puedes crear una nueva
nueva = tupla + (4, 5)
print(nueva)  # (1, 2, 3, 4, 5)

# O reemplazar la variable completa
tupla = (10, 20, 30)  # Reasignación OK
```

Note: La inmutabilidad significa que no puedes cambiar elementos individuales, ni añadir ni eliminar elementos. Sin embargo, puedes crear nuevas tuplas concatenando, o reasignar la variable a una nueva tupla. La inmutabilidad es del objeto tupla, no de la variable.


### Tuplas con elementos mutables

```python
# Tupla contiene lista (mutable)
tupla = (1, 2, [3, 4])

# No puedes cambiar qué lista contiene
# tupla[2] = [5, 6]  # TypeError

# Pero puedes modificar la lista existente
tupla[2].append(5)
print(tupla)  # (1, 2, [3, 4, 5])

# La tupla sigue siendo "inmutable"
# (mismos objetos, pero un objeto cambió internamente)
```

Note: La inmutabilidad de tuplas es sobre las referencias, no sobre los objetos referenciados. Si una tupla contiene una lista, no puedes cambiar qué lista contiene, pero puedes modificar esa lista. En la práctica, evita objetos mutables en tuplas para mantener la intención de inmutabilidad.


### Ventajas de la inmutabilidad

```python
# 1. Pueden ser claves de diccionario
coordenadas = {
    (0, 0): 'origen',
    (1, 2): 'punto A',
    (3, 4): 'punto B'
}
# Las listas no pueden ser claves

# 2. Pueden ser elementos de conjuntos
puntos = {(0, 0), (1, 1), (2, 2)}
# Conjuntos de listas no son posibles

# 3. Más rápidas
import timeit
print(timeit.timeit('x = (1, 2, 3)', number=1000000))
print(timeit.timeit('x = [1, 2, 3]', number=1000000))
```

Note: La inmutabilidad permite usar tuplas como claves de diccionarios y elementos de conjuntos. Las tuplas son más rápidas de crear y acceder. Son perfectas para datos que no cambiarán: coordenadas, RGB, configuración, retorno múltiple de funciones.

---

## Operaciones con Tuplas


### Concatenación y repetición

```python
# Concatenación
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
combinada = tupla1 + tupla2
print(combinada)  # (1, 2, 3, 4, 5, 6)

# Repetición
repetida = (1, 2) * 3
print(repetida)  # (1, 2, 1, 2, 1, 2)

# Combinación
resultado = (0,) + (1, 2) * 2 + (3,)
print(resultado)  # (0, 1, 2, 1, 2, 3)

# Nota: estas operaciones crean nuevas tuplas
```

Note: + concatena tuplas, * repite tuplas. Ambas operaciones crean nuevas tuplas, no modifican las originales. Útiles para construir tuplas complejas desde partes más simples.


### Comparación de tuplas

```python
# Comparación elemento por elemento
print((1, 2, 3) == (1, 2, 3))      # True
print((1, 2, 3) == (1, 2, 4))      # False

# Orden lexicográfico
print((1, 2) < (1, 3))             # True
print((1, 2) < (1, 2, 3))          # True
print(('a', 'b') < ('b', 'a'))     # True

# Útil para ordenar
tuplas = [(2, 'b'), (1, 'a'), (3, 'c')]
print(sorted(tuplas))
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

Note: Las tuplas se comparan lexicográficamente: compara primer elemento, si son iguales compara segundo, etc. Esto las hace perfectas para ordenar por múltiples criterios. Por ejemplo, ordenar por (prioridad, nombre).

---

## Desempaquetado (Unpacking)


### Desempaquetado básico

```python
# Asignar elementos a variables
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)  # 1 2 3

# Sin paréntesis (tuple packing + unpacking)
x, y = 10, 20
print(x, y)  # 10 20

# Intercambiar variables
x, y = y, x
print(x, y)  # 20 10

# Número de variables debe coincidir
# a, b = (1, 2, 3)  # ValueError: demasiados valores
```

Note: El desempaquetado es una característica muy potente y pythónica. Permite asignar múltiples variables en una línea. El número de variables debe coincidir con elementos. El truco para intercambiar x, y = y, x es muy elegante.


### Desempaquetado con *

```python
# Capturar múltiples elementos
primero, *resto = (1, 2, 3, 4, 5)
print(primero)  # 1
print(resto)    # [2, 3, 4, 5] (es lista, no tupla)

# * en el medio
principio, *medio, final = (1, 2, 3, 4, 5)
print(principio)  # 1
print(medio)      # [2, 3, 4]
print(final)      # 5

# Ignorar elementos con _
primer, _, tercer = (1, 2, 3)
print(primer, tercer)  # 1 3
```

Note: * captura múltiples elementos en una lista. Solo puede haber un * en el desempaquetado. _ es convención para elementos que no usarás. Muy útil para funciones que retornan múltiples valores.


### Desempaquetado en bucles

```python
# Iterar sobre tuplas
puntos = [(1, 2), (3, 4), (5, 6)]

for x, y in puntos:
    print(f'x={x}, y={y}')

# Iterar sobre diccionario
persona = {'nombre': 'Ana', 'edad': 25}
for clave, valor in persona.items():
    print(f'{clave}: {valor}')

# Enumerate
frutas = ['manzana', 'banana', 'cereza']
for indice, fruta in enumerate(frutas):
    print(f'{indice}: {fruta}')
```

Note: El desempaquetado es muy común en bucles. enumerate() retorna tuplas (índice, valor). dict.items() retorna tuplas (clave, valor). zip() combina iterables en tuplas. El desempaquetado hace estos bucles muy legibles.

---

## Tuplas con Nombre


### namedtuple

```python
from collections import namedtuple

# Definir una namedtuple
Punto = namedtuple('Punto', ['x', 'y'])

# Crear instancias
p1 = Punto(10, 20)
p2 = Punto(x=30, y=40)

# Acceso por índice
print(p1[0])   # 10

# Acceso por nombre (más legible)
print(p1.x)    # 10
print(p1.y)    # 20

# Sigue siendo tupla inmutable
# p1.x = 100  # AttributeError
```

Note: namedtuple crea clases de tuplas con campos nombrados. Combina la eficiencia de tuplas con la legibilidad de atributos nombrados. Son inmutables como tuplas pero puedes acceder por nombre. Perfectas para registros simples.


### Ejemplo con namedtuple

```python
from collections import namedtuple

# Definir estructura de persona
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear personas
ana = Persona('Ana', 25, 'Madrid')
bob = Persona('Bob', 30, 'Barcelona')

# Acceso legible
print(f'{ana.nombre} tiene {ana.edad} años')

# Lista de personas
personas = [ana, bob]
for p in personas:
    print(f'{p.nombre} vive en {p.ciudad}')

# Convertir a diccionario
print(ana._asdict())
# OrderedDict([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Madrid')])
```

Note: namedtuple es ideal para representar registros con campos fijos: puntos, personas, configuración, etc. Son más eficientes que diccionarios y más legibles que tuplas normales. _asdict() convierte a diccionario. _replace() crea copia con cambios.

---

## Métodos y Funciones


### Métodos de tuplas

```python
tupla = (1, 2, 3, 2, 4, 2, 5)

# count: contar ocurrencias
print(tupla.count(2))     # 3
print(tupla.count(10))    # 0

# index: encontrar primera posición
print(tupla.index(2))     # 1
print(tupla.index(2, 2))  # 3 (desde índice 2)
# tupla.index(10)  # ValueError

# Solo estos dos métodos (es inmutable)
```

Note: Las tuplas solo tienen dos métodos: count() e index(). No tienen métodos que modifiquen como append, remove, etc. porque son inmutables. Esta simplicidad es por diseño: las tuplas son para datos que no cambian.


### Funciones con tuplas

```python
tupla = (5, 2, 8, 1, 9, 3)

# Funciones incorporadas
print(len(tupla))       # 6
print(max(tupla))       # 9
print(min(tupla))       # 1
print(sum(tupla))       # 28

# sorted devuelve lista ordenada
print(sorted(tupla))    # [1, 2, 3, 5, 8, 9]

# tuple() constructor
print(tuple('Python'))  # ('P', 'y', 't', 'h', 'o', 'n')
print(tuple([1, 2, 3])) # (1, 2, 3)
```

Note: Aunque las tuplas no tienen muchos métodos, las funciones incorporadas como min, max, sum funcionan perfectamente. sorted() devuelve una lista ordenada (no puede devolver tupla ordenada porque no puede modificar la tupla original).

---

## Casos de Uso


### Retorno múltiple de funciones

```python
def calcular_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros) / len(numeros)

# Desempaquetar resultado
minimo, maximo, promedio = calcular_estadisticas([1, 2, 3, 4, 5])
print(f'Min: {minimo}, Max: {maximo}, Avg: {promedio}')

# O usar como tupla
stats = calcular_estadisticas([1, 2, 3, 4, 5])
print(f'Estadísticas: {stats}')

# Coordenadas
def obtener_posicion():
    return 10, 20  # tupla implícita

x, y = obtener_posicion()
```

Note: Las tuplas son perfectas para retornar múltiples valores de funciones. Python permite retornar múltiples valores separados por comas (crea tupla implícita). Puedes desempaquetar directamente o usar como tupla. Más elegante que retornar lista o diccionario.


### Claves de diccionario

```python
# Coordenadas como claves
tablero = {
    (0, 0): 'vacío',
    (0, 1): 'pieza_blanca',
    (1, 0): 'pieza_negra'
}

print(tablero[(0, 1)])  # 'pieza_blanca'

# RGB como claves
colores = {
    (255, 0, 0): 'rojo',
    (0, 255, 0): 'verde',
    (0, 0, 255): 'azul'
}

# Compuestas
registro = {
    ('Ana', 25): 'datos1',
    ('Bob', 30): 'datos2'
}
```

Note: Las listas no pueden ser claves de diccionarios porque son mutables. Las tuplas sí pueden porque son inmutables y hashables. Esto las hace perfectas para claves compuestas: coordenadas, combinaciones, tuplas de identificación.


### Datos inmutables

```python
# Configuración que no debe cambiar
COLORES = (
    (255, 0, 0),    # Rojo
    (0, 255, 0),    # Verde
    (0, 0, 255)     # Azul
)

# Dimensiones fijas
RESOLUCION = (1920, 1080)

# Fechas (año, mes, día)
NACIMIENTO = (1995, 5, 15)

# Versión
VERSION = (1, 2, 3)  # 1.2.3

# Intento de modificar falla
# COLORES[0] = (255, 255, 255)  # TypeError
```

Note: Usa tuplas para datos que conceptualmente no deben cambiar: configuración, constantes, dimensiones fijas, fechas, versiones. La inmutabilidad documenta la intención: "estos datos no cambiarán". También previene modificaciones accidentales.

---

## Tuplas vs Listas: Cuándo Usar


### Usa tuplas cuando:

* Los datos no deben modificarse
* Necesitas clave de diccionario o elemento de conjunto
* Retornas múltiples valores de función
* Quieres eficiencia en memoria y velocidad
* Representas registros/estructuras con campos fijos

```python
# Tuplas: inmutables, eficientes
coordenadas = (10, 20)
fecha = (2024, 10, 20)
persona = ('Ana', 25, 'Madrid')
```

Note: Las tuplas son para datos que no cambiarán. Su inmutabilidad es una característica, no una limitación. Documentan intención y previenen errores. Son más eficientes que listas para datos estáticos.


### Usa listas cuando:

* Necesitas modificar, añadir o eliminar elementos
* El número de elementos puede cambiar
* Necesitas métodos como sort, append, remove
* Los elementos son homogéneos (mismo tipo)

```python
# Listas: mutables, dinámicas
tareas = ['comprar', 'estudiar', 'cocinar']
tareas.append('limpiar')
tareas.remove('comprar')

numeros = [1, 2, 3]
numeros.extend([4, 5])
numeros.sort()
```

Note: Las listas son para colecciones que crecen, se reducen o se reordenan. Son más versátiles pero menos eficientes. Si no necesitas mutabilidad, considera tuplas. La elección correcta documenta tu intención.

---

## Mejores Prácticas


### Preferir tuplas para datos fijos

```python
# Mal: lista para datos que no cambiarán
colores_rgb = [255, 0, 0]
dimensiones = [1920, 1080]

# Bien: tupla documenta inmutabilidad
colores_rgb = (255, 0, 0)
dimensiones = (1920, 1080)

# Mal: modificar "constantes"
colores_rgb[0] = 200  # Funciona pero no debería

# Bien: tupla previene modificación
# colores_rgb[0] = 200  # TypeError
```

Note: Si los datos no deben cambiar, usa tuplas. La inmutabilidad documenta intención y previene errores. Es autoexplicativo: tupla = inmutable, lista = mutable. Elige el tipo correcto según semántica, no solo por conveniencia.


### Usar unpacking en lugar de índices

```python
# Mal: acceso por índice
punto = (10, 20)
x = punto[0]
y = punto[1]

# Bien: unpacking legible
punto = (10, 20)
x, y = punto

# Mal: índices en retorno de función
def dividir(a, b):
    return a // b, a % b

resultado = dividir(10, 3)
cociente = resultado[0]
resto = resultado[1]

# Bien: unpacking directo
cociente, resto = dividir(10, 3)
```

Note: El unpacking es más legible que acceso por índice. Documenta qué significa cada valor. Es especialmente importante con retorno de funciones. Los nombres de variables explican el significado de cada elemento.


### Nombrar tuplas con namedtuple

```python
# Mal: tupla sin nombres
persona = ('Ana', 25, 'Madrid')
print(persona[0], persona[1])  # ¿qué es cada elemento?

# Bien: namedtuple legible
from collections import namedtuple
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
persona = Persona('Ana', 25, 'Madrid')
print(persona.nombre, persona.edad)  # Claro y legible

# Aún mejor para estructuras complejas
```

Note: Para tuplas con varios campos, namedtuple mejora dramáticamente la legibilidad. persona.nombre es mucho más claro que persona[0]. Si tu tupla tiene más de 2-3 elementos, considera namedtuple o incluso una clase.


### No temas la inmutabilidad

```python
# Está bien crear nuevas tuplas
tupla = (1, 2, 3)
tupla = tupla + (4,)  # Nueva tupla, está bien

# Mejor que lista innecesaria
# lista = [1, 2, 3]
# lista.append(4)

# Para muchas modificaciones, sí usa lista
elementos = []
for i in range(1000):
    elementos.append(calcular(i))
# Luego convierte a tupla si quieres inmutabilidad
elementos = tuple(elementos)
```

Note: No evites tuplas porque "no se pueden modificar". Crear nuevas tuplas con + está bien. La inmutabilidad es una ventaja. Si realmente necesitas muchas modificaciones, usa lista y conviértela a tupla al final si quieres inmutabilidad.

---

## Ejercicios Propuestos


### Ejercicio 1: Intercambiar elementos

Escribe una función que intercambie el primer y último elemento de una tupla.

```python
def intercambiar_extremos(tupla):
    # Tu código aquí
    pass

# Pruebas
print(intercambiar_extremos((1, 2, 3, 4)))
# (4, 2, 3, 1)
print(intercambiar_extremos(('a', 'b')))
# ('b', 'a')
```

Note: Recuerda que las tuplas son inmutables, debes crear una nueva. Usa slicing y concatenación: (tupla[-1],) + tupla[1:-1] + (tupla[0],). Considera casos especiales: tupla vacía, un elemento, dos elementos.


### Ejercicio 2: Aplanar tupla de tuplas

Crea una función que convierta una tupla de tuplas en una tupla plana.

```python
def aplanar(tupla_anidada):
    # Tu código aquí
    pass

# Pruebas
print(aplanar(((1, 2), (3, 4), (5, 6))))
# (1, 2, 3, 4, 5, 6)
print(aplanar((('a',), ('b', 'c'))))
# ('a', 'b', 'c')
```

Note: Puedes iterar concatenando, o usar comprensión: tuple(elem for subtupla in tupla for elem in subtupla). O sum con tupla vacía como inicio. Varias soluciones posibles.


### Ejercicio 3: Tuplas únicas

Escribe una función que elimine tuplas duplicadas de una lista de tuplas.

```python
def tuplas_unicas(lista):
    # Tu código aquí
    pass

# Pruebas
print(tuplas_unicas([(1, 2), (3, 4), (1, 2), (5, 6)]))
# [(1, 2), (3, 4), (5, 6)]
```

Note: Las tuplas son hashables, puedes usar conjunto: list(dict.fromkeys(lista)) mantiene orden, o set() si no importa. Alternativamente, itera verificando con in.


### Ejercicio 4: Distancia entre puntos

Crea una función que calcule la distancia euclidiana entre dos puntos representados como tuplas (x, y).

```python
def distancia(p1, p2):
    # Tu código aquí
    pass

# Pruebas
print(distancia((0, 0), (3, 4)))  # 5.0
print(distancia((1, 2), (4, 6)))  # 5.0
```

Note: Fórmula: sqrt((x2-x1)² + (y2-y1)²). Usa desempaquetado: x1, y1 = p1. Importa math.sqrt o usa **0.5. Buen ejemplo de tuplas para coordenadas.


### Ejercicio 5: Rotar tupla

Escribe una función que rote una tupla n posiciones a la derecha.

```python
def rotar_tupla(tupla, n):
    # Tu código aquí
    pass

# Pruebas
print(rotar_tupla((1, 2, 3, 4, 5), 2))
# (4, 5, 1, 2, 3)
print(rotar_tupla(('a', 'b', 'c'), 1))
# ('c', 'a', 'b')
```

Note: Similar a listas: tupla[-n:] + tupla[:-n]. Considera n mayor que longitud (usa n % len), n negativo (rota izquierda), tupla vacía. El slicing con tuplas crea nuevas tuplas.

---

## Resumen


### Conceptos clave

* Tuplas son colecciones ordenadas e inmutables
* Se definen con paréntesis () o solo comas
* Indexación y slicing igual que listas
* Solo dos métodos: count() e index()
* Perfectas para datos que no cambiarán
* Más eficientes que listas en memoria y velocidad

Note: Las tuplas complementan a las listas. No son "listas limitadas", tienen su propósito específico. La inmutabilidad es una característica poderosa, no una limitación. Elige tuplas o listas según la semántica de tus datos.


### Cuándo usar tuplas

* ✅ Retorno múltiple de funciones
* ✅ Claves de diccionarios
* ✅ Datos que conceptualmente no cambian
* ✅ Eficiencia en memoria/velocidad
* ✅ Desempaquetado de variables
* ❌ Colecciones que crecen/reducen
* ❌ Cuando necesitas ordenar/modificar in-place

Note: La elección entre tupla y lista debe basarse en la semántica, no solo en la funcionalidad. ¿Los datos cambiarán? Lista. ¿Los datos son fijos? Tupla. La elección correcta hace tu código más claro.


### Próximos pasos

* Practicar con ejercicios de tuplas
* Aprender diccionarios (siguiente tema)
* Experimentar con namedtuple
* Estudiar cuando usar cada estructura
* Trabajar con datos reales

Note: Las tuplas son más simples que listas pero igualmente importantes. Practica identificando cuándo usar cada una. Los próximos temas (diccionarios y conjuntos) también usan conceptos de inmutabilidad y hashabilidad.

---

## ¿Preguntas?

Note: Las tuplas son conceptualmente simples pero su uso correcto requiere entender inmutabilidad. Asegúrate de que los estudiantes entienden por qué y cuándo usar tuplas vs listas. La inmutabilidad es una característica, no una restricción.
