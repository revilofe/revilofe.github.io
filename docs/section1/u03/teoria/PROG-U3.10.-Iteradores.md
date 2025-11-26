---
title: "UD 3 - 3.10 Iteradores"
description: "Iteradores y objetos iterables en Python"
summary: "Uso de iteradores y objetos iterables para recorrer secuencias como listas de forma eficiente."
authors:
    - Eduardo Fdez
date: 2025-11-08
icon: "material/file-document-outline"
permalink: /prog/unidad3/3.10
categories:
    - PROG
tags:
    - Software
    - Iteradores
    - Iterables
    - Listas
    - Python
---

## 3.10. Iteradores y Objetos Iterables

En Python, cuando recorremos los elementos de una lista, tupla o cualquier otra secuencia, normalmente utilizamos un bucle `for`. Aunque esta es la forma más común y sencilla, es importante entender el mecanismo que funciona por debajo: los **iteradores**.

Comprender cómo funcionan los iteradores nos permite escribir código más eficiente y avanzado, especialmente cuando trabajamos con grandes volúmenes de datos.

### 1. ¿Qué es un objeto iterable?

Un **objeto iterable** es cualquier objeto en Python que puede ser "iterado", es decir, que puede devolver sus elementos uno por uno. Si puedes usar un objeto en un bucle `for`, entonces es un iterable.

Algunos ejemplos de iterables que ya conoces son:

-   Listas (`[1, 2, 3]`)
-   Tuplas (`(1, 2, 3)`)
-   Cadenas de texto (`"hola"`)
-   Diccionarios (`{'a': 1, 'b': 2}`)
-   Conjuntos (`{1, 2, 3}`)

Técnicamente, un objeto es iterable si implementa el método `__iter__()`, el cual debe devolver un objeto **iterador**.

### 2. ¿Qué es un iterador?

Un **iterador** es un objeto que representa un flujo de datos. Se encarga de llevar la cuenta de qué elemento de la secuencia es el siguiente. Un iterador debe implementar dos métodos especiales, que forman el "protocolo del iterador":

1.  `__iter__()`: Devuelve el propio objeto iterador. Es necesario para que los iteradores se puedan usar tanto en bucles `for` como `while`.
2.  `__next__()`: Devuelve el siguiente elemento del flujo de datos. Cuando no hay más elementos, lanza una excepción `StopIteration`.

La principal diferencia es que un **iterable** es el objeto que contiene los datos (como una lista), mientras que un **iterador** es el objeto que se encarga de devolver los datos uno a uno.

### 3. El bucle `for` y los iteradores

Cuando utilizas un bucle `for` para recorrer una lista, Python realiza los siguientes pasos internamente:

1.  Llama a la función `iter()` sobre el objeto iterable (la lista) para obtener un objeto iterador.
2.  En cada vuelta del bucle, llama a la función `next()` sobre el iterador para obtener el siguiente elemento.
3.  Asigna ese elemento a la variable del bucle.
4.  Cuando el iterador lanza la excepción `StopIteration`, el bucle `for` termina automáticamente.

Veamos un ejemplo:

```python
mi_lista = [10, 20, 30]

# El bucle for hace esto internamente:
# 1. Obtiene el iterador de la lista
iterador = iter(mi_lista)

# 2. Llama a next() repetidamente hasta que se lanza StopIteration sin usar 
while True:
    try:
        elemento = next(iterador)
        print(elemento)
    except StopIteration:
        break
```

El resultado de este código es el mismo que el de un bucle `for` simple:

```
10
20
30
```

#### 3.1 Uso de centinelas

Para iterar usando `while` sin `while True` y sin `break`, puedes usar un **valor centinela** con `next()` que tiene un segundo argumento opcional como valor por defecto. Aquí está la solución:

```python
centinela = object()  # Un objeto único como valor centinela
elemento = next(iterador, centinela)
while elemento is not centinela:
    print(elemento)
    elemento = next(iterador, centinela)
```

