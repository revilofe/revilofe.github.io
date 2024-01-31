---
title: "UD 5 - 5.1 Revisión de las clases"
description: kotlin
summary: kotlin
authors:
    - Eduardo Fdez
date: 2022-11-14
icon:   
permalink: /prog/unidad4/4.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 

### 1. Revisión de las clases

En Kotlin, la Programación Orientada a Objetos (POO) se maneja con una sintaxis concisa y poderosas características que simplifican la codificación y mejoran la legibilidad. Entre estas características, las clases y objetos juegan un papel central, permitiendo a los desarrolladores modelar el mundo real de manera eficiente y efectiva. Kotlin, diseñado para ser completamente interoperable con Java, introduce mejoras significativas sobre este, haciendo que el trabajo con POO sea más intuitivo y menos propenso a errores.

#### 1.1. Data Class

Las "data class" en Kotlin están específicamente diseñadas para clases que actúan principalmente como portadoras de datos. En otros lenguajes de programación, la creación de este tipo de clases requiere definir explícitamente constructores, métodos `getter` y `setter`, y otros métodos como `equals()`, `hashCode()`, y `toString()`. Kotlin simplifica este proceso permitiendo que el compilador genere automáticamente estos miembros a partir de la declaración de las propiedades en el constructor primario.

```kotlin
data class Usuario(val nombre: String, val edad: Int)
```

En el ejemplo anterior, `Usuario` es una data class con dos propiedades: `nombre` y `edad`. Kotlin automáticamente proporciona una implementación de `equals()`, `hashCode()`, `toString()`, así como las funciones `componentN()` para cada propiedad, y una función `copy()`. Esto hace que las data class sean ideales para representar inmutables "puros" de datos sin la necesidad de escribir código boilerplate.

Aqui puedes ver un ejemplo en el que se compara una data class en java con una data class en kotlin: [data Class](https://devexpert.io/data-classes-kotlin/)

#### 1.2. **Enumerados (Enums)**

Los tipos enumerados en Kotlin sirven para definir un conjunto de constantes nombradas, mejorando la claridad y la seguridad del código. Además de definir valores fijos, Kotlin permite que los enums contengan propiedades y métodos.

```Kotlin
enum class Estado {
    ACTIVO, INACTIVO, PENDIENTE
}
```

Kotlin permite una mayor personalización y funcionalidad dentro de los enums, incluyendo la definición de constructores para pasar valores adicionales.

Aqui puedes ver un ejemplo más avanzado sobre el uso de enum class en kotlin: [enum Class](https://www.baeldung.com/kotlin/enum)

#### 3. **Genéricos**

Los genéricos en Kotlin permiten la creación de clases, interfaces y funciones que pueden operar sobre tipos que se especifican al momento de la instancia. Esto facilita la reutilización del código y mejora la seguridad de tipo.

<pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">class Caja<T>(val contenido: T)
</code></div></div></pre>

Aquí, `Caja` es una clase genérica que puede almacenar cualquier tipo de objeto especificado al momento de su creación, garantizando que el tipo de `contenido` se conozca y se restrinja adecuadamente.

#### 4. **Objects**

Kotlin introduce el concepto de `object` para definir un singleton, una clase objeto o un objeto compañero dentro de otra clase. Esto permite una fácil creación de singletons y la definición de miembros estáticos en un contexto orientado a objetos.

<pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">object Configuracion {
    val urlServidor = "https://mi.api.com"
    fun imprimirUrl() {
        println(urlServidor)
    }
}
</code></div></div></pre>

En este ejemplo, `Configuracion` es un singleton que mantiene la configuración global de una aplicación.

Estas características avanzadas de Kotlin ofrecen una forma poderosa y flexible de trabajar con POO, permitiendo a los desarrolladores concentrarse en la lógica de negocio mientras minimizan el código repetitivo y propenso a errores. Con estas herramientas, Kotlin se establece como un lenguaje moderno y eficiente para el desarrollo de aplicaciones.


### Herencia en Kotlin

La herencia es un concepto clave en la Programación Orientada a Objetos (POO), permitiendo a los desarrolladores crear nuevas clases basadas en otras preexistentes. Esta característica es esencial para reutilizar, extender y modificar el comportamiento de clases ya definidas, promoviendo así la eficiencia y la reducción de la redundancia en el código.

En Kotlin, la herencia se maneja con una sintaxis clara y reglas específicas diseñadas para mantener la seguridad y la claridad del código:

1. **Superclase y Subclase:**
   * La **superclase** (o clase base) es la clase existente de la que se deriva una nueva clase.
   * La **subclase** (o clase derivada) es la nueva clase creada, que hereda propiedades y métodos de la superclase.
2. **Herencia Implícita:**
   * Al heredar de una superclase, la subclase obtiene automáticamente todos los campos, propiedades y métodos de dicha superclase, incluyendo aquellos heredados por la superclase de otras superclases, si las hay.
3. **Restricción de Herencia:**
   * Kotlin permite una herencia simple, significando que una subclase solo puede tener una clase base directa, aunque puede implementar múltiples interfaces.
4. **Herencia Transitiva:**
   * La herencia es transitiva. Si una clase C hereda de B, y B hereda de A, entonces C indirectamente hereda de A.
5. **Clase Any:**
   * Todas las clases en Kotlin heredan de `Any`, la superclase predeterminada que proporciona métodos básicos como `equals()`, `hashCode()`, y `toString()`.

#### Actividad 1: Herencia de `Any`

* **Pregunta:** ¿Qué métodos y propiedades hereda `Example` de `Any`?
* **Código:**
  <pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">class Example
  </code></div></div></pre>
* **Respuesta:**`Example` hereda de `Any` los métodos `equals()`, `hashCode()`, y `toString()`.

#### Declaración de Herencia

Para que una clase herede de otra en Kotlin, se coloca el nombre de la clase base después de los dos puntos en el encabezado de la subclase. Las clases en Kotlin son `final` por defecto; para permitir la herencia, se debe usar `open`.

#### Actividad 2: Instancia de Clases Base y Derivadas

* **Pregunta:** ¿Crear una variable de clase `Base`? ¿Puedes asignarle una instancia de `DerivedWithConstructor`?
* **Código:**
  <pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">open class Base(var p: Int)
  class DerivedWithConstructor(p: Int) : Base(p)
  </code></div></div></pre>
* **Respuesta:** Sí, puedes crear una variable de tipo `Base` y asignarle una instancia de `DerivedWithConstructor` debido a la herencia.

#### Herencia sin Constructor Primario

Si una clase derivada no tiene un constructor primario, cada constructor secundario debe inicializar la clase base usando `super` o delegar a otro constructor que lo haga.

#### Actividad 3: Trabajando con Constructores Secundarios

* **Pregunta:** Ejecuta el siguiente código, instancia la subclase con 1 e imprime el valor de `p`. ¿Qué muestra en pantalla? ¿Qué sucede si quitas el constructor de la subclase? ¿Podemos definir la subclase de otra forma? ¿Qué tenemos que hacer para llamar al constructor de 2 parámetros?
* **Código:**
  <pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">open class Base(var p: Int) {
      constructor(p: Int, q: Int): this(p)
  }

  class DerivedWithoutConstructor : Base {
      constructor(p: Int) : super(p)
  }

  fun main() {
      val instancia = DerivedWithoutConstructor(1)
      println(instancia.p)
  }
  </code></div></div></pre>
