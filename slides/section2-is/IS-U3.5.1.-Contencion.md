# IS-U3.5.1 - Contención de incidentes

Note: En esta presentación vamos a trabajar la **contención de incidentes** como el momento en el que el equipo pone el freno para limitar daños. La idea clave es que **contener** no es resolver el incidente, sino **ganar control**, reducir impacto y preparar una respuesta con criterio.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Situad este contenido dentro del **RA3** de la unidad. Aquí nos centramos en las **primeras medidas de contención**, es decir, en qué acciones conviene tomar cuando un incidente ya exige actuar para que no siga creciendo.

---

## Índice

Note: Primero veremos qué es la **contención** y qué objetivos persigue. Después estudiaremos la diferencia entre contención **táctica** y **estratégica**, el flujo de decisión, las medidas por capas y varios **mini playbooks** por escenario.


### Índice I

- 1. Qué es contener y para qué sirve
- 2. Objetivos de la contención
- 3. Corto plazo y largo plazo
- 4. Principios clave antes de actuar

Note: En esta primera parte quiero que os quedéis con una idea muy clara: contener no es improvisar. Hay que actuar con **rapidez**, pero también con **método**, pensando en el impacto, en la **evidencia** y en la continuidad del servicio.


### Índice II

- 5. Qué contengo primero y cómo
- 6. Medidas por capas
- 7. Playbooks por escenarios
- 8. Errores, checklist y cierre

Note: En la segunda parte bajaremos la teoría a decisiones concretas. Veremos cómo elegir una estrategia realista, qué capa atacar primero y qué errores suelen empeorar un incidente cuando el equipo actúa con demasiada prisa o sin coordinación.

---

## 3.5.1. Contención de incidentes: medidas y estrategias

Note: Abrimos el punto 3.5.1 de la unidad. La contención aparece cuando ya sabemos que no basta con observar y hay que actuar para **frenar el incidente**, limitar su **propagación** y reducir el **impacto** sobre sistemas, personas y negocio.


### Contexto y objetivo de la unidad

- Frenar el incidente y evitar que crezca
- Identificar sistemas y usuarios afectados
- Poner en cuarentena lo necesario
- Volver al servicio con seguridad

Note: El objetivo de esta parte no es apagar cosas sin pensar, sino pasar de la **detección** a una actuación ordenada. Primero entendemos qué está pasando, después delimitamos alcance y aplicamos medidas de **cuarentena** para que el negocio pueda recuperar el control.


### RA3 y criterio asociado

- RA3: investigar incidentes de ciberseguridad
- CE 3.e: iniciar primeras medidas de contención
- Enfoque: limitar daños sin perder evidencia
- Resultado: reducir impacto y ganar tiempo

Note: Este contenido se alinea con el **CE 3.e**, que pide iniciar medidas de **contención**. Fijaos en el matiz: no se trata solo de reaccionar, sino de hacerlo sin destruir **evidencias** y sin empeorar innecesariamente el problema.


### Definición operativa de contención

- Limita alcance y propagación
- Corta la capacidad de actuar del atacante
- Protege activos críticos y negocio
- Debe convivir con investigación y recuperación

Note: La definición importante es esta: la **contención** es el conjunto de medidas que limita el alcance del incidente y corta la capacidad del atacante de seguir actuando, pero siempre con un ojo puesto en la **investigación**, la **erradicación** y la **recuperación**.

---

## 1. Objetivos de la contención

Note: Antes de elegir herramientas o acciones, necesitamos tener claros los **objetivos**. Si no sabéis qué queréis conseguir con la contención, es muy fácil aplicar medidas espectaculares pero inútiles.


### Qué persigue una buena contención

- Detener el daño activo
- Reducir superficie de ataque
- Comprar tiempo para investigar
- Proteger activos críticos
- Preservar evidencia cuando haga falta

