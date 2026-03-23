# U2.2.1 - Detección de Incidentes

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Indicios de incidentes


### 1.1. Tipos de indicios

Dos fuentes principales de indicios:

* **Precursores**: Indicios de que puede ocurrir un incidente en el futuro.
* **Indicadores**: Indicios de que un incidente puede haber ocurrido o está ocurriendo ahora.

Note: Los alumnos y alumnas deben entender que detectar precursores permite actuar proactivamente, mientras que los indicadores requieren respuesta reactiva inmediata.


### 1.2. Precursores - Definición

Un **precursor** es una señal de alerta temprana que indica que podría producirse un incidente.

**Características:**
* Son preventivos
* Permiten preparación anticipada
* No indican que el ataque esté en curso
* Tiempo para implementar contramedidas

Note: Los precursores son como las nubes oscuras antes de la tormenta. Verlas nos da tiempo para prepararnos.


### 1.3. Precursores - Ejemplos

Ejemplos típicos de precursores:

* Logs del servidor web con resultados de **escáneres de vulnerabilidades**.
* Anuncio de **nuevo exploit** para vulnerabilidad presente en nuestros sistemas.
* **Amenazas explícitas** de grupos organizados contra la organización.
* Incremento de **actividad de reconnaissance** en el perímetro.

Note: Si detectamos un escaneo, sabemos que alguien está estudiando nuestras defensas. Es el momento de reforzarlas antes del ataque real.


### 1.4. Indicadores - Definición

Un **indicador** es evidencia de que un incidente está ocurriendo o ya ha ocurrido.

**Características:**
* Son reactivos
* Requieren respuesta inmediata
* Indican compromiso activo o reciente
* Necesitan investigación forense

Note: Los indicadores son como encontrar la puerta forzada. El intruso puede estar dentro o ya haberse ido, pero el daño puede estar hecho.


### 1.5. Indicadores - Ejemplos I

Indicadores técnicos comunes:

* **Sensor IDS/IPS** emitiendo alerta de intento de desbordamiento de búfer.
* **Alertas de antivirus** detectando malware.
* **Nombres de archivo** con caracteres inusuales o sospechosos.
* **Cambios no previstos** en configuración de hosts.

Note: Estos son los indicadores más comunes que veréis en vuestro trabajo diario como analistas de seguridad.


### 1.6. Indicadores - Ejemplos II

Más indicadores a monitorizar:

* **Intentos fallidos** de login repetidos desde sistemas desconocidos.
* **Correos electrónicos rebotados** con contenido sospechoso en masa.
* **Desviación inusual** del tráfico de red interna.
* **Procesos** o servicios desconocidos en ejecución.

Note: La clave es conocer qué es "normal" en vuestra red para detectar lo "anormal". El análisis de baseline es fundamental.

---

## 2. Centro de Operaciones de Seguridad (SOC)


### 2.1. Definición de SOC

**SOC (Security Operations Center)**: Equipo responsable de garantizar la seguridad de la información.

**Función principal:**
* Supervisión y administración de seguridad del sistema de información.
* Herramientas de recogida y correlación de eventos.
* Intervención remota cuando es necesario.

Note: El SOC es el "cuartel general" de la ciberseguridad en una organización. Funciona 24/7 monitorizando y respondiendo a amenazas.


### 2.2. Objetivo del SOC

Objetivos principales:

* **Detectar** incidentes de ciberseguridad.
* **Analizar** actividad en redes, servidores, terminales.
* **Corregir** incidentes utilizando soluciones tecnológicas.
* **Garantizar** respuesta adecuada a incidentes.

Note: Un SOC bien organizado reduce el tiempo de detección y respuesta de meses a horas o incluso minutos.


### 2.3. Funcionamiento del SOC I

**Estrategia integrada:**
* Integrar objetivos de cada departamento.
* Definir infraestructura necesaria de seguridad.
* Implementar cortafuegos, IPS/IDS, soluciones de detección.
* Sistema de gestión de eventos (SIEM).

Note: El SOC no es solo herramientas, es un enfoque estratégico que requiere coordinación entre todos los departamentos.


### 2.4. Funcionamiento del SOC II

**Operativa continua:**
* Tecnología de **recolección y agregación** de información.
* Supervisión de **vulnerabilidades** de red y endpoints.
* Flujos de datos, mediciones, logs, syslog.
* **Monitorización 24/7** de eventos de seguridad.

