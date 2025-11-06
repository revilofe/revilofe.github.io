# U3.1 - Listas

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las listas?

* Colección ordenada y mutable de elementos
* Pueden contener elementos de diferentes tipos
* Se definen con corchetes []
* Una de las estructuras más versátiles de Python
* Dinámicas: crecen y se reducen según necesidad

Note: Las listas son probablemente la estructura de datos más usada en Python. A diferencia de las cadenas, son mutables: puedes modificar, añadir y eliminar elementos. Pueden contener cualquier tipo de objeto, incluso otras listas.


### Crear listas

```python
# Lista vacía
vacia = []
otra_vacia = list()

# Lista con elementos
numeros = [1, 2, 3, 4, 5]
mixta = [1, 'dos', 3.0, True, [5, 6]]

# Lista desde otra secuencia
letras = list('Python')  # ['P', 'y', 't', 'h', 'o', 'n']
rango = list(range(5))   # [0, 1, 2, 3, 4]

# Lista por repetición
ceros = [0] * 5          # [0, 0, 0, 0, 0]
```

Note: Las listas son muy flexibles en su creación. list() convierte cualquier iterable en lista. La multiplicación crea listas con elementos repetidos. Cuidado: [0] * 5 funciona bien para inmutables, pero [[]] * 5 crea 5 referencias a la MISMA lista.


### Listas vs otras estructuras

* **vs Cadenas**: Listas son mutables, cadenas no
* **vs Tuplas**: Listas son mutables, tuplas no
* **vs Conjuntos**: Listas mantienen orden y permiten duplicados
* **vs Diccionarios**: Listas usan índices numéricos

```python
cadena = 'Python'
lista = list(cadena)
lista[0] = 'J'  # OK
# cadena[0] = 'J'  # Error: inmutable
```

Note: Entender cuándo usar cada estructura es clave. Listas cuando necesitas orden, mutabilidad y acceso por índice. Tuplas para datos que no cambiarán. Conjuntos para membresía rápida sin duplicados. Diccionarios para pares clave-valor.

---

## Acceso a Elementos


### Indexación

* Índices comienzan en 0
* Índices negativos desde el final
* IndexError si fuera de rango

```python
frutas = ['manzana', 'banana', 'cereza', 'durazno']

print(frutas[0])    # 'manzana' - primero
print(frutas[2])    # 'cereza' - tercero
print(frutas[-1])   # 'durazno' - último
print(frutas[-2])   # 'cereza' - penúltimo

# frutas[10]  # IndexError: fuera de rango
```

Note: La indexación en listas funciona igual que en cadenas. Los índices negativos son muy útiles para acceder desde el final sin conocer la longitud. Recuerda que los índices van de 0 a len(lista)-1.


### Slicing

* Sintaxis: [inicio:fin:paso]
* Crea una nueva lista (copia superficial)
* Índices opcionales

```python
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numeros[2:5])     # [2, 3, 4]
print(numeros[:3])      # [0, 1, 2]
print(numeros[7:])      # [7, 8, 9]
print(numeros[::2])     # [0, 2, 4, 6, 8]
print(numeros[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Copia de lista
copia = numeros[:]
```

Note: Slicing en listas es idéntico a cadenas. [:] crea una copia superficial de la lista completa. [::-1] invierte la lista. El slicing siempre devuelve una nueva lista, no modifica la original.


### Longitud y pertenencia

```python
frutas = ['manzana', 'banana', 'cereza']

# Longitud
print(len(frutas))  # 3

# Pertenencia
print('banana' in frutas)     # True
print('uva' in frutas)        # False
print('uva' not in frutas)    # True

# Contar ocurrencias
numeros = [1, 2, 3, 2, 4, 2]
print(numeros.count(2))       # 3
```

Note: len() devuelve el número de elementos. in verifica si un elemento está en la lista (búsqueda lineal, O(n)). count() cuenta cuántas veces aparece un elemento. Para búsquedas frecuentes en listas grandes, considera usar conjuntos.

---

## Modificar Listas


### Cambiar elementos

* Las listas son mutables
* Asignación directa con []
* Modificación in-place

