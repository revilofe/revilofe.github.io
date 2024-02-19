---
Matrixtitle: "UD 3 - 1.1 Recopilación y almacenamiento de evidencias"
description: Recopilación y almacenamiento de evidencias
summary: Recopilación y almacenamiento de evidencias
authors:
    - Eduardo Fdez
date: 2024-02-13
icon: 
permalink: /is/unidad3/3.1
categories:
    - IS
tags:
    - IS
    - Seguridad
    - Evidencias
    - Recopilación
    - Almacenamiento
---
![](assets/IS-U311-RecopilacionDeEvidencias0.png)

## 4.1 PLAYBOOK

> **RA3**
> c) Se ha realizado la investigación de incidentes de ciberseguridad.

### 1. Playbook



# ¿Qué es un playbook de respuesta a incidentes de ciberseguridad?

[![MSc. Ing. Sebastián A. V.](https://media.licdn.com/dms/image/D4E03AQHK0N40FNu3zQ/profile-displayphoto-shrink_100_100/0/1700274099024?e=1714003200&v=beta&t=VcJshnRaeeGcaQlqdFCtKoqvOy6GA57d9bZNNveb8qc)](https://www.linkedin.com/in/profesorsvargas/)

[MSc. Ing. Sebastián A. V.](https://www.linkedin.com/in/profesorsvargas/)

⚔Advanced Cybersecurity Consultant and Educator▫️MSc Cyberterrorism and Cyberwarfare▫️MSc in IT/OT▫️ Civil Engineer in Computer Science▫️CEH Practical▫️eCIR▫️eJPT▫️eCDFP▫️MITRE ATT&CK THDE AE CTI PTM SOC

[21 artículos ](https://www.linkedin.com/in/profesorsvargas/recent-activity/posts/)Seguir

25 de agosto de 2023

**Abrir lector interactivo**

### 🛡️** ****Respuesta a Incidentes:** Lo que Necesitas Saber 🛡️

Un** ****runbook** se enfoca en tareas técnicas y operativas específicas, un** ****playbook** aborda respuestas estratégicas y coordinadas a eventos o incidentes. Es común que dentro de un playbook de ciberseguridad se haga referencia a un runbook específico para llevar a cabo una tarea técnica detallada. 🔄

### **RUNBOOK vs PLAYBOOK para Incidentes de Ciberseguridad** 🔍

Ambos términos, Runbook y Playbook, son ampliamente utilizados en el mundo de la ciberseguridad y las operaciones IT, pero tienen propósitos y aplicaciones distintas. Veamos las diferencias clave:

---

📘** ****RUNBOOK** 📘

1. **Definición:** 📝 Es un conjunto detallado de procedimientos operativos estándar que describe cómo realizar una tarea específica o una serie de tareas. Funciona casi como un manual técnico.
2. **Objetivo:** 🎯 Automatizar tareas rutinarias y operaciones técnicas.
3. **Contenido:** 🛠️ Instrucciones paso a paso, scripts, decisiones automatizadas, y detalles técnicos.
4. **Aplicación:** 💡 Generalmente se usa en operaciones IT para administrar y resolver problemas comunes de sistemas y aplicaciones.
5. **Ejemplo:** 🌐 Si un servidor se cae, el runbook puede tener instrucciones detalladas sobre cómo reiniciarlo, verificar su estado, y validar que todos los servicios están funcionando correctamente.

---

📒** ****PLAYBOOK** 📒

1. **Definición:** 📝 Es una guía estratégica que detalla las acciones a seguir en respuesta a eventos específicos, como incidentes de ciberseguridad.
2. **Objetivo:** 🎯 Coordinar respuestas efectivas y eficientes a incidentes y situaciones de crisis.
3. **Contenido:** 🛠️ Protocolos, responsabilidades, procesos de comunicación, y pasos a seguir durante y después de un incidente.
4. **Aplicación:** 💡 Se utiliza principalmente en equipos de respuesta a incidentes de ciberseguridad para guiar la respuesta ante eventos de seguridad específicos.
5. **Ejemplo:** 🌐 En caso de un ataque de phishing, el playbook puede guiar al equipo sobre cómo identificar el ataque, quién debe ser notificado, cómo comunicar el incidente a stakeholders, y qué pasos técnicos seguir para mitigar el daño.

**¿Qué es una respuesta a incidentes?** 🤔

Antes de adentrarnos en el tema, es posible que no estés familiarizado con el término "respuesta a incidentes". Según Varonis, la respuesta a incidentes se refiere al proceso de limpieza y recuperación cuando se detecta una violación de ciberseguridad. Estas infracciones pueden denominarse también como "incidentes de ciberseguridad". Es fundamental contar con un plan y un equipo especializado que se encargue de gestionar el incidente, con el objetivo de minimizar daños y costos de recuperación.

📚** ****Analizando el concepto: Playbook de Respuesta a Incidentes** 📚

Si hablamos en términos coloquiales, en español un "playbook" podría compararse con un libro de instrucciones detallado por un cuerpo técnico, similar al que se utiliza en deportes como el fútbol, donde se describen las distintas estrategias o jugadas a implementar. Considerando la respuesta a incidentes como un conjunto de acciones bien coordinadas, esta comparación tiene mucho sentido.

![No hay texto alternativo para esta imagen](https://media.licdn.com/dms/image/D4D12AQEEpllENc-5dg/article-inline_image-shrink_1500_2232/0/1692977775681?e=1714003200&v=beta&t=dZF-km7bDYhi-sNvVD4o87d-7EG0_RUavbpTaaFdUDI)

Según incidenteresponse.com, todas las organizaciones tienen planes para enfrentar diferentes incidentes que, de no estar bien gestionados, podrían impactar negativamente en la continuidad del negocio. El propósito de un playbook es garantizar que todos los integrantes de una organización tengan una clara comprensión de sus deberes y responsabilidades en relación a las normas de ciberseguridad, antes, durante y después de un incidente de seguridad.

📖** ****¿Qué contiene un Playbook de Respuesta a Incidentes?** 📖

* **Identificación:** Pasos detallados sobre cómo identificar el incidente.
* **Notificación:** Proceso de notificación a las personas o entidades relevantes.
* **Medidas de Seguridad:** Protocolos a implementar para garantizar la seguridad.
* **Gestión:** Estrategias para abordar y resolver el incidente.
* **Comunicación:** Plan detallado para mantener informados a empleados, clientes y otros stakeholders.
* **Contactos:** Lista de individuos o entidades clave para la gestión del incidente.

🎯** ****Objetivo Principal** 🎯

El principal propósito de un playbook de respuesta a incidentes es garantizar que las empresas u organizaciones estén preparadas para enfrentar cualquier situación de emergencia. Es esencial que cada miembro esté informado y sepa qué hacer en caso de incidente, permitiendo así minimizar impactos y resolver situaciones de manera rápida y eficaz.

### 📌** ****Definiendo los Pasos del Playbook** 📌

📊** ****El Contexto** 📊

Según SANS, con el aumento en la sofisticación de los ciberataques, es esencial que las organizaciones refuercen sus capacidades de detección y respuesta a incidentes. Las herramientas de monitorización y la correlación de eventos son fundamentales en la gestión de incidentes. Sin embargo, dada la vasta variedad de ataques, es vital tener procesos adaptativos y versátiles. 🛠️ Al diseñar un playbook eficiente, se puede mejorar la capacidad de detectar y actuar frente a diferentes amenazas.

La idea resuena en múltiples organizaciones y plataformas globales: tener un playbook para los escenarios más comunes de ciberataques es imprescindible. 🌐

### ¿Que base usar para clasificar los ciber incidentes?

** ****MITRE ATT&CK** ofrece un detallado marco de tácticas y técnicas usadas por adversarios, permitiendo a los defensores anticipar y contrarrestar amenazas. Por otro lado, la** ****Taxonomía de ENISA** proporciona un marco estandarizado para reportar y compartir información sobre incidentes de ciberseguridad en Europa. Ambos son herramientas valiosas en el ámbito de la ciberseguridad, pero se usan en diferentes contextos y con diferentes propósitos. 🔄

📘** ****MITRE ATT&CK** 📘

1. **Definición:** 📝 ATT&CK (Adversarial Tactics, Techniques, and Common Knowledge) es un marco creado por MITRE que detalla tácticas, técnicas y procedimientos (TTP) usados por los adversarios contra sistemas Windows, macOS, Linux, y móviles.
2. **Objetivo:** 🎯 Ayudar a los defensores a entender las acciones de los adversarios y desarrollar defensas más efectivas.
3. **Contenido:** 🛠️ Describe el "ciclo de vida" de un ataque, desde la recolección de información inicial hasta la ejecución del ataque y la persistencia en el sistema objetivo.
4. **Aplicación:** 💡 Usado por equipos de ciberseguridad para simular ataques, entrenar al personal, mejorar la detección y respuesta, y fortalecer la postura de seguridad.
5. **Ejemplo:** 🌐 Si un atacante utiliza spear-phishing como técnica de entrada, ATT&CK proporcionaría información sobre cómo detectar, mitigar y responder a esa técnica específica.
6. **Fuente:** **** https://attack.mitre.org/

---

📒** ****Taxonomía de ENISA** 📒

1. **Definición:** 📝 Es un marco establecido por la Agencia Europea de Ciberseguridad (ENISA) para clasificar y entender los diferentes tipos de incidentes de ciberseguridad.
2. **Objetivo:** 🎯 Proporcionar un lenguaje común para que las organizaciones europeas compartan información sobre incidentes de manera coherente y efectiva.
3. **Contenido:** 🛠️ Clasificaciones y descripciones de incidentes, que permiten a las organizaciones identificar y comunicar incidentes de manera estandarizada.
4. **Aplicación:** 💡 Usado por organizaciones y equipos de respuesta a incidentes en Europa para informar y compartir información sobre incidentes de ciberseguridad.
5. **Ejemplo:** 🌐 Si una organización en Europa sufre un ataque DDoS, la taxonomía de ENISA les ayudaría a clasificar y reportar ese incidente de manera que otras organizaciones puedan entender y aprender de él.
6. **Fuente:** https://www.enisa.europa.eu/publications/reference-incident-classification-taxonomy

### 🔄** ****Ciclo de Respuesta de 27.035** 🔄

1. **Preparación:** 📋 Equiparse con todas las herramientas y protocolos necesarios para activar el playbook.
2. **Identificación:** 🔍 Recoger y analizar toda la información relacionada con el incidente.
3. **Contención:** 🚫 Acciones inmediatas para limitar el daño, por ejemplo, aislando un equipo comprometido de la red.
4. **Remedio:** ⚙️ Implementar soluciones que reparen el daño y prevengan futuras recurrencias.
5. **Recuperación:** 💼 Tomar medidas para restaurar los servicios y sistemas afectados.
6. **Repercusiones:** 📑 Redactar un informe de crisis para ser compartido entre todos los stakeholders.
7. **Mejora Continua:** 🌱 Evaluar y adaptar la respuesta para enfrentar futuras amenazas de manera más eficiente.

![No hay texto alternativo para esta imagen](https://media.licdn.com/dms/image/D4D12AQH5vQAJv50TzA/article-inline_image-shrink_1500_2232/0/1692981412128?e=1714003200&v=beta&t=-1LPAtGK1lAWj03j1THYJLTMkouE_ysU5aTl31QCTXk)

💡** ****¿Qué playbook necesita tu empresa?** 💡

## La respuesta depende en gran medida de la matriz de riesgos que contemple los ciber-riesgos, y que esté alineada con la naturaleza y objetivos del negocio. Es vital iniciar un diálogo interno y definir estrategias en consonancia con las vulnerabilidades y amenazas específicas de tu sector. 📈🤝

## **Conclusiones**

![No hay texto alternativo para esta imagen](https://media.licdn.com/dms/image/D4D12AQH__CWXHZeEgA/article-inline_image-shrink_1500_2232/0/1692978984345?e=1714003200&v=beta&t=NHn3BzI_sar3CnEmAjPmfMKyZbt4t4qSv7a6hEbsci4)

Si bien los playbook no garantizan prevención frente a amenazas inesperadas o nuevos tipos de ataques, sí ofrecen un robusto punto de partida para prevenir** ****"decisiones impulsivas"** en momentos de crisis. Poseer un protocolo definido 📜 potencia las respuestas y agiliza los tiempos de acción. Un gran error es pensar que tu empresa es inmune a cualquier incidente. Tarde o temprano, estos sucesos pueden ocurrir. La clave 🔑 radica en cómo nos preparamos y reaccionamos ante ellos, y cómo nos adaptamos basándonos en lo aprendido.

🌟** ****Ventajas de tener un Playbook de Respuesta a Incidentes:** 🌟

1. **Mejora la Preparación:** 🏋️ ♂️ Un playbook fortalece la preparación de una empresa frente a incidentes o crisis, asegurando que cada integrante sepa exactamente cómo actuar en casos de emergencia, minimizando así el impacto y resolviendo el suceso eficientemente.
2. **Reduce el Tiempo de Respuesta:** ⏱️ Al contar con un playbook, se pueden activar protocolos de acción inmediatamente después de identificar un incidente, agilizando la solución y reduciendo el impacto en la organización.
3. **Potencia la Comunicación:** 📞 El playbook incluye un plan de comunicación que detalla la forma en que se deben notificar a empleados, clientes y stakeholders, garantizando que todos estén informados y puedan gestionar el suceso adecuadamente.
4. **Aumenta la Confianza:** 💪 Al contar con un playbook, se transmite un mensaje de preparación y profesionalismo a empleados y clientes, reforzando su confianza en la capacidad de la organización para manejar crisis.
5. **Cumplimiento de Normativas:** 📜 En algunos contextos, la ley puede requerir que las empresas tengan un plan de respuesta a incidentes. Tener un playbook garantiza el cumplimiento de estas regulaciones, evitando sanciones.

**Recuerda:** La prevención es fundamental, pero la adaptabilidad y la resiliencia definen cómo una organización supera y aprende de los desafíos. 🔄🌐

### Fuentes:

1. [FIRST (Forum of Incident Response and Security Teams)](https://www.first.org/)
2. [SANS Institute](https://www.sans.org/)
3. [GitHub - Buscar playbooks de respuesta a incidentes](https://github.com/)
4. [MITRE ATT&CK](https://attack.mitre.org/)
5. [CERT/CC](https://www.cert.org/)
6. [NIST - Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
7. [CIS (Center for Internet Security)](https://www.cisecurity.org/)
8. [Cybersecurity & Infrastructure Security Agency (CISA)](https://www.cisa.gov/)
9. [Incident Response Consortium](https://www.incidentresponse.com/)
10. [ENISA (European Union Agency for Cybersecurity)](https://www.enisa.europa.eu/)

### Referencias a Playbook:

1. [Incident Response Playbook: Phishing](https://www.incidentresponse.com/playbook/phishing/)
2. [Incident Response Playbook: Ransomware](https://www.incidentresponse.com/playbook/ransomware/)
3. [Incident Response Playbook: Credential Dump](https://www.incidentresponse.com/playbook/credential-dump/)
4. [Incident Response Playbook: Malware Outbreak](https://www.incidentresponse.com/playbook/malware-outbreak/)
5. [Incident Response Playbook: Suspicious Email](https://www.incidentresponse.com/playbook/suspicious-email/)
6. [Incident Response Playbook: Insider Threat](https://www.incidentresponse.com/playbook/insider-threat/)
7. [Incident Response Playbook: DDoS](https://www.incidentresponse.com/playbook/ddos/)
8. [Incident Response Playbook: Web Compromise](https://www.incidentresponse.com/playbook/web-compromise/)
9. [Incident Response Playbook: Lost or Stolen Device](https://www.incidentresponse.com/playbook/lost-or-stolen-device/)
10. [Incident Response Playbook: Unauthorized Access](https://www.incidentresponse.com/playbook/unauthorized-access/)
11. [Incident Response Playbook: Data Breach](https://www.incidentresponse.com/playbook/data-breach/)
12. [Incident Response Playbook: Cloud Compromise](https://www.incidentresponse.com/playbook/cloud-compromise/)
13. [Incident Response Playbook: Account Takeover](https://www.incidentresponse.com/playbook/account-takeover/)
14. [Incident Response Playbook: Suspicious Network Activity](https://www.incidentresponse.com/playbook/suspicious-network-activity/)
15. [Incident Response Playbook: Mobile Device Compromise](https://www.incidentresponse.com/playbook/mobile-device-compromise/)

## Fuente:

* [¿Que es un playbook de respuesta a incidentes - Sebastian Vargas](https://www.linkedin.com/pulse/qu%C3%A9-es-un-playbook-de-respuesta-incidentes-mg-ing-sebasti%C3%A1n-vargas/)

## Recursos:

* Mitre ATT&CK: [https://attack.mitre.org/](https://attack.mitre.org/)
* RE&CT: [https://atc-project.github.io/atc-react/](https://atc-project.github.io/atc-react/)
* RE&CT navigator: [https://atc-project.github.io/react-navigator/](https://atc-project.github.io/react-navigator/)
* Charlas: [https://github.com/aboutsecurity/Talks-and-Presentations](https://github.com/aboutsecurity/Talks-and-Presentations) (hay video tb)
* eBook: [https://github.com/Incidentes/Incident-Response-with-Threat-Intelligence](https://github.com/Incidentes/Incident-Response-with-Threat-Intelligence)

**

![](assets/IS-U311-RecopilacionDeEvidencias2.png)
