# U3.1 - Pruebas de Software

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las pruebas de software?

* Evaluación de un sistema o aplicación.
* Busca comprobar que se cumplen los requisitos.
* Asegura el funcionamiento correcto del software.
* Su objetivo es minimizar errores y asegurar calidad.
* La calidad incluye funcionalidad, rendimiento, seguridad.
* También engloba usabilidad y mantenibilidad.

Note: Introduce el concepto de pruebas de software como proceso esencial para validar si un sistema cumple con sus requisitos funcionales y no funcionales. La calidad no solo se refiere a la ausencia de errores, sino también a su rendimiento, seguridad, y facilidad de mantenimiento.


### Importancia de las pruebas

* Detectan errores en etapas tempranas.
* Reducen el coste de corrección de errores.
* Aumentan la satisfacción del usuario final.
* Evitan errores por malentendidos de requisitos.
* Identifican fallos de seguridad y rendimiento.
* Mejoran la calidad general del producto.

Note: Explica la importancia de realizar pruebas durante el desarrollo para minimizar riesgos. Subraya cómo ayudan a identificar y corregir errores antes del lanzamiento y su impacto en el coste y experiencia de usuario.


### Beneficios de realizar pruebas

* Mejora de la calidad del software.
* Aumenta la confianza del usuario en el producto.
* Reduce costos de mantenimiento post-lanzamiento.
* Evita errores en producción.
* Identifica fallos desde las fases iniciales.
* Contribuye a una marca más confiable.

Note: Resume las ventajas tangibles que aportan las pruebas al proceso de desarrollo. Se hace énfasis en el valor que agregan al producto y a la percepción de la marca.

---

## Verificación y prueba de programas


### Definición según ISTQB

* Incluye actividades del ciclo de vida del software.
* Comprende tareas estáticas y dinámicas.
* Evalúa productos para comprobar requisitos.
* Detecta defectos y asegura cumplimiento del propósito.
* Involucra planificación, preparación y evaluación.

Note: Se presenta la definición de verificación y prueba desde una perspectiva profesional, citando a la ISTQB como referencia en el área. Se explica que abarca desde la planificación hasta la evaluación final del software.


### Principios básicos de la prueba

* Las pruebas demuestran presencia, no ausencia de errores.
* No es viable probar todo (excepto en casos triviales).
* Probar desde etapas tempranas reduce costes.
* Defectos suelen concentrarse en pocos módulos.
* Las mismas pruebas pierden eficacia con el tiempo.
* Las pruebas varían según el contexto del sistema.
* Corregir errores no basta si el sistema no es útil.

Note: Explica los principios fundamentales del testing, como la imposibilidad de pruebas exhaustivas y la necesidad de adaptarlas según el tipo de software. Introduce la paradoja del pesticida y la importancia del contexto.


### Ciclo de vida de pruebas

* Planificación y control: objetivos y gestión de pruebas.
* Análisis y diseño: definición de casos de prueba.
* Implementación y ejecución: desarrollo y ejecución.
* Evaluación de resultados: comparación con criterios.
* Cierre de pruebas: lecciones aprendidas y documentación.

Note: Describe cada fase del ciclo de vida de pruebas, desde la planificación hasta el cierre. Destaca la importancia de documentar y aprender de cada iteración del proceso.

---

## Niveles de pruebas


### Niveles según ISTQB

* Pruebas unitarias: testean componentes individuales.
* Pruebas de integración: validan interacción entre módulos.
* Pruebas de sistema: evalúan el sistema completo.
* Pruebas de aceptación: realizadas por el cliente final.
* Cada nivel se asocia a una fase del desarrollo.
* El modelo en V muestra esta correspondencia.

Note: Se describen los cuatro niveles clave de pruebas según ISTQB, destacando quién las realiza y en qué momento. Se introduce el modelo en V para mostrar la correspondencia entre fases de desarrollo y pruebas.

---

## Técnicas de verificación y prueba


### Clasificación de técnicas

* Dinámicas: requieren la ejecución del software.
* Estáticas: no requieren ejecución del código.
* Las técnicas se seleccionan según el objetivo.
* Complementarias entre sí para mayor eficacia.

