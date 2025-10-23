# U3.4 - Conjuntos (Sets)

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son los conjuntos?

* Colección desordenada de elementos únicos
* Sin duplicados automáticamente
* Elementos deben ser hashables (inmutables)
* Operaciones matemáticas de conjuntos
* Muy eficientes para pertenencia y unicidad

Note: Los conjuntos son la implementación de Python de los conjuntos matemáticos. Su característica principal: solo elementos únicos. Son desordenados: no mantienen orden de inserción. Perfectos para eliminar duplicados y operaciones de conjunto.


### Características principales

* **Desordenados**: No mantienen orden de inserción
* **Elementos únicos**: Duplicados se eliminan automáticamente
* **Mutables**: set es mutable, frozenset inmutable
* **Hashables**: Solo elementos inmutables
* **Eficientes**: Pertenencia O(1) vs O(n) en listas

Note: La falta de orden puede sorprender viniendo de listas. Los elementos deben ser hashables (números, strings, tuplas inmutables). La verificación de pertenencia es tan rápida como en diccionarios.


### Casos de uso

* Eliminar duplicados de listas
* Verificar pertenencia rápidamente
* Operaciones matemáticas (unión, intersección)
* Encontrar elementos únicos/comunes
* Implementar algoritmos eficientes

```python
# Eliminar duplicados
lista = [1, 2, 2, 3, 3, 3, 4]
unicos = list(set(lista))  # [1, 2, 3, 4]

# Verificar pertenencia rápida
permitidos = {1, 2, 3, 4, 5}
if numero in permitidos:  # O(1)
    procesar(numero)
```

Note: El caso de uso más común: eliminar duplicados. La conversión set→list es el patrón estándar. La búsqueda en conjuntos es muchísimo más rápida que en listas para colecciones grandes.

---

## Crear Conjuntos


### Formas de crear conjuntos

```python
# 1. Literales con llaves
s1 = {1, 2, 3, 4, 5}

# 2. Constructor set()
s2 = set([1, 2, 3, 4, 5])

# 3. Desde string (cada carácter)
s3 = set('Python')  # {'P', 'y', 't', 'h', 'o', 'n'}

# 4. Desde cualquier iterable
s4 = set(range(5))  # {0, 1, 2, 3, 4}

# 5. Conjunto vacío (¡solo con set()!)
s5 = set()  # Correcto
# s6 = {}   # ¡ERROR! Esto es diccionario vacío
```

Note: Cuidado: {} crea diccionario vacío, no conjunto. Usa set() para conjunto vacío. Los literales {1, 2, 3} solo funcionan con elementos. Los duplicados se eliminan automáticamente al crear.


### Comprehensions de conjuntos

```python
# Básica
cuadrados = {x**2 for x in range(10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Con condición
pares = {x for x in range(20) if x % 2 == 0}
# {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}

# Desde strings
vocales = {c.lower() for c in 'Python Programación' if c.lower() in 'aeiou'}
# {'a', 'i', 'o'}

# Combinación
palabras = ['Hola', 'mundo', 'hola']
unicos_lower = {p.lower() for p in palabras}
# {'hola', 'mundo'}
```

Note: Las comprensiones de conjuntos son muy potentes. Sintaxis similar a comprensiones de lista pero con {}. Los duplicados se eliminan automáticamente. Útil para transformar y filtrar datos únicos.


### set vs frozenset

```python
# set: mutable
s = {1, 2, 3}
s.add(4)      # OK
s.remove(1)   # OK

# frozenset: inmutable
fs = frozenset([1, 2, 3])
# fs.add(4)   # AttributeError
# fs.remove(1)  # AttributeError

# frozenset puede ser clave de diccionario
d = {fs: 'valor'}  # OK
# d = {s: 'valor'}  # TypeError

# frozenset en conjunto
conjunto_de_conjuntos = {frozenset([1, 2]), frozenset([3, 4])}
```

Note: frozenset es la versión inmutable de set. No puedes modificarlo después de crearlo. Es hashable: puede ser clave de diccionario o elemento de otro conjunto. Usa frozenset cuando necesites inmutabilidad.

---

## Operaciones Básicas


### Añadir elementos

