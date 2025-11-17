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

Note: El puesto de trabajo ya no es solo un escritorio físico—puede ser remoto (laptop desde casa), híbrido (combinación), o móvil (smartphone, tablet en café). Esta flexibilidad aumenta productividad pero también amplía la superficie de ataque: cada ubicación y dispositivo es un potencial punto de entrada. La protección debe adaptarse a esta realidad distribuida.


### 1.2. Elementos del puesto de trabajo

**Componentes principales:**

* **Dispositivos hardware**: PCs, laptops, tablets, smartphones.
* **Software**: Aplicaciones para realizar tareas.
* **Comunicación y red**: Internet, VPN, acceso a servidores.
* **Instalaciones físicas**: Oficinas, salas de reuniones.
* **Acceso a datos**: Permisos sobre información.
* **Personal**: El empleado y sus hábitos de trabajo.

Note: Cada elemento del puesto representa un vector de ataque: hardware puede ser robado/infectado, software tiene vulnerabilidades, comunicaciones pueden interceptarse, instalaciones permiten accesos físicos no autorizados, permisos pueden estar mal configurados, y personal comete errores o cae en ingeniería social. Proteger el puesto requiere asegurar simultáneamente todos estos elementos.


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


### 2.1. ¿Qué es una normativa? I

**Normativa**: Conjunto de reglas y requisitos específicos para garantizar un ambiente de trabajo seguro.

**Objetivos:**
* Definir cómo gestionar y asegurar el puesto.
* Proteger información y sistemas.
* Minimizar riesgos y vulnerabilidades.
* Establecer responsabilidades claras.

Note: La normativa establece reglas claras que todos deben seguir para garantizar seguridad, como el código de circulación en tráfico. Define cómo gestionar acceso físico/lógico, uso de dispositivos, instalación de software, gestión de contraseñas, políticas de escritorio limpio, y procedimientos ante incidentes. Sin normativa clara, cada empleado sigue sus propios criterios creando vulnerabilidades.


### 2.1. ¿Qué es una normativa? II

**Desarrollo**:
 
* Emplear un documento por cada política de protección del puesto de trabajo, centrado en un aspecto.
* Describir lo que es correcto.
* Describir lo que es incorrecto.
* Responsabilizar a los empleados respecto al cumplimiento, violaciones y sanciones.
* Fomentar el conocimiento y la adherencia a las normas.

Note: La normativa se desarrolla en documentos específicos para cada área crítica del puesto de trabajo (uso de contraseñas, acceso remoto, instalación software, etc). Cada normativa debe ser clara y concisa, describiendo comportamientos correctos e incorrectos. Además, debe responsabilizar a los empleados por su cumplimiento, estableciendo consecuencias claras en caso de violaciones (advertencias, sanciones disciplinarias). Esto asegura que todos entienden sus obligaciones y las consecuencias de no cumplirlas.


### 2.1. ¿Qué es una normativa? III

**Ejemplo práctico de normativa:**

* **Restricciones de acceso**: Solo personal autorizado accede
  a datos confidenciales.
* **Seguridad física/digital**: Cerraduras, contraseñas complejas, MFA.
* **Actualizaciones**: Software actualizado con últimos parches.
* **Buenas prácticas**: Bloquear pantalla, evitar redes públicas.

Note: Traduciendo normativa a medidas concretas: restricciones de acceso aplican principio de mínimo privilegio (acceder solo a datos necesarios para tu función), seguridad física incluye cajones con llave y control de acceso con tarjetas, seguridad digital requiere contraseñas 12+ caracteres con complejidad y MFA para sistemas críticos, actualizaciones críticas en 48h máximo, y buenas prácticas como bloquear pantalla al ausentarse (Win+L) y usar VPN en redes públicas.


### 2.2. Jerarquía normativa

**Niveles de detalle creciente:**

1. **Política de Seguridad**: Compromiso general de la organización sobre seguridad.
2. **Normativa específica**: Reglas para áreas concretas (puesto de trabajo).
3. **Procedimientos**: Pasos detallados para cumplir normativa.

Note: La jerarquía normativa funciona como una pirámide donde cada nivel añade concreción: la Política establece el compromiso organizativo general (visión y valores), la Normativa traduce ese compromiso en reglas específicas medibles para áreas concretas (qué debe hacerse), y los Procedimientos detallan los pasos técnicos exactos (cómo hacerlo). Esta estructura permite que directivos definan estrategia, responsables de seguridad establezcan reglas, y personal técnico las implemente.


### 2.3. Ejemplo de jerarquía

**Caso práctico:**

* **Política**: "La organización se compromete a proteger la información con altos estándares de seguridad".
* **Normativa**: "Todos los empleados deben bloquear sus equipos al ausentarse".
* **Procedimiento**: "Para bloquear: Win + L en Windows, Ctrl + Cmd + Q en macOS, Super + L en Linux".

Note: Este ejemplo ilustra perfectamente cómo cada nivel aumenta en especificidad y ejecutabilidad: la Política es aspiracional y abstracta (compromiso con altos estándares), la Normativa establece una obligación concreta y medible (bloquear equipos al ausentarse), y el Procedimiento proporciona instrucciones técnicas precisas para cumplirla (atajos de teclado específicos por sistema operativo). De esta forma, ningún empleado puede alegar desconocimiento de qué hacer ni cómo hacerlo.


### 2.4. Tipos de medidas por audiencia I

Las medidas preventivas que la normativa requiere se clasifican:

**Según complejidad:**

1. **Básico (B)**: Sencillo y asequible (ej. Bloqueo de pantalla por inactividad)
2. **Avanzado (A)**: Requiere más recursos y conocimientos (ej. Cifrado de disco completo como BitLocker)

Note: Clasificar medidas por complejidad permite priorizar correctamente: las medidas Básicas (B) son rápidas de implementar, tienen bajo coste y alto impacto (bloqueo automático protege inmediatamente contra acceso físico no autorizado), mientras las medidas Avanzadas (A) requieren más tiempo, recursos y conocimiento técnico especializado (cifrado de disco necesita planificación, gestión de claves, posible impacto en rendimiento). Implementar primero las básicas proporciona protección inmediata mientras se planifican las avanzadas. 


### 2.4. Tipos de medidas por audiencia II

Las medidas preventivas que la normativa requiere se clasifican:

**Según destinatario:**

1. **Procesos (PRO)**: Para gestores, medidas organizativas.
2. **Tecnología (TEC)**: Para personal técnico, medidas especializadas.
3. **Personas (PER)**: Para todos, medidas simples y comprensibles.

Note: Clasificar medidas por audiencia objetivo asegura efectividad: las medidas de Procesos (PRO) requieren visión organizativa y capacidad de decisión gerencial (aprobar políticas, asignar presupuesto), las medidas de Tecnología (TEC) necesitan conocimiento técnico especializado para implementarlas correctamente (configurar firewalls, cifrado), y las medidas de Personas (PER) deben ser simples y claras porque aplican a toda la organización sin importar conocimiento técnico. Adaptar el mensaje a la audiencia maximiza cumplimiento y efectividad. 


### 2.5. Medidas de proceso (PRO)

**Orientadas a gestores:**

* Establecer políticas de seguridad.
* Definir procedimientos de auditoría.
* Gestionar roles y permisos.
* Supervisar cumplimiento normativo.

**Ejemplo:** Procedimiento de alta/baja de usuarios con checklist de permisos a revisar.

Note: Las medidas de Proceso (PRO) son el pegamento que mantiene unida la seguridad organizativa: sin políticas claras aprobadas por dirección, cada departamento actúa independientemente creando incoherencias; sin procedimientos de auditoría, nadie verifica si las medidas se cumplen realmente; sin gestión adecuada de roles y permisos, empleados acumulan accesos innecesarios; sin supervisión, la normativa queda en papel. Un ejemplo práctico: en altas/bajas de usuarios, un checklist PRO asegura revisar todos los accesos sistemáticamente evitando cuentas huérfanas.


### 2.6. Medidas de tecnología (TEC)

**Orientadas a personal técnico:**

* Implementar firewalls y sistemas IDS/IPS.
* Configurar sistemas de copias de seguridad.
* Gestionar actualizaciones y parches.
* Configurar cifrado de discos.
* Implementar autenticación multifactor.

**Ejemplo:** Configurar firewall para bloquear tráfico no autorizado al puerto 3389 (RDP).

Note: Las medidas de Tecnología (TEC) son controles técnicos que requieren conocimiento especializado para implementarse correctamente: firewalls e IDS/IPS detectan y bloquean ataques de red, copias de seguridad permiten recuperación ante ransomware o fallos, gestión de parches cierra vulnerabilidades conocidas antes de que sean explotadas, cifrado protege datos en reposo, y MFA añade capa adicional de autenticación. El ejemplo del firewall bloqueando RDP (puerto 3389) previene ataques de fuerza bruta externos al escritorio remoto, un vector común de compromiso.


### 2.7. Medidas de personas (PER)

**Orientadas a todos los empleados:**

* Política de escritorio limpio.
* Bloquear pantalla al ausentarse.
* No compartir contraseñas.
* Reportar incidentes sospechosos.
* Capacitación anual en seguridad.

**Ejemplo:** Al finalizar jornada, guardar documentos sensibles en cajón con llave.

Note: Las medidas de Personas (PER) son las más críticas porque aplican a toda la organización y su cumplimiento depende de concienciación individual: escritorio limpio evita que visitantes vean información confidencial, bloquear pantalla previene acceso físico no autorizado (el 90% de incidentes internos empiezan aquí), no compartir contraseñas mantiene responsabilidad individual, reportar incidentes permite respuesta temprana, y capacitación anual actualiza conocimiento sobre amenazas. Si todos cumplen estas medidas básicas, la superficie de ataque se reduce exponencialmente con mínimo coste.

---

## 2bis. Escenarios de riesgos y medidas


### 2bis.1. Dispositivos Hardware

**Componentes físicos del puesto:**

* Computadoras de escritorio y laptops
* Tablets y smartphones corporativos
* Memorias USB y discos externos
* Impresoras y escáneres
* Cualquier dispositivo físico de acceso a información

Note: Los dispositivos hardware (PCs, laptops, tablets, smartphones, USBs, impresoras) son los componentes físicos que empleados usan para acceder a sistemas y datos corporativos. Son críticos porque almacenan información localmente y pueden ser robados, perdidos o comprometidos. Veremos los cuatro escenarios de riesgo más comunes y medidas completas (Política, Normativa, Procedimiento) para cada uno.


### 2bis.1.1. Pérdida o Robo de Dispositivos

**Escenario de riesgo:**

* **Riesgo**: Dispositivo robado o perdido expone datos confidenciales.
* **Consecuencias**: Acceso no autorizado a información sensible,
  credenciales comprometidas, pérdida de propiedad intelectual.
* **Impacto**: ALTO - Puede afectar cumplimiento legal (GDPR).

Note: Escenario muy común—millones de dispositivos se pierden/roban cada año. Sin cifrado, cualquiera puede extraer todos los datos conectando el disco a otro PC o arrancando desde USB. Consecuencias: exposición de datos personales (violación GDPR, multas hasta 20M€), robo de propiedad intelectual. Empleados en movilidad (aeropuertos, cafeterías, transporte) son especialmente vulnerables. Es prevenible con medidas adecuadas.


### 2bis.1.1. Pérdida o Robo de Dispositivos II

**Medidas de seguridad:**

**Política**: La organización protegerá todos los dispositivos con
medidas que garanticen seguridad ante pérdida o robo.

**Normativa**:
* Autenticación segura obligatoria (contraseña + MFA).
* Bloqueo automático tras 5 minutos de inactividad.
* Cifrado de disco completo en todos los dispositivos.

Note: La Política establece el compromiso organizativo, la Normativa lo concreta en reglas específicas medibles: autenticación segura (contraseña compleja + MFA: algo que sabes + algo que tienes) impide acceso aunque roben el dispositivo, bloqueo automático protege ante descuido momentáneo, cifrado de disco completo (BitLocker/FileVault con AES-256) hace el disco completamente ilegible sin contraseña correcta. Sin cifrado los datos son vulnerables; con cifrado el dispositivo robado es inútil para el ladrón.


### 2bis.1.1. Pérdida o Robo de Dispositivos III

**Procedimiento de protección:**

1. **Activar bloqueo automático**: Configurar en Windows
   (Configuración > Cuentas > Opciones de inicio de sesión >
   Requerir inicio > 5 minutos). macOS (Preferencias > Seguridad).
2. **Activar cifrado**: Windows (BitLocker), macOS (FileVault).
3. **Verificar cifrado**: Comprobar estado en configuración.
4. **Reportar pérdida**: Llamar a IT inmediatamente al 900-XXX-XXX.

