
## Ejercicio 1: Clase Cuenta Bancaria

Crea una clase CuentaBancaria con las propiedades:
   - titular (de tipo String).
   - saldo (de tipo Double).

La clase debe tener:
   1. Un constructor que inicialice el titular con el saldo en 0 por defecto.
   2. Métodos para:
      - Ingresar dinero (ingresar).
      - Retirar dinero (retirar). Este método debe lanzar una excepción si se intenta retirar más dinero del que hay en la cuenta.

A tener en cuenta:
   1. El saldo no podrá ser modificado directamente desde fuera de la clase. Solo será posible su cambio mediante los métodos ingresar y retirar.
   2. Los métodos ingresar y retirar debe mostrar un mensaje con el saldo final después de la operación.
   3. No será posible retirar más dinero del saldo actual, ni ingresar cantidades negativas o 0. Deberá generar una excepción si ocurre esta situación.

En el programa principal:
   - Crea una cuenta bancaria con un titular.
   - Realiza un ingreso de 100.0 y un retiro de 50.0.
   - Intenta realizar un retiro que supere el saldo y captura la excepción.

Solución:

```kotlin
class CuentaBancaria(val titular: String) {
    var saldo: Double = 0.0
        private set

    fun ingresar(cantidad: Double) {
        require(cantidad > 0) { "La cantidad debe ser positiva." }
        saldo += cantidad
        println("Ingreso realizado. Saldo actual: $saldo")
    }

    fun retirar(cantidad: Double) {
        require(cantidad > 0) { "La cantidad debe ser positiva." }
        if (cantidad > saldo) {
            throw IllegalArgumentException("Saldo insuficiente.")
        }
        saldo -= cantidad
        println("Retiro realizado. Saldo actual: $saldo")
    }
}

fun main() {
    val cuenta = CuentaBancaria("Luis")

    cuenta.ingresar(100.0)
    cuenta.retirar(50.0)

    try {
        cuenta.retirar(100.0)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

## Ejercicio 2: Clase Vehículo

Crea una clase Vehiculo con las propiedades:
   - marca.
   - modelo.
   - kilometraje.

La clase debe tener:
   1. Métodos para registrar un viaje que aumente el kilometraje.
   2. Un método detalles que devuelva una descripción del vehículo o modificar el método toString.

En el programa principal:
   - Crea un vehículo, registra un viaje de 100 km y muestra sus detalles.

Solución:

```kotlin
class Vehiculo(val marca: String, val modelo: String) {
    var kilometraje: Int = 0
        private set

    fun registrarViaje(kilometros: Int) {
        require(kilometros > 0) { "La distancia debe ser mayor que 0." }
        kilometraje += kilometros
    }

    fun detalles(): String {
        return "Vehículo $marca $modelo con $kilometraje km."
    }
}

fun main() {
    val vehiculo = Vehiculo("Toyota", "Corolla")
    vehiculo.registrarViaje(100)
    println(vehiculo.detalles())
}
```

## Ejercicio 3: Clase Libro

Crea una clase Libro con las propiedades:
   - titulo (de tipo String).
   - autor (de tipo String).
   - numPaginas (de tipo Int).
   - leido (de tipo Boolean, inicializado en false).

La clase debe:
   1. Sobrescribir el método toString para mostrar: "Libro: [titulo] por [autor], Páginas: [numPaginas], Leído: [Sí/No]".
   2. Incluir un constructor secundario que inicialice numPaginas y leido con valores predeterminados.

A tener en cuenta:
   1. las propiedades titulo, autor y numPaginas serán propiedades inmutables.
   2. titulo y autor no pueden ser cadenas vacías.
   3. numPaginas debe ser un valor positivo, no superior a 5000.
   4. Por defecto un libro tiene 100 páginas si no se especifica al inicializarlo.

En el programa principal:
   - Crea dos libros, marca uno como leído e imprime el valor de cada libro.
   - Crea un libro con titulo vacío que muestre el mensaje de error correspondiente (acuérdate de capturar las excepciones).

Solución:

```kotlin
class Libro(titulo: String, autor: String, numPaginas: Int, var leido: Boolean = false) {
    constructor(titulo: String, autor: String) : this(titulo, autor, 100, false)