Note: Estos cinco objetivos resumen casi toda la lógica de la contención. Queremos parar el **daño activo**, reducir caminos para el atacante, ganar tiempo para **investigar**, proteger activos clave como **identidad** o **backups** y conservar la **evidencia** necesaria.


### Idea clave: contener no es arreglar

- La contención pone el freno
- La investigación explica qué ocurre
- La erradicación elimina la causa
- La recuperación devuelve el servicio

Note: Esta diapositiva separa fases que el alumnado suele mezclar. **Contener** es poner el freno. **Investigar** es entender. **Erradicar** es quitar la causa. **Recuperar** es volver a operar con seguridad. Si mezclamos estas fases, tomamos peores decisiones.

---

## 2. Contención a corto plazo y a largo plazo

Note: Una forma muy útil de ordenar la contención es separar lo **táctico** de lo **estratégico**. Una cosa es frenar el daño ahora mismo y otra sostener el control durante días o semanas.


### Dos horizontes de actuación

- Corto plazo: frenar impacto inmediato
- Largo plazo: evitar reentrada y recaídas
- No compiten entre sí
- Suelen aplicarse por capas

Note: La contención de **corto plazo** trabaja en minutos u horas para detener el incidente. La de **largo plazo** trabaja en días o semanas para evitar **persistencia**, reentrada y debilidades que permitan repetir el ataque.


### Ejemplos tácticos y estratégicos

- Táctica: aislar un host o bloquear un IoC
- Táctica: deshabilitar una cuenta comprometida
- Estratégica: segmentar red y endurecer MFA
- Estratégica: rotar secretos y mejorar hardening

Note: Fijaos en la diferencia práctica. Aislar un equipo o bloquear un dominio es **táctico** porque frena ya. Rediseñar segmentación, endurecer **MFA** o rotar secretos es **estratégico** porque sostiene el control después de la primera reacción.


### Tiempo y capas se combinan

- El tiempo responde a cuándo actúas
- Las capas responden a dónde actúas
- Puede haber contención táctica por capas
- Y contención estratégica por capas

Note: Este matiz es importante: organizar la contención por **tiempo** no sustituye a organizarla por **capas**. Lo normal es aplicar medidas tácticas en **red**, **identidad**, **endpoint** o **servicios**, y después reforzarlas con medidas estratégicas en esas mismas capas.

---

## 3. Principios clave antes de actuar

Note: Aquí están los principios que evitan que una contención improvisada empeore el incidente. Son decisiones sencillas de entender, pero difíciles de aplicar bien bajo presión.


### Cinco principios que no debéis olvidar

- Evidencia primero, cuando aplique
- Rapidez con cabeza
- Menor impacto posible
- Cortar acceso del atacante
- Comunicación y escalado

Note: Estos principios resumen la disciplina de la contención. Debemos actuar con **rapidez**, pero sin destruir **evidencia**, buscando el **menor impacto posible**, cortando el acceso del atacante y manteniendo una **comunicación** clara con negocio y dirección.


### Error clásico: apagar y listo

- Puede borrar memoria y conexiones activas
- Puede tumbar negocio sin necesidad
- Puede romper la investigación
- Debe justificarse y documentarse

Note: La frase "apago el servidor y listo" parece resolutiva, pero muchas veces es mala técnica. Puede eliminar **evidencia volátil**, causar un incidente de **disponibilidad** y dejar al equipo sin datos para entender cómo entró el atacante o si sigue habiendo persistencia.

---

## 4. Flujo de decisión: qué contengo y cómo

Note: La pregunta más habitual en un incidente es "¿qué hago primero?". La respuesta correcta no es una receta fija, sino un **flujo de decisión** que prioriza daño activo, evidencia crítica, identidad y validación de efecto.


### Primera decisión: ¿hay daño activo?

- Cifrado en curso
- Exfiltración confirmada
- Propagación a otros equipos
- Creación masiva de cuentas o tareas