Note: Procedimiento con pasos ejecutables concretos: bloqueo automático en Windows (Configuración > Cuentas > Opciones inicio > "Requerir inicio" cuando PC reactive + protector 5min), cifrado con BitLocker (Panel Control > activar en cada unidad > usar contraseña > guardar clave recuperación en ubicación segura nunca en el mismo dispositivo), en macOS FileVault (Preferencias Sistema > Seguridad > FileVault > Activar). Verificar estado activo. Ante pérdida/robo reportar en <1h para IT ejecute borrado remoto.


### 2bis.1.2. Acceso No Autorizado

**Escenario de riesgo:**

* **Riesgo**: Dispositivo desbloqueado permite acceso no autorizado.
* **Consecuencias**: Manipulación de datos, instalación de malware,
  robo de credenciales en memoria.
* **Impacto**: MEDIO-ALTO - Compromiso de sesión activa.

Note: Ocurre cuando empleado deja puesto desbloqueado y alguien (compañero curioso, visitante, limpieza, atacante) accede físicamente. Con sesión activa, acceso inmediato a todo: leer emails, sistemas, copiar archivos, instalar keyloggers, enviar emails suplantando usuario. Ataques internos son comunes (empleados descontentos, competidores infiltrados). Muchas brechas empiezan con "solo me ausento un minuto" que permite introducir USB malicioso o robar datos. Prevención simple: bloquear siempre.


### 2bis.1.2. Acceso No Autorizado II

**Medidas de seguridad:**

**Política**: Proteger dispositivos garantizando integridad y
confidencialidad ante accesos no autorizados.

**Normativa**:
* Bloqueo automático tras 5-10 min de inactividad.
* Contraseñas seguras (12+ caracteres, complejidad).
* Autenticación biométrica cuando sea posible.

Note: Política mantiene compromiso, Normativa lo concreta: bloqueo automático 5-10min actúa como red de seguridad cuando usuario olvida bloquear manualmente, contraseñas 12+ caracteres con complejidad son mucho más resistentes a fuerza bruta (espacio búsqueda 10^21 vs 10^9 simples), autenticación biométrica (huella, facial con Windows Hello/Touch ID) añade comodidad sin sacrificar seguridad—difícil suplantar y usuario no puede "olvidarla" o escribirla en post-it.


### 2bis.1.2. Acceso No Autorizado III

**Procedimiento de protección:**

1. **Configurar contraseña compleja**: Mínimo 12 caracteres,
   incluir May, min, números, símbolos. Usar gestor contraseñas.
2. **Activar autenticación biométrica**: Windows Hello (huella/facial),
   Touch ID en macOS.
3. **Bloquear manualmente**: Win+L (Windows), Ctrl+Cmd+Q (macOS),
   Super+L (Linux). SIEMPRE al ausentarse.

Note: Contraseñas seguras: usar passphrase tipo "Mi-Hija-Cumple-15-En-Julio!" más fuerte y memorable que "P@ssw0rd", o mejor gestor corporativo (Bitwarden, 1Password) que genera y almacena únicas ultra-seguras. Windows Hello: Configuración > Cuentas > Opciones inicio > configurar PIN primero luego facial/huella (requiere hardware compatible). macOS: Preferencias > Touch ID > añadir huella. Bloqueo manual debe ser reflejo automático: "Me levanto = Win+L". Crítico en oficinas abiertas.


### 2bis.1.3. Falta de Cifrado

**Escenario de riesgo:**

* **Riesgo**: Datos en dispositivo sin cifrar son fácilmente extraíbles.
* **Consecuencias**: Exposición total de información almacenada
  en caso de robo o acceso físico no autorizado.
* **Impacto**: CRÍTICO - Pérdida total de confidencialidad.

Note: Sin cifrado, contraseñas del SO son trivialmente eludibles: atacante arranca desde USB live, monta disco, copia todos los archivos sin protección. O extrae disco y lo conecta a otro PC. En 5-10min acceso completo a TODO: documentos, emails, historial, contraseñas guardadas, claves SSH, tokens autenticación. Cifrado disco completo es IMPRESCINDIBLE en cualquier dispositivo que salga de instalaciones seguras o contenga datos sensibles. Diferencia entre brecha masiva y dispositivo inútil para atacante.


### 2bis.1.3. Falta de Cifrado II

**Medidas de seguridad:**

**Política**: Todos los dispositivos con datos sensibles estarán cifrados
para proteger confidencialidad ante acceso físico.

**Normativa**:
* Cifrado completo de disco obligatorio en todos los dispositivos.
* Prohibido almacenar información confidencial en dispositivos
  sin cifrar o personales no autorizados.

Note: Política clara: proteger mediante cifrado. Normativa ejecutable: FDE (Full Disk Encryption) obligatorio sin excepciones—desde arranque hasta último byte cifrado con AES-256. Sin clave de cifrado (derivada de contraseña o TPM), datos son basura indescifrable. Segunda norma crítica: prohibir almacenar datos confidenciales en dispositivos sin protección (USBs personales, discos externos sin cifrar, laptop personal). Si se trabaja en dispositivo personal, debe cumplir mismos estándares (cifrado, antivirus, actualizaciones) que corporativos.


### 2bis.1.3. Falta de Cifrado III

**Procedimiento de activación:**

1. **Windows (BitLocker)**: Panel Control > BitLocker >
   Activar BitLocker > Usar contraseña > Guardar clave recuperación.
2. **macOS (FileVault)**: Preferencias > Seguridad > FileVault >
   Activar FileVault > Guardar clave recuperación.
3. **Verificar**: Comprobar que indica "Cifrado activado".
4. **Excepciones**: Reportar a IT si no puede activarse.

Note: Windows BitLocker requiere Pro/Enterprise (Home no incluido, considerar upgrade). Buscar "Administrar BitLocker", activar en C:, introducir contraseña, CRÍTICO: guardar clave recuperación en ubicación segura externa (OneDrive corporativo, USB en caja fuerte, impreso seguro)—única manera de recuperar datos si olvidas contraseña. Cifrado inicial puede tardar horas; PC usable mientras cifra en segundo plano. macOS FileVault más sencillo: Preferencias > Seguridad > FileVault > Activar, elegir recuperación iCloud o clave local (recomendado corporativo). Si problemas técnicos reportar IT inmediatamente.


### 2bis.1.4. Infección de Malware

**Escenario de riesgo:**

* **Riesgo**: Descarga de archivos maliciosos o uso de medios no seguros.
* **Consecuencias**: Malware captura información, actúa como backdoor,
  encripta datos (ransomware), se propaga en red.
* **Impacto**: MUY ALTO - Puede comprometer toda la red corporativa.

Note: Malware llega por múltiples vías: emails phishing con adjuntos maliciosos, descargas de sitios comprometidos, USBs infectadas (ataque USB drop), exploit kits en navegadores, o pre-instalado en hardware comprometido. Una vez instalado hace cualquier cosa: keyloggers capturan todo (contraseñas incluidas), infostealers roban archivos/credenciales, RATs dan control total al atacante, ransomware cifra archivos y exige pago, cryptominers usan recursos, botnets convierten PC en parte de red de ataque. Peor: puede propagarse lateralmente por red interna. Defensa requiere múltiples capas.


### 2bis.1.4. Infección de Malware II

**Medidas de seguridad:**

**Política**: Proteger dispositivos contra malware mediante defensa
en profundidad y prevención proactiva.

**Normativa**:
* Antivirus y firewall activos y actualizados obligatorios.
* Prohibida instalación de software no autorizado por IT.
* Escaneo obligatorio de medios extraíbles antes de uso.

Note: Política habla de "defensa en profundidad"—múltiples capas. Normativa define tres concretas: Primera capa antivirus/firewall—detecta malware conocido mediante firmas y heurístico, firewall bloquea conexiones no autorizadas, actualización diaria. Segunda capa control software—solo instalar autorizado verificado por IT, usuarios sin permisos admin (mínimo privilegio) para que no puedan instalar. Tercera capa control medios extraíbles—USBs son vector común, escanear obligatorio antes de abrir archivos, o mejor deshabilitar puertos USB por política para usuarios que no necesitan.


### 2bis.1.4. Infección de Malware III

**Procedimiento de protección:**

1. **Instalar antivirus corporativo**: Seguir instrucciones de IT para
   instalar Endpoint Protection aprobado.
2. **Activar firewall**: Windows Defender Firewall o macOS Firewall.
   Verificar estado "Activado".
3. **Actualizar automáticamente**: Configurar actualización automática
   de firmas de malware y sistema operativo.
4. **Navegación segura**: No descargar de fuentes desconocidas,
   no clic en enlaces sospechosos, reportar emails phishing.

Note: Instalar antivirus corporativo (Symantec, McAfee, Sophos, Defender ATP): seguir instrucciones IT, generalmente se despliega vía GPO/script, verificar icono en barra tareas indica "Protegido". Firewall Windows: buscar "Firewall Defender", activado en redes dominio/privadas/públicas, bloquear tráfico entrante por defecto. macOS: Preferencias > Seguridad > Firewall > Activar > "Bloquear todas entrantes" salvo apps firmadas. Configurar updates automáticos. Navegación segura: no abrir adjuntos inesperados (verificar remitente por otro canal), no extensiones navegador desconocidas, usar tiendas oficiales. Email sospechoso: NUNCA clic, reportar inmediatamente.

---

### 2bis.2. Software y Aplicaciones

**Herramientas para realizar tareas:**

* Aplicaciones de oficina (Word, Excel, PowerPoint)
* Software de gestión (CRM, ERP, RRHH)
* Herramientas de comunicación (email, mensajería)
* Navegadores web y extensiones
* Software especializado por departamento

Note: Software y aplicaciones son herramientas diarias para trabajar—desde procesadores texto hasta sistemas ERP complejos. Todo software que procesa/almacena datos corporativos es activo crítico de seguridad. Puede tener vulnerabilidades explotables, ser malicioso si instalado de fuentes no confiables, tener configuraciones inseguras por defecto, o usarse de formas no previstas que comprometan seguridad. Software desactualizado es vía común de compromiso—atacantes buscan activamente sistemas sin parchar para explotar vulnerabilidades públicamente conocidas.


### 2bis.2.1. Software No Autorizado

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Software no autorizado puede contener malware oculto.
* **Política**: Garantizar seguridad mediante control de software.
* **Normativa**: Solo software aprobado por IT. Solicitar aprobación
  para nuevas necesidades.
* **Procedimiento**: Consultar lista software autorizado en intranet,
  solicitar nuevos via ticket IT justificando necesidad.

Note: Software no autorizado es peligroso porque no pasó verificación seguridad IT—puede contener vulnerabilidades conocidas, ser versión troyanizada con malware, violar licencias (riesgo legal), o tener configuraciones inseguras. Procedimiento: consultar catálogo software aprobado en intranet/portal autoservicio. Si necesitan software no disponible, abrir ticket justificando necesidad negocio. IT evalúa (seguridad, licencias, compatibilidad, coste mantenimiento) antes aprobar. Una vez aprobado, IT instala centralmente o proporciona installer autorizado. Protege organización y usuario—IT puede dar soporte; si no autorizado, usuario asume responsabilidad.


### 2bis.2.2. Software Desactualizado

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Vulnerabilidades sin parchar son explotadas por atacantes.
* **Política**: Mantener todo el software actualizado y seguro.
* **Normativa**: Actualizaciones automáticas activas. Parches críticos
  en 48-72h.
* **Procedimiento**: Activar Windows Update / macOS Update en automático.
  IT despliega parches críticos centralmente.

Note: Software desactualizado es objetivo prioritario atacantes—cuando se publica parche, hacen ingeniería inversa para descubrir vulnerabilidad y crear exploits. Sistemas sin actualizar extremadamente vulnerables. WannaCry 2017 explotó vulnerabilidad Windows parcheada dos meses antes—quienes no actualizaron sufrieron ransomware masivo. Procedimiento: activar updates automáticas todos dispositivos. Windows: Configuración > Actualización > Opciones avanzadas > activar todas automáticas. macOS: Preferencias > Actualización Software > marcar todas casillas. Software crítico empresarial (SAP, Oracle): IT despliega parches vía WSUS/SCCM/Intune. Parches críticos en 48-72h máximo.


### 2bis.2.3. Permisos Excesivos en Aplicaciones

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Permisos mal configurados permiten acceso no autorizado
  a funciones sensibles.
* **Política**: Aplicar principio de mínimo privilegio en aplicaciones.
* **Normativa**: Permisos según rol. Revisión trimestral por IT.
* **Procedimiento**: IT asigna permisos basados en función. Usuarios
  solicitan accesos adicionales justificando necesidad.