```python
frutas = ['manzana', 'banana', 'cereza']

# Cambiar un elemento
frutas[1] = 'arándano'
print(frutas)  # ['manzana', 'arándano', 'cereza']

# Cambiar varios con slicing
numeros = [0, 1, 2, 3, 4, 5]
numeros[1:4] = [10, 20, 30]
print(numeros)  # [0, 10, 20, 30, 4, 5]

# Puede cambiar tamaño
numeros[1:4] = [100]
print(numeros)  # [0, 100, 4, 5]
```

Note: La mutabilidad es la característica principal de las listas. Puedes cambiar elementos individualmente o rangos completos con slicing. El slicing con asignación puede cambiar el tamaño de la lista. Esto es imposible con tuplas o cadenas.


### Añadir elementos

```python
frutas = ['manzana']

# append: añade al final
frutas.append('banana')
print(frutas)  # ['manzana', 'banana']

# insert: añade en posición específica
frutas.insert(1, 'cereza')
print(frutas)  # ['manzana', 'cereza', 'banana']

# extend: añade múltiples elementos
frutas.extend(['durazno', 'uva'])
print(frutas)  # ['manzana', 'cereza', 'banana', 'durazno', 'uva']

# += es equivalente a extend
frutas += ['kiwi']
```

Note: append() añade un elemento al final. insert(pos, elem) inserta en posición específica. extend() añade todos los elementos de un iterable. append([1,2]) añade una lista como elemento, extend([1,2]) añade 1 y 2 por separado.


### Eliminar elementos

```python
frutas = ['manzana', 'banana', 'cereza', 'durazno']

# remove: elimina primera ocurrencia del valor
frutas.remove('banana')
print(frutas)  # ['manzana', 'cereza', 'durazno']

# pop: elimina y retorna elemento por índice
ultima = frutas.pop()      # elimina última
print(ultima)              # 'durazno'
primera = frutas.pop(0)    # elimina primera
print(primera)             # 'manzana'

# del: elimina por índice o slice
del frutas[0]
del frutas[:]  # vacía la lista
```

Note: remove(valor) busca y elimina la primera ocurrencia. pop(índice) elimina por posición y devuelve el elemento. pop() sin argumentos elimina el último. del puede eliminar por índice o rangos completos. Si necesitas el elemento, usa pop. Si no, usa remove o del.


### Vaciar y copiar

```python
# Vaciar lista
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)  # []

# Copia superficial
original = [1, 2, [3, 4]]
copia = original.copy()    # o original[:]
copia[0] = 100
print(original)  # [1, 2, [3, 4]] - no afectado

# Pero cuidado con objetos mutables anidados
copia[2].append(5)
print(original)  # [1, 2, [3, 4, 5]] - afectado!
```

Note: clear() vacía la lista. copy() y [:] hacen copias superficiales: copian la lista pero no copian objetos mutables dentro de ella. Para copia profunda usa copy.deepcopy(). La diferencia es importante cuando hay listas u objetos mutables anidados.

---

## Métodos de Listas


### Buscar elementos

```python
frutas = ['manzana', 'banana', 'cereza', 'banana']

# index: encuentra posición
print(frutas.index('banana'))      # 1 (primera)
print(frutas.index('banana', 2))   # 3 (desde índice 2)
# frutas.index('uva')  # ValueError: no encontrado

# count: cuenta ocurrencias
print(frutas.count('banana'))      # 2
print(frutas.count('uva'))         # 0

# in: verifica existencia
if 'cereza' in frutas:
    print('Hay cerezas')
```

Note: index() devuelve el índice de la primera ocurrencia o lanza ValueError si no encuentra. Puedes especificar desde dónde buscar. count() cuenta cuántas veces aparece. Para verificar existencia sin excepción, usa in.


### Ordenar listas I

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# sort: ordena in-place (modifica la lista)
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]

