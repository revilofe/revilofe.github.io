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


### 2.1. ¿Qué es una normativa?

**Normativa**: Conjunto de reglas y requisitos específicos para garantizar un ambiente de trabajo seguro.

**Objetivos:**
* Definir cómo gestionar y asegurar el puesto.
* Proteger información y sistemas.
* Minimizar riesgos y vulnerabilidades.
* Establecer responsabilidades claras.

Note: La normativa establece reglas claras que todos deben seguir para garantizar seguridad, como el código de circulación en tráfico. Define cómo gestionar acceso físico/lógico, uso de dispositivos, instalación de software, gestión de contraseñas, políticas de escritorio limpio, y procedimientos ante incidentes. Sin normativa clara, cada empleado sigue sus propios criterios creando vulnerabilidades.


### 2.1. ¿Qué es una normativa? II

**Ejemplo práctico de normativa:**

* **Restricciones de acceso**: Solo personal autorizado accede
  a datos confidenciales.
* **Seguridad física/digital**: Cerraduras, contraseñas complejas, MFA.
* **Actualizaciones**: Software actualizado con últimos parches.
* **Buenas prácticas**: Bloquear pantalla, evitar redes públicas.

Note: Traduciendo normativa a medidas concretas: restricciones de acceso aplican principio de mínimo privilegio (acceder solo a datos necesarios para tu función), seguridad física incluye cajones con llave y control de acceso con tarjetas, seguridad digital requiere contraseñas 12+ caracteres con complejidad y MFA para sistemas críticos, actualizaciones críticas en 48h máximo, y buenas prácticas como bloquear pantalla al ausentarse (Win+L) y usar VPN en redes públicas.


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

Note: Los permisos excesivos son uno de los riesgos más comunes y menos gestionados. Ocurre constantemente: un empleado necesita acceso temporal a una carpeta para un proyecto, se le da acceso, el proyecto termina, pero el acceso nunca se revoca. Cinco años después, tiene acceso a decenas de sistemas y carpetas que no necesita. Si su cuenta se compromete, el atacante tiene acceso lateral a múltiples sistemas. El procedimiento implementa mínimo privilegio mediante plantillas de rol—IT tiene definido qué permisos tiene un "Analista de Ventas Junior", un "Desarrollador Senior", un "Gestor de Proyectos", etc. Cuando se incorpora alguien, se le asigna el rol apropiado automáticamente. Si necesita acceso excepcional (por ejemplo, acceder a datos financieros para un proyecto especial), debe solicitarlo vía formulario formal, su manager debe aprobar, y se concede con fecha de expiración (3-6 meses). Al acercarse la expiración, el sistema notifica al empleado para renovar si sigue siendo necesario—si no renueva, se revoca automáticamente. Trimestralmente, IT audita los permisos contra los roles actuales y revoca discrepancias. Esto requiere integración con el sistema HR (HRIS) para automatizar al tas (nuevo empleado → permisos), bajas (empleado sale → revocar TODO inmediatamente), y cambios (cambio de departamento → ajustar permisos).


### 2bis.5.2. Acceso No Autorizado a Información Confidencial

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas sin autorización acceden o visualizan datos sensibles.
* **Política**: Proteger información confidencial con controles estrictos.
* **Normativa**: Información confidencial requiere autenticación multifactor.
  Accesos registrados y auditados. Clasificación de datos obligatoria.
* **Procedimiento**: Activar MFA en sistemas críticos. IT configura
  auditoría de accesos. Empleados deben clasificar documentos (Público,
  Interno, Confidencial, Restringido).

Note: El acceso no autorizado puede ser accidental (empleado curioso) o malicioso (insider threat, atacante con credenciales robadas). Para prevenirlo se requieren múltiples controles. Primero, autenticación multifactor (MFA) en sistemas que contienen información confidencial—incluso si roban la contraseña, no pueden acceder sin el segundo factor. Segundo, auditoría de accesos—todos los accesos a información clasificada como Confidencial o superior deben registrarse automáticamente en logs centralizados (SIEM) que permitan responder "¿quién accedió a qué, cuándo?". Si ocurre una brecha, la auditoría permite investigación forense. Tercero, clasificación de datos—los empleados deben marcar documentos según sensibilidad: Público (no hay problema si se expone), Interno (solo empleados), Confidencial (solo personal autorizado), Restringido (solo roles específicos). En documentos Word/Excel, usar herramientas de clasificación (Microsoft Information Protection, Trellix DLP) que añaden metadatos y watermarks. Los sistemas de DLP pueden entonces aplicar políticas automáticas basadas en clasificación (por ejemplo, bloquear envío externo de documentos marcados Confidencial).


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

Note: La compartición insegura de información es causa frecuente de brechas. Ocurre cuando empleados usan métodos convenientes pero inseguros: email personal (Gmail, Hotmail) para "continuar trabajando en casa", WhatsApp personal para enviar documentos "rápidamente" a compañeros, USBs sin cifrar para trasladar archivos entre locaciones, WeTransfer gratuito para enviar archivos grandes a clientes. Todos estos métodos están fuera del control corporativo, generalmente sin cifrado, y crean copias de datos corporativos en sistemas no gestionados. El procedimiento establece que toda compartición de información debe usar plataformas corporativas: para compartición interna, SharePoint/OneDrive for Business o Google Workspace empresarial donde IT puede auditar, aplicar DLP, y revocar accesos. Al compartir: clic derecho en archivo, Compartir, introducir emails específicos de destinatarios autorizados (no "cualquiera con el enlace"), establecer permisos mínimos necesarios (Ver en lugar de Editar salvo necesidad), establecer fecha de expiración (30-90 días). Para compartir con externos (clientes, proveedores), usar portal de intercambio seguro de archivos (Citrix ShareFile, Accellion Kiteworks, Box) que requiere autenticación del destinatario, cifra en tránsito y reposo, y permite auditoría completa.


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

Note: Sin auditoría de accesos, los accesos no autorizados son invisibles hasta que causan daño (brecha descubierta meses después). La auditoría proactiva permite detectar y responder rápidamente. El procedimiento requiere que IT configure logging comprehensivo: todos los accesos a file shares, SharePoint, bases de datos, aplicaciones críticas deben enviar logs a un SIEM (Security Information and Event Management) centralizado como Splunk, QRadar, Sentinel, o ELK Stack. El SIEM correlaciona eventos de múltiples fuentes y puede detectar patrones anómalos: un usuario que normalmente accede 10 archivos/día de repente accede 10,000 (posible exfiltración masiva), un usuario que trabaja 9-17h de repente accede a las 3am (cuenta comprometida o actividad sospechosa), un usuario que solo accede desde IP española de repente accede desde IP china (cuenta comprometida). El SIEM genera alertas automáticas que el SOC (Security Operations Center) investiga. Para organizaciones sin SOC 24/7, al menos tener alertas por email/SMS para eventos críticos (admin accede a datos de RRHH, acceso a tabla de contraseñas, descarga masiva de datos). Revisar dashboards semanalmente buscando patrones: ¿quiénes son los top 10 usuarios con más accesos? ¿Hay accesos a recursos que no deberían tocar? ¿Hay intentos fallidos repetidos (posible ataque de fuerza bruta)?


### 2bis.6. Personal

**El empleado y su comportamiento:**

* Conocimiento de políticas de seguridad
* Hábitos de trabajo diarios (bloqueo, contraseñas)
* Capacidad de reconocer amenazas (phishing, ingeniería social)
* Actitud ante la seguridad (¿prioridad o molestia?)
* Respuesta ante incidentes sospechosos

Note: El personal—el factor humano—es simultáneamente el eslabón más débil y la defensa más importante de la seguridad. La tecnología puede fallar, pero un empleado bien formado y concienciado puede detectar y prevenir ataques que bypassean controles técnicos. Por el contrario, un empleado despreocupado o malicioso puede comprometer completamente la seguridad más robusta. Los cuatro escenarios principales relacionados con el personal son: falta de concienciación (ignorancia de riesgos y buenas prácticas), hábitos inseguros (atajos que comprometen seguridad), vulnerabilidad a ingeniería social (ser engañado por atacantes), y desconocimiento o incumplimiento deliberado de políticas. Todos estos son prevenibles con formación adecuada, pero requieren un programa continuo de concienciación, no solo un training al incorporarse.


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

Note: La falta de concienciación es el problema fundamental—los empleados no saben qué es peligroso. No reconocen phishing, usan contraseñas débiles porque "es más fácil de recordar", descargan archivos de fuentes dudosas, conectan USBs encontrados en parking ("a ver qué tiene"), comparten credenciales "para ayudar a un compañero". Todo esto ocurre por ignorancia, no malicia. El procedimiento establece programa obligatorio y medible de concienciación. Primero, formación base: todos los empleados completan curso e-learning anual (típicamente 2-3 horas) que cubre amenazas actuales (phishing, ransomware, ingeniería social), buenas prácticas (contraseñas seguras, MFA, navegación segura), políticas corporativas, y qué hacer ante incidentes. El curso termina con evaluación—deben aprobar con 80%+ o repetir. Segundo, simulacros de phishing: trimestral mente, el equipo de seguridad envía emails de phishing simulados a todos los empleados. Los que hacen clic quedan registrados y reciben formación inmediata (correo explicando qué señales debieron detectar). Los reincidentes reciben formación presencial más intensiva. Tercero, formación específica por rol: los administradores de sistemas reciben formación avanzada sobre amenazas APT, RRHH sobre protección de datos personales, etc. La formación debe actualizarse anualmente porque las amenazas evolucionan (deepfakes, ataques con IA generativa, etc.).


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

