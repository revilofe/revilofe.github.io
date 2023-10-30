---
title: Porque en Python empiezan los programas con if __name__ == __main__
description: te has encontrado if __name__ == __main__ en los programas de python. Entra y descubre que significa.
authors:
    - Eduardo Fdez.
date: 2022-10-26
tags:
    - python
---    

Cuando un intérprete de Python lee un archivo de Python, primero establece algunas variables especiales. Luego ejecuta el código desde el archivo.

Una de esas variables se llama `__name__` .

Si sigues este artículo paso a paso y lees sus fragmentos de código, aprenderás cómo usar `if __name__ == "__main__"`, y por qué es tan importante.

## Módulos de Python explicados

Los archivos de Python se llaman módulos y se identifican mediante la extensión de archivo `.py`. Un módulo puede definir funciones, clases y variables.

Entonces, cuando el intérprete ejecuta un módulo, el variable `__name__` se establecerá como `__main__` si el módulo que se está ejecutando es el programa principal.

Pero si el código está importando el módulo desde otro módulo, entonces el variable `__name__` se establecerá en el nombre de ese módulo.

Echemos un vistazo a un ejemplo. Cree un módulo de Python llamado `file_one.py` y pegue este código de nivel superior dentro:

```python
# Python file one module

print("File one __name__ is set to: {}" .format(__name__))
```

Al ejecutar este archivo, verás exactamente de lo que estábamos hablando. La variable `__name__` para este módulo se establece en `__main__`:

```
File one __name__ is set to: __main_
```

Ahora agregua otro archivo llamado `file_two.py` y pegua este código dentro:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))
```

Además, modifica el código en `file_one.py` de esta manera para que importemos el módulo `file_two`:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))
```

Ejecutando nuestro código `file_one` una vez más mostrará que la variable `__name__` en `file_one` no cambió, y aún permanece establecida en `__main__`. Pero ahora la variable `__name__` en `file_two` se establece como el nombre del módulo, por lo tanto `file_two`.

El resultado debería verse así:

```
File two __name__ is set to: file_two
File one __name__ is set to: __main__
```

Pero ejecuta `file_two` directamente y verás que su nombre está establecido en `__main__`:

```
File two __name__ is set to: __main__

```

La variable `__name__` para el archivo/módulo que se ejecuta será siempre `__main__`. Pero la variable `__name__` para todos los demás módulos que se importan se establecerá en el nombre de su módulo.

## Convenciones de nombres de archivos de Python

La forma habitual de usar `__name__` y `__main__` se ve así:

```python
if __name__ == "__main__":
   Do something here

```

Veamos cómo funciona esto en la vida real y cómo usar realmente estas variables.

Modifica `file_one` y `file_two` para que se vean así:

`file_one`:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")
```

`file_two`:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")
```

Nuevamente, al ejecutar `file_one` , verás que el programa reconoció cuál de estos dos módulos es `__main__` y ejecutó el código de acuerdo con nuestras primeras declaraciones `if else`.

El resultado debería verse así:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
```

Ahora ejecuta `file_two` y verás que la variable `__name__` está establecida en `__main__`:

```
File two __name__ is set to: __main__
File two executed when ran directly
```

Cuando se importan y ejecutan módulos como este, se importarán sus funciones y se ejecutará el código de nivel superior.

Para ver este proceso en acción, modifica tus archivos para que se vean así:

`file_one`:

```python
# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")
```

`file_two`:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")
```

Ahora las funciones se cargan pero no se ejecutan.

Para ejecutar una de estas funciones, modifica la parte `if __name__ == "__main__"` de `file_one` para que se vea así:

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
else:
   print("File one executed when imported")
```

Al ejecutar `file_one`, deberías ver que sea así:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
```

Además, puedes ejecutar funciones desde archivos importados. Para hacer eso, modifica la parte `if __name__ =="__name__"` de `file_one` para que se vea así:

```python
if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   file_two.function_three()
else:
   print("File one executed when imported")
```

Y puedes espera un resultado como este:

```
File two __name__ is set to: file_two
File two executed when imported
File one __name__ is set to: __main__
File one executed when ran directly
Function two is executed
Function three is executed
```

Ahora digamos que el módulo `file_two` es realmente grande con muchas funciones (dos en nuestro caso), y no deseas importarlas todas. Modifica   `file_two` para que se vea así:

```python
# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

def function_three():
   print("Function three is executed")

def function_four():
   print("Function four is executed")

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")
```

Y para importar las funciones específicas del módulo, usa el bloque `from` import en el archivo `file_one`:

```python
# Python module to execute
from file_two import function_three

print("File one __name__ is set to: {}" .format(__name__))

def function_one():
   print("Function one is executed")

def function_two():
   print("Function two is executed")

if __name__ == "__main__":
   print("File one executed when ran directly")
   function_two()
   function_three()
else:
   print("File one executed when imported")
```

## Conclusion

Hay un caso de uso realmente agradable para la variable `__name__`, ya sea que desees un archivo que se pueda ejecutar como el programa principal o sea importardo por otros módulos. Podemos usar un bloque `if __name__ == "__name__"` para permitir o evitar que se ejecuten partes del código cuando sean importados los módulos.

Cuando el intérprete de Python lee un archivo, la variable `__name__` se establece como `__main__` si el módulo que se está ejecutando, o como el nombre del módulo si se importa. Al leer el archivo se ejecuta todo el código de nivel superior, pero no las funciones y clases (ya que solamente se importarán).

## Fuente

* [Python if __name__ == __main__ Explicado con ejemplos de código](https://www.freecodecamp.org/espanol/news/python-if-name-main/)