Note: Permisos excesivos son peligrosos—si usuario tiene más acceso del necesario, aumenta riesgo si su cuenta se compromete (accidental/malicioso). Ejemplo: empleado ventas no necesita permisos admin en CRM, desarrollador junior no necesita acceso producción. Procedimiento implementa mínimo privilegio: cuando empleado nuevo se incorpora, IT configura permisos basados estrictamente en rol/función. Si necesita accesos adicionales, justificar ("necesito acceso temporal finanzas para reporte X proyecto Y"). IT aprueba excepcionales por tiempo limitado. Trimestralmente IT audita permisos todos usuarios, revocando no utilizados o ya innecesarios (cambio departamento). Minimiza superficie ataque.


### 2bis.2.4. Fugas via Aplicaciones en la Nube

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Configuración insegura en apps nube filtra información.
* **Política**: Uso seguro y controlado de aplicaciones cloud.
* **Normativa**: Solo apps cloud aprobadas. Configuración de
  privacidad obligatoria. No compartir datos sensibles en apps no seguras.
* **Procedimiento**: Usar solo OneDrive/SharePoint corporativo,
  Google Workspace empresarial, o apps aprobadas. Verificar
  configuración de compartición antes de subir archivos.

Note: Apps cloud (SaaS) son cómodas pero riesgosas si no gestionadas bien. Dropbox personal, Drive personal, WeTransfer no tienen controles seguridad corporativos—accesibles desde cualquier dispositivo, enlaces compartidos inadvertidamente públicos, pueden no cifrar en tránsito/reposo, fuera control IT. Procedimiento: usar solo servicios cloud aprobados corporativamente (OneDrive Business, SharePoint Online, Google Workspace empresarial, Box Enterprise). Tienen controles admin centralizados, DLP, auditoría accesos, cumplimiento normativo. Antes subir archivo sensible verificar configuración compartición: ¿quién acceso? ¿solo interno? ¿requiere autenticación? ¿fecha expiración? Configurar siempre "Solo personas organización" nunca "Cualquiera con enlace" para confidenciales.


### 2bis.3. Comunicación y Acceso a Red

**Conectividad para acceder a recursos:**

* Redes corporativas (cableadas, WiFi)
* Conexiones remotas (VPN, acceso directo)
* Redes públicas (aeropuertos, cafeterías, hoteles)
* Internet general y navegación web
* Aplicaciones en la nube (SaaS)

Note: Comunicación y acceso red esenciales para trabajar pero también mayores riesgos seguridad. Cada conexión red es potencial vector ataque: WiFi públicas sin cifrar permiten interceptación tráfico (man-in-the-middle), conexiones directas internet sin VPN exponen IP real organización, navegadores con configuraciones inseguras filtran información, apps que comunican sin cifrado envían datos en claro. Seguridad red requiere autenticación fuerte, cifrado tráfico, segmentación redes, políticas uso aceptable claras.


### 2bis.3.1. Redes WiFi Públicas Inseguras

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Tráfico interceptado en redes públicas sin cifrar.
* **Política**: Garantizar seguridad en comunicaciones desde cualquier
  ubicación.
* **Normativa**: VPN obligatoria para accesos remotos. Prohibido acceso
  a recursos corporativos desde redes públicas sin VPN.
* **Procedimiento**: Instalar cliente VPN corporativo, conectar antes
  de acceder a cualquier recurso empresarial. En WiFi público: VPN ON.

Note: WiFi públicas extremadamente inseguras porque cualquiera conectado misma red puede interceptar tráfico otros (sniffing con Wireshark, Ettercap). Atacantes crean redes WiFi maliciosas con nombres similares legítimas ("Starbucks Free WiFi") para capturar todo tráfico. Sin cifrado, contraseñas/cookies/emails viajan en claro. VPN (Virtual Private Network) cifra todo tráfico dispositivo en túnel seguro hasta servidor VPN corporativo, indescifrable para interceptores. Procedimiento: instalar cliente VPN corporativo (Cisco AnyConnect, GlobalProtect, OpenVPN) según IT, autenticar (usuario+contraseña+MFA), SIEMPRE activar VPN ANTES acceder email/intranet/apps en red no confiable. Regla simple: "WiFi público = VPN ON".


### 2bis.3.2. Acceso No Autorizado a Red Corporativa

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas no autorizadas intentan conectarse a la red interna.
* **Política**: Proteger acceso a red corporativa contra intrusiones.
* **Normativa**: Autenticación multifactor (MFA) obligatoria. Solo
  dispositivos autorizados y registrados pueden conectarse.
* **Procedimiento**: IT registra dispositivos corporativos en NAC
  (Network Access Control). Usuarios activan MFA en portales de acceso.

Note: Acceso no autorizado red puede ocurrir: atacantes logran credenciales válidas (phishing), dispositivos personales comprometidos conectan, visitantes WiFi corporativa sin autorización, atacantes físicos conectan ethernet en puertos desprotegidos. MFA defensa principal—incluso si roban contraseña, no acceden sin segundo factor (código SMS, push notification, token FIDO2). NAC (Network Access Control - Cisco ISE, ForeScout, Microsoft NAP) verifica dispositivos: registrados, cumplen políticas (antivirus actualizado, cifrado activo, parches), pertenecen usuarios autorizados. Si no cumple, denegar acceso o red cuarentena. IT registra cada dispositivo corporativo en NAC con MAC/certificado. WiFi corporativa: WPA2/WPA3-Enterprise con RADIUS, nunca WPA2-PSK compartida.


### 2bis.3.3. Intercepción de Datos en Tránsito

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Información sensible transmitida sin cifrado es interceptada.
* **Política**: Cifrar toda comunicación de datos sensibles.
* **Normativa**: Datos confidenciales deben cifrarse en tránsito.
  Emails sensibles deben usar cifrado S/MIME o PGP.
* **Procedimiento**: Verificar HTTPS (candado) en navegador. Para emails
  sensibles, usar cifrado S/MIME en Outlook o cifrado PGP.

Note: Datos en tránsito (moviéndose por red) vulnerables si no cifrados. HTTP sin S transmite texto claro, cualquier router/atacante captura credenciales/datos. HTTPS cifra con TLS protegiendo confidencialidad. Usuario verificar siempre candado verde navegador antes introducir info sensible—sin candado, conexión no segura. Para emails confidenciales (informes financieros, info legal, datos personales masivos), cifrado transporte TLS no suficiente—necesita cifrado end-to-end donde solo emisor/receptor descifran. S/MIME usa certificados digitales firmar/cifrar emails Outlook—IT proporciona certificado, instalar en Outlook. Para enviar email cifrado S/MIME: componer, Opciones > Cifrar > Cifrar S/MIME > enviar—solo destinatario con certificado podrá descifrar. Alternativa: PGP con Mailvelope para webmail.


### 2bis.3.4. Fugas via Aplicaciones Cloud No Seguras

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Apps cloud mal configuradas exponen datos públicamente.
* **Política**: Uso controlado de servicios cloud con seguridad verificada.
* **Normativa**: Solo apps cloud aprobadas por IT. Configuración
  de compartición revisada antes de uso.
* **Procedimiento**: Usar apps corporativas (OneDrive, SharePoint).
  Al compartir, verificar: ¿Quién accede? ¿Autenticación requerida?

Note: Servicios cloud (SaaS) tienen configuraciones compartición flexibles que generan exposiciones accidentales. Ejemplos reales: buckets S3 AWS públicos exponiendo millones registros, enlaces Drive/OneDrive "cualquiera con enlace" indexados por Google accesibles públicamente, presentaciones confidenciales Slideshare públicas. Procedimiento: usar exclusivamente servicios cloud aprobados corporativamente que IT gestiona centralmente. Al compartir OneDrive/SharePoint: clic derecho > Compartir > "Personas específicas" (no "Cualquiera") > introducir emails > "Pueden ver" (no editar salvo necesario) > marcar "Bloquear descarga" si muy sensible > fecha expiración. IT configurar DLP en Microsoft 365/Workspace detectar automáticamente compartir externamente contenido sensible (tarjetas, DNIs) y bloquear/alertar.

---

### 2bis.4. Instalaciones Físicas

**Espacios físicos de trabajo:**

* Oficinas individuales y abiertas (open space)
* Salas de reuniones y espacios compartidos
* Centros de datos y salas técnicas
* Áreas de recepción y zonas públicas
* Instalaciones de almacenamiento (archivos, bóvedas)

Note: Instalaciones físicas son eslabón olvidado seguridad—enfoque en firewalls/antivirus pero descuidamos puertas/ventanas/personas. Seguridad física crítica porque acceso físico generalmente = compromiso total—alguien con acceso físico puede bypasear mayoría controles lógicos. Proteger con múltiples capas: perímetro exterior (vallas, guardias), acceso edificio (puertas tarjeta, recepcionista), áreas sensibles (control biométrico, doble autenticación), protección activos individuales (cajones llave, destructoras papel). Incluye visitantes no acompañados, personal limpieza acceso nocturno, técnicos mantenimiento, "tailgating" (colarse tras alguien autorizado).


### 2bis.4.1. Acceso No Autorizado a Áreas Restringidas

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas sin autorización acceden a áreas sensibles.
* **Política**: Proteger instalaciones con control de acceso físico robusto.
* **Normativa**: Solo personal autorizado en áreas restringidas.
  Accesos registrados y monitoreados con tarjetas/biometría.
* **Procedimiento**: Usar tarjeta de acceso corporativa. En áreas
  críticas (datacenter), autenticación adicional (PIN+huella). Reportar
  personas no identificadas a seguridad inmediatamente.

Note: Áreas restringidas (datacenters, salas servidores, oficinas ejecutivas, archivos confidenciales) requieren control acceso estricto. Sistema control (tarjetas RFID + lector) registra quién/cuándo/dónde—logs auditables. Áreas críticas: autenticación 2 factores físicos tarjeta (algo tienes) + PIN/huella (algo sabes/eres). Previene que quien robe tarjeta pueda acceder. Procedimiento: presentar tarjeta, esperar tono verde, abrir, cerrar tras de sí. NUNCA permitir "tailgating"—si alguien intenta seguir sin tarjeta, indicar cortésmente que use propia. Persona sin identificación en área restringida: acercarse cortésmente ("¿Llevas tarjeta visitante?"), si sospechoso llamar seguridad. Datacenters: cámaras 24/7 + registro bitácora física.


### 2bis.4.2. Exposición de Información en Espacios Compartidos

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Documentos o dispositivos desatendidos en áreas comunes.
* **Política**: Proteger información mediante política de escritorio limpio.
* **Normativa**: No dejar documentos sensibles en escritorio. Información
  confidencial en archivadores con llave. Pantallas bloqueadas o apagadas.
* **Procedimiento**: Al finalizar jornada: guardar documentos en cajón
  con llave, bloquear PC, apagar monitor. Usar filtros de privacidad
  en laptops en espacios públicos.

Note: Política escritorio limpio (Clean Desk) simple pero efectiva. Muchas brechas empiezan con documentos/post-its contraseñas dejados visibles. Open office: cualquiera puede ver tu pantalla/documentos. Salas reuniones: documentos olvidados vistos por siguiente grupo. Procedimiento requiere disciplina diaria: al finalizar día (o ausentarse tiempo prolongado), revisar escritorio, guardar papeles en cajones con llave, bloquear PC Win+L, apagar monitor si visible desde paso/ventanas. Espacios públicos (cafeterías, aeropuertos): usar filtros privacidad 3M en laptops—pantalla solo legible frontalmente, negra desde ángulos laterales, previene "shoulder surfing". Nunca dejar laptop sin supervisión público ni para baño—empacar o pedir compañero confianza vigile.


### 2bis.4.3. Pérdida o Robo de Dispositivos en Instalaciones

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Dispositivos robados desde oficinas o áreas comunes.
* **Política**: Proteger dispositivos físicamente en instalaciones.
* **Normativa**: Dispositivos con contraseña y cifrado. Laptops en cajones
  con llave o con cable de seguridad cuando no se usan.
* **Procedimiento**: Guardar laptop en cajón con llave al salir. En
  espacios abiertos, usar cable Kensington para anclar laptop a escritorio.

Note: Aunque instalaciones tengan seguridad, robos internos ocurren—empleados deshonestos, contratistas, visitantes, robos oportunistas cuando puerta abierta. Laptops especialmente vulnerables: portátiles, valiosos, fácil reventa. Procedimiento dos niveles protección: Primero almacenamiento seguro: al finalizar jornada guardar laptop cajón/armario llave. Segundo anclaje físico: laptops tienen ranura Kensington para cable seguridad acero anclado punto fijo (escritorio, mesa)—no previene robo determinado (cortar cable con herramientas) pero previene robo oportunista. Dispositivos móviles (tablets, teléfonos): no dejar cargando desatendidos salas reuniones. Cifrado disco completo última línea defensa—si roban dispositivo, datos protegidos.


