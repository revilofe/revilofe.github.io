# U3.3 - Diccionarios

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son los diccionarios?

* Estructura de datos que asocia claves con valores
* Pares clave:valor únicos
* Las claves deben ser inmutables (hashables)
* Acceso muy rápido por clave (O(1))
* Mutables, ordenados (Python 3.7+), dinámicos

Note: Los diccionarios son la estructura de datos más potente de Python para asociar información. A diferencia de listas que usan índices numéricos, los diccionarios usan claves que pueden ser números, cadenas o cualquier tipo inmutable. Son increíblemente rápidos para búsquedas.


### Representación visual

```python
# Diccionario conceptual
persona = {
    'nombre': 'Ana',
    'edad': 25,
    'ciudad': 'Madrid',
    'email': 'ana@example.com'
}

# Clave → Valor
# 'nombre' → 'Ana'
# 'edad' → 25
# 'ciudad' → 'Madrid'
# 'email' → 'ana@example.com'
```

Note: Piensa en un diccionario como una libreta donde cada entrada tiene una etiqueta (clave) y un contenido (valor). La etiqueta te permite encontrar el contenido instantáneamente sin buscar secuencialmente.


### Características principales

* **Mutable**: Se puede modificar después de creado
* **Ordenado**: Mantiene orden de inserción (Python 3.7+)
* **Dinámico**: Crece/reduce según necesidad
* **Heterogéneo**: Claves y valores de cualquier tipo
* **Eficiente**: Búsqueda O(1) vs O(n) en listas

Note: Los diccionarios antiguos (Python <3.7) no mantenían orden. Desde Python 3.7, mantienen el orden de inserción. La eficiencia O(1) para búsqueda es su ventaja principal sobre listas.


### Claves hashables

```python
# Claves válidas (inmutables/hashables)
d = {
    42: 'número',
    'clave': 'cadena',
    (1, 2): 'tupla',
    True: 'booleano'
}

# Claves NO válidas (mutables)
# d = {[1, 2]: 'lista'}  # TypeError
# d = {{'a': 1}: 'dict'}  # TypeError
# d = {{1, 2}: 'set'}     # TypeError
```

Note: Solo objetos inmutables pueden ser claves. Python necesita calcular un hash de la clave que no cambie. Listas, diccionarios y conjuntos son mutables, por tanto no pueden ser claves. Tuplas sí pueden si contienen solo inmutables.

---

## Crear Diccionarios


### Formas de crear diccionarios

```python
# 1. Literales con llaves
d1 = {'a': 1, 'b': 2, 'c': 3}

# 2. Constructor dict()
d2 = dict(a=1, b=2, c=3)

# 3. Desde lista de tuplas
d3 = dict([('a', 1), ('b', 2), ('c', 3)])

# 4. Desde llaves y valores
d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))

# 5. Diccionario vacío
d5 = {}
d6 = dict()
```

Note: La forma más común es con llaves {}. dict() con argumentos nombrados solo permite claves que sean identificadores válidos. La forma con lista de tuplas es útil para convertir datos. zip() combina dos secuencias en pares.


### Diccionarios por comprensión

```python
# Básica
cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Con condición
pares = {x: x**2 for x in range(10) if x % 2 == 0}
# {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Desde dos listas
nombres = ['Ana', 'Bob', 'Carlos']
edades = [25, 30, 35]
personas = {nombre: edad for nombre, edad in zip(nombres, edades)}
# {'Ana': 25, 'Bob': 30, 'Carlos': 35}
```

Note: Las comprensiones de diccionarios son muy potentes y pythónicas. Sintaxis: {clave: valor for ... in ... if ...}. Son más concisas que bucles con asignaciones. Muy útiles para transformar datos.


### fromkeys() para inicializar

```python
# Crear diccionario con claves y mismo valor
claves = ['a', 'b', 'c']
d = dict.fromkeys(claves, 0)
# {'a': 0, 'b': 0, 'c': 0}

# Sin valor (None por defecto)
d2 = dict.fromkeys(['x', 'y', 'z'])
# {'x': None, 'y': None, 'z': None}

# Útil para contadores
palabras = ['hola', 'mundo', 'hola']
contador = dict.fromkeys(palabras, 0)
```

