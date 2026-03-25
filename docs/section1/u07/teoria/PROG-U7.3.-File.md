---
title: "UD 7 - 7.3 Manejo de archivos con `File`"
description: Uso de la clase `File` para representar rutas, consultar información y gestionar archivos y directorios
summary: Introducción práctica a `java.io.File` en Kotlin para trabajar con rutas, comprobar estados y realizar operaciones básicas sobre el sistema de archivos.
authors:
    - Eduardo Fdez
date: 2026-03-19
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.3
categories:
    - PROG
tags:
    - Kotlin
    - File
    - Ficheros
    - Directorios
---

## 7.3 Manejo de archivos con `File`

En `7.1` vimos qué es un sistema de archivos y en `7.2` trabajamos la entrada y salida por consola. Ahora damos un paso más: vamos a aprender a representar rutas del sistema de archivos y a consultar información sobre ellas desde Kotlin.

La clase `File` forma parte del conjunto de herramientas básicas que
necesitamos antes de leer o escribir contenido de ficheros.

| Código | Descripción |
|--------|-------------|
| RA5 | Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases. |
| CE c | Se han reconocido las posibilidades de entrada / salida del lenguaje y las librerías asociadas. |
| CE d | Se han utilizado ficheros para almacenar y recuperar información. |

!!! abstract "Qué vas a aprender en este tema"     
    - Qué representa realmente la clase `File`.    
    - Cómo crear objetos `File` con rutas absolutas y relativas.    
    - Cómo consultar información sobre un fichero o directorio.    
    - Qué operaciones básicas permite realizar sobre el sistema de archivos.    

### 1. Qué es realmente `File`

La clase `File` pertenece al paquete `java.io`:

```kotlin
import java.io.File
```

Aunque su nombre parezca indicar que representa un archivo concreto, en realidad `File` representa **una ruta del sistema de archivos**. Esa ruta puede apuntar a:

- un fichero;
- un directorio;
- o incluso una ubicación que todavía no existe.

!!! definition "Idea clave"
    Un objeto `File` no contiene el archivo en memoria ni su contenido. Lo que representa es una ruta sobre la que el programa puede consultar información u operar.

```kotlin
val fichero = File("datos/alumnos.txt")
val carpeta = File("datos")
```

En ambos casos solo estamos creando objetos que representan rutas. No estamos leyendo todavía el contenido del fichero ni creando automáticamente la carpeta.

### 2. Crear objetos `File`

Para crear un objeto `File`, basta con pasar una ruta al constructor:

```kotlin
val ruta = File("datos/notas.txt")
```

También podemos construir rutas a partir de un directorio padre y un nombre:

```kotlin
val carpeta = File("datos")
val fichero = File(carpeta, "notas.txt")
```

Esto puede hacer el código más legible cuando trabajamos con varias rutas relacionadas.

#### 2.1. Rutas absolutas y relativas

Ya vimos en `7.1` la diferencia entre rutas absolutas y relativas. Aquí la retomamos porque es fundamental al trabajar con `File`.

- **Ruta absoluta**: indica la ruta completa desde la raíz del sistema.
- **Ruta relativa**: se interpreta a partir del directorio de trabajo del programa.

Ejemplos:

- absoluta en Windows: `C:\Usuarios\ana\documentos\notas.txt`
- absoluta en Linux/macOS: `/home/ana/documentos/notas.txt`
- relativa: `datos/notas.txt`

```kotlin
val absoluta = File("/home/ana/documentos/notas.txt")
val relativa = File("datos/notas.txt")
```

!!! tip "Buena práctica"
    En ejemplos y proyectos de aula suelen ser preferibles las rutas relativas, porque hacen el código más portable entre distintos ordenadores.

#### 2.2. Directorio de trabajo

Cuando usas una ruta relativa, Kotlin la interpreta tomando como referencia el **directorio de trabajo**.

```kotlin
val fichero = File("datos/notas.txt")
println(fichero.absolutePath)
```

Este ejemplo no imprime la ruta relativa, sino la ruta completa resultante según dónde se esté ejecutando el programa.

### 3. Consultar información de una ruta

Una vez creado un objeto `File`, podemos consultar distintos datos sobre la ruta que representa.

#### 3.1. Nombre, carpeta padre y ruta absoluta

Algunas propiedades muy útiles son:

- `name`: nombre del fichero o directorio.
- `parent`: ruta de la carpeta padre.
- `absolutePath`: ruta completa.

```kotlin
import java.io.File

fun main() {
    val fichero = File("datos/notas.txt")

    println("Nombre: ${fichero.name}")
    println("Carpeta padre: ${fichero.parent}")
    println("Ruta absoluta: ${fichero.absolutePath}")
}
```

Estas propiedades ayudan mucho a entender qué ruta está manejando realmente el programa.

#### 3.2. Comprobar si existe

Antes de intentar trabajar con un fichero o directorio, conviene comprobar si existe:

```kotlin
val ruta = File("datos/notas.txt")

if (ruta.exists()) {
    println("La ruta existe")
} else {
    println("La ruta no existe")
}
```

#### 3.3. Saber si es fichero o directorio

No basta con saber que una ruta existe. A veces necesitamos distinguir si se trata de un fichero o de una carpeta:

```kotlin
val ruta = File("datos")

println("¿Existe? ${ruta.exists()}")
println("¿Es fichero? ${ruta.isFile}")
println("¿Es directorio? ${ruta.isDirectory}")
```

!!! info "Ojo"
    Que una ruta termine en algo como `.txt` no garantiza por sí sola que sea un fichero real. Para saberlo de verdad, hay que consultar el sistema de archivos.

#### 3.4. Tamaño y fecha de modificación

