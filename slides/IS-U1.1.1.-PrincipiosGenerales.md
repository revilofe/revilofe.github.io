# U1.1.1 - Principios Generales

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Conceptos Básicos de Ciberseguridad


### Ciberseguridad

* Protección de ordenadores, redes y datos digitales.
* Prevención de ataques, robos y virus.
* Equivalente digital a cerraduras y alarmas.
* Ejemplo: Contraseña en tu correo electrónico.

Note: La ciberseguridad es como poner cerraduras, alarmas y cámaras en una casa digital. Su objetivo principal es proteger todo lo que hay dentro y evitar que alguien no autorizado entre, dañe o robe algo. Es un campo complejo que abarca una amplia gama de tecnologías y prácticas. Cuando configuras una contraseña en tu correo electrónico, estás usando ciberseguridad básica para proteger tu información personal. Es importante entender que la ciberseguridad es principalmente preventiva.


### Ciberdefensa

* Respuesta activa ante ataques en curso.
* Monitorización y vigilancia constante de sistemas.
* Detección de comportamientos sospechosos.
* Reacción rápida para detener amenazas.

Note: Si la ciberseguridad es poner cerraduras, la ciberdefensa es contratar un guardia de seguridad que vigila constantemente. Se enfoca en responder a ataques que ya están ocurriendo o evitar que vuelvan a suceder. Por ejemplo, si una empresa detecta un ataque en su sistema, la ciberdefensa entra en acción para detenerlo, buscar de dónde vino y mejorar la seguridad para que no vuelva a pasar. Son dos caras de la misma moneda: la ciberseguridad previene, la ciberdefensa responde.


### Sistemas de Información

* Conjunto de datos, procesos, personas y tecnología.
* Gestionan información para decisiones empresariales.
* Incluyen tanto elementos digitales como no digitales.
* Protegen confidencialidad, integridad y disponibilidad.

Note: Los sistemas de información son el conjunto completo que maneja la información en una organización. No solo son ordenadores y software, sino también las personas que los usan, los datos almacenados y los procedimientos que se siguen. Ejemplos incluyen sistemas de gestión de inventario, sistemas de nóminas o CRM. Aunque pueden existir sin elementos informáticos (archivos en papel, procesos manuales), en la actualidad es difícil imaginar esta situación. La protección debe abarcar todos estos componentes.


### Componentes del Sistema de Información

* **Datos**: Registros, información almacenada.
* **Procesos**: Procedimientos para gestionar información.
* **Personas**: Usuarios que interactúan con el sistema.
* **Tecnología**: Hardware y software de soporte.

Note: Es fundamental entender cada componente. Los datos son la información que se almacena, como registros de empleados o ventas. Los procesos determinan cómo se recolecta y usa esa información. Las personas son los usuarios finales. Y la tecnología son los sistemas informáticos que permiten gestionar todo. Proteger un sistema de información significa proteger estos cuatro elementos simultáneamente, no solo el hardware y software.


### Sistemas Informáticos

* Hardware: Ordenadores, servidores, dispositivos móviles.
* Software: Sistemas operativos, aplicaciones, programas.
* Procesan, almacenan y transmiten información.
* Ejemplo: Tu ordenador personal con Windows y Chrome.

Note: Los sistemas informáticos se refieren específicamente al hardware y software. Son la parte tecnológica de los sistemas de información. Incluyen ordenadores personales, servidores, dispositivos móviles, sistemas operativos, aplicaciones y bases de datos. Proteger los sistemas informáticos significa garantizar actualizaciones de software, mantenimiento de hardware, uso de antivirus y firewalls, y protección del acceso físico. Es como cuidar los vehículos de una flota, mientras que los sistemas de información son todo el sistema logístico que usa esos vehículos.


### Analogía: Vehículos vs Logística

* **Sistema informático**: Los vehículos (hardware/software).
* **Sistema de información**: Todo el sistema logístico.
* Logística incluye vehículos + conductores + paquetes.
* Proteger ambos niveles es esencial.

Note: Esta analogía es muy útil para entender la diferencia. Los sistemas informáticos son como los vehículos en una flota de autos: los autos, motores, llantas, la tecnología física y programas. Los sistemas de información son todo el sistema de logística que usa esos vehículos: incluyen los autos, pero también el proceso de entrega, los conductores (personas) y la información de cada paquete (datos). Proteger solo los vehículos no es suficiente si los paquetes llegan dañados o los conductores no siguen procedimientos correctos.


### Ejemplo Integrado

**Sistema informático**: Red de computadoras + servidores.
* Protección: Antimalware, actualizaciones, funcionamiento.

**Sistema de información**: Sistema de ventas completo.
* Protección: Datos clientes, reportes, confidencialidad.

Note: Veamos un ejemplo concreto para consolidar. En una empresa, el sistema informático es la red de computadoras y servidores que ejecutan programas. Su ciberseguridad implica que los servidores estén protegidos frente a malware, actualizados y funcionando. El sistema de información es el sistema que gestiona las ventas, incluyendo las bases de datos con transacciones, los procesos que generan reportes financieros y los empleados que analizan datos. Su protección va más allá: debe garantizar confidencialidad de registros, integridad de reportes y que no sean alterados sin autorización.

---

## 2. Seguridad vs Fiabilidad


### La Imposibilidad de la Seguridad Total

* La seguridad perfecta no existe.
* Siempre habrá nuevas amenazas y vulnerabilidades.
* Los sistemas son complejos y dinámicos.
* Los atacantes evolucionan constantemente.

Note: Es fundamental comprender esta verdad: la seguridad total es imposible de conseguir. Por más que una empresa implemente controles, firewalls y medidas avanzadas, siempre existe el riesgo de que algo falle. Los sistemas informáticos son complejos y se introducen constantemente nuevos componentes y actualizaciones que pueden abrir brechas. Además, los atacantes también evolucionan, encontrando nuevas formas de vulnerar los sistemas. Es como una casa: aunque pongas puertas blindadas y alarmas, siempre puede haber alguien que descubra una nueva forma de entrar.


### El Enfoque en la Fiabilidad

* Sistemas confiables y resilientes.
* Capaces de funcionar ante fallos o ataques.
* Recuperación rápida tras incidentes.
* Minimización de daños y consecuencias.

Note: Dado que la seguridad perfecta no es posible, se pone mayor énfasis en la fiabilidad. En lugar de intentar una protección 100% segura (que sería imposible y extremadamente costosa), el objetivo es hacer que los sistemas sean confiables. Esto significa que si ocurre un incidente, los sistemas puedan seguir funcionando, recuperarse rápidamente y los daños se minimicen. La fiabilidad no implica invulnerabilidad, sino capacidad de mantener las operaciones incluso en situaciones adversas.


### Conceptos Clave de Fiabilidad I

* **Alta disponibilidad**: Sistemas disponibles ante fallos.
* Recuperación automática y rápida.
* Hay interrupción breve, el sistema vuelve solo.
* Ejemplo: Sistema con servidor de respaldo automático.

Note: La alta disponibilidad asegura que los sistemas estén operativos incluso cuando ocurre un fallo. Si un componente falla, otro toma su lugar inmediatamente. Es como tener dos generadores eléctricos: si uno falla, el otro arranca automáticamente. Puede haber una interrupción muy breve (un blip), pero el sistema se recupera solo sin intervención humana. Esto es crucial para servicios que no pueden detenerse, como hospitales o sistemas de pago.


### Conceptos Clave de Fiabilidad II

* **Resiliencia**: Recuperación después de un incidente.
* Hay parada, pero se recupera con DR/backups.
* Capacidad de volver a estado operativo.
* Ejemplo: Restaurar datos desde copias de seguridad.

Note: La resiliencia es la capacidad del sistema de recuperarse después de un incidente grave. A diferencia de la alta disponibilidad, aquí sí hay una parada significativa, pero el sistema puede recuperarse usando planes de recuperación ante desastres (DR) o copias de seguridad (backups). Por ejemplo, si un ransomware cifra todos los datos, un sistema resiliente tiene backups que permiten restaurar la información. La recuperación puede llevar horas o días, pero es posible. Es como un edificio diseñado para resistir terremotos: puede dañarse, pero no colapsa.


### Conceptos Clave de Fiabilidad III

* **Tolerancia a fallos**: Funcionamiento continuo ante fallos.
* No hay corte ante componentes conocidos que fallen.
* Sistemas redundantes y componentes duplicados.
* Ejemplo: RAID en discos duros, fuentes redundantes.

Note: La tolerancia a fallos es el nivel más alto de fiabilidad. Los sistemas están diseñados de manera que puedan seguir funcionando incluso cuando un componente falle, sin que haya corte del servicio. Esto se logra mediante redundancia: tener componentes duplicados. Por ejemplo, un sistema RAID donde varios discos almacenan los mismos datos, si uno falla, los otros continúan. O fuentes de alimentación redundantes en un servidor. No hay interrupción del servicio porque el sistema tolera el fallo de componentes conocidos.


### Por Qué Enfocarse en Fiabilidad

* **Adaptación al cambio**: Operación ante fallos o ataques.
* **Minimización del impacto**: Recuperación rápida.
* **Protección ante lo inesperado**: Nadie prevé todo.
* **Costos equilibrados**: Inversión más razonable.

Note: La fiabilidad es más realista y efectiva que buscar seguridad total. Permite que los sistemas se adapten a nuevos problemas sin colapsar. Si ocurre una vulneración, la organización no queda paralizada porque los sistemas pueden recuperarse rápidamente, minimizando pérdidas y tiempo de inactividad. Nadie puede prever todas las amenazas futuras, pero un sistema fiable puede seguir funcionando de manera predecible. Además, intentar seguridad perfecta sería extremadamente costoso, mientras que mejorar la fiabilidad es una inversión más equilibrada con mayores beneficios en continuidad operativa.


