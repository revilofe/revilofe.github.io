package vtresvcuatro.u5

import kotlin.math.ceil
import kotlin.math.floor

/**
 *
 * Clase Base Vehiculo
 *
 * Propiedades:
 * marca: String: Identifica la marca del vehículo.
 * modelo: String: Especifica el modelo del vehículo.
 * capacidadCombustible: Float: Capacidad total del tanque de combustible en litros.
 * combustibleActual: Float: Cantidad actual de combustible en litros.
 * kilometrosActuales: Int: Kilometraje actual del vehículo.
 * Métodos:
 * obtenerInformacion(): Devuelve una representación de los detalles básicos del vehículo.
 * calcularAutonomia() -> Int: Retorna los kilómetros que el vehículo puede recorrer con el combustible actual. (Suponemos que cada litro da para 10 km.)
 * realizaViaje(distancia: Int) -> Int:  Realiza un viaje hasta donde da combustibleActual. Ajusta el combunstible gastado y el kilometraje realizado de acuerdo con el viaje. Devuelve la distancia restante.
 * repostar(cantidad: float)- Float>: Incrementa combustibleActual hasta el máximo de capacidadCombustible, si cantidad es 0 o negativo. Sino, incrementa en cantidad hasta llegar a capacidadCombustible. Devuelve la cantidad repostada.
 *
 * Clase Derivada Automovil
 *
 * Propiedad Específica:
 * esElectrico (Boolean): Indica si el automóvil es eléctrico o no. En este caso, se refiere a un coche híbrido.
 * condicionBritania: Boolean: Propiedad de clase que Indica si el automóvil está configurado para conducción británica (volante a la derecha).
 * Comportamiento Especializado
 * calcularAutonomia() -> Int: Modifica el cálculo de autonomía asumiendo un rendimiento de 5 km menos por litro si es eléctrico.
 * Comportamiento Adicional:
 * cambiarCondicionBritania(nuevaCondicion: Boolean): Método de clase que permite modificar la configuración de conducción británica para todos los automóviles.
 * realizaDerrape()-> Float:  método que simula un derrape. Realiza una gasto adicional en el combustible,  retornando el combustible restante.  El gasto equivale a haber realizado 5 kilómetros.
 *
 * Clase Derivada Motocicleta
 *
 * Propiedad Específica:
 * cilindrada: Int: Capacidad del motor de la motocicleta.
 * Comportamiento Especializado:
 * calcularAutonomia() -> Int: Modifica el cálculo de autonomía asumiendo un rendimiento de 20 km por litro.
 * realizaViaje(distancia: Int) -> Boolean: Ajusta el cálculo de combustible necesario para viajes basándose en su autonomía específica.
 * Comportamiento Adicional:
 * realizaCaballito()-> Float: realiza una gasto adicional en el combustible,  retornando el combustible restante.  El gasto equivale a haber realizado 5 kilómetros.
 *
 * Clase Carrera
 * Logica de la carrera: Se iterará sobre la lista de vehículos. En cada iteración se elegirá uno aleatoriamente, incrementándole los kilómetros recorridos en una cantidad aleatoria entre 10 y 200. Cada vehículo realizará cada 20 km, y de forma aleatoria, una o dos filigramas (derrape, caballito). Hay que tener en cuenta que tendrá que repostar cuando se quede sin combustible, por tanto, si tiene que recorrer 100 km y tiene combustible para recorrer 10, tendrá que recorrer los 10 kilómetros, repostar y luego recorrer los 90 restantes.
 *
 *
 * Propiedades:
 * nombreCarrera: String - El nombre de la carrera para identificación.
 * distanciaTotal: Int - La distancia total que los vehículos deben recorrer para completar la carrera.
 * participantes: List<Vehiculo> - Una lista que contiene todos los vehículos participantes en la carrera.
 * estadoCarrera: Boolean - Un indicador de si la carrera está en curso o ha finalizado.
 * historialAcciones: MutableMap<String, MutableList<String>> - Un mapa para registrar el historial de acciones de cada vehículo. La clave es el nombre del vehículo y el valor es una lista de strings describiendo sus acciones.
 * posiciones: MutableList<Pair<String, Int>> - Una lista para mantener un registro de la posición y los kilómetros recorridos por cada vehículo. Cada elemento es un par donde el primer valor es el nombre del vehículo y el segundo su kilometraje acumulado.
 * Métodos:
 * iniciarCarrera(): Inicia la carrera, estableciendo estadoCarrera a true y comenzando el ciclo de iteraciones donde los vehículos avanzan y realizan acciones.
 *
 * avanzarVehiculo(vehiculo: Vehiculo): Identificado el vehículo, le hace avanzar una distancia aleatoria entre 10 y 200 km. Si el vehículo necesita repostar, se llama al método repostarVehiculo() antes de que pueda continuar. Este método llama a realizar filigranas.
 *
 * repostarVehiculo(vehiculo: Vehiculo, cantidad: Float): Reposta el vehículo seleccionado, incrementando su combustibleActual y registrando la acción en historialAcciones.
 *
 * realizarFiligrana(vehiculo: Vehiculo): Determina aleatoriamente si un vehículo realiza una filigrana (derrape o caballito) y registra la acción.
 *
 * actualizarPosiciones(): Actualiza posiciones con los kilómetros recorridos por cada vehículo después de cada iteración, manteniendo un seguimiento de la competencia.
 *
 * determinarGanador(): Revisa posiciones para identificar al vehículo (o vehículos) que haya alcanzado o superado la distanciaTotal, estableciendo el estado de la carrera a finalizado y determinando el ganador.
 *
 * obtenerResultados(): Devuelve una clasificación final de los vehículos, cada elemento tendrá el nombre del vehiculo, posición ocupada, la distancia total recorrida, el número de paradas para repostar y el historial de acciones. La collección estará ordenada por la posición ocupada.
 *
 * registrarAccion(vehiculo: String, accion: String): Añade una acción al historialAcciones del vehículo especificado.
 *
 *
 */

