---
title: "UD 7 - 7.4.1 Ficheros de texto"
description: Trabajo práctico con lectura y escritura de ficheros de texto en Kotlin
summary: Detalle técnico de los ficheros de texto en Kotlin - lectura completa, lectura por líneas, escritura, añadido de contenido, caracteres especiales y buenas prácticas.
authors:
    - Eduardo Fdez
date: 2026-03-19
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.4.1
categories:
    - PROG
tags:
    - Kotlin
    - Ficheros
    - Texto
    - Entrada/Salida
---

## 7.4.1 Ficheros de texto

En `7.4` vimos la visión general de la lectura y escritura de archivos. En esta ampliación nos centramos en el caso más habitual en el aula: **los ficheros de texto**.

Trabajar con texto es muy común porque permite guardar información de forma sencilla, visible y fácil de depurar. Además, es ideal para practicar cómo leer, escribir y procesar datos persistentes en programas pequeños y medianos.

| Código | Descripción |
|--------|-------------|
| RA5 | Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases. |
| CE d | Se han utilizado ficheros para almacenar y recuperar información. |
| CE e | Se han creado programas que utilicen diversos métodos de acceso al contenido de los ficheros. |

!!! abstract "Qué vas a aprender en este apartado"    
    - Cuándo conviene usar un fichero de texto.    
    - Cómo leer un fichero completo o línea a línea.     
    - Cómo escribir texto sobrescribiendo o añadiendo contenido.     
    - Cómo influyen caracteres como `\n`, `\r` y `\t`.

### 1. Qué es un fichero de texto

Un fichero de texto almacena la información como caracteres. Eso hace que, en muchos casos, podamos abrirlo con un editor y entender su contenido directamente.

Ejemplos típicos:

- configuraciones;
- listados de datos;
- archivos CSV;
- informes;
- registros de eventos.

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

!!! note "Ventaja principal"
    Los ficheros de texto son muy cómodos para aprender, porque permiten ver de forma directa qué se ha guardado realmente.

### 2. Crear una referencia al fichero

Antes de leer o escribir, necesitamos una referencia al fichero mediante `File`:

```kotlin
import java.io.File

val fichero = File("datos/notas.txt")
```

Esto no lee todavía el contenido. Solo prepara la ruta con la que vamos a trabajar.

### 3. Leer ficheros de texto

Kotlin ofrece varias formas de leer ficheros de texto. La elección depende de cuánto contenido quieras leer y de cómo vayas a procesarlo.

#### 3.1. Leer todo con `readText()`

Si el fichero es pequeño o mediano, `readText()` resulta muy cómodo:

```kotlin
import java.io.File

fun main() {
    val contenido = File("datos/notas.txt").readText()
    println(contenido)
}
```

Úsalo cuando necesites el contenido completo como una única cadena.

#### 3.2. Leer todas las líneas con `readLines()`

Si te interesa trabajar por líneas, `readLines()` devuelve una lista:

```kotlin
import java.io.File

fun main() {
    val lineas = File("datos/notas.txt").readLines()

    for (linea in lineas) {
        println(linea)
    }
}
```

Esta opción es práctica cuando el fichero no es enorme y quieres recorrerlo después con comodidad.

#### 3.3. Procesar línea a línea con `useLines()`

Si el fichero puede crecer mucho, `useLines()` permite procesar el contenido de forma más eficiente:

```kotlin
import java.io.File

fun main() {
    File("datos/notas.txt").useLines { lineas ->
        lineas.forEach { println(it) }
    }
}
```

Con `useLines()` no necesitas cargar todo el fichero a memoria a la vez.

!!! tip "Elección rápida"
    - `readText()` para obtener una sola cadena.
    - `readLines()` para trabajar con una lista de líneas.
    - `useLines()` para ficheros grandes o procesamiento secuencial.

### 4. Escribir en ficheros de texto

La escritura también puede hacerse de distintas formas según lo que necesites.

#### 4.1. Sobrescribir con `writeText()`

`writeText()` escribe texto en el fichero y reemplaza el contenido anterior si ya existía:

```kotlin
import java.io.File

fun main() {
    File("salida.txt").writeText("Hola desde Kotlin\n")
}
```

Es útil cuando quieres generar el fichero desde cero o rehacerlo completamente.

#### 4.2. Añadir con `appendText()`

Si quieres conservar lo anterior y escribir al final, usa `appendText()`:

```kotlin
import java.io.File

fun main() {
    File("log.txt").appendText("Nueva entrada\n")
}
```

Esto es muy útil para historiales, registros o acumulación de resultados.

#### 4.3. Escribir con `bufferedWriter()`

Otra opción es usar un escritor con buffer:

```kotlin
import java.io.File

fun main() {
    File("salida.txt").bufferedWriter().use { writer ->
        writer.write("Primera línea\n")
        writer.write("Segunda línea\n")
    }
}
```

