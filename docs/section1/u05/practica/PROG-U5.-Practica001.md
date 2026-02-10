---
title: "UD 5 - P1: Herencia, interfaces, clases abstractas"
summary: Herencia, interfaces, clases abstractas
description: Herencia, interfaces, clases abstractas
authors:
    - Eduardo Fdez
date: 2024-02-23
icon: "material/file-document-edit"
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

1. Libro: Título (`String`), Autor (`String`) y Año de Publicación (`Int`)

2. Revista: Título (`String`), Issue (`Int`), Año (`Int`)

3. DVD: Título (`String`), Director (`String`), Año (`Int`)

Estas clases almacenarán la información básica de cada ítem en la biblioteca. Usa `data class` para definir estas clases ya que son perfectas para almacenar datos sin necesidad de lógica adicional.

Parte 2: Definir `sealed class`

Para gestionar los distintos tipos de usuarios, puedes usar una `sealed class`. Esto te permitirá tener una jerarquía de clases cerrada, lo cual es útil para cuando se conocen todos los posibles subtipos.

1. Usuario: `sealed class Usuario`. Clases que heredan de Usuario:

    * Estudiante(id:`String`, nombre:`String`, carrera:`String`) 
    * Profesor(id:`String`, nombre:`String`, departamento:`String`)
    * Visitante(id:`String`, nombre:`String`)

La `sealed class Usuario` permitirá manejar operaciones específicas para cada tipo de usuario, como préstamos de libros o acceso a áreas restringidas de la biblioteca.

Ejercicio Propuesto:  

1. Definir las `data class` para Libro, Revista, y DVD.  
2. Crear una `sealed class Usuario` con las subclases Estudiante, Profesor, y Visitante. Cada subclase debe tener propiedades relevantes (como se describió anteriormente).  
3. Implementar una función que acepte un Usuario y un libro, y devuelva un mensaje indicando si el usuario puede o no tomar prestado el libro. Considerar reglas simples como que los Visitantes no pueden tomar prestados libros, o que los Profesores pueden tener préstamos por más tiempo.  

#### **Ejercicio 6:** Sistema de articulos

- Crear una clase `Articulo` con un `nombre` y un `precio`, que ambos se puedan modificar. También tendrá un `id` que se generará de forma automática mediante un contador (`totalArticulos`) y una función `generarId()`. Este `id` no podrá modificarse ni obtenerse fuera de Articulo.  

- Crear un método `promocionNavidad()` que reciba el porcentaje de rebaja y lo aplique al precio.  

- Sobreescribir el método `toString()` para que retorne el `"{nombre} - {precio con dos decilames}€ (ID: {id})"`.  

- Crear una clase que herede de `Articulo` y se llame `Ordenador`. Debe agregar a su constructor primario el `tipo`, que será de `TipoOrdenador` => `(BASICO, OFIMATICA, TODOTERRENO, GAMING)` y por defecto será `BASICO`.  

- Sobreescribe el método `promocionNavidad()` para que solo aplique la promoción si el precio es superior a 500 euros.  

- En el main crea dos artículos con precios 25 y 45 euros. También crea dos ordenadores, el primero GAMING de precio 1299.99 y el segundo un ordenador básico de 399.99 euros.  

- Crear una variable para generar una lista con ellos y recorrerla aplicándoles la promoción e imprimiendo su contenido.  

- Puedes declarar la variable de la siguiente forma:  

```
// Lista de todos los artículos
val articulos = listOf(articulo1, articulo2, ordenador1, ordenador2)
```

***Responde a las siguientes preguntas:***

1. ¿De qué tipo genera en la lista por defecto el compilador?  
2. ¿Qué está ocurriendo en este ejemplo con respecto a lo que hemos visto del polimorfismo de la herencia?  
3. ¿Qué pasaría si creáramos la lista con `listOf<Ordenador>`? ¿Y si la hiciéramos con `listOf<Any>`?  

#### **Ejercicio 7:** Sistema de Vehículos

Descripción: Crea una jerarquía de clases para representar diferentes tipos de vehículos. Cada vehículo tiene características comunes como la marca, el modelo y la capacidad de combustible, pero cada tipo tiene sus propias características y comportamientos.  

Clases a implementar:  

1. Clase Base `Vehiculo`  

    * Propiedades comunes: marca (`String`), modelo (`String`), capacidadCombustible (`Int`).
    * Método `mostrarInformacion()`, que imprime la información del vehículo.
    * Método `calcularAutonomia()`, que retorna un valor Int (Suponemos que cada litro da para 10 km).  

2. Clase Derivada `Automovil` (hereda de Vehiculo)  

    * Propiedad específica: tipo (`String`), como "sedán", "SUV", "deportivo", etc.
    * Implementa el método `calcularAutonomia()` (Suponemos que un automóvil puede hacer 100km más que el cálculo realizado en su clase base)

3. Clase Derivada `Motocicleta` (hereda de Vehiculo)  

    * Propiedad específica: cilindrada (`Int`).
    * Implementa el método `calcularAutonomia()` (Suponemos que una moto puede hacer 40km menos que el cálculo realizado en su clase base)  


**Objetivo**: Demostrar cómo se pueden crear clases derivadas de una superclase y cómo pueden extender o modificar su comportamiento.

#### **Ejercicio 8:** Persona y Estudiante

1. Clases y Objetos Básicos:  

    * Crea una clase `Persona` que tenga dos propiedades: `nombre` y `edad`. Luego, en el main crea un objeto de esta clase e imprime sus propiedades.  

