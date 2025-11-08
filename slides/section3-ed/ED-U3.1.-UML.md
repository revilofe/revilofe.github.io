## ED-U3.1. UML


---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

1. Introducción a UML
2. Importancia en el Ciclo de Vida
3. ¿Por qué usar UML?
4. Características de UML
5. Ventajas y Desventajas
6. Diagramas UML
## Índice I

8. Historia de UML
9. Alternativas a UML
10. Principios de Buen Modelado
11. Herramientas de Modelado UML
12. UML en el Desarrollo Ágil
13. Conclusiones
14. Recursos y Referencias

---

## 1. Introducción a UML


### 1.1. ¿Qué es UML?

* Lenguaje Unificado de Modelado (Unified Modeling Language).
* Estándar para describir, diseñar, visualizar y documentar sistemas software.
* Utiliza diagramas para representar diferentes aspectos de un sistema.
* "Una imagen vale más que mil palabras".

Note: UML es un lenguaje visual estandarizado para el modelado de software. Ayuda a todos los involucrados en un proyecto a entender el sistema de la misma manera, desde los analistas de negocio hasta los desarrolladores. Su principio fundamental es que una representación visual es mucho más clara y efectiva que una descripción textual larga.


### 1.2. ¿Qué es Modelar?

* Crear una representación abstracta y simplificada de la realidad.
* En software, es diseñar la estructura y comportamiento antes de codificar.
* Análogo a los planos de un arquitecto antes de construir un edificio.
* Los cambios en el modelo son más baratos que en el código.

Note: Modelar es como hacer un plano. Un arquitecto no empieza a poner ladrillos sin un diseño detallado. En software, es igual. Creamos modelos para pensar y validar el diseño antes de escribir código. Corregir un diagrama es rápido y barato; corregir código ya implementado es costoso y lento.


### 1.3. Propósito del Modelado

* Visualizar el diseño y compararlo con los requisitos.
* Verificación temprana del diseño antes de codificar.
* Comunicación clara entre los miembros del equipo.
* Sirve como guía para la implementación.
* Genera documentación duradera del sistema.

Note: El modelado tiene objetivos muy claros. Nos permite asegurarnos de que el diseño cumple con lo que el cliente necesita antes de empezar a programar. Un buen diagrama comunica ideas complejas de forma rápida y sin ambigüedades, sirve de mapa para los programadores y se convierte en una parte valiosa de la documentación del proyecto.

---

## 2. Importancia en el Ciclo de Vida


### 2.1. Relevancia del Modelado

* Esencial en proyectos de cualquier tamaño, crítico en los grandes.
* Sin un diseño claro, los proyectos complejos caen en el caos.
* Asegura consistencia entre diferentes equipos de desarrollo.
* Permite diseñar para escalabilidad, seguridad y correcta ejecución.

Note: En proyectos pequeños, a veces se puede improvisar el diseño. Pero en proyectos medianos o grandes, la falta de un modelo claro es una receta para el desastre. Diferentes equipos tomarán decisiones contradictorias, lo que llevará a un código inconsistente y difícil de mantener. El modelado nos obliga a pensar en la escalabilidad y la seguridad desde el principio.


### 2.2. Beneficios Concretos

* Cambios menos costosos en fase de diseño.
* Facilita la comunicación y reduce malentendidos.
* Permite la reutilización de componentes bien diseñados.
* Mejora la calidad general del software y reduce defectos.
* Reduce el tiempo y coste de mantenimiento futuro.

Note: El beneficio más grande es económico: es mucho más barato arreglar un problema en un diagrama que en una aplicación en producción. Además, un buen diseño fomenta la reutilización de código, mejora la calidad y hace que el mantenimiento futuro sea más sencillo y predecible.

---

## 3. ¿Por qué usar UML?


### 3.1. Abstracción y Flexibilidad

* Permite trabajar a un mayor nivel de abstracción.
* Ayuda a concentrarse en los conceptos importantes, ignorando detalles.
* Abstracción es enfocarse en lo que importa para resolver un problema.

Note: UML nos permite pensar en el "qué" sin perdernos en el "cómo". Por ejemplo, al diseñar una tienda online, podemos hablar de un "Cliente" y un "Producto" sin preocuparnos todavía por cómo se guardarán en la base de datos o qué tecnología usará el navegador. Esto simplifica la resolución de problemas complejos.


### 3.2. Independencia Tecnológica

* UML es independiente del lenguaje de programación, S.O. y hardware.
* Un mismo diseño UML puede implementarse en Java, Python, C#, etc.
* El conocimiento de UML es transferible y no queda obsoleto con la tecnología.
* El modelo de negocio perdura aunque la tecnología cambie.

