# Actividad: El Juego de la Búsqueda del Tesoro en la Isla

**ID actividad:** pe-Isla-u1u2u3

**Agrupamiento de la actividad**: Individual

---

## Descripción:

La actividad consiste en desarrollar y mejorar un juego interactivo en Python donde los estudiantes están atrapados en una isla y deben encontrar un tesoro escondido para escapar.

Descripción del Problema:

Los estudiantes están atrapados en una isla desierta y deben encontrar un tesoro escondido para escapar.

La isla está representada como una cuadrícula donde cada celda puede contener una pista que indica
la dirección general del tesoro, nada o una trampa que le impide el paso.

Los estudiantes deben usar su conocimiento de estructuras de datos y control de flujo para interpretar
las pistas, evitar las trampas y encontrar el tesoro.

Este es un ejemplo de mapa del tesoro con dimensión 5, con el tesoro en la posicion (0,0) y el jugador en la posicion (2,2)

El programa muestra lo siguiente al  usuario:
```
?   ?   ?
? ? ? ? ?
  ?   ?      
  ?   ? ?
? ? ?   ?
Tu posición es (2, 2)
Ingresa tu movimiento (formato: 'u:arriba', 'd:abajo', 'l:izquierda', 'r:derecha', q:salir):
```

Internamente tendréis una lista anidada para contener un mapa similar al siguiente:
```
columnas  0    1    2    3    4
filas
0       ["X", " ", "!", " ", "<"]
1       ["!", "^", "!", "<", "!"]
2       [" ", "^", " ", "<", " "]
3       [" ", "<", " ", "!", "^"]
4       ["!", "<", "!", " ", "^"]
```

Se pide realizar lo siguiente:

### 1. CORRECCIÓN DE ERRORES O PROBLEMAS:

* 1: El juego no se puede `jugar()`

* 2: Acaba la función `generar_mapa()` sino no vas a poder hacer nada.

* 3: Existen errores típicos de no declarar correctamente las funciones.

* 4: Las funciones `pedir_movimiento()` y `obtener_nueva_posicion()` tienen algo raro, ya que aparentemente parece que son correctas, pero dan problemas... igual depurando puedes aclararte y corregirlo.

* 5: Corrige otros errores sintácticos que te indique el IDE para evitar problemas y pasar a las mejoras.

### 2. MEJORAS:

* 1: Mostrar los números del tablero asociados a las filas y las columnas.
     Pero las filas y columnas que empiecen en el número 1 visualmente.
```
   1 2 3 4 5
  -----------
1 |? ? ? ? ?|
2 |?     ? ?|
3 |?       ?|
4 |? ? ? ? ?|
5 |  ? ? ? ?|
  -----------
```

* 2: Mostrar la posición del jugador con respecto a la numeración visual del mapa.

`Tu posición es (3, 3)  #aunque internamente esté en la posición (2, 2)`

* 3: Evitar que en la posición inicial del jugador en el mapa se genere una pista o una trampa.

* 4: Limpiar la consola cada vez que realices un movimiento y dejar el mensaje de la pista o trampa en la zona superior de la consola, justo arriba del mapa. Pero cuando se encuentra el tesoro no debe borrar la consola y el mensaje aparecerá abajo y finalizará el juego.

* 5 (DIFÍCIL): Mostrar un símbolo para el jugador. Para ello, una solución es cambiar el código de la función `imprimir_mapa_oculto()`


## Objetivo:

* Aplicar conocimientos de estructuras de datos y control de flujo en un contexto práctico.
* Desarrollar habilidades de depuración y resolución de problemas en programación.
* Fomentar la creatividad y la innovación en el diseño de algoritmos y soluciones.

## Trabajo a realizar:

1. Corregir errores y problemas en el código del juego proporcionado.
2. Implementar mejoras sugeridas para el juego.

Aclaración: 
- La realización de test te puede ayudar a detectar errores y problemas. No es obligatorio, pero si recomendable.
- No se puede modificar el código de las funciones proporcionadas para que hagan algo distinto, pero si se puede añadir código en las funciones proporcionadas siempre que el funcionamiento sea el mismo.

## Recursos

* Apuntes dados en clase.
* Recursos y ejemplos vistos en clase.

## Permitido y Prohibido

* Permitido el uso de apuntes, ejemplos y recursos vistos en clase.
* Prohibido el uso de cualquier otro recurso: apuntes de compañeros, ayuda de compañeros, copilot, chatgpt, etc.

El uso de cualquier recurso prohibido supondrá la calificación de 0 en la actividad.

## Evaluación y calificación

La prueba especifica (50%) consistirá de dos pruebas, la práctica que consisten en la realización de un programa en Python que cumpla con los requisitos especificados en el enunciado, y la teórica que consiste en un cuestionario de preguntas sobre los contenidos de la unidad.
- La parte práctica, este ejercicio, se evaluará con una calificación de 0 a 10 puntos. (80%)
- La parte teórica, que se realizará otro dia, y se evaluará con una calificación de 0 a 10 puntos. (20%)

Adicionalmente se realizará un práctica (40%) que se entregará esta semana. Esta práctica se evaluará con una calificación de 0 a 10 puntos.

### RA y CE evaluados:

* RA1: Conoce la estructura de un programa informático identificando y relacionando los elementos propios del lenguaje de programación utilizado.
* RA3: Escribe y depura código analizando y utilizando las estructuras de control del lenguaje.
* RA6: Escribe programas que manipulen información seleccionando y utilizando tipos avanzados de datos. (no todos los criterios de evaluación).

### Conlleva 
presentación: SI, se evaluará con el profesor.

### Rubrica:

* El programa funciona adecuadamente.
* Las mejoras solicitadas se han implementado adecuadamente
* Trabajo con Variables, Constantes y Tipos de Datos y sus operadores. 
* Comentarios y Documentación en el Código 
* Herramientas de Desarrollo y Entornos Integrados
* Identificación y uso de las Estructuras de Control y Flujo del Programa
* Manejo de Errores y Excepciones
* Desarrollo, Prueba y Depuración de Programas
* Trabajo con Librerías y Estructuras de Datos Avanzadas (Listas, Tuplas, Diccionarios, Conjuntos, etc.)


## Entrega

> **La entrega tiene que cumplir las condiciones de entrega para poder ser calificada. En caso de no cumplirlas podría calificarse como no entregada.**

* **Conlleva la entrega de URL a repositorio:** El proyecto se entregará en un repositorio GitHub, trabajando por proyectos y dejando constancia de las acciones realizadas.
