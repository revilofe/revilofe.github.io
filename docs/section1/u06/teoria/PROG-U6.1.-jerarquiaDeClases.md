---
title: "UD 6 - 6.1 Jerarquías de clases"
description: kotlin
summary: kotlin
authors:
    - Diego Cano
date: 2024-02-12
icon:   
permalink: /prog/unidad6/6.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin 
---
## 6.1. Jerarquías de clases.

La jerarquía de clases en Kotlin, dentro del contexto de la Programación Orientada a Objetos (POO), se refiere a la organización estructurada de clases en una relación de herencia, donde las clases pueden ser derivadas unas de otras para reutilizar código, extender funcionalidades y proporcionar comportamientos específicos.

### 1. Conceptos de Herencia, Superclase y Subclase

#### 1.1. Herencia

La herencia es una de las características clave que diferencian a la POO de otros paradigmas de programación, permitiendo una mayor reutilización de código, una mejor organización y una mayor facilidad para gestionar la complejidad de los sistemas de software.

La herencia es un mecanismo de la POO que permite a una clase (llamada subclase o clase derivada) adquirir o heredar los atributos y métodos de otra clase (llamada superclase o clase base). 
Este mecanismo fomenta la reutilización de código, ya que permite a los desarrolladores crear nuevas clases a partir de clases existentes, extendiendo o modificando su comportamiento según sea necesario.

La herencia facilita la creación de una jerarquía de clases, donde las clases pueden ser organizadas en niveles, con clases más generales en la parte superior y clases más específicas debajo. 
Esta jerarquía refleja las relaciones "es un tipo de" entre clases, lo que ayuda a representar conceptos y entidades del mundo real de manera más natural y eficiente en el código.

#### 1.2. Superclase o Clase Base

Una superclase, también conocida como clase base o clase padre, es la clase de la cual otras clases derivan. En una jerarquía de clases, la superclase se encuentra en un nivel superior y proporciona un conjunto 
de atributos y métodos que otras clases pueden heredar o sobrescribir. Las superclases suelen representar conceptos más generales o abstractos.

Las superclases pueden ser:
- **Concretas**: Clases que proporcionan implementaciones completas de sus métodos, lo que permite crear instancias de ellas.
- **Abstractas**: Clases declaradas específicamente para ser extendidas, no se pueden instanciar directamente y pueden contener métodos abstractos sin implementación.

#### 1.3. Subclase o Clase Derivada

Una subclase, también conocida como clase derivada o clase hija, es una clase que hereda de una superclase. Las subclases pueden utilizar los atributos y métodos heredados de sus superclases y tienen la capacidad de:
- Extender la funcionalidad de la superclase agregando nuevos atributos y métodos.
- Modificar el comportamiento existente sobrescribiendo métodos heredados.
- Proporcionar implementaciones para métodos abstractos definidos en superclases abstractas.

Las subclases representan conceptos más específicos o especializados en la jerarquía de clases, y su creación es un medio fundamental para lograr la especialización y la extensión en la POO.

#### 1.4. Ejemplo Conceptual

Imaginemos una jerarquía de clases en un sistema de gestión de vehículos:

```kotlin
// Superclase
open class Vehiculo(val marca: String, val modelo: String) {
    fun describir() = println("Vehículo de marca $marca, modelo $modelo")
}

// Subclase
class Coche(marca: String, modelo: String, val numPuertas: Int) : Vehiculo(marca, modelo) {
    fun describirCoche() {
        describir()
        println("Número de puertas: $numPuertas")
    }
}
```

En este ejemplo, `Vehiculo` es una superclase que proporciona propiedades y métodos básicos comunes a todos los vehículos. `Coche` es una subclase que hereda de `Vehiculo` y extiende su funcionalidad al introducir 
una nueva propiedad (`numPuertas`) y un nuevo método (`describirCoche`).

La herencia permite estructurar el código de manera jerárquica y lógica, promoviendo la reutilización y la extensión de las funcionalidades de manera eficiente y efectiva.

La herencia en POO no solo facilita la reutilización de código y la organización jerárquica de clases, sino que también permite la implementación de diferentes funcionalidades y patrones de diseño 
que enriquecen el diseño y la estructura de un programa:

#### 1.5. Especialización ("Es un")

La especialización es quizás el uso más intuitivo de la herencia, donde una clase derivada representa una versión más específica de su clase base. Esta relación se describe a menudo como "es un", 
significando que la subclase es un tipo especializado de la superclase.

