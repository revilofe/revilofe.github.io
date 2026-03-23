---
title: "UD 7 - 7.4 Lectura y escritura de archivos"
description: Fundamentos para leer y escribir información en ficheros de texto y binarios con Kotlin
summary: Visión general de cómo almacenar y recuperar información en archivos, diferenciando texto y binario, lectura y escritura, y buenas prácticas básicas.
authors:
    - Eduardo Fdez
date: 2026-03-19
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.4
categories:
    - PROG
tags:
    - Kotlin
    - Ficheros
    - Lectura
    - Escritura
---

## 7.4 Lectura y escritura de archivos

En `7.3` aprendimos a representar rutas con `File` y a consultar información sobre ficheros y carpetas. El siguiente paso natural es **trabajar con el contenido** de esos ficheros: leerlo, procesarlo, modificarlo o guardarlo.

> Este tema conecta directamente con los criterios del `RA5` relacionados con:    
>    - d) usar ficheros para **almacenar y recuperar información**.    
>    - e) crear programas que utilicen **distintos métodos de acceso al contenido de los ficheros**.    


!!! abstract "Qué vas a aprender en este tema"
    - Diferenciar lectura y escritura de archivos.
    - Entender la diferencia entre ficheros de texto y binarios.
    - Reconocer operaciones habituales de lectura y escritura en Kotlin.
    - Aplicar buenas prácticas básicas al trabajar con archivos.

### 1. ¿Por qué leer y escribir archivos?

Guardar datos en memoria no basta cuando queremos que la información permanezca entre distintas ejecuciones del programa. Por eso los ficheros son tan importantes: permiten conservar datos, compartirlos con otros programas y recuperarlos más adelante.

Algunos ejemplos habituales:

- guardar notas del alumnado;
- registrar eventos o errores;
- cargar configuraciones al arrancar;
- exportar resultados a un informe;
- almacenar datos para volver a usarlos en otro momento.

Cuando trabajamos con archivos, normalmente realizamos dos tipos de operación:

- **lectura**: obtener información desde un fichero hacia el programa;
- **escritura**: enviar información desde el programa hacia un fichero.

### 2. Texto y binario

Antes de leer o escribir, conviene distinguir dos grandes formas de almacenar información.

#### 2.1. Ficheros de texto

En un fichero de texto la información se representa como caracteres. Suelen poder abrirse con un editor de texto y resultan cómodos para:

- configuraciones;
- listados;
- archivos CSV;
- logs;
- informes.

Ejemplo de contenido textual:

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

#### 2.2. Ficheros binarios

En un fichero binario la información se almacena como bytes, no como texto legible directamente. Son habituales en:

- imágenes;
- audio y vídeo;
- documentos ofimáticos;
- datos serializados;
- estructuras compactas de datos.

!!! note "Idea clave"
    Texto y binario no son “mejor” o “peor”. Cada formato responde a necesidades distintas.

### 3. Acceso secuencial

En muchos programas, el contenido de un fichero se procesa **en orden**, desde el principio hasta el final. Esto se llama **acceso secuencial**.

Es el modelo más habitual en esta unidad y se parece bastante a lo que ya hacíamos con la consola:

- leemos una línea;
- o escribimos un dato detrás de otro;
- sin “saltar” constantemente a posiciones intermedias.

!!! definition "Acceso secuencial"
    Consiste en procesar los datos en el mismo orden en que aparecen almacenados en el fichero.

### 4. Leer ficheros de texto

Kotlin ofrece varias formas sencillas de leer ficheros de texto a partir de `java.io.File`.

#### 4.1. Leer todo el contenido

Si el fichero no es muy grande, podemos leerlo completo con `readText()`:

```kotlin
import java.io.File

fun main() {
    val contenido = File("datos/notas.txt").readText()
    println(contenido)
}
```

Esta opción es cómoda, pero no siempre conviene si el archivo es muy grande.

#### 4.2. Leer línea a línea

Si nos interesa trabajar por líneas, podemos usar `readLines()`:

```kotlin
import java.io.File

fun main() {
    val lineas = File("datos/notas.txt").readLines()

    for (linea in lineas) {
        println(linea)
    }
}
```

#### 4.3. Procesar de forma más eficiente

Cuando el fichero crece, resulta útil `useLines()`, porque permite procesar líneas sin cargar todo el contenido de golpe:

```kotlin
import java.io.File

fun main() {
    File("datos/notas.txt").useLines { lineas ->
        lineas.forEach { println(it) }
    }
}
```

!!! tip "Cuándo usar cada una"
    - `readText()` si quieres todo el contenido como una única cadena.
    - `readLines()` si quieres una lista de líneas.
    - `useLines()` si el archivo puede ser grande o quieres procesarlo de forma más eficiente.

### 5. Escribir ficheros de texto

Kotlin también facilita mucho la escritura en archivos de texto.

#### 5.1. Sobrescribir contenido

`writeText()` escribe el contenido indicado y, si el fichero ya existe, **reemplaza** lo que hubiera antes.

```kotlin
import java.io.File

fun main() {
    File("salida.txt").writeText("Hola desde Kotlin\n")
}
```

#### 5.2. Añadir contenido al final

Si no quieres borrar lo anterior, puedes usar `appendText()`:

```kotlin
import java.io.File

fun main() {
    File("log.txt").appendText("Nueva entrada\n")
}
```

#### 5.3. Escritura con `bufferedWriter`

