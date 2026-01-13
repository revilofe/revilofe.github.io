---
title: "UD 2 - 2.5 Cómo escribir informes técnicos"
description: "Aprende a redactar informes técnicos eficaces con esta guía completa, que abarca desde la estructura y el estilo hasta consejos para la presentación de incidentes de seguridad."
summary: "Esta guía detallada ofrece consejos prácticos para la elaboración de informes técnicos, cubriendo aspectos estratégicos, de estructura y redacción. Incluye recomendaciones específicas para documentar incidentes de seguridad, con el objetivo de mejorar la claridad y el impacto de tus documentos."
authors:
    - Eduardo Fdez
date: 2025-11-25
icon: "material/file-document-outline"
permalink: /is/unidad-2/2.5-como-escribir-informes-tecnicos
categories:
    - "Incidentes de seguridad"
tags:
    - "Informes"
    - "Documentación"
    - "Seguridad"
---

# 3.2. Vectores de ataque en incidentes de ciberseguridad

Para la elaboración de informes técnicos en ciberseguridad, es fundamental comprender ciertos conceptos clave que aseguran la claridad y precisión en la documentación de incidentes. A continuación, se detallan algunos de los conceptos más relevantes.

### 1. Introducción

Hay dos tipos de “¿por dónde ha entrado?” en esta vida:

1. El de tu madre cuando llegas tarde (“¿por dónde has entrado tú a estas horas?”).
2. El del SOC cuando suena la sirena y alguien pregunta “¿por dónde nos han entrado?”

En ciberseguridad, si no respondes bien a esa pregunta, pasa una cosa maravillosa: **todo el mundo empieza a improvisar**. Y la improvisación en incidentes es como hacer cirugía con un abrelatas: creativo, sí… recomendable, no.

Así que vamos a dejarlo **cristalino**, con un concepto que parece fácil pero se confunde más que “IP pública” con “mi IP del Wi-Fi”: **el vector de ataque**.


### 2. Qué es un vector de ataque

Cuando hablamos de **vectores de ataque**, nos referimos **estrictamente** a la **vía**, el **camino** o el **medio** por el que un atacante consigue **contacto con el sistema** para ejecutar su acción.

Dicho “para examen” (y para que no haya escapatoria):

> **Vector de ataque = el CANAL** (Email, Web, Puerto RDP, USB…) que utiliza el atacante para desplegar su **TÉCNICA** (Phishing, SQLi, Malware…).

Y la regla de oro, que vale más que muchos PDF:

> **Regla de oro:** el **vector** es el *“dónde”* (la puerta); la **técnica** es el *“cómo”* (forzar la cerradura).

!!! example "Ejemplos rápidos"
* “Nos han entrado por **correo**” → Vector: correo. Técnica: phishing.
* “Nos han entrado por **RDP expuesto**” → Vector: RDP. Técnica: fuerza bruta / credenciales filtradas.
* “Nos han entrado por **una web vulnerable**” → Vector: aplicación web. Técnica: SQLi / XSS.

!!! info "Aclaración"
    ¿Vector = phishing? No: **phishing es técnica**. El vector sería **el canal** (normalmente, correo).



### 2. Conceptos previos: la “fórmula” del incidente

Estos términos se confunden muchísimo. Imaginad que el sistema es una **casa** y queremos saber **cómo han robado**:

* **Actor de amenaza (QUIÉN):** el origen del ataque, quien lo ejecuta.

    *Ejemplos:* cibercriminal, *insider*, hacktivista.

* **Amenaza (QUÉ puede causar daño):** lo que podría ocurrir / lo que busca el ataque.

    *Ejemplos:* malware, robo de identidad, sabotaje, fraude, error humano.

* **Vulnerabilidad / Debilidad (POR QUÉ es posible):** el fallo técnico, organizativo o humano que lo permite.

    *Ejemplos:* ventana abierta (sin parches), cerradura mala (contraseña débil), el dueño abre a cualquiera (falta de formación).

* **Vector de ataque (POR DÓNDE entra):** la ruta concreta usada para llegar al objetivo.

    *Ejemplos:* entrar por la ventana del baño, entrar por la puerta haciéndose pasar por cartero (ingeniería social).

!!! tip "Resumen de pizarra"
    El **actor** elige un **vector** (camino) y aplica una **técnica**, aprovechando una **vulnerabilidad** (hueco de seguridad), para materializar una **amenaza** y causar un **impacto**.

Y ahora, el matiz que evita un montón de confusión:

!!! tip "Ojo importante"
    Un vector **no siempre** implica un “fallo informático complejo”.
    A veces el vector es **técnico** (un puerto abierto).
    A veces el vector es **humano** (un usuario engañado por teléfono).
    Y no siempre hay “Matrix” ni código verde: a veces solo hay **una contraseña válida** en manos equivocadas entrando por la puerta principal.


### 3. Componentes de un vector de ataque (lo que se analiza en un incidente)

Cuando analizamos un incidente, respondemos a cuatro preguntas. Si faltan, el informe queda cojo:

1. **Punto de entrada (Vector):** ¿Por dónde entró? (Email, USB, Wi-Fi, VPN…)
2. **Técnica:** ¿Qué hizo en ese canal? (Phishing, fuerza bruta, explotación de vulnerabilidad…)
3. **Debilidad explotada (causa raíz):** ¿Por qué funcionó? (Sin MFA, sin parches, usuario “clickeador”…)
4. **Impacto:** ¿Qué consiguió? (Cifrado, exfiltración, acceso administrativo, fraude…)

