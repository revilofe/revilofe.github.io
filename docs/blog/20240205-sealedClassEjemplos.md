---
title: Clases selladas en detalle con varios ejemplos.

description: Clases selladas en detalle con varios ejemplos.

authors:
    - Diego Cano.

date: 2024-02-05

tags:
  - atributo de clase
  - propiedad
  - kotlin
---
# Clases selladas en detalle con varios ejemplos.

## Sealed Class

Las clases selladas (`sealed class`) en Kotlin son una característica especial que se utiliza para representar jerarquías de 
clases restringidas, en las cuales una clase tiene un número limitado de subtipos. 
Se utilizan principalmente cuando se desea que un valor pueda ser de uno entre varios tipos, pero no de cualquier otro tipo. 
Son especialmente útiles en el manejo de estados o en la implementación del patrón de diseño de Visitor.

Algunas características clave de las clases selladas:

1. **Extensibilidad limitada**: Solo las clases que están en el mismo archivo que la clase sellada pueden extenderla.
   Esto asegura que todos los subtipos sean conocidos en tiempo de compilación y ayuda a evitar errores en tiempo de ejecución.
3. **Uso con `when`**: Las clases selladas son muy útiles con la expresión `when` en Kotlin, ya que puedes asegurarte de
   que has manejado todos los casos posibles sin necesidad de un bloque `else`.

## Ejemplos de uso de clases selladas:

### Ejemplo 1:

Supongamos que estás construyendo una aplicación y necesitas representar diferentes tipos de operaciones en una calculadora. 
Podrías tener operaciones como Suma, Resta, Multiplicación y División.
Aquí hay un ejemplo de cómo podrías hacerlo usando clases selladas:

```kotlin
sealed class CalculadoraOperacion {
    data class Suma(val valor1: Double, val valor2: Double) : CalculadoraOperacion()
    data class Resta(val valor1: Double, val valor2: Double) : CalculadoraOperacion()
    data class Multiplicacion(val valor1: Double, val valor2: Double) : CalculadoraOperacion()
    data class Division(val valor1: Double, val valor2: Double) : CalculadoraOperacion()
}

fun ejecutarOperacion(operacion: CalculadoraOperacion): Double {
    return when (operacion) {
        is CalculadoraOperacion.Suma -> operacion.valor1 + operacion.valor2
        is CalculadoraOperacion.Resta -> operacion.valor1 - operacion.valor2
        is CalculadoraOperacion.Multiplicacion -> operacion.valor1 * operacion.valor2
        is CalculadoraOperacion.Division -> operacion.valor1 / operacion.valor2
    }
}

fun main() {
    val suma = CalculadoraOperacion.Suma(10.0, 20.0)
    println("El resultado de la suma es: ${ejecutarOperacion(suma)}")
}
```

- En este ejemplo, `CalculadoraOperacion` es una clase sellada que tiene cuatro subtipos: 
`Suma`, `Resta`, `Multiplicacion`, y `Division`. 
- Cada uno de estos subtipos tiene su propia implementación y datos asociados. 
- La función `ejecutarOperacion` acepta un `CalculadoraOperacion` y usa `when` para determinar qué operación realizar. 
- Una de las ventajas aquí es que si añades un nuevo subtipo de `CalculadoraOperacion` y te olvidas de manejarlo en 
`ejecutarOperacion`, el compilador te advertirá que el `when` no está manejando todos los casos posibles, ayudándote 
a evitar errores.

### Ejemplo 2:

Supongamos que estás desarrollando un sistema de notificaciones para una aplicación y tienes varios tipos de 
notificaciones, como mensajes, alertas y advertencias. 

Puedes usar una clase sellada para modelar estos diferentes tipos de notificaciones.

```kotlin
// Definición de la clase sellada
sealed class Notificacion {
    class Mensaje(val contenido: String) : Notificacion()
    class Alerta(val titulo: String, val descripcion: String) : Notificacion()
    class Advertencia(val mensaje: String) : Notificacion()
}

// Función que maneja las notificaciones
fun manejarNotificacion(notificacion: Notificacion) {
    when (notificacion) {
        is Notificacion.Mensaje -> println("Tienes un nuevo mensaje: ${notificacion.contenido}")
        is Notificacion.Alerta -> println("Alerta: ${notificacion.titulo} - ${notificacion.descripcion}")
        is Notificacion.Advertencia -> println("Advertencia: ${notificacion.mensaje}")
    }
}

// Función principal para demostrar el uso de las clases selladas
fun main() {
    val mensaje = Notificacion.Mensaje("Bienvenido a Kotlin!")
    val alerta = Notificacion.Alerta("Error de Servidor", "El servidor no responde.")
    val advertencia = Notificacion.Advertencia("Batería baja.")

    manejarNotificacion(mensaje)
    manejarNotificacion(alerta)
    manejarNotificacion(advertencia)
}
```

En este ejemplo:

1. `Notificacion` es una clase sellada con tres subclases: `Mensaje`, `Alerta`, y `Advertencia`.
2. Cada tipo de notificación puede contener diferentes tipos de información. Por ejemplo, `Mensaje` solo tiene contenido,
   `Alerta` tiene título y descripción, y `Advertencia` solo tiene un mensaje.
4. La función `manejarNotificacion` usa un `when` para determinar el tipo de notificación y actuar en consecuencia.
5. En la función `main`, se crean instancias de diferentes tipos de notificaciones y se pasan a la función `manejarNotificacion`.

