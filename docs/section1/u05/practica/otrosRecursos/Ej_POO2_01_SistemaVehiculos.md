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
