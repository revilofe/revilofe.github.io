---
title: "UD 7 - 7.3 Manejo de archivos: File"
description: Manejo de archivos: File
summary: Manejo de archivos: File
authors:
- Eduardo Fdez
date: 2022-02-24
icon: material/software
permalink: /prog/unidad7/7.3
categories:
- PROG
tags:
- Software
- File
---
## La clase `File`

La pieza más básica para poder operar con archivos, independientemente de su tipo, en un programa Java es la **clase `File`** . Esta clase pertenece al *`package java.io`* de Java. Por lo tanto será necesario importarla antes de poder usarla.

```kotlin
import java.io.File
```

Esta clase permite manipular cualquier aspecto vinculado al sistema de ficheros. Su nombre ("archivo", en inglés) es un poco engañoso, ya que no se refiere exactamente a un archivo.

>![](assets/rayo.png) 2.2. 
> **La clase `File` representa una ruta dentro del sistema de archivos**

Sirve para realizar operaciones tanto sobre rutas al sistema de archivos que ya existan como no existentes. Además, se puede usar tanto para manipular archivos como directorios.

Como cualquier otra clase **hay que instanciarla para que sea posible invocar sus métodos** . El constructor de `File` recibe como argumento una cadena de texto correspondiente a la ruta sobre la que se quieren llevar a cabo las
operaciones.

```kotlin
val ruta = "data.txt"
val f = File(ruta)
```

Una ruta, path en inglés, es la forma general de un **nombre de archivo o carpeta** , por lo que identifica únicamente su localización en el sistema de archivos.

Cada uno de **los elementos de la ruta pueden existir realmente o no, pero esto no impide en modo poder inicializar File**. En realidad, su comportamiento es como una declaración de intenciones sobre qué ruta del sistema de archivos se quiere interactuar. No es hasta que se llaman los diferentes métodos definidos en File, o hasta que se escriben o se leen datos, que realmente se accede al sistema de ficheros y se procesa la información.

Un aspecto importante a tener presente al inicializar `File` es tener siempre presente que el formato de la cadena de texto que conforma la ruta puede ser diferente según el sistema operativo sobre el que se ejecuta la aplicación. Por ejemplo, el sistema operativo Windows inicia las rutas por un nombre de unidad (C :, D :, etc.), mientras que los sistemas operativos basados en Unix comienzan directamente con una barra ("/"). Además, los diferentes sistemas operativos usan diferentes separadores dentro de las rutas. Por ejemplo, los sistemas Unix usan la barra ("/") mientras que el Windows la inversa ("\\").

* Ejemplo de ruta Unix: `/usr/bin`
* Ejemplo de ruta Windows: `C:\Windows\System32`

De todos modos Java y Kotlin nos permite utilizar la barra de Unix ("/") para representar rutas en sistemas Windows. Por lo tanto, es posible utilizar siempre este tipo de barra independientemente del sistema, por simplicidad.

Es importante entender que **un objeto representa una única ruta** del sistema de ficheros. Para operar con diferentes rutas habrá que crear y manipular varios objetos. Por ejemplo, en el siguiente código se instancian tres objetos `File` diferentes.

```kotlin
var carpetaFotos: File = File("C:/Fotos")
var unaFoto: File = File("C:/Fotos/Foto1.png")
var otraFoto: File = File("C:/Fotos/Foto2.png")
```

### Rutas absolutas y relativas

En los ejemplos empleados hasta el momento para crear objetos de la clase `File` se han usado rutas absolutas, ya que es la manera de dejar más claro a qué elemento dentro del sistema de archivos, ya sea archivo o carpeta, se está haciendo referencia.

> ![](assets/book.png)
> Una **ruta absoluta** es aquella que **se refiere a un elemento a
> partir del raíz** del sistema de ficheros.
>
> Por ejemplo `C:/Fotos/Foto1.png`

