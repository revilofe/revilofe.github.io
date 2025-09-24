---
title: "UD 1 - 1.2 Documentación y herramientas"
description: Introducción a la documentación de software y sus principales herramientas
summary: Qué es la documentación de software, por qué es importante y qué herramientas existen para generarla en diferentes lenguajes.
authors:
    - Eduardo Fdez
date: 2025-09-24
icon:   
permalink: /deaw/unidad1/1.2
categories:
    - DAW
tags:
    - Documentación
    - KDoc
    - Javadoc
    - MkDocs
    - Doxygen
---

## 1.2. Documentación y herramientas
En esta unidad vamos a ver qué es la documentación de software, por qué es importante y qué herramientas existen para generarla en diferentes lenguajes (Java, Kotlin, Python y PHP).   

A continuación te dejo enlaces de otros módulos donde se habla de documentación y que ya has visto:   

- [¿Deberías documentar?](https://revilofe.github.io/section1/u02/teoria/PROG-U2.5.1.-DeberiasDocumentar/)    
- [Documentar vs comentar](https://revilofe.github.io/section3/u04/teoria/EDES-U4.4.-Documentacion/)    
- [Cómo documentar el código](https://revilofe.github.io/section1/u02/teoria/PROG-U2.5.-Documentar/)   
 
### 1. ¿Qué es la documentación de software?

La **documentación de software** es todo aquello que explica y acompaña a un programa para que otras personas (o tú mismo en el futuro) puedan entenderlo y usarlo. 

La documentación responde a tres preguntas clave:  

1. **¿Qué hace el programa?** Se incluye la funcionalidad, los requisitos y el propósito.    
2. **¿Cómo está hecho y por qué así?** Aquí se explica la arquitectura, las decisiones de diseño y las tecnologías usadas.
3. **¿Cómo se usa, instala o mantiene?** Aquí van las instrucciones para usuarios, administradores o desarrolladores que vayan a trabajar con el código.

> Piensa que un buen programa sin documentación es como un coche sin manual: puede funcionar, pero nadie sabrá cómo arrancarlo, repararlo o aprovecharlo al máximo.

### 2. Tipos de documentación
En cuanto a tipos de documentación, hay dos grandes categorías:

- **Documentación interna (en el código):**     
  Son los **comentarios especiales** en el código que se escriben en el propio código fuente. Luego, con herramientas, se transforman en manuales automáticos.  
  Ejemplo: los comentarios con `/** ... */` en Java o Kotlin.     

- **Documentación externa (fuera del código):**   
  Manuales de usuario, guías de instalación, páginas web, wikis de proyecto…  
  Sirve para explicar **cómo usar** la aplicación, no solo cómo está hecha.

Ambas son necesarias: una ayuda al programador y la otra al usuario final, al administrador o al equipo de desarrollo y/o mantenimiento.

### 3. Herramientas 

A continuación, una selección de herramientas según los lenguajes que vais a usar (Java, Kotlin, Python y PHP):

#### 3.1. KDoc (Kotlin)
Usada para documentación interna en Kotlin.   

- Es la **forma oficial** de documentar en Kotlin.  
- Usa comentarios con `/** ... */` sobre funciones, clases o propiedades.   
- Permite añadir etiquetas como `@param`, `@return`, etc.   
- Se combina con **Dokka** para generar documentación en HTML.  

#### 3.2. Javadoc (Java)
Usada para documentación interna en Java.   


- Es el **estándar en Java** desde hace décadas.  
- Usa el mismo formato que KDoc, con etiquetas como `@param`, `@throws`.  
- Genera páginas HTML navegables con el comando `javadoc`.  
- Muy usado en bibliotecas y frameworks (ejemplo: la API de Java en [docs.oracle.com](https://docs.oracle.com)).  

#### 3.3. *okka (para Kotlin y JVM)   
Una herramienta moderna para generar documentación en Kotlin y otros lenguajes de la JVM. A partir de KDoc, crea webs de documentación completas.    

- Herramienta que convierte **comentarios KDoc** en una web de documentación.  
- Admite salida en **HTML, Markdown, Jekyll**…  
- Se integra con proyectos de **Gradle** fácilmente.  

#### 3.4. Doxygen (multilenguaje)   
Una herramienta muy potente y versátil que soporta la generación de documentación interna en muchos lenguajes (C, C++, Java, Python, PHP…).

- Compatible con C, C++, Java, Python y otros.  
- Muy flexible: genera documentación en **HTML, PDF, LaTeX**.  
- Ideal para proyectos grandes o cuando se mezclan varios lenguajes.  

#### 3.5. MkDocs (documentación externa)  
Una herramienta para generar documentación externa. Permite crear sitios web de documentación a partir de archivos Markdown.

- No documenta el código, sino que convierte **archivos Markdown** en una web profesional de documentación.  
- Muy usado para manuales, guías de usuario y documentación de proyectos.  
- Se despliega fácilmente en **GitHub Pages** o en servidores propios.  
- Ejemplo real: la documentación de Python ([docs.python.org](https://docs.python.org)) podría montarse en un formato similar.

#### 3.6. Markdown
Un formato de texto ligero muy usado para escribir documentación externa e interna.    

- Fácil de aprender y usar.
- Compatible con muchas plataformas (GitHub, GitLab, Bitbucket).
- Se usa en archivos README.md, wikis y blogs.
- Se puede convertir a HTML, PDF y otros formatos con herramientas como Pandoc.
- Ideal para documentación externa y notas rápidas.
- No es específico de ningún lenguaje, por lo que es muy versátil.


#### 3.7. Otras herramientas de documentación
Además de las mencionadas, existen otras herramientas populares para documentación en distintos lenguajes:

- **JSDoc:** JSDoc es una herramienta específica para la documentación de código JavaScript.
- **Docusaurus:** Docusaurus es una herramienta de documentación estática desarrollada por Facebook, ideal para crear sitios web de documentación modernos y atractivos.
- **Wiki GitHub:** GitHub ofrece una funcionalidad de wiki integrada en los repositorios, que permite crear y mantener documentación de proyectos de manera colaborativa.
- **PyDoc:** PyDoc es una herramienta de documentación para Python que genera documentación en formato HTML a partir de los docstrings en el código fuente.


### 4. Diferencias clave

- **KDoc + Dokka / Javadoc** → Documentan directamente **el código fuente**.  
- **Doxygen** → Vale para **muchos lenguajes** y proyectos grandes.  
- **MkDocs** → Sirve para hacer **manuales externos y sitios web** de documentación.  
- **Markdown** → Formato ligero para escribir documentación de forma rápida y sencilla.

Piensa que:    

- Si quieres explicar **cómo funciona una función** → usa KDoc + Dokka/Javadoc.  
- Si quieres explicar **cómo instalar o usar tu aplicación** → usa MkDocs + Markdown.


### 5. Ejemplo en Kotlin con KDoc

```kotlin  

/**
 * Calcula el área de un círculo.
 *
 * @param radio Radio del círculo en cm.
 * @return Área del círculo en cm².
 */
fun areaCirculo(radio: Double): Double {
    return Math.PI * radio * radio
}

```

Si ejecutamos Dokka, obtendremos una **página HTML** que explica esta función:

* Qué hace.
* Qué parámetros recibe.
* Qué devuelve.

Este mismo estilo se aplica en Java con Javadoc, y en Python con herramientas como **Sphinx** (no incluida aquí, pero muy usada en ese lenguaje).


### 6. Comparativa de herramientas de documentación
Por último, una tabla comparativa para ayudarte a elegir la herramienta adecuada según el contexto.

#### 6.1. ¿Por qué comparar herramientas?

Existen muchas herramientas de documentación, pero no todas sirven para lo mismo.  
Un programador debe saber **qué herramienta usar en cada contexto**:    

- No es igual documentar una **función en Kotlin**, que escribir una **guía de usuario en la web**.  
- Tampoco es lo mismo generar documentación para un **proyecto pequeño** que para un **sistema grande y complejo**.  

Por eso, aquí tienes una tabla comparativa para orientarte.


#### 6.2. Tabla comparativa

| Herramienta | Lenguajes soportados | Tipo de documentación | Formatos de salida | Ventajas | Inconvenientes |
|-------------|----------------------|-----------------------|--------------------|----------|----------------|
| **KDoc** | Kotlin | Interna (en el código) | HTML (con Dokka) | Sintaxis sencilla, integrada en Kotlin | Depende de Dokka para generar páginas |
| **Dokka** | Kotlin (y JVM) | Interna (código) → externa (sitio web) | HTML, Markdown, Jekyll | Genera webs modernas, soporta Markdown | Configuración inicial en Gradle |
| **Javadoc** | Java | Interna (en el código) | HTML | Estándar muy extendido, bien documentado | Limitada a Java (aunque Doxygen puede leerlo) |
| **Doxygen** | C, C++, Java, Python, más | Interna (código) | HTML, PDF, LaTeX, RTF | Multilenguaje, potente, configurable | Más complejo de aprender y configurar |
| **MkDocs** | Cualquiera (usa Markdown) | Externa (manuales, guías, wikis) | HTML (sitio web estático) | Fácil de usar, aspecto profesional, despliegue en GitHub Pages | No extrae nada del código (hay que escribir la doc manualmente) |
| **Markdown** | Cualquiera | Interna (notas rápidas) y externa (manuales) | HTML, PDF, DOCX, etc. | Muy fácil de aprender, ampliamente soportado | No es específico para documentación técnica |

#### 6.3. Conclusiones rápidas

Muchas herramientas, pero ¿cuál usar?

- **¿Programas en Java?** Usa **Javadoc**.  
- **¿Programas en Kotlin?** Usa **KDoc + Dokka**.  
- **¿Tu proyecto mezcla lenguajes (C, Python, Java)?** Usa **Doxygen**.  
- **¿Quieres hacer un manual de usuario o guía de despliegue?** Usa **MkDocs**.  

La clave es combinar:     

- **Documentación técnica automática** (Javadoc, KDoc, Doxygen).  
- **Documentación externa y de usuario** (MkDocs).  


## Bibliografía y fuentes

- Articulo: [¿Cómo documentar proyectos de software? Guía sencilla](https://www.educaopen.com/digital-lab/blog/guias-digitales/como-documentar-proyectos-de-software)
- Kotlin Docs: [KDoc](https://kotlinlang.org/docs/kotlin-doc.html)  
- Oracle: [Javadoc Tool](https://www.oracle.com/technical-resources/articles/java/javadoc-tool.html)  
- Dokka: [Documentación oficial](https://kotlin.github.io/dokka/)  
- Doxygen: [Sitio oficial](https://www.doxygen.nl)  
- MkDocs: [Página oficial](https://www.mkdocs.org)
- Markdown Guide: [The Markdown Guide](https://www.markdownguide.org)
- Markdown Tutroial: [Tutorial de Markdown](https://tutorialmarkdown.com/)
- GitHub Docs: [About wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)
- JSDoc: [JSDoc Official Site](https://jsdoc.app/)
- Docusaurus: [Docusaurus Official Site](https://docusaurus.io/)
- PyDoc: [PyDoc Documentation](https://docs.python.org/3/library/pydoc.html)
- Jose Luis Gonzalez: [Repositorio del Módulo](https://github.com/joseluisgs/DespliegueAplicacionesWeb-01-2025-2026)
- JavaDoc: [Tutorial de JavaDoc](https://www.aprenderaprogramar.com/index.php?option=com_content&view=article&id=646:documentar-proyectos-java-con-javadoc-comentarios-simbolos-tags-deprecated-param-etc-cu00680b&catid=68&Itemid=188)
