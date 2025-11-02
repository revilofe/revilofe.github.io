# U1.2.1 - Plan Director de Seguridad

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

1. Introducción: la necesidad de planificar la seguridad
2. Concepto y objetivos del PDS
3. Visión general del ciclo del PDS
4. Fase 1: Conocer la situación actual
5. Fase 2: Entender la estrategia
6. Fase 3: Definir proyectos e iniciativas
7. Fase 4: Clasificar y priorizar proyectos
8. Fase 5: Obtener la aprobación
9. Fase 6: Puesta en marcha y mejora continua
10. Caso práctico ilustrativo
11. Entregables esenciales

---

## 1. Introducción: la necesidad de planificar la seguridad


### 1.1. La información como activo crítico

* La digitalización ha convertido la información en un activo imprescindible.
* Facturación, clientes, proveedores, stock y propiedad intelectual dependen de sistemas digitales.
* **Proteger la información es proteger la empresa**.
* Cuando los sistemas fallan, el negocio se detiene.

Note: En la era digital, la información es el corazón de cualquier organización. Las empresas modernas no pueden operar sin sus sistemas de información. La pérdida de datos, su robo o su indisponibilidad puede llevar al cierre de un negocio. Es fundamental entender que invertir en seguridad no es un gasto, sino una inversión en la continuidad del negocio. La información contiene el valor intelectual, operativo y comercial de la empresa.


### 1.2. Situaciones de riesgo comunes

¿Qué ocurre cuando...?

* Un **ransomware** cifra los datos y paraliza la red sin plan de respuesta.
* Un **empleado descontento** filtra datos sensibles a la competencia.
* Se **pierde un disco duro** sin cifrar con informes financieros.
* Un **ataque DDoS** tumba la web de e-commerce en plena campaña.
* El **servidor de correo** falla un día por falta de mantenimiento.

Note: Estas situaciones no son hipotéticas, ocurren constantemente en empresas de todos los tamaños. El ransomware ha crecido exponentially en los últimos años. Las amenazas internas (empleados) causan el 34% de las brechas de seguridad. Los ataques de denegación de servicio pueden costar miles de euros por hora de inactividad. Cada una de estas situaciones refleja una falta de planificación y preparación. La pregunta no es "¿nos va a pasar?", sino "¿cuándo nos va a pasar y estaremos preparados?".


### 1.3. Preguntas inquietantes

Ante estos incidentes surgen cuestiones críticas:

* ¿Existen **copias de seguridad fiables** y probadas?
* ¿Se habían **identificado los riesgos** previamente?
* ¿Contamos con **personal preparado** para reaccionar?
* ¿Sabemos **a quién avisar** y **cómo recuperar** los datos?
* ¿Tenemos un **plan de continuidad** del negocio?

**Si las respuestas son dudosas, es momento de diseñar un Plan Director de Seguridad.**

Note: La mayoría de las organizaciones solo descubren sus carencias cuando ya es tarde. Las copias de seguridad sin probar son inútiles: muchas empresas han descubierto que sus backups estaban corruptos al intentar restaurarlos tras un incidente. La identificación proactiva de riesgos permite anticiparse y prepararse. El personal sin formación toma decisiones incorrectas bajo presión. Un Plan Director de Seguridad responde sistemáticamente a todas estas preguntas antes de que ocurra el desastre.

---

## 2. Concepto y objetivos del Plan Director de Seguridad


### 2.1. Definición del PDS

Un **Plan Director de Seguridad (PDS)** consiste en:

* Definir y priorizar **proyectos de seguridad de la información**.
* Objetivo: **reducir los riesgos** a niveles aceptables.
* Hoja de ruta que organiza las actuaciones de ciberseguridad.
* Proteger la **continuidad del negocio**.

Note: El PDS es mucho más que un documento: es la estrategia integral que guía todas las decisiones de seguridad en la organización. No se trata solo de tecnología, sino de un enfoque holístico que abarca personas, procesos y herramientas. El PDS proporciona dirección, prioridades y justificación para las inversiones en seguridad. Sin un PDS, las organizaciones actúan reactivamente, apagando fuegos en lugar de prevenir incendios.


### 2.2. Requisitos para un PDS eficaz

Para que el PDS funcione debe:

1. **Alinearse** con la estrategia general y tecnológica de la empresa.
2. Tener un **alcance claro** (procesos, departamentos, sistemas incluidos).
3. **Asignar responsabilidades** a personal interno y proveedores.
4. Contar con **aprobación explícita de la dirección** (recursos y legitimidad).
5. **Contemplar obligaciones legales** (RGPD, ENS, PCI-DSS...) y buenas prácticas.

Note: Estos cinco requisitos son fundamentales. Sin alineación con el negocio, el PDS se convertirá en un proyecto de IT desconectado. Sin alcance claro, se desperdician recursos. Sin responsabilidades definidas, nadie se hace cargo. Sin apoyo de dirección, no habrá presupuesto ni autoridad. Sin considerar el marco legal, la empresa se expone a sanciones millonarias. Un PDS eficaz requiere visión de negocio, no solo técnica.


### 2.3. Ciclo de vida del PDS

* El PDS **no es un documento estático**.
* Tras completar un ciclo, se **revisa y reinicia**.
* Incorpora:
  * Cambios en la organización
  * Nuevas amenazas
  * Lecciones aprendidas
* **Mejora continua** es la clave.

Note: La seguridad es un proceso dinámico, no un proyecto con fecha de fin. Las amenazas evolucionan constantemente: nuevos tipos de malware, técnicas de ingeniería social, vulnerabilidades de día cero. La organización también cambia: nuevos servicios, fusiones, expansión geográfica. Las lecciones aprendidas de incidentes y auditorías deben realimentar el plan. Organizaciones maduras revisan su PDS anualmente como mínimo, y lo ajustan cuando hay cambios significativos en el negocio o el entorno de amenazas.

---

## 3. Visión general del ciclo del PDS


### 3.1. Las seis fases del ciclo (INCIBE)

1. **Conocer la situación actual** de la organización.
2. **Entender la estrategia** de la organización.
3. **Definir proyectos e iniciativas** de seguridad.
4. **Clasificar y priorizar** los proyectos.
5. **Obtener la aprobación** de la dirección.
6. **Poner en marcha** el plan y establecer la mejora continua.

Note: Este ciclo propuesto por INCIBE (Instituto Nacional de Ciberseguridad de España) es la referencia para organizaciones españolas. Cada fase se construye sobre la anterior formando un proceso lógico y secuencial. Si saltamos fases o las ejecutamos mal, todo el plan se tambalea. Por ejemplo, si la fotografía inicial (fase 1) es deficiente, las decisiones posteriores estarán desalineadas. Si no entendemos la estrategia (fase 2), priorizaremos proyectos incorrectos. Es fundamental seguir el orden y dedicar tiempo a cada fase.


### 3.2. Interdependencia de las fases

* Cada fase se **apoya en la anterior**.
* Una fotografía inicial deficiente → decisiones desalineadas.
* Sin entender la estrategia → prioridades incorrectas.
* El plan pierde **credibilidad** si las bases son débiles.
* **Calidad > velocidad** en la planificación.

Note: La tentación de ir rápido y saltarse pasos es grande, especialmente cuando hay presión para "hacer algo ya". Sin embargo, un PDS mal fundamentado es peor que no tener PDS: genera inversiones erróneas, frustración en los equipos y pérdida de confianza de la dirección. Es mejor tomarse el tiempo necesario en las fases iniciales de diagnóstico y estrategia. Un mes bien invertido en análisis puede ahorrar meses de trabajo malgastado en proyectos incorrectos.


### 3.3. Representación del ciclo

<figure markdown>
  ![Ciclo del PDS](assets/IS-U1.2.1.-PlanDirectorDeSeguridad-ciclo-1698075503912.png)
  <figcaption>Ciclo completo del Plan Director de Seguridad</figcaption>
</figure>

Note: Esta imagen representa visualmente cómo las seis fases forman un ciclo continuo. Observad que tras la fase 6 (puesta en marcha), la flecha vuelve a la fase 1, indicando que el proceso se reinicia. Esto refuerza el concepto de mejora continua. En cada iteración del ciclo, la organización alcanza un nivel superior de madurez en seguridad. Es como una espiral ascendente: se repiten las fases pero cada vez desde una posición más avanzada.


---

## 4. Fase 1: Conocer la situación actual


### 4.1. Objetivo de la fase

* Obtener una **fotografía precisa** del estado actual de seguridad.
* Análisis en **tres dimensiones**:
  * Técnica (infraestructura, vulnerabilidades)
  * Organizativa (políticas, procesos, roles)
  * Cumplimiento (legal y normativo)
* Identificar **brechas de seguridad** y áreas de mejora.

Note: Esta es la fase más crítica porque establece la línea base. Es como un chequeo médico completo: no podemos diseñar un tratamiento sin conocer el estado del paciente. El análisis debe ser exhaustivo pero proporcionado al tamaño de la organización. En una pyme puede tomar 2-4 semanas; en una gran corporación, meses. Se utilizan entrevistas, revisiones documentales, escaneos técnicos y observación directa. Es fundamental ser honesto: ocultar problemas solo los agrava.


### 4.2. Actividades previas: definir el alcance

**a) Definir el alcance del PDS**

* ¿Qué **departamentos** incluir? (IT, administración, producción...)
* ¿Qué **activos y procesos** proteger? (servidores, datos, aplicaciones...)
* Considerar **negocios críticos** y cadena de valor.
* Alcance realista según **recursos disponibles**.

Note: No se puede proteger todo a la vez ni con el mismo nivel de inversión. Definir el alcance es un ejercicio de priorización: comenzad por los procesos que generan ingresos o cuya paralización detendría la operación. Por ejemplo, en un e-commerce, la web y la base de datos de clientes son críticos; la intranet de RR.HH. es importante pero secundaria. Empezad con un alcance manejable y expanded gradualmente en iteraciones futuras del ciclo. Un error común es intentar abarcar toda la organización en el primer ciclo y paralizarse por la complejidad.


### 4.3. Actividades previas: inventario de activos

**b) Identificar responsable de gestión de activos**

* Nombrar **responsables** por tipo de activo.
* Crear **inventario completo** de activos:
  * Hardware (servidores, equipos, dispositivos móviles)
  * Software (aplicaciones, sistemas operativos, licencias)
  * Datos (BBDD, ficheros, información crítica)
  * Personal (conocimientos, habilidades clave)
  * Instalaciones (centros de datos, sedes)

