---
title: "UD 7 - 7.2 Consola y teclado"
description: Ampliación sobre lectura avanzada en consola, `Scanner` y argumentos de línea de comandos
summary: Complemento de U7.2 con matices sobre `readln`, `readLine`, fin de entrada, `Scanner` y utilidades reutilizables.
authors:
    - Eduardo Fdez
date: 2026-03-18
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.2.1
categories:
    - PROG
tags:
    - Kotlin
    - Consola
    - Teclado
    - Entrada/Salida
---

## 7.2.1 Consola y teclado: ampliación

Este documento complementa `7.2`, pero no lo sustituye. Allí vimos lo esencial para trabajar con consola y teclado en Kotlin. Aquí nos centramos en los casos que suelen generar más dudas cuando el programa deja de ser tan simple:

- qué diferencias hay entre `readln()`, `readlnOrNull()` y `readLine()`;
- qué ocurre cuando la entrada se termina;
- cuándo puede tener sentido usar `Scanner`;
- cómo crear funciones reutilizables para pedir datos;
- y cómo encajan los argumentos de línea de comandos en el trabajo con programas de consola.

!!! abstract "Objetivo de esta ampliación"
    Profundizar en situaciones reales de entrada por consola que no cabían en el tema principal, manteniendo el foco en el `RA5`.

### 1. `readln()`, `readlnOrNull()` y `readLine()`

En ejemplos actuales de Kotlin suele aparecer `readln()`, pero todavía es frecuente encontrar `readLine()` en materiales antiguos o en código heredado. Conviene distinguir bien cuándo usar cada opción.

| Función | Devuelve | Comportamiento |
| --- | --- | --- |
| `readln()` | `String` | Espera una línea. Si no hay entrada disponible, lanza excepción. |
| `readlnOrNull()` | `String?` | Devuelve `null` cuando no hay más datos. |
| `readLine()` | `String?` | Variante histórica, todavía válida, pero menos habitual en Kotlin moderno. |

#### 1.1. Cuándo usar cada una

- Usa `readln()` cuando trabajes con una interacción normal de consola y esperes que la persona usuaria introduzca datos.
- Usa `readlnOrNull()` cuando la entrada pueda agotarse, por ejemplo si el programa lee desde una redirección o desde un archivo.
- Reconoce `readLine()` porque sigue apareciendo en mucho código, pero no es la primera opción didáctica para esta unidad.

```kotlin
fun main() {
    print("Nombre: ")
    val nombre = readln()
    println("Hola, $nombre")
}
```

```kotlin
fun main() {
    val linea = readlnOrNull()
    if (linea == null) {
        println("No quedan más datos")
    } else {
        println("He leído: $linea")
    }
}
```

!!! note "Idea práctica"
    En ejercicios interactivos de clase, `readln()` suele ser suficiente. `readlnOrNull()` empieza a ser útil cuando la entrada no la controla directamente la persona usuaria.

### 2. Fin de entrada y `EOF`

Uno de los matices más importantes de la entrada por consola es entender que el flujo puede terminar. A ese momento se le suele llamar `EOF` (*End Of File* o fin de entrada).

Esto puede pasar, por ejemplo, cuando:

- el programa no lee desde teclado, sino desde un archivo redirigido;
- una tubería ya no tiene más datos que enviar;
- o el entorno cierra la entrada estándar.

Si usas `readln()`, el programa lanzará una excepción cuando ya no haya más datos. Si usas `readlnOrNull()`, podrás detectarlo sin excepción.

```kotlin
fun main() {
    while (true) {
        val linea = readlnOrNull() ?: break
        println("Procesando: $linea")
    }

    println("Fin de la entrada")
}
```

Este patrón resulta útil cuando quieres leer varias líneas hasta que la entrada se agote.

### 3. Uso de `Scanner` desde Kotlin

Kotlin puede usar sin problema clases de Java. Una de las más conocidas para entrada por consola es `Scanner`.

No es imprescindible para esta unidad, pero conviene conocerlo porque aparece con frecuencia en muchos ejemplos y porque en algunos contextos puede resultar cómodo para leer datos token a token.

```kotlin
import java.util.Scanner

fun main() {
    val scanner = Scanner(System.`in`)

    print("Nombre: ")
    val nombre = scanner.nextLine()

    print("Edad: ")
    val edad = scanner.nextInt()
    scanner.nextLine()

    print("Ciudad: ")
    val ciudad = scanner.nextLine()

    println("Nombre: $nombre, edad: $edad, ciudad: $ciudad")
}
```

#### 3.1. El problema del salto de línea

Cuando mezclas `nextInt()`, `nextDouble()` o métodos similares con `nextLine()`, aparece un error muy común: el salto de línea que queda pendiente puede ser consumido por la siguiente lectura.