/**
 * Clase Vehiculo
 * @param nombre: String - Nombre del vehículo.
 * @param marca: String - Marca del vehículo.
 * @param modelo: String - Modelo del vehículo.
 * @param capacidadCombustible: Float - Capacidad total del tanque de combustible en litros.
 * @param combustibleActual: Float - Cantidad actual de combustible en litros.
 * @param kilometrosActuales: Int - Kilometraje actual del vehículo.
 * @constructor Crea un vehículo con los parámetros indicados.
 * @throws IllegalArgumentException si alguno de los parámetros no cumple las condiciones.
 *
 */
open class Vehiculo(
    val nombre: String,
    val marca: String,
    val modelo: String,
    val capacidadCombustible: Float,
    protected var combustibleActual: Float,
    protected var kilometrosActuales: Int
) {

    companion object {
        const val KM_POR_LITRO = 20.0f // 20 KM por litro.
    }

    /**
     * Calcula la autonomía del vehículo en función del combustible actual.
     * @return La autonomía del vehículo en kilómetros.
     */
    open fun calcularAutonomia(): Int {
        return (combustibleActual * KM_POR_LITRO).toInt() // Cada litro da para 10 km.
    }

    override fun toString(): String {
        return "Vehículo: $nombre, Marca: $marca, Modelo: $modelo, Kilómetros Actuales: $kilometrosActuales, Combustible Actual: $combustibleActual L."
    }

    /**
     * Obtiene la información del vehículo.
     * @return La información del vehículo.
     */
    fun obtenerInformacion(): String {
        return this.toString()
    }

    /**
     * Realiza un viaje hasta donde da combustibleActual. Ajusta el combunstible gastado y el kilometraje realizado de acuerdo con el viaje. Devuelve la distancia restante.
     * @param distanciaARecorrer: Distancia a recorrer.
     * @return La distancia restante que no se pudo recorrer por falta de combustible.
     */
    fun realizaViaje(distanciaARecorrer: Int): Int {
        val distanciaRecorrida = minOf(calcularAutonomia(), distanciaARecorrer)
        actualizaCombustible(distanciaRecorrida)
        actualizaKilometros(distanciaRecorrida)
        return distanciaARecorrer - distanciaRecorrida
    }

    /**
     * Actualiza los kilómetros recorridos.
     * @param distanciaRecorrida: Distancia recorrida.
     */
    protected fun actualizaKilometros(distanciaRecorrida: Int) {
        kilometrosActuales += distanciaRecorrida
    }

    /**
     * Actualiza el combustible en función de la distancia recorrida.
     * @param distanciaReal: Distancia recorrida.
     */
    protected fun actualizaCombustible(distanciaReal: Int) {
        val combustibleGastado = distanciaReal / KM_POR_LITRO // Cada litro da para 10 km.
        combustibleActual = floor(maxOf(0f, combustibleActual - combustibleGastado)) //Redondeo a la baja
    }

    /**
     * Incrementa combustibleActual hasta el máximo de capacidadCombustible. Cantidad tiene que ser positivo. Si no se especifica cantidad o es igual o menor que 0, se llena el tanque. Si se especifica, se llena hasta el máximo o hasta la cantidad especificada, lo que sea menor.
     * @param cantidadARepostar: Cantidad de combustible a repostar.
     * @return La cantidad de combustible repostada.
     */
    open fun repostar(cantidadARepostar: Float = 0f): Float {
        val cantidadPrevia = combustibleActual
        if (cantidadARepostar <= 0)
            combustibleActual = capacidadCombustible // LLENO
        else
            combustibleActual = minOf(capacidadCombustible, combustibleActual + cantidadARepostar)

        return combustibleActual - cantidadPrevia
    }
}

