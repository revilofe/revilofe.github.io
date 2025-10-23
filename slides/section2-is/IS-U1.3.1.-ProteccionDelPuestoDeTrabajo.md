# U1.3.1 - Protección del Puesto de Trabajo

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. El puesto de trabajo


### 1.1. ¿Qué es el puesto de trabajo?

**Puesto de trabajo del usuario**: Lugar desde el cual un empleado realiza su trabajo diario.

**Puede ser:**
* **Físico**: Computadora de escritorio en oficina.
* **Remoto**: Laptop desde casa o café.
* **Híbrido**: Combinación de ambos.

Note: El puesto de trabajo moderno ha evolucionado. Ya no es solo un escritorio con un PC, puede ser cualquier lugar con conexión.


### 1.2. Elementos del puesto de trabajo

**Componentes principales:**

* **Dispositivos hardware**: PCs, laptops, tablets, smartphones.
* **Software**: Aplicaciones para realizar tareas.
* **Comunicación y red**: Internet, VPN, acceso a servidores.
* **Instalaciones físicas**: Oficinas, salas de reuniones.
* **Acceso a datos**: Permisos sobre información.
* **Personal**: El empleado y sus hábitos de trabajo.

Note: Cada elemento es un vector potencial de ataque. Como alumnos y alumnas, debéis entender que proteger el puesto es proteger todos estos elementos.


### 1.3. Criticidad del puesto de trabajo

**¿Por qué es crítico protegerlo?**

* Es el **punto de acceso** a la información corporativa.
* Almacena **datos sensibles** localmente.
* Puerta de entrada para **ataques** (phishing, malware).
* El usuario es el **eslabón más débil** de la cadena.
* Su compromiso afecta toda la organización.

Note: El 90% de los ciberataques exitosos empiezan en el puesto de trabajo del usuario. Protegerlo es proteger toda la organización.

---

## 2. Políticas y normativas


### 2.1. ¿Qué es una normativa?

**Normativa**: Conjunto de reglas y requisitos específicos para garantizar un ambiente de trabajo seguro.

**Objetivos:**
* Definir cómo gestionar y asegurar el puesto.
* Proteger información y sistemas.
* Minimizar riesgos y vulnerabilidades.
* Establecer responsabilidades claras.

Note: Una normativa es el "código de circulación" de la seguridad en el puesto de trabajo. Sin ella, cada uno haría lo que quisiera.


### 2.2. Jerarquía normativa

**Niveles de detalle creciente:**

1. **Política de Seguridad**: Compromiso general de la organización.
2. **Normativa específica**: Reglas para áreas concretas (puesto de trabajo).
3. **Procedimientos**: Pasos detallados para cumplir normativa.

Note: Es como una pirámide: arriba la filosofía general, abajo los pasos concretos a seguir.


### 2.3. Ejemplo de jerarquía

**Caso práctico:**

* **Política**: "La organización se compromete a proteger la información con altos estándares de seguridad".
* **Normativa**: "Todos los empleados deben bloquear sus equipos al ausentarse".
* **Procedimiento**: "Para bloquear: Win + L en Windows, Ctrl + Cmd + Q en macOS, Super + L en Linux".

Note: Observad cómo cada nivel añade especificidad. La política es abstracta, el procedimiento es ejecutable.


### 2.4. Tipos de medidas por audiencia

**Clasificación según destinatario:**

1. **Procesos (PRO)**: Para gestores, medidas organizativas.
2. **Tecnología (TEC)**: Para personal técnico, medidas especializadas.
3. **Personas (PER)**: Para todos, medidas simples y comprensibles.

Note: No todas las medidas son para todos. Adaptad el mensaje y la complejidad a la audiencia.


### 2.5. Medidas de proceso (PRO)

**Orientadas a gestores:**

* Establecer políticas de seguridad.
* Definir procedimientos de auditoría.
* Gestionar roles y permisos.
* Supervisar cumplimiento normativo.

**Ejemplo:** Procedimiento de alta/baja de usuarios con checklist de permisos a revisar.

Note: Las medidas PRO son el pegamento organizativo. Sin ellas, las medidas técnicas y de personas no funcionan coordinadamente.


