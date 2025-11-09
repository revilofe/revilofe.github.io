# U4.1 - Kotlin

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción a Kotlin


### ¿Qué es Kotlin?

* Lenguaje de programación de código abierto
* De tipo estático que se dirige a JVM, Android, JavaScript y Native
* Desarrollado por JetBrains desde 2010
* Primera versión oficial 1.0 en febrero de 2016
* Diseñado para ser productivo y pragmático

Note: Kotlin es un lenguaje moderno diseñado por JetBrains, la empresa creadora de IntelliJ IDEA. Aunque comenzó en 2010, su primera versión estable fue en 2016. Es un lenguaje multiplataforma que puede ejecutarse en la JVM (como Java), compilarse a JavaScript para navegadores, o ejecutarse de forma nativa. Su objetivo principal es ser un lenguaje productivo y pragmático, es decir, que ayude a los desarrolladores a escribir código de manera eficiente y con menos errores.


### Objetivos de Kotlin

* Construir un lenguaje productivo y pragmático
* Proporcionar todas las características que un desarrollador necesita
* Fácil de usar y aprender
* Interoperable con otros lenguajes de JVM
* Multiparadigma: orientado a objetos, procedimental y funcional

Note: Kotlin fue diseñado con objetivos claros: ser productivo (permitir hacer más con menos código), pragmático (resolver problemas reales), y fácil de usar. A diferencia de Java, no te obliga a usar un paradigma específico. Puedes escribir código orientado a objetos clásico, código procedimental con funciones, o usar programación funcional. Esta flexibilidad es una de sus grandes ventajas.


### Características principales I

* 100% interoperable con Java
* Compatible con Java 6+
* Ejecutable en la JVM
* Transpilable a JavaScript
* Ejecutable de forma nativa (interoperable con C y Objective-C)

Note: Una de las características más importantes es la interoperabilidad total con Java. Puedes usar librerías Java en Kotlin y viceversa sin problemas. Es compatible con Java 6 y superiores, lo que significa que puede ejecutarse en la mayoría de dispositivos Android. Además, el código Kotlin puede compilarse a bytecode de JVM, transpilarse a JavaScript para web, o compilarse a código nativo para ejecutarse sin JVM.


### Características principales II

* No requiere punto y coma al final de las sentencias
* Bloques de código delimitados por llaves `{ }`
* Soporte de primera clase para valores constantes
* Colecciones inmutables (ideal para programación paralela)
* Funciones de nivel superior (sin necesidad de clases)

Note: La sintaxis de Kotlin es más limpia que Java: no necesitas punto y coma al final de cada línea. Los bloques de código usan llaves como Java, pero de manera más flexible. Kotlin pone énfasis en la inmutabilidad: puedes declarar valores constantes fácilmente y las colecciones tienen versiones inmutables por defecto, lo que hace el código más seguro en entornos paralelos. A diferencia de Java, puedes definir funciones directamente sin tener que crear una clase.


### Características principales III

* Funciones como ciudadanos de primera clase
* Soporte completo para lambdas (funciones anónimas)
* No hay palabra clave `static`
* Clases de datos especiales para contener información
* Todo puede ser una expresión: `if`, `for`, `when`

Note: En Kotlin, las funciones son "ciudadanos de primera clase", lo que significa que pueden pasarse como parámetros, asignarse a variables y devolverse desde otras funciones. Los lambdas (funciones anónimas) están completamente integrados en el lenguaje. No existe la palabra clave `static` de Java, pero hay mejores alternativas. Las clases de datos (`data class`) simplifican enormemente la creación de clases que solo contienen datos. Y algo muy potente: estructuras como `if` o `when` son expresiones que pueden devolver valores, no solo sentencias.

---

## Kotlin en línea de comandos


### Instalación y comandos básicos

* Instalador desde: kotlinlang.org/docs/command-line.html
* Compilar aplicación: `kotlinc name.kt -include-runtime -d name.jar`
* Ejecutar programa: `java -jar name.jar`
* Consola REPL: `kotlinc-jvm`
* Ejecutar scripts: `kotlinc -script name.kts [params]`

Note: Kotlin puede usarse desde la línea de comandos sin necesidad de un IDE. El compilador `kotlinc` convierte archivos .kt a archivos JAR ejecutables. La opción `-include-runtime` incluye las librerías necesarias de Kotlin en el JAR. Una vez compilado, se ejecuta con Java como cualquier programa Java. La consola REPL (Read-Eval-Print Loop) permite ejecutar código Kotlin interactivamente, muy útil para probar cosas rápidamente. Los scripts .kts permiten ejecutar código Kotlin sin compilar previamente.


### Compilación de librerías

* Compilar librería sin runtime: `kotlinc name.kt -d name.jar`
* Ejecutar con classpath: `kotlin -classpath name.jar HelloKt`
* HelloKt es el nombre de la clase principal generada
* El nombre de la clase se genera desde el nombre del archivo

Note: Cuando creas una librería en Kotlin (no una aplicación ejecutable), no incluyes el runtime. Esto hace el JAR más pequeño. Para ejecutar código que usa esta librería, especificas el classpath con `-classpath`. Kotlin genera automáticamente una clase principal cuyo nombre es el nombre del archivo con "Kt" al final. Por ejemplo, si tu archivo se llama Hello.kt, la clase generada será HelloKt.

---

## Sintaxis básica


### Función main

El punto de entrada de todo programa Kotlin:

```kotlin
// Sintaxis moderna (Kotlin 1.3+)
fun main() {
    println("Hello World!")
}

// Sintaxis con parámetros
fun main(args: Array<String>) {
    println("Hello World!")
}
```

Note: Como en Java, el punto de entrada de un programa Kotlin es la función `main`. A partir de Kotlin 1.3, los parámetros son opcionales si no los vas a usar. La función `println` imprime en consola con salto de línea automático. Kotlin infiere automáticamente muchos tipos, por lo que el código es más limpio que en Java.


### Declaraciones de nivel superior

* Funciones y variables pueden declararse fuera de clases
* Se llaman declaraciones de "nivel superior" o "top-level"
* Útil para funciones de utilidad
* Pertenecen directamente a un paquete

Note: A diferencia de Java, en Kotlin no necesitas crear una clase para definir funciones o variables. Puedes declararlas directamente en un archivo, a nivel de paquete. Esto se llama declaraciones de nivel superior o "top-level". Es muy útil para funciones de utilidad o constantes globales que no tienen sentido dentro de una clase específica.


### Convenciones de nomenclatura I