```python
s = {1, 2, 3}

# add: añade un elemento
s.add(4)
print(s)  # {1, 2, 3, 4}

# add no produce error si existe
s.add(2)
print(s)  # {1, 2, 3, 4} - sin cambios

# update: añade múltiples elementos
s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}

# update acepta cualquier iterable
s.update({8, 9}, [10], (11,))
print(s)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
```

Note: add() añade un elemento. update() añade múltiples desde iterable(s). Añadir elemento existente no causa error ni duplicado. update() puede tomar múltiples iterables como argumentos.


### Eliminar elementos

```python
s = {1, 2, 3, 4, 5}

# remove: elimina elemento (KeyError si no existe)
s.remove(3)
print(s)  # {1, 2, 4, 5}
# s.remove(10)  # KeyError

# discard: elimina elemento (sin error si no existe)
s.discard(4)
print(s)  # {1, 2, 5}
s.discard(10)  # No hace nada, sin error

# pop: elimina y devuelve elemento arbitrario
elemento = s.pop()
print(elemento)  # Algún elemento (orden impredecible)
print(s)  # Sin ese elemento

# clear: elimina todos los elementos
s.clear()
print(s)  # set()
```

Note: remove() lanza KeyError si elemento no existe, discard() no. pop() devuelve elemento arbitrario (conjuntos no tienen orden). clear() vacía el conjunto completamente. Elige según necesites manejar ausencia.


### Tamaño y pertenencia

```python
s = {1, 2, 3, 4, 5}

# len: número de elementos
print(len(s))  # 5

# in: verificar pertenencia (O(1))
print(3 in s)        # True
print(10 in s)       # False
print(6 not in s)    # True

# Comparación con listas
lista_grande = list(range(1000000))
conjunto_grande = set(lista_grande)

# conjunto: O(1) - instantáneo
print(999999 in conjunto_grande)

# lista: O(n) - lento para listas grandes
print(999999 in lista_grande)
```

Note: in con conjuntos es O(1), increíblemente rápido incluso con millones de elementos. Con listas es O(n), proporcional al tamaño. Para verificaciones de pertenencia frecuentes, convierte a conjunto.

---

## Operaciones de Conjuntos


### Unión (|)

* Todos los elementos de ambos conjuntos
* Sin duplicados

```python
a = {1, 2, 3}
b = {3, 4, 5}

# Con operador |
union = a | b
print(union)  # {1, 2, 3, 4, 5}

# Con método union()
union = a.union(b)
print(union)  # {1, 2, 3, 4, 5}

# Múltiples conjuntos
c = {5, 6, 7}
union = a | b | c
print(union)  # {1, 2, 3, 4, 5, 6, 7}

# union acepta cualquier iterable
union = a.union([6, 7], (8, 9))
```

Note: La unión combina todos los elementos únicos. | es el operador matemático estándar. union() es el método equivalente. Ambos crean nuevo conjunto sin modificar originales. union() acepta iterables, | solo conjuntos.


### Intersección (&)

* Solo elementos comunes a ambos

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Con operador &
interseccion = a & b
print(interseccion)  # {3, 4}

# Con método intersection()
interseccion = a.intersection(b)
print(interseccion)  # {3, 4}

# Múltiples conjuntos
c = {4, 5, 6, 7}
interseccion = a & b & c
print(interseccion)  # {4}

# Caso común: encontrar elementos comunes
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
comunes = set(lista1) & set(lista2)
```

Note: La intersección encuentra elementos en todos los conjuntos. Útil para encontrar coincidencias, elementos comunes, filtrado basado en pertenencia. Si no hay elementos comunes, devuelve conjunto vacío.


### Diferencia (-)

* Elementos en primer conjunto pero no en segundo

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

# Con operador -
diferencia = a - b
print(diferencia)  # {1, 2, 3}

# Con método difference()
diferencia = a.difference(b)
print(diferencia)  # {1, 2, 3}

# Orden importa
diferencia_inversa = b - a
print(diferencia_inversa)  # {6, 7}

# Múltiples conjuntos
c = {2, 3}
diferencia = a - b - c
print(diferencia)  # {1}
```

