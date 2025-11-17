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

Note: El puesto de trabajo moderno ha evolucionado significativamente con la digitalización y el teletrabajo. Ya no se limita a un escritorio físico con un PC en la oficina. Puede ser cualquier ubicación con conexión a internet desde la cual el empleado accede a los recursos corporativos: una laptop en casa, una tablet en un café, o un smartphone en movimiento. Esta flexibilidad aumenta la productividad pero también amplía la superficie de ataque, ya que cada ubicación y dispositivo representa un potencial punto de entrada para amenazas. Por ello, la protección del puesto debe adaptarse a esta realidad distribuida y móvil.


### 1.2. Elementos del puesto de trabajo

**Componentes principales:**

* **Dispositivos hardware**: PCs, laptops, tablets, smartphones.
* **Software**: Aplicaciones para realizar tareas.
* **Comunicación y red**: Internet, VPN, acceso a servidores.
* **Instalaciones físicas**: Oficinas, salas de reuniones.
* **Acceso a datos**: Permisos sobre información.
* **Personal**: El empleado y sus hábitos de trabajo.

Note: Cada uno de estos seis elementos representa un vector potencial de ataque o vulnerabilidad. Los dispositivos hardware pueden ser robados o infectados; el software puede tener vulnerabilidades o ser malicioso; las comunicaciones pueden ser interceptadas; las instalaciones físicas pueden permitir accesos no autorizados; los permisos de datos pueden estar mal configurados; y el personal puede cometer errores o ser víctima de ingeniería social. Como alumnos y alumnas debéis comprender que la seguridad del puesto de trabajo requiere proteger simultáneamente todos estos elementos de forma coordinada, ya que el fallo en uno solo de ellos puede comprometer la seguridad global del sistema.


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

Note: Una normativa en el contexto del puesto de trabajo es comparable al código de circulación en el tráfico vial: establece reglas claras que todos deben seguir para garantizar un entorno seguro. Sin una normativa bien definida, cada empleado seguiría sus propios criterios, lo que generaría inconsistencias y vulnerabilidades de seguridad. La normativa debe cubrir aspectos como el control de acceso físico y lógico, uso de dispositivos, instalación de software, gestión de contraseñas, políticas de escritorio limpio, y procedimientos ante incidentes. Es fundamental que sea clara, específica, alcanzable y comunicada efectivamente a todo el personal para asegurar su cumplimiento.


### 2.1. ¿Qué es una normativa? II

**Ejemplo práctico de normativa:**

* **Restricciones de acceso**: Solo personal autorizado accede
  a datos confidenciales.
* **Seguridad física/digital**: Cerraduras, contraseñas complejas, MFA.
* **Actualizaciones**: Software actualizado con últimos parches.
* **Buenas prácticas**: Bloquear pantalla, evitar redes públicas.

Note: Veamos un ejemplo concreto de cómo se traduce una normativa en medidas específicas. Las restricciones de acceso impl ican que cada empleado solo debe poder acceder a los datos necesarios para su función, aplicando el principio de mínimo privilegio. La seguridad física incluye medidas como cajones con llave para documentos sensibles, control de acceso con tarjetas a ciertas áreas, mientras que la digital requiere contraseñas de al menos 12 caracteres con complejidad (mayúsculas, minúsculas, números, símbolos) y autenticación multifactor para sistemas críticos. Las actualizaciones deben aplicarse en un plazo máximo de 48 horas para parches críticos. Las buenas prácticas diarias incluyen bloquear la pantalla con Win+L al ausentarse, usar VPN en redes públicas, y reportar cualquier actividad sospechosa inmediatamente a IT.


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

Note: Los dispositivos hardware son los componentes físicos que los empleados utilizan para acceder a los sistemas y datos corporativos. Son críticos porque almacenan información localmente y pueden ser robados, perdidos o comprometidos. A continuación veremos los cuatro escenarios de riesgo más comunes asociados a estos dispositivos y las medidas completas (Política, Normativa y Procedimiento) para mitigar cada uno. Es importante entender que la protección hardware requiere una combinación de medidas físicas (cerraduras, control de acceso) y lógicas (cifrado, autenticación).


### 2bis.1.1. Pérdida o Robo de Dispositivos

**Escenario de riesgo:**

* **Riesgo**: Dispositivo robado o perdido expone datos confidenciales.
* **Consecuencias**: Acceso no autorizado a información sensible,
  credenciales comprometidas, pérdida de propiedad intelectual.
* **Impacto**: ALTO - Puede afectar cumplimiento legal (GDPR).

Note: Este es uno de los escenarios más comunes y graves. Cada año se pierden o roban millones de dispositivos corporativos. Si el dispositivo no está protegido con cifrado, cualquier persona con acceso físico puede extraer todos los datos simplemente conectando el disco a otro ordenador o arrancando desde un USB. Las consecuencias van desde la exposición de datos personales de clientes (violación GDPR con multas de hasta 20M€) hasta el robo de propiedad intelectual valorada en millones. Los empleados que trabajan en movilidad (aeropuertos, cafeterías, transporte público) son especialmente vulnerables. Este escenario es prevenible con las medidas adecuadas.


### 2bis.1.1. Pérdida o Robo de Dispositivos II

**Medidas de seguridad:**

**Política**: La organización protegerá todos los dispositivos con
medidas que garanticen seguridad ante pérdida o robo.

**Normativa**:
* Autenticación segura obligatoria (contraseña + MFA).
* Bloqueo automático tras 5 minutos de inactividad.
* Cifrado de disco completo en todos los dispositivos.