Note: Un buen inventario es la columna vertebral de la seguridad. "No puedes proteger lo que no conoces" es una máxima fundamental. EJEMPLOS DE INVENTARIO: Hardware: "SRV-PROD-01: Dell PowerEdge R740, 64GB RAM, 2TB RAID5, Windows Server 2022, CPD Madrid rack 4U, responsable: Juan García (IT Manager), criticidad: Alta (servidor ERP), última actualización inventario: 15/01/2025". "WKS-USER-045: Lenovo ThinkPad T14, i5-1135G7, 16GB, usuario: María López (ventas), ubicación: oficina Barcelona, cifrado BitLocker activo". Software: "SAP ERP v9.2: 50 licencias concurrentes, €120k/año mantenimiento, responsable: Director Financiero, 300 usuarios registrados, servidor SRV-PROD-01". "Microsoft 365 E3: 250 licencias, €3.150/mes, responsable: IT, crítico para correo+colaboración". Datos: "BBDD clientes CRM: 45.000 registros con datos personales (nombre, email, teléfono, historial compras), clasificación: CONFIDENCIAL (RGPD), responsable tratamiento: Director Comercial, DPO: Ana Ruiz, backup diario, retención 7 años". "Carpeta compartida \\srv-files\contratos: 1.200 contratos clientes escaneados, clasificación: CONFIDENCIAL, acceso: solo dpto legal+dirección, cifrada EFS". Personal clave: "Juan García (IT Manager): único que conoce configuración completa firewall Fortinet + claves maestras backup offline, antigüedad 15 años, riesgo: conocimiento crítico concentrado en 1 persona, mitigación: documentar + formar backup (técnico junior)". Instalaciones: "CPD principal: c/ Serrano 123 Madrid, sala 40m², climatización redundante, SAI 30min, acceso biométrico, 12 racks, 45 servidores físicos + 120 VMs, conectividad: 2×1Gbps fibra redundantes".


### 4.4. Valoración inicial

**c) Valoración inicial de la situación**

* **Situación actual** de la organización en seguridad.
* **Controles existentes**: qué medidas están ya implementadas.
* **Requisitos aplicables**: normativas y estándares que aplican.
* Identificación de **carencias y debilidades**.

Herramientas: entrevistas, cuestionarios, auditorías técnicas.

Note: La valoración inicial combina métodos cualitativos (entrevistas con responsables) y cuantitativos (escaneos de vulnerabilidades). Usad frameworks reconocidos como ISO/IEC 27002 o NIST CSF como checklist. Evitad el síndrome del "todo está mal": buscad también lo que sí funciona para construir sobre ello. Documentad evidencias: no bastan opiniones, necesitáis capturas de configuraciones, informes de herramientas, políticas existentes. Esta documentación será la base para medir el progreso futuro.


### 4.5. Análisis de madurez organizativa

* Evaluar **madurez de los controles** usando escalas (ej: CMM).
  * Nivel 0: Inexistente
  * Nivel 1: Inicial (ad-hoc)
  * Nivel 2: Repetible
  * Nivel 3: Definido (documentado)
  * Nivel 4: Gestionado (métricas)
  * Nivel 5: Optimizado (mejora continua)

Note: La escala de madurez CMM (Capability Maturity Model) permite evaluar cada control de forma objetiva. EJEMPLOS con "Copias de seguridad": Nivel 0 - Inexistente: no hay copias de seguridad; Nivel 1 - Inicial: Juan hace copias en USB cuando se acuerda, sin seguir ningún proceso; Nivel 2 - Repetible: se hacen copias cada viernes mediante script, siempre el mismo técnico, pero no está documentado; Nivel 3 - Definido: existe procedimiento "PROC-BACKUP-001" que especifica qué, cuándo, cómo y responsable; Nivel 4 - Gestionado: se registran las copias en CMDB, se mide % éxitos, tiempo de backup, se revisa trimestralmente; Nivel 5 - Optimizado: sistema automatizado que ajusta ventanas de backup según carga, alertas predictivas, mejora continua basada en métricas. Otro ejemplo con "Gestión de contraseñas": Nivel 0: no hay política; Nivel 1: "usa contraseña fuerte" sin definir qué es; Nivel 2: se exige 8 caracteres mínimo; Nivel 3: política documentada con complejidad, caducidad, historial; Nivel 4: se mide cumplimiento, auditorías periódicas; Nivel 5: gestor de contraseñas corporativo, MFA, revisión continua de robustez.


### 4.6. Análisis técnico

* Estado de la **infraestructura tecnológica**.
* **Configuraciones de seguridad** actuales (firewalls, antivirus...).
* **Vulnerabilidades conocidas** (escaneo con herramientas).
* **Medidas de protección** implementadas.
* **Arquitectura de red** y segmentación.

Note: El análisis técnico es el más objetivo y medible. Usad herramientas de escaneo de vulnerabilidades (Nessus, OpenVAS, Qualys...) para identificar sistemas desactualizados, configuraciones inseguras y puertos abiertos innecesarios. Revisad logs de seguridad históricos para detectar patrones de ataques. Analizad la arquitectura: ¿está la red segmentada? ¿hay perímetros defensivos? ¿se aplican principios de privilegio mínimo? Este análisis suele revelar quick wins: problemas fáciles de solucionar que reducen significativamente el riesgo.


### 4.7. Análisis de cumplimiento normativo

Verificar cumplimiento con:

* **RGPD** - Protección de datos personales (multas hasta 20M€)
* **ENS** - Esquema Nacional de Seguridad (Administraciones)
* **ISO/IEC 27001** - Gestión de seguridad de información
* Normativas **sectoriales**: PCI-DSS (pagos), HIPAA (salud)...

Note: El cumplimiento normativo no es opcional y las sanciones pueden ser devastadoras. El RGPD europeo ha impuesto multas millonarias a empresas como Amazon (746M€) o Google (90M€). El análisis debe identificar qué normativas aplican a vuestra organización según sector, tamaño y tipo de datos que maneja. Usad checklists oficiales: para RGPD, la AEPD ofrece guías; para ENS, el CCN-CERT. Documentad las brechas de cumplimiento y priorizadlas porque el riesgo legal es inmediato y cuantificable. El análisis puede requerir apoyo de departamento legal.

---

## 5. Fase 2: Entender la estrategia de la organización


### 5.1. Objetivo de la fase

* **Alinear seguridad con el negocio**: el PDS debe servir a los objetivos empresariales.
* Entender qué procesos son **críticos para la operación**.
* Identificar **iniciativas estratégicas** futuras (expansión, digitalización...).
* Definir el **nivel de riesgo aceptable** para la dirección.
* Establecer **presupuesto disponible** para seguridad.

Note: Esta fase es donde la seguridad deja de ser un tema técnico para convertirse en un tema de negocio. Reunios con la dirección y responsables de áreas: ventas, operaciones, finanzas. Entended qué les quita el sueño, qué iniciativas tienen en sus roadmaps, qué riesgos han asumido conscientemente. Un PDS desalineado con la estrategia será ignorado o saboteado. Por ejemplo, si la empresa planea lanzar una app móvil, el PDS debe contemplar seguridad móvil y APIs; si no, será irrelevante cuando llegue el momento.


### 5.2. Comprender el modelo de negocio

Preguntas clave:

* ¿Cuál es el **core business**? ¿Qué genera los ingresos?
* ¿Qué procesos son **críticos**? ¿Cuáles pueden detenerse temporalmente?
* ¿Cuáles son los **activos más valiosos**? (marca, conocimiento, datos...)
* ¿Qué **dependencias** tiene la operación? (proveedores, partners, cloud...)
* ¿Cuál es el **apetito de riesgo** de la organización?

Note: Cada organización tiene un perfil de riesgo diferente. Una startup tecnológica puede aceptar riesgos que un banco consideraría intolerables. Entender el modelo de negocio permite dimensionar correctamente las inversiones en seguridad. No se trata de alcanzar "seguridad perfecta" (que no existe), sino el nivel adecuado para ese negocio específico. Una tienda online que factura 5M€/año no debería invertir 2M€ en seguridad, pero tampoco solo 5000€. La proporción depende del sector, regulación y exposición al riesgo.


### 5.3. Identificar objetivos estratégicos

* ¿Qué **objetivos tiene la organización** a 1-3 años?
  * Expansión geográfica
  * Nuevos productos/servicios
  * Transformación digital
  * Cumplimiento de certificaciones
* ¿Cómo **impacta la seguridad** en esos objetivos?
* ¿Qué **amenazas** podrían impedirlos?

Note: Los objetivos estratégicos dan contexto al PDS. Si la empresa quiere certificarse ISO 27001 para ganar un contrato grande, esto marca prioridades claras. Si planea abrir oficina en Alemania, las exigencias del RGPD se intensifican. Si quiere ofrecer servicios cloud, la seguridad de APIs y datos en tránsito son prioritarias. Conectad cada proyecto de seguridad con un objetivo de negocio: "implantamos MFA porque permite trabajar remotamente sin aumentar el riesgo, lo que facilita contratar talento geográficamente distribuido".


### 5.4. Determinar el nivel de riesgo aceptable

* Definir **qué riesgos** puede asumir la organización.
* Establecer **umbrales**: ¿qué nivel de riesgo requiere acción inmediata?
* Considerar **impacto económico**: ¿cuánto cuesta un día de paralización?
* Tener en cuenta **impacto reputacional** y legal.

Ejemplo: "No aceptamos riesgos >100k€ de impacto potencial con probabilidad >20%"

Note: El riesgo aceptable no es una cifra arbitraria: debe calcularse considerando el impacto en negocio. EJEMPLO CÁLCULO BIA (Business Impact Analysis): E-commerce factura 5M€/año → 14k€/día promedio. Web caída pierde 100% ingresos online (60% total=8.4k€/día) + reputación + penalizaciones SLA proveedores. Día caído=10k€ pérdida directa. Semana caída=70k€ + clientes que se van (30% no vuelven)=impacto total ~150k€. Por tanto: "RTO web=4 horas máximo (coste 4h=1.7k€ tolerable), riesgo >50k€ impacto con prob>20% NO aceptable → requiere mitigación". Otro ejemplo: Clínica dental. Parálisis sistema citas 1 día: 40 pacientes/día × ticket medio 80€ = 3.2k€ pérdida + reprogramaciones manual 8h técnico = 3.5k€ total. RTO=24h aceptable (impacto contenido). BBDD pacientes filtrada: multa RGPD hasta 20M€ o 4% facturación (en pyme=500k€ realista) + litigios 50 pacientes=100k€ + cierre ordenado temporalmente=200k€ → impacto total ~800k€ → probabilidad mínima 5% ya da riesgo 40k€ esperado → NO aceptable, requiere cifrado+controles acceso+backup seguro. Con estos números, dirección firma: "Aceptamos riesgos con impacto<20k€ + probabilidad<30% = riesgo inherente <6k€. Todo riesgo>6k€ esperado debe tratarse o justificarse con firma CEO". Esto da criterio objetivo para priorizar proyectos del PDS.