### Ejemplo Práctico: Empresa con Fiabilidad

* **Escenario**: Pequeña empresa con datos importantes.
* Respaldo diario de datos (recuperación ante pérdida).
* Redundancia de sistemas (servidor de respaldo).
* Monitoreo constante (detección rápida).

Note: Imaginad una pequeña empresa que almacena datos importantes. En lugar de invertir fortunas en seguridad "perfecta" (gasto altísimo en tecnologías punta, personal especializado y auditorías constantes), decide focalizarse en fiabilidad: hace respaldos diarios (si borran datos, se restauran rápidamente), tiene redundancia de sistemas (si un servidor falla, otro toma su lugar), y monitorea constantemente (detecta ataques rápidamente antes que el daño sea irreparable). Este enfoque permite que, aunque haya incidentes de seguridad (inevitables a largo plazo), las operaciones continúen.


### Conclusión: Continuidad del Negocio

* La clave es asegurar la continuidad, no la perfección.
* Enfoque realista y efectivo.
* Equilibrio entre seguridad y operatividad.
* Preparación para lo inevitable.

Note: La frase clave que debéis recordar es: la seguridad total es imposible, por tanto hablamos de fiabilidad. En el mundo real, lo importante no es tener sistemas 100% seguros (imposible), sino sistemas que puedan continuar operando y recuperarse rápidamente cuando algo inevitablemente salga mal. Este enfoque permite a las organizaciones mantener sus operaciones, proteger lo esencial y minimizar el impacto de los incidentes. Es un equilibrio entre protección, costo y realismo.

---

## 3. Triada CIA


### La Triada CIA

* **C**onfidentialidad (Confidencialidad)
* **I**ntegridad (Integridad)
* **A**vailability (Disponibilidad)

Pilares fundamentales de toda estrategia de ciberseguridad.

Note: La Triada CIA es el fundamento de cualquier estrategia de seguridad de la información. Estos tres principios son universales y aplicables a cualquier organización, independientemente de su tamaño o sector. Si alguno de estos tres pilares falla, la seguridad del sistema está comprometida. Vamos a explorar cada uno en detalle para comprender cómo se aplican en situaciones reales.


### Confidencialidad

* Solo personas autorizadas acceden a la información.
* Protección de datos sensibles.
* Control mediante cifrado y contraseñas.
* Ejemplo: Solo tú puedes leer tu diario con candado.

Note: La confidencialidad asegura que solo las personas o sistemas autorizados puedan acceder a información sensible. Esto protege la información de accesos no autorizados. Es como tener un diario privado con candado donde solo tú tienes la llave. En el mundo digital, se logra mediante cifrado de datos (cuando envías un mensaje cifrado, solo el receptor autorizado puede leerlo), contraseñas seguras (solo quien conoce la contraseña accede), y autenticación multifactor (requiere más de un método de verificación).


### Integridad

* Información exacta y completa.
* Sin modificaciones no autorizadas.
* Detección de alteraciones.
* Ejemplo: Carta sellada que llega intacta.

Note: La integridad garantiza que los datos no sean alterados o modificados de manera no autorizada o accidental. Asegura que la información se mantenga exacta y completa desde su creación hasta su destino. Es como enviar una carta sellada: si llega con el sello roto, sabes que alguien la abrió o modificó. Se implementa mediante firmas digitales (aseguran que documentos no fueron alterados), controles de acceso (solo autorizados pueden modificar) y hashing (algoritmos que detectan cualquier cambio en un archivo).


### Disponibilidad

* Información accesible cuando se necesita.
* Sistemas operativos sin interrupciones.
* Garantía de acceso para usuarios autorizados.
* Ejemplo: Cajero automático funcionando cuando llegas.

Note: La disponibilidad asegura que los sistemas y datos estén accesibles y operativos cuando los usuarios autorizados los necesiten. De nada sirve tener datos confidenciales e íntegros si no están disponibles cuando se requieren. Es como un cajero automático: debe estar funcionando cuando llegues. Se logra mediante redundancia de sistemas (servidores duplicados que reemplazan automáticamente al que falla), planes de recuperación ante desastres (restauración rápida), y mantenimiento regular (actualizaciones para prevenir caídas).


### Ejemplo Integrado: Empresa Financiera I

**Escenario**: Trabajas en banco con acceso a cuentas de clientes.

* **Confidencialidad**: Solo tú, empleado autorizado, accedes.
* Cifrado y contraseñas seguras protegen los datos.

Note: Vamos a ver un ejemplo completo que integra los tres principios. Imagina que trabajas en una empresa financiera con acceso a información sobre cuentas de clientes. Primero, la confidencialidad: solo tú, como empleado autorizado, puedes acceder a esos datos financieros. Para protegerlos, los sistemas utilizan cifrado fuerte y contraseñas seguras. Esto previene que personas no autorizadas, incluso dentro de la empresa, puedan ver información para la que no tienen permiso.


### Ejemplo Integrado: Empresa Financiera II

**Escenario**: Trabajas en banco con acceso a cuentas de clientes.

* **Integridad**: Registros no pueden alterarse sin permiso.
* Sistema detecta cambios y activa alertas.
* Copias de seguridad para restaurar datos originales.

Note: Continuando con el ejemplo, la integridad es crucial: los registros de las cuentas no deben ser alterados sin permiso. Si alguien intenta modificar los datos sin autorización, el sistema detectará el cambio y activará alertas para corregirlo inmediatamente. Además, se mantienen copias de seguridad para asegurar que los datos originales pueden ser restaurados si hay algún problema. Imagina si alguien pudiera cambiar el saldo de una cuenta sin dejar rastro: sería catastrófico para el banco y los clientes.


### Ejemplo Integrado: Empresa Financiera III

**Escenario**: Trabajas en banco con acceso a cuentas de clientes.

* **Disponibilidad**: Clientes acceden a su cuenta online.
* Sistema activo 24/7 para realizar transacciones.
* Sin interrupciones en el servicio bancario.

Note: Finalmente, la disponibilidad: cuando los clientes intenten acceder a su cuenta bancaria en línea, el sistema debe estar activo y funcional, permitiéndoles realizar transacciones en cualquier momento sin interrupciones. Un banco no puede permitirse estar fuera de servicio porque sus clientes necesitan acceso constante a su dinero. Por eso tienen sistemas redundantes, generadores de respaldo y planes de continuidad. Si falla un servidor, otro toma su lugar instantáneamente.

---

## 4. Principios Complementarios


### Fiabilidad (Reliability)

* Sistema funciona correctamente y predeciblemente.
* Sin errores o fallos inesperados.
* Opera según lo esperado bajo condiciones normales.
* Ejemplo: Transferencia bancaria sin fallos.

Note: La fiabilidad, que ya hemos visto antes en otro contexto, también es un principio de seguridad complementario a CIA. Garantiza que el sistema funcione de manera correcta y predecible, de acuerdo con lo esperado, sin errores o fallos inesperados. Por ejemplo, cuando haces una transferencia bancaria, esperas que el sistema funcione correctamente y que el dinero llegue sin errores. Si el sistema tiene problemas y las transacciones fallan o los datos se pierden, no sería confiable. En ciberseguridad, un sistema confiable evita interrupciones inesperadas.


### Autenticidad (Authenticity)

* Verificación de identidad de usuarios y datos.
* Información proviene de fuente confiable.
* No ha sido manipulada durante transmisión.
* Ejemplo: Firma digital en un documento.

Note: La autenticidad asegura que la información o el usuario es quien dice ser, y que la información no ha sido manipulada. Tanto los datos como las identidades deben ser verificables. Cuando accedes a tu cuenta de correo con usuario y contraseña, el sistema te autentica, asegurando que eres el verdadero dueño. Si recibes un mensaje firmado digitalmente, la firma asegura la autenticidad del remitente: puedes estar seguro de que el mensaje viene de quien dice ser y no ha sido alterado.


### No Repudio (Non-repudiation)

* Ninguna parte puede negar una acción realizada.
* Evidencia irrefutable de transacciones.
* Garantía de responsabilidad.
* Ejemplo: Firma digital en contrato electrónico.

Note: El no repudio significa que ninguna de las partes involucradas en una comunicación o transacción puede negar que esa acción ocurrió. Se utiliza para garantizar la responsabilidad. Por ejemplo, si firmas un contrato digitalmente, el sistema garantiza que no puedas negar haberlo firmado en el futuro. La firma digital proporciona evidencia verificable. En transacciones bancarias online, asegura que si transfieres dinero, no puedas negar haberlo hecho, y el banco puede probarlo. Es esencial para comercio electrónico y contratos digitales.


### Integración de Todos los Principios

**Compra online**:

1. Confidencialidad: Información de pago cifrada.
2. Integridad: Pedido no modificado durante proceso.
3. Disponibilidad: Sistema de pago siempre accesible.
4. Fiabilidad: Transacción se realiza correctamente.
5. Autenticidad: Verificación de tienda y comprador.
6. No repudio: Registro irrefutable de la compra.

Note: Veamos cómo todos estos principios trabajan juntos en una compra online. La confidencialidad protege tu número de tarjeta mediante cifrado. La integridad asegura que tu pedido no sea modificado. La disponibilidad garantiza que puedas comprar cuando quieras. La fiabilidad asegura que la transacción funcione sin problemas. La autenticidad verifica que compras en la tienda legítima y que el pago proviene de ti. El no repudio crea un registro que ninguna parte puede negar. Todos estos principios se combinan para crear una experiencia de compra segura.