- **Concepto**: La subclase hereda las propiedades y comportamientos de la superclase, pero también introduce características únicas que la distinguen.
  
- **Ejemplo**: Consideremos una jerarquía de clases donde `Figura` es una superclase que define un comportamiento básico común a todas las figuras geométricas, como calcular el área o el perímetro.
  La clase `Cuadrado` sería una subclase que especializa a `Figura` definiendo cómo estos comportamientos se aplican específicamente a un cuadrado, aprovechando sus características únicas como tener
  todos sus lados de igual longitud.

#### 1.6. Extensión (Extiende Funcionalidad Heredada)

A través de la extensión, una subclase añade nuevas funcionalidades a la clase base sin cambiar su comportamiento original. Esta relación no implica necesariamente una especialización, 
sino una ampliación de las capacidades.

- **Concepto**: La subclase mantiene el comportamiento de la superclase y agrega nuevas características o funcionalidades que extienden su uso o aplicabilidad.

- **Ejemplo**: Si tenemos una clase `Lista` que implementa las operaciones básicas de una lista, una clase `ListaSalvable` podría heredar de `Lista` y extender su funcionalidad al añadir métodos para
  guardar y cargar el estado de la lista desde un archivo, sin alterar las operaciones básicas de la lista.

```
La diferencia entre "Especialización" y "Extensión" es que la primera se centra en el concepto de
"ser un tipo específico de" una clase base, introduciendo propiedades y comportamientos que son
únicos para la subclase, lo que hace que esta subclase sea más específica o adecuada para tareas
detalladas dentro de la jerarquía de la clase.

La "Extensión", por otro lado, se trata de añadir nuevas funcionalidades a la clase base sin cambiar
su comportamiento original. La subclase mantiene todas las capacidades de la clase base y agrega
nuevas funcionalidades que amplían su uso, pero no necesariamente cambia la naturaleza fundamental
de lo que la clase base representa.
```

#### 1.7. Especificación (Define Interface)

La especificación, a través de la herencia, se utiliza para definir una interfaz común para un grupo de clases. La superclase (o interfaz) declara un conjunto de métodos que todas las subclases 
deben implementar, cada una a su manera.

- **Concepto**: La superclase establece un ***contrato*** que sus subclases deben cumplir, especificando los métodos que deben implementar sin necesariamente proporcionar una implementación concreta.

- **Ejemplo**: `ObjetoGrafico` podría ser una interfaz o clase abstracta que define operaciones comunes para objetos gráficos, como dibujar o mover. Las clases `Texto`, `Linea` y `Figura` implementarían
  esta interfaz, proporcionando implementaciones específicas para cada tipo de objeto gráfico.

#### 1.8. Construcción (Usado para Construir la Subbase)

La construcción se refiere al uso de la herencia para construir una nueva clase basada en la funcionalidad de una clase existente, aunque la relación conceptual entre las dos clases no sea directa.

- **Concepto**: La clase derivada utiliza la clase base como un punto de partida o una base sobre la cual construye su propia funcionalidad única, posiblemente sin mantener una relación conceptual "es un".

- **Ejemplo**: La clase `Pila` podría heredar de la clase `Lista`. Aunque conceptualmente una pila no es una lista, esta herencia permite a `Pila` aprovechar la implementación y la funcionalidad de `Lista`
  para gestionar sus elementos internos, aplicando restricciones adicionales o métodos específicos de pilas, como operaciones LIFO (Last In, First Out).

Cada uno de estos usos de la herencia ofrece diferentes ventajas y se adapta a distintas necesidades en el diseño de software. La elección de cuándo y cómo utilizar la herencia depende de los requisitos específicos 
del sistema que se está desarrollando, así como de los principios de diseño de software como el acoplamiento, la cohesión y la encapsulación. La herencia, utilizada sabiamente, puede facilitar la creación de sistemas 
de software flexibles, mantenibles y escalables.

#### 1.9. Bloquear y forzar la herencia de clases y métodos

Es crucial comprender cómo Kotlin, al igual que otros lenguajes de programación orientada a objetos, maneja la herencia y la polimorfia a través de diferentes constructos y modificadores de acceso. 
Profundizaremos en los conceptos de clases abstractas e interfaces, así como en el uso de los modificadores `open`, `final`, `abstract` para controlar la herencia y la sobrescritura.