Note: fromkeys() crea un diccionario con las claves especificadas y el mismo valor para todas. Útil para inicializar contadores, flags, o estructuras de datos. Cuidado: todas las claves apuntan al MISMO objeto si es mutable.

---

## Acceder a Elementos


### Acceso por clave con []

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# Acceso básico
print(persona['nombre'])  # 'Ana'
print(persona['edad'])     # 25

# Error si clave no existe
# print(persona['email'])  # KeyError: 'email'

# Uso común en expresiones
if persona['edad'] >= 18:
    print('Es mayor de edad')
```

Note: El acceso con [] es directo y rápido (O(1)). Pero lanza KeyError si la clave no existe. Esto puede ser útil (falla rápido) o problemático (necesitas manejar excepción). Para evitar errores, usa get().


### Método get() - Acceso seguro

```python
persona = {'nombre': 'Ana', 'edad': 25}

# get() no lanza error
print(persona.get('nombre'))      # 'Ana'
print(persona.get('email'))       # None

# Con valor por defecto
print(persona.get('email', 'N/A'))        # 'N/A'
print(persona.get('telefono', 'No tiene')) # 'No tiene'

# Útil para evitar errores
edad = persona.get('edad', 0)
email = persona.get('email', 'sin_email@example.com')
```

Note: get() es más seguro que []. Devuelve None si la clave no existe, o el valor por defecto que especifiques. No lanza excepción. Usa get() cuando la clave podría no existir. Usa [] cuando sabes que la clave debe existir.


### Verificar existencia de claves

```python
persona = {'nombre': 'Ana', 'edad': 25}

# Con in operator (recomendado)
if 'email' in persona:
    print(persona['email'])
else:
    print('No tiene email')

# Verificar NO existencia
if 'telefono' not in persona:
    persona['telefono'] = 'Desconocido'

# Evitar EAFP anti-pattern
# Mal (innecesario try-except para esto)
try:
    email = persona['email']
except KeyError:
    email = None
```

Note: in verifica si una clave existe en O(1). Es la forma más pythónica y eficiente. No confundas: in busca en claves, no en valores. Para buscar en valores necesitas persona.values().

---

## Modificar Diccionarios


### Añadir y actualizar elementos

```python
persona = {'nombre': 'Ana'}

# Añadir nueva clave
persona['edad'] = 25
persona['ciudad'] = 'Madrid'
print(persona)
# {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# Actualizar existente
persona['edad'] = 26
print(persona)
# {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid'}

# Asignación funciona para ambos casos
persona['email'] = 'ana@example.com'  # Nueva
persona['email'] = 'ana2@example.com'  # Actualiza
```

Note: La asignación d[clave] = valor añade si la clave no existe, o actualiza si existe. No hay distinción en la sintaxis. Esto es cómodo pero puede causar bugs si esperas que falle al duplicar.


### Método setdefault()

```python
persona = {'nombre': 'Ana'}

# setdefault: devuelve valor si existe
edad = persona.setdefault('edad', 25)
print(edad)     # 25
print(persona)  # {'nombre': 'Ana', 'edad': 25}

# Si ya existe, devuelve existente (no cambia)
edad = persona.setdefault('edad', 30)
print(edad)     # 25 (no cambió a 30)

# Útil para inicializar diccionarios anidados
contador = {}
contador.setdefault('a', 0)
contador['a'] += 1
```

Note: setdefault() es atómico: verifica y establece en una operación. Útil cuando solo quieres inicializar si no existe. Si la clave existe, NO cambia el valor. Devuelve el valor (existente o nuevo).


### Método update() - Fusionar diccionarios

```python
persona = {'nombre': 'Ana', 'edad': 25}

# Update con diccionario
persona.update({'ciudad': 'Madrid', 'edad': 26})
print(persona)
# {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid'}

# Update con argumentos nombrados
persona.update(email='ana@example.com', telefono='123456')

# Update con lista de tuplas
persona.update([('pais', 'España'), ('codigo_postal', '28001')])