Note: La diferencia a - b son elementos en a que NO están en b. El orden importa: a - b ≠ b - a. Útil para filtrar, excluir elementos, encontrar elementos únicos a un conjunto.


### Diferencia simétrica (^)

* Elementos en uno u otro, pero no en ambos

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Con operador ^
diff_sim = a ^ b
print(diff_sim)  # {1, 2, 5, 6}

# Con método symmetric_difference()
diff_sim = a.symmetric_difference(b)
print(diff_sim)  # {1, 2, 5, 6}

# Equivalente a (a - b) | (b - a)
diff_sim_alt = (a - b) | (b - a)
print(diff_sim_alt)  # {1, 2, 5, 6}

# Es conmutativa: a ^ b == b ^ a
print(a ^ b == b ^ a)  # True
```

Note: La diferencia simétrica son elementos exclusivos a cada conjunto (XOR). Es como unión menos intersección. Útil para encontrar diferencias totales, cambios entre versiones, elementos no compartidos.


### Operadores compuestos

```python
a = {1, 2, 3}
b = {3, 4, 5}

# |= : update (unión in-place)
a |= b
print(a)  # {1, 2, 3, 4, 5}

# &= : intersection_update
a = {1, 2, 3, 4, 5}
a &= {3, 4, 5, 6}
print(a)  # {3, 4, 5}

# -= : difference_update
a = {1, 2, 3, 4, 5}
a -= {4, 5, 6}
print(a)  # {1, 2, 3}

# ^= : symmetric_difference_update
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)  # {1, 2, 5, 6}
```

Note: Los operadores compuestos modifican el conjunto original en lugar de crear uno nuevo. Son más eficientes en memoria. Útiles cuando ya no necesitas el conjunto original. Equivalen a los métodos *_update().

---

## Relaciones entre Conjuntos


### Subconjunto y superconjunto

```python
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

# issubset: a es subconjunto de b
print(a.issubset(b))      # True
print(a <= b)             # True (equivalente)

# Subconjunto propio (estricto)
print(a < b)              # True (a ⊂ b)

# issuperset: b es superconjunto de a
print(b.issuperset(a))    # True
print(b >= a)             # True (equivalente)

# Superconjunto propio
print(b > a)              # True (b ⊃ a)

# Un conjunto es subconjunto de sí mismo
print(a <= a)             # True
print(a < a)              # False (no es propio)
```

Note: <= y < son subconjunto y subconjunto propio respectivamente. >= y > son superconjunto y superconjunto propio. Útil para verificar jerarquías, permisos, categorías. Un conjunto siempre es subconjunto de sí mismo.


### Conjuntos disjuntos

```python
a = {1, 2, 3}
b = {4, 5, 6}
c = {3, 4, 5}

# isdisjoint: no tienen elementos comunes
print(a.isdisjoint(b))    # True (disjuntos)
print(a.isdisjoint(c))    # False (comparten 3)

# Equivalente a verificar intersección vacía
print(len(a & b) == 0)    # True
print(len(a & c) == 0)    # False

# Caso de uso: grupos excluyentes
admin = {'alice', 'bob'}
usuario = {'charlie', 'dave'}
print(admin.isdisjoint(usuario))  # True - sin overlap
```

Note: Dos conjuntos son disjuntos si no comparten ningún elemento. isdisjoint() es más eficiente que verificar if a & b. Útil para verificar exclusividad mutua, grupos sin overlap.

---

## Métodos Avanzados


### copy() - Copiar conjuntos

```python
original = {1, 2, 3, 4, 5}

# Copia independiente
copia = original.copy()
copia.add(6)

print(original)  # {1, 2, 3, 4, 5} - sin cambios
print(copia)     # {1, 2, 3, 4, 5, 6}

# También con set()
otra_copia = set(original)

# O comprensión
tercera = {x for x in original}

# Asignación NO copia
referencia = original
referencia.add(7)
print(original)  # {1, 2, 3, 4, 5, 7} - cambió!
```

Note: copy() crea copia independiente. Asignación simple crea referencia, no copia. Los cambios a referencia afectan original. Para conjuntos simples, copia es superficial (suficiente). frozenset no necesita copia (inmutable).


### Iterar sobre conjuntos

```python
s = {1, 2, 3, 4, 5}