---

## 5. Decálogo de Ciberseguridad


### 1. Cultura de Ciberseguridad

* Educación y formación de empleados.
* Concienciación sobre amenazas.
* Prevención de errores humanos.
* Ejemplo: Identificar correos de phishing.

Note: La cultura de ciberseguridad es vital. No solo se trata de instalar herramientas, sino también de educar a los empleados. Este principio refuerza todos los aspectos de la triada CIA: empleados bien capacitados son menos propensos a cometer errores que comprometan la seguridad. Por ejemplo, si un empleado recibe un correo sospechoso, debe saber que no debe abrir enlaces ni descargar archivos hasta confirmar que es legítimo. La formación es clave para que todos en la organización contribuyan a la seguridad.


### 2. No Abrir Enlaces Sospechosos

* Nunca abrir enlaces de correos dudosos.
* No descargar archivos no verificados.
* Verificar remitente antes de actuar.
* Previene phishing y malware.

Note: Este es uno de los vectores de ataque más comunes. Nunca debemos abrir enlaces ni descargar archivos adjuntos de correos que parezcan sospechosos. Este tipo de correos puede contener malware o llevarnos a sitios fraudulentos. Refuerza confidencialidad (protege información sensible) e integridad (impide malware que modifique datos). Si recibes un correo raro, aunque parezca de un amigo, es mejor verificar antes de hacer clic. Los ciberataques como phishing suelen empezar con un correo aparentemente inocente.


### 3. Usar Software de Seguridad

* Antivirus y antimalware actualizados.
* Cortafuegos (firewalls) activos.
* Herramientas de borrado seguro.
* Protección en múltiples capas.

Note: Siempre usar software de seguridad como antivirus, cortafuegos y herramientas antimalware. Estas herramientas detectan y bloquean amenazas antes de que lleguen a nuestros sistemas. Apoya los tres principios CIA: el antivirus bloquea accesos no autorizados (confidencialidad), evita que malware modifique archivos (integridad), y mantiene sistemas libres de amenazas asegurando disponibilidad. Tener un antivirus actualizado protege de virus conocidos, y un cortafuegos limita acceso no autorizado a tu red.


### 4. Limitar Superficie de Exposición

* Reducir servicios expuestos al mínimo necesario.
* Desactivar servicios innecesarios.
* Menos "puertas" para atacantes.
* Ejemplo: Cerrar puertos no utilizados.

Note: No es suficiente solo implementar medidas de seguridad, también debemos reducir la cantidad de servicios expuestos al mínimo necesario. Cuantos más servicios tengamos abiertos en nuestra red, más oportunidades tienen los atacantes de encontrar una brecha. Refuerza confidencialidad (minimiza riesgo de acceso no autorizado) y disponibilidad (reduce ataques que puedan comprometer operatividad). Si tienes un servidor que ofrece varios servicios, desactiva aquellos que no uses. Esto reduce el número de "puertas" que los atacantes pueden intentar abrir.


### 5. Cifrar Información Sensible

* Toda información confidencial debe estar cifrada.
* Protección incluso si acceden a los datos.
* Sin clave correcta, datos ilegibles.
* Ejemplo: Cifrado de datos personales y financieros.

Note: Toda la información sensible o confidencial debe estar cifrada. Esto significa que, incluso si alguien accede a los datos sin permiso, no podrá leerlos sin la clave para descifrarlos. Está directamente relacionado con confidencialidad: el cifrado asegura que, aunque alguien acceda a los datos, no podrá entenderlos sin la clave correcta. Cuando enviamos datos personales o financieros por Internet, deben estar cifrados para que, si son interceptados, no puedan ser leídos. El cifrado es esencial para proteger la privacidad.


### 6. Borrado Seguro de Información

* Eliminar datos completamente cuando no se necesitan.
* Borrado simple puede dejar rastros recuperables.
* Usar herramientas de borrado seguro.
* Ejemplo: Sobrescribir datos antes de vender equipo.

Note: Cuando ya no necesitas un archivo o vas a deshacerte de un dispositivo, debes asegurarte de que los datos se eliminen completamente. Un simple "borrado" puede dejar rastros que un atacante podría recuperar. Refuerza confidencialidad (evita que datos sensibles sean recuperados) e integridad (garantiza que datos eliminados no puedan ser restaurados indebidamente). Antes de vender o desechar un ordenador o teléfono, usa una herramienta de borrado seguro que sobrescriba los datos varias veces, haciéndolos irrecuperables.


### 7. Copias de Seguridad Periódicas

* Esenciales contra fallos y ataques (ransomware).
* Respaldos frecuentes y seguros.
* No respaldar malware accidentalmente.
* Ejemplo: Backup diario de bases de datos.

Note: Las copias de seguridad son esenciales para proteger datos contra fallos o ataques como ransomware. Las copias deben ser frecuentes y seguras, y es importante no respaldar malware accidentalmente. Se relaciona con disponibilidad (permite recuperación rápida) e integridad (restaura información exacta). Imagina que tu empresa es víctima de un ataque que borra o cifra todos los archivos. Sin copias de seguridad, podrías perderlo todo. Con una copia reciente, recuperas los datos rápidamente y minimizas el impacto.


### 8. Mantener Sistemas Actualizados

* Sistema operativo y aplicaciones al día.
* Parches de seguridad corrigen vulnerabilidades.
* Actualizaciones cierran puertas a atacantes.
* Ejemplo: Windows Update, actualizaciones de apps.

Note: Mantener el sistema operativo y aplicaciones actualizadas es crucial para evitar vulnerabilidades. Las actualizaciones incluyen parches de seguridad que corrigen errores que los atacantes podrían explotar. Apoya los tres principios CIA: cierra vulnerabilidades para acceso no autorizado (confidencialidad), evita que malware dañe datos (integridad), y previene compromisos que interrumpan servicio (disponibilidad). Si usas una versión desactualizada, los hackers podrían aprovechar una vulnerabilidad conocida. Al actualizar, cierras esa puerta y proteges tu sistema.


### 9. Revisar Configuración de Seguridad

* Revisión y ajuste regular de configuraciones.
* Verificar permisos y opciones de seguridad.
* Alineación con mejores prácticas.
* Ejemplo: Revisar permisos de aplicaciones.

Note: Es importante revisar y ajustar regularmente la configuración de seguridad de sistemas y aplicaciones. Esto incluye revisar permisos y opciones de seguridad para asegurar que están configuradas correctamente según mejores prácticas. Apoya confidencialidad (permisos correctos evitan accesos no autorizados), integridad (configuración adecuada previene manipulaciones) y disponibilidad (configuración actualizada evita vulnerabilidades que causen interrupciones). Revisa permisos de aplicaciones: una app que no necesita acceder a tu ubicación no debería tener ese permiso.

---

## 6. Activos de Información


### ¿Qué es un Activo?

* Recurso o bien valioso para la organización.
* Puede ser tangible (equipos) o intangible (datos).
* Su protección es objetivo de ciberseguridad.
* Ejemplo: Datos financieros de clientes.

Note: Antes de hablar de amenazas y riesgos, debemos entender qué son los activos. Un activo es cualquier recurso o bien que tiene valor para la empresa. En ciberseguridad, se refiere a cualquier cosa que pueda afectar la seguridad o funcionamiento de los sistemas si se viera comprometido. Los activos pueden ser tangibles como equipos o edificios, o intangibles como datos o software. Su protección es el objetivo principal de la ciberseguridad. Por ejemplo, en una empresa que gestiona datos financieros, los activos más importantes serían esos datos, las aplicaciones que los gestionan y los servidores donde se almacenan.


### Tipos de Activos I

* **Datos**: Información en cualquier formato.
* Bases de datos, documentos, contratos, informes.
* Su confidencialidad e integridad son vitales.
* Ejemplo: Base de datos de clientes.

Note: Los datos son todos los datos e información que maneja la empresa en cualquier formato: digital, físico, en la nube, etc. Pueden ser personales, financieros, de clientes, operacionales y más. Por ejemplo, bases de datos de clientes o ventas, documentación importante como contratos, manuales, normativas o informes. La confidencialidad e integridad de los datos es vital, ya que su pérdida o alteración puede tener consecuencias legales, financieras y de reputación para la empresa. Proteger los datos es uno de los pilares fundamentales de la ciberseguridad.


### Tipos de Activos II

* **Aplicaciones**: Programas y software empresarial.
* Sistemas operativos, ERP, CRM, aplicaciones custom.
* Su disponibilidad y seguridad son clave.
* Ejemplo: Sistema de gestión de recursos humanos.

Note: Las aplicaciones son los programas y software que utiliza la organización para gestionar y operar su negocio. Incluyen tanto aplicaciones comerciales como sistemas personalizados. Por ejemplo, sistemas SCADA (usados en procesos industriales), software operativo como sistemas operativos, firmware, aplicaciones de gestión de usuarios o recursos como ERP y CRM. La disponibilidad y seguridad de las aplicaciones son clave para garantizar que los sistemas y procesos funcionen sin interrupciones y que los datos se manejen de manera segura.


### Tipos de Activos III

* **Hardware industrial**: Equipos físicos críticos.
* PLC, servidores, terminales, dispositivos móviles.
* Esenciales para operaciones diarias.
* Ejemplo: Controladores lógicos programables en fábrica.

Note: El hardware industrial se refiere a los equipos físicos necesarios para el funcionamiento de la empresa, especialmente en industrias que dependen de tecnología avanzada. Por ejemplo, PLC (Controladores Lógicos Programables) que automatizan procesos industriales, servidores y terminales remotas en fábricas, dispositivos móviles usados para gestionar procesos. El hardware es crítico para las operaciones diarias, y si falla, puede causar pérdidas operativas significativas o incluso riesgos de seguridad.


