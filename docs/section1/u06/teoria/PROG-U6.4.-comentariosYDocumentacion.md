---
title: "UD 6 - 6.4 Se ha comentado y documentado el código"
description: kotlin
summary: kotlin
authors:
    - Diego Cano
date: 2024-02-12
icon:   
permalink: /prog/unidad6/6.4
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
## 6.4. Se ha comentado y documentado el código.

Un código bien documentado y comentado es esencial para asegurar la calidad, mantenibilidad y escalabilidad de cualquier proyecto de software. A continuación, se detalla una guía sobre cómo abordar la documentación y los comentarios en el código, tomando en cuenta las prácticas recomendadas y la filosofía detrás de un código bien documentado.

### 1. ¿Cómo Abordar los Comentarios en el Código?

A la hora de comentar, hay dos escuelas:

   * Usar los comentarios para clarificar lo que quisiste expresar con tu código.
   * Evitarlos al máximo y que comentar tu código es un mal necesario que sólo denota tu falta de habilidad para no hacer código lo suficientemente claro.

   ***`¿A cuál de los dos consejos deberías hacerle caso?`***

Existen gurus, como *John Ousterhout*, en *“A Philosophy of Software Design”* que recomienda ***empezar con los comentarios antes de programar***. Pero, ***¿por qué lo recomienda?***

> Escribir en un lenguaje humano cómo funciona algo antes de implementarlo realmente, te da la capacidad de ver si es lógico y suficiente, además te permite ponerte en los zapatos del usuario para notar deficiencias sobre todo en la interfaz.
> Los comentarios de la interfaz es lo primero que deberías crear porque te servirán de guía para avanzar con tu diseño y, sobre todo, que sea lógico y fácil de usar.

Aunque existen diferentes opiniones sobre el uso de comentarios en el código, es indiscutible que un sistema sin documentación es incompleto. La documentación y los comentarios bien pensados son cruciales para entender la razón de ser de ciertos módulos, funciones, y decisiones de diseño dentro del sistema. 

### 2. Directrices sobre cómo y cuándo usar comentarios

1. **Documentar Decisiones de Diseño y Arquitectura**: Es importante usar comentarios para explicar el "por qué" detrás de decisiones de diseño específicas que no son obvias a través del código.
   Esto incluye la razón de existir de ciertas clases, módulos o funciones, especialmente cuando estas decisiones afectan la arquitectura o el funcionamiento global del sistema.

2. **Comentarios sobre la Interfaz y Ejemplos de Uso**: Los comentarios deben clarificar cómo se utiliza una clase o función, incluyendo ejemplos de uso cuando sea posible.
   Esto es especialmente valioso para las interfaces y las clases abstractas, donde el comportamiento específico no se define completamente en el código.

3. **Uso de TODO’s para Indicar Mejoras y Trabajo Pendiente**: Utilizar comentarios para marcar áreas del código que requieren mejoras, trabajo pendiente o refactorización es una práctica común.
   Sin embargo, es importante gestionar estos comentarios adecuadamente para asegurar que se atienden en el tiempo y no perduren en el código de manera permanente sin resolver.

4. **Evitar Comentarios Obvios sobre la Implementación**: Los comentarios deben aportar valor y no simplemente reiterar lo que el código ya expresa claramente.
   En lugar de comentar cada línea de código, enfócate en explicar complejidades, algoritmos no triviales o comportamientos que no son inmediatamente claros.

### 3. Herramientas de Documentación: DOKKA y KDoc

