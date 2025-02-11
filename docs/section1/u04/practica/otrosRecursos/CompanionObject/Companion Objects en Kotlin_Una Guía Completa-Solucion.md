#### **Pista de implementación**

##### **Clase `Pokemon`**

```kotlin 
class Pokemon private constructor(val nombre: String, val tipo: String, val poderBase: Int) {
val id: Int

    companion object {
        private var ultimoId = 0
        private val nombresYPropiedades = listOf(
            Triple("Pikachu", "Eléctrico", 55),
            Triple("Charmander", "Fuego", 52),
            Triple("Bulbasaur", "Planta", 49),
            Triple("Squirtle", "Agua", 48),
            Triple("Jigglypuff", "Normal", 45),
            Triple("Meowth", "Normal", 40),
            Triple("Eevee", "Normal", 55),
            Triple("Snorlax", "Normal", 110),
            Triple("Gengar", "Fantasma", 65),
            Triple("Dragonite", "Dragón", 134)
        )

        private fun generarId(): Int {
            return ++ultimoId
        }

        fun generarPokemonAleatorio(): Pokemon {
            val (nombre, tipo, poderBase) = nombresYPropiedades.random()
            return crearPokemon(nombre, tipo, poderBase)
        }

        fun crearPokemon(nombre: String, tipo: String, poderBase: Int): Pokemon {
            return Pokemon(nombre, tipo, poderBase)
        }
    }

    init {
        id = generarId()
    }
}
```
##### **Clase `GestorPokemon`**
```kotlin 
class GestorPokemon {
    private val pokemons = mutableListOf<Pokemon>()

    fun registrarPokemon(nombre: String, tipo: String, poderBase: Int): Pokemon {
        val nuevoPokemon = Pokemon.crearPokemon(nombre, tipo, poderBase)
        pokemons.add(nuevoPokemon)
        return nuevoPokemon
    }

    fun registrarPokemonAleatorio(): Pokemon {
        val pokemonAleatorio = Pokemon.generarPokemonAleatorio()
        pokemons.add(pokemonAleatorio)
        return pokemonAleatorio
    }

    fun obtenerPokemon() : List<Pokemon> {
        return pokemons.toList()
    }
}

```

##### **Programa principal**
```kotlin
fun main() {
    val gestor = GestorPokemon()

    // Registrar Pokémon manualmente
    gestor.registrarPokemon("Pikachu", "Eléctrico", 55)
    gestor.registrarPokemon("Charmander", "Fuego", 52)

    // Registrar un Pokémon aleatorio
    println("Generando Pokémon aleatorio...")
    val pokemonAleatorio = gestor.registrarPokemonAleatorio()
    println("¡Ha aparecido un \${pokemonAleatorio.nombre} de tipo \${pokemonAleatorio.tipo} con poder base \${pokemonAleatorio.poderBase}!")

    // Mostrar todos los Pokémon registrados
    println("\nLista de Pokémon registrados:")
    gestor.obtenerPokemon().forEach { pokemon ->
        println("ID: ${pokemon.id}, Nombre: ${pokemon.nombre}, Tipo: ${pokemon.tipo}, Poder Base: ${pokemon.poderBase}")
    }
}

```

#### **Salida esperada**

Generando Pokémon aleatorio...

¡Ha aparecido un Eevee de tipo Normal con poder base 55\!

Lista de Pokémon registrados:

ID: 1, Nombre: Pikachu, Tipo: Eléctrico, Poder Base: 55

ID: 2, Nombre: Charmander, Tipo: Fuego, Poder Base: 52

ID: 3, Nombre: Eevee, Tipo: Normal, Poder Base: 55

#### **Extensiones opcionales**

1. Agrega un método para buscar Pokémon por tipo.  
2. Implementa un sistema de combate entre dos Pokémon.  
3. Permite actualizar los atributos de un Pokémon existente.

