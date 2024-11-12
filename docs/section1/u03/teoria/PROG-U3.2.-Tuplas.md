---
title: "UD 3 - 3.2 Tuplas"
description: Tuplas
summary: Como trabajar con tuplas en Python.
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: 
permalink: /prog/unidad3/3.1
categories:
    - PROG
tags:
    - Software
    - tuplas
---
## Tuplas
Las tublas son unos iterables que se utilizan para almacenar objetos de cualquier tipo. Se pueden considerar como listas inmutables. Se definen entre paréntesis y los elementos se separan por comas.

### Diferencia entre tuplas y listas.

Una lista no es lo mismo que una tupla. Ambas son un conjunto ordenado de valores, en donde este último puede ser cualquier objeto: un número, una cadena, una función, una clase, una instancia, etc. La diferencia es que las listas presentan una serie de funciones adicionales que permiten un amplio manejo de los valores que contienen. Basándonos en esta definición, puede decirse que las listas son dinámicas, mientras que las tuplas son estáticas.

La principal diferencia entre las listas y las tuplas de Python, y el motivo por el que muchos usuarios solamente utilizar listas, es que **las listas son mutables** mientras que **las tuplas son inmutables**. ¿Pero qué significa ser mutable o no? Básicamente un objeto mutable se puede modificar una vez creado mientras que uno que no lo es no. Así el contenido de las listas se puede modificar durante la ejecución del programa mientras para las tuplas no es posible alterar su contenido. Las tuplas se podrán usar como las listas teniendo en cuenta su inmutabilidad.

El hecho de ser mutable tiene además otras consecuencias. Para ser mutables las listas se almacena en dos bloques de memoria, mientras que las tuplas solo necesitan uno. Lo que provoca que las tuplas ocupen menos memoria que las listas. Además, por el hecho de no ser mutables, es más rápido manejar tuplas que listas. Debido a esto, hay que tener en cuenta lo anterior para elegir en nuestros algoritmos el tipo que mejor se adapte. En el caso de que no sea necesario modificar el contenido de los datos la mejor opción es la tupla, ya que es ocupa menos memoria y es más rápida. En el resto de los casos la mejor opción será utilizar listas.

### Qué es una tupla

La clase tuple en Python es un tipo **contenedor**, compuesto, que **en un principio se pensó para almacenar grupos de elementos heterogéneos**, aunque también puede contener elementos homogéneos.

Junto a las clases *list* y  *range* , **es uno de los tipos de secuencia en Python**, con la particularidad de que son  *inmutables* . Esto último quiere decir que su contenido **NO** se puede modificar después de haber sido creada.

En general, para crear una tupla en Python simplemente hay que definir una secuencia de elementos separados por comas.

Por ejemplo, para crear una tupla con los números del 1 al 5 se haría del siguiente modo:

```Python
>>> numeros = 1, 2, 3, 4, 5
```

La clase `tuple` también puede almacenar elementos de distinto tipo:

```Python
>>> elementos = 3, 'a', 8, 7.2, 'hola'
```

Incluso pueden contener otros elementos compuestos y objetos, como listas, otras tuplas, etc.:

```Python
>>> tup = 1, ['a', 'e', 'i', 'o', 'u'], 8.9, 'hola'
```

A continuación se ven las diferentes formas que existen de crear una tupla en Python:

* Para crear una tupla vacía, usa paréntesis `()` o el constructor de la clase `tuple()` sin parámetros.
* Para crear una tupla con un único elemento: `elem,` o `(elem, )`. Observa que siempre se añade una coma.
* Para crear una tupla de varios elementos, sepáralos con comas: `a, b, c` o `(a, b, c)`.
* Las tuplas también se pueden crear usando el constructor de la clase, `tuple(iterable)`. En este caso, el constructor crea una tupla cuyos elementos son los mismos y están en el mismo orden que los ítems del iterable. El objeto *iterable* puede ser una secuencia, un contenedor que soporte la iteración o un objeto iterador.

> ️**IMPORTANTE:** El hecho que determina que una secuencia de elementos sea una tupla es la coma `,` no los paréntesis. Los paréntesis son opcionales y solo se necesitan para crear una tupla vacía o para evitar ambigüedades.

```Python
# Aquí, a, b y c no son una tupla, sino tres argumentos con
# los que se llama a la función "una_funcion"
>>> una_funcion(a, b, c)
# Aquí, a, b y c son tres elementos de una tupla. Esta tupla,
# es el único argumento con el que se invoca a la
# función "una_funcion"
>>> una_funcion((a, b, c))
```

> La forma de crear una tupla sin paréntesis es conocida como *tuple packing* (algo así como empaquetado de tuplas).

### Cómo acceder a los elementos de una tupla en Python

Para acceder a un elemento de una tupla se utilizan los índices. **Un índice es un número entero que indica la posición de un elemento en una tupla**. El primer elemento de una tupla siempre comienza en el índice 0.

Por ejemplo, en una tupla con 3 elementos, los índices de cada uno de los ítems serían 0, 1 y 2.

```Python
>>> tupla = ('a', 'b', 'd')
>>> tupla[0]  # Primer elemento de la tupla. Índice 0
'a'
>>> tupla[1]  # Segundo elemento de la tupla. Índice 1
'b'
```

