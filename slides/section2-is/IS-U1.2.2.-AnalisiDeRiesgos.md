# U1.2.2 - Análisis de Riesgos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Introducción al análisis de riesgos


### 1.1. ¿Qué es el análisis de riesgos?

**Proceso fundamental** para identificar, evaluar y priorizar riesgos.

**Permite:**
* Identificar activos más valiosos.
* Conocer amenazas a las que están expuestos.
* Detectar vulnerabilidades explotables.
* Tomar decisiones informadas sobre mitigación.

Note: El análisis de riesgos es como un examen médico completo de la organización. Sin él, estás operando a ciegas sobre qué proteger y cómo.


### 1.2. Importancia en el PDS

El análisis de riesgos es **uno de los trabajos más importantes** para definir proyectos e iniciativas de seguridad.

**Función:**
* Base del Plan Director de Seguridad.
* Centrar foco en riesgos críticos.
* Reducir posibilidad de incidentes.
* Priorizar inversiones en seguridad.

Note: Sin un buen análisis de riesgos, el PDS sería como disparar a ciegas. No sabríamos dónde invertir los recursos limitados de seguridad.


### 1.3. Beneficios del análisis

**Ventajas para la organización:**

* Visibilidad completa de riesgos.
* Priorización basada en datos.
* Justificación de inversiones en seguridad.
* Cumplimiento normativo facilitado.
* Mejora continua de postura de seguridad.

Note: El análisis de riesgos no solo protege, también ahorra dinero al prevenir incidentes y optimizar inversiones en controles.

---

## 2. Fases del análisis de riesgos


### 2.1. Visión general de las 6 fases

Proceso estructurado:

1. **Definir el alcance**
2. **Identificar activos**
3. **Identificar amenazas**
4. **Identificar vulnerabilidades**
5. **Evaluar el riesgo**
6. **Tratar el riesgo**

Note: Estas 6 fases son comunes en la mayoría de metodologías. Aprenderlas os permitirá aplicar cualquier framework de análisis de riesgos.


### 2.2. Metodologías existentes

Principales metodologías:

* **MAGERIT** (Metodología de Análisis y Gestión de Riesgos)
* **ISO 27005** (Gestión de riesgos en seguridad)
* **NIST SP 800-30** (Guide for Conducting Risk Assessments)
* **OCTAVE** (Operationally Critical Threat, Asset, and Vulnerability Evaluation)

Note: MAGERIT es la metodología española oficial y la más utilizada en administraciones públicas españolas. ISO 27005 es el estándar internacional.

---

## 3. Fase 1: Definir el alcance


### 3.1. ¿Qué es el alcance?

**Establecer límites** del estudio de riesgos.

**Definir:**
* Áreas estratégicas a analizar.
* Departamentos incluidos.
* Procesos críticos.
* Sistemas y activos en scope.

Note: No podéis analizar todo a la vez. Definir el alcance os permite concentrar esfuerzos donde más impacto tendréis.


### 3.2. Opciones de alcance

**Alcances posibles:**

* **Total**: Toda la organización (ideal, pero costoso).
* **Por departamento**: Ej. Departamento de Administración.
* **Por proceso**: Ej. Proceso de producción y almacén.
* **Por sistema**: Ej. Sistemas relacionados con página web.

Note: Para vuestros primeros análisis, empezad con un alcance limitado. Mejor un análisis profundo de un área que un análisis superficial de todo.


### 3.3. Factores para definir alcance

**Consideraciones clave:**

* Criticidad para el negocio.
* Recursos disponibles (tiempo, presupuesto, personal).
* Complejidad técnica.
* Requisitos normativos.
* Incidentes previos en el área.

Note: Si un área ha sufrido incidentes recientes o contiene datos muy sensibles, debe priorizarse en el alcance.


### 3.4. Ejemplo práctico

**Caso de estudio:**

Alcance definido: "Servicios y sistemas del Departamento de Informática"

