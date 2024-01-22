package vtresvcuatro.u4

/**
 * Ejercicio 3.3.1
 * Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
 *
 * [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]
 * Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
 *
 * ### **Ejercicio 4.6**
 *
 *    1. Realizar el ejercicio 1 de Conjuntos de los "Ejercicios básicos con Kotlin" (Ejercicio 3.3.1) orientado a objetos.
 *
 *    2. Te proporciono algunas pistas de una posible solución:
 *
 *       ```
 *       /**
 *       * Clase Compra
 *       * @param cliente cliente que realizo la compra
 *       * @param dia dia de la compra
 *       * @param monto monto de la compra
 *       * @constructor Crea una compra con cliente, dia y monto
 *       */
 *       ```
 *       ```
 *       /**
 *        * Clase Cliente
 *        * @param nombre nombre del cliente
 *        * @param domicilio domicilio del cliente
 *        * @constructor Crea un cliente con nombre y domicilio
 *        */
 *        ```
 *       ```
 *       /**
 *        * Clase Domicilio
 *        * @param calle calle del domicilio
 *        * @param numero numero del domicilio
 *        * @constructor Crea un domicilio con calle y numero
 *        */
 *       ```
 *
 *    3. La clase Domicilio tendrá un método llamado dirCompleta()que retornará el domicilio completo con la calle y el número.
 *
 *    4. Las clases Compra, Cliente y Domicilio se establecerán como data class, es decir, delante de class incluirán el modificador data en la declaración de dichas clases.
 *
 *    5. Para entender mejor que es una data class, visualizar el siguiente enlace: [Data classes](https://revilofe.github.io/section1/u04/teoria/PROG-U4.3.-kotlinPOO/#data-classes)
 *
 *       ```
 *       /**
 *        * Clase RepositorioCompras
 *        * @constructor Crea un repositorio de compras
 *        */
 *       ```
 *
 *    6. La clase `RepositorioCompras` tendrá un método para agregar una compra al repositorio y un método domicilios para retornar los domicilios de cada cliente al cual se le debe enviar una factura de compra.
 *       Esta función retorna una estructura que contenga cada domicilio una sola vez.
 *
 ***/



/**
 * Clase compra
 * @param cliente cliente que realizo la compra
 * @param dia dia de la compra
 * @param monto monto de la compra
 * @constructor Crea una compra con cliente, dia y monto
 *
 */
data class Compra(val cliente: Cliente, val dia: Int, val monto: Double)

/**
 * Clase Cliente
 * @param nombre nombre del cliente
 * @param domicilio domicilio del cliente
 * @constructor Crea un cliente con nombre y domicilio
 *
 */
data class Cliente(val nombre: String, val domicilio: Domicilio)

/**
 * Clase Domicilio
 * @param calle calle del domicilio
 * @param numero numero del domicilio
 * @constructor Crea un domicilio con calle y numero
 *
 */
data class Domicilio(val calle: String, val numero: String) {
    fun completo() = "$calle, $numero"
}

/**
 * Clase RepositorioCompras
 *
 * @constructor Crea un repositorio de compras
 *
 */
class RepositorioCompras {
    private val compras = mutableListOf<Compra>()

    /**
     * Agrega una compra al repositorio
     * @param compra compra a agregar
     *
     */
    fun agregar(compra: Compra) {
        compras.add(compra)
    }

    /**
     * Retorna los domicilios de cada cliente al cual se le debe enviar una factura de compra. La función retorna una estructura que contenga cada domicilio una sola vez.
     * @return lista de domicilios
     *
     */
    fun domicilios(): List<Domicilio> {
        return compras.map { compra -> compra.cliente.domicilio }.toSet().toList()
    }
}

fun main() {
    val repositorioCompras = RepositorioCompras()

    repositorioCompras.agregar(Compra(Cliente("Nuria Costa", Domicilio("Calle Las Flores", "355")), 5, 12780.78))
    repositorioCompras.agregar(Compra(Cliente("Jorge Russo", Domicilio("Mirasol", "218")), 7, 699.0))
    repositorioCompras.agregar(Compra(Cliente("Nuria Costa", Domicilio("Calle Las Flores", "355")), 7, 532.90))
    repositorioCompras.agregar(Compra(Cliente("Julián Rodriguez", Domicilio("La Mancha", "761")), 12, 5715.99))
    repositorioCompras.agregar(Compra(Cliente("Jorge Russo", Domicilio("Mirasol", "218")), 15, 958.0))

    val domicilios = repositorioCompras.domicilios()


    for (d in domicilios)
        println(d.completo())

}

