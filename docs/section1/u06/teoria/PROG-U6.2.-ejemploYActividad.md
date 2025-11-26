---
title: "UD 6 - 6.2 Ejemplo: Sistema de Gestión de Biblioteca de Medios"
description: kotlin
summary: kotlin
authors:
    - Diego Cano
date: 2024-02-12
icon: "material/file-document-outline"
permalink: /prog/unidad6/6.2
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 6.2. Ejemplo: Sistema de Gestión de Biblioteca de Medios.

Imaginemos un sistema que gestiona diferentes tipos de medios en una biblioteca, como libros y revistas. Para este propósito, definiremos una clase base `Medio` y dos subclases `Libro` y `Revista`.

Este ejemplo involucra una jerarquía de clases, incluyendo múltiples niveles de herencia y la implementación de interfaces para gestionar una colección de artículos de una biblioteca digital. 
Esta biblioteca gestionará libros, revistas, y películas, pero también incluirá funcionalidades para buscar y listar los artículos disponibles por tipo y categoría.

### 1. Jerarquía de Clases

1. **Clase Base `Articulo`**: Una clase abstracta con propiedades comunes como `titulo` y `autor`.
2. **Subclases `Libro`, `Revista`, y `Pelicula`**: Clases derivadas que extienden `Articulo`.
3. **Interfaz `Buscable`**: Define métodos para buscar artículos por título y listar artículos por categoría.

### 2. Implementación

```kotlin
// Clase base abstracta para artículos
abstract class Articulo(val titulo: String, val autor: String) {
    abstract fun descripcion()
}

// Interfaz para funcionalidades de búsqueda
interface Buscable {
    fun buscarPorTitulo(titulo: String): List<Articulo>
    fun listarPorCategoria(categoria: String): List<Articulo>
}

// Subclase para libros
class Libro(titulo: String, autor: String, val paginas: Int, val categoria: String) : Articulo(titulo, autor) {
    override fun descripcion() {
        println("Libro: '$titulo' por $autor, $paginas páginas, Categoría: $categoria")
    }
}

// Subclase para revistas
class Revista(titulo: String, autor: String, val edicion: String, val categoria: String) : Articulo(titulo, autor) {
    override fun descripcion() {
        println("Revista: '$titulo' por $autor, Edición: $edicion, Categoría: $categoria")
    }
}

// Subclase para películas
class Pelicula(titulo: String, autor: String, val duracion: Int, val genero: String, val categoria: String) : Articulo(titulo, autor) {
    override fun descripcion() {
        println("Película: '$titulo' dirigida por $autor, Duración: $duracion minutos, Género: $genero, Categoría: $categoria")
    }
}

// Implementación de la interfaz Buscable
class BibliotecaDigital(val articulos: MutableList<Articulo>) : Buscable {
    override fun buscarPorTitulo(titulo: String): List<Articulo> =
        articulos.filter { it.titulo.contains(titulo, ignoreCase = true) }

    override fun listarPorCategoria(categoria: String): List<Articulo> =
        articulos.filter { it is Libro && it.categoria == categoria || 
                            it is Revista && it.categoria == categoria || 
                            it is Pelicula && it.categoria == categoria }
    
    fun mostrarDescripcionArticulos() {
        articulos.forEach { it.descripcion() }
    }
}

// Demostración de uso
fun main() {
    val biblioteca = BibliotecaDigital(mutableListOf(
        Libro("1984", "George Orwell", 328, "Distopía"),
        Revista("National Geographic", "Varios", "Enero 2024", "Naturaleza"),
        Pelicula("Interstellar", "Christopher Nolan", 169, "Ciencia Ficción", "Aventura")
    ))

    biblioteca.mostrarDescripcionArticulos()
    println("\nBuscando por título '1984':")
    biblioteca.buscarPorTitulo("1984").forEach { it.descripcion() }

    println("\nListando artículos en la categoría 'Aventura':")
    biblioteca.listarPorCategoria("Aventura").forEach { it.descripcion() }
}
```

### 3. Actividad Propuesta

**Objetivo**: Ampliar la `BibliotecaDigital` para incluir funcionalidades de préstamo de artículos. Cada artículo debe tener un estado que indique si está disponible para préstamo. 
Los usuarios pueden prestar y devolver artículos, cambiando su estado de disponibilidad.

### 4. Instrucciones

