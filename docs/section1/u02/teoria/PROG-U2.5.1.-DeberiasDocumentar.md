---
title: "UD 2 - 2.5.1 Deberías documentar tu código"
description: Deberías documentar tu código
summary: Deberías documentar tu código
authors:
  - Eduardo Fdez
date: 2023-10-30 
icon:
permalink: /prog/unidad2/2.5.1
categories:
  - PROG
tags:
  - Software
  - Documentar
---

## ¿Deberías documentar tu código?

Hay programadores que dice que los comentarios son un mal que se debería evitar al máximo. Aquí proponemos lo contrario:
usa los comentarios correctamente para crear código mantenible, basados en las ideas de ‘A Philosophy of Software
Design’

Cuando hablamos de los comentarios en el código, hay dos escuelas. La primera dice que debes usar los comentarios para *
*clarificar lo que quisiste expresar con tu código**, mientras que la segunda dice que deberías **evitarlos al máximo**
y que comentar tu código es un mal necesario que sólo denota tu falta de habilidad para no hacer código lo
suficientemente claro.

¿A cuál de los dos consejos deberías hacerle caso? En este artículo explicaremos por qué creemos que deberías ver los
comentarios como una **herramienta necesaria**, valiosa y muy útil, y cómo usarlos para no caer en el extremo que ha
llevado a algunas personas a tener una mala actitud hacia ellos.

### Un sistema sin documentación está incompleto

Como desarrollador estarás de acuerdo en que un sistema **no** tiene la *calidad suficiente* si no cuenta con
documentación, es decir, información acerca del sistema que comunique cosas como la razón de existir de ciertos módulos,
valores y funciones y cómo usarlos.

Si, además, tienes que modificar este sistema, será una pesadilla entender todo lo que los programadores anteriores
hicieron o *intentaron* hacer. Si tienes que *usar* algo sin documentación, es el mismo caso: **tienes estudiar el
código para saber como funciona.**

Así que hemos establecido que la documentación es completamente necesaria para crear programas útiles. Ahora bien,
¿dónde ponemos esa documentación? Muchos desarrolladores y equipos no tienen idea de dónde ponerla y crean documentos
que dejan después olvidados en una carpeta en la nube y que nadie encuentra después. Pero, ¿no sería más lógico mantener
la documentación lo **más cerca posible del código**? Eso es precisamente lo que los comentarios te permiten hacer.

Puedes usar los comentarios documentar:

* Decisiones de diseño
* Explicaciones sobre la existencia, funcionamiento o razón de ser de cierta parte del código
* Las interfaces y su ejemplo de uso
* Efectos de usar cierto código
* Partes inconclusas o que se pueden mejorar (TODO’s)

Tener esta información muy cerca del código sobre el que está proporcionando información ayudará a que sea fácil de
encontrar y además, si se establecen reglas como tratar los comentarios como ciudadanos de primer rango, se mantendrá
actualizado y útil.

También es buena idea tener un documento o sitio web especializado en documentación que te ayude a encontrar rápido lo
que buscas como Docusaurus o un sitio generado por Sophinx. Puedes utilizar esta misma documentación que escribiste
junto al código si usaste el estilo definido por el lenguaje de programación o por las herramientas de generación de
documentos.

#### Los comentarios te pueden ayudar en el futuro

Incluso aunque no los uses formalmente como documentación, los comentarios estarán ahí para darte información y
recordarte lo que hiciste, pero sobre todo **por qué** lo hiciste.

Recuerda que la mente humana busca la eficiencia máxima de recursos, por lo que es probable que elimine información que
no ocupe inmediatamente y que no recuerdas a menudo, como por qué esa variable tenía el valor 730 y no otro.

Tu yo futuro y tu equipo te agradecerán haber escrito esos comentarios que te informan sobre lo que estabas pensando en
el momento que escribiste ese código.

#### Los comentarios son una buena herramienta de diseño

John Ousterhout, en “A Philosophy of Software Design” recomienda **empezar** con los comentarios antes de programar (de
esto hablaremos más adelante). Pero, ¿por qué lo recomienda?

Escribir en un lenguaje humano cómo funciona algo antes de implementarlo realmente, te da la capacidad de ver si es
lógico y suficiente, además te permite ponerte en los zapatos del usuario para notar deficiencias sobre todo en **la
interfaz**. Los comentarios de interfaz es lo primero que deberías crear porque te servirán de guía para avanzar con tu
diseño y, sobre todo, que sea lógico y fácil de usar.