Las rutas absolutas se distinguen fácilmente, ya que el texto que las representa comienza de una manera muy característica dependiendo del sistema operativo del ordenador. En el caso de los sistemas operativos Windows a su inicio siempre se pone el nombre de la unidad ( "C:", "D:", etc.), mientras que en el caso de los sistemas operativos Unix, estas comienzan siempre por una barra ("/").

Por ejemplo, las cadenas de texto siguientes representan rutas absolutas en un sistema de archivos de Windows:

* `C:\Fotos\Viajes` (ruta a una carpeta)
* `M:\Documentos\Unitat11\apartado1` (ruta a una carpeta)
* `N:\Documentos\Unitat11\apartado1\Actividades.txt` (ruta a un archivo)

En cambio, en el caso de una jerarquía de ficheros bajo un sistema operativo Unix, un conjunto de rutas podrían estar representadas de la siguiente forma:

* `/Fotos/Viajes` (ruta a una carpeta)
* `/Documentos/Unidad11/apartado1` (ruta a una carpeta)
* `/Documentos/Unidad11/Apartado1/Actividades.txt` (ruta a un archivo)

Al instanciar objetos de tipo `File` usando una ruta absoluta siempre hay que usar la representación correcta según el sistema en que se ejecuta el programa.

Si bien el **uso de rutas absolutas resulta útil para indicar con toda claridad qué elemento dentro del sistema de archivos se está manipulando, hay casos que su uso conlleva ciertas complicaciones**. Suponga que ha hecho un programa en el que se llevan a cabo operaciones sobre el sistema de archivos. Una vez funciona, le deja el proyecto Kotlin a un amigo que lo copia en su ordenador dentro de una carpeta cualquiera y la abre con su entorno de trabajo. Para que el programa le funcione perfectamente antes será necesario que en su ordenador haya exactamente las mismas carpetas que usa en su máquina, tal como están escritas en el código fuente de su programa. De lo contrario, no funcionará, ya que las carpetas y ficheros esperados no existirán, y por tanto, no se encontrarán. Usar rutas absolutas hace que un programa siempre tenga que trabajar con una estructura del sistema de archivos exactamente igual donde quiera que se ejecute, lo cual no es muy cómodo.

Para resolver este problema, a la hora de inicializar una variable de tipo `File`, también se puede hacer referencia a una ruta relativa.

> ![](./assets/book.png)
> Una **ruta relativa** es aquella que **no incluye el raíz** y por ello se considera que **parte desde el directorio de trabajo** de la aplicación. Esta carpeta puede ser diferente cada vez que se ejecuta
> el programa.

**Cuando un programa se ejecuta** por defecto **se le asigna una carpeta de trabajo**. Esta carpeta **suele ser la carpeta desde donde se lanza el programa**. En el caso de un programa en Kotlin ejecutado a través de un IDE (como IntelliJ IDEA), la carpeta de trabajo suele ser la misma carpeta donde se ha elegido guardar los archivos del proyecto.

El formato de una ruta relativa es similar a una ruta absoluta, pero nunca se indica la raíz del sistema de ficheros.
Directamente se empieza por el primer elemento escogido dentro de la ruta. Por ejemplo:

* Viajes
* Unidad11\apartado1
* Unidad11\apartado1\Actividades.txt

Una ruta relativa siempre incluye el directorio de trabajo de la aplicación como parte inicial a pesar de no haberse escrito. El rasgo distintivo es que el directorio de trabajo puede variar. Por ejemplo, el elemento al que se refiere el siguiente objeto `File` varía según el directorio de trabajo.

```kotlin
val f = File("Unidad11/apartado1/Actividades.txt")
```


| **Directorio de trabajo** | **Ruta real**                                          |
| :-------------------------- | :------------------------------------------------------- |
| `C:/Proyectos/Java`       | `C:/Proyectos/Java/Unidad11/apartado1/Actividades.txt` |
| `X:/Unidades`             | `X:/Unidades/Unidad11/apartado1/Actividades.txt`       |
| `/Programas`              | `/Programas/Unidad11/apartado1/Actividades.txt`        |