Por eso, después de leer un número, suele hacer falta una llamada adicional a `nextLine()` para vaciar el final de línea.

!!! warning "Error frecuente con `Scanner`"
    Si después de `nextInt()` llamas a `nextLine()` y esta devuelve una cadena vacía, seguramente se debe a que aún quedaba pendiente el salto de línea anterior.

#### 3.2. ¿Cuándo compensa usar `Scanner`?

Puede tener sentido cuando:

- ya estás trabajando con materiales Java;
- quieres leer tokens separados por espacios con rapidez;
- o necesitas interoperar con ejemplos ya construidos con esta clase.

En cambio, para los ejercicios básicos e intermedios de esta unidad, `readln()` y las conversiones seguras suelen ser más claras y más fáciles de explicar.

### 4. Funciones auxiliares para pedir datos

Cuando un programa crece, repetir una y otra vez el mismo patrón de “pedir, convertir, validar y volver a pedir” hace que el código se vuelva pesado. Una mejora razonable consiste en crear funciones auxiliares.

```kotlin
fun pedirEntero(mensaje: String): Int {
    while (true) {
        print(mensaje)
        val numero = readln().toIntOrNull()

        if (numero != null) {
            return numero
        }

        System.err.println("Debes escribir un número entero válido.")
    }
}

fun main() {
    val edad = pedirEntero("Edad: ")
    val curso = pedirEntero("Curso: ")

    println("Edad: $edad | Curso: $curso")
}
```

Este enfoque tiene dos ventajas:

- evita duplicar código;
- y separa mejor la lógica de validación del resto del programa.

#### 4.1. Variante para números decimales

```kotlin
fun pedirDouble(mensaje: String): Double {
    while (true) {
        print(mensaje)
        val numero = readln().toDoubleOrNull()

        if (numero != null) {
            return numero
        }

        System.err.println("Debes escribir un número decimal válido.")
    }
}
```

Estas funciones no son obligatorias, pero ayudan mucho a escribir programas de consola más limpios.

### 5. Argumentos de línea de comandos

No toda la entrada de un programa de consola tiene por qué llegar desde teclado mientras el programa se está ejecutando. También es posible pasar información al arrancarlo mediante argumentos.

```kotlin
fun main(args: Array<String>) {
    if (args.isEmpty()) {
        println("Debes indicar al menos un nombre.")
        return
    }

    println("Hola, ${args[0]}")
}
```

Si el programa se ejecuta pasando un nombre como argumento, ese valor llegará dentro de `args`.

#### 5.1. Diferencia entre teclado y argumentos

- **Teclado**: la entrada se solicita durante la ejecución.
- **Argumentos**: la entrada se entrega antes de que el programa empiece a ejecutarse.

Ambas opciones forman parte del trabajo con programas de consola, pero no resuelven exactamente la misma necesidad.

### 6. Mini comparativa: qué mecanismo elegir

| Situación | Opción recomendable |
| --- | --- |
| Programa interactivo sencillo | `readln()` |
| Entrada que puede agotarse | `readlnOrNull()` |
| Código heredado o ejemplos antiguos | `readLine()` |
| Interoperabilidad con Java o lectura token a token | `Scanner` |
| Parámetros dados al lanzar el programa | `args: Array<String>` |

### 7. Propuestas de práctica

Para aprovechar esta ampliación, puedes probar actividades como estas:

1. Reescribir un programa hecho con `readln()` para que funcione con `readlnOrNull()`.
2. Crear una función `pedirEntero()` y reutilizarla varias veces en un mismo programa.
3. Hacer una versión de calculadora con `Scanner` y comparar su legibilidad con una versión basada en `readln()`.
4. Ejecutar un programa con argumentos y compararlo con otro que pida los datos por teclado.

### 8. Idea final que debes recordar

El tema principal `7.2` te enseña a usar la consola. Esta ampliación te ayuda a tomar mejores decisiones cuando aparecen casos menos simples: entrada que se agota, código Java heredado, validación repetitiva o datos que llegan como argumentos.

Saber elegir entre `readln()`, `readlnOrNull()`, `Scanner` o `args` forma parte de reconocer las posibilidades reales de entrada/salida del lenguaje, que es precisamente una de las ideas centrales del `RA5`.

## Fuentes

- [Kotlin Docs - Read standard input](https://kotlinlang.org/docs/read-standard-input.html)
- [Kotlin Stdlib - `readln`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/readln.html)
- [Kotlin Stdlib - `readlnOrNull`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/readln-or-null.html)
- [Kotlin Stdlib - `readLine`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/read-line.html)
- [Oracle Java SE - `Scanner`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Scanner.html)

## Presentación

- [PR-U7.2.1 - Consola y teclado: ampliación](https://revilofe.github.io/slides/section1-pr/PR-U7.2.1.-ConsolaTecladoExpansion.html)
