## El Restaurante

### Bloque 1: Gestión de Platos y Pedidos

#### 1. Clase Plato
- **Responsabilidades:**
  - Representar la información de un plato.

- **Propiedades:**
  - `nombre`: String - El nombre del plato. No puede ser vacío.
  - `precio`: Double - El precio del plato. Debe ser mayor que 0.
  - `tiempoPreparacion`: Int - Tiempo estimado para preparar el plato (en minutos).
  - `ingredientes`: List<String> - Lista de ingredientes necesarios para el plato.

- **Métodos:**
  - `agregarIngrediente(ingrediente: String)`: Añade un nuevo ingrediente a la lista de ingredientes del plato.
  - `toString()`: Retornar la información del plato (por ejemplo, "Hamburguesa (8 min.) -> 8.99€ (carne, huevo, queso, pan y tomate)")

**Premisas y Requisitos:**
- El nombre del plato no puede ser vacío.
- El precio del plato debe ser mayor que 0.
- El tiempo de preparación no podrá ser igual o inferior a 1.
- Un ingrediente no puede ser vacío.
- Considerar el uso de propiedades de Kotlin para validar automáticamente estas restricciones tanto al crear un plato cómo al modificar sus valores.

#### 2. Clase Pedido
- **Responsabilidades:**
  - Mantener un registro de los platos pedidos por un cliente.
  - `contPedidos`: Int - No pertenece a ningún pedido en concreto, sino que es un valor global a todos y se utilizará para calcular automáticamente los números de los pedidos.

- **Propiedades:**
  - `numero`: Int - El número de pedido será calculado automáticamente al crear cada pedido con respecto a un contador que existirá en la clase Pedido.
  - `platos`: List<Plato> - Lista de platos que componen el pedido.
  - `estado`: String - Estado del pedido (por ejemplo, "pendiente", "preparación", "listo" y "servido"). Por defecto, todo pedido estará en estado pendiente.

- **Métodos:**
  - `agregarPlato(plato: Plato)`: Añade un nuevo plato al pedido.
  - `eliminarPlato(nombrePlato: String)`: Elimina un plato del pedido basándose en el nombre.
  - `calcularPrecio()`: Calcula el precio total del pedido sumando los precios de cada plato.
  - `calcularTiempo()`: Calcula el tiempo total de preparación sumando el tiempo de preparación de cada plato.
  - `toString()`: Retornar la información del pedido utilizando el número de mesa, el método toString() de cada plato y su estado. (por ejemplo, "Hamburguesa (8 min.) -> 8.99€ (carne, huevo, queso, pan y tomate)")

### Bloque 2: Gestión de Mesas y Sistema de Gestión de Restaurante

#### 3. Clase Mesa
- **Responsabilidades:**
  - Representar una mesa en el restaurante.