absolutamente, el uso adecuado de clases abstractas, interfaces, y los modificadores `open`, `final`, y `abstract` en Kotlin son fundamentales para diseñar un código robusto y flexible que aprovecha los principios de la Programación Orientada a Objetos (POO). Estos elementos permiten a los desarrolladores construir jerarquías de clases bien estructuradas, promover la reutilización de código, y facilitar el mantenimiento y la escalabilidad del software.

### 2. Clases Abstractas e Interfaces: Forzando la Herencia y Especificación

Las clases abstractas e interfaces juegan roles cruciales en el diseño de software orientado a objetos:

- **Clases Abstractas**: Al forzar a las subclases a implementar métodos abstractos específicos, las clases abstractas establecen una base sólida sobre la cual se puede construir una funcionalidad más detallada.
  Permiten cierto grado de implementación compartida gracias a la capacidad de contener métodos con implementaciones por defecto, a la vez que dejan espacio para que las subclases personalicen o extiendan esas
  implementaciones según sea necesario.

- **Interfaces**: Las interfaces llevan el concepto de herencia a un nivel de contrato, donde las clases pueden implementar múltiples interfaces para cumplir con varios contratos de comportamiento.
  Esto brinda una flexibilidad increíble en el diseño de sistemas, permitiendo combinaciones complejas de comportamientos a través de la implementación de múltiples interfaces, sin las limitaciones
  impuestas por la herencia única de clases.

#### 2.1. Clases Abstractas

Las clases abstractas en Kotlin son clases que no pueden ser instanciadas por sí mismas. Esto significa que no puedes crear un objeto de una clase abstracta directamente. Están diseñadas para ser subclases, 
permitiendo que otras clases hereden de ellas.

- **Forzando la herencia**: Al definir una clase como `abstract`, estás forzando a cualquier clase que quiera utilizar su funcionalidad a heredar de ella. Esto se debe a que una clase abstracta puede contener
  uno o más métodos `abstract` (sin implementación), y cualquier clase hija debe proporcionar implementaciones concretas para todos esos métodos abstractos.
  
- **Métodos y propiedades en clases abstractas**: Aunque las clases abstractas no pueden ser instanciadas, pueden tener métodos con implementaciones completas (no abstractos) y propiedades. Esto permite a las
  clases derivadas utilizar estos métodos y propiedades directamente o sobrescribirlos si es necesario.

#### 2.2. Interfaces

Las interfaces en Kotlin definen un contrato que otras clases pueden implementar. A diferencia de las clases abstractas, las interfaces no pueden contener estado (variables de instancia con campos de respaldo) 
y pueden ser implementadas por cualquier clase, independientemente de su lugar en la jerarquía de clases.

- **Herencia a través de interfaces**: Aunque técnicamente no se considera "herencia" en el sentido tradicional, las interfaces permiten a las clases adoptar un conjunto específico de comportamientos sin necesitar
  una relación "es un" directa. Una clase puede implementar múltiples interfaces, lo que ofrece una forma de polimorfismo y flexibilidad que no es posible mediante la herencia de clases debido a la restricción de
  Kotlin (y Java) de herencia única.

### 3. Modificadores `open`, `final`, y `abstract`: Controlando la Herencia y la Sobrescritura

La gestión cuidadosa de la herencia y la sobrescritura es crucial para la integridad del diseño de clases:

- **`open`**: Al hacer que todas las clases y métodos sean `final` por defecto, Kotlin promueve la inmutabilidad y la seguridad de diseño. El modificador `open` es una herramienta poderosa para indicar explícitamente
  qué partes de una clase están disponibles para ser extendidas o sobrescritas, asegurando que la extensibilidad se otorgue de manera consciente y controlada. Esto proporciona un control fino sobre la herencia,
  permitiendo a los diseñadores de clases decidir qué comportamientos pueden ser personalizados por las clases derivadas.

- **`final`**: Si bien todo es `final` por defecto en Kotlin, cuando se utiliza el modificador `open`, puedes usar `final` en un método sobrescrito para prevenir que sea sobrescrito nuevamente en subclases más derivadas.
  Utilizar `final` para marcar métodos en clases `open` que no deben ser sobrescritos en subclases adicionales ayuda a mantener la consistencia y prevenir modificaciones no deseadas del comportamiento de
  la clase base. Esto es especialmente útil en contextos donde la extensión de ciertas funcionalidades podría comprometer la lógica o la seguridad del programa.

- **`abstract`**: Los métodos y clases `abstract` son el núcleo de la herencia y la polimorfia en POO, obligando a las subclases a implementar comportamientos específicos y permitiendo la variabilidad en cómo se realizan
  estas implementaciones. Los métodos abstractos son inherentemente `open`, ya que su propósito es ser sobrescrito.