### Tipos de Activos IV

* **Red**: Dispositivos de conectividad.
* Routers, switches, firewalls, pasarelas.
* Permiten comunicación entre sistemas.
* Ejemplo: Infraestructura de red corporativa.

Note: La red son los dispositivos y equipos que permiten la conectividad y comunicación entre los sistemas, usuarios y procesos. Por ejemplo, routers, switches y firewalls que mantienen la red segura y operativa, pasarelas que permiten la conexión entre diferentes sistemas. La disponibilidad y seguridad de las redes son fundamentales para que los sistemas de la empresa se mantengan conectados y puedan compartir información de manera eficiente y segura. Sin una red funcionando, la empresa queda aislada.


### Tipos de Activos V

* **Tecnología**: Equipos tecnológicos generales.
* Servidores, teléfonos, impresoras.
* Vitales para operatividad y comunicación.
* Ejemplo: Servidores de aplicaciones empresariales.

Note: La tecnología son otros equipos tecnológicos necesarios para el funcionamiento empresarial. Son más generales que el hardware industrial, pero siguen siendo críticos para la gestión diaria. Por ejemplo, servidores que alojan los sistemas y aplicaciones empresariales, teléfonos, impresoras y routers. La disponibilidad de estos equipos es vital para la operatividad y la comunicación interna y externa de la empresa. Sin estos activos tecnológicos, la empresa no puede funcionar correctamente.


### Tipos de Activos VI

* **Personal**: Empleados y colaboradores.
* Plantilla propia y subcontratados.
* Su concienciación es fundamental.
* Ejemplo: Equipo de IT y usuarios finales.

Note: El personal es un activo clave, ya que son quienes manejan los sistemas y toman decisiones sobre la información y los procesos de la empresa. Incluye la plantilla propia de la organización y personal subcontratado o de mantenimiento. La concienciación y capacitación en ciberseguridad del personal son fundamentales para evitar errores humanos, que muchas veces son la principal causa de vulnerabilidades. Un empleado bien formado es una de las mejores defensas contra ataques.


### Tipos de Activos VII

* **Instalaciones**: Lugares físicos.
* Edificios, oficinas, centros de datos.
* Protección física esencial.
* Ejemplo: Sala de servidores con control de acceso.

Note: Las instalaciones son los lugares físicos donde la organización aloja sus sistemas y operaciones. Por ejemplo, edificios, oficinas, instalaciones eléctricas, centros de datos y servidores físicos. Las instalaciones deben estar protegidas físicamente para evitar acceso no autorizado o daños físicos, como incendios o robos. Un intruso que accede físicamente a un centro de datos puede causar daños masivos. La seguridad física es tan importante como la seguridad digital.


### Tipos de Activos VIII

* **Equipamiento auxiliar**: Equipos de soporte.
* SAI, climatización, destructoras de datos.
* Mantienen funcionamiento de sistemas críticos.
* Ejemplo: Sistema de alimentación ininterrumpida.

Note: El equipamiento auxiliar son los equipos de soporte que ayudan a mantener el funcionamiento de los sistemas de información, aunque no son parte del núcleo principal de operación. Por ejemplo, equipos de destrucción de datos, climatización o SAI (Sistemas de Alimentación Ininterrumpida) que mantienen los servidores funcionando incluso en caso de fallos eléctricos. Aseguran que los sistemas críticos sigan operando bajo condiciones adversas o en situaciones de emergencia. Sin SAI, un corte de luz podría apagar todos los servidores.


### Clasificación y Priorización

* No todos los activos son iguales en valor.
* Priorizar protección según criticidad.
* Facilita gestión de riesgos y respuesta.
* Ejemplo: Datos de clientes (Crítico) vs impresora (Bajo).

Note: Clasificar los activos es fundamental en la gestión de ciberseguridad, ya que permite identificar y priorizar los activos más críticos. No todos los activos son iguales: algunos, como los datos confidenciales de clientes o los servidores críticos, requieren más protección que otros. Al clasificar activos, podemos priorizar la protección (enfocarnos en lo más importante), gestionar los riesgos (entender qué amenazas podrían afectarlos) y facilitar la respuesta (saber qué activos se comprometieron para actuar rápidamente). Esta clasificación es la base para todo el proceso de gestión de riesgos.

---

## 7. Vulnerabilidades


### ¿Qué es una Vulnerabilidad?

* Debilidad en sistemas de información.
* Permite comprometer confidencialidad, integridad o disponibilidad.
* Condición que hace susceptible a amenazas.
* Ejemplo: Software sin actualizar con fallos conocidos.

Note: Una vulnerabilidad es una debilidad, debido a fallos técnicos, errores humanos o deficiencias en los procedimientos, de los sistemas de información que pone en riesgo la seguridad. Puede permitir que un atacante comprometa la integridad, disponibilidad o confidencialidad de la información. También puede afectar a la autenticidad, fiabilidad y no repudio. Las vulnerabilidades son las condiciones propias de los activos que los hacen susceptibles a las amenazas. Es como una puerta sin cerradura en tu casa: un punto débil que podría ser aprovechado por un ladrón para entrar.


### Características de las Vulnerabilidades

* **Propias del sistema**: Fallos en diseño o implementación.
* **De configuración**: Errores en configuración.
* **Humanas**: Falta de formación, malas prácticas.
* **Físicas**: Deficiencias en protección física.

Note: Las vulnerabilidades pueden clasificarse según su origen. Pueden ser propias del sistema (fallos en el diseño o implementación del software o hardware), de configuración (errores al configurar sistemas o aplicaciones), humanas (falta de formación, errores de usuarios o malas prácticas) o físicas (deficiencias en la protección física de los equipos o instalaciones). Identificar el tipo de vulnerabilidad es el primer paso para corregirla. Por ejemplo, una contraseña débil es una vulnerabilidad humana, mientras que un bug en el código es una vulnerabilidad del sistema.


### Ejemplo: Software Desactualizado

* **Activo afectado**: Servidor web.
* **Vulnerabilidad**: Software sin parches de seguridad.
* **Principio comprometido**: Confidencialidad, Integridad.
* Permite acceso no autorizado al sistema.

Note: Imaginad un servidor web con una versión antigua de software que tiene un fallo de seguridad conocido. Esta vulnerabilidad podría permitir que un atacante acceda al sistema sin autorización. El activo afectado es el servidor web (Hardware industrial/Tecnología). La vulnerabilidad es el software no actualizado con parches de seguridad. Los principios comprometidos son Confidencialidad (pueden ver datos privados) e Integridad (pueden modificar información). Esta es una de las vulnerabilidades más comunes y fáciles de corregir, simplemente actualizando el software.


### Ejemplo: Contraseñas Débiles

* **Activo afectado**: Datos empresariales, sistemas.
* **Vulnerabilidad**: Políticas de contraseñas débiles.
* **Principio comprometido**: Confidencialidad, Autenticidad.
* Facilita acceso mediante fuerza bruta.

Note: En una empresa, varios empleados utilizan contraseñas simples como "123456" o "password" para acceder a sistemas críticos. Los activos afectados son los datos de la empresa y sistemas de autenticación (Aplicaciones). La vulnerabilidad es la política de contraseñas débiles y falta de formación del personal. Los principios comprometidos son Confidencialidad (fácil acceso a datos) y Autenticidad (suplantación de identidad). Esta vulnerabilidad es muy común y se soluciona con políticas de contraseñas fuertes y formación adecuada.


### Ejemplo: Falta de Cifrado

* **Activo afectado**: Datos de clientes.
* **Vulnerabilidad**: Ausencia de cifrado en comunicaciones.
* **Principio comprometido**: Confidencialidad.
* Datos sensibles expuestos en tránsito.

Note: Una aplicación móvil envía datos sensibles de clientes sin cifrar a través de Internet. El activo afectado son los datos de clientes (Datos). La vulnerabilidad es la ausencia de cifrado en las comunicaciones. El principio comprometido es la Confidencialidad. Cualquiera que intercepte las comunicaciones (man-in-the-middle) puede leer los datos en texto claro. Esta vulnerabilidad es crítica cuando se manejan datos personales o financieros. La solución es implementar cifrado TLS/SSL en todas las comunicaciones.


### Ejemplo: Acceso Físico No Controlado

* **Activo afectado**: Servidores, sistemas.
* **Vulnerabilidad**: Falta de controles físicos.
* **Principio comprometido**: Disponibilidad, Integridad.
* Cualquiera puede acceder a equipos críticos.

Note: Un centro de datos no tiene control de acceso adecuado y cualquier empleado puede entrar sin identificarse. Los activos afectados son servidores y sistemas de almacenamiento (Instalaciones, Tecnología). La vulnerabilidad es la falta de controles de acceso físico. Los principios comprometidos son Disponibilidad (pueden apagar equipos) e Integridad (pueden manipular hardware). Alguien malintencionado podría desconectar servidores, robar discos duros o instalar dispositivos maliciosos. La seguridad física es fundamental y a menudo olvidada.


### Gestión de Vulnerabilidades

1. **Identificar** mediante auditorías y análisis.
2. **Evaluar** gravedad e impacto potencial.
3. **Priorizar** según el riesgo.
4. **Implementar** medidas correctivas.
5. **Verificar** efectividad de medidas.
6. **Monitorizar** continuamente.