# sort descendente
numeros.sort(reverse=True)
print(numeros)  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted: crea nueva lista ordenada
original = [3, 1, 4, 1, 5]
ordenada = sorted(original)
print(original)  # [3, 1, 4, 1, 5] - sin cambios
print(ordenada)  # [1, 1, 3, 4, 5]
```

Note: sort() modifica la lista original, sorted() crea una nueva. sort() es un método de lista, sorted() es una función incorporada que funciona con cualquier iterable. Usa sort() para eficiencia si no necesitas la lista original.


### Ordenar listas II

```python
# Ordenar cadenas
palabras = ['python', 'java', 'C++', 'JavaScript']
palabras.sort()
print(palabras)  # ['C++', 'JavaScript', 'java', 'python']

# Case-insensitive
palabras.sort(key=str.lower)
print(palabras)  # ['C++', 'java', 'JavaScript', 'python']

# Por longitud
palabras.sort(key=len)
print(palabras)  # ['C++', 'java', 'python', 'JavaScript']

# Personalizado
numeros = [-4, -2, 1, 3, -5]
numeros.sort(key=abs)  # Por valor absoluto
print(numeros)  # [1, -2, 3, -4, -5]
```

Note: El parámetro key permite personalizar el criterio de ordenamiento. key=str.lower ordena ignorando mayúsculas. key=len ordena por longitud. key puede ser cualquier función que tome un elemento y devuelva un valor comparable.


### Invertir listas

```python
numeros = [1, 2, 3, 4, 5]

# reverse: invierte in-place
numeros.reverse()
print(numeros)  # [5, 4, 3, 2, 1]

# Con slicing (crea nueva lista)
original = [1, 2, 3, 4, 5]
invertida = original[::-1]
print(original)   # [1, 2, 3, 4, 5]
print(invertida)  # [5, 4, 3, 2, 1]

# reversed: iterador (no lista)
for elemento in reversed(numeros):
    print(elemento)
```

Note: reverse() modifica la lista original. [::-1] crea una nueva lista invertida. reversed() devuelve un iterador, no una lista, útil para bucles pero necesitas list() para crear lista. reverse() es más eficiente en memoria que [::-1].

---

## Listas Anidadas


### Matrices y listas 2D

```python
# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acceso a elementos
print(matriz[0])      # [1, 2, 3] - primera fila
print(matriz[0][0])   # 1 - primer elemento de primera fila
print(matriz[1][2])   # 6 - tercer elemento de segunda fila

# Modificar elementos
matriz[0][1] = 20
print(matriz[0])      # [1, 20, 3]
```

Note: Las listas pueden contener otras listas, creando estructuras multidimensionales. matriz[i][j] accede a fila i, columna j. Son útiles para representar tableros de juego, imágenes, datos tabulares, etc.


### Iterar sobre matrices

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterar por filas
for fila in matriz:
    print(fila)

# Iterar por elementos
for fila in matriz:
    for elemento in elemento en fila:
        print(elemento, end=' ')
    print()

# Con enumerate
for i, fila in enumerate(matriz):
    for j, elemento in enumerate(fila):
        print(f'[{i}][{j}] = {elemento}')
```

Note: Para procesar todos los elementos necesitas bucles anidados. El bucle externo recorre filas, el interno recorre elementos de cada fila. enumerate() es útil para obtener índices y valores simultáneamente.


### Cuidado con referencias

```python
# Mal: crea referencias a la misma lista
matriz = [[0] * 3] * 3
matriz[0][0] = 1
print(matriz)
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - todas cambian!

# Bien: crea listas independientes
matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1
print(matriz)
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]] - solo primera cambia

# Comprensión de lista asegura independencia
```

Note: [[0]*3]*3 crea 3 referencias a la MISMA lista. Modificar una modifica todas. Usa list comprehension para crear listas independientes. Este es un error muy común que causa bugs sutiles.

---

## Operaciones con Listas


### Concatenación y repetición

```python
# Concatenación con +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2
print(combinada)  # [1, 2, 3, 4, 5, 6]

# Repetición con *
repetida = [0] * 5
print(repetida)  # [0, 0, 0, 0, 0]

# Cuidado con objetos mutables
lista = [[]] * 3  # Tres referencias a la MISMA lista!

# Combinación
lista = [1, 2] * 2 + [3]
print(lista)  # [1, 2, 1, 2, 3]
```

