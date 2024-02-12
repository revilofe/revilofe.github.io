### Ejercicio: Persona y Estudiante

1. **Clases y Objetos Básicos:**
    - Crea una clase `Persona` que tenga dos propiedades: `nombre` y `edad`. Luego, en el main crea un objeto de esta clase e imprime sus propiedades.
   
    - Ejemplo:

        ```kotlin
        class Persona(val nombre: String, val edad: Int)

        fun main() {
            val persona = Persona("Juan", 25)
            println("Nombre: ${persona.nombre}, Edad: ${persona.edad}")
        }
        ```

2. **Métodos Simples:**
    - Añade un método `cumple` a la clase `Persona` que incremente la edad de la persona en uno cada vez que se llama.
    - Sobreescribe el método toString() y prográmalo para que se muestre una persona con todas sus propiedades.
      Por ejemplo "Persona (nombre = Lucía, edad = 21)".
    - En el main ejecuta el cumple de la persona y muestra su información de dos formas: accediendo a sus propiedades y mediante el método toString()
      *(recuerda que no es necesario llamar al método toString(), sino que se invocará automáticamente cuando necesite realizar la conversión del contenido a String)*
    - Ejemplo:

        ```kotlin
        class Persona(val nombre: String, var edad: Int) {
            fun cumple() {
                edad++
            }

            override fun toString(): String {
                return "Persona (nombre = $nombre, edad = $edad)"      
            } 
        }

        fun main() {
            val persona = Persona("Juan", 25)
            persona.cumple()
            println("Persona (nombre = ${persona.nombre}, edad = ${persona.edad})") // Debería mostrar 26
            println(persona) // Debería mostrar la misma información que la instrucción anterior
        }
        ```

3. **Encapsulamiento:**
    - Modifica la clase `Persona` para hacer la propiedad `edad` privada y añade un método `mostrarEdad()` para acceder a su valor.
    - Ejemplo:

        ```kotlin
        class Persona(val nombre: String, private var edad: Int) {
            fun mostrarEdad() = edad
            fun cumple() {
                edad++
            }
            override fun toString(): String {
                return "Persona (nombre = $nombre, edad = $edad)"      
            } 
        }
        ```

4. **Herencia:**
    - Crea una clase `Estudiante` que herede de `Persona` y añade una propiedad `carrera`. Las propiedades deben incluir el modificador `open` *(vuelve a dejar la propiedad edad pública)*
    - Realiza de nuevo un override de toString() para completar la información de Estudiante *(intenta usar el resultado del método de la clase padre y completarlo)*.
    - Ejemplo:

        ```kotlin
        open class Persona(open val nombre: String, open var edad: Int) {
            fun mostrarEdad() = edad
            fun cumple() {
                edad++
            }
            override fun toString(): String {
                return "Persona (nombre = $nombre, edad = $edad)"      
            } 
        }

        class Estudiante(override val nombre: String, override var edad: Int, val carrera: String) : Persona(nombre, edad) {
            //También es posible usar el método de la clase padre y completarlo...
            /*
            override fun toString(): String {
                return "${super.toString().dropLast(1)}, carrera = $carrera)"
            }
            */
            override fun toString() : String {
                return "Persona (nombre = $nombre, edad = $edad, carrera = $carrera)"
            }
        }

        fun main() {
            val estudiante = Estudiante("Laura", 20, "Ingeniería Informática")
            println("Nombre: ${estudiante.nombre}, Edad: ${estudiante.edad}, Carrera: ${estudiante.carrera}")
            println(estudiante)
        }
        ```

5. **Polimorfismo:**
    - Añade un método `actividad()` a la clase `Persona` que imprima "Lucía está realizando una actividad." y sobrescríbelo en `Estudiante` para que muestre un mensaje específico para estudiantes.
    - Crea en el main a una persona y un estudiante y muestra la actividad que realizan.
    - Ejemplo:

        ```kotlin
        open class Persona(open val nombre: String, open var edad: Int) {
            fun mostrarEdad() = edad
            fun cumple() {
                edad++
            }
            override fun toString(): String {
                return "Persona (nombre = $nombre, edad = $edad)"      
            } 
            open fun actividad() {
                println("$nombre está realizando una actividad.")
            }
        }

        class Estudiante(override val nombre: String, override var edad: Int, val carrera: String) : Persona(nombre, edad) {
            override fun toString(): String {
                return "${super.toString().dropLast(1)}, carrera = $carrera)"
            }
            override fun actividad() {
                println("$nombre está estudiando $carrera.")
            }
        }
        ```

6. **Clases y Objetos con Validación:**
    - Modifica la clase `Persona` para que no acepte nombres vacíos y edades negativas. Utiliza un constructor primario con valores por defecto para edad.
    - Prueba a crer un estudiante con una edad negativa, controlando las excepciones y mostrando el mensaje de error específico.
    - Ejemplo:

        ```kotlin
        class Persona(open val nombre: String, open var edad: Int = 0) {
            init {
                require(nombre.isNotBlank()) { "El nombre no puede estar vacío." }
                require(edad > 0) { "La edad no puede ser negativa." }
            }
            fun mostrarEdad() = edad
            fun cumple() {
                edad++
            }
            override fun toString(): String {
                return "Persona (nombre = $nombre, edad = $edad)"      
            } 
            open fun actividad() {
                println("$nombre está realizando una actividad.")
            }
        }

        fun main() {
            try {
                val estudiante = Estudiante("Pedro", -1, "Derecho")
            } catch (e: IllegalArgumentException) {
                println(e.message)
            }
        }
        ```

