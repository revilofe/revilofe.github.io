---
title: "UD 1 - 1.3 Tipos de datos"
description: Tipos de datos
summary: Tipos de datos
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: 
permalink: /prog/unidad1/1.1
categories:
    - PROG
tags:
    - Software
---


## 1.3. Tipos de datos
En Python, como en otros lenguajes de programación, los datos se clasifican en distintos tipos según su naturaleza y el tipo de operaciones que se pueden realizar con ellos. Los tipos de datos primitivos simples son aquellos que no se pueden descomponer en partes más pequeñas y son los que se utilizan para representar los valores más básicos. Los tipos de datos primitivos compuestos son aquellos que se pueden descomponer en partes más pequeñas y son los que se utilizan para representar estructuras más complejas.


### 1. Tipos de datos primitivos simples
Los tipos de datos primitivos simples son aquellos que NO se pueden descomponer en partes más pequeñas y son los que se utilizan para representar los valores más básicos. Los tipos de datos primitivos simples en Python son:

* **Números** (numbers): Secuencia de dígitos (pueden incluir el - para negativos y el . para decimales) que representan números.
  **Ejemplo** . 0, -1, 3.1415.
* **Cadenas** (strings): Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas simples o dobles.
  **Ejemplo** . ‘Hola’, “Adiós”.
* **Booleanos** (boolean): Contiene únicamente dos elementos `True` y `False` que representan los valores lógicos verdadero y falso respectivamente.


### 2. Tipos de datos primitivos compuestos (contenedores)
Los tipos de datos primitivos compuestos son aquellos que se pueden descomponer en partes más pequeñas y son los que se utilizan para representar estructuras más complejas. Profundizaremos más adelante en ellos. Los tipos de datos primitivos compuestos en Python son:

* **Listas** (lists): Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. Se representan con corchetes y los elementos se separan por comas.
  **Ejemplo** . [1, “dos”, [3, 4], True].
* **Tuplas** (tuples). Colecciones de objetos que representan secuencias ordenadas de objetos de distintos tipos. A diferencia de las listas son inmutables, es decir, que no cambian durante la ejecución. Se representan mediante paréntesis y los elementos se separan por comas.
  **Ejemplo** . (1, ‘dos’, 3)
* **Diccionarios** (dictionaries): Colecciones de objetos con una clave asociada. Se representan con llaves, los pares separados por comas y cada par contiene una clave y un objeto asociado separados por dos puntos.
  **Ejemplo** . {‘pi’:3.1416, ’e’:2.718}.

### 3. Clase de un dato (`type()`)

La clase a la que pertenece un dato se obtiene con el comando `type()`

```python
>>> type(1)
<class 'int'>
>>> type("Hola")
<class 'str'>
>>> type([1, "dos", [3, 4], True])
<class 'list'>
>>>type({'pi':3.1416, 'e':2.718})
<class 'dict'>
>>>type((1, 'dos', 3))
<class 'tuple'>
```

### 4. Números (clases `int` y `float`)

Secuencia de dígitos (pueden incluir el - para negativos y el . para decimales) que representan números. Pueden ser enteros (`int`) o reales (`float`).

```python
>>> type(1)
<class 'int'>
>>> type(-2)
<class 'int'>
>>> type(2.3)
<class 'float'>
```

#### 4.1. Operadores aritméticos

* Operadores aritméticos: `+` (suma), `-` (resta), `*` (producto), `/` (cociente), `//` (cociente división entera), `%` (resto división entera), `**` (potencia).

Orden de prioridad de evaluación:


|   |                        |
| --- | ------------------------ |
| 1 | Funciones predefinidas |
| 2 | Potencias              |
| 3 | Productos y cocientes  |
| 4 | Sumas y restas         |
|   |                        |

Se puede saltar el orden de evaluación utilizando paréntesis `( )`.

```python
>>> 2+3
5
>>> 5*-2
-10
>>> 5/2
2.5
>>> 5//2
2
>>> (2+3)**2
25
```

#### 4.2. Operadores lógicos con números

Devuelven un valor lógico o booleano.

