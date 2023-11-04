<!-- Con # se ponen los títulos -->

## U3.4

## Conjuntos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Indice

---

### Conjuntos en Python

* El tipo set en Python representa conjuntos.
* Un conjunto es una colección desordenada de elementos únicos.

Note: Los conjuntos en Python son colecciones desordenadas de elementos únicos.

---

### Qué es el tipo set en Python

* Colección sin orden y elementos únicos.
* Usos principales: verificar pertenencia y eliminar duplicados.

Note: Los conjuntos son útiles para verificar si un elemento pertenece a una colección y para eliminar duplicados de secuencias.

---

### Creación de conjuntos

* Usar llaves {} o el constructor set().
* Elimina elementos repetidos.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">c = {1, 3, 2, 9, 3, 1}  # {1, 2, 3, 9}
a = set('Hola Pythonista')  # {'a', 'H', 'h', 'y', 'n', 's', 'P', 't', ' ', 'i', 'l', 'o'}
unicos = set([3, 5, 6, 1, 5])  # {1, 3, 5, 6}
</code></div></div></pre>

Note: Usa {} para crear un conjunto y set() para un conjunto vacío.

---

### Conjuntos vs Frozensets

* set: Mutable, seResumen: Diccionarios en Python
Los diccionarios en Python son estructuras de datos que asocian claves con valores.
Las claves deben ser inmutables y hashables.
Las principales operaciones incluyen almacenar y recuperar valores por clave.
Note: Los diccionarios son esenciales y eficientes en Python.

Resumen: Creación y Manipulación
Crear un diccionario: {} o dict().
Acceder a elementos: d[clave] o d.get(clave, valor_por_defecto).
Recorrer un diccionario con for y keys(), values(), items().
Añadir, modificar y eliminar elementos en un diccionario.
Note: Diccionarios son mutables y versátiles.

Resumen: Conclusiones
Los diccionarios son ideales para mapear claves a valores en Python.
Permite un acceso rápido a los elementos.
Se pueden crear de varias formas y manipular eficientemente.
Utiliza objetos vista para claves, valores y pares clave-valor.
Note: Los diccionarios son una herramienta poderosa en Python. ¡Explóralos y úsalos en tus proyectos! pueden modificar.
* frozenset: Inmutable, no se puede modificar.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">f = frozenset([3, 5, 6, 1, 5])  # frozenset({1, 3, 5, 6})
</code></div></div></pre>

Note: Los conjuntos se pueden modificar, los frozensets no.

---

### Acceso a elementos

* No se puede acceder por índice.
* Son objetos que no tienen orden.
* Utilizar un bucle for.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">mi_conjunto = {1, 3, 2, 9, 3, 1}
for e in mi_conjunto:
    print(e)
# Output: 1, 2, 3, 9
</code></div></div></pre>

Note: No hay índices en conjuntos, se accede usando bucles.

---

### Añadir elementos a un conjunto

* Método `add()` para un elemento.
* Método `update()` para varios elementos.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">mi_conjunto = {1, 3, 2, 9, 3, 1}
mi_conjunto.add(7)  # {1, 2, 3, 7, 9}
mi_conjunto.update([5, 3, 4, 6])  # {1, 2, 3, 4, 5, 6, 7, 9}
</code></div></div></pre>

Note: Usa `add()` para un elemento y `update()` para varios.

---

### Eliminar elementos de un conjunto

* Métodos `discard()`, `remove()`, `pop()` y `clear()`.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">mi_conjunto = {1, 3, 2, 9, 3, 1, 6, 4, 5}
mi_conjunto.remove(1)  # {2, 3, 4, 5, 6, 9}
mi_conjunto.discard(4)  # {2, 3, 5, 6, 9}
mi_conjunto.remove(7)  # KeyError: 7
mi_conjunto.discard(7)  # No hace nada
mi_conjunto.pop()  # 2
mi_conjunto.clear()  # set()
</code></div></div></pre>

Note: Métodos para eliminar elementos de un conjunto.

---

### Número de elementos en un conjunto

* Usa len() para obtener la cantidad de elementos.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">mi_conjunto = set([1, 2, 5, 3, 1, 5])
len(mi_conjunto)  # 4
</code></div></div></pre>

Note: Usa `len()` para obtener el número de elementos en un conjunto.

---

### Verificar pertenencia en un conjunto

* Utiliza el operador `in`.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">mi_conjunto = set([1, 2, 5, 3, 1, 5])
print(1 in mi_conjunto)  # True
print(6 in mi_conjunto)  # False
print(2 not in mi_conjunto)  # False
</code></div></div></pre>

Note: Utiliza `in` para verificar si un elemento está en un conjunto.

---

## Operaciones sobre conjuntos


### Unión de conjuntos