Note: + concatena listas creando una nueva. * repite elementos. Cuidado: *replication* con objetos mutables crea referencias, no copias. [[]]*3 crea tres referencias a la misma lista vacía. Para listas independientes, usa comprensión de lista.


### Comparación de listas

```python
# Igualdad: mismo contenido y orden
print([1, 2, 3] == [1, 2, 3])      # True
print([1, 2, 3] == [3, 2, 1])      # False

# Orden lexicográfico
print([1, 2] < [1, 3])             # True
print([1, 2] < [1, 2, 3])          # True
print(['a', 'b'] < ['b', 'a'])     # True

# Identidad: mismo objeto en memoria
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b)  # True - mismo objeto
print(a is c)  # False - diferente objeto
print(a == c)  # True - mismo contenido
```

Note: == compara contenido y orden. < compara lexicográficamente elemento por elemento. is verifica si son el mismo objeto en memoria. == e is son diferentes: == verifica valor, is verifica identidad. Entender la diferencia es crucial.

---

## List Comprehensions


### Sintaxis básica

* Forma concisa de crear listas
* Más legible que bucles
* Más eficiente

```python
# Sin comprehension
cuadrados = []
for x in range(10):
    cuadrados.append(x ** 2)

# Con comprehension
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Otro ejemplo
palabras = ['python', 'java', 'c++']
mayusculas = [palabra.upper() for palabra in palabras]
print(mayusculas)  # ['PYTHON', 'JAVA', 'C++']
```

Note: List comprehensions son una característica muy pythónica. Son más concisas y generalmente más rápidas que bucles equivalentes con append(). La sintaxis es: [expresión for variable in iterable].


### Comprehensions con condición

```python
# Filtrar elementos
numeros = range(10)
pares = [x for x in numeros if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Transformar y filtrar
palabras = ['Python', 'es', 'genial']
largas = [p.upper() for p in palabras if len(p) > 3]
print(largas)  # ['PYTHON', 'GENIAL']

# Múltiples condiciones
nums = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(nums)  # [0, 6, 12, 18]
```

Note: Puedes añadir if al final para filtrar elementos. Solo se incluyen elementos que cumplen la condición. Puedes tener múltiples ifs (todos deben ser True). Esto reemplaza filter() de forma más legible.


### Comprehensions anidadas

```python
# Matriz transpuesta
matriz = [[1, 2, 3], [4, 5, 6]]
transpuesta = [[fila[i] for fila in matriz] for i in range(3)]
print(transpuesta)  # [[1, 4], [2, 5], [3, 6]]

# Aplanar lista de listas
anidada = [[1, 2], [3, 4], [5, 6]]
plana = [elemento for sublista in anidada for elemento in sublista]
print(plana)  # [1, 2, 3, 4, 5, 6]

# Combinaciones
colores = ['rojo', 'verde']
tamaños = ['S', 'M']
productos = [f'{c} {t}' for c in colores for t in tamaños]
print(productos)  # ['rojo S', 'rojo M', 'verde S', 'verde M']
```

Note: Las comprehensions pueden anidarse pero cuidado con la legibilidad. Para casos complejos, un bucle normal puede ser más claro. El orden de los for en comprehensions anidadas es de izquierda a derecha, como bucles anidados.

---

## Iteración sobre Listas


### For loop básico

```python
frutas = ['manzana', 'banana', 'cereza']

# Iterar sobre elementos
for fruta in frutas:
    print(fruta)

# No hagas esto (no pythónico)
for i in range(len(frutas)):
    print(frutas[i])

# Tampoco esto
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1
```

Note: En Python, siempre itera directamente sobre los elementos, no sobre índices. Es más legible, menos propenso a errores, y más eficiente. Solo usa índices si realmente los necesitas (para modificar la lista, por ejemplo).


### Enumerate para índices y valores

```python
frutas = ['manzana', 'banana', 'cereza']

# Con enumerate
for i, fruta in enumerate(frutas):
    print(f'{i}: {fruta}')
# 0: manzana
# 1: banana  
# 2: cereza

# Empezar desde índice diferente
for i, fruta in enumerate(frutas, start=1):
    print(f'{i}. {fruta}')
# 1. manzana
# 2. banana
# 3. cereza
```

