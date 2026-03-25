# PR-U7.4.1 - Ficheros de texto

Note: Esta presentación profundiza en el caso más frecuente del aula, que son los **ficheros de texto**. Aquí vamos a aterrizar con más detalle cómo se **leen**, cómo se **escriben** y cómo se diseña un **formato textual** que luego el programa pueda recuperar sin ambigüedades.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Este bloque continúa lo visto en `7.4`, pero ahora con foco total en el formato **textual**, que es el más didáctico para empezar. Queremos que el alumnado no solo conozca métodos como **`readText()`**, **`readLines()`**, **`useLines()`**, **`writeText()`** o **`appendText()`**, sino que sepa elegirlos con un criterio razonado.

---

## Índice

Note: Esta presentación profundiza en el caso más habitual del aula, que son los **ficheros de texto**. La meta es que el alumnado entienda no solo la API de Kotlin, sino también las decisiones de **formato**, **lectura** y **escritura** que hacen que un fichero textual sea realmente útil.


### Índice I

- 1. Qué es un fichero de texto
- 2. Crear una referencia con `File`
- 3. Leer con `readText()`, `readLines()` y `useLines()`
- 4. Escribir con `writeText()`, `appendText()` y `bufferedWriter()`

Note: La primera parte del tema se centra en las operaciones básicas y en elegir la **herramienta adecuada** según la tarea. Quiero que el alumnado vea pronto que no hay un único método "bueno", sino varias opciones cuya utilidad depende del tipo de **procesamiento** que queramos hacer.


### Índice II

- 5. Mantener el mismo formato al leer y escribir
- 6. Caracteres especiales: `\n`, `\r` y `\t`
- 7. Casos prácticos
- 8. Buenas prácticas, errores frecuentes y resumen

Note: La segunda mitad se detiene en matices que suelen generar fallos reales: el **formato**, los **caracteres especiales**, la coherencia entre lectura y escritura y varios **errores frecuentes**. Es la parte que convierte el uso de texto en una práctica más rigurosa.

---

## 1. ¿Que es un fichero de texto?

Note: Abrimos con la principal ventaja del formato **textual**: permite ver directamente qué se ha guardado. Eso lo convierte en un caso ideal para aprender, porque el alumnado puede relacionar muy fácilmente el código que escribe con el resultado visible en el fichero.


### 1.1. Informacion legible

- Guarda caracteres en lugar de bytes opacos
- Suele poder abrirse con un editor
- Es útil para configuraciones, CSV, informes y logs

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

Note: Este ejemplo muestra por qué el **texto** es tan cómodo en aprendizaje: se puede inspeccionar rápidamente con herramientas muy simples y permite ver enseguida si el programa está guardando la información con el **formato** esperado.

---

## 2. Crear una referencia al fichero

Note: Antes de leer o escribir, siempre necesitamos una **ruta** representada por **`File`**. Conviene remarcar que esta es la puerta de entrada al trabajo con el archivo: primero localizamos, luego comprobamos, y solo después leemos o escribimos contenido.


### 2.1. Preparar la ruta con `File`

```kotlin
import java.io.File

val fichero = File("datos/notas.txt")
```

- La ruta puede ser relativa al proyecto
- Aún no se ha leído ni escrito contenido
- Solo estamos preparando la referencia

Note: Conviene reforzar una vez más la distinción entre **representar una ruta** y **acceder al contenido** del fichero. Esa diferencia parece pequeña, pero evita muchos malentendidos cuando el alumnado empieza a combinar `File` con los métodos de lectura y escritura.

---

## 3. Leer ficheros de texto

Note: Kotlin ofrece varias formas de **lectura**, y conviene presentarlas como decisiones de diseño, no como una lista para memorizar. La elección depende del **tamaño del fichero**, de si queremos todo el contenido de golpe o si vamos a procesarlo paso a paso.


### 3.1. `readText()` y `readLines()`

- `readText()` devuelve una cadena completa
- `readLines()` devuelve una lista de líneas

```kotlin
val contenido = File("datos/notas.txt").readText()
val lineas = File("datos/notas.txt").readLines()
```

Note: La diferencia práctica aquí es muy importante: unas veces necesitaremos el texto completo como una única **cadena**, y otras necesitaremos recorrer el fichero **línea a línea**. Elegir bien esa forma de lectura simplifica mucho el resto del programa.


### 3.2. `useLines()` para procesar mejor

- Procesa el archivo de forma secuencial
- Evita cargar todo en memoria si no hace falta

```kotlin
File("datos/notas.txt").useLines { lineas ->
    lineas.forEach { println(it) }
}
```

Note: **`useLines()`** es especialmente útil cuando el fichero puede crecer bastante o cuando solo necesitamos recorrerlo una vez. Es una buena oportunidad para introducir la idea de **procesamiento secuencial** y de uso más contenido de la memoria.

---

## 4. Escribir en ficheros de texto

Note: En **escritura** la decisión principal es si queremos **rehacer** el archivo desde cero o **añadir** nueva información conservando lo que ya había. Este punto conviene explicarlo con mucha claridad porque de él depende no perder datos por accidente.


