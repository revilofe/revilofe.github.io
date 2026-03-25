---
title: "UD 7 - 7.2 Consola y teclado"
description: Lectura y escritura en consola con Kotlin
summary: Uso de la consola, lectura por teclado, validación básica y formato de salida en Kotlin.
authors:
    - Eduardo Fdez
date: 2026-03-18
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.2
categories:
    - PROG
tags:
    - Kotlin
    - Consola
    - Teclado
    - Entrada/Salida
---

## 7.2 Lectura y escritura en consola

Después de comprender en `7.1` qué es la entrada/salida, ahora toca trabajar
con el caso más cercano y habitual: la **consola**.

La consola es el entorno más sencillo para practicar cómo un programa muestra
información, pide datos y responde a lo que introduce la persona usuaria.
Aunque parezca un caso básico, aquí aparecen ideas que luego se reutilizan en
muchos programas: validación, formato y separación entre lógica y presentación.

| Código | Descripción                                                    |
|--------|----------------------------------------------------------------|
| RA5    | Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases. |
| CE a   | Se ha utilizado la consola para realizar operaciones de entrada y salida de información. |
| CE b   | Se han aplicado formatos en la visualización de la información. |
| CE c   | Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas. |

La idea es sencilla: un programa de consola **muestra mensajes**, **pide
datos** y **responde en función de lo que introduce la persona usuaria**.

!!! abstract "Qué vas a aprender en este tema"
    - Escribir mensajes en la salida estándar y de error.
    - Leer datos desde teclado con Kotlin.
    - Validar conversiones básicas de texto a números.
    - Aplicar formato a la salida para que sea más clara y útil.

### 1. La consola como canal de entrada y salida

En una aplicación de consola trabajamos, como mínimo, con tres canales:

- **entrada estándar**, normalmente el teclado;
- **salida estándar**, normalmente la consola;
- **salida de error**, usada para avisos o mensajes de fallo.

En la JVM estos canales se representan mediante:

- `System.in`
- `System.out`
- `System.err`

En Kotlin no solemos trabajar directamente con ellos todo el tiempo, porque el lenguaje ofrece funciones más cómodas para el caso habitual de consola.

!!! note "Idea clave"
    En este tema no estamos guardando todavía información en ficheros. Aquí nos centramos en la comunicación inmediata entre la persona usuaria y el programa.

### 2. Escribir información en consola

Las funciones más habituales para mostrar texto son `print()` y `println()`.

- `print()` escribe sin salto de línea final.
- `println()` escribe y añade un salto de línea al final.

```kotlin
fun main() {
    print("Hola")
    print(" ")
    println("mundo")
    println("Segunda línea")
}
```

Salida:

```text
Hola mundo
Segunda línea
```

Si necesitas un salto de línea dentro del propio texto, puedes usar `\n`:

```kotlin
println("Línea 1\nLínea 2")
```

#### 2.1. Plantillas de cadenas

En Kotlin, la forma más cómoda de mezclar texto con variables suele ser la interpolación:

```kotlin
val nombre = "Alicia"
val nota = 8.5

println("Alumno: $nombre")
println("Nota final: $nota")
println("El doble de la nota es ${nota * 2}")
```

Esta técnica hace el código más legible que concatenar muchas cadenas con `+`.

#### 2.2. Salida de error

Cuando quieres diferenciar un mensaje correcto de uno problemático, puedes usar `System.err`:

```kotlin
System.err.println("No se ha podido leer la edad")
```

No siempre será visible de forma distinta en el terminal, pero conceptualmente es importante porque separa la salida normal de los errores.

### 3. Leer datos desde teclado

En Kotlin actual, para leer una línea completa desde teclado es habitual usar `readln()` o `readlnOrNull()`.

- `readln()` devuelve un `String`.
- `readlnOrNull()` devuelve `String?` y permite contemplar el caso en que no haya datos.

#### 3.1. Leer texto

```kotlin
fun main() {
    print("Introduce tu nombre: ")
    val nombre = readln()
    println("Hola, $nombre")
}
```

Este ejemplo es suficiente cuando esperamos una línea de texto y damos por hecho que la entrada estará disponible.

#### 3.2. Leer números con seguridad

El teclado siempre entrega texto. Si queremos obtener un número, primero leemos una cadena y después la convertimos.

La forma más segura para empezar no es `toInt()`, sino `toIntOrNull()`:

```kotlin
fun main() {
    print("Introduce tu edad: ")
    val edad = readln().toIntOrNull()

    if (edad != null) {
        println("Tienes $edad años")
    } else {
        System.err.println("La edad introducida no es válida")
    }
}
```

También existen:

- `toDoubleOrNull()`
- `toFloatOrNull()`
- `toLongOrNull()`

#### 3.3. Evita `!!` al leer datos

Es frecuente encontrar ejemplos como este:

```kotlin
val numero = readln().toInt()
```

o, en ejemplos antiguos:

```kotlin
val numero = readLine()!!.toInt()
```