#### 3.1. Ejemplo Práctico

Consideremos la clase `Employee` y su subclase `Teacher`:

```kotlin
abstract class Employee(val firstName: String, val lastName: String) {
    val propFoo: String = "bla bla"
    
    abstract fun earnings(): Double

    open fun fullName(): String = "$lastName $firstName"
}

class Teacher(firstName: String, lastName: String): Employee(firstName, lastName) {
    override fun earnings(): Double = 50000.0
    
    // Intento de sobrescribir fullName provocaría error si se marca como final en Employee
    override fun fullName(): String = "Prof. $lastName"
}
```

En este ejemplo, `Employee` es una clase abstracta que define una implementación predeterminada para `fullName()` y declara un método abstracto `earnings()`. 
La clase `Teacher` hereda de `Employee` y proporciona implementaciones concretas para los métodos abstractos. Si `fullName()` en `Employee` se marcara como `final`, 
entonces `Teacher` no podría sobrescribir ese método, demostrando cómo los modificadores controlan la herencia y la sobrescritura.

#### 3.2. Conclusión

La habilidad para forzar y bloquear la herencia y la sobrescritura en Kotlin a través del uso estratégico de clases abstractas, interfaces, y modificadores específicos es una herramienta poderosa en el arsenal de cualquier 
desarrollador de software. No solo facilita la creación de sistemas de software cohesivos y bien organizados, sino que también asegura que estos sistemas sean capaces de adaptarse y crecer con el tiempo sin comprometer su 
integridad estructural o funcional.

Al diseñar y desarrollar con Kotlin, los principios de encapsulación, abstracción, herencia, y polimorfismo se manifiestan a través de estas construcciones de lenguaje, permitiendo a los desarrolladores abordar problemas 
complejos de manera modular y mantenible. Entender y aplicar estos conceptos y herramientas de manera efectiva es fundamental para aprovechar plenamente las capacidades de Kotlin y desarrollar software de alta calidad que 
sea fácil de entender, extender y mantener.

### 4. Incidencia de los constructores en la herencia

La incidencia de los constructores en la herencia es un aspecto fundamental en la Programación Orientada a Objetos (POO), especialmente en lenguajes como Kotlin, donde la sintaxis y los mecanismos de herencia tienen 
particularidades específicas que influyen directamente en cómo se diseñan y se implementan las jerarquías de clases. Este criterio de evaluación se centra en comprender cómo los constructores de las clases base (superclases) 
afectan y son afectados por las clases derivadas (subclases) durante el proceso de herencia.

#### 4.1. Conceptos Básicos de Constructores en Kotlin

En Kotlin, los constructores juegan un papel crucial en la inicialización de objetos. Hay dos tipos de constructores:

- **Constructor Primario**: Se declara en la línea de definición de la clase. Es compacto y se utiliza para inicializar la clase con menos código.
- **Constructores Secundarios**: Permiten más lógica de inicialización y pueden llamar al constructor primario usando `this`. También se utilizan para ofrecer más opciones de inicialización.

#### 4.2. Llamadas al Constructor de la Superclase

Cuando una clase hereda de otra, Kotlin requiere que la subclase inicialice la superclase. Esto se hace mediante una llamada explícita al constructor de la superclase, ya sea su constructor primario o uno de sus constructores secundarios. 
Esta llamada asegura que todos los campos y bloques de inicialización de la superclase se ejecuten antes de la subclase:

```kotlin
open class Persona(val nombre: String)

class Empleado(nombre: String, val empleadoId: Int) : Persona(nombre)
```

En este ejemplo, `Empleado` hereda de `Persona`, y el constructor de `Empleado` llama al constructor de `Persona` pasando el `nombre`, asegurando que la inicialización de `Persona` se complete antes de proceder con `Empleado`.

#### 4.3. Sobrecarga de Constructores y Herencia

Las clases en Kotlin pueden tener múltiples constructores secundarios, cada uno con diferentes parámetros. La herencia de una clase con múltiples constructores introduce complejidad, ya que la subclase debe decidir explícitamente 
cuál constructor de la superclase llamar, si es que hay más de uno disponible:

```kotlin
open class Persona(val nombre: String) {
    constructor(nombre: String, edad: Int) : this(nombre) {
        // Lógica adicional
    }
}

class Empleado(nombre: String) : Persona(nombre)
```

#### 4.4. Constructores Secundarios en Subclases