# Múltiples al mismo tiempo
persona.update({'altura': 165}, peso=60)
```

Note: update() fusiona otro diccionario en el actual. Añade claves nuevas y actualiza existentes. Acepta diccionario, keywords, o lista de tuplas. Es eficiente para actualizar múltiples claves. Modifica el diccionario original.


### Operador | para fusionar (Python 3.9+)

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# | crea nuevo diccionario
d3 = d1 | d2
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d1)  # {'a': 1, 'b': 2} (sin cambios)

# |= modifica el original
d1 |= d2
print(d1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Claves duplicadas: gana el de la derecha
d4 = {'a': 1, 'b': 2} | {'b': 3, 'c': 4}
print(d4)  # {'a': 1, 'b': 3, 'c': 4}
```

Note: | y |= son operadores modernos (Python 3.9+) para fusionar diccionarios. | crea nuevo, |= modifica. Son más legibles que update(). Cuando hay claves duplicadas, el diccionario de la derecha gana. Muy pythónico.

---

## Eliminar Elementos


### Métodos para eliminar

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# pop(clave): elimina y retorna valor
edad = persona.pop('edad')
print(edad)     # 25
print(persona)  # {'nombre': 'Ana', 'ciudad': 'Madrid'}

# pop con valor por defecto
email = persona.pop('email', 'No tiene')
print(email)  # 'No tiene'

# pop sin defecto lanza KeyError si no existe
# persona.pop('telefono')  # KeyError
```

Note: pop() elimina y devuelve el valor. Útil cuando necesitas el valor antes de eliminarlo. El segundo parámetro es el valor por defecto si la clave no existe. Sin valor por defecto, lanza KeyError.


### popitem() - Eliminar último

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# popitem(): elimina y retorna último par (clave, valor)
ultimo = persona.popitem()
print(ultimo)   # ('ciudad', 'Madrid')
print(persona)  # {'nombre': 'Ana', 'edad': 25}

# Otro popitem
otro = persona.popitem()
print(otro)     # ('edad', 25)

# En diccionario vacío lanza KeyError
# {}.popitem()  # KeyError: 'dictionary is empty'
```

Note: popitem() elimina el último elemento insertado (Python 3.7+). En versiones antiguas era aleatorio. Útil para procesar diccionario destruyéndolo. Devuelve tupla (clave, valor). Lanza KeyError si está vacío.


### del statement

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# del elimina por clave
del persona['edad']
print(persona)  # {'nombre': 'Ana', 'ciudad': 'Madrid'}

# del lanza KeyError si no existe
# del persona['email']  # KeyError

# del puede eliminar el diccionario completo
del persona  # Ahora persona no existe
# print(persona)  # NameError

# del vs pop: del no retorna valor
```

Note: del es un statement de Python, no un método. Elimina la entrada del diccionario. No retorna nada. Lanza KeyError si la clave no existe. También puede eliminar la variable completa del namespace.


### clear() - Vaciar diccionario

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# clear() elimina todos los elementos
persona.clear()
print(persona)  # {}

# Es diferente de asignar {}
d = {'a': 1}
d2 = d  # d2 referencia el mismo diccionario
d.clear()
print(d2)  # {} (también se vació)

d3 = {'b': 2}
d4 = d3
d3 = {}  # d3 ahora es nuevo diccionario
print(d4)  # {'b': 2} (no cambió)
```

Note: clear() vacía el diccionario pero mantiene la identidad del objeto. Si hay otras referencias al diccionario, también se ven afectadas. Asignar {} crea un nuevo diccionario. La diferencia es importante con referencias compartidas.

---

## Métodos de Vista


### keys(), values(), items()

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# keys(): vista de claves
claves = persona.keys()
print(claves)  # dict_keys(['nombre', 'edad', 'ciudad'])

# values(): vista de valores
valores = persona.values()
print(valores)  # dict_values(['Ana', 25, 'Madrid'])

# items(): vista de pares (clave, valor)
items = persona.items()
print(items)  # dict_items([('nombre', 'Ana'), ('edad', 25), ('ciudad', 'Madrid')])
```

Note: keys(), values(), items() devuelven vistas dinámicas, no copias. Si modificas el diccionario, las vistas se actualizan. Son iterables y eficientes en memoria. No son listas pero puedes convertirlas con list().


### Iterar sobre diccionarios

```python
persona = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# Iterar sobre claves (por defecto)
for clave in persona:
    print(clave)

# Explícitamente sobre claves
for clave in persona.keys():
    print(clave, persona[clave])

# Iterar sobre valores
for valor in persona.values():
    print(valor)

