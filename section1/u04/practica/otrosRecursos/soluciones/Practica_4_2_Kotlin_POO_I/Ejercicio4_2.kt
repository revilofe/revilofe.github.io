package vtresvcuatro.u4



fun main(){
    val personaUno = Persona(80F,1.80F)
    val personaDos = Persona("Juan", 67.5F, 1.5F)
    val personaTres = Persona("Juan", 67.5F, 1.5F)

    println("*******************************************")
    println("Persona 1: $personaUno")
    println("Persona 2: $personaDos")
    println("Persona 3: $personaTres")

    println("*******************************************")
    val nombre = pideNombreAlUsuario()
    personaUno.nombre = nombre
    println("Persona 1")
    println("nombre: ${personaUno.nombre}")
    println("peso: ${personaUno.peso}")
    println("altura: ${personaUno.altura}")
    println("*******************************************")

    println("Persona 3")
    println("peso: ${personaTres.peso}")
    println("altura: ${personaTres.altura}")
    println("imc: ${personaTres.imc}")
    println("Modificado altura a 1.80 en P3")
    personaTres.altura = 1.80F
    println("Persona 3")
    println("peso: ${personaTres.peso}")
    println("altura: ${personaTres.altura}")
    println("imc: ${personaTres.imc}")
    println("*******************************************")

    println("Modificado altura a 1.80 en P2")
    personaDos.altura = 1.80F
    println("Persona 2: $personaDos")
    println("Persona 3: $personaTres")
    println("Persona 2 y 3 ${if (personaTres == personaDos) "iguales." else "distintas."}")
}

fun pideNombreAlUsuario(): String {
    var nombre:String
    do {
        print("Introduzca el nombre de la persona: ")
        nombre = readln()
    }while (nombre.isBlank())
    return nombre
}