Note: Los hábitos inseguros se desarrollan gradualmente por conveniencia—"solo me ausento un segundo", "es más fácil recordar si uso la misma contraseña", "guardar en el cajón es molesto". Cada atajo parece inofensivo individualmente pero colectivamente crean vulnerabilidades masivas. El procedimiento combina recordatorios y auditorías para reforzar hábitos. Primero, recordatorios visuales: pósters en áreas comunes ("¿Bloqueaste tu pantalla?", "Clean desk = Secure desk"), salvapantallas con mensajes de seguridad, email mensual del CISO con consejos. Segundo, auditorías aleatorias: equipo de seguridad (o managers) hacen "security walk-throughs" sin previo aviso—recorren las oficinas al final del día verificando: ¿hay pantallas desbloqueadas? ¿Hay documentos confidenciales en escritorios? ¿Hay post-its con contraseñas? ¿Hay USBs dejados conectados? No es ejercicio punitivo sino educativo—si encuentran escritorio con documentos, dejan nota cortés: "Encontramos documentos confidenciales en tu escritorio. Recuerda la política Clean Desk. Cualquier duda, contacta seguridad". Para reincidentes, escalación a manager. También feedback positivo: "Este mes, el 95% de escritorios estaban limpios, ¡excelente trabajo!". El objetivo es crear cultura donde seguridad sea "lo normal" y no cumplir sea "incómodo socialmente".


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

Note: La ingeniería social explota psicología humana: urgencia ("tu cuenta será suspendida si no actúas ya"), autoridad ("esto viene del CEO"), reciprocidad ("te ayudé antes, ahora ayúdame tú"), curiosidad ("mira esta foto tuya que encontré"). Los atacantes son expertos manipuladores. El phishing es la forma más común: email que parece legítimo (banco, Microsoft, CEO de la empresa) pidiendo clic en enlace, descarga de adjunto, o proporcionar credenciales. El vishing (phishing por voz/teléfono) y smishing (SMS) también son frecuentes. El procedimiento enseña técnica "STOP-THINK-CONNECT": STOP—pausar, no actuar impulsivamente ante emails urgentes. THINK—analizar indicadores de phishing: ¿el remitente es la dirección real o similar pero incorrecta (microsft.com en lugar de microsoft.com)? ¿El lenguaje tiene errores gramaticales? ¿Solicita acciones inusuales? ¿Hay sensación artificial de urgencia? CONNECT (o no)—si pasa el análisis, proceder; si hay dudas, verificar por canal independiente. Para solicitudes financieras o cambios de datos bancarios por email, SIEMPRE verificar llamando al número conocido del proveedor (no al que viene en el email sospechoso)—los ataques BEC (Business Email Compromise) han causado pérdidas de millones con emails falsos pidiendo transferencias urgentes. Entrenar con simulacros realistas para que empleados desarrollen "spidey sense" ante solicitudes raras.


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

Note: El incumplimiento deliberado ocurre cuando el empleado conoce la política pero la ignora porque es "inconveniente", porque "nadie la cumple", o porque no cree en su importancia. Es crítico distinguir entre desconocimiento (solución: formación) e incumplimiento deliberado (solución: consecuencias). El procedimiento comienza con el compromiso formal: todos los nuevos empleados, durante onboarding, reciben formación sobre políticas de seguridad y firman documento de "Aceptación de Políticas" que indica que han leído, entendido y se comprometen a cumplir. Este documento tiene valor legal y puede usarse en caso de incidente grave. Cuando hay actualizaciones importantes de políticas (por ejemplo, nueva política de trabajo remoto), se comunica a todos y deben aceptar nuevamente. Las auditorías técnicas y físicas (mencionadas en otros puntos) detectan incumplimientos. El proceso de escalación es: Primera vez—conversación con manager + email formal de warning + formación de refuerzo (enfoque educativo: asumimos que fue error). Segunda vez—medida disciplinaria formal según política de RRHH (puede ser amonestación escrita, suspensión temporal, según gravedad y normativa laboral local). Tercera vez o incumplimiento muy grave (por ejemplo, compartir deliberadamente credenciales con externos)—despido procedente. Lo importante es ser consistente: si no hay consecuencias reales, las políticas se vuelven papel mojado. Pero también celebrar cumplimiento: programas de "Security Champions", reconocimientos a empleados que reportan incidentes o demuestran excelentes prácticas.

---

## 3. Estándares aplicables


### 3.1. ISO/IEC 27001

**Estándar internacional de gestión de seguridad:**

* Marco para **Sistema de Gestión de Seguridad de la Información (SGSI)**.
* Anexo A incluye controles para puestos de trabajo.
* Cubre seguridad en estaciones y control de accesos.
* Evaluación y mitigación de riesgos.

Note: ISO/IEC 27001 es el estándar internacional más reconocido y respetado para la gestión de la seguridad de la información a nivel mundial. Proporciona un marco sistemático para establecer, implementar, mantener y mejorar continuamente un Sistema de Gestión de Seguridad de la Información (SGSI). El estándar es aplicable a organizaciones de cualquier tamaño y sector, desde PYMEs hasta multinacionales. Su Anexo A contiene 114 controles de seguridad organizados en 14 dominios, incluyendo controles específicos para la protección de puestos de trabajo como la seguridad física de las estaciones, políticas de escritorio limpio, control de acceso lógico, protección contra malware, y gestión de activos. Certificarse en ISO 27001 (como profesional mediante cursos ISO 27001 Lead Implementer o Lead Auditor) es altamente valorado en el mercado laboral internacional y abre puertas en cualquier país del mundo. Las organizaciones certificadas en ISO 27001 demuestran a clientes, socios y reguladores que gestionan la seguridad de la información con rigor y siguiendo mejores prácticas reconocidas internacionalmente.


### 3.2. Controles ISO 27001 relevantes

**Controles del Anexo A para puestos:**

* **A.7.2** Control de acceso físico.
* **A.8.1** Inventario de activos.
* **A.8.3** Uso aceptable de activos.
* **A.11.2** Seguridad de equipos.
* **A.12.3** Copias de seguridad.

Note: El Anexo A de ISO 27001:2022 (versión actual) contiene 93 controles organizados en 4 temas: Organizacionales (37 controles), Personas (8 controles), Físicos (14 controles), y Tecnológicos (34 controles). Para la protección del puesto de trabajo son especialmente relevantes: Control A.7.2 sobre seguridad física de áreas que incluye control de acceso a oficinas y espacios de trabajo; A.8.1 sobre inventario de activos que requiere mantener registro actualizado de todos los dispositivos y software en uso; A.8.3 sobre uso aceptable de activos que define cómo los empleados pueden usar equipos y datos corporativos; A.11.2 sobre equipamiento que cubre protección física de equipos contra robos, daños ambientales y acceso no autorizado; y A.12.3 sobre copias de seguridad que asegura que la información crítica tenga backup regular y verificado. Cada uno de estos controles tiene objetivos específicos, guías de implementación, y puede ser auditado durante una certificación ISO 27001. Estudiad estos controles en detalle porque son la base de cualquier política robusta de protección del puesto de trabajo y son frecuentemente evaluados en auditorías de seguridad y cumplimiento normativo.


### 3.3. GDPR

**Reglamento General de Protección de Datos (UE):**

* Protege **privacidad y datos personales**.
* Exige seguridad en acceso y almacenamiento.
* Cifrado y contraseñas seguras obligatorias.
* Notificación de brechas en 72 horas.

Note: El GDPR (General Data Protection Regulation) o Reglamento (UE) 2016/679 es LA normativa más importante sobre protección de datos personales en Europa y tiene alcance extraterritorial—afecta a cualquier organización en el mundo que procese datos de ciudadanos europeos. Entró en vigor en mayo de 2018 y ha transformado radicalmente cómo las organizaciones deben gestionar datos personales. El GDPR no es opcional ni negociable para ninguna organización que opere en Europa o con clientes europeos. Establece principios fundamentales como minimización de datos (solo recoger lo necesario), limitación de propósito (usar datos solo para lo declarado), exactitud, limitación de almacenamiento, integridad y confidencialidad. Las multas por incumplimiento son severas y reales: hasta 20 millones de euros o el 4% de la facturación anual global (lo que sea mayor). Google fue multada con 50M€ en 2019, Amazon con 746M€ en 2021, y Meta con 1,200M€ en 2023—las multas son reales y duelen. Específicamente para el puesto de trabajo, el GDPR exige que cualquier dispositivo que procese datos personales (nombres, emails, DNIs, direcciones, datos financieros, datos de salud, etc.) esté protegido con medidas técnicas y organizativas apropiadas incluyendo cifrado, control de acceso, y capacidad de auditoría. Como profesionales de IT y seguridad, debéis tomároslo extremadamente en serio.


### 3.4. Implicaciones GDPR en el puesto

**Requisitos específicos:**

* Solo acceder a datos personales si es **necesario** para el trabajo.
* Usar **conexiones seguras** (VPN) para acceso remoto.
* **Cifrar** dispositivos que contengan datos personales.
* **No compartir** datos personales por canales inseguros.