### 5.5. Mapeo de procesos críticos

* Identificar y documentar **procesos de negocio críticos**.
* Determinar **dependencias tecnológicas** de cada proceso.
* Establecer **RTOs y RPOs**:
  * RTO (Recovery Time Objective): tiempo máximo de recuperación tolerable
  * RPO (Recovery Point Objective): pérdida de datos máxima tolerable
* Priorizar procesos por **impacto en negocio**.

Note: El mapeo de procesos críticos es un BIA (Business Impact Analysis) ligero. No todos los procesos son iguales: el proceso de facturación es más crítico que el de gestión de vacaciones. Para cada proceso crítico, estableced RTOs y RPOs realistas: "el sistema de ventas debe recuperarse en <4 horas (RTO) con pérdida máxima de 1 hora de transacciones (RPO)". Esto determina qué tipo de copias de seguridad, redundancia y planes de contingencia necesitáis. Un RTO de 4 horas permite restauración desde backup; un RTO de 15 minutos requiere alta disponibilidad activo-pasivo.


### 5.6. Restricciones y recursos disponibles

* **Presupuesto** disponible para seguridad (CAPEX y OPEX).
* **Recursos humanos**: ¿hay equipo interno o se requiere externalizar?
* **Limitaciones tecnológicas**: sistemas legacy incompatibles con controles modernos.
* **Restricciones temporales**: plazos legales, fechas de auditorías.
* **Restricciones organizativas**: resistencia al cambio, cultura corporativa.

Note: Ser realista sobre recursos es fundamental para el éxito del PDS. Un plan ambicioso sin presupuesto ni personal es papel mojado. Si solo tenéis un técnico IT a media jornada, no planifiquéis desplegar un SOC completo. Valorad opciones de externalización: servicios gestionados de seguridad (MSSP), SOC as a Service, auditorías externas. Las restricciones tecnológicas son comunes: sistemas industriales antiguos que no pueden actualizarse, aplicaciones legacy sin autenticación fuerte. Documentad estas restricciones y estableced planes B o compensaciones (aislar sistemas antiguos en redes separadas, monitorización adicional...).



---

## 6. Fase 3: Definir proyectos e iniciativas


### 6.1. Objetivo de la fase

* Transformar **brechas identificadas** en proyectos concretos.
* Proponer iniciativas para **cerrar gaps** de seguridad.
* Cubrir **tres áreas principales**:
  * Organizativas y legales
  * Técnicas
  * Concienciación y formación
* Cada proyecto debe tener objetivo, alcance, recursos y métricas claras.

Note: Aquí es donde el PDS se convierte en acción. Las fases anteriores han diagnosticado problemas; ahora toca diseñar las soluciones. Es fundamental ser específico: no vale "mejorar la seguridad", necesitamos "implementar MFA en todos los accesos privilegiados en Q1 2025 con presupuesto de 15k€". Cada iniciativa debe responder a una brecha o riesgo identificado anteriormente. Mantened trazabilidad: este proyecto mitiga aquel riesgo, cierra aquella brecha de cumplimiento, eleva la madurez de este control del nivel 1 al 3.


### 6.2. Tipos de iniciativas organizativas

**Ejemplos de proyectos organizativos:**

* Redacción y aprobación de **política de seguridad** corporativa.
* Elaboración de **Declaración de Aplicabilidad (SoA)**.
* Implantación de **gestión formal de incidentes** (detección, respuesta, lecciones aprendidas).
* Programa anual de **concienciación** en seguridad.
* Adecuación a **RGPD**: evaluaciones de impacto, registro de tratamientos.
* Revisión de **contratos con proveedores** (cláusulas de seguridad, SLAs).

Note: Las iniciativas organizativas son la base: definen el marco de gobernanza. Sin políticas claras, cada persona interpreta la seguridad a su manera. EJEMPLOS: 1) Política de seguridad: "Documento de 10-15 páginas aprobado por CEO que establece principios generales: clasificación de información (pública/interna/confidencial/secreta), responsabilidades de usuarios, uso aceptable de recursos IT, consecuencias de incumplimiento. Ejemplo real: prohibido usar USB personales en equipos corporativos, datos confidenciales solo en carpetas cifradas". 2) SoA (Statement of Applicability): "Excel con los 93 controles ISO 27002: Control A.5.1 Política seguridad = Implantado nivel 3; Control A.8.1 Inventario activos = En curso nivel 2; Control A.8.23 Filtrado web = No aplicable (justificación: navegación solo en estaciones con endpoint protection)". 3) Gestión de incidentes: "Proceso con 5 fases: Detección (usuario reporta o SIEM alerta) → Clasificación (crítico/alto/medio/bajo) → Contención (aislar sistema afectado) → Erradicación (eliminar causa raíz) → Recuperación (restaurar servicio) → Lecciones (documento post-mortem). Ejemplo: phishing detectado → clasificado medio → emails maliciosos borrados de buzones → usuarios afectados formados → documentado en base conocimiento".


### 6.3. Tipos de iniciativas técnicas

**Ejemplos de proyectos técnicos:**

* **Segmentación de red** e implementación de IDS/IPS.
* Despliegue de **MFA** (autenticación multifactor) en accesos críticos.
* Implantación de **SIEM** (correlación de logs y detección de anomalías).
* Política robusta de **copias de seguridad** con pruebas periódicas de restauración.
* **Cifrado** de datos en reposo y en tránsito.
* **Gestión de vulnerabilidades**: escaneos periódicos y parcheo.
* Implementación de **DLP** (Data Loss Prevention).

Note: Las medidas técnicas son las que típicamente se asocian con "ciberseguridad", pero son ineficaces sin la base organizativa. EJEMPLOS: 1) Segmentación de red: "Dividir la red plana actual en VLANs: VLAN10=Servidores críticos (ERP, BBDD), VLAN20=Servidores web DMZ, VLAN30=Estaciones usuario, VLAN40=WiFi invitados, VLAN50=Impresoras/IoT. Firewalls entre VLANs con reglas restrictivas: VLAN30 puede acceder a VLAN10 puerto 1433 SQL solo con autenticación; VLAN40 sin acceso a VLANs internas. IDS Suricata monitorizando tráfico inter-VLAN detecta lateral movement". 2) MFA: "Implementar Microsoft Authenticator o Google Authenticator para: acceso VPN, acceso remoto (RDP/SSH), consola administración (switches, firewalls, servidores), aplicaciones críticas (ERP, correo). Ejemplo real: admin intenta acceder a servidor producción → solicita contraseña + código 6 dígitos del móvil que cambia cada 30s". 3) SIEM: "Wazuh o Splunk centralizando logs de: firewalls, servidores Windows (eventos 4624 login, 4625 fallo), Linux (auth.log), aplicaciones web, antivirus. Correlación: detecta 5 fallos login desde IP extranjera en 2 minutos → alerta SOC → bloqueo automático IP en firewall". 4) Copias seguridad: "Backup diario incremental 23:00h, completo domingos, retención 30 días on-site + 90 días off-site. Prueba restauración mensual: recuperar VM completa en <4h. Ejemplo: ransomware cifra servidor → restauración desde backup de hace 12h → pérdida 12h datos pero sistema operativo en 3h".


### 6.4. Iniciativas de continuidad

**Proyectos de continuidad del negocio:**

* **Plan de Continuidad TIC** (BIA, estrategias de recuperación).
* **Plan de Recuperación ante Desastres** (DRP).
* Pruebas periódicas de **restauración desde backup**.
* Implementación de **sistemas de alta disponibilidad** para servicios críticos.
* **Redundancia** de enlaces, energía, equipamiento crítico.

Note: La continuidad es la razón de ser de la seguridad: mantener el negocio operando incluso ante incidentes graves. El BIA (Business Impact Analysis) identifica qué procesos son críticos y su tolerancia a interrupciones. El DRP detalla paso a paso cómo recuperar sistemas tras un desastre (incendio, inundación, ransomware...). Las pruebas de restauración deben ser reales, no simuladas: restaurad un servidor completo desde backup en un entorno de pruebas. La alta disponibilidad (clustering, balanceo) elimina puntos únicos de fallo. Documentad y probad estos planes: un plan no ensayado fallará bajo presión.


### 6.5. Iniciativas de formación

**Proyectos de concienciación y capacitación:**

* Programa de **concienciación** para toda la plantilla (phishing, contraseñas...).
* **Formación técnica** especializada para el equipo IT.
* **Simulacros** de incidentes y crisis.
* Campañas de **phishing simulado** con feedback educativo.
* Sesiones de **sensibilización para directivos** (riesgos y decisiones).

Note: El factor humano es el eslabón más débil y también el más fuerte si está bien preparado. La concienciación no es una charla anual: debe ser continua, variada y medible. El phishing simulado entrena a los usuarios a identificar correos maliciosos en un entorno seguro. Las métricas (% clics en phishing simulado, % reportes de sospechosos) permiten ver el progreso. La formación técnica especializada mantiene al equipo IT actualizado en nuevas amenazas y herramientas. Los simulacros de crisis (tabletop exercises) preparan a la organización para responder coordinadamente ante incidentes reales.


### 6.6. Estructura de cada iniciativa

Cada proyecto debe definir:

* **Objetivo claro**: qué problema resuelve o qué riesgo mitiga.
* **Alcance**: qué incluye y qué no.
* **Responsable**: quién lidera el proyecto.
* **Recursos**: coste estimado, personas involucradas.
* **Cronograma**: hitos y fecha de finalización.
* **Métricas de éxito**: cómo sabemos que ha funcionado.
* **Dependencias**: qué otros proyectos o recursos requiere.

Note: La definición rigurosa de cada iniciativa es crucial para su éxito. Objetivos vagos llevan a proyectos que nunca terminan. El alcance debe ser realista: mejor completar proyectos pequeños que fallar en grandes. Asignad responsables nominales, no "el equipo IT". Los recursos incluyen no solo presupuesto sino tiempo de personas: un proyecto que requiere 200 horas de un técnico que solo tiene 40h/mes disponibles tardará 5 meses, no 1. Las métricas objetivas permiten declarar el éxito: "reducir el tiempo medio de parcheo de 45 a 15 días" es medible; "mejorar la gestión de parches" no lo es.

---

## 7. Fase 4: Clasificar y priorizar proyectos


### 7.1. Objetivo de la priorización

* **No todo puede hacerse a la vez**: recursos limitados.
* Priorizar según **impacto en reducción de riesgo**.
* Considerar **coste**, **complejidad** y **tiempo**.
* Equilibrar **quick wins** con proyectos estratégicos.
* Generar **roadmap realista** y ejecutable.

