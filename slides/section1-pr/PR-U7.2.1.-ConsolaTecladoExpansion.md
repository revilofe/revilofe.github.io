# PR-U7.2.1 - Consola y teclado: ampliacion

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: Esta presentación amplía `7.2`. No sustituye los fundamentos, sino que
aclara los casos que suelen generar dudas cuando el programa deja de ser tan
simple: final de entrada, `Scanner`, funciones auxiliares y argumentos.


### Índice I

- 1. `readln()`, `readlnOrNull()` y `readLine()`
- 2. Fin de entrada y `EOF`
- 3. `Scanner` desde Kotlin
- 3.1. El problema del salto de linea

Note: Primero comparamos las funciones de lectura más habituales y después
introducimos el concepto de **fin de entrada**, que cambia bastante el diseño
de algunos programas de consola.


### Índice II

- 4. Funciones auxiliares para pedir datos
- 5. Argumentos de linea de comandos
- 6. Comparativa rapida de mecanismos
- 7. Propuestas de practica y cierre

Note: La segunda parte tiene una orientación más de diseño: cómo reutilizar la
validación, cuándo usar argumentos y cómo elegir el mecanismo más adecuado en
cada situación.

---

## 1. `readln()`, `readlnOrNull()` y `readLine()`

Note: El alumnado suele ver estas tres opciones en materiales distintos. Por
eso conviene compararlas de forma explícita y explicar cuándo interesa cada una.


### 1.1. Comparativa rapida

| Funcion | Devuelve | Comportamiento |
| --- | --- | --- |
| `readln()` | `String` | Espera una linea y falla si no hay entrada |
| `readlnOrNull()` | `String?` | Devuelve `null` si no quedan datos |
| `readLine()` | `String?` | Variante historica frecuente en codigo antiguo |
<!-- .element.table: style="font-size:70%;" -->

Note: La idea clave no es memorizar la tabla, sino entender la diferencia entre
una lectura que **asume entrada disponible** y otra que puede detectar su
agotamiento sin lanzar una excepción.


### 1.2. Cuando usar cada una

- `readln()` en programas interactivos sencillos
- `readlnOrNull()` si la entrada puede agotarse
- `readLine()` para reconocer codigo heredado

```kotlin
print("Nombre: ")
val nombre = readln()
println("Hola, $nombre")
```

Note: En contexto didáctico, `readln()` suele ser la opción más clara. La
versión anulable empieza a cobrar sentido cuando la entrada no la controla
directamente la persona usuaria.

---

## 2. Fin de entrada y `EOF`

Note: Esta sección introduce un matiz importante: la entrada estándar también
puede terminar. Entender esto evita muchos errores conceptuales.


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

Note: Este patrón es muy útil para leer múltiples líneas hasta que la entrada
se agote. Conviene remarcar que no depende de un número fijo de repeticiones.

---

## 3. Uso de `Scanner` desde Kotlin

Note: `Scanner` no es imprescindible en la unidad, pero aparece en mucho
material Java. Por eso merece una explicación breve y práctica.


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

Note: Aquí interesa que el alumnado vea `Scanner` como una opción posible, no
como la herramienta obligatoria. En Kotlin moderno, muchas veces `readln()`
resulta más sencilla de explicar y mantener.


### 3.2. El problema del salto de linea

- `nextInt()` o `nextDouble()` no consumen el fin de linea completo
- La siguiente llamada a `nextLine()` puede devolver vacio
- Suele resolverse con una llamada adicional a `nextLine()`

```kotlin
val edad = scanner.nextInt()
scanner.nextLine()
val ciudad = scanner.nextLine()
```

Note: Este es uno de los errores más típicos con `Scanner`. Es importante
explicarlo bien porque, si no, parece que el programa "lee mal" sin motivo.


### 3.3. Cuando compensa usar `Scanner`

- Si el material base ya esta en Java
- Si quieres leer tokens separados por espacios
- Si necesitas interoperar con ejemplos ya construidos
- En ejercicios normales, `readln()` suele ser mas claro

Note: La recomendación práctica para esta unidad es clara: conocer `Scanner`,
pero priorizar `readln()` y conversiones seguras cuando el objetivo sea la
claridad didáctica.

---

## 4. Funciones auxiliares para pedir datos

Note: Cuando un programa crece, repetir siempre el mismo patrón de validación
ensucia el código. Aquí aparece la idea de encapsular la lectura en funciones.


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

Note: Esta función es un buen ejemplo de abstracción útil. El alumnado ve que
la validación no tiene por qué repetirse manualmente en cada punto del programa.


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

Note: Aquí conviene destacar el patrón, no memorizar la función concreta. La
decisión de diseño importante es encapsular comportamientos repetidos.

---

## 5. Argumentos de linea de comandos

Note: No toda la entrada llega desde teclado durante la ejecución. A veces los
datos se entregan al arrancar el programa.


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

Note: El contraste importante aquí es entre datos **pedidos en tiempo de
ejecución** y datos **pasados al inicio**. Ambos mecanismos forman parte del
trabajo con programas de consola, pero no cumplen la misma función.


### 5.2. Teclado frente a argumentos

- **Teclado**: entrada durante la ejecución
- **Argumentos**: entrada al lanzar el programa
- El teclado es más interactivo
- Los argumentos son más cómodos para automatizar

Note: Esta comparación ayuda a elegir mejor el mecanismo según el contexto. No
se trata de cuál es "mejor", sino de cuál encaja mejor con la necesidad real.

---

## 6. Mini comparativa de mecanismos

Note: Esta slide resume la toma de decisiones de todo el tema. Es útil como
referencia rápida antes de pasar a práctica.


### 6.1. Que mecanismo elegir

| Situacion | Opcion recomendable |
| --- | --- |
| Programa interactivo sencillo | `readln()` |
| Entrada que puede agotarse | `readlnOrNull()` |
| Codigo heredado | `readLine()` |
| Interoperabilidad con Java | `Scanner` |
| Parametros al arrancar | `args` |
<!-- .element.table: style="font-size:70%;" -->

Note: Esta tabla no pretende ser absoluta, pero sí ofrecer un criterio inicial
razonable para elegir sin improvisar.

---

## 7. Practica y cierre

Note: Cerramos con propuestas concretas de trabajo y con la idea final que debe
quedar clara después de la ampliación.


### 7.1. Propuestas de practica

- Reescribir un programa de `readln()` usando `readlnOrNull()`
- Crear una funcion `pedirEntero()` reutilizable
- Comparar una version con `Scanner` y otra con `readln()`
- Ejecutar un programa recibiendo argumentos

Note: Estas actividades permiten convertir la teoría en criterio práctico. Cada
una obliga a elegir una herramienta distinta y justificarla.


### 7.2. Idea final que debes recordar

- `7.2` enseña el uso básico de consola
- `7.2.1` ayuda a tomar mejores decisiones en casos menos simples
- Elegir bien entre `readln()`, `Scanner` o `args` también es RA5

Note: El cierre del tema no es memorizar nombres de funciones, sino entender
qué posibilidades reales ofrece el lenguaje para la entrada y salida en consola.
