## Ejercicio 01: Base de datos de Empleados.

### **Contexto:** 

Este código maneja tanto la lógica de negocio de los empleados como la interacción con la base de datos dentro de la misma clase, lo cual va en contra del SRP (principio de responsabilidad única).

### **Tarea:** 

Refactoriza el código para que cumpla el SRP.

   ```kotlin
   class Empleado(val id: Int, var nombre: String, var puesto: String) {
      fun guardarEmpleado() {
          // Conexión a la base de datos
          println("Conectando a la base de datos...")
          // Lógica para guardar el empleado
          println("Empleado $nombre guardado en la base de datos")
      }
   
      fun eliminarEmpleado() {
          // Conexión a la base de datos
          println("Conectando a la base de datos...")
          // Lógica para eliminar el empleado
          println("Empleado $nombre eliminado de la base de datos")
      }
   
      fun generarInformeEmpleado() {
          // Generar un informe del empleado
          println("Generando informe para el empleado $nombre")
      }
   }
   
   fun main() {
      val empleado = Empleado(1, "Juan Pérez", "Desarrollador")
      empleado.guardarEmpleado()
      empleado.eliminarEmpleado()
      empleado.generarInformeEmpleado()
   }
   ```

### Solución refactorizada:

La solución involucra separar las responsabilidades en clases diferentes: una para manejar las operaciones de la base de datos (BaseDatosEmpleado), otra para la generación de informes (GeneradorInformeEmpleado), y 
mantenemos la clase Empleado enfocada en los datos del empleado.

   ```kotlin
   // Data class para las propiedades del empleado
   data class Empleado(val id: Int, var nombre: String, var puesto: String)
   
   // Clase para manejar las operaciones de la base de datos de empleados
   class BaseDatosEmpleado {
       fun guardarEmpleado(empleado: Empleado) {
           println("Empleado ${empleado.nombre} guardado en la base de datos")
       }
   
       fun eliminarEmpleado(empleado: Empleado) {
           println("Empleado ${empleado.nombre} eliminado de la base de datos")
       }
   }
   
   // Clase para generar informes de empleados
   class GeneradorInformeEmpleado {
       fun generarInforme(empleado: Empleado) {
           println("Generando informe para el empleado ${empleado.nombre}")
       }
   }
   
   fun main() {
       val empleado = Empleado(1, "Juan Pérez", "Desarrollador")
       val dbEmpleado = BaseDatosEmpleado()
       val generadorInforme = GeneradorInformeEmpleado()
   
       dbEmpleado.guardarEmpleado(empleado)
       dbEmpleado.eliminarEmpleado(empleado)
       generadorInforme.generarInforme(empleado)
   }
   ```