Aquí aparece `use()`, que garantiza que el recurso se cierre correctamente al terminar.

!!! warning "Muy importante"
    `writeText()` borra el contenido anterior. Si necesitas conservar lo ya escrito, usa `appendText()`.

### 5. Leer y escribir con el mismo formato

Cuando un programa escribe información en un fichero de texto, debe hacerlo siguiendo un formato claro. Después, al leer ese fichero, hay que respetar ese mismo formato.

Por ejemplo, si decides guardar cada alumno así:

```text
Ana,8.5
Luis,7.25
```

al leer tendrás que tener presente que:

- cada línea representa un alumno;
- el separador es la coma;
- el primer dato es el nombre;
- el segundo dato es la nota.

Si cambias el formato al escribir y no ajustas la lectura, el programa fallará o interpretará mal los datos.

### 6. Caracteres especiales importantes

En los ficheros de texto aparecen caracteres que no siempre se ven de forma explícita, pero que afectan mucho al resultado.

#### 6.1. Salto de línea `\n`

Sirve para empezar una nueva línea:

```kotlin
val texto = "Primera línea\nSegunda línea"
println(texto)
```

#### 6.2. Retorno de carro `\r`

En sistemas Windows suele combinarse con `\n` para formar `\r\n`.

```kotlin
val textoWindows = "Primera línea\r\nSegunda línea"
println(textoWindows)
```

#### 6.3. Tabulador `\t`

Permite alinear texto en columnas sencillas:

```kotlin
val tabla = "Nombre\tNota\nAna\t8.5"
println(tabla)
```

#### 6.4. Fin de fichero

Cuando lees un fichero secuencialmente, llega un momento en que no quedan más datos. A eso se le llama **fin de fichero** o **EOF**.

Por eso, al leer línea a línea, conviene usar mecanismos que sepan detenerse correctamente, como `useLines()` o un bucle que controle el final de lectura.

### 7. Ejemplos prácticos

#### 7.1. Contar líneas

```kotlin
import java.io.File

fun main() {
    val numeroDeLineas = File("datos/notas.txt").useLines { it.count() }
    println("El fichero tiene $numeroDeLineas líneas.")
}
```

#### 7.2. Registro de eventos

```kotlin
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun registrarEvento(evento: String) {
    val marcaTiempo = LocalDateTime.now()
        .format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))

    File("registro.txt").appendText("[$marcaTiempo] $evento\n")
}

fun main() {
    registrarEvento("Inicio de la aplicación")
    registrarEvento("Operación completada")
}
```

#### 7.3. Leer y mostrar un pequeño informe

```kotlin
import java.io.File

fun main() {
    val informe = File("informe.txt")

    if (!informe.exists()) {
        println("El fichero no existe.")
        return
    }

    println("Contenido del informe:")
    println(informe.readText())
}
```

### 8. Buenas prácticas

Cuando trabajes con ficheros de texto, intenta seguir estas ideas:

- comprueba si el fichero existe antes de leerlo, cuando tenga sentido hacerlo;
- usa rutas relativas si el proyecto va a moverse entre equipos;
- diferencia claramente entre sobrescribir y añadir contenido;
- usa `use()` cuando trabajes con lectores o escritores explícitos;
- no cargues en memoria ficheros enormes si puedes procesarlos por líneas;
- y define un formato claro si luego vas a volver a leer el fichero.

!!! tip "Consejo didáctico"
    Si estás empezando, piensa siempre en dos preguntas: “¿cómo voy a guardar esto?” y “¿cómo lo recuperaré después?”.

### 9. Errores frecuentes

- leer un fichero que no existe;
- usar `writeText()` cuando querías añadir y no sobrescribir;
- no incluir saltos de línea y dejar todos los datos pegados;
- suponer que el contenido siempre tendrá el formato esperado;
- usar `readText()` con ficheros demasiado grandes sin necesidad.

### 10. Resumen

En este apartado has visto que:

- los ficheros de texto son muy útiles para almacenar información legible;
- Kotlin ofrece varias formas cómodas de leerlos y escribirlos;
- `readText()`, `readLines()` y `useLines()` responden a necesidades distintas;
- `writeText()` sobrescribe y `appendText()` añade;
- y los caracteres especiales como `\n` o `\t` influyen directamente en el formato final.

Con esto queda cerrada la parte de trabajo básico con ficheros de texto de la unidad.

## Fuentes y referencias

- [Kotlin Stdlib - Kotlin I/O](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/)
- [Oracle Java SE - `BufferedReader`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedReader.html)
- [Oracle Java SE - `BufferedWriter`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)

## Presentación

- [PR-U7.4.1 - Ficheros de texto](https://revilofe.github.io/slides/section1-pr/PR-U7.4.1.-TextFile.html)
