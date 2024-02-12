---
title: Diferencias entre clase abstracta e interfaz.

description: Diferencias entre clase abstracta e interfaz.

authors:
    - Diego Cano.

date: 2024-02-04

tags:
  - clase abstracta
  - interfaz
  - kotlin
---
# Diferencias entre clase abstracta e interfaz

En Kotlin, tanto las clases abstractas como las interfaces son conceptos fundamentales para la abstracción y el diseño de clases. 
Permiten definir una estructura que otras clases pueden implementar o heredar. Aunque comparten algunos propósitos, 
tienen características y usos distintos. 

### Clase Abstracta

Una clase abstracta es una clase que no se puede instanciar por sí misma. Se utiliza como clase base para otras clases. 
Las clases abstractas se utilizan para definir un patrón común para un grupo de clases relacionadas.

**Características:**
- Puede contener implementaciones concretas de algunos métodos.
- Puede declarar constructores.
- Puede tener propiedades con estado (variables con valores almacenados).
- Las clases que heredan de una clase abstracta deben implementar todos los métodos abstractos, a menos que ellas mismas sean abstractas.

**Uso típico:**
- Cuando tienes una base común para varias clases, pero nunca necesitas instanciar la clase base por sí misma.
- Cuando tus clases base necesitan tener algunas implementaciones comunes que quieres compartir con las clases derivadas.

### Interfaz

Una interfaz define un contrato que otras clases pueden implementar. En Kotlin, las interfaces son más flexibles y 
potentes que en muchos otros lenguajes.

**Características:**
- No puede contener un estado (no puede tener propiedades inicializadas).
- Puede contener declaraciones de métodos así como implementaciones de métodos (a partir de Java 8 y Kotlin). 
  Sin embargo, las implementaciones de métodos en las interfaces no pueden tener un estado.
- Una clase puede implementar múltiples interfaces.

**Uso típico:**
- Cuando varias clases no relacionadas deben compartir métodos comunes (pero la implementación puede ser diferente para cada clase).
- Cuando necesitas asegurarte de que una clase implemente ciertos métodos.

### Diferencias Principales

- **Instanciación**: No puedes instanciar clases abstractas ni interfaces. La diferencia es que una clase abstracta puede tener un constructor 
  y puede realizar inicialización en él. Las interfaces no pueden tener constructores.
- **Estado**: Las clases abstractas pueden mantener un estado (tener propiedades que almacenen valores), pero las interfaces no.
- **Implementación Múltiple**: Las clases en Kotlin no pueden heredar de más de una clase (abstracta o no), pero pueden implementar múltiples interfaces.
- **Funciones con Implementación**: Ambas, clases abstractas e interfaces, pueden tener funciones con implementación. 
  Sin embargo, solo las clases abstractas pueden tener un estado que esas funciones puedan modificar.

### Cuándo usar uno u otro

- **Usa una clase abstracta** cuando tengas clases que compartan un código común muy estrechamente relacionado,
  y cuando ese código incluya algún estado que deba ser mantenido.
- **Usa una interfaz** cuando tengas clases que necesiten compartir métodos, pero no comportamientos (implementaciones de métodos) o estados,
  o cuando quieras aprovechar la implementación múltiple para combinar varios comportamientos.

En resumen, la elección entre una clase abstracta y una interfaz puede depender de las necesidades específicas de tu diseño de software y 
de las características del lenguaje que estés utilizando. Kotlin ofrece una gran flexibilidad y características adicionales para interfaces 
que otros lenguajes no tienen, por lo que vale la pena considerar estas características al tomar tu decisión.

### Ejemplo de Clase Abstracta

**Escenario:**
Supongamos que estás construyendo un sistema para un zoológico que necesita manejar diferentes tipos de animales. 
Todos los animales tienen ciertas características en común, como la necesidad de alimentarse, pero cada tipo de animal tiene su propia forma de alimentarse.

```kotlin
// Clase abstracta Animal
abstract class Animal(val nombre: String) {
    abstract fun alimentarse()

    fun dormir() {
        println("$nombre está durmiendo")
    }
}

// Clase concreta León que hereda de Animal
class Leon(nombre: String) : Animal(nombre) {
    override fun alimentarse() {
        println("$nombre, el león, está comiendo carne")
    }
}

// Clase concreta Elefante que hereda de Animal
class Elefante(nombre: String) : Animal(nombre) {
    override fun alimentarse() {
        println("$nombre, el elefante, está comiendo vegetales")
    }
}

fun main() {
    val leon = Leon("Leo")
    leon.alimentarse()  // Output: Leo, el león, está comiendo carne
    leon.dormir()       // Output: Leo está durmiendo
    
    val elefante = Elefante("Eli")
    elefante.alimentarse()  // Output: Eli, el elefante, está comiendo vegetales
    elefante.dormir()       // Output: Eli está durmiendo
}
```

En este ejemplo, `Animal` es una clase abstracta que define un método abstracto `alimentarse` y un método concreto `dormir`. 
Las clases `Leon` y `Elefante` heredan de `Animal` y proporcionan su propia implementación del método `alimentarse`.

### Ejemplo de Interfaz

**Escenario:**
Imagina que estás desarrollando un software para gestionar dispositivos inteligentes en una casa. Cada dispositivo tiene diferentes capacidades, 
pero todos deben poder ser encendidos o apagados.

```kotlin
// Interfaz DispositivoInteligente
interface DispositivoInteligente {
    fun encender()
    fun apagar()
}

// Clase Luz que implementa la interfaz DispositivoInteligente
class Luz : DispositivoInteligente {
    override fun encender() {
        println("La luz está encendida")
    }

    override fun apagar() {
        println("La luz está apagada")
    }
}

// Clase Termostato que implementa la interfaz DispositivoInteligente
class Termostato : DispositivoInteligente {
    override fun encender() {
        println("El termostato está ajustando la temperatura")
    }

    override fun apagar() {
        println("El termostato está apagado")
    }
}

fun main() {
    val luz = Luz()
    luz.encender()  // Output: La luz está encendida
    luz.apagar()    // Output: La luz está apagada
    
    val termostato = Termostato()
    termostato.encender()  // Output: El termostato está ajustando la temperatura
    termostato.apagar()    // Output: El termostato está apagado
}
```

En este ejemplo, `DispositivoInteligente` es una interfaz que define dos métodos: `encender` y `apagar`. 
Las clases `Luz` y `Termostato` implementan esta interfaz y proporcionan sus propias implementaciones de estos métodos.

### Resumen

- **Usa una clase abstracta** cuando quieras que varias clases compartan un código común y tengan un estado común, como en el ejemplo del zoológico,
  donde todos los animales se alimentan de formas diferentes, pero comparten ciertas características y comportamientos.
- **Usa una interfaz** cuando quieras que diferentes clases sigan un contrato común pero no necesariamente compartan un código común o estado,
  como en el ejemplo de los dispositivos inteligentes, donde diferentes dispositivos pueden ser encendidos y apagados, pero la implementación varía
  significativamente entre dispositivos.
