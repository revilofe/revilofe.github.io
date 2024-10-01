
class Pedido {
    companion object {
        var contPedidos = 0
    }

    val numero = ++contPedidos
    var platos = mutableListOf<Plato>()
    var estado = "pendiente"

    fun agregarPlato(plato: Plato) {
        platos.add(plato)
    }

    fun eliminarPlato(nombrePlato: String) {
        platos.removeAll { it.nombre == nombrePlato }
    }

    fun calcularPrecio(): Double {
        return platos.sumOf { it.precio }
    }

    fun calcularTiempo(): Int {
        return platos.sumOf { it.tiempoPreparacion }
    }

    override fun toString(): String {
        return platos.joinToString("\n") { it.toString() } + "\nEstado: $estado"
    }
}
