---
title: "UD 2 - 2.3 Captura de excepciones"
description: Captura de excepciones
summary: Captura de excepciones
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: 
permalink: /prog/unidad2/2.3
categories:
    - PROG
tags:
    - Software
---
## 2.3. Captura de excepciones

Las excepciones y los errores son dos conceptos fundamentales en programación, pero tienen significados distintos.

### 1. Diferencia entre errores y excepciones

La principal diferencia entre errores y excepciones radica en su naturaleza y cómo afectan el flujo de ejecución del programa. Los errores indican problemas en el código que **deben ser corregidos**, mientras que las excepciones son **situaciones inesperadas** que pueden ser manejadas para asegurar que el programa siga funcionando sin interrupciones.

#### 1.1. Errores

Los errores, también conocidos como bugs, son problemas en el código que impiden que el programa funcione correctamente.
Pueden ser de diferentes tipos, como errores de sintaxis, errores lógicos (cuando el programa produce resultados incorrectos debido a un error en el algoritmo), o errores de tiempo de ejecución (que ocurren mientras el programa se está ejecutando).
Los errores pueden ser causados por una variedad de razones, incluyendo lógica incorrecta, mal uso de funciones o librerías, o incluso problemas con la configuración del entorno de desarrollo.

#### 1.2. Excepciones:

Las excepciones son eventos anómalos o inusuales que ocurren durante la ejecución de un programa y que afectan el flujo normal del mismo.
A diferencia de los errores, las excepciones no siempre indican un fallo en el código. Por ejemplo, si un programa intenta abrir un archivo que no existe, esto generará una excepción `FileNotFoundError`. Sin embargo, esto no es un error en el código en sí, sino una situación inesperada que el programa debe saber cómo manejar.
Las excepciones en Python están diseñadas para gestionar este tipo de situaciones y permitir que el programa continúe su ejecución en lugar de detenerse abruptamente.

### 2. Uso de try y except

Hemos visto varios casos de código en donde usábamos las funciones `input` e `int` para leer y analizar un número entero introducido por el usuario. También vimos lo poco seguro que podía llegar a resultar hacer algo así:

```Python
>>> velocidad = input(prompt)
¿Cual.... es la velocidad de vuelo de una golondrina sin carga?
¿Te refieres a una golondrina africana o a una europea?
>>> int(velocidad)
ValueError: invalid literal for int() with base 10:
>>>
```

Cuando estamos trabajando con el intérprete de Python, tras esta error/excepción simplemente nos aparece de nuevo el prompt, así que pensamos “¡epa, me he equivocado!”, y continuamos con la siguiente sentencia.

Sin embargo, si se escribe ese código en un script de Python y se produce el error/excepción, el script se detendrá inmediatamente, y mostrará un “traceback”. No ejecutará la siguiente sentencia.

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

Existen estructuras de ejecución condicional dentro de Python para manejar este tipo de errores/excepciones esperados e inesperados, llamadas `try / except`. La idea de `try` y `except` es que si se sabe que cierta secuencia de instrucciones puede generar un problema, sea posible añadir ciertas sentencias para que sean ejecutadas en caso de error. Estas sentencias extras (el bloque `except`) serán ignoradas si no se produce ningún error.

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

Gestionar una excepción con una sentencia `try` recibe el nombre de *capturar una excepción*. En este ejemplo, la cláusula `except` muestra un mensaje de error. En general, capturar una excepción te da la oportunidad de corregir el problema, volverlo a intentar o, al menos, terminar el programa con elegancia.

### 3. Capturar excepciones concretas