Las subclases pueden tener sus propios constructores secundarios, pero cada uno de ellos debe delegar al constructor de la superclase, directa o indirectamente, a través de otro constructor de la subclase utilizando `this`:

```kotlin
class Empleado : Persona {
    constructor(nombre: String, empleadoId: Int) : super(nombre)
    constructor(nombre: String, empleadoId: Int, edad: Int) : this(nombre, empleadoId)
}
```

#### 4.5. Consideraciones Especiales

- **Inicialización de Propiedades**: Las propiedades declaradas en la superclase deben ser inicializadas antes de que la subclase pueda usarlas. Esto es crucial para evitar el acceso a estados no inicializados.

- **Bloques de Inicialización**: Los bloques de inicialización de la superclase se ejecutan antes de los bloques de inicialización de la subclase. Esto es importante para la secuencia de inicialización y la lógica
  de configuración del objeto.

- **Herencia de Interfaces y Constructores**: Aunque las interfaces no tienen constructores, la implementación de interfaces en una jerarquía de clases no afecta la cadena de llamadas al constructor.
  Sin embargo, las clases que implementan interfaces aún deben seguir las reglas de inicialización de sus superclases.

#### 4.6. Conclusión

La correcta comprensión y manejo de los constructores en la herencia son esenciales para garantizar que los objetos se inicialicen de manera coherente y segura en Kotlin. La necesidad de llamar explícitamente al 
constructor de la superclase subraya la importancia de la secuencia de inicialización en la herencia, asegurando que todas las propiedades y estados necesarios de las superclases estén configurados antes de que se 
ejecute cualquier lógica específica de la subclase. Este mecanismo refuerza el encapsulamiento y la integridad de los objetos a lo largo de la jerarquía de herencia, contribuyendo a la creación de software robusto y mantenible.

### 5. Sobrescritura de Métodos en Clases Heredadas

La sobrescritura de métodos es una característica esencial en la Programación Orientada a Objetos que permite a una clase derivada ofrecer una implementación específica de un método que ya está definido en su clase base. 
Esta capacidad es fundamental para modificar o extender el comportamiento de métodos heredados según las necesidades específicas de la subclase.

#### 5.1. Principios de Sobrescritura

- **Uso de `override`**: En Kotlin, para sobrescribir un método de la clase base, el método en la subclase debe estar precedido por el modificador `override`. Esto indica explícitamente que el método está sobrescribiendo uno de la superclase.
- **Compatibilidad de Firmas**: La firma del método sobrescrito en la subclase debe coincidir con la firma del método en la clase base. Esto incluye el nombre del método, el número y tipo de sus parámetros, y el tipo de retorno.
- **Acceso a la Implementación de la Superclase**: La subclase puede llamar a la implementación del método de la superclase utilizando `super`.

```kotlin
open class Animal {
    open fun emitirSonido() {
        println("Este animal emite un sonido genérico.")
    }
}

class Perro : Animal() {
    override fun emitirSonido() {
        super.emitirSonido()
        println("El perro ladra.")
    }
}
```

### 6. Diseño y Aplicación de Jerarquías de Clases

El diseño de jerarquías de clases es un proceso que implica organizar las clases en una estructura de árbol que refleje relaciones "es un" entre ellas, permitiendo la reutilización de código y la extensibilidad del software.

#### 6.1. Características de una Buena Jerarquía de Clases

- **Claridad y Mantenibilidad**: La jerarquía debe ser fácil de entender y mantener. Cada clase debe tener un propósito claro y estar bien definida.
- **Reutilización de Código**: Las clases base deben diseñarse con el objetivo de maximizar la reutilización de código por parte de las subclases.
- **Extensibilidad**: La arquitectura debe permitir la fácil extensión de clases y funcionalidades sin alterar significativamente la estructura existente.

#### 6.2. Estrategias para el Diseño

- **Identificación de Conceptos Comunes**: Determinar las propiedades y comportamientos comunes que pueden ser abstractos en clases base.
- **Uso de Abstracciones Adecuadas**: Utilizar clases abstractas e interfaces para definir contratos y generalizaciones.
- **Especialización Progresiva**: Derivar subclases que especialicen y extiendan las funcionalidades de las clases base.

#### 6.3. Pruebas y Depuración de las Jerarquías de Clases

Las pruebas y la depuración son cruciales para asegurar la correcta implementación y funcionamiento de las jerarquías de clases. Esto implica verificar que cada clase y método se comporten como se espera, tanto individualmente como en conjunto.