Note: La Política establece el compromiso organizativo general de proteger los dispositivos. La Normativa concreta ese compromiso en tres reglas específicas y medibles. La autenticación segura con contraseña compleja más MFA (algo que sabes + algo que tienes) asegura que aunque roben el dispositivo, no puedan acceder sin las credenciales. El bloqueo automático protege en caso de descuido momentáneo. El cifrado de disco completo (BitLocker en Windows, FileVault en macOS) es la medida técnica clave: cifra todos los datos del disco con AES-256, haciendo que sin la contraseña correcta el disco sea completamente ilegible. Sin cifrado, los datos son vulnerables; con cifrado, el dispositivo robado es un pisapapeles inútil para el ladrón.


### 2bis.1.1. Pérdida o Robo de Dispositivos III

**Procedimiento de protección:**

1. **Activar bloqueo automático**: Configurar en Windows
   (Configuración > Cuentas > Opciones de inicio de sesión >
   Requerir inicio > 5 minutos). macOS (Preferencias > Seguridad).
2. **Activar cifrado**: Windows (BitLocker), macOS (FileVault).
3. **Verificar cifrado**: Comprobar estado en configuración.
4. **Reportar pérdida**: Llamar a IT inmediatamente al 900-XXX-XXX.

Note: El Procedimiento proporciona los pasos ejecutables concretos. Para el bloqueo automático en Windows, ir a Configuración, Cuentas, Opciones de inicio de sesión, y en "Requerir inicio de sesión" seleccionar "Cuando el PC se reactive desde el modo de suspensión" y configurar el protector de pantalla en 5 minutos. Para cifrado en Windows Pro/Enterprise, buscar "BitLocker" en el Panel de Control, seleccionar "Activar BitLocker" en cada unidad, elegir "Usar contraseña para desbloquear", y guardar la clave de recuperación en ubicación segura (nunca en el propio dispositivo). En macOS, ir a Preferencias del Sistema, Seguridad y Privacidad, FileVault, "Activar FileVault". Verificar que aparece "FileVault está activado" o "BitLocker activado". Ante pérdida o robo, reportar en menos de 1 hora para que IT pueda ejecutar borrado remoto si el dispositivo se conecta.


### 2bis.1.2. Acceso No Autorizado

**Escenario de riesgo:**

* **Riesgo**: Dispositivo desbloqueado permite acceso no autorizado.
* **Consecuencias**: Manipulación de datos, instalación de malware,
  robo de credenciales en memoria.
* **Impacto**: MEDIO-ALTO - Compromiso de sesión activa.

Note: Este escenario ocurre cuando un empleado deja su puesto desbloqueado y alguien (un compañero curioso, un visitante, personal de limpieza, o un atacante) accede físicamente al equipo. Con sesión activa, el atacante tiene acceso inmediato a todo lo que el usuario legítimo puede hacer: leer emails, acceder a sistemas, copiar archivos, instalar keyloggers, o incluso enviar emails suplantando al usuario. Los ataques internos son más comunes de lo que se piensa (empleados descontentos, competidores disfrazados en eventos). Muchas brechas empiezan con un "solo me ausento un minuto" que se convierte en 15 minutos y permite a alguien introducir un USB malicioso o robar datos. La prevención es simple: bloquear siempre, sin excepciones.


### 2bis.1.2. Acceso No Autorizado II

**Medidas de seguridad:**

**Política**: Proteger dispositivos garantizando integridad y
confidencialidad ante accesos no autorizados.

**Normativa**:
* Bloqueo automático tras 5-10 min de inactividad.
* Contraseñas seguras (12+ caracteres, complejidad).
* Autenticación biométrica cuando sea posible.

Note: La Política mantiene el compromiso general, la Normativa lo concreta. El bloqueo automático actúa como red de seguridad cuando el usuario olvida bloquear manualmente—el sistema lo hace automáticamente. Las contraseñas seguras de mínimo 12 caracteres con mayúsculas, minúsculas, números y símbolos especiales son mucho más resistentes a ataques de fuerza bruta (un espacio de búsqueda de 10^21 combinaciones vs 10^9 de contraseñas simples). La autenticación biométrica (huella dactilar, reconocimiento facial con Windows Hello o Touch ID) añade comodidad sin sacrificar seguridad, ya que es difícil de suplantar y el usuario no puede "olvidarla" o escribirla en un post-it.


### 2bis.1.2. Acceso No Autorizado III

**Procedimiento de protección:**

1. **Configurar contraseña compleja**: Mínimo 12 caracteres,
   incluir May, min, números, símbolos. Usar gestor contraseñas.
2. **Activar autenticación biométrica**: Windows Hello (huella/facial),
   Touch ID en macOS.
3. **Bloquear manualmente**: Win+L (Windows), Ctrl+Cmd+Q (macOS),
   Super+L (Linux). SIEMPRE al ausentarse.

Note: Para crear contraseñas seguras y memorables, usar técnica de passphrase: "Mi-Hija-Cumple-15-En-Julio!" es mucho más fuerte y memorable que "P@ssw0rd". Mejor aún, usar un gestor de contraseñas corporativo (Bitwarden, 1Password, LastPass) que genera y almacena contraseñas únicas ultra-seguras para cada sistema. Para Windows Hello, ir a Configuración, Cuentas, Opciones de inicio de sesión, configurar PIN primero, luego Reconocimiento facial o Huella dactilar (requiere hardware compatible). En macOS, Preferencias, Touch ID, añadir huella. El bloqueo manual debe volverse un reflejo automático: "Me levanto = Win+L". Entrenar este hábito con práctica deliberada. En oficinas abiertas es especialmente crítico—un segundo de descuido puede comprometer años de seguridad.


### 2bis.1.3. Falta de Cifrado

**Escenario de riesgo:**

