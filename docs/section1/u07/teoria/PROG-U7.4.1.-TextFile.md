---

title: "UD 7 - 7.4.1 Text File"
description: Text File
summary: Text File
authors:
  - Eduardo Fdez
date: 2024-03-28
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.4.1
categories:
  - PROG
tags:
  - Software
  - File

---
## 7.4.1 Text File
En esta sección se proporciona una guía detallada sobre cómo trabajar con ficheros de texto en Kotlin, incluyendo cómo escribir y leer ficheros, manejar caracteres especiales y consideraciones importantes al trabajar con ficheros de texto. Se incluyen ejemplos prácticos y recomendaciones para facilitar el manejo eficiente y seguro de ficheros en Kotlin.

### 1. Introducción a Ficheros de Texto en Kotlin

El trabajo con ficheros de texto es una capacidad esencial en la programación que permite a las aplicaciones leer y escribir datos persistentes. Kotlin, gracias a su interoperabilidad con Java y sus propias abstracciones de alto nivel, facilita considerablemente estas tareas, proporcionando un conjunto de herramientas eficaces y sencillas de usar que mejoran tanto la productividad del desarrollador como la seguridad del código.

#### 1.1. ¿Por Qué Ficheros de Texto?

Los ficheros de texto se utilizan ampliamente para almacenar y transferir datos debido a su simplicidad, interoperabilidad entre diferentes sistemas y facilidad de edición y visualización. Desde la configuración de aplicaciones hasta el almacenamiento de grandes volúmenes de datos, los ficheros de texto ofrecen una forma flexible y accesible de manejar información.

#### 1.2. Ventajas de Kotlin

Kotlin se destaca en el manejo de ficheros de texto por varias razones:

- **Sintaxis Concisa**: Kotlin reduce la verbosidad típica de Java, permitiendo realizar operaciones complejas con ficheros en menos líneas de código y de manera más legible.
- **Seguridad de Tipos**: Kotlin maneja la nulidad a nivel del sistema de tipos, lo que reduce el riesgo de errores comunes como `NullPointerException`.
- **Interoperabilidad con Java**: Kotlin puede utilizar todas las bibliotecas de Java para manejar ficheros, incluyendo `java.io.File`, proporcionando una gran cantidad de funcionalidades mientras se añaden mejoras específicas de Kotlin.

#### 1.3. Operaciones Básicas con Ficheros

En Kotlin, las operaciones más comunes con ficheros de texto incluyen:

- **Lectura de ficheros**: Puede realizarse de manera simple con funciones como `readText()` para leer el contenido completo del fichero en una cadena de texto, o `readLines()` para obtener una lista de todas las líneas del fichero.
- **Escritura en ficheros**: Con `writeText()`, se puede escribir una cadena de texto en un fichero, sobrescribiendo su contenido anterior, o `appendText()` para añadir texto al final del fichero existente.
- **Manejo de ficheros y directorios**: Kotlin permite crear, borrar, y verificar la existencia de ficheros y directorios con métodos como `createNewFile()`, `delete()`, y `exists()`.

#### 1.4. Ejemplo Introductorio

```kotlin
import java.io.File

fun main() {
    // Crear o abrir un fichero
    val miFichero = File("miArchivo.txt")

    // Escribir en el fichero
    miFichero.writeText("Hola, Kotlin.\n")

    // Leer del fichero
    val contenido = miFichero.readText()
    println(contenido)
}
```

Este ejemplo demuestra cómo crear un fichero, escribir un simple mensaje y luego leer el mensaje del fichero, todo ello con pocas líneas de código gracias a las funciones de Kotlin diseñadas para trabajar de forma eficiente con ficheros de texto.

### 2. Escribir en un Fichero de Texto en Kotlin

Escribir en ficheros de texto es una operación fundamental en la mayoría de las aplicaciones, desde el registro de eventos (logging) hasta la generación de reportes. Kotlin ofrece métodos directos y seguros para escribir en ficheros, facilitando esta tarea con su sintaxis concisa y expresiva.

