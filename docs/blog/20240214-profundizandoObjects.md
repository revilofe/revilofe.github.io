---
title: OBJECTS - Ejemplos y diferencias claves.

description: OBJECTS - Ejemplos y diferencias claves.

authors:
    - Diego Cano.

date: 2024-02-14

tags:
  - object
  - kotlin
---
# OBJECTS - Ejemplos y diferencias claves

En Kotlin, los objetos son una forma flexible y poderosa de definir estructuras únicas sin la necesidad de seguir el procedimiento tradicional de definición de clases. 
Podemos pensar en ellos como una manera de crear una "instancia única" de una clase con funcionalidades específicas, sin necesidad de crear una clase de manera explícita.

### 1. Object Expressions

Los "object expressions" crean una instancia de una clase anónima al vuelo, lo que es útil cuando necesitas una ligera modificación de una clase o interfaz existente sin declarar una nueva clase en tu código. 
Son similares a las clases anónimas en Java.

Por ejemplo, si tenemos una interfaz gráfica con un componente que requiere un escuchador de eventos, podemos usar un "object expression" para manejar clics o movimientos del mouse directamente donde los necesitemos, 
sin crear una clase `MouseAdapter` completa en otra parte:

```kotlin
fun countClicks(window: JComponent) {
    var clickCount = 0
    var enterCount = 0

    window.addMouseListener(object : MouseAdapter() {
        override fun mouseClicked(e: MouseEvent) {
            clickCount++
        }

        override fun mouseEntered(e: MouseEvent) {
            enterCount++
        }
    })
    // Aquí podemos usar clickCount y enterCount según lo necesites.
}
```

En este ejemplo estamos creando una única instancia de una clase que hereda de MouseAdapter. La clase MouseAdapter es una clase existente en el API de Swing de Java, que se usa para recibir eventos del ratón (mouse). 
Lo que hacemos con el "object expression" es crear un objeto anónimo que extiende MouseAdapter y sobreescribimos los métodos mouseClicked y mouseEntered para modificar su funcionalidad de acuerdo con nuestras necesidades específicas.

* Al sobreescribir mouseClicked, definimos lo que sucede cada vez que se hace clic con el mouse sobre el componente JComponent (en este caso, incrementando el contador clickCount).
* Al sobreescribir mouseEntered, definimos lo que sucede cada vez que el cursor del mouse entra en el área del componente JComponent (incrementando el contador enterCount).

Esto nos permite manejar eventos específicos del mouse directamente, sin la necesidad de crear una subclase de MouseAdapter en otra parte de nuestro código. 
Es una forma muy directa y concisa de adjuntar comportamiento específico a eventos de componentes GUI en aplicaciones Java/Kotlin.

Otro ejemplo similar modificando una clase existente al Vuelo sería el siguiente:

Supongamos que estamos trabajando en una aplicación que necesita realizar una operación específica cuando se hace clic en un botón, pero no queremos o no necesitamos crear una clase completa solo para esto. 
Podemos usar un object expression para manejar el evento del clic directamente:

```kotlin
button.setOnClickListener(object : View.OnClickListener {
    override fun onClick(v: View?) {
        // Aquí manejamos el clic en el botón
        println("El botón fue clickeado")
    }
})
```

Este código crea una instancia anónima de una clase que implementa la interfaz View.OnClickListener. Esto significa que en ese bloque de código, estamos definiendo una clase anónima que no tiene nombre 
pero que implementa los métodos de la interfaz OnClickListener. Este objeto anónimo sobrescribe el método onClick para proporcionar una implementación específica de lo que debe suceder cuando se haga clic 
en la vista (en este caso, un botón).

El contexto de uso aquí es típico del desarrollo de aplicaciones Android con Kotlin, donde se prefiere el uso de expresiones lambda y objetos anónimos para implementaciones de interfaces con un solo método, 
como View.OnClickListener. Esto permite un código más limpio y conciso, evitando la necesidad de definir una clase completa en otro lugar solo para implementar la interfaz de escucha de clics.