Una buena guía: si no eres capaz de crear un comentario concreto y corto sobre cómo funciona o por qué existe algo, **lo
más probable es que tengas que re-pensar tu diseño**.

#### El lenguaje de programación no es suficiente para expresar todo lo necesario

Todos los lenguajes de programación están pensados para ser un **subconjunto del lenguaje humano** que elimine las
ambigüedades, manteniendo el mayor poder expresivo posible. Esto nos lleva a sus limitantes: es imposible, o por lo
menos impráctico, intentar expresar todas las ideas con el código.

En la práctica, el tiempo y los recursos para lograr algo son limitados, por lo que a veces es más conveniente y fácil
para todos explicar lenguaje humano algo que intentar expresarlo con código, como los puristas afirman.

No te sientas mal si tienes que recurrir de vez en cuando a explicar la forma en que funciona algo, siempre y cuando no
sea la práctica común.

### ¿Cómo usar los comentarios para que sean valiosos?

No todos los comentarios son valiosos, hay algunos que pueden estorbar más de lo que ayudan, por ejemplo, los que no
aportan información a lo que es obvio en el código.

Hablemos de algunas formas de aprovecharlos lo mejor posible para que contribuyan positivamente a aumentar la calidad
del proyecto.

#### Escribe los comentarios primero

Una de las partes más importantes de los comentarios como documentación es que deben ser concretos, cercanos a la
realidad y que proporcionen la mayor cantidad de información útil posible.

Para lograr esto, se tienen que crear lo más cerca que puedas a la *creación del código*. Pero como todos sabemos que
después de escribir y probar (básicamente) el código vamos a sentir que ya está terminado, es buena práctica obligarte a
escribirlos antes, justo como propone TDD con las pruebas.

De esta manera te asegurarás que tu código esté documentado incluso antes de escribirlo y te servirán como una *
*herramienta de diseño** que te ayudará a pensar mejor en la usabilidad de tus módulos y piezas de software.

#### Crea comentarios acerca de la interfaz

La interfaz es el **medio de uso** que tus módulos o funciones presentan para que las demás partes de tu sistema lo
usen. Lo primero que deberías documentar y explicar es **esta interfaz**, para que más personas a parte de ti puedan
usar este pedazo de código.

Debes escribir comentarios claros sobre:

* **Cómo usar esa pieza de código**
* **Por qué existe esa parte del sistema**
* **Qué efectos tiene usarla**

Este tipo de comentarios son los que aportan mayor valor al sistema y si están lo suficientemente completos, con
ejemplos y explicaciones claras, son una documentación válida que está en un muy buen lugar: es fácil de encontrar y no
se va a perder enterrada entre otros documentes que después nadie va a consultar.

#### Evita los comentarios sobre la implementación

Los comentarios sobre la implementación son aquello que describen *qué* estas haciendo, como por ejemplo, sumar número,
abrir un archivo, etc. Estos comentarios normalmente son innecesarios, ya que lo que se está haciendo es obvio si el
código es lo suficientemente expresivo y *siempre deberíamos buscar que sea así*.

De hecho, estos son los comentarios que hacen que la gente odie a los comentarios en general, pues en vez de
proporcionar información extra son una carga que hay que mantener y pueden confundir si no son actualizados.

Si realmente sientes que tienes que explicar *qué* estás haciendo con cierta pieza de código, primero pregúntate si no
hay una manera de reescribirlo para que **sea obvio**. Si no existe o no es práctica esta solución, entonces escribe el
comentario de la manera más concisa posible, incluyendo la razón de la existencia de ese código.

Para hacer esto debes tomar muy en cuenta los recursos del proyecto: no te puedes tardar el triple del tiempo
implementando la pieza de código perfecta porque no quieres escribir un comentario que explique cómo funciona.

### Conclusión

Escribir comentarios es una de las grandes tareas que los programadores debemos dominar. Los lenguajes de programación y
los entornos de programación cada vez le dan más poder a esta parte de los programas y permiten incluso escribir pruebas
en ellos, generar documentación automática y listar tareas a partir de ellos.

Si pones el suficiente esmero en aprender a escribir buenos comentarios y mantenerlos, serán una gran herramienta de
diseño y documentación de tu software.

*Este artículo está basado en las ideas del “A Philosophy of Software Design de John Ousterhout”, en el que se le
dedican **4 capítulos** al buen uso de los comentarios*.

## Fuente

* [¿Deberías documentar tu código? - Héctor Patricio](https://blog.thedojo.mx/2020/12/30/deberias-comentar-tu-codigo.html)
