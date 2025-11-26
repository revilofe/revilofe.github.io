---
title: "UD 3 - 3.9 Ampliación 2"
description: Ampliación 2
summary: Ampliación 2
authors:
  - Diego Cano
date: 2023-11-15
icon: "material/file-document-outline"
permalink: /prog/unidad3/3.9
categories:
  - PROG
tags:
  - Software
  - Globales
  - join
  - Iterables con for
  - Return con operadores lógicos
---

## Variables globales

Las variables declaradas fuera de las funciones son de ámbito global.

No es una buena práctica abusar de este uso, más bien solo para variables definidas cómo constantes.
El resto de variables podemos seguir utilizándolas de manera local, dentro de las funciones y utilizando los pasos de
parámetros a las distintas funciones y el retorno de valores cuando sea necesario para actualizarlas.

Las colecciones pasan su id o referencia, esto quiere decir, que si modificamos algo en ellas dentro de una función, se
modificará también en la colección original... a diferencia de los tipos de variables primitivos (`int`, `float`, `str`,
`bool`... que son inmutables y debemos reasignar su valor)

## Método join

La sintaxis del método `join()` es:

```<sep>.join(<iterable>)```

Donde,

* `<iterable>` es cualquier iterable de Python que contenga subcadenas, como una lista o una tupla, y
* `<sep>` es el separador sobre el que quieres que se unan las subcadenas.

En esencia, el método `join()` une todos los elementos en un `<iterable>` usando `<sep>` como el separador.

Ejemplo:

```
def mostrar_lista(asignaturas: list):
    print(" - ".join(asignaturas))

def main():
    asignaturas = ['Programación', 'Entornos de Desarrollo', 'Sistemas Informáticos', 'FOL', 'Lenguajes de Marcas', 'Bases de Datos']
    mostrar_lista(asignaturas)
```

El resultado mostrará en consola los elementos de la lista separados por la cadena de caracteres " - ":

```
Programación - Entornos de Desarrollo - Sistemas Informáticos - FOL - Lenguajes de Marcas - Bases de Datos
```

## Bucle for para generar iterables

```
Instrucción for _ in range()
```

```
Instrucción for i in range()
```

La variable definida en `for` con nombre `_` indica que no vamos a usar dicha variable, sino que solo
necesitamos ejecutar una instrucción un número determinado de veces.

Un ejemplo sencillo sería crear una lista de 10 elementos con todos los valores asignados a la cadena de caracteres
vacía:

```lista_valores = list('' for _ in range(10))```

Para crear listas o tuplas con elementos iterables necesitamos ejecutar el constructor `list()` o `[]` para listas o `tuple()` o `()` para tuplas.

Un ejemplo un poco más complejo, ejecutando una función para crear un iterable y construir una tupla, sería el
siguiente:

```
def pedir_asignatura(indice: int) -> str:
    asignatura = None
    while asignatura == None:
        try:
            asignatura = input(f"{indice}. ").strip()
            if len(asignatura) <= 0:
                asignatura = None
                raise ValueError("No es posible introducir una asignatura vacía.")
        except ValueError as e:
            print(f"**Error** {e}")
    return asignatura


def crear_asignaturas(num_asignaturas = 6) -> tuple:
    print("Introduzca las asignaturas de 1º de DAM: ")
    asignaturas = tuple(pedir_asignatura(i + 1) for i in range(num_asignaturas))
    return asignaturas


def main():
    asignaturas_1DAM = crear_asignaturas()
    print(asignaturas_1DAM)


if __name__ == "__main__":
    main()
```

Otro ejemplo sería la creación de una matriz. Las matrices son estructuras de más de una dimensión.

Si necesitamos almacenar un tablero de ajedrez y en sus posiciones inicialmente quiero almacenar el valor 0, podemos
crear una tupla con listas anidadas en su interior.

El cerebro humano percibe esta matriz cómo una estructura de filas y columnas:

```
Tablero: 8x8
 
Columnas 0  1  2  3  4  5  6  7
Filas
0       [0, 0, 0, 0, 0, 0, 0, 0]
1       [0, 0, 0, 0, 0, 0, 0, 0]
2       [0, 0, 0, 0, 0, 0, 0, 0]
3       [0, 0, 0, 0, 0, 0, 0, 0]
4       [0, 0, 0, 0, 0, 0, 0, 0]
5       [0, 0, 0, 0, 0, 0, 0, 0]
6       [0, 0, 0, 0, 0, 0, 0, 0]
7       [0, 0, 0, 0, 0, 0, 0, 0]
```