# Iteración básica (orden impredecible)
for elemento in s:
    print(elemento)

# Iterar ordenado
for elemento in sorted(s):
    print(elemento)  # 1, 2, 3, 4, 5

# Comprehension sobre conjunto
cuadrados = {x**2 for x in s}

# Filtrar durante iteración
pares = {x for x in s if x % 2 == 0}

# No modificar durante iteración
# Mal:
for x in s:
    s.remove(x)  # RuntimeError!
```

Note: Los conjuntos son iterables pero orden es impredecible. Si necesitas orden, usa sorted(). Nunca modifiques conjunto durante iteración (crea copia primero). Comprehensions son la forma pythónica de transformar/filtrar.

---

## Patrones Comunes


### Eliminar duplicados

```python
# De lista
lista = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unicos = list(set(lista))
print(unicos)  # [1, 2, 3, 4]

# De string (caracteres únicos)
texto = 'programacion'
caracteres_unicos = set(texto)
print(caracteres_unicos)  # {'p', 'r', 'o', 'g', 'a', 'm', 'c', 'i', 'n'}

# Preservando orden (dict)
from collections import OrderedDict
lista_ordenada = list(OrderedDict.fromkeys(lista))

# Python 3.7+ (dict mantiene orden)
lista_ordenada = list(dict.fromkeys(lista))
```

Note: set() es la forma más rápida de eliminar duplicados, pero pierde orden. Para preservar orden, usa dict.fromkeys() (Python 3.7+) o OrderedDict. El trade-off: velocidad vs orden.


### Encontrar elementos comunes

```python
# Elementos en todas las listas
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
lista3 = [4, 5, 9, 10]

comunes = set(lista1) & set(lista2) & set(lista3)
print(comunes)  # {4, 5}

# Elementos en al menos una lista
en_alguna = set(lista1) | set(lista2) | set(lista3)
print(en_alguna)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Elementos solo en primera lista
solo_primera = set(lista1) - set(lista2) - set(lista3)
print(solo_primera)  # {1, 2, 3}
```

Note: Convierte listas a conjuntos para operaciones eficientes. Intersección para elementos comunes, unión para cualquier aparición, diferencia para exclusivos. Mucho más eficiente que bucles anidados.


### Verificar permisos/roles

```python
# Permisos requeridos vs permisos del usuario
permisos_requeridos = {'leer', 'escribir', 'ejecutar'}
permisos_usuario = {'leer', 'escribir'}

# ¿Tiene todos los permisos?
tiene_acceso = permisos_requeridos.issubset(permisos_usuario)
print(tiene_acceso)  # False

# ¿Qué permisos faltan?
faltan = permisos_requeridos - permisos_usuario
print(faltan)  # {'ejecutar'}

# ¿Tiene al menos uno de estos permisos?
permisos_admin = {'admin', 'superuser'}
es_admin = bool(permisos_usuario & permisos_admin)
print(es_admin)  # False
```

Note: Los conjuntos son perfectos para modelar permisos, roles, capacidades. issubset para verificar todos, intersección para verificar alguno, diferencia para encontrar faltantes. Más claro que lógica booleana compleja.


### Validar datos únicos

```python
# Verificar IDs únicos
ids_registrados = {1001, 1002, 1003, 1004}
nuevos_ids = [1005, 1006, 1002]  # 1002 duplicado

# Detectar duplicados
if set(nuevos_ids) & ids_registrados:
    print('IDs duplicados encontrados')
    duplicados = set(nuevos_ids) & ids_registrados
    print(f'Duplicados: {duplicados}')

# Validar sin duplicados
if len(nuevos_ids) == len(set(nuevos_ids)):
    print('Todos los IDs son únicos')
else:
    print('Hay IDs duplicados en la entrada')
```

Note: Los conjuntos detectan duplicados automáticamente. Comparar len(lista) con len(set(lista)) detecta duplicados. Intersección con conjunto de referencia detecta conflictos. Útil para validación de datos.

---

## Conjuntos vs Otras Estructuras


### Set vs List

```python
import time

# Crear estructuras grandes
n = 1000000
lista = list(range(n))
conjunto = set(range(n))