Este mecanismo permite facilitar la portabilidad del software entre distintos ordenadores y sistemas operativos, ya que solo es necesario que los archivos y carpetas permanezcan en la misma ruta relativa al directorio de trabajo. Veámoslo con un ejemplo:

```kotlin
val f = File("Activdades.txt")
```

Dada esta ruta relativa, basta garantizar que el fichero `Activdades.txt` esté siempre en el mismo directorio de trabajo de la aplicación, cualquiera que sea éste e independientemente del sistema operativo utilizado (en un ordenador puede ser `C:\Programas` y en otro `/Kotlin`). En cualquiera de todos estos casos, la ruta siempre será correcta. De hecho, aún más. Nótese como **las rutas relativas a Kotlin permiten crear código independiente del sistema operativo**, ya que no es necesario especificar un formato de raíz ligada a un sistema de archivos concreto ( "C:", "D:", "/", etc.).

### Métodos de la clase File

`File` ofrece varios métodos para poder manipular el sistema de archivos u obtener información a partir de su ruta.
Algunos de los más significativos para entender las funcionalidades se muestran a continuación, ordenados por tipo de operación.

#### Obtención de la ruta

Una vez se ha instanciado un objeto de tipo `File`, puede ser necesario recuperar la información empleada durante su inicialización y conocer en formato texto a qué ruta se está refiriendo, o al menos parte de ella.

* `fun getParent():String` devuelve la ruta de la carpeta del elemento referido por esta ruta. Básicamente la cadena de texto resultante es idéntica a la ruta original, eliminando el último elemento. Si la ruta tratada se refiere a la carpeta raíz de un sistema de archivos ("C:\",
  "/", etc.), este método devuelve `null`. En el caso de tratarse de una ruta relativa, este método no incluye la parte de la carpeta de trabajo.
* `fun getName():String` devuelve el nombre del elemento que representa la ruta, ya sea una carpeta o un archivo. Es el caso inverso del método `getParent()`, ya que el texto resultante es solo el último elemento.
* `fun getAbsolutePath():String` devuelve la ruta absoluta. Si el objeto `File` se inicializó usando una ruta relativa, el resultado incluye también la carpeta de trabajo.

Veamos un ejemplo de cómo funcionan estos tres métodos. Obsérvese que las rutas relativas se añaden a la ruta de la carpeta de trabajo (donde se encuentra el proyecto):

```Kotlin
import kotlin.jvm.JvmStatic
import java.io.File

object PruebasFicheros {
    @JvmStatic
    fun main(args: Array<String>) {
        // Dos rutas absolutas
        val carpetaAbs = File("/home/lionel/fotos")
        val archivoAbs = File("/home/lionel/fotos/albania1.jpg")

        // Dos rutas relativas
        val carpetaRel = File("trabajos")
        val fitxerRel = File("trabajos/documento.txt")

        // Mostremos sus rutas
        mostrarRutas(carpetaAbs)
        mostrarRutas(archivoAbs)
        mostrarRutas(carpetaRel)
        mostrarRutas(fitxerRel)
    }

    fun mostrarRutas(f: File) {
        println("getParent(): " + f.parent)
        println("getName(): " + f.name)
        println("getAbsolutePath(): " + f.absolutePath)
    }
}
```

Este programa produce la salida:

```
getParent()     :   /home/lionel
getName()       :   fotos
getAbsolutePath():  /home/lionel/fotos

getParent()     :   /home/lionel/fotos
getName()       :   albania1.jpg
getAbsolutePath():  /home/lionel/fotos/albania1.jpg

getParent()     :   null
getName()       :   trabajos
getAbsolutePath():  /home/lionel/NetBeans/Ficheros/trabajos

getParent()     :   trabajos
getName()       :   documento.txt
getAbsolutePath():  /home/lionel/NetBeans/Ficheros/trabajos/documento.txt
```

#### Comprobaciones de estado