### 2bis.4.4. Gestión Insegura de Residuos Confidenciales

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Documentos confidenciales desechados sin destrucción segura.
* **Política**: Destruir información confidencial antes de desechar.
* **Normativa**: Documentos confidenciales deben triturarse. Prohibido
  desechar en papelera común. Discos duros deben destruirse físicamente.
* **Procedimiento**: Usar trituradoras de papel (cross-cut) en cada
  planta. Para dispositivos: entregar a IT para destrucción certificada.

Note: "Dumpster diving" (bucear basureros) técnica real recopilación información—atacantes revisan físicamente basura empresas buscando documentos descartados: diagramas red, listados empleados, org charts, credenciales anotadas, reportes financieros, contratos proveedores. Organizaciones han sufrido brechas por tirar documentos sin triturar. Procedimiento: trituradoras papel cross-cut (corte transversal, convierte en confeti ilegible) cada planta cerca impresoras. Trituradoras strip-cut (tiras) insuficientes—tiras reconstruibles. Documentos MUY sensibles: trituradoras P-4+ (cortes menores) según DIN 66399. Triturar cualquier documento confidencial: borradores, copias defectuosas, notas reuniones, post-its información sensible. Medios digitales (discos, USBs, CDs): NO basura normal—entregar IT destrucción física (perforación, pulverización magnética, incineración) + certificado destrucción.


### 2bis.5. Acceso a Datos

**Permisos sobre información corporativa:**

* Documentos electrónicos (Word, PDF, Excel)
* Bases de datos (CRM, ERP, RRHH)
* Archivos compartidos (file shares, SharePoint)
* Aplicaciones internas con datos sensibles
* Información personal (clientes, empleados)

Note: Gestión acceso datos fundamental para proteger confidencialidad/integridad información. Principio rector "mínimo privilegio"—cada persona acceso únicamente datos necesarios su función, nada más. Minimiza radio impacto caso compromiso cuenta o empleado deshonesto (insider threat). Acceso gestionado mediante roles RBAC (Role-Based Access Control) en vez permisos individuales ad-hoc—más escalable/auditable asignar rol "Ventas EMEA" que permisos individuales 50 carpetas. Accesos revisarse periódicamente (trimestral/anual mínimo) porque necesidades cambian: empleados cambian departamento, proyectos finalizan, colaboradores externos terminan contratos, pero permisos quedan indefinidamente generando "privilege creep" (acumulación privilegios).


### 2bis.5.1. Permisos Excesivos o Inadecuados

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Empleado con permisos excesivos accede información
  fuera de su función.
* **Política**: Aplicar principio de mínimo privilegio estrictamente.
* **Normativa**: Permisos según rol y función. Revisión trimestral.
  Proceso automatizado de alta/baja/cambio en ciclo de vida del empleado.
* **Procedimiento**: IT asigna permisos basados en plantilla de rol.
  Solicitudes de accesos adicionales requieren aprobación del manager
  y tienen vigencia temporal (3-6 meses) con renovación explícita.

Note: Permisos excesivos riesgo común menos gestionado. Escenario típico: empleado necesita acceso temporal carpeta proyecto, se da acceso, proyecto termina, acceso nunca revocado. Cinco años después, acceso decenas sistemas/carpetas innecesarios. Si cuenta comprometida, atacante acceso lateral múltiples sistemas. Procedimiento: mínimo privilegio mediante plantillas rol—IT define permisos "Analista Ventas Junior", "Desarrollador Senior", "Gestor Proyectos". Incorporación: asignar rol apropiado automático. Acceso excepcional: solicitud formal, aprobación manager, fecha expiración 3-6 meses, renovación explícita o revocación automática. IT audita permisos trimestralmente vs roles actuales, revoca discrepancias. Integración HRIS: altas (nuevo → permisos), bajas (sale → revocar TODO), cambios (cambio departamento → ajustar).


### 2bis.5.2. Acceso No Autorizado a Información Confidencial

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas sin autorización acceden o visualizan datos sensibles.
* **Política**: Proteger información confidencial con controles estrictos.
* **Normativa**: Información confidencial requiere autenticación multifactor.
  Accesos registrados y auditados. Clasificación de datos obligatoria.
* **Procedimiento**: Activar MFA en sistemas críticos. IT configura
  auditoría de accesos. Empleados deben clasificar documentos (Público,
  Interno, Confidencial, Restringido).

Note: Acceso no autorizado puede ser accidental (empleado curioso) o malicioso (insider, atacante credenciales robadas). Prevención requiere múltiples controles: MFA en sistemas información confidencial—sin segundo factor no acceden aunque roben contraseña. Auditoría accesos—accesos info Confidencial+ registrados automáticamente logs centralizados (SIEM) permitiendo investigación forense ("¿quién/qué/cuándo?"). Clasificación datos—empleados marcan documentos: Público (exposición OK), Interno (solo empleados), Confidencial (solo autorizados), Restringido (solo roles específicos). Herramientas clasificación (Microsoft Information Protection, Trellix DLP) añaden metadatos/watermarks. Sistemas DLP aplican políticas automáticas según clasificación (bloquear envío externo Confidencial).


### 2bis.5.3. Compartición Insegura de Información

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Información sensible compartida por canales inseguros
  o con destinatarios incorrectos.
* **Política**: Compartir información únicamente por canales seguros aprobados.
* **Normativa**: Datos sensibles solo via plataformas corporativas cifradas.
  Prohibido email personal, WhatsApp personal, USBs sin cifrar.
* **Procedimiento**: Para compartir: usar SharePoint/OneDrive empresarial,
  configurar permisos específicos, establecer expiración. Para enviar
  externo: usar portal seguro de intercambio de archivos corporativo.

Note: Compartición insegura causa frecuente brechas. Empleados usan métodos convenientes pero inseguros: email personal (Gmail, Hotmail) "trabajar casa", WhatsApp personal "enviar rápido" documentos, USBs sin cifrar trasladar archivos, WeTransfer gratuito archivos grandes clientes. Métodos fuera control corporativo, sin cifrado, crean copias datos en sistemas no gestionados. Procedimiento: compartición SOLO plataformas corporativas. Interna: SharePoint/OneDrive Business o Workspace empresarial (IT audita, aplica DLP, revoca accesos). Al compartir: clic derecho > Compartir > emails específicos (no "cualquiera enlace") > permisos mínimos (Ver no Editar) > fecha expiración 30-90 días. Externa (clientes, proveedores): portal intercambio seguro (Citrix ShareFile, Accellion, Box) requiere autenticación destinatario, cifra tránsito/reposo, auditoría completa.


### 2bis.5.4. Falta de Auditoría de Accesos

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Accesos indebidos pasan desapercibidos por falta de monitoreo.
* **Política**: Auditar todos los accesos a información sensible.
* **Normativa**: Accesos a datos confidenciales registrados automáticamente.
  Revisión mensual de logs por equipo de seguridad. Alertas automáticas
  en patrones anómalos (accesos fuera de horario, volumen excesivo).
* **Procedimiento**: IT configura logging centralizado en SIEM. Analyst
  de seguridad revisa dashboards semanalmente. Alertas críticas se
  investigan en <1 hora.

Note: Sin auditoría accesos, accesos no autorizados invisibles hasta causar daño (brecha descubierta meses después). Auditoría proactiva detecta/responde rápidamente. Procedimiento: IT configura logging comprehensivo—accesos file shares, SharePoint, bases datos, apps críticas envían logs SIEM centralizado (Splunk, QRadar, Sentinel, ELK). SIEM correlaciona eventos múltiples fuentes, detecta patrones anómalos: usuario 10 archivos/día súbito 10,000 (exfiltración masiva), usuario 9-17h súbito 3am (cuenta comprometida), usuario IP España súbito IP China (compromiso). SIEM genera alertas automáticas investigadas por SOC. Sin SOC 24/7: alertas email/SMS eventos críticos (admin accede RRHH, acceso tabla contraseñas, descarga masiva). Dashboards semanales: ¿top 10 usuarios más accesos? ¿Accesos recursos indebidos? ¿Intentos fallidos repetidos (fuerza bruta)?


### 2bis.6. Personal

**El empleado y su comportamiento:**

* Conocimiento de políticas de seguridad
* Hábitos de trabajo diarios (bloqueo, contraseñas)
* Capacidad de reconocer amenazas (phishing, ingeniería social)
* Actitud ante la seguridad (¿prioridad o molestia?)
* Respuesta ante incidentes sospechosos

Note: Personal—factor humano—simultáneamente eslabón más débil y defensa más importante seguridad. Tecnología puede fallar, pero empleado bien formado/concienciado detecta/previene ataques que bypassean controles técnicos. Contrario, empleado despreocupado/malicioso compromete completamente seguridad más robusta. Cuatro escenarios principales: falta concienciación (ignorancia riesgos/buenas prácticas), hábitos inseguros (atajos comprometen seguridad), vulnerabilidad ingeniería social (ser engañado), desconocimiento/incumplimiento deliberado políticas. Todos prevenibles con formación adecuada, programa continuo concienciación no solo training incorporación.


### 2bis.6.1. Falta de Concienciación en Seguridad

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Empleados ignoran riesgos y toman decisiones inseguras.
* **Política**: Fomentar cultura de seguridad mediante formación continua.
* **Normativa**: Capacitación obligatoria anual para todos. Evaluaciones
  de conocimiento post-formación. Nuevas incorporaciones: formación
  inicial en primera semana.
* **Procedimiento**: RRHH asigna curso e-learning de seguridad (2-3h)
  anual. Simulacros de phishing trimestrales. Resultados registrados
  en sistema HR. Incumplimiento = formación adicional presencial.

Note: Falta concienciación problema fundamental—empleados no saben qué es peligroso. No reconocen phishing, usan contraseñas débiles "más fácil recordar", descargan archivos fuentes dudosas, conectan USBs encontrados parking ("ver qué tiene"), comparten credenciales "ayudar compañero". Ocurre por ignorancia, no malicia. Procedimiento programa obligatorio medible: Formación base anual—curso e-learning 2-3h cubre amenazas actuales (phishing, ransomware, ingeniería social), buenas prácticas (contraseñas seguras, MFA), políticas, qué hacer ante incidentes. Evaluación 80%+ o repetir. Simulacros phishing trimestrales—clic registrado = formación inmediata explicando señales perdidas. Reincidentes formación presencial intensiva. Formación específica rol (admins APT, RRHH protección datos). Actualizar anualmente (deepfakes, ataques IA).


### 2bis.6.2. Hábitos Inseguros de Trabajo

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Empleados desarrollan hábitos inseguros por comodidad.
* **Política**: Establecer y mantener hábitos seguros en trabajo diario.
* **Normativa**: Dispositivos deben bloquearse al ausentarse. Prohibido
  compartir contraseñas. Política escritorio limpio obligatoria.
* **Procedimiento**: Recordatorios periódicos. Auditorías aleatorias
  (security walk-through): equipo seguridad recorre oficina verificando
  escritorios limpios, pantallas bloqueadas. Feedback positivo para
  cumplimiento, correctivo para incumplimiento.

Note: Hábitos inseguros desarrollan gradualmente por conveniencia—"solo me ausento segundo", "más fácil misma contraseña", "guardar cajón es molesto". Cada atajo parece inofensivo individualmente pero colectivamente crean vulnerabilidades masivas. Procedimiento combina recordatorios y auditorías reforzar hábitos: Recordatorios visuales—pósters áreas comunes ("¿Bloqueaste pantalla?", "Clean desk = Secure desk"), salvapantallas mensajes seguridad, email mensual CISO consejos. Auditorías aleatorias—equipo seguridad/managers "security walk-throughs" sin aviso, recorren oficinas final día verificando pantallas bloqueadas, documentos guardados, no post-its contraseñas, no USBs conectados. No punitivo sino educativo—escritorio incumplidor nota cortés recordando política. Reincidentes escalación manager. Feedback positivo: "Este mes 95% escritorios limpios, ¡excelente!". Objetivo crear cultura donde seguridad sea "lo normal".


### 2bis.6.3. Vulnerabilidad a Ingeniería Social

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Empleados engañados por atacantes mediante manipulación
  psicológica (phishing, vishing, pretexting).
* **Política**: Capacitar para reconocer y resistir ingeniería social.
* **Normativa**: Todos deben reconocer señales de phishing/ingeniería social.
  Procedimiento de verificación obligatorio para solicitudes sensibles
  (pagos, cambios de datos bancarios, accesos).
* **Procedimiento**: Ante solicitud inusual (pago urgente, cambio datos,
  acceso extraordinario): PAUSAR, verificar por canal secundario (llamar
  a número conocido, no al del email), consultar con supervisor si dudas.

