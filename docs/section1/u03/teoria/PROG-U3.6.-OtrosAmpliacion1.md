---
title: "UD 3 - 3.8 Ampliación 1"
description: Ampliación 1
summary: Ampliación 1
authors:
    - Diego Cano
date: 2023-11-15
icon: 
permalink: /prog/unidad3/3.8
categories:
    - PROG
tags:
    - Software
    - Asignación
    - Identidad
    - Mutabilidad
    - Paso por valor
    - Paso por referencia
    - Copia superficial
    - Copia profunda
---
## 3.8 Ampliación I

## Identidad, tipo y valor

Python es un lenguaje de programación orientado a objetos, y como tal, trata a todos los tipos de datos como objetos. Un simple entero es un objeto.

```
# x es un objeto
x = 5
```

Y una función es también un objeto.

```
# saludar es un objeto
def saludar(nombre: str):
    print(f"Hola, {nombre}")
```
 
Cada objeto viene identificado por su ***identidad***, ***tipo*** y ***valor***:

* ___Identidad___:
    > Nunca cambia e identifica de manera unívoca al objeto. El operador ```is``` nos permite saber si dos objetos son en realidad el mismo. Es decir, si dos variables hacen referencia al mismo.
* ___Tipo___:
    > Nos indica el tipo al que pertenece, como un ```float``` o una ```lista```. La función ```type()``` nos indica el tipo de un determinado objeto. Es la clase a la que pertenece.
* ___Valor___:
    > Todo objeto tiene unas características particulares. Si estas características pueden ser modificadas, diremos que es un tipo ```mutable```. De lo contrario, que es ```inmutable```.

Veamos un ejemplo con un entero:

```
x = 10
print("Identidad:", id(x))
print("Tipo:", type(x))
print("Valor:", x)
```

Podemos ver con ```id()```, que se trata de un identificador único. Es importante notar que si ejecutamos el código diferentes veces, su valor no tiene porqué se el mismo.
Por otro lado el tipo entero, ```<class 'int'>```.
Por último tenemos su valor, ```10```.

```
Identidad: 4474035136
Tipo: <class 'int'>
Valor: 10
```

Los tipos de datos ```int```, ```float```, ```bool``` y ```str``` en Python, son un tipo inmutable.


## Mutabilidad

Los diferentes tipos de Python u otros objetos en general, pueden ser clasificados atendiendo a su mutabilidad. Pueden ser:

   * Mutables: Si permiten ser modificados una vez creados.
   * Inmutables: Si no permiten ser modificados una vez creados.
    
Son mutables los siguientes tipos:

   * Listas
   * Diccionarios
   * Sets
   * Bytearray
   * Memoryview
   * Y clases definidas por el usuario

Y son inmutables:

   * Booleanos
   * Enteros
   * Float
   * Cadenas
   * Tuplas
   * Frozenset
   * Range
   * Bytes

Python trata de manera diferente a los tipos mutables e inmutables.

Por ejemplo, una lista puede ser modificada una vez creada, pero una tupla no.

```
l = [1, 2, 3]
print(id(l)) #4383854144
l[0] = 0
print(id(l)) #4383854144
```

Se puede observar que el ```id``` es el mismo antes y después de realizar la modificación.

Sin embargo, una tupla es inmutable, por lo que la siguiente asignación dará un error.

```
# La asignación no se puede realizar
t = (1, 2, 3)
t[0] = 0
```

Aunque la tupla es inmutable, si que habría una forma de modificar el valor de t, pero lo que en realidad hacemos es crear una nueva tupla y asignarle el mismo nombre, como pasa con un tipo ```int``` o ```str```.

Se podría hacer algo como lo siguiente, convertir la tupla en lista, modificar la lista y convertir a tupla otra vez.

```
t = (1, 2, 3)
print(id(t)) #4483581184
t = list(t)

# Modificar elemento
t[0] = 0

t = tuple(t)
print(t)     #(0, 2, 3)
print(id(t)) #4483953088
```

Ahora hemos conseguido modificar el valor de t, pero id(t) ya no nos devuelve el mismo valor. El nombre de la variable es el mismo, pero el objeto al que “apunta” ha cambiado.

Lo mismo pasa con los sets (mutables) y los frozenset (no mutables).