Dada la ruta empleada para inicializar una variable de tipo File, esta puede que realmente exista dentro del sistema de ficheros o no, ya sea en forma de archivo o carpeta. La clase `File` ofrece un conjunto de métodos que permiten hacer comprobaciones sobre su estado y saber si es así.

* `fun exists(): Boolean` comprueba si la ruta existe dentro del sistema de ficheros. Devolverá `true` si existe   y `false` en caso contrario. Normalmente los archivos incorporan en su nombre una extensión (.txt, .jpg, .mp4, etc.).
  Aún así, hay que tener en cuenta que la extensión no es un elemento obligatorio en el nombre de un archivo, sólo se usa como mecanismo para que tanto el usuario como algunos programas puedan discriminar más fácilmente el tipo de archivos. Por lo tanto, solo con el texto de una ruta no se puede estar 100% seguro de si esta se refiere a un archivo   o una carpeta. Para poder estar realmente seguros se pueden usar los métodos siguientes:
* `fun isFile(): Boolean` comprueba el sistema de ficheros en busca de la ruta y devuelve true si existe y es un fichero. Devolverá `false` si no existe, o si existe pero no es un fichero.
* `fun isDirectory():Boolean` funciona como el anterior pero comprueba si es una carpeta.

Por ejemplo, el siguiente código hace una serie de comprobaciones sobre un conjunto de rutas. Para poder probarlo puedes crear la carpeta `Temp` en la raíz `C:` (si estas en Windows). Dentro, un archivo llamado `Document.txt` (puede estar vacío) y una carpeta llamada `Fotos`. Después de probar el programa puedes eliminar algún elemento y volver a probar para ver la diferencia.

```Kotlin
import kotlin.jvm.JvmStatic
import un7.PruebaExiste
import java.io.File

object PruebaExiste {
    @JvmStatic
    fun main(args: Array<String>) {
        val temp = File("C:/Temp")
        val fotos = File("C:/Temp/Fotos")
        val document = File("C:/Temp/Documento.txt")
        println(temp.absolutePath + " ¿existe? " + temp.exists())
        mostrarEstado(fotos)
        mostrarEstado(document)
    }

    fun mostrarEstado(f: File) {
        println(f.absolutePath + " ¿archivo? " + f.isFile)
        println(f.absolutePath + " ¿carpeta? " + f.isDirectory)
    }
}
```

#### Propiedades de ficheros

El sistema de ficheros de un sistema operativo almacena diversidad de información sobre los archivos y carpetas que puede resultar útil conocer: sus atributos de acceso, su tamaño, la fecha de modificación, etc. En general, todos los datos mostrados en acceder a las propiedades del archivo. Esta información también puede ser consultada usando los métodos adecuados. Entre los más populares hay los siguientes:

* `fun length(): Long` devuelve el tamaño de un archivo en bytes. Este método solo puede ser llamado sobre una ruta que represente un archivo, de lo contrario no se puede garantizar que el resultado sea válido.
* `fun lastModified(): Long` devuelve la última fecha de edición del elemento representado por esta ruta. El resultado se codifica en un único número entero cuyo valor es el número de milisegundos que han pasado desde el 1 de junio de 1970.

El ejemplo siguiente muestra cómo funcionan estos métodos. Para probarlos crea el archivo `Documento.txt` en la carpeta `C:\Temp`. Primero deja el archivo vacío y ejecuta el programa. Luego, con un editor de texto, escribe cualquier cosa, guarda los cambios y vuelve a ejecutar el programa. Observa cómo el resultado es diferente. Como curiosidad, fíjate en el uso de la clase `Date` para poder mostrar la fecha en un formato legible.

```Kotlin
import java.io.File
import java.util.*
import kotlin.jvm.JvmStatic

object PruebaPropiedades {
    @JvmStatic
    fun main(args: Array<String>) {
        val documento = File("C:/Temp/Documento.txt")
        println(documento.absolutePath)
        val milisegundos = documento.lastModified()
        val fecha = Date(milisegundos)
        println("Últimamodificación (ms)   : $milisegundos")
        println("Últimamodificación (fecha): $fecha")
        println("Tamañodel archivo: " + documento.length())
    }
}
```

