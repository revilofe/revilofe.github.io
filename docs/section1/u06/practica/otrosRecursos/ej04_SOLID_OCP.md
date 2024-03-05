## Ejercicio 04: Procesamiento de Pedidos

### **Contexto:** 

Estás creando una aplicación para gestionar el procesamiento de pedidos en una tienda en línea. Los pedidos pueden ser procesados de diferentes maneras dependiendo del tipo de producto (por ejemplo, productos digitales, físicos, suscripciones).

### **Tarea:** 

Diseñar un sistema de procesamiento de pedidos que cumpla con el principio SOLID de Abierto/Cerrado (OCP). Debe ser fácil añadir nuevos tipos de productos y sus respectivos procesamientos sin modificar el código existente.

### **Requerimientos:**

1. Crea una interfaz `ProcesadorPedido` con un método `procesar(pedido: Pedido)`.
2. Implementa clases concretas para procesar diferentes tipos de pedidos (por ejemplo, `ProcesadorPedidoDigital`, `ProcesadorPedidoFisico`, `ProcesadorPedidoSuscripcion`).
3. Asegúrate de que añadir un nuevo tipo de producto sólo requiera añadir una nueva clase que implemente `ProcesadorPedido` sin modificar ninguna otra parte del código.

### **Consideraciones:** 

- El pedido tendrá un id (Int), un tipo (String) y detalles (String).
- El método procesar simplemente debe imprimir por consola que está procesando un pedido específico, imaginemos que tenemos los siguientes pedidos: 

   * Pedido(1, "digital", "E-book de Kotlin")
   * Pedido(2, "fisico", "Libro impreso de Kotlin")
   * Pedido(3, "suscripcion", "Suscripción a curso de Kotlin")
   * Pedido(4, "desconocido", "Producto misterioso")

Los mensajes que debe mostrar por consola el método procesar serán los siguientes:

   * Procesando pedido digital: E-book de Kotlin
   * Procesando pedido físico: Libro impreso de Kotlin
   * Procesando suscripción: Suscripción a curso de Kotlin
   * Tipo de pedido 'desconocido' no soportado
  
- Reflexiona sobre cómo estructurarías las clases y las interfaces para maximizar la reutilización del código y minimizar el impacto de los cambios futuros, siguiendo el principio de Abierto/Cerrado (OCP).
  Intenta crear una clase `GestorPedidos(private val procesadores: Map<String, ProcesadorPedido>)` que reciba un diccionario con el mapeo de los posibles procesadores de pedidos que habéis definido.

### **Solución refactorizada:**

Para resolver el ejercicio propuesto, siguiendo el Principio de Abierto/Cerrado, diseñaremos un sistema que permita gestionar distintos tipos de procesamiento de pedidos sin necesidad de modificar el 
código existente cada vez que se añada un nuevo tipo de pedido.

#### Paso 1: Definir la Interfaz `ProcesadorPedido`

Primero, definimos una interfaz que será implementada por todas las clases encargadas de procesar los diferentes tipos de pedidos.

```kotlin
interface ProcesadorPedido {
    fun procesar(pedido: Pedido)
}
```

#### Paso 2: Crear la Clase `Pedido`

Luego, definimos una clase básica `Pedido` que contendrá los detalles necesarios para cualquier pedido. A fines de este ejemplo, mantenemos la clase `Pedido` simple.

```kotlin
data class Pedido(val id: String, val tipo: String, val detalles: String)
```

#### Paso 3: Implementar Clases Concretas de Procesamiento

Ahora, implementamos clases concretas para cada tipo de procesamiento de pedido. Estas clases implementarán la interfaz `ProcesadorPedido`.

```kotlin
class ProcesadorPedidoDigital : ProcesadorPedido {
    override fun procesar(pedido: Pedido) {
        println("Procesando pedido digital: ${pedido.detalles}")
    }
}

class ProcesadorPedidoFisico : ProcesadorPedido {
    override fun procesar(pedido: Pedido) {
        println("Procesando pedido físico: ${pedido.detalles}")
    }
}

class ProcesadorPedidoSuscripcion : ProcesadorPedido {
    override fun procesar(pedido: Pedido) {
        println("Procesando suscripción: ${pedido.detalles}")
    }
}
```

#### Paso 4: Crear un Gestor de Pedidos

Para facilitar el procesamiento de los pedidos, podemos crear una clase gestora que, dependiendo de los posibles procesadores del Sistema, elija el adecuado. Esto permite mantener el sistema flexible y abierto 
a extensiones sin modificar el código existente.

```kotlin
class GestorPedidos(private val procesadores: Map<String, ProcesadorPedido>) {
    fun procesarPedido(pedido: Pedido) {
        val procesador = procesadores[pedido.tipo]
        procesador?.procesar(pedido) ?: println("Tipo de pedido '${pedido.tipo}' no soportado.")
    }
}
```

#### Paso 5: Demostración del Uso

Finalmente, aquí hay un ejemplo de cómo utilizar este sistema para procesar diferentes tipos de pedidos.

```kotlin
fun main() {
    val procesadores = mapOf(
        "digital" to ProcesadorPedidoDigital(),
        "fisico" to ProcesadorPedidoFisico(),
        "suscripcion" to ProcesadorPedidoSuscripcion()
        // Añadir nuevos procesadores de pedidos aquí no requeriría modificar el código de GestorPedidos.
    )

    val gestorPedidos = GestorPedidos(procesadores)

    // Procesar pedidos...

    val pedidoDigital = Pedido(1, "digital", "E-book de Kotlin")
    gestorPedidos.procesarPedido(pedidoDigital)

    val pedidoFisico = Pedido(2, "fisico", "Libro impreso de Kotlin")
    gestorPedidos.procesarPedido(pedidoFisico)

    val pedidoSuscripcion = Pedido(3, "suscripcion", "Suscripción a curso de Kotlin")
    gestorPedidos.procesarPedido(pedidoSuscripcion)

    val pedidoDesconocido = Pedido(4, "desconocido", "Producto misterioso")
    gestorPedidos.procesarPedido(pedidoDesconocido) // Este mostrará un mensaje de tipo de pedido no soportado.
}
```

Esta solución demuestra cómo aplicar el Principio de Abierto/Cerrado en el diseño de un sistema de procesamiento de pedidos. Se puede añadir fácilmente soporte para nuevos tipos de pedidos simplemente implementando la interfaz `ProcesadorPedido` en una nueva clase, sin necesidad de modificar el código existente.