Este patrón de diseño es muy común en Android para manejar eventos de la interfaz de usuario debido a su simplicidad y eficiencia. Al hacerlo como se muestra en el ejemplo, estamo efectivamente diciendo: 
"Aquí hay una clase que cumple con View.OnClickListener y su implementación de onClick es la siguiente". Esto encapsula la lógica de manejo de clics justo en el lugar donde se configura el listener, 
lo que puede hacer que el código sea más fácil de entender y mantener.

En resumen, estamos creando un objeto de la clase View.OnClickListener de manera anónima, y dentro de este objeto, estamos sobrescribiendo el método onClick. 
Esto significa que estamos proporcionando una implementación específica para el método onClick que será llamado cuando ocurra el evento de clic en el botón. En Kotlin, este patrón se utiliza comúnmente para 
manejar eventos de interfaz de usuario o para personalizar el comportamiento de ciertas callbacks sin necesidad de declarar una clase completa en otra parte del código.

***Al usar un "object expression", Kotlin te permite:***

* Implementar una o más interfaces de forma anónima.
* Sobrescribir métodos de estas interfaces directamente en el lugar donde se necesita la instancia.
* Esto es especialmente útil en el desarrollo de aplicaciones Android, donde a menudo necesitas reaccionar a eventos como clics en botones, cambios en textos, etc.,
  sin crear clases completas para cada pequeña acción o variación de comportamiento.

Al hacer esto, el objeto que creamos con el object expression tiene una única instancia en ese contexto específico y lleva consigo las personalizaciones que hemos definido, 
como en este caso, la acción a realizar cuando el botón es clicado.

#### 1.1. Dónde se pueden utilizar

Los "object expressions" no se limitan únicamente a ser utilizados como parámetros en llamadas a funciones. Se pueden usar en cualquier lugar donde se esperaría una expresión en Kotlin. 
Por ejemplo, podríamos asignar un "object expression" a una variable, o usarlo en cualquier otro contexto que acepte una expresión.

Sin embargo, es muy común ver "object expressions" utilizados en contextos como parámetros de funciones cuando se necesita pasar una implementación concreta de una interfaz sin crear una clase nombrada. 
Esto es especialmente útil en situaciones donde la implementación es breve o solo se necesita en un lugar específico, como en el manejo de eventos de interfaz de usuario o en callbacks.

Los "object expressions" ofrecen una forma flexible de definir e instanciar clases anónimas para usos específicos, ya sea extendiendo una clase existente, implementando una interfaz, 
o simplemente definiendo un objeto con su propio conjunto de propiedades y métodos.

#### 1.2. Object expression sin herencia

Es posible crear un "object expression" en Kotlin sin heredar de una clase o interfaz específica, aunque es menos común. 
Al hacerlo, básicamente estamos creando una instancia anónima de una clase sin nombre con cualquier miembro que desees definir dentro de ella. 
Esto puede incluir propiedades, métodos, y bloques de inicialización, ***pero no constructores***.

Un ejemplo sencillo de un "object expression" que no hereda de ninguna clase o interfaz:

```kotlin
val saludo = object {
    val mensaje = "Hola"
    fun mostrarMensaje() {
        println(mensaje)
    }
}

saludo.mostrarMensaje() // Imprime: Hola
```

En este caso, estamos creando un objeto anónimo con una propiedad `mensaje` y un método `mostrarMensaje()`. Este objeto es único y solo existe una instancia de él (la asignada a `saludo`).

#### 1.3. Inicialización

Un "object expression" en Kotlin no puede tener constructores. Esto se debe a que los "object expressions" son instancias anónimas de clases definidas al vuelo, y Kotlin no permite 
definir constructores para estas instancias. La razón principal es que los constructores están destinados a inicializar nuevas instancias de clases cuando se crean, y los 
"object expressions" se inicializan en el punto donde se definen, sin necesidad de un mecanismo adicional como un constructor.

