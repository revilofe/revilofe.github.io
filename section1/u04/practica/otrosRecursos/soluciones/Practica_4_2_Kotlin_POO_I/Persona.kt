package vtresvcuatro.u4

/**
 * class Persona
 */
class Persona(var peso:Float,var altura:Float ) {
    companion object{
        const val ALTURA_MEDIA = 1.75f
        const val PESO_MEDIA = 70f
    }

    var nombre = ""
    var imc:Float=0.0F
        private set
        get() = peso / (altura * altura)
    // IMC = peso (kg)/ [altura (m)]2

    constructor(nombre:String, peso:Float, altura:Float): this(peso,altura){
        this.nombre = nombre
    }

    override fun toString(): String {
        return "nombre: $nombre,  peso: $peso,  altura: $altura, imc: $imc"
    }

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (other !is Persona) return false

        if (nombre != other.nombre) return false
        if (altura != other.altura) return false
        if (peso != other.peso) return false

        return true
    }

    fun saludar(): String {
        return "Hola!! soy $nombre. "
    }

    fun alturaEncimaMedia() = altura > ALTURA_MEDIA
    fun pesoEncimaMedia() = peso > PESO_MEDIA
    fun obtenerDescImc() = IMCTYPE.getIMCTYPEByImc(imc).desc

    fun obtenerDesc(): String {
        var desc = "$nombre "
        desc += """con una altura de ${altura}m ${if (alturaEncimaMedia()) "(por encima de la media)" else "(Por debajo de la media)"}"""
        desc += """ y un peso de ${peso}kg ${if (pesoEncimaMedia()) "(por encima de la media)" else "(Por debajo de la media)"}"""
        desc += """ tiene un IMC de $imc ${obtenerDescImc()}"""

        return desc
    }

}

enum class IMCTYPE(val imcValueMin:Float,val imcValueMax:Float, val desc: String) {
    INSUFICIENTE(0F, 18.4F, "Peso insuficiente"),
    SALUDABLE(18.5F, 24.9F, "Peso saludable"),
    SOBREPESO(25.0F, 29.9F,"Sobrepeso"),
    OBESIDAD(30.0F, 100.0F, "Obesidad");

    companion object {
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