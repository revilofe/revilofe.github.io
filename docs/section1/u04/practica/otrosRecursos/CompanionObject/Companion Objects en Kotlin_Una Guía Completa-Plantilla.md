### **Plantilla para el Ejercicio: Generador de Pokémon**

#### **Descripción del ejercicio**

En este ejercicio, implementarás una aplicación para gestionar Pokémon. Completarás una clase `Pokemon` con un **companion object** que se usará para:

1. Generar un ID único para cada Pokémon.  
2. Crear Pokémon de manera aleatoria.

También usarás la clase `GestorPokemon` para registrar y mostrar los Pokémon.

---

#### **Código base**

Te proporcionamos el siguiente código base. Completa las secciones marcadas con `TODO`.

##### **Clase `Pokemon`**

import kotlin.random.Random

class private Pokemon(val nombre: String, val tipo: String, val poderBase: Int) {  
    val id: Int

    companion object {  
        // TODO: Declara una variable para almacenar el último ID generado

        // TODO: Crea un método para generar IDs únicos

        // TODO: Crea un método para generar un Pokémon aleatorio

        // TODO: Crea un método para crear un Pokémon

    }

    init {  
        // TODO: Inicializa el ID usando el método del companion object  
    }  
}

##### **Clase `GestorPokemon`**

class GestorPokemon {  
    // TODO: Estructura en la que almacenaras tus pokemons  
    private val pokemons \=....

   // TODO: Registra tus pokemons  
   fun registrarPokemon(nombre: String, tipo: String, poderBase: Int): Pokemon {  
        …  
        return nuevoPokemon  
    }

   // TODO: Estructura en la que almacenaras tus pokemons aleatorios   
    fun registrarPokemonAleatorio(): Pokemon {  
        …  
        return pokemonAleatorio  
    }

   // TODO: Obtener los pokemons   
    fun obtenerPokemon(): ….. {  
        …  
        }  
    }  
}

##### 

##### 

##### **Programa principal**

fun main() {  
    val gestor \= GestorPokemon()

    // Registrar Pokémon manualmente  
    gestor.registrarPokemon("Pikachu", "Eléctrico", 55\)  
    gestor.registrarPokemon("Charmander", "Fuego", 52\)

    // Registrar un Pokémon aleatorio  
    println("Generando Pokémon aleatorio...")  
    gestor.registrarPokemonAleatorio()

    // TODO: Mostrar todos los Pokémon registrados  
    println("\\nLista de Pokémon registrados:")  
    var pokemon \= gestor.mostrarPokemon()

}  
---

#### **Pista para el Companion Object**

1. Usa una variable `private var` para llevar el control del último ID generado.  
   Crea una lista de triples con nombres, tipos y poderes base de Pokémon predefinidos. Por ejemplo:  
     
   private val nombresYPropiedades \= listOf(

    Triple("Pikachu", "Eléctrico", 55),  
    Triple("Charmander", "Fuego", 52),  
    Triple("Bulbasaur", "Planta", 49\)

2. Usa el método `.random()` de Kotlin para seleccionar un elemento aleatorio de la lista.

---

#### **Entregables**

1. Completa la clase `Pokemon` con el companion object.  
2. Asegúrate de que el programa genera IDs únicos y permite registrar Pokémon tanto manual como aleatoriamente.  
3. Sube el código completo y funcional.

