# UD1 - 1.2 Práctica con un lenguaje

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice 

---

## 1. Bloques de un programa


### 1.1 En Kotlin: piezas básicas

* Un programa se organiza en **paquetes** e **imports**.  
* El **punto de entrada** es la función `main`.  
* **Funciones**: bloques reutilizables con nombre.  
* **Clases** y **objetos** modelan datos y comportamiento.  
* Estructuras básicas: secuencia, decisión y repetición.  

Note: Recorre la doc de Kotlin: paquete/imports, `main` como entry point, 
funciones y clases. Conecta con la figura “Bloques en un programa” y el enlace 
oficial. Comentario didáctico: aunque hoy practicamos Python, el concepto 
de bloques es transversal a cualquier lenguaje.


### 1.2 En Python: módulos y ejecución

* Un **programa** es un **módulo** (`.py`) con código ejecutable.  
* Puede **definir** funciones, clases y variables.  
* `if __name__ == "__main__":` marca código principal.  
* **Importaciones** para reutilizar otros módulos.  
* Misma lógica: secuencia, decisión y repetición.  

Note: Explica que `__name__` vale `"__main__"` si se ejecuta directamente
y toma el nombre del módulo si se importa. Contrasta con `main` de Kotlin.


### 1.2 En Python: módulos y ejecución

```python
# file_one.py
from file_two import function_three

print(f"__name__ es: {__name__}")

def main():
    print("Cuerpo principal")

if __name__ == "__main__":
    main()          # Ejecutado si lanzas este archivo
else:
    print("Importado desde otro módulo")
```

Note: Explica que `__name__` vale `"__main__"` si se ejecuta directamente
y toma el nombre del módulo si se importa. Contrasta con `main` de Kotlin.

---

## 2. Comenzando con Python


### 2.1 Python: visión general

* **Multiparadigma**: imperativo, POO y funcional.
* **Multiplataforma**: Windows, Linux, macOS.
* **Tipado dinámico** y **fuerte**.
* **Interpretado**: ejecuta línea a línea.
* Sintaxis clara y legible.

Note: Aclara “dinámico” (el tipo se decide en ejecución) y “fuerte” (no hay
conversión implícita peligrosa). Ejemplos: concatenar str + int provoca error.


### 2.2 Intérprete interactivo

* Comandos `python` o `python3` abren el REPL.
* Permite probar **expresiones** y **sentencias**.
* `print('Hola')` muestra texto.
* `quit()` para salir.
* Útil para aprender y validar ideas.

```py
>>> 2 + 3
5
>>> print('¡Hola mundo!')
¡Hola mundo!
```

Note: Recomienda REPL para exploración, pero promueve archivos `.py` para
programas reales y control de versiones.


### 2.3 Primer programa en archivo

* Crea `suma.py` con instrucciones.
* Ejecuta: `$ python3 suma.py`.
* El intérprete lee y ejecuta el código.
* Es la forma más común de trabajar.


### 2.3 Primer programa en archivo

```py
# suma.py
suma = 2 + 3
print(suma)   # 5
```

Note: Refuerza flujo: escribir → guardar → ejecutar. Introduce la carpeta
de trabajo y buenas prácticas con rutas relativas.

---

## 3. Variables, literales y constantes


### 3.1 Valores y tipos básicos

* Literales: números, textos y booleanos.
* `int`, `float`, `str`, `bool`, `None`.
* `type(x)` revela el tipo en tiempo de ejecución.
* Ojo: `'17'` es `str`, no `int`.
* Los decimales usan **punto** (`3.2`).

```py
>>> type('Hola')  # str
>>> type(17)      # int
>>> type(3.2)     # float
```

Note: Muestra errores semánticos típicos (p. ej. `print(1,000,000)` imprime
tres enteros). Diferencia dato y representación textual del dato.


### 3.2 Variables y asignación