* **Riesgo**: Datos en dispositivo sin cifrar son fácilmente extraíbles.
* **Consecuencias**: Exposición total de información almacenada
  en caso de robo o acceso físico no autorizado.
* **Impacto**: CRÍTICO - Pérdida total de confidencialidad.

Note: Sin cifrado, las contraseñas de acceso al sistema operativo son trivialmente eludibles. Un atacante puede simplemente arrancar el dispositivo desde un USB live, montar el disco duro, y copiar todos los archivos sin que el sistema operativo proteja nada. O puede extraer físicamente el disco y conectarlo a otro ordenador. En 5-10 minutos tiene acceso completo a TODOS los datos: documentos, emails descargados, historial de navegación, contraseñas guardadas en navegadores, claves SSH, tokens de autenticación en caché. El cifrado de disco completo es por ello IMPRESCINDIBLE en cualquier dispositivo que salga de instalaciones seguras o contenga datos sensibles. Es la diferencia entre una brecha masiva de datos y un dispositivo inútil para el atacante.


### 2bis.1.3. Falta de Cifrado II

**Medidas de seguridad:**

**Política**: Todos los dispositivos con datos sensibles estarán cifrados
para proteger confidencialidad ante acceso físico.

**Normativa**:
* Cifrado completo de disco obligatorio en todos los dispositivos.
* Prohibido almacenar información confidencial en dispositivos
  sin cifrar o personales no autorizados.

Note: La Política es clara: proteger mediante cifrado. La Normativa la hace ejecutable: cifrado de disco completo (FDE - Full Disk Encryption) es obligatorio sin excepciones. Esto significa que desde el momento en que el dispositivo arranca, hasta el último byte del disco está cifrado con algoritmo robusto (AES-256). Sin la clave de cifrado (derivada de la contraseña o del TPM), los datos son basura aleatoria indescifrable. La segunda norma es crítica: prohibir almacenar datos confidenciales en dispositivos sin protección—esto incluye USBs personales, discos externos sin cifrar, o el portátil personal del empleado. Si se necesita trabajar en dispositivo personal, debe cumplir mismos estándares (cifrado, antivirus, actualizaciones) que los corporativos.


### 2bis.1.3. Falta de Cifrado III

**Procedimiento de activación:**

1. **Windows (BitLocker)**: Panel Control > BitLocker >
   Activar BitLocker > Usar contraseña > Guardar clave recuperación.
2. **macOS (FileVault)**: Preferencias > Seguridad > FileVault >
   Activar FileVault > Guardar clave recuperación.
3. **Verificar**: Comprobar que indica "Cifrado activado".
4. **Excepciones**: Reportar a IT si no puede activarse.

Note: En Windows, BitLocker requiere edición Pro o Enterprise (Home no lo incluye por defecto, considerar upgrade). Buscar "Administrar BitLocker" en el menú inicio, seleccionar la unidad del sistema (C:), "Activar BitLocker", elegir "Introducir contraseña" para desbloquear, crear contraseña segura (12+ caracteres), CRÍTICO: guardar la clave de recuperación en ubicación segura externa (OneDrive corporativo, USB guardado en caja fuerte, impreso en ubicación segura)—esta clave es la única manera de recuperar datos si olvidas la contraseña. El proceso de cifrado inicial puede tardar horas dependiendo del tamaño del disco; se puede usar el PC mientras cifra en segundo plano. En macOS, FileVault es más sencillo: Preferencias del Sistema, Seguridad y Privacidad, pestaña FileVault, clic en candado para autenticar, "Activar FileVault", elegir si permitir recuperación con cuenta iCloud o crear clave de recuperación local (recomendado para entornos corporativos). Verificar que el estado cambia a "FileVault está activado". Si hay problemas técnicos (hardware incompatible, falta módulo TPM), reportar inmediatamente a IT para solución alternativa o cifrado software.


### 2bis.1.4. Infección de Malware

**Escenario de riesgo:**

* **Riesgo**: Descarga de archivos maliciosos o uso de medios no seguros.
* **Consecuencias**: Malware captura información, actúa como backdoor,
  encripta datos (ransomware), se propaga en red.
* **Impacto**: MUY ALTO - Puede comprometer toda la red corporativa.

Note: El malware en dispositivos hardware puede llegar por múltiples vías: emails de phishing con adjuntos maliciosos, descargas de internet desde sitios comprometidos, memorias USB infectadas (ataque USB drop), exploit kits que aprovechan vulnerabilidades del navegador, o incluso pre-instalado en hardware comprometido en la cadena de suministro. Una vez instalado, el malware puede hacer prácticamente cualquier cosa: keyloggers capturan todo lo que tecleas (contraseñas incluidas), infostealers roban archivos y credenciales, RATs (Remote Access Trojans) dan control total del PC al atacante, ransomware cifra todos los archivos y exige pago, cryptominers usan tus recursos para minar criptomonedas, botnets convierten tu PC en parte de una red de ataque. Peor aún, malware sofisticado puede propagarse lateralmente por la red interna infectando otros dispositivos. La defensa requiere múltiples capas.


### 2bis.1.4. Infección de Malware II

**Medidas de seguridad:**

**Política**: Proteger dispositivos contra malware mediante defensa
en profundidad y prevención proactiva.

**Normativa**:
* Antivirus y firewall activos y actualizados obligatorios.
* Prohibida instalación de software no autorizado por IT.
* Escaneo obligatorio de medios extraíbles antes de uso.