Note: Cada empleado que accede a datos personales desde su puesto de trabajo está sujeto al GDPR y comparte responsabilidad en su cumplimiento, no solo la organización como entidad legal sino también potencialmente a nivel individual. El Artículo 5 del GDPR establece los principios fundamentales que deben aplicarse: los datos personales deben procesarse de manera lícita, leal y transparente; recopilarse para fines específicos y legítimos; ser adecuados, pertinentes y limitados a lo necesario; ser exactos y actualizados; conservarse solo el tiempo necesario; y tratarse de manera que garantice su seguridad mediante medidas técnicas u organizativas apropiadas contra el tratamiento no autorizado o ilícito. En la práctica del puesto de trabajo esto significa: solo acceder a datos personales cuando sea estrictamente necesario para realizar tu función laboral específica (principio de necesidad); usar siempre conexiones seguras y cifradas como VPN cuando accedas remotamente a datos personales desde ubicaciones no controladas; asegurar que todos los dispositivos que contengan datos personales estén cifrados con BitLocker, FileVault o equivalente para proteger contra robo o pérdida; nunca compartir datos personales por canales inseguros como email personal, WhatsApp personal, USBs sin cifrar, o servicios cloud no aprobados; reportar inmediatamente cualquier posible brecha de seguridad que involucre datos personales porque el GDPR exige notificación a la autoridad de protección de datos en 72 horas. La responsabilidad es verdaderamente compartida entre la organización y cada individuo que maneja datos personales.


### 3.5. LOPDGDD

**Ley Orgánica de Protección de Datos (España):**

* Complementa y adapta GDPR a España.
* Añade especificidades sobre videovigilancia.
* Regula uso de dispositivos digitales en el trabajo.
* Derechos digitales de los trabajadores.

Note: La LOPDGDD (Ley Orgánica 3/2018, de 5 de diciembre, de Protección de Datos Personales y garantía de los derechos digitales) es la implementación y adaptación española del GDPR. No reemplaza al GDPR sino que lo complementa, añadiendo especificidades del contexto español y desarrollando aspectos que el GDPR dejó a discreción de cada estado miembro. La LOPDGDD es fundamental conocerla si trabajáis en España porque añade requisitos adicionales y aclara aplicaciones específicas. Por ejemplo, incluye disposiciones detalladas sobre videovigilancia en el ámbito laboral (artículo 89)—regula cómo las empresas pueden instalar cámaras en instalaciones, qué señalización es obligatoria, qué derechos tienen los trabajadores; sobre el uso de dispositivos digitales en el ámbito laboral (artículo 87)—establece que los empleadores pueden acceder a contenidos derivados del uso de dispositivos digitales facilitados a los trabajadores exclusivamente para controlar cumplimiento de obligaciones laborales pero respetando privacidad y dignidad, lo cual tiene implicaciones directas para políticas de monitorización de puestos de trabajo; regula derechos digitales de los trabajadores como el derecho a la desconexión digital (artículo 88) que tiene implicaciones para políticas de trabajo remoto y disponibilidad fuera de horario laboral. Conocer tanto GDPR como LOPDGDD es absolutamente esencial para cualquier profesional que trabaje en protección de datos, cumplimiento normativo o seguridad de la información en España.


### 3.6. ENS (Esquema Nacional de Seguridad)

**Para administraciones públicas españolas:**

* Obligatorio para organismos públicos.
* Categorización de sistemas (BAJO, MEDIO, ALTO).
* Medidas de seguridad proporcionales a categoría.
* Auditorías periódicas obligatorias.

Note: El ENS (Esquema Nacional de Seguridad) aprobado mediante Real Decreto 3/2010 y actualizado por Real Decreto 951/2015 es de cumplimiento OBLIGATORIO para todas las administraciones públicas españolas (estatales, autonómicas, locales) y entidades del sector público. No es opcional ni voluntario—es ley. El ENS establece un marco de seguridad completo basado en la categorización de sistemas según el impacto potencial que una brecha de seguridad tendría sobre la información y servicios. Cada sistema debe categorizarse como BAJO, MEDIO o ALTO en tres dimensiones: confidencialidad, integridad y disponibilidad. Esta categorización determina qué medidas de seguridad son obligatorias—a mayor categoría, medidas más estrictas y rigurosas. Por ejemplo, un sistema categorizado como ALTO en las tres dimensiones requiere cifrado militar, autenticación multifactor robusta, auditorías exhaustivas continuas, planes de contingencia y continuidad de negocio muy detallados, controles de acceso físico extremadamente estrictos, monitorización 24/7, y personal con acreditaciones de seguridad. Las auditorías de cumplimiento del ENS son periódicas y obligatorias, realizadas por auditores externos independientes que verifican que los controles implementados corresponden a la categoría del sistema. Si trabajáis en administración pública española en cualquier capacidad relacionada con IT o seguridad, debéis conocer el ENS en profundidad—no es opcional, es requisito legal y su incumplimiento puede tener consecuencias graves incluyendo sanciones administrativas y responsabilidades legales.


### 3.7. CCN-STIC

**Guías del Centro Criptológico Nacional:**

* Documentos técnicos detallados.
* CCN-STIC 800 serie sobre ENS.
* Guías de configuración segura.
* Buenas prácticas de seguridad.

Note: Las guías CCN-STIC (Centro Criptológico Nacional - Seguridad de las Tecnologías de la Información y las Comunicaciones) son documentos técnicos de altísima calidad, extremadamente detallados y rigurosos, desarrollados por el Centro Criptológico Nacional que es el organismo español de referencia en ciberseguridad para las administraciones públicas y sectores estratégicos. Lo extraordinario es que están disponibles gratuitamente para descarga pública en la web del CCN-CERT (ccn-cert.cni.es). La serie CCN-STIC 800 desarrolla específicamente las medidas de seguridad del ENS con guías para cada control, incluyendo guías operativas, guías de configuración segura para tecnologías específicas, y guías de buenas prácticas. Por ejemplo, CCN-STIC 817 sobre gestión de ciberincidentes, CCN-STIC 825 sobre esquemas de firma electrónica, CCN-STIC 807 sobre criptología de empleo en el ENS. También hay guías CCN-STIC sobre configuración segura (hardening) de sistemas operativos específicos, bases de datos, aplicaciones web, etc. Estas guías son de nivel técnico avanzado, escritas por expertos nacionales en ciberseguridad, y representan el estado del arte en seguridad práctica aplicada. Deberían ser lectura obligatoria y de referencia continua para todo profesional de seguridad en España, especialmente quienes trabajen en sector público pero también en sector privado que busque implementar seguridad de nivel alto. Son recursos invaluables completamente gratuitos—aprovechadlos.

---

## 4. Políticas específicas del puesto


### 4.1. Política de contraseñas

**Requisitos típicos:**

* Longitud mínima: 12-16 caracteres.
* Complejidad: mayúsculas, minúsculas, números, símbolos.
* Cambio periódico: cada 90 días.
* No reutilizar últimas 5 contraseñas.
* Usar gestor de contraseñas corporativo.

Note: A pesar del avance tecnológico en métodos de autenticación como biométricos, tokens hardware, y certificados digitales, las contraseñas siguen siendo el método de autenticación más común y omnipresente en prácticamente todos los sistemas y servicios en 2024. Esto se debe a su facilidad de implementación, bajo coste, y familiaridad universal. Sin embargo, las contraseñas son también uno de los vectores de compromiso más frecuentes—el 81% de las brechas de seguridad involucran contraseñas débiles, robadas o reutilizadas según el Verizon Data Breach Investigations Report. Una política de contraseñas estricta pero sensata reduce drásticamente el riesgo. Los requisitos modernos recomendados por NIST (National Institute of Standards and Technology) han evolucionado: longitud es más importante que complejidad—una passphrase de 16 caracteres como "Café-Mañana-Sol-Playa" es más segura y memorable que "P@ssw0rd1"; el cambio periódico forzado cada 90 días se considera contraproducente porque induce a usuarios a hacer cambios mínimos predecibles ("Password1" → "Password2") o anotar contraseñas—solo cambiar cuando haya evidencia de compromiso; no reutilizar contraseñas entre sistemas es crítico—si una se compromete, todas lo están; usar gestor de contraseñas corporativo (Bitwarden, 1Password, LastPass Enterprise) es esencial para generar y almacenar contraseñas únicas ultra-seguras para cada sistema sin que el usuario tenga que recordarlas. Una política de contraseñas efectiva balancea seguridad con usabilidad para lograr cumplimiento real.


### 4.2. Autenticación multifactor (MFA)

**Segunda capa de seguridad:**

* Algo que **sabes** (contraseña).
* Algo que **tienes** (token, móvil).
* Algo que **eres** (huella, rostro).

**Obligatorio para:**
* Accesos administrativos.
* Acceso remoto (VPN).
* Sistemas críticos.

Note: La autenticación multifactor (MFA) o autenticación de dos factores (2FA) es probablemente la medida de seguridad individual más efectiva que existe actualmente, y las estadísticas lo demuestran rotundamente: según estudios de Microsoft y Google, MFA previene el 99.9% de los ataques de compromiso de cuenta automatizados. Funciona requiriendo múltiples factores de autenticación de categorías diferentes: algo que SABES (contraseña, PIN), algo que TIENES (smartphone con app autenticadora, token hardware FIDO2, tarjeta inteligente), y opcionalmente algo que ERES (huella dactilar, reconocimiento facial, iris). La clave es que un atacante que robe tu contraseña mediante phishing, keylogger, o brecha de base de datos, no puede acceder sin también tener físicamente tu segundo factor. MFA debe ser obligatoria sin excepciones para todos los accesos administrativos (cuentas con privilegios elevados), todo acceso remoto vía VPN especialmente desde redes no confiables, y todos los sistemas críticos que contengan información sensible o financiera. Las implementaciones modernas incluyen: push notifications a smartphone (Microsoft Authenticator, Duo), códigos TOTP de 6 dígitos (Google Authenticator, Authy), tokens hardware FIDO2/U2F (YubiKey, Titan Security Key) que son los más seguros contra phishing, o SMS (menos seguro por SIM swapping pero mejor que nada). No implementar MFA en 2024 es negligencia de seguridad inaceptable.


