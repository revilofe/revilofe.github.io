---
title: "UD 7 - 7.2 Consola y teclado"
description: Consola y teclado
summary: Consola y teclado
authors:
    - Eduardo Fdez
date: 2022-02-24
icon:   
permalink: /prog/unidad7/7.2
categories:
    - PROG
tags:
    - Software
    - Consola
    - Teclado
---

## 7.2. Lectura y escritura en entrada y salida estándar

Dentro de la biblioteca estándar de Kotlin, el paquete `kotlin.io` proporciona elementos esenciales para trabajar con los flujos de entrada y salida estándar (Input/Output o I/O). Esta transmisión de información entre la memoria principal y los dispositivos de entrada y salida permite, entre otras cosas, leer y escribir datos.

Vamos a ver cómo se transfieren datos de entrada y salida en consola (el paquete `kotlin.io` también proporciona herramientas para trabajar con archivos, como veremos mas adelante), lo que es útil para mostrar una información en **pantalla** y para obtener información aportada por el usuario, habitualmente a través de un dispositivo de entrada como el **teclado**.

### 1. Entrada y salida estándar
A continuación se muestra un esquema de las interfaces básicas para leer/escribir información:

#### 1.1 Output: Escribir en consola

Como ya hemos visto en multitud de ejemplos previos durante el curso, para enviar un mensaje a la salida estándar (la pantalla) usamos habitualmente las funciones `print()` y `println()`, que se diferencian en que la segunda incluye un salto de línea al final. Este salto de línea es reproducible a través del caracter especial `\n`, de la siguiente forma `print("\n")`

```kotlin
fun main(args: Array<String>) {
    println("1. println ")
    println("2. println ")

    print("1. print ")
    print("2. print ")
}
```

El programa anterior obtiene este resultado:

```
1. println 
2. println 
1. print 2. print
```

Podemos añadir un salto de línea en la función `print` (aunque para eso ya tenemos a `println`):

```kotlin
print("Función print con salto de línea\n")
```

Un ejemplo que utiliza la función println para mostrar valores en consola:

```kotlin
val numero = 12.3
println("numero")               // numero
println(numero)                 // 12.3
println("$numero")              // 12.3
println("numero = $numero")     // numero = 12.3
println("${numero + numero}")   // 24.6
println(12.3)                   // 12.3
```

#### 1.2. Input: Lectura de datos en consola

Para la lectura de datos por teclado utilizamos la función `readLine` y `readLn` (otra opción que no vamos a ver ahora es utilizar la clase `Scanner` importada desde la librería estándar de Java con `import java.util.Scanner`):

```kotlin

fun main(args: Array<String>) {
    print("Tu nombre: ")
    val nombre = readLine()
    println("Hola $nombre")
}
```

La función `readLine()` convierte la entrada en un `String` (realmente devuelve un `String?` puesto que puede ser nulo) aunque es posible tomar la entrada y convertirla a otro tipo explícitamente:

```kotlin
print("Nombre: ")
val nombre = readLine()
print("Edad: ")
val edad = Integer.valueOf(readLine()) // cuidadín!!   
println("Tu nombre es $nombre y tienes $edad años.")
``` 

El programa anterior funcionará bien mientras el usuario introduzca un entero como valor de edad, pero en caso contrario saltará un excepción durante la ejecución (`NumberFormatException`). Una primera solución podría pasar por el uso del manejo de excepciones (que veremos en posteriores entradas) para capturar los casos problemáticos:

```kotlin
print("Nombre: ")
val nombre = readLine()
print("Edad: ")
try {
    val edad = Integer.valueOf(readLine())
    println("Tu nombre es $nombre y tienes $edad años.")
} catch (ex: NumberFormatException) {
    println("Edad no válida")
}
```

A veces se pueden ver ejemplos de código que intentan resolver este problema con el operador de aserción `!!` (revisar Gestión de tipos nulos en Kotlin), y de esta manera se le avisa al compilador que confíe que la función `readLine` siempre retornará un `String`, pero en general no es una buena manera de validar la entrada de datos.

```kotlin
val num: Int
print("Introduce un número entero: ")
num = readLine()!!.toInt() // prometemos algo que no podemos cumplir
println(num)
```

A pesar de la pretendida seguridad del operador `!!`, seguimos sin escapar del `NumberFormatException`. Recuerda que además de la función `toInt()` también existen las funciones `toFloat()`, `toDouble()`, `toLong()`, `toShort()` y `toByte()` para la conversión de tipos (ver Tipos básicos de datos).

Existen distintas formas de resolver éste y otros problemas similares respecto a la entrada de datos por parte del usuario. Algunas soluciones pasan por combinar la función `readLine` con el operador de llamada segura `?` y con la expresión `try` para devolver un valor (otras soluciones también utilizan el operador `as` que vimos en comprobación y conversión de tipos con `is` y `as`). Un ejemplo:

