---
title: "UD 7 - 7.4 Lectura y escritura de archivos"
description: Lectura y escritura de archivos
summary: Lectura y escritura de archivos
authors:
   - Eduardo Fdez
date: 2023-03-01
icon:   
permalink: /prog/unidad7/7.4
categories:
   - PROG
tags:
   - Software
   - File
---


## Lectura y escritura de archivos   
Normalmente las aplicaciones que utilizan archivos no están centradas en la gestión del sistema de archivos del ordenador. El objetivo principal de usar archivos es **poder almacenar datos de modo que entre diferentes ejecuciones del programa**, incluso en diferentes equipos, sea posible recuperar los datos almacenados. El caso más típico es un editor de documentos, que mientras se ejecuta se encarga de gestionar los datos relativos al texto que está escribiendo, pero en cualquier momento puede guardarlo en un archivo para poder recuperar este texto cuando se desee, y añadir otros nuevos si fuera necesario. El archivo con los datos del documento lo puede abrir tanto en el editor de su ordenador como en el de otro compañero.

Para saber cómo tratar los datos de un archivo en un programa, hay que **tener muy claro cómo se estructuran**. Dentro de un archivo se pueden almacenar todo tipo de valores de cualquier tipo de datos. La parte más importante es que estos valores **se almacenan en forma de secuencia**, uno tras otro. Por lo tanto, como pronto veréis, la forma más habitual de tratar archivos es **secuencialmente**, de forma parecida a como se hace para leer los datos desde teclado, mostrarlas por pantalla o recorrer las posiciones de un array.

> ![](./assets/book.png)
> Se denomina **acceso secuencial** al procesamiento de un conjunto de elementos de manera que sólo es posible acceder a ellos de acuerdo a su orden de aparición. Para procesar un elemento es necesario procesar primero todos los elementos anteriores.

Kotlin, junto con otros lenguajes de programación, diferencia entre dos tipos de archivos según cómo se representan los valores almacenados en un archivo.

> ![](./assets/book.png)
> En los **archivos orientados a carácter**, los datos se representan como una secuencia de cadenas de texto, donde cada valor se  diferencia del otro usando un delimitador. En cambio, en los **archivos orientados a byte**, los datos se representan directamente de acuerdo a su formato en binario, sin ninguna separación. Estos últimos archivos son no son legibles a simple vista, y son interpretados por programas que entienden su formato. Por ejemplo, pdf, doc, xls.

Nos centraremos principalmente en el procesamiento de archivos orientados a carácter.

### archivos orientados a carácter

Un archivo orientado a carácter no es más que un **documento de texto**, como el que podría generar con cualquier editor de texto simple. Los valores están almacenados según su representación en cadena de texto, exactamente en el mismo formato que ha usado hasta ahora para entrar datos desde el teclado. Del mismo modo, los diferentes valores se distinguen al estar separados entre ellos con un delimitador, que por defecto es cualquier conjunto de espacios en blanco o salto de línea. Aunque estos valores se puedan distribuir en líneas de texto diferentes, conceptualmente, se puede considerar que están organizados uno tras otro, secuencialmente, como las palabras en la página de un libro.

El siguiente podría ser el contenido de un archivo orientado a carácter donde hay diez valores de tipo `float`, 7 en la primera línea y 3 en la segunda:

```
1,5 0,75 −2,35 18,0 9,4 3,1416 −15,785
−200,4 2,56 9,3785
```

Y este el de un archivo con 3 valores de tipo `String`: `"Había"`, `"una"` y `"vez..."` en una línea.

```
Había una vez...
```

En un archivo orientado a carácter **es posible almacenar cualquier combinación de datos de cualquier tipo** (`int` , `double`, `boolean`, `String`, etc.).

```
7 10 20,51 6,99
Había una vez...
true false 2020 0,1234
```

La principal ventaja de un archivo de este tipo es que resulta muy sencillo inspeccionar su contenido y generarlos de acuerdo a nuestras necesidades.