Note: enumerate() es la forma pythónica de obtener índice y valor simultáneamente. Devuelve tuplas (índice, valor). El parámetro start permite empezar desde un número diferente. Mucho mejor que usar range(len()).


### Iterar sobre múltiples listas

```python
nombres = ['Ana', 'Bob', 'Carlos']
edades = [25, 30, 35]
ciudades = ['Madrid', 'Barcelona', 'Valencia']

# Con zip
for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f'{nombre}, {edad} años, vive en {ciudad}')

# zip se detiene en la lista más corta
lista1 = [1, 2, 3]
lista2 = ['a', 'b']
print(list(zip(lista1, lista2)))  # [(1, 'a'), (2, 'b')]

# Desempaquetar zip
pares = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letras = zip(*pares)
print(nums)    # (1, 2, 3)
print(letras)  # ('a', 'b', 'c')
```

Note: zip() combina múltiples iterables en tuplas. Se detiene cuando se acaba el iterable más corto. zip(*lista) es el opuesto, desempaqueta lista de tuplas. Muy útil para procesar datos relacionados en paralelo.

---

## Copias de Listas


### Copia superficial vs profunda

```python
import copy

# Referencia (no es copia)
original = [1, 2, [3, 4]]
referencia = original
referencia[0] = 100
print(original)  # [100, 2, [3, 4]] - cambió!

# Copia superficial
copia_super = original.copy()  # o original[:] o list(original)
copia_super[0] = 1
print(original)  # [100, 2, [3, 4]] - no cambió el número
copia_super[2].append(5)
print(original)  # [100, 2, [3, 4, 5]] - sí cambió la lista interna!

# Copia profunda
copia_prof = copy.deepcopy(original)
copia_prof[2].append(6)
print(original)  # [100, 2, [3, 4, 5]] - no cambió!
```

Note: Asignación simple crea una referencia, no una copia. Copia superficial copia la lista pero no objetos mutables dentro. Copia profunda copia recursivamente todo. Usa deepcopy cuando tengas listas anidadas u objetos mutables.


### Cuándo usar cada tipo

```python
# Referencia: quieres que ambas variables apunten a la misma lista
resultado = procesar_datos(lista)
guardar_resultado(resultado)

# Copia superficial: lista simple sin objetos mutables anidados
numeros = [1, 2, 3, 4, 5]
respaldo = numeros.copy()
numeros.sort()  # respaldo no se ordena

# Copia profunda: listas anidadas u objetos mutables
matriz = [[1, 2], [3, 4]]
otra_matriz = copy.deepcopy(matriz)
matriz[0][0] = 100
# otra_matriz no se afecta
```

Note: La elección depende de tu necesidad. Referencias son para cuando quieres que los cambios se reflejen. Copias superficiales son suficientes y eficientes para listas simples. Copias profundas solo cuando necesitas independencia total, tienen costo de rendimiento.

---

## Listas como Pilas y Colas


### Lista como pila (LIFO)

* Last In, First Out
* Usa append() y pop()

```python
pila = []

# Push: añadir al final
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)  # [1, 2, 3]

# Pop: sacar del final
elemento = pila.pop()
print(elemento)  # 3
print(pila)      # [1, 2]

# Peek: ver último sin sacar
if pila:
    ultimo = pila[-1]
```

Note: Las listas son excelentes para implementar pilas. append() añade al final (O(1)), pop() saca del final (O(1)). Verifica que la pila no esté vacía antes de pop() para evitar IndexError. Usa if pila para verificar.


### Lista como cola (FIFO)

* First In, First Out
* Usa append() y pop(0)
* Mejor: collections.deque

```python
# Con lista (ineficiente)
cola = []
cola.append(1)
cola.append(2)
cola.append(3)
primero = cola.pop(0)  # O(n) - lento!

# Con deque (eficiente)
from collections import deque
cola = deque()
cola.append(1)
cola.append(2)
cola.append(3)
primero = cola.popleft()  # O(1) - rápido!
print(primero)  # 1
```

