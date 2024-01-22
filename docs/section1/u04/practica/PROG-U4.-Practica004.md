---
title: "UD 4 - POO4: Ejercicios básicos de POO III"
summary: Ejercicios básicos de POO III
description: Ejercicios básicos de POO III
authors:
    - Diego Cano
date: 2024-01-16
icon: 
permalink: /prog/unidad4/p4.3
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - POO
---
## P4.4 - Robots

### Descripción ¿Dónde está R2D2?
Calcula dónde estará un robot (sus coordenadas finales) que se encuentra en una cuadrícula representada por los ejes "x" e "y".

- El robot comienza en la coordenada (0, 0).  
- Para indicarle que se mueva, le enviamos un array formado por enteros (positivos o negativos) que indican la secuencia de pasos a dar.
Por ejemplo: `[10, 5, -2]` indica que primero se mueve `10` pasos, se detiene, luego `5`, se detiene, y finalmente `2`. El resultado en este caso sería `(x: -5, y: 12)`   
- Si el número de pasos es negativo, se desplazaría en sentido contrario al que está mirando.   
- Los primeros pasos los hace en el eje "y". Interpretamos que está mirando hacia la parte positiva del eje "y".   
- El robot tiene un fallo en su programación: cada vez que finaliza una secuencia de pasos gira 90 grados en el sentido contrario a las agujas del reloj.

No te olvides lo aprendido en las primeras unidades.
Estructura condicionales, repetitivas, comentarios, etc.

Tras los siguientes movimientos:
```
[10, 5, -2]
[0, 0, 0]
[]
[-10, -5, 2]
[-10, -5, 2, 4, -8]
```
Las salidas son estas:
```
x: -5, y: 12, direction: POSITIVEX
x: 0, y: 0, direction: POSITIVEX
x: 0, y: 0, direction: POSITIVEY
x: 5, y: -12, direction: POSITIVEX
x: 9, y: -20, direction: NEGATIVEX
```
### **PARTE 1**

   1. Crear una versión del programa ¿Dónde está R2D2?, pero ORIENTADO A OBJETOS.
      
   2. La clase Robot debe tener 4 propiedades: `nombre`, `posX`, `posY` y `direccion`. También tendrá un comportamiento por medio de 3 métodos: `mover()`, `obtenerPosicion()` y `obtenerDireccion()`.
      
   3. El método `mover()` debe recibir un array de elementos enteros y no retornará nada, ya que los cambios quedarán almacenados en las propiedades del mismo.
      
   4. El método `obtenerDireccion()` no recibe parámetros y retorna una cadena de caracteres con la dirección `PositiveX`, `NegativeX`, `PositiveY` o `NegativeY`. ***(Posible mejora con `enum class` [Enum classes](https://kotlinlang.org/docs/enum-classes.html))***
      
   5. El método `obtenerPosicion()` debe devolver la posición. Ejemplo: `(10, -5)`.

   6. Describe la posición actual del robot en el método `toString()`. (Pulsa Ctrl+o) Ejemplo: `R2D2 está en (10, -5) PositiveX`
       
   7. Un objeto de la clase Robot debe inicializarse siempre en la posición `(0, 0)` y la dirección eje Y positivo (hacia arriba) cuando se instancia. En esta versión ya no va a moverse siempre desde la posición (0,0), sino que lo hará desde la última posición y dirección dónde se quedó al realizar su último movimiento.
       
   8. En este programa, vamos a realizar los mismos movimientos, pero el robot comenzará cada movimiento en la posición final después de realizar el movimiento anterior.
       
   9. En el main debes crear un objeto de Robot (o una variable de tipo Robot) con el nombre `R2D2`. El nombre de la variable que utilices para crearlo puede ser `robot1`.

   10. La clase Robot debe obligar a introducir un nombre que no esté vacío.
       
   11. Cread los movimientos en un array de arrays y recorrerlos para realizar en cada iteración los movimientos del robot y mostrar la posición del mismo al finalizar cada uno. En cada iteración del bucle llamaremos a los métodos `mover()` y `mostrarPosicion()`.

Un ejemplo de una estructura que podéis utilizar para los movimientos sería la siguiente:

   ```
   [
      [1, -5, 0, -9],
      [3, 3, 5, 6, 1, 0, 0, -7],
      [2, 1, 0, -1, 1, 1, -4],
      [],
      [3, 5]
   ]
   ```