#### 2.1. Abrir o Crear un Fichero para Escritura

Antes de escribir en un fichero, primero debemos tener una referencia a este fichero. En Kotlin, esto se hace instanciando un objeto de la clase `File` del paquete `java.io`, que es totalmente accesible gracias a la interoperabilidad de Kotlin con Java.

```kotlin
import java.io.File

val miFichero = File("miArchivo.txt")
```

Si el fichero especificado no existe, se creará uno nuevo al realizar la escritura. Si ya existe, su contenido puede ser sobrescrito o complementado, dependiendo del método que se utilice.

#### 2.2. Escribir Texto en el Fichero

Kotlin simplifica la escritura en ficheros con el método `writeText()`, que toma una cadena de caracteres como argumento y la escribe en el fichero, sobrescribiendo cualquier contenido previo.

```kotlin
miFichero.writeText("Este es un nuevo contenido.\n")
```

Para añadir texto a un fichero existente sin sobrescribir su contenido, se puede usar `appendText()`:

```kotlin
miFichero.appendText("Este texto se añade al final.\n")
```

#### 2.3. Cerrar el Fichero

Una de las ventajas de trabajar con ficheros en Kotlin es que no es necesario cerrarlos explícitamente cuando se usan `writeText()` o `appendText()`. Estas funciones se encargan del manejo de recursos automáticamente, asegurando que el fichero se cierre adecuadamente después de la operación.

#### 2.4. Ejemplo Práctico: Registro de Eventos

A continuación, se muestra un ejemplo práctico de cómo podrías usar la escritura en ficheros para implementar un simple sistema de registro de eventos (logging).

```kotlin
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun registrarEvento(evento: String) {
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")
    val timestamp = LocalDateTime.now().format(formatter)
    File("registroDeEventos.txt").appendText("[$timestamp] $evento\n")
}

fun main() {
    registrarEvento("Inicio de la aplicación")
    // Simular otras operaciones...
    registrarEvento("Operación realizada correctamente")
}
```

Este código añade entradas de registro a un fichero, incluyendo una marca de tiempo para cada evento, demostrando cómo `appendText()` puede ser especialmente útil para mantener un historial de eventos sin sobrescribir los registros anteriores.


### 3. Leer de un Fichero de Texto en Kotlin

La lectura de ficheros de texto en Kotlin es una operación que se beneficia de la simplicidad y potencia del lenguaje, permitiendo procesar contenidos de archivos de manera eficiente y segura.

#### 3.1. Abrir el Fichero para Lectura

Al igual que para la escritura, la lectura de un fichero comienza por obtener una referencia al archivo deseado mediante la clase `File`. No es necesario abrir explícitamente el fichero en un modo de lectura; el acceso se determina por la función que se utilice para leer el contenido.

```kotlin
import java.io.File

val miFichero = File("miArchivo.txt")
```

#### 3.2. Leer el Contenido Completo del Fichero

Kotlin proporciona el método `readText()` para leer el contenido completo de un fichero de texto en una sola operación, devolviendo todo el texto como una cadena (`String`).

```kotlin
val contenido = miFichero.readText()
println(contenido)
```

Este método es conveniente cuando se necesita trabajar con el texto completo del fichero, pero puede ser ineficiente con archivos muy grandes debido a las limitaciones de memoria.

#### 3.3. Leer el Fichero Línea por Línea

Para ficheros grandes o cuando se necesita procesar el archivo línea por línea, Kotlin ofrece `readLines()`, que devuelve una lista de todas las líneas del fichero como cadenas (`List<String>`).

```kotlin
val lineas = miFichero.readLines()
for (linea in lineas) {
    println(linea)
}
```

Leer el fichero de esta manera puede ser más eficiente para procesar archivos grandes, ya que permite iterar sobre las líneas del fichero sin cargar todo el contenido en memoria a la vez.