Note: Las listas no son ideales para colas porque pop(0) es O(n) (debe mover todos los elementos). Para colas, usa collections.deque que implementa popleft() en O(1). deque (double-ended queue) es eficiente para añadir/sacar de ambos extremos.

---

## Mejores Prácticas


### Usar comprehensions cuando sea claro

```python
# Bien: comprehension clara
cuadrados = [x**2 for x in range(10)]

# Mal: comprehension compleja (mejor bucle normal)
resultado = [proceso_complejo(x, y, z) 
             for x in lista1 
             for y in lista2 
             for z in lista3 
             if condicion_compleja(x, y, z)]

# Bien: bucle normal más legible
resultado = []
for x in lista1:
    for y in lista2:
        for z in lista3:
            if condicion_compleja(x, y, z):
                resultado.append(proceso_complejo(x, y, z))
```

Note: Las comprehensions son pythónicas y eficientes, pero la legibilidad es más importante. Si la comprehension es compleja o requiere múltiples líneas, usa un bucle normal. La regla: si no cabe cómodamente en una línea, probablemente un bucle es mejor.


### Evitar modificar lista durante iteración

```python
# Mal: modificar mientras iteras
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Salta elementos!

# Bien: iterar sobre copia
for num in numeros[:]:
    if num % 2 == 0:
        numeros.remove(num)

# Mejor: comprehension
numeros = [num for num in numeros if num % 2 != 0]
```

Note: Nunca modifiques una lista mientras iteras sobre ella, causará comportamiento inesperado. Soluciones: iterar sobre copia (numeros[:]), crear nueva lista con comprehension, o iterar hacia atrás con reversed(). La comprehension suele ser la más clara.


### Verificar lista vacía

```python
# Bien: pythónico
lista = []
if not lista:
    print('Lista vacía')

if lista:
    print('Lista tiene elementos')

# Evitar (no pythónico)
if len(lista) == 0:
    print('Lista vacía')

if len(lista) > 0:
    print('Lista tiene elementos')
```

Note: En Python, listas vacías son falsas (falsy), listas con elementos son verdaderas (truthy). Usa if lista o if not lista en lugar de comparar len(). Es más pythónico y más eficiente (no necesita calcular longitud).


### Inicializar listas según necesidad

```python
# Mal: lista pre-inicializada innecesariamente
resultado = [None] * 100
for i in range(10):  # Solo usa 10
    resultado[i] = calcular(i)

# Bien: lista crece según necesidad
resultado = []
for i in range(10):
    resultado.append(calcular(i))

# Mejor: comprehension
resultado = [calcular(i) for i in range(10)]

# OK: cuando realmente necesitas tamaño fijo
matriz = [[0] * columnas for _ in range(filas)]
```

Note: No pre-inicialices listas a menos que sea necesario. Las listas dinámicas de Python son eficientes. Pre-inicializa solo si necesitas índices específicos o tamaño fijo conocido (como matrices). En la mayoría de casos, append() o comprehension son mejores.

---

## Ejercicios Propuestos


### Ejercicio 1: Eliminar duplicados

Escribe una función que elimine elementos duplicados de una lista manteniendo el orden.

```python
def eliminar_duplicados(lista):
    # Tu código aquí
    pass

# Pruebas
print(eliminar_duplicados([1, 2, 2, 3, 4, 4, 5]))
# [1, 2, 3, 4, 5]
print(eliminar_duplicados(['a', 'b', 'a', 'c']))
# ['a', 'b', 'c']
```

Note: Varias soluciones posibles: iterar verificando con in, usar diccionario para preservar orden (dict.fromkeys()), o usar conjunto si no importa el orden. Recuerda que set() elimina duplicados pero no mantiene orden (en Python < 3.7).


### Ejercicio 2: Rotar lista

Crea una función que rote una lista n posiciones a la derecha.

```python
def rotar(lista, n):
    # Tu código aquí
    pass

# Pruebas
print(rotar([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3]
print(rotar([1, 2, 3], 1))         # [3, 1, 2]
```

Note: Usa slicing: lista[-n:] + lista[:-n]. Considera casos especiales: n mayor que longitud (usa n % len), n negativo (rota izquierda), lista vacía. Piensa en rotación como mover elementos del final al principio.