Otra opción es usar un escritor con buffer y `use()` para asegurar el cierre correcto:

```kotlin
import java.io.File

fun main() {
    File("salida.txt").bufferedWriter().use { writer ->
        writer.write("Primera línea\n")
        writer.write("Segunda línea\n")
    }
}
```

!!! warning "Muy importante"
    `writeText()` sobrescribe el contenido existente. Si necesitas conservar lo anterior, usa `appendText()` o un modo de escritura equivalente.

### 6. Leer y escribir no es lo mismo

Cuando trabajamos con un fichero, es importante tener claro qué operación estamos realizando en cada momento.

- **Leer** significa interpretar datos que ya existen.
- **Escribir** significa generar o modificar datos dentro del fichero.

Esto parece obvio, pero tiene consecuencias didácticas importantes:

- al leer, debes saber qué formato esperas;
- al escribir, debes decidir cómo vas a organizar la información;
- y ambas partes deben ser coherentes entre sí.

Por ejemplo, si escribes varias notas separadas por comas, luego tendrás que leerlas respetando ese mismo formato.

### 7. Errores frecuentes al trabajar con texto

Cuando se empieza a trabajar con archivos, aparecen varios errores típicos:

- intentar leer un fichero que no existe;
- no comprobar si la ruta es correcta;
- sobrescribir datos sin querer;
- no respetar el formato esperado del archivo;
- suponer que el contenido siempre será válido;
- cargar en memoria ficheros más grandes de lo necesario.

!!! warning "Error muy común"
    Si escribes datos en un formato y después intentas leerlos con otra lógica distinta, el programa fallará o interpretará mal la información.

### 8. Introducción a los ficheros binarios

Aunque en clase trabajaremos mucho con texto, también existen situaciones en las que interesa usar binario.

En Java y Kotlin podemos apoyarnos en clases como:

- `DataOutputStream` para escribir datos binarios;
- `DataInputStream` para leerlos.

```kotlin
import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.FileInputStream
import java.io.FileOutputStream

fun main() {
    DataOutputStream(FileOutputStream("datos.bin")).use { salida ->
        salida.writeInt(25)
        salida.writeBoolean(true)
    }

    DataInputStream(FileInputStream("datos.bin")).use { entrada ->
        val numero = entrada.readInt()
        val activo = entrada.readBoolean()

        println("Número: $numero")
        println("Activo: $activo")
    }
}
```

#### 8.1. La regla clave del binario

Cuando se trabaja con binario, los datos deben leerse **en el mismo orden y con los mismos tipos** con los que se escribieron.

Si escribes:

1. un `Int`
2. un `Boolean`

después tendrás que leer:

1. un `Int`
2. un `Boolean`

en ese mismo orden.

!!! danger "Regla esencial"
    En binario, cambiar el orden o el tipo de lectura rompe la interpretación de los datos.

### 9. Ejemplo integrador con fichero de texto

El siguiente ejemplo combina varias ideas del tema:

```kotlin
import java.io.File

fun main() {
    val fichero = File("pedidos.txt")

    fichero.appendText("Portátil,2\n")
    fichero.appendText("Ratón,5\n")

    val lineas = fichero.readLines()

    println("Contenido del fichero:")
    for (linea in lineas) {
        println(linea)
    }
}
```

Este ejemplo:

- escribe datos en un fichero;
- conserva el contenido previo usando `appendText()`;
- y vuelve a leerlo para mostrarlo por consola.

### 10. Relación con `U7.4.1`

Este tema ofrece la visión general de la lectura y escritura de archivos. En `7.4.1` profundizaremos en el caso más habitual en el aula: **los ficheros de texto**, con más detalle sobre:

- `readText()`, `readLines()` y `useLines()`;
- `writeText()` y `appendText()`;
- caracteres especiales como el salto de línea;
- y pequeños casos prácticos de uso.

### 11. Buenas prácticas básicas

Cuando trabajes con archivos, intenta seguir estas recomendaciones:

- usa rutas relativas cuando sea posible;
- comprueba si el fichero existe antes de leerlo;
- elige bien entre sobrescribir y añadir contenido;
- usa `use()` o funciones de alto nivel que gestionen bien los recursos;
- mantén coherencia entre cómo escribes y cómo lees;
- y separa el trabajo con archivos de la lógica principal del programa cuando el proyecto crezca.

### 12. Resumen

En este tema has visto que:

- leer y escribir archivos permite conservar información entre ejecuciones;
- los ficheros pueden ser de texto o binarios;
- el acceso secuencial es el modelo más habitual en esta unidad;
- Kotlin facilita la lectura con `readText()`, `readLines()` y `useLines()`;
- y facilita la escritura con `writeText()`, `appendText()` y escritores con buffer.

Con esta base ya puedes empezar a construir programas que no solo procesen datos en memoria, sino que también los guarden y los recuperen de forma persistente.

## Fuentes y referencias

- [Kotlin Stdlib - Kotlin I/O](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.io/)
- [Oracle Java SE - `DataInputStream`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/DataInputStream.html)
- [Oracle Java SE - `DataOutputStream`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/DataOutputStream.html)
- [Oracle Java SE - `BufferedReader`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedReader.html)
- [Oracle Java SE - `BufferedWriter`](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/io/BufferedWriter.html)

## Presentación

- [PR-U7.4 - Lectura y escritura de archivos](https://revilofe.github.io/slides/section1-pr/PR-U7.4.-LecturaEscritura.html)
