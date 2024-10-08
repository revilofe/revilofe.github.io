---
title: "UD 1 - 1.4 Realización de pruebas con Pytest"
description: Realización de pruebas con Pytest
summary: description: Realización de pruebas con Pytest
authors:
    - Eduardo Fdez
date: 2023-09-30
icon: 
permalink: /prog/unidad1/1.4
categories:
    - PROG
tags:
    - Software
    - test
    - pytest
---

## 1.4 Realización de pruebas con Pytest

En este apartado vamos a ver como realizar pruebas con **pytest**. Para ello, vamos a crear un entorno virtual y vamos a instalar pytest.

### 1. Instalación/Actualización de pip

Antes de realizar, nada, vamos a actualizar la herramienta que nos va a permitir instalar los comandos que necesitamos. Como no viene por defecto, hay que instalarlo. Antes de instalarlo, actualizamos pip.

> **pip** es un [sistema de gestión de paquetes](https://es.wikipedia.org/wiki/Sistema_de_gesti%C3%B3n_de_paquetes) utilizado para instalar y administrar paquetes de software escritos en [Python](https://es.wikipedia.org/wiki/Python). Muchos paquetes pueden ser encontrados en el [Python Package Index](https://es.wikipedia.org/wiki/Python_Package_Index) ([PyPI](https://es.wikipedia.org/wiki/PyPI)). Python 2.7.9 y posteriores (en la serie Python2), Python 3.4 y posteriores incluyen pip (pip3 para Python3) por defecto.
>

El comando para instalar `pip`

```bash
> sudo apt-get install pip

```

El comando para actualizar `pip`

```bash
> sudo python3 -m pip install --upgrade pip
```

### 2. Crear un entorno virtual

Las aplicaciones en Python usualmente hacen uso de paquetes y módulos que no forman parte de la librería estándar. Las aplicaciones a veces necesitan una versión específica de una librería, debido a que dicha aplicación requiere que un bug particular haya sido solucionado o bien la aplicación ha sido escrita usando una versión obsoleta de la interfaz de la librería.

Esto significa que tal vez no sea posible para una instalación de Python cumplir los requerimientos de todas las aplicaciones. Si la aplicación A necesita la versión 1.0 de un módulo particular y la aplicación B necesita la versión 2.0, entonces los requerimientos entran en conflicto e instalar la versión 1.0 o 2.0 dejará una de las aplicaciones sin funcionar.

La solución a este problema es crear un entorno virtual, un directorio que contiene una instalación de Python de una versión en particular, además de unos cuantos paquetes adicionales.

> **Virtualenv** es una herramienta usada para crear un entorno Python aislado. Este entorno tiene sus propios directorios de instalación que no comparten bibliotecas con otros entornos virtualenv o las bibliotecas instaladas globalmente en el servidor.
Virtualenv es la manera más fácil recomendada para configurar un ambiente personalizado Python.
>

A contiuación instalamos el modulo **virtualenv**, haciendo uso de pip.

```bash
> sudo pip install virtualenv
```

Si tienes problemas con la instalación, puedes forzar la instalación con el siguiente comando:

```bash
> sudo pip install virtualenv --break-system-packages 
```

Una vez instalado el módulo, podemos usarlo para crear un entorno llamado **env** en la carpeta base de nuestro proyecto. 

Accedemos a la carpeta de nuestro proyecto

```bash
> cd /ruta/a/mi/proyecto
```

ejecutamos el comando para crear el entorno virtual **env**:

```bash
> python -m virtualenv env
```

La creación del entorno, creará una carpeta con el mismo nombre: `./env`

Una vez creado, pasamos a activar el entorno recien creado: env

```bash
> . ./env/bin/activate
```

Eliminando la carpeta `env` eliminaremos el entorno. Además, si queremos desactivar el entorno, podemos hacerlo con el comando:

```bash
> deactivate
```

Una vez hemos creado el entorno, y tenemos lo hemos activado, podemos listar los módulos que tenemos disponibles en el entorno:

```bash
> pip list
```

Adicionalmente, si en un momento determinado necesitamos recoger los módulos instalados, podemos captura los requerimientos a un archivo.

```bash
> pip freeze > requirements.txt
```

Y posteriormente, reinstalar esos mismos módulos:

```bash
> pip install -r requirements.txt
```

La estructura creada en el nuevo entorno, tiene por defecto los directorios `bin` (ejecutables) y `lib` (paquetes instalados).

```bash
> ls env

env/
│
├──/bin
└──/lib
```

Para continuar creando la estructura de nuestro proyecto, vamos a crear los directorios necesarios para almacenar el código fuente y los tests.

En el raiz de nuestro proyecto `/ruta/a/mi/proyecto`, crearemos los directorios **src** para almacenar el código fuente y **test** para almacenar los tests. Además, crearemos un archivo **`__init__.py`** vacío en cada uno de estos dos directorios.

> El archivo **__init__.py** es utilizado para inicializar paquetes de Python, es decir, le indica al intérprete de Python que el directorio package contiene un módulo, y que debe tratarlo como tal (es decir, hacer que sea posible importar los archivos como parte del módulo).
En general no es necesario poner nada en el archivo `__init__.py`, pero es muy común usarlo para realizar configuraciones e importar cualquier objeto necesario de nuestra librería.
>
  
La estructura final que tiene que tener es la siguiente:

```bash
proyecto/              # Carpeta raíz del proyecto
│
├── env/           # Carpeta del entorno virtual (no incluida en Git)
├── src/               # Código fuente del proyecto
│   ├── __init__.py
│   └── main.py
├── tests/             # Pruebas unitarias
│   └── test_suma.py
├── .gitignore         # Archivo para excluir el entorno virtual y otros archivos innecesarios
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Información del proyecto
```

Agrega las siguientes líneas a `.gitignore` para ignorar la carpeta del entorno virtual y otros archivos temporales:

```
# Ignorar entornos virtuales
env/

# Archivos de configuración de Python
*.pyc
__pycache__/

# Archivos de configuración de IDEs y sistemas operativos
.vscode/
.idea/
.DS_Store
```

### 3. Pruebas con pytest

> **Pytest** es un marco de pruebas en Python que se utiliza para escribir y ejecutar pruebas de manera sencilla y eficiente. Proporciona una forma fácil de definir casos de prueba y realizar aserciones sobre el comportamiento esperado de las funciones o módulos que se están probando.
>

Para realizar un test sencillo con pytest, sigue los siguientes pasos:

1. Asegúrate de tener pytest instalado en tu entorno virtual. Puedes instalarlo utilizando el siguiente comando.
   Despues de instalar pytest, si listamos de nuevo los módulos del entorno, veremos que los modulos instalados se habŕan incrementado.

    ```bash
    > pip install pytest
    ```

2. Suponiendo que tienes una función llamada suma en el archivo `main.py` en el directorio src de tu proyecto. Aquí tienes un ejemplo de una función `suma` en Python, que toma dos argumentos `a` y `b` y devuelve la suma de los dos números.

    ```python
    def suma(a, b):
        return a + b
    ```

3. Crea un archivo de prueba en el directorio "test" de tu proyecto. Por ejemplo, podrías llamarlo `test_suma.py`.
4. En este archivo de prueba, importa pytest y la función que deseas probar desde tu código fuente. Por ejemplo, podrías importar la función `suma` desde el módulo `main.py` en el directorio `src`.

    ```python
    import pytest
    from src.main import suma
    
    ```

5. Define una función de prueba utilizando el decorador `@pytest.mark.parametrize`. Esta función de prueba `test_suma_params` debe tomar los parámetros de entrada que deseas probar y el resultado esperado. Por ejemplo:

    ```python
    @pytest.mark.parametrize(
        "input_x, input_y, expected",
        [
            (0, 0, 0),
            (-1, 1, 0),
            (5, 5, 10)
        ]
    )
    
    def test_suma_params(input_x, input_y, expected):
        assert suma(input_x, input_y) == expected
    
    ```
  
    En este ejemplo, estamos probando la función "suma" con diferentes valores de entrada y comprobando si el resultado es igual al valor esperado.

6. Desde el directorio base de tu proyecto, ejecuta los tests utilizando el siguiente comando en la terminal:

    ```bash
    > pytest ./test
    
    ```
    
    Esto ejecutará todos los archivos de prueba con el prefijo "test_" en el nombre y mostrará los resultados de las pruebas.

## Fuentes:

- [Entornos virutales y paquetes.](https://docs.python.org/es/3/tutorial/venv.html)
- [Instalar y usar virtualenv con Python 3](https://www.notion.so/Qu-es-el-Cyber-Kill-Chain-1-600ccf7d6ee24cb2ae8601e10b6e9348?pvs=21)
- [Módulos en python](https://docs.python.org/es/3/tutorial/modules.html)
- [Tutorial de pytest](https://misovirtual.virtual.uniandes.edu.co/codelabs/tutorial-PyTest/index.html#0)
