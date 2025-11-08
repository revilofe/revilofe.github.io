## ED-U3.1. UML


---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

* 1. Introducción a UML
* 2. ¿Qué es UML?
* 3. Importancia en el Ciclo de Vida del Software
* 4. ¿Por qué usar UML?
* 5. Características de UML
* 6. Ventajas y Desventajas
* 7. Diagramas UML
* 8. Historia de UML
* 9. Alternativas a UML
* 10. Principios de buen modelado
* 11. Herramientas de modelado
* 12. UML en Desarrollo Ágil
* 13. Conclusiones

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

## 7. Conclusiones


### 7.1. Puntos Clave

* UML es el estándar para modelado visual de software.
* Facilita la comunicación y reduce errores y costos.
* Es independiente de la tecnología y muy versátil.
* Se debe usar de forma pragmática: modelar para comunicar, no para documentar todo.
* El valor real está en el pensamiento y la comunicación que habilita.

Note: Para concluir, UML es mucho más que una simple notación. Es una herramienta de pensamiento y comunicación. Usado correctamente, lleva a mejores arquitecturas, código más mantenible y equipos más alineados. La clave es ser práctico y centrarse en el valor que aporta cada diagrama.

---

## ¡Gracias por vuestra atención!

### Preguntas

¿Alguna pregunta sobre UML o modelado de software?

Note: Abrimos espacio para preguntas. Preguntad cualquier duda sobre conceptos vistos: diagramas, ventajas, cuándo usar UML, etc. Estoy aquí para ayudaros a entender mejor esta poderosa herramienta.
