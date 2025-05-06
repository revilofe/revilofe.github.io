---
title: "UD 3 - 3.1 Pruebas"
description: Pruebas
summary: Pruebas
authors:
  - Eduardo Fdez
date: 2023-01-15
icon:   
permalink: /edes/unidad3/3.1
categories:
  - EDES
tags:
  - EDES
  - Software
  - test
  - Pruebas
---
## 3.1. Pruebas

Se pretente estudiar algunas técnicas de verificación y pruebas de programas, se comenzará por los principios básicos, ciclo de vida y niveles y tipos de pruebas, posteriormente profundizaremos en algunas técnicas de prueba más usadas para terminar comentado algunas de las herramientas usadas para las pruebas.

### 1. Introducción

Las pruebas de software son **el proceso de evaluación de un sistema o aplicación para determinar si cumple con los requisitos especificados y funciona correctamente**. El objetivo principal de las pruebas de software es:

1. Garantizar la calidad del software.     
2. Minimizar el riesgo de errores en el producto final.     
   
Como **calidad del software** se entiende la capacidad de un producto para satisfacer las necesidades y expectativas de los usuarios, así como su capacidad para funcionar correctamente en diferentes entornos y condiciones. Esto incluye aspectos como la funcionalidad, la usabilidad, el rendimiento, la seguridad y la mantenibilidad del software.

#### 1.1. Importancia de las pruebas de software

Las pruebas de software es uno de los puntos más importantes del proceso de desarrollo de software, ya que ayudan a identificar problemas y errores en una etapa temprana, que pueden tener un impacto significativo en la funcionalidad del software. Esto permite a los desarrolladores corregir los errores antes de que el software se lance al mercado, lo que puede ahorrar tiempo, costos y reducir la frustración del usuario final.

Los errores que son identificados, pueden incluir:

- Errores que pueden afectar la calidad del software y la satisfacción del usuario final, por ejemplo, errores producidos por el no cumplimiento de los requisitos especificados, ya sea por malentendidos durante la fase de análisis o por cambios en los requisitos durante el desarrollo.    

- Otros errores:

   * Fallos de seguridad.             
   * Problemas de rendimiento.            
   * Problemas de usabilidad.      
   * Errores de lógica.   


#### 1.2. Beneficios de realizar pruebas de software

Los beneficios de realizar pruebas de software incluyen:

- Identificación temprana de errores y problemas en el software.          
- Mejora de la calidad del software y la satisfacción del usuario.          
- Reducción de costos y tiempos de corrección de errores.             
- Reducción del riesgo de errores en el software en producción.           
- Mejora de la confianza en el software y la marca de la empresa.          

Por todo esto, las pruebas de software son una parte mas que importante del proceso de desarrollo de software que ayudan a garantizar la calidad del producto final y a reducir el riesgo de errores en producción.

### 2. Verificación y prueba de programas

La **ISTQB** (International Software Testing Qualifications Board), una organización especializada en el campo de las pruebas y la industria del software, define la **verificación y pruebas de programas** como:

> Proceso que consiste en todas las actividades del ciclo de vida del software, tanto estáticas como dinámicas, concernientes con la planificación, preparación y evaluación de productos software y los trabajos relacionados, para determinar que éstos satisfacen los requisitos especificados, para demostrar que se ajustan al propósito y para detectar defectos.

#### 2.1. Principios básicos

Los principios básicos que rigen el proceso de verificación y prueba de los programas son los siguientes:

- Las pruebas **demuestran la presencia** de defectos no la ausencia de ellos.
- Las **pruebas exhaustivas no existen** (salvo en casos triviales).
- Las pruebas tempranas ayudan a **reducir costes**.
- Agrupación de defectos: Normalmente, la mayor parte de los defectos detectados se **concentran en un número reducido de módulos**.
- Paradoja del pesticida (de Bruce Beizer): La eficacia en la detección de errores de las mismas pruebas **disminuye con el paso del tiempo**.
- Las pruebas **dependen del contexto**: Así por ejemplo, la forma de probar un software crítico de una central nuclear es diferente a la página web de una frutería.
- La **falacia de la ausencia de errores**: La detección y corrección de defectos no servirá de nada si el sistema no es usable y no cumple con las expectativas de los usuarios.

#### 2.2. El ciclo de vida