1. Añade una propiedad `disponible` a la clase `Articulo` para indicar la disponibilidad.
2. Implementa métodos `prestarArticulo(titulo: String)` y `devolverArticulo(titulo: String)` en `BibliotecaDigital` que cambien el estado de disponibilidad del artículo correspondiente.
3. Asegúrate de manejar casos donde el artículo no esté disponible para préstamo o ya haya sido prestado.
4. Modifica `main` para demostrar las funcionalidades de préstamo y devolución.

### 5. Implementación de una posible solución.

Esta actividad proporciona una oportunidad para explorar conceptos avanzados de herencia y la implementación de interfaces, al tiempo que se introducen nuevas funcionalidades que reflejan 
operaciones del mundo real en sistemas de gestión de bibliotecas.

Para completar la actividad propuesta y proporcionar una solución detallada, vamos a expandir la funcionalidad de la `BibliotecaDigital` para incluir el préstamo de artículos,
modificando la clase base `Articulo` para añadir una propiedad que indique su disponibilidad y actualizando la lógica de la biblioteca para gestionar el préstamo y la devolución de artículos.

### NO SIGAS...

***IMPORTANTE***

```
Aquí deberías parar e intentar tu la solución antes de seguir leyendo...
```

***IMPORTANTE***


La solución impica modificar la clase `Articulo` para incluir la propiedad `disponible` y actualizar `BibliotecaDigital` con los métodos de préstamo y devolución. 
Después, en `main`, se demostrarían estas nuevas funcionalidades prestando un libro y luego devolviéndolo, mostrando el cambio en su disponibilidad.


#### 5.1. Paso 1: Modificar la Clase Base `Articulo`

Agregaremos una propiedad `disponible` a la clase `Articulo` para indicar si el artículo está disponible para préstamo.

```kotlin
abstract class Articulo(val titulo: String, val autor: String, var disponible: Boolean = true) {
    abstract fun descripcion()
    fun cambiarDisponibilidad() { disponible = !disponible }
}
```

#### 5.2. Paso 2: Implementar Métodos de Préstamo y Devolución en `BibliotecaDigital`

Actualizaremos `BibliotecaDigital` para incluir métodos que permitan prestar y devolver artículos, modificando su estado de disponibilidad.

```kotlin
class BibliotecaDigital(val articulos: MutableList<Articulo>) : Buscable {
    // Métodos existentes

    fun prestarArticulo(titulo: String) {
        articulos.find { it.titulo == titulo && it.disponible }?.let {
            it.cambiarDisponibilidad()
            println("Artículo prestado: ${it.titulo}")
        } ?: println("Artículo no disponible para préstamo: $titulo")
    }
 
    fun devolverArticulo(titulo: String) {
        articulos.find { it.titulo == titulo && !it.disponible }?.let {
            it.cambiarDisponibilidad()
            println("Artículo devuelto: ${it.titulo}")
        } ?: println("Error al intentar devolver el artículo: $titulo")
    }
}
```

#### 5.3. Paso 3: Demostración de Préstamo y Devolución

Finalmente, modificaremos la función `main` para demostrar las funcionalidades de préstamo y devolución, asegurándonos de que los artículos cambian su estado de disponibilidad adecuadamente.

```kotlin
fun main() {
    val biblioteca = BibliotecaDigital(mutableListOf(
        Libro("1984", "George Orwell", 328, "Distopía"),
        Revista("National Geographic", "Varios", "Enero 2024", "Naturaleza"),
        Pelicula("Interstellar", "Christopher Nolan", 169, "Ciencia Ficción", "Aventura")
    ))

    println("Estado inicial de los artículos:")
    biblioteca.mostrarDescripcionArticulos()

    // Prestar un artículo
    println("\nPrestar el libro '1984':")
    biblioteca.prestarArticulo("1984")

    // Intentar prestar el mismo artículo de nuevo
    println("\nIntentar prestar el libro '1984' otra vez:")
    biblioteca.prestarArticulo("1984")

    // Devolver el artículo
    println("\nDevolver el libro '1984':")
    biblioteca.devolverArticulo("1984")

    // Verificar el estado final de los artículos
    println("\nEstado final de los artículos:")
    biblioteca.mostrarDescripcionArticulos()
}
```

Este flujo demuestra cómo los artículos pueden ser prestados y devueltos, modificando su disponibilidad en la biblioteca digital. Al prestar el libro "1984", se marca como no disponible, y al intentar 
prestarlo nuevamente, se muestra un mensaje indicando que el artículo no está disponible para préstamo. Al devolver el libro, su disponibilidad se restablece.