* Archivos: si contienen una sola clase, mismo nombre con extensión .kt
* Si contienen varias clases o solo funciones: formato UpperCamelCase
* Ejemplo: `ProcessDeclarations.kt`
* Paquetes: siempre en minúsculas sin guiones bajos
* Ejemplo: `org.example.myproject`

Note: Kotlin sigue convenciones similares a Java pero con algunas diferencias. Los archivos que contienen una sola clase deben tener el mismo nombre que la clase. Si un archivo contiene varias clases o solo declaraciones de nivel superior, su nombre debe describir su contenido en formato UpperCamelCase (primera letra de cada palabra en mayúscula). Los nombres de paquetes van siempre en minúsculas, sin guiones bajos, usando puntos para separar niveles.


### Convenciones de nomenclatura II

Ejemplos de convenciones en Kotlin:

```kotlin
// Clases y objetos: UpperCamelCase
open class DeclarationProcessor { ... }
object EmptyDeclarationProcessor : DeclarationProcessor() { ... }

// Funciones y variables: lowerCamelCase
fun processDeclarations() { ... }
var declarationCount = ...

// Constantes: MAYÚSCULAS con guiones bajos
const val MAX_COUNT = 8
val USER_NAME_FIELD = "UserName"
```

Note: Las clases y objetos usan UpperCamelCase (primera letra de cada palabra en mayúscula). Las funciones, propiedades y variables locales usan lowerCamelCase (primera letra en minúscula, resto de palabras con primera letra mayúscula). Las constantes (marcadas con `const`) usan MAYÚSCULAS con guiones bajos separando palabras. Esta es la convención estándar de Kotlin.

---

## Variables y tipos básicos


### Todo es un objeto

* En Kotlin todo es un objeto
* Puedes llamar funciones y propiedades en cualquier variable
* Algunos tipos tienen representación primitiva interna
* Para el usuario se comportan como clases ordinarias
* Mejora sobre los tipos primitivos de Java

Note: Una diferencia fundamental con Java es que en Kotlin todo es un objeto. No hay tipos primitivos separados como en Java (int, boolean, etc.). Aunque internamente Kotlin optimiza y puede usar primitivos en tiempo de ejecución para eficiencia, desde el punto de vista del programador todo es un objeto con métodos y propiedades. Esto hace el lenguaje más consistente y fácil de usar.


### Declaración de variables: val vs var

Diferencias entre val (inmutable) y var (mutable):

```kotlin
val fooVal = 10     // Inmutable (read-only), no puede reasignarse
var fooVar = 10     // Mutable, puede cambiar su valor
fooVar = 20         // OK

val otherVal        // Declaración sin inicialización
otherVal = "My Value"   // Asignación posterior (solo una vez)
```

Note: Kotlin distingue entre valores constantes (`val`) y variables mutables (`var`). Los `val` son inmutables: una vez asignados no pueden cambiar. Los `var` son mutables: puedes cambiar su valor cuantas veces quieras, pero siempre del mismo tipo. La recomendación es usar `val` siempre que sea posible, ya que hace el código más seguro y fácil de entender. Solo usa `var` cuando realmente necesites cambiar el valor. Puedes declarar un `val` en una línea y asignarle valor después, pero solo una vez.


### Inferencia de tipos

Kotlin puede deducir tipos automáticamente:

```kotlin
val foo: Int = 7        // Tipo explícito
val bar = 10            // Kotlin infiere Int automáticamente

val hello: String       // Si no se inicializa, tipo obligatorio
hello = "World"

var name = "Ana"        // Kotlin infiere String
// name = 5             // ERROR: el tipo no puede cambiar
```

Note: Kotlin tiene inferencia de tipos muy potente. En la mayoría de casos no necesitas especificar el tipo explícitamente porque Kotlin lo deduce del valor asignado. Sin embargo, si declaras una variable sin inicializarla, debes indicar el tipo porque Kotlin no puede adivinarlo. Una vez determinado el tipo (explícita o implícitamente), no puede cambiarse. Si declaras una variable como String, no puedes luego asignarle un número.


### Tipos numéricos enteros

Kotlin ofrece cuatro tipos de enteros:

* `Byte`: 8 bits (-128 a 127)
* `Short`: 16 bits (-32,768 a 32,767)
* `Int`: 32 bits (-2³¹ a 2³¹-1)
* `Long`: 64 bits (-2⁶³ a 2⁶³-1)

Ejemplos de declaración:

```kotlin
val int: Int = 32
val long: Long = 64L        // Sufijo L para Long
val hexadecimal: Int = 0x16 // Notación hexadecimal
val binary: Int = 0b101     // Notación binaria
```

Note: Kotlin proporciona cuatro tipos de enteros con diferentes tamaños. `Int` es el tipo por defecto cuando escribes un número entero. Para `Long` añades el sufijo L. También soporta notación hexadecimal (prefijo 0x) y binaria (prefijo 0b). Por defecto, cualquier número entero sin sufijo se infiere como `Int` si cabe en 32 bits, o `Long` si es mayor.


### Tipos numéricos decimales

Kotlin proporciona dos tipos para decimales:

* `Float`: 32 bits, precisión de ~6-7 dígitos decimales
* `Double`: 64 bits, precisión de ~15-16 dígitos decimales

Ejemplos de uso:

```kotlin
val double: Double = 64.0   // Por defecto es Double
val float: Float = 32.0F    // Sufijo F o f para Float

val a = 1       // Kotlin infiere Int
val b = 1L      // Kotlin infiere Long
val c = 3.14    // Kotlin infiere Double
val d = 2.7123F // Kotlin infiere Float
```

Note: Para decimales, Kotlin ofrece `Float` y `Double`. Por defecto, cualquier número decimal se infiere como `Double` si no especificas tipo o sufijo. Para `Float` debes añadir el sufijo F o f. Es importante entender que estos tipos tienen precisión limitada. Para cálculos financieros o donde necesites precisión exacta, deberías usar la clase `BigDecimal`.


### Legibilidad numérica y conversiones

Mejora la legibilidad y convierte entre tipos:

```kotlin
// Guiones bajos para legibilidad
val million = 1_000_000
val creditCard = 1234_5678_9012_3456

// Conversiones explícitas
val int = 100
val long = int.toLong()
val double = int.toDouble()
val direct = 25.toLong()
```

Note: Kotlin permite usar guiones bajos en números para mejorar la legibilidad. Son ignorados por el compilador pero hacen más fácil leer números grandes. A diferencia de Java, las conversiones entre tipos numéricos deben ser explícitas. No hay conversión automática. Esto previene errores y hace el código más claro. Cada tipo numérico tiene métodos `toXxx()` para convertir a otros tipos: `toInt()`, `toLong()`, `toDouble()`, etc.


