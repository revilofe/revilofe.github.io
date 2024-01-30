---
title: "UD 4 - 4.1 kotlin"
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
# Revisión de las clases

En Kotlin, la Programación Orientada a Objetos (POO) se maneja con una sintaxis concisa y poderosas características que simplifican la codificación y mejoran la legibilidad. Entre estas características, las clases y objetos juegan un papel central, permitiendo a los desarrolladores modelar el mundo real de manera eficiente y efectiva. Kotlin, diseñado para ser completamente interoperable con Java, introduce mejoras significativas sobre este, haciendo que el trabajo con POO sea más intuitivo y menos propenso a errores.

## 1. Data Class

Las "data class" en Kotlin están específicamente diseñadas para clases que actúan principalmente como portadoras de datos. En otros lenguajes de programación, la creación de este tipo de clases requiere definir explícitamente constructores, métodos `getter` y `setter`, y otros métodos como `equals()`, `hashCode()`, y `toString()`. Kotlin simplifica este proceso permitiendo que el compilador genere automáticamente estos miembros a partir de la declaración de las propiedades en el constructor primario.

```kotlin
data class Usuario(val nombre: String, val edad: Int)


En el ejemplo anterior, `Usuario` es una data class con dos propiedades: `nombre` y `edad`. Kotlin automáticamente proporciona una implementación de `equals()`, `hashCode()`, `toString()`, así como las funciones `componentN()` para cada propiedad, y una función `copy()`. Esto hace que las data class sean ideales para representar inmutables "puros" de datos sin la necesidad de escribir código boilerplate.

#### 2. **Enumerados (Enums)**

Los tipos enumerados en Kotlin sirven para definir un conjunto de constantes nombradas, mejorando la claridad y la seguridad del código. Además de definir valores fijos, Kotlin permite que los enums contengan propiedades y métodos.

<pre><div class="dark bg-black rounded-md"><div class="flex items-center relative text-token-text-secondary bg-token-surface-primary px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>kotlin</span><span class="" data-state="closed"><button class="flex gap-1 items-center"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M12 4C10.8954 4 10 4.89543 10 6H14C14 4.89543 13.1046 4 12 4ZM8.53513 4C9.22675 2.8044 10.5194 2 12 2C13.4806 2 14.7733 2.8044 15.4649 4H17C18.6569 4 20 5.34315 20 7V19C20 20.6569 18.6569 22 17 22H7C5.34315 22 4 20.6569 4 19V7C4 5.34315 5.34315 4 7 4H8.53513ZM8 6H7C6.44772 6 6 6.44772 6 7V19C6 19.5523 6.44772 20 7 20H17C17.5523 20 18 19.5523 18 19V7C18 6.44772 17.5523 6 17 6H16C16 7.10457 15.1046 8 14 8H10C8.89543 8 8 7.10457 8 6Z" fill="currentColor"></path></svg>Copy code</button></span></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-kotlin">enum class Estado {
    ACTIVO, INACTIVO, PENDIENTE
}
</code></div></div></pre>

Kotlin permite una mayor personalización y funcionalidad dentro de los enums, incluyendo la definición de constructores para pasar valores adicionales.

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
