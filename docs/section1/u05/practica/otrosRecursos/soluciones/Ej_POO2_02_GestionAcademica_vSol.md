### Ejercicio: Sistema de Gestión Académica

**Descripción:**
Crea una jerarquía de clases para representar distintos roles en un entorno académico, como estudiantes y profesores.

**Clases a implementar:**

1. **Clase Base `Persona`**
   - Propiedades comunes: nombre (String), edad (Int), id (String).
   - Método `mostrarRol()`, que imprime el rol de la persona (Estudiante, Profesor, etc.).

2. **Clase Derivada `Estudiante`**
   - Propiedades específicas: curso (String), calificacionPromedio (Double).
   - Implementa el método `mostrarRol()` y añade un método `mostrarCalificacion()` para imprimir la calificación promedio.

3. **Clase Derivada `Profesor`**
   - Propiedades específicas: departamento (String), aniosExperiencia (Int).
   - Implementa el método `mostrarRol()` y añade un método `mostrarExperiencia()` para imprimir los años de experiencia.

**Objetivo:**
Familiarizarse con la herencia y cómo las clases derivadas pueden tener propiedades y métodos adicionales, así como comportamientos específicos.

4. **Solución:**

```kotlin
// Clase Base `Persona`
open class Persona(val nombre: String, val edad: Int, val id: String) {

    // Método `mostrarRol()`
    open fun mostrarRol() {
        println("Persona: $nombre, Id: $id")
    }

    // Método `toString()`
    override fun toString() = "Nombre: $nombre, Edad: $edad, Id: $id"
}
```

```kotlin
// Clase Derivada `Estudiante`
class Estudiante(nombre: String, edad: Int, id: String, val curso: String, val calificacionPromedio: Double) 
    : Persona(nombre, edad, id) {

    // Implementación de `mostrarRol()`
    override fun mostrarRol() {
        println("Estudiante: $nombre, Curso: $curso, Id: $id")
    }

    // Método `mostrarCalificacion()`
    fun mostrarCalificacion() {
        println("Calificación Promedio de $nombre es $calificacionPromedio")
    }

    // Método `toString()`
    override fun toString() = "${super.toString()}, Curso: $curso, Calificación Promedio: $calificacionPromedio"
}
```

```kotlin
// Clase Derivada `Profesor`
class Profesor(nombre: String, edad: Int, id: String, val departamento: String, val aniosExperiencia: Int) 
    : Persona(nombre, edad, id) {

    // Implementación de `mostrarRol()`
    override fun mostrarRol() {
        println("Profesor: $nombre, Departamento: $departamento, Id: $id")
    }

    // Método `mostrarExperiencia()`
    fun mostrarExperiencia() {
        println("El profesor $nombre tiene $aniosExperiencia años de experiencia")
    }

    // Método `toString()`
    override fun toString() = "${super.toString()}, Departamento: $departamento, Años de Experiencia: $aniosExperiencia"
}
```