Si se intenta acceder a un índice que está fuera del rango de la tupla, el intérprete lanzará la excepción `IndexError`. De igual modo, si se utiliza un índice que no es un número entero, se lanzará la excepción `TypeError`:

```Python
>>> tupla = 1, 2, 3  # Los índices válidos son 0, 1 y 2
>>> tupla[8]
Traceback (most recent call last):
File "<input>", line 1, in <module>
IndexError: tuple index out of range
>>> tupla[1.0]
Traceback (most recent call last):
File "<input>", line 1, in <module>
TypeError: tuple indices must be integers or slices, not float
>
```

#### Acceso a los elementos usando un índice negativo
Al igual que ocurre con las listas (y todos los tipos secuenciales), está permitido usar índices negativos para acceder a los elementos de una tupla. En este caso, el índice -1 hace referencia al último elemento de la secuencia, el -2 al penúltimo y así, sucesivamente:

```Python
>>> bebidas = ('agua', 'café', 'batido', 'sorbete')
>>> bebidas[-1]
'sorbete'
>>> bebidas[-3]
'café'
```

#### Acceso a un subconjunto de elementos
También es posible acceder a un subconjunto de elementos de una tupla utilizando el operador `[:]`:

```Python
>>> vocales = 'a', 'e', 'i', 'o', 'u'
>>> vocales[2:3]  # Elementos desde el índice 2 hasta el índice 3-1
('i',)
>>> vocales[2:4]  # Elementos desde el 2 hasta el índice 4-1
('i', 'o')
>>> vocales[:]  # Todos los elementos
('a', 'e', 'i', 'o', 'u')
>>> vocales[1:]  # Elementos desde el índice 1
('e', 'i', 'o', 'u')
>>> vocales[:3]  # Elementos hasta el índice 3-1
('a', 'e', 'i')
```

O indicando un salto entre los elementos con el operador `[::]`:

```Python
>>> pares = 2, 4, 6, 8, 10, 12, 14
>>> pares[::2]  # Acceso a los elementos de 2 en 2
(2, 6, 10, 14)
>>> pares[1:5:2]  # Elementos del índice 1 al 4 de 2 en 2
(4, 8)
>>> pares[1:6:3]  # Elementos del índice 1 al 5 de 3 en 3
(4, 10)
```

#### tuple unpacking
El concepto conocido como *tuple unpacking* (desempaquetado de una tupla) se puede aplicar sobre cualquier objeto de tipo secuencia, aunque se usa mayoritariamente con las tuplas, y consiste en lo siguiente:

```Python
>>> bebidas = 'agua', 'café', 'batido'
>>> a, b, c = bebidas
>>> a
'agua'
>>> b
'café'
>>> c
'batido'
```

Como puedes apreciar, es un tipo de asignación múltiple. Requiere que haya tantas variables a la izquierda del operador de asignación `=` como elementos haya en la secuencia.

### for tuple Python – Recorrer una tupla
El bucle `for` en Python es una de las estructuras ideales para iterar sobre los elementos de una secuencia. Para recorrer una tupla en Python utiliza la siguiente estructura:

```Python
>>> colores = 'azul', 'blanco', 'negro'
>>> for color in colores:
...   print(color)
azul
blanco
negro
```

### Modificar una tupla en Python
Como hemos dicho ya, las tuplas son objetos inmutables. No obstante, las tuplas pueden contener objetos u otros elementos de tipo secuencia, por ejemplo, una lista. Estos objetos, si son mutables, sí se pueden modificar:

```Python
>>> tupla = (1, ['a', 'b'], 'hola', 8.2)
>>> tupla[1].append('c')  # tupla[1] hace referencia a la lista
>>> tupla
(1, ['a', 'b', 'c'], 'hola', 8.2)
```

### Longitud (len) de una tupla en Python
Como cualquier tipo secuencia, para conocer la longitud de una tupla en Python se hace uso de la función `len()`. Esta función devuelve el número de elementos de una tupla:

```Python
>>> vocales = ('a', 'e', 'i', 'o', 'u')
>>> len(vocales)
5
```

### Cómo saber si un elemento está en una tupla en Python
Como hemos visto en otras unidades, para saber si un elemento está contenido en una tupla, se utiliza el operador de pertenencia `in`:

```Python
>>> colores = 'azul', 'blanco', 'negro'
>>> if 'azul' in colores:
...     print('Sí')
...     
Sí
>>> if 'verde' not in colores:
...     print('No')
...     
No
```

### Listado de métodos de la clase tuple en Python
Para terminar, se muestran los métodos de la clase tuple en Python, que son los métodos definidos para cualquier tipo secuencial:

| Método           | Descripción                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `index(elemento)` | Obtiene el índice de la primera ocurrencia del elemento en la tupla. Si el elemento no se encuentra, se lanza la excepción`ValueError`. |
| `count(elemento)` | Devuelve el número de ocurrencias del elemento en la tupla.                                                                              |


## Fuente
* [Pagina de Juan Jose Lozano Gomez sobre Python](https://j2logo.com/)
* [Estructuras de datos](https://blog.soyhenry.com/que-es-una-estructura-de-datos-en-programacion/)
* [Python para todos](https://es.py4e.com/)
* [Aprende con Alf](ttps://aprendeconalf.es)
