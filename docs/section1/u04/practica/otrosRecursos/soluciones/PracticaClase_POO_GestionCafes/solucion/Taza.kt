/**
 * Clase que representa una taza con atributos como color, capacidad y cantidad de líquido.
 * El color por defecto es blanco y la capacidad por defecto es 50 c.c. La cantidad se establece inicialmente en 0.
 * @param color Color de la taza (por defecto blanco).
 * @param capacidad Capacidad de la taza en c.c. (por defecto 50).
 */
class Taza(val color: Color = Color.BLANCO, val capacidad: Int = 50) {

    /**
     * Cantidad de líquido actual en la taza.
     * Si el valor que recibe es mayor que la capacidad de la taza, solo establece el valor de dicha capacidad.
     */
    var cantidad = 0
        set(value) {
            field = if (value > this.capacidad) this.capacidad else value
        }

    /**
     * Llena la taza estableciendo la cantidad igual a su capacidad máxima.
     */
    fun llenar() {
        this.cantidad = this.capacidad
    }

    /**
     * Llena la taza estableciendo la cantidad según el valor pasado como argumento.
     * @param cantidad Cantidad de líquido con la que se llenará la taza.
     */
    fun llenar(cantidad: Int) {
        this.cantidad = cantidad
    }

    /**
     * Representación textual de la taza en formato de cadena.
     * @return Cadena que describe la taza con su color, capacidad y cantidad.
     */
    override fun toString(): String {
        return "Taza(color = ${this.color}, capacidad = ${this.capacidad} c.c., cantidad = ${this.cantidad} c.c.)"
    }
}