Sin embargo, podemos inicializar un "object expression" usando bloques de inicialización (init blocks) y definir propiedades y métodos dentro de ellos. 
Los bloques de inicialización se ejecutan en el momento en que se crea la instancia del objeto.

Un ejemplo de cómo podríamos inicializar un "object expression" sin un constructor pero utilizando un bloque `init` para inicializar propiedades:

```kotlin
val ejemplo = object {
    val propiedad1: String
    val propiedad2: Int

    // Bloque de inicialización
    init {
        propiedad1 = "Hola"
        propiedad2 = 42
    }

    fun mostrarPropiedades() {
        println("$propiedad1, $propiedad2")
    }
}

ejemplo.mostrarPropiedades() // Imprime: Hola, 42
```

En este ejemplo, el "object expression" inicializa sus propiedades `propiedad1` y `propiedad2` dentro del bloque `init`. Aunque no es un constructor en el sentido tradicional 
(como los que se utilizan en las clases), el bloque `init` sirve a un propósito similar en términos de inicialización de las instancias.

Por lo tanto, aunque no podemos usar constructores en "object expressions", Kotlin ofrece mecanismos flexibles como los bloques de inicialización para configurar nuestros objetos 
anónimos en el momento de su creación.

#### 1.4. Conclusión

Cuando usamos un "object expression" en Kotlin, estamos creando una única instancia de una clase anónima. Esta clase no tiene un nombre que puedas utilizar para crear otras instancias; 
la instancia se crea en el lugar donde se define el "object expression" y es única en ese contexto.

Esta singularidad de la instancia es especialmente útil en casos donde solo necesitas una implementación específica de una interfaz o una extensión de una clase para un uso particular, 
sin la necesidad de definir una clase completa en otra parte de tu código.

Los "object expressions" proporcionan una forma conveniente y concisa de manejar tales situaciones, permitiéndote definir y crear una instancia de una clase anónima al vuelo, 
completa con propiedades, métodos, y bloques de inicialización según sea necesario, sin la complejidad de definir una nueva clase nombrada.

Este enfoque es comúnmente utilizado para escenarios de uso único, como escuchas de eventos o adaptadores en programación de interfaces de usuario, donde la implementación específica 
no se reutiliza en otra parte del código. La clase anónima creada por un "object expression" vive en el alcance en el que se define y se destruye cuando sale de ese alcance, lo que 
proporciona no solo una solución elegante para necesidades específicas sino también una gestión de memoria eficiente.

### 2. Object Declarations

Los "object declarations" se usan para crear un único objeto de una clase. Kotlin gestiona la creación de este objeto de manera que solo se crea una instancia (Singleton). 
Esto es útil para cosas como mantener un conjunto de constantes relacionadas o una instancia de un servicio que se va a usar a lo largo de toda tu aplicación.

Supongamos que necesitamos una configuración global en nuestra aplicación para mantener URLs o configuraciones de API. En lugar de pasar esta configuración alrededor, 
podemos usar un object declaration para tenerla accesible globalmente:

```kotlin
object ConfiguracionGlobal {
    val urlAPI: String = "https://api.misitio.com"
    fun obtenerInfo() {
        println("Accediendo a la API en $urlAPI")
    }
}

// Acceso a la configuración global desde cualquier parte del código
ConfiguracionGlobal.obtenerInfo()
```

Este código define `ConfiguracionGlobal` como un singleton, asegurándose de que la URL de la API y el método `obtenerInfo` estén disponibles globalmente sin necesidad de crear 
múltiples instancias de la configuración.

En Kotlin, un "object declaration" se utiliza para declarar un tipo de objeto con una única instancia en toda la aplicación. 
A diferencia de las clases, donde puedes crear múltiples instancias, un "object declaration" nos permite tener una sola instancia de ese objeto, accesible globalmente. 
Esta única instancia se crea de manera perezosa, es decir, la primera vez que se accede al objeto.

La sintaxis para declarar un objeto es simple: usas la palabra clave `object` seguida del nombre del objeto:

```kotlin
object MiSingleton {
    val propiedad = "Esta es una propiedad de MiSingleton"
    fun miFuncion() {
        println("Esta es una función de MiSingleton")
    }
}
```

Podemos acceder a la propiedad y llamar a la función de `MiSingleton` directamente a través del nombre del objeto:

```kotlin
println(MiSingleton.propiedad)  // Accede a la propiedad
MiSingleton.miFuncion()         // Llama a la función
```

#### 2.1. ¿Qué es un Singleton?

Un Singleton es un patrón de diseño que restringe la instanciación de una clase a un solo objeto. Es útil cuando necesitas exactamente una instancia de una clase para coordinar acciones 
a través de tu aplicación. El patrón Singleton asegura que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.

En muchos lenguajes de programación, implementar un Singleton requiere varios pasos, incluyendo:

1. Hacer el constructor de la clase privado para prevenir la instanciación directa.
2. Crear una propiedad estática en la clase que almacene la única instancia.
3. Proporcionar un método estático que permita a los clientes acceder a la instancia única.

En Kotlin, las "object declarations" simplifican este proceso. Al declarar un objeto con `object`, Kotlin automáticamente maneja la creación de la única instancia y asegura que no puedas 
crear instancias adicionales por tu cuenta.

#### 2.2. Ejemplo Práctico de Singleton

Un uso común de los Singletons es para la configuración de una aplicación o para gestionar recursos compartidos, como conexiones a bases de datos o preferencias de usuario.

```kotlin
object ConfiguracionApp {
    var urlServidor: String = "https://api.miapp.com"
    var puerto: Int = 8080
    // Más configuración aquí
}

// Acceso a la configuración en otra parte del código
fun establecerConfiguracion() {
    ConfiguracionApp.urlServidor = "https://api.otrodominio.com"
}
```

Este enfoque garantiza que la configuración sea accesible de manera uniforme en toda la aplicación, y cambios hechos en una parte del código serán reflejados en todo lugar donde se acceda a esta configuración.

#### 2.3. Conclusión

Las "object declarations" en Kotlin brindan una forma muy clara y concisa de implementar el patrón Singleton, garantizando que solo exista una instancia de un objeto y que esta sea accesible globalmente. 
Esto simplifica la gestión de recursos compartidos y la configuración de aplicaciones, entre otros usos.

### 3. Companion Objects

Los "companion objects" se usan dentro de una clase para proporcionar miembros estáticos *(que en Kotlin no se llaman estáticos como en Java)* accesibles sin una instancia de la clase. 
Son útiles para cuando necesitas funciones o propiedades que están relacionadas con la clase pero que pueden ser accedidas sin tener una instancia de la clase.

Por ejemplo, si quieres tener un método `create()` para tu clase `MyClass` que actúe como un constructor alternativo, puedes hacerlo en un companion object:

```kotlin
class MyClass {
    companion object {
        fun create(): MyClass = MyClass()
    }
}
// Accedes así
val myClassInstance = MyClass.create()
```

#### 3.1. Métodos y Propiedades Relacionados con la Clase

Supongamos que tenemos una clase `Usuario` y queremos tener un método para crear un usuario predeterminado. En lugar de tener este método como estático *(como lo harías en Java)*, 
Kotlin utiliza el "companion object":

```kotlin
class Usuario(val nombre: String, val edad: Int) {
    companion object {
        fun usuarioPredeterminado() = Usuario("NombrePredeterminado", 30)
    }
}

// Crear un usuario predeterminado
val usuario = Usuario.usuarioPredeterminado()
```

Este código permite acceder al método `usuarioPredeterminado` sin necesidad de instanciar primero la clase `Usuario`. 
Es útil para métodos que están relacionados con la clase pero no requieren una instancia de la misma para funcionar.

#### 3.2. Herencia e implementación de interfaces

Un `companion object` en Kotlin puede implementar interfaces y extender otras clases ya que son objetos reales.