Note: La Política habla de "defensa en profundidad"—múltiples capas de seguridad. La Normativa define tres capas concretas. Primera: antivirus y firewall—el antivirus detecta y bloquea malware conocido mediante firmas y comportamiento heurístico, el firewall bloquea conexiones de red no autorizadas. Deben actualizarse diariamente (las firmas de malware se actualizan constantemente). Segunda: control de software—solo se permite instalar software autorizado y verificado por IT, eliminando la vía de infección por "descargas de internet". Los usuarios no deben tener permisos de administrador local (principio de mínimo privilegio) para que no puedan instalar software. Tercera: control de medios extraíbles—las memorias USB son vector común de malware, por lo que deben escanearse obligatoriamente antes de abrir cualquier archivo, o mejor aún, deshabilitar puertos USB por política para usuarios que no los necesiten legítimamente.


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

Note: Para instalar antivirus corporativo (Symantec, McAfee, Sophos, Windows Defender ATP, etc.), seguir las instrucciones específicas del departamento IT—generalmente se despliega centralmente via GPO o script, el usuario solo debe ejecutar el instalador. Verificar que aparece icono del antivirus en la barra de tareas y que indica "Protegido" o "Actualizado". Para activar firewall en Windows, buscar "Firewall de Windows Defender", asegurar que está "Activado" en redes de dominio, privadas y públicas—bloquear todo el tráfico entrante por defecto excepto aplicaciones específicamente permitidas. En macOS, Preferencias del Sistema, Seguridad y Privacidad, Firewall, "Activar Firewall", "Opciones de Firewall", "Bloquear todas las conexiones entrantes" salvo aplicaciones firmadas. Configurar Windows Update o macOS Software Update en automático para recibir parches inmediatamente. Lo más importante: formar al usuario en navegación segura—no abrir adjuntos de emails inesperados aunque parezcan legítimos (verificar con el remitente por otro canal), no instalar extensiones de navegador desconocidas, usar solo tiendas oficiales (Microsoft Store, Mac App Store) si necesitan software. Si ven email sospechoso, NUNCA hacer clic, reportar inmediatamente al botón "Reportar Phishing" o reenviar a abuse@empresa.com.

---

### 2bis.2. Software y Aplicaciones

**Herramientas para realizar tareas:**

* Aplicaciones de oficina (Word, Excel, PowerPoint)
* Software de gestión (CRM, ERP, RRHH)
* Herramientas de comunicación (email, mensajería)
* Navegadores web y extensiones
* Software especializado por departamento

Note: El software y las aplicaciones son las herramientas que los empleados usan diariamente para realizar su trabajo. Desde procesadores de texto hasta complejos sistemas ERP, todo software que procesa o almacena datos corporativos es un activo crítico de seguridad. El software puede tener vulnerabilidades explotables, puede ser malicioso si se instala de fuentes no confiables, puede tener configuraciones inseguras por defecto, o puede ser usado de formas no previstas que comprometan la seguridad. Además, el software desactualizado es una de las vías más comunes de compromiso—los atacantes buscan activamente sistemas sin parchar para explotar vulnerabilidades públicamente conocidas.


### 2bis.2.1. Software No Autorizado

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Software no autorizado puede contener malware oculto.
* **Política**: Garantizar seguridad mediante control de software.
* **Normativa**: Solo software aprobado por IT. Solicitar aprobación
  para nuevas necesidades.
* **Procedimiento**: Consultar lista software autorizado en intranet,
  solicitar nuevos via ticket IT justificando necesidad.

Note: El software no autorizado es peligroso porque no ha pasado por el proceso de verificación de seguridad de IT—puede contener vulnerabilidades conocidas, puede ser una versión troyanizada con malware, puede violar licencias y exponer a la empresa a riesgos legales, o puede tener configuraciones inseguras. El procedimiento requiere que los empleados primero consulten el catálogo de software aprobado disponible en la intranet corporativa o portal de autoservicio. Si necesitan software no disponible, deben abrir un ticket justificando la necesidad de negocio. IT evaluará el software (seguridad, licencias, compatibilidad, coste de mantenimiento) antes de aprobarlo. Una vez aprobado, IT lo instalará centralmente o proporcionará installer autorizado. Esto protege a la organización y al usuario—si el software causa problemas, IT puede dar soporte; si no está autorizado, el usuario asume la responsabilidad.


### 2bis.2.2. Software Desactualizado

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Vulnerabilidades sin parchar son explotadas por atacantes.
* **Política**: Mantener todo el software actualizado y seguro.
* **Normativa**: Actualizaciones automáticas activas. Parches críticos
  en 48-72h.
* **Procedimiento**: Activar Windows Update / macOS Update en automático.
  IT despliega parches críticos centralmente.

Note: El software desactualizado es objetivo prioritario para atacantes—cuando se publica un parche de seguridad, los atacantes hacen ingeniería inversa para descubrir la vulnerabilidad y crear exploits. Los sistemas sin actualizar quedan extremadamente vulnerables. WannaCry en 2017 explotó una vulnerabilidad de Windows para la que Microsoft había publicado parche dos meses antes—organizaciones que no actualizaron sufrieron ransomware masivo. El procedimiento requiere activar actualizaciones automáticas en todos los dispositivos. En Windows: Configuración, Actualización y Seguridad, Windows Update, "Opciones avanzadas", activar todas las opciones de actualización automática. En macOS: Preferencias, Actualización de Software, marcar todas las casillas de actualización automática. Para software crítico empresarial (SAP, Oracle, etc.), IT despliega parches centralmente vía herramientas de gestión (WSUS, SCCM, Intune). Los parches críticos de seguridad deben aplicarse en ventana de 48-72 horas máximo.


### 2bis.2.3. Permisos Excesivos en Aplicaciones

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Permisos mal configurados permiten acceso no autorizado
  a funciones sensibles.
