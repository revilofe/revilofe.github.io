---
title: "UD 6 - 6.3 Análisis estático de código"
description: Análisis estático de código
summary: Análisis estático de código
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: "material/file-document-outline"
permalink: /edes/unidad6/4.3
categories:
    - EDES
tags:
    - EDES
    - Tools
    - ktlint
    - Detekt
---
## 6.3. Análisis estático de código

La relación entre las personas, los ordenadores y el código es bastante compleja. Aunque la mayoría de los códigos se desarrollan para ser ejecutados en ordenadores, su propósito no se limita a eso. También se desarrollan para ser leídos y comprendidos cuidadosamente, de hecho la mayoría de tu tiempo como programador lo dedicarás a leer código.

Desgraciadamente, el desarrollo moderno de software no va de la mano de la comprensión del código. Además, los códigos de software que no se pueden entender, mantener o mejorar tienen mayores tasas de defectos.

### 1. ¿Qué es el análisis estático de código?

El análisis estático de código es una de las técnicas que los desarrolladores y programadores emplean para analizar el código fuente en función de criterios específicos predeterminados. Esta técnica se lleva a cabo antes de la ejecución del programa y se utiliza para detectar errores funcionales y vulnerabilidades en el software que se va a desplegar. En este caso, es fácil mantener las convenciones de codificación para los equipos de desarrollo debido a la presencia de criterios predeterminados. Además, este tipo de análisis ayuda a identificar las vulnerabilidades, por lo que proporciona una herramienta importante para evitar fallos de seguridad y bugs.

Los desarrolladores también pueden revisar el código manualmente, pero esto puede dar lugar a que se produzcan fallos debido a un error humano. Y los errores de software acaban costando una cantidad significativa de tiempo y dinero, por lo que es imperativo producir códigos sin errores. Además, cada vez más empresas de desarrollo se suben al carro del análisis estático de código. Así, el análisis estático de código se considera ahora un aspecto clave a la hora de [escribir código para aplicaciones Android](https://mutualmobile.com/es/resources/top-10-best-practices-for-empathetic-coding).

### 2. Ventajas de utilizar el análisis estático de código

* Más rápido, preciso y eficiente en comparación con la revisión manual del código.
* Ayuda a identificar posibles bugs, vulnerabilidades y errores que las pruebas unitarias o manuales podrían haber pasado por alto.
* Ayuda a imbuirse de prácticas de código adecuadas.
* Analiza cada línea de código, ayudando así a conseguir un código de alta calidad.
* Ayuda a definir la estructura del proyecto que puede configurarse y personalizarse para las necesidades específicas de un proyecto.


### 3. Herramientas populares de análisis de código estático

#### 3.1. Ktlint

[Ktlint requiere poca o ninguna personalización](https://ktlint.github.io/), por lo que es fácil de usar. Esta herramienta permite centrarse en la importancia de la claridad del código y las convenciones de la comunidad por encima de las preferencias personales. Este aspecto hace que el código sea más legible y fácil de entender. Ktlint sí ofrece características de personalización; sin embargo, eso queda a discreción del desarrollador o programador. También ofrece a los desarrolladores la opción de añadir sus reglas para descubrir posibles errores, comprobar los antipatrones, etc.

#### 3.2. Detekt

[Kotlin, un lenguaje de programación multiplataforma](https://kotlinlang.org/), tiene su versión de análisis estático de código, conocida como Detekt. Esta herramienta se basa en el árbol sintáctico abstracto que proporciona el compilador de Kotlin. Detekt ofrece conjuntos de reglas *altamente configurables*, lo que la hace muy usada. Además, Detekt también proporciona las características de análisis de *code smell**, informes de complejidad en las líneas del código y [complejidad ciclomática](https://johndev.co/posts/ciclomatic-complexity/).

#### 3.3. FindBugs

FindBugs analiza los Bytecodes de Java, especialmente los *archivos .class,* para buscar posibles errores y fallos de diseño. Esta herramienta necesita código compilado para ser empleada. Los aspectos clave de FindBugs incluyen la corrección de malas prácticas, la corrección multihilo, la detección de código dudoso, el rendimiento malicioso, la vulnerabilidad del código, la seguridad experimental y la internacionalización.

#### 3.4. Checkstyle

Checkstyle analiza el código fuente del proyecto en busca de errores y fallos, al tiempo que trabaja para mejorar el estándar del código. También ayuda a verificar el código fuente para las convenciones de codificación.

#### 3.5. Android Lint

Android Lint viene empaquetado por defecto con Android Studio. Esta herramienta comprueba los archivos fuente del proyecto para identificar posibles errores y optimizar la usabilidad, la corrección, la seguridad, la accesibilidad y la internacionalización.

### 6. Linting en el análisis estático de código

Te preguntarás, ¿qué demonios es el linting? Bueno, en pocas palabras, linting es el proceso de analizar el código en busca de errores potenciales. Veamos cómo puedes usar linting para diagnosticar errores. Los desarrolladores utilizan varias guías de estilo, como [Java Code Style](https://source.android.com/setup/contribute/code-style) y [Kotlin Style Guide](https://developer.android.com/kotlin/style-guide).

En este caso, vamos a utilizar Ktlint o Detekt, un linter que es sinónimo de la plataforma Kotlin, ya que este formato ofrece simplicidad, extensibilidad y una comunidad de desarrolladores activa.

#### 6.1. Uso de Ktlint

* Añade al fichero `build.gradle` de tu proyecto la configuración de ktling:

```kotlin
import org.jlleitschuh.gradle.ktlint.reporter.ReporterType

plugins {
    id("org.jlleitschuh.gradle.ktlint") version "11.0.0"
}

// Configuración de klint
ktlint {
    verbose.set(true)
    outputToConsole.set(true)
    coloredOutput.set(true)
    reporters {
        reporter(ReporterType.CHECKSTYLE)
        reporter(ReporterType.JSON)
        reporter(ReporterType.HTML)
    }
    filter {
        exclude("**/style-violations.kt")
    }
}
```   

También existe un plugin no oficial que puedes instalar.
En `File -> Settings -> Tools -> ktlint` podrás ver y trabajar en la configuración

#### 6.2. Uso de Detekt
Instala el plugin [Detekt](https://github.com/detekt/detekt).
En `File -> Settings -> Tools -> Detekt` podrás ver y trabajar en la configuración

### 5. Recursos
* [Detekt](https://github.com/detekt/detekt)
* [ktlint](https://pinterest.github.io/ktlint)

## Fuente
- [¿Qué es lo que pasa con el análisis estático del código?](https://mutualmobile.com/es/blog/whats-the-fuss-about-static-code-analysis)
- [Complejidad ciclomática](https://johndev.co/posts/ciclomatic-complexity/)