**Primera salida:**

```
C:/Temp/Documento.txt
Últimamodificación (ms)   : 1583025735411
Últimamodificación (fecha): Sun Mar 01 02:22:15 CET 2020
Tamañodel archivo: 0
```

**Segunda salida:**

```
C:/Temp/Documento.txt
Últimamodificación (ms)   : 1583025944088
Últimamodificación (fecha): Sun Mar 01 02:25:44 CET 2020
Tamañodel archivo: 7
```

#### Gestión de los archivos

El conjunto de operaciones más habituales al acceder a un sistema de ficheros de un ordenador son las vinculadas a su gestión directa: renombrar archivos, borrarlos, copiarlos o moverlos. Dado el nombre de una ruta, Java y kotlin también permite realizar estas acciones.

* `fun mkdir(): Boolean` permite crear la carpeta indicada en la ruta. La ruta debe indicar el nombre de una carpeta que no existe en el momento de invocar el método. Por ejemplo, dado un objeto `File`  instanciado con la ruta `C: /Fotos/Albania` que no existe, el método `mkdir()` creará la carpeta `Albania` dentro de `C:/Fotos`. Devuelve `true` si se ha creado correctamente, en caso contrario devuelve `false` (por ejemplo si la ruta es incorrecta, la carpeta ya existe o el usuario no tiene permisos de escritura).
* `fun delete(): Boolean` borra el archivo o carpeta indicada en la ruta. La ruta debe indicar el nombre de un archivo o carpeta que sí existe en el momento de invocar el método. Se podrá borrar una carpeta solo si está vacía (no contiene ni carpetas ni archivos). Devuelve `true` o `false` según si la operación se ha podido llevar a cabo.

Para probar el ejemplo que se muestra a continuación de manera que se pueda ver cómo funcionan estos métodos, primero asegúrate de que en la raíz de la unidad `C:` no hay ninguna carpeta llamada `Temp` y ejecute el programa. Todo fallará, ya que las rutas son incorrectas (no existe `Temp`). Luego, crea la carpeta `Temp` y en su interior crea un nuevo documento llamado `Documento.txt` (puede estar vacío). Ejecuta el programa y verás que se habrá creado una nueva carpeta llamada `Fotos`. Si lo vuelves a ejecutar por tercera vez podrás comprobar que se habrá borrado.

```Kotlin
import java.io.File
import kotlin.jvm.JvmStatic

object PruebasGestionFicheros {
    @JvmStatic
    fun main(args: Array<String>) {
        val fotos = File("C:/Temp/Fotos")
        val doc = File("C:/Temp/Documento.txt")
        val mkdirFot: Boolean = fotos.mkdir()
        if (mkdirFot) {
            println("Creada carpeta " + fotos.getName().toString() + "? " + mkdirFot)
        } else {
            val delCa: Boolean = fotos.delete()
            println("Borrada carpeta " + fotos.getName().toString() + "? " + delCa)
            val delAr: Boolean = doc.delete()
            println("Borrado archivo " + doc.getName().toString() + "? " + delAr)
        }
    }
}
```

Desde el punto de vista de un sistema operativo la operación de `mover` un archivo o carpeta no es más que cambiar su nombre desde su ruta original hasta una nueva ruta destino. Para hacer esto también hay un método.

* `fun renameTo(File destino): Boolean` el nombre de este método es algo engañoso ("renombrar", en inglés), ya que su función real no es simplemente cambiar el nombre de un archivo o carpeta, sino cambiar la ubicación completa. El método se invoca el objeto `File` con la ruta origen (donde se encuentra el archivo o carpeta), y se le da como argumento otro objeto `File` con la ruta destino. Devuelve `true` o `false` según si la operación se ha podido llevar a cabo correctamente o no (la ruta origen y destino son correctos, no existe ya un archivo con este nombre en el destino, etc.). Nótese que, en el caso de carpetas, es posible moverlas aunque contengan archivos.

