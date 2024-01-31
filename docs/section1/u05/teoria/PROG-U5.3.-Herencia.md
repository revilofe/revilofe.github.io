---
title: "UD 5 - 5.1 Revisión de las clases"
description: kotlin
summary: kotlin
authors:
    - Eduardo Fdez
date: 2022-11-14
icon:   
permalink: /prog/unidad4/4.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 5.2. Herencia. Interfaces


### 1. Concepto de Herencia

La herencia es uno de los pilares fundamentales de la OOP, junto con el encapsulamiento, la abstracción y el polimorfismo. Es un mecanismo que permite que una clase, conocida como subclase o clase hija, herede atributos (campos) y comportamientos (métodos) de otra clase, llamada superclase o clase padre. Esta relación no solo facilita la reutilización del código existente sino que también establece una jerarquía de clases dentro de la arquitectura del software.

#### 1.1. Objetivos y Beneficios

* **Reutilización de Código:** Reduce la duplicación de código al permitir que las clases compartan atributos y métodos, lo que facilita el mantenimiento y la actualización del software.
* **Jerarquía de Clases:** Establece una estructura lógica y jerárquica que refleja relaciones del mundo real o categorizaciones lógicas, mejorando la legibilidad y organización del código.
* **Extensibilidad:** Permite que el software se extienda con nuevas características de manera eficiente, añadiendo o modificando comportamientos en las subclases sin afectar la superclase o las clases hermanas.
* **Polimorfismo:** Facilita el uso de polimorfismo, donde un objeto de la subclase puede ser tratado como un objeto de la superclase, permitiendo un diseño de software más flexible y dinámico.

#### 1.2. Mecanismos y Consideraciones

* **Sobrescritura de Métodos:** Las subclases pueden sobrescribir los métodos heredados de las superclases para proporcionar implementaciones específicas que se ajusten a sus necesidades particulares.
* **Acceso a Miembros Superiores:** Las subclases pueden acceder a los miembros (atributos y métodos) de la superclase, dependiendo de los modificadores de acceso aplicados (private, protected, etc.).
* **Constructor de la Superclase:** Al crear una instancia de una subclase, también se debe inicializar la superclase, a menudo llamando explícitamente al constructor de la superclase desde el constructor de la subclase.

#### 1.3. Limitaciones y Desventajas

* **Precaución:** La herencia puede introducir complejidad y riesgo en el diseño del software, por lo que debe usarse con precaución. En general, se recomienda favorecer la composición sobre la herencia. 
* **Acoplamiento:** Un uso excesivo o inadecuado de la herencia puede llevar a un acoplamiento elevado entre clases, lo que puede complicar el mantenimiento y la escalabilidad del software.
* **Jerarquías Profundas:** Las jerarquías de herencia profundas o complicadas pueden hacer que el código sea difícil de seguir y entender.
* **Flexibilidad vs. Rigidez:** Mientras que la herencia promueve la reutilización del código, también puede imponer una estructura rígida, lo que podría limitar la flexibilidad del diseño si no se usa cuidadosamente.

#### 1.4. Ejemplo Conceptual

Imaginemos un sistema de clasificación biológica. En este sistema, cada nivel hereda características del nivel anterior. Así, todos los mamíferos comparten ciertas características, pero dentro de los mamíferos, los primates forman un subgrupo con características adicionales, y dentro de los primates, los humanos tienen características aún más específicas. En términos de OOP, `Mamífero` sería una superclase de `Primate`, que a su vez sería una superclase de `Humano`. Cada subclase hereda y potencialmente extiende o modifica las características de su superclase.

### 2. Herencia en Kotlin

La herencia es un concepto clave en la Programación Orientada a Objetos (POO), permitiendo a los desarrolladores crear nuevas clases basadas en otras preexistentes. Esta característica es esencial para reutilizar, extender y modificar el comportamiento de clases ya definidas, promoviendo así la eficiencia y la reducción de la redundancia en el código.

En Kotlin, la herencia se maneja con una sintaxis clara y reglas específicas diseñadas para mantener la seguridad y la claridad del código:

1. **Superclase y Subclase:**
   * La **superclase** (o clase base) es la clase existente de la que se deriva una nueva clase.
   * La **subclase** (o clase derivada) es la nueva clase creada, que hereda propiedades y métodos de la superclase.
2. **Herencia Implícita:**
   * Al heredar de una superclase, la subclase obtiene automáticamente todos los campos, propiedades y métodos de dicha superclase, incluyendo aquellos heredados por la superclase de otras superclases, si las hay.
3. **Restricción de Herencia:**
   * Kotlin permite una herencia simple, significando que una subclase solo puede tener una clase base directa, aunque puede implementar múltiples interfaces.
4. **Herencia Transitiva:**
   * La herencia es transitiva. Si una clase C hereda de B, y B hereda de A, entonces C indirectamente hereda de A.
5. **Clase Any:**
   * Todas las clases en Kotlin heredan de `Any`, la superclase predeterminada que proporciona métodos básicos como `equals()`, `hashCode()`, y `toString()`.

#### Actividad 1: Herencia de `Any`

* **Pregunta:** ¿Qué métodos y propiedades hereda `Example` de `Any`?
* **Código:**

  ```Kotlin
  class Example
  ```
* **Respuesta:**

  * `Example` hereda de `Any` los métodos `equals()`, `hashCode()`, y `toString()`.

#### 2.1. Declaración de Herencia

Para que una clase herede de otra en Kotlin, se coloca el nombre de la clase base después de los dos puntos en el encabezado de la subclase. Las clases en Kotlin son `final` por defecto (por similitud con java, utilizando `final` cuando se decide no permitir heredar de una clase); para permitir la herencia, se debe usar `open`.

#### Actividad 2: Instancia de Clases Base y Derivadas

* **Pregunta:** ¿Crear una variable de clase `Base`? ¿Puedes asignarle una instancia de `DerivedWithConstructor`?
* **Código:**

  ```Kotlin
  open class Base(var p: Int)
  class DerivedWithConstructor(p: Int) : Base(p)
  ```
* **Respuesta:** Sí, puedes crear una variable de tipo `Base` y asignarle una instancia de `DerivedWithConstructor` debido a la herencia.

#### 2.2. Herencia sin Constructor Primario

Si una clase derivada no tiene un constructor primario, cada constructor secundario debe inicializar la clase base usando `super` o delegar a otro constructor de la clase derivada que lo haga.

#### Actividad 3: Trabajando con Constructores Secundarios

* **Pregunta:** Ejecuta el siguiente código, instancia la subclase con 1 e imprime el valor de `p`. ¿Qué muestra en pantalla? ¿Qué sucede si quitas el constructor de la subclase? ¿Podemos definir la subclase de otra forma? ¿Qué tenemos que hacer para llamar al constructor de 2 parámetros?
* **Código:**
  ```kotlin
  open class Base(var p: Int) {
      constructor(p: Int, q: Int): this(p)
  }

  class DerivedWithoutConstructor : Base {
      constructor(p: Int) : super(p)
  }

  fun main() {
      val instancia = DerivedWithoutConstructor(1)
      println(instancia.p)
  }
  ```
* **Respuesta:**
  * Al ejecutar, muestra `1` en pantalla, indicando el valor de `p`.
  * Si quitas el constructor de la subclase, el código no compilará porque `DerivedWithoutConstructor` necesita definir cómo inicializar `Base`.
  * Para definir la subclase de otra manera, podríamos considerar agregar un constructor primario o utilizar un constructor secundario que llame al constructor de dos parámetros de `Base`.
  * Para llamar al constructor de 2 parámetros de `Base`, necesitamos definir explícitamente ese constructor en la subclase y utilizar `super(p, q)` dentro del constructor secundario.

---

## Reference

* [Kotlinlang Inheritance](https://kotlinlang.org/docs/inheritance.html)
* [Kotlinlang Classes and Inheritance](https://kotlinlang.org/docs/reference/classes.html#inheritance)
* [Kotlinlang Constructors](https://kotlinlang.org/docs/reference/classes.html#constructors)
* [Kotlinlang Secondary Constructors](https://kotlinlang.org/docs/reference/classes.html#secondary-constructors)
* [Kotlinlang Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin/-any/index.html)



## Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)


```
