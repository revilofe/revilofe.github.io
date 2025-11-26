---
title: "UD 5 - 5.1 Revisión de las clases/objetos"
description: Revisión de las clases/objetos
summary: Revisión de las clases/objetos
authors:
    - Eduardo Fdez
date: 2024-01-31
icon: "material/file-document-outline"
permalink: /prog/unidad5/5.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 5.1. Revisitando las clases y los objetos

En Kotlin, la Programación Orientada a Objetos (POO) se maneja con una sintaxis concisa y poderosas características que simplifican la codificación y mejoran la legibilidad. Entre estas características, las clases y objetos juegan un papel central, permitiendo a los desarrolladores modelar el mundo real de manera eficiente y efectiva. Kotlin, diseñado para ser completamente interoperable con Java, introduce mejoras significativas sobre este, haciendo que el trabajo con POO sea más intuitivo y menos propenso a errores.

### 1. Data class

Las clases de datos, o "data classes", son una característica de Kotlin diseñada para contener datos puros. Son particularmente útiles cuando necesitas crear clases que actúen principalmente como contenedores de datos sin mucha lógica adicional.

Un ejemplo de data class en Kotlin:
```
data class User(val name: String, val age: Int, val email: String)
```

La clase de datos anterior define una clase `User` con dos propiedades: `name`, `age` y `email`. Kotlin genera automáticamente métodos como `equals()`, `hashCode()`, y `toString()` para esta clase, lo que la hace muy conveniente para trabajar con datos de forma clara y concisa.

#### 1.1. ¿Cuándo usarlas?

Aquí te explico cuándo es especialmente apropiado usarlas:

##### 1.1.1. Modelado de Datos Simples

Usa data classes cuando necesites modelar datos simples y concisos. Por ejemplo, si estás creando una aplicación que maneja usuarios, una data class podría ser perfecta para representar un usuario con propiedades como nombre, edad y correo electrónico. Las data classes te permiten definir estos datos de forma clara y legible.

##### 1.1.2. Objetos Inmutables

Las data classes son una buena elección cuando prefieres trabajar con objetos inmutables. Aunque Kotlin permite propiedades mutables en data classes, el paradigma funcional favorece la inmutabilidad para evitar efectos secundarios. Es decir, si prefieres que tus objetos de datos no cambien una vez creados, las data classes son una excelente opción. Ademas, proporcionan un método `copy()` que te permite crear copias inmutables de un objeto con propiedades modificadas.

```kotlin
data class User(val name: String, val age: Int, val email: String)

val jack = User(name = "Jack", age = 1, email = "jack@sd.es")
val olderJack = jack.copy(age = 2) // Crear una copia inmutable con la edad modificada
```


##### 1.1.3. Necesidad de Métodos Útiles Integrados

Kotlin genera automáticamente métodos útiles para data classes, como `equals()`, `hashCode()`, y `toString()`. Esto es muy útil para comparar instancias de data classes o para imprimir sus propiedades de forma legible. Si necesitas estas funcionalidades "gratis" sin implementarlas tú mismo, las data classes son el camino a seguir.

Los métodos generados automáticamente por Kotlin para data classes son:
- `equals()`: Compara dos instancias de la clase por igualdad estructural. Equivale a usar el operador `==`.
- `hashCode()`: Devuelve un valor hash único para cada instancia de la clase.
- `toString()`: Devuelve una representación de cadena de la instancia de la clase.

```kotlin
// uso de metodos generados equals(), hashCode() y toString()
data class User(val name: String, val age: Int)

val jack = User(name = "Jack", age = 1)
val olderJack = User(name = "Jack", age = 1)

println(jack == olderJack) // => true
println(jack.hashCode() == olderJack.hashCode()) // => true
println(jack.toString()) // => User(name=Jack, age=1)
```

##### 1.1.4. Destructuración de Objetos

Las data classes admiten la destructuración de objetos de forma nativa. Si quieres descomponer un objeto en varias variables fácilmente, las data classes te permiten hacerlo de manera elegante. Esto es especialmente útil en operaciones como iterar sobre una colección de objetos de datos y acceder a sus propiedades directamente.