La belleza de este enfoque es que si decides añadir un nuevo tipo de notificación en el futuro, el compilador te advertirá 
en los lugares donde no estés manejando este nuevo tipo, gracias a las garantías de exhaustividad proporcionadas por las 
clases selladas en combinación con `when`.

### Ejemplo 3:

Las clases que están dentro de una clase sellada pueden tener sus propios métodos y propiedades adicionales, 
no solo los que se definen en su constructor primario. 

Esto te permite tener una estructura de clases muy flexible y rica en comportamiento. Cada subclase puede 
tener su propia implementación de métodos y sus propias propiedades.

```kotlin
sealed class Dispositivo {
    abstract fun mostrarInfo(): String

    class Smartphone(val marca: String, val modelo: String, val sistemaOperativo: String) : Dispositivo() {
        private val appsInstaladas = mutableListOf<String>()

        fun instalarApp(nombreApp: String) {
            appsInstaladas.add(nombreApp)
        }

        override fun mostrarInfo(): String {
            return "Smartphone $marca $modelo con SO $sistemaOperativo. Apps instaladas: $appsInstaladas"
        }
    }

    class Tableta(val marca: String, val tamañoPantalla: Double) : Dispositivo() {
        var nivelBateria = 100

        fun usarBateria(porcentaje: Int) {
            nivelBateria -= porcentaje
        }

        override fun mostrarInfo(): String {
            return "Tableta $marca con pantalla de $tamañoPantalla pulgadas. Batería al $nivelBateria%"
        }
    }
}

fun describirDispositivo(dispositivo: Dispositivo) {
    println(dispositivo.mostrarInfo())
}

fun main() {
    val miSmartphone = Dispositivo.Smartphone("Pixel", "5", "Android")
    miSmartphone.instalarApp("Twitter")
    miSmartphone.instalarApp("Spotify")

    val miTableta = Dispositivo.Tableta("iPad", 10.2)
    miTableta.usarBateria(10)

    describirDispositivo(miSmartphone)
    describirDispositivo(miTableta)
}
```

En este ejemplo:

1. `Dispositivo` es una clase sellada con dos subclases: `Smartphone` y `Tableta`.
2. `Smartphone` tiene una propiedad `appsInstaladas` que no se define en el constructor, sino en el cuerpo de la clase.
   También tiene un método `instalarApp` para agregar aplicaciones a la lista.
4. `Tableta` tiene una propiedad mutable `nivelBateria` y un método `usarBateria` para simular el uso de la batería.
5. Ambas clases `Smartphone` y `Tableta` implementan el método abstracto `mostrarInfo` de la clase sellada `Dispositivo`,
   pero cada una con su propia lógica.

Este ejemplo muestra cómo puedes tener estructuras de clases complejas y bien organizadas utilizando clases selladas, 
aprovechando la posibilidad de añadir propiedades y métodos específicos en cada subclase.

### Ejemplo 4:

Las clases que extienden una clase sellada en Kotlin no necesitan estar anidadas dentro de la clase sellada; sin embargo, 
deben estar en el mismo archivo que la clase sellada. 

Esto se debe a que el objetivo de una clase sellada es restringir la jerarquía de herencia a un conjunto conocido de subtipos, 
lo que se facilita al requerir que todas las subclases estén en el mismo archivo.

Si las clases `Smartphone` y `Tableta` están fuera de la clase sellada `Dispositivo`, pero en el mismo archivo, 
seguirían siendo subclases válidas de `Dispositivo`. Funcionalmente, sería lo mismo en términos de cómo puedes usar estas clases 
y cómo funcionaría la comprobación de tipos en tiempo de compilación.

```kotlin
sealed class Dispositivo {
    abstract fun mostrarInfo(): String
}

class Smartphone(val marca: String, val modelo: String, val sistemaOperativo: String) : Dispositivo() {
    private val appsInstaladas = mutableListOf<String>()

    fun instalarApp(nombreApp: String) {
        appsInstaladas.add(nombreApp)
    }

    override fun mostrarInfo(): String {
        return "Smartphone $marca $modelo con SO $sistemaOperativo. Apps instaladas: $appsInstaladas"
    }
}

class Tableta(val marca: String, val tamañoPantalla: Double) : Dispositivo() {
    var nivelBateria = 100

    fun usarBateria(porcentaje: Int) {
        nivelBateria -= porcentaje
    }

    override fun mostrarInfo(): String {
        return "Tableta $marca con pantalla de $tamañoPantalla pulgadas. Batería al $nivelBateria%"
    }
}

fun describirDispositivo(dispositivo: Dispositivo) {
    println(dispositivo.mostrarInfo())
}

fun main() {
    val miSmartphone = Smartphone("Pixel", "5", "Android")
    miSmartphone.instalarApp("Twitter")
    miSmartphone.instalarApp("Spotify")

    val miTableta = Tableta("iPad", 10.2)
    miTableta.usarBateria(10)

    describirDispositivo(miSmartphone)
    describirDispositivo(miTableta)
}
```

En este código, `Smartphone` y `Tableta` son clases independientes que extienden la clase sellada `Dispositivo` y proporcionan 
su propia implementación de `mostrarInfo()`.

Esto mantiene la capacidad de `Dispositivo` para limitar sus subtipos a un conjunto conocido y manejable, aprovechando las 
ventajas de las clases selladas en Kotlin.