### 4.1. `writeText()` y `appendText()`

- `writeText()` sobrescribe el contenido previo
- `appendText()` añade contenido al final

```kotlin
File("salida.txt").writeText("Hola desde Kotlin\n")
File("log.txt").appendText("Nueva entrada\n")
```

Note: Muchísimos fallos vienen de no distinguir entre **`writeText()`** y **`appendText()`**. Es uno de los mensajes que más conviene repetir durante la unidad, porque la diferencia entre **sobrescribir** y **añadir** cambia por completo el comportamiento del programa.


### 4.2. `bufferedWriter()` y `use()`

- Permite escribir varias líneas con un escritor
- `use()` garantiza el cierre correcto del recurso

```kotlin
File("salida.txt").bufferedWriter().use { writer ->
    writer.write("Primera linea\n")
    writer.write("Segunda linea\n")
}
```

Note: Esta slide también sirve para reforzar la idea de **gestionar bien los recursos** cuando trabajamos con una **E/S** más explícita. No basta con escribir; también hay que cerrar correctamente y mantener un código ordenado, y ahí **`use()`** ayuda mucho.

---

## 5. Leer y escribir con el mismo formato

Note: Este punto es esencial y merece remarcarse mucho en voz docente. No basta con **guardar datos**; también hay que poder **recuperarlos** después siguiendo exactamente la misma lógica de **formato** y de estructura que se usó al escribir.


### 5.1. La estructura del fichero importa

- Cada línea puede representar un registro
- Un separador como la coma también es parte del formato
- Si cambias la escritura, tendrás que ajustar la lectura

```text
Ana,8.5
Luis,7.25
```

Note: Aquí conviene hacer la pregunta didáctica clave: "¿cómo voy a guardar esto y cómo lo recuperaré después?". Esa pregunta guía casi todo el diseño del fichero, porque obliga a pensar en **separadores**, **líneas**, orden de campos y forma de lectura futura.

---

## 6. Caracteres especiales importantes

Note: En **texto** hay caracteres que no siempre se ven, pero cambian completamente el resultado final del archivo o de la salida en consola. Por eso conviene explicar despacio qué hacen **`\n`**, **`\r`** o **`\t`** y por qué afectan al aspecto del contenido.


### 6.1. `\n`, `\r` y `\t`

- `\n` crea una nueva línea
- `\r\n` es habitual en Windows
- `\t` introduce un tabulador

```kotlin
val tabla = "Nombre\tNota\nAna\t8.5"
println(tabla)
```

Note: Explicar estos caracteres ayuda mucho a entender por qué a veces el texto queda "pegado", con saltos extraños o mal alineado. Es un detalle pequeño en apariencia, pero muy útil para que el alumnado entienda mejor el comportamiento real del formato **textual**.


### 6.2. Fin de fichero y lectura secuencial

- Al leer secuencialmente llega un momento sin más datos
- Ese punto se llama fin de fichero o `EOF`
- Métodos como `useLines()` ayudan a controlarlo bien

Note: Esta idea conecta el trabajo con archivos con lo que ya se vio en consola cuando la **entrada estándar** podía agotarse. El concepto de **fin de fichero** muestra que leer datos también implica saber reconocer cuándo ya no queda nada más que procesar.

---

## 7. Ejemplos practicos

Note: Cerramos la parte técnica con dos actividades pequeñas, pero muy útiles para que el alumnado vea valor inmediato en el trabajo con **texto**. La idea es pasar de la explicación teórica a ejemplos con una utilidad reconocible y fácil de comprobar.


### 7.1. Contar lineas de un fichero

```kotlin
val numeroDeLineas = File("datos/notas.txt").useLines { it.count() }
println("El fichero tiene $numeroDeLineas lineas.")
```

- Muestra un procesamiento secuencial sencillo
- Obliga a pensar en el fichero como colección de líneas

Note: Este ejemplo es breve, pero muy expresivo. Hace visible que un fichero de **texto** también puede tratarse como una **secuencia de registros**, y eso ayuda a pensar en líneas no solo como texto, sino como unidades de información procesables.


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

Note: Esta slide une dos usos muy típicos del formato **textual**: mantener un **log** histórico y mostrar el contenido de un **informe** guardado previamente. Es un buen ejemplo para que el alumnado vea dos patrones muy frecuentes de persistencia en programas reales.

---

## 8. Buenas practicas y resumen

Note: Terminamos con una lista corta de **control** y con las ideas esenciales del apartado para que el alumnado pueda aplicarlas en ejercicios y prácticas. Este cierre sirve como **resumen operativo**, no solo como recapitulación teórica.


### 8.1. Lista de control final

- Comprueba la ruta antes de leer cuando tenga sentido
- Distingue entre sobrescribir y añadir
- No cargues ficheros enormes sin necesidad
- Define un formato claro si luego vas a releer el archivo
- Piensa siempre en cómo recuperarás lo que guardas

Note: Si esta lista queda clara, el tema está bien asentado. El alumnado ya dispone de una base sólida para trabajar con **persistencia textual** en Kotlin y para diseñar ficheros cuyo **formato** se pueda leer después sin ambigüedades ni sorpresas.