- **Propiedades:**
  - `numero`: Int - Número de la mesa.
  - `capacidad`: Int - Capacidad máxima de personas que pueden sentarse en la mesa. Solo existen mesas de 1 a 6 comensales.
  - `estado`: String - Estado de la mesa (por ejemplo, "libre", "reservada y "ocupada").
  - `pedidos`: List<Pedido> - Lista de pedidos realizados por la mesa.

- **Métodos:**
  - `ocuparMesa()`: Cambia el estado de la mesa a "ocupada", pero solo si la mesa está en estado "libre".
  - `ocuparReserva()`: Cambia el estado de la mesa a "ocupada", pero solo si la mesa está en estado "reservada".
  - `liberarMesa()`: Cambia el estado de la mesa a "libre".
  - `agregarPedido(Pedido)`: Agrega un pedido a los pedidos de la mesa.

#### 4. Sistema de Gestión de Restaurante
- **Responsabilidades:**
  - Integrar y gestionar las operaciones del restaurante.

- **Propiedades:**
  - `mesas`: List<Mesa> - Lista de todas las mesas en el restaurante.

- **Métodos:**
  - `realizarPedido(numeroMesa: Int, pedido: Pedido)`: Asocia un nuevo pedido a una mesa. Debe verificar que la mesa esté ocupada antes de asociar el pedido.
  - `cerrarPedido(numeroMesa: Int)`: Marca el último pedido de una mesa como servido.
  - `cerrarPedido(numeroMesa: Int, numeroPedido: Int)`: Marca el pedido de una mesa como servido.
  - `cerrarMesa(numeroMesa: Int)`: Si todos los pedidos están servidos, libera la mesa.
  - `buscarPlatos()`: Retorna una lista con el nombre de los platos pedidos. Si no hay ninguno retorna null.
  - `contarPlato(nombre: String)`: Cuenta el número de veces que se ha pedido un plato. Si no hay ninguno retorna null.
  - `buscarPlatoMasPedido()`: Busca y retorna el o los platos más pedidos. Si no hay ninguno retorna null. Utiliza los dos métodos anteriores.

**Premisas y Requisitos:**
- La capacidad de una mesa debe ser un número positivo.
- El estado de la mesa debe ser manejado adecuadamente para reflejar si está libre, reservada u ocupada.

### Programa principal

Aquí tienes un ejemplo de cómo podría ser el `main` para probar todas las funcionalidades del sistema de gestión del restaurante. 
Este `main` incluye la creación de platos y pedidos, la gestión de mesas y el uso del sistema de gestión del restaurante para realizar y cerrar pedidos, 
y para buscar información relevante sobre los platos más pedidos.
Este programa principal debería funcionar bien si creáis correctamente las clases que os he solicitado.

```kotlin
fun main() {
    // Inicialización de mesas
    val mesas = listOf(
        Mesa(numero = 1, capacidad = 4),
        Mesa(numero = 2, capacidad = 2),
        Mesa(numero = 3, capacidad = 6)
    )
    
    // Inicialización del sistema de gestión de restaurante
    val sistema = SistemaGestionRestaurante(mesas)

    // Creación de platos
    val plato1 = Plato("Hamburguesa", 9.99, 8, mutableListOf("carne", "huevo", "queso", "pan", "tomate"))
    val plato2 = Plato("Ensalada", 7.99, 5, mutableListOf("lechuga", "tomate", "zanahoria", "maíz"))
    val plato3 = Plato("Tortilla", 5.99, 10, mutableListOf("huevo", "patata"))
    val plato4 = Plato("Serranito", 6.00, 4, mutableListOf("carne", "pimiento", "pan", "jamón serrano"))
    val plato5 = Plato("Spagetti carbonara", 6.00, 12, mutableListOf("huevo", "pasta", "bacon", "nata"))
    val plato6 = Plato("Rissotto setas", 6.00, 12, mutableListOf("arroz", "setas", "gambas", "nata"))

    // Agregar ingredientes
    plato1.agregarIngrediente("salsa")
    plato2.agregarIngrediente("atún")

    //Simular el registro de comensales a una mesa
    mesas[0].ocuparMesa() // Ocupar mesa 1

    // Creación de pedidos
    val pedido1 = Pedido()
    pedido1.agregarPlato(plato1)
    pedido1.agregarPlato(plato2)
    pedido1.agregarPlato(plato3)
    pedido1.agregarPlato(plato4)

    println("***** Pedido ${pedido1.numero} *****")
    println(pedido1)

    // Simulación del proceso de los pedidos
    sistema.realizarPedido(1, pedido1)

    println("***** Mesa ${mesa[0].numero} *****")
    println(mesa[0])

    //Simular el registro de comensales a una mesa
    mesas[1].ocuparMesa() // Ocupar mesa 2

    //Crear otro pedido
    val pedido2 = Pedido()
    pedido2.agregarPlato(plato2)
    pedido2.agregarPlato(plato3)
    pedido2.agregarPlato(plato4)

    // Simulación del proceso de los pedidos
    sistema.realizarPedido(2, pedido2)

    //Crear un segundo pedido para la mesa 2
    val pedido3 = Pedido()
    pedido3.agregarPlato(plato5)
    pedido3.agregarPlato(plato6)

    // Simulación del proceso de los pedidos
    sistema.realizarPedido(2, pedido3)

    println("***** Mesa ${mesa[1].numero} *****")
    println(mesa[1])

    // Cerrar pedidos y liberar mesas
    sistema.cerrarPedido(1)
    sistema.cerrarMesa(1)

    sistema.cerrarPedido(2)
    sistema.cerrarMesa(2)

    // Buscar platos y contar pedidos
    val platosPedidos = sistema.buscarPlatos() ?: listOf()
    if (platosPedidos.size > 0) {
        println("Platos pedidos: ${platosPedidos.joinToString()}")
    }
    else {
        println("No existen platos.")
    }
    
    val contPlato = sistema.contarPlato("Hamburguesa") ?: 0
    println("El plato 'Hamburguesa' fue pedido $contPlato veces.")

    val platosMasPedidos = sistema.buscarPlatoMasPedido()
    if (platosMasPedidos != null) {
        println("${if (platosMasPedidos.size == 1) "El plato más pedido es " else "Los platos más pedidos son "} ${platosMasPedidos.joinToString()}.")
    }
    else {
        println("No existen platos.")
    }
}
```

Este `main` proporciona una base sólida para probar el sistema. Los estudiantes pueden usarlo como punto de partida para verificar que todas las partes de su sistema funcionen como se espera. Se anima a los estudiantes a expandir o modificar este `main` según sea necesario para probar todas las características y manejar diferentes escenarios que puedan ocurrir en un restaurante real.
