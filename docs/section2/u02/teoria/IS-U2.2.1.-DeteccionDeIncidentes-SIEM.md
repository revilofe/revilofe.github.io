# Las mejores prácticas para implementar una estrategia SIEM

Al comenzar a implementar un SIEM, es importante plantearnos, qué es lo que deseamos que el SIEM logre para nuestro negocio en cuanto a ciberseguridad.

[Ruben.Ramiro](https://ciberseguridad.blog/author/ruben-ramiro/)7 de marzo de 2021 — 9 minutos de lectura

![Las mejores prácticas para implementar una estrategia SIEM](https://ciberseguridad.blog/content/images/size/w1200/2021/03/Estrategia-Implantar-un-SIEM.jpg)


La gestión de eventos de seguridad mediante [SIEM](https://ciberseguridad.blog/por-que-las-herramientas-soar-revitalizaran-el-ecosistema-siem/)s nos permite obtener análisis en tiempo real sobre las amenazas y las alertas de seguridad en nuestro negocio. Controla el almacenamiento, la manipulación, el análisis y la generación de informes de diferentes datos de seguridad, nos permitirá correlacionar diferentes eventos y alertas, llevando así la seguridad de nuestra organización a otro nivel.

El SIEM juega un papel determinante en el [cumplimiento normativo](https://ciberseguridad.blog/balbix-la-plataforma-predictiva-de-riesgo-de-incumplimiento/) de nuestra entidad  y por ello, debe ser una de las piezas claves en nuestra estrategia corporativa . Una solución de gestión de eventos e información de seguridad bien implementada nos permitirá ir un paso por delante de los ciberataques al proporcionar una vista centralizada de los eventos e información relacionados con la [**ciberseguridad**](https://ciberseguridad.blog/).


Independientemente del fabricante que elijamos, metiendo en el mismo saco, todos los productos opensource, los SIEMs, se caracterizan por contar con una serie de componente bien diferenciados. Algunos aunarán ambos en un solo componente , pero en el fondo todos disponen de al menos estos :

El SIEM tiene varios [componentes clave](https://www.uhcl.edu/information-security/tips-best-practices/?ref=ciberseguridad.blog) o funciones importantes que deben estar presentes en una implementación exitosa de [SIEM](https://stackify.com/siem-for-developers/?ref=ciberseguridad.blog) :

1. ****Agregación de datos**:** Que incluye gestión de registros y eventos . El SIEM recopila datos y registros de una variedad de fuentes para garantizar que no se pierda ningún evento de seguridad importante. Lo que comúnmente llamamos el colector, recolector o similar ...
2. ****Correlación**:**Componente  que busca tendencias y atributos comunes que vinculan diferentes eventos para que se pueda derivar información significativa y útil. La parte de las tendencias, cada vez más de moda en la tecnología SIEM , y atributos , aquellos que nosotros definamos en nuestros casos de uso.
3. ****Notificación**:**  Implica que el análisis automático de eventos relacionados, crea alertas para notificar a los administradores de TI cualquier problema potencial. Esta, puede darse por diferentes medios , pero lo común, es la notificación vía email, pero en base a la criticidad, podríamos llegar a implementar incluso llamadas automáticas.
4. ****Paneles**:** Los SIEM se caracterizan por ser un punto centralizado de tratamiento de eventos de seguridad, por ello, suelen incluir herramientas que pueden procesar datos en bruto en algo que sea más fácil de entender, como cuadros, gráficos y barras.
5. ****Cumplimiento**:** Una de las características a las que más nos ayuda disponer de un SIEM, es al cumplimiento normativo. Involucra diferentes herramientas que recopilarían automáticamente datos relacionados con el cumplimiento, así cómo la creación de informes que demuestren el cumplimiento de las regulaciones por parte de la empresa.
6. ****Retención**:** Aborda cómo se almacenan los datos y eventos a largo plazo, así como qué hacer con los datos históricos. Puede ser un componente propio del SIEM o derivar la retención a almacenamiento externo, pero en cualquier caso, las políticas de retención , rotado y tratamiento, serán definidas en el propio sistema.
7. **Forense:** Característica directamente relacionada directamente con la retención,  que nos permite acceder a los eventos y registrar datos que residen en diferentes activos, de diferentes períodos de tiempo y recopilarlos todos juntos, generalmente mediante el uso de un conjunto específico de criterios.

Os dejo un antiguo, pero interesante video sobre las mejores prácticas SIEM para operaciones diarias de seguridad  de [NitroSecurity](https://en.wikipedia.org/wiki/NitroSecurity?ref=ciberseguridad.blog) ( Empresa adquirida por McAfee en 2011 y su actual SIEM ), donde se explora las habilidades SIEM necesarias y explica cómo es posible la detección de amenazas y la respuesta a incidentes:

Mejores prácticas para las operaciones de seguridad diarias

# Estrategia para implementar un SIEM

## Fase de descubrimiento y planificación

Al igual que con cualquier proceso empresarial y de TI, la implementación de sistemas SIEM comienza con una **planificación y revisión exhaustivas**.

Al comenzar a implementar un SIEM para nuestra organización, es importante revisar primero nuestra posición y plantearnos, qué es lo que deseamos que  el SIEM logre para nuestro negocio: simplemente establecer [el/los caso/s de negocios](http://searchsecurity.techtarget.com/essentialguide/How-to-define-SIEM-strategy-management-and-success-in-the-enterprise?ref=ciberseguridad.blog), en los que comenzaremos elaborando una lista de metas y objetivos que tendremos que clasificar según la importancia para nuestra organización, poniendo foco en comprender, qué tareas y procesos son fundamentales para respaldar la implementación, priorizando los mismos en consecuencia.

En este punto, es imprescindible revisar  las políticas de seguridad, en las que debemos tener muy claro, cuáles de estas políticas debemos priorizar:

* Qué políticas son importantes para nuestro negocio
* Qué políticas son importantes para el cumplimiento normativo
* Cuáles se consideran mejores prácticas.

Debemos tener una visión clara de los controles actuales usados para auditar estas políticas de seguridad, y cuales nos ayudarían a garantizar el cumplimiento. SANS.org describió hace  unos años, 20 controles críticos en [esta guía](https://www.sans.org/reading-room/whitepapers/analyst/implementing-20-critical-controls-security-information-event-management-siem-systems-34965?ref=ciberseguridad.blog), que actualmente siguen siendo totalmente válidos:

1. **Inventario de Autorizados y no autorizados en dispositivos** : El SIEM debe utilizarse como base de datos de inventario de información sobre autorizaciones en activos. Los SIEM pueden usar el conocimiento de la información de los activos (ubicación, regulaciones, criticidad de los datos, etc.) para detectar y priorizar amenazas.
2. **Inventario de Autorizados y no autorizados en aplicaciones **: Al igual que en el control anterior, el SIEM debe usarse como base de datos de inventario de autorizados en aplicaciones, para la correlación con la red y la actividad de las mismas.
3. **Configuraciones seguras** : Las vulnerabilidades conocidas siguen siendo una vía principal para exploits exitosos. Si una herramienta automatizada de escaneo de dispositivos descubre un sistema de red mal configurado durante un escaneo de Enumeración de configuración común (CCE), ese error de configuración debe informarse o reflejarse en el SIEM, poniendo un mayor foco en dicho activo. Esto, nos ayudará a solucionar incidentes y a mejorar la postura de seguridad general.
4. **Configuraciones seguras para dispositivos de red** : Al igual que con el control 3, cualquier error de configuración en los dispositivos de red también debe reflejarse en el SIEM .
5. **Defensa de fronteras** : Las violaciones de las reglas de red, también deben informarse a una fuente central (un SIEM) para su correlación con los datos de inventario  de autorizados anteriormente indicada, con el fin de controlar nuestros accesos.
6. **Análisis de registros de auditoría** : Es básicamente un control sobre los SIEM, que son un medio líder para recopilar y centralizar datos de registro críticos. Los SIEM son el motor de análisis central que puede analizar los eventos de registro a medida que ocurren.
7. **Seguridad del software de aplicación** : Al igual que los resultados del análisis de CCE, las vulnerabilidades que se descubren en las aplicaciones de software también se deben trasladar a los SIEM, con ello, podremos correlacionar la información con los datos de la red, capturados a través de registros, para determinar si las vulnerabilidades se están explotando en tiempo real.
8. **Uso controlado de privilegios administrativos** : Cuando no se cumplen los principios de este control , el SIEM puede correlacionar los registros de acceso para detectar la infracción y generar una alerta.
9. **Acceso controlado según la necesidad de saber** : El SIEM puede correlacionar la actividad del usuario con los derechos y  los roles del usuario para detectar violaciones de mínimo privilegio en aplicaciones.
10. **Evaluación y corrección continua de vulnerabilidades** : El SIEM puede correlacionar el contexto de la vulnerabilidad con la actividad real del sistema para determinar si se están explotando las vulnerabilidades.
11. **Seguimiento y control de cuentas** : La actividad anormal de la cuenta solo se puede detectar cuando se compara con una línea de base de buena actividad conocida. El SIEM debe registrar la línea de base para cumplir con este control; y, a medida que se registren instantáneas o líneas de base futuras, se pueden comparar con la línea de base aprobada en el SIEM.
12. **Defensa contra Malware** : El malware que se descubra debe registrarse de acuerdo con este control. Las herramientas anti-malware centralizadas deben informar sus hallazgos al SIEM, quien correlacionará con los datos del sistema y las vulnerabilidades para determinar qué sistemas presentan un mayor riesgo debido al malware descubierto en ese sistema.
13. **Limitación y control de puertos, protocolos y servicios de red** : Los SIEM pueden monitorear los datos de registro para detectar el tráfico a través de puertos, protocolos y servicios restringidos. Las organizaciones pueden usar estos controles para determinar qué puertos y servicios son útiles para las empresas, cuáles no, y qué tipos de tráfico y puertos limitar.
14. **Control de dispositivos inalámbricos** : Las configuraciones erróneas del dispositivo y las intrusiones inalámbricas deben informarse a una base de datos central para fines de manejo de incidentes. Un SIEM es un candidato perfecto para consolidar esta información y utilizarla para la correlación o detección de amenazas a la infraestructura inalámbrica.
15. **Data Loss Prevention ( DLP )** : Al igual que con el control 5, las violaciones de las reglas de pérdida de datos, también deben informarse a una fuente central, como un SIEM, que puede correlacionar los eventos de pérdida de datos con la información de inventario o activos, así como con otras actividades del sistema y del usuario para detectar violaciones complejas de datos sensibles.

La fase de descubrimiento generalmente implica la implementación del SIEM en un subconjunto pequeño pero representativo de la tecnología y la política existentes de la organización, lo que nos permite recopilar datos críticos que pueden informar cambios y mejoras antes de una implementación completa. *Un objetivo principal es identificar las debilidades y lagunas en la ejecución de los controles y la implementación de planes para remediarlos*. Idealmente, deberíamos poder cubrir cualquier brecha antes de que estos elementos y controles de seguridad se incorporen en su implementación de SIEM. De lo contrario, no agregarán valor a nuestros procesos de monitorización de ciberseguridad.

## Fase piloto

Comenzando con la fase de implementación, debe tener dos objetivos en mente:

1. La demostración de que un sistema SIEM genera un retorno de la inversión
2. Que debemos disponer de un modelo funcional y un runbook.

Durante la etapa de descubrimiento, debemos ejecutar el SIEM en un pequeño subconjunto de tecnologías que sean representativas de todos los dispositivos y políticas de nuestra organización. Cuando lleguemos a la etapa piloto, podremos aplicar las lecciones aprendidas de los datos recopilados durante el descubrimiento e implementar cualquier mejora que hayamos realizado en un subconjunto más grande de políticas y dispositivos.

En la fase piloto, todas las suposiciones que hemos creado durante la fase de descubrimiento debemos probarlas minuciosamente, mientras nos ocupamos de un número creciente de dispositivos cubiertos. Una vez logrados los resultados de de nuestras pruebas de una forma satisfactoria, debemos tener todos los datos y la información que necesitamos para pasar a la fase de implementación controlada.

## Fase de implementación

La implementación de SIEM no necesita realizarse en una fase rápida. Primero podemos desarrollar la capacidad de manera gradual y constante a medida que pasamos por la fase de implementación.

La fase de implementación es cuando desarrollamos un flujo de trabajo de implementación que nos permita desarrollar la capacidad para la implementación completa, además de servir como etapa de prueba en un entorno de producción real. Durante esta fase, todos los procesos, procedimientos y operaciones deben describirse claramente en el **[runbook](https://es.wikipedia.org/wiki/Runbook?ref=ciberseguridad.blog)**.

## Fase de mejora continua

La implementación exitosas de un SIEM, no es algo único y ligado a la propia implementación, si no que debe estar en continuo desarrollo. Los actores maliciosos, nunca dejan de desarrollar métodos de ataque más sofisticados, por lo que debemos seguir evolucionando para estar un paso por delante de nuestros posibles enemigos.

Después de la fase de desarrollo, y a medida que continuemos implementando nuestro sistema SIEM, obtendremos más datos sobre cómo funciona todo en producción. Debemos utilizar estos datos e información para ajustar nuestra implementación y desarrollar las políticas y los procesos de seguridad de nuestra organización. Esto significa que nuestras implementaciones de SIEM están en constante cambio, y este proceso nunca debería detenerse.

# Las mejores prácticas para la implementación de SIEM

La mejor forma de implementar un SIEM es gradualmente. Un enfoque paso a paso nos ayudará a aprender más sobre nuestros sistemas actuales e implementar nuestra estrategia pieza por pieza, lo que nos permitirá ajustarla a lo largo del camino.

De una forma sencilla, desgajaremos, cuáles son las mejores prácticas para implementar un SIEM:

1. **Tenga una visión clara de los casos de uso**: Antes de comenzar a revisar y evaluar las soluciones, debes conocer los casos de usos que implementarías, unidos y ligados a tu negocio y su estrategia de ciberseguridad
2. **Prepárate para lo peor** . Piense siempre en los peores escenarios posibles para que puedas elegir directamente herramientas que puedan manejarlos, o si tienes ya elegidas dichas herramientas, como tratarias los mismos. Un caso de uso, siempre debe ir acompañado del tratamiento del mismo.
3. **Utiliza** los datos de reputación** **: Datos que provengan, tanto del exterior, como del interior de la red. Esto, nos permitirá controlar la reputación de nuestra propia organización y priorizar las alertas y casos de uso en su tratamiento y despliegue.
4. **Asegúrate de que nuestras herramientas dispongan de la información más reciente sobre amenazas**: Siempres debemos estar actualizados, cuanto menor sea dicha periodicidad, mejor.
5. **I3**: Iterar - Iterar - Iterar , este I3, me lo acabo de inventar, pero si que creo que debemos pasar , al menos 3 veces, por una alerta o caso de uso, hasta afinarlo perfectamente y conseguir el resultado que nos gustaría.

![Implementar SORA - SIEM](https://ciberseguridad.blog/content/images/2021/03/Implementar-SORA---SIEM.png)

Para llegar al summun de la monitorización ( [**SOAR**](https://ciberseguridad.blog/por-que-las-herramientas-soar-revitalizaran-el-ecosistema-siem/) ) , que ya tratamos hace tiempo, tenemos que empezar con una lógica idéntica que los SIEM tradicionales, por ello, tener claro como implementar un SIEM en todas sus variedades , es una metodología atemporal que nos ayudará en muchísimas implementaciones. Podremos dividir en más o menos fases, según los gustos , pero todas ellas llevan a la alineación de nuestros SIEMs , con nuestra estrategia de ciberseguridad, de forma que intentemos ir un paso por delante de nuestros actores maliciosos. Este post, daría muchísimos más, para una charla de varias horas, por lo que cualquier cuestión, no dudéis en hacérnosla llegar en los comentarios.

## Referencia
- [Las Mejores prácticas para implemetar una estrategía SIEM](https://ciberseguridad.blog/las-mejores-practicas-para-implementar-una-estrategia-siem/)

---
# Por qué las herramientas SOAR revitalizarán el ecosistema SIEM

Las soluciones SIEM, se nos quedan cortas, adquirir soluciones SOAR (Security Orchestration Automation and Response) es más que necesario. ! EVOLUCIONA ¡

[Ruben.Ramiro](https://ciberseguridad.blog/author/ruben-ramiro/)18 de noviembre de 2018 — 6 minutos de lectura

![Por qué las herramientas SOAR revitalizarán el ecosistema SIEM](https://ciberseguridad.blog/content/images/size/w1200/2018/11/herramientas-SOAR.png)

Fue por el 2005, cuando el SIEM se popularizó por primera vez como una forma de ayudar a las organizaciones a monitorizar sus redes y sistemas TI de manera más efectiva, el panorama digital era marcadamente diferente. La adopción cloud fue mínima, las fuerzas de trabajo estaban menos distribuidas y se usaban muchos menos endpoints.

Cómo cambian los tiempos. La superficie de ataque se ha transformado en la última década y continúa evolucionando a gran velocidad. Al mismo tiempo, las amenazas se han vuelto cada vez más sofisticadas y difíciles de detectar.

Para evitar ser descartados como una solución heredada, **las tecnologías SIEM tienen que mejorar** su estrategia.

## La evolución del SIEM.

El panorama digital cambiante está creando una serie de nuevos desafíos para los desarrolladores de tecnologías SIEM. Si bien SIEM se basó en solo unas pocas fuentes de datos, como firewalls y sistemas de detección de intrusos (IDS / IPS), la '*próxima generación*' de sistemas SIEM debe evolucionar para procesar un mayor volumen y variedad de datos, así como mejorar su capacidad de correlación.

*Las **[amenazas avanzadas](https://ciberseguridad.blog/indicadores-de-deteccion-apt-advanced-persistent-threat/)** (APTs) ahora son [polimórficas](https://es.wikipedia.org/wiki/Polimorfismo_(virus_inform%C3%A1ticos)?ref=ciberseguridad.blog) en lugar de estáticas*, capaces de cambiar constantemente su comportamiento para evadir la detección. Como tal, los [sistemas SIEM](https://ciberseguridad.blog/soluciones-open-source-para-la-gestion-de-logs-en-ciberseguridad/) no solo deben procesar más datos, sino que también deben ser mucho mejores para reconocer nuevos patrones dentro de ellos.

Mejorar la interoperabilidad con las nuevas tecnologías de seguridad, como las herramientas EDR (detección y respuesta de puntos finales) y [**UEBA**](https://ciberseguridad.blog/ueba-user-and-entity-behavior-analytics-deteccion-por-comportamiento/) (User & Entity Behavior Analytics), así como las plataformas de inteligencia de amenazas, El SIEM ha sido un foco para muchos proveedores en los últimos años. Permitiendo que los equipos de seguridad maximicen los beneficios de una selección cada vez mayor de herramientas de seguridad, por ello, también las soluciones SIEM tienen que evolucionar para facilitar la administración de todas estas tecnologías.

A pesar de su capacidad para aumentar la visibilidad de las amenazas, las tecnologías complementarias tienen el potencial de aumentar la **fatiga de alertas** y el tiempo muerto cuando el contexto cambia entre aplicaciones. La mejora del flujo de trabajo, la reducción de la carga de la monitorización de seguridad y la aceleración de la [**respuesta ante incidentes**](https://www.welivesecurity.com/la-es/2015/05/18/que-es-como-trabaja-csirt-respuesta-incidentes/?ref=ciberseguridad.blog) (CSIRT) son áreas que se deben mejorar para que los equipos de seguridad se den cuenta de los beneficios de los sistemas SIEM más inteligentes. Esto es particularmente importante dado los muchos desafíos que a los que se enfrentan las organizaciones para atraer y retener el talento de seguridad que necesitan para ejecutar las operaciones: **el objetivo es trabajar de manera más inteligente**, no más difícil.

## Herramientas SOAR

**Security Orchestration, Automation and Response (SOAR)** es un área de seguridad en crecimiento que los proveedores de SIEM están aprovechando.

Está compuesto por tres mercados tecnológicos distintos:

1. Orquestación y automatización de la seguridad
2. Plataformas de respuesta a incidentes de seguridad (SIRP)
3. Plataformas de inteligencia de amenazas (TIP).

Su propósito general es ayudar a las organizaciones a mejorar la detección y respuesta de amenazas a través de la agregación y la correlación de datos más ricos y de calidad unida a la automatización de las tareas rutinarias de seguridad.

Mientras que las soluciones SIEM tradicionales dependían en gran medida de una pequeña cantidad de fuentes de inteligencia de amenazas, las herramientas SOAR estan impulsando a las organizaciones a recopilar mayores volúmenes de datos internos/externos y procesarlos de forma más rápida y precisa. Es una tendencia que está ayudando a las operaciones de seguridad a ser más inteligentes siendo impulsadas por Big Data, lo que permite a los equipos tomar decisiones más rápidas y mejor informadas. Una inteligencia más amplia también significa una identificación de amenazas más confiable y con menos falsos positivos.

Otra manera clave en la que las **herramientas SOAR** está influenciando los planes de trabajo de los productos SIEM es ayudando a estandarizar los procedimientos de respuesta y análisis de incidentes. El objetivo en esta parte es automatizar parcial o totalmente una serie de actividades para que el personal de seguridad tenga más tiempo para buscar amenazas en lugar de responder a ellas.

A través de la automatización de acciones de respuesta, como bloquear una dirección IP en un firewall o un sistema de detección de intrusos, suspender las cuentas de usuario o poner en cuarentena los puntos finales infectados de una red, las herramientas SOAR pueden ayudar a facilitar una respuesta a incidentes más rápida y, por lo tanto, reducir el daño potencial y las interrupciones que las violaciones pueden provocar.

Playbooks Demisto

## El SIEM del futuro

*[Gartner](https://www.gartner.com/en?ref=ciberseguridad.blog) predice que para fines de 2020, el 15% de las organizaciones con un equipo de seguridad de más de cinco personas aprovechará las soluciones SOAR*. Su enorme potencial para mejorar la eficiencia y eficacia de las operaciones de seguridad significa que es probable que desempeñe un papel crucial para ayudar a dar forma al desarrollo del futuro SIEM.

La clave para la adopción de herramientas SOAR por parte de los proveedores de soluciones  SIEM será demostrar que se puede confiar en la [inteligencia artificial](https://es.wikipedia.org/wiki/Inteligencia_artificial?ref=ciberseguridad.blog) y el [aprendizaje automático](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico?ref=ciberseguridad.blog) para hacer cambios en los sistemas. Si bien este es el caso, las personas / humanos tomadores de decisiones seguirán siendo vitales para la detección y respuesta de amenazas.

Aprovechar al máximo el SIEM, para ayudar a enfrentarnos a los crecientes desafíos de seguridad, no solo dependerá de algoritmos más inteligentes, sino de personal mejor capacitadas que puedan usar los sistemas con mayor eficacia y validar alertas.

La superficie de ataque, que ya se ha transformado drásticamente desde la introducción de SIEM, continuará cambiando a gran velocidad en los próximos años. Las organizaciones solo podrán responder a estos cambios con mejores herramientas y una fuerza laboral más capacitada y eficiente.

## La necesidad de disponer herramientas SOAR

Por ahora, los beneficios de los sistemas **Security Orchestration, Automation and Response** (**SOAR**) son obvios para casi todos los analistas CISO y de seguridad.

Los beneficios para los Centros de Operaciones de Seguridad (SOCs) incluyen:

* Automatización de tareas para ayudar a los SOCs con personal limitado  aumentando la productividad de manera exponencial.
* Automatizar la clasificación básica de seguridad, para que las alertas se manejen de manera integral y las alertas importantes nunca se pasen por alto debido a la  carga de trabajo del personal
* Liberar a los analistas de seguridad para trabajar en tareas no repetitivas, como la búsqueda proactiva de amenazas y la colaboración con unidades de negocios, una vez que las operaciones de rutina son automatizadas, lo que mejora la efectividad general del SOC
* Lograr la excelencia operacional al reemplazar los procesos ad hoc con las mejores prácticas documentadas, automatizadas y realizadas de manera consistente

Pero mientras los SOC reconocen los beneficios de los sistemas SOAR, también podemos enumerar una larga lista de obstáculos que pueden limitar la efectividad de una implementación SOAR o hacer que una implementación de herramientas SOAR parezca demasiado poco práctica. Y es que los que vivimos en el mundo de la tecnología, conocemos los problemas y dolores de cabeza que produce introduccir una nueva tecnología.

Aquí hay una rápida lista de obstáculos en el despliegue de herramientas SOAR:

* **Muchos sistemas SOAR son demasiado caros**: Las nuevas tecnologías potentes a menudo tienen precios exorbitantes cuándo se presentan. Los automóviles solían ser accesibles solo por los aficionados más ricos. Con el tiempo, se convirtieron en necesidades asequibles para todos los hogares. Muchos sistemas SOAR de hoy solo son asequibles para SOC con grandes presupuestos.
* **Los sistemas SOAR requieren programación, pero la mayoría de los equipos SOC carecen de desarrolladores**: Muchos sistemas SOAR requieren que los usuarios escriban Python para construir Playbooks e integrarlos con otras herramientas y aplicaciones de seguridad. La gran mayoría de los equipos de SOC carecen de las habilidades de programación de Python y el tiempo para asumir un nuevo trabajo de integración, por lo que el requisito de la programación se convierte en un factor decisivo.
* **Las llamadas integraciones listas para usar son demasiado limitadas:** Los SOAR deben integrarse con herramientas de seguridad para las que puedan recopilar alertas y otros datos de ellos y emitir comandos, orquestando las respuestas a las amenazas. Algunos proveedores SOAR ofrecen integraciones, pero los SOC pronto descubren que las integraciones no incluyen funciones para las tareas y características de las que dependen. Con demasiada frecuencia, los SOC se ven obligados a desarrollar integraciones o contratar a expertos externos para crear integraciones no proporcionadas por los proveedores.
* **Las API de las herramientas de seguridad son demasiado limitadas**: Para complicar aún más el desafío de integrar SOARs con herramientas de seguridad, está la limitación de muchas API de herramientas de seguridad. Estas herramientas pueden ofrecer APIs para unas pocas operaciones básicas, suficientes para aprobar una demostración, pero no lo suficiente como para admitir la automatización efectiva de sus operaciones. Hay datos en los que ciertos SOCs  solo han integrado un 30% de las funciones de sus herramientas de seguridad debido a la dispodición de las APIs. Sin APIs para aprovechar, la automatización de la seguridad, se termina confiando en comandos basados en el navegador. O bien los analistas continúan emitiendo estos comandos en los navegadores, o las soluciones de automatización de seguridad necesitan expandir sus características para admitir la automatización basada en el navegador. Hasta ahora, la mayoría de los sistemas SOAR siguen siendo débiles en esta área de automatización, y por ello, debemos conocer muy bien nuestro scope de integración.
* **Los SOCs creen que sus procesos son demasiado ad hoc o especializados para ser automatizados**: Escuchamos esta objeción de muchos analistas de seguridad. Están convencidos de que lo que hacen es demasiado único o complicado de documentar. Y es que si no se puede documentar, no se puede automatizar.
* **Los SOCs carecen del tiempo necesario para construir y ajustar las automatizaciones por sí solas:** La construcción de la automatización lleva tiempo. Se necesita atención sostenida y un poco de ensayo y error. Desafortunadamente, la mayoría de los SOCs están tan ocupados luchando contra sus colas de clasificación que no pueden disponer de las horas o los días para crear lo que les llevaría a ahorrarse semanas o meses a lo largo del año.

## Referencia

[Herramientas SOAR que revitalizaran el ecosistema SIEM](https://ciberseguridad.blog/por-que-las-herramientas-soar-revitalizaran-el-ecosistema-siem.html)