Si la ruta representa un fichero existente, también podemos consultar metadatos:

- `length()`: tamaño en bytes.
- `lastModified()`: instante de la última modificación, expresado en milisegundos.

```kotlin
import java.io.File
import java.util.Date

fun main() {
    val fichero = File("datos/notas.txt")

    if (fichero.exists() && fichero.isFile) {
        println("Tamaño: ${fichero.length()} bytes")
        println("Última modificación: ${Date(fichero.lastModified())}")
    }
}
```

Este tipo de información es útil, por ejemplo, para saber si un fichero está vacío o cuándo se actualizó por última vez.

### 4. Operaciones básicas con directorios y rutas

La clase `File` no sirve solo para consultar información. También permite realizar operaciones sencillas sobre archivos y directorios.

#### 4.1. Crear directorios

Para crear una carpeta se puede usar `mkdir()`:

```kotlin
val carpeta = File("salidas")
val creada = carpeta.mkdir()

println("¿Carpeta creada? $creada")
```

Si necesitas crear varias carpetas anidadas de una vez, suele ser más práctico `mkdirs()`:

```kotlin
val carpetas = File("salidas/2026/marzo")
carpetas.mkdirs()
```

#### 4.2. Borrar archivos o carpetas

Para borrar una ruta se puede usar `delete()`:

```kotlin
val temporal = File("temporal.txt")
val borrado = temporal.delete()

println("¿Se ha borrado? $borrado")
```

Si la ruta corresponde a un directorio, normalmente solo se podrá borrar si está vacío.

!!! warning "Importante"
    `delete()` devuelve `false` si la operación no se puede realizar. Por ejemplo, cuando el fichero no existe, cuando faltan permisos o cuando la carpeta no está vacía.

#### 4.3. Renombrar o mover

El método `renameTo()` permite cambiar el nombre o mover un fichero o directorio a otra ruta:

```kotlin
val origen = File("borrador.txt")
val destino = File("entrega.txt")

val cambiado = origen.renameTo(destino)
println("¿Renombrado correctamente? $cambiado")
```

Si origen y destino están en carpetas distintas, además de renombrar se estará moviendo la ruta.

### 5. Listar el contenido de una carpeta

Cuando una ruta representa un directorio, podemos consultar sus elementos con `listFiles()`:

```kotlin
import java.io.File

fun main() {
    val carpeta = File("datos")
    val elementos = carpeta.listFiles()

    if (elementos != null) {
        for (elemento in elementos) {
            if (elemento.isDirectory) {
                println("[DIR] ${elemento.name}")
            } else {
                println("[FILE] ${elemento.name}")
            }
        }
    }
}
```

Este método resulta muy útil para:

- mostrar el contenido de un directorio;
- filtrar ficheros;
- recorrer una carpeta de trabajo;
- o preparar procesos por lotes.

### 6. Crear ficheros vacíos

Aunque el trabajo de lectura y escritura se desarrolla en `7.4`, conviene saber que `File` también permite crear un fichero vacío mediante `createNewFile()`:

```kotlin
import java.io.File

fun main() {
    val fichero = File("registro.txt")
    val creado = fichero.createNewFile()

    println("¿Se ha creado el fichero? $creado")
}
```

Este método:

- crea el fichero si no existía;
- devuelve `true` si lo ha creado;
- y devuelve `false` si ya existía.

!!! note "Puente con el siguiente tema"
    En este apartado nos centramos en representar rutas y gestionar archivos o carpetas. La lectura y escritura de contenido la desarrollaremos en `7.4`.

### 7. Ejemplo integrador

El siguiente ejemplo combina varias ideas del tema:

```kotlin
import java.io.File

fun main() {
    val carpeta = File("datos")

    if (!carpeta.exists()) {
        carpeta.mkdir()
    }

    val fichero = File(carpeta, "notas.txt")

    println("Ruta absoluta: ${fichero.absolutePath}")
    println("¿Existe? ${fichero.exists()}")
    println("¿Es fichero? ${fichero.isFile}")
    println("¿Carpeta padre? ${fichero.parent}")
}
```

Este programa no escribe todavía contenido en el fichero, pero sí muestra cómo `File` nos permite:

- construir rutas;
- apoyarnos en rutas relativas;
- comprobar estados;
- y consultar información útil del sistema de archivos.

### 8. Buenas prácticas iniciales

Cuando trabajes con `File`, intenta recordar estas ideas:

- usa rutas relativas siempre que tenga sentido;
- comprueba si una ruta existe antes de operar con ella;
- distingue entre fichero y directorio;
- evita ejemplos rígidos ligados a una unidad concreta como `C:/Temp`;
- y no confundas “representar una ruta” con “leer o escribir el contenido”.

### 9. Resumen

En este tema has visto que:

- `File` representa rutas del sistema de archivos;
- puede referirse tanto a ficheros como a directorios;
- permite consultar propiedades como nombre, padre, ruta absoluta, tamaño o fecha;
- permite hacer comprobaciones de estado como `exists()`, `isFile` e `isDirectory`;
- y ofrece operaciones básicas de gestión como crear carpetas, borrar, renombrar y listar contenido.

Con esta base ya estamos preparados para pasar al siguiente paso: **leer y escribir datos dentro de los ficheros**.

## Fuentes y referencias

- [Oracle Java SE - `java.io.File`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/File.html)
- [Oracle Java SE - `java.nio.file.Path`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/nio/file/Path.html)
- [Kotlin Stdlib - Kotlin I/O](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/)

## Presentación

- [PR-U7.3 - Manejo de archivos con File](https://revilofe.github.io/slides/section1-pr/PR-U7.3.-File.html)