* Operadores lógicos: `==` (igual que), `>` (mayor que), `<` (menor que), `>=` (mayor o igual que), `<=` (menor o igual que), `!=` (distinto de).

```python
>>> 3==3
True
>>> 3.1<=3
False
>>> -1!=1
True
```

### 5. Cadenas (clase `str`)

Secuencia de caracteres alfanuméricos que representan texto. Se escriben entre comillas sencillas ’ o dobles “.

```python
'Python'
"123"
'True'
# Cadena vacía
''
# Cadena con un espacio en blanco
' '
# Cambio de línea
'\n'
# Tabulador
'\t'
```

#### 5.1. Acceso a los elementos de una cadena

Cada carácter tiene asociado un índice que permite acceder a él.


| Cadena           | `P` | `y` | `t` | `h` | `o` | `n` |
| ------------------ | ----- | ----- | ----- | ----- | ----- | ----- |
| Índice positivo | 0   | 1   | 2   | 3   | 4   | 5   |
| Índice negativo | -6  | -5  | -4  | -3  | -2  | -1  |

* `c[i]` devuelve el carácter de la cadena `c` con el índice `i`.

*El índice del primer carácter de la cadena es 0.*

También se pueden utilizar índices negativos para recorrer la cadena del final al principio.

*El índice del último carácter de la cadena es -1.*

```python
>>> 'Python'[0]
'P'
>>> 'Python'[1]
'y'
>>> 'Python'[-1]
'n'
>>> 'Python'[6]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
```

#### 5.2. Subcadenas

* `c[i:j:k]` : Devuelve la subcadena de `c` desde el carácter con el índice `i` hasta el carácter anterior al índice `j`, tomando caracteres cada `k`.

```python
>>> 'Python'[1:4]
'yth'
>>> 'Python'[1:1]
''
>>> 'Python'[2:]
'thon'
>>> 'Python'[:-2]
'Pyth'
>>> 'Python'[:]
'Python'
>>> 'Python'[0:6:2]
'Pto'
```

#### 5.3. Operaciones con cadenas

* `c1 + c2` : Devuelve la cadena resultado de concatenar las cadenas `c1` y `c2`.
* `c * n` : Devuelve la cadena resultado de concatenar `n` copias de la cadena `c`.
* `c1 in c2` : Devuelve `True` si `c1` es una cadena concenida en `c2` y `False` en caso contrario.
* `c1 not in c2` : Devuelve `True` si `c1` es una cadena no concenida en `c2` y `False` en caso contrario.

```python
>>> 'Me gusta ' + 'Python'
'Me gusta Python'
>>> 'Python' * 3
'PythonPythonPython'
>>> 'y' in 'Python'
True
>>> 'tho' in 'Python'
True
>>> 'to' not in 'Python'
True
```

#### 5.4. Operaciones de comparación de cadenas

* `c1 == c2` : Devuelve `True` si la cadena `c1` es igual que la cadena `c2` y `False` en caso contrario.
* `c1 > c2` : Devuelve `True` si la cadena `c1` sucede a la cadena `c2` y `False` en caso contrario.
* `c1 < c2` : Devuelve `True` si la cadena `c1` antecede a la cadena `c2` y `False` en caso contrario.
* `c1 >= c2` : Devuelve `True` si la cadena `c1` sucede o es igual a la cadena `c2` y `False` en caso contrario.
* `c1 <= c2` : Devuelve `True` si la cadena `c1` antecede o es igual a la cadena `c2` y `False` en caso contrario.
* `c1 != c2` : Devuelve `True` si la cadena `c1` es distinta de la cadena `c2` y `False` en caso contrario.
  