Note: La correlación de eventos de múltiples fuentes es lo que convierte datos aislados en inteligencia accionable.


### 2.5. Organización del SOC

Niveles de especialización:

* **Nivel 1 - Analistas de alertas**: Monitorizan y escalan.
* **Nivel 2 - Analistas de respuesta**: Evalúan impacto y recomiendan acciones.
* **Nivel 3 - Expertos**: Resuelven incidentes complejos y previenen recurrencia.

Note: Esta estructura permite eficiencia. Los casos simples se resuelven rápido en Nivel 1, los complejos llegan a expertos de Nivel 3.


### 2.6. SOC vs CERT/CSIRT/CIRT

Diferencias fundamentales:

* **SOC**: Operaciones completas de seguridad (proactivo y reactivo).
* **CERT**: Computer Emergency Response Team (foco en emergencias).
* **CSIRT**: Computer Security Incident Response Team (respuesta a incidentes).
* **CIRT**: Computer Incident Response Team (similar a CSIRT).

Note: El SOC es el paraguas que cubre todo, mientras que CERT/CSIRT/CIRT son equipos especializados en respuesta. Pueden coexistir.


### 2.7. Enfoque de respuesta

Todos siguen las 4 fases del NIST:

1. **Preparación**: Políticas, procedimientos, herramientas.
2. **Detección y Análisis**: Identificar y evaluar incidentes.
3. **Contención, Erradicación y Recuperación**: Limitar daño y restaurar.
4. **Post-incidente**: Lecciones aprendidas y mejoras.

Note: Esta metodología del NIST es estándar internacional. Aprenderla os permitirá trabajar en cualquier organización del mundo.

---

## 3. Sistemas de detección I


### 3.1. IDS - Intrusion Detection System

**Sistema de Detección de Intrusiones:**

* **Función**: Detectar accesos no autorizados a un ordenador o red.
* **Operación**: Monitoriza tráfico entrante.
* **Comparación**: Base de datos de firmas de ataque conocidas.
* **Respuesta**: Emite alertas a administradores.

Note: IDS es como un vigilante que observa pero no interviene directamente. Solo avisa cuando ve algo sospechoso.


### 3.2. IDS - Características

**Ventajas:**
* Detección de ataques conocidos.
* No interrumpe el tráfico legítimo.
* Útil para análisis forense.

**Limitaciones:**
* Solo detecta, no previene.
* Actuación reactiva.
* Requiere intervención humana.

Note: El IDS es fundamental para análisis post-incidente, pero no detiene el ataque en tiempo real.


### 3.3. Tipos de IDS

Clasificación según ubicación:

* **NIDS** (Network IDS): Monitoriza tráfico de red completo.
* **HIDS** (Host IDS): Monitoriza un sistema específico.
* **Híbridos**: Combinación de ambos enfoques.

Note: NIDS detecta ataques de red, HIDS detecta cambios locales en el sistema. Idealmente, se usan ambos para cobertura completa.

---

## 4. Sistemas de detección II


### 4.1. IPS - Intrusion Prevention System

**Sistema de Prevención de Intrusiones:**

* **Función**: Detectar Y bloquear accesos no autorizados.
* **Operación**: Análisis en tiempo real del tráfico.
* **Respuesta**: Bloqueo automático de amenazas.
* **Ubicación**: Inline en el flujo de red.

Note: IPS es como un vigilante que no solo observa, sino que también actúa para detener al intruso inmediatamente.


### 4.2. IPS - Características

**Ventajas:**
* Prevención activa de intrusiones.
* Respuesta automática e inmediata.
* Reduce carga de administradores.

**Limitaciones:**
* Falsos positivos pueden bloquear tráfico legítimo.
* Requiere afinación cuidadosa.
* Punto único de fallo potencial.

Note: El IPS debe calibrarse cuidadosamente. Un falso positivo puede bloquear servicios críticos del negocio.


### 4.3. IDS vs IPS - Comparativa

| Aspecto | IDS | IPS |
|---------|-----|-----|
| **Acción** | Detecta y alerta | Detecta y bloquea |
| **Ubicación** | Fuera del flujo | En el flujo (inline) |
| **Impacto** | No afecta tráfico | Puede bloquear tráfico |
| **Velocidad** | Análisis posterior | Tiempo real |

