## Ejercicio 02: Sistema de Biblioteca

### **Contexto:** 

Imagina que estás diseñando un sistema para una biblioteca que gestiona libros y préstamos. El sistema necesita soportar operaciones para agregar nuevos libros al inventario, 
prestar libros a los usuarios, devolver libros y generar informes de libros prestados.

Inicialmente, se te ocurre crear una clase `Libro` que maneje todo: las propiedades del libro, la gestión del inventario, los préstamos, las devoluciones y la generación de informes. 
Rápidamente te das cuenta de que esto viola el Principio de Responsabilidad Única (SRP).

### **Tarea:** 

1. Refactoriza este diseño inicial para adherir al Principio de Responsabilidad Única. Considera separar las responsabilidades en diferentes clases, por ejemplo, una clase para 
manejar las operaciones del inventario, otra para los préstamos de libros, y otra para generar informes, además de mantener la clase `Libro` centrada en las propiedades del libro.

2. Las características de los libros pueden ser el isbn, titulo, autor y estado (disponible, prestado). El sistema debe permitir agregar, eliminar y comprobar si un libro está disponible (por isbn).

3. En el `main` utiliza las clases para agregar tres libros, prestar dos de ellos, intentar volver a prestar uno ya prestado y finalmente eliminar un libro del inventario. Los datos de los libros son los siguientes:

   - isbn: 123-456-789, título: Kotlin para principiantes y autor: Juan Pérez.
   - isbn: 987-654-321, título: Desarrollo Avanzado con Kotlin y autor: Ana López.
   - isbn: 456-789-123, título: Fundamentos de Programación en Kotlin y autor: Carlos García.

5. Por último, nuestro sistema debe ser capaz de generar los siguientes informes: un informe detallado que incluya todos los libros, un informe con los libros disponibles para préstamo y otro con
   los que actualmente están prestados. Mostrar en el main los tres informes al final del programa.

### Solución Propuesta

A continuación, se detalla una solución posible para el ejercicio propuesto. La idea es dividir las responsabilidades en clases distintas, cada una enfocada en un único aspecto del sistema de la biblioteca.

**Paso 1: Definir la clase `Libro` como una `data class`**

Esta clase contiene solo las propiedades que definen un libro.

```kotlin
data class Libro(val isbn: String, var titulo: String, var autor: String, var estado: EstadoLibro = EstadoLibro.DISPONIBLE)

enum class EstadoLibro {
    DISPONIBLE, PRESTADO
}
```

**Paso 2: Crear una clase `GestorInventario` para manejar el inventario de libros**

Esta clase se encarga de agregar y remover libros del inventario.

```kotlin
class GestorInventario {
    private val libros = mutableListOf<Libro>()

    fun agregarLibro(libro: Libro) {
        libros.add(libro)
        println("Libro agregado: ${libro.titulo}")
    }

    fun removerLibro(libro: Libro) {
        libros.remove(libro)
        println("Libro removido: ${libro.titulo}")
    }

    fun cambiarEstadoLibro(isbn: String, nuevoEstado: EstadoLibro) {
        libros.find { it.isbn == isbn }?.let {
            it.estado = nuevoEstado
            println("Estado cambiado a $nuevoEstado para el libro: ${it.titulo}")
        }
    }

    fun estaDisponible(isbn: String): Boolean {
        return libros.any { it.isbn == isbn && it.estado == EstadoLibro.DISPONIBLE }
    }

    fun listarTodosLosLibros(): List<Libro> = libros

    fun listarLibrosDisponibles(): List<Libro> = libros.filter { it.estado == EstadoLibro.DISPONIBLE }

    fun listarLibrosPrestados(): List<Libro> = libros.filter { it.estado == EstadoLibro.PRESTADO }
}
```

**Paso 3: Crear una clase `SistemaPrestamos` para manejar los préstamos**

Esta clase gestiona el préstamo de libros a los usuarios.

```kotlin
class SistemaPrestamos(private val inventario: GestorInventario) {
    fun prestarLibro(isbn: String) {
        if (inventario.estaDisponible(isbn)) {
            inventario.cambiarEstadoLibro(isbn, EstadoLibro.PRESTADO)
            println("Libro prestado con ISBN: $isbn")
        } else {
            println("El libro con ISBN $isbn no está disponible para préstamo.")
        }
    }

    fun devolverLibro(isbn: String) {
        inventario.cambiarEstadoLibro(isbn, EstadoLibro.DISPONIBLE)
        println("Libro devuelto con ISBN: $isbn")
    }
}
```

**Paso 4: Crear una clase `GeneradorInformes` para generar informes de libros**

Esta clase se encarga de generar informes relacionados con los libros, como los libros más prestados.

```kotlin
class GeneradorInformes(private val inventario: GestorInventario) {
    fun generarInformeDetalladoCompleto() {
        println("\nInforme Detallado Completo de la Biblioteca:")
        inventario.listarTodosLosLibros().forEach { libro ->
            println("- ${libro.titulo} (ISBN: ${libro.isbn}) - Estado: ${libro.estado}")
        }
    }

    fun generarInformeLibrosDisponibles() {
        println("\nInforme de Libros Disponibles para Préstamo:")
        inventario.listarLibrosDisponibles().forEach { libro ->
            println("- ${libro.titulo} (ISBN: ${libro.isbn})")
        }
    }

    fun generarInformeLibrosPrestados() {
        println("\nInforme de Libros Actualmente Prestados:")
        inventario.listarLibrosPrestados().forEach { libro ->
            println("- ${libro.titulo} (ISBN: ${libro.isbn})")
        }
    }
}
```

**Implementación en el `main`:**

```kotlin
fun main() {
    val libro1 = Libro("123-456-789", "Kotlin para principiantes", "Juan Pérez")
    val libro2 = Libro("987-654-321", "Desarrollo Avanzado con Kotlin", "Ana López")
    val libro3 = Libro("456-789-123", "Fundamentos de Programación en Kotlin", "Carlos García")

    val gestorInventario = GestorInventario()
    gestorInventario.agregarLibro(libro1)
    gestorInventario.agregarLibro(libro2)
    gestorInventario.agregarLibro(libro3)

    val sistemaPrestamos = SistemaPrestamos(gestorInventario)

    println("Prestar libros:")
    sistemaPrestamos.prestarLibro(libro1.isbn) // Libro 1 prestado
    sistemaPrestamos.prestarLibro(libro2.isbn) // Libro 2 prestado

    println("\nIntentar prestar un libro ya prestado:")
    sistemaPrestamos.prestarLibro(libro1.isbn) // Intento fallido, libro 1 ya está prestado

    println("\nDevolver un libro y luego eliminarlo:")
    sistemaPrestamos.devolverLibro(libro2.isbn) // Libro 2 devuelto
    gestorInventario.removerLibro(libro2) // Libro 2 eliminado del inventario

    val generadorInformes = GeneradorInformes(gestorInventario)
    generadorInformes.generarInformeDetalladoCompleto() // Genera un informe detallado de todos los libros
    generadorInformes.generarInformeLibrosDisponibles() // Genera un informe de los libros disponibles
    generadorInformes.generarInformeLibrosPrestados() // Genera un informe de los libros prestados
}
```

Esta solución demuestra cómo aplicar el Principio de Responsabilidad Única en un sistema de biblioteca. Cada clase tiene una única razón para cambiar, lo que facilita 
el mantenimiento y la extensión del sistema.
