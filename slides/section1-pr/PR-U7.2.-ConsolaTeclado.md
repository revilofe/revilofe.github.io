# PR-U7.2 - Consola y teclado

Note: En esta presentación trabajamos la **consola** y el **teclado** como primeros mecanismos reales de **entrada** y **salida**. La idea importante es que un programa ya puede comunicarse con la persona usuaria, pedir datos y mostrar resultados mucho antes de empezar a guardar información en ficheros.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Esta parte de la unidad 7 sirve para fijar la base de la **E/S básica** sobre la que se apoyará todo lo demás. Vamos a distinguir **entrada estándar**, **salida estándar** y **salida de error**, y a ver cómo Kotlin nos permite pedir datos, validarlos y mostrarlos con claridad.

---

## Índice

Note: En esta presentación pasamos de la teoría general de la **entrada/salida** al caso más cercano y más visible: la **consola**. El objetivo es que el alumnado sepa mostrar mensajes, leer datos, validarlos y cuidar el formato de salida dentro del **RA5**, entendiendo que comunicar bien también es parte de programar.


### Índice I

- 1. Consola como canal de entrada y salida
- 2. `print()` y `println()`
- 2.1. Plantillas de cadenas
- 2.2. `System.err`
- 3. Lectura con `readln()` y `readlnOrNull()`

Note: En la primera mitad fijamos la base que toda aplicación de **consola** necesita: qué **canales** usa y cómo se muestra la información de forma comprensible. Después introducimos la lectura desde **teclado**, que es la operación más habitual en los ejercicios iniciales y la que abre la puerta a la **interacción** real.


### Índice II

- 3.2. Conversión segura de texto a números
- 3.4. Repetir la petición hasta validar
- 4. Formato de salida con interpolación y `format`
- 5. Ejemplo integrador
- 6. Buenas prácticas y resumen

Note: En la segunda mitad nos centramos en la parte más práctica y más cercana a los errores reales de aula: **validar** entrada, **formatear** resultados y evitar fallos frecuentes. La meta no es solo que el programa funcione, sino que se comunique bien con la persona usuaria y reaccione con cierta robustez.

---

## 1. La consola como canal de entrada y salida

Note: Abrimos con la idea clave del tema: aunque todavía no haya ficheros, ya estamos haciendo **entrada/salida** cuando un programa habla con la **consola**. Esto ayuda a que el alumnado vea la consola como un caso concreto del problema general de intercambio de datos.


### 1.1. Tres canales básicos

- **Entrada estándar**: normalmente teclado
- **Salida estándar**: normalmente pantalla
- **Salida de error**: mensajes de fallo o aviso
- En la JVM aparecen como `System.in`, `System.out` y `System.err`

Note: Conviene insistir en que estos tres canales tienen funciones distintas y no están ahí por capricho. Separar **salida normal** y **salida de error** ayuda a pensar mejor los programas, a guiarlos mejor y a depurarlos después con más orden.

---

## 2. Escribir información en consola

Note: Esta sección enseña a producir **salida visible**, que es el primer paso para que un programa pueda guiar a la persona usuaria. Un programa que no explica qué pide ni qué ha obtenido puede funcionar técnicamente, pero sigue estando mal comunicado.


### 2.1. `print()` y `println()`

- `print()` escribe sin salto de línea final
- `println()` añade salto de línea al terminar
- `\n` permite insertar un salto dentro del texto

```kotlin
fun main() {
    print("Hola")
    print(" ")
    println("mundo")
    println("Segunda linea")
}
```

Note: La diferencia entre **`print()`** y **`println()`** parece pequeña, pero afecta directamente a cómo se ven los mensajes y a la claridad del diálogo en **consola**. Conviene mostrarla pronto porque muchos programas sencillos se vuelven confusos precisamente por no controlar bien esos **saltos de línea**.


### 2.2. Plantillas de cadenas

- Kotlin permite interpolar variables con `$variable`
- También admite expresiones con `${...}`
- Suele ser más legible que concatenar con `+`

```kotlin
val nombre = "Alicia"
val nota = 8.5

println("Alumno: $nombre")
println("El doble es ${nota * 2}")
```