Funcionan si la entrada es correcta, pero fallan con facilidad cuando la persona usuaria introduce algo inesperado. Para aplicaciones de aprendizaje y para programas robustos, conviene validar.

!!! warning "Error frecuente"
    Si conviertes directamente con `toInt()` y la entrada no es un entero válido, obtendrás una excepción en tiempo de ejecución.

#### 3.4. Repetir la petición hasta obtener un dato válido

Una mejora muy habitual consiste en seguir preguntando hasta recibir una entrada correcta:

```kotlin
fun main() {
    var cantidad: Int? = null

    while (cantidad == null) {
        print("Introduce una cantidad entera: ")
        cantidad = readln().toIntOrNull()

        if (cantidad == null) {
            System.err.println("Dato no válido. Inténtalo de nuevo.")
        }
    }

    println("Cantidad aceptada: $cantidad")
}
```

Este patrón aparece mucho en programas de consola y en actividades de clase.

### 4. Formato de salida

Una cosa es que un programa funcione y otra que su salida sea clara. No basta
con "que imprima algo": la información debe verse bien y resultar fácil de
interpretar.

#### 4.1. Cuándo basta con interpolación

Para mensajes sencillos, la interpolación suele ser suficiente:

```kotlin
val producto = "Teclado"
val precio = 19.95

println("Producto: $producto")
println("Precio: $precio €")
```

#### 4.2. Cuándo usar `format`

Si necesitas controlar decimales, anchos de columna o alineación, es más útil usar `format`:

```kotlin
val nombre = "Marta"
val nota = 7.456

println("Alumno: %s | Nota: %.2f".format(nombre, nota))
```

Salida:

```text
Alumno: Marta | Nota: 7.46
```

Algunos especificadores habituales son:

| Formato | Uso habitual |
| --- | --- |
| `%s` | texto |
| `%d` | entero |
| `%.2f` | decimal con 2 cifras |
| `%n` | salto de línea |

#### 4.3. Ejemplo de tabla sencilla

```kotlin
val articulos = listOf(
    "Cuaderno" to 2.5,
    "Bolígrafo" to 1.2,
    "Mochila" to 24.95
)

println("%-12s | %8s".format("Artículo", "Precio"))
println("-----------------------------")

for ((articulo, precio) in articulos) {
    println("%-12s | %8.2f €".format(articulo, precio))
}
```

Salida:

```text
Artículo     |   Precio
-----------------------------
Cuaderno     |     2.50 €
Bolígrafo    |     1.20 €
Mochila      |    24.95 €
```

### 5. Ejemplo integrador

El siguiente programa combina lectura por teclado, validación y formato de salida:

```kotlin
fun main() {
    print("Nombre del producto: ")
    val producto = readln()

    print("Unidades: ")
    val unidades = readln().toIntOrNull()

    print("Precio unitario: ")
    val precio = readln().toDoubleOrNull()

    if (unidades == null || precio == null) {
        System.err.println("No se puede generar el ticket porque hay datos no válidos.")
        return
    }

    val total = unidades * precio

    println()
    println("Ticket de compra")
    println("------------------------------")
    println("Producto: $producto")
    println("Unidades: %d".format(unidades))
    println("Precio/u: %.2f €".format(precio))
    println("Total: %.2f €".format(total))
}
```

Este ejemplo ya refleja una situación realista de trabajo con consola:

- se lee información desde teclado;
- se muestra información en consola;
- se valida la entrada;
- y se cuida el formato de salida.

### 6. Buenas prácticas

Cuando trabajes con consola y teclado, intenta seguir estas ideas:

- muestra mensajes claros antes de pedir cada dato;
- valida los números antes de usarlos;
- no abuses de `!!`;
- usa `System.err` para errores o avisos;
- separa, cuando el programa crezca, la lógica del cálculo y la presentación en consola.

!!! tip "Ampliación"
    Si necesitas más detalle sobre lectura avanzada, `Scanner` o variantes históricas como `readLine()`, consulta [7.2.1. Consola y teclado: ampliación](./PROG-U7.2.1.-ConsolaTecladoExpansion.md).

### 7. Resumen

En este tema has visto que:

- la consola permite interactuar con la persona usuaria de forma inmediata;
- `print()` y `println()` sirven para mostrar información;
- `readln()` y `readlnOrNull()` permiten leer desde teclado;
- la validación con `toIntOrNull()` y similares evita muchos errores;
- el formato de salida mejora la claridad del resultado.

Con esta base ya puedes crear programas sencillos de consola que pidan datos, los validen y muestren resultados de forma clara.

## Fuentes

- [Kotlin Docs - Read standard input](https://kotlinlang.org/docs/read-standard-input.html)
- [Kotlin Docs - Basic syntax](https://kotlinlang.org/docs/basic-syntax.html#print-to-the-standard-output)
- [Kotlin Docs - Strings](https://kotlinlang.org/docs/strings.html)
- [Oracle Java SE - Formatter](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Formatter.html)

## Presentación

- [PR-U7.2 - Consola y teclado](https://revilofe.github.io/slides/section1-pr/PR-U7.2.-ConsolaTeclado.html)
