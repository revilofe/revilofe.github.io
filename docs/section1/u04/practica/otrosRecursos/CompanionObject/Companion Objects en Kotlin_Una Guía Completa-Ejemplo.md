#### **Ejemplo extendido: Creación de usuarios anónimos y normalizados**

Usando un companion object, podemos añadir lógica adicional para crear usuarios con diferentes reglas:

class **private** Usuario(val nombre: String) {  
    val id: Int

    companion object {  
        private var ultimoId \= 0

        private fun generarId(): Int {  
            ultimoId++  
            return ultimoId  
        }

		 private fun normaliza(nombre:String): String {  
  return nombre.trim().capitalize()  
		 }

        fun crearAnonimo(): Usuario {  
            return Usuario("Anónimo")  
        }

        fun crearNormalizado(nombre: String): Usuario {  
            val nombreNormalizado \= normaliza(nombre)  
            return Usuario(nombreNormalizado)  
        }  
    }

    init {  
        id \= generarId()  
    }  
}

fun main() {  
    val usuarioAnonimo \= Usuario.crearAnonimo()  
    val usuarioNormalizado \= Usuario.crearNormalizado("   martina   ")

    println("Usuario anónimo: \\${usuarioAnonimo.nombre}, ID: \\${usuarioAnonimo.id}")  
    println("Usuario normalizado: \\${usuarioNormalizado.nombre}, ID: \\${usuarioNormalizado.id}")  
}

**Salida esperada:**

Usuario anónimo: Anónimo, ID: 1  
Usuario normalizado: Martina, ID: 2  
---

Con estos conceptos, estás listo para aplicar los companion objects en tus proyectos, aprovechando su flexibilidad para centralizar lógicas comunes y mantener un código organizado. Ahora procederemos al ejercicio de aplicación práctica.