Note: Aquí conviene remarcar que la **interpolación** mejora mucho la legibilidad del código y también del pensamiento del alumnado. Para quien empieza, suele ser bastante más clara que encadenar varias sumas de cadenas y permite concentrarse en el mensaje en lugar de en la sintaxis.


### 2.3. Salida de error con `System.err`

- Sirve para diferenciar errores de la salida normal
- Conceptualmente separa resultado correcto y problema detectado
- Es útil para avisos de validación y fallos de entrada

```kotlin
System.err.println("No se ha podido leer la edad")
```

Note: Aunque en algunos terminales no se vea una diferencia llamativa, la separación entre **salida estándar** y **salida de error** es importante y forma parte del modelo real de **entrada/salida**. Quiero que el alumnado entienda que un mensaje de error no es solo "otro `println`", sino una salida con un propósito distinto.

---

## 3. Leer datos desde teclado

Note: Leer desde teclado parece simple cuando se mira por encima, pero aquí aparecen muchas decisiones reales: qué función usar, cómo convertir **texto** a otros tipos y cómo evitar **excepciones** innecesarias. Este bloque es el que transforma una lectura ingenua en una lectura algo más robusta.


### 3.1. Lectura básica de texto

- `readln()` devuelve un `String`
- `readlnOrNull()` devuelve `String?`
- Ambas leen una línea completa desde entrada estándar

```kotlin
fun main() {
    print("Introduce tu nombre: ")
    val nombre = readln()
    println("Hola, $nombre")
}
```

Note: Para ejercicios interactivos sencillos, `readln()` suele ser suficiente y además es muy fácil de explicar en voz alta. La versión anulable empieza a tener sentido cuando la entrada puede agotarse o cuando ya no depende directamente del **teclado**, y ese matiz conviene dejarlo bien sembrado.


### 3.2. Convertir texto a números con seguridad

- El teclado siempre entrega **texto**
- Después hay que convertirlo al tipo necesario
- `toIntOrNull()` evita excepciones al validar
- Existen variantes como `toDoubleOrNull()`

```kotlin
print("Introduce tu edad: ")
val edad = readln().toIntOrNull()

if (edad != null) {
    println("Tienes $edad anios")
} else {
    System.err.println("La edad no es valida")
}
```

Note: Este bloque conecta directamente con la idea de **robustez**, que es una palabra importante aunque todavía estemos en ejercicios básicos. La entrada puede venir mal y el programa debe anticiparlo, porque programar no es solo pensar en el caso ideal, sino también en los errores normales de la persona usuaria.


### 3.3. Evita conversiones directas sin validar

- `toInt()` funciona si la entrada es correcta
- Si no lo es, lanza una excepción
- `!!` en ejemplos antiguos también aumenta el riesgo

```kotlin
val numero = readln().toInt()
// o en ejemplos antiguos:
val otro = readLine()!!.toInt()
```

Note: Este es un buen momento para insistir en un criterio de calidad que el alumnado debe empezar a interiorizar: **funcionar cuando todo va bien no basta**. También hay que pensar qué ocurre cuando la persona usuaria escribe algo inesperado, se equivoca o introduce un formato que el programa no esperaba.


### 3.4. Repetir la petición hasta obtener un dato valido

- Un patrón frecuente es pedir, validar y repetir
- Se puede resolver con un bucle `while`
- Mejora la experiencia de uso del programa

```kotlin
var cantidad: Int? = null

while (cantidad == null) {
    print("Introduce una cantidad entera: ")
    cantidad = readln().toIntOrNull()
    if (cantidad == null) {
        System.err.println("Dato no valido. Intentalo de nuevo.")
    }
}
```

Note: Este patrón aparece muchísimo en las actividades de aula porque es simple, útil y muy formativo. Enseña a la vez **validación**, **control de flujo** y mensajes de error bien orientados, y además muestra cómo un programa puede insistir sin romperse.

---

## 4. Formato de salida

Note: El criterio de evaluación no pide solo "imprimir algo", sino comunicarlo bien y con intención. También importa que la **salida** sea clara, legible y fácil de interpretar por quien usa el programa, porque un programa oscuro sigue siendo un programa mal resuelto.


### 4.1. Interpolación para mensajes sencillos

