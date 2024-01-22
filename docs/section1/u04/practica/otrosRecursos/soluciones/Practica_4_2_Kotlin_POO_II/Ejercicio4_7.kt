package vtresvcuatro.u4


/**
 * ### **Ejercicio 4.7**
 *
 *    1. Se quiere crear una clase `Cuenta` la cual se caracteriza por tener asociado un número de cuenta y un saldo disponible.
 *
 *    2. Además, se puede consultar el saldo disponible, recibir abonos y realizar pagos.
 *
 *    3. Crear también una clase Persona, que se caracteriza por un DNI y una lista de cuentas bancarias.
 *
 *    4. La `Persona` puede tener asociada hasta 3 cuentas bancarias, y debe tener un método que permita añadir cuentas *(hasta 3 el máximo permitido)*.  Las cuentas se almacenarán en un array/vector. No usar una lista.
 *
 *    5. Métodos de clase:
 *
 *        * Debe contener un método que devuelva si la persona es morosa *(si tienen alguna cuenta con saldo negativo)*. Recibirá como parámetro el objeto `Persona` y devolverá un booleano.
 *        * Debe contener un método que realice una transferencia entre dos cuentas. Recibirá como parámetro dos objetos `PersonaB`, dos identificacdors de cuentas y la cantidad a transferir. Devolverá un booleano indicando si se ha podido realizar o no la operación.
 *
 *    6. En el programa principal, instanciar un objeto Persona con un DNI cualquiera, así como dos objetos cuenta, una sin saldo inicial y otra con 700 euros.
 *       La persona recibe la nómina mensual, por lo que ingresa 1100 euros en la primera cuenta, pero tiene que pagar el alquiler de 750 euros con la segunda.
 *       Imprimir por pantalla si la persona es morosa.
 *
 *    7. Posteriormente hacer una transferencia de una cuenta a otra *(de forma que todos los saldos sean positivos)* y mostrar por pantalla el estado de la persona.
 *
 *
 */


/**
 * Clase cuenta. Representa una cuenta bancaria.
 *
 * @property numeroCuenta Número de cuenta. No puede ser nulo ni vacío.
 * @property saldo, saldo de la cuenta. Por defecto es 0.0. Puede consultarse, recibir abonos y realizar pagos, pero no modificarse directamente.
 */
class Cuenta(val numeroCuenta: String, saldo: Double = 0.0) {

    var saldo: Double = saldo
        private set

    init {
        require(numeroCuenta.isNotEmpty()) { "Numero de cuenta no puede ser nulo" }
    }

    /**
     * Realiza un abono en la cuenta. El saldo aumenta en la cantidad indicada.
     *
     * @param abono Cantidad a abonar en la cuenta.
     * @return Saldo de la cuenta tras el abono.
     */
    fun realizaAbono(abono: Double): Double {
        require(abono > 0.0) { "El abono debe ser mayor que 0" }
        saldo += abono
        return saldo
    }

    /**
     * Realiza un cargo en la cuenta. El saldo disminuye en la cantidad indicada.
     *
     * @param cargo Cantidad a cargar en la cuenta.
     * @return Saldo de la cuenta tras el cargo.
     */
    fun realizaCargo(cargo: Double): Double {
        require(cargo > 0.0) { "El cargo debe ser mayor que 0" }
        saldo -= cargo
        return saldo
    }

    /**
     * Companion object. Contiene métodos estáticos de la clase Cuenta. En este caso, solo se implementa el método isMorosa.
     *
     * @constructor Create empty Companion
     */
    companion object {
        /**
         * Comprueba si una persona es morosa. Una persona es morosa si tiene alguna cuenta con saldo negativo.
         *
         * @param persona Persona a comprobar.
         * @return True si la persona es morosa, false en caso contrario.
         */
        fun isMorosa(persona: PersonaB): Boolean {
            return persona.cuentas.any { (it?.saldo ?: 0.0) < 0.0 }
        }

        /**
         * Realiza una transferencia entre dos cuentas. La transferencia se realiza entre dos cuentas de dos personas distintas.
         *
         * @param pOrigen PersonaB origen de la transferencia.
         * @param numeroCuentaOrigen Número de cuenta origen de la transferencia.
         * @param pDestino PersonaB destino de la transferencia.
         * @param numeroCuentaDestino Número de cuenta destino de la transferencia.
         * @param tranferencia Cantidad a transferir.
         */
        fun transferencia(
            pOrigen: PersonaB,
            numeroCuentaOrigen: String,
            pDestino: PersonaB,
            numeroCuentaDestino: String,
            tranferencia: Double
        ): Boolean {
            val cuentaOrigen = pOrigen.cuenta(numeroCuentaOrigen)
            val cuentaDestino = pDestino.cuenta(numeroCuentaDestino)

            if ((cuentaOrigen == null || cuentaDestino == null) ||  (cuentaOrigen.saldo < tranferencia))
                return false

            cuentaOrigen.realizaCargo(tranferencia)
            cuentaDestino.realizaAbono(tranferencia)
            return true
        }
    }

    override fun toString(): String {
        return "Cuenta $numeroCuenta => con saldo: $saldo"
    }
}

class PersonaB(private var dni: String) {
    val cuentas = arrayOfNulls<Cuenta>(3)
    private var numeroDeCuentas = 0

    fun agregarCuenta(cuenta: Cuenta): Int {
        if (TOTAL_CUENTAS != numeroDeCuentas) {
            cuentas[numeroDeCuentas] = cuenta
            numeroDeCuentas++
        }
        return numeroDeCuentas
    }

    /**
     * Devuelve la cuenta con el número indicado.
     *
     * @param cuenta Número de cuenta a buscar.
     * @return Cuenta con el número indicado, o null si no existe.
     */
    fun cuenta(cuenta: String): Cuenta? {
        var c: Cuenta? = null
        val cuentas = cuentas.filter { it?.numeroCuenta == cuenta }
        if (cuentas.isNotEmpty())
            c = cuentas[0]
        return c
    }

    companion object {
        const val TOTAL_CUENTAS = 3
    }

    override fun toString(): String {
        return "Persona: $dni, cuentas: ${cuentas.toList()}"
    }

}

fun main() {
    val p = PersonaB("1")
    listOf(
        Cuenta("123"),
        //Cuenta("124", 1.1),
        //Cuenta("125", -0.1),
        Cuenta("126", 700.0)
    ).forEach {
        print("Count del array es: ${p.cuentas.size} -> ")
        println("El numero de cuentas es ${p.agregarCuenta(it)}")
    }
    p.cuenta("123")?.realizaAbono(1100.0)
    println("Tras cobrar, es morosa: ${Cuenta.isMorosa(p)}")
    p.cuenta("126")?.realizaCargo(750.0)
    println("Tras pagar el alquiler, es morosa: ${Cuenta.isMorosa(p)}. Saldo: Cuenta 126: ${p.cuenta("126")?.saldo}")

    if (!Cuenta.transferencia(p, "123", p, "126", 200.0))
        println("No se ha podido realizar la transferencia")
    else
        println("Tras realizar transferencia, es morosa: ${Cuenta.isMorosa(p)}")
    println(p)
}
