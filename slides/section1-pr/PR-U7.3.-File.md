# PR-U7.3 - Manejo de archivos con File

Note: En esta presentación introducimos la clase **`File`** como la pieza que nos permite trabajar con **rutas** dentro del sistema de archivos. Quiero que el alumnado salga con una idea muy clara desde el principio: un objeto **`File`** no contiene el fichero en memoria, sino que representa una **ubicación** sobre la que luego podremos consultar información y hacer operaciones básicas.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Este bloque hace de puente entre la teoría del **sistema de archivos** y el trabajo práctico con lectura y escritura real. Primero vamos a aprender a pensar en términos de **rutas**, **directorios** y **metadatos**, porque sin esa base es muy fácil escribir código que "parece correcto" pero apunta al sitio equivocado.

---

## Índice

Note: En esta presentación trabajamos la clase **`File`** con un objetivo muy concreto: aprender a representar **rutas**, comprobar su estado y operar de forma básica con **ficheros** y **directorios** antes de meternos con el contenido. Es importante que el alumnado entienda que aquí estamos preparando el terreno para la **E/S**, no leyendo datos todavía.


### Índice I

- 1. Qué representa realmente `File`
- 2. Crear objetos `File`
- 2.1. Rutas absolutas y relativas
- 2.2. Directorio de trabajo
- 3. Consultar información de una ruta

Note: La primera mitad del tema se apoya en una idea conceptual que conviene repetir varias veces: un objeto **`File`** representa una **ruta**, no el contenido del archivo ni el archivo "abierto". Si esta diferencia queda clara, luego resulta mucho más fácil entender por qué unas operaciones consultan y otras realmente leen o escriben.


### Índice II

- 3.2. `exists()`, `isFile` e `isDirectory`
- 3.4. Tamaño y fecha de modificación
- 4. Operaciones básicas con directorios y rutas
- 5. `listFiles()` y `createNewFile()`
- 6. Ejemplo, buenas prácticas y resumen

Note: En la segunda mitad dejamos de mirar la ruta solo como un dato y empezamos a usarla para **consultar** y **operar**. La meta es que el alumnado sepa distinguir qué puede resolver la clase **`File`** por sí sola y qué tareas quedarán ya para los métodos de **lectura** y **escritura** del siguiente apartado.

---

## 1. Qué es realmente `File`

Note: Esta es la idea central del tema y conviene detenerse aquí con calma. En programación es muy habitual que al principio se mezclen **ruta**, **archivo** y **contenido** como si fueran lo mismo, pero no lo son: la **ruta** localiza, el **archivo** existe o no existe en disco, y el **contenido** solo aparece cuando lo leemos.


### 1.1. `File` representa una ruta

- Pertenece a `java.io.File`
- Puede apuntar a un fichero
- Puede apuntar a un directorio
- Puede señalar una ubicación que aún no existe

```kotlin
import java.io.File

val fichero = File("datos/alumnos.txt")
val carpeta = File("datos")
```

Note: Fijaos en que en ambos casos solo estamos construyendo objetos que representan una **ruta**. Todavía no hemos leído ningún dato, no hemos creado el fichero automáticamente y no hemos abierto ningún flujo: simplemente hemos preparado una referencia con la que el programa podrá trabajar después.


### 1.2. Lo que `File` no hace por si solo

- No carga el fichero completo en memoria
- No implica que la ruta exista
- No lee ni escribe contenido automáticamente
- Sirve como punto de partida para consultar u operar

Note: Este matiz evita muchos errores de base. Tener un objeto **`File`** no significa que el fichero exista, ni que esté cargado, ni que podamos suponer que ya hay datos listos para usar; significa únicamente que tenemos una **referencia a una ruta** sobre la que luego habrá que consultar o actuar.

---

## 2. Crear objetos `File`

Note: Una vez entendido qué representa **`File`**, el siguiente paso lógico es aprender a construirlo bien. Aquí conviene insistir en que, en proyectos de aula y también en muchos proyectos reales, las **rutas relativas** suelen ser más mantenibles que las absolutas porque hacen el código más portable.


### 2.1. Crear rutas simples y compuestas

- Se puede pasar una ruta directa al constructor
- También se puede combinar carpeta padre y nombre de fichero

```kotlin
val ruta = File("datos/notas.txt")

val carpeta = File("datos")
val fichero = File(carpeta, "notas.txt")
```