#### 3.4. Uso de `useLines` para una Gestión de Recursos Eficiente

Kotlin también proporciona una manera eficiente y segura de manejar la lectura de archivos grandes a través del método `useLines`, que abre un flujo de todas las líneas del archivo, permitiendo procesar cada una de ellas de manera secuencial. Este método asegura que el fichero se cierre correctamente una vez que se completa el procesamiento, incluso si ocurre una excepción.

```kotlin
miFichero.useLines { lineas ->
    lineas.forEach { linea ->
        println(linea)
    }
}
```

#### 3.5. Ejemplo Práctico: Contar Líneas de un Fichero

Un caso de uso común es contar el número de líneas de un fichero, lo cual se puede hacer eficientemente de la siguiente manera:

```kotlin
val numeroDeLineas = miFichero.useLines { it.count() }
println("El fichero tiene $numeroDeLineas líneas.")
```

Este ejemplo demuestra cómo se puede usar `useLines` para realizar operaciones más complejas sobre el contenido del fichero de manera eficiente y segura.


### 4. Caracteres Especiales en Ficheros de Texto

Al trabajar con ficheros de texto, es crucial entender el papel que juegan ciertos caracteres especiales. Estos caracteres pueden afectar el formato del texto y son esenciales para el procesamiento correcto de los datos.

#### 4.1. EOF (End of File / Fin de Archivo)

- **Nombre en inglés**: End of File (EOF)
- **Nombre en español**: Fin de Archivo
- **Descripción**: EOF no es un carácter visible dentro del texto del fichero pero es una condición importante que indica el final del contenido de un fichero.
- **Ejemplo**:
    ```kotlin
    val reader = File("miArchivo.txt").bufferedReader()
    var linea: String?
    while (reader.readLine().also { linea = it } != null) {
        println(linea)
    }
    // Al llegar al EOF, la lectura se detiene.
    ```

#### 4.2. Salto de Línea (\n / LF - Line Feed)

- **Nombre en inglés**: Line Feed (LF)
- **Nombre en español**: Salto de Línea
- **Descripción**: Representa el final de una línea de texto y el inicio de otra. Esencial para estructurar el contenido en líneas separadas.
- **Ejemplo**:
    ```kotlin
    val texto = "Primera línea\nSegunda línea"
    println(texto) // Imprime el texto en dos líneas separadas.
    ```

#### 4.3. Retorno de Carro (\r / CR - Carriage Return)

- **Nombre en inglés**: Carriage Return (CR)
- **Nombre en español**: Retorno de Carro
- **Descripción**: En los sistemas basados en Windows, se utiliza junto con \n para crear un salto de línea (\r\n). Solo o en otros contextos, mueve el cursor al inicio de la línea actual.
- **Ejemplo**:
    ```kotlin
    val textoWindows = "Primera línea\r\nSegunda línea"
    println(textoWindows) // Funciona como salto de línea en Windows.
    ```

#### 4.4. Espacio en Blanco (' ' / Space)

- **Nombre en inglés**: Space
- **Nombre en español**: Espacio
- **Descripción**: Un carácter que crea una separación horizontal entre caracteres o palabras.
- **Ejemplo**:
    ```kotlin
    val textoConEspacios = "Kotlin es increíble"
    println(textoConEspacios) // Muestra el texto con espacios entre palabras.
    ```

#### 4.5. Tabulador (\t / Tab)

- **Nombre en inglés**: Horizontal Tab (HT)
- **Nombre en español**: Tabulador
- **Descripción**: Proporciona una separación horizontal más significativa que un espacio, comúnmente utilizado para alinear texto o datos en columnas.
- **Ejemplo**:
    ```kotlin
    val textoConTabs = "Nombre:\tJohn Doe\nEdad:\t30"
    println(textoConTabs)
    // Imprime el texto con tabulaciones, alineando las columnas.
    ```