/**
 * Clase Automovil
 * @param esElectrico: Boolean - Indica si el automóvil es eléctrico o no. En este caso, se refiere a un coche híbrido.
 * @constructor Crea un automóvil con los parámetros indicados.
 * @throws IllegalArgumentException si alguno de los parámetros no cumple las condiciones.
 *
 */
class Automovil(
    nombre: String,
    marca: String,
    modelo: String,
    capacidadCombustible: Float,
    combustibleActual: Float,
    kilometrosActuales: Int,
    val esElectrico: Boolean
) : Vehiculo(nombre, marca, modelo, capacidadCombustible, combustibleActual, kilometrosActuales) {

    companion object {
        private const val KM_POR_LITRO = 10.0f // Gasto equivalente a 10 km/l.
        private const val AHORRO_ELECTRICO = 5.0f // Gasto equivalente a 10 km/l.
        private const val KM_POR_DERRAPE = 5.0f
        var condicionBritania: Boolean = false
            private set

        fun cambiarCondicionBritania(nuevaCondicion: Boolean) {
            condicionBritania = nuevaCondicion
        }
    }

    override fun calcularAutonomia(): Int {
        // Si es eléctrico, asume un rendimiento de 5 km menos por litro.
        return if (esElectrico) (combustibleActual * (KM_POR_LITRO - AHORRO_ELECTRICO)).toInt() else super.calcularAutonomia()
    }

    /**
     * Realiza el derrape aunque no quede combustible....y actualiza el combustible en función de lo gastado.
     * @return el combustible restante
     *
     */
    fun realizaDerrape(): Float {
        actualizaCombustible(KM_POR_DERRAPE.toInt())
        return combustibleActual
    }
}

class Motocicleta(
    nombre: String,
    marca: String,
    modelo: String,
    capacidadCombustible: Float,
    combustibleActual: Float,
    kilometrosActuales: Int,
    val cilindrada: Int
) : Vehiculo(nombre, marca, modelo, capacidadCombustible, combustibleActual, kilometrosActuales) {

    companion object {
        const val KM_POR_LITRO = 20.0f // 20 KM por litro.
        const val KM_POR_CABALLITO = 5 // 5 KM Gasto equivalente a 5 km.

    }

    override fun calcularAutonomia(): Int {
        // Suponemos que cada litro da para 20 km para motocicletas.
        return (combustibleActual * KM_POR_LITRO).toInt()
    }

    fun realizaCaballito(): Float {
        actualizaCombustible(KM_POR_CABALLITO)
        return combustibleActual
    }
}


/**
 * Clase Carrera
 * @param nombreCarrera: String - El nombre de la carrera para identificación.
 * @param distanciaTotal: Int - La distancia total que los vehículos deben recorrer para completar la carrera.
 * @param vehiculos: List<Vehiculo> - Una lista que contiene todos los vehículos participantes en la carrera.
 *
 */
