# PR-U7.2.1 - Consola y teclado: ampliacion

Note: Esta presentación amplía el trabajo anterior con **consola** y **teclado**, pero centrándose en los casos menos obvios y más propensos a dudas. Aquí vamos a hablar de **fin de entrada**, uso de **`Scanner`**, reutilización de validaciones y **argumentos de línea de comandos**, que son detalles que aparecen en cuanto un programa deja de ser tan simple.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: El objetivo de esta ampliación no es añadir teoría por añadir, sino dar **criterio** para tomar mejores decisiones cuando el programa deja de ser tan simple. Queremos que el alumnado entienda qué mecanismo encaja mejor según el contexto y no solo por costumbre o por copiar un ejemplo visto antes.

---

## Índice

Note: Esta presentación amplía `7.2` y debe entenderse como una capa de profundidad, no como un tema distinto. No sustituye los fundamentos, sino que aclara los casos que suelen generar dudas cuando el programa deja de ser tan simple: **final de entrada**, **`Scanner`**, funciones auxiliares y **argumentos**.


### Índice I

- 1. `readln()`, `readlnOrNull()` y `readLine()`
- 2. Fin de entrada y `EOF`
- 3. `Scanner` desde Kotlin
- 3.1. El problema del salto de linea

Note: Primero comparamos las funciones de lectura más habituales para que el alumnado deje de verlas como nombres sueltos sin contexto. Después introducimos el concepto de **fin de entrada**, que cambia bastante el diseño de algunos programas de consola y explica por qué existen varias alternativas.


### Índice II

- 4. Funciones auxiliares para pedir datos
- 5. Argumentos de linea de comandos
- 6. Comparativa rapida de mecanismos
- 7. Propuestas de practica y cierre

Note: La segunda parte tiene una orientación más de **diseño** que de simple sintaxis. Nos centraremos en cómo reutilizar la **validación**, cuándo usar **argumentos** y cómo elegir el mecanismo más adecuado en cada situación sin improvisar.

---

## 1. `readln()`, `readlnOrNull()` y `readLine()`

Note: El alumnado suele ver estas tres opciones en materiales distintos y acaba con la sensación de que son equivalentes o intercambiables sin más. Por eso conviene compararlas de forma explícita y explicar cuándo interesa cada una, qué problema resuelve realmente y qué diferencia hay entre una lectura **segura**, una lectura **anulable** y una opción más **histórica**.


### 1.1. Comparativa rapida

| Funcion | Devuelve | Comportamiento |
| --- | --- | --- |
| `readln()` | `String` | Espera una linea y falla si no hay entrada |
| `readlnOrNull()` | `String?` | Devuelve `null` si no quedan datos |
| `readLine()` | `String?` | Variante historica frecuente en codigo antiguo |
<!-- .element.table: style="font-size:70%;" -->

Note: La idea clave no es memorizar la tabla como si fuera un formulario, sino entender la diferencia entre una lectura que **asume entrada disponible** y otra que puede detectar su agotamiento sin lanzar una excepción. Ese matiz es pequeño en apariencia, pero cambia por completo el diseño de algunos programas.


### 1.2. Cuando usar cada una

- `readln()` en programas interactivos sencillos
- `readlnOrNull()` si la entrada puede agotarse
- `readLine()` para reconocer codigo heredado

```kotlin
print("Nombre: ")
val nombre = readln()
println("Hola, $nombre")
```

Note: En contexto didáctico, **`readln()`** suele ser la opción más clara porque reduce ruido y deja ver bien la intención del código. La versión **anulable** empieza a cobrar sentido cuando la **entrada** ya no la controla directamente la persona usuaria y necesitamos detectar con seguridad cuándo se ha terminado.

---

## 2. Fin de entrada y `EOF`

Note: Esta sección introduce un matiz muy importante que suele pasar desapercibido en los primeros ejercicios: la **entrada estándar** también puede terminar. Entender esto evita muchos errores conceptuales porque rompe la idea de que siempre habrá una línea más esperando al programa.


### 2.1. Que significa `EOF`

