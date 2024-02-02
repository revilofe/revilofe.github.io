class Plato(
    nombre: String,
    precio: Double,
    tiempoPreparacion: Int,
    private var ingredientes: MutableList<String>
) {
    var nombre: String = nombre
        set(value) {
            requireNombre(value)
            field = value
        }

    var precio: Double = precio
        set(value) {
            requirePrecio(value)
            field = value
        }

    var tiempoPreparacion: Int = tiempoPreparacion
        set(value) {
            requireTiempo(value)
            field = value
        }

    init {
        requireNombre(nombre)
        requirePrecio(precio)
        requireTiempo(tiempoPreparacion)
    }

    private fun requireNombre(nombre: String) {
        require(nombre.isNotBlank()) { "El nombre del plato no puede estar vacío." }
    }

    private fun requirePrecio(precio: Double) {
        require(precio > 0) { "El precio debe ser mayor que 0." }
    }

    private fun requireTiempo(tiempo: Int) {
        require(tiempo > 0) { "El tiempo de preparación debe ser mayor que 0." }
    }

    fun agregarIngrediente(ingrediente: String) {
        require(ingrediente.isNotBlank()) { "El ingrediente no puede estar vacío." }
        ingredientes.add(ingrediente)
    }

    override fun toString(): String {
        return "$nombre ($tiempoPreparacion min.) -> $precio€ (${ingredientes.joinToString(", ")})"
    }
}
