package vtresvcuatro.u4

class Rectangulo(val base:Int, val altura:Int){

    init {
        require(base>0 && altura>0) { "Atributos de construcción erróneos" }
    }
    fun area() = base * altura
    fun perimetro() = 2*base + 2*altura

    override fun toString(): String {
        return "base: $base, altura: $altura"
    }
}

fun main(){
    val rectanguloUno = Rectangulo(2,2)
    try {
        val rectanguloDos = Rectangulo(0, 0)
    } catch (e:IllegalArgumentException) {
        println("*********** Error creando rectángulo.")
        println(e)
    }
    val rectanguloDos = Rectangulo(10, 5)

    println("*********** Rectangulo 1")
    println(rectanguloUno)
    println("Área: ${rectanguloUno.area()}")
    println("Perímetro: ${rectanguloUno.perimetro()}")
    println("*********** Rectangulo 2")
    println(rectanguloDos)
    println("Área: ${rectanguloDos.area()}")
    println("Perímetro: ${rectanguloDos.perimetro()}")
}