# Iterar sobre pares (más común)
for clave, valor in persona.items():
    print(f'{clave}: {valor}')
```

Note: Iterar directamente sobre un diccionario itera sobre sus claves. items() es la forma más común: da clave y valor simultáneamente con desempaquetado. values() cuando solo necesitas valores. keys() es redundante pero explícito.


### Vistas son dinámicas

```python
persona = {'nombre': 'Ana', 'edad': 25}

# Crear vista
claves = persona.keys()
print(list(claves))  # ['nombre', 'edad']

# Modificar diccionario
persona['ciudad'] = 'Madrid'

# Vista se actualiza automáticamente
print(list(claves))  # ['nombre', 'edad', 'ciudad']

# Las vistas NO son copias
# Son ventanas al diccionario original
```

Note: Las vistas son "ventanas" al diccionario, no copias independientes. Si el diccionario cambia, las vistas reflejan los cambios. Esto es eficiente en memoria pero puede ser sorprendente. Si necesitas snapshot independiente, convierte a lista.

---

## Diccionarios Anidados


### Crear diccionarios anidados

```python
# Diccionario de diccionarios
estudiantes = {
    'Ana': {'edad': 20, 'carrera': 'Informática'},
    'Bob': {'edad': 22, 'carrera': 'Matemáticas'},
    'Carlos': {'edad': 21, 'carrera': 'Física'}
}

# Acceso anidado
print(estudiantes['Ana']['edad'])      # 20
print(estudiantes['Bob']['carrera'])   # 'Matemáticas'

# Modificar anidado
estudiantes['Ana']['edad'] = 21
estudiantes['Carlos']['nota'] = 9.5
```

Note: Los diccionarios pueden contener otros diccionarios, creando estructuras jerárquicas. Útil para representar objetos complejos, configuración, datos JSON. El acceso usa múltiples corchetes. Cada nivel es un diccionario independiente.


### Casos de uso anidados

```python
# Configuración de aplicación
config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'credentials': {
            'user': 'admin',
            'password': 'secret'
        }
    },
    'api': {
        'endpoint': 'https://api.example.com',
        'timeout': 30
    }
}

# Acceso profundo
db_user = config['database']['credentials']['user']
api_timeout = config['api']['timeout']
```

Note: Los diccionarios anidados son perfectos para configuración jerárquica, datos JSON, representar objetos con atributos complejos. Estructuras como árboles, grafos, pueden representarse con diccionarios anidados.


### get() con diccionarios anidados

```python
config = {
    'database': {
        'host': 'localhost'
    }
}

# Acceso seguro anidado es verbose
host = config.get('database', {}).get('host', 'default')
port = config.get('database', {}).get('port', 5432)
user = config.get('database', {}).get('credentials', {}).get('user', 'root')

# Alterativa: función helper
def get_nested(d, *keys, default=None):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d

host = get_nested(config, 'database', 'host', default='localhost')
```

Note: El acceso seguro a diccionarios anidados es verboso. .get() anidados se vuelven ilegibles. Puedes crear funciones helper o usar librerías como pydash. Python 3.11+ añade mejoras para este caso.


### Inicializar diccionarios anidados

```python
# Mal: referencia compartida
d = {'a': []} * 3  # NO hagas esto
d = dict.fromkeys(['x', 'y', 'z'], {})  # Tampoco

# Bien: comprensión de diccionario
matriz = {i: {} for i in range(3)}

# Bien: defaultdict
from collections import defaultdict
anidado = defaultdict(dict)
anidado['user1']['edad'] = 25  # Crea automáticamente
anidado['user2']['ciudad'] = 'Madrid'

# Alternativa manual
def crear_usuario():
    return {'edad': 0, 'ciudad': 'Desconocida'}

usuarios = {f'user{i}': crear_usuario() for i in range(3)}
```

Note: Inicializar diccionarios anidados requiere cuidado. fromkeys() con mutable crea referencias compartidas (bug común). Usa comprensiones o defaultdict. defaultdict es especialmente útil para diccionarios anidados.

---

## Operaciones Comunes


### Copiar diccionarios

```python
original = {'a': 1, 'b': 2}

# Copia superficial con copy()
copia1 = original.copy()
copia1['a'] = 100
print(original)  # {'a': 1, 'b': 2} - no cambió