Las principales diferencias entre tipos mutables e inmutables son las siguientes:

   * Los tipos inmutables son generalmente más rápidos de acceder. Por lo que si no piensas modificar una lista, es mejor que uses una tupla.
   * Los tipos mutables son perfectos cuando quieres cambiar su contenido repetidas veces.
   * Los tipos inmutables son caros de cambiar, ya que lo que se hace en realidad es hacer una copia de su contenido en un nuevo objeto con las modificaciones.

## Paso por valor/referencia

La mutabilidad de los objetos es una característica muy importante cuando tratamos con funciones, ya que Python los tratará de manera distinta.

Si conoces lenguajes de programación como C, los conceptos de paso por valor o referencia te resultarán familiares:

   * Los tipos inmutables son pasados por valor, por lo tanto dentro de la función se accede a una copia y no al valor original.
   * Los tipos mutables son pasados por referencia, como es el caso de las listas y los diccionarios. Algo similar a como C pasa las array como punteros.

Tenemos una función que modifica dos variables.

```
def funcion(a, b):
    a = 10
    b[0] = 10

def main():
    # x es un entero
    x = 5
    # y es una lista
    y = [5]

    funcion(x, y)

    print(x) # 5
    print(y) # 10

if __name__ == "__main__":
    main()
```

Si llamamos a la función con ambas variables, vemos como el valor de x no ha cambiado, pero el de y sí.
Esto se debe a que ```a = 10``` trabaja con un valor de ```a``` local a la función, al ser el entero un tipo inmutable. Sin embargo ```b[0] = 10``` actúa sobre la variable original.


## Copia superficial y profunda:

En Python para los tipos de datos inmutables solamente se usan asignaciones y para los tipos de datos mutables además se utiliza la copia superficial y la copia profunda.

Las variables en Python no guardan directamente valores ni objetos sino referencias a estos. Por lo que cuando se hace una asignación no se están copiando esos valores.

```
num1 = 5
num2 = num1

print(f"num1 = {num1} (id => {id(num1)})")
print(f"num2 = {num2} (id => {id(num2)})\n")

num1 += 1

print(f"num1 = {num1} (id => {id(num1)})")
print(f"num2 = {num2} (id => {id(num2)})")
```

Si ejecutamos nuestro ejemplo, podemos observar cómo :

```
num1 = 5 (id => 140716801844136)
num2 = 5 (id => 140716801844136)

num1 = 6 (id => 140716801844168)
num2 = 5 (id => 140716801844136)
```

### Copia superficial:

```Solamente se copian las referencias a los elementos contenidos en el objeto.```

### Copia profunda:

```Si el objeto contiene subobjetos estos se copian recursivamente.```

Veamos el siguiente ejemplo:

```
from random import randint
from copy import copy, deepcopy

def lista(n = 2):
    lst = list()
    for k in range(n):
        lst.append(randint(0,99))
    return lst

def main():
    LA = [lista(), lista()]
    A = LA
    B = copy(LA)
    C = deepcopy(LA)
    
    print("LA id =", id(LA), "->", LA)
    print("A id =", id(A), "->", A)
    print("B id =", id(B), "->", B)
    print("C id =", id(C), "->", C)
    print("LA[0] id =", id(LA[0]), "->", LA[0])
    print("A[0] id =", id(A[0]), "->", A[0])
    print("B[0] id =", id(B[0]), "->", B[0])
    print("C[0] id =", id(C[0]), "->", C[0])

if __name__ == "__main__":
    main()
```

Como se puede observar el id de LA y A es el mismo ya que ambos hacen referencia a la misma instancia.

El id de B es diferente porque este es una copia, sin embargo los id de sus listas interiores son iguales a los identificadores de las listas contenidas en LA, debido a que B es una copia superficial.

En el caso de C, su id también es diferente al de A y LA, así como los identificadores de las listas que contiene, puesto que C es una copia profunda.

A simple vista parece que la copia superficial hace exactamente lo mismo que la copia profunda porque los valores son iguales, sin embargo la diferencia radica en que las instancias a los objetos referenciados por A, B y C respectivamente son distintas.

Se puede ver más claramente en el siguiente diagrama:

![Diagrama de ejemplo con referencias de las listas original y copiadas](https://codingornot.com/wp-content/uploads/2017/06/copia-superficial-y-profunda-768x698.png)


## Fuente

* [Python: copia superficial y copia profunda](https://codingornot.com/05-python-copia-superficial-y-copia-profunda)
* [Tipos y estructuras - Mutabilidad](https://ellibrodepython.com/mutabilidad-python)