El ciclo de vida en el proceso de pruebas consta de las siguientes actividades principales:

![](assets/cicloVidaPruebas.png)

1. **Planificación y control**: Se establecen los objetivos y el plan de pruebas y se controla el avance con respecto a lo planificado.
2. **Análisis y diseño**: los objetivos se transforman en casos de prueba tangibles
3. **Implementación y ejecución**: Se configuran, desarrollan y ejecutan las pruebas.
4. **Evaluación de los criterios de salida**: En este punto se evalúa los resultados de las pruebas respecto a los objetivos definidos y se decide sobre reproceso.
5. **Actividades de cierre de pruebas**: Aquí se realizan varias tareas finales, tales como analizar lecciones aprendidas, documentar la aceptación del sistema, etc.

#### 2.3. Niveles

Según el ISTQB, el proceso de prueba se puede ejecutar en los siguientes niveles:

* **Pruebas unitarias**: Realizadas por el equipo de desarrollo, tienen como objeto comprobar el funcionamiento de un único componente.
* **Pruebas de integración**: Realizadas por el equipo de desarrollo, su objetivo principal es comprobar la interacción de diferentes partes de un sistema, validando la comunicación entre sus interfaces.
* **Pruebas de sistema**: Realizadas por el equipo de pruebas, buscan probar el sistema como un todo y si los componentes de un sistema son compatibles e interactúan correctamente.
* **Pruebas de aceptación de usuario**: Realizadas por el usuario final, el objetivo de estas pruebas es validar la disposición de un sistema para su despliegue y uso.

Los niveles de las pruebas están estrechamente relacionados con las fases del ciclo de desarrollo del software, así en el modelo o método en V se establece dicha relación de forma explícita:

![](assets/ModeloV.png)

### 3. Técnicas de verificación y prueba de programas

Las técnicas pueden ser de dos tipos dependiendo de si el código de la aplicación es ejecutado o no.

#### 3.1. Técnicas dinámicas

Las pruebas dinámicas se clasifican, a su vez, en técnicas de pruebas de caja negra, en las que se desconoce el código fuente del componente y de caja blanca, en donde sí se conoce:

##### 3.1.1. Pruebas de caja negra

En las que los casos se diseñan **considerando las entradas y salidas sin conocer la estructura interna**. Las pruebas funcionales y no funcionales y de regresión suelen utilizar esta técnica.

* **Partición equivalente**: La idea es dividir los valores válidos y no válidos para entradas y salidas en un número reducido de particiones de forma que, el comportamiento del software sea el mismo para cualquier valor contenido en una partición particular. Así se reduce el número de casos que hay que probar. Por ejemplo, para las notas de un alumno tendríamos 3 clases de equivalencia (particionando los número enteros)


| Clases             | Valores inferiores a los válidos | Valores válidos | Valores superiores a los válidos |
| ------------------ | --------------------------------- |-----------------| --------------------------------- |
| V. representativos | -1                                | 0,10            | 11                                |

* **Análisis de valores límites**: Los casos de prueba que exploran las condiciones límites de un programa producen buenos resultados. Para el ejemplo anterior, los valores límites serían (-1,0, y 10,11).
* **Pruebas de transición de estado**: En este caso se considera el sistema como una máquina de estados, y se diseñan pruebas para cubrir secuencias típicas de estados, o cubrir todos los estados, transiciones o probar transiciones inválidas.   
* **Pruebas de caso de uso**: Consisten en ejecutar escenarios que describen el uso que los usuarios van a darle al software. Son de gran utilidad para diseñar las pruebas de aceptación con la participación del cliente.    
* **Pruebas según la experiencia**: Consisten en la generación de casos de prueba a partir de la intuición y la experiencia.    

##### 3.1.2. Pruebas de caja blanca

Permiten examinar la estructura interna de un sistema, **se centran en los detalles procedimentales**, como las pruebas de software estructurales:

* **Pruebas de camino básico**: Esta técnica consiste en utilizar el **grafo de flujo** del código —donde los **nodos** representan bloques de instrucciones y las **aristas** representan el flujo de ejecución entre esos bloques— junto con el cálculo de la **complejidad ciclomática**, que indica el número de caminos de ejecución independientes del programa. A partir de esta información, se diseñan casos de prueba con el objetivo de recorrer cada uno de esos caminos, asegurando que **todas las instrucciones** del programa se ejecuten **al menos una vez** y que los resultados obtenidos sean los **esperados**.    
* **Pruebas de coberturas de sentencias**: Este tipo de pruebas mide el porcentaje de sentencias del código que han sido ejecutadas durante la ejecución de un conjunto de pruebas (o test suite). Su objetivo principal es evaluar en qué medida las pruebas existentes ejercitan el código, proporcionando un indicador cuantitativo de la cobertura alcanzada, permitiendo identificar casos para los que diseñar pruebas que aumenten la cobertura.

#### 3.2. Técnicas estáticas

Al contrario que las pruebas dinámicas, que exigen la ejecución de software, las técnicas de pruebas estáticas se basan en el examen manual (revisiones) y en el análisis automatizado (análisis estático) del código sin ejecutar el código. Ejemplo de este tipo de pruebas son:

##### 3.2.1. Revisión de Código

Involucra la inspección manual del código fuente por parte de otros desarrolladores para identificar errores, problemas de estilo, violaciones de las mejores prácticas y posibles mejoras.    


* **Ejemplo**: Un equipo de desarrollo realiza una reunión de revisión de código donde cada miembro examina y comenta el código de otros.

##### 3.2.2. Análisis Estático Automatizado:

Utiliza herramientas de software para analizar automáticamente el código fuente o los artefactos de diseño para encontrar defectos.    

* **Ejemplo**: Herramientas como **SonarQube** o **Lint** que se ejecutan en el código fuente para identificar problemas como fugas de memoria, errores de concurrencia, etc.

##### 3.2.3. Inspecciones:

Son más formales que las revisiones de código e incluyen una preparación y revisión exhaustiva del código por parte de un equipo, a menudo con roles asignados (moderador, autor, revisor, etc.).     

* **Ejemplo**: Un equipo realiza una inspección planificada y estructurada del código con un moderador guiando la discusión.

##### 3.2.4. Caminatas de Código (Code Walkthroughs):

Proceso en el cual el autor del código guía a un grupo a través de su código para explicar su lógica y decisiones de diseño, buscando retroalimentación y detección de errores.    

* **Ejemplo**: Un desarrollador presenta su código línea por línea a colegas, explicando el razonamiento detrás de cada sección.

##### 3.2.5. Auditorías:

Revisión formal del código y otros elementos relacionados (documentación, estándares de codificación, etc.) para asegurarse de que cumplen con los estándares y regulaciones especificados.     

* **Ejemplo**: Un auditor externo revisa el código fuente y la documentación para asegurarse de que cumple con las normas de seguridad o calidad específicas de la industria.

##### 3.2.6. Análisis de Documentación y Requisitos:

Revisión de los requisitos y documentación del proyecto (especificaciones, diseños, manuales de usuario) para detectar inconsistencias, omisiones y errores.    

* **Ejemplo**: Revisar la documentación de los requisitos para asegurarse de que sean completos, claros, coherentes y testables.

Estas prácticas son complementarias a las pruebas dinámicas (que requieren la ejecución del código) y ayudan a mejorar la calidad del software desde las etapas iniciales de su desarrollo. Las pruebas estáticas son efectivas para mejorar la claridad y la mantenibilidad del código y para asegurar que el software cumpla con los estándares y regulaciones pertinentes.

### 4. Tipos de pruebas de software

#### 4.1. Pruebas unitarias

Las pruebas unitarias son un tipo de prueba que se enfoca en evaluar el **funcionamiento individual de cada unidad de código del software**, como funciones o métodos. Las pruebas unitarias se realizan en un ambiente aislado del resto del software para evaluar el comportamiento de una unidad de código específica y detectar errores en su funcionamiento.    

* **Ejemplo**: En una aplicación de gestión de tareas, se realiza una prueba unitaria en el módulo de creación de tareas para verificar que se crean correctamente con la información proporcionada y que se pueden guardar en la base de datos. Se verifica que la creación de tareas genera una respuesta de éxito y que la tarea se encuentra en la base de datos.

#### 4.2. Pruebas de integración

Las pruebas de integración son un tipo de prueba que se enfoca en evaluar cómo las **diferentes unidades de código se integran y trabajan juntas como un todo**. Este tipo de prueba se suele realizar después de las pruebas unitarias para detectar problemas en la interacción entre las diferentes unidades de código.   