Note: Lo primero es decidir si hay **daño activo**. Si el incidente sigue creciendo, el tiempo juega en vuestra contra. En esos casos, la prioridad es detener el impacto, incluso aunque después tengamos que volver a recoger más contexto.


### Evidencia mínima viable antes de contener

- Memoria, procesos y conexiones pueden perderse
- Solo se captura si no retrasa la respuesta
- La prioridad sigue siendo frenar el daño
- Lo persistente puede preservarse después

Note: Este punto exige criterio. Si una captura rápida de **memoria** o **conexiones** tarda minutos y aporta evidencia irrepetible, puede merecer la pena. Si retrasa demasiado mientras el incidente sigue avanzando, se impone la **contención inmediata**.


### Después de la primera contención

- Investigar alcance y vector
- Buscar otros sistemas afectados con IoC
- Decidir si hay compromiso de identidad
- Completar contención por capas

Note: La primera contención no cierra el trabajo. Después hay que investigar el **alcance**, buscar más sistemas afectados usando **IoC** y decidir si la **identidad** está comprometida, porque si no se corta esa vía el atacante puede volver.


### Validar efecto y monitorizar

- Comprobar que el daño se ha parado
- Confirmar que no hay rutas alternativas
- Ajustar medidas si aparecen nuevos IoC
- Documentar decisiones y responsables

Note: Contener también significa verificar. No basta con aplicar una medida; hay que comprobar que realmente ha frenado el **impacto**, que no quedan rutas alternativas y que todo queda **documentado** para seguir investigando y coordinar recuperación.

---

## 4.1. Indicadores, alcance y cuarentena

Note: En contención no basta con ver el primer síntoma. La idea potente es convertir ese síntoma en **indicadores de compromiso**, buscar esos indicadores en el entorno y así delimitar el **alcance real** del incidente.


### De síntoma a IoC

- Hashes, dominios, URLs o IPs
- Servicios, tareas o claves de persistencia
- Cambios en archivos o configuración
- Firmas y detecciones de malware

Note: Un **IoC** es una pista observable. Puede ser un **hash**, un **dominio**, un servicio nuevo o una tarea programada. Lo útil no es solo detectarlo en un equipo, sino usarlo para buscar más casos en todo el entorno.


### Delimitar población afectada

- Qué equipos están tocados
- Qué cuentas y servicios aparecen implicados
- Si solo aislas el paciente cero, te quedas corto
- El alcance guía erradicación y recuperación

Note: Delimitar la **población afectada** marca la diferencia entre contener un equipo y contener un incidente. Si solo tratamos el primer sistema detectado y no buscamos más, es muy probable que el atacante ya haya avanzado por otros activos.


### Cuarentena segura

- Aislar no siempre significa apagar
- Puede hacerse con EDR, VLAN o ACL
- Hay que valorar memoria volátil antes
- El objetivo es frenar sin perder control

Note: La **cuarentena** es una medida frecuente, pero debe aplicarse con cabeza. A veces basta con aislar por **EDR**, por **red** o con reglas de acceso. Apagar solo tiene sentido cuando no destruye evidencia importante o cuando el daño exige un corte inmediato.

---

## 4.2. Elegir estrategia según capacidad y objetivos

Note: La mejor estrategia no es la más brillante en abstracto, sino la que el equipo puede ejecutar con los **recursos**, el **tiempo** y las **capacidades** que realmente tiene.


### Preguntas para elegir enfoque

- Qué capacidades internas tenemos
- Qué apoyo externo podemos activar
- Si prima volver al servicio o inventariar alcance
- Qué riesgo tiene cada decisión

Note: Antes de decidir, hay que medir capacidades. No todas las organizaciones pueden buscar **IoC** a gran velocidad, tomar imágenes forenses o sostener monitorización avanzada. Por eso a veces hay que apoyarse en terceros o simplificar el enfoque.


### Dos enfoques habituales