### 2.6. Medidas de tecnología (TEC)

**Orientadas a personal técnico:**

* Implementar firewalls y sistemas IDS/IPS.
* Configurar sistemas de copias de seguridad.
* Gestionar actualizaciones y parches.
* Configurar cifrado de discos.
* Implementar autenticación multifactor.

**Ejemplo:** Configurar firewall para bloquear tráfico no autorizado al puerto 3389 (RDP).

Note: Las medidas TEC requieren conocimientos especializados. No intentéis implementarlas sin formación adecuada.


### 2.7. Medidas de personas (PER)

**Orientadas a todos los empleados:**

* Política de escritorio limpio.
* Bloquear pantalla al ausentarse.
* No compartir contraseñas.
* Reportar incidentes sospechosos.
* Capacitación anual en seguridad.

**Ejemplo:** Al finalizar jornada, guardar documentos sensibles en cajón con llave.

Note: Las medidas PER son las que más impacto tienen porque afectan a toda la organización. Si todos las cumplen, la seguridad mejora exponencialmente.

---

## 3. Estándares aplicables


### 3.1. ISO/IEC 27001

**Estándar internacional de gestión de seguridad:**

* Marco para **Sistema de Gestión de Seguridad de la Información (SGSI)**.
* Anexo A incluye controles para puestos de trabajo.
* Cubre seguridad en estaciones y control de accesos.
* Evaluación y mitigación de riesgos.

Note: ISO 27001 es el estándar de referencia mundial. Certificarse en él abre puertas laborales en todo el mundo.


### 3.2. Controles ISO 27001 relevantes

**Controles del Anexo A para puestos:**

* **A.7.2** Control de acceso físico.
* **A.8.1** Inventario de activos.
* **A.8.3** Uso aceptable de activos.
* **A.11.2** Seguridad de equipos.
* **A.12.3** Copias de seguridad.

Note: Estos controles son directamente aplicables a la protección del puesto de trabajo. Estudiadlos en detalle.


### 3.3. GDPR

**Reglamento General de Protección de Datos (UE):**

* Protege **privacidad y datos personales**.
* Exige seguridad en acceso y almacenamiento.
* Cifrado y contraseñas seguras obligatorias.
* Notificación de brechas en 72 horas.

Note: El GDPR no es opcional en Europa. Multas de hasta 20M€ o 4% facturación global. Tomáoslo muy en serio.


### 3.4. Implicaciones GDPR en el puesto

**Requisitos específicos:**

* Solo acceder a datos personales si es **necesario** para el trabajo.
* Usar **conexiones seguras** (VPN) para acceso remoto.
* **Cifrar** dispositivos que contengan datos personales.
* **No compartir** datos personales por canales inseguros.

Note: Cada vez que un empleado accede a datos personales desde su puesto, está sujeto a GDPR. La responsabilidad es compartida.


### 3.5. LOPDGDD

**Ley Orgánica de Protección de Datos (España):**

* Complementa y adapta GDPR a España.
* Añade especificidades sobre videovigilancia.
* Regula uso de dispositivos digitales en el trabajo.
* Derechos digitales de los trabajadores.

Note: LOPDGDD es la implementación española del GDPR. Conocer ambas es esencial para trabajar en España.


### 3.6. ENS (Esquema Nacional de Seguridad)

**Para administraciones públicas españolas:**

* Obligatorio para organismos públicos.
* Categorización de sistemas (BAJO, MEDIO, ALTO).
* Medidas de seguridad proporcionales a categoría.
* Auditorías periódicas obligatorias.

Note: Si trabajáis en administración pública, el ENS es ley. Categoría ALTA requiere medidas muy estrictas.


### 3.7. CCN-STIC

**Guías del Centro Criptológico Nacional:**

* Documentos técnicos detallados.
* CCN-STIC 800 serie sobre ENS.
* Guías de configuración segura.
* Buenas prácticas de seguridad.

Note: Las guías CCN-STIC son recursos gratuitos y de altísima calidad. Deberían ser lectura obligatoria para todo profesional de seguridad en España.

---

## 4. Políticas específicas del puesto


### 4.1. Política de contraseñas

