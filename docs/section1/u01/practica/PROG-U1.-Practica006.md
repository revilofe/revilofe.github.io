---
title: "UD 1 - P6: PU con Pytest"
summary: PU con Pytest
description: Mis primeras pruebas unitarias
authors:
    - Diego Cano
date: 2023-09-29
icon: 
permalink: /prog/unidad1/p1.6
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

## P1.6 - Mis primeras pruebas unitarias

### 1. Introducción

Para realizar pruebas unitarias de forma básica debemos conocer qué es y para qué se usan las funciones en los lenguajes de programación.

### 2. Funciones

Una función te permite definir un bloque de código reutilizable que se puede ejecutar muchas veces dentro de tu programa.

Las funciones en Python son componentes importantes en la programación que cuentan con una estructura que consta de dos principios.

- Principio de reutilización: puedes reutilizar una función varias veces y en distintos programas.
- Principio de modularización: te permite segmentar programas complejos con módulos más simples para depurar y programar con mayor facilidad.
	
En Python, una definición de función tiene las siguientes características:

1. La palabra clave def.
2. Un nombre de función
3. Paréntesis ’()’, y dentro de los paréntesis los parámetros de entrada (opcionales).
4. Dos puntos ’:’
5. Algún bloque de código para ejecutar
6. Una sentencia de retorno (opcional)
	
Un ejemplo, que además vamos a usar en nuestra práctica es el siguiente:

```
def suma(num1, num2):
    return num1 + num2
```
		
En el código podemos llamarla las veces que nosotros necesitemos:

```
print(suma(3, 2))
print("La suma de", 3, "+", 2, "es", suma(3, 2))
tot = 100 + suma(25, 40)
```

### 3. Pruebas unitarias

Las pruebas automáticas son consideradas una herramienta y una metodología indispensable para producir software de calidad.

Un conjunto de pruebas, es código que realiza pruebas a nuestro código. Las pruebas unitarias nos permiten verificar que nuestro código funciona como se espera.

Las pruebas unitarias son un conjunto de casos de prueba diseñados para verificar que cada “unidad” o componente de nuestro código funciona como se espera.

Cada prueba unitaria se ejecuta en un entorno aislado, lo que significa que no afecta a otras partes del código y viceversa.

Además de ejecutarse en la máquina del desarrollador, en entornos de trabajo profesional, estas se ejecutan en forma continua, por ejemplo cada hora o cada commit del código. Esta ejecución continua se realiza mediante sistemas automatizados como Jenkins. Debido a esto, agregar una pieza de código de pruebas implica que esta se probará una y otra vez cada que una funcionalidad sea agregada o un error sea corregido.

#### 3.1. Pytest

Pytest es un framework con muchas funcionalidades, desde pruebas pequeñas hasta pruebas de gran escala como pruebas funcionales de aplicaciones y librerías. Ofrece la recolección automática de los tests, aserciones simples, soporte para fixtures, debugeo y mucho más…

#### 3.2. Assert

La palabra assert en Python se refiere a un enunciado que verifica ciertas suposiciones sobre nuestro código. Si la suposición no es cierta, la afirmación falla y se genera una excepción.

Por ejemplo, si suponemos que una variable es mayor que cero, podemos usar assert para verificar esa suposición:

```
def funcion_ejemplo(x):
    assert x > 0, "x no es mayor que cero"
    return x * 2
```
	
En este ejemplo, si x es igual a cero o menor que cero, se generará una excepción AssertionError con el mensaje “x no es mayor que cero”.

### 4. Creando el primer test

1. Para empezar, vamos a partir de la práctica 5, donde creamos un entorno virtual e instalamos pytest. Vamos a seguir los siguientes pasos para realizar nuestro primer test y ejecutarlo desde el terminal.

2. Abrir en Visual Studio Code nuestra carpeta de trabajo, vamos a crear una carpeta en **~/Documents/practica6**, activar el entorno virtual y comprobar que está instalado correctamente pytest.

3. Lo habitual es crear un directorio llamado `tests` que contenga los ficheros de pruebas y `src` para incluir los programas o módulos. Si hacéis esto, incluid en todas las carpetas del proyecto el fichero `__init__.py` vacío *(si lo hacéis desde el terminal: touch __init__.py)*.

    Por ejemplo, si tenemos la siguiente estructura de nuestra carpeta o proyecto `practica6`:
     
     ```
        practica6
         --__init__.py
         |
         --scr
         |   __init__.py
         |   main.py
         --tests
         |   __init__.py
         |   test_main.py
    ```    

4. Crear una carpeta que se llame `src`. En ella crearemos un nuevo fichero `main.py` con el siguiente contenido:

    ```
    def suma(num1, num2):
        return num1 + num2


    def main():
        print("La suma de 3 + 2 es {}".format(suma(3, 2)))
    
        # Otras formas de hacer lo mismo:
        print("La suma de", 3, "+", 2, "es", suma(3, 2))

        print("La suma de " + str(3) + " + " + str(2) + " es " + str(suma(3, 2)))

        res = "La suma de "
        res += str(3)
        res += " + " + str(2)
        res += " es " + str(suma(3, 2))
        print(res)

        print(f"La suma de 3 + 2 es {suma(3, 2)}")


    if __name__ == "__main__":
        main()
    
    ```
    
    Si os fijáis en el código, no es más que una función que voy a llamar en mi función principal en varias ocasiones.