- Volver al servicio rápido
- Inventario completo de afectados
- Ambos son válidos según el contexto
- El daño activo cambia la prioridad

Note: El enfoque de **volver al servicio** puede ser razonable si el impacto operativo es crítico y el incidente está controlado. El enfoque de **inventario completo** es más seguro cuando sospechamos movimiento lateral o persistencia y no queremos dejar sistemas sin contener.

---

## 4.3. Secuencia típica de contención

Note: Muchas respuestas reales siguen una secuencia parecida. No es una fórmula mágica, pero ayuda a ordenar la cabeza cuando hay presión y poco tiempo.


### Secuencia operativa común

- Identificar síntomas e IoC iniciales
- Poner en cuarentena sistemas sospechosos
- Tomar imágenes si procede
- Extraer más IoC de la investigación
- Buscar esos IoC en el resto del entorno

Note: Esta secuencia crea un ciclo útil. Empezamos con un **síntoma**, lo convertimos en **IoC**, aplicamos **cuarentena**, investigamos más y volvemos al entorno para descubrir otros equipos afectados. Así evitamos quedarnos solo con la primera alerta.

---

## 5. Catálogo de medidas por capas

Note: A partir de aquí agrupamos las medidas por **capas**. Esta organización es muy práctica porque os obliga a pensar dónde aplicar controles: **red**, **identidad**, **endpoint** y **servicios**.


### Vista global por capas

- Red: frenar propagación y C2
- Identidad: cortar reentrada y privilegios
- Endpoint: aislar y conservar para análisis
- Servicios: proteger aplicaciones y secretos

Note: Cada capa responde a un problema distinto. **Red** corta movimiento y C2. **Identidad** evita que el atacante vuelva. **Endpoint** aísla equipos sin perder capacidad de análisis. **Servicios** protege aplicaciones, claves y configuraciones críticas.


### 5.1. Red

- Táctica: cuarentena, ACL y bloqueo de IoC
- Táctica: limitar salida a Internet
- Estratégica: segmentación y deny by default
- Estratégica: monitorizar NetFlow y logs

Note: La capa de **red** suele ser la más rápida para frenar propagación y cortar **mando y control**. En lo táctico bloqueamos **IoC**, reducimos **egress** y aislamos segmentos. En lo estratégico rediseñamos segmentación y mejoramos detección de flujos sospechosos.


### 5.2. Identidad

- Táctica: deshabilitar cuentas y revocar sesiones
- Táctica: reset de contraseñas y rotación de secretos
- Estratégica: MFA y acceso condicional
- Estratégica: mínimo privilegio y PAM

Note: La **identidad** es la llave maestra del entorno. Si el atacante conserva cuentas, **tokens** o secretos, puede reentrar aunque hayamos aislado equipos. Por eso muchas contenciones fracasan cuando se centran solo en máquinas y olvidan la capa de identidad.


### 5.3. Endpoint

- Táctica: aislar con EDR o por red
- Táctica: bloquear hashes, firmas o ejecución
- Estratégica: allowlisting y control de scripts
- Estratégica: parcheo y hardening del sistema

Note: En **endpoint** lo habitual es aislar el equipo para que deje de comunicarse, pero conservándolo para análisis. Además podemos bloquear ejecución por **hash** o **firma** y, a medio plazo, endurecer políticas de **scripts**, **macros** y **parcheo**.


### 5.4. Servicios y aplicaciones

- Táctica: mantenimiento, WAF y rate limiting
- Táctica: rotar secretos de despliegue y base de datos
- Estratégica: parcheo y configuración segura
- Estratégica: pipeline endurecido y gestión de secretos

Note: En **servicios** muchas medidas son temporales para ganar tiempo. Podemos poner un servicio en **mantenimiento**, endurecer reglas de **WAF** o rotar secretos urgentes. Después llega la parte estratégica: corregir la **causa raíz** y reforzar el **pipeline** y la gestión de secretos.