Note: Esta es una de las características más potentes de UML. El diseño que creas no está atado a una tecnología específica. Si hoy usas Java y mañana la empresa decide migrar a Kotlin, el diagrama de clases que describe la lógica del negocio sigue siendo válido. Tu habilidad para modelar con UML es una inversión a largo plazo.

---

## 4. Características de UML


### 4.1. Sencillez

* Aunque existen 14 tipos de diagramas, la mayoría de proyectos usan 3 o 4.
* Es modular: usas solo los diagramas que necesitas.
* No es necesario ser un experto para empezar a usarlo de forma útil.

Note: La cantidad de diagramas en UML puede asustar al principio, pero la realidad es que no necesitas saberlos todos. La mayoría de las veces, con los diagramas de Clases, Casos de Uso y Secuencia tienes más que suficiente. Es un lenguaje que puedes aprender y usar de forma progresiva.


### 4.2. Versatilidad y Universalidad

* **Versatilidad**: Modela cualquier tipo de sistema (web, móvil, embebido...).
* **Universalidad**: Crea un lenguaje común para todos los roles del equipo.
* Arquitectos, analistas, testers y desarrolladores pueden entender el mismo diagrama.

Note: UML es como una navaja suiza: sirve para modelar casi cualquier tipo de sistema. Y lo más importante, crea un puente de comunicación. En una reunión, todos pueden mirar el mismo diagrama y entenderlo desde su propia perspectiva, lo que evita muchísimas confusiones.


### 4.3. Extensibilidad

* UML no es un sistema cerrado.
* Permite crear extensiones y especializaciones para dominios específicos.
* Se pueden definir perfiles para adaptar UML a necesidades concretas.

Note: Si estás trabajando en un campo muy especializado, como telecomunicaciones o finanzas, y necesitas conceptos que no están en UML estándar, puedes extenderlo. UML proporciona mecanismos para crear tus propios "dialectos" sin dejar de ser compatible con el estándar.

---

## 5. Ventajas y Desventajas


### 5.1. Ventajas

* Lenguaje estandarizado y reconocido mundialmente (OMG).
* Facilita la comunicación en equipos multidisciplinares.
* Independencia de plataforma y lenguaje de programación.
* Amplia variedad de diagramas para distintas perspectivas.
* Reduce costos al detectar errores en fase de diseño.

Note: Las ventajas son claras: es un estándar global, mejora la comunicación, protege tu diseño de la obsolescencia tecnológica y, sobre todo, ahorra dinero al encontrar problemas antes de que se conviertan en crisis.


### 5.2. Desventajas

* Es un lenguaje muy amplio, con una especificación de más de 600 páginas.
* Requiere una curva de aprendizaje inicial.
* Puede ser excesivo para proyectos muy pequeños ("overkill").
* Los diagramas pueden quedar desactualizados si no se mantienen.

Note: UML no es perfecto. Es grande y aprenderlo lleva tiempo. En un proyecto de fin de semana, probablemente no valga la pena. El mayor riesgo es que los diagramas se queden obsoletos. Por eso es crucial usarlo de forma pragmática y mantenerlos sincronizados con el código en los aspectos clave.

---

## 6. Diagramas UML


### 6.1. Clasificación de Diagramas

* UML tiene 14 tipos de diagramas, divididos en dos categorías.
* Ningún diagrama muestra toda la realidad del sistema.
* Cada diagrama responde a una pregunta diferente.

Note: No hay un único "diagrama verdadero". Al igual que un arquitecto necesita planos de planta, eléctricos y de fontanería para describir una casa, un analista de software necesita diferentes diagramas UML para describir un sistema desde múltiples perspectivas.


### 6.2. Diagramas Estructurales

* Responden: **¿De qué está hecho el sistema?**
* Muestran los elementos estáticos: clases, componentes, nodos.
* **Diagrama de Clases**: El más común. Muestra clases, atributos y relaciones.
* **Diagrama de Componentes**: Muestra la organización en módulos de alto nivel.
* **Diagrama de Despliegue**: Muestra el hardware donde se ejecuta el software.

Note: Los diagramas estructurales son como una radiografía del sistema. Nos enseñan las "piezas" que lo componen y cómo se conectan entre sí. El Diagrama de Clases es el más fundamental y el que más usarás. Los de Componentes y Despliegue son clave para entender la arquitectura.


### 6.3. Diagramas de Comportamiento

* Responden: **¿Qué hace el sistema y cómo?**
* Muestran la dinámica del sistema: flujos, interacciones, estados.
* **Diagrama de Casos de Uso**: Requisitos desde la vista del usuario.
* **Diagrama de Secuencia**: Interacción de objetos en el tiempo.
* **Diagrama de Actividades**: Flujo de trabajo de un proceso.
* **Diagrama de Máquina de Estados**: Ciclo de vida de un objeto.

