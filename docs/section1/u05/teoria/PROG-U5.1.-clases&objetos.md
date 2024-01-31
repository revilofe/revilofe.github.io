---
title: "UD 5 - 5.1 Revisión de las clases/objetos"
description: Revisión de las clases/objetos
summary: Revisión de las clases/objetos
authors:
    - Eduardo Fdez
date: 2024-01-31
icon:   
permalink: /prog/unidad5/5.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 5.1.- Revisitando las clases y los objetos

En Kotlin, la Programación Orientada a Objetos (POO) se maneja con una sintaxis concisa y poderosas características que simplifican la codificación y mejoran la legibilidad. Entre estas características, las clases y objetos juegan un papel central, permitiendo a los desarrolladores modelar el mundo real de manera eficiente y efectiva. Kotlin, diseñado para ser completamente interoperable con Java, introduce mejoras significativas sobre este, haciendo que el trabajo con POO sea más intuitivo y menos propenso a errores.

### 1. Data classes

Las **Data classes** son una forma concisa de crear clases que solo contienen datos. Estas clases se definen con la palabra clave `'data'`.

```kotlin
data class User(val name: String, val age: Int)
```

De forma automática el compilador crear los métodos `hashCode()`, `equals()`, `copy()` y `toString()` a partir de todas las propiedades declaradas en el constructor primario. También se generan las funciones `componentN()` que corresponden a las propiedades declaradas en orden en el constructor primario.

Para evitar comportamientos extraños estas clases deben **cumplir ciertos requisitos**:

* El constructor primario necesita tener al menos un parámetro.
* Todos los parámetros del constructor primario estarán marcados como `'val'` o `'var'`.
* Una _'data class'_ no puede ser `'abstract'`, `'open'`, `'sealed'` o `'inner'`.
* (Antes de 1.1) Las _'data classes'_ no pueden extender de otras clases (pero pueden implementar interfaces).

El compilador sólo tiene en cuenta las propiedades declaradas en el constructor primario a la hora de generar los métodos de forma automática. Por tanto, para excluir propiedades se deben declarar en el cuerpo de la clase.

```kotlin
data class DataClassExample(val x: Int, val y: Int, val z: Int) {
    // Propiedad excluida
    var xx; Int = 0
}

val fooData = DataClassExample(1, 2, 4)
val fooCopy = fooData.copy(y = 100)

// El formato de 'toString()' es el mismo 'ClassName(prop=xx, prop=yy, ....)'
println(fooData) // => DataClassExample(x=1, y=2, z=4)
println(fooCopy) // => DataClassExample(x=1, y=100, z=4)
```

El compilador genera la función `copy()` que permite copiar un objeto y en caso necesario, crear la copia alterando algunas de sus propiedades y manteniendo el resto.

```kotlin
data class User(val name: String, val age: Int)

// Función 'copy()' generada automáticamente
// fun copy(name: String = this.name, age: Int = this.age) = User(name, age)

val jack = User(name = "Jack", age = 1)

// Copiamos el objeto pero modificando la propiedad 'age'
val olderJack = jack.copy(age = 2)
```

Las funciones `componentN()` permite desestructurar las propiedades:

```kotlin
val jane = User("Jane", 35)
val (name, age) = jane
println("$name, $age years of age") // => Jane, 35 years of age
```

Cada tipo se deriva de `'Any'`, que viene con una declaración de método `'hashCode()'`. Esto es el equivalente de un método `'hashCode()'` de clase _'Object'_ de Java. Este método es importante cuando se insertan instancias del objeto en colecciones, como un mapa. Al implementar este método, se debe cumplir con una serie de requisitos:

1. Cuando se invoque en el mismo objeto más de una vez durante el tiempo de ejecución, el método `'hashCode()'` debe devolver constantemente el mismo valor, dado que el objeto no se modificó.
2. Si para dos objetos el método `'equals()'`  devuelve true, entonces llamar al método `'hashCode()'` en cada uno de ellos debería devolver el mismo valor entero.
3. Si dos objetos no son iguales, es decir, que el método `'equals()'` devuelve false cuando se comparan, no es un requisito que cada método `'hashCode()'` del objeto devuelva valores distintos. Sin embargo, producir un entero distinto para objetos desiguales podría mejorar el rendimiento de las colecciones basadas en 'hash'.