* `A ∪ B`: contiene todos los elementos de A y de B.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
a | b  # {1, 2, 3, 4, 6, 8}
</code></div></div></pre>

Note: Usa el operador `|` para la unión de conjuntos.


### Intersección de conjuntos

* `A ∩ B`: contiene elementos comunes de A y B.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
a & b  # {2, 4}
</code></div></div></pre>

Note: Usa el operador `&` para la intersección de conjuntos.


### Diferencia de conjuntos

* `A - B`: contiene elementos de A que no están en B.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
a - b  # {1, 3}
</code></div></div></pre>

Note: Usa el operador `-` para la diferencia de conjuntos.


### Diferencia simétrica de conjuntos

* Contiene elementos que no son comunes en A y B.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
a ^ b  # {1, 3, 6, 8}
</code></div></div></pre>

Note: Usa el operador `^` para la diferencia simétrica de conjuntos.


### Inclusión de conjuntos

* `A ⊆ B`: A es subconjunto de B.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2}
b = {1, 2, 3, 4}
a <= b  # True
</code></div></div></pre>

Note: Usa `<=` para comprobar si A es subconjunto de B.


### Conjuntos disjuntos

* A y B no tienen elementos en común.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2}
b = {3, 4}
a.isdisjoint(b)  # True
</code></div></div></pre>

Note: Usa `isdisjoint()` para comprobar si dos conjuntos son disjuntos.


### Igualdad de conjuntos

* Dos conjuntos son iguales si todos los elementos de uno están en el otro.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2}
b = {1, 2}
a == b  # True
</code></div></div></pre>

Note: Dos conjuntos son iguales si tienen los mismos elementos.

---

## Métodos de la clase set


### Métodos de la clase set en Python

* `add(e)`: Añade un elemento al conjunto.
* `clear()`: Elimina todos los elementos del conjunto.
* `copy()`: Devuelve una copia superficial del conjunto.
* `difference(iterable)`: Devuelve la diferencia con otro conjunto o iterable.
* `discard(e)`: Elimina el elemento si existe.

Note: Estos son algunos de los métodos disponibles para conjuntos en Python.


### Más métodos de la clase set

* `intersection(iterable)`: Devuelve la intersección con otro conjunto o iterable.
* `isdisjoint(iterable)`: Devuelve True si dos conjuntos son disjuntos.
* `issubset(iterable)`: Devuelve True si el conjunto es subconjunto.
* `issuperset(iterable)`: Devuelve True si el conjunto es superconjunto.

Note: Hay más métodos disponibles para conjuntos en Python.


### Métodos de actualización de conjuntos

* `difference_update(iterable)`: Actualiza el conjunto con la diferencia.
* `intersection_update(iterable)`: Actualiza el conjunto con la intersección.
* `symmetric_difference_update(iterable)`: Actualiza con la diferencia simétrica.
* `update(iterable)`: Actualiza el conjunto con la unión.

Note: Estos métodos actualizan el conjunto con el resultado de la operación.

---

## Resumen: Conjuntos en Python


### Conjuntos en Python
* Un conjunto es una colección desordenada de elementos únicos.
* Útil para verificar pertenencia y eliminar duplicados.

Note: Los conjuntos son una herramienta poderosa en Python para manipular colecciones de datos.


### Crear un conjunto

* `{elemento1, elemento2, ...}` o `set(iterable)`.
* Elementos repetidos son eliminados.

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">c = {1, 3, 2, 9, 3, 1}  # {1, 2, 3, 9}
a = set('Hola Pythonista')  # {'a', 'H', 'h', 'y', 'n', 's', 'P', 't', ' ', 'i', 'l', 'o'}
</code></div></div></pre>

Note: Puedes crear conjuntos usando llaves o el constructor `set()`.


### Operaciones con conjuntos

* Operadores como `|`, `&`, `-`, `^` para operaciones de conjuntos.
* Unión, intersección, diferencia, diferencia simétrica.
* Inclusión, conjuntos disjuntos, igualdad.

Note: Los conjuntos permiten realizar operaciones al estilo del álgebra de conjuntos.


### Operaciones con conjuntos

<pre><div class="bg-black rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 gizmo:dark:bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>python</span><button class="flex ml-auto gizmo:ml-0 gap-2 items-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-sm" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-python">a = {1, 2, 3, 4}
b = {2, 4, 6, 8}
a | b  # Unión
a & b  # Intersección
a - b  # Diferencia
a ^ b  # Diferencia simétrica
</code></div></div></pre>


### Métodos importantes

* `add()`, `remove()`, `clear()`.
* `update()`, `discard()`, `pop()`.
* `len()`, `in`.

Note: Tanto operadores como métodos son útiles para manipular conjuntos en Python.

---

## ¡Gracias por su atención!

Note: ¿Alguna pregunta sobre conjuntos en Python?