### 4.3. Política de pantalla bloqueada

**Protección ante ausencias:**

* Bloqueo **automático** tras 5-10 minutos de inactividad.
* Bloqueo **manual** obligatorio al ausentarse.
* Requiere contraseña para desbloquear.
* Protectores de pantalla no son suficientes.

Note: Un puesto de trabajo desbloqueado y desatendido es literalmente una invitación abierta a cualquier persona—compañero curioso, visitante malicioso, personal de limpieza, atacante oportunista—para acceder a todo lo que el usuario legítimo puede hacer: leer emails confidenciales, acceder a sistemas corporativos, copiar archivos sensibles, instalar malware o keyloggers, enviar emails suplantando identidad del usuario, modificar documentos, o simplemente curiosear información privada. Los ataques de tipo "evil maid" (atacante con acceso físico temporal) son reales y efectivos. La política de pantalla bloqueada es extraordinariamente simple de implementar pero increíblemente efectiva. Debe incluir dos componentes: bloqueo automático tras 5-10 minutos de inactividad como red de seguridad para cuando el usuario olvida—configurado centralmente via GPO en Windows o perfil de configuración en macOS; y bloqueo manual OBLIGATORIO cuando el usuario se ausenta aunque sea brevemente para ir al baño, café, reunión, o simplemente girar a hablar con compañero—debe convertirse en reflejo automático muscular presionar Win+L en Windows, Control+Command+Q en macOS, o Super+L en Linux. Los protectores de pantalla animados NO SON medidas de seguridad—solo ocultan visualmente pero no bloquean acceso. La política debe ser clara, comunicada repetidamente, reforzada con recordatorios visuales, y verificada mediante auditorías aleatorias walk-through.


### 4.4. Política de escritorio limpio

**Clean Desk Policy:**

* No dejar documentos sensibles en el escritorio.
* Guardar papeles en cajones con llave.
* No notas con contraseñas pegadas.
* Al finalizar jornada, escritorio despejado.

Note: La política de escritorio limpio o Clean Desk Policy parece trivial o de sentido común pero es sorprendentemente efectiva contra vectores de ataque de baja sofisticación técnica pero alta efectividad práctica. La ingeniería social y la recopilación de información (OSINT - Open Source Intelligence) frecuentemente comienzan con información visible físicamente: documentos impresos dejados en escritorios con datos confidenciales, diagramas de red pegados en cubículos, organigramas con nombres y roles, contraseñas anotadas en post-its pegados al monitor (increíblemente común), listados de servidores, credenciales de prueba, informes financieros, contratos con proveedores, información de clientes. Atacantes físicos (ya sean externos que logran acceso a instalaciones o insiders deshonestos) pueden simplemente fotografiar con smartphone toda esta información en segundos mientras pasan caminando. El "shoulder surfing" (mirar por encima del hombro) también aplica a información física. La política Clean Desk establece reglas simples pero estrictas: al finalizar la jornada laboral o al ausentarse por tiempo prolongado, TODOS los documentos deben guardarse en cajones o armarios con cerradura; no dejar nunca contraseñas, PINs o códigos de acceso anotados visibles (usar gestor de contraseñas en su lugar); triturar con cross-cut shredder documentos confidenciales antes de desechar; en espacios open office o salas compartidas, ser especialmente conscientes de qué es visible desde posiciones de paso. Compliance se verifica con walk-throughs aleatorios del equipo de seguridad.


### 4.5. Política de dispositivos USB

**Control de medios extraíbles:**

* **Prohibición** total (política más restrictiva).
* **Lista blanca** de dispositivos autorizados.
* **Escaneo** obligatorio de contenido antes de uso.
* **Cifrado** obligatorio en USBs corporativos.

Note: Los dispositivos USB y otros medios extraíbles (discos externos, tarjetas SD) son vectores clásicos, probados y extremadamente efectivos de propagación de malware y exfiltración de datos. El caso más famoso es Stuxnet, el sofisticado malware que saboteó el programa nuclear iraní en 2010, que se propagó inicialmente mediante USBs infectados introducidos físicamente en instalaciones air-gapped (sin conexión a internet). La técnica "USB drop attack" es simple pero efectiva: atacantes dejan USBs infectados en parkings, recepciones, o cafeterías de organizaciones objetivo con etiquetas curiosas como "Salarios 2024 Confidencial" o "Fotos Fiesta Empresa", contando con que alguien los conecte por curiosidad—y funciona con tasas de éxito del 45-60% según estudios. Los USBs también son vía trivial de exfiltración de datos—un empleado deshonesto o descuidado puede copiar gigas de información confidencial en segundos. La política debe ser clara y enforced técnicamente: OPCIÓN A (más restrictiva): prohibición total de USBs mediante deshabilitación de puertos USB vía GPO o herramientas endpoint; OPCIÓN B (balanceada): whitelist de dispositivos USB corporativos específicos autorizados identificados por hardware ID, el resto bloqueados; OPCIÓN C (permisiva pero controlada): permitir USBs pero obligar escaneo antivirus automático antes de acceder a contenido, más DLP (Data Loss Prevention) que alerte o bloquee copia de archivos clasificados como confidenciales. Todo USB corporativo debe estar cifrado con BitLocker To Go o equivalente. La política debe complementarse con awareness training sobre riesgos de conectar USBs desconocidos.


### 4.6. Política de instalación de software

**Control de aplicaciones:**

* Solo software **aprobado** por TI.
* **Prohibición** de software personal/gratuito.
* Actualizaciones solo desde **fuentes oficiales**.
* Usuarios sin **permisos de administrador**.

Note: Cada aplicación no autorizada instalada en dispositivos corporativos representa una potencial puerta trasera, vulnerabilidad sin parchar, vector de malware, fuga de datos, o violación de licencia con riesgo legal y financiero. El software "gratuito" descargado de internet frecuentemente viene con adware, spyware, o incluso malware oculto en instaladores aparentemente legítimos—sitios de descarga populares están plagados de versiones troyanizadas de software popular. Software desactualizado o pirata tiene vulnerabilidades conocidas sin parches. Software no autorizado no tiene soporte de IT cuando causa problemas. La política debe establecer claramente: solo software pre-aprobado por IT disponible en catálogo corporativo puede instalarse; usuarios NO deben tener permisos de administrador local en sus dispositivos para prevenir instalaciones no autorizadas técnicamente; todas las actualizaciones deben venir desde fuentes oficiales verificadas (Microsoft Update, Apple Software Update, repositorios oficiales del vendor) nunca desde sitios de terceros; proceso formal para solicitar software nuevo—usuario justifica necesidad de negocio, IT evalúa seguridad/compatibilidad/coste/licencias, aprueba o proporciona alternativa autorizada, instala centralmente o proporciona installer verificado. Esta política DEBE complementarse con controles técnicos efectivos: AppLocker en Windows o Gatekeeper en macOS configurados en modo whitelist (solo ejecutables firmados y aprobados pueden correr); herramientas de inventario de software que detecten aplicaciones no autorizadas; sin permisos admin local salvo excepciones justificadas y controladas. Es balance entre seguridad y productividad pero la seguridad debe prevalecer.


### 4.7. Política de uso aceptable (AUP)

**Usos permitidos y prohibidos:**

* **Permitido**: Uso profesional, formación relacionada.
* **Prohibido**: Descarga de contenido ilegal, gaming, torrents.
* **Monitorización**: La organización puede monitorizar actividad.
* **Consecuencias**: Sanciones por incumplimiento.

Note: La Política de Uso Aceptable (AUP - Acceptable Use Policy) es un documento contractual fundamental que establece explícitamente qué usos de recursos tecnológicos corporativos (dispositivos, red, software, datos) están permitidos y cuáles están prohibidos, los derechos de monitorización que la organización se reserva, y las consecuencias del incumplimiento. El AUP debe firmarse por TODOS los empleados durante onboarding y tras actualizaciones significativas—esta firma tiene valor legal y protege a la organización estableciendo que el empleado fue informado claramente de las reglas y las aceptó. Usos típicamente PERMITIDOS: actividades profesionales directamente relacionadas con función laboral, formación y desarrollo profesional relacionado con el trabajo, uso personal mínimo razonable (email personal ocasional, llamada breve) siempre que no interfiera con productividad ni viole otras políticas. Usos típicamente PROHIBIDOS: descarga de contenido ilegal (piratería, material protegido por derechos de autor), acceso a contenido inapropiado (pornografía, apuestas, contenido odioso), instalación de software no autorizado, gaming durante horario laboral, uso de torrents o P2P, intentos de bypass de controles de seguridad, acceso no autorizado a sistemas o datos de otros usuarios. Monitorización: el AUP debe establecer claramente que la organización SE RESERVA EL DERECHO de monitorizar actividad en dispositivos corporativos, tráfico de red, emails corporativos, accesos a sistemas—esto es legal si está informado previamente (según LOPDGDD artículo 87). Consecuencias: deben ser proporcionadas y escaladas—primer incumplimiento menor warning verbal, reincidencia medidas disciplinarias formales, incumplimientos graves despido procedente. El AUP equilibra productividad, privacidad razonable del empleado, y protección legal de la organización.

