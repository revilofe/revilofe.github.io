### **Ejercicio: Generador de Pokémon**

#### **Descripción del ejercicio**

Vas a construir un programa para gestionar Pokémon utilizando companion objects en Kotlin. Este ejercicio te ayudará a entender cómo usar companion objects para generar IDs únicos y lógica compartida.

Tendrás dos clases principales:

1. **Clase \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*`Pokemon`**:  
   * Representará un Pokémon con los siguientes atributos:  
     * `nombre`: Nombre del Pokémon (String).  
     * `tipo`: Tipo del Pokémon (String, como "Eléctrico", "Agua").  
     * `poderBase`: Poder base del Pokémon (Int).  
     * `id`: ID único del Pokémon (generado automáticamente por el companion object).  
   * Incluirá un companion object que:  
     * Genere IDs únicos para cada Pokémon.  
     * Permita crear un Pokémon pasando parametros, y de forma aleatoria a partir de una lista predefinida.  
2. **Clase \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*`GestorPokemon`**:  
   * Gestionará una lista de Pokémon registrados.  
   * Incluirá métodos para:  
     * Registrar un Pokémon manualmente.  
     * Registrar un Pokémon aleatorio.  
     * Devolver una lista de todos los Pokémon registrados.

#### **Requisitos**

1. Implementa las clases `Pokemon` y `GestorPokemon` siguiendo la descripción.  
2. En el programa principal, crea tres Pokémon manualmente y al menos uno aleatorio.  
3. Usa el método `mostrarPokemon()` para imprimir la lista completa de Pokémon registrados.

