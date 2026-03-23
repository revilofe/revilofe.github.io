# PR-U7.3 - Manejo de archivos con File

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: En esta presentación trabajamos la clase **`File`**. El objetivo no es
leer contenido todavía, sino aprender a representar **rutas**, consultar su
estado y realizar operaciones básicas sobre ficheros y directorios.


### Índice I

- 1. Qué representa realmente `File`
- 2. Crear objetos `File`
- 2.1. Rutas absolutas y relativas
- 2.2. Directorio de trabajo
- 3. Consultar información de una ruta

Note: La primera mitad se centra en una idea conceptual importante: un objeto
`File` representa una **ruta**, no el contenido del archivo en memoria. Desde
ahí construimos el resto del tema.


### Índice II

- 3.2. `exists()`, `isFile` e `isDirectory`
- 3.4. Tamaño y fecha de modificación
- 4. Operaciones básicas con directorios y rutas
- 5. `listFiles()` y `createNewFile()`
- 6. Ejemplo, buenas prácticas y resumen

Note: En la segunda mitad pasamos de consultar a operar. El alumnado debe salir
del tema sabiendo qué permite `File` y qué cosas quedan para `7.4`.

---

## 1. Qué es realmente `File`

Note: Esta es la idea central del tema. Si no se entiende bien, es fácil
confundir "ruta", "archivo" y "contenido" como si fueran lo mismo.


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

Note: En ambos casos solo estamos creando objetos que representan rutas. Aún no
se ha leído ningún contenido ni se ha creado automáticamente nada en disco.


### 1.2. Lo que `File` no hace por si solo

- No carga el fichero completo en memoria
- No implica que la ruta exista
- No lee ni escribe contenido automáticamente
- Sirve como punto de partida para consultar u operar

Note: Este matiz evita muchos malentendidos. Tener un objeto `File` no es lo
mismo que tener el archivo leído o creado. Solo tenemos una referencia de ruta.

---

## 2. Crear objetos `File`

Note: Después de entender qué representa, toca ver cómo se construye y por qué
las rutas relativas suelen ser la opción más razonable en proyectos de aula.


### 2.1. Crear rutas simples y compuestas

- Se puede pasar una ruta directa al constructor
- También se puede combinar carpeta padre y nombre de fichero

```kotlin
val ruta = File("datos/notas.txt")

val carpeta = File("datos")
val fichero = File(carpeta, "notas.txt")
```

Note: La segunda forma mejora la legibilidad cuando trabajamos con varias rutas
relacionadas dentro de una misma carpeta.


### 2.2. Rutas absolutas y relativas

- La ruta absoluta parte de la raíz del sistema
- La relativa se interpreta desde el directorio de trabajo
- En proyectos portables, suele convenir usar rutas relativas

```kotlin
val absoluta = File("/home/ana/documentos/notas.txt")
val relativa = File("datos/notas.txt")
```

Note: La recomendación didáctica es clara: evitar rutas rígidas ligadas a un
único equipo salvo que haya una razón concreta para hacerlo.


### 2.3. Directorio de trabajo

- Una ruta relativa depende de dónde se ejecuta el programa
- `absolutePath` permite ver la ruta completa resultante

```kotlin
val fichero = File("datos/notas.txt")
println(fichero.absolutePath)
```

Note: Esta slide ayuda a entender por qué el mismo código puede apuntar a
ubicaciones distintas si cambia el directorio desde el que se lanza el programa.

---

## 3. Consultar información de una ruta

Note: Ahora pasamos a las consultas. Este bloque enseña a inspeccionar una ruta
antes de operar con ella, que es justo lo que evita muchos errores.


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

Note: Estas propiedades son útiles para depuración, trazas y comprobaciones. El
alumnado debería acostumbrarse a inspeccionar rutas reales cuando algo falla.


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

Note: Este bloque es clave para no operar "a ciegas". También conviene recordar
que una extensión como `.txt` no prueba por sí sola que sea un fichero real.


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

Note: Estos metadatos permiten responder preguntas prácticas: si el fichero
está vacío, si se ha modificado recientemente o si merece procesarse.

---

## 4. Operaciones básicas con directorios y rutas

Note: Aquí `File` deja de ser solo consulta y pasa a permitir acciones. La
idea es mostrar operaciones sencillas y su resultado booleano.


### 4.1. Crear directorios

- `mkdir()` crea una carpeta
- `mkdirs()` crea varias carpetas anidadas

```kotlin
val carpeta = File("salidas")
carpeta.mkdir()

val arbol = File("salidas/2026/marzo")
arbol.mkdirs()
```

Note: Conviene explicar la diferencia entre crear una carpeta simple y crear un
árbol completo. Es una distinción práctica que suele aparecer pronto.


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

Note: Es importante remarcar que devolver `false` no es raro: puede no existir
la ruta, faltar permisos o estar la carpeta aún no vacía.

---

## 5. Listar y crear ficheros vacios

Note: Cerramos la parte operativa con dos casos muy frecuentes: recorrer una
carpeta y crear un fichero vacío antes de trabajar con su contenido.


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

Note: Aquí interesa remarcar que el resultado puede ser `null`, así que no se
debe asumir siempre que la carpeta existe o que la operación saldrá bien.


### 5.2. `createNewFile()` como puente a `7.4`

- Crea un fichero vacío si no existía
- Devuelve `true` si lo crea
- Devuelve `false` si ya existía

```kotlin
val fichero = File("registro.txt")
val creado = fichero.createNewFile()
println("Creado: $creado")
```

Note: Esta operación sirve como enlace natural con el siguiente tema. Aquí aún
no tratamos el contenido, pero ya preparamos la ruta y el fichero.

---

## 6. Ejemplo integrador y cierre

Note: Terminamos uniendo varias piezas del tema en un único programa sencillo y
dejando claras las buenas prácticas básicas.


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

Note: Este ejemplo no escribe contenido todavía. Su función es mostrar cómo
`File` sirve para representar y consultar antes de leer o escribir nada.


### 6.2. Buenas practicas y resumen

- Usa rutas relativas cuando tenga sentido
- Comprueba si la ruta existe antes de operar
- Distingue entre fichero y directorio
- No confundas ruta con contenido
- `7.4` se encargará de leer y escribir datos

Note: Si el alumnado sale con esta lista clara, el tema está bien asentado. La
siguiente etapa será trabajar con el contenido real de los ficheros.