**Incluye:**
* Servidores del CPD.
* Red corporativa.
* Sistemas de backup.
* Accesos remotos.

**Excluye:**
* Sistemas de producción industrial.
* Red de oficinas regionales.

Note: La claridad en el alcance evita malentendidos. Documentad qué está incluido Y qué está excluido explícitamente.

---

## 4. Fase 2: Identificar activos


### 4.1. ¿Qué son los activos?

**Activos**: Elementos de valor para la organización que deben protegerse.

**Tipos principales:**
* Hardware (servidores, equipos).
* Software (aplicaciones, sistemas).
* Datos (bases de datos, documentos).
* Personas (conocimiento, habilidades).
* Servicios (aplicaciones web, email).

Note: Un activo es todo aquello cuya pérdida o compromiso afectaría negativamente a la organización.


### 4.2. Inventario de activos I

**Creación del inventario:**

* Usar hoja de cálculo o herramienta especializada.
* Incluir información relevante de cada activo.
* Clasificar por tipo y criticidad.
* Identificar propietario/responsable.

Note: No podéis proteger lo que no conocéis. El inventario es la piedra angular del análisis de riesgos.


### 4.3. Inventario de activos II

**Información a recopilar:**

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| ID | Identificador único | SRV-001 |
| Nombre | Denominación | Servidor Web Principal |
| Tipo | Categoría | Hardware |
| Ubicación | Localización física | CPD Principal |
| Propietario | Responsable | Jefe IT |

Note: Cuanto más detallado el inventario, mejor será el análisis posterior. Pero no os perdáis en detalles irrelevantes.


### 4.4. Valoración de activos

**Criterios de valoración:**

* **Valor económico**: Coste de reposición.
* **Valor para el negocio**: Impacto si se pierde.
* **Valor estratégico**: Ventaja competitiva.
* **Valor legal**: Cumplimiento normativo.

Note: Un servidor de 1000€ que aloja la base de datos de clientes puede tener un valor para el negocio de millones de euros.

---

## 5. Fase 3: Identificar amenazas


### 5.1. ¿Qué son las amenazas?

**Amenaza**: Evento o acción que puede causar daño a un activo.

**Categorías:**
* **Naturales**: Incendios, inundaciones, terremotos.
* **Humanas**: Ataques, errores, sabotaje.
* **Técnicas**: Fallos hardware, bugs software.

Note: Las amenazas son potenciales. Pueden materializarse o no, pero debemos estar preparados para ellas.


### 5.2. Fuentes de amenazas

**Origen de las amenazas:**

* **Externas**: Hackers, competencia, desastres naturales.
* **Internas**: Empleados descontentos, errores humanos.
* **Ambientales**: Condiciones físicas adversas.

Note: Las estadísticas muestran que las amenazas internas causan tantos o más daños que las externas. No os centréis solo en hackers externos.


### 5.3. Catálogos de amenazas I

**Recursos para identificar amenazas:**

* **MAGERIT**: Catálogo completo de amenazas.
* **ISO 27005**: Lista de amenazas típicas.
* **CCN-CERT**: Amenazas actuales y emergentes.
* **Experiencia propia**: Incidentes previos.

Note: No reinventéis la rueda. Usad catálogos existentes como punto de partida y adaptadlos a vuestra realidad.


### 5.4. Catálogos de amenazas II

**Ejemplos de amenazas del catálogo MAGERIT:**

* **[N.1]** Fuego
* **[N.2]** Daños por agua
* **[I.5]** Avería de origen físico o lógico
* **[I.7]** Condiciones inadecuadas de temperatura
* **[E.1]** Errores de usuarios
* **[E.2]** Errores del administrador
* **[A.5]** Suplantación de identidad

Note: MAGERIT usa codificación: N=Natural, I=Industrial, E=Errores, A=Ataques. Familiarizaos con este catálogo, es estándar en España.


### 5.5. Asociación amenazas-activos