* Una **variable** nombra y referencia un valor.
* Asignación con `=` crea o actualiza valores.
* El tipo **va con el valor**, no con el nombre.
* `print(x)` muestra su contenido.

```py
mensaje = "Texto"
n = 17
pi = 3.14159
print(n, type(n))     # 17 <class 'int'>
```

Note: Subraya “nombre apunta a valor”. Evita hablar de “cajas” rígidas; en
Python, el nombre referencia objetos con identidad y tipo.


### 3.3 Constantes en Python

* Python **no** tiene constantes de lenguaje.
* Se usa CONVENCIÓN: nombres en MAYÚSCULAS.
* Constantes integradas: `True`, `False`, `None`.
* La inmutabilidad real requiere tipos inmutables.

Note: Comenta que existen herramientas (mypy, dataclasses congeladas,
enums) para acercarse a constantes en diseños más avanzados.

---

## 4. Operadores, expresiones y sentencias


### 4.1 Operadores y precedencia (PEMDSR)

* Paréntesis → Exponenciación → Mult/Div → Suma/Resta.
* Operadores se evalúan de **izq. a der.** con igual nivel.
* Usa paréntesis si hay dudas de orden.

```py
2 * (3 - 1)   # 4
(1 + 1) ** 3  # 8
6 + 4 / 2     # 8.0
```

Note: Pide reescritura con paréntesis para mejorar legibilidad. Señala
errores comunes por precedencia al inicio.


### 4.2 Cadenas y operadores

* `+` concatena cadenas: `"a" + "b"`.
* `*` repite cadenas: `"ha" * 3`.
* Mezclar tipos sin convertir lanza error.

```py
print('Hola ' + 'Python')   # Hola Python
print('Na' * 4)             # NaNaNaNa
```

Note: Introduce `str(x)` para convertir a cadena si es necesario.


### 4.3 Expresiones y sentencias

* **Expresión**: combina operandos y operadores y devuelve valor.
* **Sentencia**: instrucción que realiza una acción.
* Ej.: asignación, `if`, `for`, `while`, `def`.

```py
a = 2 + 3            # sentencia con expresión
b = a < 10           # expresión booleana
```

Note: Aclara que el REPL muestra el valor de una expresión, pero en archivos
necesitas `print` para ver salida.

---

## 5. Entrada de usuario y comentarios


### 5.1 `input()` y conversión

* `input()` lee texto del usuario.
* Siempre devuelve una **cadena**.
* Convierte con `int()`, `float()`.
* Maneja errores si la conversión falla.

```py
nombre = input('¿Nombre? ')
edad = int(input('¿Edad? '))
print(f"Hola, {nombre}. Tienes {edad}.")
```

Note: Advierte sobre `ValueError` en conversiones. Propón validar con
`str.isdigit()` o `try/except` (lo verán más adelante).


### 5.2 Comentarios y docstrings

* Comentario de línea con `#`.
* Multilínea: varias líneas con `#`.
* **Docstrings** (`"""..."""`) documentan funciones.
* IDEs usan docstrings para ayuda contextual.

```py
def suma(a, b):
    """Devuelve la suma de a y b."""
    return a + b
```

Note: Recomienda escribir docstrings con verbo en presente, parámetros y
valor de retorno. Conecta con buenas prácticas desde el inicio.

---

## 6. Palabras reservadas y nombres


### 6.1 Palabras reservadas

* No pueden ser nombres de variables o funciones.
* Ej.: `and`, `class`, `def`, `for`, `if`, `None`, `True`.
* Evita sombras con nombres parecidos.

Note: Pide a la clase detectar por qué `class = 3` falla. Motiva a usar
nombres expresivos y evitar conflictos con keywords.


### 6.2 Convenciones de nombres

* Identificadores: letras, dígitos, `_`; no empiezan con dígito.
* Variables y funciones: `snake_case`.
* Clases: `CamelCase`.
* Python distingue mayúsculas/minúsculas.