Note: Si existe una vulnerabilidad, siempre existirá alguien que intentará explotarla. Por eso es necesario seguir un proceso sistemático de gestión. Primero identificar las vulnerabilidades mediante auditorías y análisis de seguridad. Luego evaluar su gravedad e impacto potencial. Después priorizar su corrección según el riesgo que representen. Implementar medidas correctivas como parches, actualizaciones o configuraciones. Verificar que las medidas son efectivas. Y finalmente monitorizar continuamente para detectar nuevas vulnerabilidades. Es un ciclo continuo, no una tarea única.


### CVE - Common Vulnerabilities and Exposures

* Sistema de identificación de vulnerabilidades conocidas.
* Cada vulnerabilidad tiene CVE-ID único.
* Base de datos pública para consulta.
* Ejemplo: CVE-2024-XXXX

Note: El sistema CVE (Common Vulnerabilities and Exposures) es una lista estándar de vulnerabilidades conocidas. Cada vulnerabilidad registrada recibe un número único llamado CVE-ID (por ejemplo, CVE-2024-XXXX) que la identifica a nivel global. Es una base de datos pública que permite a usuarios y administradores estar al tanto de problemas que pueden afectar sus sistemas y cómo mitigarlos. Es un lenguaje común en ciberseguridad: todos los expertos del mundo pueden referirse a una vulnerabilidad específica con el mismo número.


### Contenido de una Entrada CVE

* Número de identificación (CVE-ID).
* Descripción breve de la vulnerabilidad.
* Versiones de software/hardware afectadas.
* Posible solución o recomendaciones.
* Referencias adicionales y enlaces.

Note: Cada entrada CVE incluye información valiosa. Primero, un número de identificación único (CVE-ID). Luego, una descripción breve de qué es la vulnerabilidad y cómo afecta a los sistemas. También especifica qué versiones de software o hardware están afectadas. Si existe, incluye una posible solución como un parche o actualización, o recomendaciones para mitigar el riesgo. Finalmente, proporciona referencias adicionales como publicaciones o foros con más información. Todo esto permite a los administradores entender rápidamente el problema y actuar.


### Importancia del Sistema CVE

* Mantiene informados a profesionales y empresas.
* Lenguaje común en ciberseguridad global.
* Permite priorizar qué vulnerabilidades corregir.
* Consultar: Incibe-Cert, CCN-Cert.

Note: El sistema CVE es importante por varias razones. Permite que profesionales de ciberseguridad, administradores y empresas se mantengan informados sobre vulnerabilidades activas y tomen medidas necesarias para reducir riesgos. Es un lenguaje común: todos pueden referirse a una vulnerabilidad específica con el mismo número. Las organizaciones pueden priorizar qué vulnerabilidades corregir primero, basándose en su gravedad. En España, podemos consultar vulnerabilidades en Incibe-Cert y CCN-Cert, que publican avisos sobre vulnerabilidades relevantes y recomendaciones de seguridad.

---

## 8. Amenazas


### ¿Qué es una Amenaza?

* Acción que aprovecha una vulnerabilidad.
* Potencial efecto negativo sobre activos.
* Puede ser interna o externa.
* Ejemplo: Ataque de ransomware, empleado descontento.

Note: Una amenaza es toda acción que aprovecha una vulnerabilidad para atentar contra la seguridad de un sistema de información. Es decir, que podría tener un potencial efecto negativo sobre algún elemento de nuestros sistemas. Desde el punto de vista de una organización pueden ser tanto internas como externas. Las internas provienen de dentro (empleados, contratistas), mientras que las externas vienen de fuera (hackers, competidores). Las amenazas atentan contra la seguridad, por tanto, se incumplirán los principios generales: Confidencialidad, Integridad, Disponibilidad, Autenticidad, Fiabilidad y No repudio.


### Amenazas Lógicas I: Malware

* Programas maliciosos para dañar sistemas.
* **Virus**: Se replican y propagan dañando archivos.
* **Gusanos**: Se propagan por redes sin interacción.
* **Troyanos**: Aparentan ser inofensivos, toman control.

Note: Las amenazas lógicas están relacionadas con software y procesos digitales. El malware son programas maliciosos creados para dañar sistemas, robar información o causar mal funcionamiento. Los virus se replican y propagan entre archivos y sistemas causando daños. Los gusanos son similares pero se propagan por redes sin necesidad de interactuar con archivos. Los troyanos parecen inofensivos pero una vez dentro permiten a atacantes tomar el control o robar datos. Por ejemplo, un virus que infecta un sistema y corrompe archivos, o un gusano que se propaga consumiendo recursos hasta colapsar servidores.


### Amenazas Lógicas II: Más Tipos de Malware

* **Ransomware**: Cifra datos y exige rescate.
* **Spyware**: Espía actividades y roba datos.
* **Backdoors**: Puertas traseras para acceso oculto.
* **Keyloggers**: Registran pulsaciones de teclado.

Note: Continuando con tipos de malware, el ransomware cifra los archivos de la víctima y exige pago para descifrarlos, siendo uno de los ataques más destructivos. El spyware espía las actividades del usuario robando datos sensibles sin que lo sepa. Los backdoors son puertas traseras que permiten acceso al sistema sin conocimiento del usuario. Los keyloggers registran todas las pulsaciones del teclado para capturar contraseñas y datos sensibles. Estos tipos de malware son cada vez más sofisticados y representan amenazas constantes.


### Amenazas Lógicas III: Otros Tipos

* **Ingeniería social**: Engañar personas para revelar datos.
* **Phishing**: Correos falsos para robar credenciales.
* **DoS/DDoS**: Sobrecargar sistemas para colapsar.
* Ejemplo: Correo de banco falso pidiendo contraseña.

Note: La ingeniería social son técnicas para engañar a personas y hacer que revelen información confidencial como contraseñas. No atacan sistemas directamente, sino a las personas. El phishing es el ejemplo más común: correos electrónicos que parecen venir del banco pidiendo ingresar usuario y contraseña. Los ataques de denegación de servicio (DoS/DDoS) buscan sobrecargar un sistema con muchas solicitudes simultáneas para que los servicios queden inaccesibles. Por ejemplo, un ataque DDoS en un servidor web puede hacer que una tienda online esté fuera de servicio durante horas causando pérdida de ventas.


### Amenazas Físicas I

* Afectan a equipos físicos y entorno.
* **Robos y sabotajes**: Robo o daño de equipos.
* **Acceso no autorizado**: Entrada a instalaciones críticas.
* Ejemplo: Robo de servidores con datos sensibles.

Note: Las amenazas físicas afectan a los equipos físicos o al entorno donde se encuentran los sistemas. Los robos y sabotajes incluyen el robo de equipos o el sabotaje intencionado de sistemas. El acceso no autorizado es cuando personas sin autorización entran a instalaciones críticas como salas de servidores. Por ejemplo, alguien podría entrar a la sala de servidores y desconectar equipos o robar dispositivos que contienen datos importantes. La seguridad física es tan importante como la digital pero a menudo se descuida.


### Amenazas Físicas II

* **Desastres naturales**: Incendios, inundaciones, terremotos.
* **Errores humanos**: Acciones no intencionadas.
* **Fallos eléctricos**: Cortes de suministro.
* **Condiciones ambientales**: Temperatura, humedad.

Note: Los desastres naturales como incendios, inundaciones o terremotos pueden dañar físicamente los sistemas causando pérdida de datos y caídas de servicio. Los errores humanos son acciones no intencionadas que causan daños, como borrar archivos accidentalmente o apagar sistemas críticos. Los fallos de suministro eléctrico pueden hacer que sistemas se apaguen repentinamente, provocando pérdida de datos o daños. Las condiciones ambientales inadecuadas como temperatura o humedad excesiva pueden afectar negativamente al hardware, provocando fallos o incluso incendios. Todos estos factores deben considerarse en el plan de seguridad.


### Clasificación: Cómo Interfieren

* **Interrupción**: Activo no disponible o inutilizable.
* **Interceptación**: Acceso no autorizado a activo.
* **Modificación**: Acceso y modificación no autorizada.
* **Fabricación**: Creación de objetos falsos.

Note: Según la forma en que interfieren con los activos, las amenazas se clasifican en cuatro tipos. Interrupción: la amenaza hace que un activo se pierda, quede no disponible o inutilizable (ejemplo: ataque DDoS que hace caer un servidor). Interceptación: un elemento no autorizado consigue acceso a un activo (ejemplo: escucha de comunicaciones no cifradas). Modificación: un elemento no autorizado no solo accede sino que modifica el activo (ejemplo: alteración de registros en base de datos). Fabricación: un elemento no autorizado crea objetos falsos en el sistema (ejemplo: inserción de transacciones fraudulentas).


### Amenazas Internas vs Externas

**Externas**:
* Hackers y ciberdelincuentes.
* Competencia desleal.
* Estados y grupos políticos.

**Internas**:
* Empleados descontentos o negligentes.
* Personal sin formación.
* Ex-empleados con acceso.

Note: Es importante distinguir el origen de las amenazas. Las amenazas externas provienen de fuera de la organización: hackers y ciberdelincuentes que atacan por diversos motivos, competencia desleal buscando información, grupos organizados de ciberdelincuencia, o estados y grupos con motivaciones políticas. Las amenazas internas provienen de dentro: empleados descontentos o negligentes que pueden causar daños intencionados o accidentales, personal sin formación adecuada que comete errores, ex-empleados con acceso no revocado, o proveedores y contratistas con acceso a sistemas. Las amenazas internas son especialmente peligrosas porque ya tienen acceso.


### Ejemplo: Ataque de Phishing

* **Activo objetivo**: Credenciales de acceso.
* **Vulnerabilidad explotada**: Falta de formación personal.
* **Tipo**: Lógica, externa, interceptación.
* **Principios comprometidos**: Confidencialidad, Autenticidad.
* **Impacto**: Acceso no autorizado a sistemas internos.