* **Política**: Aplicar principio de mínimo privilegio en aplicaciones.
* **Normativa**: Permisos según rol. Revisión trimestral por IT.
* **Procedimiento**: IT asigna permisos basados en función. Usuarios
  solicitan accesos adicionales justificando necesidad.

Note: Los permisos excesivos en aplicaciones son peligrosos—si un usuario tiene más acceso del necesario para su función, aumenta el riesgo en caso de compromiso de su cuenta (accidental o malicioso). Por ejemplo, un empleado de ventas no necesita permisos de administrador en el CRM, ni un desarrollador junior necesita acceso a datos de producción. El procedimiento implementa el principio de mínimo privilegio: cuando un empleado nuevo se incorpora, IT configura sus permisos basándose estrictamente en su rol y función. Si necesita accesos adicionales, debe justificarlos (por ejemplo, "necesito acceso temporal a módulo de finanzas para generar reporte X para el proyecto Y"). IT aprueba accesos excepcionales por tiempo limitado. Trimestralmente, IT audita los permisos de todos los usuarios, revocando permisos no utilizados o que ya no son necesarios (por ejemplo, si un empleado cambió de departamento). Esto minimiza la superficie de ataque.


### 2bis.2.4. Fugas via Aplicaciones en la Nube

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Configuración insegura en apps nube filtra información.
* **Política**: Uso seguro y controlado de aplicaciones cloud.
* **Normativa**: Solo apps cloud aprobadas. Configuración de
  privacidad obligatoria. No compartir datos sensibles en apps no seguras.
* **Procedimiento**: Usar solo OneDrive/SharePoint corporativo,
  Google Workspace empresarial, o apps aprobadas. Verificar
  configuración de compartición antes de subir archivos.

Note: Las aplicaciones en la nube (SaaS) son cómodas pero riesgosas si no se gestionan bien. Dropbox personal, Google Drive personal, WeTransfer, etc., no tienen los controles de seguridad corporativos—pueden estar accesibles desde cualquier dispositivo, pueden tener enlaces compartidos configurados inadvertidamente como públicos, pueden no cifrar en tránsito o en reposo, y están fuera del control de IT. El procedimiento establece que solo se deben usar servicios cloud aprobados corporativamente (OneDrive for Business, SharePoint Online, Google Workspace con dominio empresarial, Box Enterprise, etc.). Estos servicios tienen controles administrativos centralizados, DLP (Data Loss Prevention), auditoría de accesos, y cumplimiento normativo. Antes de subir un archivo sensible, el usuario debe verificar la configuración de compartición: ¿quién tiene acceso? ¿es solo interno? ¿requiere autenticación? ¿tiene fecha de expiración? Configurar siempre en "Solo personas de la organización" y nunca "Cualquiera con el enlace" para datos confidenciales.


### 2bis.3. Comunicación y Acceso a Red

**Conectividad para acceder a recursos:**

* Redes corporativas (cableadas, WiFi)
* Conexiones remotas (VPN, acceso directo)
* Redes públicas (aeropuertos, cafeterías, hoteles)
* Internet general y navegación web
* Aplicaciones en la nube (SaaS)

Note: La comunicación y el acceso a la red son esenciales para que los empleados trabajen, pero también representan uno de los mayores riesgos de seguridad. Cada conexión de red es un potencial vector de ataque: redes WiFi públicas sin cifrar permiten interceptación de tráfico (man-in-the-middle), conexiones directas a internet sin VPN exponen la IP real de la organización, navegadores con configuraciones inseguras filtran información, y aplicaciones que comunican sin cifrado envían datos en claro. La seguridad de red requiere autenticación fuerte, cifrado de tráfico, segmentación de redes, y políticas de uso aceptable claras.


### 2bis.3.1. Redes WiFi Públicas Inseguras

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Tráfico interceptado en redes públicas sin cifrar.
* **Política**: Garantizar seguridad en comunicaciones desde cualquier
  ubicación.
* **Normativa**: VPN obligatoria para accesos remotos. Prohibido acceso
  a recursos corporativos desde redes públicas sin VPN.
* **Procedimiento**: Instalar cliente VPN corporativo, conectar antes
  de acceder a cualquier recurso empresarial. En WiFi público: VPN ON.

Note: Las redes WiFi públicas son extremadamente inseguras porque cualquier persona conectada a la misma red puede interceptar el tráfico de otros (ataques de tipo sniffing con Wireshark, Ettercap, etc.). Peor aún, los atacantes crean redes WiFi maliciosas con nombres similares a redes legítimas ("Starbucks Free WiFi", "Airport_Guest") para que los usuarios se conecten y capturar todo su tráfico. Sin cifrado, contraseñas, cookies de sesión, emails, archivos descargados—todo viaja en claro. La VPN (Virtual Private Network) cifra todo el tráfico del dispositivo dentro de un túnel seguro hasta el servidor VPN corporativo, haciendo que sea indescifrable para interceptores. El procedimiento requiere instalar el cliente VPN corporativo (Cisco AnyConnect, GlobalProtect, OpenVPN, etc.) según instrucciones de IT, autenticarse con credenciales corporativas (generalmente usuario + contraseña + MFA), y SIEMPRE activar la VPN ANTES de acceder a email, intranet, aplicaciones corporativas, etc., cuando se esté en red no confiable. Regla simple: "WiFi público = VPN ON, sin excepciones".


### 2bis.3.2. Acceso No Autorizado a Red Corporativa

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas no autorizadas intentan conectarse a la red interna.
* **Política**: Proteger acceso a red corporativa contra intrusiones.
* **Normativa**: Autenticación multifactor (MFA) obligatoria. Solo
  dispositivos autorizados y registrados pueden conectarse.
* **Procedimiento**: IT registra dispositivos corporativos en NAC
  (Network Access Control). Usuarios activan MFA en portales de acceso.

