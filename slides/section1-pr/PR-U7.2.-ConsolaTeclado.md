# PR-U7.2 - Consola y teclado

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: En esta presentación pasamos de la teoría general de la
**entrada/salida** al caso más cercano: la **consola**. El objetivo es que el
alumnado sepa mostrar mensajes, leer datos, validarlos y cuidar el formato de
salida dentro del **RA5**.


### Índice I

- 1. Consola como canal de entrada y salida
- 2. `print()` y `println()`
- 2.1. Plantillas de cadenas
- 2.2. `System.err`
- 3. Lectura con `readln()` y `readlnOrNull()`

Note: En la primera mitad fijamos la base: qué canales usa una aplicación de
consola y cómo mostrar información. Después introducimos la lectura desde
teclado, que es la operación más habitual en ejercicios iniciales.


### Índice II

- 3.2. Conversión segura de texto a números
- 3.4. Repetir la petición hasta validar
- 4. Formato de salida con interpolación y `format`
- 5. Ejemplo integrador
- 6. Buenas prácticas y resumen

Note: En la segunda mitad nos centramos en la parte más práctica: validar
entrada, formatear resultados y evitar errores frecuentes. La meta no es solo
que el programa funcione, sino que se comunique bien con la persona usuaria.

---

## 1. La consola como canal de entrada y salida

Note: Abrimos con la idea clave del tema: aunque todavía no haya ficheros, ya
estamos haciendo **entrada/salida** cuando un programa habla con la consola.


### 1.1. Tres canales básicos

- **Entrada estándar**: normalmente teclado
- **Salida estándar**: normalmente pantalla
- **Salida de error**: mensajes de fallo o aviso
- En la JVM aparecen como `System.in`, `System.out` y `System.err`

Note: Conviene insistir en que estos tres canales tienen funciones distintas.
Separar salida normal y salida de error ayuda a pensar mejor los programas y a
depurarlos después.

---

## 2. Escribir información en consola

Note: Esta sección enseña a producir salida visible. Es el primer paso para que
un programa guíe a la persona usuaria y muestre resultados comprensibles.


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

Note: La diferencia entre ambas funciones parece pequeña, pero afecta a cómo se
ven los mensajes. Es útil mostrarlo pronto porque luego condiciona la claridad
de los diálogos en consola.


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

Note: Aquí conviene remarcar que la interpolación mejora la legibilidad del
código. Para alumnado que empieza, suele ser más clara que encadenar varias
sumas de cadenas.


### 2.3. Salida de error con `System.err`

- Sirve para diferenciar errores de la salida normal
- Conceptualmente separa resultado correcto y problema detectado
- Es útil para avisos de validación y fallos de entrada

```kotlin
System.err.println("No se ha podido leer la edad")
```

Note: Aunque en algunos terminales no se vea diferente, la separación entre
**salida estándar** y **salida de error** es importante y forma parte del
modelo real de entrada/salida.

---

## 3. Leer datos desde teclado

Note: Leer desde teclado parece simple, pero aquí aparecen muchas decisiones:
qué función usar, cómo convertir texto y cómo evitar excepciones innecesarias.


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

Note: Para ejercicios interactivos sencillos, `readln()` suele ser suficiente.
La versión anulable será útil cuando la entrada pueda agotarse o no dependa del
teclado directamente.


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

Note: Este bloque conecta directamente con la robustez. La idea clave es que la
entrada puede venir mal y que el programa debe anticiparlo en lugar de fallar.


### 3.3. Evita conversiones directas sin validar

- `toInt()` funciona si la entrada es correcta
- Si no lo es, lanza una excepción
- `!!` en ejemplos antiguos también aumenta el riesgo

```kotlin
val numero = readln().toInt()
// o en ejemplos antiguos:
val otro = readLine()!!.toInt()
```

Note: Este es un buen momento para insistir en un criterio de calidad:
**funcionar cuando todo va bien no basta**. Hay que pensar qué pasa cuando la
persona usuaria escribe algo inesperado.


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

Note: Este patrón aparece mucho en actividades de aula. Es simple y enseña a la
vez validación, control de flujo y mensajes de error bien orientados.

---

## 4. Formato de salida

Note: El criterio de evaluación no pide solo "imprimir algo". También importa
que la salida sea clara y fácil de interpretar por quien usa el programa.


### 4.1. Interpolación para mensajes sencillos

- Es suficiente para mensajes cortos y claros
- Resulta muy legible en ejemplos pequeños

```kotlin
val producto = "Teclado"
val precio = 19.95

println("Producto: $producto")
println("Precio: $precio EUR")
```

Note: Para salidas simples no hace falta complicarse. La interpolación resuelve
la mayoría de mensajes de consola de manera directa.


### 4.2. `format` para decimales y columnas

- Permite controlar alineación y número de decimales
- Es útil en tickets, tablas y listados
- Formatos habituales: `%s`, `%d`, `%.2f`, `%n`

```kotlin
val nombre = "Marta"
val nota = 7.456

println("Alumno: %s | Nota: %.2f".format(nombre, nota))
```

Note: Aquí conviene mostrar que `format` no sustituye a la interpolación, sino
que la complementa cuando necesitamos precisión en la presentación.


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

Note: Este ejemplo ayuda a que el alumnado vea por qué el formato importa. La
misma información puede ser mucho más útil si está bien presentada.

---

## 5. Ejemplo integrador

Note: Cerramos con un caso que combina lectura, validación y formato. Es la
traducción directa del tema a un ejercicio típico de clase.


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

Note: El interés del ejemplo está en que combina varias piezas del tema. No es
solo pedir datos: también hay que interpretar qué valores son válidos.


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

Note: Esta slide sirve como transición al resumen. La idea es que el alumnado
salga con una pequeña lista de control para futuros programas de consola.

---

## 6. Resumen

Note: Recuperamos las ideas imprescindibles antes de pasar a la ampliación
`7.2.1` o a los temas de ficheros. El grupo ya debería ver la consola como un
caso concreto del problema general de entrada/salida.


### 6.1. Ideas clave del tema

- La consola permite interacción inmediata con la persona usuaria
- `print()` y `println()` muestran información
- `readln()` y `readlnOrNull()` leen desde teclado
- `toIntOrNull()` y similares evitan muchos errores
- El formato mejora la claridad de la salida

Note: Si estas cinco ideas están claras, el objetivo del tema está cumplido.
Con esta base ya se pueden construir programas sencillos de consola bien
formados y razonablemente robustos.
