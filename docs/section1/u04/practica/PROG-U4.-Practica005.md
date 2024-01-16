---
title: "UD 4 - POO4: Ejercicios básicos de POO IV"
summary: Ejercicios básicos de POO IV
description: Ejercicios básicos de POO IV
authors:
    - Diego Cano
date: 2024-01-16
icon: 
permalink: /prog/unidad4/p4.4
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - POO
---
## P4.4 - Robots *(con RETO incluido)*

### **PARTE 2**

   1. Crear varios robots en una estructura de datos.

   2. Los robots serán R2D2, C3PO, DAW1B y DAM1.

   3. ***RETO***: En la clase Robot debéis realizar una modificación para que el método mover() reciba una función tipo que modifique la dirección del mismo según la info siguiente:

      * R2D2 se sigue igual, comienza en (0, 0) PositiveY cuando se instancia el objeto y realiza un giro de -90º al detenerse en cada movimiento.

      * C3PO comienza en una posición aleatoria entre -5 y 5 para x y en el eje y en 0. La dirección será PositiveX.
        Al detenerse, si está en x positiva gira 180º y si está en x negativa gira 90º.

      * DAW1B comienza en la posición x = 0, pero y es aleatoria entre -10 y 10. Su dirección inicial será aleatoria.
        La dirección que toma al detenerse será -90º si la y es positiva y 270º si la y es negativa.

      * DAM1 comienza en en una posición aleatoria entre -5 y 5 en cada eje. La dirección inicial es aleatoria.
        Debe tomar una también una dirección totalmente aleatoria al detenerse entre cada movimiento, siempre que no sea la misma en la que estaba.

   4. Si no sois capaces de realizar estos cambios en el método `mover()` pasándole una `función como parámetro`, intentad realizadlo de otra forma *(con sentido)*,
      pero que cada robot tenga el comportamiento que se indica al moverse con la dirección.

   5. El programa debe pedirme un número de movimientos por consola y ejecutar esos movimientos con todos los robots, indicando su posición y dirección final.
      Los movimientos deben ser números enteros comprendidos entre -20 y 20.