---

## 6. Contención por escenarios: mini playbooks

Note: Cuando hay prisa, los **playbooks** ayudan a no improvisar. Son guiones de actuación que indican qué se hace, en qué orden y qué evidencias conviene recoger.


### Qué aportan los playbooks

- Orden en situaciones de presión
- Reparto claro de decisiones y roles
- Secuencia repetible y documentable
- Menos improvisación y menos ruido

Note: Un **playbook** no reemplaza el criterio técnico, pero sí aporta estructura. Reduce improvisación, ayuda a repartir **roles** y hace más probable que el equipo actúe con una secuencia coherente incluso cuando la presión es alta.


### 6.1. Ransomware

- Aislar equipos afectados
- Proteger backups y cortar credenciales
- Bloquear IoC conocidos
- Registrar acciones y preservar evidencia mínima

Note: En **ransomware**, la prioridad es detener el **cifrado**, proteger los **backups** y cortar las **credenciales** que permitan ampliar el impacto. Aquí el tiempo cuenta mucho, porque cada minuto puede suponer más sistemas y más datos comprometidos.


### 6.2. Credenciales comprometidas

- Deshabilitar cuentas sospechosas
- Revocar sesiones y tokens
- Reset forzado y MFA
- Revisar correo, reglas y accesos remotos

Note: En incidentes de **phishing** o **password spraying**, la contención real suele estar en la **identidad**. Deshabilitar cuentas, revocar **tokens**, resetear credenciales y revisar reglas de reenvío o accesos remotos corta la posibilidad de reentrada.


### 6.3. Web comprometida y C2

- Sacar el servicio de Internet si hace falta
- Copiar logs y artefactos web
- Rotar secretos y revisar persistencia
- Bloquear comunicaciones C2 y aislar hosts

Note: Si la aplicación web está comprometida o hay **webshell** y **C2**, toca combinar medidas sobre **servicio**, **secretos** y **red**. Sacar temporalmente la web de Internet puede ser necesario, pero debe hacerse coordinando impacto con negocio.


### 6.4. DoS o DDoS

- Caracterizar tráfico y activos objetivo
- Aplicar rate limit, reglas o blackhole
- Coordinar con ISP o CDN
- Preparar capacidad de absorción

Note: En **DoS** o **DDoS**, la contención gira alrededor de la **disponibilidad**. Hay que entender el flujo del ataque, ajustar reglas de perímetro, coordinar con **ISP** o **CDN** y, a medio plazo, diseñar mejor capacidad de absorción.


### 6.5. Pérdida de activo, exfiltración y uso indebido

- Revisar qué datos y accesos estaban expuestos
- Revocar sesiones, tokens y claves si procede
- Bloquear canales de salida y revisar staging
- Aumentar monitorización y revisar privilegios

Note: No todo incidente es malware. En pérdida de portátil, **robo de datos** o **uso indebido de activos**, la pregunta clave es qué **datos** y qué **accesos** estaban implicados. Desde ahí decidimos revocar accesos, cortar canales de salida y reforzar monitorización.

---

## 7. Matriz de decisiones de contención

Note: No existe una contención perfecta en todos los casos. Toda decisión tiene ventajas y riesgos, y el trabajo del analista es justificar por qué elige una u otra.


### Opciones habituales y su trade-off

- Contención agresiva: detiene rápido, pero puede tumbar negocio
- Contención selectiva: impacta menos, pero puede dejar persistencia
- Contención por identidad: corta reentrada, pero afecta a usuarios
- Contención por red: limita lateralidad, pero exige diseño

Note: Esta matriz resume los **trade-offs** reales. Una contención **agresiva** puede frenar el daño con rapidez, pero costar mucha disponibilidad. Una contención **selectiva** reduce impacto, pero corre el riesgo de dejar **persistencia** o rutas de escape.

---