Note: La priorización es una de las decisiones más difíciles del PDS. Todas las iniciativas parecen urgentes, pero los recursos son finitos. La clave es ser riguroso y basarse en datos, no en opiniones. Un error común es intentar hacer todo en paralelo y terminar sin completar nada. Es mejor ejecutar bien 5 proyectos que ejecutar mal 20. La priorización también considera dependencias: algunos proyectos son prerequisitos de otros (ej: no puedes desplegar un SIEM si antes no centralizas los logs).


### 7.2. Criterios de priorización

Factores a considerar:

* **Riesgo que mitiga**: ¿reduce riesgos críticos o moderados?
* **Urgencia legal**: ¿hay deadlines regulatorios?
* **Coste**: inversión requerida (CAPEX y OPEX).
* **Complejidad técnica**: ¿cuánto esfuerzo de implementación?
* **Tiempo**: ¿cuánto tarda en completarse?
* **Impacto en negocio**: ¿cómo afecta a operaciones durante la implantación?
* **ROI esperado**: ¿cuánto riesgo reduce por euro invertido?

Note: Usad una matriz de decisión con estos criterios ponderados. Por ejemplo: riesgo que mitiga (peso 40%), coste (20%), complejidad (15%), tiempo (15%), impacto negocio (10%). Puntuad cada proyecto (1-5) en cada criterio y calculad la puntuación ponderada. Los proyectos con mayor puntuación son prioritarios. La urgencia legal puede ser determinante: una multa de RGPD justifica priorizar proyectos de protección de datos sobre otros de mayor ROI técnico. El impacto en negocio: evitad proyectos que paralicen operaciones críticas en temporadas altas.


### 7.3. Quick wins

**Características de quick wins:**

* **Alto impacto** en seguridad.
* **Bajo coste** y esfuerzo.
* **Rápidos** de implementar (semanas, no meses).
* **Visibles**: demuestran progreso a la organización.

**Ejemplos:**
* Habilitar MFA en cuentas de administrador.
* Realizar prueba de restauración de backups.
* Implementar política de contraseñas robustas.

Note: Los quick wins son fundamentales para generar momentum y credibilidad. Cuando la organización ve resultados rápidos, aumenta la confianza en el PDS. EJEMPLOS CONCRETOS: 1) "Habilitar MFA en admins": Coste=0€ (Google/Microsoft Authenticator gratis), Tiempo=2 días (instalar app en móviles 5 admins + configurar), Impacto=crítico (previene 99.9% compromiso credenciales). Caso real: admin con contraseña filtrada en breach → atacante intenta acceder pero no tiene el código del móvil → ataque bloqueado. 2) "Prueba restauración backups": Coste=500€ (tiempo técnico), Tiempo=1 semana (restaurar 1 servidor test completo + 1 BBDD), Impacto=alto (descubre que 30% backups estaban corruptos, se corrige antes del desastre real). Ejemplo: intentan restaurar SQL Server desde backup de hace 1 mes → error "archivo corrupto" → identifican que tarea backup fallaba silenciosamente desde hace 3 meses → reconfiguran + alertas. 3) "Política contraseñas robustas": Coste=0€, Tiempo=1 semana (redactar política + configurar AD: mínimo 12 caracteres, mayús+minús+número+símbolo, caducidad 90 días, historial 24 contraseñas), Impacto=medio (reduce ataques de diccionario). Ejemplo real: antes "Empresa123" era válida → ahora requiere "Empr3s4!2024$Seg". Estos 3 proyectos cuestan 500€, tardan 4 semanas, reducen significativamente 3 riesgos críticos → perfecto para Q1 y demostrar valor.


### 7.4. Proyectos estratégicos

**Características de proyectos estratégicos:**

* **Alto impacto** a medio-largo plazo.
* **Mayor inversión** y recursos.
* **Complejidad** técnica u organizativa significativa.
* Requieren **cambios culturales** o de procesos.

**Ejemplos:**
* Implementar SGSI completo (ISO 27001).
* Desplegar SOC (Security Operations Center).
* Transformar arquitectura a Zero Trust.

Note: Los proyectos estratégicos transforman la postura de seguridad de manera fundamental. Son inversiones que requieren visión a largo plazo y paciencia. La certificación ISO 27001 puede tardar 12-18 meses pero proporciona un marco completo de gobernanza. Un SOC cambia radicalmente la capacidad de detección y respuesta, pero requiere inversión en herramientas, personal y procesos. La arquitectura Zero Trust elimina confianza implícita en la red, pero implica rediseñar prácticamente todo. Estos proyectos necesitan apoyo sostenido de dirección y planificación cuidadosa.


### 7.5. Matriz de priorización

<figure markdown>
  ![Matriz de priorización](assets/IS-U1.2.1.-PlanDirectorDeSeguridad-priorizacion.png)
  <figcaption>Matriz: Impacto vs Esfuerzo</figcaption>
</figure>

* **Alto impacto, bajo esfuerzo** → Quick wins (primera prioridad)
* **Alto impacto, alto esfuerzo** → Proyectos estratégicos (segunda prioridad)
* **Bajo impacto, bajo esfuerzo** → Relleno (si sobran recursos)
* **Bajo impacto, alto esfuerzo** → Descartar

Note: La matriz impacto-esfuerzo es visual e intuitiva para comunicar prioridades. El cuadrante superior izquierdo (alto impacto, bajo esfuerzo) es oro: hacedlos primero. El superior derecho (alto impacto, alto esfuerzo) son los estratégicos: planificadlos tras los quick wins. El inferior izquierdo (bajo impacto, bajo esfuerzo) se puede hacer si sobra tiempo. El inferior derecho (bajo impacto, alto esfuerzo) generalmente no vale la pena: descartadlos o diferidlos indefinidamente. Revisad esta matriz en cada ciclo del PDS.


### 7.6. Cronograma realista

* Distribuir proyectos en **horizontes temporales**:
  * Corto plazo (0-6 meses): Quick wins y urgencias.
  * Medio plazo (6-12 meses): Proyectos estructurales.
  * Largo plazo (12-24 meses): Transformaciones estratégicas.
* Considerar **capacidad real** del equipo.
* Incluir **holguras** (siempre hay imprevistos).
* **Milestones visibles** para seguimiento.

Note: Un cronograma irreal condena al PDS al fracaso. Sed conservadores: multiplicad las estimaciones iniciales por 1.5 o 2. Considerad vacaciones, bajas, otros proyectos concurrentes. No planifiquéis proyectos críticos en temporadas de negocio intenso. Estableced milestones intermedios que permitan celebrar avances y detectar retrasos temprano. Un buen cronograma tiene buffers entre proyectos. Usad herramientas de gestión de proyectos (Gantt, Kanban) para visualizar dependencias y carga de trabajo.


---

## 8. Fase 5: Obtener la aprobación de la dirección


### 8.1. Objetivo de la fase

* **Conseguir el compromiso real** de la dirección.
* Presentar el PDS de forma **ejecutiva y convincente**.
* Justificar la **inversión** en términos de negocio.
* Obtener **asignación de recursos**: presupuesto, personal, autoridad.
* Formalizar **responsabilidades** y gobernanza.

Note: Esta es la fase política del PDS. Sin aprobación de dirección, todo lo anterior es papel mojado. La dirección debe entender que la seguridad no es un gasto sino una inversión en continuidad del negocio. La presentación debe durar 30-45 minutos máximo: directivos no tienen tiempo para detalles técnicos. Usad lenguaje de negocio: "este proyecto reduce el riesgo de paralización de ventas online que cuesta 50k€/día". Preparad respuestas a objeciones típicas: "es muy caro", "podemos esperar", "nunca nos ha pasado nada".


### 8.2. Preparación de la presentación ejecutiva

**Elementos imprescindibles:**

* **Resumen ejecutivo** (1-2 páginas): situación, riesgos, propuesta, inversión.
* **Análisis de riesgos** en lenguaje de negocio (impactos económicos y reputacionales).
* **Catálogo de proyectos priorizados** con justificación clara.
* **Presupuesto desglosado** (CAPEX y OPEX) y cronograma.
* **ROI o coste de no hacer nada**: comparar inversión vs impacto potencial de incidentes.
* **Quick wins** destacados: victorias tempranas que demuestran valor.

Note: La presentación ejecutiva debe ser visual y concisa. Usad gráficos, no tablas. Destacad números que impacten: "sin este plan, un ransomware nos costaría 500k€ en rescate, pérdida de negocio y recuperación; el plan completo cuesta 150k€ en 2 años". Incluid casos reales de empresas similares que sufrieron incidentes: esto hace tangible la amenaza. Preparad versiones corta (15 min), media (30 min) y larga (45 min) para adaptaros al tiempo disponible. Ensayad la presentación.


### 8.3. Comunicar el coste de la inacción

* Calcular el **coste potencial de incidentes** principales:
  * Ransomware: rescate + tiempo inactivo + recuperación + multas RGPD.
  * Fuga de datos: multas + litigios + pérdida de clientes + daño reputacional.
  * Indisponibilidad: ingresos perdidos × RTO.
* Comparar con el **coste del PDS**.
* Usar **casos reales** del sector: "la competencia X sufrió Y y le costó Z".
* Mostrar **tendencia de amenazas**: los ataques crecen exponencialmente.

Note: Los directivos responden a números. Un ransomware promedio cuesta 4.24M$ según IBM (2021), pero puede hundir una pyme. Las multas RGPD van de 10M€ o 2% facturación (leve) a 20M€ o 4% (grave). Calculad escenarios: "si nos hackean la BBDD de clientes, multa estimada 500k€ + litigios 200k€ + 30% clientes se van = 1M€". Este cálculo justifica una inversión de 150k€ en dos años. Usad informes sectoriales de Verizon DBIR, IBM Cost of Data Breach, etc. para datos creíbles.


### 8.4. Conseguir el compromiso

La aprobación debe incluir:

* **Firma del acta de aprobación** del PDS por CEO/Consejo.
* **Asignación de presupuesto** en plan financiero anual.
* **Nombramiento de sponsor ejecutivo** (defensor del plan en dirección).
* **Asignación de responsable del PDS** (CISO, responsable IT, externo).
* **Inclusión en objetivos estratégicos** y balanced scorecard.
* **Calendario de revisiones** trimestrales con comité de dirección.