* **Ejemplo**: 1En una aplicación de e-commerce, se realiza una prueba de integración para verificar que el módulo de pago interactúa correctamente con el módulo de compras. Se verifica que los datos de pago se envían correctamente a la pasarela de pago y que se actualiza el estado del pedido en la base de datos.

#### 4.3. Pruebas de sistema

Las pruebas de sistema son un tipo de prueba que se enfoca en evaluar el funcionamiento del **software como un sistema completo**. Este tipo de prueba se realiza después de las pruebas de integración para evaluar la funcionalidad del software en un ambiente más realista.   

* **Ejemplo**: En una aplicación de chat en tiempo real, se realiza una prueba de sistema para verificar que el servicio de chat funciona correctamente con varios usuarios conectados al mismo tiempo. Se verifica que los mensajes se envían y reciben correctamente, y que se mantienen las conexiones entre los usuarios.

#### 4.4. Pruebas de aceptación

Las pruebas de aceptación son un tipo de prueba que se enfoca en evaluar si el software **cumple con los requisitos y las expectativas del usuario final**. Estas pruebas suelen ser realizadas por el cliente o el usuario final para evaluar si el software cumple con los requisitos establecidos.   

* **Ejemplo**: En una aplicación de reserva de vuelos, se realiza una prueba de aceptación para verificar que se cumplen los requisitos del cliente. Se verifica que los usuarios pueden buscar vuelos disponibles, seleccionar asientos y reservar los vuelos seleccionados.

#### 4.5. Pruebas de regresión

Las pruebas de regresión son un tipo de prueba que se enfoca en evaluar que el sistema **sigue funcionando adecuadamente tras la realización de nuevos cambios**. Estas pruebas se realizan para asegurarnos que las modificaciones realizadas en el software no han introducido errores en áreas que antes funcionaban correctamente. Normalmente suelen ser automatizadas y se ejecutan cada vez que se genera una nueva versión para asegurarnos que las modificaciones se integran sin causar problemas.  

* **Ejemplo**: En una aplicación de edición de imágenes, se realiza una prueba de regresión después de una actualización de software para verificar que las funcionalidades que funcionaban antes de la actualización siguen funcionando correctamente después. Se verifica que la edición de imágenes, la aplicación de efectos y la exportación de imágenes siguen funcionando sin errores.

#### 4.6. Pruebas de carga

Las pruebas de carga son un tipo de prueba que se enfoca en evaluar el **comportamiento del software en condiciones de alta demanda**. Estas pruebas se realizan para evaluar la capacidad del software para manejar una gran cantidad de usuarios o procesos simultáneamente. Es decir, obtener el límite de carga que puede soportar el sistema. Las pruebas de carga son importantes para garantizar que el software pueda manejar la carga esperada en un entorno de producción. 

* **Ejemplo**: En una aplicación web, simular un gran número de usuarios que acceden a esta de forma simultánea, y monitorizar cómo el software responde a esta carga. Se podrían medir aspectos como el tiempo de respuesta de la aplicación, el número de errores producidos y la tasa de transacciones completadas con éxito.

#### 4.7. Pruebas de rendimiento

Las pruebas de rendimiento son un tipo de prueba que se enfoca en evaluar la **velocidad, la estabilidad y la escalabilidad del software en diferentes situaciones y cargas de trabajo**.  Es decir, obtener si se tendrá un rendimiento aceptable en condiciones de uso normal y en condiciones de carga máxima no extrema. Estas pruebas son importantes para garantizar que el software funcione correctamente y cumpla con los requisitos de rendimiento establecidos.

* **Ejemplo**: En una aplicación de streaming de video, se realiza una prueba de rendimiento para verificar que la aplicación puede manejar la carga de usuarios concurrentes y ofrecer una experiencia de visualización sin interrupciones. Se miden tiempos de carga, calidad de imagen y velocidad de reproducción en diferentes resoluciones.

#### 4.8. Pruebas de seguridad

Las pruebas de seguridad son un tipo de prueba que se enfoca en evaluar **la capacidad del software para proteger los datos y el sistema** contra posibles amenazas y ataques externos.    