---

## 5. Trabajo remoto y BYOD


### 5.1. Desafíos del trabajo remoto

**Nuevos riesgos:**

* Redes WiFi domésticas **inseguras**.
* **Falta de control físico** del entorno.
* **Dificultad** en aplicar políticas de seguridad.
* Mezcla de **uso personal y profesional**.
* Mayor superficie de ataque.

Note: La pandemia COVID-19 en 2020 forzó una transformación masiva y súbita al trabajo remoto sin tiempo para preparación, planificación o implementación adecuada de controles de seguridad—organizaciones que nunca habían contemplado trabajo remoto tuvieron que implementarlo en días. Esta transición precipitada expuso y amplificó riesgos de seguridad significativos que muchas organizaciones siguen enfrentando. Las redes WiFi domésticas típicamente usan WPA2-PSK con contraseñas débiles compartidas con familiares y vecinos, son vulnerables a ataques de descifrado, y frecuentemente tienen routers sin actualizar con vulnerabilidades conocidas. La falta de control físico del entorno significa que la organización no puede garantizar quién tiene acceso visual o físico a dispositivos y documentos—familiares, niños, visitas pueden ver pantallas o acceder a equipos. Aplicar políticas de seguridad es técnicamente más difícil cuando dispositivos están distribuidos geográficamente fuera del perímetro corporativo. La mezcla inevitable de uso personal y profesional en el mismo entorno físico y misma red aumenta riesgos de exposición. La superficie de ataque se multiplica—en vez de un perímetro corporativo único defendible, ahora hay cientos o miles de ubicaciones remotas cada una con sus propias vulnerabilidades. Estas son realidades que las organizaciones deben gestionar activamente, no ignorar.


### 5.2. Política de trabajo remoto

**Medidas específicas:**

* **VPN obligatoria** para acceso a recursos corporativos.
* **Verificación de seguridad** WiFi doméstica.
* **Separación** de red doméstica (red invitados para trabajo).
* **Cifrado de disco** completo obligatorio.
* **Soporte remoto** IT disponible.

Note: El trabajo remoto requiere crear un "perímetro virtual" con VPN obligatoria (cifra todo el tráfico end-to-end), verificación de seguridad WiFi doméstica (cambiar contraseña default del router, activar WPA2/WPA3, deshabilitar WPS), y separación de red doméstica creando VLAN o red de invitados solo para trabajo. Cifrado de disco es aún MÁS crítico en remoto donde el riesgo de robo físico es mayor. IT debe proporcionar soporte remoto multicanal.


### 5.3. BYOD (Bring Your Own Device)

**Uso de dispositivos personales:**

**Ventajas:**
* Ahorro de costes para empresa.
* Comodidad para empleado.

**Desventajas:**
* Control limitado de seguridad.
* Mezcla uso personal/profesional.
* Dificultad en borrado remoto.

Note: BYOD ahorra 500-1500€ por empleado en hardware pero introduce complejidades masivas: control limitado (no puedes forzar políticas sin consentimiento del propietario), mezcla datos personales/corporativos (problemas legales de privacidad GDPR), dificultad de borrado remoto selectivo sin afectar datos personales. Muchas organizaciones maduras en seguridad simplemente lo prohíben y proporcionan dispositivos corporativos dedicados—más caro upfront pero más simple y seguro long-term.


### 5.4. Política BYOD

**Si se permite, requisitos mínimos:**

* **MDM** (Mobile Device Management) obligatorio.
* **Containerización** de datos corporativos.
* **Antivirus** actualizado.
* Sistema operativo **actualizado**.
* **Aceptación** de borrado remoto en caso de pérdida.

Note: Si se permite BYOD, MDM es obligatorio no opcional. La containerización es clave: crea un "contenedor" cifrado separado donde viven apps y datos corporativos completamente aislados de lo personal mediante separación a nivel de kernel. El usuario ve iconos con badge corporativo que al abrirse entran al contenedor con sus propias políticas (contraseña más fuerte, MFA). Crítico: el empleado debe aceptar por escrito el borrado remoto selectivo del contenedor si pierde el dispositivo o deja la empresa.


### 5.5. Gestión de dispositivos móviles (MDM)

**Capacidades del MDM:**

* **Inventario** de dispositivos conectados.
* **Aplicación** de políticas de seguridad.
* **Actualización** remota de configuraciones.
* **Borrado remoto** (wipe) si se pierde dispositivo.
* **Geolocalización** de dispositivos corporativos.

Note: MDM es fundamental para gestionar flotas de dispositivos centralizada y remotamente—sin él, gestionar más de 10-20 dispositivos es imposible. Capacidades clave: inventario automático (todos los dispositivos con detalles completos), aplicación remota de políticas (desplegar configuraciones a cientos simultáneamente), actualización remota de configuraciones (cambiar políticas on-the-fly), borrado remoto si se pierde/roba (protege datos aunque dispositivo esté en manos equivocadas), y geolocalización GPS (recuperar robados, debe estar en política por privacidad). Herramientas: Microsoft Intune, VMware Workspace ONE, MobileIron/Ivanti.

---

## 6. Protección técnica del puesto


### 6.1. Antivirus y antimalware

**Defensa básica obligatoria:**

* Instalación y **actualización automática**.
* Escaneo en **tiempo real**.
* Escaneo **programado** semanal completo.
* **Cuarentena** de archivos sospechosos.
* Reportar detecciones a consola central.

Note: El antivirus es necesario pero no suficiente. Combina detección por firmas (malware conocido) con análisis heurístico (comportamientos sospechosos). Las soluciones modernas EDR (Endpoint Detection & Response) añaden capacidades de investigación y respuesta automatizada, pero no protegen contra phishing o ingeniería social—por eso necesitamos defensa en profundidad con múltiples capas.


### 6.2. Firewall personal

**Protección de red local:**

* **Activado** siempre, especialmente en público.
* Bloquear **conexiones entrantes** no solicitadas.
* Permitir solo **aplicaciones autorizadas**.
* Perfil **público** activado en redes no confiables.

Note: El firewall nativo de Windows/macOS es suficiente para la mayoría—la clave es configurarlo bien y NUNCA deshabilitarlo "temporalmente". Debe bloquear conexiones entrantes no solicitadas por defecto. El perfil público en redes WiFi no confiables aplica reglas más restrictivas bloqueando servicios como compartición de archivos que son seguros en red corporativa pero peligrosos en cafeterías o aeropuertos.


### 6.3. Cifrado de disco completo

**BitLocker (Windows) o FileVault (macOS):**

* Cifrado de **disco completo** (FDE - Full Disk Encryption).
* Protege datos si **roban** el dispositivo físico.
* Transparente para el usuario.
* Clave de recuperación en custodia de IT.

Note: Sin cifrado, cualquiera puede extraer el disco y leer TODOS los datos en minutos sin necesitar contraseña—solo arrancar desde USB o conectar disco a otro PC. Con cifrado completo (BitLocker/FileVault), el disco robado es basura matemáticamente indescifrable. Es transparente al usuario después del arranque y crítico: la clave de recuperación debe custodiarse por IT porque si se pierde y olvidas la contraseña, los datos son irrecuperables incluso para ti.


### 6.4. Actualizaciones de seguridad

**Patch management crítico:**

* Actualizaciones de **sistema operativo** automáticas.
* Actualizaciones de **aplicaciones** críticas.
* Parches de **seguridad** prioritarios (deploy en 48h).
* **Testing** previo en entorno controlado.

Note: Los exploits aparecen días u horas después de publicarse un parche—los atacantes hacen ingeniería inversa para descubrir la vulnerabilidad. WannaCry en 2017 explotó una vulnerabilidad parcheada dos meses antes—quien no actualizó sufrió ransomware devastador. Los parches críticos deben desplegarse en 48-72h máximo. El testing previo es necesario en grandes organizaciones pero no puede retrasar tanto que amplifique la ventana de vulnerabilidad.


### 6.5. Control de puertos USB

**Restricción técnica:**

* **Deshabilitar** puertos USB via GPO o software.
* **Whitelist** de dispositivos autorizados por hardware ID.
* **Alertas** ante conexión de dispositivos no autorizados.
* **Cifrado** obligatorio en USBs corporativos.

Note: El control técnico via GPO o software es más efectivo que confiar en que usuarios cumplan la política—los humanos olvidan o ignoran, los sistemas nunca. Deshabilitar puertos USB completamente o usar whitelist por hardware ID previene ataques USB drop (dejar USBs infectados con etiquetas curiosas en parkings, 45-60% los conectan) y exfiltración trivial de datos. Stuxnet se propagó así en instalaciones air-gapped.


### 6.6. Application whitelisting

**Solo software autorizado:**

* **Lista blanca** de aplicaciones permitidas.
* Bloqueo de **todo lo demás**.
* Herramientas: AppLocker (Windows), Gatekeeper (macOS).
* Actualización dinámica de whitelist.

Note: Application whitelisting (lista blanca) es más seguro que lista negra—en vez de bloquear malware conocido (infinito), solo permites software conocido y confiable (finito y controlable). AppLocker en Windows Enterprise o Gatekeeper en macOS permiten ejecutar solo aplicaciones firmadas digitalmente y aprobadas. Reduce drásticamente superficie de ataque bloqueando malware, herramientas de hacking, y software no autorizado aunque sea legítimo.


### 6.7. Backup del puesto de trabajo