Note: El acceso no autorizado a la red corporativa puede ocurrir de varias formas: atacantes que logran credenciales válidas (phishing), dispositivos personales comprometidos que se conectan, visitantes que se conectan a WiFi corporativa sin autorización, o incluso atacantes físicos que conectan cable Ethernet en puertos desprotegidos. La autenticación multifactor (MFA) es la defensa principal—incluso si roban la contraseña, no pueden acceder sin el segundo factor (código SMS, push notification, token hardware FIDO2). El NAC (Network Access Control) con soluciones como Cisco ISE, ForeScout, o Microsoft NAP verifica que los dispositivos que intentan conectarse estén registrados, cumplan políticas de seguridad (antivirus actualizado, cifrado activo, parches instalados), y pertenezcan a usuarios autorizados. Si un dispositivo no cumple, se le deniega acceso o se le coloca en red cuarentena con acceso limitado. IT debe registrar cada dispositivo corporativo en el NAC con su MAC address y certificado. Para WiFi corporativa, usar WPA2-Enterprise o WPA3-Enterprise con autenticación RADIUS, nunca WPA2-PSK con contraseña compartida.


### 2bis.3.3. Intercepción de Datos en Tránsito

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Información sensible transmitida sin cifrado es interceptada.
* **Política**: Cifrar toda comunicación de datos sensibles.
* **Normativa**: Datos confidenciales deben cifrarse en tránsito.
  Emails sensibles deben usar cifrado S/MIME o PGP.
* **Procedimiento**: Verificar HTTPS (candado) en navegador. Para emails
  sensibles, usar cifrado S/MIME en Outlook o cifrado PGP.

Note: Los datos en tránsito (moviéndose por la red) son vulnerables si no están cifrados. HTTP sin S transmite en texto claro, permitiendo que cualquier router intermedio o atacante en la red capture credenciales, datos personales, etc. HTTPS cifra la comunicación con TLS, protegiendo la confidencialidad. El usuario debe verificar siempre el candado verde en el navegador antes de introducir información sensible—si no hay candado, la conexión no es segura. Para emails altamente confidenciales (informes financieros, información legal, datos personales masivos), el cifrado del transporte (TLS entre servidores de email) no es suficiente—se necesita cifrado end-to-end donde solo emisor y receptor pueden descifrar. S/MIME (Secure/Multipurpose Internet Mail Extensions) usa certificados digitales para firmar y cifrar emails en Outlook—IT debe proporcionar certificado S/MIME al usuario e instalar en Outlook. Alternativamente, PGP (Pretty Good Privacy) con plugins como Mailvelope para webmail. El procedimiento para enviar email cifrado con S/MIME en Outlook: componer email, Opciones, Cifrar, Cifrar con S/MIME, enviar—solo el destinatario con certificado correspondiente podrá descifrarlo.


### 2bis.3.4. Fugas via Aplicaciones Cloud No Seguras

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Apps cloud mal configuradas exponen datos públicamente.
* **Política**: Uso controlado de servicios cloud con seguridad verificada.
* **Normativa**: Solo apps cloud aprobadas por IT. Configuración
  de compartición revisada antes de uso.
* **Procedimiento**: Usar apps corporativas (OneDrive, SharePoint).
  Al compartir, verificar: ¿Quién accede? ¿Autenticación requerida?

Note: Los servicios cloud (SaaS) tienen configuraciones de compartición muy flexibles que pueden generar exposiciones accidentales. Ejemplos reales: buckets S3 de AWS configurados como públicos exponiendo millones de registros, enlaces de Google Drive/OneDrive con "cualquiera con el enlace" indexados por Google y accesibles públicamente, presentaciones confidenciales en Slideshare públicas. El procedimiento requiere usar exclusivamente servicios cloud aprobados corporativamente que IT puede gestionar centralmente. Al compartir un archivo en OneDrive/SharePoint: clic derecho, Compartir, establecer "Personas específicas" (no "Cualquiera"), introducir emails de destinatarios, establecer "Pueden ver" (no "Pueden editar" salvo necesario), marcar "Bloquear descarga" si es muy sensible, establecer fecha de expiración. IT debe configurar DLP (Data Loss Prevention) en Microsoft 365 / Google Workspace para que detecte automáticamente cuando se intenta compartir externamente contenido sensible (números de tarjetas, DNIs, etc.) y bloquee o alerte.

---

### 2bis.4. Instalaciones Físicas

**Espacios físicos de trabajo:**

* Oficinas individuales y abiertas (open space)
* Salas de reuniones y espacios compartidos
* Centros de datos y salas técnicas
* Áreas de recepción y zonas públicas
* Instalaciones de almacenamiento (archivos, bóvedas)

Note: Las instalaciones físicas son a menudo el eslabón olvidado de la seguridad—nos enfocamos en firewalls y antivirus pero descuidamos puertas, ventanas y personas. La seguridad física es crítica porque el acceso físico generalmente equivale a compromiso total—alguien con acceso físico a un dispositivo puede bypasear la mayoría de controles lógicos. Las instalaciones deben protegerse con múltiples capas: perímetro exterior (vallas, guardias), acceso a edificio (puertas con tarjeta, recepcionista), acceso a áreas sensibles (control biométrico, doble autenticación), y protección de activos individuales (cajones con llave, destructoras de papel). También incluye aspectos menos obvios como visitantes no acompañados, personal de limpieza con acceso nocturno, técnicos de mantenimiento, o "tailgating" (colarse detrás de alguien autorizado).


### 2bis.4.1. Acceso No Autorizado a Áreas Restringidas

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Personas sin autorización acceden a áreas sensibles.
* **Política**: Proteger instalaciones con control de acceso físico robusto.
* **Normativa**: Solo personal autorizado en áreas restringidas.
  Accesos registrados y monitoreados con tarjetas/biometría.
