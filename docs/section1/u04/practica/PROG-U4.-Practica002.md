---
title: "UD 4 - POO2: Ejercicios básicos de POO I"
summary: Ejercicios básicos de POO I
description: Ejercicios básicos de POO I
authors:
    - Diego Cano
date: 2024-01-16
icon: 
permalink: /prog/unidad4/p4.1
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - POO
    - Kotlin
---
## P4.2 - Ejercicios básicos de POO 1 al 5

### **Ejercicio 4.1**

   1. Crear una clase `Rectángulo`, con atributos `base` y `altura`. La clase debe disponer del constructor y los métodos para calcular el `area` y el `perimetro`. Los atributos no se podrán modificar, aunque si consultar. Por último, tendrán que ser mayor que 0.

   2. Opcionalmente se puede crear el método `toString()` para mostrar información sobre el rectángulo: `override fun toString() = ""`. (Pulsa Ctrl+o)

   3. En el programa principal, crear varios rectángulos. Mostarlos y mostrar por pantalla sus áreas y perímetros.

### **Ejercicio 4.2**

   1. Crear una clase `Persona` que tenga `nombre`, `peso` *(en kg con decimales)*, `altura` *(en metros con decimales)* y su `imc`.
   
   2. Crear un ***constructor primario*** con todos los atributos, excepto nombre e imc. Este último atributo se calcula en función del peso y la altura. Por tanto no se debe poder modificar, pero si consultar.  
   
   3. Crear un ***constructor secundario*** que también incluya el nombre de la persona cómo parámetro.

   4. Implementa el método `toString`, representación del objeto en forma de `String`:  `override fun toString() = ""`. (Pulsa Ctrl+o)

   5. En el `main()` a) crear 3 personas diferentes (la primera sin nombre) utilizando el constructor primario y secundario y b) mostrarlas por consola. A continuación, realizar lo siguiente:   
   
      * Sobre la persona 1: a) modificar su nombre y para ello debes solicitarlo al usuario por consola. No puede ser nulo o vacio. b) Mostrar por consola sólo el nombre, peso y altura.
      * Sobre la persona 3: a) Mostrar el peso, altura y imc. b) Modificar la altura, por ejemplo a `1.80` c) Mostrar el peso, altura y imc.
      * Sobre la persona 2; a) Modificar la altura para que tenga el mismo valor que la persona 3. b) Mostrar la persona 2 y persona 3. c) Comparar si las dos personas son iguales, y mostrar el resultado. d) Implementa el método `equals():boolean` (Pulsa Ctrl+o). e) Ejecutar la comparación.
      

### **Ejercicio 4.3**

   1. Actualizar el ejercicio 4.2 para añadir a la clase `Persona` el siguiente comportamiento:

      * Debe retornar un saludo con su nombre... `saludar():String`
      * Debe retornar si altura por encima de la media (solo si altura >= 1.75)... `alturaEncimaMedia():Boolean`
      * Debe retornar si peso por encima de la media (solo si peso >= 70)... `pesoEncimaMedia():Boolean`
      * Sería conveniente añadir también un método `obtenerDescImc()` para usar en `obtenerDesc()`, que implemente el retorno de la descripción del rango de tipo de imc al que equivale su cálculo. 

      ***Nota***: (Mejora: Enum class en https://www.baeldung.com/kotlin/enum)
         * Si el IMC es menos de 18.5, se encuentra dentro del rango de "peso insuficiente". 
         * Si el IMC está entre 18.5 y 24.9, se encuentra dentro del rango de "peso saludable". 
         * Si el IMC está entre 25.0 y 29.9, se encuentra dentro del rango de "sobrepeso". 
         * Si el IMC es 30.0 o superior, se encuentra dentro del rango de "obesidad".

      * Debe implementar también un método que muestre una descripción completa de la persona... `obtenerDesc():String`. Por ejemplo, este método mostrará por pantalla algo así:

         ```
         "Julia con una altura de 1.72m (Por debajo de la media) y un peso 64.7kg (Por encima de la media) tiene un IMC de 21,87 (peso saludable)". 
         ```
   2. Crear en el `main()` una estructura de datos con 4 o 5 personas más, recorrer la estructura y por cada persona debe saludar y mostrar su descripción completa.

   3. Finalmente, revisa el IDE e intenta actualizar el modificador de visibilidad de los métodos de tu clase cómo os estará indicando... 
   veréis que los métodos que realmente no van a ser llamados desde fuera de la clase te recomienda que sean privados a la misma. 
   De esta manera estamos `encapsulando` estos métodos para que se puedan utilizar solo desde dentro de la clase y no sean públicos.

### **Ejercicio 4.4**

   1. Crear una clase `Coche`, a través de la cual se pueda conocer el `color` del coche, la `marca`, el `modelo`, el `número de caballos`, el `número de puertas` y la `matrícula`. 
   Crear el constructor del coche, así como los métodos estándar: `getters`, `setters` y `toString()`.

   2. Para realizar getters y setters, añade el modificador private a los atributos de la clase y genera los métodos `getColor()`, `setColor()`, ..., así para todos los atributos.

   3. En el programa principal, instancia varios coches, muestra su información, cambia el color a algunos de ellos y vuelve a mostrarlos por pantalla.

   4. Realiza también una modificación al método `setNumCaballos()` para que no permita actualizar el atributo `numCaballos` con un valor interior a 70, ni superior a 700.

   5. Realiza otra modificación al método `setNumPuertas()` para que no se pueda actualizar con un valor inferior a 3, ni superior a 5... pero esta vez utiliza `require`.

   6. Para probar las modificaciones a los métodos anteriores, solicita al usuario el número de caballos para un coche y haz lo mismo para el número de puertas.

### **Ejercicio 4.5**

   1. Crear una clase `Tiempo`, con atributos `hora`, `minuto` y `segundo`, que pueda ser construida indicando los tres atributos, sólo hora y minuto o sólo la hora *(si no se indica, el valor de minuto o segundo será 0)*. 

   2. Crear el método `toString()` para mostrar el tiempo en formato: ***`XXh XXm XXs`***.

   3. En el programa principal, debe solicitar por teclado hora, minuto y segundo de forma que se puedan omitir los segundos o los minutos *(y segundos, claro)* e instancie la clase `Tiempo` mostrando su valor.

   4. A tener en cuenta:  

      * Si segundos o minutos es mayor que 60, se tendrá que hacer las operaciones necesarios para incrementar la magnitud superior por el resultado del modulo de 60, quedándose en segundos o minutos con el resto. Es decir 65 segundos equivale a : 1 minuto y 5 segundos.
      * Hora siempre tendrá que ser menor que 24, si no, lanzará una excepción. 
