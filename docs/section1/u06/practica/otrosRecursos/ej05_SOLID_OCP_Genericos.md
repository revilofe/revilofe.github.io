## Ejercicio 05: Refactorización del Sistema de Procesamiento de Pedidos utilizando Genéricos

### **Contexto:**

Imagina que eres parte de un equipo de desarrollo encargado de mejorar y extender un sistema de gestión de pedidos para una tienda en línea. La versión actual del sistema maneja diferentes tipos de pedidos 
(digitales, físicos, y suscripciones) mediante un enfoque que no utiliza genéricos, lo que ha resultado en un código más rígido y difícil de mantener cada vez que se introducen nuevos tipos de pedidos.

### **Objetivo:**

Tu tarea es refactorizar este sistema aplicando el uso de genéricos para lograr una solución más flexible y adherente al Principio de Abierto/Cerrado. Esto permitirá añadir nuevos tipos de pedidos 
en el futuro sin modificar el código existente del gestor de pedidos.

### **Requisitos:**

1. **Definir Clases de Pedidos**: Crea `data class` para representar distintos tipos de pedidos (p.ej., `PedidoDigital`, `PedidoFisico`, `PedidoSuscripcion`). Cada clase debe tener propiedades que reflejen sus
   características específicas (p.ej., `urlDescarga` para digitales, `direccionEnvio` para físicos, `duracionMeses` para suscripciones).

3. **Implementar la Interfaz Genérica `ProcesadorPedido`**: Diseña una interfaz genérica `ProcesadorPedido<T>` que declare un método `procesar(pedido: T)`.
   Esta interfaz será la base para implementar diferentes procesadores de pedidos.

5. **Crear Procesadores de Pedidos**: Implementa clases concretas para procesar cada tipo de pedido. Estas clases deben implementar `ProcesadorPedido<T>` especificando el tipo de pedido correspondiente.

6. **Desarrollar el Gestor de Pedidos Genérico**: Crea una clase `GestorPedidos<T>` que utilice un procesador de pedidos para procesar pedidos de cualquier tipo. La instancia de `GestorPedidos` debe ser
   capaz de aceptar un procesador específico en el momento de su creación.

8. **Demostración**: Escribe un bloque de código `main` que demuestre cómo se pueden crear y procesar diferentes tipos de pedidos utilizando tu sistema refactorizado. Asegúrate de mostrar cómo se añade un
   nuevo tipo de pedido al sistema con mínimo esfuerzo.

### **Consideraciones Adicionales:**

- Reflexiona sobre cómo el uso de genéricos no solo facilita la adherencia al Principio de Abierto/Cerrado, sino que también promueve la reutilización de código y mejora la legibilidad.
- Considera realizar los siguientes pasos para la realización de esta nueva solución:
   1. Definir las Clases de Pedido.
   2. Definir la Interfaz `ProcesadorPedido` con Genéricos.
   3. Implementar Clases Concretas de Procesamiento que implementen la interfaz `ProcesarPedido`
   4. Crear un Gestor de Pedidos Genérico.
   5. Demostración del Uso en el programa pcincipal.

### **Entrega:**

Tu solución debe incluir:

- El código fuente de las clases y la interfaz que diseñaste.
- Un ejemplo de ejecución que demuestre la flexibilidad de tu sistema para manejar diferentes tipos de pedidos.
- Una breve explicación de cómo tu diseño permite añadir nuevos tipos de pedidos sin modificar el código existente.

Este ejercicio no solo pondrá a prueba tu habilidad para aplicar genéricos en Kotlin, sino que también te desafiará a pensar en diseños de software flexibles y mantenibles.

### **Solución refactorizada:**

Para aplicar el Principio de Abierto/Cerrado (OCP) usando genéricos en Kotlin, adaptaremos la solución anterior considerando que `PedidoDigital`, `PedidoFisico`, y `PedidoSuscripcion` son `data class` con características diferentes. 
Esto nos permitirá manejar distintos tipos de pedidos de forma más específica y extensible.

