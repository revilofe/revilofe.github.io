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
## P4.3 - Robots

### **PARTE 1**

   1. Crear una versión del programa realizado en la tarea ¿Dónde está R2D2?, pero ORIENTADO A OBJETOS.
      
   3. La clase Robot debe tener 4 propiedades: nombre, posX, posY y dir. También tendrá un comportamiento por medio de 3 métodos: mover(), mostrarPosicion() y obtenerDireccion().
      
   5. El método mover() debe recibir un array de elementos enteros y no retornará nada, ya que los cambios quedarán almacenados en las propiedades del mismo.
      
   7. El método obtenerDireccion() no recibe parámetros y retorna una cadena de caracteres con la dirección PositiveX, NegativeX, PositiveY o NegativeY.
      
   9. El método mostrarPosicion() debe mostrar por consola la posición y dirección. Ejemplo: "R2D2 está en (10, -5) PositiveX".
       
   11. Un objeto de la clase Robot debe inicializarse siempre en la posición (0, 0) y la dirección eje Y positivo (hacia arriba) cuando se instancia.
       
   13. En este programa, vamos a realizar los mismos movimientos, pero el robot comenzará cada movimiento en la posición final después de realizar el movimiento anterior.
       
   15. En el main debes crear un objeto de Robot (o una variable de tipo Robot) con el nombre "R2D2". El nombre de la variable que utilices para crearlo puede ser robot1.
       
   17. Cread los movimientos en un array de arrays y recorrerlos para realizar en cada iteración los movimientos del robot y mostrar la posición del mismo al finalizar cada uno. En cada iteración del bucle llamaremos a los métodos mover() y mostrarPosicion().

   18. Un ejemplo de una estructura que podéis utilizar para los movimientos sería la siguiente:

      ```
      [
          [1, -5, 0, -9],
          [3, 3, 5, 6, 1, 0, 0, -7],
          [2, 1, 0, -1, 1, 1, -4],
          [],
          [3, 5]
      ]
      ```
      
