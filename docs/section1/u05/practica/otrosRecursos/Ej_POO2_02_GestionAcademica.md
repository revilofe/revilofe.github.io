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