#### Paso 1: Definir las Clases de Pedido

Primero, definimos las `data class` para cada tipo de pedido, con sus características únicas:

```kotlin
data class PedidoDigital(val id: Int, val productoDigital: String, val urlDescarga: String)
data class PedidoFisico(val id: Int, val productoFisico: String, val direccionEnvio: String)
data class PedidoSuscripcion(val id: Int, val servicio: String, val duracionMeses: Int)
```

#### Paso 2: Definir la Interfaz `ProcesadorPedido` con Genéricos

A continuación, definimos una interfaz genérica para procesar los pedidos. Esta interfaz aceptará cualquier tipo de pedido:

```kotlin
interface ProcesadorPedido<T> {
    fun procesar(pedido: T)
}
```

#### Paso 3: Implementar Clases Concretas de Procesamiento

Implementamos clases concretas que procesan cada tipo de pedido. Cada una implementará la interfaz `ProcesadorPedido` especificando el tipo de pedido correspondiente:

```kotlin
class ProcesadorPedidoDigital : ProcesadorPedido<PedidoDigital> {
    override fun procesar(pedido: PedidoDigital) {
        println("Procesando pedido digital '${pedido.productoDigital}' para descarga desde: ${pedido.urlDescarga}")
    }
}

class ProcesadorPedidoFisico : ProcesadorPedido<PedidoFisico> {
    override fun procesar(pedido: PedidoFisico) {
        println("Procesando pedido físico '${pedido.productoFisico}' para enviar a: ${pedido.direccionEnvio}")
    }
}

class ProcesadorPedidoSuscripcion : ProcesadorPedido<PedidoSuscripcion> {
    override fun procesar(pedido: PedidoSuscripcion) {
        println("Procesando suscripción a '${pedido.servicio}' por ${pedido.duracionMeses} meses")
    }
}
```

#### Paso 4: Crear un Gestor de Pedidos Genérico

Creamos una clase genérica `GestorPedidos` que pueda aceptar y procesar cualquier tipo de pedido utilizando el procesador adecuado:

```kotlin
class GestorPedidos<T>(private val procesador: ProcesadorPedido<T>) {
    fun procesarPedido(pedido: T) {
        procesador.procesar(pedido)
    }
}
```

#### Paso 5: Demostración del Uso

Finalmente, mostramos cómo utilizar esta estructura para procesar diferentes tipos de pedidos:

```kotlin
fun main() {
    val pedidoDigital = PedidoDigital(1, "Curso Online de Kotlin", "http://dcs-curso-kotlin.com")
    val gestorPedidoDigital = GestorPedidos(ProcesadorPedidoDigital())
    gestorPedidoDigital.procesarPedido(pedidoDigital)

    val pedidoFisico = PedidoFisico(2, "Libro de Kotlin", "Calle Real 123, San Fernando")
    val gestorPedidoFisico = GestorPedidos(ProcesadorPedidoFisico())
    gestorPedidoFisico.procesarPedido(pedidoFisico)

    val pedidoSuscripcion = PedidoSuscripcion(3, "Suscripción a Revista de Programación", 12)
    val gestorPedidoSuscripcion = GestorPedidos(ProcesadorPedidoSuscripcion())
    gestorPedidoSuscripcion.procesarPedido(pedidoSuscripcion)

    //Con este código no sería posible crear un pedido misterioso con un tipo de procesamiento desconocido o no soportado.
}
```

Esta solución mantiene el sistema abierto para la extensión permitiendo la adición de nuevos tipos de pedidos y sus respectivos procesadores sin necesidad de modificar el código existente 
del gestor de pedidos, cumpliendo con el principio de estar abierto para la extensión pero cerrado para la modificación. Al usar `data class` y genéricos, se facilita la implementación de 
un diseño robusto y flexible.