**Requisitos típicos:**

* Longitud mínima: 12-16 caracteres.
* Complejidad: mayúsculas, minúsculas, números, símbolos.
* Cambio periódico: cada 90 días.
* No reutilizar últimas 5 contraseñas.
* Usar gestor de contraseñas corporativo.

Note: Las contraseñas siguen siendo el método de autenticación más común. Una política estricta reduce significativamente el riesgo de compromiso.


### 4.2. Autenticación multifactor (MFA)

**Segunda capa de seguridad:**

* Algo que **sabes** (contraseña).
* Algo que **tienes** (token, móvil).
* Algo que **eres** (huella, rostro).

**Obligatorio para:**
* Accesos administrativos.
* Acceso remoto (VPN).
* Sistemas críticos.

Note: MFA reduce el riesgo de compromiso en un 99%. Es una de las medidas de seguridad más efectivas y debe ser obligatoria.


### 4.3. Política de pantalla bloqueada

**Protección ante ausencias:**

* Bloqueo **automático** tras 5-10 minutos de inactividad.
* Bloqueo **manual** obligatorio al ausentarse.
* Requiere contraseña para desbloquear.
* Protectores de pantalla no son suficientes.

Note: Un puesto desbloqueado es una invitación a curiosos o atacantes internos. Esta política es simple pero extremadamente efectiva.


### 4.4. Política de escritorio limpio

**Clean Desk Policy:**

* No dejar documentos sensibles en el escritorio.
* Guardar papeles en cajones con llave.
* No notas con contraseñas pegadas.
* Al finalizar jornada, escritorio despejado.

Note: La ingeniería social empieza mirando lo que dejáis visible en vuestro escritorio. Esta política previene ataques de baja sofisticación pero alta efectividad.


### 4.5. Política de dispositivos USB

**Control de medios extraíbles:**

* **Prohibición** total (política más restrictiva).
* **Lista blanca** de dispositivos autorizados.
* **Escaneo** obligatorio de contenido antes de uso.
* **Cifrado** obligatorio en USBs corporativos.

Note: Los USBs son vector clásico de malware. Stuxnet se propagó así. La política debe ser clara y técnicamente enforced.


### 4.6. Política de instalación de software

**Control de aplicaciones:**

* Solo software **aprobado** por TI.
* **Prohibición** de software personal/gratuito.
* Actualizaciones solo desde **fuentes oficiales**.
* Usuarios sin **permisos de administrador**.

Note: Cada aplicación no autorizada es una potencial puerta trasera. Esta política debe complementarse con controles técnicos (AppLocker, whitelist).


### 4.7. Política de uso aceptable (AUP)

**Usos permitidos y prohibidos:**

* **Permitido**: Uso profesional, formación relacionada.
* **Prohibido**: Descarga de contenido ilegal, gaming, torrents.
* **Monitorización**: La organización puede monitorizar actividad.
* **Consecuencias**: Sanciones por incumplimiento.

Note: El AUP debe firmarse por todos los empleados. Es un contrato que protege legalmente a la organización.

---

## 5. Trabajo remoto y BYOD


### 5.1. Desafíos del trabajo remoto

**Nuevos riesgos:**

* Redes WiFi domésticas **inseguras**.
* **Falta de control físico** del entorno.
* **Dificultad** en aplicar políticas de seguridad.
* Mezcla de **uso personal y profesional**.
* Mayor superficie de ataque.

Note: El COVID-19 aceleró el trabajo remoto sin tiempo para preparación adecuada. Muchas organizaciones aún luchan con estos desafíos.


### 5.2. Política de trabajo remoto

**Medidas específicas:**

* **VPN obligatoria** para acceso a recursos corporativos.
* **Verificación de seguridad** WiFi doméstica.
* **Separación** de red doméstica (red invitados para trabajo).
* **Cifrado de disco** completo obligatorio.
* **Soporte remoto** IT disponible.

Note: El trabajo remoto no debe comprometer la seguridad. Estas medidas crean un "perímetro virtual" donde no hay físico.


### 5.3. BYOD (Bring Your Own Device)

**Uso de dispositivos personales:**