Note: Introduce la clasificación general entre técnicas dinámicas y estáticas, explicando la diferencia clave entre ambas y su complementariedad.


### Pruebas dinámicas: Caja negra

* No se conoce la estructura interna del código.
* Basadas en entradas/salidas del sistema.
* Tipos:
    
    * Partición equivalente.
    * Valores límites.
    * Transición de estado.
    * Casos de uso.
    * Basadas en experiencia.

Note: Describe las técnicas de caja negra, en las que se prueba funcionalidad sin conocimiento interno del sistema. Menciona los tipos más representativos y su enfoque basado en entradas y salidas.


### Pruebas dinámicas: Caja blanca

* Conocimiento de la lógica interna del código.
* Se estudia el flujo de ejecución y sentencias.
* Tipos:
    
    * Camino básico.
    * Cobertura de sentencias.
* Asegura ejecución de todas las rutas posibles.

Note: Se explica que en la caja blanca se analizan las estructuras internas del código, como ramas de decisión y bucles, para lograr cobertura completa del flujo.

---

## Técnicas estáticas


### Técnicas estáticas de prueba

* No requieren ejecutar el código.
* Se basan en revisión y análisis de código.
* Permiten detectar defectos tempranamente.
* Incluyen revisión de requisitos y documentación.

Note: Introduce el enfoque estático, que se centra en examinar el software sin ejecutarlo. Explica que es útil desde fases iniciales del desarrollo.


### Revisión de código y análisis estático

* Revisión de código: hecha por compañeros del equipo.
* Análisis estático: realizado por herramientas automáticas.
* Busca errores, malas prácticas y mejoras posibles.
* Ejemplos: SonarQube, Lint.

Note: Comenta las dos técnicas más comunes: la revisión por pares y el uso de herramientas automáticas. Muestra ejemplos conocidos de herramientas del sector.


### Otras técnicas estáticas

* Inspecciones formales con roles definidos.
* Caminatas de código dirigidas por el autor.
* Auditorías para verificar cumplimiento de normas.
* Análisis de requisitos y documentación.

Note: Explica otras técnicas estáticas como las inspecciones y auditorías. Destaca su utilidad en asegurar estándares y en la mejora de documentación y claridad del código.
Perfecto, continúo generando las siguientes secciones:

---

## Tipos de pruebas de software


### Pruebas unitarias

* Evalúan unidades individuales del código.
* Pruebas aisladas del resto del sistema.
* Realizadas por desarrolladores.
* Permiten detectar errores funcionales simples.
* Verifican salidas esperadas con entradas dadas.
* Aumentan la mantenibilidad del software.

Note: Describe las pruebas unitarias como las más cercanas al código fuente. Explica su utilidad en validar funciones o métodos de forma aislada y su rol en el mantenimiento del sistema.


### Pruebas de integración

* Verifican interacción entre distintos módulos.
* Detectan errores de comunicación entre interfaces.
* Se realizan tras las pruebas unitarias.
* Pueden usar stubs o drivers si faltan módulos.
* Evaluación de datos compartidos y lógica integrada.

Note: Se presenta la prueba de integración como paso siguiente a las unitarias. Se profundiza en cómo ayudan a garantizar la colaboración correcta entre partes del software.


### Pruebas de sistema

* Evalúan el sistema como un todo integrado.
* Simulan condiciones de uso reales.
* Se verifican funcionalidades globales.
* Se prueba estabilidad, rendimiento y usabilidad.
* Son la antesala a la prueba de aceptación.

Note: Estas pruebas simulan el uso real del sistema completo. Se centra en validar que el producto final cumple los requisitos funcionales y no funcionales en conjunto.


### Pruebas de aceptación

* Realizadas por el cliente o usuario final.
* Verifican si el software cumple lo esperado.
* Validan funcionalidad y requisitos definidos.
* Se basan en casos de uso reales del negocio.
* Deciden si el sistema puede pasar a producción.

Note: Resalta que estas pruebas son las más cercanas al cliente y validan que el software cumple con lo que se prometió. Son determinantes para la entrega.


### Pruebas de regresión

* Aseguran que cambios no generen nuevos errores.
* Se ejecutan tras modificaciones o correcciones.
* Se automatizan para ejecuciones repetidas.
* Comparan comportamientos antiguos y actuales.
* Detectan efectos secundarios no deseados.