Note: El compromiso debe ser explícito y documentado, no una aprobación verbal. El sponsor ejecutivo es crucial: un miembro de dirección que defiende el PDS en decisiones estratégicas y desbloquea recursos. Sin sponsor, el PDS compite en desventaja con otros proyectos. El responsable del PDS debe tener autoridad transversal y acceso directo a dirección. Las revisiones trimestrales aseguran seguimiento continuo: presentad avances, riesgos, desviaciones y decisiones necesarias. Si dirección ve progreso, renovará su compromiso.


### 8.5. Gestionar resistencias

**Objeciones típicas y respuestas:**

* "Es muy caro" → Comparar con coste de un incidente.
* "Nunca nos ha pasado" → Mostrar estadísticas: pasa a empresas como la nuestra.
* "Podemos esperar" → Destacar urgencias legales (RGPD) y crecimiento de amenazas.
* "IT ya se encarga" → Explicar que la seguridad requiere enfoque estratégico, no solo operativo.
* "Tenemos antivirus" → Educar que la seguridad es multi-capa, no una herramienta única.

Note: Anticipad resistencias antes de la presentación. EJEMPLOS DE DIÁLOGOS REALES: Director Financiero: "130k€ es muy caro, no tenemos presupuesto". Respuesta: "Entiendo la preocupación. Un solo ransomware nos costaría 200k€ en rescate+recuperación+pérdida negocio según estadísticas de nuestro sector. Además, sin certificación ISO 27001 perdemos el contrato con ClienteGrande que vale 1M€/año. La inversión de 130k€ protege ingresos de 6M€ anuales y evita pérdidas de 200-500k€. El coste real es no hacerlo". CEO: "Llevamos 20 años y nunca nos han hackeado". Respuesta: "Cierto, hemos tenido suerte. Pero el panorama cambió: según informe Verizon DBIR, el 43% de pymes sufrieron ciberataques en 2023, 60% cerraron en 6 meses. Empresas de nuestro sector como [CompetidorX] sufrieron ransomware el año pasado con coste 300k€. Las amenazas crecen 400% anualmente. No es cuestión de 'si' sino 'cuándo'". Director Comercial: "¿No puede esperar al próximo ejercicio?". Respuesta: "El RGPD nos obliga a proteger datos clientes ahora: si hay brecha, multa hasta 20M€ o 4% facturación. Además, ClienteGrande exige ISO 27001 para renovar contrato en julio. Si esperamos, perdemos el contrato. Los quick wins (pruebas backup, MFA) solo cuestan 6.5k€ y reducen 60% del riesgo en Q1". Técnico IT: "Ya tenemos antivirus y firewall, con eso basta". Respuesta: "El antivirus solo detecta malware conocido (40% de ataques según Gartner). No protege contra phishing (85% de brechas empiezan así), ni ransomware de día cero, ni fugas internas. Necesitamos defensa en profundidad: formación+MFA+segmentación+backup+monitorización. Es como un edificio: no basta cerrar la puerta, necesitas alarma+cámaras+vigilante+caja fuerte".

---

## 9. Fase 6: Puesta en marcha y mejora continua


### 9.1. Objetivo de la fase

* **Ejecutar los proyectos** planificados según prioridades.
* Establecer **gobernanza**: comité, responsables, procesos de seguimiento.
* Definir y medir **KPIs** para evaluar progreso.
* **Comunicar avances** a toda la organización.
* Preparar la **revisión del ciclo** para mejora continua.

Note: Aquí es donde el plan se convierte en realidad. La ejecución requiere disciplina de gestión de proyectos: seguimiento de hitos, gestión de riesgos, cambios, comunicación. No subestiméis la gestión del cambio organizativo: la seguridad implica cambios en hábitos de las personas y esto genera resistencia. Celebrad cada logro: completar un proyecto, pasar una auditoría, detectar y bloquear un ataque. La comunicación interna mantiene la visibilidad y el apoyo.


### 9.2. Establecer la gobernanza

**Estructuras necesarias:**

* **Comité de gestión del PDS**: se reúne mensualmente, revisa avances, resuelve bloqueos.
  * Miembros: CISO/responsable IT, responsables de áreas, sponsor ejecutivo.
* **Responsables de proyecto**: cada iniciativa tiene un líder nominal.
* **RACI matrix**: quién es responsable, aprobador, consultado, informado en cada tarea.
* **Procesos de escalado**: cómo se elevan problemas y decisiones que requieren dirección.

Note: La gobernanza asegura que el PDS no se quede en un cajón. El comité de gestión es el motor del plan: revisa KPIs, ajusta prioridades, desbloquea recursos. Las reuniones mensuales de 60-90 minutos son suficientes si están bien preparadas: enviad dashboard previo, centrad la reunión en decisiones. La RACI matrix elimina ambigüedades: cada tarea tiene un responsable claro que rinde cuentas. Los procesos de escalado evitan parálisis: si un proyecto se bloquea, hay un camino claro para resolverlo en dirección.


### 9.3. Definir KPIs (indicadores clave)

**Ejemplos de KPIs efectivos:**

* **% de controles implantados** vs planificados (ej: 45/100 controles al 80% de madurez).
* **Tiempo medio de respuesta** a incidentes (MTTR).
* **% de restauraciones exitosas** en pruebas de backup (meta: 100%).
* **% de empleados** formados en concienciación (meta: 100% anual).
* **Tiempo medio de parcheo** de vulnerabilidades críticas (meta: <15 días).
* **% cumplimiento de SLAs** con proveedores críticos.
* **Riesgo residual agregado** (debe disminuir trimestre a trimestre).

Note: Los KPIs deben ser SMART: específicos, medibles, alcanzables, relevantes, temporales. Evitad KPIs vanidad como "número de logs analizados" que no reflejan mejora en seguridad. EJEMPLOS CONCRETOS CON VALORES: 1) "% controles implantados": Mes 1=15% (15/100 controles nivel≥3), Mes 6=45%, Mes 12=70%. Dashboard con barra de progreso verde. 2) "MTTR (Mean Time To Respond)": situación inicial=48 horas desde detección hasta contención; Meta año 1=12h; Medición real: Ene=45h, Feb=38h, Mar=28h... Dic=11h. Gráfico tendencia descendente. 3) "% restauraciones exitosas": Mes 1=70% (7 de 10 backups restauran OK), Mes 3=85%, Mes 6=100%. Ejemplo medición: cada mes se intenta restaurar 1 servidor completo y 2 BBDD; éxito=sistema arranca y datos íntegros en <RTO. 4) "Tiempo parcheo vulnerabilidades críticas": CVE crítico publicado → tiempo hasta aplicar patch en todos sistemas afectados. Inicial=45 días, Meta=<15 días. Ejemplo: CVE-2024-XXXX crítico Windows → detectado día 1 con scanner → parcheado 100% servidores día 8 → KPI=8 días (verde). 5) "% empleados formados": 250 empleados, objetivo 100% anual. Q1=25% (sesión presencial 62 personas), Q2=55% (e-learning 75), Q3=80%, Q4=100%. Certificados firmados como evidencia. 6) "Riesgo residual agregado": suma ponderada de riesgos altos y críticos. Q1=850 puntos, Q2=720 (proyectos mitigadores ejecutados), Q3=580, Q4=420 → tendencia clara a la baja.


### 9.4. Gestionar el cambio organizativo

* **Comunicación proactiva**: explicar el "por qué" de cada cambio.
* **Involucrar a usuarios** desde el diseño, no solo en la implantación.
* **Formación y soporte**: ayudar a las personas a adaptarse (ej: cómo usar MFA).
* **Gestión de resistencias**: identificar opositores clave y trabajar con ellos.
* **Celebrar victorias**: reconocer contribuciones y logros.

Note: El cambio organizativo es el reto más difícil del PDS. Las personas se resisten a cambios que perciben como inconvenientes adicionales sin beneficio claro para ellas. La comunicación debe enfatizar "esto nos protege a todos" y "facilitamos vuestro trabajo de forma segura". Involucrad a usuarios en pilotos: "probad esta solución y dadnos feedback". Proporcionad formación práctica, no solo manuales: sesiones cortas, vídeos, soporte directo. Identificad champions: usuarios entusiastas que adoptan temprano y evangelizan a sus colegas. Celebrad públicamente: email de felicitación, mención en reunión general.


### 9.5. Revisión periódica y ajustes

* **Revisiones mensuales** en comité de gestión: KPIs, proyectos en riesgo, decisiones.
* **Revisiones trimestrales** con dirección: progreso estratégico, ROI, peticiones de recursos.
* **Auditorías internas/externas** anuales o semestrales.
* **Actualización del análisis de riesgos** cuando cambien condiciones del negocio o aparezcan nuevas amenazas.
* **Lecciones aprendidas**: al completar cada proyecto, documentar qué funcionó y qué no.

Note: La revisión continua mantiene el PDS relevante. Las revisiones mensuales son operativas: "¿vamos según plan?". Las trimestrales son estratégicas: "¿sigue siendo el plan correcto?". Las auditorías validan que lo que decimos hacer realmente se hace. Actualizad el análisis de riesgos si lanzáis un producto nuevo, abrís una oficina, contratáis un cloud provider, hay una brecha de seguridad importante en el sector, etc. Las lecciones aprendidas crean memoria institucional: "cuando implantamos MFA, subestimamos el soporte necesario" ayuda en el siguiente proyecto.


### 9.6. Iniciar el siguiente ciclo

* Al completar el primer ciclo (típicamente 12-24 meses), **volver a la fase 1**.
* **Evaluar progreso**: qué mejoró, qué riesgos persisten.
* **Actualizar inventario** de activos y análisis técnico.
* **Redefinir alcance**: posiblemente ampliar a nuevas áreas.
* **Aprovechar lecciones aprendidas** para mejorar el proceso.
* El segundo ciclo se ejecuta **más rápido y mejor** gracias a la experiencia.

Note: El PDS es cíclico, no lineal. Completar un ciclo no significa "ya estamos seguros", sino "hemos alcanzado un nivel superior de madurez". En el segundo ciclo, la organización tiene más experiencia: el inventario está más completo, los procesos de análisis son más eficientes, la dirección está más comprometida (si el primer ciclo fue exitoso). El alcance puede ampliarse: si el primer ciclo cubrió IT corporativo, el segundo puede incluir IT operacional (OT), oficinas regionales o nuevas líneas de negocio. Este proceso de mejora continua es lo que distingue organizaciones maduras de las reactivas.



---

## 10. Caso práctico ilustrativo


### 10.1. Contexto: Editorial con e-commerce

**Empresa ejemplo:**

* Editorial mediana: 50 empleados, factura 5M€/año.
* Combina **tienda online** (60% ingresos) y **logística** de libros físicos.
* **Sistemas**: web e-commerce, ERP logístico, BBDD clientes, correo corporativo.
* **Problemática recurrente**: correos caídos, pedidos perdidos, incidentes sin respuesta coordinada.