Podemos crearla manualmente introduciendo una a una todas las listas de la tupla:

```tablero = ([0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], ...)```

O utilizar un for para generar un iterable:

```
#Constante que define el valor de las celdas de la matriz inicialmente
VALORINI = 0

def crear_fila() -> list:
    return list(VALORINI for _ in range (8))


def crear_tablero() -> list:
    return list(crear_fila() for _ in range (8))


def mostrar_matriz(tablero: list) :
    res = ""
    for fila in tablero:
        for celda in fila:
            res += str(celda) + " "
        res += "\n"
    print(res)


def main():
    tablero = crear_tablero()
    mostrar_matriz(tablero)


if __name__ == "__main__":
    main()
```

El resultado del programa será el siguiente:

```
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0	
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0	
```

**También podemos utilizar condiciones en los propios bucles**. 

En el ejemplo siguiente buscamos extraer de un conjunto los nombres que empiezan por la letra 'A':
   
   ```
   nombres = ('Ana', 'Patri', 'David', 'Alba', 'Dario', 'Antonio', 'Ricardo', 'Vícky')
   nombres_que_empiezan_por_A = {nombre for nombre in nombres if nombre[:1].upper() == 'A'}
   print(nombres_que_empiezan_por_A)
   ```

El resultado del programa será el siguiente:

   ```
   {'Alba', 'Ana', 'Antonio'}
   ```

## Uso de operadores lógicos para retornar valores de distintas funciones

Cómo ya sabemos, si evaluamos en Python el contenido de una variable de tipo `str` de manera lógica, si se trata de una
cadena vacía lo tomará como `False` y si tiene algún contenido será `True`.

```
def mostrar_contenido(cadena: str):
    if cadena: #es lo mismo que si escribimos if cadena == ""
        print(cadena)
    else:
        print("La variable a es una cadena vacía")

def main():
    mostrar_contenido('')
    mostrar_contenido('hola')
```

El resultado sería el siguiente:

```
La variable a es una cadena vacía
hola
```

Lo mismo ocurre con el tipo de dato `int` o `float`... si es `0` Python lo considera `False` y cualquier número distinto a `0` es
considerado `True`.

De esta manera, os podéis encontrar programas que utilicen operadores lógicos para retornar valores de más de una
función.

Un ejemplo simple sería el siguiente:

```

EDAD = 1
def bebida_alcoholica(edad: int) -> str:
    if edad >= 18:
        return "Cubata"
    return ""


def bebida_sin_alcohol(edad: int) -> str:
    if edad >= 12:
        return "Zumo"
    return "Agua"


def dar_bebida(cliente: tuple) -> str:
    return bebida_alcoholica(cliente[EDAD]) or bebida_sin_alcohol(cliente[EDAD]) ## "" evaluado como False, entonces se ejecuta la función de la derecha
     
     
def main():
    clientes = [("Antonio", 17), ("Ana", 21), ("Marta", 8)]
    for cliente in clientes:
        print(cliente[0] + " toma " + dar_bebida(cliente))
         
         
if __name__ == "__main__":
    main()
```

La función `dar_bebida()` contiene únicamente la instrucción `return` que evalúa dos expresiones con un operador
lógico `or`. Las expresiones son funciones que a su vez retornan un valor `str`.
Si ejecutamos el programa, la función `dar_bebida()` con la primera tupla `("Antonio", 17)` realiza lo
siguiente:

1. Se ejecuta la función que está a la izquierda del operador `or`.
2. Si el resultado de la función `bebida_alcoholica()` es una cadena de caracteres vacía.
3. Entonces, el intérprete de Python toma esa cadena como `False`, y pasa a ejecutar la expresión de la derecha del
   operador `or`.
4. La función `bebida_sin_alcohol()` para la edad `17` retorna un `str` no vacía.
5. En este caso, Python entiende que el retorno de la función `dar_bebida()` debe ser la cadena de caracteres que se
   evalúa como `True`.

El resultado del programa será el siguiente:

```
Antonio toma Zumo
Ana toma Cubata
Marta toma Agua
```