Note: Veamos un ejemplo completo. Un empleado recibe un correo que aparenta ser del departamento de IT solicitando sus credenciales para "actualizar el sistema". El activo objetivo son las credenciales de acceso (Datos). La vulnerabilidad explotada es la falta de formación en ciberseguridad del personal. El tipo de amenaza es lógica, externa y de interceptación. Los principios comprometidos son Confidencialidad (roban las credenciales) y Autenticidad (se hacen pasar por IT). El impacto es que el atacante obtiene acceso no autorizado a sistemas internos, pudiendo robar datos o causar daños.


### Ejemplo: Ransomware

* **Activo objetivo**: Datos corporativos, servidores.
* **Vulnerabilidad explotada**: Falta de actualizaciones, sin backups.
* **Tipo**: Lógica, externa, modificación e interrupción.
* **Principios comprometidos**: Disponibilidad, Integridad.
* **Impacto**: Pérdida de acceso, paralización operaciones.

Note: Otro ejemplo: un malware cifra todos los archivos de los servidores de la empresa y exige rescate para descifrarlos. Los activos objetivo son datos corporativos y servidores (Datos, Tecnología). La vulnerabilidad explotada es la falta de actualizaciones de seguridad y ausencia de copias de seguridad. El tipo de amenaza es lógica, externa, de modificación (cifra los datos) e interrupción (no se puede acceder). Los principios comprometidos son Disponibilidad (datos inaccesibles) e Integridad (datos modificados/cifrados). El impacto es pérdida de acceso a información crítica y paralización de operaciones. Este tipo de ataque es devastador sin backups adecuados.

---

## 9. Riesgos


### ¿Qué es el Riesgo?

* Probabilidad de que se materialice una amenaza.
* Explota una vulnerabilidad causando daños.
* **Riesgo = Probabilidad × Impacto**
* Ejemplo: Sistema sin actualizar con vulnerabilidad conocida.

Note: El riesgo es la probabilidad de que se produzca un incidente de seguridad, materializándose una amenaza y causando pérdidas o daños. Es la probabilidad de que una amenaza se materialice por el impacto que provocaría la explotación de una vulnerabilidad. El riesgo depende de dos factores: la probabilidad de que la amenaza ocurra y el impacto del daño que causaría. Por ejemplo, si un sistema crítico está desactualizado (vulnerabilidad) y sabemos que los atacantes buscan activamente explotar esa falla (amenaza), el riesgo de un ataque es elevado.


### Componentes del Riesgo

* **Probabilidad**: Posibilidad de que amenaza explote vulnerabilidad.
* **Impacto**: Magnitud del daño si ocurre.
* Ambos factores determinan nivel de riesgo.
* Ejemplo: Alta probabilidad + Alto impacto = Riesgo MUY ALTO.

Note: El riesgo se calcula combinando dos componentes. La probabilidad es la posibilidad de que una amenaza aproveche una vulnerabilidad. Puede ser muy baja, baja, media, alta o muy alta. El impacto es la magnitud del daño que causaría si la amenaza se materializa. Puede ser bajo, medio, alto o crítico. Por ejemplo, una vulnerabilidad pública con herramientas de explotación disponibles tiene probabilidad alta. Si afecta a un sistema crítico con datos de millones de clientes, el impacto es crítico. Combinados, resultan en un riesgo MUY ALTO que requiere acción inmediata.


### Análisis de Riesgos

* Identifica activos críticos del sistema.
* Obtiene imagen rigurosa de riesgos.
* Determina magnitud y gravedad de consecuencias.
* Define umbral de riesgos asumibles.

Note: Podemos identificar los activos críticos de los sistemas de información que pueden suponer un riesgo realizando un análisis de riesgos. Este análisis nos llevará a obtener una imagen rigurosa de los riesgos a los que se encuentra expuesta una organización. Con el análisis del riesgo averiguamos la magnitud y la gravedad de las consecuencias del riesgo a la que está expuesta la organización. Para ello tendremos que definir un umbral que determine los riesgos asumibles de los que no lo son. Es un proceso sistemático y fundamental para cualquier estrategia de ciberseguridad.


### Ejemplo: Servidor Web Sin Actualizar

* **Vulnerabilidad**: Software sin parches conocidos.
* **Amenaza**: Ataque de explotación remota por hackers.
* **Probabilidad**: Alta (vulnerabilidad pública, herramientas disponibles).
* **Impacto**: Crítico (robo datos, pérdida económica, daño reputacional).
* **RIESGO**: MUY ALTO → Acción inmediata requerida.

Note: Veamos un ejemplo de evaluación de riesgos. Tenemos un servidor web de comercio electrónico. La vulnerabilidad es software con vulnerabilidades conocidas sin parches. La amenaza es un ataque de explotación remota por hackers. La probabilidad es alta porque la vulnerabilidad es pública y existen herramientas automatizadas para explotarla. El impacto es crítico porque podría resultar en robo de datos de tarjetas, pérdida económica y daño reputacional devastador. Combinando probabilidad alta con impacto crítico, el riesgo es MUY ALTO y requiere acción inmediata. El servidor debe actualizarse urgentemente o desconectarse hasta resolver el problema.


### Matriz de Riesgos

| Prob/Impacto | Bajo | Medio | Alto | Crítico |
|--------------|------|-------|------|---------|
| **Muy Alta** | Medio | Alto | Muy Alto | Crítico |
| **Alta** | Medio | Alto | Alto | Muy Alto |
| **Media** | Bajo | Medio | Alto | Alto |
| **Baja** | Bajo | Bajo | Medio | Alto |

Note: Una herramienta común para visualizar riesgos es la matriz de probabilidad e impacto. En el eje horizontal tenemos el impacto (Bajo, Medio, Alto, Crítico). En el eje vertical tenemos la probabilidad (Muy Baja, Baja, Media, Alta, Muy Alta). La intersección nos da el nivel de riesgo resultante. Por ejemplo, una amenaza con probabilidad Muy Alta y impacto Crítico resulta en un riesgo Crítico. Mientras que una amenaza con probabilidad Baja e impacto Bajo resulta en un riesgo Bajo. Esta matriz ayuda a priorizar qué riesgos atender primero.


### Tratamiento del Riesgo I

* **EVITAR**: Eliminar la causa del riesgo.
* No implementar actividad que implique riesgo.
* Ejemplo: No ofrecer servicios cloud para evitar riesgos asociados.

Note: Una vez identificados los riesgos, debemos decidir cómo tratarlos. La primera opción es EVITAR el riesgo eliminando su causa. Por ejemplo, cuando sea viable optar por no implementar una actividad o proceso que pudiera implicar un riesgo. Un ejemplo sería que una empresa decide no ofrecer servicios de almacenamiento en la nube para evitar los riesgos asociados con el manejo de datos de terceros. Es la opción más radical: si no tienes el activo o no realizas la actividad, no existe el riesgo asociado.


### Tratamiento del Riesgo II

* **MITIGAR**: Reducir probabilidad o impacto.
* Implementar y monitorizar controles.
* Ejemplo: Instalar firewall y sistemas de detección.

Note: La segunda opción es MITIGAR el riesgo adoptando medidas que reduzcan el impacto o la probabilidad del riesgo a través de la implementación y monitorización de controles. Por ejemplo, instalar un firewall y sistemas de detección de intrusos para reducir la probabilidad de ataques exitosos. Esta es la opción más común en ciberseguridad: no puedes eliminar completamente el riesgo, pero puedes reducirlo a niveles aceptables mediante controles de seguridad apropiados. Es un equilibrio entre costo de controles y reducción de riesgo.


### Tratamiento del Riesgo III

* **TRANSFERIR**: Compartir riesgo con terceros.
* Seguros, contratos, outsourcing.
* Ejemplo: Contratar seguro de ciberseguridad.

Note: La tercera opción es TRANSFERIR el riesgo compartiéndolo con terceros a través de seguros, contratos, etc. Por ejemplo, contratar un seguro de ciberseguridad que cubra las pérdidas en caso de un ataque de ransomware. También se transfiere riesgo contratando servicios externos especializados que asumen la responsabilidad de ciertos aspectos de seguridad. No elimina el riesgo, pero transfiere el impacto financiero a otra entidad. Es útil cuando el coste del seguro es menor que el impacto potencial del riesgo.


### Tratamiento del Riesgo IV

* **ACEPTAR**: Asumir la existencia del riesgo.
* Monitorizar sin tomar medidas activas.
* Cuando coste de mitigación supera impacto potencial.
* Ejemplo: No duplicar sistema no crítico muy costoso.

Note: La cuarta opción es ACEPTAR el riesgo, asumiendo su existencia y monitorizándolo cuando el coste de mitigación supera el impacto potencial. Por ejemplo, una pequeña empresa acepta el riesgo de no tener redundancia en un sistema no crítico porque el coste del sistema duplicado es muy alto en relación al impacto. Es una decisión consciente y documentada: la organización entiende el riesgo, evalúa que es aceptable, y decide no invertir en controles adicionales. Debe monitorizarse periódicamente por si las circunstancias cambian.

---

## 10. Medidas de Seguridad


### Propósito de las Medidas

* Reducir riesgos o minimizar su impacto.
* Procedimientos de control del riesgo.
* Protegen información confidencial.
* Evitan robos y fugas de información.

