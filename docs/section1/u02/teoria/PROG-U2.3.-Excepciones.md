---
title: "UD 2 - 2.3 Captura de excepciones"
description: Captura de excepciones
summary: Captura de excepciones
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: material/software
permalink: /prog/unidad2/2.3
categories:
    - PROG
tags:
    - Software
---
## Captura de excepciones

### Uso de try y except

Hemos vistos varios casos de código en donde usábamos las funciones `input` e `int` para leer y analizar un número entero introducido por el usuario. También vimos lo poco seguro que podía llegar a resultar hacer algo así:

```Python
>>> velocidad = input(prompt)
¿Cual.... es la velocidad de vuelo de una golondrina sin carga?
¿Te refieres a una golondrina africana o a una europea?
>>> int(velocidad)
ValueError: invalid literal for int() with base 10:
>>>
```

Cuando estamos trabajando con el intérprete de Python, tras el error simplemente nos aparece de nuevo el prompt, así que pensamos “¡epa, me he equivocado!”, y continuamos con la siguiente sentencia.

Sin embargo, si se escribe ese código en un script de Python y se produce el error, el script se detendrá inmediatamente, y mostrará un “traceback”. No ejecutará la siguiente sentencia.

He aquí un programa de ejemplo para convertir una temperatura desde grados Fahrenheit a grados Celsius:

```Python
ent = input('Introduzca la Temperatura Fahrenheit:')
fahr = float(ent)
cel = (fahr - 32.0) * 5.0 / 9.0
print(cel)

# Código: https://es.py4e.com/code3/fahren.py
```

Si ejecutamos este código y le damos una entrada no válida, simplemente fallará con un mensaje de error bastante antipático:

```Python
python fahren.py
Introduzca la Temperatura Fahrenheit:72
22.2222222222
```

```Python
python fahren.py
Introduzca la Temperatura Fahrenheit:fred
Traceback (most recent call last):
  File "fahren.py", line 2, in <module>
    fahr = float(ent)
ValueError: invalid literal for float(): fred
```

Existen estructuras de ejecución condicional dentro de Python para manejar este tipo de errores esperados e inesperados, llamadas `try / except`. La idea de `try` y `except` es que si se sabe que cierta secuencia de instrucciones puede generar un problema, sea posible añadir ciertas sentencias para que sean ejecutadas en caso de error. Estas sentencias extras (el bloque except) serán ignoradas si no se produce ningún error.

Puedes pensar en la característica `try` y `except` de Python como una “póliza de seguros” en una secuencia de sentencias.

Se puede reescribir nuestro conversor de temperaturas de esta forma:

```Python
ent = input('Introduzca la Temperatura Fahrenheit:')
try:
    fahr = float(ent)
    cel = (fahr - 3Python2.0) * 5.0 / 9.0
    print(cel)
except:
    print('Por favor, introduzca un número')

# Código: https://es.py4e.com/code3/fahren2.py
```

Python comienza ejecutando la secuencia de sentencias del bloque `try`. Si todo va bien, se saltará todo el bloque `except` y terminará. Si ocurre una excepción dentro del bloque `try`, Python saltará fuera de ese bloque y ejecutará la secuencia de sentencias del bloque `except`.

```Python
python fahren2.py
Introduzca la Temperatura Fahrenheit:72
22.2222222222
```

```Python
python fahren2.py
Introduzca la Temperatura Fahrenheit:fred
Por favor, introduzca un número
```

Gestionar una excepción con una sentencia `try` recibe el nombre de *capturar* una excepción. En este ejemplo, la cláusula `except` muestra un mensaje de error. En general, capturar una excepción te da la oportunidad de corregir el problema, volverlo a intentar o, al menos, terminar el programa con elegancia.

### Capturar excepciones concretas

Es posible escribir programas que capturen y manejen determnadas excepciones. Durante el siguiente ejemplo, se le pide al usuario que ingrese un numero hasta que se haya ingresado un número entero válido, aunque el usuario podra interrumpir el programa (puede variar las formas entres sistemas operativos); En linux/windows se utiliza Control-C y esta interrupción generara la excepción.[`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt)

```Python
>>>x = None
...while x == None:
...     try:
...         x = int(input("Please enter a number: "))
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
```
## Lanzar excepciones

La declaración [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise) permite al programador forzar que ocurra una excepción específica.

Por ejemplo:

```Python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
El único argumento para`raise` indica la excepción que se va a generar. Debe ser una instancia de excepción o una clase de excepción (una clase que se deriva de [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception). Si se pasa una clase de excepción, se instanciará implícitamente llamando a su constructor sin argumentos:

```Python
raise ValueError  # shorthand for 'raise ValueError()'
```
Si quieres saber si se generó una excepción pero no tienes la intención de manejarla, la siguiente forma de usar la declaración `raise`, te permitirá volver a generarla:

```Python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```
## Actividades

**Actividad 1**: Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando `try` y `except`.

**Actividad 2**: Escribe un programa que lea repetidamente la temperadebe detectar los fallos usando `try` y `except`.

## Fuente
* [Pagina de Juan Jose Lozano Gomez sobre Python](https://j2logo.com/)
* [Aprende con Alf](https://aprendeconalf.es/)
* [Python para todos](https://es.py4e.com/)
* [Documentación Python.org](https://docs.python.org/3/tutorial/errors.html)