Una vez más, veamos un ejemplo. Dentro de la carpeta `C:/Temp` crea una carpeta llamada `Media` y otra llamada `Fotos`.

Dentro de la carpeta`Fotos` crea dos documentos llamados `Documento.txt` y `Fotos.txt`. Después de ejecutar el programa, observa como la carpeta `Fotos` se ha movido y ha cambiado de nombre, pero mantiene en su interior el archivo `Fotos.txt`. El archivo `Documento.txt` se ha movido hasta la carpeta `Temp`.

```Kotlin
import java.io.File
import kotlin.jvm.JvmStatic

object PruebasGestionFicheros2 {
    @JvmStatic
    fun main(args: Array<String>) {
        val origenDir = File("C:/Temp/Fotos")
        val destinoDir = File("C:/Temp/Media/Fotografies")
        val origenDoc = File("C:/Temp/Media/Fotografies/Document.txt")
        val destinoDoc = File("C:/Temp/Document.txt")
        var res = origenDir.renameTo(destinoDir)
        println("Se ha movido y renombrado la carpeta? $res")
        res = origenDoc.renameTo(destinoDoc)
        println("Se ha movido el documento? $res")
    }
}

```

Como ya se ha comentado este método también sirve, implícitamente, para renombrar archivos o carpetas. Si el elemento final de las rutas origen y destino son diferentes, el nombre del elemento, sea archivo o carpeta, cambiará. Para simplemente renombrar un elemento sin moverlo de lugar, simplemente su ruta padre sea exactamente la misma. El resultado es que el elemento de la ruta origen "se mueve" en la misma carpeta donde está ahora, pero con un nombre diferente.

Por ejemplo, si utilizamos `C:/Trabajos/Doc.txt` como ruta origen y `C:/Trabajos/File.txt` como ruta destino, el archivo `Doc.txt` cambiará de nombre a `File.txt` pero permanecerá en la misma carpeta
`C:/Trabajos`.

#### Listado de archivos

Finalmente, sólo en el caso de las carpetas, es posible consultar cuál es el listado de archivos y carpetas que contiene.

* `fun listFiles(): Array<File>` devuelve un vector de objectos `File` con todos los elementos contenidos en la carpeta (representados por objetos `File`, uno por elemento). Para que se ejecute correctamente la ruta debe indicar una carpeta. El tamaño del vector será igual al número de elementos que contiene la carpeta. Si el tamaño es `0`, el valor devuelto será `null` y toda operación posterior sobre el vector será errónea. El orden de los elementos es aleatorio (al contrario que en el explorador de archivos del sistema operativo, no se ordena automáticamente por tipo ni alfabéticamente).

Veamos un ejemplo. Antes de ejecutarlo, crea una carpeta `Temp` en la raíz de la unidad `C:`. Dentro crea o copia cualquier cantidad de carpetas o archivos.

```Kotlin
import java.io.File
import kotlin.jvm.JvmStatic

object PruebasGestionFicheros3 {
    @JvmStatic
    fun main(args: Array<String>) {
        val dir = File("C:/Temp")
        val lista = dir.listFiles()
        println("Contenido de " + dir.absolutePath + " :")

        // Recorremos el array y mostramos el nombre de cada elemento
        for (i in lista.indices) {
            val f = lista[i]
            if (f.isDirectory) {
                println("[DIR] " + f.name)
            } else {
                println("[ARX] " + f.name)
            }
        }
    }
}
```

#### Creación de archivos

En Kotlin, se puede crear un nuevo archivo usando `File.createNewFile()`, `File.writeText(text :String)`, `Files.writeBytes()`, etc. Hay muchas otras formas de crear un archivo en Kotlin. Examinaremos la implementación del código para algunos de ellos utilizando programas Kotlin de ejemplo.

##### Crear archivo usando `File.createNewFile()`