!!! tip "Consejo de memorización"
    **Vector → Técnica → Debilidad → Impacto**.


### 4. Ejemplos claros de vectores de ataque (vida real, sin adornos)

#### 4.1. Vector: Correo electrónico

**Técnica:** phishing (login falso), adjuntos maliciosos, suplantación.
**Debilidad:** falta de formación, filtros antispam insuficientes, ausencia de MFA.
**Impacto:** robo de credenciales o infección inicial (y desde ahí, escalada a ransomware en muchos casos).

!!! example "Escenario"
    Llega “Factura pendiente” → clic → login falso → credenciales robadas.
    (Y a partir de ahí, el atacante ya no “entra”: **inicia sesión** como si fuera el usuario.)


#### 4.2. Vector: Servicios remotos expuestos (RDP / VPN / SSH)

**Técnica:** fuerza bruta, *password spraying*, credenciales filtradas.
**Debilidad:** contraseñas débiles, sin MFA, firewall mal segmentado, poca monitorización.
**Impacto:** acceso remoto real, movimiento lateral, ransomware.

!!! example "Escenario"
    Un servidor tiene RDP abierto a Internet → el atacante prueba credenciales o reutiliza contraseñas filtradas → entra.
    (Y a partir de ahí, ya no “entra”: **está dentro**.)

#### 4.3. Vector: Aplicaciones web

**Técnica:** SQL Injection (SQLi), Cross-Site Scripting (XSS), u otros fallos según el caso.
**Debilidad:** validación/sanitización inexistente, desarrollo inseguro.
**Impacto:** extracción de datos, secuestro de sesión, modificación de información.

!!! example "Escenario"
    Una tienda online tiene un formulario mal programado → el atacante inyecta datos maliciosos y rompe la lógica.
    (Y a partir de ahí, ya no “entra”: **manipula la aplicación** para robar datos o tomar el control.)

#### 4.4. Vector: Cadena de suministro (Supply Chain)

**Técnica:** comprometer actualización o librería de terceros.
**Debilidad:** confianza implícita sin verificación, falta de controles de integridad y revisión de dependencias.
**Impacto:** *backdoor* desplegado de forma masiva.

!!! example "Escenario"
    Un software popular lanza una actualización comprometida (en origen ha sido manipulada o la dependencia está comprometida.) → los usuarios la instalan confiando en el proveedor → el atacante obtiene acceso a miles de sistemas.
    (Y a partir de ahí, ya no “entra”: **está dentro** de todos los sistemas que actualizaron.)

#### 4.5. Vector: Medios físicos (USB)

**Técnica:** malware en USB o BadUSB (emulación de teclado).

**Escenario A (dirigido):** alguien deja un USB (“Nóminas”) en el parking para que lo cojas.
**Escenario B (mundano/accidental):** un empleado usa su USB personal en casa (PC infectado por “ver pelis piratas”), el virus salta al USB y al día siguiente lo conecta en la oficina.

**Debilidad:** puertos sin control, antivirus desactualizado, falta de concienciación.
**Impacto:** el vector físico ha **puenteado el firewall perimetral**.

!!! tip "Consejo"
    La seguridad perimetral” no sirve si el ataque **entra en el bolsillo**.


#### 4.6. Vector: Redes inalámbricas (Wi-Fi)

**Técnica:** Evil Twin (gemelo malvado), Rogue AP, portal cautivo malicioso.
**Debilidad:** conexión automática a redes abiertas, malas configuraciones, falta de verificación y hábitos inseguros.
**Impacto:** robo de credenciales, interceptación de tráfico, ataques Man-in-the-Middle (MitM).

**Matiz clave:** con **HTTPS** el atacante no “ve todo” porque el contenido va cifrado, pero **sí puede** robar credenciales si te engancha a un portal falso o aprovechar servicios sin cifrar.

!!! example "Escenario"
“WIFI_GRATIS_GUEST” → te conectas → portal cautivo falso → introduces credenciales → adiós credenciales.


#### 4.7. Vector: Comunicaciones personales (Vishing / Smishing)

**Técnica:** ingeniería social por teléfono o SMS.
**Debilidad:** falta de procedimiento de verificación, presión/urgencia, desconocimiento.
**Impacto:** acceso por robo de credenciales o bypass de MFA “humano”.

!!! example "Escenario"
    Llamada del “soporte técnico” → “Necesito que me confirmes tu contraseña para solucionar un problema urgente” → usuario la da → el atacante entra.
    (Y a partir de ahí, ya no “entra”: **inicia sesión** como si fuera el usuario.)

!!! tip "Idea clave"
    Aquí el atacante no hackea máquinas. Hackea **decisiones**.


### 5. Mini-plantilla para analizar incidentes (clase y examen)

Al analizar un incidente, es fundamental identificar claramente los cuatro componentes clave: vector, técnica, vulnerabilidad e impacto. Aquí tienes una mini-plantilla para ayudarte a estructurar tu análisis:

1. **Vector (Medio):** Ej. Correo electrónico.
2. **Técnica (Acción):** Ej. Phishing con enlace malicioso.
3. **Vulnerabilidad (Causa raíz):** Ej. usuario sin formación + no había MFA.
4. **Impacto (Consecuencia):** Ej. robo de credenciales y acceso al sistema.


!!! tip "Analogía para recordar"
    El **vector** es el **vehículo** (el camino).
    La **técnica** es el **arma** (el método).
    La **vulnerabilidad** es la **falta de chaleco antibalas** (la debilidad).