### Caracteres

El tipo Char y caracteres especiales:

```kotlin
val char: Char = 'a'

// Caracteres especiales con barra invertida
val tab = '\t'      // Tabulación
val newline = '\n'  // Nueva línea
val backspace = '\b'
val quote = '\''    // Comilla simple
val doubleQuote = '\"'  // Comilla doble
val backslash = '\\'    // Barra invertida
val dollar = '\$'       // Símbolo dólar
```

Note: Los caracteres en Kotlin se representan con el tipo `Char` y se escriben entre comillas simples. A diferencia de Java, los caracteres NO son números en Kotlin, son un tipo completamente separado. Los caracteres especiales se escapan con barra invertida: \n para nueva línea, \t para tabulación, etc. Esto es importante cuando necesitas incluir caracteres especiales o comillas dentro de strings.


### Conversión de caracteres

Convertir caracteres a números:

```kotlin
fun decimalDigitValue(c: Char): Int {
    if (c !in '0'..'9')
        throw IllegalArgumentException("Out of range")
    return c.toInt() - '0'.toInt()
}

// Uso
val digit = '5'
val value = decimalDigitValue(digit)  // 5
```

Note: Aunque los caracteres no son números, puedes convertirlos explícitamente con `toInt()`. Esto te da el valor Unicode del carácter. Para convertir un dígito carácter ('0'-'9') a su valor numérico (0-9), restas el valor Unicode de '0'. Este patrón es común cuando procesas texto que contiene números.


### Booleanos

Valores booleanos y operadores lógicos:

```kotlin
val myTrue: Boolean = true
val myFalse: Boolean = false
val boolNull: Boolean? = null  // Boolean nullable

// Operadores lógicos
println(myTrue || myFalse)  // OR lógico
println(myTrue && myFalse)  // AND lógico
println(!myTrue)            // NOT lógico
```

Note: El tipo `Boolean` representa valores de verdad: true o false. Los operadores lógicos son `||` (OR), `&&` (AND) y `!` (NOT). Kotlin usa evaluación perezosa: en `a || b`, si `a` es true, no evalúa `b`. En `a && b`, si `a` es false, no evalúa `b`. Esto puede ser importante si `b` tiene efectos secundarios o puede lanzar excepciones. Además, Kotlin permite Boolean nullable (`Boolean?`) que puede tener valores true, false o null.

---

## Strings


### Cadenas de texto básicas

Las cadenas son secuencias inmutables de caracteres:

```kotlin
val fooString = "My String Is Here!"
val barString = "Printing on a new line?\nNo Problem!"
val bazString = "Do you want to add a tab?\tNo Problem!"

println(fooString)
println(barString)
println(bazString)
println("John Doe"[2])              // => 'h'
println("John Doe".startsWith("J")) // => true
```

Note: Las cadenas en Kotlin son secuencias inmutables de caracteres representadas por el tipo `String`. Se crean con comillas dobles. Los caracteres especiales se escapan con barra invertida: \n para nueva línea, \t para tabulación. Puedes acceder a caracteres individuales con corchetes (indexación como en arrays), y tienen muchos métodos útiles como `startsWith()`, `endsWith()`, `contains()`, etc.


### Acceso e iteración en Strings

Acceder a caracteres e iterar sobre strings:

```kotlin
val str = "Kotlin"

// Acceso por índice
println(str[0])     // 'K'
println(str[5])     // 'n'

// Iteración con for
for (c in str) {
    println(c)      // K, o, t, l, i, n
}
```

Note: Las cadenas en Kotlin se comportan como arrays de caracteres. Puedes acceder a cualquier carácter por su índice con corchetes. Los índices empiezan en 0. También puedes iterar sobre todos los caracteres de una cadena con un bucle `for..in`. Esto es más limpio y seguro que usar índices manualmente.


### Concatenación de Strings

Unir cadenas con el operador +:

```kotlin
val s1 = "abc"
val s2 = 1
val s3 = "def"

// Operador +
val result = s1 + s2        // "abc1"
println(result + s3)        // "abc1def"

// Al menos uno debe ser String
val combined = "The answer: " + 42
```

Note: El operador `+` concatena strings. Si uno de los operandos es String, el otro se convierte automáticamente a String. Esto funciona con números, booleanos, y cualquier objeto que tenga un método `toString()`. Sin embargo, ten cuidado: concatenar muchas strings en un bucle es ineficiente. Para esos casos, usa `StringBuilder` o join.


### Raw Strings (cadenas sin procesar)

Cadenas multilínea sin escapar caracteres:

```kotlin
val rawString = """
fun helloWorld(val name : String) {
    println("Hello, world!")
}
val hello = $who
val result = ${2 + 2}
"""

// Eliminar espacios con trimMargin
val text = """
    |Tell me and I forget.
    |Teach me and I remember.
    |Involve me and I learn.
    |(Benjamin Franklin)
    """.trimMargin()
```