- **DOKKA**: Es una herramienta de documentación para Kotlin que permite generar documentación de alta calidad directamente desde los comentarios del código.
  La configuración básica en el fichero `build.gradle.kts` habilita nuevas tareas en Gradle para generar la documentación en formatos accesibles.

   ```kotlin
 	 plugins {
      id("org.jetbrains.dokka") version "1.6.10"
	 } 

 	 repositories {
      mavenCentral()
	 }
   ```

  [Enlace a la web oficial de DOKKA](https://kotlin.github.io/dokka/1.6.10/)
  
- **KDoc**: Es el lenguaje de documentación para Kotlin, similar a JavaDoc para Java. KDoc se utiliza para documentar la interfaz pública de las clases, métodos, propiedades, etc.
  Permite a los desarrolladores escribir documentación estructurada y rica directamente en el código, la cual luego puede ser procesada por herramientas como DOKKA para generar documentación externa.

  [Document Kotlin code: KDoc](https://kotlinlang.org/docs/kotlin-doc.html)

### Ejemplo de Documentación con KDoc

```kotlin
/**
 * Representa un artículo en una biblioteca digital.
 *
 * Esta clase es la base para diferentes tipos de medios como libros, revistas y películas.
 * @property titulo El título del artículo.
 * @property autor El autor o director del artículo.
 * @property disponible Indica si el artículo está disponible para préstamo.
 */
abstract class Articulo(val titulo: String, val autor: String, var disponible: Boolean = true) {
    /**
     * Proporciona una descripción detallada del artículo.
     */
    abstract fun descripcion()
}
```

### 4. Consejos a la hora de documentar tu proyecto

Ya hemos visto que un sistema sin documentación está incompleto. Para tener un software de calidad, se necesita tener documentación, pero esta tiene que tener sentido: es decir, información acerca del sistema que comunique cosas como la razón de existir de ciertos módulos, valores y funciones y cómo usarlo.

   - La documentación debe ubicarse lo más cerca posible del código, para eso tenemos los comentarios, facilitará encontrarlos y mantenerlos.

   - Los comentarios pueden ayudarte en el futuro.

   - Estarán ahi para recordarte lo que hiciste y por qué.
   
   - Seguramente tu mente haya borrado información valiosa de por qué una variable tiene un valor de inicio y no otro.
   
   - Tu yo futuro y tu equipo te agradecerán los comentarios aclaratorios de tomas de decisiones.
   
   - Los comentarios son una buena herramienta de diseño.
   
   - Si no eres capaz de crear un comentario concreto y corto sobre cómo funciona o por qué existe algo, lo más probable es que tengas que re-pensar tu diseño.

#### 4.1. Puedes usar los comentarios para documentar:

   1. Decisiones de diseño.
   
   2. Explicaciones sobre la existencia, funcionamiento o razón de ser de cierta parte del código.
   
   3. Las interfaces y su ejemplo de uso.
   
   4. Efectos de usar cierto código.
   
   5. Partes no finalizadas o que se pueden mejorar (TODO’s).

El lenguaje de programación no es suficiente para expresar todo lo necesario.

Todos los lenguajes de programación están pensados para ser un subconjunto del lenguaje humano que elimine las ambigüedades, manteniendo el mayor poder expresivo posible. 

Esto nos lleva a sus limitaciones: es imposible, o por lo menos no muy práctico, intentar expresar todas las ideas con el código.

En la práctica, el tiempo y los recursos para lograr algo son limitados, por lo que a veces es más conveniente y fácil para todos explicar con lenguaje humano algo que 
intentar expresarlo con código, como los puristas afirman.

No te sientas mal si tienes que recurrir de vez en cuando a explicar la forma en que funciona algo, siempre y cuando no sea la práctica común.

#### 4.2. ¿Cómo usar los comentarios para que sean valiosos?

   - No todos los comentarios son valiosos, hay algunos que pueden estorbar más de lo que ayudan, por ejemplo, los que no aportan información a lo que es obvio en el código.
   
   - Una de las partes más importantes de los comentarios como documentación es que deben ser concretos, cercanos a la realidad y que proporcionen la mayor cantidad de información útil posible.
   
   - Para lograr esto, se tienen que crear lo más cerca que puedas a la creación del código.
  
   - Pero como todos sabemos que después de escribir y probar (básicamente) el código vamos a sentir que ya está terminado, es buena práctica obligarte a ***"escribir los comentarios primero"***.
 
   - De esta manera te asegurarás que tu código esté documentado incluso antes de escribirlo y te servirán como una herramienta de diseño que te ayudará a pensar mejor en la usabilidad de tus módulos y piezas de software.

   - Crear comentarios sobre la interfaz.
 
   - La interfaz es el medio de uso que tus módulos o funciones presentan para que las demás partes de tu sistema lo usen.

   - Lo primero que deberías documentar y explicar es esta interfaz, para que más personas a parte de ti puedan usar este pedazo de código.

   - Debes escribir comentarios claros sobre:
	    * Cómo usar esa pieza de código
	    * Por qué existe esa parte del sistema
	    * Qué efectos tiene usarla

   - Este tipo de comentarios son los que aportan mayor valor al sistema y si están lo suficientemente completos, con ejemplos y explicaciones claras, son una documentación válida que está en un muy buen lugar:
     es fácil de encontrar y no se va a perder enterrada entre otros documentes que después nadie va a consultar.

#### 4.3. No hacer cuando documentamos

   - Evita los comentarios sobre la implementación.

   - Los comentarios sobre la implementación son aquellos que describen qué estas haciendo, como por ejemplo, sumar número, abrir un archivo, etc.

   - Estos comentarios normalmente son innecesarios, ya que lo que se está haciendo es obvio si el código es lo suficientemente expresivo y siempre deberíamos buscar que sea así.

   - De hecho, estos son los comentarios que hacen que la gente odie a los comentarios en general, pues en vez de proporcionar información extra son una carga que hay que mantener y pueden confundir si no son actualizados.

   - Si realmente sientes que tienes que explicar qué estás haciendo con cierta pieza de código, primero pregúntate si no hay una manera de reescribirlo para que sea obvio.

   - Si no existe o no es práctica esta solución, entonces escribe el comentario de la manera más concisa posible, incluyendo la razón de la existencia de ese código.

   - Para hacer esto debes tomar muy en cuenta los recursos del proyecto: no te puedes tardar el triple del tiempo implementando la pieza de código perfecta porque no quieres escribir un comentario que explique cómo funciona.

### 5. Conclusión

> Escribir comentarios es una de las grandes tareas que los programadores debemos dominar. Los lenguajes de programación y los entornos de programación cada vez le dan más poder a esta parte de los programas y permiten incluso escribir pruebas en ellos, generar documentación automática y listar tareas a partir de ellos.
> Si pones el suficiente esmero en aprender a escribir buenos comentarios y mantenerlos, serán una gran herramienta de diseño y documentación de tu software.

La documentación y los comentarios en el código son herramientas indispensables para cualquier desarrollador. Facilitan la comprensión del sistema, ayudan en la futura mantenibilidad del código y 
mejoran la colaboración dentro de equipos de desarrollo. Al seguir las prácticas recomendadas y utilizar herramientas como DOKKA y KDoc, puedes asegurar que tu documentación sea útil, relevante y 
fácilmente accesible tanto para ti como para tus colegas en el futuro.

 