Note: Ingeniería social explota psicología humana: urgencia ("cuenta suspendida si no actúas ya"), autoridad ("viene del CEO"), reciprocidad ("te ayudé, ayúdame"), curiosidad ("mira foto tuya encontré"). Atacantes expertos manipuladores. Phishing forma más común: email parece legítimo (banco, Microsoft, CEO) pidiendo clic enlace, descarga adjunto, credenciales. También vishing (teléfono) y smishing (SMS). Procedimiento técnica "STOP-THINK-CONNECT": STOP—pausar, no actuar impulsivamente ante urgencia. THINK—analizar indicadores: ¿remitente dirección real o similar incorrecta (microsft.com vs microsoft.com)? ¿Errores gramaticales? ¿Acciones inusuales? ¿Urgencia artificial? CONNECT (o no)—si pasa análisis proceder, dudas verificar canal independiente. Solicitudes financieras/cambios datos bancarios: SIEMPRE verificar llamando número conocido (no del email). Ataques BEC (Business Email Compromise) causan pérdidas millones. Entrenar simulacros realistas desarrollar intuición.


### 2bis.6.4. Incumplimiento de Políticas

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Empleados conocen políticas pero no las siguen deliberadamente.
* **Política**: Asegurar cumplimiento mediante comunicación clara,
  consecuencias definidas y cultura de seguridad.
* **Normativa**: Todos deben firmar compromiso de cumplimiento de políticas
  al incorporarse. Incumplimientos graves = medidas disciplinarias.
* **Procedimiento**: Nuevas incorporaciones firman política en primera
  semana. Actualiz aciones importantes = nueva firma. Auditorías detectan
  incumplimientos. Escalación: 1ª vez warning + formación, 2ª medidas
  disciplinarias según código laboral.

Note: Incumplimiento deliberado ocurre cuando empleado conoce política pero ignora porque "inconveniente", "nadie cumple", o no cree importancia. Crítico distinguir desconocimiento (solución formación) vs deliberado (solución consecuencias). Procedimiento compromiso formal: nuevos empleados onboarding reciben formación políticas + firman "Aceptación Políticas" (leído, entendido, compromiso cumplir). Documento valor legal, usable incidente grave. Actualizaciones importantes políticas comunicadas + nueva aceptación. Auditorías técnicas/físicas detectan incumplimientos. Escalación: 1ª vez conversación manager + warning email + formación refuerzo (enfoque educativo). 2ª vez medida disciplinaria formal según RRHH (amonestación escrita, suspensión temporal). 3ª vez o muy grave (compartir credenciales externos) despido procedente. Importante consistencia—sin consecuencias reales políticas papel mojado. También celebrar cumplimiento: programas "Security Champions", reconocimientos empleados ejemplares.

---

## 3. Estándares aplicables


### 3.1. ISO/IEC 27001

**Estándar internacional de gestión de seguridad:**

* Marco para **Sistema de Gestión de Seguridad de la Información (SGSI)**.
* Anexo A incluye controles para puestos de trabajo.
* Cubre seguridad en estaciones y control de accesos.
* Evaluación y mitigación de riesgos.

Note: ISO/IEC 27001 estándar internacional más reconocido/respetado gestión seguridad información mundial. Marco sistemático para establecer, implementar, mantener, mejorar continuamente SGSI (Sistema Gestión Seguridad Información). Aplicable organizaciones cualquier tamaño/sector, desde PYMEs hasta multinacionales. Anexo A contiene 114 controles seguridad organizados 14 dominios, incluyendo controles específicos protección puestos trabajo: seguridad física estaciones, políticas escritorio limpio, control acceso lógico, protección malware, gestión activos. Certificarse ISO 27001 (profesional mediante cursos Lead Implementer/Auditor) altamente valorado mercado laboral internacional, abre puertas cualquier país. Organizaciones certificadas ISO 27001 demuestran clientes/socios/reguladores gestión seguridad información rigurosa siguiendo mejores prácticas reconocidas internacionalmente.


### 3.2. Controles ISO 27001 relevantes

**Controles del Anexo A para puestos:**

* **A.7.2** Control de acceso físico.
* **A.8.1** Inventario de activos.
* **A.8.3** Uso aceptable de activos.
* **A.11.2** Seguridad de equipos.
* **A.12.3** Copias de seguridad.

Note: Anexo A ISO 27001:2022 (versión actual) contiene 93 controles organizados 4 temas: Organizacionales (37), Personas (8), Físicos (14), Tecnológicos (34). Protección puesto trabajo especialmente relevantes: A.7.2 seguridad física áreas (control acceso oficinas/espacios trabajo), A.8.1 inventario activos (registro actualizado todos dispositivos/software), A.8.3 uso aceptable activos (cómo empleados pueden usar equipos/datos corporativos), A.11.2 equipamiento (protección física contra robos, daños ambientales, acceso no autorizado), A.12.3 copias seguridad (info crítica backup regular verificado). Cada control tiene objetivos específicos, guías implementación, auditable certificación ISO 27001. Base cualquier política robusta protección puesto trabajo, frecuentemente evaluados auditorías seguridad/cumplimiento.


### 3.3. GDPR

**Reglamento General de Protección de Datos (UE):**

* Protege **privacidad y datos personales**.
* Exige seguridad en acceso y almacenamiento.
* Cifrado y contraseñas seguras obligatorias.
* Notificación de brechas en 72 horas.

Note: GDPR (Reglamento UE 2016/679) LA normativa más importante protección datos personales Europa, alcance extraterritorial—afecta cualquier organización mundo procese datos ciudadanos europeos. Vigor mayo 2018, transformó radicalmente gestión datos personales. No opcional ni negociable organizaciones Europa o clientes europeos. Principios fundamentales: minimización datos (solo necesario), limitación propósito (usar solo declarado), exactitud, limitación almacenamiento, integridad/confidencialidad. Multas severas reales: hasta 20M€ o 4% facturación anual global (mayor). Google 50M€ 2019, Amazon 746M€ 2021, Meta 1.200M€ 2023—multas reales duelen. Para puesto trabajo: dispositivo procese datos personales (nombres, emails, DNIs, direcciones, financieros, salud) debe protección medidas técnicas/organizativas apropiadas: cifrado, control acceso, auditoría. Profesionales IT/seguridad tomaros extremadamente serio.


### 3.4. Implicaciones GDPR en el puesto

**Requisitos específicos:**

* Solo acceder a datos personales si es **necesario** para el trabajo.
* Usar **conexiones seguras** (VPN) para acceso remoto.
* **Cifrar** dispositivos que contengan datos personales.
* **No compartir** datos personales por canales inseguros.

Note: Cada empleado accede datos personales desde puesto trabajo sujeto GDPR, comparte responsabilidad cumplimiento—no solo organización entidad legal sino también potencialmente nivel individual. Artículo 5 GDPR principios fundamentales: datos personales procesarse lícitamente, lealmente, transparentemente; recopilarse fines específicos legítimos; adecuados, pertinentes, limitados necesario; exactos/actualizados; conservarse solo tiempo necesario; tratarse garantizando seguridad mediante medidas técnicas/organizativas apropiadas. Práctica puesto trabajo: solo acceder datos personales estrictamente necesario función laboral específica (principio necesidad); usar siempre conexiones seguras cifradas VPN remotamente desde ubicaciones no controladas; dispositivos contengan datos personales cifrados BitLocker/FileVault/equivalente proteger robo/pérdida; nunca compartir datos personales canales inseguros (email personal, WhatsApp, USBs sin cifrar, cloud no aprobados); reportar inmediatamente posible brecha datos personales (GDPR exige notificación autoridad 72h).


### 3.5. LOPDGDD

**Ley Orgánica de Protección de Datos (España):**

* Complementa y adapta GDPR a España.
* Añade especificidades sobre videovigilancia.
* Regula uso de dispositivos digitales en el trabajo.
* Derechos digitales de los trabajadores.

Note: LOPDGDD (Ley Orgánica 3/2018) implementación/adaptación española GDPR. No reemplaza sino complementa GDPR, añadiendo especificidades contexto español y desarrollando aspectos GDPR dejó discreción cada estado miembro. Fundamental conocerla trabajando España porque añade requisitos adicionales y aclara aplicaciones específicas. Disposiciones detalladas: videovigilancia ámbito laboral (art. 89)—regula cómo empresas instalan cámaras instalaciones, qué señalización obligatoria, derechos trabajadores; uso dispositivos digitales ámbito laboral (art. 87)—empleadores pueden acceder contenidos derivados uso dispositivos facilitados trabajadores SOLO controlar cumplimiento obligaciones laborales respetando privacidad/dignidad, implicaciones directas políticas monitorización puestos; derechos digitales trabajadores como desconexión digital (art. 88) implicaciones trabajo remoto/disponibilidad fuera horario. Conocer GDPR + LOPDGDD esencial profesionales protección datos/cumplimiento/seguridad información España.


### 3.6. ENS (Esquema Nacional de Seguridad)

**Para administraciones públicas españolas:**

* Obligatorio para organismos públicos.
* Categorización de sistemas (BAJO, MEDIO, ALTO).
* Medidas de seguridad proporcionales a categoría.
* Auditorías periódicas obligatorias.

Note: ENS (Real Decreto 3/2010, actualizado RD 951/2015) cumplimiento OBLIGATORIO todas administraciones públicas españolas (estatales, autonómicas, locales) y entidades sector público. No opcional ni voluntario—es ley. Marco seguridad completo basado categorización sistemas según impacto potencial brecha tendría sobre información/servicios. Cada sistema categorizarse BAJO/MEDIO/ALTO en tres dimensiones: confidencialidad, integridad, disponibilidad. Categorización determina medidas seguridad obligatorias—mayor categoría, medidas más estrictas. Sistema ALTO tres dimensiones requiere cifrado militar, MFA robusto, auditorías exhaustivas continuas, planes contingencia/continuidad muy detallados, controles acceso físico extremadamente estrictos, monitorización 24/7, personal acreditaciones seguridad. Auditorías cumplimiento ENS periódicas obligatorias, auditores externos independientes verifican controles corresponden categoría. Trabajar administración pública española IT/seguridad: conocer ENS profundidad no opcional, requisito legal, incumplimiento consecuencias graves incluyendo sanciones administrativas/responsabilidades legales.


### 3.7. CCN-STIC

**Guías del Centro Criptológico Nacional:**

* Documentos técnicos detallados.
* CCN-STIC 800 serie sobre ENS.
* Guías de configuración segura.
* Buenas prácticas de seguridad.

Note: Guías CCN-STIC (Centro Criptológico Nacional) documentos técnicos altísima calidad, extremadamente detallados/rigurosos, desarrollados CCN organismo español referencia ciberseguridad administraciones públicas/sectores estratégicos. Extraordinario: disponibles gratuitamente descarga pública web CCN-CERT (ccn-cert.cni.es). Serie CCN-STIC 800 desarrolla específicamente medidas seguridad ENS: guías cada control, guías operativas, configuración segura tecnologías específicas, buenas prácticas. Ejemplos: CCN-STIC 817 gestión ciberincidentes, 825 esquemas firma electrónica, 807 criptología empleo ENS. También guías configuración segura (hardening) SO específicos, bases datos, apps web. Guías nivel técnico avanzado, escritas expertos nacionales, representan estado del arte seguridad práctica aplicada. Lectura obligatoria/referencia continua profesionales seguridad España, especialmente sector público también privado nivel alto. Recursos invaluables completamente gratuitos.

---

## 4. Políticas específicas del puesto


### 4.1. Política de contraseñas

**Requisitos típicos:**

* Longitud mínima: 12-16 caracteres.
* Complejidad: mayúsculas, minúsculas, números, símbolos.
* Cambio periódico: cada 90 días.
* No reutilizar últimas 5 contraseñas.
* Usar gestor de contraseñas corporativo.

Note: Las contraseñas siguen siendo el método de autenticación más común y el 81% de brechas las involucran. La clave está en equilibrar seguridad con usabilidad: longitud (16+ caracteres) más importante que complejidad, evitar cambios periódicos forzados que inducen patrones predecibles, nunca reutilizar entre sistemas, y usar gestor corporativo para contraseñas únicas ultra-seguras sin memorización. Una política efectiva reduce drásticamente el riesgo sin hacer la vida imposible a usuarios.


### 4.2. Autenticación multifactor (MFA)

**Segunda capa de seguridad:**

* Algo que **sabes** (contraseña).
* Algo que **tienes** (token, móvil).
* Algo que **eres** (huella, rostro).

**Obligatorio para:**
* Accesos administrativos.
* Acceso remoto (VPN).
* Sistemas críticos.