2. Métodos Simples:   

    * Añade un método `cumple` a la clase `Persona` que incremente la edad de la persona en uno cada vez que se llama.
    * Sobreescribe el método `toString()` y prográmalo para que se muestre una persona con todas sus propiedades. Por ejemplo "Persona (nombre = Lucía, edad = 21)".
    * En el main ejecuta el cumple de la persona y muestra su información de dos formas: accediendo a sus propiedades y mediante el método `toString()` (recuerda que no es necesario llamar al método `toString()`, sino que se invocará automáticamente cuando necesite realizar la conversión del contenido a `String`).  

3. Encapsulamiento:  

    * Modifica la clase `Persona` para que la propiedad `edad` no se pueda modificar desde fuera (por ejemplo, con `private set`), pero siga siendo consultable.
    * La única forma de cambiar la edad será mediante el método `cumple()`.

4. Herencia:  

    * Crea una clase `Estudiante` que herede de `Persona` y añade una propiedad `carrera`. Las propiedades que deban ser sobrescritas deben incluir el modificador `open`.
    * Realiza de nuevo un override de `toString()` para completar la información de Estudiante (intenta usar el resultado del método de la clase padre y completarlo).  

5. Polimorfismo:  

    * Añade un método `actividad()` a la clase `Persona` que imprima "Lucía está realizando una actividad." y sobreescribe en `Estudiante` para que muestre un mensaje específico para estudiantes.
    * Crea en el main a una persona y un estudiante y muestra la actividad que realizan.  

6. Clases y Objetos con Validación:  

    * Modifica la clase `Persona` para que no acepte nombres vacíos y edades negativas. Utiliza un constructor primario con un valor por defecto para `edad`.
    * Prueba a crear un estudiante con una edad negativa, controlando las excepciones y mostrando el mensaje de error específico.  


**Objetivo**: Aprender a crear clases y objetos, a utilizar métodos y propiedades, a aplicar el encapsulamiento, a utilizar la herencia y el polimorfismo, y a controlar las excepciones.  

#### **Ejercicio 9:** Sistema de Gestión Académica

Descripción: Crea una jerarquía de clases para representar distintos roles en un entorno académico, como estudiantes y profesores.  

Clases a implementar:  

1. Clase Base `Persona`  

    * Propiedades comunes: nombre (`String`), edad (`Int`), id (`String`).
    * Método `mostrarRol()`, que imprime el rol de la persona (Estudiante, Profesor, etc.).  

2. Clase Derivada `Estudiante`  

    * Propiedades específicas: curso (`String`), calificacionPromedio (`Double`).
    * Implementa el método `mostrarRol()` y añade un método `mostrarCalificacion()` para imprimir la calificación promedio.  

3. Clase Derivada `Profesor`  

    * Propiedades específicas: departamento (`String`), aniosExperiencia (`Int`).
    * Implementa el método `mostrarRol()` y añade un método `mostrarExperiencia()` para imprimir los años de experiencia.  


**Objetivo**: Familiarizarse con la herencia y cómo las clases derivadas pueden tener propiedades y métodos adicionales, así como comportamientos específicos.

#### **Ejercicio 10:** Sistema de Gestión de Personal en una Empresa

Requisitos:  

1. Clase Base `Persona`:  

    * Propiedades:

        * nombre (`String`)
        * edad (`Int)`  

   * Métodos:

        * `toString()`: Devuelve una cadena con información básica sobre la persona (por ejemplo, "Nombre: Julia, Edad: 24").
        * `celebrarCumple()`: Incrementa la edad en 1 y retorna un mensaje de felicitación (por ejemplo, "Feliz cumpleaños Julia! Ahora tienes 25 años.").  

2. Clase Derivada `Empleado` (de `Persona`):  

    * Propiedades:

        * salarioBase (`Double`) (Intenta permitir también que se pueda construir un empleado con un argumento Int en esta propiedad)
        * porcentajeImpuestos (`Double`) (Intenta permitir también que se pueda construir un empleado con un argumento Int en esta propiedad) (El valor por defecto es 10.0)  
    
    * Métodos:

        * `calcularSalario()`: Devuelve el salarioBase aplicando los impuestos.
        * `toString()`: Devuelve una cadena que incluye la información de `Persona` y detalles adicionales del `Empleado` (por ejemplo, "Nombre: Julia, Edad: 24, Salario: 28273.47€" con 2 posiciones decimales para el salario).
        * `trabajar()`: Retorna un mensaje que indica que el empleado está trabajando. (por ejemplo, "Pablo está trabajando en la empresa.")  

3. Clase Derivada `Gerente` (de `Empleado`):   

    * Propiedades:

        * bonus (`Double`)
        * exentoImpuestos (`Boolean`) (Por defecto no estará exento de los impuestos)  
        * Sobrescribir el porcentajeImpuestos para que los gerentes tengan un porcentaje de impuestos siempre del 33.99%. 

    * Métodos:

        * `calcularSalario()`: Devuelve el salarioBase más el bonus aplicando los impuestos solo al salario base o sin aplicar impuestos si exentoImpuestos es `true`.
        * `toString()`: Devuelve una cadena que incluye la información de `Persona` y `Empleado`, además de detalles específicos del `Gerente`.
        * `administrar()`: Retorna un mensaje que indica que el gerente está administrando. (por ejemplo, "Ana está administrando la empresa.")  

4. Uso en la Función `main`:  

Crear una persona, un empleado y un gerente. Realizar distintas pruebas... para cada uno mostrar su información y ejecutar los métodos que tienen accesibles.
