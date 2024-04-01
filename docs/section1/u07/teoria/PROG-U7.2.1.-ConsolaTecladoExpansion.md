---
title: "UD 7 - 7.2 Consola y teclado"
description: Consola y teclado expansión
summary: Consola y teclado expansión
authors:
    - Eduardo Fdez
date: 2024-03-29
icon:   
permalink: /prog/unidad7/7.2.1
categories:
    - PROG
tags:
    - Software
    - Consola
    - Teclado
---

## 7.2.1  Lectura de Datos desde Teclado en Kotlin

En Kotlin, la captura y manejo de datos introducidos por el usuario se realiza de manera eficiente y segura. 

A diferencia de Java, Kotlin ofrece un mecanismo simplificado para leer datos del teclado a través de la función `readLine()`. Esta función es parte de la biblioteca estándar de Kotlin y devuelve un valor de tipo `String?`, lo que indica que el resultado puede ser una cadena de texto o un valor nulo (`null`).

La lectura de datos desde el teclado es una tarea común en aplicaciones de consola, donde se requiere interactuar con el usuario solicitando y procesando su entrada. Kotlin maneja esta tarea de forma concisa, pero poderosa, permitiendo el manejo de diferentes tipos de datos con facilidad y seguridad.

Para realizar la lectura de datos desde el teclado en Kotlin, se emplea la siguiente sintaxis básica:

```kotlin
fun main() {
    println("Introduce un dato:")
    val dato: String? = readLine()
    println("Dato introducido: $dato")
}
```

Este enfoque básico se puede expandir para leer diferentes tipos de datos, como números enteros, decimales, entre otros, mediante la conversión del texto leído a los tipos de datos deseados. Es importante destacar que, al trabajar con `readLine()`, siempre debemos considerar la posibilidad de que el resultado sea `null`, especialmente si se espera realizar conversiones de tipo.

En los siguientes puntos, exploraremos cómo leer tipos específicos de datos desde el teclado y cómo utilizar `readLine()` y `readln()` en conjunción con conversiones de tipo para manejar entradas numéricas y otros tipos de datos de manera segura en Kotlin.

Este marco general proporciona la base para entender cómo Kotlin facilita la interacción con el usuario a través de la entrada de datos en aplicaciones de consola, manteniendo al mismo tiempo las prácticas de seguridad de tipo que son fundamentales en Kotlin.

### 1. Lectura de Texto en Kotlin

La lectura de texto del usuario es una tarea común en muchas aplicaciones de consola. Kotlin simplifica esta operación con el uso de la función `readLine()`, que lee una línea completa de entrada hasta que se encuentra un salto de línea (por ejemplo, cuando el usuario presiona Enter). Esta función devuelve un `String?`, lo que significa que el resultado puede ser una cadena de caracteres o un valor nulo (`null`). Esto último ocurre si se alcanza el final del flujo de entrada sin leer ningún dato.

#### 1.1. Ejemplo Básico de Lectura de Texto:

```kotlin
fun main() {
    println("Por favor, introduce tu nombre:")
    val nombre: String? = readLine()
    if (nombre != null) {
        println("Hola, $nombre!")
    } else {
        println("No se ha introducido ningún nombre.")
    }
}
```

```kotlin
fun main() {
    println("Por favor, introduce tu nombre:")
    val nombre: String? = readLine()
    nombre?.let { unNombre ->
        println("Hola, $unNombre!")
    } ?: println("No se ha introducido ningún nombre.")
}
```

En este ejemplo, se solicita al usuario que introduzca su nombre. Usamos `readLine()` para leer esta entrada desde el teclado. La comprobación `if (nombre != null)` es necesaria porque, aunque es raro en aplicaciones interactivas, `readLine()` puede devolver `null` si no hay más datos para leer, se llega a `EOF` (esto podría suceder, por ejemplo, si la entrada se redirige desde un archivo que termina).

> EOF: End of File. Fin de archivo. Acrónimo que se usa para indicar que no hay más datos para leer.

#### 1.2. Consideraciones de Seguridad Tipo:

Dado que `readLine()` devuelve un `String?`, el manejo de `null` es una parte crucial de la lectura segura de entradas en Kotlin. Kotlin introduce el concepto de seguridad de tipo nulo en el nivel del lenguaje, lo que significa que debemos tratar explícitamente la posibilidad de valores nulos. Esto ayuda a prevenir errores comunes como `NullPointerException` que son frecuentes en otros lenguajes de programación.

#### 1.3. Conversión Segura de Tipos:

En ocasiones, además de leer texto, querrás convertir esa entrada a un tipo específico, como un número. Kotlin facilita esto con funciones como `toIntOrNull()` que se puede usar en cadena con `readLine()` para una conversión segura:

```kotlin
fun main() {
    println("Introduce tu edad:")
    val edad: Int? = readLine()?.toIntOrNull()
    if (edad != null) {
        println("Tienes $edad años.")
    } else {
        println("Edad no válida.")
    }
}
```

