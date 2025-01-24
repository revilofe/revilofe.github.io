package vtresvcuatro.u4

/**
 * class Persona
 * Representa a una persona con atributos básicos como peso, altura y nombre.
 * Calcula dinámicamente su IMC y permite realizar comparaciones.
 */
class Persona(var peso:Float,var altura:Float ) {
    companion object{
        const val ALTURA_MEDIA = 1.75f // Altura media de referencia.
        const val PESO_MEDIA = 70f // Peso medio de referencia.
    }

    var nombre = "" // Nombre de la persona.
    var imc:Float=0.0F
        private set // El IMC es calculado automáticamente y no puede ser modificado manualmente.
        get() = peso / (altura * altura) // Cálculo dinámico del IMC usando la fórmula estándar.

    /**
     * Constructor secundario que inicializa una persona con nombre, peso y altura.
     * @param nombre Nombre de la persona.
     * @param peso Peso en kilogramos.
     * @param altura Altura en metros.
     */
    constructor(nombre:String, peso:Float, altura:Float): this(peso,altura){
        this.nombre = nombre
    }

    /**
     * Representación en forma de cadena del objeto Persona.
     * @return Cadena con los atributos principales de la persona.
     */
    override fun toString(): String {
        return "nombre: $nombre,  peso: $peso,  altura: $altura, imc: $imc"
    }

    /**
     * Compara si dos objetos Persona son iguales basándose en sus atributos.
     * @param other Otro objeto a comparar.
     * @return true si los objetos son iguales, false en caso contrario.
     */
    override fun equals(other: Any?): Boolean {
        if (this === other) return true // Tres iguales para comparar referencias.
        if (other !is Persona) return false // Si el objeto no es de la clase Persona, no son iguales.

        if (nombre != other.nombre) return false // Si los nombres no coinciden, no son iguales.
        if (altura != other.altura) return false // Si las alturas no coinciden, no son iguales.
        if (peso != other.peso) return false // Si los pesos no coinciden, no son iguales.

        return true
    }

    /**
     * Genera un saludo personalizado con el nombre de la persona.
     * @return Cadena con el saludo.
     */
    fun saludar(): String {
        return "Hola!! soy $nombre. "
    }

    /**
     * Comprueba si la altura de la persona está por encima de la media.
     * @return true si la altura es mayor a ALTURA_MEDIA, false en caso contrario.
     */
    fun alturaEncimaMedia() = altura > ALTURA_MEDIA

    /**
     * Comprueba si el peso de la persona está por encima de la media.
     * @return true si el peso es mayor a PESO_MEDIA, false en caso contrario.
     */
    fun pesoEncimaMedia() = peso > PESO_MEDIA

    /**
     * Obtiene la descripción asociada al rango de IMC de la persona.
     * @return Cadena con la descripción del IMC.
     */
    fun obtenerDescImc() = IMCTYPE.getIMCTYPEByImc(imc).desc

    /**
     * Genera una descripción detallada de la persona incluyendo altura, peso e IMC.
     * @return Cadena con la descripción completa.
     */
    fun obtenerDesc(): String {
        var desc = "$nombre "
        desc += """con una altura de ${altura}m ${if (alturaEncimaMedia()) "(por encima de la media)" else "(Por debajo de la media)"}"""
        desc += """ y un peso de ${peso}kg ${if (pesoEncimaMedia()) "(por encima de la media)" else "(Por debajo de la media)"}"""
        desc += """ tiene un IMC de $imc ${obtenerDescImc()}"""

        return desc
    }

}

/**
 * Enum IMCTYPE
 * Representa los distintos rangos de IMC con descripciones asociadas.
 */
enum class IMCTYPE(val imcValueMin:Float,val imcValueMax:Float, val desc: String) {
    INSUFICIENTE(0F, 18.4F, "Peso insuficiente"),
    SALUDABLE(18.5F, 24.9F, "Peso saludable"),
    SOBREPESO(25.0F, 29.9F,"Sobrepeso"),
    OBESIDAD(30.0F, 100.0F, "Obesidad");

    companion object {
        /**
         * Obtiene el tipo de IMC basado en un valor dado.
         * @param imcValue Valor de IMC.
         * @return Tipo de IMC correspondiente.
         */
        fun getIMCTYPEByImc(imcValue: Float) : IMCTYPE {
            return when {
                imcValue.compareTo(INSUFICIENTE.imcValueMax) <= 0 ->  INSUFICIENTE
                imcValue.compareTo(SALUDABLE.imcValueMax) <= 0 ->  SALUDABLE
                imcValue.compareTo(SOBREPESO.imcValueMax) <= 0 ->  SOBREPESO
                else -> OBESIDAD
            }
        }
    }

}