Note: Solicita ejemplos buenos/malos: `contador_total` vs `ct`. Recomienda
consistencia y claridad para facilitar lecturas futuras.

---

## 7. Depuración y errores comunes


### 7.1 Sintaxis y tiempo de ejecución

* `SyntaxError`: texto inválido (p. ej., espacios en nombre).
* `NameError`: usar nombre no definido.
* Sensible a mayúsculas: `latex` ≠ `LaTeX`.
* Errores semánticos: resultado incorrecto sin fallo.

```py
# NameError por variable mal escrita
principal = 100
interest = principle * 0.05
```

Note: Enseña a leer trazas de error. Distingue sintaxis, runtime y semántica.
Propón estrategia: reproducir, aislar, imprimir valores, corregir.


### 7.2 Indentación y bloques

* Python usa **indentación** para agrupar código.
* Bloque empieza al aumentar sangrado.
* Termina al volver al nivel anterior.
* Usa espacios (4) mejor que tabuladores.

```py
def suma(nums):
    total = 0
    for n in nums:
        total += n
    return total
```

Note: Pide activar en el IDE “convertir tabs a espacios” y mostrar guías de
indentación. Corrige errores por mezcla tabs/espacios.

---

## 8. Operadores en Python (resumen)


### 8.1 Lógicos y comparación

* Lógicos: `and`, `or`, `not`.
* Comparación: `>`, `>=`, `<`, `<=`, `==`, `!=`.
* Encadenables: `1 < x < 20`.
* `and` / `or` devuelven **operandos**, no `True/False`.

```py
x, y = 0, 10
x or y   # 10
x and y  # 0
```

Note: Aclara cortocircuito y retorno de operandos. Muestra impacto en
expresiones y condiciones compuestas.


### 8.2 Aritméticos y asignación

* `+ - * / // % **` (división `/` siempre `float`).
* Asignación compuesta: `+=`, `-=`, `*=`, `/=`, `//=`, `%=`.
* Usa paréntesis para priorizar.

```py
x = 7; y = 2
x / y   # 3.5
x // y  # 3
x %= y  # x = 1
```

Note: Ejercita diferencias entre `/` y `//` y el operador `%` como resto
útil en ciclos y alternancias.


### 8.3 Pertenencia, identidad y bits

* Pertenencia: `in`, `not in`.
* Identidad: `is`, `is not` (mismo **objeto**).
* Bit a bit: `| ^ & << >> ~` (entornos numéricos).

```py
lista = [1, 3, 2]
3 in lista     # True
x is y         # Mismo objeto en memoria
```

Note: Diferencia `==` (igualdad) de `is` (identidad). `is` es útil con
`None` y objetos singleton; evita usarlo para comparar cadenas o números.

---

## 9. Cierre y práctica guiada


### Resumen y mini-retos

* Flujo: intérprete, archivo, ejecución.
* Variables, tipos y conversión.
* Operadores, expresiones y sentencias.
* Entrada con `input()` y docstrings.
* Estilo: nombres y sangrado.

**Retos rápidos:**

1. Lee nombre y edad, imprime en una línea.
2. Pide 2 números y muestra suma y media.
3. Dado un entero, imprime “par”/“impar”.

Note: Propón resolver en REPL y luego pasar a archivo. Pide añadir manejo
básico de errores para la conversión de números (lo verán con `try/except`
más adelante). Cierra conectando con la siguiente unidad.

---

# Dudas
![](./assets/IS-U011-Presentacion4.png)

Note: Abre el espacio para preguntas. Anima a los alumnos a expresar dudas o compartir ideas.

---

## ¡Gracias por su atención!

![](./assets/Fin.png) <!-- .element height="50%" width="50%" -->

Note: Finaliza la presentación invitando a preguntas y aclaraciones. Refuerza que la relación entre hardware y software es fundamental para comprender cómo funciona un ordenador y que este conocimiento será la base de temas más avanzados en programación y sistemas.

---