Note: Si los diagramas estructurales son la anatomía, los de comportamiento son la fisiología. Muestran el sistema en acción. El de Casos de Uso es vital para entender qué quiere el cliente. El de Secuencia es perfecto para desenredar flujos complejos. El de Actividades es ideal para modelar procesos de negocio.

---

### 7 . Diagramas UML en la Práctica

Antes de continuar veamos algunos ejemplos prácticos de diagramas UML comunes.

#### [Diagrmas en PlantUML](https://plantuml.com/es/)

Note: PlantUML es una herramienta fantástica para crear diagramas UML a partir de texto. Permite versionar los diagramas junto con el código y es muy fácil de integrar en documentación técnica. Aquí tenéis algunos ejemplos básicos de cómo se ven los diagramas en PlantUML.

---

## 8. Historia de UML


### 8.1. La Era de la Confusión

* Años 60-70: "Crisis del Software", sin acuerdo sobre cómo modelar.
* Múltiples métodos estructurados no compatibles entre sí.
* Problema: División entre datos y procedimientos.

Note: En los inicios de la informática, cada equipo inventaba su propia forma de diseñar software. Esto creaba una gran confusión, ya que los modelos no eran portables ni comprensibles para otros. El principal problema era que los datos y la lógica del programa se trataban como dos mundos separados.


### 8.2. Revolución Orientada a Objetos

* Años 80: La Programación Orientada a Objetos (POO) une datos y comportamiento.
* Surge un nuevo problema: cada experto crea su propia notación para modelar objetos.
* Booch, Rumbaugh (OMT), Jacobson (OOSE) son los más populares, pero incompatibles.

Note:
La POO fue una revolución al unificar datos y comportamiento en "objetos". Sin embargo, esto trasladó el problema: ahora existían múltiples formas de dibujar y modelar esos objetos. Tres de las más importantes eran las de Grady Booch, James Rumbaugh e Ivar Jacobson. Aunque eran potentes, eran incompatibles entre sí.


### 8.3. El Nacimiento de UML

* 1994: Booch, Rumbaugh y Jacobson ("los tres amigos") se unen en Rational Software.
* Objetivo: Crear un único lenguaje unificado.
* 1997: Se publica UML 1.0, combinando las mejores ideas de sus métodos.
* 1997: La OMG (Object Management Group) lo adopta como estándar.

Note: La industria se dio cuenta de que esta "guerra de métodos" no era sostenible. En un movimiento histórico, los tres principales visionarios decidieron colaborar para unificar sus propuestas. El resultado fue UML, el Lenguaje Unificado de Modelado, que fue rápidamente adoptado como un estándar por la industria a través de la OMG.

---

## 9. Alternativas a UML


### 9.1. ¿Existen otras opciones?

* UML es el estándar dominante, pero no es la única herramienta.
* En proyectos muy pequeños, puede ser excesivo.
* Para dominios muy específicos, pueden existir lenguajes mejor adaptados.

Note: Aunque UML es el rey, no siempre es la herramienta perfecta para cada situación. Es importante conocer algunas alternativas para poder elegir la mejor opción según el contexto del proyecto.


### 9.2. Alternativas Principales

* **ArchiMate**: Para modelado de arquitectura empresarial completa.
* **SysML**: Extensión de UML para ingeniería de sistemas (hardware + software).
* **Diagramas informales (Sketching)**: Para brainstorming y comunicación rápida.
* **C4 Model**: Enfoque jerárquico simplificado para arquitectura de software.

Note: ArchiMate es ideal si necesitas modelar toda la empresa, no solo el software. SysML es para sistemas complejos como en automoción o aeroespacial. Los bocetos en pizarra son geniales para ideas rápidas. Y el modelo C4 es una alternativa moderna y más simple para documentar arquitectura de software.

---

## 10. Principios de Buen Modelado


### 10.1. Claves para un Modelado Efectivo

* **No modeles todo**: Céntrate en los aspectos complejos o importantes.
* **La simplicidad es sofisticación**: Los mejores diagramas son los más simples.
* **Mantener sincronía con el código**: Usa herramientas o actualiza en cambios clave.
* **Acompaña con documentación**: Los diagramas no siempre son autoexplicativos.

Note: Saber UML no es suficiente; hay que saber usarlo bien. No intentes dibujarlo todo, solo lo que aporte valor. Un diagrama que no cabe en una página es una mala señal. Mantén los diagramas vivos y sincronizados con el código, y añade pequeñas notas que expliquen las decisiones de diseño importantes.