```kotlin
val num: Int?
print("Introduce un número entero: ")
num = try {
    readLine()?.toInt()
} catch (ex: NumberFormatException) {
    null
}
if (num != null) {
    println("El número es: $num")
} else {
    println("¡Eso no es un número entero!")
}
```

En este ejemplo el valor introducido es asignado a la variable anulable `num`, cuyo valor depende de que se procese el contenido de la expresión `try` (cuando se ingresa un entero) o de que, en caso contrario, se produzca un `NumberFormatException` que es capturado por `catch`, que retorna `null` que es asignado a la variable `num`.

Pero podemos mejorarla prescindiendo de `try..catch` y sustituyendo la función `toInt` por la función `toIntOrNull`:

```kotlin
val num: Int?
print("Introduce un número entero: ")
num = readLine()?.toIntOrNull()
if (num != null) {
    println("El número es: $num")
} else {
    println("¡Eso no es un número entero!")
}
```

En el ejemplo anterior llamamos a `readLine` con el operador `?` para realizar la conversión con `toIntOrNul` de forma segura. La función `toIntOrNull()` requiere que la variable sea de tipo anulable (`val num: Int?`) porque si la conversión a entero falla, se retorna null, que es asignado a `num`. Igualmente contamos con las funciones `toFloatOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`, `toShortOrNull()` y `toByteOrNull()` que en caso de no poder realizar la conversión de tipos devuelven `null`.

#### 1.3. Mejorando las funciones

