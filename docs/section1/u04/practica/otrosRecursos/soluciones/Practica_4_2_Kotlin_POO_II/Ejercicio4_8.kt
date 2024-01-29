package vtresvcuatro.u4


/**
 *
 * Ejercicio 5.10
 * Queremos mantener una colección de los libros que hemos ido leyendo, poniéndoles una calificación
 * según nos haya gustado más o menos al leerlo.
 * Para ello, crear la clase Libro, cuyos atributos son el título, el autor, el número de páginas y
 * la calificación que le damos entre 0 y 10. Crear los métodos para poder modificar y obtener los
 * atributos (sólo si tienen sentido).
 * Posteriormente, crear una clase ConjuntoLibros, que almacena un conjunto de libros (con un vector
 * de un tamaño fijo). Se pueden añadir libros que no existan (siempre que haya espacio), eliminar
 * libros por título o autor, mostrar por pantalla los libros con la mayor y menor calificación y,
 * por último, mostrar un contenido de todo el conjunto.
 * En el programa principal realizar las siguientes operaciones: crear dos libros, añadirlos al
 * conjunto, eliminarlos por los dos criterios (título y autor) hasta que el conjunto esté vacío,
 * volver a añadir un libro y mostrar el contenido final.
 */


/**
 * Clase Libro.
 * @param titulo Título del libro. No puede ser nulo ni vacío.
 * @param autor Autor del libro. No puede ser nulo ni vacío.
 * @param numeroPaginas Número de páginas del libro. Debe ser mayor que 10.
 * @param calificacion Calificación del libro. Debe estar entre 1 y 10.
 * @throws IllegalArgumentException si alguno de los parámetros no cumple las condiciones.
 * @property titulo Título del libro. No puede ser nulo ni vacío.
 * @property autor Autor del libro. No puede ser nulo ni vacío.
 * @property numeroPaginas Número de páginas del libro. Debe ser mayor que 10.
 * @property calificacion Calificación del libro. Debe estar entre 1 y 10.
 * @constructor Crea un libro con los parámetros indicados.
 * @throws IllegalArgumentException si alguno de los parámetros no cumple las condiciones.
 *
 */
class Libro(
    val titulo: String,
    val autor: String,
    private val numeroPaginas: Int,
    calificacion: Int = 1
) {

    companion object{
        const val MINIMO_PAGINAS = 10
        const val MINIMO_CALIFICACION = 1
        const val MAXIMO_CALIFICACION = 10
    }
    var calificacion: Int = calificacion
        set(value) {
            require(calificacion in MINIMO_CALIFICACION..MAXIMO_CALIFICACION) { "Calificación errónea" }
            field = value
        }

    init {
        require(titulo.isNotEmpty()) { "Titulo del libro erróneo" }
        require(autor.isNotEmpty()) { "Autor del libro erróneo" }
        require(numeroPaginas > MINIMO_PAGINAS) { "Numero de páginas erróneas" }
    }


    override fun toString(): String {
        return "LIBRO: Titulo - '$titulo', Autor - '$autor', Paginas ($numeroPaginas), Calificación [$calificacion]"
    }
}

/**
 * Clase conjunto de libros, que almacena un conjunto de libros. Se pueden añadir libros que no existan
 * (siempre que haya espacio), eliminar libros por título o autor, mostrar por pantalla los libros
 * con la mayor y menor calificación y, por último, mostrar un contenido de todo el conjunto.
 * @param capacidadAlmacenamiento Capacidad de almacenamiento del conjunto. Debe ser mayor que 1.
 * @throws IllegalArgumentException si alguno de los parámetros no cumple las condiciones.
 * @property capacidadAlmacenamiento Capacidad de almacenamiento del conjunto. Debe ser mayor que 1.
 * @property totalLibrosAlmacenados Total de libros almacenados en el conjunto.
 * @constructor Crea un conjunto de libros con la capacidad indicada.
 */