Note: Este caso ilustrativo refleja una pyme típica española. La tienda online es crítica: si cae, el 60% de los ingresos se paraliza. Los pedidos perdidos afectan la reputación y generan costes de compensación a clientes. Los incidentes sin respuesta coordinada se resuelven caóticamente, con tiempos de recuperación impredecibles. Esta empresa necesita urgentemente un PDS. Identificad elementos similares en organizaciones que conocéis: casi todas las pymes tienen patrones similares.


### 10.2. Fase 1: Situación inicial detectada

**Análisis revela:**

* **No hay inventario** actualizado de activos.
* **Copias de seguridad** semanales, pero **nunca probadas** para restauración.
* **Red sin segmentar**: todos los sistemas en misma VLAN.
* **No hay IDS/IPS**: ataques pasan desapercibidos.
* **Políticas de contraseñas débiles**: muchas contraseñas reutilizadas, sin MFA.
* **Incidentes gestionados informalmente**: sin registro ni aprendizaje.
* Controles ISO/IEC 27002 en niveles 0-1 (inexistente o inicial).

Note: Esta fotografía es alarmante pero común. Sin inventario no se sabe qué proteger. Las copias sin probar son inútiles: el 30% de las restauraciones fallan en el primer intento. La red plana permite que un atacante se mueva libremente si compromete un equipo. Sin IDS/IPS, un atacante puede estar meses en la red sin detectar. Las contraseñas débiles son la puerta de entrada preferida. La gestión informal de incidentes impide aprender y mejorar. Este diagnóstico honest es el primer paso para mejorar.


### 10.3. Fase 2: Estrategia de negocio

**Objetivos estratégicos identificados:**

* Crecer ofreciendo **impresión bajo demanda** (más datos personales, mayor procesamiento).
* Expandirse a **mercado francés** en 18 meses (nuevo cumplimiento normativo).
* Certificarse en **ISO 27001** para ganar contrato con gran distribuidor.
* **Tolerancia a riesgo**: no más de 4 horas de caída de e-commerce (coste: 8k€/hora).
* **Presupuesto disponible**: 80k€ primer año, 50k€ segundo año.

Note: Estos objetivos estratégicos dan contexto al PDS. El servicio de impresión bajo demanda implica procesar más datos personales (archivos de clientes) y mayor carga de procesamiento (riesgo de disponibilidad). La expansión a Francia intensifica exigencias de RGPD. La certificación ISO 27001 es requisito comercial: sin ella, pierden contrato de 1M€/año. La tolerancia de 4 horas (RTO) marca el nivel de inversión en alta disponibilidad. El presupuesto de 130k€ en dos años es realista para una empresa de 5M€ facturación (2.6% durante dos años).


### 10.4. Fase 3: Riesgos identificados

**Top riesgos del análisis:**

1. **Ransomware** paraliza todos los sistemas (probabilidad media, impacto crítico = riesgo alto).
2. **Ataque DDoS** tumba el e-commerce 24-48h (probabilidad media-alta, impacto alto = riesgo alto).
3. **Fuga de datos** de clientes vía empleado o brecha técnica (prob. media, impacto crítico por RGPD = riesgo alto).
4. **Fallo prolongado** de copias de seguridad sin detectar (prob. alta, impacto crítico = riesgo crítico).
5. **Compromiso de correo** para phishing a clientes (prob. media, impacto medio = riesgo medio).

**Riesgo residual supera el umbral aceptable en web y ERP**.

Note: Estos cinco riesgos guían las prioridades del PDS. El fallo de copias es riesgo crítico porque la probabilidad es alta (nunca se prueban) y el impacto crítico (no hay recuperación posible). El ransomware es el miedo principal de toda pyme: el coste medio de recuperación es 170k€ según Sophos, más que todo el presupuesto del PDS, justificando la inversión preventiva. El DDoS es probable: los e-commerce son objetivo frecuente, especialmente en Black Friday. La fuga de datos implica multas RGPD de potencialmente 500k€. Todos estos riesgos están por encima del umbral aceptable, por lo que requieren tratamiento inmediato.


### 10.5. Fase 4: Proyectos definidos y priorizados

**20 iniciativas identificadas, priorizadas así:**

**Quick wins (Q1):**
1. **Probar restauraciones** de todas las copias (0.5k€, 2 semanas).
2. **Formalizar proceso de gestión de incidentes** (1k€, 3 semanas).
3. **Segmentar red perimetral** (5k€, 4 semanas).

**Proyectos mediano plazo (Q2-Q4):**
4. Desplegar **MFA en todos los accesos** (8k€, 8 semanas).
5. Elaborar **Plan de Continuidad TIC** con BIA (10k€, 12 semanas).
6. Lanzar **programa de concienciación** anual (6k€, continuo).
7. Implementar **IDS/IPS** y monitorización (15k€, 10 semanas).

Note: La priorización es ejemplar. Los tres quick wins cuestan solo 6.5k€ y se completan en Q1, generando momentum: las pruebas de restauración detectan problemas y se corrigen, la gestión de incidentes ordena el caos, la segmentación limita movimiento lateral. Todos reducen riesgo significativamente con poco esfuerzo. Los proyectos de mediano plazo abordan riesgos altos: MFA previene compromiso de credenciales, el Plan de Continuidad asegura capacidad de recuperación, la concienciación reduce errores humanos, el IDS/IPS detecta ataques temprano. Juntos suman 39k€ del primer año, quedando margen para imprevistos.


### 10.6. Fase 5: Aprobación obtenida

**Presentación a dirección:**

* Mostrado impacto de no actuar: ransomware costaría 200k€ (rescate + recuperación + pérdida negocio).
* Fuga RGPD costaría 500k€ en multas más pérdida clientes.
* 4 horas caída e-commerce = 32k€ pérdida.
* **PDS cuesta 130k€ en 2 años, mitigando riesgos de 700k€+.**
* Destacado que sin certificación ISO 27001, pierden contrato de 1M€/año.

**Dirección aprueba**: presupuesto, nombra sponsor (Director Financiero) y responsable del PDS (responsable IT con apoyo de consultor externo).

Note: La presentación fue efectiva porque habló en lenguaje de negocio, no técnico. Los directivos entienden perfectamente una ecuación "invertir 130k€ para evitar pérdidas potenciales de 700k€+ y habilitar contrato de 1M€/año". El ROI es claro. Nombrar al CFO (Director Financiero) como sponsor es estratégico: tiene poder de decisión sobre presupuesto y entiende el riesgo financiero. Apoyar al responsable IT con un consultor externo compensa la falta de experiencia interna en PDS. Este caso muestra que incluso pymes con presupuestos modestos pueden tener PDS exitosos si se priorizan bien.


### 10.7. Fase 6: Ejecución y resultados

**Tras 12 meses:**

* **Quick wins completados** en Q1: problemas de copias detectados y corregidos, respuesta a incidentes coordinada, red segmentada.
* **MFA desplegado** en Q2: cero compromisos de credenciales desde entonces.
* **Primer incidente respondido** con el nuevo proceso: ataque de phishing detectado, contenido en 2h, documentado y aprendido.
* **Programa de concienciación** lanzado: reducción del 60% en clics en phishing simulado.
* **IDS/IPS operativo**: detecta y bloquea 15-20 intentos de intrusión al mes.
* **KPIs verde**: riesgo residual bajo nivel aceptable, 80% proyectos año 1 completados.

**Se inicia segundo ciclo para ampliar alcance y completar ISO 27001.**

Note: Este desenlace realista muestra un PDS exitoso. Los quick wins generaron confianza y permitieron completar proyectos mayores. El MFA demuestra ROI inmediato: cero compromisos es éxito tangible. La respuesta al incidente de phishing (contenido en 2h vs los días que tardaban antes) valida la inversión en proceso. La concienciación muestra resultados medibles. El IDS/IPS visibiliza amenazas antes invisibles. Los KPIs verdes y el 80% de proyectos completados (realista: siempre hay retrasos) justifican continuar. El segundo ciclo ampliará el alcance y se trabajará la certificación ISO 27001, aprovechando la base construida. Este caso inspira confianza en que el PDS funciona.

---

## 11. Entregables esenciales del PDS


### 11.1. Documentación mínima requerida

Tras completar el ciclo, debe existir:

* **Inventario de activos** con responsables y clasificación.
* **Informe de valoración inicial** y Declaración de Aplicabilidad (SoA).
* **Matriz de madurez** por dominios con objetivos a corto y largo plazo.
* **Informes de auditoría técnica** y listas de comprobación de cumplimiento.
* **Registro de riesgos** con decisiones de tratamiento y riesgo residual.
* **Catálogo de iniciativas** con costes, recursos, dependencias y métricas de éxito.
* **Cronograma consolidado**, acta de aprobación y plan de seguimiento.
* **Informes periódicos** al comité de dirección y actas del comité de gestión.

Note: Estos entregables no son burocracia inútil: son la evidencia de que el PDS se ejecutó rigurosamente. El inventario de activos se mantiene actualizado y sirve para análisis de riesgos futuros. La SoA es requisito ISO 27001. La matriz de madurez muestra evolución trimestre a trimestre. El registro de riesgos documenta decisiones que pueden ser cuestionadas en auditorías: "¿por qué aceptaron este riesgo?". El catálogo de iniciativas permite auditar que se hizo lo que se dijo. Los informes y actas crean trazabilidad. Sin documentación, el PDS es invisible y no auditable.


### 11.2. Declaración de Aplicabilidad (SoA)

* Lista completa de **controles** de ISO/IEC 27002 (o marco elegido).
* Para cada control:
  * **Estado**: implantado, en curso, pendiente, no aplicable.
  * **Nivel de madurez** (0-5 según CMM).
  * **Justificación**: especialmente para no aplicables.
  * **Evidencias**: procedimientos, registros, configuraciones.
* La SoA se **revisa y actualiza** en cada ciclo.

