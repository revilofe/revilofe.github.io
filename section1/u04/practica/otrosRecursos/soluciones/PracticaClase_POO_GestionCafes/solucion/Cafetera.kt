/**
 * Clase que representa una cafetera con atributos como ubicación, capacidad y cantidad de café.
 * La capacidad máxima por defecto es 1000 c.c. y la cantidad inicial por defecto es 0 (cafetera vacía).
 * @param ubicacion Nombre de la sala o habitación donde se encuentra la cafetera.
 */
class Cafetera(val ubicacion: String) {

    var capacidad: Int = 1000
    var cantidad: Int = 0

    /**
     * Constructor secundario que permite especificar la capacidad máxima de la cafetera al crearla.
     * @param ubicacion Nombre de la sala o habitación donde se encuentra la cafetera.
     * @param capacidad Capacidad máxima de la cafetera en c.c.
     */
    constructor(ubicacion: String, capacidad: Int) : this(ubicacion) {
        this.capacidad = capacidad
        this.cantidad = capacidad
    }

    /**
     * Constructor secundario que permite especificar la capacidad máxima y la cantidad inicial de la cafetera.
     * Ajusta la cantidad inicial al máximo si es mayor que la capacidad máxima.
     * @param ubicacion Nombre de la sala o habitación donde se encuentra la cafetera.
     * @param capacidad Capacidad máxima de la cafetera en c.c.
     * @param cantidad Cantidad inicial de café en la cafetera en c.c.
     */
    constructor(ubicacion: String, capacidad: Int, cantidad: Int) : this(ubicacion) {
        this.capacidad = capacidad
        this.cantidad = if (cantidad > capacidad) capacidad else cantidad
    }

    /**
     * Llena la cafetera estableciendo la cantidad actual igual a la capacidad máxima.
     */
    fun llenar() {
        this.cantidad = this.capacidad
    }

    /**
     * Simula la acción de servir una cantidad específica de café de la cafetera.
     * Resta la cantidad servida de la cantidad actual de café en la cafetera.
     * @param cantidad Cantidad de café a servir.
     */
    fun servirCafe(cantidad: Int) {
        this.cantidad -= cantidad
    }

    /**
     * Simula la acción de servir una taza con la capacidad que tenga la taza.
     * Si la cafetera tiene café, llenará la taza y restará la cantidad servida en la cantidad de la cafetera.
     * Si la cantidad actual de café "no alcanza" para llenar la taza, se sirve lo que quede.
     * Actualiza la cantidad de la cafetera y aplica el método adecuado de la taza.
     * @param taza Taza a la que se va a servir café.
     */
    fun servirTaza(taza: Taza) {
        if (this.cantidad > 0) {
            if (this.cantidad > taza.capacidad) {
                taza.llenar()
                servirCafe(taza.capacidad)
            } else {
                taza.llenar(this.cantidad)
                vaciar()
            }
        }
    }

    /**
     * Pone la cantidad de café actual en cero.
     */
    fun vaciar() {
        this.cantidad = 0
    }

    /**
     * Añade a la cafetera la cantidad de café indicada. Por defecto, añade 50 c.c.
     * Si la cantidad sumada es igual a la capacidad máxima o excede la capacidad, llena la cafetera.
     * @param cantidad Cantidad de café a agregar (por defecto 50 c.c.).
     */
    fun agregarCafe(cantidad: Int = 200) {
        if (this.cantidad + cantidad > this.capacidad) {
            llenar()
        }
        else {
            this.cantidad += cantidad
        }
    }

    /**
     * Representación textual de la cafetera en formato de cadena.
     * @return Cadena que describe la cafetera con su ubicación, capacidad y cantidad.
     */
    override fun toString(): String {
        return "Cafetera(ubicación = ${this.ubicacion}, capacidad = ${this.capacidad} c.c., cantidad = ${this.cantidad} c.c.)"
    }
}