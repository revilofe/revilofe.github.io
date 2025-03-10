Para explicar el criterio de evaluación "**Se han recopilado y almacenado de forma segura evidencias de incidentes de ciberseguridad que afectan a la organización**" a los alumnos, es fundamental detallar los procesos de **recopilación** y **almacenamiento seguro** de la evidencia digital. A continuación, se presenta el contenido que se podría impartir, basado en las fuentes proporcionadas:

**I. Recopilación de Evidencias de Incidentes de Ciberseguridad**

La recopilación de evidencias digitales en incidentes de ciberseguridad es un proceso crítico que debe realizarse siguiendo **principios forenses** para garantizar la **integridad**, **autenticidad** y **admisibilidad** de la evidencia. Es esencial que las acciones tomadas **no alteren los datos originales**.

**A. Fases de la Recopilación:**

1.  **Identificación de la Evidencia:**
    *   **Reconocimiento:** El primer paso es **reconocer e identificar** los posibles **dispositivos electrónicos** que puedan contener evidencia relevante para el incidente. Esto puede incluir ordenadores, servidores, dispositivos móviles, dispositivos de red, medios de almacenamiento extraíbles, etc..
    *   **Determinación de la Relevancia:** Es importante **establecer qué datos son probablemente relevantes y admisibles** para la investigación del incidente. En caso de duda, es mejor recopilar más información que menos.
    *   **Ubicación de la Evidencia:** Se debe **listar los sistemas involucrados** en el incidente y desde dónde se recopilará la evidencia.

2.  **Documentación de la Escena y la Evidencia:**
    *   **Documentación Continua:** La **documentación** es un proceso **continuo** durante toda la investigación.
    *   **Registro Detallado:** Se debe **registrar con precisión la ubicación y condición** de los equipos informáticos, medios de almacenamiento y otros dispositivos electrónicos. Esto incluye **fotografías y/o videos** de la escena y las pantallas.
    *   **Anotación de Acciones:** Se deben tomar **notas detalladas de todas las acciones** realizadas en relación con el equipo informático.
    *   **Etiquetado:** Todos los elementos deben tener **etiquetas de identificación firmadas**.
    *   **Información Adicional:** Recopilar cualquier **documentación** asociada al sistema (manuales, configuraciones), **contraseñas** encontradas (en notas, diarios) o proporcionadas por el usuario (si las circunstancias lo permiten), **claves de cifrado**, y **claves de seguridad**.

3.  **Preservación de la Integridad de la Evidencia durante la Recopilación:**
    *   **Fragilidad de la Evidencia:** Recordar que la evidencia electrónica es **frágil** y puede alterarse fácilmente.
    *   **No Modificar Datos:** Las acciones tomadas **no deben añadir, modificar o destruir** los datos almacenados.
    *   **Manejo Adecuado:** Manipular los dispositivos con **precaución** para evitar daños físicos, descargas electrostáticas, campos magnéticos y variaciones extremas de temperatura o humedad.
    *   **Consideración de Sistemas Encendidos vs. Apagados:**
        *   **Sistemas Apagados:** En general, si un sistema está apagado, **no encenderlo**; si está encendido, **no apagarlo** hasta evaluar la situación.
        *   **Sistemas Encendidos (Live Forensics):** Requiere **personal capacitado** para capturar información volátil (memoria RAM) antes de que se pierda al apagar el equipo. Se debe seguir un **orden de volatilidad** para la recopilación. Se deben **documentar cuidadosamente** los procesos realizados en sistemas encendidos, ya que pueden no ser totalmente reproducibles.
    *   **Aislamiento de Red:** Si el dispositivo está encendido y conectado a una red, considerar el **aislamiento de la red** para evitar acceso remoto o alteraciones.

4.  **Adquisición Técnica de la Evidencia:**
    *   **Creación de Copias Forenses:** Generalmente, el análisis se realiza sobre una **copia forense** del original para preservar la integridad de este último. Esto implica realizar un **clonado bit a bit** o una **imagen forense** del medio de almacenamiento.
    *   **Uso de Herramientas Forenses:** Utilizar **herramientas de hardware y software forenses reconocidas** que garanticen la integridad del proceso de adquisición.
    *   **Hash del Original y la Copia:** Calcular el **resumen digital (hash)** del medio original y de la copia para **verificar la integridad** de la copia. La coincidencia de los hashes garantiza que la copia es idéntica al original.
    *   **Protección contra Escritura:** Utilizar **dispositivos de bloqueo de escritura (write blockers)** para evitar modificaciones accidentales en el dispositivo original durante la adquisición.