Note: La SoA (Statement of Applicability) es el corazón del SGSI ISO 27001. Es un Excel/tabla que lista los 93 controles de ISO 27002 (versión 2022; versión 2013 tenía 114 en Anexo A) y documenta su estado en vuestra organización. EJEMPLOS CONCRETOS DE CONTROLES EN SoA: 1) Control "5.1 Políticas de seguridad de la información": Estado=IMPLANTADO, Madurez=3 (definido), Evidencia="Política Seguridad Corporativa v2.3 aprobada CEO 15/03/2024, publicada intranet, firmada por 100% empleados en onboarding", Responsable="CISO", Revisión="Anual (próxima marzo 2025)". 2) Control "5.7 Inteligencia de amenazas": Estado=EN CURSO, Madurez=1, Evidencia="Suscripción feeds CCN-CERT desde enero 2024, sin proceso formal análisis", Objetivo="Madurez 3 en 12 meses: procedimiento análisis semanal + correlación con activos propios", Proyecto asociado="PDS-15 Threat Intelligence". 3) Control "8.1 Dispositivos de usuario final": Estado=IMPLANTADO, Madurez=4, Evidencia="MDM Intune gestiona 245 portátiles + 180 móviles, cifrado obligatorio, políticas contraseñas, borrado remoto, inventario automático, KPI: 98% dispositivos conformes", Auditoría="Trimestral, última 10/12/2024 OK". 4) Control "8.23 Filtrado web": Estado=NO APLICABLE, Justificación="Los servidores de producción no tienen navegación web. Las estaciones de trabajo tienen protección endpoint con filtrado integrado (control 8.7). Filtrado web adicional duplicaría control sin valor añadido", Aprobado="Comité SGSI 20/11/2024". 5) Control "8.10 Eliminación de información": Estado=PENDIENTE, Madurez=0, Justificación="No existe proceso formal eliminación segura. Se requiere por RGPD", Proyecto="PDS-22 Proc.Borrado seguro", Prioridad=ALTA, Plazo="Q2 2025".


### 11.3. Matriz de madurez (CMM)

**Escala de 0 a 5 por control:**

* **0 - Inexistente**: no se realiza el control.
* **1 - Inicial**: se hace de forma ad-hoc, sin proceso ni responsables formales.
* **2 - Repetible**: método informal aplicado por personas concretas (no documentado).
* **3 - Definido**: procedimiento documentado y aprobado, se sigue habitualmente.
* **4 - Gestionado/Medido**: se mide su eficacia con KPIs, se revisa periódicamente.
* **5 - Optimizado**: mejora continua basada en métricas, se ajusta dinámicamente.

Note: CMM (Capability Maturity Model) permite objetivar la evolución. EJEMPLOS DETALLADOS POR NIVEL: Control "Gestión de accesos privilegiados": Nivel 0 - Inexistente: todos los técnicos tienen contraseña de administrador de dominio "Admin123", no hay registro ni control. Nivel 1 - Inicial: el jefe IT da acceso admin cuando se lo piden verbalmente, sin criterio formal. Nivel 2 - Repetible: se otorgan accesos según solicitud por email del jefe de departamento, siempre el mismo proceso informal. Nivel 3 - Definido: procedimiento "PROC-ACC-001" documentado: solicitud formal → aprobación por responsable de área → creación cuenta privilegiada temporal → registro en Excel; se revoca tras 90 días inactividad. Nivel 4 - Gestionado: PAM (Privileged Access Management) registra todas las sesiones, se mide tiempo medio de aprobación (meta <2h), auditorías trimestrales de cuentas activas vs necesarias. Nivel 5 - Optimizado: PAM con MFA, sesiones grabadas en vídeo, accesos just-in-time (se otorgan automáticamente por 1h para tarea específica), ML detecta comportamientos anómalos, revisión continua basada en análisis de patrones de uso. Otro ejemplo "Gestión de parches": Nivel 0: no se parchea nunca; Nivel 1: se parchea cuando hay problema; Nivel 2: parches cada 2 meses manualmente; Nivel 3: procedimiento con ventana de mantenimiento mensual, testing previo en pre-producción; Nivel 4: automatizado con WSUS/Ansible, se mide % sistemas parcheados <15 días desde CVE; Nivel 5: parcheo continuo automatizado, priorización dinámica según criticidad+exposición, rollback automático si detecta problemas.


### 11.4. Registro de riesgos

Para cada riesgo identificado, documentar:

* **Activo** afectado y su valor.
* **Amenaza** y **vulnerabilidad** asociadas.
* **Probabilidad e impacto** (escalas 1-5).
* **Riesgo intrínseco** (antes de controles) y **residual** (después).
* **Decisión de tratamiento**: mitigar, transferir, evitar, aceptar.
* **Controles aplicados** o planificados.
* **Responsable** de la decisión (especialmente para aceptaciones).
* **Fecha de revisión** (los riesgos cambian).

Note: El registro de riesgos es el documento de decisión estratégica del PDS. Debe estar firmado por dirección para riesgos aceptados: esto protege al CISO/responsable de IT de ser responsabilizado si un riesgo aceptado se materializa. Ejemplo: "Riesgo de compromiso de sistema legacy sin autenticación fuerte - Impacto Alto, Prob. Media, Riesgo Intrínseco Alto - Decisión: Aceptar temporalmente (no puede actualizarse) + Mitigar parcialmente aislando en VLAN separada - Responsable: CEO - Revisión: trimestral". Mantened este registro vivo: revisadlo tras incidentes, cambios en el negocio o nuevas amenazas.



---

## 12. Análisis de riesgos en el PDS


### 12.1. Metodología de análisis

**Proceso sistemático:**

1. **Identificar activos** críticos y su valoración.
2. **Identificar amenazas** relevantes para cada activo.
3. **Identificar vulnerabilidades** que facilitan las amenazas.
4. **Calcular riesgo intrínseco** (sin controles): Probabilidad × Impacto.
5. **Evaluar controles existentes** y su efectividad.
6. **Calcular riesgo residual** (con controles actuales).
7. **Comparar con umbral aceptable** y decidir tratamiento.

Note: El análisis de riesgos es técnico pero debe ser comprensible para dirección. Usad escalas cualitativas (muy bajo, bajo, medio, alto, muy alto) o cuantitativas (1-5) según la madurez de la organización. No busquéis precisión matemática: una aproximación razonable es suficiente. Documentad las asunciones: "probabilidad alta = ocurre 1+ veces/año según histórico sector". Revisad el análisis periódicamente y tras incidentes importantes. Apoyadfuentes externas: informes Verizon DBIR, ENISA Threat Landscape, CCN-CERT avisos.


### 12.2. Tratamiento de riesgos

**Cuatro opciones de tratamiento:**

* **Mitigar**: implementar controles para reducir probabilidad o impacto (la más común).
* **Transferir**: trasladar el riesgo a terceros (seguros, outsourcing con SLAs).
* **Evitar**: eliminar la actividad que genera el riesgo (ej: cerrar servicio no crítico).
* **Aceptar**: asumir el riesgo conscientemente porque mitigarlo cuesta más que el impacto esperado.

**Toda aceptación debe estar firmada por dirección.**

Note: La elección del tratamiento depende del coste-beneficio. EJEMPLOS CONCRETOS: 1) MITIGAR - Riesgo: "Ransomware paraliza servidores". Probabilidad=Media, Impacto=Crítico (500k€). Controles: a) Backups offline diarios (15k€/año), b) Segmentación red (8k€), c) EDR en servidores (12k€/año), d) Formación anti-phishing (3k€/año). Total 38k€ reduce probabilidad a Baja y daño a Medio (50k€) → Riesgo residual=aceptable. 2) TRANSFERIR - Riesgo: "Fuga masiva datos 100k clientes". Impacto=Catastrófico (multa RGPD 2M€ + litigios 500k€ + reputacional incalculable). Controles técnicos insuficientes solos. Solución: contratar seguro ciberriesgos 2M€ cobertura (prima 25k€/año) que cubre costes legales, multas, notificaciones, relaciones públicas. El riesgo se transfiere a la aseguradora. 3) EVITAR - Riesgo: "Servidor FTP público legacy explotable". Impacto=Alto. Análisis: se usa solo por 2 clientes antiguos que generan 500€/año. Mitigarlo requiere 10k€ (actualizar/reemplazar). Decisión: EVITAR → cerrar servicio FTP, migrar esos 2 clientes a SFTP moderno (coste 1k€) o perderlos (aceptable por bajo valor). El riesgo desaparece. 4) ACEPTAR - Riesgo: "Sistema industrial SCADA legacy sin parches". Impacto=Alto (parar producción 2 días=80k€), Probabilidad=Baja (aislado en red física sin Internet). Mitigarlo: reemplazar SCADA=300k€. Decisión dirección: ACEPTAR temporalmente (2 años hasta renovación planificada), firma CEO en registro riesgos, compensar aislando VLAN dedicada sin acceso exterior + monitorización IDS + procedimiento manual si cae.


### 12.3. Riesgo residual y umbral aceptable

Tened en cuenta:

* **Riesgo residual**: riesgo que permanece después de aplicar controles.
* **Umbral aceptable**: nivel de riesgo que la organización está dispuesta a asumir.
* **Brecha de seguridad**: diferencia entre riesgo residual y umbral aceptable.
* **Objetivo del PDS**: cerrar las brechas mediante nuevos controles.

**Ejemplo:** Umbral = "riesgo medio o inferior". Si un activo tiene riesgo residual "alto", hay brecha → proyecto del PDS para mitigarlo.

Note: El umbral no es arbitrario: se establece considerando apetito de riesgo de dirección, sector, regulación, capacidad financiera. Una startup tecnológica puede aceptar riesgos medios; un banco no puede aceptar ni riesgos bajos. La brecha de seguridad guía la priorización: riesgos muy por encima del umbral requieren acción urgente; riesgos ligeramente sobre el umbral pueden esperar. Representad visualmente con mapas de calor (heatmaps): ejes probabilidad-impacto, colores según severidad, línea marcando el umbral. Esto comunica eficazmente a dirección.

---

## 13. Buenas prácticas y errores frecuentes


### 13.1. Factores críticos de éxito

Fijáos en estos factores:

* **Apoyo visible de dirección**: sin patrocinio real, el plan fracasa.
* **Comunicación continua**: informar a toda la plantilla refuerza cultura de seguridad.
* **Coordinación entre áreas**: seguridad es transversal (RR.HH., Legal, Compras, IT, Dirección).
* **Documentación y evidencias**: decisiones y resultados documentados para auditorías.
* **Capacidad realista**: mejor pocos proyectos bien gestionados que muchos incompletos.
* **Lecciones aprendidas**: al final de cada ciclo, extraer conclusiones para mejorar.

Note: Estos factores son las lecciones de décadas de PDS exitosos y fracasados. El apoyo de dirección no es solo "dar el OK": es participar en revisiones, asignar recursos, comunicar prioridad a la organización. La comunicación debe ser bidireccional: no solo informar sino escuchar preocupaciones y feedback. La coordinación entre áreas es crucial: RR.HH. gestiona las políticas de empleados, Legal revisa contratos y cumplimiento, Compras selecciona proveedores con criterios de seguridad. La documentación protege y permite mejorar. La capacidad realista evita burn-out del equipo. Las lecciones aprendidas convierten errores en aprendizaje.


### 13.2. Errores comunes que evitar