[Aquí](https://stackoverflow.com/questions/41283393/reading-console-input-in-kotlin) hay un grupo extendido (inspirado en el [artículo](https://kotlinlang.org/docs/competitive-programming.html#functional-operators-example-long-number-problem)) de funciones de ayuda para leer todos los tipos posibles, listas, arrays, arrays 2D, etc.:

```Kotlin
// private fun readln() = readLine()!! //Ya disponib le en la versión 1.6
private fun readlnByte() = readln().toByte()
private fun readlnShort() = readln().toShort()
private fun readlnInt() = readln().toInt()
private fun readlnLong() = readln().toLong()
private fun readlnFloat() = readln().toFloat()
private fun readlnDouble() = readln().toDouble()
private fun readlnBigInt(radix: Int = 10) = readln().toBigInteger(radix)
private fun readlnBigDecimal() = readln().toBigDecimal()

private fun lineSequence(limit: Int = Int.MAX_VALUE) = generateSequence { readLine() }.constrainOnce().take(limit)
private fun readlnStrings() = readln().split(' ')
private fun readlnBytes() = readlnStrings().map { it.toByte() }
private fun readlnShorts() = readlnStrings().map { it.toShort() }
private fun readlnInts() = readlnStrings().map { it.toInt() }
private fun readlnLongs() = readlnStrings().map { it.toLong() }
private fun readlnFloats() = readlnStrings().map { it.toFloat() }
private fun readlnDoubles() = readlnStrings().map { it.toDouble() }

private fun readByteArray() = readlnStrings().run { ByteArray(size) { get(it).toByte() } }
private fun readShortArray() = readlnStrings().run { ShortArray(size) { get(it).toShort() } }
private fun readIntArray() = readlnStrings().run { IntArray(size) { get(it).toInt() } }
private fun readLongArray() = readlnStrings().run { LongArray(size) { get(it).toLong() } }
private fun readFloatArray() = readlnStrings().run { FloatArray(size) { get(it).toFloat() } }
private fun readDoubleArray() = readlnStrings().run { DoubleArray(size) { get(it).toDouble() } }

private fun readlnByteArray(n: Int) = ByteArray(n) { readlnByte() }
private fun readlnShortArray(n: Int) = ShortArray(n) { readlnShort() }
private fun readlnIntArray(n: Int) = IntArray(n) { readlnInt() }
private fun readlnLongArray(n: Int) = LongArray(n) { readlnLong() }
private fun readlnFloatArray(n: Int) = FloatArray(n) { readlnFloat() }
private fun readlnDoubleArray(n: Int) = DoubleArray(n) { readlnDouble() }

private fun readByteArray2d(rows: Int, cols: Int) = Array(rows) { readByteArray().also { require(it.size == cols) } }
private fun readShortArray2d(rows: Int, cols: Int) = Array(rows) { readShortArray().also { require(it.size == cols) } }
private fun readLongArray2d(rows: Int, cols: Int) = Array(rows) { readLongArray().also { require(it.size == cols) } }
private fun readIntArray2d(rows: Int, cols: Int) = Array(rows) { readIntArray().also { require(it.size == cols) } }
private fun readFloatArray2d(rows: Int, cols: Int) = Array(rows) { readFloatArray().also { require(it.size == cols) } }
private fun readDoubleArray2d(rows: Int, cols: Int) =
    Array(rows) { readDoubleArray().also { require(it.size == cols) } }

private fun isWhiteSpace(c: Char) = c in " \r\n\t"

// JVM-only targeting code follows next

// readString() via sequence is still slightly faster than Scanner
private fun readString() = generateSequence { System.`in`.read().toChar() }
    .dropWhile { isWhiteSpace(it) }.takeWhile { !isWhiteSpace(it) }.joinToString("")
private fun readByte() = readString().toByte()
private fun readShort() = readString().toShort()
private fun readInt() = readString().toInt()
private fun readLong() = readString().toLong()
private fun readFloat() = readString().toFloat()
private fun readDouble() = readString().toDouble()
private fun readBigInt(radix: Int = 10) = readString().toBigInteger(radix)
private fun readBigDecimal() = readString().toBigDecimal()

private fun readBytes(n: Int) = generateSequence { readByte() }.take(n)
private fun readShorts(n: Int) = generateSequence { readShort() }.take(n)
private fun readInts(n: Int) = generateSequence { readInt() }.take(n)
private fun readLongs(n: Int) = generateSequence { readLong() }.take(n)
private fun readFloats(n: Int) = generateSequence { readFloat() }.take(n)
private fun readDoubles(n: Int) = generateSequence { readDouble() }.take(n)
```

#### 1.4. Aplicando formato a la salida estándar

A continuación veremos como aplicar formato a las cadenas que se imprimen en salida estandar. La explicación esta hecha en Kotlin pero en Java aplica prácticamente lo mismo.

En Kotlin (Y la mayoría de los lenguajes de programación) podemos utilizar formatos para reemplazar variables dentro de los String, supongamos que queremos imprimir nuestro nombre, edad y peso, podríamos hacer algo así

```kotlin
val name: String = "Walter White"
val age: Int = 50
val weight: Double = 75.5

val description = "Me llamo " + name + ", tengo " + age + " años y peso " + weight + " kg."
println(description)

// O mejor aún, en Kotlin podemos hacer esto
val description = "Me llamo $name, tengo $age años y peso $weight kg"
println(description)

// Ahora, si usamos el String format
val description = String.format("Me llamo %s, tengo %d años y peso %.2f kg", name, age, weight)
println(description)
```

Las 3 soluciones son correctas e imprimen lo mismo, pero la tercera es la más útil al usar `Strings` donde tendrás que reemplazar variables porque te ayuda a tener código más limpio y soportar diferentes idiomas.

Si observas en la última opción, lo que hacemos es poner ciertos formatos dentro del `String` y luego al final, separados por coma, ponemos las variables que queremos que se reemplacen en el `String`: `%s` para otros strings como `name`, `%d` para enteros como `age` y `%f` para `doubles` y `floats`, en el `.2` que ves en el `%f` el `2` es la cantidad de decimales que queremos que se impriman, así por ejemplo en este caso se imprimiría el peso como `75.50`.

Aquí te dejo una tabla con los formatos más comunes, también pueden ser usados en Java:


| **Formato** | Tipo de**dato**                                          |
| ------------- | ---------------------------------------------------------- |
| %b          | Boolean                                                  |
| %c          | Char                                                     |
| %d          | Integer                                                  |
| %e          | Float en notación científica                           |
| %f          | Float y Double (Agrega %**.n**f para forzar n decimales) |
| %o          | Formato Octal                                            |
| %s          | Strings                                                  |
| %x          | Formato Hexadecimal                                      |

Hay otros 3 o 4 formatos más pero son tan poco usuales que si los necesitas prefiero que los consultes tu en la documentación.

¿Qué muestra como salida el siguiente código?

```kotlin
 val str1 = String.format("%d", 404) // Integer value  
val str2 = String.format("%s", "Mehmet") // String value  
val str3 = String.format("%f", 404.00) // Float value  
val str4 = String.format("%x", 404) // Hexadecimal value  
val str5 = String.format("%c", 'c') // Char value  
println(str1)
println(str2)
println(str3)
println(str4)
println(str5)
```

### 2. Otras Bibliotecas

Existen bibliotecas que intentan solucionar alguna necesidad que han encontrado en sus desarrollos. Algunas de ellas para trabajar con la consola:   
- [KFormat](https://github.com/marcelmay/kformat)   
- [Mordant](https://github.com/ajalt/mordant)
- [clikt](https://ajalt.github.io/clikt/)   
- [kotlinx-cli](https://github.com/Kotlin/kotlinx-cli)   

#### 2.1. Kotlin Console Output Formatting

[KFormat](https://github.com/marcelmay/kformat) es una pequeña biblioteca de Kotlin para la salida de texto con formato, como por ejemplo la impresión de valores en una tabla estructurada. Los casos de uso típicos incluyen el desarrollo de herramientas CLI. (Command Line Interface)

Un ejemplo: Dar formato a una tabla, incluido el cambio de tamaño de celda:

```kotlin
table {
    header("A", "B", "C", "Long_Header")

    row(10, "b...1", 2.1f, "foo")
    row(20, "b2", 1 / 3f, "bar")

    hints {
        alignment("A", Hints.Alignment.LEFT)
        precision("C", 2)
        postfix("C", "%")
        borderStyle = Table.BorderStyle.SINGLE_LINE // or NONE
    }
}.render(StringBuilder())
```

Genera la siguiente salida:

```
A  |     B |     C | Long_Header
---|-------|-------|------------
10 | b...1 | 2.10% |         foo
20 |    b2 | 0.33% |         bar
```

[Mordant](https://github.com/ajalt/mordant) es otra biblioteca que proporciona una API para dar formato a la salida de texto en la consola. Permite dar formato a texto en la consola, como colores, negritas, cursivas, subrayados, etc.

#### 2.2. Kotlin Command-Line Arguments
En Kotlin, los argumentos de la línea de comandos se pasan a través de la función `main()`. En este apartado veremos cómo leer y procesar los argumentos de la línea de comandos en Kotlin.

##### 2.2.1 Línea de comandos en `Main`

Al invocar un programa desde la línea de comandos, puedes pasarle un número variable de argumentos. Por ej: `> tar -vzf file.tar.gz`

Para capturar los argumentos de la línea de comandos, debes proporcionar un parámetro predefinido a `main()`:

```kotlin
// MainArgs.kt

fun main (args: Array < String >) {
   for (a in args) {
    imprimir (a)
  }
}
```

El parámetro se llama tradicionalmente `args` aunque puede llamarlo de cualquier manera, y el tipo de `args` solo puede ser `Array<String>` (Array of String).

También se puede usar el compilador kotlinc para crear un programa que se ejecuta desde línea de comandos.

Una vez que haya creado y guardado y compilado el código para un programa llamado `MainArgs.kt`, escriba lo siguiente en el símbolo del sistema:


```Bash
> kotlinc MainArgsKt
```

Puedes proporcionar los argumentos de la línea de comandos después de la invocación del programa, así:

```Bash
> kotlin MainArgsKt aaa 42 3.14159.
```
Y por salida estandar, saldrá lo siguiente:

```
aaa
42
3.14159
```

Si una vez leídos los parśmetros quieres convertir un parámetro `String` en un tipo específico, Kotlin proporciona funciones de conversión, como`toInt()` para convertir a `Int` y `toFloat()` para convertir a `Float`...

El uso de estos métodos supone que los argumentos de la línea de comandos aparecen en un orden particular.

Por ejemplo, en el siguiente código, el programa espera un `String`, seguido de algo convertible a `Int`, seguido de algo convertible a `Float`:


```kotlin
// MainArgConversion.kt`

fun main (args: Array < String >) {
   if (args.size < 3) return 
    val primero = args[0]
    val segundo = args[1].toInt ()
    val tercero = args[2].toFloat ()
    println( "$primero $segundo $tercero" )
}
```

La primera línea de `main()` cierra el programa si no hay suficientes argumentos.

Si no proporciona algo convertible a `Int` y `Float` como segundo y tercer argumento de la línea de comandos, verá errores de tiempo de ejecución.

Si compilas y ejecutas `MainArgConversion.kt` con los mismos argumentos de línea de comandos que usamos antes, verás la siguiente salida:

```
aaa 42 3.14159
```

##### 2.2.2. Bibliotecas para manejar argumentos de la línea de comandos
[clikt](https://ajalt.github.io/clikt/) y [kotlinx-cli](https://github.com/Kotlin/kotlinx-cli) son dos bibliotecas que facilitan el manejo de los argumentos que facilita el parseo y procesado de los argumentos que se le pasan al programa. Aunque podemos realizarlo nosotros mismos.


## Fuente

- [Formatos de String en Kotlin](https://hackaprende.com/2020/11/25/formatos-de-string-en-kotlin/)   
- [Kotlin String Formatting](https://stonesoupprogramming.com/2017/11/17/kotlin-string-formatting/)   
- [Format](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/format.html)   
- [Add padding to a string in Kotlin](https://www.techiedelight.com/add-padding-to-a-string-in-kotlin/)   
- [padStart](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.text/pad-start.html)   
- [IO Entra y salida de datos en consola](https://kotlindoc.blogspot.com/2019/04/io-entrada-y-salida-de-datos-en-consola.html)   
- [Kotlin command line arguments](https://www.demo2s.com/kotlin/kotlin-command-line-arguments.html)   