Este enfoque garantiza que tu programa maneje de manera segura tanto las entradas nulas como las que no son convertibles al tipo deseado, evitando así excepciones en tiempo de ejecución.

En resumen, la lectura de texto en Kotlin es simple y segura, gracias a la función `readLine()` y al sistema de tipos de Kotlin que maneja `null` de forma explícita, evitando errores comunes en la entrada de datos.


### 2. Lectura de Números en Kotlin

La lectura de datos numéricos desde el teclado es una tarea frecuente en aplicaciones de consola. Kotlin maneja la lectura de números de una manera segura y eficiente, permitiendo la conversión de la entrada de texto a diversos tipos numéricos como `Int`, `Double`, `Float`, etc.

#### 2.1. Ejemplo Básico de Lectura de un Entero

```kotlin
fun main() {
    println("Introduce un número entero:")
    val numero: Int? = readLine()?.toIntOrNull()

    numero.?let { unNumero ->
        println("El número introducido es $unNumero.")
    } ?: println("No se ha introducido un número entero válido.")

}
```

Este ejemplo solicita al usuario que introduzca un número entero. Utiliza `readLine()` para leer la entrada como texto y luego `toIntOrNull()` para intentar convertir esa entrada en un `Int`. Si la conversión falla (por ejemplo, si el usuario introduce texto que no se puede interpretar como un entero), `toIntOrNull()` devuelve `null`.

Seguidamente, `let { unNumero -> ... }` es una forma de ejecutar un bloque de código si el valor no es nulo. En este caso, si el número no es nulo, se imprime en la consola. De lo contrario, se muestra un mensaje de error.

#### 2.2. Lectura de Otros Tipos Numéricos

De manera similar, se pueden leer otros tipos numéricos usando las funciones de conversión correspondientes, como `toDoubleOrNull()` para `Double`, `toFloatOrNull()` para `Float`, etc. Estas funciones siguen el mismo patrón que `toIntOrNull()`, proporcionando una forma segura de intentar convertir la entrada de texto en el tipo numérico deseado.

```kotlin
fun main() {
    println("Introduce un número decimal:")
    val decimal: Double? = readLine()?.toDoubleOrNull()

    if (decimal != null) {
        println("El número decimal introducido es $decimal.")
    } else {
        println("No se ha introducido un número decimal válido.")
    }
}
```

#### 2.3. Consideraciones Importantes

- **Manejo de `null`**: Es crucial manejar el caso de `null` al leer números para evitar `NullPointerException`. La utilización de `toIntOrNull()`, `toDoubleOrNull()`, etc., y verificar el resultado antes de usarlo, es una práctica recomendada.
- **Validación de Entrada**: Cuando se solicitan datos numéricos específicos, es importante validar la entrada para asegurarse de que cumple con los requisitos esperados (por ejemplo, un número dentro de un rango específico).
- **Usabilidad**: Para mejorar la experiencia del usuario, considera proporcionar mensajes de error claros o instrucciones en caso de entradas inválidas.

El manejo seguro y eficiente de la entrada numérica en Kotlin ayuda a crear aplicaciones robustas y amigables para el usuario, aprovechando las ventajas del sistema de tipos de Kotlin y su tratamiento de los valores nulos.

### 3. Uso de la Clase Scanner en Kotlin para la Lectura de Datos

Aunque Kotlin proporciona `readLine()` para leer datos del teclado, en ciertos casos, cuando necesitamos leer diferentes tipos de datos de manera secuencial o realizar lecturas más complejas, todavía podemos beneficiarnos del uso de `Scanner` de Java. Esto demuestra la potente interoperabilidad de Kotlin con Java, permitiéndonos acceder a todo el ecosistema de bibliotecas de Java.

#### 3.1. Ejemplo de Uso de Scanner en Kotlin

Para utilizar `Scanner` en Kotlin, primero debemos importar la clase de Java:

```kotlin
import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    println("Introduce tu nombre:")
    val nombre = scanner.nextLine()
    println("Hola, $nombre.")

    println("Introduce tu edad:")
    val edad = scanner.nextInt()
    // Consumir la línea restante después de un número entero
    scanner.nextLine()

    println("Introduce tu ciudad:")
    val ciudad = scanner.nextLine()

    println("Tu nombre es $nombre, tienes $edad años y vives en $ciudad.")
}
```

#### 3.2. Detalles Importantes

- **Consumir la Nueva Línea**: Después de leer un dato numérico (como `nextInt()`), es importante llamar a `nextLine()` para consumir el resto de la línea (incluido el salto de línea) antes de la próxima llamada a `nextLine()`. Si no lo hacemos, `nextLine()` podría no funcionar como se espera, ya que leerá el salto de línea restante en lugar de la próxima entrada del usuario.
- **Interoperabilidad con Java**: Este ejemplo muestra cómo Kotlin puede usar sin problemas las clases y métodos disponibles en Java, lo que amplía significativamente las capacidades de Kotlin al proporcionar acceso a una vasta cantidad de bibliotecas existentes.
- **Manejo de Excepciones**: Al igual que en Java, al usar `Scanner` en Kotlin, debemos estar conscientes de las posibles excepciones que pueden ocurrir durante la lectura de datos, especialmente cuando los tipos de datos de entrada no coinciden con lo que esperamos.