Evitar estos errores:

* **Solo enfoque tecnológico**: ignorar personas y procesos condena al fracaso.
* **Desalineación con negocio**: proyectos de seguridad que no entiende ni apoya el negocio.
* **Presupuesto insuficiente**: infrafinanciar obliga a recortar proyectos críticos.
* **Ausencia de seguimiento**: sin control, el plan se queda en papel.
* **No involucrar usuarios**: imponer cambios sin participación genera resistencia.
* **Perfeccionismo paralizante**: esperar el análisis perfecto en lugar de iterar.
* **Falta de quick wins**: solo proyectos largos sin resultados visibles temprano.

Note: Estos errores son extraordinariamente comunes. EJEMPLOS REALES: 1) "Solo enfoque tecnológico": empresa compra firewall de última generación por 50k€, pero los empleados siguen usando contraseñas "12345" y cayendo en phishing porque nadie les formó. El firewall no para el 85% de ataques que entran por error humano. Solución correcta: 40k€ firewall + 10k€ formación anual. 2) "Desalineación con negocio": IT decide "vamos a apagar todos los servidores el viernes a las 14h para instalar parches críticos", pero resulta que es Black Friday y la web de ventas genera 50k€ entre 14-22h. Ventas furiosas, CEO furioso. Solución: coordinar ventanas de mantenimiento con calendario comercial. 3) "Presupuesto insuficiente": dirección aprueba PDS de 100k€ pero solo da 30k€. Resultado: se compra el SIEM pero no hay dinero para el técnico que lo gestione → SIEM sin configurar, sin alarmas, sin valor. 4) "Ausencia seguimiento": se lanza proyecto de segmentación de red en enero, nadie pregunta por él hasta diciembre → descubren que está parado desde abril porque el switch necesario no se compró. 5) "No involucrar usuarios": se implanta MFA sin avisar → lunes 9am 200 personas llamando a helpdesk enfadadas "no puedo entrar". Solución: pilotar con 20 usuarios, recoger feedback, formar al resto, lanzar con soporte reforzado. 6) "Perfeccionismo": "necesitamos 6 meses más de análisis para tener el inventario 100% completo antes de empezar" → nunca empiezan. Mejor: inventario 80% suficiente para empezar, refinar después. 7) "Falta quick wins": todos los proyectos tardan 12+ meses → en mes 6 dirección pregunta "¿qué hemos conseguido?" → "nada visible aún" → pierden confianza y cortan presupuesto.


### 13.3. Recomendaciones prácticas

Aplicad estas recomendaciones:

* **Empezad pequeño**: alcance acotado en primer ciclo, ampliar después.
* **Celebrad victorias**: comunicad cada hito completado.
* **Involucrad champions**: usuarios entusiastas que evangelizan.
* **Usad frameworks reconocidos**: ISO 27001, NIST, CCN-STIC... no inventéis.
* **Buscad apoyo externo** si falta experiencia: consultores, formación, comunidades.
* **Medid y comunicad el ROI**: mostrad valor generado, no solo coste.
* **Sed resilientes**: habrá obstáculos, aprended y ajustad.

Note: Estas recomendaciones vienen de la experiencia práctica. Empezar pequeño permite ganar experiencia sin riesgo excesivo. Celebrar victorias mantiene la moral y visibilidad. Los champions son multiplicadores: un usuario entusiasta convence a diez escépticos mejor que diez emails corporativos. Los frameworks reconocidos ahorran años de trabajo: no reinventéis la rueda, adaptad lo que ya funciona. El apoyo externo compensa carencias internas: un consultor experimentado acelera meses el proceso. Medir ROI: "hemos reducido el tiempo de resolución de incidentes de 48h a 6h, ahorrando X horas/persona al año". Sed resilientes: el primer proyecto se retrasará, surgirán resistencias, aparecerán crisis que desvíen recursos; esto es normal, ajustad y continuad.

---

## 14. Conclusión y próximos pasos


### 14.1. Resumen clave

* El **PDS es la hoja de ruta** para gestionar sistemáticamente la ciberseguridad.
* Proceso estructurado en **6 fases** que forman un ciclo continuo.
* Requiere **análisis riguroso** de situación actual, estrategia y riesgos.
* Debe **alinearse con objetivos de negocio** y contar con apoyo de dirección.
* Es un **proceso de mejora continua**, no un proyecto con fin.
* **Proteger la información es proteger el negocio**.

Note: El PDS transforma la seguridad de reactiva a proactiva, de caótica a ordenada, de intuitiva a basada en evidencias. No es un lujo para grandes corporaciones: cualquier organización que dependa de tecnología (es decir, todas) necesita un PDS adaptado a su tamaño y realidad. El mensaje clave para los estudiantes: la seguridad no es solo tecnología, es estrategia de negocio. Como futuros profesionales, debéis entender cómo construir, ejecutar y mantener un PDS, o al menos participar efectivamente en él.


### 14.2. Beneficios tangibles del PDS

Beneficios claros para la organización:

* **Reducción medible del riesgo** y exposición a amenazas.
* **Cumplimiento normativo** (RGPD, ENS...) reduciendo multas.
* **Mejora de la reputación** ante clientes, partners, inversores.
* **Continuidad del negocio** asegurada ante incidentes.
* **Optimización de inversiones** en seguridad (priorización).
* **Cultura de seguridad** organizacional fortalecida.
* **Ventaja competitiva**: certificaciones, confianza del mercado.

Note: Estos beneficios justifican la inversión en PDS. La reducción de riesgo es el core: menos probabilidad de incidentes paralizantes. El cumplimiento evita multas millonarias y permite operar legalmente. La reputación importa: cada vez más clientes exigen garantías de seguridad, las certificaciones ISO 27001 abren puertas comerciales. La continuidad garantiza que un incidente no hunda la empresa. La optimización evita desperdiciar dinero en soluciones inefectivas. La cultura de seguridad convierte a los empleados en primera línea de defensa. La ventaja competitiva: en licitaciones públicas y contratos B2B, la seguridad demostrada es diferenciador.


### 14.3. Vuestros próximos pasos

**Para aplicar lo aprendido:**

1. **Elegid una organización** (real o ficticia) para un ejercicio práctico.
2. **Definid el alcance** inicial del PDS (empezad pequeño).
3. **Realizad un inventario** básico de activos críticos.
4. **Ejecutad un análisis de riesgos** simplificado (top 5-10 riesgos).
5. **Proponed 5-10 proyectos** priorizados (incluid quick wins).
6. **Preparad una presentación ejecutiva** (10 slides) para "dirección".
7. **Defended vuestra propuesta** ante compañeros.

Note: La mejor forma de aprender PDS es haciéndolo. Este ejercicio simula el proceso completo en versión reducida. Podéis usar empresas donde habéis trabajado/practicado, o inventar una: "Clínica dental con 20 empleados, 15k pacientes en BBDD, web de citas online". Definid alcance: "solo sistemas informáticos corporativos, no equipamiento médico". Inventario: servidor BBDD, web, equipos administrativos, backup NAS. Riesgos: ransomware, fuga datos pacientes RGPD, caída web. Proyectos: probar backups, MFA, cifrado BBDD, política RGPD, formación. Presentación: contexto, riesgos, propuesta, presupuesto, cronograma. Defended: preparaos para preguntas como "¿por qué es prioritario?" o "¿y si lo dejamos para el año que viene?". Este ejercicio desarrolla las habilidades que necesitaréis profesionalmente.

---

## Bibliografía y recursos


### Referencias principales

Recursos clave para profundizar en el PDS:

* **INCIBE** - [Guía del Plan Director de Seguridad](https://www.incibe.es)
* **ISO/IEC 27001:2022** - Sistemas de Gestión de Seguridad de la Información
* **ISO/IEC 27002:2022** - Código de buenas prácticas para controles de seguridad
* **CCN-CERT** - Guías de Seguridad CCN-STIC (Centro Criptológico Nacional)
* **NIST Cybersecurity Framework** - Marco de ciberseguridad (EE.UU.)
* **ENS** - Esquema Nacional de Seguridad (Real Decreto 311/2022)

Note: Estos son los recursos de referencia para profundizar. La guía de INCIBE es especialmente valiosa: documento gratuito de ~100 páginas con metodología completa y plantillas. ISO 27001 es el estándar internacional de SGSI, la versión 2022 simplifica y actualiza la de 2013. ISO 27002 lista 93 controles de seguridad organizados en 4 pilares. Las guías CCN-STIC del Centro Criptológico Nacional español son excelentes y gratuitas. El NIST CSF es muy usado en sectores regulados (finanzas, energía). El ENS es obligatorio para administraciones públicas españolas pero aplicable a cualquier organización.


### Recursos adicionales

Recursos útiles para justificar inversiones y mantenerse actualizado:

* **Verizon Data Breach Investigations Report (DBIR)** - Estadísticas anuales de brechas
* **IBM Cost of a Data Breach Report** - Análisis de costes de incidentes
* **ENISA Threat Landscape** - Panorama de amenazas europeo
* **OWASP** - Guías de seguridad en aplicaciones web
* **CIS Controls** - Controles críticos de seguridad priorizados
* **SANS Institute** - Formación y recursos de ciberseguridad

Note: Estos recursos complementarios aportan datos para justificar inversiones y mantenerse actualizado. El Verizon DBIR analiza miles de brechas anuales identificando patrones: "el 74% involucra el factor humano". El IBM Cost Report quantifica: "coste medio de una brecha 4.45M$ en 2023". ENISA Threat Landscape identifica amenazas emergentes en Europa. OWASP proporciona guías técnicas para desarrollo seguro. CIS Controls prioriza 18 controles en orden de efectividad: ideal para organizaciones pequeñas que no saben por dónde empezar. SANS ofrece formación de calidad y investigación.

---

## ¡Gracias!

### Contacto y recursos

* **Documentación del curso**: disponible en el repositorio del módulo
* **Prácticas**: ejercicio completo de diseño de PDS en grupos
* **Tutorías**: consultas sobre vuestros casos prácticos

**¿Preguntas?**

Note: Reforzad que la seguridad es un viaje, no un destino. Animadlos a explorar los recursos, a probar herramientas en entornos de lab, a seguir actualiz ándose (blogs, podcasts, conferencias como RootedCON). Recordad que muchos empezaréis vuestra carrera profesional participando en PDS de organizaciones reales: este conocimiento es directamente aplicable y valorado por employers. La certificación ISO 27001 Lead Implementer o Lead Auditor es un gran complemento profesional. Mantened una actitud de aprendizaje continuo: las amenazas evolucionan, las tecnologías cambian, pero los principios del PDS (conocer, planificar, ejecutar, medir, mejorar) permanecen.