* **Respuesta:**
  * Al ejecutar, muestra `1` en pantalla, indicando el valor de `p`.
  * Si quitas el constructor de la subclase, el código no compilará porque `DerivedWithoutConstructor` necesita definir cómo inicializar `Base`.
  * Para definir la subclase de otra manera, podríamos considerar agregar un constructor primario o utilizar un constructor secundario que llame al constructor de dos parámetros de `Base`.
  * Para llamar al constructor de 2 parámetros de `Base`, necesitamos definir explícitamente ese constructor en la subclase y utilizar `super(p, q)` dentro del constructor secundario.



---

## Reference

* [https://kotlinlang.org/docs/reference/](https://kotlinlang.org/docs/reference/)
* [https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209](https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209)
* [https://www.packtpub.com/application-development/programming-kotlin](https://www.packtpub.com/application-development/programming-kotlin)
* [https://learnxinyminutes.com/docs/kotlin/](https://learnxinyminutes.com/docs/kotlin/)
* [https://gist.github.com/dodyg/5823184](https://gist.github.com/dodyg/5823184)
* [https://gist.github.com/dodyg/5616605](https://gist.github.com/dodyg/5616605)
* [https://github.com/Zhuinden/guide-to-kotlin](https://github.com/Zhuinden/guide-to-kotlin)
* [https://superkotlin.com/kotlin-mega-tutorial/](https://superkotlin.com/kotlin-mega-tutorial/)
* [https://revilofe.github.io/IESRA-DAM-Prog/#/](https://revilofe.github.io/IESRA-DAM-Prog/#/)

## Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)

## License

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)
Esta obra está bajo una [licencia de Creative Commons Reconocimiento-Compartir Igual 4.0 Internacional](http://creativecommons.org/licenses/by-sa/4.0/).
```
