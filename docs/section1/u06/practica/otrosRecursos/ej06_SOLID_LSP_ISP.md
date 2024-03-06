## Ejercicio 06: Elementos de la Biblioteca

### **Contexto:**

El siguiente código ilustra una violación del Principio de Sustitución de Liskov (LSP) utilizando una clase abstracta que incluye un método que `ElementoDeReferencia` no puede implementar adecuadamente.

```kotlin
abstract class ElementoBiblioteca {
    abstract fun mostrarInfo()
    abstract fun catalogar()
    abstract fun mostrarUbicacion()
    abstract fun prestar()
}

class Libro : ElementoBiblioteca() {
    override fun mostrarInfo() {
        println("Libro: Información detallada.")
    }

    override fun catalogar() {
        println("Libro: Catalogado en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Libro: Disponible en la sección de literatura.")
    }

    override fun prestar() {
        println("Libro: Prestado a un lector.")
    }
}

class Revista : ElementoBiblioteca() {
    override fun mostrarInfo() {
        println("Revista: Información detallada.")
    }

    override fun catalogar() {
        println("Revista: Catalogada en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Revista: Disponible en la sección de revistas.")
    }

    override fun prestar() {
        println("Revista: Prestada a un lector.")
    }
}

class ElementoDeReferencia : ElementoBiblioteca() {
    override fun mostrarInfo() {
        println("Elemento de Referencia: Información detallada.")
    }

    override fun catalogar() {
        println("Elemento de Referencia: Catalogado en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Elemento de Referencia: Disponible en la sección de referencia.")
    }

    override fun prestar() {
        throw UnsupportedOperationException("Los elementos de referencia no se pueden prestar.")
    }
}
```

El programa principal sería de la siguiente manera:

```kotlin
fun main() {
    val elementos: List<ElementoBiblioteca> = listOf(Libro(), Revista(), ElementoDeReferencia())

    elementos.forEach { elemento ->
        try {
            elemento.prestar()
        } catch (e: UnsupportedOperationException) {
            println(e.message)
        }
    }
}
```

### **Tarea:**

- Refactoriza el código para cumplir el principio SOLID de Sustitución de Liskov (LSP)
- Responde a la siguiente pregunta: ¿Qué otro principio SOLID estamos aplicando a nuestra solución para hacer cumplir el principio de Sustitución de Liskov?

### **Solución refactorizada:**

Para solucionar la violación del LSP y seguir el principio correctamente, podemos eliminar el método `prestar()` de la clase abstracta `ElementoBiblioteca` y crear una interfaz separada `Prestable` para los elementos que 
pueden ser prestados. `ElementoDeReferencia` no implementará esta interfaz, resolviendo así el problema.

```kotlin
abstract class ElementoBiblioteca {
    abstract fun mostrarInfo()
    abstract fun catalogar()
    abstract fun mostrarUbicacion()
}
```

```kotlin
interface Prestable {
    fun prestar()
}
```

```kotlin
class Libro : ElementoBiblioteca(), Prestable {
    override fun mostrarInfo() {
        println("Libro: Información detallada.")
    }

    override fun catalogar() {
        println("Libro: Catalogado en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Libro: Disponible en la sección de literatura.")
    }

    override fun prestar() {
        println("Libro prestado.")
    }
}
```

```kotlin
class Revista : ElementoBiblioteca(), Prestable {
    override fun mostrarInfo() {
        println("Revista: Información detallada.")
    }

    override fun catalogar() {
        println("Revista: Catalogada en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Revista: Disponible en la sección de revistas.")
    }

    override fun prestar() {
        println("Revista prestada.")
    }
}
```

```kotlin
class ElementoDeReferencia : ElementoBiblioteca() {
    override fun mostrarInfo() {
        println("Elemento de Referencia: Información detallada.")
    }

    override fun catalogar() {
        println("Elemento de Referencia: Catalogado en el sistema de la biblioteca.")
    }

    override fun mostrarUbicacion() {
        println("Elemento de Referencia: Disponible en la sección de referencia.")
    }
}
```

Demostración de uso en el programa principal:

```kotlin
fun main() {
    val prestables: List<Prestable> = listOf(Libro(), Revista())
    prestables.forEach { prestable ->
        prestable.prestar()
    }

    val elementos: List<ElementoBiblioteca> = listOf(Libro(), Revista(), ElementoDeReferencia())
    elementos.forEach { elemento ->
        elemento.mostrarInfo()
        elemento.catalogar()
        elemento.mostrarUbicacion()
        println()
    }
}
```

En este caso, solo los elementos que implementan Prestable se incluyen en la lista de objetos a prestar, eliminando la posibilidad de un error en tiempo de ejecución relacionado con intentar prestar un ElementoDeReferencia. 
Todos los elementos, sin embargo, pueden mostrar su información, ser catalogados, y mostrar su ubicación, lo cual demuestra el uso seguro y conforme al LSP de las abstracciones definidas.

Este enfoque garantiza que el comportamiento de nuestro programa sea predecible y robusto, eliminando la necesidad de controles de errores específicos para casos que no deberían ocurrir si se sigue el LSP correctamente. 
Al adherirnos al principio, facilitamos la extensión y mantenimiento del sistema al tiempo que evitamos la propagación de errores en tiempo de ejecución.

#### Respuesta a la pregunta:

Este ejercicio también aborda la solución del Principio de Sustitución de Liskov (LSP) aplicando el Principio de Segregación de la Interfaz (ISP), incluso cuando utilizamos una clase abstracta en combinación con interfaces. 
Aunque la implementación específica involucre tanto clases abstractas como interfaces, el concepto subyacente de ISP aún se aplica y es relevante para nuestra solución.

El ISP establece que ninguna clase debería verse forzada a implementar interfaces que no utiliza. En el caso de nuestra solución refactorizada:

* Para Libro y Revista: estas clases implementan tanto la clase abstracta `ElementoBiblioteca` como la interfaz `Prestable`. Esto se alinea con el `ISP` porque estas clases realmente necesitan y utilizan ambas abstracciones;
  la interfaz `Prestable` para la acción de prestar y la clase abstracta `ElementoBiblioteca` para otras operaciones comunes de biblioteca.

* Para `ElementoDeReferencia`: esta clase solo implementa la clase abstracta `ElementoBiblioteca` y no la interfaz Prestable, ya que no se supone que los elementos de referencia se presten.
  Esto cumple con el `ISP`, ya que ElementoDeReferencia no está forzado a implementar métodos de la interfaz Prestable que no va a utilizar.

Aunque el principio se llama "Segregación de la Interfaz", el espíritu del principio es evitar que las clases tengan que implementar comportamientos que no usan, independientemente de si estos comportamientos están definidos 
en interfaces o clases abstractas. En este contexto, segregamos las responsabilidades de prestar (Prestable) de otras operaciones de elementos de la biblioteca (ElementoBiblioteca), lo cual permite una mejor organización del 
código, facilita su mantenibilidad y extensión, y asegura que las implementaciones específicas de nuestras clases se adhieran solo a las abstracciones que necesitan.

***Por lo tanto, aunque el foco principal de este ejercicio era demostrar y resolver una violación del LSP, el diseño adoptado también aplica y beneficia de los principios del ISP, demostrando cómo estos principios SOLID 
frecuentemente se apoyan y refuerzan mutuamente en el diseño de software efectivo y sostenible.***
