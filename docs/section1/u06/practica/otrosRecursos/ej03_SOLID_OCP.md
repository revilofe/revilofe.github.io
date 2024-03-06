## Ejercicio 03: Sistema de Notificaciones

### **Contexto:** 

Imagina que estás construyendo un sistema de notificaciones para una aplicación. Inicialmente, el sistema sólo envía notificaciones por correo electrónico, pero con el tiempo, 
se requiere añadir más métodos de notificación como SMS y notificaciones push. El diseño inicial podría ser algo así, lo cual viola el principio de abierto/cerrado porque para 
añadir nuevos métodos de notificación, necesitas modificar la clase existente.

```kotlin
class Notificador {
    fun enviarNotificacion(usuario: Usuario, mensaje: String) {
        when (usuario.tipoNotificacion) {
            "email" -> println("Enviando correo electrónico a ${usuario.email}: $mensaje")
            "sms" -> println("Enviando SMS a ${usuario.telefono}: $mensaje")
            // Para añadir un nuevo método de notificación, debes modificar esta clase.
        }
    }
}

data class Usuario(val nombre: String, val email: String, val telefono: String, val tipoNotificacion: String)

// Uso
fun main() {
    val usuario = Usuario("Juan", "juan@example.com", "1234567890", "email")
    Notificador().enviarNotificacion(usuario, "¡Bienvenido a nuestro sistema!")
}
```

La solución para adherir al principio de abierto/cerrado implica diseñar el sistema de modo que sea fácil añadir nuevos métodos de notificación sin modificar el código existente. 
Esto se puede lograr mediante el uso de interfaces o clases abstractas.

### **Tarea:** 

Implementa un interface para realizar la misma solución, pero cumpliendo el segundo principio SOLID Abierto/Cerrado (OCP). Crea las clases que necesites y modifica también el programa principal
para poder usar la nueva solución al problema.

### **Solución refactorizada:**

```kotlin
interface MetodoNotificacion {
    fun enviar(usuario: Usuario, mensaje: String)
}

class NotificacionEmail: MetodoNotificacion {
    override fun enviar(usuario: Usuario, mensaje: String) {
        println("Enviando correo electrónico a ${usuario.email}: $mensaje")
    }
}

class NotificacionSMS: MetodoNotificacion {
    override fun enviar(usuario: Usuario, mensaje: String) {
        println("Enviando SMS a ${usuario.telefono}: $mensaje")
    }
}

data class Usuario(val nombre: String, val email: String, val telefono: String)

class Notificador(private val metodo: MetodoNotificacion) {
    fun enviarNotificacion(usuario: Usuario, mensaje: String) {
        metodo.enviar(usuario, mensaje)
    }
}

// Uso
fun main() {
    val usuario = Usuario("Juan", "juan@example.com", "1234567890")
    val notificadorEmail = Notificador(NotificacionEmail())
    notificadorEmail.enviarNotificacion(usuario, "¡Bienvenido a nuestro sistema!")

    val notificadorSMS = Notificador(NotificacionSMS())
    notificadorSMS.enviarNotificacion(usuario, "Tu código de verificación es 1234")
}
```