*Utilizan el orden establecido en el [código ASCII](https://www.codigosascii.com/)* .

```python
>>> 'Python' == 'python'
False
>>> 'Python' < 'python'
True
>>> 'a' > 'Z'
True
>>> 'A' >= 'Z'
False
>>> '' < 'Python'
True
```

#### 5.5. Funciones de cadenas

* `len(c)` : Devuelve el número de caracteres de la cadena `c`.
* `min(c)` : Devuelve el carácter menor de la cadena `c`.
* `max(c)` : Devuelve el carácter mayor de la cadena `c`.
* `c.upper()` : Devuelve la cadena con los mismos caracteres que la cadena `c` pero en mayúsculas.
* `c.lower()` : Devuelve la cadena con los mismos caracteres que la cadena `c` pero en minúsculas.
* `c.title()` : Devuelve la cadena con los mismos caracteres que la cadena `c` con el primer carácter en mayúsculas y el resto en minúsculas.
* `c.split(delimitador)` : Devuelve la lista formada por las subcadenas que resultan de partir la cadena `c` usando como delimitador la cadena `delimitador`. Si no se especifica el delimitador utiliza por defecto el espacio en blanco.

```python
>>> len('Python')
6
>>> min('Python')
'P'
>>> max('Python')
'y'
>>> 'Python'.upper()
'PYTHON'
>>> 'A,B,C'.split(',')
['A', 'B', 'C']
>>> 'I love Python'.split()
['I', 'love', 'Python']
```

#### 5.6. Cadenas formateadas (`format()`)

* `c.format(valores)`: Devuelve la cadena `c` tras sustituir los valores de la secuencia `valores` en los marcadores de posición de `c`. Los marcadores de posición se indican mediante llaves `{}` en la cadena `c`, y el reemplazo de los valores se puede realizar por posición, indicando en número de orden del valor dentro de las llaves, o por nombre, indicando el nombre del valor, siempre y cuando los valores se pasen con el formato `nombre = valor`.

```python
>>> 'Un {} vale {} {}'.format('€', 1.12, '$')
'Un € vale 1.12 $'
>>> 'Un {2} vale {1} {0}'.format('€', 1.12, '$')
'Un $ vale 1.12 €'
>>> 'Un {moneda1} vale {cambio} {moneda2}'.format(moneda1 = '€', cambio = 1.12, moneda2 = '$')
'Un € vale 1.12 $'
```

Los marcadores de posición, a parte de indicar la posición de los valores de reemplazo, pueden indicar también el formato de estos. Para ello se utiliza la siguiente sintaxis:

* `{:n}` : Alinea el valor a la izquierda rellenando con espacios por la derecha hasta los `n` caracteres.
* `{:>n}` : Alinea el valor a la derecha rellenando con espacios por la izquierda hasta los `n` caracteres.
* `{:^n}` : Alinea el valor en el centro rellenando con espacios por la izquierda y por la derecha hasta los `n` caracteres.
* `{:nd}` : Formatea el valor como un número entero con `n` caracteres rellenando con espacios blancos por la izquierda.
* `{:n.mf}` : Formatea el valor como un número real con un tamaño de `n` caracteres (incluído el separador de decimales) y `m` cifras decimales, rellenando con espacios blancos por la izquierda.

```python
>>> 'Hoy es {:^10}, mañana {:10} y pasado {:>10}'.format('lunes', 'martes', 'miércoles')
'Hoy es   lunes   , mañana martes     y pasado  miércoles'
>>> 'Cantidad {:5d}'.format(12)'
'Cantidad    12'
>>> 'Pi vale {:8.4f}'.format(3.141592)
'Pi vale   3.1416'
```

### 6. Datos lógicos o booleanos (clase `bool`)

Contiene únicamente dos elementos `True` y `False` que representan los valores lógicos verdadero y falso respectivamente.

`False` tiene asociado el valor 0 y `True` tiene asociado el valor 1.

#### 6.1. Operaciones con valores lógicos

* Operadores lógicos: `==` (igual que), `>` (mayor), `<` (menor), `>=` (mayor o igual que), `<=` (menor o igual que), `!=` (distinto de).
* `not b` (negación) : Devuelve `True` si el dato booleano `b` es `False` , y `False` en caso contrario.
* `b1 and b2` : Devuelve `True` si los datos booleanos `b1` y `b2` son `True`, y `False` en caso contrario.
* `b1 or b2` : Devuelve `True` si alguno de los datos booleanos `b1` o `b2` son `True`, y `False` en caso contrario.

#### 6.2. Tabla de verdad


| `x`     | `y`     | `not x` | `x and y` | `x or y` |
| --------- | --------- | --------- | ----------- | ---------- |
| `False` | `False` | `True`  | `False`   | `False`  |
| `False` | `True`  | `True`  | `False`   | `True`   |
| `True`  | `False` | `False` | `False`   | `True`   |
| `True`  | `True`  | `False` | `True`    | `True`   |

```python
>>> not True
False
>>> False or True
True
>>> True and False
False
>>> True and True
True
```

#### 6.3. Conversión de datos primitivos simples

En algunos casos, es necesario convertir un dato de un tipo a otro. Las conversiones de datos en Python se pueden clasificar en dos tipos:

1. **Conversiones explícitas**: Son aquellas en las que se especifica manualmente el tipo al que se quiere convertir el dato.
2. **Conversiones implícitas**: Son aquellas en las que Python realiza la conversión de forma automática durante la ejecución del programa.

#### 6.3.1. Conversiones explícitas

Las siguientes funciones permiten convertir un dato de un tipo a otro, siempre y cuando la conversión sea válida:

- **`int()`** convierte a entero.
  - Ejemplo:
    ```python
    int('12')  # 12
    int(True)  # 1
    int('c')   # Error
    ```

- **`float()`** convierte a número real (flotante).
  - Ejemplo:
    ```python
    float('3.14')  # 3.14
    float(True)    # 1.0
    float('III')   # Error
    ```

- **`str()`** convierte a cadena.
  - Ejemplo:
    ```python
    str(3.14)   # '3.14'
    str(True)   # 'True'
    ```

- **`bool()`** convierte a booleano.
  - Ejemplo:
    ```python
    bool('0')     # False
    bool('3.14')  # True
    bool('')      # False
    bool('Hola')  # True
    ```

#### 6.3.2. Conversiones implícitas

Python realiza ciertas conversiones de tipos de datos de manera implícita durante las operaciones. Las conversiones implícitas que Python efectúa son las siguientes:

- **De `int` a `float`**: Si se realiza una operación aritmética entre un número entero y un número real, el entero se convierte automáticamente en un número real.

  Ejemplo:
  ```python
  2 + 3.0  # 5.0 (int convertido a float)
  ```

- **De `float` a `int`**: Python no convierte automáticamente un `float` a `int` en una operación aritmética, ya que esto implicaría pérdida de precisión. Para convertir un `float` a `int`, se debe realizar una conversión explícita utilizando `int()`.

- **No hay conversión implícita de `int` a `str` ni de `float` a `str`**: Para concatenar un número con una cadena, se debe convertir explícitamente el número a cadena utilizando `str()`. Python no realiza esta conversión de manera implícita.

  Ejemplo:
  ```python
  'Hola' + str(3)  # 'Hola3'
  ```

- **No hay conversión implícita de `str` a `int` o `float`**: Si se necesita realizar operaciones aritméticas con una cadena que contiene un número, es necesario convertir la cadena explícitamente a `int` o `float` utilizando las funciones `int()` o `float()`.

  Ejemplo:
  ```python
  2 + int('3')    # 5 (conversión explícita de str a int)
  2 + float('3.0')  # 5.0 (conversión explícita de str a float)
  ```

**En resumen:**

- Las **conversiones implícitas** en Python ocurren principalmente en operaciones numéricas entre `int` y `float`.
- Tambien ocurren **conversiones implicitas** a tipo `bool` al utilizar `""`, `0`, `None` a `False`. Y todo lo que no sea  `""`, `0`, `None` a `False` se convierte a `true`.
- Para realizar operaciones con cadenas y números, es necesario realizar **conversiones explícitas** utilizando funciones como `str()`, `int()`, o `float()`.


## Fuente

* [Aprende con Alf](https://aprendeconalf.es/)
* [Pagina de Juan Jose Lozano Gomez sobre Python](https://j2logo.com/)
* [Documentación de Python](https://docs.python.org/es/3/library/index.html)
* [Tipos de datos](https://entrenamiento-python-basico.readthedocs.io/es/3.7/leccion3/tipo_numericos.html))