Note: Las raw strings o cadenas sin procesar se delimitan con triple comilla ("""). Pueden contener múltiples líneas y cualquier carácter sin necesidad de escapar (excepto las triple comillas). Son muy útiles para textos multilínea, expresiones regulares, o código SQL. El método `trimMargin()` elimina espacios en blanco usando el carácter | como marcador de margen. También funcionan los string templates (variables con $).


### String Templates I

Insertar valores y expresiones en strings:

```kotlin
val name = "John Doe"
val age = 40

// Variable simple con $
println("$name has ${name.length} characters")
// => John Doe has 8 characters

// Expresión con ${}
println("You are ${if (age > 60) "old" else "young"}")
// => You are young
```

Note: Los string templates son una forma elegante de insertar valores en strings. Usa `$` seguido del nombre de una variable para insertar su valor. Para expresiones más complejas, usa `${}` con la expresión dentro de las llaves. Esto es mucho más legible que concatenar con `+` y más eficiente. Puedes poner cualquier expresión válida de Kotlin dentro de `${}`: operaciones, llamadas a funciones, if-else, etc.


### String Templates II

Templates avanzados y símbolo $ literal:

```kotlin
// Template con llamada a método
val text = "KOTLIN"
println("Lowercase: ${text.lowercase()}")
// => Lowercase: kotlin

// Representar el símbolo $ literal
val price = """
${'$'}9.99
"""
println(price)  // => $9.99
```

Note: Dentro de `${}` puedes llamar a métodos del objeto. Muy útil para transformaciones rápidas. Para representar el símbolo `$` literal en un string (especialmente en raw strings), usa la sintaxis `${'$'}`. Esto es necesario porque `$` tiene significado especial en templates.

---

## Arrays


### Creación de Arrays I

Crear arrays con arrayOf():

```kotlin
// Array con diferentes tipos (Any)
val cardNames = arrayOf("Jack", "Queen", "King", 3, false)
println(cardNames[1])   // => Queen

// Array del mismo tipo
val myArray = arrayOf<Int>(1, 2, 3, 4)
println(myArray.contentToString())  // => [1, 2, 3, 4]
```

Note: Los arrays en Kotlin se representan con la clase `Array`. La función `arrayOf()` crea un array con los elementos que le pases. Si no especificas tipo, Kotlin infiere el tipo común más específico. Si los elementos son de diferentes tipos, el array será de tipo `Any`. Para forzar un tipo específico, usa `arrayOf<Tipo>()`. El método `contentToString()` es útil para imprimir el contenido del array.


### Creación de Arrays II

Arrays de tipos primitivos especializados:

```kotlin
// Arrays de tipos primitivos
val cards = intArrayOf(10, 11, 12)  // IntArray
println("${cards[1]}")              // => 11

// Otros arrays primitivos
val longArray = longArrayOf(1L, 2L, 3L)
val charArray = charArrayOf('a', 'b', 'c')
val doubleArray = doubleArrayOf(1.0, 2.0, 3.0)
```

Note: Para arrays de tipos primitivos (Int, Long, Char, Double, etc.), Kotlin proporciona funciones especiales como `intArrayOf()`, `longArrayOf()`, etc. Estas son más eficientes que `arrayOf()` porque evitan el overhead de boxing/unboxing. Siempre que trabajes con tipos primitivos, usa estas versiones especializadas. La diferencia de rendimiento puede ser significativa en arrays grandes o código crítico.


### Array con constructor

Crear arrays con función generadora:

```kotlin
// Constructor Array(tamaño, función generadora)
val allCards = Array(12) { i -> i + 1 }
println("${allCards.first()} - ${allCards.last()}")
// => 1 - 12

// Ejemplo: array de cuadrados
val squares = Array(5) { i -> i * i }
// [0, 1, 4, 9, 16]
```

Note: Además de `arrayOf()`, puedes crear arrays con el constructor `Array(tamaño, función)`. El primer parámetro es el tamaño del array. El segundo es una función lambda que recibe el índice y devuelve el valor para esa posición. Esto es muy útil para generar arrays con patrones. La lambda recibe el índice (0, 1, 2, ...) y tú decides qué valor poner en cada posición.


### Iteración sobre Arrays I

Iterar con índices usando la propiedad indices:

```kotlin
val cardNames = arrayOf("Jack", "Queen", "King")

// Iterar con índices
for (index in cardNames.indices) {
    println("Element $index is ${cardNames[index]}")
}
// Element 0 is Jack
// Element 1 is Queen
// Element 2 is King
```

Note: Para iterar sobre un array con índices, usa la propiedad `indices` que devuelve un rango con todos los índices válidos (0 hasta size-1). Esto es más seguro que usar un rango manual porque no puede haber errores de uno más/menos (off-by-one errors). Dentro del bucle accedes a cada elemento con `array[index]`.


### Iteración sobre Arrays II

Iterar con índice y valor simultáneamente:

```kotlin
val cardNames = arrayOf("Jack", "Queen", "King")

// Iterar con valor e índice
for ((index, value) in cardNames.withIndex()) {
    println("$index - $value")
}
// 0 - Jack
// 1 - Queen
// 2 - King
```

Note: Cuando necesitas tanto el índice como el valor, usa `withIndex()`. Esta función devuelve pares (índice, valor) que puedes desestructurar en el for con paréntesis. La desestructuración `(index, value)` es una forma elegante de extraer ambos valores del par. Este patrón es muy común en Kotlin y hace el código más legible que mantener un contador manual.

---

## Packages e Imports


### Packages

Organizar código en paquetes:

```kotlin
package com.example.kotlin

class MyClass { /*...*/ }

fun saySomething(): String { /*...*/ }
```

Note: La palabra clave `package` funciona como en Java. El nombre del paquete construye el "Fully Qualified Name" (FQN) de clases y funciones. En el ejemplo, el FQN de la clase es `com.example.kotlin.MyClass`. Como Kotlin soporta funciones de nivel superior, la función `saySomething()` tendría el FQN `com.example.kotlin.saySomething`. Los paquetes deben escribirse en minúsculas sin guiones bajos. Si no especificas paquete, el contenido pertenece al paquete "default".


### Imports

Importar clases, funciones y objetos:

```kotlin
// Importar clase/función específica
import foo.Bar

// Resolver conflictos con 'as'
import foo.Bar
import bar.Bar as bBar

// Importar todo el contenido
import foo.*
```

Note: Los imports en Kotlin funcionan similar a Java, pero con una diferencia importante: puedes importar no solo clases, sino también funciones de nivel superior, propiedades y objetos. Si hay conflicto de nombres entre dos imports, usa la palabra clave `as` para darle un alias. El import con asterisco (*) importa todo el contenido del paquete. Ten cuidado: aunque funciona, puede hacer el código menos claro y puede causar conflictos.


### Imports por defecto

Paquetes importados automáticamente:

* kotlin.*
* kotlin.annotation.*
* kotlin.collections.*
* kotlin.comparisons.*
* kotlin.io.*
* kotlin.ranges.*
* kotlin.sequences.*
* kotlin.text.*

Note: Kotlin importa automáticamente varios paquetes estándar. No necesitas importarlos manualmente. El paquete `kotlin.*` contiene tipos básicos como Int, String, etc. El paquete `kotlin.collections.*` incluye List, Map, Set y sus funciones. Dependiendo de la plataforma (JVM, JS, Native), se importan paquetes adicionales. En JVM también se importa `java.lang.*` automáticamente.

---

## Control de flujo


### Bucle for I

Iterar sobre rangos y strings:

```kotlin
// Iterar sobre String
for (c in "hello") {
    println(c)  // h, e, l, l, o
}

// Iterar sobre rango
for (i in 1..3) {
    println(i)  // 1, 2, 3
}
```

Note: El bucle `for` en Kotlin es diferente al de Java. No usas inicialización, condición e incremento. En su lugar, iteras sobre cualquier cosa que proporcione un iterador: rangos, colecciones, strings, etc. El rango `1..3` incluye tanto 1 como 3. Es una forma más legible y menos propensa a errores que el for tradicional de C/Java.


### Bucle for II

Rangos con downTo, step y until:

```kotlin
// Descendente con paso
for (i in 6 downTo 0 step 2) {
    println(i)  // 6, 4, 2, 0
}

// Rango excluyente
for (i in 1 until 5) {
    println(i)  // 1, 2, 3, 4 (no incluye 5)
}
```

Note: Kotlin ofrece varios operadores para rangos. `downTo` crea un rango descendente. `step` cambia el incremento (por defecto es 1). `until` crea un rango que excluye el límite superior (1 until 5 es 1, 2, 3, 4 sin incluir 5). Estos operadores se pueden combinar para crear rangos complejos de forma legible.


### Bucles while y do-while

Bucles clásicos de repetición:

```kotlin
var x = 10
while (x > 0) {
    x--
}

// do-while: ejecuta al menos una vez
do {
    val y = retrieveData()
} while (y != null)  // 'y' es visible aquí
```

Note: Los bucles `while` y `do-while` funcionan exactamente igual que en Java. `while` verifica la condición antes de ejecutar el bloque. `do-while` ejecuta el bloque al menos una vez y luego verifica la condición. Una diferencia con Java: en `do-while`, la variable declarada dentro del bloque es visible en la condición.


### if como expresión I

El if devuelve un valor en Kotlin:

```kotlin
// if tradicional
var max = a
if (a < b) max = b

// if como expresión
val max = if (a > b) a else b

// Con bloques
val max = if (a > b) {
    println("a is greater")
    a
} else {
    println("b is greater")
    b
}
```

Note: En Kotlin, `if` es una expresión que devuelve un valor, no solo una sentencia. Esto elimina la necesidad del operador ternario (`? :`) de Java. Cuando usas `if` como expresión, debes incluir la parte `else` porque la expresión debe devolver algo en ambos casos. Si usas bloques, la última expresión del bloque es el valor devuelto.


### when sin argumentos

Alternativa limpia a if-else-if:

```kotlin
when {
    x.isOdd() -> print("x is odd")
    x.isEven() -> print("x is even")
    else -> print("x is funny")
}
```

Note: `when` sin argumentos funciona como una cadena `if-else if-else` más limpia. Cada condición es una expresión booleana. Se ejecuta el bloque de la primera condición que sea verdadera. La rama `else` es opcional si las otras ramas cubren todos los casos posibles. Esto es útil cuando tienes múltiples condiciones que no están relacionadas con un solo valor.


### when con argumentos I

Similar al switch pero más potente:

```kotlin
when (x) {
    1 -> print("x == 1")
    2 -> print("x == 2")
    else -> {
        println("none of the above")
    }
}
```

Note: `when` con un argumento es similar al `switch` de Java pero mucho más potente. Compara el valor del argumento con cada rama. A diferencia de Java, no necesitas `break` porque no hay fall-through: solo se ejecuta una rama. El `else` es opcional si las otras ramas cubren todos los valores posibles. Puedes usar bloques (con llaves) en cualquier rama si necesitas múltiples sentencias.


### when con argumentos II

When como expresión que devuelve valores:

```kotlin
val result = when (i) {
    0, 21 -> "0 or 21"
    in 1..20 -> "in the range 1 to 20"
    else -> "none of the above"
}
println(result)
```

Note: `when` es también una expresión, como `if`. Cuando lo usas como expresión, generalmente debes incluir `else` (a menos que el compilador pueda garantizar que cubres todos los casos, como con enums o sealed classes). Puedes combinar múltiples valores con comas. El operador `in` verifica si el valor está en un rango o colección. Esto hace el código muy legible.


### when: casos avanzados

Expresiones arbitrarias y verificación de tipos:

```kotlin
when (x) {
    parseInt(s) -> print("s encodes x")
    in validNumbers -> print("x is valid")
    !in 10..20 -> print("x is outside the range")
    is String -> print("x is a String")
    else -> print("none of the above")
}
```

Note: `when` puede usar expresiones arbitrarias, no solo constantes. Puedes llamar funciones como `parseInt(s)`. Usa `in` para verificar pertenencia a colecciones o rangos. Usa `!in` para verificar no pertenencia. Usa `is` para verificar el tipo del valor (smart cast automático). Esta flexibilidad hace de `when` una herramienta muy potente y expresiva.

---

## Funciones


### Declaración básica de funciones

Sintaxis de funciones con fun:

```kotlin
fun powerOf(number: Int, exponent: Int): Int {
    // Implementación
    return number.toDouble().pow(exponent.toDouble()).toInt()
}

fun hello(name: String = "world"): String {
    return "Hello, $name!"
}
```

Note: Las funciones se declaran con la palabra clave `fun`. Los parámetros se escriben como `nombre: Tipo`. El tipo de retorno va después de los paréntesis precedido de dos puntos. Los parámetros pueden tener valores por defecto. Si un parámetro tiene valor por defecto, es opcional al llamar la función. El tipo de retorno es obligatorio excepto cuando la función devuelve `Unit` (equivalente a void).


### Parámetros por defecto

Valores por defecto y argumentos con nombre:

```kotlin
fun hello(name: String = "world"): String {
    return "Hello, $name!"
}

hello("foo")        // => Hello, foo!
hello(name = "bar") // => Hello, bar!
hello()             // => Hello, world!

fun bye(bye: String = "Bye", name: String): String {
    return "$bye, $name!!"
}

bye(name = "John")                    // => Bye, John!!
bye(name = "John", bye = "Good bye") // => Good bye, John!!
```

Note: Los parámetros por defecto hacen las funciones más flexibles. Si un parámetro por defecto precede a uno sin valor predeterminado, debes usar argumentos con nombre al llamar la función. Los argumentos con nombre mejoran la legibilidad y permiten cambiar el orden de los argumentos. Una vez que usas un argumento con nombre, todos los siguientes también deben tener nombre.


### Anotación @JvmOverloads

Facilitar llamadas desde Java:

```kotlin
@JvmOverloads
fun calCircumference(radius: Double, pi: Double = Math.PI): Double {
    return (2 * pi) * radius
}

// Desde Java se generan dos métodos:
// double calCircumference(double radius, double pi)
// double calCircumference(double radius)
```

Note: Java no soporta parámetros por defecto. Cuando llamas una función Kotlin desde Java, debes proporcionar todos los valores. La anotación `@JvmOverloads` le indica al compilador que genere versiones sobrecargadas de la función para cada combinación de parámetros. Esto facilita el uso de funciones Kotlin desde código Java.


### Tipo Unit

Funciones sin valor de retorno significativo:

```kotlin
fun hello(name: String): Unit {
   print("Hello $name")
}

// Equivalente (Unit es opcional)
fun sayHello(name: String) {
   print("Hello $name")
}
```

Note: `Unit` es el tipo que representa "sin valor significativo de retorno", similar a `void` en Java/C. A diferencia de `void`, `Unit` es un objeto real. Cuando una función devuelve `Unit`, puedes omitir la declaración del tipo de retorno porque el compilador lo infiere automáticamente. Solo es necesario especificarlo explícitamente cuando quieres ser más claro o en ciertos contextos genéricos.


### Argumentos con nombre

Mejorar la legibilidad de las llamadas:

```kotlin
fun area(width: Int, height: Int): Int {
    return width * height
}

area(10, 12)
area(width = 10, height = 12)    // Más legible
area(height = 12, width = 10)    // Cambiar orden
area(10, height = 12)            // Mezclando posicionales y nombrados
// area(width = 10, 12)          // ERROR: nombrados antes de posicionales
```

Note: Los argumentos con nombre hacen el código más legible, especialmente con muchos parámetros o parámetros del mismo tipo. Cuando usas argumentos con nombre, puedes cambiar el orden. Puedes mezclar argumentos posicionales y con nombre, pero todos los posicionales deben ir antes de los nombrados. Los argumentos con nombre son especialmente útiles con funciones que tienen múltiples parámetros booleanos o numéricos.


### Parámetros vararg

Número variable de argumentos:

```kotlin
fun varargExample(vararg names: Int) {
    println("Argument has ${names.size} elements")
}

varargExample()           // => 0 elements
varargExample(1)          // => 1 element
varargExample(1, 2, 3)    // => 3 elements

// Con otros parámetros
fun car(vararg model: String, year: Int) {}
car("Audi", "A6", year = 2005)
```

Note: `vararg` permite pasar un número variable de argumentos del mismo tipo. La función recibe los argumentos como un array. Puedes pasar cero, uno o muchos argumentos. Si hay otros parámetros después del `vararg`, debes usar argumentos con nombre para ellos. Solo puede haber un parámetro `vararg` por función. Dentro de la función, accedes a los valores mediante notación de array.


### Spread operator

Expandir arrays en argumentos individuales:

```kotlin
val intArray = intArrayOf(1, 2, 3, 4)
val array = Array(5) { i -> i + 1 }

// Operador spread (*)
varargExample(*intArray)           // => 4 elements
varargExample(*array.toIntArray()) // => 5 elements

// Combinar arrays y valores
varargExample(0, *intArray, 5)     // => 6 elements
```

Note: El operador spread (*) "expande" un array en argumentos individuales. Sin él, pasarías el array como un solo objeto. Con él, cada elemento del array se pasa como un argumento separado. Puedes combinar el operador spread con argumentos normales. El operador * es necesario cada vez que quieras pasar un array a una función vararg.


### Funciones de expresión única

Sintaxis concisa para funciones simples:

```kotlin
// Con cuerpo de bloque
fun odd(x: Int): Boolean {
    return x % 2 == 1
}

// Expresión única (tipo opcional)
fun odd(x: Int): Boolean = x % 2 == 1

// Sin tipo de retorno (inferido)
fun even(x: Int) = x % 2 == 0
```

Note: Cuando una función consiste en una sola expresión, puedes usar la sintaxis de expresión única con `=`. El cuerpo va después del símbolo igual sin llaves. En expresiones únicas, el tipo de retorno es opcional porque el compilador lo infiere de la expresión. Solo es obligatorio especificar el tipo cuando el cuerpo es un bloque (con llaves).


### Retornar múltiples valores

Usar Pair y Triple para múltiples retornos:

```kotlin
fun getNumbers(num: Int): Pair<Int?, Int?> {
    require(num > 0) { "Error: num is less than 0" }
    return Pair(num, num * 2)
}

// Desestructuración
val (num, num2) = getNumbers(10)

// También con Pair usando 'to'
val pair = 234 to "Nigeria"
val pair2 = Pair(234, "Nigeria")  // Equivalente
```

Note: Para devolver múltiples valores, usa `Pair` (para dos valores) o `Triple` (para tres). Kotlin proporciona desestructuración: puedes extraer los valores del par directamente en variables separadas con `val (a, b) = pair`. La función `to` es un atajo para crear `Pair`, es más concisa y legible que el constructor. También existe `Triple` para tres valores, pero si necesitas más, considera crear una data class.

---

## Extension Functions


### Concepto de Extension Function

Añadir funcionalidad a clases existentes:

```kotlin
fun String.remove(c: Char): String {
    return this.filter { it != c }
}

// Uso
println("Hello, world!".remove('l'))  // => Heo, word!
```

Note: Las extension functions permiten añadir nuevas funcionalidades a clases existentes sin heredar ni modificar la clase original. Esto es similar a los métodos de extensión de C#. La función se declara fuera de la clase, prefijando el nombre de la clase que extiendes antes del nombre de la función. Dentro de la función, `this` se refiere a la instancia sobre la cual se llama. El tipo que extiendes se llama "tipo receptor" y el objeto concreto es el "objeto receptor".


### Precedencia: miembros vs extensiones

Qué sucede cuando hay conflictos de nombres:

```kotlin
class C {
    fun foo() { println("member") }
}

fun C.foo() {
    println("extension")
}

fun C.foo(i: Int) {
    println("extension & overrided")
}

C().foo()    // => member
C().foo(5)   // => extension & overrided
```

Note: Si una extension function tiene la misma firma (nombre y parámetros) que un método miembro de la clase, el compilador siempre preferirá el método miembro. La extensión no se ejecutará. Sin embargo, puedes sobrecargar: si tu extensión tiene diferente número o tipo de parámetros, sí se usará. Esto es importante para evitar conflictos y comportamientos inesperados.

---

## Top-level Functions


### Funciones de nivel superior

Funciones fuera de clases:

```kotlin
// Archivo: UserUtils.kt
@file:JvmName("UserUtils")
package com.example.project.utils

fun checkUserStatus(): String {
    return "online"
}

// Desde Kotlin
val status = checkUserStatus()

// Desde Java (generado)
String status = UserUtils.checkUserStatus();
```

Note: Las top-level functions son funciones definidas directamente en un archivo, fuera de cualquier clase u objeto. Son útiles para funciones de utilidad que no pertenecen lógicamente a ninguna clase. Desde Kotlin se llaman directamente por su nombre. Java no soporta funciones fuera de clases, así que el compilador genera una clase con métodos estáticos. La anotación `@file:JvmName` controla el nombre de esa clase generada.

---

## High-Order Functions


### Concepto de High-Order Function

Funciones que reciben o devuelven funciones:

```kotlin
// Función que acepta otra función como parámetro
fun foo(str: String, fn: (String) -> String): Unit {
    val applied = fn(str)
    println(applied)
}

foo("Hello") { it.reversed() }  // => olleH
```

Note: Una high-order function es una función que toma funciones como parámetros y/o devuelve funciones. En Kotlin, las funciones son ciudadanos de primera clase: pueden almacenarse en variables, pasarse como argumentos y devolverse como resultados. El tipo de una función se escribe como `(parametros) -> retorno`. Por ejemplo, `(String) -> String` es una función que toma un String y devuelve un String.


### High-Order Functions: retornando funciones I

Funciones que devuelven otras funciones:

```kotlin
// Función que retorna otra función
fun isPositive(n: Int): (Int) -> Boolean {
    return { n > 0 }
}

// Forma más compacta
fun modulo(k: Int): (Int) -> Boolean = { it % k == 0 }

// Uso
val evens = listOf(1, 2, 3, 4, 5, 6).filter(modulo(2))
// => [2, 4, 6]
```

Note: Las high-order functions también pueden devolver funciones. En el ejemplo, `modulo` devuelve una función que verifica si un número es divisible por `k`. La sintaxis `{ it % k == 0 }` es un lambda (función anónima). La forma compacta con `=` es más concisa. Este patrón es muy común en programación funcional para crear funciones parametrizadas.


### High-Order Functions: retornando funciones II

Reutilizar funciones devueltas:

```kotlin
fun modulo(k: Int): (Int) -> Boolean = { it % k == 0 }

// Asignar función a variable
val isEven: (Int) -> Boolean = modulo(2)

// Usar en múltiples contextos
listOf(1, 2, 3, 4).filter(isEven)  // => [2, 4]
listOf(5, 6, 7, 8).filter(isEven)  // => [6, 8]
```

Note: Puedes asignar la función devuelta a una variable y reutilizarla. El tipo de la variable es un tipo función: `(Int) -> Boolean`. Esto es útil cuando quieres aplicar la misma lógica en múltiples lugares sin repetir código. Es más flexible que definir múltiples funciones para cada caso.

---

## Function Types y Lambdas


### Tipos función I

Definir tipos de función:

```kotlin
fun executor(action: () -> Unit) {
    action()
}

// action es el nombre del parámetro
// () -> Unit es el tipo función
```

Note: Un tipo función define la firma de una función: parámetros y tipo de retorno, separados por `->`. Los paréntesis contienen los tipos de los parámetros (vacíos si no hay parámetros). El tipo de retorno siempre debe especificarse explícitamente, incluso si es `Unit`. Los paréntesis son obligatorios incluso sin parámetros: `() -> Unit`, no `-> Unit`.


### Tipos función II

Ejemplos de tipos función:

* `() -> Unit`: no toma parámetros, no devuelve nada
* `() -> String`: no toma parámetros, devuelve String
* `(String) -> Unit`: toma String, no devuelve nada
* `(String, Float) -> Int`: toma String y Float, devuelve Int

Note: Los tipos función pueden tener cualquier número de parámetros (incluso ninguno) y cualquier tipo de retorno. Son tipos como cualquier otro en Kotlin: puedes usarlos para declarar variables, parámetros de funciones, o tipos de retorno. La sintaxis es siempre la misma: `(tipos de parámetros) -> tipo de retorno`.


### Asignar funciones a variables

Funciones como valores:

```kotlin
// Con lambda
val saySomething: (String) -> Unit = { x -> println(x) }
saySomething("Good morning")  // => Good morning

// Con referencia a función
fun tell(text: String) {
    println(text)
}

var saySomething2: (String) -> Unit = ::tell
saySomething2("Hello")  // => Hello
```

Note: Puedes asignar funciones a variables de dos formas. Primera: con un lambda (función anónima) usando la sintaxis `{ parámetros -> cuerpo }`. Segunda: con una referencia a una función existente usando el operador `::nombreFuncion`. Ambas formas crean un valor de tipo función que puedes almacenar, pasar o ejecutar. Las referencias con `::` son útiles cuando ya tienes la función definida.


### Lambdas I

Funciones anónimas inline:

```kotlin
// Lambda con dos parámetros
val sum: (Int, Int) -> Int = { x, y -> x + y }
sum(10, 20)  // => 30

// Equivalente con función normal
fun operation(x: Int, y: Int): Int {
    return x + y
}
val sum2: (Int, Int) -> Int = ::operation
sum2(10, 20)  // => 30
```

Note: Un lambda es una función literal: una función anónima que no se declara formalmente sino que se usa directamente como expresión. La sintaxis es `{ parámetros -> cuerpo }`. Los parámetros se declaran antes de la flecha, el cuerpo después. No necesitas especificar tipos de parámetros si el compilador puede inferirlos del contexto. El valor de la última expresión es el valor de retorno del lambda.


### Lambdas II: parámetro it

Parámetro implícito para lambdas de un solo argumento:

```kotlin
// Lambda con un parámetro
val isNegative: (Int) -> Boolean = { x -> x < 0 }

// Usando 'it' (parámetro implícito)
val isNegative2: (Int) -> Boolean = { it < 0 }

isNegative(-5)   // => true
isNegative2(-5)  // => true
```

Note: Cuando un lambda tiene un solo parámetro, puedes omitir su declaración y usar el nombre especial `it`. El compilador infiere el tipo del parámetro. Esto hace los lambdas más concisos. Sin embargo, si el lambda es complejo o `it` no es claro, mejor declara el parámetro con un nombre descriptivo.


### Lambdas III: fuera de paréntesis

Sintaxis trailing lambda:

```kotlin
// Lambda dentro de paréntesis
val upperCaseLetters = "Hello World".filter({ it.isUpperCase() })

// Lambda fuera de paréntesis (convención Kotlin)
val lowerCaseLetters = "Hello World".filter { it.isLowerCase() }

println("$upperCaseLetters - $lowerCaseLetters")
// => HW - elloorld
```

Note: Cuando el último parámetro de una función es un lambda, puedes sacarlo fuera de los paréntesis. Si el lambda es el único argumento, puedes omitir los paréntesis completamente. Esta es una convención muy común en Kotlin que hace el código más limpio y parecido a sintaxis integrada del lenguaje. Muchas funciones de la biblioteca estándar están diseñadas para aprovechar esto.


### Lambdas IV: función como parámetro

Pasar lambdas a funciones:

```kotlin
// High-order function que acepta lambda
fun isAnEmail(email: (String) -> Boolean) {
    val result = email("myemail@example.com")
    println(result)
}

// Diferentes formas de llamar
isAnEmail({ s: String -> s.contains("@") })  // forma completa
isAnEmail { s: String -> s.contains("@") }   // sin paréntesis
isAnEmail { it.contains("@") }               // usando 'it'
```

Note: Cuando defines una función que acepta un lambda, especificas el tipo función del parámetro. Al llamarla, puedes pasar el lambda de varias formas: entre paréntesis, fuera de paréntesis, con tipos explícitos o inferidos, usando nombres de parámetros o `it`. Elige la forma más legible según el contexto.


### Parámetros no utilizados

Usar guión bajo para parámetros ignorados:

```kotlin
val unusedSecondParam: (String, Int) -> Boolean = { s, _ ->
    s.length > 10
}

unusedSecondParam("Hello World", 0)  // 0 no se usa

// También en desestructuración
val (name, _) = person  // Ignorar segundo valor
```

Note: Cuando un parámetro de un lambda no se usa, puedes indicarlo con guión bajo (_) en lugar de un nombre. Esto comunica claramente tu intención de no usar ese valor. El compilador no generará advertencias sobre parámetros no usados. También funciona en desestructuración para ignorar valores que no necesitas.

---

## Anonymous Functions


### Funciones anónimas

Alternativa a lambdas con sintaxis fun:

```kotlin
// Función anónima con expresión
fun(x: Int, y: Int): Int = x + y

// Función anónima con bloque
fun(x: Int, y: Int): Int {
    return x + y
}

// Uso en contexto
ints.filter(fun(item) = item > 0)
```

Note: Una función anónima es como una función normal pero sin nombre. Se declara con `fun` pero sin nombre después. Puede tener cuerpo de expresión (con `=`) o de bloque (con llaves). Los tipos de parámetros pueden omitirse si se infieren del contexto. La diferencia con lambdas es principalmente sintáctica y en cómo funciona `return` (en función anónima, `return` sale de la función anónima; en lambda, sale de la función contenedora).

---

## Closures


### Closures

Capturar variables del ámbito exterior:

```kotlin
fun printFilteredNamesByLength(length: Int) {
    val names = arrayListOf("Adam", "Andrew", "Chike", "Kechi")
    
    val filterResult = names.filter {
        it.length == length  // 'length' está fuera del lambda
    }
    
    println(filterResult)
}
```

Note: Un closure es un lambda o función anónima que "captura" variables del ámbito exterior. En el ejemplo, el lambda dentro de `filter` accede a la variable `length` que está fuera de él. A diferencia de Java (antes de Java 8), en Kotlin las variables capturadas pueden ser modificadas. Esto hace los closures más flexibles y poderosos.

---

## Nested Functions


### Funciones locales o anidadas

Funciones dentro de otras funciones:

```kotlin
fun printCircumferenceAndArea(radius: Double): Unit {
    
    fun calCircumference(radius: Double): Double = 
        (2 * Math.PI) * radius
    val circumference = "%.2f".format(calCircumference(radius))
    
    fun calArea(radius: Double): Double = 
        Math.PI * Math.pow(radius, 2.0)
    val area = "%.2f".format(calArea(radius))
    
    print("The circle circumference of $radius radius " +
          "is $circumference and area is $area")
}
```

Note: Las funciones locales o nested functions son funciones declaradas dentro de otras funciones. Solo son visibles dentro de la función contenedora. Son útiles para extraer lógica repetitiva sin contaminar el ámbito exterior. Las funciones locales tienen acceso a todas las variables de la función contenedora, por lo que no necesitas pasar parámetros que ya existen en el ámbito exterior.

---

## Infix Functions


### Funciones infix

Llamar funciones sin punto ni paréntesis:

```kotlin
class Student {
    var kotlinScore = 0.0

    infix fun addKotlinScore(score: Double): Unit {
        this.kotlinScore = kotlinScore + score
    }

    fun build() {
        this addKotlinScore 95.0   // Notación infix
        addKotlinScore(95.0)       // Notación normal
    }
}

val student = Student()
student addKotlinScore 95.00  // Notación infix
student.addKotlinScore(95.0)  // Notación normal
```

Note: Las funciones marcadas con `infix` pueden llamarse sin punto ni paréntesis, usando notación infix (objeto función argumento). Requisitos: debe ser función miembro o de extensión, tener exactamente un parámetro, y ese parámetro no puede ser vararg ni tener valor por defecto. Las funciones infix hacen el código más legible para ciertas operaciones, como `1 to "one"` para crear pares.

---

## Inline Functions


### Inline functions

Optimizar lambdas evitando overhead:

```kotlin
inline fun repeat(times: Int, action: (Int) -> Unit) {
    for (i in 0 until times) {
        action(i)
    }
}

// Uso
repeat(3) { index ->
    println("Iteration $index")
}
```

Note: El modificador `inline` hace que el compilador copie el código de la función y del lambda en el lugar de la llamada, en lugar de crear objetos función. Esto elimina el overhead de las lambdas (creación de objetos, llamadas virtuales). Sin embargo, aumenta el tamaño del bytecode generado. Usa `inline` solo para funciones pequeñas que aceptan lambdas, especialmente si se llaman frecuentemente. La biblioteca estándar usa mucho `inline` en funciones como `filter`, `map`, etc.

---

## Referencias


### Documentación y recursos

* Documentación oficial: kotlinlang.org
* Tutorial Kotlin: code.tutsplus.com/series/kotlin-from-scratch
* Learn X in Y minutes: learnxinyminutes.com/docs/kotlin/
* Programming Kotlin (Packt Publishing)
* Super Kotlin Tutorial: superkotlin.com
* GitHub: Zhuinden/guide-to-kotlin

Note: Para profundizar en Kotlin, la documentación oficial es excelente y muy completa. Hay numerosos tutoriales online, libros, y recursos de la comunidad. Kotlin tiene una comunidad muy activa. Se recomienda practicar mucho con ejemplos y proyectos pequeños para familiarizarse con la sintaxis y características del lenguaje.

---

## ¿Preguntas?

Note: Kotlin es un lenguaje moderno, expresivo y seguro que mejora muchas áreas problemáticas de Java manteniendo total interoperabilidad. Las características clave que lo hacen destacar son: null safety (seguridad frente a null), funciones de extensión, lambdas y programación funcional, clases de datos, smart casts, y una sintaxis más concisa. Es el lenguaje recomendado por Google para desarrollo Android, pero también es excelente para backend (con frameworks como Ktor o Spring), desarrollo web (Kotlin/JS), y aplicaciones multiplataforma (Kotlin Multiplatform). Anima a los estudiantes a practicar escribiendo pequeños programas, experimentando con las diferentes características del lenguaje.