- Es suficiente para mensajes cortos y claros
- Resulta muy legible en ejemplos pequeños

```kotlin
val producto = "Teclado"
val precio = 19.95

println("Producto: $producto")
println("Precio: $precio EUR")
```

Note: Para salidas simples no hace falta complicarse ni introducir mecanismos más pesados antes de tiempo. La **interpolación** resuelve la mayoría de mensajes de consola de manera directa y deja el código bastante más limpio y fácil de leer.


### 4.2. `format` para decimales y columnas

- Permite controlar alineación y número de decimales
- Es útil en tickets, tablas y listados
- Formatos habituales: `%s`, `%d`, `%.2f`, `%n`

```kotlin
val nombre = "Marta"
val nota = 7.456

println("Alumno: %s | Nota: %.2f".format(nombre, nota))
```

Note: Aquí conviene mostrar que `format` no sustituye a la **interpolación**, sino que la complementa cuando necesitamos más precisión en la presentación. La idea es que el alumnado vea que hay una escala de herramientas y que cada una encaja mejor según el nivel de control que haga falta.


### 4.3. Tabla sencilla en consola

```kotlin
val articulos = listOf(
    "Cuaderno" to 2.5,
    "Boligrafo" to 1.2,
    "Mochila" to 24.95
)

println("%-12s | %8s".format("Articulo", "Precio"))
println("-----------------------------")
for ((articulo, precio) in articulos) {
    println("%-12s | %8.2f EUR".format(articulo, precio))
}
```

- Mejora la legibilidad respecto a una salida desordenada
- Hace visible el valor del formato como parte del resultado

Note: Este ejemplo ayuda a que el alumnado vea por qué el **formato** importa de verdad y no es solo maquillaje. La misma información puede ser mucho más útil si está bien presentada, especialmente cuando hay números, resultados o datos que deben leerse con rapidez.

---

## 5. Ejemplo integrador

Note: Cerramos con un caso que combina **lectura**, **validación** y **formato** en un único ejercicio reconocible. Es la traducción directa del tema a una actividad típica de clase y por eso sirve muy bien como modelo de repaso.


### 5.1. Ticket de compra en consola

```kotlin
print("Nombre del producto: ")
val producto = readln()

print("Unidades: ")
val unidades = readln().toIntOrNull()

print("Precio unitario: ")
val precio = readln().toDoubleOrNull()
```

- Lee datos desde teclado
- Obliga a validar cantidades y precios
- Prepara una salida con formato claro

Note: El interés del ejemplo está en que combina varias piezas del tema dentro de una misma situación. No es solo pedir datos, sino también interpretar qué valores son **válidos**, reaccionar si no lo son y mostrar una salida final bien presentada.


### 5.2. Salida final y buenas practicas

```kotlin
if (unidades == null || precio == null) {
    System.err.println("No se puede generar el ticket.")
    return
}

val total = unidades * precio
println("Total: %.2f EUR".format(total))
```

- Muestra mensajes claros antes de pedir cada dato
- Valida antes de usar el valor leído
- Usa `System.err` para errores
- Separa, si el programa crece, lógica y presentación

Note: Esta slide sirve como transición al **resumen** y como pequeña **lista de control** para futuros programas de consola. Quiero que el alumnado salga con criterios muy concretos sobre qué revisar cuando construya un programa **interactivo** sencillo y tenga que cuidar tanto la **entrada** como la **salida**.

---

## 6. Resumen

Note: Recuperamos aquí las ideas imprescindibles antes de pasar a la ampliación `7.2.1` o a los temas de ficheros para que no se pierda el hilo. A estas alturas el grupo ya debería ver la **consola** como un caso concreto del problema general de **entrada/salida**.


### 6.1. Ideas clave del tema

- La consola permite interacción inmediata con la persona usuaria
- `print()` y `println()` muestran información
- `readln()` y `readlnOrNull()` leen desde teclado
- `toIntOrNull()` y similares evitan muchos errores
- El formato mejora la claridad de la salida

Note: Si estas cinco ideas están claras, el objetivo del tema está cumplido y la base ya es buena. Con ella el alumnado puede construir programas sencillos de **consola** bien formados, más legibles y razonablemente **robustos** para el nivel de la unidad.
