import kotlin.random.Random

/**
 * Clase que proporciona funciones para gestionar cafeteras y tazas.
 */
class GestionCafes {
    companion object {

        /**
         * Crea y devuelve una lista de tazas (por defecto 20) con capacidades aleatorias (50, 75 o 100 c.c.).
         * Los colores de las tazas son seleccionados aleatoriamente de entre los colores disponibles.
         * @return Lista de tazas generadas.
         */
        fun crearListaTazas(num: Int = 20) : List<Taza> {
            return mutableListOf<Taza>().apply {
                for (i in 1..num) {
                    val capacidadAleatoria = when (Random.nextInt(3)) {
                        0 -> 50
                        1 -> 75
                        else -> 100
                    }
                    val taza = Taza(Color.entries.toTypedArray().random(), capacidadAleatoria)
                    add(taza)
                }
            }.toList()
        }

        /**
         * Simula la acción de servir cada taza en la lista utilizando las cafeteras proporcionadas.
         * Las tazas se sirven una por una, y se utiliza la primera cafetera disponible.
         * @param tazas Lista de tazas a servir.
         * @param cafeteras Lista de cafeteras disponibles para servir.
         */
        fun servirTazas(tazas: List<Taza>, cafeteras: List<Cafetera>) {
            for (taza in tazas) {
                for (cafetera in cafeteras) {
                    if (cafetera.cantidad > 0) {
                        cafetera.servirTaza(taza)
                        //Si se utilizó una cafetera, salimos del bucle for porque ya sirvió la taza
                        break
                    }
                }
            }
        }

        /**
         * Muestra la información de las tazas y las cafeteras proporcionadas.
         * @param tazas Lista de tazas a mostrar.
         * @param cafeteras Lista de cafeteras a mostrar.
         */
        fun mostrarInfo(tazas: List<Taza>, cafeteras: List<Cafetera>) {
            mostrarCafeteras(cafeteras)
            mostrarTazas(tazas)
        }

        /**
         * Muestra la información de cada taza en la lista.
         * @param tazas Lista de tazas a mostrar.
         */
        private fun mostrarTazas(tazas: List<Taza>) {
            for (taza in tazas) {
                println(taza)
            }
        }

        /**
         * Muestra la información de cada cafetera en la lista.
         * @param cafeteras Lista de cafeteras a mostrar.
         */
        fun mostrarCafeteras(cafeteras: List<Cafetera>) {
            for (cafetera in cafeteras) {
                println(cafetera)
            }
        }
    }
}