* **Procedimiento**: Usar tarjeta de acceso corporativa. En áreas
  críticas (datacenter), autenticación adicional (PIN+huella). Reportar
  personas no identificadas a seguridad inmediatamente.

Note: Las áreas restringidas como centros de datos, salas de servidores, oficinas ejecutivas, o archivos confidenciales deben tener control de acceso estricto. El sistema de control de acceso (típicamente tarjetas RFID + lector) registra quién entra, cuándo, y a dónde—estos logs son auditables. Para áreas más críticas, se requiere autenticación de dos factores físicos: tarjeta (algo que tienes) + PIN o huella dactilar (algo que sabes/eres). Esto previene que alguien que robe o encuentre una tarjeta pueda acceder. El procedimiento para empleados: presentar tarjeta en lector, esperar tono/luz verde, abrir puerta, cerrar tras de sí asegurando que queda cerrada (no dejarla abierta para "el siguiente"). NUNCA permitir "tailgating"—si alguien intenta seguirte sin tarjeta propia, cortésmente indicar que debe usar su propia tarjeta (incluso si parece compañero). Si ves a alguien sin identificación visible en área restringida, acércate cortésmente ("¿Puedo ayudarte? ¿Llevas tu tarjeta de visitante?") y si es sospechoso, llamar a seguridad. En datacenters, normalmente hay cámaras grabando 24/7 y se requiere  registro en bitácora física además del electrónico.


### 2bis.4.2. Exposición de Información en Espacios Compartidos

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Documentos o dispositivos desatendidos en áreas comunes.
* **Política**: Proteger información mediante política de escritorio limpio.
* **Normativa**: No dejar documentos sensibles en escritorio. Información
  confidencial en archivadores con llave. Pantallas bloqueadas o apagadas.
* **Procedimiento**: Al finalizar jornada: guardar documentos en cajón
  con llave, bloquear PC, apagar monitor. Usar filtros de privacidad
  en laptops en espacios públicos.

Note: La política de escritorio limpio (Clean Desk Policy) es simple pero efectiva. Muchas brechas empiezan con documentos o post-its con contraseñas dejados visibles. En espacios de open office, cualquiera que pase puede ver tu pantalla o leer documentos en tu escritorio. En salas de reuniones, los documentos olvidados tras la reunión pueden ser vistos por el siguiente grupo. El procedimiento requiere disciplina diaria: al finalizar el día (o al ausentarse por tiempo prolongado), revisar escritorio, guardar todos los papeles en cajones que se cierran con llave (IT debe proporcionar armarios/cajones con cerradura), bloquear el PC con Win+L, y si el monitor es visible desde áreas de paso o ventanas, apagarlo. Para trabajo en espacios públicos (cafeterías, aeropuertos, trenes), usar filtros de privacidad 3M en pantallas de laptop—estos filtros hacen que la pantalla solo sea legible frontalmente, viéndose negra desde ángulos laterales, previniendo "shoulder surfing" (mirones por encima del hombro). Nunca dejar laptop sin supervisión en público, ni siquiera para ir al baño—empacar y llevar o pedir a compañero de confianza que vigile.


### 2bis.4.3. Pérdida o Robo de Dispositivos en Instalaciones

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Dispositivos robados desde oficinas o áreas comunes.
* **Política**: Proteger dispositivos físicamente en instalaciones.
* **Normativa**: Dispositivos con contraseña y cifrado. Laptops en cajones
  con llave o con cable de seguridad cuando no se usan.
* **Procedimiento**: Guardar laptop en cajón con llave al salir. En
  espacios abiertos, usar cable Kensington para anclar laptop a escritorio.

Note: Aunque las instalaciones tengan seguridad, los robos internos ocurren—empleados deshonestos, contratistas, visitan tes, o robos oportunistas cuando alguien deja la puerta abierta. Los laptops son especialmente vulnerables porque son portátiles, valiosos y fáciles de revender. El procedimiento establece dos niveles de protección. Primero, almacenamiento seguro: al finalizar jornada, guardar laptop en cajón o armario con llave. Segundo, anclaje físico: los laptops tienen ranura Kensington que permite conectar un cable de seguridad de acero que se ancla a un punto fijo (escritorio, pata de mesa)—esto no previene robo determinado (pueden cortar el cable con herramientas) pero previene robo oportunista. Las empresas deben proporcionar estos cables. Para dispositivos móviles (tablets, teléfonos), no dejarlos cargando desatendidos en salas de reuniones. El cifrado de disco completo (mencionado en sección hardware) es la última línea de defensa—si roban el dispositivo físico, al menos los datos están protegidos.


### 2bis.4.4. Gestión Insegura de Residuos Confidenciales

**Escenario, Política, Normativa y Procedimiento:**

* **Riesgo**: Documentos confidenciales desechados sin destrucción segura.
* **Política**: Destruir información confidencial antes de desechar.
* **Normativa**: Documentos confidenciales deben triturarse. Prohibido
  desechar en papelera común. Discos duros deben destruirse físicamente.
* **Procedimiento**: Usar trituradoras de papel (cross-cut) en cada
  planta. Para dispositivos: entregar a IT para destrucción certificada.