**Respaldo de datos críticos:**

* Backup **automático** nocturno.
* Almacenamiento en **servidor central** o nube.
* Incluir carpetas de **usuario** (Documentos, Escritorio).
* **Exclusión** de software (reinstalable).
* Test de **restauración** trimestral.

Note: Los usuarios pierden datos por mil razones: fallos de hardware (discos fallan sin aviso), borrados accidentales, ransomware que cifra todo. El backup automático nocturno a servidor central o nube es el único salvavidas real. Debe incluir carpetas de usuario (Documentos, Escritorio, Descargas) pero no software reinstalable. Crítico: test de restauración trimestral—un backup no verificado es un backup que podría no funcionar cuando lo necesites desesperadamente.

---

## 7. Formación y concienciación


### 7.1. Importancia de la formación

**El usuario como primera línea:**

* Tecnología sola **no es suficiente**.
* Usuario formado detecta **phishing**.
* Usuario concienciado sigue **políticas**.
* Usuario comprometido = organización comprometida.

Note: La tecnología más avanzada (firewalls, EDR, DLP) es inútil si un usuario cae en phishing y entrega sus credenciales. El 90% de brechas exitosas empiezan con ingeniería social. Un usuario formado detecta emails sospechosos, verifica remitentes extraños, no hace clic en enlaces dudosos, usa contraseñas seguras únicas, activa MFA voluntariamente, y reporta incidentes inmediatamente. La formación convierte usuarios de eslabón más débil a primera línea de defensa activa.


### 7.2. Programa de concienciación

**Elementos del programa:**

* Formación **inicial** para nuevos empleados.
* Formación **anual** de refuerzo para todos.
* **Simulacros** de phishing periódicos.
* **Newsletters** de seguridad mensuales.
* **Carteles** recordatorios en oficinas.

Note: La concienciación debe ser continua y repetitiva porque la memoria humana se desvanece y las amenazas evolucionan constantemente—el phishing de 2020 es muy diferente al de 2024 (ahora usan IA generativa para crear emails perfectos). La formación inicial en onboarding crea base, anual refuerza conocimientos con amenazas actualizadas, simulacros proporcionan práctica real, newsletters mensuales mantienen seguridad top-of-mind, y carteles físicos recordatorios refuerzan buenas prácticas diarias. Múltiples touchpoints repetidos crean hábitos de seguridad sostenidos.


### 7.3. Temas de formación

**Contenidos esenciales:**

* Identificación de **phishing** y spear-phishing.
* Creación de **contraseñas seguras**.
* Uso de **MFA**.
* **Ingeniería social** y cómo defenderse.
* Qué hacer ante un **incidente** sospechoso.

Note: Estos cinco temas cubren los vectores de ataque más comunes que explotan el factor humano. Phishing/spear-phishing son vector #1 (emails engañosos, verificar remitente/enlaces/urgencia artificial). Contraseñas seguras únicas con gestor previenen reutilización. MFA bloquea 99.9% ataques automatizados. Ingeniería social va más allá de phishing: vishing (llamadas telefónicas), pretexting (inventar escenarios), tailgating físico. Qué hacer ante incidente: no apagar equipo, desconectar red si seguro, reportar inmediatamente IT/Seguridad con detalles. Personalizar contenido a amenazas específicas del sector (healthcare sufre mucho ransomware, finanzas sufre BEC Business Email Compromise).


### 7.4. Simulacros de phishing

**Entrenamiento práctico:**

* Envío de **emails falsos** de phishing a empleados.
* Monitorizar quién **hace clic**.
* Formación **inmediata** para quien cae.
* Sin **penalizaciones**, enfoque educativo.
* **Métricas** de mejora trimestral.

Note: Los simulacros de phishing son la mejor forma de medir efectividad real de formación—proveen práctica realista en entorno seguro controlado. Herramientas como KnowBe4, Cofense, o Proofpoint simulan emails maliciosos personalizados. Los usuarios que hacen clic van a página explicativa de por qué era phishing (señales que debieron detectar) y reciben formación focalizada inmediata—aprender del error propio es más efectivo que teoría abstracta. Crítico: enfoque 100% educativo sin penalizaciones, el objetivo es mejorar no castigar. Métricas trimestrales (% clic) muestran mejora—organizaciones maduras logran <5% tasa de clic vs 30-40% iniciales.

---

## 8. Monitorización y cumplimiento


### 8.1. Necesidad de monitorización

**¿Por qué monitorizar?**

* Verificar **cumplimiento** de políticas.
* Detectar **anomalías** de comportamiento.
* Responder **rápidamente** a incidentes.
* **Evidencia** para investigaciones.

Note: La monitorización verifica que políticas definidas se cumplen realmente, detecta comportamientos anómalos que indican compromiso (usuario accediendo datos inusuales, login desde geolocalización imposible, descarga masiva de archivos), permite respuesta rápida a incidentes (alertas en tiempo real), y proporciona evidencia forense para investigaciones posteriores. NO es espionaje ni vigilancia abusiva si se hace transparentemente informando a empleados, proporcionalmente monitorizando solo lo necesario para seguridad, y dentro del marco legal LOPDGDD artículo 87. Debe documentarse en AUP firmado por empleados.


### 8.2. Qué monitorizar

**Aspectos a supervisar:**

* **Logs** de autenticación (exitosos y fallidos).
* **Instalación** de software.
* **Conexión** de dispositivos USB.
* **Tráfico** de red anómalo.
* Acceso a **recursos** sensibles.

Note: No intentéis monitorizar TODO o generaréis ruido abrumador que ahoga señales importantes (alert fatigue—analistas ignoran alertas por volumen excesivo). Centraos en eventos de seguridad relevantes: logs de autenticación para detectar brute-force o credential stuffing (múltiples fallos seguidos) o accesos desde ubicaciones sospechosas, instalación de software para detectar malware o herramientas hacking no autorizadas, conexión USB para detectar exfiltración de datos, tráfico de red anómalo hacia dominios maliciosos conocidos o volumen inusual, y accesos a recursos sensibles (carpetas confidenciales, bases de datos críticas) para detectar escalada de privilegios o curiosidad no legítima.


### 8.3. Herramientas de monitorización

**Soluciones técnicas:**

* **SIEM**: Correlación de logs centralizados.
* **EDR**: Endpoint Detection and Response.
* **DLP**: Data Loss Prevention.
* **NAC**: Network Access Control.

Note: SIEM (Security Information and Event Management como Splunk, QRadar, Azure Sentinel) agrega logs de múltiples fuentes y correlaciona eventos para detectar patrones de ataque complejos. EDR (Endpoint Detection & Response como CrowdStrike, SentinelOne) monitoriza comportamiento de endpoints detectando malware avanzado y permitiendo respuesta remota. DLP (Data Loss Prevention como Symantec, McAfee) previene que datos sensibles salgan de organización por email USB o cloud. NAC (Network Access Control como Cisco ISE) verifica que dispositivos cumplan políticas antes de permitir acceso a red. Ninguna es "instalar y olvidar"—requieren tuning continuo y analistas que investiguen alertas activamente, por eso el coste real incluye personal especializado no solo licencias software.


### 8.4. Aspectos legales de la monitorización

**Marco legal en España:**

* **Informar** a empleados de la monitorización.
* **Proporcionalidad**: Solo monitorizar lo necesario.
* **LOPDGDD** Artículo 87: Uso de dispositivos digitales.
* **Estatuto de Trabajadores**: Límites a vigilancia.

Note: La monitorización sin informar previamente a empleados puede ser ilegal en España. LOPDGDD artículo 87 regula uso de dispositivos digitales en trabajo: empleadores pueden acceder a contenidos derivados del uso para controlar cumplimiento de obligaciones laborales pero respetando dignidad y privacidad, deben informar previamente a trabajadores, y monitorizar solo lo proporcional y necesario para el fin legítimo. El Estatuto de Trabajadores limita vigilancia (art. 20.3): debe respetar dignidad del trabajador y ser proporcional. Recomendación: documentar la monitorización en AUP firmado por empleados, limitar a datos técnicos de seguridad no contenido de comunicaciones privadas, y consultar con legal antes de implementar cualquier sistema de monitorización para asegurar conformidad.


### 8.5. Auditorías de cumplimiento

**Verificación periódica:**

* Auditoría **trimestral** de configuraciones.
* Verificación **semestral** de controles técnicos.
* Revisión **anual** completa de políticas.
* Pentesting **anual** de puestos de trabajo.

Note: Las auditorías periódicas descubren el inevitable gap entre políticas definidas en papel y realidad implementada en campo—lo que está documentado vs lo que realmente ocurre. Auditoría trimestral de configuraciones verifica que sistemas mantienen configuraciones de seguridad (cifrado activo, firewall encendido, parches aplicados). Verificación semestral de controles técnicos testea efectividad de controles (¿el DLP realmente bloquea exfiltración? ¿NAC realmente previene dispositivos no conformes?). Revisión anual completa de políticas actualiza documentación reflejando cambios tecnológicos organizativos y amenazas emergentes. Pentesting anual de puestos simula atacante real intentando comprometer endpoints identificando vulnerabilidades antes que atacantes reales. Auditorías son esenciales para mejora continua ciclo PDCA Plan-Do-Check-Act.

---

## 9. Gestión de incidentes en el puesto


### 9.1. Tipos de incidentes comunes

**Incidentes típicos:**

* **Malware** detectado.
* **Phishing** exitoso.
* **Pérdida** o robo de dispositivo.
* **Acceso no autorizado** a cuenta.
* **Fuga** de información.

