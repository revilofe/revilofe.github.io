---
title: "UD 5 - P1: Herencia, interfaces, clases abstractas"
summary: Herencia, interfaces, clases abstractas
description: Herencia, interfaces, clases abstractas
authors:
    - Eduardo Fdez
date: 2024-02-23
icon: 
permalink: /prog/unidad5/p5.1
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - Herencia
    - interfaces
    - clases abstractas
---
## P5.1 - Ejercicios

#### **Ejercicio 1:** Sistema de Figuras Geométricas

Crea una clase abstracta `Figura` que tenga métodos abstractos para `area()` y `perimetro()`. Implementa subclases concretas como `Circulo`, `Rectangulo`, y `Triangulo`, proporcionando la implementación específica de estos métodos. La clase `Figura` podría tener propiedades comunes como el color, que se inicializarán a través del constructor.

El valor de PI lo conseguimos con Math.PI

Objetivos:

* Practicar la creación de clases abstractas y métodos abstractos.
* Entender cómo las subclases proporcionan implementaciones concretas de métodos abstractos.
* Familiarizarse con los conceptos básicos de geometría y cómo se pueden aplicar en la programación orientada a objetos.

#### **Ejercicio 2:** Sistema de Empleados y Departamentos

Diseña una clase abstracta `Empleado` con propiedades como `nombre`, `id`, y un método abstracto `calculaSalario()`. Crea clases derivadas como `EmpleadoPorHora` y `EmpleadoFijo`, que implementen el método `calculaSalario()` de diferentes maneras. Considera añadir una clase `Departamento` que tenga una lista de empleados y pueda calcular el salario total que se debe pagar a todos sus empleados.

`EmpleadoPorHora` podría implementar dos propiedades cómo horasTrabajadas al mes y tarifaPorHora para realizar el cálculo de su salario mensual. `EmpleadoFijo` podría tener a su vez dos propiedades distintas, salarioFijo y numPagas del que podríamos calcular su salario mensual.

`Departamento` podría tener una lista de empleados y dos métodos: agregarEmpleado y calculaSalarioTotal que tienen sus empleados al mes.

En el main crea una instancia de Departamento, agrega varios empleados, recorre la lista de los empleados mostrando su información "Nombre con ID-0001 tiene un salario de 28697.96 al mes." (el id siempre con 4 posiciones numéricas y el salario con 2 decimales)

¿Se te ocurre alguna restricción lógica que podríamos introducir a las propiedades?

Objetivos:

* Aprender a manejar la herencia y la implementación de métodos abstractos.
* Comprender cómo diferentes subclases pueden tener implementaciones distintas de la misma operación (polimorfismo).
* Entender cómo agrupar múltiples objetos en una colección y realizar operaciones sobre ellos.

#### **Ejercicio 3:** Sistema de Dispositivos Electrónicos

Crea tres interfaces:

* `EncendidoApagado` con métodos como `encender()` y `apagar()`.
* `DispositivoElectronico` con un método llamado `reiniciar()`.
* `Vehiculo` con dos propiedades: `motorEncendido` y `kmHora`; y los métodos `acelerar(Int)` y `frenar(Int)`.

Implementa estas interfaces en varias clases como `Telefono`, `Lavadora` y `Coche`. Cada clase debería tener su propia implementación de los métodos de las interfaces que tengan sentido que implementen, simulando el comportamiento que le obligan a desarrollar a cada una.

Un coche solo acelera y frena si tiene el motor encendido. Por defecto un objeto coche estará apagado. Si a un coche le mandamos frenar y su valor final fuera negativo le asignaremos a kmHora el valor 0.

Objetivos:

* Practicar la implementación de interfaces y entender cómo fuerzan a las clases a proporcionar implementaciones concretas de los métodos definidos.
* Comprender cómo se puede usar una interfaz para imponer un contrato que varias clases deben seguir.
* Familiarizarse con el concepto de separación de la interfaz y la implementación.

#### **Ejercicio 4:** Sistema de Notificación

Diseña una interfaz `Notificable` con un método `enviarNotificacion()`. Implementa esta interfaz en clases como `CorreoElectronico`, `MensajeTexto`, y `NotificacionPush`. Cada clase debe tener una implementación específica de `enviarNotificacion()`, simula el envío de la notificación a través del canal apropiado.

En el programa principal crea una lista de tipo `Notificable` llamada notificaciones y en ella crea un objeto de cada clase. Recorre la lista enviando una notificación con cada elemento.

Objetivos:

* Aprender a utilizar interfaces para definir un comportamiento común entre varias clases.
* Entender el beneficio de usar interfaces para permitir que diferentes clases sean tratadas de manera uniforme.
* Practicar el diseño de sistemas flexibles donde se pueden agregar nuevos tipos de notificaciones sin modificar el código que utiliza la interfaz `Notificable`.

Estos ejercicios están diseñados para reforzar la comprensión de los conceptos de clases abstractas e interfaces, y cómo se aplican en diferentes situaciones en la programación orientada a objetos.

#### **Ejercicio 5:** Sistema de Gestión de Biblioteca

Imagina que estás construyendo un sistema para una biblioteca que gestiona libros y usuarios. Este sistema deberá poder manejar distintos tipos de items en la biblioteca (libros, revistas, DVDs) y distintos tipos de usuarios (estudiante, profesor, visitante).

Parte 1: Definir `data class`

1. Libro   
      * Título:`String`  
      * Autor:`String`  
      * Año de Publicación:`Int`  

3. Revista   
      * Título:`String`  
      * Issue:`Int`  
      * Año:`Int` 
3. DVD    
      * Título:`String` 
      * Director:`String` 
      * Año:`Int` 

Estas clases almacenarán la información básica de cada ítem en la biblioteca. Usa `data class` para definir estas clases ya que son perfectas para almacenar datos sin necesidad de lógica adicional.

Parte 2: Definir `sealed class`

Para gestionar los distintos tipos de usuarios, puedes usar una `sealed class`. Esto te permitirá tener una jerarquía de clases cerrada, lo cual es útil para cuando se conocen todos los posibles subtipos.

1. Usuario
   * `sealed class Usuario`
     * Clases que heredan de Usuario:
       * Estudiante(id:`String`, nombre:`String`, carrera:`String`) 
       * Profesor(id:`String`, nombre:`String`, departamento:`String`) 
       * Visitante(id:`String`, nombre:`String`) 

La `sealed class Usuario` permitirá manejar operaciones específicas para cada tipo de usuario, como préstamos de libros o acceso a áreas restringidas de la biblioteca.

Ejercicio Propuesto

1. Definir las `data class` para Libro, Revista, y DVD.
2. Crear una `sealed class Usuario` con las subclases Estudiante, Profesor, y Visitante. Cada subclase debe tener propiedades relevantes (como se describió anteriormente).
3. Implementar una función que acepte un Usuario y un libro, y devuelva un mensaje indicando si el usuario puede o no tomar prestado el libro. Considerar reglas simples como que los Visitantes no pueden tomar prestados libros, o que los Profesores pueden tener préstamos por más tiempo.