* **Ejemplo**: En una aplicación de gestión de contraseñas, se realiza una prueba de seguridad para verificar que los datos de los usuarios están protegidos contra posibles amenazas externas. Se verifica la fortaleza de las contraseñas, la encriptación de los datos y la seguridad de los servidores de almacenamiento de contraseñas.

Como has podido observar, existen varios tipos de pruebas de software que se pueden realizar para evaluar diferentes aspectos de la funcionalidad y la calidad del software. Es importante elegir el tipo de prueba adecuado para cada situación y realizar pruebas continuas durante todo el proceso de desarrollo para garantizar la calidad del software.

### 5. Plan de pruebas

Un plan de pruebas es un documento que describe **cómo se realizarán las pruebas de software y cuáles serán los objetivos y las expectativas de estas pruebas**. El plan de pruebas es esencial para garantizar que las pruebas se realicen de manera efectiva y se puedan evaluar los resultados.   

La identificación de los objetivos de las pruebas nos permitirá acotar los puntos que forman el plan de pruebas. Por ejemplo, el objetivo puede ser identificar y corregir errores en el software, evaluar si el software cumple con los requisitos establecidos o evaluar la calidad y la funcionalidad del software, evaluar el rendimiento en horas de alta carga, etc.

A continuación, se describen los elementos más comunes de un plan de pruebas:

#### 5.1. Definición del alcance de las pruebas

En este punto, se deben **establecer los límites de las pruebas y definir cuáles son los componentes y funcionalidades del software que se van a probar**. Es importante que esta definición sea lo suficientemente amplia como para cubrir todas las áreas críticas del software, pero también lo suficientemente específica como para asegurarse de que se están probando todas las funcionalidades de manera exhaustiva.

* **Ejemplo**: Se establece que el alcance de las pruebas para una aplicación web de comercio electrónico incluye el registro de usuarios, el proceso de compra, la gestión de la cuenta de usuario, la gestión de productos y la integración con pasarelas de pago.

#### 5.2. Identificación de los recursos necesarios para las pruebas

Identificar los **recursos necesarios para realizar las pruebas** es otro de los aspectos importantes del plan de pruebas. Los recursos pueden incluir hardware, software, personal de pruebas y cualquier otro tipo de recurso que se necesite para ejecutar las pruebas de manera efectiva. Es importante identificar y asignar los recursos adecuados para garantizar que las pruebas se puedan realizar sin problemas.

* **Ejemplo**: Se identifica que se necesitan 2 equipos para ejecutar las pruebas, cada equipo con diferentes navegadores y sistemas operativos. También se necesitan datos de prueba para simular la interacción del usuario con la aplicación, y un servidor para alojar la aplicación y las herramientas de pruebas.

#### 5.3. Selección de herramientas de pruebas

La selección de las **herramientas de pruebas adecuadas** es clave para asegurar que las pruebas se realicen de manera efectiva. Las herramientas de pruebas pueden incluir software para la creación de casos de prueba, herramientas para la automatización de pruebas, herramientas para la gestión de defectos, entre otras. Es importante seleccionar las herramientas adecuadas para las necesidades específicas del proyecto.

* **Ejemplo**: Se seleccionan las herramientas Selenium y JMeter para realizar las pruebas funcionales y de rendimiento respectivamente, y MockK y Kotest para realizar pruebas unitarias, de integración y aceptación. Además, se decide utilizar Git como sistema de control de versiones para el código de la aplicación y los scripts de pruebas.

#### 5.4. Diseño de casos de prueba

Los casos de prueba describen los **pasos específicos que deben seguirse para evaluar el software** y verificar si cumple con los requisitos establecidos. El diseño de casos de prueba debe ser **exhaustivo para cubrir todas las áreas críticas** del software y asegurar que todas las funcionalidades se prueben adecuadamente.

* **Ejemplo**: Se elaboran casos de prueba para verificar la funcionalidad de la aplicación en diferentes escenarios, tales como pruebas de navegación, formularios, funcionalidad de compra, validaciones de datos y seguridad.

Por ejemplo, para verificar la funcionalidad de una aplicación de gestión de tareas:

- Casos de prueba de creación de tareas:       
   * Verificación de que se pueden crear tareas con éxito.    
   * Verificación de que se pueden asignar tareas a usuarios específicos.    
   * Verificación de que se pueden establecer fechas de vencimiento para las tareas.    
