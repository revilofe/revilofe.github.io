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

**Pregunta:** ¿Qué métodos y propiedades hereda `Example` de `Any`?
**Código:**

```Kotlin
class Example
```

**Respuesta:**

  * `Example` hereda de `Any` los métodos `equals()`, `hashCode()`, y `toString()`.

#### 2.1. Declaración de Herencia

Para que una clase herede de otra en Kotlin, se coloca el nombre de la clase base después de los dos puntos en el encabezado de la subclase. Las clases en Kotlin son `final` por defecto (por similitud con java, utilizando `final` cuando se decide no permitir heredar de una clase); para permitir la herencia, se debe usar `open`.

#### Actividad 2: Instancia de Clases Base y Derivadas

**Pregunta:** ¿Crear una variable de clase `Base`? ¿Puedes asignarle una instancia de `DerivedWithConstructor`?
**Código:**

  ```Kotlin
  open class Base(var p: Int)
  class DerivedWithConstructor(p: Int) : Base(p)
  ```
**Respuesta:** Sí, puedes crear una variable de tipo `Base` y asignarle una instancia de `DerivedWithConstructor` debido a la herencia.

#### 2.2. Herencia sin Constructor Primario

Si una clase derivada no tiene un constructor primario, cada constructor secundario debe inicializar la clase base usando `super` o delegar a otro constructor de la clase derivada que lo haga.

#### Actividad 3: Trabajando con Constructores Secundarios

**Pregunta:** Ejecuta el siguiente código, instancia la subclase con 1 e imprime el valor de `p`. ¿Qué muestra en pantalla? ¿Qué sucede si quitas el constructor de la subclase? ¿Podemos definir la subclase de otra forma? ¿Qué tenemos que hacer para llamar al constructor de 2 parámetros?
**Código:**
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
**Respuesta:**
  * Al ejecutar, muestra `1` en pantalla, indicando el valor de `p`.
  * Si quitas el constructor de la subclase, el código no compilará porque `DerivedWithoutConstructor` necesita definir cómo inicializar `Base`.
  * Para definir la subclase de otra manera, podríamos considerar agregar un constructor primario o utilizar un constructor secundario que llame al constructor de dos parámetros de `Base`.
  * Para llamar al constructor de 2 parámetros de `Base`, necesitamos definir explícitamente ese constructor en la subclase y utilizar `super(p, q)` dentro del constructor secundario.

### 3. Sobreescritura

La sobreescritura de métodos o propiedades, también conocida como "overriding", es un concepto clave en la programación orientada a objetos (OOP) que se refiere a la capacidad de una clase derivada (subclase) de proporcionar una implementación específica para un método o propiedad que ya está definido en su clase base (superclase). Este mecanismo permite a las subclases ajustar o mejorar el comportamiento heredado de la superclase según sus propias necesidades.

#### 3.1. Conceptos Fundamentales

* **Polimorfismo:** La sobreescritura es una forma de polimorfismo, que permite que un objeto de una subclase se comporte de manera diferente al mismo método o propiedad definido en la superclase.
* **Invocación Dinámica:** Cuando un método sobreescrito se invoca en un objeto, la versión del método que se ejecuta es la que corresponde a la clase real del objeto, no necesariamente la clase desde la cual se hace la llamada.

#### 3.2. ¿Cómo Funciona?

Para sobreescibir un método o propiedad en Kotlin, la superclase debe marcar ese método o propiedad con el modificador `open`, indicando que está disponible para ser sobreescrito. Luego, la subclase usa el modificador `override` para proporcionar su propia implementación del método o propiedad.

#### 3.3. Propósito y Beneficios

* **Especialización:** Permite que las subclases especialicen o modifiquen comportamientos heredados de las superclases para satisfacer requisitos específicos.
* **Flexibilidad:** Aumenta la flexibilidad del diseño del software al permitir que nuevas versiones de métodos o propiedades reemplacen a las antiguas en contextos específicos.
* **Consistencia:** Mantiene una interfaz consistente, permitiendo que las subclases se utilicen en lugar de una superclase sin alterar el comportamiento esperado del programa.

#### 3.4.  Consideraciones Importantes

* **Coherencia:** Al sobreescibir métodos o propiedades, es crucial mantener la coherencia en cuanto a la funcionalidad esperada. La nueva implementación debe adherirse al "contrato" del método original, respetando su propósito y comportamiento general.
* **Uso de `super`:** Las subclases pueden llamar al método o propiedad de la superclase usando `super`, permitiendo que la sobreescritura complemente en lugar de reemplazar completamente el comportamiento heredado.

#### 3.5. Sobreescritura en kotlin.

##### 3.5.1. Sobreescritura de métodos