Para el caso de los archivos orientados a carácter, hay que usar dos clases diferentes según si lo que se quiere es leer o escribir datos en un archivo. Normalmente esto no es muy problemático, ya que **en un bloque de código dado solo se llevarán a cabo operaciones de lectura o de escritura sobre un mismo archivo, pero no los dos tipos de operaciones a la vez**.

Una diferencia importante a la hora de tratar con archivos respecto a leer datos del teclado es que las operaciones de lectura no son producto de una interacción directa con el usuario, que es quien escribe los datos. Solo se puede trabajar con los datos que hay en el archivo y nada más. Esto tiene dos efectos sobre el proceso de lectura:

1. Por un lado, recuerda que **cuando se lleva a cabo el proceso de lectura de una secuencia de valores, siempre hay que tener cuidado de usar el método adecuado al tipo de valor que se espera que venga a continuación** . Qué tipo de valor se espera es algo que habréis decidido vosotros a la hora de hacer el programa que escribió ese archivo, por lo que es vuestra responsabilidad saber qué hay que leer en cada momento. De todos modos nada garantiza que no se haya cometido algún error o que el archivo haya sido manipulado por otro programa o usuario. Como operamos con archivos y no por el teclado, no existe la opción de pedir al usuario que vuelva a escribir el dato. Por lo tanto, el programa debería decir que se ha producido un error ya que el archivo no tiene el formato correcto y finalizar el proceso de lectura.
2. Por otra parte, **también es necesario controlar que nunca se lean más valores de los que hay disponibles para leer**. En el caso de la entrada de datos por el teclado el programa simplemente se bloqueaba y espera a que el usuario escribiera nuevos valores. Pero con archivos esto no sucede. Intentar leer un nuevo valor cuando el apuntador ya ha superado el último disponible se considera erróneo y lanzará una excepción. Para evitarlo, habrá que utilizar algún procedimiento que nos permita saber si se ha llegado al final de archivo en vez de suponer que siguen existiendo datos que leer.

#### Lectura de archivo

En Kotlin demos leer el contenido de un archivo utilizando los métodos estándar de la clase `java.io.File` o los métodos que proporciona Kotlin como una extensión de `java.io.File`.

Examinaremos programas de ejemplo para los métodos de extensión, proporcionados por Kotlin a la clase `java.io.File` de Java, para leer el contenido de un archivo.

##### Usar `java.io.File.bufferedReader()` de Java