**Ventajas:**
* Ahorro de costes para empresa.
* Comodidad para empleado.

**Desventajas:**
* Control limitado de seguridad.
* Mezcla uso personal/profesional.
* Dificultad en borrado remoto.

Note: BYOD es tentador económicamente pero complejo desde seguridad. Muchas organizaciones lo prohíben por los riesgos.


### 5.4. Política BYOD

**Si se permite, requisitos mínimos:**

* **MDM** (Mobile Device Management) obligatorio.
* **Containerización** de datos corporativos.
* **Antivirus** actualizado.
* Sistema operativo **actualizado**.
* **Aceptación** de borrado remoto en caso de pérdida.

Note: MDM permite gestionar remotamente el dispositivo. La containerización separa datos personales de corporativos.


### 5.5. Gestión de dispositivos móviles (MDM)

**Capacidades del MDM:**

* **Inventario** de dispositivos conectados.
* **Aplicación** de políticas de seguridad.
* **Actualización** remota de configuraciones.
* **Borrado remoto** (wipe) si se pierde dispositivo.
* **Geolocalización** de dispositivos corporativos.

Note: MDM es esencial para BYOD y trabajo remoto. Herramientas populares: Microsoft Intune, VMware Workspace ONE, MobileIron.

---

## 6. Protección técnica del puesto


### 6.1. Antivirus y antimalware

**Defensa básica obligatoria:**

* Instalación y **actualización automática**.
* Escaneo en **tiempo real**.
* Escaneo **programado** semanal completo.
* **Cuarentena** de archivos sospechosos.
* Reportar detecciones a consola central.

Note: El antivirus no es suficiente por sí solo, pero sigue siendo necesario. Es la primera línea de defensa contra amenazas conocidas.


### 6.2. Firewall personal

**Protección de red local:**

* **Activado** siempre, especialmente en público.
* Bloquear **conexiones entrantes** no solicitadas.
* Permitir solo **aplicaciones autorizadas**.
* Perfil **público** activado en redes no confiables.

Note: El firewall de Windows/macOS es suficiente para la mayoría de usuarios. La clave es configurarlo correctamente y no deshabilitarlo.


### 6.3. Cifrado de disco completo

**BitLocker (Windows) o FileVault (macOS):**

* Cifrado de **disco completo** (FDE - Full Disk Encryption).
* Protege datos si **roban** el dispositivo físico.
* Transparente para el usuario.
* Clave de recuperación en custodia de IT.

Note: Sin cifrado, cualquiera puede extraer el disco y leer todos los datos. Con cifrado, el disco robado es inútil sin la contraseña.


### 6.4. Actualizaciones de seguridad

**Patch management crítico:**

* Actualizaciones de **sistema operativo** automáticas.
* Actualizaciones de **aplicaciones** críticas.
* Parches de **seguridad** prioritarios (deploy en 48h).
* **Testing** previo en entorno controlado.

Note: Los exploits suelen aparecer días después de que se publique un parche. La ventana de vulnerabilidad debe minimizarse.


### 6.5. Control de puertos USB

**Restricción técnica:**

* **Deshabilitar** puertos USB via GPO o software.
* **Whitelist** de dispositivos autorizados por hardware ID.
* **Alertas** ante conexión de dispositivos no autorizados.
* **Cifrado** obligatorio en USBs corporativos.

Note: El control técnico es más efectivo que solo la política. Los usuarios pueden olvidar o ignorar, el sistema nunca.


### 6.6. Application whitelisting

**Solo software autorizado:**

* **Lista blanca** de aplicaciones permitidas.
* Bloqueo de **todo lo demás**.
* Herramientas: AppLocker (Windows), Gatekeeper (macOS).
* Actualización dinámica de whitelist.

Note: El enfoque de lista blanca es más seguro que lista negra. En lugar de bloquear lo malo conocido, solo permites lo bueno conocido.


### 6.7. Backup del puesto de trabajo

**Respaldo de datos críticos:**

* Backup **automático** nocturno.
* Almacenamiento en **servidor central** o nube.
* Incluir carpetas de **usuario** (Documentos, Escritorio).
* **Exclusión** de software (reinstalable).
* Test de **restauración** trimestral.

