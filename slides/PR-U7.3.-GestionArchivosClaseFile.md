# U7.3 - Gestión de Archivos con la clase File

---

## Introducción a la clase ´File´


### ¿Qué es la clase File?

* La clase `File` permite manipular rutas del sistema de archivos en Java y Kotlin.
* No solo sirve para archivos: también para carpetas o rutas que no existen aún.
* Es necesario importar `java.io.File` para usarla.
* Hay que instanciar un objeto `File` con la ruta deseada.
* La ruta puede ser a un archivo o a una carpeta, existente o no.
* El objeto representa una única ruta; para varias rutas, varios objetos.

Note: Presenta la clase File, aclarando que gestiona rutas (archivos o carpetas) y que se debe importar y crear instancias para operar sobre ellas.


### Ejemplo de uso básico

```kotlin
import java.io.File

val ruta = "data.txt"
val f = File(ruta) // Instancia un objeto File para la ruta especificada
```

* Se puede usar tanto para archivos como para carpetas.
* El objeto File aún no accede al sistema de archivos hasta usar sus métodos.

Note: Explica cómo instanciar un objeto File y que no accede realmente al sistema de archivos hasta llamar a sus métodos.

---

## Rutas Absolutas y Relativas


### Rutas absolutas

* Una ruta absoluta parte del directorio raíz del sistema de archivos.
* En Windows: comienzan con la unidad (ej. `C:\Fotos\Viajes`).
* En Unix/Linux: comienzan con `/` (ej. `/Fotos/Viajes`).
* Son útiles para identificar exactamente un archivo o carpeta.
* Requieren que la estructura de carpetas exista igual en todos los equipos.

Note: Define rutas absolutas y sus diferencias según el sistema operativo, remarcando su utilidad y limitaciones para la portabilidad.


### Rutas relativas

* No incluyen el directorio raíz, parten del directorio de trabajo de la aplicación.
* El directorio de trabajo suele ser donde se lanza el programa.
* Facilitan la portabilidad del software entre distintos sistemas.
* Ejemplo: `Unidad11/apartado1/Actividades.txt` es relativo.
* El mismo código puede funcionar en diferentes equipos si se mantiene la estructura relativa.

Note: Explica rutas relativas, su relación con el directorio de trabajo y su ventaja en portabilidad.

---

## Métodos principales de la clase File


### Métodos para obtener información de la ruta

* `getParent()`: devuelve la ruta del directorio padre.
* `getName()`: devuelve el nombre del archivo o carpeta.
* `getAbsolutePath()`: devuelve la ruta absoluta completa.
* Permiten conocer y mostrar información sobre la ruta gestionada.

Note: Describe los métodos para obtener partes de la ruta y su utilidad para mostrar información contextual.


### Comprobaciones de estado

* `exists()`: indica si la ruta existe en el sistema de archivos.
* `isFile()`: indica si la ruta existe y es un archivo.
* `isDirectory()`: indica si la ruta existe y es una carpeta.
* Útiles para validar la existencia y tipo antes de operar.

Note: Explica cómo comprobar si la ruta existe y su tipo, fundamental para evitar errores al manipular archivos o carpetas.


### Propiedades de archivos

* `length()`: devuelve el tamaño del archivo en bytes.
* `lastModified()`: devuelve la fecha de última modificación en milisegundos desde 1970.
* Permiten consultar atributos importantes de archivos.

Note: Presenta métodos para consultar tamaño y fecha de modificación, útiles para gestión y auditoría de archivos.

---

## Gestión de Archivos y Carpetas


### Operaciones básicas

* `mkdir()`: crea una carpeta en la ruta especificada.
* `delete()`: borra el archivo o carpeta (solo si la carpeta está vacía).
* `renameTo(destino)`: mueve o renombra un archivo o carpeta.
* Devuelven `true` si la operación fue exitosa, `false` en caso contrario.

Note: Enumera los métodos principales para crear, borrar y mover archivos o carpetas, y sus condiciones de uso.


### Listado de archivos en una carpeta

* `listFiles()`: devuelve un array de objetos File con el contenido de la carpeta.
* Solo funciona si la ruta es una carpeta existente.
* El orden de los elementos es aleatorio.

Note: Explica cómo obtener el listado de archivos y carpetas dentro de un directorio, útil para recorrer estructuras de archivos.

---

## Creación de Archivos en Kotlin


### Crear archivos de distintas formas

* `createNewFile()`: crea un archivo vacío si no existe, devuelve `true` si lo crea.
* `writeText(text)`: crea o sobrescribe el archivo y escribe texto.
* `writeBytes(bytes)`: crea o sobrescribe el archivo y escribe un array de bytes.
* Si el archivo ya existe, `writeText` y `writeBytes` lo sobrescriben.

Note: Presenta los métodos más comunes para crear archivos en Kotlin, destacando el comportamiento ante archivos existentes.


### Usando `createNewFile()`

- Crea archivo vacío si no existe, devuelve `true`.
- Si existe, devuelve `false`, sin sobrescribir.
- Método seguro para evitar pérdida de datos.

Note: Explica que `createNewFile()` es ideal para crear archivos nuevos sin riesgo de sobrescribir datos existentes. Si el archivo ya está creado, simplemente informa de ello sin modificarlo, lo que lo hace un método seguro.


### Ejemplo: Crear archivo con createNewFile

```kotlin
import java.io.File

val file = File("data.txt")
val creado = file.createNewFile()
if (creado) {
    println("Archivo creado.")
} else {
    println("El archivo ya existe.")
}
```

* Crea el archivo solo si no existe, evitando sobrescribir datos.

Note: Ejemplo práctico de uso de createNewFile, mostrando cómo evitar sobrescribir archivos existentes.


### Usando `writeText()`

- Crea archivo y escribe texto (UTF-8 por defecto).
- Sobrescribe si existe, perdiendo datos previos.
- Útil solo si sobrescribir no es un problema.

Note: Describe que `writeText()` no solo crea archivos, sino que permite escribir contenido directamente. Sin embargo, advierte que sobrescribe archivos existentes, lo que puede ser riesgoso si hay datos importantes.


### Ejemplo: Crear archivo con writeText

```kotlin
import java.io.File

val file = File("data.txt")
file.writeText("Contenido de ejemplo") // Sobrescribe si ya existe
```

* Escribe texto en el archivo, sobrescribiendo el contenido anterior.

Note: Ejemplo de uso de writeText para crear o sobrescribir archivos con contenido textual.


### Usando `writeBytes()`

- Crea archivo y escribe array de bytes.
- Sobrescribe si existe, perdiendo datos previos.
- Similar a `writeText()`, pero con datos binarios.

Note: Detalla que `writeBytes()` es análogo a `writeText()`, pero trabaja con datos binarios en lugar de texto. Al igual que el anterior, sobrescribe archivos existentes, por lo que debe usarse con precaución.


### Ejemplo: Crear archivo con writeBytes

```kotlin
import java.io.File

val file = File("data.txt")
file.writeBytes(ByteArray(0)) // Escribe un array de bytes vacío
```

* Permite escribir datos binarios en el archivo.

Note: Ejemplo de uso de writeBytes, útil para archivos binarios o cuando se requiere control sobre los datos escritos.

---

## Resumen
Estas slides cubren los conceptos clave sobre la clase File en Java/Kotlin:

- Qué es y cómo se instancia.
- Diferencias entre rutas absolutas y relativas y su impacto en la portabilidad.
- Métodos principales para obtener información, comprobar estado y gestionar archivos/carpetas.
- Ejemplos prácticos de creación de archivos usando distintos métodos en Kotlin.