    val titulo: String = "Sin titulo"
    init {
        require(titulo.isNotEmpty()) { "El título no puede estar vacío." }
    }

    val autor: String = "Sin Autor"
    init {
        require(nombre.isNotEmpty()) { "El autor no puede estar vacío." }
    }

    val numPaginas: Int = 0
    init {
        require(numPaginas in 1..5000) { "El número de páginas debe estar en el rango 1-5000." }
    }

    fun marcarComoLeido() {
        leido = true
    }

    override fun toString(): String {
        return "Libro: $titulo por $autor, Páginas: $numPaginas, Leído: ${if (leido) "Sí" else "No"}"
    }
}

fun main() {
    val libro1 = Libro("El Hobbit", "J.R.R. Tolkien")
    val libro2 = Libro("1984", "George Orwell", 328, true)

    libro1.marcarComoLeido()

    println(libro1)
    println(libro2)

    val libro3 = try {
        Libro("", "")
    } catch (3: IllegalArgumentException) {
        println("ERROR: ${e.message}!")
    }

    println(libro3)
}
```

## Ejercicio 4: Clase Estudiante

Crea una clase Estudiante con las propiedades:
   - nombre
   - nota

La clase debe:
   1. Modificar el setter de nota para asegurarse de que esté en el rango 0-10.
   2. Sobrescribir el método toString para mostrar: "Estudiante: [nombre], Nota: [nota]".

A tener en cuenta:
   1. El nombre del estudiante no se podrá modificar una vez inicializado un objeto de tipo Estudiante.
   2. La propiedad nombre no puede ser tampoco visible desde fuera de la clase Estudiante.

En el programa principal:
   - Crea varios estudiantes, intenta asignarles notas fuera del rango y muestra sus detalles.

Solución:

```kotlin
class Estudiante(private val nombre: String, notaInicial: Double) {
    var nota: Double = notaInicial
        set(value) {
            require(value in 0.0..10.0) { "La nota debe estar entre 0 y 10." }
            field = value
        }

    init {
        require(notaInicial in 0.0..10.0) { "La nota inicial debe estar entre 0 y 10." }
    }

    override fun toString(): String {
        return "Estudiante: $nombre, Nota: $nota"
    }
}

fun main() {
    try {
        val estudiante1 = Estudiante("Laura", 7.5)
        val estudiante2 = Estudiante("Pedro", 11.0) // Lanza excepción

        estudiante1.nota = 9.0
        println(estudiante1)
        println(estudiante2)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

## Ejercicio 5: Clase Producto

Crea una clase Producto con las propiedades:
   - nombre
   - precio
   - stock

La clase debe:
   1. Utilizar un bloque init para asegurarse de que el precio y el stock sean positivos.
   2. Sobrescribir el método toString para mostrar: "Producto: [nombre], Precio: [precio]€, Stock: [stock]".
   3. Métodos vender y readastecer, que actualizarán el stock. Realizar los controles que veáis adecuados.
   4. Las propiedades precio y stock no pueden ser modificadas directamente desde fuera de la clase Producto.

En el programa principal:
   - Crea varios productos, usa sus métodos y muestra sus detalles.

Solución:

```kotlin
class Producto(val nombre: String, precioInicial: Double, stockInicial: Int) {
    var precio: Double = precioInicial
        private set
    var stock: Int = stockInicial
        private set

    init {
        require(precioInicial > 0) { "El precio debe ser mayor que 0." }
        require(stockInicial >= 0) { "El stock no puede ser negativo." }
    }

    fun vender(cantidad: Int) {
        require(cantidad > 0) { "La cantidad debe ser positiva." }
        if (cantidad > stock) {
            throw IllegalArgumentException("Stock insuficiente.")
        }
        stock -= cantidad
    }

    fun reabastecer(cantidad: Int) {
        require(cantidad > 0) { "La cantidad debe ser positiva." }
        stock += cantidad
    }

    override fun toString(): String {
        return "Producto: $nombre, Precio: $precio€, Stock: $stock"
    }
}

fun main() {
    try {
        val producto1 = Producto("Manzana", 0.5, 100)
        val producto2 = Producto("Plátano", -0.3, 50) // Lanza excepción

        producto1.vender(10)
        println(producto1)
    } catch (e: IllegalArgumentException) {
        println("Error: ${e.message}")
    }
}
```