[`BufferedReader`](https://dcodingames.com/como-usar-la-clase-bufferedreader/) lee texto desde un flujo de entrada de caracteres, almacenando los caracteres para proporcionar una lectura eficiente de caracteres, arreglos y líneas.

Se puede configurar específicamente el tamaño del buffer, o usar el que se otorga por default, el cual es suficientemente grande para la mayoría de los casos.

Dado que esta clase extiende de `Reader`, cada petición de lectura causa una petición de lectura del flujo de entrada, por lo que es aconsejable envolverla con la clase `InputStreamReader` o `FileReader`, según el propósito de la lectura.

A continuación podemos ver cómo leer el contenido de un archivo en `BufferedReader`, El proceso es el siguiente:

1. Prepare el objeto `File` con la ubicación del archivo pasado como argumento al constructor de la clase de `File`.
2. `File.bufferedReader` devuelve un nuevo `BufferedReader` para leer el contenido del archivo.
3. Utilice `BufferedReader.readLines()` para leer el contenido del archivo.

Un ejemplo

```kotlin

import java.io.File

fun main(args: Array<String>) {
    val file = File("input" + File.separator + "contents.txt")
    val bufferedReader = file.bufferedReader()
    val text: List<String> = bufferedReader.readLines()
    for (line in text) {
        println(line)
    }
}

```

El contenido del archivo se imprime en la consola.

##### Usar `java.io.File.forEachLine()` de Kotlin

Lee un archivo línea por línea en Kotlin. El proceso es el siguiente:

1. Prepare el objeto `File` con la ubicación pasada como argumento al constructor de la clase de `File`.
2. Use la función `File.forEachLine` y lea cada línea del archivo.

Un ejemplo

```kotlin

import java.io.File

fun main(args: Array<String>) {
    val file = File("input" + File.separator + "contents.txt")
    file.forEachLine { println(it) }
}
```

El contenido del archivo se imprime en la consola.

<!--
> ![](./../../resources/img/un7/lu37016xc6sgf_tmp_e5d45b04953e17dd.png)
>
> ...Para tratar de manera sencilla archivos orientados a carácter, Java
> proporciona las clases `Scanner` (para lectura) del `package
> java.util`, y `FileWriter` (para escritura) del `package java.io`

## 3.2. Lectura de archivo (clase Scanner)

**La clase que permite llevar a cabo la lectura de datos desde un archivo orientado a carácter es exactamente la misma
que permite leer datos desde el teclado: Scanner** . Al fin y al cabo, los valores almacenados en los archivos de este
tipo se encuentran exactamente en el mismo formato que ha usado hasta ahora para entrar información en sus programas:
una secuencia de cadenas de texto. La única diferencia es que estos valores no se piden al usuario durante la ejecución,
sino que se encuentran almacenados en un archivo.

Para procesar datos desde un archivo, **el constructor de la clase Scanner permite como argumento un objeto de tipo
File** que contenga la ruta a un archivo.

Por ejemplo, para crear un objeto de tipo Scanner de modo que permita leer datos desde el archivo ubicado en la ruta
"C:\Programas\Unidad11\Documento.txt", habría que hacer:

importjava.io.File;

importjava.util.Scanner;

...

Filef = new File("C:\Programas\Unidad11\Documento.txt");

ScannerlectorArchivo = new Scanner(f);

...

Una vez instanciado el objeto Scanner **podemos utilizar sus métodos exactamente igual que si leyéramos de teclado** :
hasNext(), next(), nextLine(), nextInt(), nextDouble(), nextBoolean(), etc. La única diferencia es que el objeto Scanner
leerá secuencialmente el contenido del archivo.

Es importante entender que en el caso de un archivo, **el objeto Scanner gestiona internamente un apuntador que indica
sobre qué valor actuarán las operaciones de lectura** . Inicialmente el apuntador se encuentra en el primer valor dentro
del archivo. **Cada vez que se hace una lectura el apuntador avanza automáticamente hasta el siguiente valor dentro del
archivo y no hay ninguna manera de hacerlo retroceder** . A medida que invocamos métodos de lectura el apuntador sigue
avanzando hasta que hayamos leído tantos datos como queramos, o hasta que no podamos seguir leyendo porque hemos llegado
al final del archivo.

A continuación se muestra un pequeño esquema de este proceso, recalcando cómo avanza el apuntador a la hora de realizar
operaciones de lectura sobre un archivo que contiene valores de tipo entero.

![](file:///tmp/lu37016xc6sfk.tmp/lu37016xc6sgf_tmp_43d276c79f83a115.png)

**Es importante recordar la diferencia entre el método next() y nextLine()** , ya que ambos evalúan una cadena de texto.
El método
**next() sólo lee una palabra individual** (conjuntos de caracteres, incluidos dígitos, que no están separados por
espacios o saltos de línea, como por ejemplo "casa", "hola", "2", "3,14", "1024", etc.). En cambio, **nextLine() lee
todo el texto que encuentre (espacios incluidos) hasta el siguiente salto de línea** . En tal caso el apuntador se
posiciona al inicio de la siguiente línea.

**Una vez se ha finalizado la lectura del archivo** , ya sean todas o solo una parte, **es imprescindible ejecutar un
método especial llamado close()** . Este método indica al sistema operativo que el archivo ya no está siendo utilizado
por el programa. Esto es muy importante ya que mientras un archivo se considera en uso, su acceso puede verse limitado.
Si no se utiliza close() el sistema operativo puede tardar un tiempo en darse cuenta de que el archivo ya no está en
uso.

| ...**Siempre hay que cerrar los archivos con close()**cuando se ha terminado de leer o escribir en
ellos.![](file:///tmp/lu37016xc6sfk.tmp/lu37016xc6sgf_tmp_4f43f86e4682ec35.png)
| |

|

Es importante saber que al instanciar el objeto Scanner **se lanzará una excepción de tipo java.io.FileNotFoundException
si el archivo no existe** . Siempre habrá que manejar dicha excepción mediante un try-catch. Scanner también **puede
lanzar otras excepciones** , por ejemplo si se intenta leer el tipo de dato incorrecto (llamamos a nextInt() cuando no
hay un entero, como sucede en la entrada por teclado,) o si hemos llegado al final del archivo e intentamos seguir
leyendo (podemos comprobarlo mediante el método hasNext() de Scanner, que devuelve true si aún hay algún elemento que
leer).

El programa siguiente muestra un ejemplo de cómo leer diez valores enteros de un archivo llamado "Enteros.txt" ubicado
en la carpeta de trabajo (debería ser la carpeta del proyecto Netbeans). Para probarlo, crea el archivo e introduce
exactamente 10 valores enteros separados por espacios en blanco o saltos de línea.

importjava.io.File;

importjava.util.Scanner;

publicclass Pruebasarchivos {

publicstatic final int NUM_VALORES = 10;

publicstatic void main(String[] args) {

try{

//Intentamos abrir el archivo

Filef = new File("Enteros.txt");

Scannerlector = new Scanner(f);

//Si llega aquí es que ha abierto el archivo :)

for(int i = 0; i < NUM_VALORES; i++) {

intvalor = lector.nextInt();

System.out.println("Elvalor leído es: " + valor); }

//¡Hay que cerrar el archivo!

lector.close(); }catch (Exception e) {

//En caso de excepción mostramos el error

System.out.println("Error:" + e);

e.printStackTrace(); } }

}
-->

##### Oros métodos de lectura

Existen otras formas de leer archivos:

- `File.inputStream().readBytes()`: Lee el contenido del archivo en InputStream
- `File.readBytes()`: devuelve todo el contenido del archivo como ByteArray
- `File.readLines()`: devuelve todo el contenido del archivo como una lista de líneas
- `File.readText()`: devuelve todo el contenido del archivo como una sola cadena
- `java.util.Scanner`: permite leer indicando el tipo de dato a leer.

#### Escritura en archivo

Con en el lenguaje de programación Kotlin tambien se puede escribir en un archivo. Por lo general, en los archivos orientados a caracteres se escriben cadenas de texto.

Igual que para la lectura, haciendo uso de Kotlin podremos escribir en un archivo usando las funciones de extensión proporcionadas por Kotlin o también puede usar el código Java existente que escribe contenido en un archivo.

A continuación veremos ejemplos de cómo usar clases de Java como `PrintWriter` para escribir en un archivo y más ejemplos usando funciones de extensión de Kotlin.

##### Usar `java.io.File.bufferedWriter`

Podemos usar la función de extensión `java.io.File.bufferedWriter()` para obtener el objeto de escritura y luego usar la función `write()` en el objeto de escritura para escribir contenido en el archivo.

1. Tenga su contenido como una cadena.
2. Pase el nombre del archivo al constructor de archivos (`File`).
3. Luego llame al método `bufferedWriter()` de la clase `File`.
4. Haciendo uso de la función `use()` (Veremos que ventajas nos proporciona hacer uso de ella), llama al método `writer(content)` del bufer escritor devuelto por `bufferedWriter()`, y que se encarga de escribir el contenido en el archivo.

```kotlin
import java.io.File
 
/**
 * Example to use File.bufferedWriter() in Kotlin to write content to a text file
 */
fun main(args: Array<String>) {
    // content to be written to file
    var content = "Hello World. Welcome to Kotlin!!"
 
    // write content to file
    File("file.txt").bufferedWriter().use { out ->
        out.write(content)
    }
}
```
> ![](./assets/rayo.png)
> Aplicamos la función `use()` para **garantizar que todos los recursos se liberen correctamente cuando hayamos terminado**

##### Usar `java.io.File.writeText()`

Si está escribiendo exclusivamente texto en un archivo, puede usar la función de extensión `java.io.File.writeText()`.

En el siguiente ejemplo, hemos usado esta función de extensión de kotlin para escribir texto en un archivo.

```kotlin
import java.io.File
 
/**
 * Example to use File.writeText in Kotlin to write text to a file
 */
fun main(args: Array<String>) {
    // content to be written to file
    var content = "Hello World. Welcome to Kotlin!!"
 
    // write content to file
    File("file.txt").writeText(content)
}
```

##### Usar `java.io.File.printWriter`

En este ejemplo, usaremos la función de extensión de Kotlin `printWriter()` para la clase `java.io.File`. El siguiente es el proceso para escribir en el archivo.

1. Tenga su contenido como una cadena.
2. Pase el nombre del archivo al constructor de archivos (`File`).
3. Luego llame al método `printWriter()` de la clase `File`.
4. Haciendo uso de la función `use()`(Veremos que ventajas nos proporciona hacer uso de ella), llama al método `println(content)` del escritor devuelto por `printWriter()`, y que se encarga de escribir el contenido en el archivo.

```kotlin
import java.io.File
 
/**
 * Example to use File.printWriter in Kotlin to write content to a text file
 */
fun main(args: Array<String>) {
    // content to be written to file
    var content = "Hello World. Welcome to Kotlin!!"
 
    // write content to file
    File("file.txt").printWriter().use { out ->
        out.println(content)
    }
}
```


##### Usar `java.io.PrintWriter`

En este ejemplo, tomamos una cadena y la escribimos en un archivo usando la clase `java.io.PrintWriter`. Para ello se siguen los siguientes pasos.

1. Tenga sus datos listos como una cadena en una variable.
2. Inicialice un objeto escritor de la clase `PrintWriter`.
3. Agregue la cadena al archivo usando la función `PrintWriter.append()`.
4. Cerrar el escritor.

```kotlin
import java.io.PrintWriter

/**
 * Example to use standard Java method in Kotlin to write content to a text file
 */
fun main(args: Array<String>) {
    // content to be written to file
    var content = "Hello World. Welcome to Kotlin!!"

    // using java class java.io.PrintWriter
    val writer = PrintWriter("file.txt")
    writer.append(content)
    writer.close()
}
```

En los ejemplso, se creará un nuevo archivo con el nombre `file.txt`, como se especifica para el argumento de `PrintWriter()`, con el contenido. Si el archivo ya está presente, primero se borra el contenido del archivo y luego se escribe el nuevo contenido en el archivo.

##### Oros métodos de escritura

Existen otras formas de leer archivos:

- `java.io.FileWriter`: Escribe en un archivo haciendo uso del método `writer()`.

<!--
Existen muchas formas de acceder a un archivo para escribir en él. Una de las formas más fáciles, es el uso de la clase  `FileWriter`.

### 4.1.2.1. Usar `FileWriter`

Esta clase tiene dos constructores que
merece la pena conocer:

* public FileWriter(File file)
* public FileWriter(File file, boolean append)

El primer constructor es muy parecido al del Scanner. Solo hay que pasarle un objeto `File` con la ruta al archivo. Al
tratarse de escritura la ruta puede indicar un archivo que puede existir o no dentro del sistema. **Si el archivo no
existe, se creará uno nuevo** . Pero
**si el archivo ya existe, su contenido se borra por completo, con tamaño igual a 0** . Esto puede ser peligroso ya que
si no se maneja correctamente puede producir la pérdida de datos valiosos. Hay que estar completamente seguro de que se
quiere sobreescribir el archivo. importjava.io.File; importjava.io.FileWriter; ... Filef = new File("C:
\Programas\Unidad11\Documento.txt"); FileWriterwriter= newFileWriter(f); El segundo constructor tiene otro **parámetro
de tipo booleano llamado “append”** **(añadir) que nos permite indicar si queremos escribir al final del archivo o no**
. Es decir, si le pasamos “false” hará lo mismo que el contructor anterior (si el archivo ya existe, lo sobreescribirá),
pero si le pasamos “true” abrirá el archivo para escritura en **modo “append”** , es decir, **escribiremos al final del
archivo sin borrar los datos ya existentes** . importjava.io.File; importjava.io.FileWriter; ... Filef = new File("C:
\Programas\Unidad11\Documento.txt"); FileWriterwriter= newFileWriter(f, true); La escritura secuencial de datos en un
archivo orientado a carácter es muy sencilla. Solo es necesario utilizar el siguiente método
**void write(String str)** que escribirá la cadena str en el archivo. Si se desea agregar un **final de línea** se puede
agregar **" \n"** . | ...**Tanto el constructor de FileWriter como el método write() pueden lanzar una excepción
IOException**si se produce algún error
inesperado.![](file:///tmp/lu37016xc6sfk.tmp/lu37016xc6sgf_tmp_4f43f86e4682ec35.png)
| |

---

|

Es importante tener en cuenta que **para que el método write() escriba texto correctamente es imprescindible pasarle
como argumento un String**
. Está permitido utilizar datos o variables distintas a String, pero se escribirá directamente su valor en bytes, no
como texto. Veamos dos ejemplos ilustrativos.

writer.write("8"); // Escribe el carácter 8

writer.write(8); // Escribe 8 como byte, es un carácter no imprimible

writer.write("65");// Escribe dos carácteres, el 6 y el 5

writer.write(65); // Escribe 65 como byte, es el carácter A

Por lo tanto cuando queremos escribir el valor de variables que no sean String será necesario pasárselas a write() como
String. Esto es muy sencillo, solo hay que concatenar un String vacío con la variable (Java siempre convierte a String
la concatenación de cadenas de texto con cualquier otro elemento): ""+ variable

intedad = 35;

writer.write(""+ edad); // escribe el texto "35"

La escritura de datos en archivo tiene la particularidad de que una vez se ha escrito un dato ya no hay marcha atrás. No
es posible escribir información antes o en medio de valores que ya están escritos.

Como en el caso de la lectura, la clase FileWriter también gestiona un apuntador que le permite saber a partir de qué
posición del texto debe ir escribiendo. Cada vez que se invoca uno de sus métodos de escritura, el apuntador avanza
automáticamente y no es posible hacerlo retroceder. A efectos prácticos este apuntador siempre está al final del
archivo, de modo que a medida que se van escribiendo datos el archivo va incrementando su tamaño.

A continuación se muestra un esquema del funcionamiento de la escritura en archivo.

![](file:///tmp/lu37016xc6sfk.tmp/lu37016xc6sgf_tmp_78a0f492846799d6.png)

La escritura no genera automáticamente un delimitador entre valores. Los espacios en blanco o saltos de línea que se
deseen incorporar deben escribirse esplícitamente. De lo contrario los valores quedarán pegados y en una posterior
lectura se interpretarán como un único valor. Por ejemplo, si se escribe el valor 2 y luego el 4, sin espacio, en el
archivo se habrá escrito el valor 24. Si se leyera mediante un nextInt()
nos devolvería un único valor, no dos.

**Al escribir en archivos el cierre con close() es todavía más importante** que en la lectura. Esto se debe a que los
sistemas operativos a menudo actualizan los datos de forma diferida. Es decir, el hecho de ejecutar una instrucción de
escritura no significa que inmediatamente se escriba en el archivo. Puede pasar un intervalo de tiempo variable. Solo al
ejecutar el método close() se fuerza al sistema operativo a escribir los datos pendientes (si los hubiera).

| ...Al terminar la escritura también**es imprescindible invocar el método close()**para cerrarlo y asegurar la correcta
escritura de datos.![](file:///tmp/lu37016xc6sfk.tmp/lu37016xc6sgf_tmp_4f43f86e4682ec35.png)
| |

|

El código siguiente sirve como ejemplo de un programa que escribe un archivo llamado "Enteros.txt" dentro de la carpeta
de trabajo. Se escriben 20 valores enteros, empezando por el 1 y cada vez el doble del anterior. Pruébalo para ver su
funcionamiento. Ten en cuenta que si ya existía un archivo con ese nombre, quedará totalmente sobrescrito. Después,
puedes intentar leerlo con el programa del ejemplo anterior para leer 10 valores enteros y mostrarlos por pantalla.

publicstatic void main(String[] args) {

try{

Filef = new File("Enteros.txt");

FileWriterfw = new FileWriter(f);

intvalor = 1;

for(int i = 1; i <= 20; i++) {

fw.write(""+ valor); // escribimos valor

fw.write(""); // escribimos espacio en blanco

valor= valor * 2; // calculamos próximo valor }

fw.write("\n");// escribimos nueva línea

fw.close();// cerramos el FileWriter

System.out.println("archivoescrito correctamente"); }catch (IOException e) {

System.out.println("Error:" + e); }

}

Prueba a ejecutar el código varias veces. Verás que el archivo se sobrescribe y siempre queda igual. Luego, modifica la
instanciación del FileWriter agregando el segundo argumento (“append”) a true:
FileWriterfw = new FileWriter(f, true); Pruébalo y verás que ya no se sobreescribe el archivo, sino que se añaden los 20
números al final. -->

### Archivos binarios.

Los Data Stream (Flujos de datos) se utilizan para escribir datos binarios. `DataOutputStream` escribe datos binarios de tipos primitivos(`Int`, `Long`, `String`) mientras que `DataInputStream` lee datos del flujo binario y los convierte en tipos primitivos.

A continuación veremos un programa de ejemplo que escribe datos en un archivo y luego los vuelve a leer a memoria para finalmente imprimirlos por salida estándar.

```kotlin
import java.io.DataInputStream
import java.io.DataOutputStream
import java.io.FileInputStream
import java.io.FileOutputStream
 
fun main(args : Array<String>){
    val burgers = "data.burgers"
 
    //Open the file in binary mode
    DataOutputStream(FileOutputStream(burgers)).use { dos ->
        with(dos){
            //Notice we have to write our data types
            writeInt("Bob is Great\n".length) //Record length of the array
            writeChars("Bob is Great\n") //Write the array
            writeBoolean(true) //Write a boolean
 
            writeInt("How many burgers can Bob cook?\n".length) //Record length of array
            writeBytes("How many burgers can Bob cook?\n") //Write the array
            writeInt(Int.MAX_VALUE) //Write an int
 
            for (i in 0..5){
                writeByte(i) //Write a byte
                writeDouble(i.toDouble()) //Write a double
                writeFloat(i.toFloat()) //Write a float
                writeInt(i) //Write an int
                writeLong(i.toLong()) //Write a long
            }
        }
    }
 
    //Open a binary file in read mode. It has to be read in the same order
    //in which it was written
    DataInputStream(FileInputStream(burgers)).use {dis ->
        with (dis){
            val bobSize = readInt() //Read back the size of the array
            for (i in 0 until bobSize){
                print(readChar()) //Print the array one character at a time
            }
            println(readBoolean()) //Read a boolean
 
            val burgerSize = readInt() //Length of the next array
            for (i in 0 until burgerSize){
                print(readByte().toChar()) //Print array one character at a time
            }
            println(readInt()) //Read an int
 
            for (i in 0..5){
                println(readByte()) //Read a byte
                println(readDouble()) //Read a double
                println(readFloat()) //Read a float
                println(readInt()) //Read an int
                println(readLong()) //Read a long
            }
        }
 
    }
}
```

El programa crea un objeto `FileOutputStream`, para ello pasa el nombre del archivo a su constructor. Luego, el objeto `FileOutputStream` se pasa como parámetro al constructor de `DataOutputStream`. 

Hacemos uso de la función `use()` para **garantizar que todos los recursos se liberen correctamente cuando hayamos terminado**. El archivo ahora está abierto para escritura en modo binario.

Cuando deseamos usar el mismo objeto repetidamente, podemos pasarlo a la función `with()`. En nuestro caso, tenemos la intención de seguir usando nuestro objeto `DataOutputStream`, por lo que en la línea 11, lo pasamos a la función `with()`. Dentro de la función `with()`, todas las llamadas a métodos apuntarán al objeto `dos` ya que se proporcionó a `with()` como parámetro.

> ![](./assets/rayo.png)
> Cuando deseamos usar un mismo objeto repetidamente, podemos pasarlo a la función `with()`. Cuando un objeto es pasado a la función `with()`, dentro de esta, **todas las llamadas a métodos apuntarán al objeto que se le ha pasado por parámetro**.

Siguiendo con el ejemplo, dado que tenemos la intención de escribir un `String` en el archivo, necesitamos registrar la longitud de la cadena, ya que de otra forma no sabriamos cuantos bytes se han escrito. Hacemos esto usando la función `writeInt` y pasándole la longitud de nuestra cadena. Luego podemos usar `writeChars()` para escribir un string, puesto que el argumento `String` se convierte en una matriz de caracteres. Finalmente, llamamos a `writeBoolean()` para escribir valores `true`/`false` en el archivo.

La siguiente sección es una repetición de la primera. Tenemos la intención de escribir otro `String` en el archivo, pero al hacerlo, necesitamos registrar la longitud en el archivo. Una vez más, recurrimos a `writeInt()` para registrar un valor `int`. En la siguiente línea, usamos `writeBytes()` en lugar de `writeChars()` para demostrar cómo podemos escribir una matriz de bytes en lugar de una cadena. La clase `DataOutputStream` se ocupa de los detalles de convertir un `String` en una matriz de bytes. Finalmente, escribimos otro valor int en la secuencia.

A continuación, se ejecuta un ciclo `for` en la línea 21. Dentro del ciclo `for`, demostramos como escribir diferentes tipos primitivos en el archivo. Podemos usar `writeByte()` para un `byte`, `writeDouble()` para un `double`, y así sucesivamente para cada tipo primitivo. **La clase `DataOutputStream` conoce el tamaño de cada tipo primitivo y escribe el número correcto de bytes para cada primitivo**.

Cuando terminamos de escribir el objeto, lo abrimos nuevamente para leerlo. La línea 33 crea un objeto `FileInputStream` que acepta la ruta al archivo en su constructor. El objeto `FileInputStream` está encadenado a `DataInputStream` pasándolo al constructor de `DataInputStream`. Aplicamos la función `use()` para garantizar que todos los recursos estén correctamente cerrados.

La lectura del archivo requiere que el archivo se lea en el mismo orden en que se escribe. Nuestra primera orden por tanto, debería ser tomar el tamaño de la matriz de caracteres que escribimos en el archivo anteriormente. Usamos `readInt()` en la línea 35 seguido de un ciclo `for` que termina en el tamaño de la matriz en la línea 36. Cada iteración del ciclo `for` llama a `readChar()` y la cadena se imprime en la consola. Cuando terminamos, leemos un booleano en la línea 39.

Nuestra siguiente matriz fue una matriz de bytes. Una vez más, necesitamos su tamaño final, por lo que llamamos a `readInt()` en la línea 41. Las líneas 42-44 recorren la matriz y llaman a `readByte()` hasta que finaliza el bucle. Cada `byte` se convierte en un objeto de carácter mediante `toChar()`. En la línea 45, leemos un `int` usando `readInt()`.

La parte final del programa repite el ciclo for encontrado anteriormente. En este caso, se hace uso de un bucle `for` que termina después de cinco iteraciones (línea 47). Dentro de este, se llama a los métodos `readByte()`, `readDouble()`, `readFloat()`, y así sucesivamente. Después de cada llamada se imprime el valor recuperado en la consola.


## Fuente

- Apuntes de programación de Joan Arnedo Moreno (Institut Obert de Catalunya, IOC)
- Apuntes de programación de Natividad Prieto, Francisco Marqués y Javier Piris (E.T.S. de Informática, Universidad Politécnica de Valencia).
- [Apuntes de programación de Jose Luis Comesaña](sitiolibre.com).
- [Create File](https://www.tutorialkart.com/kotlin/kotlin-create-file/)
- [Kotlinn data streams](https://stonesoupprogramming.com/2017/11/24/kotlin-data-streams)
- [Read File](https://www.baeldung.com/kotlin/read-file)
- [Inputstream to String](https://www.baeldung.com/kotlin/inputstream-to-string)

