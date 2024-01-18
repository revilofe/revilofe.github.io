//Parte 2
//Comentar que lo adecuado sería separar el código en distintos ficheros:
// - Direccion.kt (incluye solo la clase enumerada Direccion)
// - Robot.kt (incluye solo la clase Robot)
// - UtilidadEntrada.kt (incluye solo la clase UtilidadEntrada)
// - CalculosDireccion.kt (incluye solo la clase CalculosDireccion)
// - Main.kt (influye la función main())

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
 * @property nuevaDireccion Función lambda que define cómo cambiar la dirección del robot.
 */
class Robot(
    private val nombre: String,
    private var posX: Int = 0,
    private var posY: Int = 0,
    private var dir: Direccion = Direccion.POSITIVEY,
    private val nuevaDireccion: (Int, Int, Direccion) -> Direccion,
) {
    /**
     * Realiza el movimiento del robot en 2D sobre el eje x, y.
     *
     * @param movs Array de pasos que debe dar el robot.
     */
    fun mover(movs: IntArray) {
        //Realizar los movimientos en la dirección en la que está el robot
        for (valor in movs) {
            when (this.dir) {
                Direccion.POSITIVEY -> this.posY += valor
                Direccion.NEGATIVEX -> this.posX -= valor
                Direccion.NEGATIVEY -> this.posY -= valor
                Direccion.POSITIVEX -> this.posX += valor
            }
            //Al finalizar cada movimiento, debe actualizar la orientación del robot
            //según la función tipo que le hemos asignado al objeto Robot al crearlo.
            dir = this.nuevaDireccion(posX, posY, dir)
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
 * Clase de utilidad para la entrada de datos.
 */
class UtilidadEntrada {
    companion object {
        /**
         * Solicita un número entero en un rango.
         *
         * @param text Texto a mostrar para solicitar el número.
         * @param min Valor mínimo.
         * @param max Valor máximo.
         * @return Número entero válido dentro del rango especificado.
         */
        private fun pedirNum(text: String, min: Int = -20, max: Int = 20): Int? {
            var num: Int?
            var entrada: String
            var error = false
            val mensajeError: (String) -> Unit = { x ->
                print("**Error** $x ...) ")
            }

            do {
                print(text)
                entrada = readln().trim()
                if (entrada.isNotEmpty()) {
                    num = try {
                        entrada.toInt()
                    } catch (ex: NumberFormatException) {
                        error = true
                        -1
                    }

                    if (error || num !in min..max) {
                        error = false
                        mensajeError("Número no válido")
                    }
                } else {
                    num = null
                }
            } while (entrada.isNotEmpty() && num !in min..max)

            return num
        }

        /**
         * Solicita una lista de movimientos para los robots.
         *
         * @return Lista de movimientos ingresados por el usuario.
         */
        fun pedirMovimientos(): List<Int> {
            var cont = 1
            val listaMovimentos = mutableListOf<Int>()

            println("Introduzca los pasos que deben dar los robots...(ENTER para finalizar)")

            do {
                val num = pedirNum("${cont++} => ")
                if (num != null) {
                    listaMovimentos.add(num)
                }
            } while (num != null)

            return listaMovimentos
        }
    }
}

/**
 * Clase que contiene funciones de cálculo relacionadas con las direcciones del robot.
 */
class CalculosDireccion {
    companion object {
        /**
         * Función que gira la dirección del robot según el ángulo especificado.
         *
         * @param dir Dirección actual del robot.
         * @param angulo Ángulo de giro (90, 180, 270, -90, -180, -270).
         * @return Nueva dirección después del giro.
         */
        fun girar(dir: Direccion, angulo: Int) =
            when(angulo) {
                90, -270 ->
                    when (dir) {
                        Direccion.POSITIVEY -> Direccion.POSITIVEX
                        Direccion.NEGATIVEX -> Direccion.POSITIVEY
                        Direccion.NEGATIVEY -> Direccion.NEGATIVEX
                        Direccion.POSITIVEX -> Direccion.NEGATIVEY
                    }
                180, -180 ->
                    when (dir) {
                        Direccion.POSITIVEY -> Direccion.NEGATIVEY
                        Direccion.NEGATIVEX -> Direccion.POSITIVEX
                        Direccion.NEGATIVEY -> Direccion.POSITIVEY
                        Direccion.POSITIVEX -> Direccion.NEGATIVEX
                    }
                270, -90 ->
                    when (dir) {
                        Direccion.POSITIVEY -> Direccion.NEGATIVEX
                        Direccion.NEGATIVEX -> Direccion.NEGATIVEY
                        Direccion.NEGATIVEY -> Direccion.POSITIVEX
                        Direccion.POSITIVEX -> Direccion.POSITIVEY
                    }
                else -> dir
            }

        /**
         * Genera un valor aleatorio entre los límites especificados (inclusive).
         *
         * @param min Valor mínimo.
         * @param max Valor máximo.
         * @return Valor aleatorio generado.
         */
        fun generarValorAleatorio(min: Int, max: Int)= Random.nextInt(min, (max + 1))

        /**
         * Genera una dirección aleatoria del enum class Direccion.
         *
         * @return Dirección aleatoria.
         */
        fun generarDireccionAleatoria(): Direccion {
            val direcciones = Direccion.entries.toTypedArray()
            return direcciones[Random.nextInt(direcciones.size)]
        }
    }
}

/**
 * Punto de entrada principal del programa.
 */
fun main() {

    // Funciones de cálculo de dirección para cada robot...
    fun calcularDireccionR2D2(posX: Int, posY:Int, dir: Direccion) = CalculosDireccion.girar(dir, 90)

    fun calcularDireccionDAW1A(posX: Int, posY:Int, dir: Direccion) =
        if (posX >= 0) { //Si tiene un valor X positivo => gira 180º
            CalculosDireccion.girar(dir, 180)
        } else { //Si tiene un valor X negativo => gira 90º
            CalculosDireccion.girar(dir, 90)
        }

    fun calcularDireccionDAW1B(posX: Int, posY:Int, dir: Direccion) =
        if (posY >= 0) //Si tiene un valor Y positivo => gira -90º
            CalculosDireccion.girar(dir, -90)
        else { //Si tiene un valor Y negativo => gira 270º
            CalculosDireccion.girar(dir, 270)
        }

    fun calcularDireccionDAM1(posX: Int, posY:Int, dir: Direccion) : Direccion {
        var newDir: Direccion
        do {
            newDir = CalculosDireccion.generarDireccionAleatoria()
        } while (dir == newDir)
        return newDir
    }

    //Creación de un array de robots con los 4 tipos, cómo pide el enunciado del ejercicio...
    val robots = arrayOf(
        Robot(nombre = "R2D2", nuevaDireccion = ::calcularDireccionR2D2),
        Robot(
            nombre = "DAW1A",
            posX = CalculosDireccion.generarValorAleatorio(-5, 5),
            posY = 0,
            dir = Direccion.POSITIVEX,
            nuevaDireccion = ::calcularDireccionDAW1A
        ),
        Robot(
            nombre = "DAW1B",
            posX = 0,
            posY = CalculosDireccion.generarValorAleatorio(-10, 10),
            dir = CalculosDireccion.generarDireccionAleatoria(),
            nuevaDireccion = ::calcularDireccionDAW1B
        ),
        Robot(
            nombre = "DAM1",
            posX = CalculosDireccion.generarValorAleatorio(-5, 5),
            posY = CalculosDireccion.generarValorAleatorio(-5, 5),
            dir = CalculosDireccion.generarDireccionAleatoria(),
            nuevaDireccion = ::calcularDireccionDAM1
        )
    )
    
    //Solicitar al usuario un movimiento que incluya un número indeterminado de pasos a realizar...
    val movimientos = UtilidadEntrada.pedirMovimientos().toIntArray()

    //Por cada robot realizaremos el movimiento y mostraremos su posición final...
    for (robot in robots) {
        robot.mover(movimientos)
        robot.mostrarPosicion()
    }
}
