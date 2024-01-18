//Práctica 4.4: Kotlin POO III - Parte 1

/**
 * Enumeración que representa las posibles direcciones de movimiento para el robot en un sistema 2D.
 *
 * @property desc Descripción asociada a cada dirección.
 */
enum class Direccion(val desc: String) {
    POSITIVEY("PositiveY"),
    NEGATIVEX("NegativeX"),
    NEGATIVEY("NegativeY"),
    POSITIVEX("PositiveX")
}

/**
 * Clase que representa a un robot en un sistema 2D.
 *
 * @property nombre El nombre del robot.
 * @property posX La posición actual en el eje x.
 * @property posY La posición actual en el eje y.
 * @property dir La dirección actual del robot.
 */
class Robot(private val nombre: String) {
    //Siempre debe comenzar en la posición (0, 0) y la dirección eje Y positivo (hacia arriba)
    private var posX = 0
    private var posY = 0
    private var dir = Direccion.POSITIVEY

    /**
     * Realiza el movimiento del robot en 2D sobre el eje x, y.
     *
     * @param movs Array de pasos que debe dar el robot.
     */
    fun mover(movs: Array<Int>) {
        //Realizar los movimientos en la dirección en la que está el robot
        for (valor in movs) {
            when (this.dir) {
                Direccion.POSITIVEY -> this.posY += valor
                Direccion.NEGATIVEX -> this.posX -= valor
                Direccion.NEGATIVEY -> this.posY -= valor
                Direccion.POSITIVEX -> this.posX += valor
            }
            //Al finalizar cada movimiento, debe actualizar la orientación en -90º
            this.nuevaDireccion()
        }
    }

    /**
     * Actualizar la orientación -90º
     */
    private fun nuevaDireccion() {
        when (this.dir) {
            Direccion.POSITIVEY -> this.dir = Direccion.NEGATIVEX
            Direccion.NEGATIVEX -> this.dir = Direccion.NEGATIVEY
            Direccion.NEGATIVEY -> this.dir = Direccion.POSITIVEX
            Direccion.POSITIVEX -> this.dir = Direccion.POSITIVEY
        }
    }

    /**
     * Mostrar por consola una descripción de la posición del robot basada en sus propiedades
     */
    fun mostrarPosicion() {
        println("$nombre está en ($posX, $posY) ${obtenerDireccion()}")
    }

    /**
     * Retorna la dirección del robot positivo o negativo en el eje x o y.
     *
     * @return String con la dirección del robot.
     */
    private fun obtenerDireccion() = this.dir.desc

}

/**
 * Función principal que crea un robot y realiza movimientos predefinidos,
 * mostrando la posición después de cada movimiento.
 */
fun main() {
    val robot1 = Robot("R2D2")

    val movimientos = arrayOf(
        arrayOf(1, -5, 0, -9),
        arrayOf(3, 3, 5, 6, 1, 0, 0, -7),
        arrayOf(2, 1, 0, -1, 1, 1, -4),
        arrayOf(),
        arrayOf(3, 5)
    )

    for (movimiento in movimientos) {
        robot1.mover(movimiento)
        robot1.mostrarPosicion()
    }
}