5.  **Consideraciones Específicas para Diferentes Tipos de Evidencia:**
    *   **Dispositivos Móviles:** Pueden requerir un manejo especial para evitar la pérdida de datos o la alteración de la información de localización. Considerar el **aislamiento de redes inalámbricas** y la extracción de información de la **tarjeta SIM** y la **memoria interna**.
    *   **Redes:** El procesamiento de escenas con redes requiere **conocimiento especializado**. Documentar la **topología de la red** y **aislar los dispositivos** de forma controlada.
    *   **Entornos Virtualizados:** Requieren la **captura de los discos duros virtuales** y potencialmente volcados de memoria de las máquinas virtuales.

**B. Personal y Legal:**

*   **Personal Capacitado:** La recopilación y el manejo de evidencia digital deben ser realizados por **personal capacitado** en forense digital.
*   **Autoridad Legal:** Asegurarse de contar con la **autoridad legal necesaria** (por ejemplo, una orden judicial) para la búsqueda y decomiso de la evidencia.

**II. Almacenamiento Seguro de Evidencias de Incidentes de Ciberseguridad**

Una vez recopilada, la evidencia digital debe almacenarse de forma **segura** para **mantener su integridad**, **garantizar la cadena de custodia** y **prevenir el acceso no autorizado**, la **alteración** o la **pérdida**.

**A. Cadena de Custodia:**

*   **Documentación Detallada:** Establecer y mantener una **cadena de custodia clara y documentada** desde el momento del descubrimiento y la recopilación hasta la presentación final.
*   **Registro de Manipulación:** Documentar **quién, cuándo, dónde y cómo** se descubrió, recopiló, manejó, examinó, transfirió y almacenó la evidencia.
*   **Registro de Transferencias:** Registrar las **transferencias de custodia**, incluyendo fechas, horas, personas involucradas y métodos de transferencia (por ejemplo, números de envío).

**B. Almacenamiento Físico Seguro:**

*   **Área Segura:** Almacenar la evidencia en un **área segura**, con **acceso restringido** y **registrado**. Debe ser posible **detectar el acceso no autorizado**.
*   **Control Ambiental:** Proteger la evidencia de **temperaturas y humedad extremas**, **campos magnéticos**, **polvo**, **humedad** y otros contaminantes dañinos.
*   **Embalaje Adecuado:** Utilizar **embalaje adecuado** para proteger los dispositivos contra daños físicos durante el transporte y almacenamiento. Los equipos deben asegurarse en los vehículos para evitar golpes y vibraciones excesivas.
*   **Inventario:** Realizar un **inventario detallado** de toda la evidencia almacenada, de acuerdo con las políticas de la organización.

**C. Almacenamiento Digital Seguro:**

*   **Medios Comúnmente Utilizados:** Si es posible, utilizar **medios de almacenamiento comúnmente utilizados** para el archivo.
*   **Integridad de los Datos:** Asegurar la **integridad de los datos adquiridos** de manera trazable hasta la adquisición original.
*   **Protección contra Pérdida de Datos:** Considerar el riesgo de **pérdida de datos** debido al agotamiento de baterías en dispositivos activos y tomar precauciones como mantenerlos cargados o analizarlos rápidamente.
*   **Respaldo y Recuperación:** Considerar la **coste y facilidad de la recuperación ante desastres** de los medios de archivo y cómo abordar problemas que afecten los valores hash de los archivos.
*   **Obsolescencia Tecnológica:** Tener en cuenta los posibles problemas de **obsolescencia** de la tecnología de archivo histórica y cómo recuperar la información.
*   **Seguridad del Acceso Digital:** Implementar **medidas de seguridad** para proteger el acceso a las copias digitales de la evidencia, como **cifrado** y **control de acceso basado en roles**.

**D. Políticas y Procedimientos:**

*   **Desarrollo de Políticas:** La organización debe desarrollar **políticas y procedimientos claros** para la recopilación y el almacenamiento seguro de evidencia digital.
*   **Evaluación de Riesgos:** Realizar una **evaluación de riesgos** de la política y los procedimientos de archivo, abordando la probabilidad de daños y la obsolescencia.
*   **Formación del Personal:** Proporcionar **formación inicial y continua** al personal sobre los procedimientos adecuados de recopilación y almacenamiento.

Al explicar estos puntos, se proporcionará a los alumnos una comprensión sólida de los criterios necesarios para recopilar y almacenar de forma segura evidencias de incidentes de ciberseguridad. Se puede complementar la explicación con ejemplos prácticos y casos de estudio para ilustrar la importancia de seguir estos principios.