#### 6.4. Pruebas

- **Pruebas Unitarias**: Escribir pruebas unitarias para cada clase y método, asegurando que funcionan correctamente de forma aislada.
- **Pruebas de Integración**: Realizar pruebas que involucren interacciones entre clases en la jerarquía para asegurar que cooperen correctamente.

Para ilustrar cómo realizar pruebas unitarias y de integración en el contexto de jerarquías de clases en Kotlin, utilizaremos como ejemplo la jerarquía de clases `Animal` y `Perro` definida anteriormente. 
Asumiremos que estas clases forman parte de un proyecto Kotlin que utiliza JUnit para las pruebas.

#### 6.5. Ejemplo de Prueba Unitaria para `Perro`

Las pruebas unitarias se centran en verificar la funcionalidad de una sola clase o método en aislamiento. Para la clase `Perro`, una prueba unitaria podría verificar que el método `emitirSonido()` se comporta como se espera.

```kotlin
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.Test

class PerroTest {

    @Test
    fun testEmitirSonido() {
        val perro = Perro()
        var sonido = ""
        
        // Redirigir la salida estándar para capturar el texto impreso por emitirSonido()
        val originalOut = System.out
        try {
            val outputStreamCaptor = ByteArrayOutputStream()
            System.setOut(PrintStream(outputStreamCaptor))
            
            perro.emitirSonido()
            sonido = outputStreamCaptor.toString().trim()
            
        } finally {
            System.setOut(originalOut)
        }
        
        assertTrue(sonido.contains("El perro ladra"), "El sonido emitido por el perro debe contener 'El perro ladra'")
    }
}
```

Este test verifica que al llamar a `emitirSonido()` en un objeto `Perro`, la salida incluye la cadena específica "El perro ladra". Se utiliza una redirección de `System.out` para capturar la salida impresa y verificarla.

#### 6.6. Ejemplo de Prueba de Integración para la Jerarquía de `Animal` y `Perro`

Las pruebas de integración evalúan cómo diferentes partes del sistema trabajan juntas. En este caso, podríamos verificar cómo la clase `Perro` interactúa dentro del contexto más amplio de la jerarquía de clases `Animal`.

```kotlin
import org.junit.jupiter.api.Test
import kotlin.test.assertNotNull

class IntegracionAnimalTest {

    @Test
    fun testCreacionPerro() {
        val perro = Perro()
        assertNotNull(perro, "El objeto perro no debería ser nulo")
        
        // Verificar que Perro es instancia de Animal
        assertTrue(perro is Animal, "Perro debería ser instancia de Animal")
        
        // Verificar comportamiento heredado (como emitirSonido o cualquier otro método relevante)
        var sonido = ""
        val originalOut = System.out
        try {
            val outputStreamCaptor = ByteArrayOutputStream()
            System.setOut(PrintStream(outputStreamCaptor))
            
            perro.emitirSonido()
            sonido = outputStreamCaptor.toString().trim()
            
        } finally {
            System.setOut(originalOut)
        }
        
        assertTrue(sonido.contains("El perro ladra"), "Perro debería emitir su sonido característico al llamar a emitirSonido()")
    }
}
```

Esta prueba de integración verifica varios aspectos:

- La creación de un objeto `Perro` y su no nulidad.
- Que un objeto `Perro` sea reconocido como una instancia de `Animal`, validando así la relación de herencia.
- Que el método sobrescrito `emitirSonido()` funcione correctamente dentro del contexto de la jerarquía de clases, manteniendo la coherencia del comportamiento esperado.

Estos ejemplos demuestran cómo se pueden implementar pruebas unitarias y de integración para validar tanto el comportamiento específico de las subclases como su correcta integración dentro de una jerarquía de clases más amplia, 
asegurando así que el sistema funcione como se espera en conjunto.

#### 6.7. Depuración

- **Uso de IDEs**: Aprovechar las herramientas de depuración integradas en los Entornos de Desarrollo Integrado (IDEs) para inspeccionar el estado y el flujo de ejecución.
- **Rastreo de Llamadas a Métodos**: Prestar especial atención a las llamadas a métodos sobrescritos y a la ejecución de constructores a lo largo de la jerarquía.

#### 6.8. Herramientas y Técnicas

- **Registro y Monitoreo**: Utilizar registros (logging) para seguir el flujo de ejecución y detectar anomalías.
- **Análisis Estático de Código**: Emplear herramientas de análisis estático para identificar problemas comunes y potenciales errores en el diseño de las clases.