Note: MFA previene el 99.9% de ataques automatizados de compromiso de cuenta (Microsoft/Google). Combina factores de categorías diferentes: algo que SABES, algo que TIENES, algo que ERES. Incluso si roban tu contraseña por phishing, sin tu segundo factor (smartphone/token físico) no pueden acceder. Obligatoria para accesos admin, VPN remota, y sistemas críticos. Implementaciones: push notifications, códigos TOTP, o tokens hardware FIDO2 (más seguros anti-phishing). No implementar MFA en 2024 es negligencia inaceptable.


### 4.3. Política de pantalla bloqueada

**Protección ante ausencias:**

* Bloqueo **automático** tras 5-10 minutos de inactividad.
* Bloqueo **manual** obligatorio al ausentarse.
* Requiere contraseña para desbloquear.
* Protectores de pantalla no son suficientes.

Note: Un puesto desbloqueado es una invitación abierta a cualquiera para acceder a emails, sistemas, archivos, instalar malware o suplantar identidad. La política requiere dos componentes: bloqueo automático tras 5-10 minutos (red de seguridad configurada centralmente vía GPO), y bloqueo manual OBLIGATORIO al ausentarse (Win+L, Cmd+Ctrl+Q) que debe ser reflejo automático muscular. Protectores de pantalla NO son seguridad—solo ocultan visualmente. Verificar cumplimiento con auditorías walk-through aleatorias.


### 4.4. Política de escritorio limpio

**Clean Desk Policy:**

* No dejar documentos sensibles en el escritorio.
* Guardar papeles en cajones con llave.
* No notas con contraseñas pegadas.
* Al finalizar jornada, escritorio despejado.

Note: Clean Desk Policy es simple pero extremadamente efectiva contra ingeniería social y OSINT físico. Información visible (documentos confidenciales, diagramas de red, contraseñas en post-its—increíblemente común) puede fotografiarse con smartphone en segundos. Reglas: al terminar jornada guardar TODO en cajones con llave, nunca dejar credenciales anotadas visibles, triturar documentos confidenciales antes de desechar. En open office ser consciente de qué es visible desde posiciones de paso. Verificar con walk-throughs aleatorios.


### 4.5. Política de dispositivos USB

**Control de medios extraíbles:**

* **Prohibición** total (política más restrictiva).
* **Lista blanca** de dispositivos autorizados.
* **Escaneo** obligatorio de contenido antes de uso.
* **Cifrado** obligatorio en USBs corporativos.

Note: USBs son vectores extremadamente efectivos de malware (Stuxnet) y exfiltración de datos. "USB drop attacks" (dejar USBs infectados con etiquetas curiosas en parking/recepción) tienen 45-60% éxito. Opciones de política: A) prohibición total vía GPO, B) whitelist de USBs corporativos autorizados por hardware ID, C) permitir con escaneo antivirus obligatorio + DLP que bloquee copia de archivos confidenciales. Todo USB corporativo debe cifrar con BitLocker To Go. Complementar con awareness training.


### 4.6. Política de instalación de software

**Control de aplicaciones:**

* Solo software **aprobado** por TI.
* **Prohibición** de software personal/gratuito.
* Actualizaciones solo desde **fuentes oficiales**.
* Usuarios sin **permisos de administrador**.

Note: Software no autorizado es puerta trasera, vulnerabilidad, malware, fuga de datos o riesgo legal. Software "gratuito" frecuentemente incluye adware/spyware oculto. Política: solo software pre-aprobado en catálogo corporativo, usuarios SIN permisos admin local para prevenir instalaciones técnicamente, actualizaciones solo desde fuentes oficiales verificadas, proceso formal de solicitud con justificación de negocio. Enforced con controles técnicos: AppLocker/Gatekeeper en modo whitelist, inventario que detecte apps no autorizadas. Balance seguridad-productividad pero prevalece seguridad.


### 4.7. Política de uso aceptable (AUP)

**Usos permitidos y prohibidos:**

* **Permitido**: Uso profesional, formación relacionada.
* **Prohibido**: Descarga de contenido ilegal, gaming, torrents.
* **Monitorización**: La organización puede monitorizar actividad.
* **Consecuencias**: Sanciones por incumplimiento.

Note: AUP (Acceptable Use Policy) es documento contractual que establece usos permitidos/prohibidos de recursos IT, derechos de monitorización, y consecuencias de incumplimiento. Debe firmarse por TODOS durante onboarding—valor legal. Permitido: actividad profesional, formación laboral, uso personal mínimo razonable. Prohibido: contenido ilegal/inapropiado, software no autorizado, gaming, torrents, bypass de seguridad. Monitorización: organización se reserva derecho a monitorizar dispositivos/red/emails (legal si se informa LOPDGDD art. 87). Consecuencias escaladas: warning verbal→medidas disciplinarias→despido procedente. Equilibra productividad, privacidad y protección legal.

---

## 5. Trabajo remoto y BYOD


### 5.1. Desafíos del trabajo remoto

**Nuevos riesgos:**

* Redes WiFi domésticas **inseguras**.
* **Falta de control físico** del entorno.
* **Dificultad** en aplicar políticas de seguridad.
* Mezcla de **uso personal y profesional**.
* Mayor superficie de ataque.

Note: COVID-19 forzó transición masiva súbita a trabajo remoto sin preparación, exponiendo riesgos significativos persistentes. WiFi domésticas con WPA2-PSK y contraseñas débiles compartidas, routers sin actualizar con vulnerabilidades. Falta de control físico—familia, niños, visitas pueden ver pantallas/acceder equipos. Aplicar políticas es técnicamente más difícil fuera del perímetro corporativo. Mezcla inevitable de uso personal/profesional aumenta exposición. La superficie de ataque se multiplica—en vez de un perímetro único defendible, ahora cientos/miles de ubicaciones cada una con vulnerabilidades propias.


### 5.2. Política de trabajo remoto

**Medidas específicas:**

* **VPN obligatoria** para acceso a recursos corporativos.
* **Verificación de seguridad** WiFi doméstica.
* **Separación** de red doméstica (red invitados para trabajo).
* **Cifrado de disco** completo obligatorio.
* **Soporte remoto** IT disponible.

Note: Trabajo remoto requiere crear "perímetro virtual" robusto. VPN obligatoria cifra todo tráfico end-to-end protegiendo contra interceptación. Verificación seguridad WiFi doméstica: cambiar contraseña default del router, activar WPA3/WPA2 fuerte, deshabilitar WPS vulnerable. Separación de red doméstica creando VLAN o red invitados dedicada solo para trabajo aísla de dispositivos personales potencialmente comprometidos. Cifrado disco completo es AÚN MÁS crítico en remoto donde riesgo de robo físico/pérdida es significativamente mayor. IT debe proporcionar soporte remoto accesible multicanal.


### 5.3. BYOD (Bring Your Own Device)

**Uso de dispositivos personales:**

**Ventajas:**
* Ahorro de costes para empresa.
* Comodidad para empleado.

**Desventajas:**
* Control limitado de seguridad.
* Mezcla uso personal/profesional.
* Dificultad en borrado remoto.

Note: BYOD (Bring Your Own Device) permite usar dispositivos personales para trabajo. Ahorra 500-1500€/empleado en hardware pero introduce complejidades masivas de seguridad y gestión. Control limitado—no puedes forzar políticas estrictas sin consentimiento del propietario del dispositivo. Mezcla datos personales/corporativos crea problemas legales complejos de privacidad GDPR. Dificultad técnica y legal de borrado remoto selectivo solo de datos corporativos sin afectar datos personales. Muchas organizaciones maduras simplemente prohíben BYOD y proporcionan dispositivos corporativos dedicados—más caro upfront pero más simple, seguro y gestionable long-term.


### 5.4. Política BYOD

**Si se permite, requisitos mínimos:**

* **MDM** (Mobile Device Management) obligatorio.
* **Containerización** de datos corporativos.
* **Antivirus** actualizado.
* Sistema operativo **actualizado**.
* **Aceptación** de borrado remoto en caso de pérdida.

Note: Si se permite BYOD, MDM es obligatorio no opcional. La containerización crea "contenedor" cifrado separado a nivel kernel donde viven apps/datos corporativos completamente aislados de lo personal—usuario ve iconos con badge corporativo. El empleado debe aceptar por escrito borrado remoto selectivo del contenedor si pierde dispositivo o deja empresa, antivirus actualizado, y sistema operativo con últimos parches. Sin MDM con containerización, BYOD es ingobernable e inseguro.


### 5.5. Gestión de dispositivos móviles (MDM)

**Capacidades del MDM:**

* **Inventario** de dispositivos conectados.
* **Aplicación** de políticas de seguridad.
* **Actualización** remota de configuraciones.
* **Borrado remoto** (wipe) si se pierde dispositivo.
* **Geolocalización** de dispositivos corporativos.

Note: MDM es fundamental para gestionar flotas de dispositivos centralizada y remotamente—sin él, gestionar más de 10-20 es imposible. Capacidades: inventario automático de todos los dispositivos, aplicación remota de políticas a cientos simultáneamente, actualización de configuraciones on-the-fly, borrado remoto si se pierde/roba (protege datos aunque dispositivo esté en manos equivocadas), y geolocalización GPS para recuperar robados (debe estar en política por privacidad). Herramientas: Microsoft Intune, VMware Workspace ONE, MobileIron.

---

## 6. Protección técnica del puesto


### 6.1. Antivirus y antimalware

**Defensa básica obligatoria:**

* Instalación y **actualización automática**.
* Escaneo en **tiempo real**.
* Escaneo **programado** semanal completo.
* **Cuarentena** de archivos sospechosos.
* Reportar detecciones a consola central.

Note: Antivirus combina detección por firmas (malware conocido) con análisis heurístico (comportamientos sospechosos). Soluciones modernas EDR (Endpoint Detection & Response) añaden capacidades de investigación y respuesta automatizada. Configuración esencial: actualización automática de definiciones, escaneo en tiempo real de todo lo que se ejecuta/descarga, escaneo programado semanal completo del sistema, cuarentena automática de archivos sospechosos, y reporte a consola central para visibilidad IT. Es necesario pero no suficiente—no protege contra phishing o ingeniería social, por eso defensa en profundidad con múltiples capas.


### 6.2. Firewall personal

**Protección de red local:**

* **Activado** siempre, especialmente en público.
* Bloquear **conexiones entrantes** no solicitadas.
* Permitir solo **aplicaciones autorizadas**.
* Perfil **público** activado en redes no confiables.

Note: El firewall nativo de Windows/macOS es suficiente para mayoría—clave es configurarlo bien y NUNCA deshabilitarlo "temporalmente". Debe bloquear conexiones entrantes no solicitadas por defecto. El perfil público debe activarse automáticamente en redes WiFi no confiables (cafeterías, aeropuertos, hoteles) aplicando reglas más restrictivas que bloquean servicios como compartición de archivos que son seguros en red corporativa pero peligrosos en redes públicas hostiles donde hay atacantes escaneando activamente.


### 6.3. Cifrado de disco completo

**BitLocker (Windows) o FileVault (macOS):**

* Cifrado de **disco completo** (FDE - Full Disk Encryption).
* Protege datos si **roban** el dispositivo físico.
* Transparente para el usuario.
* Clave de recuperación en custodia de IT.

Note: Sin cifrado, cualquiera puede extraer el disco y leer TODOS los datos en minutos sin necesitar contraseña—solo arrancar desde USB o conectar disco a otro PC. Con cifrado completo BitLocker/FileVault, el disco robado es basura matemáticamente indescifrable. Es completamente transparente al usuario después del arranque inicial. Crítico: la clave de recuperación debe custodiarse por IT en ubicación segura porque si se pierde y usuario olvida contraseña, los datos son irrecuperables permanentemente incluso para legítimo propietario.


### 6.4. Actualizaciones de seguridad

**Patch management crítico:**

* Actualizaciones de **sistema operativo** automáticas.
* Actualizaciones de **aplicaciones** críticas.
* Parches de **seguridad** prioritarios (deploy en 48h).
* **Testing** previo en entorno controlado.

Note: Los exploits aparecen días u horas después de publicarse parche—atacantes hacen ingeniería inversa para descubrir vulnerabilidad. WannaCry 2017 explotó vulnerabilidad parcheada dos meses antes—quien no actualizó sufrió ransomware devastador. Parches críticos de seguridad deben desplegarse en 48-72h máximo. Testing previo es necesario en grandes organizaciones pero no puede retrasar tanto que amplifique ventana de vulnerabilidad. Balance entre estabilidad y seguridad—la seguridad suele ganar.


### 6.5. Control de puertos USB

**Restricción técnica:**

