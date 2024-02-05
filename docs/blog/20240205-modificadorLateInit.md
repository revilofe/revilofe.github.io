---
title: Modificador lateinit.

description: Modificador lateinit, ejemplo de uso.

authors:
    - Diego Cano.

date: 2024-02-05

tags:
  - lateinit
  - inicialización
  - kotlin
---
# Modificador lateinit

El modificador `lateinit` es útil en Kotlin para casos en los que queremos declarar una propiedad no nula pero no podemos inicializarla en el momento de la creación del objeto. 
Es comúnmente utilizado en situaciones como la inyección de dependencias o la inicialización posterior en el ciclo de vida del objeto.

## **Ejemplo: Gestor de Tareas**

Vamos a crear una clase `GestorTareas` que represente un sistema simple para manejar tareas. Inicialmente, cuando se crea el gestor, aún no tenemos una lista de tareas para asignarle, 
así que queremos inicializar esa lista más tarde.

1. **Creación de la Clase con `lateinit`:**
    - Define una clase `Tarea` con una propiedad `descripcion`.
    - Define la clase `GestorTareas` que inicialmente no sabe cuáles son las tareas que va a gestionar.
    - Utiliza `lateinit` para declarar una propiedad que almacenará una lista de `Tarea`.
    - Proporciona una función `inicializarTareas` para configurar las tareas después de la creación del objeto `GestorTareas`.

        ```kotlin
        class Tarea(val descripcion: String)
        
        class GestorTareas {
            lateinit var tareas: List<Tarea>
        
            fun inicializarTareas(tareas: List<Tarea>) {
                this.tareas = tareas
            }
        
            fun mostrarTareas() {
                if (::tareas.isInitialized) {
                    tareas.forEach { tarea ->
                        println(tarea.descripcion)
                    }
                } else {
                    println("Las tareas aún no han sido inicializadas.")
                }
            }
        }
        ```
        
        ```kotlin
        fun main() {
            val gestor = GestorTareas()
            gestor.mostrarTareas()  // Debe indicar que las tareas no están inicializadas
        
            val listaTareas = listOf(Tarea("Aprender Kotlin"), Tarea("Hacer ejercicio"))
            gestor.inicializarTareas(listaTareas)
            
            gestor.mostrarTareas()  // Ahora debe mostrar las tareas asignadas
        }
        ```

    En este ejemplo, el gestor de tareas comienza sin conocer las tareas. Solo después de inicializarlo con una lista de tareas (mediante el método `inicializarTareas`), 
    está listo para funcionar y mostrar las tareas. Esto demuestra el uso de `lateinit` para propiedades que serán inicializadas más tarde y también muestra cómo comprobar 
    si una propiedad `lateinit` ha sido inicializada antes de usarla, usando `::tareas.isInitialized`.
    
    En Kotlin, el operador `::` se utiliza como referencia a funciones o propiedades, y también para acceder a ciertas propiedades de la reflexión del lenguaje.

2. **Verificación de Inicialización con `lateinit`:**
   - En el contexto de una propiedad `lateinit`, puedes usar `::` para hacer referencia a la propiedad y luego `.isInitialized` para verificar si la propiedad ha sido inicializada.
   - Ejemplo:
        ```kotlin
        class Ejemplo {
            lateinit var texto: String
        }

        fun main() {
            val ejemplo = Ejemplo()
            if (::texto.isInitialized) { // Verifica si 'texto' ha sido inicializado
                println(ejemplo.texto)
            } else {
                println("texto no está inicializado.")
            }
        }
        ```
   - Esto es especialmente útil para propiedades `lateinit`, ya que acceder a una propiedad `lateinit` no inicializada lanzaría una excepción.
     La verificación con `.isInitialized` te permite evitar esta excepción comprobando primero si la propiedad ha sido inicializada.

    El uso de `::` es bastante versátil y forma parte de las capacidades reflexivas y funcionales de Kotlin, 
    permitiendo escribir código más abstracto y general, así como realizar comprobaciones en tiempo de ejecución sobre las propiedades y funciones de tus objetos.

### Referencia a Funciones o Propiedades:
   - Puedes obtener una referencia a una función específica de una clase o un objeto usando el operador `::`.
   - Esto es útil, por ejemplo cómo ya hemos visto anteriormente en esta unidad, cuando quieres pasar una función como argumento a otra función de orden superior.
   - Ejemplo:

        ```kotlin
        fun saludar() {
            println("¡Hola!")
        }

        fun ejecutarAccion(accion: () -> Unit) {
            accion()
        }

        fun main() {
            // Pasamos la referencia de la función 'saludar' a 'ejecutarAccion'
            ejecutarAccion(::saludar) // Imprime "¡Hola!"
        }
        ```
   - Lo mismo se puede hacer con propiedades para obtener una referencia a la propiedad que puedes usar para leer o modificar la propiedad.
   - Ejemplo:
        ```kotlin
        var contador = 0

        fun main() {
            val referenciaContador = ::contador
            referenciaContador.set(referenciaContador.get() + 1)
            println(contador) // Imprime 1
        }
        ```