**Matriz amenazas-activos:**

* No todas las amenazas aplican a todos los activos.
* Un servidor tiene amenazas diferentes a un documento.
* Documentar qué amenazas afectan a cada activo.

**Ejemplo:**
* Servidor → Amenazas: Fallo hardware, ataque DDoS, robo.
* Documento confidencial → Amenazas: Fuga, acceso no autorizado.

Note: Sed eficientes. No perdáis tiempo analizando amenazas que claramente no aplican a un activo específico.

---

## 6. Fase 4: Identificar vulnerabilidades


### 6.1. ¿Qué son las vulnerabilidades?

**Vulnerabilidad**: Debilidad que puede ser explotada por una amenaza.

**Características:**
* Facilitan la materialización de amenazas.
* Pueden ser técnicas u organizativas.
* Reducen la efectividad de las salvaguardas.

Note: Una amenaza sin vulnerabilidad que explotar es menos peligrosa. Es como un ladrón sin puerta o ventana por donde entrar.


### 6.2. Tipos de vulnerabilidades

**Clasificación:**

* **Técnicas**: Software desactualizado, configuraciones inseguras.
* **Físicas**: Falta de control de acceso, climatización inadecuada.
* **Organizativas**: Procedimientos inexistentes, falta de formación.
* **Humanas**: Personal no concienciado, falta de supervisión.

Note: Las vulnerabilidades técnicas son las más obvias, pero las organizativas y humanas suelen ser las más explotadas.


### 6.3. Identificación de vulnerabilidades

**Métodos:**

* **Auditorías técnicas**: Escaneo de vulnerabilidades.
* **Revisión de configuraciones**: Hardening checks.
* **Entrevistas**: Conocer procedimientos reales.
* **Observación**: Verificar cumplimiento de políticas.
* **Pentesting**: Pruebas de penetración.

Note: No confiéis solo en herramientas automáticas. Las entrevistas y observación revelan vulnerabilidades organizativas que ningún escáner detectará.


### 6.4. Salvaguardas existentes

**Identificar controles implementados:**

* **Preventivos**: Firewall, control de acceso.
* **Detectivos**: IDS, logs, monitorización.
* **Correctivos**: Backups, procedimientos de recuperación.

**Importante:** Las salvaguardas reducen probabilidad o impacto.

Note: Documentad las salvaguardas existentes. Afectan directamente al cálculo del riesgo en la fase siguiente.


### 6.5. Ejemplo práctico

**Caso: Servidor de base de datos**

**Vulnerabilidades identificadas:**
* Sistema operativo con 3 meses sin actualizar.
* Contraseña de admin débil.
* Sin backup automático configurado.

**Salvaguardas:**
* Firewall filtrando acceso al puerto.
* Logs de acceso activados.

Note: Este servidor tiene múltiples vulnerabilidades pero algunas salvaguardas que reducen el riesgo. El análisis debe considerar ambos factores.

---

## 7. Fase 5: Evaluar el riesgo I


### 7.1. ¿Qué es el riesgo?

**Riesgo**: Probabilidad de que una amenaza se materialice y el impacto que causaría.

**Fórmula básica:**
```
RIESGO = PROBABILIDAD × IMPACTO
```

Note: El riesgo combina dos dimensiones: qué tan probable es que ocurra algo malo, y qué tan malo sería si ocurre.


### 7.2. Enfoques de evaluación

**Dos aproximaciones:**

* **Cualitativo**: Usa escalas descriptivas (Bajo, Medio, Alto).
* **Cuantitativo**: Usa valores numéricos (1-5, 1-10, monetarios).

**Ventajas cualitativo:** Más rápido, más intuitivo.
**Ventajas cuantitativo:** Más preciso, permite análisis ROI.

Note: Para vuestros primeros análisis, el enfoque cualitativo es más práctico. El cuantitativo requiere datos históricos precisos.


### 7.3. Escala de probabilidad