## 8. Errores frecuentes en contención

Note: En esta sección recogemos errores muy repetidos en ejercicios y en incidentes reales. Conocerlos evita decisiones impulsivas que complican mucho la respuesta.


### Los fallos que más empeoran un incidente

- Formatear o reinstalar sin investigar
- Aislar solo el primer sistema detectado
- No cortar credenciales o tokens
- Bloquear IoC a ciegas
- No documentar nada

Note: Estos errores tienen un patrón común: intentan cerrar el problema demasiado pronto. Formatear destruye **evidencia**, aislar solo el primer equipo ignora el **alcance**, no cortar **credenciales** permite reentrada, bloquear a ciegas rompe servicios y no documentar deja al equipo sin memoria operativa.

---

## 9. Checklist de contención

Note: Cuando los primeros minutos son caóticos, un **checklist** ayuda a mantener orden y a no olvidar tareas críticas. Es una herramienta muy simple, pero muy potente.


### Primeros 30 a 60 minutos

- Identificar alcance inicial
- Valorar evidencia volátil
- Aislar con el menor impacto posible
- Cortar accesos del atacante
- Bloquear IoC conocidos
- Proteger backups y activos críticos
- Escalar, comunicar y documentar

Note: Este checklist resume la primera hora del incidente. Lo importante es mantener la secuencia: primero **alcance** y **evidencia**, luego **aislamiento**, después corte de **accesos**, bloqueo de **IoC**, protección de activos críticos y, en paralelo, **comunicación** y **documentación**.

---

## 10. Evidencia forense y expectativas de dirección

Note: La contención no es solo técnica. También hay que gestionar la **evidencia forense** y las **expectativas** de dirección, porque la presión por tener respuestas rápidas puede empujar al equipo a especular o a tomar decisiones pobres.


### Apoyo forense y comunicación con dirección

- La investigación necesita evidencias fiables
- A veces hace falta apoyo externo
- Dirección quiere hechos, progreso y próximos pasos
- Es mejor no especular antes de tiempo

Note: Durante un incidente, la dirección quiere respuestas rápidas, pero el equipo debe comunicar **hechos**, **progreso** y **siguientes pasos**, no conclusiones precipitadas. La **especulación** suele causar más daño que beneficio cuando luego hay que rectificar.

---

## 11. Actividades de aula recomendadas

Note: Cerramos con propuestas de trabajo práctico para que la contención no se quede en teoría. Lo importante es que el alumnado practique decisiones, no solo definiciones.


### Propuestas de práctica

- Caso guiado: aislar sin perder evidencia
- Diseñar segmentación mínima viable
- Redactar playbook de ransomware
- Simular una war room con decisiones y timeline

Note: Estas actividades obligan a pensar como equipo de respuesta. Debéis decidir qué capturar, cómo segmentar, qué pasos pondríais en un **playbook** y cómo documentaríais una reunión de crisis o **war room** con decisiones justificadas.

---

## Ideas clave para estudio

Note: Terminamos con las ideas que debéis poder recordar y explicar con claridad en un caso práctico o en una prueba.


### Resumen final

- Contener es frenar, no resolver
- La prioridad depende de daño activo y evidencia
- Identidad, red, endpoint y servicios se coordinan
- Los playbooks reducen improvisación
- Sin documentación, la respuesta se debilita

Note: Si os quedáis con una sola idea, que sea esta: una buena **contención** combina **rapidez**, **criterio**, **capas**, **evidencia** y **comunicación**. No gana quien hace más cosas, sino quien hace las correctas en el orden adecuado.


### Cierre

- Poner el freno con método
- Proteger negocio y evidencias
- Preparar erradicación y recuperación

Note: El objetivo final de esta unidad es que penséis como analistas que contienen con método. Eso significa proteger el **negocio**, conservar la **evidencia** útil y dejar preparado el terreno para una **erradicación** y una **recuperación** seguras.