Note: Los usuarios pierden datos por mil razones: fallos hardware, borrados accidentales, ransomware. El backup es el salvavidas.

---

## 7. Formación y concienciación


### 7.1. Importancia de la formación

**El usuario como primera línea:**

* Tecnología sola **no es suficiente**.
* Usuario formado detecta **phishing**.
* Usuario concienciado sigue **políticas**.
* Usuario comprometido = organización comprometida.

Note: Podéis tener la mejor tecnología del mundo, pero un usuario que cae en phishing lo invalida todo. La formación es crítica.


### 7.2. Programa de concienciación

**Elementos del programa:**

* Formación **inicial** para nuevos empleados.
* Formación **anual** de refuerzo para todos.
* **Simulacros** de phishing periódicos.
* **Newsletters** de seguridad mensuales.
* **Carteles** recordatorios en oficinas.

Note: La concienciación debe ser continua. La memoria se desvanece y las amenazas evolucionan constantemente.


### 7.3. Temas de formación

**Contenidos esenciales:**

* Identificación de **phishing** y spear-phishing.
* Creación de **contraseñas seguras**.
* Uso de **MFA**.
* **Ingeniería social** y cómo defenderse.
* Qué hacer ante un **incidente** sospechoso.

Note: Estos temas cubren los vectores de ataque más comunes. Adaptad el contenido a las amenazas específicas de vuestra organización.


### 7.4. Simulacros de phishing

**Entrenamiento práctico:**

* Envío de **emails falsos** de phishing a empleados.
* Monitorizar quién **hace clic**.
* Formación **inmediata** para quien cae.
* Sin **penalizaciones**, enfoque educativo.
* **Métricas** de mejora trimestral.

Note: Los simulacros son la mejor forma de medir efectividad de la formación. Los usuarios aprenden más de sus errores en simulacro que de teoría.

---

## 8. Monitorización y cumplimiento


### 8.1. Necesidad de monitorización

**¿Por qué monitorizar?**

* Verificar **cumplimiento** de políticas.
* Detectar **anomalías** de comportamiento.
* Responder **rápidamente** a incidentes.
* **Evidencia** para investigaciones.

Note: La monitorización no es espionaje, es protección. Debe hacerse con transparencia y dentro del marco legal.


### 8.2. Qué monitorizar

**Aspectos a supervisar:**

* **Logs** de autenticación (exitosos y fallidos).
* **Instalación** de software.
* **Conexión** de dispositivos USB.
* **Tráfico** de red anómalo.
* Acceso a **recursos** sensibles.

Note: No monitorizéis todo o crearéis demasiado ruido. Centraos en eventos de seguridad relevantes.


### 8.3. Herramientas de monitorización

**Soluciones técnicas:**

* **SIEM**: Correlación de logs centralizados.
* **EDR**: Endpoint Detection and Response.
* **DLP**: Data Loss Prevention.
* **NAC**: Network Access Control.

Note: Estas herramientas generan alertas que analistas deben investigar. No son "instalar y olvidar", requieren gestión activa.


### 8.4. Aspectos legales de la monitorización

**Marco legal en España:**

* **Informar** a empleados de la monitorización.
* **Proporcionalidad**: Solo monitorizar lo necesario.
* **LOPDGDD** Artículo 87: Uso de dispositivos digitales.
* **Estatuto de Trabajadores**: Límites a vigilancia.

Note: La monitorización sin información previa a los empleados puede ser ilegal. Consultad con el departamento legal antes de implementar.


### 8.5. Auditorías de cumplimiento

**Verificación periódica:**

* Auditoría **trimestral** de configuraciones.
* Verificación **semestral** de controles técnicos.
* Revisión **anual** completa de políticas.
* Pentesting **anual** de puestos de trabajo.

Note: Las auditorías descubren el gap entre políticas definidas y realidad implementada. Son esenciales para mejora continua.

---

## 9. Gestión de incidentes en el puesto


### 9.1. Tipos de incidentes comunes

**Incidentes típicos:**

* **Malware** detectado.
* **Phishing** exitoso.
* **Pérdida** o robo de dispositivo.
* **Acceso no autorizado** a cuenta.
* **Fuga** de información.

