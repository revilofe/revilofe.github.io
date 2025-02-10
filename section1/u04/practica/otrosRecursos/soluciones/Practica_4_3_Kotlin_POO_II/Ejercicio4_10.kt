package vtresvcuatro.u4

/**
 * ### **Ejercicio 4.10**
 *
 *    1. Realizar el juego del 3 en raya con POO.
 *
 **/

class Consola {
    var tablero: Tablero? = null

    private fun leerPosicion(): Int {
        return readln().toIntOrNull() ?: -1
    }


    /**
     * Muestra el tablero de juego.
     */
    fun mostrarTablero() {
        val t = tablero
        if (t != null) {
            for (fila in 0 until t.filas) {
                for (columna in 0   until t.columnas) {
                    print(" ${t.simbolo(fila, columna)} ")
                    if (columna < t.columnas - 1) print("|")
                }
                println()
                if (fila < t.filas - 1) {
                    for (columna in 0  until  t.columnas) {
                        print("---")
                        if (columna < t.columnas - 1) print("|")
                    }
                    println()
                }
            }
        }
    }

    /**
     * Presenta el mensaje de fin de partida.
     */
    fun finPartida() {
        val t = tablero
        if (t != null) {
            if (t.isGanador())
                println("Ha ganado ${t.ganador()?.nombre}")
            else if (t.isEmpate())
                println("Empate")
        }
    }

    /**
     * Solicita un movimiento al jugador.
     * @param jugador Jugador que debe realizar el movimiento.
     * @return Devuelve la posición del movimiento.
     */
    fun solicitarMovimiento(jugador: Jugador): Pair<Int, Int> {
        println("Turno de ${jugador.nombre}")
        println("Introduce la fila:")
        val fila = leerPosicion()
        println("Introduce la columna:")
        val columna = leerPosicion()
        return Pair(fila, columna)
    }

}

/**
 * Clase Tablero.
 * @param filas Número de filas del tablero.
 * @param columnas Número de columnas del tablero.
 * @param simboloVacio Símbolo que representa una casilla vacía.
 * @param simboloJugador1 Símbolo que representa una casilla ocupada por el jugador 1.
 * @param simboloJugador2 Símbolo que representa una casilla ocupada por el jugador 2.
 * @property tablero Tablero de juego.
 * @property jugador1 Jugador 1.
 * @property jugador2 Jugador 2.
 * @property turno Turno actual.
 * @property ganador Ganador del juego.
 * @property finalizado Indica si el juego ha finalizado.
 * @property empate Indica si el juego ha finalizado en empate.
 * @property ganador Indica si el juego ha finalizado con un ganador.
 */