Kotlin requiere **anotaciones explícitas** para la sobreescritura de funciones miembro.

Para que una función pueda ser sobreescrita se utiliza la palabra clave `'open'` delante del nombre de la función. Dado que las clases son **finales** en Kotlin, sólo podemos utilizar la palabra clave `'open'` en funciones miembro de clases que también hayan sido definidas como `'open'`.

Para indicar que una función en la clase derivada sobreescribe una función de la clase padre se utiliza la palabra clave `'override'` delante del nombre de la función. De esta forma le indicamos al compilador que esta función sobreescribe una función de la clase padre y puede realizar las comprobaciones en tiempo de compilación.

Una función con la palabra clave `'override'` también es `'open'` por definición y puede ser sobreescrita por las subclases sucesivas. Es posible marcar una función `'override'` con la palabra clave `'final'` para evitar que sea sobreescrita.

La sobreescritura de métodos en Kotlin permite modificar el comportamiento de métodos heredados en subclases, mientras que el uso de `final` previene la sobreescritura adicional, proporcionando un control detallado sobre la herencia y el polimorfismo en el diseño de software.

##### Actividad 4: Exploración de Sobreescritura de Métodos en Kotlin

**Pregunta:** ¿Cómo funcionan la sobreescritura de métodos y las restricciones de sobreescritura en Kotlin? Examina el comportamiento de sobreescritura en una jerarquía de clases, las limitaciones impuestas por el modificador `final` y la extensión de funcionalidad mediante la sobreescritura en una subclase adicional.

**Código:**

```kotlin
open class Base {
    open fun v() { println("base") }
    open fun x(p: Int) { println(p) }
    fun nv() { println(this.toString() + ": sin sobreescribir") }
}

class Derived: Base() {
    override fun v() { println("derivada") }
    final override fun x(p: Int) { println(p+1) }
}

class Derived2: Base() {
    override fun v() { println("Derivada2") }
}

fun main() {
    val base = Base()
    base.v()
    base.x(10)
    base.nv()

    val derived = Derived()
    derived.v()
    derived.x(10)
    derived.nv()

    val derived2 = Derived2()
    derived2.v()
    derived2.x(10)
    derived2.nv()
}
```

**Respuesta:** Al ejecutar el código proporcionado en la función `main`, observarás lo siguiente en la consola:

```Kotlin
base
10
Base@hashcode: sin sobreescribir
derivada
11
Derived@hashcode: sin sobreescribir
Derivada2
10
Derived2@hashcode: sin sobreescribir
```

* Al llamar a los métodos desde instancias de `Base`, `Derived` y `Derived2`, la consola muestra cómo cada clase maneja sus implementaciones específicas de `v()` y `x(p: Int)`, así como el método `nv()` que no está marcado para sobreescritura y, por lo tanto, mantiene su comportamiento original en todas las clases.
* Intentar sobreescrbir el método `nv` en `Derived` o `Derived2` resultaría en un error de compilación, ya que `nv()` no está marcado con `open` en la clase `Base`, lo que significa que no está disponible para sobreescritura.
* Dado que el método `x(p: Int)` en `Derived` está marcado como `final`, no puede ser sobreescrito en `Derived2`. Si intentas hacerlo, recibirás un error de compilación. En este ejemplo, `Derived2` no intenta sobreescrbir `x(p: Int)`, por lo que no hay conflicto.
* `Derived2` demuestra cómo se puede sobreescrbir el método `v()` para proporcionar una nueva implementación, imprimiendo "Derivada2" cuando se invoca, ilustrando la extensibilidad de las clases en Kotlin mediante la sobreescritura.

En Kotlin, la herencia está regulada por la siguiente regla: si una clase hereda varias implementaciones del mismo miembro de sus superclases inmediatas, debe invalidar este miembro y proporcionar su propia implementación. Para denotar el supertipo del cual se toma la implementación heredada, usamos la palaba clave `'super'` calificado por el nombre de supertipo entre paréntesis angulares, por ejemplo, `super<Base>`:

##### Actividad 5: Entendiendo la Herencia y Polimorfismo en Kotlin

**Pregunta:** ¿Cómo interactúan la herencia de clases y la implementación de interfaces en Kotlin cuando múltiples superclases proporcionan implementaciones para el mismo método? Explora el comportamiento al instanciar la subclase `C` y realizar llamadas polimórficas utilizando referencias de diferentes tipos.

**Código:**