class Carrera(
    val nombreCarrera: String,
    val distanciaTotal: Int,
    vehiculos: List<Vehiculo> = listOf<Vehiculo>()
) {
    private val participantes: MutableList<Vehiculo> = mutableListOf<Vehiculo>()
    private val historialAcciones = mutableMapOf<String, MutableList<String>>()
    private var estadoCarrera = false // Indica si la carrera está en curso o ha finalizado.
    private val posiciones = mutableMapOf<String, Int>()
    override fun toString(): String {
        return "NombreCarrera: $nombreCarrera, DistanciaTotal: $distanciaTotal, Participantes: $participantes, EstadoCarrera: $estadoCarrera, HistorialAcciones: $historialAcciones, Posiciones: $posiciones." }

    init {
        if (distanciaTotal < 1000) throw IllegalArgumentException("La distancia total de la carrera debe ser al menos 100 km.")
        vehiculos.forEach { vehiculo -> agregarParticipante(vehiculo) }
    }

    companion object {
        private const val KM_PARA_FILIGRANA = 20 // Cada 20 km, se realiza una filigrana.
    }

    /**
     * Agrega un vehículo a la carrera.
     * @param vehiculo: Vehiculo - El vehículo a agregar a la carrera.
     */
    fun agregarParticipante(vehiculo: Vehiculo) {
        participantes.add(vehiculo)
        inicializaDatosParticipante(vehiculo)
    }

    private fun inicializaDatosParticipante(vehiculo: Vehiculo) {
        historialAcciones[vehiculo.nombre] = mutableListOf()
        posiciones[vehiculo.nombre] = 0
    }

    /**
     * Se iterará sobre la lista de vehículos. En cada iteración se elegirá uno aleatoriamente, incrementándole los kilómetros recorridos en una cantidad aleatoria entre 10 y 200. Cada vehículo realizará cada 20 km, y de forma aleatoria, una o dos filigramas (derrape, caballito). Hay que tener en cuenta que tendrá que repostar cuando se quede sin combustible, por tanto, si tiene que recorrer 100 km y tiene combustible para recorrer 10, tendrá que recorrer los 10 kilómetros, repostar y luego recorrer los 90 restantes.
     *
     */
    fun iniciarCarrera() {
        estadoCarrera = true // Indica que la carrera está en curso.
        while (estadoCarrera) {
            val vehiculoSeleccionado = seleccionaVehiculoQueAvanzara()
            avanzarVehiculo(vehiculoSeleccionado)
            if (determinarGanador() != null) estadoCarrera = false
        }
    }

    private fun seleccionaVehiculoQueAvanzara() = participantes.random()

    private fun obtenerNumeroDeTramos(distancia: Int) = ceil(distancia.toDouble() / KM_PARA_FILIGRANA).toInt()


    private fun avanzarVehiculo(vehiculo: Vehiculo) {
        val distanciaTotalEnAvance = obtenerDistanciaARecorrer()
        val numeroDeTramos = obtenerNumeroDeTramos(distanciaTotalEnAvance) // Rompemos el recorrido en tramos de 20 km.
        registrarAccion(vehiculo.nombre, "Inicia viaje: A recorer $distanciaTotalEnAvance kms.")
        var distanciaRestanteEnAvance = distanciaTotalEnAvance
        repeat(numeroDeTramos) { //Tramos de KM_PARA_FILIGRANA km
            val distanciaDeTramo = minOf(KM_PARA_FILIGRANA, distanciaRestanteEnAvance)
            avanzarTramo(vehiculo, distanciaDeTramo)
            distanciaRestanteEnAvance -= distanciaDeTramo
            repeat(2) { realizarFiligrana(vehiculo) }
        }
        registrarAccion(vehiculo.nombre, "Finaliza viaje: Total Recorrido ${distanciaTotalEnAvance} kms.")
        actualizarPosiciones(vehiculo.nombre, distanciaTotalEnAvance)
    }

    private fun avanzarTramo(vehiculo: Vehiculo, distanciaEnTramo: Int) {
        var distanciaRestante = vehiculo.realizaViaje(distanciaEnTramo)
        registrarAccion(vehiculo.nombre, "Avance tramo: Recorrido ${distanciaEnTramo - distanciaRestante} kms.")
        while (distanciaRestante > 0) {
            val repostado = vehiculo.repostar()
            registrarAccion(vehiculo.nombre, "Repostaje tramo: $repostado L.")
            distanciaRestante = vehiculo.realizaViaje(distanciaRestante)
            registrarAccion(vehiculo.nombre, "Avance tramo: Recorrido ${distanciaEnTramo - distanciaRestante} kms.")
        }
    }

    private fun obtenerDistanciaARecorrer() = (10..200).random()

    private fun realizarFiligrana(vehiculo: Vehiculo) {
        // Lógica para realizar filigranas de motociletas y automovil y registrarlas. Se hará o no aleatoriamente.
        if (vehiculo is Automovil) {
            if (Math.random() < 0.5) {
                val combustibleRestante = (vehiculo as Automovil).realizaDerrape()
                registrarAccion(vehiculo.nombre, "Derrape: Combustible restante $combustibleRestante L.")
            }
        } else if (vehiculo is Motocicleta) {
            if (Math.random() < 0.5) {
                val combustibleRestante = (vehiculo as Motocicleta).realizaCaballito()
                registrarAccion(vehiculo.nombre, "Caballito: Combustible restante $combustibleRestante L.")
            }
        }
    }

    private fun actualizarPosiciones(nombreVehiculo: String, kilometraje: Int) {
        val kilometrosRecorridos = posiciones[nombreVehiculo] ?: 0
        posiciones.put(nombreVehiculo, kilometrosRecorridos + kilometraje)
    }


    private fun determinarGanador(): Vehiculo? {
        val maxPuntuacion = posiciones.maxByOrNull { it.value }
        var ganador: Vehiculo? = null
        if ((maxPuntuacion?.value ?: 0) >= distanciaTotal)
            ganador = participantes.find { it.nombre == maxPuntuacion?.key }
        return ganador
    }

    private fun registrarAccion(nombreVehiculo: String, accion: String) {
        historialAcciones[nombreVehiculo]?.add(accion)
    }

    /**
     *  Devuelve una clasificación final de los vehículos, cada elemento tendrá el nombre del vehiculo, posición ocupada, la distancia total recorrida, el número de paradas para repostar y el historial de acciones. La collección estará ordenada por la posición ocupada.
     *
     */
    fun obtenerResultados(): List<ResultadoCarrera> {
        val resultados = mutableListOf<ResultadoCarrera>()
        posiciones.toList().sortedByDescending { it.second }.forEachIndexed { posicion, (nombre, kilometraje) ->
            val vehiculo = participantes.find { it.nombre == nombre }
            val paradasRepostaje = historialAcciones[nombre]?.count { it.contains("Repostaje") } ?: 0
            val historial = historialAcciones[nombre] ?: emptyList()
            if (vehiculo != null)
                resultados.add(
                    ResultadoCarrera(
                        vehiculo,
                        posicion + 1,
                        kilometraje,
                        paradasRepostaje,
                        historial
                    )
                )
        }
        return resultados
    }

    data class ResultadoCarrera(
        val vehiculo: Vehiculo,
        val posicion: Int,
        val kilometraje: Int,
        val paradasRepostaje: Int,
        val historialAcciones: List<String>
    )

}


fun main() {

    val vehiculos = listOf(
        Automovil("Aurora", "Seat", "Panda", 50f, 50f * 0.1f, 0, true),
        Automovil("Boreal", "BMW", "Boeal", 80f, 80f * 0.1f, 0, false),
        Motocicleta("Céfiro", "Derbi", "Motoreta", 15f, 15f * 0.1f, 0, 500),
        Automovil("Dinamo", "Cintroen", "Sor", 70f, 70f * 0.1f, 0, true),
        Automovil("Eclipse", "Renault", "Espacio", 60f, 60f * 0.1f, 0, false),
        Motocicleta("Fénix", "Honda", "Vital", 20f, 20f * 0.1f, 0, 250)
    )
    val carrera = Carrera("Gran Carrera de Filigranas", 1000, vehiculos)


    println("Iniciando la carrera: ${carrera.nombreCarrera}")
    carrera.iniciarCarrera()
    println("Finalizando la carrera: ${carrera.nombreCarrera}")

    val resultado = carrera.obtenerResultados()
    println(resultado.joinToString("\n") { it.toString() })
}

