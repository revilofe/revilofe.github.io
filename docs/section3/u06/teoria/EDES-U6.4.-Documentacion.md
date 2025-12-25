---
title: "UD 6 - 6.4 Documentación y comentarios"
description: Documentación y comentarios
summary: Documentación y comentarios
authors:
    - Eduardo Fdez
date: 2023-01-20
icon: "material/file-document-outline"
permalink: /edes/unidad6/4.4
categories:
    - EDES
tags:
    - EDES
    - Dokka
    - KDoc
---

## 6.4. Documentación y comentarios.

### 1. Documentacion y comentarios

A la hora de comentar, hay dos escuelas:

1. Usar los comentarios para **clarificar lo que quisiste expresar con tu código**
2. **Evitarlos al máximo** y que comentar tu código es un mal necesario que sólo denota tu falta de habilidad para no hacer código lo suficientemente claro.

>¿A cuál de los dos consejos deberías hacerle caso?

Un sistema **sin documentación** está **incompleto**. Para tener **calidad**, necesita tener **documentación**, pero esta tiene que tener sentido,  es decir, *información acerca del sistema que comunique cosas, como la razón de existir de ciertos módulos, valores y funciones y cómo usarlo*.

Si más tardes tienes que modificar el software, estos comentarios, facilitarán la **comprensíón** de lo que los programadores anteriores hicieron o intentarón hacer.

#### 1.1. ¿Dónde situar la documentación?

Por tanto la documentación es **totalmente necesaria**, pero ¿donde la ponemos?    

- Mala práctica: En documentos **separados** del código. Suelen **olvidarse** y no se mantienen.
- Buena práctica: Lo más **cerca del código**, para eso tenemos los comentarios, **facilitará encontrarlos y mantenerlos**.
  

#### 1.2. ¿Qué documentar?

Puedes usar los comentarios para **documentar**:   

- Decisiones de diseño.   
- Explicaciones sobre la existencia, funcionamiento o razón de ser de cierta parte del código.   
- Las interfaces y su ejemplo de uso.   
- Efectos de usar cierto código.   
- Partes no finalizadas o que se pueden mejorar (TODO’s).   


#### 1.3. ¿Por qué documentar?
Ten en cuenta que los comentarios pueden **ayudarte en el futuro**, ya que estarán ahi para recordarte lo que hiciste y por qué lo hiciste. Por ejemplo ,seguramente tu mente haya borrado información valiosa de por qué una variable tiene un valor de inicio y no otro. Por tanto, tu yo futuro y tu equipo te agradecerán los comentarios aclaratorios de tomas de decisiones.  

Además, los comentarios son una **buena herramienta de diseño**. Existen gurus, como John Ousterhout, en “A Philosophy of Software Design” que recomienda **empezar con los comentarios antes de programar**. Pero, ¿por qué lo recomienda? Escribir en un lenguaje humano cómo funciona algo antes de implementarlo realmente, te da la capacidad de
**ver si es lógico y suficiente**, además te permite **ponerte en los zapatos del usuario** para notar deficiencias sobre todo en la interfaz. Los **comentarios de la interfaz es lo primero que deberías crear** porque te servirán de guía para avanzar con tu diseño y, sobre todo, que sea lógico y fácil de usar.  

**El lenguaje de programación no es suficiente** para expresar todo lo necesario. Todos los lenguajes de programación están pensados para ser un subconjunto del lenguaje humano que elimine las ambigüedades, manteniendo el mayor poder expresivo posible. Esto nos lleva a sus limitantes: es **imposible**, o por lo menos impráctico, **intentar expresar todas las ideas con el código**.  En la práctica, el tiempo y los recursos para lograr algo son limitados, por lo que a veces es más conveniente y fácil para todos explicar lenguaje humano algo que intentar expresarlo con código, como los puristas afirman.  

No te sientas mal si tienes que recurrir de vez en cuando a explicar la forma en que funciona algo, siempre y cuando *no sea la práctica común*.

#### 1.4. ¿Cómo usar los comentarios para que sean valiosos?

Como una buena guía, si no eres capaz de crear un comentario **concreto y corto** sobre cómo funciona o por qué existe algo, lo más probable es que **tengas que re-pensar tu diseño**.

No todos los comentarios son valiosos, hay **algunos que pueden estorbar** más de lo que ayudan, por ejemplo, los que no aportan información a lo que es obvio en el código.

Hablemos de algunas formas de **aprovecharlos lo mejor posible** para que contribuyan positivamente a aumentar la calidad del proyecto:    