**Ejemplo de escala cualitativa:**

| Nivel | Descripción | Frecuencia |
|-------|-------------|-----------|
| Muy Baja | Casi imposible | < 1 vez cada 10 años |
| Baja | Improbable | 1 vez cada 5-10 años |
| Media | Posible | 1 vez cada 1-5 años |
| Alta | Probable | Varias veces al año |
| Muy Alta | Casi seguro | Mensual o más |

Note: Estas frecuencias son orientativas. Adaptadlas a vuestra realidad organizacional.


### 7.4. Escala de impacto

**Ejemplo de escala cualitativa:**

| Nivel | Descripción | Efecto |
|-------|-------------|--------|
| Muy Bajo | Mínimo | Molestia menor |
| Bajo | Limitado | Afecta un departamento |
| Medio | Importante | Afecta varios departamentos |
| Alto | Grave | Afecta toda la organización |
| Muy Alto | Catastrófico | Puede cerrar la empresa |

Note: El impacto debe considerar múltiples dimensiones: económico, reputacional, legal, operacional.

---

## 8. Fase 5: Evaluar el riesgo II


### 8.1. Matriz de riesgo

**Herramienta visual** para calcular riesgo:

|  | Muy Baja | Baja | Media | Alta | Muy Alta |
|---|---|---|---|---|---|
| **Muy Alto** | Medio | Alto | Alto | Muy Alto | Muy Alto |
| **Alto** | Bajo | Medio | Alto | Alto | Muy Alto |
| **Medio** | Bajo | Bajo | Medio | Alto | Alto |
| **Bajo** | Muy Bajo | Bajo | Bajo | Medio | Alto |
| **Muy Bajo** | Muy Bajo | Muy Bajo | Bajo | Medio | Medio |

Note: Esta matriz cruza probabilidad (columnas) con impacto (filas). El resultado es el nivel de riesgo.


### 8.2. Interpretación de resultados

**Niveles de riesgo:**

* **Muy Bajo/Bajo**: Aceptable, monitorizar.
* **Medio**: Requiere atención, planificar mitigación.
* **Alto**: Acción requerida pronto.
* **Muy Alto**: Acción inmediata necesaria.

Note: Estos umbrales son decisiones de negocio. La dirección debe aprobarlos según apetito de riesgo de la organización.


### 8.3. Factores que modifican el riesgo

**Ajustes al cálculo:**

* **Vulnerabilidades presentes**: Aumentan probabilidad/impacto.
* **Salvaguardas existentes**: Reducen probabilidad/impacto.

**Ejemplo:**
* Riesgo base: Alto
* + Vulnerabilidad (sistema sin parchear): Muy Alto
* - Salvaguarda (backup diario): Alto

Note: El riesgo no es estático. Cambia según las medidas que implementéis o las vulnerabilidades que se descubran.


### 8.4. Ejemplo completo

**Caso: Caída del servidor principal**

* **Probabilidad base**: Media (fallo hardware cada 3 años)
* **Impacto base**: Alto (para toda operación 2 días)
* **Vulnerabilidad**: Mantenimiento no realizado (+1 nivel prob.)
* **Salvaguarda**: Servidor redundado (-2 niveles impacto)
* **Probabilidad final**: Alta
* **Impacto final**: Medio
* **Riesgo resultante**: Alto

Note: Este ejemplo muestra cómo las vulnerabilidades y salvaguardas modifican el cálculo del riesgo base.

---

## 9. Fase 6: Tratar el riesgo


### 9.1. Estrategias de tratamiento

**4 opciones principales:**

1. **Mitigar**: Reducir probabilidad o impacto.
2. **Transferir**: Trasladar a tercero (seguros).
3. **Evitar**: Eliminar la actividad que genera riesgo.
4. **Aceptar**: Asumir el riesgo conscientemente.

Note: No todos los riesgos deben mitigarse. A veces es más económico aceptarlos o transferirlos.