Note: Estos cinco incidentes representan >80% de casos en puestos de trabajo. Malware detectado (antivirus alerta, comportamiento extraño del sistema). Phishing exitoso (usuario hizo clic en enlace, descargó adjunto, proporcionó credenciales). Pérdida/robo de dispositivo (laptop robada en coche, móvil olvidado en taxi). Acceso no autorizado a cuenta (alguien conoce tu contraseña, sesión secuestrada). Fuga de información (datos sensibles compartidos inadvertidamente, email al destinatario equivocado). Cada organización debe tener procedimientos documentados formales por escrito accesibles para empleados especificando exactamente qué hacer en cada escenario—no improvisar durante crisis.


### 9.2. Procedimiento de reporte

**¿Qué debe hacer el usuario?**

1. **No apagar** el equipo (preservar evidencias).
2. **Desconectar** de red si es seguro.
3. **Notificar** a IT/Seguridad inmediatamente.
4. **Documentar** qué observó y cuándo.
5. **No investigar** por cuenta propia.

Note: La velocidad de reporte es crítica—cada minuto cuenta en contención porque malware se propaga, atacantes exfiltran más datos, o daño se amplifica. Los usuarios deben saber exactamente a quién llamar (número directo IT/Seguridad, email abuse@empresa, portal interno) y qué información proporcionar (qué observaron, cuándo exactamente, qué hicieron antes del incidente). Regla de oro: NO apagar equipo (borra evidencias en RAM), desconectar ethernet/WiFi si seguro para prevenir propagación lateral, NO investigar por cuenta propia ni "probar cosas" que pueden empeorar situación, documentar todo inmediatamente mientras memoria es fresca.


### 9.3. Respuesta a malware

**Pasos del equipo IT:**

1. **Aislar** el equipo afectado.
2. **Identificar** el tipo de malware.
3. **Eliminar** la amenaza.
4. **Verificar** que no haya lateral movement.
5. **Restaurar** desde backup si necesario.
6. **Analizar** causa raíz.

Note: La respuesta debe ser rápida pero metodológica siguiendo procedimiento formal no pánico improvisado. Aislar el equipo afectado física (desconectar cables) y lógicamente (bloquear en red por MAC/IP) previene propagación lateral. Identificar tipo de malware (ransomware, trojan, rootkit) mediante análisis con herramientas forenses permite respuesta específica. Eliminar amenaza con antivirus especializado o herramientas de remediación. Verificar que no hubo movimiento lateral inspeccionando logs de red y otros endpoints. Restaurar desde backup verificado limpio si sistema muy comprometido. Analizar causa raíz (¿email phishing? ¿USB infectado? ¿vulnerabilidad sin parchar?) para prevenir recurrencia. Crítico: no borrar evidencias prematuramente—preservar para análisis forense e identificar cómo ocurrió compromiso.


### 9.4. Respuesta a pérdida de dispositivo

**Protocolo de dispositivo perdido/robado:**

1. Reporte **inmediato** por el usuario.
2. IT ejecuta **borrado remoto** (MDM).
3. **Cambio** de contraseñas de cuentas accedidas.
4. **Revisión** de actividad reciente de la cuenta.
5. **Denuncia** policial si es robo.
6. **Lecciones aprendidas** del incidente.

Note: El borrado remoto solo funciona si dispositivo se conecta a internet después de robo—por eso el cifrado de disco es la primera y más importante línea de defensa (protege incluso si borrado remoto falla). El usuario debe reportar pérdida/robo inmediatamente (minutos no horas) para minimizar ventana de exposición. IT ejecuta wipe remoto vía MDM que borra datos corporativos próxima vez que dispositivo se encienda y conecte. Cambiar INMEDIATAMENTE todas las contraseñas a las que dispositivo tenía acceso (email, VPN, sistemas corporativos) porque podrían estar guardadas o en sesión activa. Revisar logs de actividad de cuenta buscando accesos sospechosos antes/después de pérdida. Denunciar a policía si es robo con número de serie del dispositivo para registro oficial. Hacer post-mortem identificando cómo mejorar prevención (¿cable Kensington? ¿más concienciación sobre no dejar laptops en coches visibles?).

---

## 10. Conclusión


### 10.1. Resumen de conceptos clave

* **Puesto de trabajo**: Punto crítico de acceso a información.
* **Políticas**: Definen qué debe hacerse.
* **Estándares**: ISO 27001, GDPR, ENS proporcionan marco.
* **Protección técnica**: Múltiples capas de defensa.
* **Formación**: Usuario concienciado es mejor defensa.

Note: La protección del puesto de trabajo NO es una medida única silver bullet sino un sistema integrado de controles técnicos (antivirus, firewall, cifrado, MDM), organizativos (políticas, procedimientos, auditorías), y humanos (formación, concienciación, cultura de seguridad) trabajando sinérgicamente. Cada control complementa y refuerza los demás. Las políticas definen el qué, los controles técnicos lo hacen ejecutable y auditable, y la formación asegura que las personas entiendan el por qué y el cómo. Es arquitectura de seguridad holística no checklist de tecnologías a comprar.


### 10.2. Defensa en profundidad

**Capas de protección:**

1. Política y concienciación.
2. Autenticación fuerte (MFA).
3. Antivirus y firewall.
4. Cifrado.
5. Monitorización.
6. Respuesta a incidentes.

Note: Si una capa falla, las demás siguen protegiendo—esta es la esencia de defensa en profundidad o defense in depth, concepto militar aplicado a ciberseguridad. Ejemplo: usuario cae en phishing proporcionando contraseña (falla capa 1 concienciación) → MFA bloquea acceso sin segundo factor (capa 2) → si MFA también comprometida, monitorización detecta login desde geolocalización anómala (capa 5) → respuesta a incidentes contiene daño (capa 6). Ninguna capa es perfecta 100% pero combinadas crean seguridad robusta resiliente. No confiar en una sola tecnología o control—redundancia es fortaleza no desperdicio.


### 10.3. Responsabilidad compartida

**Seguridad es tarea de todos:**

* **Dirección**: Aprobar políticas y presupuesto.
* **IT/Seguridad**: Implementar controles técnicos.
* **Usuarios**: Seguir políticas y reportar incidentes.
* **RRHH**: Formar y gestionar incumplimientos.

Note: La seguridad NO es responsabilidad exclusiva del departamento IT o de Seguridad—requiere compromiso y colaboración activa de toda la organización a todos los niveles. Un solo eslabón débil (usuario que cae en phishing, director que exige excepción a políticas, IT que posterga parches) puede comprometer toda la cadena. Dirección debe aprobar políticas formalmente, asignar presupuesto adecuado, y dar ejemplo cumpliendo ellos primero. IT/Seguridad implementan y mantienen controles técnicos pero no pueden estar en cada escritorio. Usuarios son primera línea: siguen políticas, reportan incidentes, mantienen vigilancia. RRHH gestiona ciclo de vida del empleado (formación onboarding, refuerzo anual, medidas disciplinarias ante incumplimientos graves). La seguridad es cultura organizativa no proyecto de IT.

---

## 11. Políticas de seguridad INCIBE


### 11.1. Políticas INCIBE para PYMEs

**Documentos de referencia para protección:**

* Políticas sector ializadas para pequeñas y medianas empresas
* Formato PDF y Word editable
* Incluyen checklists de verificación
* Adaptables a contexto específico
* Disponibles gratuitamente en INCIBE

Note: El Instituto Nacional de Ciberseguridad (INCIBE) ha desarrollado un conjunto de políticas de seguridad específicamente diseñadas para que las PYMEs españolas puedan mejorar su ciberseguridad de forma práctica y asequible. Estas políticas son documentos profesionales que guían a la empresa en los procesos internos necesarios para proteger la información y la infraestructura digital de forma organizada y medible. Lo más valioso es que están disponibles gratuitamente en la web de INCIBE, en formatos editables (PDF y Word) para que cada empresa pueda personalizarlas según su contexto particular. No son documentos meramente teóricos sino herramientas prácticas que incluyen checklists ejecutables y roles claramente definidos.


### 11.2. ¿Qué contienen estas políticas?

**Elementos principales:**

* **Aspectos de seguridad esenciales**: Áreas críticas a proteger
* **Roles y responsabilidades**: Empresario, técnico, empleados
* **Checklists**: Acciones concretas por grupo
* **Formatos editables**: Personalizables según empresa
* **Guías de seguimiento**: Cómo medir cumplimiento

Note: Cada política de INCIBE cubre aspectos fundamentales de la seguridad que deben ser supervisados y gestionados activamente, desde la protección de los equipos y el control de accesos hasta la gestión de aplicaciones y el almacenamiento de datos. La idea es que toda PYME, sin importar su tamaño, identifique áreas clave donde aplicar controles y pueda adaptarlos según sus necesidades y recursos. Las políticas están diseñadas para que el empresario (que toma decisiones estratégicas), el equipo técnico (que implementa técnicamente) y todos los empleados (que aplican buenas prácticas diarias) conozcan claramente sus funciones y responsabilidades específicas en seguridad. Incluyen checklists o listas de verificación con acciones específicas y medibles para cada grupo, facilitando enormemente la implementación práctica.


### 11.3. Estructura de los documentos INCIBE

**Secciones estándar de cada política:**

1. **Antecedentes**: Justificación y contexto de la política
2. **Objetivos**: Qué busca lograr la política
3. **Checklist**: Lista de controles (medidas) por nivel y alcance
4. **Puntos Clave**: Prácticas o reglas esenciales a cumplir
5. **Referencias**: Enlaces a normativas y guías relacionadas

