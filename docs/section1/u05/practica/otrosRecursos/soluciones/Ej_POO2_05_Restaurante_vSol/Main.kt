
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

    println("***** Mesa ${mesas[0].numero} *****")
    println(mesas[0])

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

    println("***** Mesa ${mesas[1].numero} *****")
    println(mesas[1])

    // Cerrar pedidos y liberar mesas
    sistema.cerrarPedido(1)
    sistema.cerrarMesa(1)

    sistema.cerrarPedido(2)
    sistema.cerrarMesa(2)

    // Buscar platos y contar pedidos
    val platosPedidos = sistema.buscarPlatos() ?: listOf()
    if (platosPedidos.isNotEmpty()) {
        println("Platos pedidos: ${platosPedidos.joinToString()}")
    }
    else {
        println("No existen platos.")
    }

    val contPlato = sistema.contarPlato("Ensalada") ?: 0
    println("El plato 'Ensalada' fue pedido $contPlato " +
            "${if (contPlato == 1) "vez" else "veces" }.")

    val platosMasPedidos = sistema.buscarPlatoMasPedido()
    if (platosMasPedidos != null) {
        println("${if (platosMasPedidos.size == 1) 
                "El plato más pedido es " else "Los platos más pedidos son "} " +
                "${platosMasPedidos.joinToString()}.")
    }
    else {
        println("No existen platos.")
    }
}