Note: La segunda forma suele ser más clara cuando trabajamos con varias rutas dentro de una misma carpeta porque separa mejor la idea de **directorio padre** y **nombre del fichero**. Didácticamente es útil porque hace visible que una ruta también puede construirse por partes y no solo como una cadena larga.


### 2.2. Rutas absolutas y relativas

- La ruta absoluta parte de la raíz del sistema
- La relativa se interpreta desde el directorio de trabajo
- En proyectos portables, suele convenir usar rutas relativas

```kotlin
val absoluta = File("/home/ana/documentos/notas.txt")
val relativa = File("datos/notas.txt")
```

Note: La recomendación práctica aquí es evitar rutas rígidas y pegadas a un único ordenador salvo que exista una razón concreta. Si escribimos una **ruta absoluta** muy específica, el programa puede funcionar en nuestro equipo y fallar en todos los demás, así que conviene enseñar pronto el valor de la **portabilidad**.


### 2.3. Directorio de trabajo

- Una ruta relativa depende de dónde se ejecuta el programa
- `absolutePath` permite ver la ruta completa resultante

```kotlin
val fichero = File("datos/notas.txt")
println(fichero.absolutePath)
```

Note: Esta slide es importante porque explica un fallo muy frecuente: el mismo código puede apuntar a sitios distintos si cambia el **directorio de trabajo**. Quiero que el alumnado entienda que una **ruta relativa** siempre depende del contexto desde el que se ejecuta el programa, y por eso `absolutePath` ayuda tanto a depurar.

---

## 3. Consultar información de una ruta

Note: Ahora dejamos de crear rutas y pasamos a **inspeccionarlas** antes de tocar nada. Esta costumbre es muy sana a nivel docente y profesional, porque consultar primero el estado de una ruta evita muchas operaciones a ciegas y ayuda a construir programas más robustos.


### 3.1. Nombre, padre y ruta absoluta

- `name` devuelve el nombre del fichero o directorio
- `parent` devuelve la carpeta padre
- `absolutePath` devuelve la ruta completa

```kotlin
val fichero = File("datos/notas.txt")
println(fichero.name)
println(fichero.parent)
println(fichero.absolutePath)
```

Note: Estas propiedades parecen sencillas, pero son muy valiosas para **depuración**, **trazas** y comprobaciones rápidas. Conviene acostumbrar al alumnado a imprimir o revisar **nombre**, **padre** y **ruta absoluta** cuando una operación falla, porque muchas veces el error real está en la ruta y no en el resto del programa.


### 3.2. Comprobar si existe y de que tipo es

- `exists()` comprueba si la ruta existe
- `isFile` indica si es un fichero
- `isDirectory` indica si es un directorio

```kotlin
val ruta = File("datos")
println(ruta.exists())
println(ruta.isFile)
println(ruta.isDirectory)
```

Note: Este bloque es clave para no operar "a ciegas". Antes de leer, borrar o renombrar, lo sensato es comprobar si la ruta **existe** y si apunta a un **fichero** o a un **directorio**; además, una extensión como `.txt` puede orientarnos, pero no demuestra por sí sola qué hay realmente detrás de esa ruta.


### 3.3. Metadatos: tamaño y fecha

- `length()` devuelve tamaño en bytes
- `lastModified()` indica la última modificación
- Son útiles si la ruta existe y es un fichero

```kotlin
if (fichero.exists() && fichero.isFile) {
    println(fichero.length())
    println(fichero.lastModified())
}
```

Note: Estos **metadatos** permiten responder preguntas prácticas antes de tocar el contenido: si el fichero está vacío, si se modificó hace poco o si tiene sentido procesarlo. Es útil remarcar que la información del sistema de archivos también forma parte del problema, no solo el texto guardado dentro.

---

## 4. Operaciones básicas con directorios y rutas

Note: En esta parte **`File`** deja de ser solo una herramienta de consulta y pasa a permitir **acciones** sobre el sistema de archivos. El alumnado debe ver que muchas de estas operaciones devuelven un **booleano**, y eso obliga a comprobar el resultado en lugar de asumir que todo ha salido bien.


### 4.1. Crear directorios

- `mkdir()` crea una carpeta
- `mkdirs()` crea varias carpetas anidadas

