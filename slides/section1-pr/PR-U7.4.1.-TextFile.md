# PR-U7.4.1 - Ficheros de texto

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: Esta presentación profundiza en el caso más habitual del aula: los
**ficheros de texto**. Aquí aterrizamos con más detalle cómo leer, escribir y
dar formato a información persistente en Kotlin.


### Índice I

- 1. Qué es un fichero de texto
- 2. Crear una referencia con `File`
- 3. Leer con `readText()`, `readLines()` y `useLines()`
- 4. Escribir con `writeText()`, `appendText()` y `bufferedWriter()`

Note: La primera parte del tema se centra en las operaciones básicas y en elegir
la herramienta adecuada según la tarea que se quiera realizar.


### Índice II

- 5. Mantener el mismo formato al leer y escribir
- 6. Caracteres especiales: `\n`, `\r` y `\t`
- 7. Casos prácticos
- 8. Buenas prácticas, errores frecuentes y resumen

Note: La segunda mitad resuelve matices importantes: el formato, los caracteres
especiales y los errores que aparecen al empezar a trabajar con texto.

---

## 1. ¿Que es un fichero de texto?

Note: Abrimos con la ventaja principal del formato textual: permite ver de
forma directa qué se ha guardado, lo que lo hace ideal para aprender.


### 1.1. Informacion legible

- Guarda caracteres en lugar de bytes opacos
- Suele poder abrirse con un editor
- Es útil para configuraciones, CSV, informes y logs

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

Note: Este ejemplo muestra por qué el texto es tan cómodo en aprendizaje:
permite inspeccionar rápidamente el resultado sin herramientas especiales.

---

## 2. Crear una referencia al fichero

Note: Antes de leer o escribir, siempre necesitamos una ruta representada por
`File`. Es la puerta de entrada al trabajo con el archivo.


### 2.1. Preparar la ruta con `File`

```kotlin
import java.io.File

val fichero = File("datos/notas.txt")
```

- La ruta puede ser relativa al proyecto
- Aún no se ha leído ni escrito contenido
- Solo estamos preparando la referencia

Note: Conviene reforzar una vez más la distinción entre representar una ruta y
acceder realmente al contenido del fichero.

---

## 3. Leer ficheros de texto

Note: Kotlin ofrece varias formas de lectura. La elección depende del tamaño
del fichero y del tipo de procesamiento que queremos hacer.


### 3.1. `readText()` y `readLines()`

- `readText()` devuelve una cadena completa
- `readLines()` devuelve una lista de líneas

```kotlin
val contenido = File("datos/notas.txt").readText()
val lineas = File("datos/notas.txt").readLines()
```

Note: La diferencia práctica es importante: a veces necesitas el texto entero y
otras veces necesitas recorrer el fichero línea a línea.


### 3.2. `useLines()` para procesar mejor

- Procesa el archivo de forma secuencial
- Evita cargar todo en memoria si no hace falta

```kotlin
File("datos/notas.txt").useLines { lineas ->
    lineas.forEach { println(it) }
}
```

Note: Esta opción es especialmente útil cuando el fichero puede crecer o cuando
solo necesitas recorrerlo una vez.

---

## 4. Escribir en ficheros de texto

Note: En escritura la decisión principal es si queremos rehacer el archivo o
añadir nueva información conservando lo anterior.


### 4.1. `writeText()` y `appendText()`

- `writeText()` sobrescribe el contenido previo
- `appendText()` añade contenido al final

```kotlin
File("salida.txt").writeText("Hola desde Kotlin\n")
File("log.txt").appendText("Nueva entrada\n")
```

Note: Muchísimos fallos vienen de no distinguir estas dos operaciones. Es uno
de los mensajes que más conviene repetir durante la unidad.


### 4.2. `bufferedWriter()` y `use()`

- Permite escribir varias líneas con un escritor
- `use()` garantiza el cierre correcto del recurso

```kotlin
File("salida.txt").bufferedWriter().use { writer ->
    writer.write("Primera linea\n")
    writer.write("Segunda linea\n")
}
```

Note: Esta slide también sirve para reforzar la idea de gestionar bien los
recursos cuando trabajamos con E/S más explícita.

---

## 5. Leer y escribir con el mismo formato

Note: Este punto es esencial. No basta con guardar datos: también hay que poder
recuperarlos siguiendo la misma lógica.


### 5.1. La estructura del fichero importa

- Cada línea puede representar un registro
- Un separador como la coma también es parte del formato
- Si cambias la escritura, tendrás que ajustar la lectura

```text
Ana,8.5
Luis,7.25
```

Note: Aquí conviene hacer la pregunta didáctica clave: "¿cómo voy a guardar
esto y cómo lo recuperaré después?". Esa pregunta guía casi todo el diseño.

---

## 6. Caracteres especiales importantes

Note: En texto hay caracteres que no siempre se ven, pero sí cambian el
resultado final del archivo o de la salida en consola.


### 6.1. `\n`, `\r` y `\t`

- `\n` crea una nueva línea
- `\r\n` es habitual en Windows
- `\t` introduce un tabulador

```kotlin
val tabla = "Nombre\tNota\nAna\t8.5"
println(tabla)
```

Note: Explicar estos caracteres ayuda mucho a entender por qué a veces el texto
queda "pegado", con saltos extraños o mal alineado.


### 6.2. Fin de fichero y lectura secuencial

- Al leer secuencialmente llega un momento sin más datos
- Ese punto se llama fin de fichero o `EOF`
- Métodos como `useLines()` ayudan a controlarlo bien

Note: Esta idea conecta el trabajo con archivos con lo que ya se vio en consola
cuando la entrada estándar puede agotarse.

---

## 7. Ejemplos practicos

Note: Cerramos la parte técnica con dos actividades pequeñas y muy útiles para
ver valor inmediato en el trabajo con texto.


### 7.1. Contar lineas de un fichero

```kotlin
val numeroDeLineas = File("datos/notas.txt").useLines { it.count() }
println("El fichero tiene $numeroDeLineas lineas.")
```

- Muestra un procesamiento secuencial sencillo
- Obliga a pensar en el fichero como colección de líneas

Note: Este ejemplo es breve, pero muy expresivo. Hace visible que un fichero de
texto también puede tratarse como una secuencia de registros.


### 7.2. Registro de eventos e informe

```kotlin
File("registro.txt").appendText("[inicio] Aplicacion lanzada\n")

val informe = File("informe.txt")
if (informe.exists()) {
    println(informe.readText())
}
```

- `appendText()` resulta útil para historiales
- `readText()` permite mostrar un informe completo
- Conviene comprobar existencia antes de leer

Note: Esta slide une dos usos muy típicos de texto: mantener un log y mostrar
el contenido de un informe guardado previamente.

---

## 8. Buenas practicas y resumen

Note: Terminamos con una lista corta de control y con las ideas esenciales del
apartado para que el alumnado pueda aplicarlas en ejercicios y prácticas.


### 8.1. Lista de control final

- Comprueba la ruta antes de leer cuando tenga sentido
- Distingue entre sobrescribir y añadir
- No cargues ficheros enormes sin necesidad
- Define un formato claro si luego vas a releer el archivo
- Piensa siempre en cómo recuperarás lo que guardas

Note: Si esta lista queda clara, el tema está bien asentado. El alumnado ya
dispone de una base sólida para trabajar con persistencia textual en Kotlin.