```kotlin
open class A {
    open fun f() { print("A") }
    fun a() { print("a") }
}

interface B {
    fun f() { print("B") } // Los miembros de las interfaces son `open` por defecto.
    fun b() { print("b") }
}

class C() : A(), B {
    // El compilador requiere que 'f()' sea sobreescrito para eliminar la ambigüedad
    override fun f() {
        super<A>.f() // Llamada a A.f()
        super<B>.f() // Llamada a B.f()
    }
}

fun main() {
    val c = C()
    c.f()
    println() // Para separar las salidas

    var a: A = C()
    a.f()
    println() // Para separar las salidas

    var b: B = C()
    b.f()
    println() // Para separar las salidas

    val aInstance = A()
    aInstance.f()
}
```
**Respuesta:** Al ejecutar el código en `main`, observarás lo siguiente en la consola:

1. **Instancia de C:** Al instanciar `C` y llamar a `c.f()`, muestra en pantalla "AB". Esto se debe a que `C.f()` sobreescrito ejecuta explícitamente ambas implementaciones de `f()` de `A` y `B`.
2. **Referencia de A hacia C:** Al declarar `var a: A = C(); a.f()`, también muestra "AB". Aunque `a` es de tipo `A`, el objeto referenciado es una instancia de `C`, por lo que se ejecuta el método `f()` sobreescrito en `C`, que incluye las llamadas a `A.f()` y `B.f()`.
3. **Referencia de B hacia C:** Al declarar `var b: B = C(); b.f()`, muestra "AB" por las mismas razones que el caso anterior. La referencia es de tipo `B`, pero el objeto es de `C`, invocando `C.f()` que llama a ambas implementaciones.
4. **Instancia de A asignada a `a`:** Si instancias `A` y lo asignas a `a`, llamando a `a.f()`, solo muestra "A". En este caso, `a` es de tipo `A` y el objeto referenciado es una instancia directa de `A`, por lo que solo se ejecuta la implementación de `f()` definida en `A`.

**Diferencias Observadas:**

* La principal diferencia radica en el tipo del objeto referenciado. Aunque las variables `a` y `b` pueden tener tipos estáticos diferentes (`A` o `B`), el comportamiento en tiempo de ejecución depende del tipo dinámico del objeto (en este caso, `C`), que ejecuta su propia implementación de `f()`, llamando a las implementaciones tanto de `A` como de `B`.
* En contraste, una instancia directa de `A` solo ejecutará la implementación de `f()` definida en `A`, sin invocar la de `B`, evidenciando cómo el polimorfismo en Kotlin maneja la resolución de métodos en la herencia y las implementaciones de interfaces.

En la sobreescritura de métodos con valores por defecto siempre se utilizan los mismos valores de parámetros por defecto que el método base. Cuando se sobreescribe un método, los valores por defecto deben omitirse de la firma:

```kotlin
open class A {
    open fun foo(i: Int = 10) { ... }
}

class B : A() {
    override fun foo(i: Int) { ... }  // no default value allowed
}
```
##### 3.5.2. Sobreescritura de propiedades

La sobreescritura de propiedades funciona de manera similar a la sobreescritura de métodos.

Las propiedades declaradas en una superclase que luego se vuelven a declarar en una clase derivada deben ir precedidas por la palabra clave `'override'` y deben tener un tipo compatible. También se puede usar la palabra clave `'override'` como parte de la declaración de una propiedad en un constructor primario.

Cada propiedad declarada puede ser sobreescrita por una propiedad con un inicializador o por una propiedad con un método `'getter()'`

##### Actividad 6: Explorando la Sobreescritura de Propiedades en Kotlin

**Pregunta:** ¿Cómo se comporta la sobreescritura de propiedades en Kotlin y qué diferencias se observan al imprimir los valores de las propiedades sobreescritas en una clase base y sus subclases?

**Código:**

```kotlin
open class Foo {
    open val x: String
    get() = "base"
}

class Bar : Foo() {
    override val x: String = "subclase"
}

interface Foo1 {
    val count: Int
}

class Bar1(override val count: Int) : Foo1

fun main() {
    val foo = Foo()
    println(foo.x)

    val bar = Bar()
    println(bar.x)

    val bar1 = Bar1(10)
    println(bar1.count)
}
```

**Respuesta:** Al ejecutar el código proporcionado en la función `main`, se observa lo siguiente en la consola:

1. **Objeto de `Foo`:** Imprime el valor de la propiedad `x` definida en la clase base `Foo`, que es "base". Esto se debe a que se accede al getter de la propiedad `x` en la clase `Foo`, que devuelve el valor "base".
2. **Objeto de `Bar`:** Imprime el valor de la propiedad `x` sobreescrita en la subclase `Bar`, que es "subclase". Esto muestra cómo la sobreescritura de la propiedad `x` en `Bar` cambia el valor devuelto por el getter de esta propiedad, demostrando la sobreescritura de propiedades en acción.
3. **Objeto de `Bar1`:** Imprime el valor de la propiedad `count` en la instancia de `Bar1`, que es 10. Aquí se ilustra cómo se puede sobreescrbir una propiedad definida en una interfaz (`Foo1`) al implementar esta interfaz en una clase (`Bar1`), proporcionando un valor específico (en este caso, a través del constructor de `Bar1`).