```kotlin
val carpeta = File("salidas")
carpeta.mkdir()

val arbol = File("salidas/2026/marzo")
arbol.mkdirs()
```

Note: Conviene explicar con calma la diferencia entre crear una sola carpeta y crear un **árbol de directorios** completo. Esta distinción parece pequeña, pero aparece enseguida en ejercicios reales y ayuda a que el alumnado piense mejor la estructura de carpetas que necesita el programa.


### 4.2. Borrar y renombrar

- `delete()` borra si la operación es posible
- `renameTo()` permite renombrar o mover
- Ambas operaciones devuelven `true` o `false`

```kotlin
val temporal = File("temporal.txt")
val borrado = temporal.delete()

val origen = File("borrador.txt")
val destino = File("entrega.txt")
val cambiado = origen.renameTo(destino)
```

Note: Es importante remarcar que un `false` no significa necesariamente que el código esté "mal hecho". Puede faltar la ruta, pueden faltar **permisos**, puede haber conflictos de nombres o una carpeta puede no estar vacía; por eso la programación con archivos exige comprobar resultados y no dar nada por supuesto.

---

## 5. Listar y crear ficheros vacios

Note: Cerramos la parte operativa con dos casos muy frecuentes y muy útiles para el aula: recorrer el contenido de una **carpeta** y crear un **fichero vacío** como preparación para trabajar después con su contenido. Son operaciones muy pequeñas, pero conectan muy bien con tareas reales de **automatización** y de inspección del sistema de archivos.


### 5.1. `listFiles()` para recorrer directorios

- Devuelve los elementos de una carpeta
- Resulta útil para listar, filtrar o procesar por lotes

```kotlin
val carpeta = File("datos")
val elementos = carpeta.listFiles()

if (elementos != null) {
    for (elemento in elementos) {
        println(elemento.name)
    }
}
```

Note: Aquí interesa remarcar que el resultado puede ser **`null`**, y eso obliga a pensar con cuidado. No debemos asumir automáticamente que la carpeta existe, que es accesible o que la operación ha salido bien; precisamente por eso esta slide enseña a programar con más **prudencia** y más control de errores.


### 5.2. `createNewFile()` como puente a `7.4`

- Crea un fichero vacío si no existía
- Devuelve `true` si lo crea
- Devuelve `false` si ya existía

```kotlin
val fichero = File("registro.txt")
val creado = fichero.createNewFile()
println("Creado: $creado")
```

Note: Esta operación funciona como enlace natural con el siguiente tema. Aquí todavía no trabajamos el **contenido** del fichero, pero sí dejamos claro que primero hay una **ruta**, luego puede haber un **fichero creado**, y solo después llegará la lectura o la escritura de datos reales.

---

## 6. Ejemplo integrador y cierre

Note: Terminamos reuniendo varias piezas del tema en un ejemplo sencillo para que el alumnado vea el recorrido completo. La intención no es impresionar con complejidad, sino mostrar cómo se combinan **rutas relativas**, comprobaciones básicas y consultas sobre el sistema de archivos en un programa coherente.


### 6.1. Ejemplo integrador

```kotlin
val carpeta = File("datos")
if (!carpeta.exists()) carpeta.mkdir()

val fichero = File(carpeta, "notas.txt")
println(fichero.absolutePath)
println(fichero.exists())
println(fichero.isFile)
println(fichero.parent)
```

- Construye rutas relativas
- Comprueba estados básicos
- Consulta información útil del sistema de archivos

Note: Este ejemplo no escribe contenido todavía, y eso es precisamente lo interesante. Sirve para mostrar que **`File`** ya aporta valor antes de leer o escribir nada, porque nos permite **representar**, **consultar** y verificar rutas con las que luego trabajaremos de manera más segura.


### 6.2. Buenas practicas y resumen

- Usa rutas relativas cuando tenga sentido
- Comprueba si la ruta existe antes de operar
- Distingue entre fichero y directorio
- No confundas ruta con contenido
- `7.4` se encargará de leer y escribir datos

Note: Si el alumnado sale con esta lista clara, el tema está bien asentado. La idea final que quiero que recuerden es distinguir siempre entre **ruta**, **fichero** y **contenido**, porque esa separación conceptual es la que permitirá leer y escribir datos reales sin confusiones en el siguiente bloque.