* **Deshabilitar** puertos USB via GPO o software.
* **Whitelist** de dispositivos autorizados por hardware ID.
* **Alertas** ante conexión de dispositivos no autorizados.
* **Cifrado** obligatorio en USBs corporativos.

Note: Control técnico via GPO o software endpoint es más efectivo que confiar en usuarios cumplan política—humanos olvidan o ignoran, sistemas nunca fallan. Deshabilitar puertos USB completamente o usar whitelist por hardware ID previene ataques USB drop (dejar USBs infectados con etiquetas curiosas en parkings—45-60% los conectan) y exfiltración trivial de gigas de datos confidenciales en segundos. Stuxnet se propagó así en instalaciones air-gapped sin internet. Alertar ante conexiones no autorizadas permite investigación inmediata.


### 6.6. Application whitelisting

**Solo software autorizado:**

* **Lista blanca** de aplicaciones permitidas.
* Bloqueo de **todo lo demás**.
* Herramientas: AppLocker (Windows), Gatekeeper (macOS).
* Actualización dinámica de whitelist.

Note: Application whitelisting (lista blanca) es más seguro que lista negra—en vez de bloquear malware conocido (infinito e imposible), solo permites software conocido confiable (finito y controlable). AppLocker en Windows Enterprise o Gatekeeper en macOS permiten ejecutar solo aplicaciones firmadas digitalmente y aprobadas explícitamente. Reduce drásticamente superficie de ataque bloqueando malware, herramientas de hacking, y software no autorizado aunque sea legítimo. Requiere mantenimiento de whitelist actualizada dinámicamente.


### 6.7. Backup del puesto de trabajo

**Respaldo de datos críticos:**

* Backup **automático** nocturno.
* Almacenamiento en **servidor central** o nube.
* Incluir carpetas de **usuario** (Documentos, Escritorio).
* **Exclusión** de software (reinstalable).
* Test de **restauración** trimestral.

Note: Usuarios pierden datos por fallos hardware (discos fallan sin aviso), borrados accidentales, ransomware que cifra todo. Backup automático nocturno a servidor central o nube es único salvavidas real. Debe incluir carpetas usuario (Documentos, Escritorio, Descargas) pero no software reinstalable. Crítico: test de restauración trimestral—un backup no verificado es backup que podría no funcionar cuando lo necesitas desesperadamente en crisis. Seguir regla 3-2-1: 3 copias, 2 medios diferentes, 1 offsite.

---

## 7. Formación y concienciación


### 7.1. Importancia de la formación

**El usuario como primera línea:**

* Tecnología sola **no es suficiente**.
* Usuario formado detecta **phishing**.
* Usuario concienciado sigue **políticas**.
* Usuario comprometido = organización comprometida.

Note: La tecnología más avanzada (firewalls, EDR, DLP) es inútil si usuario cae en phishing y entrega credenciales. El 90% de brechas exitosas empiezan con ingeniería social. Usuario formado detecta emails sospechosos, verifica remitentes extraños, no hace clic en enlaces dudosos, usa contraseñas seguras únicas, activa MFA voluntariamente, reporta incidentes inmediatamente. La formación convierte usuarios de eslabón más débil a primera línea de defensa activa humana complementando defensa técnica.


### 7.2. Programa de concienciación

**Elementos del programa:**

* Formación **inicial** para nuevos empleados.
* Formación **anual** de refuerzo para todos.
* **Simulacros** de phishing periódicos.
* **Newsletters** de seguridad mensuales.
* **Carteles** recordatorios en oficinas.

Note: Concienciación debe ser continua y repetitiva porque memoria humana se desvanece y amenazas evolucionan constantemente—phishing 2020 muy diferente a 2024 (ahora IA generativa crea emails perfectos). Formación inicial onboarding crea base, anual refuerza con amenazas actualizadas, simulacros proporcionan práctica realista, newsletters mensuales mantienen seguridad top-of-mind, carteles físicos refuerzan buenas prácticas diarias. Múltiples touchpoints repetidos crean hábitos de seguridad sostenidos en el tiempo.


### 7.3. Temas de formación

**Contenidos esenciales:**

* Identificación de **phishing** y spear-phishing.
* Creación de **contraseñas seguras**.
* Uso de **MFA**.
* **Ingeniería social** y cómo defenderse.
* Qué hacer ante un **incidente** sospechoso.

Note: Estos cinco temas cubren vectores de ataque más comunes explotando factor humano. Phishing/spear-phishing son vector #1 (verificar remitente/enlaces/urgencia artificial). Contraseñas seguras únicas con gestor previenen reutilización. MFA bloquea 99.9% ataques automatizados. Ingeniería social va más allá: vishing (llamadas), pretexting (inventar escenarios), tailgating físico. Qué hacer ante incidente: no apagar equipo, desconectar red si seguro, reportar inmediatamente IT/Seguridad. Personalizar a amenazas específicas del sector (healthcare ransomware, finanzas BEC).


### 7.4. Simulacros de phishing

**Entrenamiento práctico:**

* Envío de **emails falsos** de phishing a empleados.
* Monitorizar quién **hace clic**.
* Formación **inmediata** para quien cae.
* Sin **penalizaciones**, enfoque educativo.
* **Métricas** de mejora trimestral.

Note: Simulacros de phishing son mejor forma de medir efectividad real de formación—práctica realista en entorno seguro controlado. Herramientas como KnowBe4, Cofense, Proofpoint simulan emails maliciosos personalizados. Usuarios que hacen clic van a página explicativa (señales que debieron detectar) y reciben formación focalizada inmediata—aprender del error propio es más efectivo que teoría abstracta. Crítico: enfoque 100% educativo sin penalizaciones, objetivo es mejorar no castigar. Métricas trimestrales (% clic) muestran mejora—organizaciones maduras logran <5% vs 30-40% inicial.

---

## 8. Monitorización y cumplimiento


### 8.1. Necesidad de monitorización

**¿Por qué monitorizar?**

* Verificar **cumplimiento** de políticas.
* Detectar **anomalías** de comportamiento.
* Responder **rápidamente** a incidentes.
* **Evidencia** para investigaciones.

Note: Monitorización verifica que políticas definidas se cumplen realmente, detecta comportamientos anómalos indicando compromiso (acceso datos inusuales, login desde geolocalización imposible, descarga masiva archivos), permite respuesta rápida con alertas tiempo real, y proporciona evidencia forense para investigaciones. NO es espionaje abusivo si se hace transparentemente informando a empleados, proporcionalmente monitorizando solo necesario para seguridad, dentro marco legal LOPDGDD art. 87. Documentar en AUP firmado.


### 8.2. Qué monitorizar

**Aspectos a supervisar:**

* **Logs** de autenticación (exitosos y fallidos).
* **Instalación** de software.
* **Conexión** de dispositivos USB.
* **Tráfico** de red anómalo.
* Acceso a **recursos** sensibles.

Note: No monitorizar TODO o generaréis ruido abrumador ahogando señales importantes (alert fatigue—analistas ignoran alertas por volumen). Centraos en eventos seguridad relevantes: logs autenticación detectar brute-force o credential stuffing (múltiples fallos) o accesos desde ubicaciones sospechosas, instalación software detectar malware/herramientas hacking, conexión USB detectar exfiltración datos, tráfico red anómalo hacia dominios maliciosos o volumen inusual, accesos recursos sensibles detectar escalada privilegios o curiosidad no legítima. Calidad sobre cantidad.


### 8.3. Herramientas de monitorización

**Soluciones técnicas:**

* **SIEM**: Correlación de logs centralizados.
* **EDR**: Endpoint Detection and Response.
* **DLP**: Data Loss Prevention.
* **NAC**: Network Access Control.

Note: SIEM (Security Information Event Management como Splunk, QRadar, Azure Sentinel) agrega logs de múltiples fuentes y correlaciona eventos detectando patrones ataque complejos. EDR (Endpoint Detection Response como CrowdStrike, SentinelOne) monitoriza comportamiento endpoints detectando malware avanzado y permitiendo respuesta remota. DLP (Data Loss Prevention) previene datos sensibles salgan por email/USB/cloud. NAC (Network Access Control como Cisco ISE) verifica dispositivos cumplan políticas antes de acceso red. Ninguna es "instalar y olvidar"—requieren tuning continuo y analistas investigando alertas.


### 8.4. Aspectos legales de la monitorización

**Marco legal en España:**

* **Informar** a empleados de la monitorización.
* **Proporcionalidad**: Solo monitorizar lo necesario.
* **LOPDGDD** Artículo 87: Uso de dispositivos digitales.
* **Estatuto de Trabajadores**: Límites a vigilancia.

Note: Monitorización sin informar previamente a empleados puede ser ilegal en España. LOPDGDD art. 87 regula uso dispositivos digitales trabajo: empleadores pueden acceder a contenidos para controlar cumplimiento obligaciones laborales pero respetando dignidad y privacidad, deben informar previamente, monitorizar solo proporcional y necesario para fin legítimo. Estatuto Trabajadores art. 20.3 limita vigilancia: respetar dignidad y ser proporcional. Recomendación: documentar en AUP firmado, limitar a datos técnicos seguridad no contenido comunicaciones privadas, consultar legal.


### 8.5. Auditorías de cumplimiento

**Verificación periódica:**

* Auditoría **trimestral** de configuraciones.
* Verificación **semestral** de controles técnicos.
* Revisión **anual** completa de políticas.
* Pentesting **anual** de puestos de trabajo.

Note: Auditorías periódicas descubren inevitable gap entre políticas definidas en papel y realidad implementada en campo—lo documentado vs lo que realmente ocurre. Trimestral: verificar sistemas mantienen configuraciones seguridad (cifrado activo, firewall encendido, parches aplicados). Semestral: testear efectividad controles (¿DLP realmente bloquea exfiltración?). Anual: actualizar políticas reflejando cambios tecnológicos/organizativos/amenazas emergentes, pentesting simula atacante real identificando vulnerabilidades antes que atacantes reales. Auditorías esenciales para mejora continua ciclo PDCA Plan-Do-Check-Act.

---

## 9. Gestión de incidentes en el puesto


### 9.1. Tipos de incidentes comunes

**Incidentes típicos:**

* **Malware** detectado.
* **Phishing** exitoso.
* **Pérdida** o robo de dispositivo.
* **Acceso no autorizado** a cuenta.
* **Fuga** de información.

Note: Estos cinco incidentes representan >80% casos en puestos trabajo. Malware detectado (antivirus alerta, comportamiento extraño sistema). Phishing exitoso (usuario hizo clic enlace, descargó adjunto, proporcionó credenciales). Pérdida/robo dispositivo (laptop robada coche, móvil olvidado taxi). Acceso no autorizado cuenta (alguien conoce contraseña, sesión secuestrada). Fuga información (datos sensibles compartidos inadvertidamente, email destinatario equivocado). Cada organización debe tener procedimientos documentados formales accesibles especificando exactamente qué hacer—no improvisar durante crisis.


### 9.2. Procedimiento de reporte

**¿Qué debe hacer el usuario?**

1. **No apagar** el equipo (preservar evidencias).
2. **Desconectar** de red si es seguro.
3. **Notificar** a IT/Seguridad inmediatamente.
4. **Documentar** qué observó y cuándo.
5. **No investigar** por cuenta propia.

Note: Velocidad de reporte es crítica—cada minuto cuenta en contención porque malware se propaga, atacantes exfiltran más datos, daño se amplifica. Usuarios deben saber exactamente a quién llamar (número directo IT/Seguridad, email abuse@, portal interno) y qué información proporcionar (qué observaron, cuándo exactamente, qué hicieron antes). Regla oro: NO apagar equipo (borra evidencias RAM), desconectar ethernet/WiFi si seguro prevenir propagación lateral, NO investigar por cuenta propia ni "probar cosas", documentar todo mientras memoria fresca.


### 9.3. Respuesta a malware

**Pasos del equipo IT:**

1. **Aislar** el equipo afectado.
2. **Identificar** el tipo de malware.
3. **Eliminar** la amenaza.
4. **Verificar** que no haya lateral movement.
5. **Restaurar** desde backup si necesario.
6. **Analizar** causa raíz.

Note: Respuesta debe ser rápida pero metodológica siguiendo procedimiento formal no pánico improvisado. Aislar equipo física (desconectar cables) y lógicamente (bloquear MAC/IP) previene propagación lateral. Identificar tipo malware (ransomware, trojan, rootkit) con análisis forense permite respuesta específica. Eliminar con antivirus especializado o herramientas remediación. Verificar sin movimiento lateral inspeccionando logs red y otros endpoints. Restaurar desde backup verificado limpio si muy comprometido. Analizar causa raíz (¿phishing? ¿USB? ¿vulnerabilidad sin parchar?) prevenir recurrencia. No borrar evidencias prematuramente.