Note: El tratamiento del riesgo mediante controles supone claros beneficios para la "salud" de la ciberseguridad. De esta manera mantenemos protegida nuestra información confidencial frente a la mayoría de amenazas y vulnerabilidades detectadas o no, evitando robos y fugas de información. A los procedimientos utilizados para reducir los riesgos o minimizar su impacto se les denomina "mecanismos o medidas de seguridad". Estas medidas son la implementación práctica de nuestra estrategia de seguridad. Sin medidas efectivas, el análisis de riesgos no sirve de nada.


### Controles Preventivos

* Eliminan o reducen posibilidad de amenazas.
* Implementados ANTES de que ocurra el incidente.
* Ejemplos: Firewall, cifrado, MFA, formación.

Note: Los controles preventivos eliminan o reducen la posibilidad de que las amenazas lleguen a materializarse. Se implementan antes de que ocurra cualquier incidente. Ejemplos incluyen firewall (bloquea accesos no autorizados desde Internet), sistema de autenticación multifactor o MFA (requiere múltiples formas de verificación), cifrado de datos (protege información en reposo y en tránsito), políticas de contraseñas fuertes (requiere complejidad y renovación periódica), segmentación de red (separa sistemas críticos de otros menos seguros), y formación de empleados (previene errores humanos y ataques de ingeniería social). Son la primera línea de defensa.


### Controles de Detección

* Permiten detectar suceso no deseado.
* Funcionan durante o después del incidente.
* Ejemplos: IDS, SIEM, monitorización logs, auditorías.

Note: Los controles de detección permiten detectar un suceso no deseado cuando está ocurriendo o ha ocurrido. Funcionan durante o después del incidente. Ejemplos incluyen IDS o Sistema de Detección de Intrusos (detecta intentos de acceso no autorizado), SIEM o Security Information and Event Management (correlaciona eventos de seguridad de múltiples fuentes), monitorización de logs (registra y analiza actividades sospechosas), sistemas de detección de malware (identifica software malicioso), auditorías de seguridad (revisiones periódicas de controles), y alertas de accesos anómalos (notifica comportamientos inusuales). Son cruciales para responder rápidamente.


### Medidas de Reacción y Recuperación

* Reducen impacto tras materializarse amenazas.
* Implementadas DESPUÉS del incidente.
* Ejemplos: Backups, BCP, DRP, equipos redundantes.

Note: Las medidas de reacción y recuperación reducen el impacto en caso de haberse materializado las amenazas. Se implementan después de que ocurra el incidente. Ejemplos incluyen backups o copias de seguridad (permiten restaurar datos perdidos), Plan de Continuidad de Negocio o BCP (mantiene operaciones críticas), Plan de Recuperación ante Desastres o DRP (restaura sistemas tras incidentes graves), dispositivos redundantes (equipos duplicados para sustitución inmediata), Equipo de Respuesta a Incidentes o CSIRT (gestiona y resuelve incidentes), y sistemas de respaldo automático o failover (cambian a sistemas alternativos automáticamente). Minimizan el tiempo de inactividad.


### Ejemplo: Empresa de Desarrollo I

**Riesgo**: Robo de código fuente.

**Preventivas**:
* Control de acceso basado en roles.
* Autenticación de dos factores para repositorio.
* Cifrado de datos en repositorios.

Note: Veamos un ejemplo completo de implementación de medidas. Una empresa de desarrollo de software identifica el riesgo de robo de código fuente. Para prevenirlo, implementa control de acceso basado en roles (solo desarrolladores acceden al repositorio), autenticación de dos factores para acceso al repositorio (mayor seguridad en autenticación), y cifrado de datos en repositorios (protección adicional). Estas medidas preventivas reducen significativamente la probabilidad de que el código sea robado. El acceso está limitado, requiere múltiples factores de autenticación y los datos están cifrados.


### Ejemplo: Empresa de Desarrollo II

**Riesgo**: Robo de código fuente.

**Detectivas**:
* Monitorización de descargas masivas.
* Logs de acceso con alertas automáticas.
* Auditorías trimestrales de permisos.

Note: Continuando con el ejemplo, para detectar posibles incidentes, implementan monitorización de descargas masivas de código (detecta si alguien descarga todo el repositorio sospechosamente), logs de acceso al repositorio con alertas automáticas (registra todos los accesos y alerta si hay patrones anómalos), y auditorías trimestrales de permisos (revisan periódicamente quién tiene acceso a qué). Estas medidas detectivas permiten identificar rápidamente si alguien está intentando robar código o si hay accesos sospechosos, permitiendo responder antes de que el daño sea mayor.


### Ejemplo: Empresa de Desarrollo III

**Riesgo**: Robo de código fuente.

**Reacción/Recuperación**:
* Backups diarios del repositorio.
* Procedimiento de revocación inmediata.
* Seguro de ciberseguridad cobriendo robo IP.

Note: Finalmente, para recuperarse si ocurre un incidente, tienen backups diarios del repositorio (si borran el código, se puede restaurar), procedimiento de revocación inmediata de accesos (si detectan actividad sospechosa, pueden bloquear al usuario inmediatamente), y seguro de ciberseguridad que cubre pérdidas por robo de propiedad intelectual (transfiere el impacto financiero). Estas medidas de recuperación aseguran que, incluso si el código es robado, la empresa puede continuar operando y minimizar las pérdidas financieras. Es un enfoque en capas: prevenir, detectar y recuperar.


### Proceso de Selección de Medidas I

1. **Definir alcance**: ¿Qué analizar?
2. **Identificar activos**: ¿Qué proteger?
3. **Medidas existentes**: ¿Qué ya tenemos?
4. **Vulnerabilidades**: ¿Qué puntos débiles?

Note: Para identificar e implementar medidas adecuadas, seguimos un proceso sistemático. Primero, definir el alcance del análisis: ¿nos centramos en un servicio, departamento o toda la organización? Por ejemplo, analizar la seguridad del departamento de recursos humanos y su sistema de gestión de nóminas. Segundo, identificar qué activos participarán en el estudio y realizar su valoración. Por ejemplo, base de datos de empleados (valor: Crítico), software de nóminas (valor: Alto). Tercero, identificar las medidas de seguridad existentes: qué controles ya están implementados. Si no hay, entonces hay puntos débiles claros.


### Proceso de Selección de Medidas II

5. **Valorar amenazas**: ¿Qué nos puede atacar?
6. **Calcular riesgos**: ¿Cuál es la probabilidad e impacto?
7. **Objetivos de seguridad**: ¿Qué umbral aceptamos?
8. **Seleccionar medidas**: ¿Qué implementar?

Note: Continuando con el proceso. Cuarto, descubrir los puntos débiles o vulnerabilidades que afectan a los activos. Por ejemplo, base de datos sin cifrar, falta de MFA. Quinto, valorar las posibles amenazas que pueden afectar. Por ejemplo, ataque de ransomware (Probabilidad: Media, Impacto: Crítico). Sexto, obtener el riesgo para cada activo/amenaza valorando probabilidad e impacto. Por ejemplo, ransomware en BD de empleados = Riesgo ALTO. Séptimo, establecer objetivos de seguridad: el umbral por encima del cual tomaremos medidas. Octavo, seleccionar las medidas de protección posibles basándose en el análisis y los recursos disponibles.

---

## 11. Visión Integrada


### La Cadena de la Seguridad

* **Activos** → tienen → **Vulnerabilidades**
* **Amenazas** → explotan → **Vulnerabilidades**
* **Amenazas** + **Vulnerabilidades** = **Riesgos**
* **Medidas de Seguridad** → mitigan → **Riesgos**

Note: La seguridad se puede entender como una cadena de elementos interrelacionados. Primero tenemos los activos, que son los recursos valiosos de la organización. Estos activos tienen vulnerabilidades, que son puntos débiles. Las amenazas intentan explotar esas vulnerabilidades. La combinación de una amenaza que explota una vulnerabilidad genera un riesgo. Finalmente, las medidas de seguridad se implementan para mitigar esos riesgos. Es un ciclo continuo: identificamos activos, encontramos sus vulnerabilidades, evaluamos amenazas, calculamos riesgos, e implementamos medidas. Entender esta cadena es fundamental para cualquier profesional de ciberseguridad.


### Ejemplo Integrado: Supermercado I

**Contexto**: Cadena de supermercados con sistema de pago.

**Activo**:
* Base de datos con transacciones de tarjetas.
* Valor: Crítico (datos financieros, regulación PCI-DSS).

Note: Veamos un ejemplo integrado completo que une todos los conceptos. Una cadena de supermercados tiene sistema de pago con tarjeta. El activo principal es la base de datos con información de transacciones de tarjetas de crédito. Su valor es crítico porque contiene datos financieros de clientes y está sujeto a regulación PCI-DSS (Payment Card Industry Data Security Standard). La pérdida o compromiso de este activo tendría consecuencias devastadoras: multas millonarias, pérdida de confianza de clientes, posible cierre del negocio, y responsabilidad legal.


### Ejemplo Integrado: Supermercado II

**Vulnerabilidad**:
* TPV no segmentado del resto de red.
* Software de TPV con versión antigua vulnerable.
* Personal sin formación en seguridad.

Note: Continuando con el ejemplo, identificamos vulnerabilidades. El sistema de punto de venta (TPV) no está segmentado del resto de la red, lo que significa que si alguien accede a la red general, puede llegar a los TPV. El software del TPV tiene una versión antigua con vulnerabilidades conocidas, lo cual es muy peligroso porque existen exploits públicos. Y el personal no está formado en seguridad, lo que los hace vulnerables a ingeniería social. Estas tres vulnerabilidades crean puntos de entrada potenciales para atacantes. La combinación de las tres es especialmente peligrosa.


### Ejemplo Integrado: Supermercado III