Note: Se enfoca en los riesgos de modificar código ya existente. Se recomienda automatizar estas pruebas para detectar errores que pueden haber sido introducidos accidentalmente.


### Pruebas de carga y rendimiento

* Evalúan comportamiento bajo demanda elevada.
* Determinan el límite de usuarios concurrentes.
* Miden tiempos de respuesta y consumo de recursos.
* Aseguran estabilidad y velocidad del sistema.
* Identifican cuellos de botella.

Note: Estas pruebas son clave en aplicaciones de alto tráfico. Se analiza la resistencia del sistema ante muchas peticiones simultáneas y su impacto en rendimiento.


### Pruebas de seguridad

* Evalúan resistencia ante ataques o vulnerabilidades.
* Protegen datos y sistemas ante accesos no autorizados.
* Incluyen pruebas de autenticación y cifrado.
* Simulan ataques conocidos (XSS, SQLi...).
* Imprescindibles en software que maneja información sensible.

Note: Estas pruebas son vitales en entornos donde se manejan datos confidenciales. Se deben simular amenazas reales para validar la protección del software.

Perfecto, continúo con la sección del **Plan de pruebas** y las siguientes:

---

## Plan de pruebas


### ¿Qué es un plan de pruebas?

* Documento que organiza y define las pruebas.
* Establece objetivos, alcance y cronograma.
* Determina recursos, herramientas y responsabilidades.
* Asegura ejecución efectiva de pruebas.
* Permite evaluar resultados de forma estructurada.

Note: Se explica qué es un plan de pruebas y su importancia para guiar y controlar todo el proceso de testing. Es una herramienta clave para coordinar esfuerzos y tomar decisiones basadas en resultados.


### Definición del alcance

* Determina qué se va a probar y qué no.
* Incluye funcionalidades críticas del sistema.
* Define límites para centrar el esfuerzo de pruebas.
* Asegura cobertura de requisitos prioritarios.

Note: El alcance delimita el esfuerzo de pruebas. Se debe encontrar un equilibrio entre probar lo necesario sin desperdiciar recursos en lo irrelevante.


### Identificación de recursos

* Se especifican los equipos necesarios.
* Se detalla el personal implicado en las pruebas.
* Se definen herramientas y datos de prueba requeridos.
* Ayuda a prever y evitar cuellos de botella.

Note: Esta slide se centra en organizar los elementos logísticos necesarios para que el equipo de pruebas pueda realizar su trabajo sin obstáculos.


### Selección de herramientas

* Herramientas para pruebas funcionales (Selenium...).
* Herramientas para pruebas de rendimiento (JMeter...).
* Herramientas para pruebas unitarias (MockK, Kotest).
* Control de versiones para scripts de prueba (Git).

Note: Se explican las herramientas más comunes y su rol dentro del plan. La elección correcta puede facilitar mucho el trabajo y aumentar la cobertura de pruebas.


### Diseño de casos de prueba

* Casos que verifican diferentes funcionalidades.
* Se deben cubrir escenarios normales y extremos.
* Incluyen datos de entrada, pasos y resultados esperados.
* Organizados por funcionalidad o módulo.

Note: Aquí se explica cómo se crean los casos de prueba para validar diferentes partes del sistema. Se recomienda diseñarlos pensando en posibles errores o fallos.


### Asignación de responsabilidades

* Cada miembro tiene un rol claro.
* Se asignan pruebas a ejecutores específicos.
* Mejora el seguimiento y control del proceso.
* Fomenta la responsabilidad y la colaboración.

Note: El reparto de tareas es esencial para evitar solapamientos o vacíos. Se puede organizar por tipo de prueba, módulo o cronograma.


### Cronograma de pruebas

* Se define cuándo se ejecutará cada fase.
* Incluye fechas y responsables.
* Facilita seguimiento del progreso.
* Incluye revisión de incidencias y retroalimentación.

Note: Se destaca que el cronograma permite planificar y coordinar el trabajo de testing con otras fases del desarrollo. Asegura que el producto se entregue a tiempo.

---

## Pruebas de integración


### ¿Qué son las pruebas de integración?