5. A continuación, nos creamos la carpeta `tests` y dentro de ella un fichero con el nombre `test_main.py` *(Pytest va a reconocer por defecto todos los programas que comiencen por test_ cómo pruebas unitarias que debe realizar)*. El contenido será el siguiente:

    ```
      from src.main import suma
    
      def test_suma():
        assert suma(1, 1) == 2
        assert suma(0, 0) == 0
        assert suma(100, -100) == 0
    ```
   
   - Para empezar, siempre debemos importar la función que deseamos probar del módulo dónde está definida.
   - Todas las pruebas serán también una función con el nombre `test_nombreFunciónAProbar`.
   - Si realizamos varias funciones para probar una misma función es recomendable añadir un texto explicativo de la prueba.
   - `assert` verifica que la expresión de la derecha es verdadera (true), sino generará una excepción.
   - Pytest capturará la excepción si se produce y la gestionará para mostrarnos los resultados.

6. Vamos a ejecutar las pruebas unitarias desde la terminal:

    ```
    pytest
    ```
    
    El comando `pytest` nos muestra si las pruebas pasaron o no. Si queremos una información un poco más detallada usamos el parámetro `-v`:
    
    ```
    pytest -v
    ```

7. Se pueden usar las marcas para realizar múltiples pruebas sobre un determinado método *(marca parametrize)*. En el mismo fichero `test_main.py` añadimos otra función:

    ```
    import pytest
    from src.main import suma

    def test_suma():
        assert suma(1, 1) == 2
        assert suma(0, 0) == 0
        assert suma(100, -100) == 0
    
    @pytest.mark.parametrize(
        "input_n1, input_n2, expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (100, -100, 0),
            (-15, -1, -16),
            (-3, 8, 5),
            (9, suma(-1, -2), 6)
        ]
    )
    def test_suma_params(input_n1, input_n2, expected):
        assert suma(input_n1, input_n2) == expected
    ```
    Necesitamos importar las librerías de pytest en nuestro fichero de pruebas con `import pytest`.

8. Al volver a realizar el test obtendremos un resultado por cada tupla de parámetros probados:

    ```
    pytest -v
    ```

9. **Obliguemos a que se produzca un error**, por ejemplo modificando uno de los parámetros expected `(0, 0, 1)` y observemos lo que nos muestra pytest.

10. Pruébalo y vuelve a ejecutar los tests unitarios.

### 5. Crea tu el test

Desarrolla una función en `compara_numeros.py` que reciba dos números y retorne el mayor número de los dos o 0 si son iguales. Realiza las pruebas unitarias y ejecútalas con pytest.

Entrega lo siguiente:   
* Los ficheros `compara_numeros.py` y `test_compara_numeros.py`      
* Un pantallazo donde se muestre la vista del Explorador (View -> Explorer) con las carpetas y ficheros del proyecto.   
* Un pantallazo del terminal con las pruebas unitarias detalladas realizadas con éxito.   
* Fuerza un error en tu código, no en los tests, y muestra un pantallazo de tus pruebas unitarias realizadas de nuevo.

### 6. Configura las pruebas en el IDE

Ahora vamos a configurar y realizar las pruebas unitarias desde el IDE, sin necesidad de usar los comandos. Para ello, sigue los 6 pasos de la siguiente documentación para configurar y ejecutar las pruebas unitarias:  

[How to run pytest in VSCode](https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/)  

### 7. Crea tu el test usando el IDE 

Desarrolla una función en `calcula_factorial.py` que reciba un número y retorne el factorial del mismo. Crea también las pruebas unitarias.

Debe cumplir que el número de entrada debe ser igual o superior a 0 y menor o igual a 10 (si no es correcto, retornará -1).

   ```
   > El factorial de 0 es 1. El factorial de un número entero se define como el producto de todos los números enteros positivos desde el 1 hasta n. Por ejemplo, el factorial de 3 es 6 (3! = 3 x 2 x 1 = 6).
   ```

Entrega lo siguiente:   
* Los ficheros calcula_factorial.py y test_calcula_factorial.py   
* Un pantallazo de la vista de Testing.  
* Fuerza un error en tu código, no en los tests, y muestra un pantallazo de tus pruebas unitarias realizadas de nuevo en la vista de Testing de Visual Studio Code.

## Fuentes:

  * [Guía de funciones de Python con ejemplos](https://www.freecodecamp.org/espanol/news/guia-de-funciones-de-python-con-ejemplos/)
  * [Qué son las funciones en Python](https://keepcoding.io/blog/que-son-las-funciones-en-python/)
  * [Full pytest documentation](https://docs.pytest.org/en/7.1.x/contents.html)
  * [Asegura la calidad de tu código](https://apuntes.de/python/uso-de-assert-y-pruebas-unitarias-en-python-asegura-la-calidad-de-tu-codigo/)
  * [Pruebas unitarias con pytest](https://old.tacosdedatos.com/pruebas-unitarias-pytest)
  * [Introducción a pytest](https://www.clubdetecnologia.net/cursos/pruebas-con-python/introduccion-a-pytest/)
  * [The Import System](https://docs.python.org/3/reference/import.html)