### 9.2. Mitigar el riesgo

**Implementar controles** para reducir riesgo:

* **Reducir probabilidad**: Parches, formación, controles preventivos.
* **Reducir impacto**: Backups, redundancia, planes de contingencia.

**Ejemplo:**
* Riesgo: Ransomware en estaciones de trabajo.
* Mitigación: Antivirus + formación anti-phishing + backups.

Note: La mitigación es la estrategia más común. Casi siempre combina múltiples controles trabajando juntos.


### 9.3. Transferir el riesgo

**Trasladar responsabilidad** a tercero:

* **Seguros de ciberseguridad**: Cubren daños por incidentes.
* **Contratos con proveedores**: SLAs con penalizaciones.
* **Outsourcing**: Delegar servicios a especialistas.

**Ejemplo:** Contratar seguro que cubra hasta 1M€ en caso de fuga de datos.

Note: Transferir no elimina el riesgo, solo traslada las consecuencias financieras. El daño reputacional sigue siendo vuestro.


### 9.4. Evitar el riesgo

**Eliminar la actividad** que genera el riesgo:

* Dejar de ofrecer un servicio vulnerable.
* No almacenar ciertos tipos de datos.
* Discontinuar sistemas legacy inseguros.

**Ejemplo:** Eliminar WiFi pública de cortesía para clientes si no es crítica.

Note: Evitar es la opción más radical. Solo tiene sentido cuando el coste de mitigar supera ampliamente el beneficio de la actividad.


### 9.5. Aceptar el riesgo

**Asumir conscientemente** el riesgo:

* Cuando coste de mitigación > valor del activo.
* Cuando probabilidad es extremadamente baja.
* Requiere **aprobación formal** de dirección.

**Ejemplo:** No instalar grupo electrógeno si coste (50K€) > pérdidas esperadas (5K€/año).

Note: Aceptar un riesgo debe ser decisión documentada y aprobada por quien tenga autoridad para hacerlo, nunca decisión técnica unilateral.


### 9.6. Plan de tratamiento

**Documentar decisiones:**

Para cada riesgo alto/muy alto:

* Estrategia elegida (mitigar/transferir/evitar/aceptar).
* Controles a implementar.
* Responsable de implementación.
* Plazo de ejecución.
* Presupuesto necesario.

Note: El plan de tratamiento es el entregable principal del análisis de riesgos. Es lo que se lleva a la dirección para aprobación y ejecución.

---

## 10. Integración con el PDS


### 10.1. Del análisis al PDS

**Flujo de trabajo:**

1. Análisis de riesgos identifica controles necesarios.
2. Controles se convierten en **proyectos del PDS**.
3. Proyectos se priorizan y presupuestan.
4. Se implementan según plan.
5. Se revisa efectividad.

Note: El análisis de riesgos alimenta el PDS, que a su vez ejecuta las acciones para reducir los riesgos identificados.


### 10.2. Priorización de proyectos

**Criterios de priorización:**

* **Riesgo que mitiga**: Riesgos altos primero.
* **Coste/beneficio**: ROI del control.
* **Facilidad de implementación**: Quick wins.
* **Dependencias**: Prerequisitos técnicos u organizativos.

Note: Los quick wins (bajo coste, alto impacto) generan momentum inicial y demuestran valor rápido a la dirección.


### 10.3. Revisión continua

**El análisis de riesgos no es estático:**

* Nuevas amenazas emergen constantemente.
* Activos cambian (nuevos sistemas, servicios).
* Vulnerabilidades se descubren.
* Controles pueden quedar obsoletos.

**Recomendación:** Revisar anualmente como mínimo.

Note: Un análisis de riesgos de hace 3 años probablemente no contempla amenazas actuales como ransomware as a service o ataques a supply chain.

---

## 11. Herramientas y metodologías


### 11.1. MAGERIT

**Metodología española de referencia:**

