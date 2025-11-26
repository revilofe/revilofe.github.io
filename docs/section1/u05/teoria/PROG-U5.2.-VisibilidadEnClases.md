---
title: "UD 5 - 5.2 Visibilidad en miembros de clases"
description: Visibilidad en miembros de clases
summary: Visibilidad en miembros de clases
authors:
    - Eduardo Fdez
date: 2024-01-31
icon: "material/file-document-outline"
permalink: /prog/unidad5/5.2
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 5.2. Visibilidad en miembros de clases

En Kotlin, al igual que en una base de superhéroes, no todo el mundo puede entrar en todas las áreas. Hay diferentes niveles de acceso dependiendo de quién seas y qué permisos tengas. Los modificadores de visibilidad de Kotlin controlan exactamente esto: quién puede acceder a tus clases, interfaces, funciones y propiedades. Vamos a ver los diferentes niveles de acceso disponibles:

### 1. Visibilidad

Los modificadores de visibilidad se utilizan para determinar qué otros elementos del código tienen acceso al elemento que se está consultando/modificando. Se aplican a algunos elementos diferentes en el código, en varios niveles de alcance. La forma en que se aplican estas reglas puede variar ligeramente entre estos diferentes usos, lo que puede resultar confuso al principio.

Las clases, objetos, interfaces, constructores, funciones/métodos, propiedades/atributos y sus _'setters'_ pueden tener modificadores de visibilidad. (Los _'setters'_ tendrán una visibilidad igual o más restrictiva que la propiedad).

#### 1.1. Public

Este es el valor predeterminado, y se puede acceder a cualquier clase, función/método, propiedad/atributo, interfaz u objeto que tenga este modificador desde cualquier lugar.

#### 1.2. Private

Se puede acceder a una función/método, interfaz o clase de nivel superior que se declara como privada SOLO desde dentro del mismo archivo.

Cualquier función/método o propiedad/atributo que se declare privada dentro de una clase, objeto o interfaz solo puede ser visible para otros miembros de esa misma clase, objeto o interfaz.

Un constructor privado debe usar la palabra clave `'constructor'`. Si un constructor es marcado como privado no se puede instanciar un objeto con ese constructor, tendrá que usarse desde dentro de la misma clase. Su uso más común es para crear objetos singleton, desde un companion object un método llama al constructor, creando una instancia de la clase y se guarda en una propiedad del companion object, y se crea otro método de clase para acceder a esa propiedad.

```kotlin
class Car private constructor(val name: String, val plateNo: String) {
    companion object {
        private val car = Car("BMW", "1234")
        fun getInstance() = car
      
    }
}
// Obtengo el objeto coche. 
fun main(){
    var car = Car.getInstance()
}
```

#### 1.3. Protected

Solo se puede aplicar a propiedades/atributos o funciones/métodos dentro de una clase, objeto o interfaz, no se puede aplicar a funciones, clases o interfaces de nivel superior. Las propiedades o funciones con este modificador solo son accesibles dentro de la clase que lo define y cualquier subclase.

#### 1.4. Internal

En un proyecto que tiene un módulo (módulo Gradle o Maven), una clase, objeto, interfaz o función especificada con este modificador dentro de ese módulo solo es accesible desde ese módulo.

#### Actividad 1: Jugando con Modificadores de Visibilidad   
**Pregunta:** ¿Cómo afectan los modificadores de visibilidad al acceso de una propiedad dentro de una clase y desde fuera de ella en Kotlin?

  Supongamos que tienes una clase `Libro` que tiene una propiedad `titulo` y un método `mostrarTitulo()`. Queremos entender cómo los diferentes modificadores de visibilidad (`private`, `protected`, `internal`, `public`) afectan la capacidad de acceder a `titulo` desde dentro de la clase, desde una subclase, y desde fuera de cualquier clase.  

**Código:**

  ```Kotlin
  open class Libro {
      var titulo: String = "El secreto de Kotlin"
  
      fun mostrarTitulo():String {
          return titulo.uppercase()
      }
  }
  
  class Novela : Libro() {
      fun revelarTitulo():String {
          titulo.uppercase()
      }
  }
  
  fun main() {
      val miLibro = Libro()
      println(miLibro.mostrarTitulo())  // Intenta acceder a titulo desde aquí
      println(miLibro.titulo)  // Intenta acceder a titulo desde aquí
    
      val miNovela = Novela()
      println(miNovela.revelarTitulo())  // Intenta acceder a titulo desde aquí
      println(miNovela.titulo)  // Intenta acceder a titulo desde aquí
  }
  ```

**Respuesta:** Para entender el impacto de los modificadores de visibilidad, vamos a modificar el modificador de visibilidad de la propiedad `titulo` en la clase `Libro` y observar los resultados:

  * **`public` (Por defecto):** La propiedad `titulo` es accesible desde cualquier parte del código. En este caso, tanto `mostrarTitulo()` dentro de `Libro` como `revelarTitulo()` dentro de `Novela` pueden acceder a `titulo`, así como el acceso directo a `titulo` desde `main`.
  * **`private`:** La propiedad `titulo` solo es accesible dentro de la clase `Libro`. Ni `Novela` ni el método `main` pueden acceder a `titulo` directamente. Tendrías que usar `mostrarTitulo()` para ver el título.
  * **`protected`:** Similar a `private`, pero permite el acceso desde subclases. En este caso, `revelarTitulo()` en `Novela` puede acceder a `titulo`, pero `main` no puede.
  * **`internal`:** La propiedad `titulo` es accesible desde cualquier archivo dentro del mismo módulo. Si `Libro`, `Novela`, y `main` están en el mismo módulo, todos pueden acceder a `titulo`. Este acceso es restringido fuera del módulo.

  Para modificar el código y probar cada uno de estos escenarios, simplemente cambia el modificador de `titulo` en `Libro` a `private`, `protected`, o `internal` y observa los errores de compilación que surgen al intentar acceder a `titulo` desde diferentes partes del código.

### 2. Resumen

Aquí te dejo una forma divertida de recordarlo:

* Public: Como un parque público; abierto a todos.
* Private: Como tu diario personal; solo para tus ojos.
* Protected: Como la cocina en una fiesta; solo para el equipo y familiares cercanos.
* Internal: Como un club local; solo para los miembros de la comunidad.

¡Ahora ya tienes el poder de controlar quién puede acceder a las partes de tu código, como un verdadero maestro de la base secreta de superhéroes de Kotlin!

---

## Reference

* [Modificadores de acceso](https://kotlinlang.org/docs/visibility-modifiers.html)
* [Visibility Modifiers](https://www.baeldung.com/kotlin/visibility-modifiers)

## Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)