```kotlin
data class User(val name: String, val age: Int)

val jane = User("Jane", 35)
val (name, age) = jane // Destructuración de objetos, asignando propiedades a variables individuales. Tiene el mismo efecto que val name = jane.name y val age = jane.age
println("$name, $age years of age") // => Jane, 35 years of age
```


##### 1.1.5. Uso con Colecciones y Operaciones Funcionales

Si trabajas frecuentemente con colecciones y realizas operaciones funcionales sobre ellas (como filtrar, mapear, etc.), las data classes pueden ser muy prácticas. Permiten representar elementos de colecciones de una manera clara y concisa, facilitando operaciones funcionales sobre esos datos.

```kotlin
data class User(val name: String, val age: Int)

val users = listOf(User("Alice", 25), User("Bob", 30), User("Charlie", 35))

val names = users.map { it.name } // Operación funcional para mapear la lista de usuarios a una lista de nombres
val adults = users.filter { it.age >= 30 } // Operación funcional para filtrar la lista de usuarios para obtener solo los mayores de 30 años
```


Como puedes ver, son bastante útiles. Úsalas cuando quieras simplicidad, claridad y funcionalidad integrada para tus objetos de datos.

#### 1.2. ¿Cómo se implementan en kotlin?

Las data classes son ideales para casos donde la principal responsabilidad de la clase es almacenar datos. De ahi que estas clases se definen con la palabra clave `'data'`. No son la mejor opción cuando tu clase necesita contener mucha lógica de negocio o cuando la herencia (más allá de implementar interfaces) es una parte crucial del diseño de tu clase.

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

Cada clase deriva de `'Any'`, y viene con una declaración de método `'hashCode()'`. Esto es el equivalente de un método `'hashCode()'` de clase _'Object'_ de Java. Este método es importante cuando se insertan instancias del objeto en colecciones, como un mapa. Al implementar este método, se debe cumplir con una serie de requisitos:

1. Cuando se invoque en el mismo objeto más de una vez durante el tiempo de ejecución sin que haya sufrido cambios, el método `'hashCode()'` debe devolver constantemente el mismo valor, dado que el objeto no se modificó.      
2. Si para dos objetos el método `'equals()'`  devuelve true, entonces llamar al método `'hashCode()'` en cada uno de ellos debería devolver el mismo valor entero.      
3. Si dos objetos no son iguales, es decir, que el método `'equals()'` devuelve false cuando se comparan, no es un requisito que cada método `'hashCode()'` del objeto devuelva valores distintos. Sin embargo, producir un entero distinto para objetos desiguales podría mejorar el rendimiento de las colecciones basadas en 'hash'.     

Las _'data classes'_ son un forma compacta y legible de devolver dos o más valores de una función. Otra alternativa, menos legible, es utilizar el tipo `'Pair'` o `'Triple'` proporcionado por Kotlin:

```kotlin
data class Result(val result: Int, val status: Boolean)

fun checkStatus() = Result(10, true)  // función que retorna un tipo 'Result'

val (result, status) = checkStatus() // usamos la desestructuración de datos para acceder a los datos
```