#### 4.6. Consideraciones Adicionales

El manejo adecuado de estos caracteres especiales es fundamental para la correcta lectura, escritura y presentación de los datos de un fichero de texto. Algunas funciones de Kotlin, como `print()` y `println()`, interpretan estos caracteres automáticamente, mientras que en otras situaciones, puede ser necesario gestionarlos de manera explícita para lograr el formato deseado.


### 5. Recomendaciones Finales y Consideraciones al Trabajar con Ficheros de Texto

Manejar ficheros de texto en Kotlin, aunque es una tarea simplificada gracias a las funcionalidades del lenguaje, requiere atención a ciertos detalles para asegurar que el proceso sea eficiente, seguro y acorde a las necesidades de la aplicación.

#### 5.1. Verificar la Existencia del Fichero

Antes de intentar leer o escribir en un fichero, es una buena práctica verificar si el fichero existe para evitar errores en tiempo de ejecución.

```kotlin
val miFichero = File("miArchivo.txt")
if (!miFichero.exists()) {
    println("El fichero no existe.")
    return
}
```

#### 5.2. Manejo Eficiente de Ficheros Grandes

Para ficheros grandes, es recomendable utilizar métodos que lean o escriban de manera secuencial y no carguen todo el contenido en memoria a la vez. Kotlin ofrece varias funciones, como `useLines`, para manejar eficientemente grandes volúmenes de datos.

#### 5.3. Tratamiento de Caracteres Especiales

Ser consciente de cómo los caracteres especiales (\n, \r, \t, etc.) afectan el contenido y formato de tu fichero. Asegúrate de manejarlos adecuadamente según el contexto de tu aplicación.

#### 5.4. Seguridad y Excepciones

Al trabajar con entrada/salida de ficheros, siempre existe el riesgo de enfrentarse a excepciones. Kotlin facilita el manejo de estas a través de bloques `try-catch`.

```kotlin
try {
    val contenido = File("miArchivo.txt").readText()
    println(contenido)
} catch (e: Exception) {
    println("Ocurrió un error al leer el fichero: ${e.message}")
}
```

#### 5.5. Ejemplo Integrado: Aplicación de Registro de Eventos

A continuación, se presenta un ejemplo que combina la lectura, escritura y manejo de caracteres especiales en una aplicación simple de registro de eventos. Este ejemplo también ilustra cómo verificar la existencia de un fichero y manejar posibles excepciones.

```kotlin
import java.io.File
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun registrarEvento(fichero: File, evento: String) {
    if (!fichero.exists()) {
        println("Creando fichero de registro...")
        fichero.createNewFile()
    }
    
    try {
        val timestamp = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"))
        fichero.appendText("[$timestamp] $evento\n")
    } catch (e: Exception) {
        println("Error al registrar evento: ${e.message}")
    }
}

fun main() {
    val miFicheroDeRegistro = File("registroDeEventos.txt")
    
    registrarEvento(miFicheroDeRegistro, "Inicio de la aplicación")
    // Simula más operaciones...
    registrarEvento(miFicheroDeRegistro, "Operación realizada correctamente")
    
    println("Eventos registrados:\n${miFicheroDeRegistro.readText()}")
}
```

Este código crea un fichero de registro si no existe, registra eventos con marcas de tiempo y finalmente lee y muestra todos los eventos registrados. Demuestra un manejo efectivo y seguro de ficheros en Kotlin, considerando las prácticas recomendadas y las consideraciones necesarias para trabajar con archivos de texto.


## Fuente

* [Writing to a File in kotlin](https://www.baeldung.com/kotlin/write-file)
* [Reading from a File in kotlin](https://www.baeldung.com/kotlin/read-file)
* [Baeldung Kotlin IO](https://www.baeldung.com/kotlin/category/kotlin-io)
* [Book: The joy of kotlin](https://livebook.manning.com/book/the-joy-of-kotlin)
* [Kotlin IO](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/)