La capacidad de utilizar `Scanner` de Java en Kotlin para leer datos del teclado es un excelente ejemplo de cómo Kotlin no solo simplifica el desarrollo sino que también mantiene la compatibilidad con Java, permitiéndonos elegir la herramienta más adecuada para cada tarea.

### 4. Actualización
En versiones recientes de Kotlin (a partir de Kotlin 1.6), se introdujo la función `readln()` como una alternativa a `readLine()`. La principal diferencia entre `readln()` y `readLine()` es que `readln()` nunca devuelve `null`. Si el flujo de entrada estándar está cerrado o llega a su fin, `readln()` lanzará una excepción (`NoSuchElementException`), en lugar de devolver `null` como lo hace `readLine()`.

Esto hace que `readln()` sea más conveniente para los casos en los que estás seguro de que la entrada estará disponible y prefieres manejar una posible falta de entrada mediante excepciones en lugar de comprobar `null`. Esta función simplifica el código en muchos casos de uso, eliminando la necesidad de comprobaciones nulas explícitas después de cada llamada a `readLine()`.

#### 4.1. Ejemplo de Uso de `readln()`

```kotlin
fun main() {
    println("Introduce tu nombre:")
    val nombre = readln() // No requiere comprobación de null
    
    println("Hola, $nombre")
}
```

#### 4.2. Ejemplo con Conversión de Tipo

Junto con `readln()`, Kotlin 1.6 también introdujo las funciones `readlnOrNull()` para casos en los que pueda ser aceptable recibir un `null` (aunque su uso es menos común que `readln()`), y funciones de extensión como `toIntOrNull()` que pueden ser encadenadas directamente después de `readln()` para la conversión de tipos.

```kotlin
fun main() {
    println("Introduce tu edad:")
    val edad = readln().toIntOrNull() // Convierte la entrada a Int, con manejo seguro de errores
    
    if (edad != null) {
        println("Tu edad es $edad")
    } else {
        println("No has introducido una edad válida.")
    }
}
```

Estas adiciones a Kotlin simplifican la lectura y el manejo de la entrada del usuario, permitiendo escribir código más claro y directo para la interacción con el usuario a través de la consola.


### 5. Ejercicios de Lectura de Datos en Kotlin

Los siguientes ejercicios en Kotlin están diseñados para reforzar el aprendizaje sobre la lectura de datos desde el teclado, abarcando desde la lectura de tipos de datos simples hasta el manejo de entrada más compleja.

#### 5.1. Ejercicio 1: Lectura de un Número y Cálculo de su Cuadrado

Este ejercicio pide al usuario que introduzca un número entero y calcula el cuadrado de este número.

```kotlin
fun main() {
    println("Introduce un número entero:")
    val numero = readLine()?.toIntOrNull()
    
    if (numero != null) {
        val cuadrado = numero * numero
        println("El cuadrado de $numero es $cuadrado")
    } else {
        println("Entrada no válida")
    }
}
```

#### 5.2. Ejercicio 2: Lectura de Datos Personales

Solicita al usuario que introduzca su nombre, edad y país de origen, y luego imprime esta información en un formato estructurado.

```kotlin
fun main() {
    println("Introduce tu nombre:")
    val nombre = readLine()
    println("Introduce tu edad:")
    val edad = readLine()?.toIntOrNull()
    println("Introduce tu país de origen:")
    val pais = readLine()

    if (nombre != null && edad != null && pais != null) {
        println("Nombre: $nombre, Edad: $edad, País de origen: $pais")
    } else {
        println("Alguna de las entradas es inválida.")
    }
}
```

#### 5.3. Ejercicio 3: Calculadora Simple

Implementa una calculadora simple que lee dos números y un operador (+, -, *, /) desde el teclado, y muestra el resultado de la operación.

```kotlin
import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)
    
    println("Introduce el primer número:")
    val numero1 = scanner.nextDouble()
    println("Introduce el operador (+, -, *, /):")
    val operador = scanner.next()[0]
    println("Introduce el segundo número:")
    val numero2 = scanner.nextDouble()
    
    val resultado = when (operador) {
        '+' -> numero1 + numero2
        '-' -> numero1 - numero2
        '*' -> numero1 * numero2
        '/' -> numero1 / numero2
        else -> "Operador no válido"
    }
    
    println("Resultado: $resultado")
}
```

Estos ejercicios cubren aspectos básicos de la lectura de datos en Kotlin y demuestran cómo manejar diferentes tipos de entrada de manera efectiva. A través de la práctica con estos ejemplos, se puede obtener una comprensión sólida de cómo procesar la entrada del usuario en aplicaciones Kotlin.


## Fuente

- [Kotlin Programming Language](https://kotlinlang.org/)
- [Kotlin Reference](https://kotlinlang.org/docs/reference/)
- [Java Scanner Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Scanner.html)
- [ReadLine Function in Kotlin](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/read-line.html) 