Note: El "dumpster diving" (bucear en basureros) es técnica real de recopilación de información—los atacantes físicamente revisan la basura de empresas buscando documentos descartados, diagramas de red, listados de empleados, org charts, credenciales anotadas, reportes financieros, contratos con proveedores, etc. Ocurre más de lo que pensáis—organizaciones han sufrido brechas simplemente porque alguien tiró a la basura documentos sin triturar. El procedimiento requiere trituradoras de papel estilo cross-cut (corte transversal, convierte papel en confeti ilegible) en cada planta, preferiblemente cerca de impresoras. Las trituradoras strip-cut (corte en tiras) son insuficientes—las tiras pueden reconstruirse. Para documentos MUY sensibles, considerar trituradoras P-4 o superiores (cortes más pequeños) según DIN 66399. Los empleados deben triturar cualquier documento confidencial antes de desecharlo, incluyendo borradores impresos, copias defectuosas, notas de reuniones, post-its con información sensible. Para medios digitales (discos duros, USBs, CDs con información), NO tirarlos a basura normal—entregar a IT que los destruirá físicamente (perforación de discos, pulverización magnética, o incineración) y proporcionará certificado de destrucción.


### 2bis.5. Acceso a Datos

**Permisos sobre información corporativa:**

* Documentos electrónicos (Word, PDF, Excel)
* Bases de datos (CRM, ERP, RRHH)
* Archivos compartidos (file shares, SharePoint)
* Aplicaciones internas con datos sensibles
* Información personal (clientes, empleados)

Note: La gestión de acceso a datos es fundamental para proteger la confidencialidad e integridad de la información. El principio rector es "mínimo privilegio"—cada persona debe tener acceso únicamente a los datos necesarios para su función, nada más. Esto minimiza el radio de impacto en caso de compromiso de una cuenta o de un empleado deshonesto (insider threat). El acceso a datos debe gestionarse mediante roles (RBAC - Role-Based Access Control) en lugar de permisos individuales ad-hoc—es mucho más escalable y auditable asignar a un empleado el rol "Ventas EMEA" que darle permisos individuales a 50 carpetas. Los accesos deben revisarse periódicamente (trimestralmente o al menos anualmente) porque las necesidades cambian: empleados cambian de departamento, proyectos finalizan, colaboradores externos terminan contratos, pero los permisos frecuentemente quedan asignados indefinidamente generando "privilege creep" (acumulación de privilegios).


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

Note: El trabajo remoto NO debe ser excusa para comprometer la seguridad—debe protegerse con el mismo rigor que el trabajo presencial, solo que requiere controles adaptados a la realidad distribuida. Las medidas enumeradas recrean efectivamente un "perímetro virtual" o arquitectura "Zero Trust" alrededor de cada trabajador remoto, compensando la pérdida del perímetro físico corporativo tradicional. La VPN obligatoria cifra todo el tráfico entre dispositivo remoto y red corporativa dentro de un túnel seguro AES-256, creando una conexión privada virtual a través de internet público—esto hace irrelevante si la red WiFi doméstica o de cafetería es insegura porque todo el tráfico viaja cifrado end-to-end. La verificación de seguridad WiFi doméstica mediante checklist ayuda a usuarios a endurecer su red local: cambiar contraseña default del router (admin/admin es común y peligroso), activar WPA3 o mínimo WPA2-Personal con contraseña fuerte, deshabilitar WPS que es vulnerable a ataques de PIN, actualizar firmware del router regularmente, cambiar SSID a algo no identificable con la dirección, ocultar SSID broadcast opcionalmente. La separación de red doméstica creando VLAN o red de invitados dedicada solo para trabajo mantiene dispositivos laborales aislados de otros dispositivos domésticos potencialmente comprometidos como IoT smart TVs cámaras consolas de juego que raramente se actualizan. Cifrado de disco completo es aún MÁS crítico en remoto donde riesgo físico de robo del laptop es significativamente mayor que en oficina controlada. Soporte remoto IT debe estar disponible vía múltiples canales chat teléfono email y herramientas de escritorio remoto para resolver problemas técnicos sin requerir presencia física.


### 5.3. BYOD (Bring Your Own Device)

**Uso de dispositivos personales:**

**Ventajas:**
* Ahorro de costes para empresa.
* Comodidad para empleado.

**Desventajas:**
* Control limitado de seguridad.
* Mezcla uso personal/profesional.
* Dificultad en borrado remoto.

Note: BYOD (Bring Your Own Device) donde empleados usan sus smartphones tablets o laptops personales para acceder a recursos corporativos es extremadamente tentador económicamente para organizaciones porque elimina CAPEX significativo de compra provisioning mantenimiento y reemplazo de hardware corporativo—puede ahorrar 500-1500€ por empleado. Los empleados también lo aprecian porque significa usar un solo dispositivo familiar para todo trabajo y personal sin cargar múltiples teléfonos. Sin embargo BYOD introduce complejidades de seguridad masivas que frecuentemente superan los beneficios económicos. La organización tiene control muy limitado sobre dispositivo que legalmente no posee—no puede forzar políticas de seguridad estrictas sin consentimiento explícito del propietario lo cual crea fricción, no puede inspeccionar completamente su estado de seguridad o contenido sin violar privacidad, no puede prevenir que instalen apps potencialmente maliciosas o juegos con permisos excesivos en su uso personal que podrían comprometer también datos corporativos. La mezcla inevitable de datos corporativos y personales fotos videos contactos en mismo dispositivo crea problemas legales de privacidad complejos—si hay investigación de incidente ¿puede la organización acceder a fotos personales del empleado? ¿Cómo se protegen datos GDPR si están mezclados con datos personales? La dificultad de ejecutar borrado remoto corporativo sin borrar también datos personales cuando empleado deja empresa o dispositivo se compromete es técnicamente compleja y legalmente problemática. Por estas razones muchas organizaciones maduras en seguridad simplemente prohíben BYOD completamente y proporcionan dispositivos corporativos dedicados donde tienen control total—más caro upfront pero más simple seguro y gestionable long-term.


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