- Casos de prueba de edición de tareas:    
   * Verificación de que se pueden editar tareas existentes.    
   * Verificación de que se pueden actualizar los datos de la tarea, como la fecha de vencimiento y la asignación de usuarios.    

- Casos de prueba de eliminación de tareas:    
   * Verificación de que se pueden eliminar tareas con éxito.    
   * Verificación de que no se pueden eliminar tareas asignadas a otros usuarios.    

#### 5.5. Asignación de responsabilidades

La asignación de responsabilidades es vital para garantizar que las pruebas se realicen de manera efectiva. En este punto, se deben **definir los roles y responsabilidades de cada miembro del equipo de pruebas**, así como los roles y responsabilidades de cualquier otro miembro del equipo que esté involucrado en el proceso de pruebas. Esto asegura que cada persona tenga claro lo que se espera de él o ella durante el proceso de pruebas.

* **Ejemplo**: Se asignan responsabilidades a los miembros del equipo de pruebas, por ejemplo, un tester será responsable de la ejecución de las pruebas de integración, otro tester será responsable de las pruebas de sistema, y un tercero será responsable de las pruebas de aceptación.

#### 5.6. Cronograma de pruebas

El cronograma debe incluir la **duración de cada fase de pruebas y los plazos de entrega para cada etapa**. También debe tener en cuenta los plazos y recursos disponibles para el proyecto en su totalidad. El cronograma de pruebas ayuda a asegurar que las pruebas se realicen dentro de los plazos establecidos y que el proyecto se entregue en tiempo y forma.

* **Ejemplo**: Se establece un cronograma que indica cuándo se llevarán a cabo las diferentes pruebas y quién será responsable de su ejecución, y el proceso mediante el cual el equipo de desarrollo debe corregir las incidencias reportadas durante las pruebas, por ejemplo,  antes de que se inicie la siguiente fase de pruebas.

En ejemplo simple de cronograma:

- Semana 1:        
   * Revisión y aprobación de casos de prueba por el desarrollador.   
   * Configuración del entorno de prueba.    
   * Ejecución de pruebas unitarias.    

- Semana 2:   
   * Ejecución de pruebas de interfaz de usuario.    
   * Ejecución de pruebas de rendimiento.    

- Semana 3:    
   * Ejecución de pruebas de aceptación.    
   * Documentación de los resultados de las pruebas.    

- Semana 4:    
   * Revisión de resultados de pruebas y toma de decisiones sobre la aprobación de la entrega.   


Por tanto, un plan de pruebas es esencial para garantizar que las pruebas de software se realicen de manera efectiva y se puedan evaluar los resultados. Un plan de pruebas detallado debe incluir los objetivos de las pruebas, el alcance de las pruebas, el cronograma y los recursos, el plan de pruebas detallado, los roles y las responsabilidades y el proceso de seguimiento y documentación de errores.

### 6. Pruebas de integración

Las pruebas de integración son un tipo de prueba de software que se enfoca en probar cómo diferentes componentes de software interactúan entre sí cuando se integran. Estas pruebas se realizan después de haber completado las pruebas unitarias y antes de realizar las pruebas del sistema. El objetivo de las pruebas de integración es detectar problemas de integración entre los diferentes componentes de software para garantizar que el sistema completo funcione correctamente.

#### 6.1. Tipos de pruebas de integración

Existen diferentes tipos de pruebas de integración, que se pueden clasificar según el nivel de integración que se está probando:

- Pruebas de integración ascendente: se inician con las unidades de menor nivel (módulos o componentes) y se van integrando hacia arriba, hasta llegar al nivel de sistema completo.
- Pruebas de integración descendente: se inician con los módulos de más alto nivel y se van integrando hacia abajo, hasta llegar a las unidades de menor nivel.
- Pruebas de integración híbridas: combinan los dos enfoques anteriores, empezando por un grupo de módulos y luego continuando hacia arriba y hacia abajo simultáneamente.

Además, las pruebas de integración también se pueden clasificar según la estrategia que se utilice para realizarlas.

#### 6.2. Estrategias para realizar pruebas de integración

Existen diferentes estrategias que se pueden utilizar para realizar pruebas de integración. Algunas de las más comunes son:

- **Pruebas Big-Bang**: en esta estrategia, se integran todos los componentes a la vez y se realizan pruebas para verificar que funcionen correctamente. Esta estrategia es rápida y sencilla de realizar, pero puede ser difícil detectar los problemas de integración si hay muchos componentes.
- **Pruebas por módulos**: esta estrategia consiste en integrar los componentes de software en módulos lógicos y realizar pruebas en cada uno de ellos. Luego, se integran los módulos y se realizan pruebas en el sistema completo.
- **Pruebas de fachada**: esta estrategia consiste en crear fachadas (interfaces) para los componentes que aún no se han desarrollado y realizar pruebas con estas interfaces, para simular el comportamiento de los componentes reales que aún no están disponibles.
- **Pruebas de stub y driver**: esta estrategia consiste en utilizar stubs (programas que simulan la funcionalidad de los componentes faltantes) y drivers (programas que simulan la entrada y salida de los componentes faltantes) para realizar pruebas en los componentes que aún no están disponibles.

* **Ejemplo**: Un ejemplo en de prueba de integración ascendente en la que se sigue una estrategia por módulos. Supongamos que estamos desarrollando un sistema de compras en línea que consta de tres módulos: el módulo de autenticación de usuarios, el módulo de gestión de carritos de compras y el módulo de procesamiento de pagos. Cada uno de estos módulos ha sido desarrollado por un equipo diferente de desarrolladores.

Para realizar pruebas de integración ascendente, comenzamos con el módulo más bajo en la jerarquía y vamos subiendo gradualmente. En este caso, comenzaríamos con el módulo de autenticación de usuarios.

1. Se desarrollan y prueban los componentes individuales del módulo de autenticación de usuarios, como la validación de la dirección de correo electrónico y la contraseña del usuario.
2. Luego, se integran los componentes individuales del módulo y se prueban los flujos de trabajo completos, como el registro de nuevos usuarios y la autenticación de usuarios existentes.
3. Una vez que se ha probado el módulo de autenticación de usuarios por completo, se procede a integrar el módulo de gestión de carritos de compras.
4. Se siguen los mismos pasos que con el módulo de autenticación de usuarios: se prueban los componentes individuales del módulo, luego se integran y se prueban los flujos de trabajo completos.
5. Finalmente, se integra el módulo de procesamiento de pagos y se prueban los flujos de trabajo completos, desde la selección de productos hasta la finalización del pago.

De esta manera, se van integrando gradualmente los distintos módulos del sistema y se prueban los flujos de trabajo completos, asegurando que no hay conflictos o errores en la interacción entre los distintos componentes. Este proceso se denomina "ascendente" ya que se comienza con los módulos más bajos en la jerarquía y se va avanzando hacia arriba.

En resumen, las pruebas de integración son un tipo de prueba de software que se enfoca en probar la integración de los diferentes componentes del software. Para realizarlas, se pueden utilizar diferentes estrategias, como pruebas Big-Bang, por módulos, de fachada y de stub y driver. El objetivo es detectar problemas de integración para garantizar que el sistema completo funcione correctamente.

### 7. Pruebas de sistema

Las pruebas de sistema son una etapa importante del proceso de prueba de software en la que se evalúa el sistema completo para asegurarse de que cumple con los requisitos y especificaciones definidos. Estas pruebas se realizan después de las pruebas de integración y antes de las pruebas de aceptación.

#### 7.1. Tipos de pruebas de sistema

Los tipos de pruebas de sistema que se pueden realizar son los siguientes:

1. Pruebas de funcionalidad: se asegura que todas las funciones del sistema estén funcionando correctamente.
2. Pruebas de rendimiento: se verifica que el sistema cumpla con los requisitos de rendimiento definidos, como la velocidad de respuesta, el tiempo de carga, etc.
3. Pruebas de carga: se comprueba la capacidad del sistema para manejar grandes volúmenes de datos o usuarios simultáneos.
4. Pruebas de seguridad: se evalúa la seguridad del sistema y se verifica que cumple con los requisitos de seguridad definidos.
5. Pruebas de compatibilidad: se verifica la capacidad del sistema para trabajar con diferentes entornos de hardware, software y configuraciones de red.
6. Pruebas de usabilidad: se evalúa la facilidad de uso y la experiencia del usuario.

#### 7.2. Estrategias para realizar pruebas de sistema

Las estrategias comunes para realizar pruebas de sistema son:

1. Pruebas de casos de uso: se prueban los casos de uso definidos y se verifica que el sistema funcione según lo previsto en cada caso.
2. Pruebas de escenarios: se prueban los diferentes escenarios de uso del sistema, incluyendo los casos de uso complejos y poco comunes.
3. Pruebas de extremo a extremo: se prueban las funcionalidades del sistema desde el inicio hasta el final, incluyendo todas las interacciones entre los diferentes módulos y componentes del sistema.
4. Pruebas de seguridad: se realizan diferentes tipos de pruebas de seguridad, como pruebas de penetración, pruebas de vulnerabilidad, etc., para evaluar la seguridad del sistema.
5. Pruebas de compatibilidad: se realizan pruebas en diferentes entornos de hardware y software para verificar la compatibilidad del sistema.
6. Pruebas de estrés: se prueban las capacidades del sistema en situaciones de alta carga o bajo condiciones extremas para verificar su capacidad para manejar tales situaciones.

Por último recordar que las pruebas de sistema son críticas para garantizar que el sistema cumpla con los requisitos y especificaciones definidos antes de que sea entregado al cliente. Para ello, se deben definir diferentes tipos de pruebas y estrategias apropiadas para realizarlas de manera efectiva.

### 8. Pruebas de aceptación

Las pruebas de aceptación son un tipo de prueba de software que se realiza para **verificar si el sistema cumple con los requisitos y expectativas del cliente**. Estas pruebas se realizan al final del ciclo de vida del desarrollo de software, antes de que el sistema sea entregado al cliente o puesto en producción. El objetivo principal de las pruebas de aceptación es garantizar que el sistema esté listo para su uso y cumpla con los requisitos establecidos.

#### 8.1. Tipos de pruebas de aceptación
Existen diferentes tipos de pruebas de aceptación, que se pueden clasificar según el tipo de usuario que las realiza. Normalmente, las pruebas de aceptación son realizadas por el cliente o el usuario final, pero también pueden ser realizadas por el equipo de desarrollo o el equipo de pruebas. 

Se enfoca en que el sistema cumpla con los distintos aspectos que se han definido en los requisitos. Algunos de los tipos de pruebas de aceptación son:
1. Cumple con los requisitos funcionales: se verifica que el sistema cumpla con los requisitos funcionales establecidos en la especificación de requisitos, es decir el sistema debe funcionar como se espera.
2. Cumple con los requisitos no funcionales (usabilidad,  seguridad, compatibilidad, rendimiento,  escalabilidad, mantenimiento,  portabilidad, fiabilidad, disponibilidad, recuperación ante fallos, documentación)

#### 8.2. Estrategias para realizar pruebas de aceptación
Las estrategias para realizar pruebas estan orientadas a la realziación y cumplimiento del tipo de pruebas que hemos visto anteriormente. Algunas de las estrategias más comunes son:
1. Pruebas de aceptación funcional: se centran en verificar que el sistema cumpla con los requisitos funcionales establecidos. Se realizan por el cliente o el usuario final, y se basan en los casos de uso y escenarios de negocio definidos en la especificación de requisitos.
2. Pruebas de aceptación no funcional: se centran en verificar que el sistema cumpla con los requisitos no funcionales establecidos. Se realizan por el equipo de pruebas y se basan en los criterios de aceptación definidos en la especificación de requisitos no funcionales.


### 9. Conclusiones

Concluimos destacando la importancia de las pruebas de software en el ciclo de vida del desarrollo de software, como algo fundamental para garantizar la calidad y el correcto funcionamiento del sistema. Hemos explorado los diferentes tipos de pruebas, sus objetivos y estrategias, así como la importancia de un plan de pruebas bien definido.
Es vital la colaboración entre desarrolladores y testers para asegurar que el software cumpla con los requisitos y expectativas del cliente. Además, hemos visto cómo las pruebas de integración, sistema y aceptación son esenciales para garantizar que el software funcione correctamente en un entorno real y cumpla con los requisitos establecidos.
Por último y no menos importante destacamos la importancia de la mejora continua en el proceso de pruebas de software y la necesidad de adaptarse a los cambios en los requisitos y expectativas del cliente. La implementación de un enfoque ágil y flexible en las pruebas de software puede ayudar a garantizar que el software cumpla con los estándares de calidad y satisfacción del cliente.