Es posible escribir programas que capturen y manejen determinadas excepciones. Durante el siguiente ejemplo, se le pide al usuario que ingrese un numero hasta que se haya ingresado un número entero válido, aunque el usuario podrá interrumpir el programa (puede variar las formas entre sistemas operativos); En linux/windows se utiliza Control-C y esta interrupción generará la excepción[`KeyboardInterrupt`](https://docs.python.org/3/library/exceptions.html#KeyboardInterrupt)

```Python
>>>x = None
...while x == None:
...     try:
...         x = int(input("Please enter a number: "))
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
```

Ten en cuenta que se a la cláusula except le puedes indicar que gestione varias excepciones, añadiendo el nombre de la excepción a continuación de la otra. Además, se pueden añadir varias cláusulas `except` cada diferenciar los bloques que gestionan la excepción en función de la excepción que se ha producido.

### 4. Lanzar excepciones

La declaración [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise) permite al programador forzar que ocurra una excepción específica.

Por ejemplo:

```Python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

El único argumento para `raise` indica la excepción que se va a generar. Debe ser una instancia de excepción o una clase de excepción (una clase que se deriva de [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception). Si se pasa una clase de excepción, se instanciará implícitamente llamando a su constructor sin argumentos:

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

### 5. Testear
También podemos testear que se lanza una determinada excepción cuando esperamos que se lance. Supongamos que tienes una función llamada dividir en un archivo `calculadora.py` que debería lanzar una excepción `ZeroDivisionError` cuando se intenta dividir por cero. A continuación puedes ver cómo escribirías la prueba:

```Python
# Archivo: test_calculadora.py

from calculadora import dividir

def test_dividir_por_cero_deberia_lanzar_excepcion():
    with pytest.raises(ZeroDivisionError):
    dividir(10, 0)
```

la sentencia `with pytest.raises(ExcepcionEsperada)` es la sintaxis que se utiliza para probar si una excepción es lanzada durante la ejecución del código.

En este ejemplo, estamos usando `pytest.raises(ZeroDivisionError)` para verificar que cuando llamamos a `dividir(10, 0)`, se lanza una excepción `ZeroDivisionError`.

En este caso, si la función `dividir` está correctamente implementada y lanza una excepción `ZeroDivisionError` cuando se divide por cero, la prueba pasará con éxito. Si no, la prueba fallará y te proporcionará información sobre el fallo.

Este es un ejemplo simple, pero pytest es una herramienta muy versátil que puede manejar una amplia gama de situaciones de prueba. Puedes escribir pruebas para casos normales, casos de borde, y muchas otras situaciones que desees probar en tu código.


### 6. Ejemplo completo

```Python

import pytest

def fahr2cel(fahr:float) -> float:
    ''' Convertir grados Fahrenheit a grados Celsius'''
    if fahr < -459.67:
        raise ValueError('Temperatura Fahrenheit incorrecta: ' + str(fahr))
    
    cel = (fahr - 32.0) * 5.0 / 9.0
    return cel

if __name__ == '__main__':
    numeroCorrecto = False
    fahr = None
    while not numeroCorrecto:
        try:
            ent = input('Introduzca la Temperatura Fahrenheit:')
            fahr = float(ent)
            cel = fahr2cel(fahr)
            numeroCorrecto = True
        except ValueError:   # Si no se puede convertir a float
            if fahr == None:
                print('Por favor introduzca un número.')
            else:
                print('La temperatura Fahrenheit es incorrecta: ' + str(fahr))

    print(cel)



def test_fahr2cel():
    with pytest.raises(ValueError):
        fahr2cel(-300)

```


### 7. Actividades

**Actividad 1**: Escribe un programa que capture la excepción división entre cero. Tendrá que mostar el mensaje del error capturado.

**Actividad 2**: Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando `try` y `except`.

## Fuente

* [Pagina de Juan Jose Lozano Gomez sobre Python](https://j2logo.com/)
* [Aprende con Alf](https://aprendeconalf.es/)
* [Python para todos](https://es.py4e.com/)
* [Documentación Python.org](https://docs.python.org/3/tutorial/errors.html)
* [Testear Excepciones](https://www.educative.io/answers/how-to-check-if-an-exception-gets-raised-in-pytest)
