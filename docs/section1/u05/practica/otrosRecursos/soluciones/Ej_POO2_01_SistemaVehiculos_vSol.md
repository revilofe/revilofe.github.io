### Ejercicio: Sistema de Vehículos

**Descripción:**
Crea una jerarquía de clases para representar diferentes tipos de vehículos. 
Cada vehículo tiene características comunes como la marca, el modelo y la capacidad de combustible, pero cada tipo tiene sus propias características y comportamientos.

**Clases a implementar:**

1. **Clase Base `Vehiculo`**
   - Propiedades comunes: marca (String), modelo (String), capacidadCombustible (Int).
   - Método `mostrarInformacion()`, que imprime la información del vehículo.
   - Método `calcularAutonomia()`, que retorna un valor Int *(Suponemos que cada litro da para 10 km.)*.

2. **Clase Derivada `Automovil`** *(hereda de Vehiculo)*
   - Propiedad específica: tipo (String), como "sedán", "SUV", "deportivo", etc.
   - Implementa el método `calcularAutonomia()` *(Suponemos que un automóvil puede hacer 100km más que el cálculo realizado en su clase base)*

3. **Clase Derivada `Motocicleta`** *(hereda de Vehiculo)*
   - Propiedad específica: cilindrada (Int).
   - Implementa el método `calcularAutonomia()` *(Suponemos que una moto puede hacer 40km menos que el cálculo realizado en su clase base)*

**Objetivo:**
Demostrar cómo se pueden crear clases derivadas de una superclase y cómo pueden extender o modificar su comportamiento.

4. Solución:

  ```kotlin
  open class Vehiculo(val marca: String, val modelo: String, val capacidadCombustible: Int) {
  
      override fun toString() = "Marca: $marca, Modelo: $modelo, Capacidad de Combustible: $capacidadCombustible"
  
      open fun calcularAutonomia(): Int {
          // Implementación básica. Puede ser más compleja dependiendo del tipo de vehículo.
          return capacidadCombustible * 10  // Ejemplo: cada litro da para 10 km.
      }
  }
  ```

  ```kotlin
  class Automovil(marca: String, modelo: String, capacidadCombustible: Int, val tipo: String) 
      : Vehiculo(marca, modelo, capacidadCombustible) {
  
      override fun calcularAutonomia(): Int {
          // Puede ser diferente dependiendo del tipo de automóvil.
          return super.calcularAutonomia() + 50 // Supongamos que los automóviles tienen 50 km extra de autonomía.
      }
  
      override fun toString() = "${super.toString()}, Tipo: $tipo"
  }
  ```

  ```kotlin
  // Clase Derivada `Motocicleta`
  class Motocicleta(marca: String, modelo: String, capacidadCombustible: Int, val cilindrada: Int) 
      : Vehiculo(marca, modelo, capacidadCombustible) {
  
      override fun calcularAutonomia(): Int {
          // La autonomía podría ser diferente para motocicletas.
          return super.calcularAutonomia() - 20 // Supongamos que las motocicletas tienen 20 km menos de autonomía.
      }
  
      override fun toString() = "${super.toString()}, Cilindrada: $cilindrada"
  }
  ```
