package vtresvcuatro.u4
/**
1. Crear una clase `Coche`, a través de la cual se pueda conocer el `color` del coche, la `marca`, el `modelo`,
el `número de caballos`, el `número de puertas` y la `matrícula`. Crear el constructor del coche, así como
el método `toString()`.

 * Marca y modelo no podrán ser blancos ni nulos y no podrán modificarse.
 * Número de caballos, número de puertas y matrícula no podrán modificarse, ni podrán ser nulos.
 * Color podrá modificarse, pero no podrá ser nulo.

2. Recuerda que Kotlin añade los getters y setters con el comportamiento por defecto, por lo que no es necesario que los
implementes, a no ser que tengas que añadir alguna funcionalidad extra.

* Modifica el atributo matricula para que no permita actualizar la matrícula con un valor que no tenga 7 caracteres.
* Los atributos de modelo la marca siempre se devolverán con la primera letra en mayúscula.
* Realiza también una modificación del atributo número de caballos, para que no permita actualizar
  el atributo `numCaballos` con un valor interior a 70, ni superior a 700.
* Realiza una modificación del atributo número de puertas, para que no permita actualizar el atributo `numPuertas`
  con un valor inferior a 3, ni superior a 5.
* Ten en cuenta todas estas condiciones a la hora de crear el constructor de la clase.

3. En el programa principal, instancia varios coches y muéstralos por pantalla. Probar las modificaciones anteriores,
modifica el número de caballos para un coche y haz lo mismo para el número de puertas, el color, la marca y modelo.
Vuelve a mostrarlos por pantalla.

* Intenta instanciar y modificar con la marca y modelo con valores nulos o blancos y comprueba que no es posible.
* Intenta instanciar y modificar con el número de caballos con un valor inferior a 70 o superior a 700 y comprueba que
  no es posible.
* Intenta instanciar y modificar con el número de puertas con un valor inferior a 3 o superior a 5 y comprueba que no
  es posible.
* Intenta instanciar y modificar con la matrícula con un valor que no tenga 7 caracteres y comprueba que no es posible.
* Intenta instanciar y modificar con el color, el número de caballos, el número de puertas y la matrícula con valores
  nulos/blancos y comprueba que no es posible.
   **/

/**
 * Clase Coche.
 * @param marca Marca del coche
 * @param modelo Modelo del coche
 * @param numCaballos Numero de caballos del coche
 * @param color Color del coche
 * @param numPuertas Numero de puertas del coche
 * @param matricula Matricula del coche
 */

class Coche(
    marca: String,
    modelo: String,
    val numCaballos: Int,
    val numPuertas: Int,
    val matricula: String,
    color: String) {

    var color: String = color
        set(value) {
            require(!value.isBlank()) { "Color no puede ser nulo o blanco" }
            field = value
        }

    var marca: String = marca
        get() = field.capitalize()

    var modelo: String = modelo
        get() = field.capitalize()

    init {
        require(!marca.isBlank()) { "Marca no puede ser nula o blanca" }
        require(!modelo.isBlank()) { "Modelo no puede ser nulo o blanco" }
        require(numCaballos in 70..700) { "El numero de caballos debe estar entre 70 y 700" }
        require(numPuertas in 3..5) { "El numero de puertas debe estar entre 3 y 5" }
        require(matricula.length == 7) { "La matricula debe tener 7 caracteres" }
        require(!color.isBlank()) { "Color no puede ser nulo o blanco" }
    }

    override fun toString(): String {
        return "Coche: marca $marca, modelo $modelo, numero de caballos $numCaballos, color $color, numero de puertas $numPuertas, matricula $matricula"
    }

}

fun main()
{
    //Creamos los coches
    println("Creamos los coches. Coche 1 con color blanco y coche 2 con color gris")
    val c1 = Coche("Opel", "Corsa", 90, 3, "ASJ8453", "Blanco")
    val c2 = Coche("reanult", "espace", 110, 5, "AHK8453", "Gris")
    println(c1)
    println(c2)
    //Modificamos los coches

    println("Modificamos los coches, cambio el color a rojo y azul")
    c1.color = "Rojo"
    c2.color = "Azul"
    println(c1)
    println(c2)
    //Intentamos modificar los coches con valores nulos o blancos
    println("Intentamos modificar los coches con valores nulos o blancos")
    try {
        c1.color = ""
        println(c1)
    } catch (e: IllegalArgumentException) {
        println(e.message)
    }
    try {
        c2.color = ""
        println(c2)
    } catch (e: IllegalArgumentException) {
        println(e.message)
    }

    println("Intentamos crear un coche 3 con valores de caballos, puertas y matricula incorrectos")
    var c3:Coche
    try {
        c3 = Coche("", "", 69, 2, "AHK845", "")
        println(c3)
    } catch (e: IllegalArgumentException) {
        println("ERROR:" + e.message)

    }

}