**Diferencias Observadas:**

* La principal diferencia observada es cómo el valor de la propiedad `x` cambia entre la clase base `Foo` y su subclase `Bar` debido a la sobreescritura de la propiedad. En `Foo`, el getter de `x` devuelve "base", mientras que en `Bar`, la propiedad sobreescrita `x` tiene un valor fijo de "subclase".
* Al comparar con la implementación y sobreescritura de propiedades en interfaces y clases que las implementan, como `Foo1` y `Bar1`, se ve que el mecanismo de sobreescritura permite personalizar los valores de las propiedades en subclases o en implementaciones de interfaces, ofreciendo flexibilidad en cómo se representan y se accede a los datos de un objeto.

##### 3.5.3. Orden de inicialización

Durante la construcción de una nueva instancia de una clase derivada, **la inicialización de la clase base se realiza como primer paso** (precedida solo por la evaluación de los argumentos para el constructor de la clase base) y, por lo tanto, ocurre antes de que se ejecute la lógica de inicialización de la clase derivada.

Por lo tanto, durante la inicialización de las propiedades de la clase base las propiedades de la clase derivada aún no se han inicializado. Si alguna de esas propiedades se utilizan (de forma directa o indirecta) en la inicialización de la clase base se pueden producir comportamientos extraños o errores en tiempo de ejecución.


##### Actividad 7: Comprendiendo el Orden de Inicialización en Kotlin

**Pregunta:** ¿Cuál es el orden de inicialización de una clase base y su clase derivada en Kotlin, especialmente cuando la clase derivada sobreescribe propiedades de la clase base? Observa cómo este orden afecta la inicialización de las propiedades.

**Código:**

```kotlin 
open class Base(val name: String) {
    init { println("Initializing Base") }
    open val size: Int = name.length.also { println("Initializing size in Base: $it") }
}

class Derived(name: String, val lastName: String) : Base(name.capitalize().also { println("Argument for Base: $it") }) {
    init { println("Initializing Derived") }
    override val size: Int = (super.size + lastName.length).also { println("Initializing size in Derived: $it") }
}

fun main() {
    Derived("john", "doe")
}
```

**Respuesta:** Al ejecutar el código proporcionado en la función `main`, el orden de salida en la consola será el siguiente:

1. "Argument for Base: John" - Este mensaje se imprime primero debido a la evaluación del argumento para el constructor de la clase base (`Base`) que se realiza antes de su inicialización.
2. "Initializing Base" - Indica que la inicialización de la clase base `Base` comienza inmediatamente después de la evaluación de los argumentos para su constructor.
3. "Initializing size in Base: 4" - Muestra la inicialización de la propiedad `size` en la clase base `Base`. El valor `4` corresponde a la longitud del nombre "John" después de aplicar `capitalize()`.
4. "Initializing Derived" - Señala que la inicialización de la clase derivada `Derived` comienza después de completar la inicialización de la clase base.
5. "Initializing size in Derived: 7" - Muestra la inicialización de la propiedad `size` sobrescrita en `Derived`, sumando la longitud del apellido "doe" a la `size` de la clase base, resultando en 7.

**Diferencias Observadas:**

* El proceso de inicialización comienza con la evaluación de los argumentos pasados al constructor de la clase base, seguido de la inicialización de la clase base antes que la clase derivada.
* Las propiedades de la clase derivada que sobrescriben a las de la clase base no se inicializan hasta que no se complete la inicialización de la clase base, lo que es crucial para evitar referencias a propiedades que aún no se han inicializado.
* Este orden garantiza que todas las propiedades y bloques de inicialización de la clase base se procesen antes de ejecutar cualquier lógica de inicialización en la clase derivada, siguiendo una secuencia lógica y predecible que previene errores en tiempo de ejecución relacionados con la inicialización prematura de propiedades.


#### 3.6. Invocar la implementación de la superclase

El código en una clase derivada puede llamar a funciones en la superclase e implementaciones de accesores de propiedades usando la palabra clave `'super'`:

```kotlin
open class Foo {
    open fun f() { println("Foo.f()") }
    open val x: Int get() = 1
}

class Bar : Foo() {
    override fun f() {
        super.f()  // Calling the super function  
        println("Bar.f()")
    }
    override val x: Int get() = super.x + 1
}
```




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

```