class Tablero(
    val filas: Int,
    val columnas: Int,
    private val simboloVacio: Char = ' ',
    private val simboloJugador1: Char = 'X',
    private val simboloJugador2: Char = 'O',
    private val consola: Consola = Consola()

) {



    private val tablero = Array(filas) { CharArray(columnas) { simboloVacio } }
    private var jugador1: Jugador? = null
    private var jugador2: Jugador? = null
    private var turno = 0
    private var ganador: Jugador? = null
    private var finalizado = false
    private var empate = false

    init {
        require(filas > 2 && columnas > 2) { "El tablero debe tener al menos 3 filas y 3 columnas" }
        consola.tablero = this
    }

    /**
     * Asigna los jugadores.
     * @param jugador1 Jugador 1.
     * @param jugador2 Jugador 2.
     */
    fun asignarJugadores(jugador1: Jugador, jugador2: Jugador) {
        this.jugador1 = jugador1
        this.jugador2 = jugador2

        jugador1.simbolo = simboloJugador1
        jugador1.consola = this.consola
        jugador2.simbolo = simboloJugador2
        jugador2.consola = this.consola

    }


    /**
     * Comprueba si el juego ha finalizado con un ganador.
     * @return Devuelve true si el juego ha finalizado con un ganador, false en caso contrario.
     */
    fun isGanador(): Boolean {
        return ganador != null
    }

    /**
     * Ejecuta un turno de juego.
     */
    private fun ejecutarTurno() {
        if (turno % 2 == 0)
            jugador1?.jugar(this)
        else
            jugador2?.jugar(this)
        turno++
    }


    /**
     * Ejecuta el juego.
     */
    fun loopear() {
        while (!finalizado) {
            consola.mostrarTablero()
            ejecutarTurno()
            if (isGanador() || isEmpate())
                finalizado = true
        }
        consola.mostrarTablero()
        consola.finPartida()

    }

    /**
     * Introduce un símbolo en el tablero. Si el símbolo es el de un jugador, comprueba si ha ganado o si hay empate.
     * @param fila Fila en la que se introduce el símbolo.
     * @param columna Columna en la que se introduce el símbolo.
     * @param simbolo Símbolo a introducir.
     * @return Devuelve true si se ha introducido el símbolo, false en caso contrario.
     */
    fun introducir(fila: Int, columna: Int, simbolo: Char): Boolean {
        if (fila < 0 || fila >= filas || columna < 0 || columna >= columnas)
            return false
        if (tablero[fila][columna] != simboloVacio)
            return false
        tablero[fila][columna] = simbolo
        if (comprobarGanador(fila, columna, simbolo)) {
            ganador = if (simbolo == simboloJugador1) jugador1 else jugador2
            return true
        }
        if (comprobarEmpate()) {
            empate = true
            return true
        }
        return true
    }

    /**
     * Comprueba si hay empate.
     * @return Devuelve true si hay empate, false en caso contrario.
     */
    private fun comprobarEmpate(): Boolean { // con un contador del numero de celdas rellenas, podría saber si hay empate.
        for (fila in 0 until filas)
            for (columna in 0 until columnas)
                if (tablero[fila][columna] == simboloVacio)
                    return false
        return true
    }

    /**
     * Comprueba si un jugador ha ganado.
     * @param fila Fila en la que se ha introducido el último símbolo.
     * @param columna Columna en la que se ha introducido el último símbolo.
     * @param simbolo Símbolo introducido.
     * @return Devuelve true si el jugador ha ganado, false en caso contrario.
     */
    private fun comprobarGanador(fila: Int, columna: Int, simbolo: Char): Boolean {
        var contador = 0
        for (f in 0 until filas)
            if (tablero[f][columna] == simbolo)
                contador++
        if (contador == filas)
            return true
        contador = 0
        for (c in 0 until columnas)
            if (tablero[fila][c] == simbolo)
                contador++
        if (contador == columnas)
            return true
        contador = 0
        for (f in 0 until filas)
            if (tablero[f][f] == simbolo)
                contador++
        if (contador == filas)
            return true
        contador = 0
        for (f in 0 until filas)
            if (tablero[f][columnas - f - 1] == simbolo)
                contador++
        return contador == filas
    }

    /**
     * Comprueba si el juego ha finalizado en empate.
     * @return Devuelve true si el juego ha finalizado en empate, false en caso contrario.
     */
    fun isEmpate(): Boolean {
        return empate
    }

    /**
     * Devuelve el símbolo de una casilla. Si la casilla está vacía, devuelve el símbolo de casilla vacía.
     * @param fila Fila de la casilla.
     * @param columna Columna de la casilla.
     * @return Devuelve el símbolo de la casilla.
     */
    fun simbolo(fila: Int, columna: Int): String {
        return tablero[fila][columna].toString()
    }

    /**
     * Devuelve el ganador del juego. Si no hay ganador, devuelve null.
     * @return Devuelve el ganador del juego. Si no hay ganador, devuelve null.
     */
    fun ganador(): Jugador? {
        return ganador
    }
}

class Jugador(val nombre: String) {
    var simbolo: Char = ' '

    var consola: Consola? = null

    /**
     * Realiza un movimiento en el tablero.
     * @param tablero Tablero de juego.
     */
    fun jugar(tablero: Tablero) {
        val con = consola
        if ( con!=null )
            do {
                    var movimiento = con.solicitarMovimiento(this)
            } while (!tablero.introducir(movimiento.first, movimiento.second, simbolo))
    }
}


fun main() {
    val tablero = Tablero(3, 3)
    val jugador1 = Jugador("Jugador 1")
    val jugador2 = Jugador("Jugador 2")
    tablero.asignarJugadores(jugador1, jugador2)
    tablero.loopear()
}