* Verifican interacción entre distintos componentes.
* Se realizan tras las pruebas unitarias.
* Detectan fallos en comunicación entre módulos.
* Garantizan la cohesión del sistema.

Note: Estas pruebas comprueban que los módulos funcionen correctamente al integrarse. Son clave para validar que los componentes se conectan como se espera y que no hay errores en su interacción.


### Tipos de integración

* Ascendente: de componentes bajos a altos.
* Descendente: de componentes altos a bajos.
* Híbrida: combinación de ambos enfoques.
* Cada tipo tiene ventajas según el contexto.

Note: Se explican las tres estrategias principales para realizar pruebas de integración. Se debe elegir según la disponibilidad de módulos y los objetivos del sistema.


### Estrategias de integración

* Big-Bang: todo junto, simple pero difícil de depurar.
* Por módulos: integración parcial progresiva.
* Fachada: simula módulos no disponibles.
* Stubs y Drivers: simulan componentes faltantes.

Note: Se introducen diversas estrategias para aplicar las pruebas según las necesidades. Algunas son útiles en fases tempranas, otras en sistemas más maduros.

---

## Pruebas de sistema


### ¿Qué son las pruebas de sistema?

* Evalúan el sistema completo e integrado.
* Validan cumplimiento de requisitos globales.
* Se realizan antes de la aceptación.
* Se centran en el producto final desde la visión del usuario.

Note: Estas pruebas simulan la experiencia real del usuario con el producto terminado. Verifican que el sistema está listo para ser entregado al cliente o puesto en producción.


### Tipos de pruebas de sistema

* Funcionalidad: validan funciones del sistema.
* Rendimiento: evalúan tiempo de respuesta.
* Carga: verifican soporte ante muchos usuarios.
* Seguridad: evalúan resistencia a amenazas.
* Compatibilidad: en distintos entornos.
* Usabilidad: enfocadas en experiencia de usuario.

Note: Presenta los tipos de pruebas más comunes realizadas a nivel de sistema. Cada una enfoca un aspecto diferente del funcionamiento global.


### Estrategias de prueba de sistema

* Casos de uso: basados en escenarios del usuario.
* Escenarios completos: simulaciones realistas.
* Extremo a extremo: de principio a fin del flujo.
* Estrés: pruebas bajo condiciones extremas.
* Compatibilidad y seguridad.

Note: Detalla métodos usados para validar exhaustivamente que el sistema cumple con todos los requisitos bajo distintos enfoques.

---

## Pruebas de aceptación


### ¿Qué son las pruebas de aceptación?

* Validan si el software cumple requisitos del cliente.
* Última etapa antes de entregar el sistema.
* Realizadas por usuarios o clientes.
* Determinan si se aprueba el producto.

Note: Explica la función clave de las pruebas de aceptación: decidir si el producto cumple lo prometido. Se enfocan en lo que realmente importa al cliente.


### Tipos de pruebas de aceptación

* Funcionales: validan requisitos funcionales.
* No funcionales: rendimiento, usabilidad, etc.
* Simulan escenarios reales del negocio.
* Determinan si se puede usar el sistema en producción.

Note: Detalla los tipos de pruebas que se ejecutan durante la aceptación, con foco en las funciones esperadas y en aspectos como seguridad y rendimiento.


### Estrategias de aceptación

* Participación del cliente en la validación.
* Casos de uso centrados en el negocio.
* Pruebas manuales y automáticas combinadas.
* Definición clara de criterios de éxito.

Note: Se explican formas de estructurar las pruebas de aceptación para asegurar que se alineen con lo que el cliente espera, con criterios de éxito bien definidos.

---

## Conclusiones


### Resumen de lo aprendido

* Las pruebas aseguran calidad del software.
* Tipos y niveles permiten cubrir todo el proceso.
* Técnicas estáticas y dinámicas son complementarias.
* Un plan bien definido es esencial para el éxito.
* La colaboración entre equipos es clave.
* Las pruebas deben adaptarse a requisitos cambiantes.

Note: Cierra el tema con un repaso general. Se recuerda la importancia de realizar pruebas desde el inicio, de elegir el tipo adecuado y de mantener flexibilidad durante todo el ciclo de vida del software.