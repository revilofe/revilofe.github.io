---
title: "UD 2 - 2.5 Documentar el código"
description: Documentar el código
summary: Documentar el código
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: "material/file-document-outline"
permalink: /prog/unidad2/2.5
categories:
    - PROG
tags:
    - Software
    - Documentar
---
## 2.5. Documentar el código en Python

Intentaremos explicar como documentar el código de Python. Ya sea un script pequeño o un proyecto grande, ya sea un [principiante](https://realpython.com/python-beginner-tips/) o un Pythonista experimentado.

La unidad se divide en cuatro secciones principales:

1. **Por qué es tan importante documentar su código:** una introducción a la documentación y su importancia
2. **Comentar vs. Documentar código:** una descripción general de las principales diferencias entre comentar y documentar, así como los momentos y formas apropiados para usar los comentarios.
3. **Documentación de la base de código de Python mediante Docstrings:** una inmersión profunda en docstrings para clases, métodos de clase, funciones, módulos, paquetes y scripts, así como lo que se debe encontrar dentro de cada uno
4. **Documentación de sus proyectos de Python:** los elementos necesarios y lo que deben contener para sus proyectos de Python

### 1. Por qué es tan importante documentar su código

Es posible que ya te hayas dado cuenta de la importancia de documentar el código. Pero si no, ten en cuenta esto que dijo Guido en una [PyCon](https://realpython.com/pycon-guide/), creador del Python:

> “Code is more often read than written.”
>
> —Guido *van Rossum*

Cuando escribes código, lo haces dirigido principalmente a dos audiencias: los usuarios y los desarrolladores (incluido tu mismo). Ambos públicos son igualmente importantes. Con el tiempo, abrirás el código fuente que creaste en el pasado, y te te preguntarás: "¿Que ... estaba intentando hacer aquí?" Si tiene problemas para tu propio código, imagínate lo que pueden experimentar los usuarios u otros desarrolladores cuando intenten usar o [contribuir](https://realpython.com/start-contributing-python/) a tu código.

Por otra parte, con el tiempo te encontrarás en la siguiente situación, quieres hacer algo en Python y encuentras lo que parece ser una gran biblioteca que puede hacer el trabajo. Sin embargo, cuando comienzas a usar la biblioteca, buscas ejemplos, artículos o incluso documentación oficial sobre cómo hacer algo específico y te resulta difícil o imposible encontrarlo.

Después de buscar, te das cuenta de que falta algo de documentación o, lo que es peor, no hay nada de documentación. Esta situación, posiblemente te lleve a no usar la biblioteca, sin importar el trabajo que te podía haber quitado. Daniele Procida resumió mejor esta situación:

> “It doesn’t matter how good your software is, because **if the documentation is not good enough, people will not use
it** “
>
> —Daniel *[Procida](https://www.divio.com/en/blog/documentation/)*

### 2. Comentar vs Documentar Código

Antes de que podamos analizar cómo documentar su código Python, debemos distinguir la documentación de los comentarios.

En general, **comentar código** es describirlo para los desarrolladores. La audiencia principal del código fuente serán los desarrolladores que mantendrán o usarán ese código. Junto con un código bien escrito, los comentarios ayudarán a comprender mejor el código y su propósito y diseño:

> “Code tells you how; Comments tell you why.”
>
> — *[Jeff Atwood](https://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/) (también conocido como Coding Horror)*

Por otra parte, **documentar código** es describir su uso y funcionalidad a los usuarios que harán uso de este. Si bien puede ser útil en el proceso de desarrollo, la principal audiencia prevista son los usuarios. Seguidamente veremos cómo y cuándo comentar su código.

#### 2.1. Conceptos básicos durante los comentarios en el código

En python, los comentarios se crean haciendo uso del carácter `#` al comienzo de la linea. Deben ser declaraciones breves de no más de unas pocas frases. Aquí hay un ejemplo simple:

```Python
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
```

Según [PEP 8](http://pep8.org/#maximum-line-length) , los comentarios deben tener una longitud máxima de 72 caracteres. Esto es cierto aunque tus lineas de código sean mayores que los 80 caracteres recomendados. Si un comentario va a ser mayor que el límite remendado, es apropiado usar varias líneas para el comentario:

```Python
def hello_long_world():
    # A very long statement that just goes on and on and on and on and
    # never ends until after it's reached the 80 char limit
    print("Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooo World")
```

Los comentarios pueden tener [múltiples propósitos, que incluyen](https://en.wikipedia.org/wiki/Comment_(computer_programming)#Uses) :

* **Planificación y revisión:** cuando esté desarrollando nuevas partes de tu código, puede ser apropiado usar primero los comentarios como una forma de planificar o delinear esa sección de código. Recuerde eliminar estos comentarios una vez que se haya implementado y revisado/probado la funcionalidad real:

  ```Python
  # First step
  # Second step
  # Third step
  ```   

* **Descripción del código:** los comentarios se pueden usar para explicar la intención de secciones específicas del código:

  ```Python
  # Attempt a connection based on previous settings. If unsuccessful,
  # prompt user for new settings.
  ```   

* **Descripción algorítmica:** cuando se usan algoritmos, especialmente los complicados, puede ser útil explicar cómo funciona el algoritmo o cómo se implementa dentro de su código. También puede ser apropiado describir por qué se seleccionó un algoritmo específico sobre otro.

  ```Python
  # Using quick sort for performance gains
  ```   

* **Etiquetado:** para etiquetar secciones específicas de código donde se encuentran problemas conocidos o áreas de mejora. Algunos ejemplos son: `BUG`, `FIXME`y `TODO`.

  ```Python
  # TODO: Add condition for when val is None
  ```   

Los comentarios a su código deben ser breves y clarificadores. Evite el uso de comentarios largos cuando sea posible. Además, debe utilizar las siguientes cuatro reglas esenciales [sugeridas por Jeff Atwood](https://blog.codinghorror.com/when-good-comments-go-bad/) :

1. Mantenga los comentarios lo más cerca posible del código que se describe. Los comentarios que no están cerca del código al que se refieren, son frustrantes para el lector y se pasan por alto fácilmente cuando se realizan actualizaciones.
2. No utilice formatos complejos (como tablas o cifras ASCII). ya que pueden distraer y pueden ser difíciles de mantener con el tiempo.
3. No incluyas información redundante. Suponga que el lector del código tiene una comprensión básica de los principios de programación y la sintaxis del lenguaje.
4. Diseña el código para que se comente a sí mismo. La forma más fácil de entender el código es leyéndolo. Cuando diseñas el código utilizando conceptos claros (variables y metodos con nombres clarificadores) y fáciles de entender, el lector entenderá la intención del código que está leyendo, sin necesidad de comentarios.

Recuerda que los comentarios están diseñados para el lector, incluido tu mismo, para ayudarlo a comprender el propósito y el diseño del software.

#### 2.2. Comentarios a través de las sugerencias de tipo (Python 3.5+)

La sugerencia de tipo se agregó a Python 3.5 y es una forma adicional para ayudar a los lectores. Aplica la cuarta sugerencia de Jeff, ya que permite al desarrollador diseñar y explicar partes del código sin comentar. He aquí un ejemplo rápido:

```Python
def hello_name(name: str) -> str:
    return(f"Hello {name}")
```

Al examinar la sugerencia de tipo, inmediatamente entiendes que la función espera que la entrada `name`sea de tipo `str`. También entienes que la salida esperada de la función será de tipo `str`. Si bien las sugerencias de tipo ayudan a reducir los comentarios, tenga en cuenta que hacerlo también puede generar trabajo adicional al crear o actualizar la documentación de su proyecto.

### 3. Documentar su base de código de Python usando Docstrings

Ahora que hemos aprendido a comentar, profundicemos en la documentación del código de Python. Veremos como usar las cadenas de documentación `docstring` y cómo usarlas para la documentación:

#### 3.1. Cadenas de documentación `docstring`

La documentación de código Python se centra en cadenas de documentación. La propiedad `docstring` viene predefinida en los objetos y , cuando se configuran correctamente, pueden ayudar a los usuarios de este código a entender los objetos, y al desarrollador a tener documentado el proyecto. Junto con las cadenas de documentación, Python también tiene la función `help()` que imprime la cadena de documentación de los objetos en la consola. He aquí un ejemplo rápido:

```Python
>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |
 |  Create a new string object from the given object. If encoding or
 |  errors are specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 # Truncated for readability
```

¿Cómo se genera esta salida? Como en Python todo es un objeto, puede examinar el directorio del objeto usando el comando `dir()`, es decir, listar los métodos y propiedades del objeto indicado. Hagamos eso y veamos qué encontramos:

```Python
>>> dir(str)
['__add__', ..., '__doc__', ..., 'zfill'] # Truncated for readability
```

En ese volcado, hay una propiedad interesante, `__doc__`. Si profundizamos en esta propiedad, veremos lo siguiente:

```Python
>>> print(str.__doc__)
str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors are specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.
```

Como podemos observar, en la propiedad `__doc__` se almacena la documentación del objeto. Esto significa que puedes manipular directamente esa propiedad. Sin embargo, existen restricciones que no nos permiten modificarlo los objetos predeterminados:

```Python
>>> str.__doc__ = "I'm a little string doc! Short and stout; here is my input and print me for my out"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't set attributes of built-in/extension type 'str'
```

Cualquier otro objeto personalizado puede ser manipulado:

```Python
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")

say_hello.__doc__ = "A simple function that says hello... Richie style"
```

```Python
>>> help(say_hello)
Help on function say_hello in module __main__:

say_hello(name)
    A simple function that says hello... Richie style
```

Python tiene una característica más que simplifica la asignación de contenido a las docstrings. En lugar de manipular directamente la propiedad `__doc__`, la ubicación estratégica del literal debajo de la definicion del objeto establecerá automáticamente el valor de `__doc__`. Esto es lo que sucede con el mismo ejemplo que el anterior:

```Python
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
```

```Python
>>> help(say_hello)
Help on function say_hello in module __main__:

say_hello(name)
    A simple function that says hello... Richie style
```

Ya que conoces el trasfondo de las docstrings. Ahora es el momento de conocer los diferentes tipos de docstrings y qué información deben contener.

#### 3.2. Tipos de cadenas de documentos

Las convenciones de docstring se describen en [PEP 257](https://www.python.org/dev/peps/pep-0257/). Su propósito es proporcionar a sus usuarios una breve descripción general del objeto. Deben mantenerse lo suficientemente concisos para que sean fáciles de mantener, pero aún así ser lo suficientemente elaborados para que los nuevos usuarios entiendan su propósito y cómo usar el objeto documentado.

En todos los casos, las cadenas de documentación deben usar el formato de cadena de triples comillas dobles `"""`, ya sea con Docstrings que tengan varias líneas o no. Como mínimo, una cadena de documentación debe ser un resumen rápido de lo que sea que estés describiendo y debe estar contenida en una sola línea:

```Python
"""This is a quick summary line used as a description of the object."""
```

Las cadenas de documentos de varias líneas se utilizan para realizar una descripción mas elaborada del objeto más allá de un mero resumen. Todas las Docstrings compuestas por varias líneas tendrían que tener las siguientes partes:

* Una línea de resumen de una línea
* Una línea en blanco antes del resumen
* Cualquier elaboración adicional para la cadena de documentación
* Otra línea en blanco

```Python
"""This is the summary line

This is the further elaboration of the docstring. Within this section,
you can elaborate further on details as appropriate for the situation.
Notice that the summary and the elaboration is separated by a blank new
line.
"""

# Notice the blank line above. Code should continue on this line.
```

Las Docstrings deben tener la misma longitud que la recomendad para los comentarios (72 caracteres). Además, se pueden dividir en tres categorías principales:

* **Class Docstrings:** clase y métodos de clase
* **Docstrings de paquetes y módulos:** paquetes, módulos y funciones
* **Script Docstrings:** Script y funciones

##### 3.2.1. Docstrings de clase

Las Docstrings de clase se crean para la clase en sí, así como para cualquier método de clase. Se colocan inmediatamente después de la clase o el método de clase con una sangría de un nivel:

```Python
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""

        print(f'Hello {name}')
```

Las Docstrings de clase deben contener la siguiente información:

* Un breve resumen de su propósito y comportamiento.
* Cualquier método público, junto con una breve descripción.
* Cualquier propiedad de clase (atributos)
* Cualquier cosa relacionada con la [interfaz](https://realpython.com/python-interface/) para subclases.

Los parámetros del [constructor de clase](https://realpython.com/python-class-constructor/) deben documentarse dentro de la Docstring del método de clase `__init__` . Los métodos individuales deben documentarse utilizando sus Docstrings individuales, y deben contener lo siguiente:

* Una breve descripción de qué es el método y para qué se utiliza.
* Todos los argumentos (tanto obligatorios como opcionales) que se pasan.
* Etiquete cualquier argumento que se considere opcional o que tenga un valor predeterminado
* Cualquier efecto secundario que ocurra al ejecutar el método.
* Cualquier excepción que se plantee
* Cualquier restricción sobre cuándo se puede llamar al método

Tomemos un ejemplo simple de una clase de datos que representa un Animal. Esta clase contendrá algunas propiedades de clase, propiedades de instancia, un método `__init__`, y un [método de instancia](https://realpython.com/instance-class-and-static-methods-demystified/):

```Python
class Animal:
    """
    A class used to represent an Animal

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    says_str = "A {name} says {sound}"

    def __init__(self, name, sound, num_legs=4):
        """
        Parameters
        ----------
        name : str
            The name of the animal
        sound : str
            The sound the animal makes
        num_legs : int, optional
            The number of legs the animal (default is 4)
        """

        self.name = name
        self.sound = sound
        self.num_legs = num_legs

    def says(self, sound=None):
        """
        Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """

        if self.sound is None and sound is None:
            raise NotImplementedError("Silent Animals are not supported!")

        out_sound = self.sound if sound is None else sound
        print(self.says_str.format(name=self.name, sound=out_sound))
```

##### 3.2.2. Docstrings de paquetes y módulos

Las **docstring del paquete** deben colocarse en la parte superior del archivo `__init__.py` del paquete. Esta cadena de documentación debe enumerar los módulos y subpaquetes que exporta el paquete.

Las **docstring del módulo** son similares a las Docstrings de la clase, salvo que en lugar de que se documenten las clases y los métodos de clase, ahora es el módulo y las funciones que se encuentran dentro. Las Docstrings del módulo se colocan en la parte superior del archivo incluso antes de cualquier importación, y deben incluir lo siguiente:

* Una breve descripción del módulo y su propósito.
* Una lista de cualquier clase, excepción, función y cualquier otro objeto exportado por el módulo

La **docstring para una función de módulo** debe incluir los mismos elementos que un método de clase:

* Una breve descripción de qué es la función y para qué se utiliza.
* Todos los argumentos (tanto obligatorios como opcionales) que se pasan.
* Etiquete cualquier argumento que se considere opcional
* Cualquier efecto secundario que ocurra al ejecutar la función
* Cualquier excepción que se plantee
* Cualquier restricción sobre cuándo se puede llamar a la función

##### 3.2.3. Docstrings de scripts

Los scripts se consideran ejecutables de un solo archivo que se ejecutan desde la consola. Las docstrings para los scripts se colocan en la parte superior del archivo y deben documentarse lo suficientemente bien como para que los usuarios puedan tener una comprensión suficiente de cómo usar el script. Debería poder usarse para obtener un mensaje de como "usar el script", cuando el usuario pasa incorrectamente un parámetro o usa la opción `-h` al ejecutar el script.

Si usa `argparse`, puede omitir la documentación específica, suponiendo que se haya documentado correctamente dentro del parámetro `help` de la función `argparser.parser.add_argument`. Se recomienda usar la propiedad `__doc__`para el parámetro `description` del constructor `argparse.ArgumentParser`. Consulte este tutorial sobre [bibliotecas de análisis de línea de comandos](https://realpython.com/comparing-python-command-line-parsing-libraries-argparse-docopt-click/) para obtener más detalles sobre cómo usar `argparse`y otros analizadores de línea de comandos comunes.

Finalmente, cualquier importación personalizada o de terceros debe incluirse en las docstring para permitir a los usuarios saber qué paquetes pueden ser necesarios para ejecutar el script. Aquí hay un ejemplo de un script que se usa para imprimir los encabezados de las columnas de una hoja de cálculo:

```Python
"""Spreadsheet Column Printer

This script allows the user to print to the console all columns in the
spreadsheet. It is assumed that the first row of the spreadsheet is the
location of the columns.

This tool accepts comma separated value files (.csv) as well as excel
(.xls, .xlsx) files.

This script requires that `pandas` be installed within the Python
environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_spreadsheet_cols - returns the column headers of the file
    * main - the main function of the script
"""

import argparse

import pandas as pd


def get_spreadsheet_cols(file_loc, print_cols=False):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    file_loc : str
        The file location of the spreadsheet
    print_cols : bool, optional
        A flag used to print the columns to the console (default is
        False)

    Returns
    -------
    list
        a list of strings used that are the header columns
    """

    file_data = pd.read_excel(file_loc)
    col_headers = list(file_data.columns.values)

    if print_cols:
        print("\n".join(col_headers))

    return col_headers


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'input_file',
        type=str,
        help="The spreadsheet file to pring the columns of"
    )
    args = parser.parse_args()
    get_spreadsheet_cols(args.input_file, print_cols=True)


if __name__ == "__main__":
    main()
```

#### 3.3. Formatos de docstrings

Es posible que haya notado en los ejemplos vistos hasta ahora de docstrings que existían elementos comunes: `Arguments`, `Returns`y `Attributes`. Hay formatos específicos de docstrings que se pueden usar para ayudar a los analizadores de docstrings y a los usuarios a tener un formato familiar y conocido. El formato utilizado para los docstrings sigue el estilo NumPy/SciPy. Algunos de los formatos más comunes son los siguientes:


| Tipo de formato                                                                                                  | Descripción                                                                                                 | Con el apoyo de Sphynx | especificación formal |
| ------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------ |
| [docstrings de Google](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) | Forma de documentación recomendada por Google                                                               | Sí                    | No                     |
| [Texto reestructurado](http://docutils.sourceforge.net/rst.html)                                                 | Estándar de documentación oficial de Python; No es amigable para principiantes pero tiene muchas funciones | Sí                    | Sí                    |
| [docstrings NumPy/SciPy](https://numpydoc.readthedocs.io/en/latest/format.html)                                  | La combinación de NumPy de reStructuredText y Google Docstrings                                             | Sí                    | Sí                    |
| [epitexto](http://epydoc.sourceforge.net/epytext.html)                                                           | Una adaptación Python de Epydoc; Ideal para desarrolladores de Java                                         | no oficialmente        | Sí                    |

La selección del formato a seguir en la creación de las docstrings es decisión personal, pero una vez eligida una, hay que ceñirse al mismo formato en todo el documento/proyecto. Los siguientes son ejemplos de cada tipo para darle una idea de cómo se ve cada formato de documentación.

##### 3.3.1. Ejemplo de docstrings de Google

```Python
"""Gets and prints the spreadsheet's header columns

Args:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""
```

##### 3.3.2. Ejemplo de texto reestructurado

```Python
"""Gets and prints the spreadsheet's header columns

:param file_loc: The file location of the spreadsheet
:type file_loc: str
:param print_cols: A flag used to print the columns to the console
    (default is False)
:type print_cols: bool
:returns: a list of strings representing the header columns
:rtype: list
"""
```

##### 3.3.3. Ejemplo de cadenas de documentación NumPy/SciPy

```Python
"""Gets and prints the spreadsheet's header columns

Parameters
----------
file_loc : str
    The file location of the spreadsheet
print_cols : bool, optional
    A flag used to print the columns to the console (default is False)

Returns
-------
list
    a list of strings representing the header columns
"""
```

##### 3.3.4. Ejemplo de epitexto

```Python
"""Gets and prints the spreadsheet's header columns

@type file_loc: str
@param file_loc: The file location of the spreadsheet
@type print_cols: bool
@param print_cols: A flag used to print the columns to the console
    (default is False)
@rtype: list
@returns: a list of strings representing the header columns
"""
```

### 4. Documentación de sus proyectos de Python

Los proyectos de Python vienen en todo tipo de formas, tamaños y propósitos. La forma en que documente su proyecto debe adaptarse a su situación específica. Ten en cuenta quiénes van a ser los usuarios de tu proyecto y adáptate a sus necesidades. Dependiendo del tipo de proyecto, se recomiendan ciertos aspectos de la documentación. El [diseño](https://realpython.com/python-application-layouts/) general del proyecto y su documentación debe ser el siguiente:

```Python
project_root/
│
├── project/  # Project source code
├── docs/
├── README
├── HOW_TO_CONTRIBUTE
├── CODE_OF_CONDUCT
├── examples.py
```

Los proyectos se pueden subdividir generalmente en tres tipos principales: Privado, Compartido y Público/Código Abierto.

#### 4.1. Proyectos Privados

Los proyectos privados son proyectos destinados solo para uso personal y, por lo general, no se comparten con otros usuarios o desarrolladores. La documentación puede ser bastante ligera en este tipo de proyectos. La documentación recomendada para este tipo de proyectos, según sea necesario:

* **Readme.md:** un breve resumen del proyecto y su propósito. Incluya cualquier requisito especial para la instalación u operación del proyecto.
* **`examples.py`:** un archivo de secuencia de comandos de Python que brinda ejemplos simples de cómo usar el proyecto.

Recuerda, aunque los proyectos privados están destinados a ti, también eres considerado un usuario. Piense en cualquier cosa que pueda resultarle confusa en el futuro y asegúrese de capturarla en comentarios, docstring o el archivo Readme.md.

#### 4.2. Proyectos Compartidos

Los proyectos compartidos son proyectos en los que colaboras con otras personas en el desarrollo y/o uso del proyecto. El "cliente" o usuario del proyecto sigue siendo usted mismo y otros desarrolladores que utilizan el proyecto.

La documentación debe ser un poco más rigurosa de lo que debe ser para un proyecto privado, principalmente para ayudar a incorporar nuevos miembros al proyecto o alertar a los contribuyentes/usuarios de nuevos cambios en el proyecto. La documentación recomendada para estos proyectos es la siguiente:

* **Readme.md:** un breve resumen del proyecto y su propósito. Incluya cualquier requisito especial para instalar u operar el proyecto. Además, agregue cualquier cambio importante desde la versión anterior.
* **`examples.py`:** un archivo de secuencia de comandos de Python que brinda ejemplos simples de cómo usar los proyectos.
* **Cómo contribuir:** esto debe incluir cómo los nuevos contribuyentes al proyecto pueden comenzar a contribuir.

#### 4.3. Proyectos públicos y de código abierto

Los proyectos públicos y de código abierto son proyectos que están destinados a compartirse con un gran grupo de usuarios y pueden involucrar a grandes equipos de desarrollo. Estos proyectos deben otorgar una prioridad tan alta a la documentación del proyecto como al desarrollo real del proyecto en sí. La documentación recomendada para estos proyectos es las siguiente:

* **Readme.md:** un breve resumen del proyecto y su propósito. Incluya cualquier requisito especial para instalar u operar los proyectos. Además, agregue cualquier cambio importante desde la versión anterior. Finalmente, agregue enlaces a documentación adicional, informes de errores y cualquier otra información importante para el proyecto. Dan Bader ha elaborado [un excelente tutorial](https://dbader.org/blog/write-a-great-readme-for-your-github-project) sobre todo lo que debe incluirse en su archivo Léame.
* **Cómo contribuir:** esto debe incluir cómo pueden ayudar los nuevos contribuyentes al proyecto. Esto incluye el desarrollo de nuevas funciones, la solución de problemas conocidos, la adición de documentación, la adición de nuevas pruebas o la notificación de problemas.
* **Código de conducta:** define cómo deben comportarse los demás colaboradores al desarrollar o utilizar su software. Esto también establece lo que sucederá si este código no es correcto. Si está utilizando Github, se puede generar una [plantilla de Código de conducta con la redacción recomendada. ](https://help.github.com/articles/adding-a-code-of-conduct-to-your-project/)Especialmente para proyectos de código abierto, considere agregar esto.
* **Licencia:** un archivo de texto sin formato que describe la licencia que utiliza su proyecto. Especialmente para proyectos de código abierto, considere agregar esto.
* **docs:** una carpeta que contiene más documentación. La siguiente sección describe con más detalle qué debe incluirse y cómo organizar el contenido de esta carpeta.

##### 4.3.1. Las cuatro secciones principales de la carpeta `docs`

Daniele Procida dio una maravillosa [charla sobre PyCon 2017](https://www.youtube.com/watch?v=azf6yzuJt54) y una publicación de [blog posterior](https://www.divio.com/en/blog/documentation/) sobre la documentación de proyectos de Python. Menciona que todos los proyectos deben tener las siguientes cuatro secciones principales para ayudarlo a enfocar su trabajo:

* **Tutoriales**: Lecciones que llevan al lector de la mano a través de una serie de pasos para completar un proyecto (o ejercicio significativo). Orientado al aprendizaje del usuario.
* **Guías prácticas**: guías que llevan al lector a través de los pasos necesarios para resolver un problema común (Recetas orientadas a resolver problemas).
* **Referencias**: Explicaciones que aclaran e iluminan un tema en particular. Orientado a la comprensión.
* **Explicaciones**: descripciones técnicas de la maquinaria y cómo operarla (clases clave, funciones, API, etc.). Artículo de Think Encyclopedia.

La siguiente tabla muestra cómo todas estas secciones se relacionan entre sí, así como su propósito general:


|                             | Más útil cuando estamos estudiando | Más útil cuando estamos programando |
| ----------------------------- | -------------------------------------- | --------------------------------------- |
| **Paso práctico**          | *Tutoriales*                         | *Guías prácticas*                   |
| **Conocimientos teóricos** | *Explicación*                       | *Referencia*                          |

Al final, deseas asegurarte de que los usuarios tiene acceso a las respuestas a cualquier pregunta que puedan tener. Al organizar el proyecto de esta manera, podrás responder esas preguntas fácilmente y en un formato que podrán navegar rápidamente.

#### 4.4. Herramientas y recursos de documentación

Documentar su código, especialmente proyectos grandes, puede ser desalentador. Afortunadamente, existen algunas herramientas y referencias para comenzar:


| Herramienta                                               | Descripción                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Esfinge](http://www.sphinx-doc.org/en/stable/)           | Una colección de herramientas para autogenerar documentación en múltiples formatos                                                                                                                                                                                                         |
| [Epydoc](http://epydoc.sourceforge.net/)                  | Una herramienta para generar documentación de API para módulos de Python basada en sus docstrings                                                                                                                                                                          |
| [Leer los documentos](https://readthedocs.org/)           | Creación, control de versiones y alojamiento automáticos de sus documentos.                                                                                                                                                                                                    |
| [doxígeno](https://www.doxygen.nl/manual/docblocks.html) | Una herramienta para generar documentación compatible con Python, así como con muchos otros lenguajes.                                                                                                                                                                                      |
| [MkDocs](https://www.mkdocs.org/)                         | Un generador de sitios estáticos para ayudar a construir la documentación del proyecto utilizando el lenguaje Markdown. Consulta [Crea tu documentación de proyecto de Python con MkDocs](https://realpython.com/python-project-documentation-with-mkdocs/) para obtener más información. |
| [pycco](https://pycco-docs.github.io/pycco/)              | Un generador de documentación "rápido y sucio" que muestra el código y la documentación uno al lado del otro. Consulta [Tutorial sobre cómo usar pycco](https://realpython.com/generating-code-documentation-with-pycco/) .                            |
| [pydoc](https://docs.python.org/es/3/library/pydoc.html)              | El módulo pydoc genera automáticamente documentación a partir de módulos de Python. La documentación puede presentarse como páginas de texto en la consola, enviarse a un navegador web o guardarse en archivos HTML. .                            |

Junto con estas herramientas, hay algunos tutoriales, videos y artículos adicionales que pueden ser útiles cuando esté documentando su proyecto:

1. [Carol Willing - Práctica Esfinge - PyCon 2018](https://www.youtube.com/watch?v=0ROZRNZkPS8)
2. [Daniele Procida - Desarrollo basado en documentación - Lecciones del Proyecto Django - PyCon 2016](https://www.youtube.com/watch?v=bQSR1UpUdFQ)
3. [Eric Holscher - Documentando su proyecto con Sphinx & Read the Docs - PyCon 2016](https://www.youtube.com/watch?v=hM4I58TA72g)
4. [Titus Brown, Luiz Irber - Crear, construir, probar y documentar un proyecto de Python: un CÓMO práctico - PyCon 2016](https://youtu.be/SUt3wT43AeM?t=6299)
5. [reStructuredText Documentación Oficial](http://docutils.sourceforge.net/rst.html)
6. [Manual de texto reestructurado de Sphinx](http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
7. [El generador de documentación y sistema de ayuda en línea pydoc](https://docs.python.org/es/3/library/pydoc.html)

A veces, la mejor forma de aprender es imitando a los demás. Aquí hay algunos excelentes ejemplos de proyectos que usan bien la documentación:

* **Django:** [Documentos](https://docs.djangoproject.com/en/2.0/) ( [Fuente](https://github.com/django/django/tree/master/docs) )
* **Solicitudes:** [Documentos](https://requests.readthedocs.io/en/master/) ( [Fuente](https://github.com/requests/requests/tree/master/docs) )
* **Haga clic en:** [Documentos](http://click.pocoo.org/dev/) ( [Fuente](https://github.com/pallets/click/tree/master/docs) )
* **Pandas:** [Documentos](http://pandas.pydata.org/pandas-docs/stable/) ( [Fuente](https://github.com/pandas-dev/pandas/tree/master/doc) )

### 5. ¿Dónde empiezo?

La documentación de proyectos tiene una progresión sencilla:

1. Sin documentación
2. Algo de documentación
3. Documentación completa
4. buena documentacion
5. Gran documentación

Si no sabes por donde empezar con la documentación, identifica dónde se encuentra tu proyecto ahora en relación con la progresión anterior. ¿Tienes alguna documentación? Si no, entonces comience allí. Si tiene alguna documentación pero le faltan algunos de los archivos clave del proyecto, comience agregándolos.

Al final, no te desanimes ni te sientas abrumad@ por la cantidad de trabajo que se requiere para documentar el código. Una vez que comienzas a documentar el código, será más fácil continuar. 

## Fuente
* [Documentando código python](https://realpython.com/documenting-python-code/)