**Amenaza**:
* Ataque dirigido para instalar malware en TPV.
* Ingeniería social a empleados.
* Conexión de dispositivos USB infectados.

Note: Las amenazas que podrían explotar estas vulnerabilidades incluyen ataques dirigidos para instalar malware en los TPV que capture datos de tarjetas (muy común en retail), ataques de ingeniería social a empleados para acceder a la red interna (aprovechando la falta de formación), y conexión de dispositivos USB infectados en los TPV (puede ser intencional o accidental). Estas amenazas son reales y han ocurrido en múltiples cadenas de retail a nivel mundial, resultando en robos masivos de datos de tarjetas.


### Ejemplo Integrado: Supermercado IV

**Análisis de Riesgo**:
* Probabilidad: Alta (objetivo atractivo, vulnerabilidades conocidas).
* Impacto: Crítico (pérdida masiva datos, multas, pérdida confianza).
* **RIESGO TOTAL**: MUY ALTO

Note: El análisis de riesgo combina probabilidad e impacto. La probabilidad es alta porque es un objetivo muy atractivo para ciberdelincuentes (datos de tarjetas tienen valor en mercado negro), existen vulnerabilidades conocidas en el software, y los ataques a retail son comunes. El impacto es crítico porque un ataque exitoso resultaría en pérdida masiva de datos financieros, multas millonarias por incumplimiento de PCI-DSS, pérdida de confianza de clientes que dejarían de comprar allí, y posiblemente cierre del negocio. Combinando probabilidad alta con impacto crítico, el riesgo total es MUY ALTO. Requiere acción inmediata.


### Ejemplo Integrado: Supermercado V

**Medidas Preventivas**:
* Segmentación de red (TPV en VLAN aislada).
* Actualización de software de TPV.
* Desactivación de puertos USB.
* Formación trimestral del personal.
* Cifrado punto a punto (P2PE) de datos.

Note: Para mitigar este riesgo muy alto, se implementan múltiples medidas preventivas. Segmentación de red pone los TPV en una VLAN aislada del resto de la red, limitando el movimiento lateral si alguien compromete otro sistema. Actualización de software de TPV a última versión cierra las vulnerabilidades conocidas. Desactivación de puertos USB en TPV evita conexión de dispositivos infectados. Formación trimestral del personal en ciberseguridad reduce riesgo de ingeniería social. Y cifrado punto a punto (P2PE) de datos de tarjetas asegura que, incluso si capturan las comunicaciones, los datos están cifrados e inutilizables.


### Ejemplo Integrado: Supermercado VI

**Medidas Detectivas**:
* IDS/IPS monitorizando tráfico de red de TPV.
* Logs centralizados de todos los TPV.
* Auditorías mensuales de seguridad.
* Detección de anomalías en transacciones.

Note: Las medidas detectivas permiten identificar rápidamente si algo va mal. IDS/IPS (Sistema de Detección/Prevención de Intrusos) monitoriza el tráfico de red de TPV buscando patrones sospechosos. Logs centralizados de todos los TPV permiten análisis forense si hay incidente. Auditorías mensuales de seguridad verifican que todos los controles están funcionando correctamente. Y sistema de detección de anomalías en transacciones identifica comportamientos inusuales que podrían indicar fraude o compromiso. Estas medidas no previenen el ataque, pero permiten detectarlo rápidamente para minimizar el daño.


### Ejemplo Integrado: Supermercado VII

**Medidas de Reacción/Recuperación**:
* Plan de respuesta a incidentes PCI-DSS.
* Seguro de ciberseguridad con cobertura específica.
* Backups cifrados de configuraciones de TPV.
* Equipo de respuesta 24/7.

Note: Finalmente, las medidas de recuperación aseguran que, si todo lo demás falla, pueden minimizar el daño. Plan de respuesta a incidentes conforme a PCI-DSS define exactamente qué hacer si hay una brecha. Seguro de ciberseguridad con cobertura específica transfiere el impacto financiero. Backups cifrados de configuraciones de TPV permiten restaurar rápidamente sistemas comprometidos. Y equipo de respuesta 24/7 puede actuar inmediatamente en cualquier momento. Con todas estas medidas, el riesgo residual se reduce a BAJO, aunque bajo monitorización continua. El coste anual de estas medidas (150.000€) es ínfimo comparado con la pérdida potencial (varios millones de euros más daño reputacional).


### Conclusión

* Entender relación entre conceptos es fundamental.
* Activos → Vulnerabilidades → Amenazas → Riesgos → Medidas.
* Base para Plan Director de Seguridad.
* Base para Análisis de Riesgos continuo.
* Aplicación práctica en siguientes unidades.

Note: Entender la relación entre activos, vulnerabilidades, amenazas, riesgos y medidas de seguridad es fundamental para construir una estrategia de ciberseguridad efectiva. Estos conceptos forman la base sobre la que se construyen el Plan Director de Seguridad (estrategia a largo plazo de la organización), el Análisis de Riesgos (evaluación continua de amenazas y vulnerabilidades), y las Políticas de Seguridad (normativas y procedimientos). En las siguientes unidades profundizaremos en cómo estos conceptos se aplican de forma práctica en el Plan Director de Seguridad y el Análisis de Riesgos. Habéis aprendido los principios generales fundamentales de la ciberseguridad.

---

## Resumen Final


### Conceptos Clave Aprendidos

* Ciberseguridad: Protección preventiva.
* Ciberdefensa: Respuesta activa.
* Triada CIA: Confidencialidad, Integridad, Disponibilidad.
* Fiabilidad sobre seguridad total.

Note: Hoy hemos cubierto los principios generales fundamentales de la ciberseguridad. Aprendimos que la ciberseguridad es protección preventiva de sistemas y datos, mientras que la ciberdefensa es respuesta activa ante ataques. Vimos la Triada CIA como pilares fundamentales: Confidencialidad (solo autorizados acceden), Integridad (datos no alterados), y Disponibilidad (sistemas accesibles cuando se necesitan). También entendimos por qué enfocarse en fiabilidad es más realista que buscar seguridad total imposible. Estos son conceptos que usaréis continuamente en vuestra carrera profesional.


### Cadena de Seguridad

* **Activos** valiosos con **vulnerabilidades**.
* **Amenazas** que explotan vulnerabilidades.
* Generan **riesgos** que deben gestionarse.
* **Medidas de seguridad** mitigan riesgos.

Note: La cadena de seguridad que hemos estudiado es el marco conceptual para entender ciberseguridad. Los activos son recursos valiosos que tienen vulnerabilidades o puntos débiles. Las amenazas intentan explotar esas vulnerabilidades. Cuando una amenaza puede explotar una vulnerabilidad, se genera un riesgo. Y las medidas de seguridad (preventivas, detectivas y de recuperación) se implementan para mitigar esos riesgos. Esta cadena es el fundamento de toda gestión de seguridad: identificar, analizar, priorizar y proteger.


### Decálogo de Ciberseguridad

1. Cultura de ciberseguridad y concienciación.
2. No abrir enlaces ni descargar archivos sospechosos.
3. Usar software de seguridad actualizado.
4. Limitar superficie de exposición a amenazas.
5. Cifrar información sensible.

Note: Repasemos el decálogo de ciberseguridad que debéis tener siempre presente. Primero, cultura de ciberseguridad y concienciación: educar a todos es fundamental. Segundo, no abrir enlaces ni descargar archivos sospechosos: previene phishing y malware. Tercero, usar software de seguridad actualizado: antivirus, firewalls, etc. Cuarto, limitar superficie de exposición: cerrar servicios innecesarios. Quinto, cifrar información sensible: protección adicional de datos críticos. Estos cinco primeros puntos son principalmente preventivos.


### Decálogo de Ciberseguridad (cont.)

6. Borrado seguro de información.
7. Realizar copias de seguridad periódicas.
8. Mantener actualizados sistemas y aplicaciones.
9. Revisar regularmente configuración de seguridad.

Note: Continuando con el decálogo. Sexto, borrado seguro de información: eliminar completamente datos innecesarios. Séptimo, realizar copias de seguridad periódicas: esencial contra ransomware y fallos. Octavo, mantener actualizados sistemas y aplicaciones: parches cierran vulnerabilidades. Noveno, revisar regularmente configuración de seguridad: verificar que todo está correctamente configurado. Estos puntos combinan prevención, detección y recuperación. Aplicarlos consistentemente reduce significativamente el riesgo de incidentes de seguridad.


### Próximos Pasos

* Plan Director de Seguridad de la Información.
* Análisis de Riesgos en profundidad.
* Implementación práctica de medidas.
* Aplicación a casos reales.

Note: Estos principios generales son la base sobre la que construiremos el resto del módulo. En las próximas unidades profundizaremos en el Plan Director de Seguridad de la Información, donde veremos cómo diseñar una estrategia integral de seguridad para una organización. Estudiaremos el Análisis de Riesgos en profundidad, aplicando metodologías estándar. Y trabajaremos en la implementación práctica de medidas de seguridad, aplicándolas a casos reales. Todo lo que habéis aprendido hoy os servirá como fundamento para estos temas más avanzados.


### ¡Gracias!

¿Preguntas?

Note: Esto concluye la sesión sobre Principios Generales de Ciberseguridad. Espero que hayáis comprendido estos conceptos fundamentales que son la base de todo lo que estudiaremos en este módulo. Recordad que la ciberseguridad no es solo tecnología, sino también personas, procesos y una cultura organizacional. Os animo a consultar los recursos adicionales en Incibe-Cert y CCN-Cert, y a practicar identificando activos, vulnerabilidades y amenazas en vuestro entorno. ¿Tenéis alguna pregunta sobre lo que hemos visto hoy?