Las _'data classes'_ son un forma compacta y legible de devolver dos o más valores de una función. Otra alternativa, menos legible, es utilizar el tipo `'Pair'` o `'Triple'` proporcionado por Kotlin:

```kotlin
data class Result(val result: Int, val status: Boolean)

fun checkStatus() = Result(10, true)  // función que retorna un tipo 'Result'

val (result, status) = checkStatus() // usamos la desestructuración de datos para acceder a los datos
```

Aqui puedes ver un ejemplo en el que se compara una data class en java con una data class en kotlin: [data Class](https://devexpert.io/data-classes-kotlin/)

### 2. Sealed classes

En Kotlin una *__'sealed class'__* es una clase abstracta (no se puede crear instancias) que otras clases pueden extender. Estas subclases se definen dentro del cuerpo de la _'sealed class'_, en el mismo archivo por lo que podemos conocer todas las subclases posibles simplemente viendo el archivo.

Las _'sealed class'_ se utilizan para representar jerarquías de clases restringidas, de forma que una clase solo pueda heredar de un conjunto limidado de tipos. Son, en cierto sentido, una extensión de las clases de enumeración.

* Podemos agregar el modificador `'abstract'`, pero esto es redundante porque estas clases son abstractas por defecto.
* No pueden tener el modificador `'open'` ni `'final'`.
* Podemos declarar clases de datos y objetos como subclases a una _'sealed class'_ (aún deben declararse en el mismo archivo).
* No pueden tener constructores públicos ya que sus constructores son privados de forma predeterminada.

```kotlin
// shape.kt

sealed class Shape

class Circle : Shape()
class Triangle : Shape()
class Rectangle: Shape()
```

### 3. Generics

*__'Covariance'__* y *__'contravariance'__* son términos que hacen referencia a la capacidad de usar un tipo más derivado (más específico) o menos derivado (menos específico) que el indicado originalmente. Los parámetros de tipo genérico admiten estos términos para proporcionar mayor flexibilidad a la hora de asignar y usar tipos genéricos. Cuando se hace referencia a un sistema de tipos, se definen como:

* *__'Covariance'__* -> Permite usar un tipo más derivado que el especificado originalmente. Puede asignar una instancia de `Class<Derived>` a una variable de tipo `Class<Base>`.
* *__'Contravariance'__* -> Permite usar un tipo más genérico (menos derivado) que el especificado originalmente. Puede asignar una instancia de `Class<Base>` a una variable de tipo `Class<Derived>`.
* *__'Invariance'__* -> Significa que solo se puede usar el tipo especificado originalmente. Así, un parámetro de tipo genérico invariable no es covariante ni contravariante. No se puede asignar una instancia de `List<Base>` a una variable de tipo `List<Derived>` o viceversa.

Al igual que en Java, en Kotlin las clases pueden tener tipos con parámetros.

```kotlin
class Box<T>(t: T) {
    var value = t
}
```

En general, para crear una instancia de una clase genérica tenemos que proveer el tipo a la clase:

```kotlin
val box: Box<Int> = Box<Int>(1)
```

Si los parámetros se pueden inferir, como por ejemplo de los argumentos del constructor o por algún otro medio, se pueden omitir los argumentos de tipo:

```kotlin
val box = Box(1) // '1' tiene tipo Int así que el compilador infiere el tipo "Box<Int>"
```

#### 3.1. La palabra clave 'out'

Digamos que queremos crear una clase de productor que producirá un resultado de algún tipo 'T'. A veces; queremos asignar ese valor producido a una referencia que es de un supertipo del tipo 'T'.

Para lograr eso usando Kotlin, necesitamos usar la palabra clave `'out'` en el tipo genérico. Esto significa que podemos asignar esta referencia a cualquiera de sus supertipos. El valor de salida solo puede ser producido por la clase dada pero no consumido:

```kotlin
class ParameterizedProducer<out T>(private val value: T) {
    fun get(): T {
        return value
    }
}

val a = ParameterizedProducer("string") // ParameterizedProducer<String>
val x: ParameterizedProducer<Any> = a // Correcto

val b = ParameterizedProducer(10) // ParameterizedProducer<Int>
val y: ParameterizedProducer<Number> = b // Correcto
val z: ParameterizedProducer<String> = b // ¡Error de compilación!
```

#### 3.2. La palabra clave 'in'

A veces, tenemos una situación opuesta, lo que significa que tenemos una referencia de tipo T y queremos poder asignarla al subtipo de T.

Podemos usar la palabra clave `'in'` en el tipo genérico si queremos asignarlo a la referencia de su subtipo. La palabra clave `'in'` solo se puede utilizar en el tipo de parámetro que se consume, no se produce:

```kotlin
class ParameterizedConsumer<in T> {
    fun toString(value: T): String {  // 'toString()' will only be consuming a value of type T.
        return value.toString()
    }
}

val a = ParameterizedConsumer<Number>()

val b: ParameterizedConsumer<Double> = a // Correcto
val c: ParameterizedConsumer<Int> = a // Correcto
val d: ParameterizedConsumer<String> = a // ¡Error de compilación!
```

#### 3.3. Star projections

Hay situaciones en las que no es importante el tipo específico de un valor. Para ello usamos el operador `'*'` o _'star projection'_:

```kotlin
fun printArray(array: Array<*>) {
    array.forEach { println(it) }
}

// Podemos pasar una matriz de cualquier tipo al método 'printArray()'
printArray(arrayOf(1,2,3))

printArray(arrayOf("hello", "World!!", 5))
```

#### 3.4. Generic functions

Las funciones también pueden ser genéricas en los tipos que utilizan. Esto permite escribir una función que puede funcionar con cualquier tipo, en lugar de solo un tipo específico. Para ello, definimos los parámetros de tipo en la firma de función.

```kotlin
fun <T> choose(t1: T, t2: T, t3: T): T {
    return when (Random().nextInt(3)) {
        0 -> t1
        1 -> t2
        else -> t3
    }
}

// Podemos usar esta función con enteros. Si el compilador puede inferir el tipo se puede omitir.
val r = choose<Int>(5, 7, 9)
val r = choose(5, 7, 9)

// También es válido usar la función con Strings
val s = choose<String>("BMW", "Audi", "Ford")
val s = choose("BMW", "Audi", "Ford")
```

#### 3.5. Generic constraints

El conjunto de todos los tipos posibles que pueden sustituirse por un parámetro de tipo dado puede estar restringido por restricciones genéricas.

El tipo más común de restricción es un límite superior que corresponde a la palabra clave de extensión de Java:

```kotlin
fun <T : Comparable<T>> sort(list: List<T>) {  ... }

sort(listOf(1, 2, 3)) // OK. Int is a subtype of Comparable<Int>
sort(listOf(HashMap<Int, String>())) // Error: HashMap<Int, String> is not a subtype of Comparable<HashMap<Int, String>>
```

El límite superior predeterminado (si no se especifica) es `'Any?'`.


### 4. Clases Internamente Agrupadas
En Kotlin, tenemos estas 'Clases Internamente Agrupadas', que pueden ser o bien 'Nested Classes' sin acceso directo a la clase exterior, o bien 'Inner Classes' que sí tienen acceso."

#### 4.1 Nested classes

Al igual que las funciones, Kotlin permite las clases internas, es decir, clases definidas dentro de otra clase. Son equivalentes a las clases internas estáticas en Java.

```kotlin
class OuterClass {

    class NestedClass {
        fun nestedClassFunc() { }
    }
}

val nestedClass = OuterClass.NestedClass().nestedClassFunc()
```

#### 4.2. Inner class

Las clases internas, por otro lado, pueden hacer referencia a la clase externa en la que se declaró. Para crear una clase interna, colocamos la palabra clave `'inner'` antes de la palabra clave `'class'`.

```kotlin
class OuterClass() {
    val oCPropt: String = "Yo"

    inner class InnerClass {
        fun innerClassFunc() {
            val outerClass = this@OuterClass
            print(outerClass.oCPropt)
        }
    }
}
val demo = OuterClass().InnerClass().innerClassFunc() // => yo
```

#### 4.3. Diferencias entre Nested e Inner classes

¡Vamos a desenredar este lío de clases en Kotlin con un poco de humor y claridad!

Imagina que tienes una familia grande viviendo en una casa enorme. La "Nested Class" es como tu primo que vive en la casa pero tiene su propia entrada y no depende de nadie para sus cosas. Es bastante independiente; vive allí, pero su vida es separada. En Kotlin, una "Nested Class" es estática por defecto, lo que significa que no puede acceder directamente a las propiedades de la clase externa. Es como si tu primo no pudiera simplemente abrir tu refrigerador sin preguntar.

Por otro lado, la "Inner Class" es como tu hermano que vive en la misma habitación que tú. Está muy unido a ti y comparte todo contigo. En Kotlin, una "Inner Class" está marcada con la palabra clave `inner` y puede acceder a los miembros de su clase externa. Es como si tu hermano pudiera usar tu computadora portátil sin tener que pedirte permiso cada vez.

Por tanto:

* **Nested Class (Clase Anidada)**: Es como un inquilino independiente en tu casa grande. No necesita de la clase externa para funcionar, por lo que no puede acceder a sus miembros directamente. Se declara sin la palabra clave `inner`.

    ```Kotlin 
    class CasaGrande {
        class PrimoIndependiente {
            fun hacerAlgo() {
                // Puede hacer cosas, pero no puede acceder directamente a lo que está en CasaGrande.
            }
        }
    }
    ```

* **Inner Class (Clase Interna)**: Es como un hermano con el que compartes tu habitación. Tiene acceso completo a todo lo que es tuyo. Se declara con la palabra clave `inner` y puede acceder a los miembros de la clase externa.

    ```kotlin
    class CasaGrande {
        inner class HermanoCompartido {
            fun hacerAlgo() {
                // Puede hacer cosas Y acceder a lo que está en CasaGrande.
            }
        }
    }
    ```


### 5. Enumeraciones

**Las clases de enumeración son similares a los tipos _'enum'_ de Java**. El uso más básico de las clases de enumeración es la implementación de enumeraciones de tipos seguros. Cada constante de la enumeración es un objeto. Las constantes de la enumeración están separadas por comas.

```kotlin
enum class Country {
    Spain, France, Portugal
}
```

Las enumeraciones pueden tener constructor:

```kotlin
enum class Direction(val angle: Int) {
    North(90), West(180), South(270), East(0)
}
```

En Kotlin las constantes de la enumeración pueden declarar sus propias clases anónimas con sus métodos correspondientes, así como sobreescribir métodos primarios.

Si la enumeración define algún miembro, debe separar las definiciones de constantes de enumeración de las definiciones de miembros con un punto y coma, al igual que en Java.

```kotlin
enum class ProtocolState {
    WAITING {
        override fun signal() = TALKING
    },

    TALKING {
        override fun signal() = WAITING
    };

    abstract fun signal(): ProtocolState
}
```

En Kotlin las enumeraciones disponen de forma predeterminada de los métodos:

* `EnumClass.valueOf(value: String): EnumClass` -> Devuelve la constante de enumeración por su nombre. Lanza un `IllegalArgumentException` si no existe la constante.
* `EnumClass.values(): Array<EnumClass>` -> Retorna un array con las constantes de enumeración.

Además de los métodos las instancias de enumeración vienen con dos propiedades predefinidas. Uno es `'name'` de tipo `String` y el segundo es `'ordinal'` de tipo `Int` para obtener la posición de la constante dentro de la enumeración, teniendo en cuenta que empiezan por 0:

```kotlin
enum class Country {
    Spain, France, Portugal
}

println(Country.Spain) // => Spain
println(Country.valueOf("Spain")) // => Spain

println(Country.Portugal.name) // => Portugal
println(Country.France.ordinal) // => 1

fun countries() {
    for (country in Country.values()) {
        println("Country: $country")
    }
}
```

Aqui puedes ver un ejemplo más avanzado sobre el uso de [enum Class](https://www.baeldung.com/kotlin/enum) en kotlin. 

### 6. Objects

En kotlin, los objetos pueden ser definidos de forma muy similar a las clases. A veces necesitamos crear un objeto con una ligera modificación de alguna clase, sin declarar explícitamente una nueva subclase para ello. Java maneja este caso con clases internas anónimas. Kotlin generaliza ligeramente este concepto con _'object expressions'_ y _'objects declarations'_.

Estas son algunas de las características de los objetos en Kotlin:

* Pueden tener propiedades, métodos y un bloque init.
* Estas propiedades o métodos pueden tener modificadores de visibilidad.
* No pueden tener constructores (primarios o secundarios).
* Pueden extender otras clases o implementar una interfaz.

Hay importantes diferencias semánticas entre un _'object expression'_ y un _'object declaration'_

* Los _'object expression'_ se ejecutan (y se inicializan) inmediatamente, donde se usan.
* Los _'object declaration'_ se inicializan cuando se accede por primera vez, de forma perezosa. Suelen usarse para implementar patrones de diseño como el patrón _'Singleton'_.
* Por su parte, un _'companion object'_ se inicializa cuando se carga la clase correspondiente. Se usa para implementar métodos y propiedades de nivel de clase en Kotlin.

#### 6.1. Objects expressions

Para crear un objeto de una clase anónima que hereda de algún tipo (o tipos), escribimos:

```kotlin
fun countClicks(window: JComponent) {
    var clickCount = 0
    var enterCount = 0

    window.addMouseListener(object : MouseAdapter() {
        override fun mouseClicked(e: MouseEvent) {
            clickCount++
        }

        override fun mouseEntered(e: MouseEvent) {
            enterCount++
        }
    })
    // ...
}
```

#### 6.2. Objects declarations

Colocamos la palabra clave `'object'` antes del nombre del objeto que queremos crear. De hecho, estamos creando un **SINGLETON** cuando creamos objetos en Kotlin usando esta construcción ya que solo existe una instancia de un objeto.

```kotlin
object ObjectExample {
    val baseUrl: String = "http://www.myapi.com/"
    fun hello(): String {
        return "Hello"
    }
}

println(ObjectExample.hello()) // => Hello

fun useObject() {
    ObjectExample.hello() // => Hello
    val someRef: Any = ObjectExample // Usamos el nombre de los objetos tal como son
}
```

Al igual que una declaración de variable, una declaración de objeto no es una expresión y no se puede utilizar en el lado derecho de una declaración de asignación.

Los objetos en Kotlin pueden utilizarse también para crear constantes.

```kotlin
object APIConstants {
    val baseUrl: String = "http://www.myapi.com/"
}
```

### 7. Companion objects

Los _'companion objects'_ son un tipo de _'object declaration'_. Como Kotlin no admite clases, métodos y/o propiedades estáticas, como las que tenemos en Java (tambien llamadas métodos/propiedades de clase),  Kotlin provee los _'companion objects'_. Estos objetos son básicamente un objeto que pertenece a una clase que se conoce como la clase complementaria del objeto. Este objeto se indica con la palabra clave `'companion'`.

Similar a los métodos estáticos en Java, un _'companion object'_ no está asociado con una instancia de clase, sino con la propia clase.

Se puede llamar a los miembros del _'companion object'_ usando simplemente el nombre de la clase como el calificador, como si fuera un método estático.

Un _'companion object'_ puede tener nombre que facilitará el ser invocado desde Java aunque es opcional.

```kotlin
class Person private constructor(var firstName: String, var lastName: String) {

    // Podemos omitir el nombre del objeto
    companion object {
        var count: Int = 0
        fun create(firstName: String, lastName: String): Person = Person(firstName, lastName)

        // Podemos tener bloques 'init' dentro de un 'companion object'
        init {
            println("Person companion object created")
        }
    }
}
val person = Person.create("John", "Doe")

class MyClass {

    fun sayHello() = println("hello")

    // Objeto con el nombre 'Factory' y que utilizaremos como 'Factory Pattern'
    companion object Factory {
        fun create(): MyClass = MyClass()

        fun sayHelloFromCompanion() = MyClass().sayHello() // Podemos acceder a miembros de la clase
    }
}

val myClass = MyClass.create()
MyClass().sayHello() // incorrecto
MyClass.Factory.sayHelloFromCompanion() // Invocar un método del 'companion'
```

---

## Reference

* [https://devexpert.io/data-classes-kotlin/](data class)
* [https://www.baeldung.com/kotlin/enum](class enum)
* [https://kotlinlang.org/docs/reference/](https://kotlinlang.org/docs/reference/)
* [https://www.packtpub.com/application-development/programming-kotlin](https://www.packtpub.com/application-development/programming-kotlin)
* [https://learnxinyminutes.com/docs/kotlin/](https://learnxinyminutes.com/docs/kotlin/)
* [https://github.com/Zhuinden/guide-to-kotlin](https://github.com/Zhuinden/guide-to-kotlin)
* [https://superkotlin.com/kotlin-mega-tutorial/](https://superkotlin.com/kotlin-mega-tutorial/)
* [https://revilofe.github.io/](https://revilofe.github.io/)

## Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)

## License

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)
Esta obra está bajo una [licencia de Creative Commons Reconocimiento-Compartir Igual 4.0 Internacional](http://creativecommons.org/licenses/by-sa/4.0/).