Note: Cada organización debe tener procedimientos documentados para responder a estos incidentes comunes.


### 9.2. Procedimiento de reporte

**¿Qué debe hacer el usuario?**

1. **No apagar** el equipo (preservar evidencias).
2. **Desconectar** de red si es seguro.
3. **Notificar** a IT/Seguridad inmediatamente.
4. **Documentar** qué observó y cuándo.
5. **No investigar** por cuenta propia.

Note: La velocidad de reporte es crítica. Cada minuto cuenta en contención de un incidente. Los usuarios deben saber exactamente a quién llamar.


### 9.3. Respuesta a malware

**Pasos del equipo IT:**

1. **Aislar** el equipo afectado.
2. **Identificar** el tipo de malware.
3. **Eliminar** la amenaza.
4. **Verificar** que no haya lateral movement.
5. **Restaurar** desde backup si necesario.
6. **Analizar** causa raíz.

Note: La respuesta debe ser rápida pero metodológica. Borrar evidencias puede impedir entender cómo ocurrió el compromiso.


### 9.4. Respuesta a pérdida de dispositivo

**Protocolo de dispositivo perdido/robado:**

1. Reporte **inmediato** por el usuario.
2. IT ejecuta **borrado remoto** (MDM).
3. **Cambio** de contraseñas de cuentas accedidas.
4. **Revisión** de actividad reciente de la cuenta.
5. **Denuncia** policial si es robo.
6. **Lecciones aprendidas** del incidente.

Note: El borrado remoto solo funciona si el dispositivo se conecta a internet. Por eso el cifrado de disco es tan importante como backup.

---

## 10. Conclusión


### 10.1. Resumen de conceptos clave

* **Puesto de trabajo**: Punto crítico de acceso a información.
* **Políticas**: Definen qué debe hacerse.
* **Estándares**: ISO 27001, GDPR, ENS proporcionan marco.
* **Protección técnica**: Múltiples capas de defensa.
* **Formación**: Usuario concienciado es mejor defensa.

Note: La protección del puesto de trabajo no es una medida, es un conjunto de controles técnicos, organizativos y humanos trabajando juntos.


### 10.2. Defensa en profundidad

**Capas de protección:**

1. Política y concienciación.
2. Autenticación fuerte (MFA).
3. Antivirus y firewall.
4. Cifrado.
5. Monitorización.
6. Respuesta a incidentes.

Note: Si una capa falla, las demás siguen protegiendo. Esta es la esencia de defensa en profundidad (defense in depth).


### 10.3. Responsabilidad compartida

**Seguridad es tarea de todos:**

* **Dirección**: Aprobar políticas y presupuesto.
* **IT/Seguridad**: Implementar controles técnicos.
* **Usuarios**: Seguir políticas y reportar incidentes.
* **RRHH**: Formar y gestionar incumplimientos.

Note: Un solo eslabón débil compromete toda la cadena. La seguridad requiere compromiso de toda la organización.


### 10.4. Próximos pasos para alumnos y alumnas

Práctica recomendada:

1. Revisar políticas de seguridad de vuestra universidad.
2. Configurar MFA en todas vuestras cuentas personales.
3. Habilitar cifrado de disco en vuestro portátil.
4. Practicar identificación de phishing con ejercicios online.
5. Leer estándares ISO 27001 Anexo A y GDPR completo.

Note: La mejor forma de aprender es aplicándolo a vuestro entorno personal primero. Mejoraréis vuestra seguridad y ganaréis experiencia práctica.

---

## Bibliografía

* [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) - Information Security Management
* [GDPR](https://gdpr-info.eu/) - General Data Protection Regulation
* [CCN-STIC 800](https://www.ccn-cert.cni.es/series-ccn-stic/800-guia-esquema-nacional-de-seguridad.html) - Guías ENS
* [INCIBE - Protección del puesto de trabajo](https://www.incibe.es/)
* LOPDGDD - Ley Orgánica 3/2018

Note: Estos recursos son fundamentales y de acceso gratuito. Dedicad tiempo a estudiarlos en profundidad, especialmente ISO 27001 y GDPR.