# Búsqueda en lista: O(n) - lento
inicio = time.time()
print(999999 in lista)
print(f'Lista: {time.time() - inicio:.4f}s')

# Búsqueda en conjunto: O(1) - rápido
inicio = time.time()
print(999999 in conjunto)
print(f'Conjunto: {time.time() - inicio:.6f}s')

# Diferencia: varios órdenes de magnitud
```

Note: Para búsqueda/pertenencia, conjuntos son infinitamente más rápidos que listas. Para acceso por índice, solo listas. Para orden, listas. Para unicidad y operaciones de conjunto, sets. Elige según tu necesidad.


### Set vs Dict

```python
# Conjunto: solo claves
tags = {'python', 'java', 'javascript'}

# Diccionario: claves con valores
lenguajes = {
    'python': 1991,
    'java': 1995,
    'javascript': 1995
}

# Internamente, set es dict sin valores
# Por eso mismo rendimiento O(1)

# Si solo necesitas verificar existencia, usa set
# Si necesitas asociar datos, usa dict
```

Note: Internamente, set es como dict solo con claves. Por eso comparten características: hashables, O(1), desordenados. Si solo verificas pertenencia, set es más claro y eficiente. Si asocias datos, usa dict.

---

## Mejores Prácticas


### Cuándo usar conjuntos

* ✅ Eliminar duplicados
* ✅ Verificar pertenencia frecuentemente
* ✅ Operaciones matemáticas de conjuntos
* ✅ Elementos únicos garantizados
* ✅ Performance crítica para búsquedas
* ❌ Necesitas mantener orden
* ❌ Necesitas acceso por índice
* ❌ Elementos no son hashables

Note: Los conjuntos no son para todo. Sin orden, sin índices, solo hashables. Pero cuando necesitas sus características, no hay alternativa mejor. Elige la estructura apropiada para tu problema.


### Conversiones eficientes

```python
# Lista → Conjunto (eliminar duplicados)
lista = [1, 2, 2, 3, 3, 3]
unicos = set(lista)  # Rápido

# Conjunto → Lista (cuando necesitas índices)
lista_unicos = list(unicos)

# No conviertas innecesariamente
# Mal: if item in list(conjunto)
# Bien: if item in conjunto

# Mantén como conjunto mientras puedas
# Convierte solo cuando necesites lista
```

Note: Las conversiones tienen costo. Mantén datos en la estructura más apropiada el máximo tiempo posible. Convertir lista→set→lista en cada operación es ineficiente. Convierte una vez, trabaja, convierte de vuelta si necesario.


### Inmutabilidad con frozenset

```python
# Cuando necesites conjunto inmutable
DIAS_LABORABLES = frozenset(['lunes', 'martes', 'miércoles', 
                              'jueves', 'viernes'])

# Puede ser clave de diccionario
horarios = {
    frozenset(['lunes', 'miércoles']): '9:00-11:00',
    frozenset(['martes', 'jueves']): '10:00-12:00'
}

# Conjunto de conjuntos
grupos = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
```

Note: Usa frozenset para datos que no deben cambiar: constantes, configuración, claves de diccionario, elementos de conjuntos. Documenta inmutabilidad. Es el equivalente de tupla para conjuntos.

---

## Ejercicios Propuestos


### Ejercicio 1: Palabras únicas

Encuentra palabras únicas en un texto ignorando mayúsculas.

```python
def palabras_unicas(texto):
    # Tu código aquí
    pass

# Prueba
texto = "Python es genial Python es poderoso"
print(palabras_unicas(texto))
# {'python', 'es', 'genial', 'poderoso'}
```

Note: Divide con split(), convierte a minúsculas con lower(), usa conjunto. Considera puntuación. Resultado debe ser set. Piensa si orden importa.


### Ejercicio 2: Diferencias entre versiones

Encuentra usuarios añadidos y eliminados entre dos versiones.

```python
def cambios_usuarios(version_anterior, version_nueva):
    # Retorna (añadidos, eliminados)
    pass