- `EOF` significa fin de entrada
- Puede ocurrir con redirecciones, tuberias o datos agotados
- `readln()` lanza excepción si ya no hay datos
- `readlnOrNull()` permite detectarlo con `null`

```kotlin
while (true) {
    val linea = readlnOrNull() ?: break
    println("Procesando: $linea")
}
```

Note: Este patrón es muy útil para leer múltiples líneas hasta que la **entrada** se agote y, además, es muy fácil de explicar en voz docente. Conviene remarcar que no depende de un número fijo de repeticiones, sino de una condición real: que todavía queden **datos** por leer.

---

## 3. Uso de `Scanner` desde Kotlin

Note: **`Scanner`** no es imprescindible en la unidad, pero aparece en muchísimo material de **Java** y por eso merece una explicación breve y práctica. La idea no es adoptarlo como herramienta principal, sino reconocerlo y saber leer ejemplos que lo usen sin confundirlo con la opción por defecto en **Kotlin**.


### 3.1. Que aporta `Scanner`

- Es una clase de Java: `java.util.Scanner`
- Puede leer datos token a token
- Resulta útil en ejemplos heredados o interoperabilidad con Java

```kotlin
import java.util.Scanner

val scanner = Scanner(System.`in`)
print("Edad: ")
val edad = scanner.nextInt()
```

Note: Aquí interesa que el alumnado vea **`Scanner`** como una opción posible dentro del ecosistema **JVM**, no como la herramienta obligatoria. En Kotlin moderno, muchas veces **`readln()`** resulta más sencilla de explicar, mantener y justificar cuando el objetivo es la **claridad didáctica**.


### 3.2. El problema del salto de linea

- `nextInt()` o `nextDouble()` no consumen el fin de linea completo
- La siguiente llamada a `nextLine()` puede devolver vacio
- Suele resolverse con una llamada adicional a `nextLine()`

```kotlin
val edad = scanner.nextInt()
scanner.nextLine()
val ciudad = scanner.nextLine()
```

Note: Este es uno de los errores más típicos con **`Scanner`** y conviene dramatizarlo un poco en clase para que no se olvide. Si no se explica bien, parece que el programa "lee mal" sin motivo, cuando en realidad el problema está en cómo se consume el **salto de línea**.


### 3.3. Cuando compensa usar `Scanner`

- Si el material base ya esta en Java
- Si quieres leer tokens separados por espacios
- Si necesitas interoperar con ejemplos ya construidos
- En ejercicios normales, `readln()` suele ser mas claro

Note: La recomendación práctica para esta unidad debe quedar muy clara: conocer `Scanner`, sí, pero priorizar `readln()` y conversiones seguras cuando el objetivo sea la **claridad didáctica**. No queremos más herramientas por tenerlas, sino herramientas adecuadas para el nivel y el contexto.

---

## 4. Funciones auxiliares para pedir datos

Note: Cuando un programa crece, repetir siempre el mismo patrón de **validación** empieza a ensuciar el código y a ocultar la lógica importante. Aquí aparece la idea de encapsular la lectura en **funciones auxiliares**, que es un paso pequeño pero muy valioso hacia un diseño más limpio.


### 4.1. Reutilizar validacion con `pedirEntero`

```kotlin
fun pedirEntero(mensaje: String): Int {
    while (true) {
        print(mensaje)
        val numero = readln().toIntOrNull()
        if (numero != null) return numero
        System.err.println("Debes escribir un entero valido.")
    }
}
```

- Evita duplicar código
- Separa validación y lógica principal
- Hace más legible el programa

Note: Esta función es un buen ejemplo de **abstracción útil** porque no introduce complejidad gratuita, sino que elimina repeticiones y hace el programa más legible. El alumnado ve así que la **validación** no tiene por qué repetirse manualmente en cada punto del programa.


### 4.2. Variantes para otros tipos

- Se puede repetir la idea con `Double`, `Long` o menús
- El patrón general es pedir, convertir y repetir