# Copia superficial con dict()
copia2 = dict(original)

# Copia superficial con comprensión
copia3 = {k: v for k, v in original.items()}

# Copia profunda para anidados
import copy
anidado = {'a': {'b': 1}}
copia_prof = copy.deepcopy(anidado)
```

Note: copy() crea copia superficial: copia el diccionario pero no objetos mutables dentro. Para diccionarios anidados, necesitas copy.deepcopy(). dict() y comprensión también son copias superficiales. Las copias son independientes del original.


### Fusionar múltiples diccionarios

```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Forma moderna (Python 3.9+)
fusionado = d1 | d2 | d3

# Forma antigua pero compatible
fusionado = {}
for d in [d1, d2, d3]:
    fusionado.update(d)

# Con comprensión
fusionado = {k: v for d in [d1, d2, d3] for k, v in d.items()}

# Con desempaquetado (Python 3.5+)
fusionado = {**d1, **d2, **d3}
```

Note: Hay muchas formas de fusionar diccionarios. El operador | es el más moderno y legible. {**d1, **d2} es compacto y común. update() en bucle es la forma tradicional. Todas manejan claves duplicadas: la última gana.


### Invertir diccionario

```python
original = {'a': 1, 'b': 2, 'c': 3}

# Invertir (valores → claves)
invertido = {v: k for k, v in original.items()}
print(invertido)  # {1: 'a', 2: 'b', 3: 'c'}

# Cuidado con valores duplicados
original2 = {'a': 1, 'b': 2, 'c': 1}
invertido2 = {v: k for k, v in original2.items()}
print(invertido2)  # {1: 'c', 2: 'b'} - 'a' se perdió

# Para valores duplicados: lista de claves
from collections import defaultdict
invertido3 = defaultdict(list)
for k, v in original2.items():
    invertido3[v].append(k)
```

Note: Invertir diccionario intercambia claves y valores. Solo funciona si valores son hashables. Si hay valores duplicados, se pierden claves (última gana). Para preservar todas, usa defaultdict(list) y acumula claves.


### Filtrar diccionario

```python
datos = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Filtrar por valor
pares = {k: v for k, v in datos.items() if v % 2 == 0}
# {'b': 2, 'd': 4}

# Filtrar por clave
starts_with_c = {k: v for k, v in datos.items() if k.startswith('c')}
# {'c': 3}

# Filtrar por ambos
filtrado = {k: v for k, v in datos.items() 
            if k in ['a', 'c', 'e'] and v > 2}
# {'c': 3, 'e': 5}

# Con función filter
mayores_3 = dict(filter(lambda item: item[1] > 3, datos.items()))
```

Note: Las comprensiones de diccionarios son perfectas para filtrar. Puedes filtrar por clave, valor, o ambos. filter() también funciona pero comprensiones son más pythónicas y legibles. El resultado es un nuevo diccionario.

---

## defaultdict y Counter


### defaultdict - Valores por defecto

```python
from collections import defaultdict

# Contador de palabras
contador = defaultdict(int)  # int() devuelve 0
palabras = ['manzana', 'banana', 'manzana', 'cereza', 'banana']
for palabra in palabras:
    contador[palabra] += 1  # No necesitas verificar si existe
print(contador)  # {'manzana': 2, 'banana': 2, 'cereza': 1}

# Agrupar por inicial
grupos = defaultdict(list)  # list() devuelve []
for palabra in palabras:
    grupos[palabra[0]].append(palabra)
print(dict(grupos))  # {'m': ['manzana', 'manzana'], 'b': ['banana', 'banana'], 'c': ['cereza']}
```

Note: defaultdict es un diccionario que crea valores por defecto automáticamente cuando accedes a clave inexistente. Evita verificar existencia con if o get(). El argumento es una función (int, list, set, etc.) que se llama sin argumentos.


### Counter - Contar elementos

```python
from collections import Counter

# Contar elementos
palabras = ['manzana', 'banana', 'manzana', 'cereza', 'banana', 'manzana']
contador = Counter(palabras)
print(contador)  # Counter({'manzana': 3, 'banana': 2, 'cereza': 1})

# Métodos útiles
print(contador.most_common(2))  # [('manzana', 3), ('banana', 2)]
print(contador['manzana'])      # 3
print(contador['uva'])          # 0 (no KeyError)