`File.createNewFile()` crea un nuevo archivo si aún no existe y devuelve el valor booleano de `true`. Si el archivo ya existe en la ruta proporcionada, el método devuelve `false`. El archivo creado está vacío y tiene cero bytes escritos.

Usar `File.createNewFile()` es el mejor procedimiento y el más seguro para crear un nuevo archivo. La mayoría de los otros métodos, **sobrescribirían el archivo si existe**, lo que puede resultar en la pérdida de los datos existentes en el archivo, y puede ser que no se desee este efecto.

En el siguiente ejemplo, intentamos crear un nuevo archivo con el nombre `data.txt`. La primera vez se crea el archivo y se devuelve `true`. Cuando intentamos crear el archivo por segunda vez, como el archivo `data.txt` ya se creó, obtenemos `false`.

```Kotlin
import java.io.File

fun main(args: Array<String>) {

    val fileName = "data.txt"
    var file = File(fileName)

    // create a new file
    val isNewFileCreated: Boolean = file.createNewFile()

    if (isNewFileCreated) {
        println("$fileName is created successfully.")
    } else {
        println("$fileName already exists.")
    }

    // try creating a file that already exists
    val isFileCreated: Boolean = file.createNewFile()

    if (isFileCreated) {
        println("$fileName is created successfully.")
    } else {
        println("$fileName already exists.")
    }

}
```

mostrará como salida:

```
data.txt is created successfully.
data.txt already exists.
```

##### Crear archivo usando `File.writeText()`

`File.writeText()` crea un nuevo archivo si aún no existe y escribe el texto (argumento de cadena) en el archivo. Si se proporciona una cadena vacía, se crea el archivo y no se escribe nada en él. De forma predeterminada, el archivo está codificado como UTF-8. Pasar cualquier otro conjunto de caracteres como segundo argumento codifica el archivo en consecuencia.

> ![](./assets/rayo.png)
> En caso de que el archivo ya exista, se sobrescribe y los datos existentes se pierden

Utilice este método si está seguro de que el archivo aún no existe o si sobrescribir los datos existentes no afecta a su aplicación.

En este ejemplo, usaremos `File.writeText()` para crear un nuevo archivo.

```Kotlin
import java.io.File

fun main(args: Array<String>) {

    val fileName = "data.txt"

    var file = File(fileName)

    // create a new file
    file.writeText("")

}
```

Al método `writeText()` se le puede proporcionar como argumento la cadena que le gustaría escribir en este archivo. Le hemos pasado una cadena vacía, como dato a escribir en el archivo.

##### Crear archivo usando `File.writeBytes()`

`File.writeBytes()` crea un nuevo archivo si aún no existe y escribe los bytes del `ByteArray` proporcionado sin ningún formato. Si se proporciona un `ByteArray` vacío, se crea el archivo y no se escribe nada en él.

> ![](./assets/rayo.png)
> En caso de que el archivo ya exista, se sobrescribe y los datos existentes se pierden

Utilice este método si está seguro de que el archivo aún no existe o si sobrescribir los datos existentes no afecta a su aplicación.

En este ejemplo, usaremos `File.writeBytes()` para crear un nuevo archivo.

```Kotlin
import java.io.File

fun main(args: Array<String>) {

    val fileName = "data.txt"

    var file = File(fileName)

    // create a new file
    file.writeBytes(ByteArray(0))
}
```

Al método `writeBytes()` se le puede proporcionar como argumento el vector de Bytes que le gustaría escribir en este archivo. Le hemos pasado un vector vacío, como dato a escribir en el archivo.

## Fuente

* [Writing to a File in kotlin](https://www.baeldung.com/kotlin/write-file)
* [Reading from a File in kotlin](https://www.baeldung.com/kotlin/read-file)
* [Baeldung Kotlin IO](https://www.baeldung.com/kotlin/category/kotlin-io)
* [Book: The joy of kotlin](https://livebook.manning.com/book/the-joy-of-kotlin)
* [Kotlin IO](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.io/)