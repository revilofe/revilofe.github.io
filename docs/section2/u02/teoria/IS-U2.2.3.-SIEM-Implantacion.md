---
title: "UD 2 - 2.2.3 Implementación de SIEM"
description: Implementación de SIEM
summary: Implementación de SIEM
authors:
    - Eduardo Fdez
date: 2025-01-04
icon: "material/file-document-outline"
permalink: /is/unidad2/2.2.3
categories:
    - IS
tags:
    - SOC
    - SIEM
---

## 2.2.3 Las mejores prácticas para implementar una estrategia SIEM

Al comenzar a implementar un SIEM, es importante plantearnos, qué es lo que deseamos que el SIEM logre para nuestro negocio en cuanto a ciberseguridad.


![Las mejores prácticas para implementar una estrategia SIEM](https://ciberseguridad.blog/content/images/size/w1200/2021/03/Estrategia-Implantar-un-SIEM.jpg)


La gestión de eventos de seguridad mediante [SIEM](https://ciberseguridad.blog/por-que-las-herramientas-soar-revitalizaran-el-ecosistema-siem/)s nos permite obtener análisis en tiempo real sobre las amenazas y las alertas de seguridad en nuestro negocio. Controla el almacenamiento, la manipulación, el análisis y la generación de informes de diferentes datos de seguridad, nos permitirá correlacionar diferentes eventos y alertas, llevando así la seguridad de nuestra organización a otro nivel.

### 1. SIEM y componentes.

El SIEM juega un papel determinante en el [cumplimiento normativo](https://ciberseguridad.blog/balbix-la-plataforma-predictiva-de-riesgo-de-incumplimiento/) de nuestra entidad y por ello, debe ser una de las piezas claves en nuestra estrategia corporativa. Una solución de gestión de eventos e información de seguridad bien implementada nos permitirá ir un paso por delante de los ciberataques al proporcionar una vista centralizada de los eventos e información relacionados con la [**ciberseguridad**](https://ciberseguridad.blog/).

Independientemente del fabricante que elijamos, metiendo en el mismo saco, todos los productos opensource, los SIEMs, se caracterizan por contar con una serie de componente bien diferenciados. Algunos aunarán ambos en un solo componente, pero en el fondo todos disponen de al menos estos:

El SIEM tiene varios [componentes clave](https://www.uhcl.edu/information-security/tips-best-practices/?ref=ciberseguridad.blog) o funciones importantes que deben estar presentes en una implementación exitosa de [SIEM](https://stackify.com/siem-for-developers/?ref=ciberseguridad.blog) :

1. **Agregación de datos**: Que incluye gestión de registros y eventos. El SIEM recopila datos y registros de una variedad de fuentes para garantizar que no se pierda ningún evento de seguridad importante. Lo que comúnmente llamamos el colector, recolector o similar ...
2. **Correlación**: Componente que busca tendencias y atributos comunes que vinculan diferentes eventos para que se pueda derivar información significativa y útil. La parte de las tendencias, cada vez más de moda en la tecnología SIEM, y atributos, aquellos que nosotros definamos en nuestros casos de uso.
3. **Notificación**: Implica que el análisis automático de eventos relacionados, crea alertas para notificar a los administradores de TI cualquier problema potencial. Esta, puede darse por diferentes medios, pero lo común, es la notificación vía email, pero en base a la criticidad, podríamos llegar a implementar incluso llamadas automáticas.
4. **Paneles**: Los SIEM se caracterizan por ser un punto centralizado de tratamiento de eventos de seguridad, por ello, suelen incluir herramientas que pueden procesar datos en bruto en algo que sea más fácil de entender, como cuadros, gráficos y barras.
5. **Cumplimiento**: Una de las características a las que más nos ayuda disponer de un SIEM, es al cumplimiento normativo. Involucra diferentes herramientas que recopilarían automáticamente datos relacionados con el cumplimiento, así cómo la creación de informes que demuestren el cumplimiento de las regulaciones por parte de la empresa.
6. **Retención**: Aborda cómo se almacenan los datos y eventos a largo plazo, así como qué hacer con los datos históricos. Puede ser un componente propio del SIEM o derivar la retención a almacenamiento externo, pero en cualquier caso, las políticas de retención , rotado y tratamiento, serán definidas en el propio sistema.
7. **Forense**: Característica directamente relacionada directamente con la retención, que nos permite acceder a los eventos y registrar datos que residen en diferentes activos, de diferentes períodos de tiempo y recopilarlos todos juntos, generalmente mediante el uso de un conjunto específico de criterios.



### 2. Estrategia para implementar un SIEM

La implementación de un SIEM es un proceso complejo que requiere una planificación cuidadosa y una ejecución precisa. A continuación, se describen las fases clave de la implementación de un SIEM:

#### 2.1. Fase de descubrimiento y planificación

Al igual que con cualquier proceso empresarial y de TI, la implementación de sistemas SIEM comienza con una **planificación y revisión exhaustivas**.

Al comenzar a implementar un SIEM para nuestra organización, es importante revisar primero nuestra posición y plantearnos, qué es lo que deseamos que  el SIEM logre para nuestro negocio: simplemente establecer [el/los caso/s de negocios](http://searchsecurity.techtarget.com/essentialguide/How-to-define-SIEM-strategy-management-and-success-in-the-enterprise?ref=ciberseguridad.blog), en los que comenzaremos elaborando una lista de metas y objetivos que tendremos que clasificar según la importancia para nuestra organización, poniendo foco en comprender, qué tareas y procesos son fundamentales para respaldar la implementación, priorizando los mismos en consecuencia.

En este punto, es imprescindible revisar las políticas de seguridad, en las que debemos tener muy claro, cuáles de estas políticas debemos priorizar:

* Qué políticas son importantes para nuestro negocio
* Qué políticas son importantes para el cumplimiento normativo
* Cuáles se consideran mejores prácticas.

Debemos tener una visión clara de los controles actuales usados para auditar estas políticas de seguridad, y cuáles nos ayudarían a garantizar el cumplimiento. SANS.org describió hace unos años, 20 controles críticos en [esta guía](https://www.sans.org/reading-room/whitepapers/analyst/implementing-20-critical-controls-security-information-event-management-siem-systems-34965?ref=ciberseguridad.blog), que actualmente siguen siendo totalmente válidos:

1. **Inventario de Autorizados y no autorizados en dispositivos**: El SIEM debe utilizarse como base de datos de inventario de información sobre autorizaciones en activos. Los SIEM pueden usar el conocimiento de la información de los activos (ubicación, regulaciones, criticidad de los datos, etc.) para detectar y priorizar amenazas.
2. **Inventario de Autorizados y no autorizados en aplicaciones**: Al igual que en el control anterior, el SIEM debe usarse como base de datos de inventario de autorizados en aplicaciones, para la correlación con la red y la actividad de las mismas.
3. **Configuraciones seguras**: Las vulnerabilidades conocidas siguen siendo una vía principal para exploits exitosos. Si una herramienta automatizada de escaneo de dispositivos descubre un sistema de red mal configurado durante un escaneo de Enumeración de configuración común (CCE), ese error de configuración debe informarse o reflejarse en el SIEM, poniendo un mayor foco en dicho activo. Esto, nos ayudará a solucionar incidentes y a mejorar la postura de seguridad general.
4. **Configuraciones seguras para dispositivos de red**: Al igual que con el control 3, cualquier error de configuración en los dispositivos de red también debe reflejarse en el SIEM.
5. **Defensa de fronteras**: Las violaciones de las reglas de red, también deben informarse a una fuente central (un SIEM) para su correlación con los datos de inventario  de autorizados anteriormente indicada, con el fin de controlar nuestros accesos.
6. **Análisis de registros de auditoría**: Es básicamente un control sobre los SIEM, que son un medio líder para recopilar y centralizar datos de registro críticos. Los SIEM son el motor de análisis central que puede analizar los eventos de registro a medida que ocurren.
7. **Seguridad del software de aplicación**: Al igual que los resultados del análisis de CCE, las vulnerabilidades que se descubren en las aplicaciones de software también se deben trasladar a los SIEM, con ello, podremos correlacionar la información con los datos de la red, capturados a través de registros, para determinar si las vulnerabilidades se están explotando en tiempo real.
8. **Uso controlado de privilegios administrativos**: Cuando no se cumplen los principios de este control, el SIEM puede correlacionar los registros de acceso para detectar la infracción y generar una alerta.
9. **Acceso controlado según la necesidad de saber**: El SIEM puede correlacionar la actividad del usuario con los derechos y los roles del usuario para detectar violaciones de mínimo privilegio en aplicaciones.
10. **Evaluación y corrección continua de vulnerabilidades**: El SIEM puede correlacionar el contexto de la vulnerabilidad con la actividad real del sistema para determinar si se están explotando las vulnerabilidades.
11. **Seguimiento y control de cuentas**: La actividad anormal de la cuenta solo se puede detectar cuando se compara con una línea de base de buena actividad conocida. El SIEM debe registrar la línea de base para cumplir con este control; y, a medida que se registren instantáneas o líneas de base futuras, se pueden comparar con la línea de base aprobada en el SIEM.
12. **Defensa contra Malware**: El malware que se descubra debe registrarse de acuerdo con este control. Las herramientas anti-malware centralizadas deben informar sus hallazgos al SIEM, quien correlacionará con los datos del sistema y las vulnerabilidades para determinar qué sistemas presentan un mayor riesgo debido al malware descubierto en ese sistema.
13. **Limitación y control de puertos, protocolos y servicios de red**: Los SIEM pueden monitorear los datos de registro para detectar el tráfico a través de puertos, protocolos y servicios restringidos. Las organizaciones pueden usar estos controles para determinar qué puertos y servicios son útiles para las empresas, cuáles no, y qué tipos de tráfico y puertos limitar.
14. **Control de dispositivos inalámbricos**: Las configuraciones erróneas del dispositivo y las intrusiones inalámbricas deben informarse a una base de datos central para fines de manejo de incidentes. Un SIEM es un candidato perfecto para consolidar esta información y utilizarla para la correlación o detección de amenazas a la infraestructura inalámbrica.
15. **Data Loss Prevention (DLP)**: Al igual que con el control 5, las violaciones de las reglas de pérdida de datos, también deben informarse a una fuente central, como un SIEM, que puede correlacionar los eventos de pérdida de datos con la información de inventario o activos, así como con otras actividades del sistema y del usuario para detectar violaciones complejas de datos sensibles.

La fase de descubrimiento generalmente implica la implementación del SIEM en un subconjunto pequeño pero representativo de la tecnología y la política existentes de la organización, lo que nos permite recopilar datos críticos que pueden informar cambios y mejoras antes de una implementación completa. *Un objetivo principal es identificar las debilidades y lagunas en la ejecución de los controles y la implementación de planes para remediarlos*. Idealmente, deberíamos poder cubrir cualquier brecha antes de que estos elementos y controles de seguridad se incorporen en su implementación de SIEM. De lo contrario, no agregarán valor a nuestros procesos de monitorización de ciberseguridad.

#### 2.2. Fase piloto

Comenzando con la fase de implementación, debe tener dos objetivos en mente:

1. La demostración de que un sistema SIEM genera un retorno de la inversión
2. Que debemos disponer de un modelo funcional y un runbook.

Durante la etapa de descubrimiento, debemos ejecutar el SIEM en un pequeño subconjunto de tecnologías que sean representativas de todos los dispositivos y políticas de nuestra organización. Cuando lleguemos a la etapa piloto, podremos aplicar las lecciones aprendidas de los datos recopilados durante el descubrimiento e implementar cualquier mejora que hayamos realizado en un subconjunto más grande de políticas y dispositivos.

En la fase piloto, todas las suposiciones que hemos creado durante la fase de descubrimiento debemos probarlas minuciosamente, mientras nos ocupamos de un número creciente de dispositivos cubiertos. Una vez logrados los resultados de de nuestras pruebas de una forma satisfactoria, debemos tener todos los datos y la información que necesitamos para pasar a la fase de implementación controlada.

#### 2.3. Fase de implementación

La implementación de SIEM no necesita realizarse en una fase rápida. Primero podemos desarrollar la capacidad de manera gradual y constante a medida que pasamos por la fase de implementación.

La fase de implementación es cuando desarrollamos un flujo de trabajo de implementación que nos permita desarrollar la capacidad para la implementación completa, además de servir como etapa de prueba en un entorno de producción real. Durante esta fase, todos los procesos, procedimientos y operaciones deben describirse claramente en el **[runbook](https://es.wikipedia.org/wiki/Runbook?ref=ciberseguridad.blog)**.

#### 2.3. Fase de mejora continua

La implementación exitosas de un SIEM, no es algo único y ligado a la propia implementación, si no que debe estar en continuo desarrollo. Los actores maliciosos, nunca dejan de desarrollar métodos de ataque más sofisticados, por lo que debemos seguir evolucionando para estar un paso por delante de nuestros posibles enemigos.

Después de la fase de desarrollo, y a medida que continuemos implementando nuestro sistema SIEM, obtendremos más datos sobre cómo funciona todo en producción. Debemos utilizar estos datos e información para ajustar nuestra implementación y desarrollar las políticas y los procesos de seguridad de nuestra organización. Esto significa que nuestras implementaciones de SIEM están en constante cambio, y este proceso nunca debería detenerse.

### 3. Las mejores prácticas para la implementación de SIEM

La mejor forma de implementar un SIEM es gradualmente. Un enfoque paso a paso nos ayudará a aprender más sobre nuestros sistemas actuales e implementar nuestra estrategia pieza por pieza, lo que nos permitirá ajustarla a lo largo del camino.

De una forma sencilla, desgajaremos, cuáles son las mejores prácticas para implementar un SIEM:

1. **Tenga una visión clara de los casos de uso**: Antes de comenzar a revisar y evaluar las soluciones, debes conocer los casos de usos que implementarías, unidos y ligados a tu negocio y su estrategia de ciberseguridad
2. **Prepárate para lo peor**. Piense siempre en los peores escenarios posibles para que puedas elegir directamente herramientas que puedan manejarlos, o si tienes ya elegidas dichas herramientas, como tratarias los mismos. Un caso de uso, siempre debe ir acompañado del tratamiento del mismo.
3. **Utiliza** los datos de reputación: Datos que provengan, tanto del exterior, como del interior de la red. Esto, nos permitirá controlar la reputación de nuestra propia organización y priorizar las alertas y casos de uso en su tratamiento y despliegue.
4. **Asegúrate de que nuestras herramientas dispongan de la información más reciente sobre amenazas**: Siempre debemos estar actualizados, cuanto menor sea dicha periodicidad, mejor.
5. **I3**: Iterar - Iterar - Iterar , este I3, es propio, pero si que creo que debemos pasar, al menos 3 veces, por una alerta o caso de uso, hasta afinarlo perfectamente y conseguir el resultado que nos gustaría.

![Implementar SORA - SIEM](https://ciberseguridad.blog/content/images/2021/03/Implementar-SORA---SIEM.png)

Para llegar al summun de la monitorización ([**SOAR**](https://ciberseguridad.blog/por-que-las-herramientas-soar-revitalizaran-el-ecosistema-siem/)), que ya tratamos hace tiempo, tenemos que empezar con una lógica idéntica que los SIEM tradicionales, por ello, tener claro como implementar un SIEM en todas sus variedades, es una metodología atemporal que nos ayudará en muchísimas implementaciones. Podremos dividir en más o menos fases, según los gustos , pero todas ellas llevan a la alineación de nuestros SIEMs, con nuestra estrategia de ciberseguridad, de forma que intentemos ir un paso por delante de nuestros actores maliciosos. 

## Referencia
- [Las Mejores prácticas para implemetar una estrategía SIEM](https://ciberseguridad.blog/las-mejores-practicas-para-implementar-una-estrategia-siem/)
- [Ruben.Ramiro](https://ciberseguridad.blog/author/ruben-ramiro/)