### Ejercicio 3: Encontrar segundo mayor

Escribe una función que encuentre el segundo elemento más grande de una lista.

```python
def segundo_mayor(lista):
    # Tu código aquí
    pass

# Pruebas
print(segundo_mayor([1, 5, 3, 9, 2]))  # 5
print(segundo_mayor([10, 10, 9, 8]))   # 9
```

Note: Opciones: ordenar y tomar segundo, o mantener dos variables (mayor y segundo_mayor) actualizándolas en un bucle. Considera duplicados del mayor. La solución con dos variables es O(n), ordenar es O(n log n).


### Ejercicio 4: Partir lista en chunks

Crea una función que divida una lista en sublistas de tamaño n.

```python
def partir_lista(lista, n):
    # Tu código aquí
    pass

# Pruebas
print(partir_lista([1, 2, 3, 4, 5, 6, 7], 3))
# [[1, 2, 3], [4, 5, 6], [7]]
print(partir_lista(['a', 'b', 'c', 'd'], 2))
# [['a', 'b'], ['c', 'd']]
```

Note: Usa slicing en un bucle: [lista[i:i+n] for i in range(0, len(lista), n)]. El último chunk puede ser menor que n. Este patrón es común para procesar datos por lotes.


### Ejercicio 5: Mezclar dos listas ordenadas

Escribe una función que mezcle dos listas ordenadas en una sola lista ordenada.

```python
def mezclar_ordenadas(lista1, lista2):
    # Tu código aquí
    pass

# Pruebas
print(mezclar_ordenadas([1, 3, 5], [2, 4, 6]))
# [1, 2, 3, 4, 5, 6]
print(mezclar_ordenadas([1, 2, 7], [3, 5]))
# [1, 2, 3, 5, 7]
```

Note: Dos enfoques: (1) concatenar y ordenar (simple pero O(n log n)), (2) merge manual (O(n) pero más código). Para listas ya ordenadas, merge manual es más eficiente. Este es el núcleo del algoritmo merge sort.


### Ejercicio 6: Matriz transpuesta

Crea una función que transponga una matriz (intercambie filas por columnas).

```python
def transponer(matriz):
    # Tu código aquí
    pass

# Pruebas
print(transponer([[1, 2, 3], [4, 5, 6]]))
# [[1, 4], [2, 5], [3, 6]]
```

Note: Usa comprehension anidada: [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]. También puedes usar zip(*matriz) que es muy pythónico. Asegúrate de que todas las filas tengan la misma longitud.

---

## Resumen


### Conceptos clave

* Listas son colecciones ordenadas y mutables
* Indexación y slicing como cadenas
* Métodos: append, extend, insert, remove, pop, sort
* Comprehensions para crear listas concisamente
* Iterate sobre elementos, no índices
* Cuidado con copias superficiales vs profundas

Note: Las listas son la estructura de datos más versátil de Python. Su mutabilidad las hace perfectas para colecciones dinámicas. Dominar listas es esencial para cualquier programador Python.


### Métodos más importantes

* **Modificación**: append, extend, insert, remove, pop, clear
* **Búsqueda**: index, count, in
* **Ordenamiento**: sort, reverse
* **Creación**: list(), [:], copy(), comprehensions

Note: No necesitas memorizar todo, solo los métodos más comunes. La práctica hará que los recuerdes naturalmente. Consulta la documentación cuando necesites algo específico.


### Próximos pasos

* Practicar con ejercicios variados
* Aprender tuplas (siguiente tema)
* Estudiar algoritmos de búsqueda y ordenamiento
* Explorar estructuras más avanzadas (deque, heapq)
* Trabajar con datos reales

Note: Las listas son fundamentales. Practica mucho con ejercicios variados. Los próximos temas (tuplas, diccionarios, conjuntos) se construyen sobre estos conceptos. Entender listas profundamente facilita todo lo demás.

---

## ¿Preguntas?

Note: Las listas son extensas y tienen muchas aplicaciones. Asegúrate de que los estudiantes entienden mutabilidad, indexación, y los métodos principales. Anima a experimentar y cometer errores, es la mejor forma de aprender.