```kotlin
fun pedirDouble(mensaje: String): Double {
    while (true) {
        print(mensaje)
        val numero = readln().toDoubleOrNull()
        if (numero != null) return numero
    }
}
```

Note: Aquí conviene destacar el **patrón** general y no memorizar una función concreta como si fuera una receta cerrada. La decisión de diseño importante es encapsular comportamientos repetidos, de forma que el programa gane claridad y sea más fácil de mantener.

---

## 5. Argumentos de linea de comandos

Note: No toda la entrada llega desde el **teclado** durante la ejecución, y esa idea es importante para abrir la mente del alumnado. A veces los datos se entregan al arrancar el programa y entonces el modelo de interacción cambia bastante.


### 5.1. `args: Array<String>`

- Los argumentos llegan antes de que el programa empiece a interactuar
- Son útiles para configuraciones simples y automatización

```kotlin
fun main(args: Array<String>) {
    if (args.isEmpty()) {
        println("Debes indicar al menos un nombre.")
        return
    }
    println("Hola, ${args[0]}")
}
```

Note: El contraste importante aquí es entre datos **pedidos en tiempo de ejecución** y datos **pasados al inicio** mediante argumentos. Ambos mecanismos forman parte del trabajo con programas de consola, pero no cumplen la misma función ni encajan en los mismos escenarios.


### 5.2. Teclado frente a argumentos

- **Teclado**: entrada durante la ejecución
- **Argumentos**: entrada al lanzar el programa
- El teclado es más interactivo
- Los argumentos son más cómodos para automatizar

Note: Esta comparación ayuda a elegir mejor el mecanismo según el **contexto**, que es justo el tipo de criterio que queremos enseñar. No se trata de decidir cuál es "mejor" en abstracto, sino de cuál encaja mejor con la necesidad real del programa.

---

## 6. Mini comparativa de mecanismos

Note: Esta slide resume la **toma de decisiones** de todo el tema y por eso funciona muy bien como referencia rápida antes de pasar a práctica. Quiero que el alumnado la vea como una pequeña **guía** para elegir sin improvisar cuando tenga varias opciones delante.


### 6.1. Que mecanismo elegir

| Situacion | Opcion recomendable |
| --- | --- |
| Programa interactivo sencillo | `readln()` |
| Entrada que puede agotarse | `readlnOrNull()` |
| Codigo heredado | `readLine()` |
| Interoperabilidad con Java | `Scanner` |
| Parametros al arrancar | `args` |
<!-- .element.table: style="font-size:70%;" -->

Note: Esta tabla no pretende ser absoluta ni sustituir el **juicio del programador**, pero sí ofrecer un criterio inicial razonable para elegir sin improvisar. En un tema como este, tener una **brújula práctica** vale más que memorizar muchas funciones aisladas.

---

## 7. Practica y cierre

Note: Cerramos con propuestas concretas de **trabajo** para que la ampliación no se quede en teoría y con la idea final que debe permanecer después del tema. El objetivo es salir con **criterio**, no solo con más nombres técnicos en la cabeza.


### 7.1. Propuestas de practica

- Reescribir un programa de `readln()` usando `readlnOrNull()`
- Crear una funcion `pedirEntero()` reutilizable
- Comparar una version con `Scanner` y otra con `readln()`
- Ejecutar un programa recibiendo argumentos

Note: Estas actividades permiten convertir la teoría en **criterio práctico**, que es justo lo que más interesa en clase. Cada una obliga a elegir una herramienta distinta y a justificarla, y esa justificación es casi tan importante como el código.


### 7.2. Idea final que debes recordar

- `7.2` enseña el uso básico de consola
- `7.2.1` ayuda a tomar mejores decisiones en casos menos simples
- Elegir bien entre `readln()`, `Scanner` o `args` también es RA5

Note: El cierre del tema no es memorizar nombres de funciones, sino entender qué posibilidades reales ofrece el lenguaje para la **entrada** y la **salida en consola**. Si esta idea queda clara, el alumnado podrá elegir con criterio entre **`readln()`**, **`Scanner`** o **`args`** según la necesidad real del programa y no por simple inercia.