# Operaciones de conjunto
c1 = Counter(['a', 'b', 'c', 'a'])
c2 = Counter(['a', 'c', 'd'])
print(c1 + c2)  # Counter({'a': 3, 'c': 2, 'b': 1, 'd': 1})
print(c1 - c2)  # Counter({'a': 1, 'b': 1})
```

Note: Counter es una subclase de dict especializada en contar. most_common() es muy útil. Acceder a clave inexistente devuelve 0, no KeyError. Soporta operaciones matemáticas (+, -, &, |). Perfecto para análisis de frecuencias.

---

## Patrones y Mejores Prácticas


### Usar get() con operaciones

```python
datos = {'usuarios': 100, 'paginas': 50}

# Mal: verificación verbose
if 'visitas' in datos:
    visitas = datos['visitas']
else:
    visitas = 0
visitas += 1

# Bien: get() conciso
visitas = datos.get('visitas', 0) + 1
datos['visitas'] = visitas

# Aún mejor con setdefault
datos.setdefault('visitas', 0)
datos['visitas'] += 1
```

Note: get() con valor por defecto es más conciso que if/else. setdefault() es perfecto para inicializar antes de modificar. Estos patrones hacen el código más legible y pythónico.


### Evitar KeyError con EAFP

```python
config = {'host': 'localhost', 'port': 8080}

# LBYL (Look Before You Leap) - menos pythónico
if 'timeout' in config:
    timeout = config['timeout']
else:
    timeout = 30

# EAFP (Easier to Ask Forgiveness than Permission) - pythónico
try:
    timeout = config['timeout']
except KeyError:
    timeout = 30

# Pero en este caso, get() es mejor
timeout = config.get('timeout', 30)
```

Note: EAFP es pythónico: intenta y maneja excepción. LBYL verifica antes. Pero para diccionarios, get() suele ser mejor que ambos. Usa try/except cuando hay lógica compleja, get() para casos simples.


### Diccionarios como switch/case

```python
# Python no tiene switch/case, usa diccionarios
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

operaciones = {
    '+': sumar,
    '-': restar,
    '*': multiplicar
}

# Usar
operacion = '+'
resultado = operaciones[operacion](5, 3)  # 8

# Con get() para default
resultado = operaciones.get(operacion, sumar)(5, 3)
```

Note: Los diccionarios son excelentes como dispatch tables (reemplazo de switch/case). Asocia valores (strings, enums) con funciones. Más escalable y mantenible que if/elif. Las funciones se almacenan como valores y se llaman con ().


### No modificar durante iteración

```python
d = {'a': 1, 'b': 2, 'c': 3}

# Mal: RuntimeError
for k in d:
    if d[k] == 2:
        del d[k]  # Error!

# Bien: iterar sobre copia
for k in list(d.keys()):
    if d[k] == 2:
        del d[k]

# Mejor: comprensión
d = {k: v for k, v in d.items() if v != 2}

# Alternativa: collect y delete
a_eliminar = [k for k, v in d.items() if v == 2]
for k in a_eliminar:
    del d[k]
```

Note: Nunca modifiques un diccionario mientras iteras sobre él, causará RuntimeError. Soluciones: iterar sobre copia (list(d.keys())), usar comprensión para crear nuevo diccionario, o recolectar claves a eliminar primero. La comprensión suele ser más clara.

---

## Ejercicios Propuestos


### Ejercicio 1: Contar frecuencia

Escribe una función que cuente la frecuencia de cada palabra en un texto.

```python
def contar_palabras(texto):
    # Tu código aquí
    pass

# Pruebas
texto = "python es genial python es facil"
print(contar_palabras(texto))
# {'python': 2, 'es': 2, 'genial': 1, 'facil': 1}
```

Note: Divide el texto con split(), itera contando cada palabra. Usa diccionario normal con get() o setdefault(), o usa defaultdict(int) o Counter. Considera mayúsculas/minúsculas y puntuación.


### Ejercicio 2: Agrupar por longitud

Crea una función que agrupe palabras por su longitud.

```python
def agrupar_por_longitud(palabras):
    # Tu código aquí
    pass