Esto proporciona una flexibilidad adicional en Kotlin, permitiendo que el `companion object` no solo contenga propiedades y métodos estáticos, sino también que tenga comportamientos 
definidos por interfaces o clases base. Esto puede ser útil en varios casos de uso, como cuando se quiere que un objeto compañero actúe como un factory con una interfaz común, 
o cuando se quiere agrupar métodos estáticos que deben cumplir con un contrato de interfaz.

Un ejemplo de cómo un `companion object` puede implementar una interfaz:

```kotlin
interface MyInterface {
    fun doSomething()
}

class MyClass {
    companion object : MyInterface {
        override fun doSomething() {
            println("Haciendo algo")
        }
    }
}

fun main() {
    MyClass.doSomething() // Accede directamente mediante la clase
}
```

Un ejemplo de cómo un `companion object` puede extender una clase:

```kotlin
open class MyBaseClass {
    open fun printMessage() {
        println("Mensaje desde MyBaseClass")
    }
}

class MyClass {
    companion object : MyBaseClass() {
        override fun printMessage() {
            println("Mensaje sobrescrito desde el companion object")
        }
    }
}

fun main() {
    MyClass.printMessage() // Accede directamente mediante la clase
}
```

Estos ejemplos muestran cómo los `companion objects` ofrecen una rica funcionalidad que va más allá de simplemente contener miembros estáticos, 
permitiéndoles participar en la jerarquía de clases e interfaces de Kotlin.

#### 3.3. Conclusión

Un "companion object" en Kotlin es un objeto especial que se define dentro de una clase. Cada clase puede tener un solo companion object, el cual puede contener propiedades y 
funciones que son accesibles sin tener una instancia de la clase, pero aún así, ***están relacionadas con la clase***. Esto es similar a los miembros estáticos en lenguajes como Java, 
con la diferencia de que en Kotlin, se agrupan dentro de un "objeto compañero".

Los "companion objects" son útiles cuando necesitamos funciones o propiedades que se relacionan con una clase, pero que no requieren una instancia de esa clase para ser usadas. 
Por ejemplo, podríamos querer tener un método de fábrica para crear instancias de una clase o variables estáticas que sean compartidas por todas las instancias.

Ejemplo de Companion Object:

```kotlin
Copy code
class MiClase {
    companion object {
        val CONSTANTE = "Una constante"
        fun crearInstancia(): MiClase = MiClase()
    }
}

// Acceso a la constante y función sin una instancia de MiClase
val miInstancia = MiClase.crearInstancia()
println(MiClase.CONSTANTE)
```

En este ejemplo, MiClase tiene un "companion object" que contiene una constante y un método para crear instancias. Estos miembros son accesibles a través de la clase en sí, no de una instancia de la clase.

### 4. Diferencias Clave entre "object declarations" y "Companion objects"

* ***Ubicación***: Los "companion objects" se definen dentro de una clase y están relacionados con esa clase. Las "object declarations" se definen por su cuenta y representan un único objeto global.

* ***Acceso***: Los miembros de un "companion object" son accesibles a través de la clase contenedora, imitando el acceso estático. Los miembros de una "object declaration" son accesibles directamente a través del nombre del objeto.

* ***Uso***: Los "companion objects" se utilizan para miembros relacionados con la clase que no requieren una instancia de la clase, como métodos de fábrica o constantes.
  Las "object declarations" se utilizan para crear singletons, útiles para gestionar estados o configuraciones globales.

* ***Herencia***: Un "companion object" puede implementar interfaces o extender otras clases. Una "object declaration" también puede hacerlo, pero su propósito principal es ser una instancia única más que relacionarse con otra clase.

Los "companion objects" y las "object declarations", son herramientas poderosas en Kotlin que sirven a diferentes propósitos. Mientras que las "object declarations" son ideales para crear singletons y 
manejar configuraciones o estados globales, los "companion objects" ofrecen una forma de tener acceso a propiedades y métodos relacionados con una clase sin necesidad de crear una instancia de ella.