Note: Los documentos de políticas de INCIBE siguen una estructura común que facilita su lectura, comprensión e implementación. Primero, Antecedentes: justifican por qué es necesaria la política basándose en riesgos identificados—por ejemplo, en "Aplicaciones permitidas" se justifica por la obligación de usar software legal para evitar sanciones y reducir riesgos de malware; en "Protección del puesto de trabajo" se destacan riesgos tanto tecnológicos como humanos. Segundo, Objetivos: establecen qué busca lograr la política en términos de seguridad, control y prevención. Tercero, Checklist: la parte más práctica—lista de controles (medidas) clasificados por nivel de complejidad (Básico o Avanzado) y alcance (Procesos para gestores, Tecnología para técnicos, Personas para todos). Esto permite priorizar implementación. Cuarto, Puntos Clave: resumen de las prácticas o reglas esenciales que todos deben cumplir para efectividad de la política. Quinto, Referencias: enlaces a normativas externas o guías complementarias.


### 11.3. Estructura de los documentos INCIBE II

**Relación con conceptos vistos:**

* **Antecedentes** → Elementos del puesto + Escenarios de riesgo
* **Objetivos** → Política (declaración de intenciones)
* **Checklist** → Medidas Básicas/Avanzadas + PRO/TEC/PER
* **Puntos Clave** → Normativas específicas
* **Referencias** → ISO 27001, GDPR, LOPDGDD

Note: Observad cómo la estructura de INCIBE se corresponde perfectamente con los conceptos que hemos estudiado. Los Antecedentes conectan con la identificación de elementos vulnerables del puesto de trabajo y sus escenarios de riesgo—establecen el "por qué" necesitamos esta política. Los Objetivos son la Política en sí—la declaración general de intenciones y compromiso. El Checklist aplica directamente nuestra clasificación de medidas por complejidad (Básico/Avanzado) y alcance (PRO/TEC/PER)—es la herramienta clave para evaluar y medir el cumplimiento y nivel de madurez de seguridad de la empresa. Los Puntos Clave son las Normativas—las reglas y requisitos específicos que deben cumplirse. Las Referencias fortalecen la política alineándola con regulaciones y estándares externos como ISO 27001, GDPR y LOPDGDD.


### 11.4. Ejemplo: Protección del Puesto de Trabajo

**Controles incluidos (ejemplos del checklist):**

* **[B-PER]** Política de bloqueo de sesión configurada
* **[B-PER]** Política de escritorio limpio implementada
* **[A-TEC]** Desactivación de puertos USB por defecto
* **[A-TEC]** Cifrado de disco completo activado
* **[B-PRO]** Procedimiento de reporte de dispositivos perdidos

Note: Veamos ejemplos concretos del checklist de "Protección del puesto de trabajo" de INCIBE. Observad la notación: [Nivel-Alcance]. Controles Básicos para Personas (B-PER) como "Política de bloqueo de sesión" son asequibles y aplicables a todos sin conocimientos técnicos avanzados—simplemente configurar bloqueo automático y educar a todos a usar Win+L. "Política de escritorio limpio" tampoco requiere tecnología compleja, solo disciplina organizativa. Los controles Avanzados para Tecnología (A-TEC) requieren inversión y conocimiento especializado: "Desactivación de puertos USB por defecto" implica configurar GPOs o herramientas de gestión endpoint para deshabilitar selectivamente puertos; "Cifrado de disco completo" requiere hardware compatible (TPM), configuración técnica (BitLocker, FileVault) y gestión de claves de recuperación. Los controles de Procesos (B-PRO) establecen procedimientos organizativos como "tener definido y comunicado cómo reportar dispositivos perdidos"—es básico porque no requiere tecnología sofisticada, solo documentar el proceso y comunicarlo.


### 11.5. Cómo utilizar las políticas INCIBE

**Pasos prácticos para implementación:**

1. **Descargar** políticas relevantes desde web INCIBE
2. **Identificar** elementos de seguridad esenciales de tu organización
3. **Asignar** roles y responsabilidades claras (dirección, IT, empleados)
4. **Adaptar** políticas editables a tu contexto específico
5. **Usar checklist** para registrar qué se implementó y qué falta
6. **Medir progreso** y priorizar acciones pendientes

Note: Para un supuesto práctico o implementación real, seguid estos pasos. Primero, descargar del sitio web de INCIBE (incibe.es/empresas/herramientas/politicas) el paquete completo de políticas o las específicas que necesitéis—están en ZIP con PDFs y Words. Segundo, revisad los puntos clave de cada política identificando cuáles son los aspectos de seguridad que debéis controlar en vuestra organización—esto ayuda a priorizar (quizás "Protección del puesto" y "Almacenamiento" son más urgentes que "Política de teletrabajo" si no tenéis remote workers). Tercero, asignad responsabilidades dividiendo entre dirección (aprueba políticas, asigna presupuesto), equipo técnico de IT (implementa controles técnicos) y resto de empleados (siguen prácticas diarias)—cada uno debe conocer claramente su rol. Cuarto, abrid las versiones Word y personalizadlas: cambiad el nombre de la empresa, adaptad ejemplos a vuestro sector, ajustad medidas a vuestros recursos. Quinto, usad la checklist como plan de acción: marcad qué controles YA tenéis implementados (¡celebrad lo que ya está bien!) e identificad qué falta—esto crea vuestro roadmap de seguridad. Sexto, revisad periódicamente (trimestral o semestral) el progreso: ¿implementamos 5 controles nuevos este trimestre? ¿Mejoramos de 40% a 60% cumplimiento? Esto visualiza mejora continua.


### 11.6. Políticas disponibles en INCIBE

**Conjunto completo de políticas:**

* Protección del puesto de trabajo
* Almacenamiento en equipos de trabajo
* Aplicaciones permitidas
* Política de contraseñas
* Política de teletrabajo
* Copias de seguridad
* Y muchas más especializadas

Note: INCIBE ofrece un catálogo completo de políticas que cubren prácticamente todos los aspectos de seguridad relevantes para PYMEs. "Protección del puesto de trabajo" cubre lo que hemos estudiado en detalle en esta unidad. "Almacenamiento en equipos" trata sobre qué se puede guardar localmente, cifrado de almacenamiento, gestión de medios extraíbles. "Aplicaciones permitidas" establece repositorio de software autorizado y auditoría de instalaciones. "Política de contraseñas" define requisitos de complejidad, gestión, y no reutilización. "Política de teletrabajo" especifica medidas adicionales para trabajo remoto (VPN obligatoria, seguridad WiFi doméstica, espacios de trabajo en casa). "Copias de seguridad" detalla qué, cuándo, dónde y cómo hacer backups. Existen también políticas sobre gestión de proveedores, uso de dispositivos móviles (MDM), gestión de incidentes, etc. Recomendación: comenzar con las 3-4 más críticas para vuestro negocio, implementarlas bien, y gradualmente ampliar. Es mejor tener 4 políticas realmente cumplidas que 15 solo en papel.


### 11.7. Beneficios de usar políticas INCIBE

**Ventajas prácticas:**

* **Gratuitas** y profesionalmente desarrolladas
* **Adaptadas** al contexto PYME español
* **Editables** para personalización
* **Completas** con checklists ejecutables
* **Alineadas** con normativa española (LOPDGDD) y europea (GDPR)
* **Actualizadas** periódicamente por INCIBE

Note: Usar las políticas de INCIBE tiene ventajas enormes para PYMEs. Son completamente gratuitas, eliminando la barrera de coste—contratar consultoría para desarrollar políticas desde cero puede costar miles de euros; INCIBE lo ofrece gratis. Están desarrolladas profesionalmente por expertos en ciberseguridad del instituto nacional, garantizando calidad y exhaustividad. Están específicamente adaptadas a la realidad de PYMEs españolas—entienden las limitaciones de recursos y proponen medidas proporcionales y realistas, no soluciones de gran empresa. Son documentos vivos en formato editable que podéis modificar para vuestro sector, tamaño, y necesidades específicas. Incluyen checklists prácticos y ejecutables que transforman conceptos abstractos en acciones concretas—no solo dicen "protege los equipos" sino "activa cifrado, configura bloqueo, instala antivirus" con pasos verificables. Están alineadas con las normativas legales aplicables en España y Europa (LOPDGDD, GDPR), ayudando con cumplimiento normativo—si seguís las políticas, estáis mejor posicionados para cumplir obligaciones legales. INCIBE las actualiza periódicamente reflejando amenazas emergentes y cambios normativos. Finalmente, usarlas demuestra diligencia debida—si sufrís un incidente, poder mostrar que implementasteis políticas oficiales de INCIBE ayuda legal y reputacionalmente.

---

## Bibliografía

* [ISO/IEC 27001:2022](https://www.iso.org/standard/27001) - Information Security Management
* [GDPR](https://gdpr-info.eu/) - General Data Protection Regulation
* [CCN-STIC 800](https://www.ccn-cert.cni.es/series-ccn-stic/800-guia-esquema-nacional-de-seguridad.html) - Guías ENS
* [INCIBE - Protección del puesto de trabajo](https://www.incibe.es/)
* LOPDGDD - Ley Orgánica 3/2018

Note: Estos recursos son fundamentales y de acceso gratuito. Dedicad tiempo a estudiarlos en profundidad, especialmente ISO 27001 y GDPR.