* Desarrollada por CCN (Centro Criptológico Nacional).
* Gratuita y completa.
* Incluye catálogos de activos, amenazas y salvaguardas.
* Herramienta PILAR para análisis.

Note: MAGERIT es obligatoria en administraciones públicas españolas. Conocerla os abrirá muchas puertas profesionales.


### 11.2. ISO 27005

**Estándar internacional:**

* Parte de familia ISO 27000.
* Compatible con ISO 27001.
* Enfoque más genérico que MAGERIT.
* Reconocido mundialmente.

Note: ISO 27005 es el estándar que empresas multinacionales suelen seguir. Complementa perfectamente a ISO 27001.


### 11.3. Herramientas software

**Opciones populares:**

* **PILAR**: Herramienta oficial de MAGERIT.
* **CRAMM**: Risk Analysis and Management Method.
* **RiskWatch**: Análisis cuantitativo.
* **Hojas de cálculo**: Para análisis sencillos.

Note: Para empezar, una hoja de cálculo bien diseñada puede ser suficiente. Las herramientas especializadas aportan valor en análisis complejos.

---

## 12. Conclusión


### 12.1. Resumen de conceptos clave

* **Análisis de riesgos**: Identificar, evaluar, priorizar y tratar riesgos.
* **6 fases**: Alcance, activos, amenazas, vulnerabilidades, evaluación, tratamiento.
* **Fórmula base**: Riesgo = Probabilidad × Impacto.
* **4 estrategias**: Mitigar, transferir, evitar, aceptar.
* **Integración**: Alimenta el Plan Director de Seguridad.

Note: El análisis de riesgos es ciencia y arte. La ciencia está en la metodología, el arte en interpretar resultados y tomar decisiones.


### 12.2. Errores comunes a evitar

**Top 5 errores:**

1. Alcance demasiado ambicioso (intentar analizar todo).
2. Inventario de activos incompleto o desactualizado.
3. Confiar solo en catálogos, ignorar amenazas específicas.
4. Análisis una sola vez (no revisar periódicamente).
5. No involucrar a la dirección en decisiones de aceptación.

Note: El error más común es hacer el análisis y dejarlo en un cajón. El valor está en ejecutar el plan de tratamiento.


### 12.3. Habilidades a desarrollar

Para alumnos y alumnas:

* **Pensamiento analítico**: Descomponer problemas complejos.
* **Conocimiento técnico**: Entender sistemas y amenazas.
* **Comunicación**: Explicar riesgos a no-técnicos.
* **Negociación**: Convencer para asignación de recursos.
* **Actualización continua**: Amenazas evolucionan constantemente.

Note: Los mejores analistas de riesgos combinan habilidades técnicas con comprensión del negocio. No os quedéis solo en lo técnico.


### 12.4. Próximos pasos

Práctica recomendada:

1. Leer metodología MAGERIT completa.
2. Practicar con caso real (vuestra universidad/hogar).
3. Usar herramienta PILAR en ejercicio guiado.
4. Estudiar análisis de riesgos de organizaciones públicas.
5. Participar en ejercicios de mesa de crisis.

Note: Montad un análisis de riesgos de vuestro entorno familiar. Es excelente práctica y mejorará vuestra seguridad personal.

---

## Bibliografía

* [MAGERIT v3](https://www.ccn-cert.cni.es/series-ccn-stic/800-guia-esquema-nacional-de-seguridad/988-ccn-stic-817-gestion-de-ciberincidentes/file.html) - Metodología de Análisis y Gestión de Riesgos
* [ISO/IEC 27005](https://www.iso.org/standard/75281.html) - Information security risk management
* [NIST SP 800-30](https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final) - Guide for Conducting Risk Assessments
* [INCIBE - Gestión de Riesgos](https://www.incibe.es/empresas/guias/gestion-riesgos-guia-empresario)

Note: MAGERIT es lectura obligatoria y está disponible gratuitamente. Dedicad tiempo a estudiarla en profundidad.