Aquí puedes ver un ejemplo en el que se compara una data class en java con una data class en kotlin: [data Class](https://devexpert.io/data-classes-kotlin/)


### 2. Sealed classes

Las clases selladas, o "sealed classes", son un concepto poderoso en Kotlin que te permite restringir la jerarquía de herencia. Son especialmente útiles en casos donde un valor puede tener uno de varios tipos específicos, pero no puede tener cualquier otro tipo. 

```kotlin
sealed class ResultadoOperacion {
    data class Exito(val data: String): ResultadoOperacion()
    data class Error(val error: Exception): ResultadoOperacion()
}

fun procesarResultado(resultado: ResultadoOperacion) {
    when (resultado) {
        is ResultadoOperacion.Exito -> println("Operación exitosa: ${resultado.data}")
        is ResultadoOperacion.Error -> println("Error en la operación: ${resultado.error.message}")
    }
}

```
En el ejemplo anterior, la variable `resultado` de tipo `ResultadoOperacion` puede ser de tipo `Exito` o `Error`, pero no de ningún otro tipo. Las sealed classes permiten definir un conjunto limitado de subclases que pueden ser utilizadas para representar diferentes estados o resultados de manera segura y controlada.


#### 2.1. ¿Cuándo usarlas?

Aquí te dejo algunos escenarios en los cuales es ideal usarlas:

##### 2.1.1. Modelado de Estados o Resultados Limitados

Cuando estás modelando un conjunto finito de estados para un sistema o los posibles resultados de una operación, las sealed classes son tu mejor opción. Permiten representar de manera segura y clara estos estados limitados, garantizando que todos los casos posibles sean cubiertos durante la compilación, como vimos en el ejemplo anterior.

##### 2.1.2. Uso en Patrones de Diseño Tipo "Cuando" (when)

Las sealed classes son particularmente útiles con el patrón de diseño "when" en Kotlin, ya que el compilador puede verificar si todos los casos posibles han sido cubiertos. Esto elimina la necesidad de un cláusula `else` innecesaria y aumenta la seguridad del código al garantizar que todos los casos posibles sean considerados. 

```kotlin
sealed class ResultadoOperacion {
    data class Exito(val data: String): ResultadoOperacion()
    data class Error(val error: Exception): ResultadoOperacion()
}

fun procesarResultado(resultado: ResultadoOperacion) {
    when (resultado) {
        is ResultadoOperacion.Exito -> println("Operación exitosa: ${resultado.data}")
        is ResultadoOperacion.Error -> println("Error en la operación: ${resultado.error.message}")
    }
}
```

##### 2.1.3. Definición de API Internas y Controladas

Si estás diseñando una API o un conjunto de interacciones dentro de tu módulo o librería y quieres controlar estrictamente cómo pueden ser extendidas o utilizadas las clases, las clases selladas son una excelente elección. Limitan la creación de subclases a las definidas dentro del mismo archivo, manteniendo un control sobre la extensión y uso de tu API.

```kotlin
sealed class Shape

class Circle : Shape()
class Triangle : Shape()
class Rectangle: Shape()
```

En este ejemplo, la clase `Shape` es sellada, lo que significa que solo las subclases `Circle`, `Triangle` y `Rectangle` pueden extenderla. Esto asegura que no se puedan crear subclases adicionales fuera de este archivo, manteniendo el control sobre la jerarquía de clases.

##### 2.1.4. Manejo de Eventos o Acciones Específicas

En sistemas de manejo de eventos o en la implementación de patrones como el MVI (Model-View-Intent) en desarrollo de aplicaciones, las sealed classes permiten definir un conjunto cerrado de acciones o eventos que pueden ser manejados o disparados, asegurando que todos los casos sean considerados y tratados adecuadamente.

```kotlin
sealed class Evento {
    object CargarDatos: Evento()
    data class MostrarError(val mensaje: String): Evento()
    data class MostrarDatos(val datos: List<String>): Evento()
}

fun procesarEvento(evento: Evento) {
    when (evento) {
        is Evento.CargarDatos -> println("Cargando datos...")
        is Evento.MostrarError -> println("Error: ${evento.mensaje}")
        is Evento.MostrarDatos -> println("Mostrando datos: ${evento.datos}")
    }
}

```

En este ejemplo, la clase sellada `Evento` define tres tipos de eventos posibles: `CargarDatos`, `MostrarError` y `MostrarDatos`. Cada uno de estos eventos puede ser manejado de manera específica, asegurando que todos los casos posibles sean considerados y tratados adecuadamente. El beneficio de usar sealed classes en este contexto es que el compilador te obliga a considerar todos los casos posibles, evitando errores en tiempo de ejecución.

##### 2.1.5. Simplificación de la Lógica de Negocio

Al usar sealed classes para representar diferentes tipos de operaciones o entidades con comportamientos específicos, puedes simplificar significativamente la lógica de negocio. Esto se debe a que puedes usar el tipo de la clase sellada para controlar el flujo de la lógica en tu aplicación, asegurándote de que solo se consideren las instancias permitidas.

En los ejemplos anteriores, las sealed classes se utilizan para representar diferentes resultados de operaciones y eventos, lo que simplifica la lógica de manejo de estos casos específicos. Al usar sealed classes, puedes garantizar que solo se consideren los casos permitidos y que la lógica de negocio sea más clara y concisa.k

#### 2.2. ¿Cómo usarlas?

En Kotlin una *__'sealed class'__* es una clase abstracta (no se puede crear instancias) que otras clases pueden extender. Estas subclases se definen dentro del cuerpo de la _'sealed class'_, en el mismo archivo por lo que podemos conocer todas las subclases posibles simplemente viendo el archivo.

Las _'sealed class'_ son una herramienta excelente para cuando necesitas asegurar una jerarquía cerrada de clases, lo que te permite manejar de manera exhaustiva y segura los distintos tipos definidos. Usarlas promueve un diseño de software más seguro, limpio y mantenible, especialmente en escenarios donde el conjunto de posibles tipos es conocido y limitado. Son, en cierto sentido, una extensión de las clases de enumeración.

* Podemos agregar el modificador `'abstract'`, pero esto es redundante porque estas clases son abstractas por defecto.
* No pueden tener el modificador `'open'` ni `'final'`.
* Podemos declarar clases de datos y objetos como subclases a una _'sealed class'_ (aún deben declararse en el mismo archivo).
* No pueden tener constructores públicos, ya que sus constructores son privados de forma predeterminada.

##### 2.2.1 Ejemplos Prácticos

```kotlin
// shape.kt

sealed class Shape

class Circle : Shape()
class Triangle : Shape()
class Rectangle: Shape()
```

```kotlin
sealed class ResultadoOperacion {
    data class Exito(val data: String): ResultadoOperacion()
    data class Error(val error: Exception): ResultadoOperacion()
}
```

Este último ejemplo ilustra cómo una operación puede terminar en éxito o error, y cómo las sealed classes pueden ser usadas para modelar estos dos resultados posibles de manera segura y controlada.

### 3. Generics

Los genéricos son una herramienta poderosa en programación que te permite escribir código más flexible y reutilizable al permitirte trabajar con tipos de datos aún no especificados.

#### 3.1. ¿Cuándo usarlos?

Aquí tienes algunas situaciones clave en las que es especialmente útil usar genéricos:

##### 3.1.1. Para Crear Colecciones Tipo-Seguras

Usa genéricos para crear colecciones que pueden contener cualquier tipo de objetos pero manteniendo la seguridad de tipo. Esto te permite tener, por ejemplo, una lista de `Int` o una lista de `String`, asegurando que todos los elementos son del tipo especificado.

##### 3.1.2. Cuando Necesitas Clases, Interfaces o Funciones Reutilizables

Cuando quieras que tu clase, interfaz o función pueda trabajar con diferentes tipos de datos sin estar ligada a ninguno en particular. Los genéricos te permiten escribir un código que puede ser reutilizado con diferentes tipos, aumentando la reusabilidad y reduciendo la redundancia.

##### 3.1.3. Para Implementar Algoritmos Genéricos

Cuando estés implementando algoritmos que pueden ser aplicados independientemente del tipo de datos, los genéricos son la solución. Esto es útil en algoritmos de ordenación, búsqueda, y otras operaciones sobre colecciones que no dependen del tipo específico de los elementos.

##### 3.1.4. Para Aumentar la Legibilidad y la Seguridad del Código

Los genéricos te ayudan a escribir código más claro y seguro, evitando el uso excesivo de casting y reduciendo la posibilidad de errores en tiempo de ejecución relacionados con tipos incorrectos.

##### 3.1.5. Para Desarrollar Bibliotecas y Frameworks

Si estás desarrollando una biblioteca o framework que será utilizado en una variedad de contextos y con diferentes tipos de datos, los genéricos te permiten proporcionar componentes flexibles y tipo-seguros que pueden ser personalizados por los usuarios según sus necesidades específicas.

#### 3.2. ¿Como usarlos?

Los genéricos son fundamentales cuando buscas escribir código más abstracto, flexible y reutilizable, permitiéndote definir comportamientos que son independientes del tipo de datos con los que trabajan. Su uso correcto puede llevar a un diseño de software más limpio, seguro y fácil de mantener. Los siguientes conceptos son útiles para entender cómo funcionan los genéricos en Kotlin:

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

##### 3.2.1. La palabra clave 'out'

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

##### 3.2.2. La palabra clave 'in'

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

##### 3.2.3. Star projections

Hay situaciones en las que no es importante el tipo específico de un valor. Para ello usamos el operador `'*'` o _'star projection'_:

```kotlin
fun printArray(array: Array<*>) {
    array.forEach { println(it) }
}

// Podemos pasar una matriz de cualquier tipo al método 'printArray()'
printArray(arrayOf(1,2,3))

printArray(arrayOf("hello", "World!!", 5))
```

##### 3.2.4. Generic functions

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

##### 3.2.5. Generic constraints

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

#### 4.1. ¿Cuándo usarlas?

Para explicar cuándo usar una Inner Class y cuándo optar por una Nested Class, podemos utilizar analogías que ayuden a comprender su propósito y diferencias en contextos reales. Es posible que necesites releer esta sección varias veces para comprender completamente las diferencias entre las dos.

##### 4.1.1. Inner Class: El Miembro de la Familia

Imagina que una clase es como una casa familiar. Una Inner Class sería como un miembro de esta familia que vive en la casa. Este miembro tiene acceso completo a todos los recursos y secretos de la casa (la clase externa) porque es parte integral de la familia. Puede interactuar libremente con los demás miembros y utilizar todo lo que está en la casa.

**¿Cuándo usarla?** Utiliza una Inner Class cuando necesites una clase que esté estrechamente vinculada a la clase externa y que necesite acceder a sus miembros, incluidos los privados. Es útil cuando tu clase interna debe "conocer" a la clase externa y colaborar estrechamente con ella, como un miembro de la familia que trabaja en un proyecto familiar.

##### 4.1.2. Nested Class: El Vecino Independiente

Por otro lado, una Nested Class (específicamente una clase anidada estática en lenguajes que lo soportan) es como un vecino que vive al lado de tu casa. Aunque comparten la misma localización (el archivo fuente), este vecino tiene su propia vida y no necesita entrar a tu casa para conseguir lo que necesita. No tiene acceso directo a tus recursos privados, pero aún así, puede interactuar con la familia (la clase externa) en cierta medida, mediante interfaces públicas.

**¿Cuándo usarla?** Opta por una Nested Class cuando necesites agrupar clases que están relacionadas, pero que no necesitan acceso directo a los miembros de la clase externa. Es ideal para situaciones en las que deseas mantener una separación clara y una independencia funcional, como un vecino que colabora en proyectos comunitarios sin necesidad de acceso a tu casa.

##### 4.1.3. Consideraciones Conceptuales

* **Acoplamiento:** Si tu clase interna está tan acoplada a la clase externa que no tiene sentido sin ella, una Inner Class es apropiada. Es una relación íntima y directa, como la de los miembros de una familia.
* **Independencia y Modularidad:** Si tu clase puede funcionar de manera independiente de la clase externa, y especialmente si puede ser útil para otras clases, entonces una Nested Class (estática) es la mejor elección. Piensa en ella como un vecino que tiene su propia casa y vida pero comparte una comunidad contigo.


#### 4.2. ¿Cómo usarlas?
La elección entre Inner Class y Nested Class depende de la relación que necesitas que tenga tu clase con su clase externa. Considera si tu clase interna necesita estar íntimamente ligada y tener un acceso profundo a la clase externa (Inner Class) o si funciona mejor como una entidad independiente que, aunque relacionada, no necesita acceso directo a los recursos internos de la clase externa (Nested Class).

##### 4.2.1. Nested classes

Al igual que las funciones, Kotlin permite las clases internas, es decir, clases definidas dentro de otra clase. Son equivalentes a las clases internas estáticas en Java.

```kotlin
class OuterClass {

    class NestedClass {
        fun nestedClassFunc() { }
    }
}

val nestedClass = OuterClass.NestedClass().nestedClassFunc()
```

##### 4.2.2. Inner class

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

##### 4.2.3 Diferencias entre Nested e Inner classes

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
Las enumeraciones, o "enums", son tipos especiales en programación que definen un conjunto de constantes nombradas, mejorando la legibilidad y seguridad de tu código. 

#### 5.1. ¿Cuándo usarlas?
Son útiles en varios contextos:

##### 5.1.1. Representar un Conjunto Fijo de Constantes

Usa enums cuando necesites representar un grupo fijo de constantes relacionadas. Por ejemplo, los días de la semana, los meses del año, o los estados de un pedido (NUEVO, EN PROCESO, ENVIADO, ENTREGADO) son excelentes candidatos para ser modelados como enumeraciones.

##### 5.1.2. Control de Flujo Basado en Valores Limitados

Cuando tu lógica de negocio implica ramificaciones basadas en un conjunto limitado de valores posibles, las enumeraciones hacen tu código más legible y menos propenso a errores, permitiéndote usar `switch` o `when` para gestionar diferentes casos de manera clara.

##### 5.1.3. Evitar Valores Mágicos

Los "valores mágicos" son números o cadenas literales con significado especial que pueden hacer que el código sea difícil de entender y mantener. Reemplazar estos valores por enums ayuda a evitar este problema, dando un nombre significativo a cada valor.

##### 5.1.4. Asegurar la Consistencia

Si tienes una variable que solo debería tomar uno de varios valores predefinidos, definir esos valores como un enum asegura que la variable no pueda contener ningún otro valor, lo que mejora la integridad de tus datos.

##### 5.1.5. Agrupar Datos Relacionados

Algunos lenguajes permiten que las enums contengan no solo nombres de constantes, sino también propiedades y métodos. Esto es útil para agrupar datos y comportamientos relacionados, por ejemplo, asociar cada estado de un pedido con un mensaje específico o una acción.

#### 5.2. ¿Cómo usarlas?


Las enumeraciones son una herramienta poderosa para mejorar la legibilidad, la seguridad de tipo y la integridad de tu código. Son especialmente útiles cuando trabajas con un conjunto cerrado de valores que conoces de antemano. Usar enums te ayuda a escribir código más claro y mantenible, asegurando que tus variables solo contengan valores válidos.

**Las clases de enumeración son similares a los tipos _'enum'_ de Java**. El uso más básico de las clases de enumeración es la implementación de enumeraciones de tipos seguros. Cada constante de la enumeración es un objeto. Las constantes de la enumeración están separadas por comas.

##### 5.2.1 Ejemplo práctico

Imagina que estás desarrollando un juego y necesitas representar las direcciones en las que un jugador puede moverse. Podrías usar una enum para esto:

```kotlin
enum class Direccion {
    NORTE, SUR, ESTE, OESTE
}
```

Este enfoque mejora la legibilidad del código y asegura que solo se puedan usar las direcciones definidas en la enum, en lugar de cadenas o números arbitrarios.

##### 5.2.2. Constructores de Enumeración

Ademas, las enumeraciones pueden tener constructor:

```kotlin
enum class Direction(val angle: Int) {
    North(90), West(180), South(270), East(0)
}
```

##### 5.2.3. Clases anónimas en enumeraciones


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

##### 5.2.4. Métodos predeterminados de Enumeración

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

* [data class](https://devexpert.io/data-classes-kotlin/)
* [class enum](https://www.baeldung.com/kotlin/enum)
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