Note: La elección entre IDS e IPS depende de vuestras necesidades y tolerancia al riesgo de falsos positivos.


### 4.4. Métodos de detección

Técnicas utilizadas por IDS/IPS:

* **Basado en firmas**: Compara con patrones conocidos.
* **Basado en anomalías**: Detecta desviaciones del comportamiento normal.
* **Basado en políticas**: Verifica cumplimiento de reglas.
* **Híbrido**: Combinación de métodos anteriores.

Note: Los sistemas modernos suelen combinar múltiples métodos para mejor precisión y menor tasa de falsos positivos.

---

## 5. SIEM - Security Information and Event Management


### 5.1. Definición de SIEM

**SIEM**: Plataforma centralizada para gestión de seguridad.

**Funciones principales:**
* **Agregación** de logs de múltiples fuentes.
* **Correlación** de eventos para detectar patrones.
* **Alertas** en tiempo real sobre amenazas.
* **Análisis** forense e informes de compliance.

Note: El SIEM es el cerebro del SOC. Procesa miles de eventos por segundo para encontrar las agujas en el pajar.


### 5.2. Componentes del SIEM

Arquitectura típica:

* **Colectores**: Recopilan logs de dispositivos.
* **Agregadores**: Normalizan y centralizan datos.
* **Motor de correlación**: Analiza y relaciona eventos.
* **Almacenamiento**: Base de datos de eventos históricos.
* **Consola**: Interfaz para analistas.

Note: Cada componente es crítico. Sin buenos colectores, el SIEM no tiene datos. Sin correlación, solo tenemos ruido.


### 5.3. Fuentes de datos del SIEM I

Dispositivos de red:

* Firewalls y routers.
* Switches y balanceadores.
* IDS/IPS.
* Proxies y gateways.

Note: Cuantas más fuentes alimenten al SIEM, mejor visibilidad tendremos de lo que ocurre en la red.


### 5.4. Fuentes de datos del SIEM II

Sistemas y aplicaciones:

* Servidores (Windows, Linux).
* Bases de datos.
* Aplicaciones web.
* Sistemas de autenticación.
* Antivirus y EDR.

Note: La correlación entre eventos de red y de sistemas permite detectar ataques complejos multi-etapa.


### 5.5. Correlación de eventos

**Ejemplo de correlación:**

1. Firewall: Escaneo de puertos desde IP externa.
2. IDS: Intento de explotación de vulnerabilidad.
3. Servidor: Login exitoso con cuenta admin.
4. Antivirus: Detección de malware.

**SIEM correlaciona** → **Alerta: Compromiso de sistema**

Note: Individualmente, cada evento podría parecer menor. Correlacionados, revelan un ataque en progreso.


### 5.6. Casos de uso SIEM I

Detección de amenazas:

* **Accesos no autorizados**: Múltiples intentos fallidos seguidos de éxito.
* **Movimiento lateral**: Accesos inusuales entre sistemas.
* **Exfiltración de datos**: Transferencias grandes a destinos externos.
* **Malware**: Patrones de comportamiento malicioso.

Note: Estos casos de uso son configurables. Cada organización debe adaptar las reglas a sus necesidades específicas.


### 5.7. Casos de uso SIEM II

Compliance y auditoría:

* **PCI-DSS**: Monitorización de sistemas de pago.
* **GDPR**: Accesos a datos personales.
* **ISO 27001**: Gestión de incidentes.
* **HIPAA**: Protección datos sanitarios.

Note: El SIEM no es solo seguridad, es también cumplimiento normativo. Facilita enormemente las auditorías.


### 5.8. Beneficios del SIEM

Ventajas para la organización:

* **Visibilidad** centralizada de seguridad.
* **Detección rápida** de amenazas.
* **Reducción** de tiempo de respuesta.
* **Cumplimiento** regulatorio facilitado.
* **Análisis forense** post-incidente.

Note: El ROI de un SIEM se mide en reducción de daños por incidentes y ahorro en costes de compliance.


### 5.9. Desafíos del SIEM

Retos comunes:

* **Volumen de datos**: Miles de eventos por segundo.
* **Falsos positivos**: Requieren afinación constante.
* **Complejidad**: Curva de aprendizaje pronunciada.
* **Coste**: Licencias y hardware pueden ser costosos.
* **Mantenimiento**: Actualizaciones y ajustes continuos.

Note: Implementar un SIEM es un proyecto complejo. Requiere planificación, recursos y compromiso a largo plazo.

---

## 6. Indicadores de compromiso (IoC)


### 6.1. ¿Qué son los IoC?

**Indicators of Compromise**: Evidencias técnicas de que un sistema ha sido comprometido.

**Tipos comunes:**
* Hashes de archivos maliciosos.
* IPs o dominios maliciosos.
* URLs de C&C (Command and Control).
* Patrones de comportamiento.

Note: Los IoC son como las huellas dactilares del atacante. Permiten identificar si otros sistemas también están comprometidos.


### 6.2. Fuentes de IoC

Dónde obtener IoC:

* **Threat intelligence** comercial (Mandiant, CrowdStrike).
* **Feeds públicos** (AlienVault OTX, Abuse.ch).
* **Análisis propio** de incidentes.
* **Comunidades** de sharing (ISAC).
* **Organismos** gubernamentales (CCN-CERT, INCIBE).

Note: Compartir IoC entre organizaciones fortalece la seguridad de todos. El atacante que falla en una empresa puede intentarlo en la vuestra.


### 6.3. Uso de IoC en detección

Aplicación práctica:

* **Integración en IDS/IPS**: Bloqueo automático.
* **Búsqueda en SIEM**: Correlación histórica.
* **Análisis de endpoints**: Hunting proactivo.
* **Filtrado perimetral**: Bloqueo en firewall.

Note: Los IoC permiten detección reactiva rápida. Si otro sufrió el ataque, podéis prevenirlo en vuestra organización.


### 6.4. Threat Hunting

**Búsqueda proactiva** de amenazas:

* No esperar alertas automáticas.
* Usar IoC para buscar amenazas ocultas.
* Análisis de comportamientos anómalos.
* Hipótesis sobre posibles compromisos.

Note: Threat hunting es la evolución natural de la detección pasiva. Los mejores analistas no esperan alertas, las buscan activamente.

---

## 7. Conclusión


### 7.1. Resumen de conceptos

* **Indicios**: Precursores (preventivos) e Indicadores (reactivos).
* **SOC**: Centro de operaciones de seguridad 24/7.
* **IDS**: Detecta y alerta sobre intrusiones.
* **IPS**: Detecta y bloquea intrusiones.
* **SIEM**: Correlaciona eventos de múltiples fuentes.
* **IoC**: Indicadores técnicos de compromiso.

Note: Estos conceptos forman el ecosistema de detección moderno. Todos trabajan juntos para proteger la organización.


### 7.2. Defensa en profundidad

**Estrategia de capas:**

1. Prevención (Firewall, IPS)
2. Detección (IDS, SIEM)
3. Respuesta (SOC, CSIRT)
4. Análisis (IoC, Threat Hunting)

Ninguna capa es suficiente por sí sola.

Note: La defensa en profundidad asume que alguna capa fallará. Por eso necesitamos múltiples niveles de protección.


### 7.3. Habilidades necesarias

Para alumnos y alumnas:

* Análisis de logs y eventos.
* Comprensión de protocolos de red.
* Conocimiento de sistemas operativos.
* Capacidad de correlación.
* Pensamiento crítico y analítico.

Note: La tecnología es importante, pero el criterio humano es insustituible. Desarrollad vuestras habilidades de análisis.


### 7.4. Próximos pasos

1. Practicar con herramientas SIEM (Splunk, ELK).
2. Instalar y configurar IDS/IPS (Snort, Suricata).
3. Analizar logs reales de sistemas.
4. Participar en ejercicios de threat hunting.
5. Estudiar casos reales de incidentes.

Note: La práctica es fundamental. Montad un lab virtual y experimentad con estas herramientas.

---

## Bibliografía

* NIST SP 800-61 - Computer Security Incident Handling Guide
* SANS - Incident Handler's Handbook
* MITRE ATT&CK Framework
* CCN-CERT - Guías de detección y respuesta
* INCIBE - Recursos de ciberseguridad

Note: El NIST 800-61 y MITRE ATT&CK son lecturas obligatorias para cualquier profesional de detección de incidentes.