### 9.4. Respuesta a pérdida de dispositivo

**Protocolo de dispositivo perdido/robado:**

1. Reporte **inmediato** por el usuario.
2. IT ejecuta **borrado remoto** (MDM).
3. **Cambio** de contraseñas de cuentas accedidas.
4. **Revisión** de actividad reciente de la cuenta.
5. **Denuncia** policial si es robo.
6. **Lecciones aprendidas** del incidente.

Note: Borrado remoto solo funciona si dispositivo se conecta internet después robo—por eso cifrado disco es primera y más importante defensa (protege incluso si borrado falla). Usuario debe reportar pérdida/robo inmediatamente (minutos no horas) minimizar ventana exposición. IT ejecuta wipe remoto vía MDM próxima vez dispositivo encienda y conecte. Cambiar INMEDIATAMENTE todas contraseñas accesibles desde dispositivo (email, VPN, sistemas). Revisar logs actividad buscando accesos sospechosos antes/después pérdida. Denunciar policía si robo con número serie. Post-mortem: ¿cómo mejorar prevención?

---

## 10. Conclusión


### 10.1. Resumen de conceptos clave

* **Puesto de trabajo**: Punto crítico de acceso a información.
* **Políticas**: Definen qué debe hacerse.
* **Estándares**: ISO 27001, GDPR, ENS proporcionan marco.
* **Protección técnica**: Múltiples capas de defensa.
* **Formación**: Usuario concienciado es mejor defensa.

Note: Protección del puesto NO es medida única silver bullet sino sistema integrado de controles técnicos (antivirus, firewall, cifrado, MDM), organizativos (políticas, procedimientos, auditorías), y humanos (formación, concienciación, cultura seguridad) trabajando sinérgicamente. Cada control complementa y refuerza demás. Políticas definen el qué, controles técnicos lo hacen ejecutable y auditable, formación asegura personas entiendan por qué y cómo. Es arquitectura seguridad holística no checklist tecnologías a comprar.


### 10.2. Defensa en profundidad

**Capas de protección:**

1. Política y concienciación.
2. Autenticación fuerte (MFA).
3. Antivirus y firewall.
4. Cifrado.
5. Monitorización.
6. Respuesta a incidentes.

Note: Si una capa falla, demás siguen protegiendo—esencia de defensa en profundidad o defense in depth, concepto militar aplicado a ciberseguridad. Ejemplo: usuario cae phishing proporcionando contraseña (falla capa 1 concienciación) → MFA bloquea acceso sin segundo factor (capa 2) → si MFA también comprometida, monitorización detecta login desde geolocalización anómala (capa 5) → respuesta incidentes contiene daño (capa 6). Ninguna capa es perfecta 100% pero combinadas crean seguridad robusta resiliente. No confiar en una sola—redundancia es fortaleza.


### 10.3. Responsabilidad compartida

**Seguridad es tarea de todos:**

* **Dirección**: Aprobar políticas y presupuesto.
* **IT/Seguridad**: Implementar controles técnicos.
* **Usuarios**: Seguir políticas y reportar incidentes.
* **RRHH**: Formar y gestionar incumplimientos.

Note: Seguridad NO es responsabilidad exclusiva IT/Seguridad—requiere compromiso y colaboración activa de toda organización a todos niveles. Un solo eslabón débil (usuario cae phishing, director exige excepción políticas, IT posterga parches) puede comprometer toda cadena. Dirección debe aprobar políticas, asignar presupuesto adecuado, dar ejemplo cumpliendo primero. IT/Seguridad implementan controles pero no pueden estar en cada escritorio. Usuarios son primera línea: siguen políticas, reportan incidentes, mantienen vigilancia. RRHH gestiona ciclo empleado. Seguridad es cultura organizativa no proyecto IT.

---

## 11. Políticas de seguridad INCIBE


### 11.1. Políticas INCIBE para PYMEs

**Documentos de referencia para protección:**

* Políticas sector ializadas para pequeñas y medianas empresas
* Formato PDF y Word editable
* Incluyen checklists de verificación
* Adaptables a contexto específico
* Disponibles gratuitamente en INCIBE

Note: INCIBE desarrolló políticas seguridad específicas para PYMEs españolas mejoren ciberseguridad de forma práctica y asequible. Son documentos profesionales que guían empresa en procesos internos necesarios proteger información e infraestructura digital organizadamente y medible. Disponibles gratuitamente en web INCIBE en formatos editables (PDF y Word) para personalizar según contexto particular. No son meramente teóricos sino herramientas prácticas con checklists ejecutables y roles claramente definidos. Eliminan barrera de tener que desarrollar políticas desde cero.


### 11.2. ¿Qué contienen estas políticas?

**Elementos principales:**

* **Aspectos de seguridad esenciales**: Áreas críticas a proteger
* **Roles y responsabilidades**: Empresario, técnico, empleados
* **Checklists**: Acciones concretas por grupo
* **Formatos editables**: Personalizables según empresa
* **Guías de seguimiento**: Cómo medir cumplimiento

Note: Cada política INCIBE cubre aspectos fundamentales seguridad que deben supervisarse y gestionarse activamente: protección equipos, control accesos, gestión aplicaciones, almacenamiento datos. Toda PYME identifica áreas clave donde aplicar controles adaptándolos según necesidades y recursos. Roles claramente definidos: empresario (decisiones estratégicas, aprueba políticas, asigna presupuesto), equipo técnico (implementa técnicamente), empleados (aplican buenas prácticas diarias). Checklists con acciones específicas medibles para cada grupo facilitan implementación práctica transformando conceptos abstractos en pasos verificables concretos.


### 11.3. Estructura de los documentos INCIBE

**Secciones estándar de cada política:**

1. **Antecedentes**: Justificación y contexto de la política
2. **Objetivos**: Qué busca lograr la política
3. **Checklist**: Lista de controles (medidas) por nivel y alcance
4. **Puntos Clave**: Prácticas o reglas esenciales a cumplir
5. **Referencias**: Enlaces a normativas y guías relacionadas

Note: Documentos políticas INCIBE siguen estructura común facilitando lectura, comprensión e implementación. Antecedentes: justifican por qué necesaria la política basándose en riesgos identificados. Objetivos: establecen qué busca lograr en términos seguridad/control/prevención. Checklist: parte más práctica—lista controles clasificados por nivel complejidad (Básico/Avanzado) y alcance (Procesos/Tecnología/Personas) permitiendo priorizar implementación. Puntos Clave: resumen prácticas/reglas esenciales que todos deben cumplir. Referencias: enlaces normativas externas (ISO 27001, GDPR, LOPDGDD) o guías complementarias.


### 11.3. Estructura de los documentos INCIBE II

**Relación con conceptos vistos:**

* **Antecedentes** → Elementos del puesto + Escenarios de riesgo
* **Objetivos** → Política (declaración de intenciones)
* **Checklist** → Medidas Básicas/Avanzadas + PRO/TEC/PER
* **Puntos Clave** → Normativas específicas
* **Referencias** → ISO 27001, GDPR, LOPDGDD

Note: La estructura INCIBE se corresponde perfectamente con conceptos estudiados. Antecedentes conectan con identificación elementos vulnerables puesto trabajo y escenarios riesgo—establecen el "por qué". Objetivos son la Política—declaración general intenciones y compromiso. Checklist aplica clasificación medidas por complejidad (Básico/Avanzado) y alcance (PRO/TEC/PER)—herramienta clave evaluar y medir cumplimiento y nivel madurez seguridad empresa. Puntos Clave son Normativas—reglas y requisitos específicos cumplirse. Referencias fortalecen política alineándola con regulaciones y estándares externos ISO 27001, GDPR, LOPDGDD.


### 11.4. Ejemplo: Protección del Puesto de Trabajo

**Controles incluidos (ejemplos del checklist):**

* **[B-PER]** Política de bloqueo de sesión configurada
* **[B-PER]** Política de escritorio limpio implementada
* **[A-TEC]** Desactivación de puertos USB por defecto
* **[A-TEC]** Cifrado de disco completo activado
* **[B-PRO]** Procedimiento de reporte de dispositivos perdidos

Note: Ejemplos checklist "Protección puesto trabajo" INCIBE. Notación: [Nivel-Alcance]. Controles Básicos Personas (B-PER) como bloqueo sesión son asequibles sin conocimientos técnicos avanzados—configurar bloqueo automático y educar usar Win+L. Escritorio limpio solo requiere disciplina organizativa. Controles Avanzados Tecnología (A-TEC) requieren inversión y conocimiento especializado: desactivación USB implica GPOs o herramientas endpoint, cifrado disco requiere hardware compatible (TPM), configuración técnica BitLocker/FileVault, gestión claves recuperación. Controles Procesos (B-PRO) establecen procedimientos organizativos como documentar y comunicar cómo reportar dispositivos perdidos.


### 11.5. Cómo utilizar las políticas INCIBE

**Pasos prácticos para implementación:**

1. **Descargar** políticas relevantes desde web INCIBE
2. **Identificar** elementos de seguridad esenciales de tu organización
3. **Asignar** roles y responsabilidades claras (dirección, IT, empleados)
4. **Adaptar** políticas editables a tu contexto específico
5. **Usar checklist** para registrar qué se implementó y qué falta
6. **Medir progreso** y priorizar acciones pendientes

Note: Pasos implementación real: 1) Descargar desde incibe.es/empresas/herramientas/politicas el paquete o políticas específicas necesarias (ZIP con PDFs y Words). 2) Revisar puntos clave identificando aspectos seguridad controlar en organización—priorizar (ej: Protección puesto y Almacenamiento más urgentes que Teletrabajo si no hay remote workers). 3) Asignar responsabilidades: dirección aprueba/asigna presupuesto, IT implementa controles técnicos, empleados siguen prácticas diarias. 4) Personalizar versiones Word: nombre empresa, ejemplos sector, ajustar medidas a recursos. 5) Usar checklist como plan acción: marcar qué YA está implementado, identificar qué falta. 6) Revisar progreso trimestral/semestral visualizando mejora continua.


### 11.6. Políticas disponibles en INCIBE

**Conjunto completo de políticas:**

* Protección del puesto de trabajo
* Almacenamiento en equipos de trabajo
* Aplicaciones permitidas
* Política de contraseñas
* Política de teletrabajo
* Copias de seguridad
* Y muchas más especializadas

Note: INCIBE ofrece catálogo completo políticas cubriendo aspectos seguridad relevantes PYMEs. Protección puesto trabajo (estudiado en detalle unidad). Almacenamiento equipos (qué guardar localmente, cifrado, medios extraíbles). Aplicaciones permitidas (repositorio software autorizado, auditoría instalaciones). Contraseñas (requisitos complejidad, gestión, no reutilización). Teletrabajo (medidas adicionales remoto: VPN obligatoria, seguridad WiFi). Copias seguridad (qué, cuándo, dónde, cómo). Existen también gestión proveedores, MDM, gestión incidentes. Recomendación: comenzar con 3-4 más críticas, implementarlas bien, gradualmente ampliar. Mejor 4 políticas realmente cumplidas que 15 solo papel.


### 11.7. Beneficios de usar políticas INCIBE

**Ventajas prácticas:**

* **Gratuitas** y profesionalmente desarrolladas
* **Adaptadas** al contexto PYME español
* **Editables** para personalización
* **Completas** con checklists ejecutables
* **Alineadas** con normativa española (LOPDGDD) y europea (GDPR)
* **Actualizadas** periódicamente por INCIBE

Note: Ventajas usar políticas INCIBE para PYMEs: completamente gratuitas (consultoría desarrollar desde cero cuesta miles euros), profesionalmente desarrolladas por expertos garantizando calidad, adaptadas a realidad PYMEs españolas con medidas proporcionales y realistas, editables para personalizar según sector/tamaño/necesidades, checklists prácticos transforman conceptos abstractos en acciones concretas verificables, alineadas con normativas legales aplicables España/Europa (LOPDGDD/GDPR) ayudando cumplimiento, actualizadas periódicamente reflejando amenazas emergentes, demuestran diligencia debida legal y reputacionalmente si ocurre incidente.

---

## Bibliografía

* [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) - Information Security Management
* [GDPR](https://gdpr-info.eu/) - General Data Protection Regulation
* [CCN-STIC 800](https://www.ccn-cert.cni.es/series-ccn-stic/800-guia-esquema-nacional-de-seguridad.html) - Guías ENS
* [INCIBE - Protección del puesto de trabajo](https://www.incibe.es/)
* LOPDGDD - Ley Orgánica 3/2018

Note: Estos recursos son fundamentales y de acceso gratuito. Dedicad tiempo a estudiarlos en profundidad, especialmente ISO 27001 y GDPR.