En este enfoque, `next(iterador, centinela)`,  el segundo argumento `centinela` actúa como **valor predeterminado** que se devuelve cuando
el iterador está vacío, en lugar de lanzar `StopIteration`. La condición del `while` verifica si el elemento obtenido 
es diferente del centinela, y cuando finalmente se devuelve el centinela, el bucle termina naturalmente sin necesidad de `break`.
Es importante usar `object()` como centinela porque crea un objeto único que garantiza que nunca será igual a ningún valor legítimo del iterador


Esta técnica es especialmente útil cuando necesitas procesar datos secuenciales hasta encontrar un valor específico
que señale el final.

También puedes combinar el centinela con un bucle `for` utilizando la forma de dos argumentos de `iter()`:

```
mi_lista =[2][3][1]
iterador = iter(mi_lista)

centinela = object()  # Un objeto único como valor centinela
for elemento in iter(lambda: next(iterador, centinela), centinela):
    print(elemento)
```

**¿Cómo funciona esto?**

Cuando `iter()` recibe dos argumentos, el primero debe ser un **callable** (una función) y el segundo es un **valor centinela**. En este modo, `iter()` crea un iterador especial que:

1. Llama repetidamente a la función callable (`lambda: next(iterador, centinela)`)
2. Devuelve cada resultado obtenido
3. Se detiene cuando el resultado es igual al valor centinela, lanzando `StopIteration` automáticamente

En nuestro ejemplo:

- `lambda: next(iterador, centinela)` crea una función anónima que obtiene el siguiente elemento del iterador
- Si el iterador tiene elementos, `next()` los devuelve normalmente (10, 20, 30)
- Cuando el iterador se agota, `next(iterador, centinela)` devuelve el `centinela` en lugar de lanzar `StopIteration`
- En ese momento, `iter(lambda..., centinela)` detecta que la función devolvió el centinela y genera `StopIteration`, terminando el bucle `for`

Este patrón es útil cuando ya tienes un iterador y quieres procesarlo de manera elegante sin manejar excepciones explícitamente.


### 4. Uso explícito de iteradores

Podemos usar las funciones `iter()` y `next()` para controlar el proceso de iteración manualmente. Esto nos da un mayor control sobre cómo y cuándo accedemos a los elementos de una secuencia.

```python
# Creamos una lista, que es un objeto iterable
numeros = [1, 2, 3]

# Obtenemos el iterador a partir del iterable
mi_iterador = iter(numeros)

# Obtenemos los elementos uno por uno usando next()
print(next(mi_iterador))  # Salida: 1
print(next(mi_iterador))  # Salida: 2
print(next(mi_iterador))  # Salida: 3

# Si intentamos obtener otro elemento, se lanzará la excepción StopIteration
# print(next(mi_iterador))  # Esto daría un error: StopIteration
```

### 5. Ventajas de usar iteradores

Aunque el bucle `for` es más sencillo, entender los iteradores es útil por varias razones:

-   **Eficiencia de memoria (Lazy Evaluation)**: Los iteradores son "perezosos" (lazy). No cargan todos los elementos en memoria a la vez, sino que los "generan" uno por uno cuando se les pide con `next()`. Esto es extremadamente útil para trabajar con archivos muy grandes o secuencias de datos infinitas, ya que el consumo de memoria es mínimo.
-   **Código más flexible**: Permiten crear flujos de datos complejos que no necesariamente provienen de una lista o tupla. Por ejemplo, se puede crear un iterador que genere números primos, lea líneas de un sensor en tiempo real o procese datos de una base de datos sin cargarlos todos en memoria.
-   **Base para otras herramientas de Python**: Muchas funciones y construcciones avanzadas de Python, como las "list comprehensions" y las "expresiones generadoras", se basan en el concepto de iteración.

### 6. Conclusión

Aunque en el día a día seguiremos usando bucles `for` para recorrer listas y otros iterables por su simplicidad, ahora sabemos que, por debajo, Python está utilizando **iteradores**.

Este conocimiento nos permite entender mejor cómo funciona el lenguaje y nos abre la puerta a escribir código más eficiente y potente, especialmente cuando nos enfrentamos a grandes volúmenes de datos donde la gestión de la memoria es crucial.

## Fuente
* [Python para todos](https://es.py4e.com/)
* [Aprende con Alf](https://aprendeconalf.es)
* [Real Python - Iterators and Iterables](https://realpython.com/python-iterators-iterables/)
