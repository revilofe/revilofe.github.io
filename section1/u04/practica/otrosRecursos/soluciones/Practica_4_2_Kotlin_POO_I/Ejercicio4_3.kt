package vtresvcuatro.u4



fun main(){
    val personas = listOf (Persona("Edu", 80F,1.80F),
            Persona("Juan", 67.5F, 1.5F),
            Persona("Sole", 55.5F, 1.76F),
    )

    personas.forEach{
        println(it.obtenerDesc())
    }

}