class ConjuntoLibros(
    private val capacidadAlmacenamiento: Int
) {
    private val libros: Array<Libro?> = arrayOfNulls(capacidadAlmacenamiento)
    private var totalLibrosAlmacenados = 0
    init {
        require(capacidadAlmacenamiento > 1) { "Error en el número de libros." }
    }


    /**
     * Introduce un libro.
     * @param libro Libro a introducir.
     * return: Devuelve el total de libros.
     */
    fun introducir(libro: Libro): Int {
        if (totalLibrosAlmacenados < capacidadAlmacenamiento) // ¿Hay espacio?
            if (libros.none { it?.titulo.equals(libro.titulo) }) { // ¿No existe ya?
                libros[libros.indexOfFirst { it == null }] = libro
                totalLibrosAlmacenados++
            }
        return totalLibrosAlmacenados
    }

    /**
     * Elimina los libros que cumplen condicion.
     * @param condicion Condición que debe cumplir el libro para ser eliminado.
     * return: Devuelve el total de libros.
     */
    fun eliminar(condicion: (Libro?) -> Boolean): Int {
        var pos: Int
        do {
            pos = libros.indexOfFirst { condicion(it) }
            if (pos >= 0) {
                libros[pos] = null
                totalLibrosAlmacenados--
            }
        } while (pos >= 0)
        return totalLibrosAlmacenados
    }

    /**
     * Convierte a String el contenido de todo el conjunto
     */
    override fun toString(): String {
        var sConjunto = ""
        libros.forEachIndexed { index, libro -> sConjunto += if (libro != null) "[$index] $libro \n" else "" }
        return sConjunto
    }

    /**
     * Obtiene el libro con calificacion maxima.
     * return: un libro
     */
    fun obtenerPorCalificacionMax(): Libro? = obtenerSegunComparacion { libroConCalificacionMayor, otroLibro ->
        (libroConCalificacionMayor?.calificacion ?: 0) > (otroLibro?.calificacion ?: 0)
    }

    /**
     * Obtiene el libro con calificacion minima.
     * return: un libro
     */
    fun obtenerPorCalificacionMin(): Libro? = obtenerSegunComparacion { libroConCalificacionMenor, otroLibro ->
        (libroConCalificacionMenor?.calificacion ?: (Libro.MAXIMO_CALIFICACION + 1)) < (otroLibro?.calificacion
            ?: (Libro.MAXIMO_CALIFICACION + 1))
    }

    /**
     * Obtiene un libro que cumple una condición de comparación con el resto de libros.
     * @param comparacion Condición de comparación.
     * @return Un libro que cumple la condición de comparación.
     */
    private fun obtenerSegunComparacion(comparacion: (Libro?, Libro?) -> Boolean): Libro? {

        var libroQueCumpleComparacion: Libro? = null

        if (totalLibrosAlmacenados > 0) {
            libroQueCumpleComparacion = libros[0]
            libroQueCumpleComparacion = libros.reduce { libroQueCumpleComparacion, otroLibro ->
                if (comparacion(
                        libroQueCumpleComparacion,
                        otroLibro
                    )
                ) libroQueCumpleComparacion else otroLibro
            }
        }
        return libroQueCumpleComparacion

    }
}


fun main() {
    println("Programa que trabaja con libros!")

    val conjunto = ConjuntoLibros(10)
    // Crea dos libros y un conjunto
    listOf(
        Libro("Kotlin in action", "Antonio Guiri", 300, 6),
        Libro("Kotlin Reference", "Jose Guiri", 150, 9),
        Libro("Kotlin Chulo", "Apañao Guiri", 50, 10),
        Libro("Kotlin guay", "Una Guiri", 50),
        Libro("Kotlin ++", "Maria Guiri", 150, 9),
    ).forEach {    // Añadelos al conjunto
        conjunto.introducir(it)
    }
    println("TODOS Los libros")
    println(conjunto)

    // Eliminalos por los dos criterios (título y Autor) hasta que esté vacio.
    conjunto.eliminar { "Kotlin in action" == it?.titulo }
    println("eliminado kotlin in action")
    println(conjunto)

    conjunto.eliminar { "Una Guiri" == it?.autor }
    println("eliminado Una Guiri")
    println(conjunto)

    // Añade un libro
    conjunto.introducir(Libro("Reference of Kotlin", "Pepe Guiri", 150, 8))
    conjunto.introducir(Libro("Kotlin se secas", "Android Guiri", 150))

    // Mostrar el contenido final
    println(conjunto)

    println("Libro Mayor: ")
    println(conjunto.obtenerPorCalificacionMax())

    println("Libro Menor: ")
    println(conjunto.obtenerPorCalificacionMin())
}