---

## 11. Herramientas de Modelado UML


### 11.1. Tipos de Herramientas

* **Comerciales**: Enterprise Architect, Visual Paradigm. Potentes pero de pago.
* **Código Abierto**: PlantUML, StarUML. Gratuitas y muy capaces.
* **Online / En la nube**: Lucidchart, Draw.io. Colaborativas y accesibles.
* **Integradas en IDEs**: Plugins en IntelliJ, Eclipse, Visual Studio.

Note: Hay una herramienta para cada necesidad y presupuesto. Las comerciales son muy potentes para grandes empresas. Las de código abierto como PlantUML (basada en texto) son fantásticas para desarrolladores. Las herramientas online son ideales para equipos remotos. Y los plugins de los IDEs son muy cómodos para generar diagramas rápidos desde el código.


### 11.2. Recomendaciones

* **Para aprender**: Draw.io o PlantUML son un buen punto de partida.
* **Proyectos pequeños**: StarUML o PlantUML.
* **Equipos medianos**: Visual Paradigm Community.
* **Grandes empresas**: Enterprise Architect o licencias profesionales.

Note: Mi recomendación personal: si eres programador, aprende PlantUML. Es texto, se versiona con Git y se integra en la documentación. Para diagramas rápidos y colaborativos, Draw.io es imbatible. Para un entorno más profesional, Visual Paradigm ofrece un buen equilibrio.

---

## 12. UML en el Desarrollo Ágil


### 12.1. ¿UML y Ágil son compatibles?

* **Creencia incorrecta**: "Ágil = sin documentación = sin UML".
* **Realidad**: Ágil busca "documentación útil y just-in-time".
* UML en ágil debe ser pragmático, colaborativo e incremental.
* El diagrama es una herramienta de comunicación, no un artefacto final.

Note: Existe un mito de que en las metodologías ágiles no se documenta, pero no es cierto. Lo que se evita es la documentación inútil. UML puede ser muy ágil si se usa para facilitar conversaciones y no como un requisito burocrático. Un diagrama en una pizarra que se borra después de la reunión es un uso perfectamente válido de UML en un entorno ágil.


### 12.2. ¿Cuándo usar UML en Ágil?

* **Sprint Planning**: Para aclarar requisitos con Casos de Uso.
* **Diseño técnico**: Diagramas de Clases o Secuencia para refinar una historia.
* **Análisis de problemas**: Para entender bugs complejos.
* **Documentar decisiones de arquitectura** importantes (ADRs).

Note: En un sprint, UML es útil en momentos concretos. Al planificar, para asegurar que todo el equipo entiende la tarea. Durante el desarrollo, para pensar en una solución técnica antes de codificar. Para investigar un bug difícil. O para registrar una decisión de arquitectura importante que afectará al futuro del proyecto.

---

## 13. Conclusiones


### 13.1. Puntos Clave

* UML es el estándar para modelado visual de software.
* Facilita la comunicación y reduce errores y costos.
* Es independiente de la tecnología y muy versátil.
* Se debe usar de forma pragmática: modelar para comunicar, no para documentar todo.
* El valor real está en el pensamiento y la comunicación que habilita.

Note: Para concluir, UML es mucho más que una simple notación. Es una herramienta de pensamiento y comunicación. Usado correctamente, lleva a mejores arquitecturas, código más mantenible y equipos más alineados. La clave es ser práctico y centrarse en el valor que aporta cada diagrama.

---

## 14. Recursos y Referencias


### 14.1. Libros y Enlaces

* **Libros**:
    * "UML Distilled" de Martin Fowler (guía práctica).
    * "Applying UML and Patterns" de Craig Larman.
* **Herramientas y tutoriales**:
    * [PlantUML](https://plantuml.com/) (diagramas desde texto).
    * [Draw.io](https://draw.io/) (editor online gratuito).
    * [DiagramasUML.com](https://diagramasuml.com/) (tutoriales en español).
* **Especificación oficial**: [OMG UML](https://www.uml.org/).

Note:
Si queréis profundizar, el libro "UML Distilled" de Martin Fowler es la mejor guía de referencia: corta, clara y al grano. Para practicar, os recomiendo empezar con PlantUML o Draw.io. Y para cualquier duda, la especificación oficial de la OMG es la fuente de la verdad, aunque es muy densa.

---

## ¡Gracias por vuestra atención!

### Preguntas

¿Alguna pregunta sobre UML o modelado de software?

Note: Abrimos espacio para preguntas. Preguntad cualquier duda sobre conceptos vistos: diagramas, ventajas, cuándo usar UML, etc. Estoy aquí para ayudaros a entender mejor esta poderosa herramienta.