# Pruebas
palabras = ['hola', 'mundo', 'python', 'es', 'genial']
print(agrupar_por_longitud(palabras))
# {4: ['hola'], 5: ['mundo'], 6: ['python', 'genial'], 2: ['es']}
```

Note: Usa defaultdict(list) para facilitar. Para cada palabra, añádela a la lista correspondiente a su longitud. Alternativamente, usa comprensión con set de longitudes y filtrado.


### Ejercicio 3: Fusionar inventarios

Fusiona dos diccionarios de inventario sumando cantidades.

```python
def fusionar_inventarios(inv1, inv2):
    # Tu código aquí
    pass

# Pruebas
inv1 = {'manzanas': 5, 'naranjas': 3}
inv2 = {'manzanas': 2, 'peras': 4}
print(fusionar_inventarios(inv1, inv2))
# {'manzanas': 7, 'naranjas': 3, 'peras': 4}
```

Note: Itera sobre ambos inventarios, sumando valores para claves comunes. Usa Counter para facilitar (suma automática), o manualmente con get(). Considera qué hacer si los valores no son números.


### Ejercicio 4: Invertir diccionario anidado

Invierte un diccionario de productos por categoría a categorías por producto.

```python
def invertir_categorias(catalogo):
    # Tu código aquí
    pass

# Prueba
catalogo = {
    'Frutas': ['manzana', 'banana'],
    'Verduras': ['lechuga', 'tomate'],
    'Lacteos': ['leche']
}
# Resultado esperado:
# {'manzana': 'Frutas', 'banana': 'Frutas', ...}
```

Note: Itera sobre cada categoría y sus productos, creando entradas invertidas. Cuidado con productos en múltiples categorías si es posible. Decide si valor debe ser string o lista.


### Ejercicio 5: Diccionario de configuración

Crea función que lea configuración con valores por defecto anidados.

```python
def aplicar_configuracion(config, defaults):
    # Fusionar config con defaults (defaults no sobreescriben)
    pass

# Prueba
defaults = {'db': {'host': 'localhost', 'port': 5432},
            'cache': {'ttl': 300}}
config = {'db': {'port': 3306}}
# Resultado: {'db': {'host': 'localhost', 'port': 3306},
#             'cache': {'ttl': 300}}
```

Note: Fusionar diccionarios anidados recursivamente. config sobreescribe defaults. Necesitas recursión para manejar anidamiento. Alterativa: usa librerías como `merge` o implementa manualmente.

---

## Resumen


### Conceptos clave

* Diccionarios asocian claves hashables con valores
* Acceso O(1) - increíblemente eficiente
* Métodos: get, setdefault, update, pop, items, keys, values
* Comprensiones de diccionarios para transformaciones
* defaultdict y Counter para casos especiales
* Fusión con | y ** unpacking

Note: Los diccionarios son la estructura más potente de Python después de funciones y clases. Su eficiencia O(1) los hace insuperables para búsquedas. Dominarlos es esencial para Python avanzado.


### Cuándo usar diccionarios

* ✅ Necesitas búsquedas rápidas por clave
* ✅ Asociar datos relacionados (nombre→edad)
* ✅ Agrupar, contar, indexar datos
* ✅ Configuración jerárquica
* ✅ Caché y memoización
* ❌ Orden específico crítico (considera OrderedDict)
* ❌ Datos tabulares (considera pandas)

Note: Los diccionarios son versátiles pero no para todo. Para datos tabulares, pandas es mejor. Para orden estricto (no solo preservación), OrderedDict. Para búsqueda en secuencia, sigue siendo O(n) con valores().


### Próximos pasos

* Practicar con ejercicios variados
* Aprender conjuntos (siguiente tema)
* Estudiar collections (OrderedDict, ChainMap)
* Explorar JSON y diccionarios
* Implementar algoritmos con diccionarios

Note: Los diccionarios son fundamentales en Python. Se usan constantemente: APIs JSON, bases de datos, configuración, algoritmos. Practica mucho. El siguiente tema, conjuntos, usa conceptos similares de hashing.

---

## ¿Preguntas?

Note: Los diccionarios son extensos y fundamentales. Asegúrate de que los estudiantes entienden la diferencia entre claves y valores, cuándo usar get() vs [], y cómo iterar eficientemente. Los diccionarios son la base de muchas estructuras avanzadas en Python.