- Escribe *los comentarios primero*: Una de las partes más importantes de los comentarios como documentación es que **deben ser concretos, cercanos a la realidad y que proporcionen la mayor cantidad de información útil posible**.  Para lograr esto, se tienen que **crear lo más cerca que puedas a la creación del código**. Pero como todos sabemos que después de escribir y probar (básicamente) el código vamos a sentir que ya está terminado, por tanto, es buena
  práctica obligarte a escribirlos antes, **justo como propone TDD con las pruebas**. De esta manera te asegurarás que tu código esté documentado incluso antes de escribirlo y **te servirán como una herramienta de diseño** que te ayudará a pensar mejor en la usabilidad de tus módulos y piezas de software.   

- *Crea comentarios sobre la interfaz*: **La interfaz es el medio de uso que tus módulos o funciones presentan** para que las demás partes de tu sistema lo usen. Lo primero que deberías documentar y explicar es esta interfaz, para que más personas a parte de ti puedan usar este pedazo de código.    

- *Escribe comentarios claros* sobre:    
   
    * **Cómo usar esa pieza de código**   
    * **Por qué existe esa parte del sistema**   
    * **Qué efectos tiene usarla**   

    Este tipo de comentarios son los que aportan mayor valor al sistema y si están lo suficientemente completos, con ejemplos y explicaciones claras, son una documentación válida que está en un muy buen lugar: es fácil de encontrar y no se va a perder enterrada entre otros documentes que después nadie va a consultar.  

- *Evita los comentarios sobre la implementación*: Los comentarios sobre la implementación son aquellos que describen qué estás haciendo, como por ejemplo, sumar número, abrir un archivo, etc. Estos comentarios normalmente **son innecesarios**, ya que lo que se está haciendo es obvio si el código es lo suficientemente expresivo y siempre deberíamos buscar que sea así. De hecho, estos son los comentarios que hacen que la gente odie a los comentarios en general, pues **en vez de proporcionar información extra son una carga que hay que mantener y pueden confundir si no son actualizados**. Si realmente sientes que tienes que explicar qué estás haciendo con cierta pieza de código, primero **pregúntate si no hay una manera de reescribirlo para que sea obvio**. Si no existe o no es práctica esta solución, entonces escribe el comentario de la manera más concisa posible, incluyendo la razón de la existencia de ese código. Para hacer esto debes tomar muy en cuenta los recursos del proyecto: **no te puedes tardar el triple del tiempo** implementando la pieza de código perfecta porque no quieres escribir un comentario que explique cómo funciona.    

> Escribir comentarios es una de las grandes tareas que los programadores debemos dominar. Los lenguajes de programación y los entornos de programación cada vez le dan más poder a esta parte de los programas y permiten incluso escribir pruebas en ellos, generar documentación automática y listar tareas a partir de ellos.
> Si pones el suficiente esmero en aprender a escribir buenos comentarios y mantenerlos, serán una gran herramienta de diseño y documentación de tu software.

### 2. Herramientas para documentar
#### 2.1. DOKA
[Dokka](https://kotlin.github.io/dokka/2.1.0-Beta/)

- Herramienta que nos permite generar la documentación en distintos formatos.
- Configuración básica y mínima: Añade al fichero `build.gradle.kts:`

```kotlin
plugins {
    id("org.jetbrains.dokka") version "2.0.0"
}

repositories {
    mavenCentral()
}
```
Ahora en aparecerán nuevas tareas en la pestaña de gradle.

Para generar documentación, ejecute las siguientes tareas de Gradle:    

* `dokkaHtml` para compilaciones de un solo proyecto.
* `dokkaHtmlMultiModule` para compilaciones de múltiples proyectos.

De forma predeterminada, el directorio de salida se establece en `/build/dokka/html` y `/build/dokka/htmlMultiModule`.

#### 2.2. KDOC

[Sintaxis de KDoc](https://kotlinlang.org/docs/kotlin-doc.html#kdoc-syntax)

- **Lenguaje que permite documentar**.
- Documenta la interface de las clases, métodos, propiedades, etc.
- Para genera la documentación, en las opciones de `Gradle`, busca la tarea `Task->Documentación->DokkaHtml` y púlsala.
- La documentación se genera en la carpeta `build` de tu proyecto.

## Bibliografía y fuente    
* [Deberías comentar tu código - Héctor Patricio](https://blog.thedojo.mx/2020/12/30/deberias-comentar-tu-codigo.html)
* [Como escribir comentarios para documentar tu código](https://www.oracle.com/es/technical-resources/articles/java/javadoc-tool.html)
* [Document Kotlin code: KDoc](https://kotlinlang.org/docs/kotlin-doc.html)
* Head First Kotlin, A Brain-Friendly Guide; Dawn Griffiths & David Griffiths; 2019 - O'Reilly Media
* A Philosophy of Software Design, John Ousterhout. (Le dedica 4 capítulos a buen uso de los comentarios)