# Prueba
v1 = {'alice', 'bob', 'charlie'}
v2 = {'bob', 'charlie', 'dave', 'eve'}
# Resultado: ({'dave', 'eve'}, {'alice'})
```

Note: Usa diferencia: añadidos = nueva - anterior, eliminados = anterior - nueva. Retorna tupla de conjuntos. Piensa cómo representarías también los que permanecieron.


### Ejercicio 3: Validar sudoku

Verifica si una fila de sudoku es válida (9 números únicos 1-9).

```python
def fila_valida(fila):
    # Tu código aquí
    pass

# Pruebas
print(fila_valida([1,2,3,4,5,6,7,8,9]))  # True
print(fila_valida([1,2,3,4,5,6,7,8,8]))  # False (duplicado)
print(fila_valida([1,2,3,4,5,6,7,8]))    # False (faltan)
```

Note: Verifica: len == 9, todos entre 1-9, sin duplicados. Usa conjunto para detectar duplicados. Compara longitud lista vs conjunto. Verifica rango válido.


### Ejercicio 4: Encontrar amigos comunes

Dados diccionarios de amigos, encuentra amigos comunes entre usuarios.

```python
def amigos_comunes(amigos, usuario1, usuario2):
    # amigos = {'alice': {'bob', 'charlie'}, ...}
    pass

# Prueba
amigos = {
    'alice': {'bob', 'charlie', 'dave'},
    'eve': {'bob', 'dave', 'frank'}
}
print(amigos_comunes(amigos, 'alice', 'eve'))
# {'bob', 'dave'}
```

Note: Accede a conjuntos de amigos de cada usuario, usa intersección. Maneja caso de usuario inexistente. Considera si dos usuarios pueden ser amigos entre sí.


### Ejercicio 5: Análisis de tags

Analiza tags de posts: encuentra tags populares, únicas, etc.

```python
def analizar_tags(posts):
    # posts = [{'tags': {'python', 'web'}}, ...]
    # Retorna: todos_tags, tags_comunes (en 50%+ posts)
    pass

# Prueba
posts = [
    {'tags': {'python', 'web', 'flask'}},
    {'tags': {'python', 'data', 'pandas'}},
    {'tags': {'python', 'web', 'django'}}
]
# 'python' está en todos, 'web' en 2/3
```

Note: todos_tags: unión de todos. tags_comunes: iterando contando apariciones. Usa conjunto para cada post. Piensa cómo contar frecuencias eficientemente.

---

## Resumen


### Conceptos clave

* Conjuntos son colecciones de elementos únicos
* Desordenados y solo elementos hashables
* Operaciones O(1): add, remove, in
* Operaciones matemáticas: |, &, -, ^
* set mutable, frozenset inmutable
* Perfectos para unicidad y pertenencia

Note: Los conjuntos son especializados pero poderosos. Cuando necesitas sus características (unicidad, operaciones de conjunto, búsqueda rápida), no hay mejor alternativa. Entiende sus limitaciones (sin orden, sin índices).


### Operaciones matemáticas

* **| (union)**: Todos los elementos
* **& (intersection)**: Elementos comunes
* **- (difference)**: En primero, no en segundo
* **^ (symmetric_difference)**: En uno u otro, no ambos
* **<= (subset)**: Todos del primero están en segundo
* **>= (superset)**: Segundo contiene todos del primero

Note: Estas operaciones son la fuerza de los conjuntos. Resuelven problemas complejos de forma concisa. Practica visualizar operaciones con diagramas de Venn. La notación matemática hace el código muy expresivo.


### Próximos pasos

* Practicar con ejercicios de conjuntos
* Aprender funciones (siguiente tema)
* Explorar collections.Counter
* Estudiar algoritmos con conjuntos
* Aplicar a problemas reales

Note: Los conjuntos son fundamentales en algoritmos y estructuras de datos. Muchos problemas se simplifican enormemente con conjuntos. Practica identificando cuándo usarlos. El próximo tema, funciones, usa todos los tipos de datos vistos.

---

## ¿Preguntas?

Note: Los conjuntos son más simples que diccionarios pero igualmente importantes. Asegúrate de que los estudiantes entienden la diferencia entre set y frozenset, las operaciones matemáticas, y cuándo usar conjuntos vs listas. La eficiencia O(1) es su ventaja principal.
