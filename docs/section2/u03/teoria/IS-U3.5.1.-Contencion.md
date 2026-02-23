---
title: "UD 3 - 3.5.1 Contención de incidentes: medidas y estrategias"
description: "Apuntes didácticos sobre contención en respuesta a incidentes: objetivos, estrategias, playbooks, decisiones y checklist técnico-organizativo para alumnado de ciberseguridad."
summary: "Guía de contención: qué es, cuándo aplicarla, cómo decidir entre contención a corto/largo plazo y cómo ejecutarla por escenarios y por capas."
authors:
    - Eduardo Fdez
date: 2026-02-23
icon: "material/file-document-outline"
permalink: /is/unidad-3/3.5.1-contencion-de-incidentes
categories:
    - "Incidentes de seguridad"
tags:
    - "Incidentes"
    - "Contención"
    - "Respuesta"
    - "Ciberresiliencia"
    - "Playbooks"
    - "Ransomware"
---

## 3.5.1. Contención de incidentes: medidas y estrategias

En esta parte vamos a centrarnos en **la contención**: el conjunto de acciones que se aplican para **frenar un incidente** y evitar que su impacto aumente.

Este tema está directamente alineado con:

- **RA3 (CE 3.e)**: iniciar las primeras medidas de contención para limitar daños.

!!! definition "Definición"
    La contención es el conjunto de medidas que **limitan el alcance** de un incidente, reducen su propagación y cortan la capacidad del atacante de seguir actuando, **sin perder de vista la evidencia** y el impacto en negocio.

### 1. Objetivos de la contención

La contención persigue objetivos muy concretos (y evaluables):

1. **Parar el “sangrado”**: detener propagación, exfiltración o cifrado.

    En la practica suele ser lo primero: si el incidente sigue “en marcha”, cada minuto puede aumentar el impacto. Un ejemplo claro es el ransomware: si hay cifrado activo, el objetivo es **pararlo ya** para que no afecte a mas equipos.

2. **Reducir superficie de ataque**: limitar movimiento lateral y accesos.

    Esto implica que el atacante tenga menos “caminos” para avanzar: menos rutas de red, menos privilegios, menos servicios accesibles, menos credenciales validas. Si no reduces superficie, puede que “contengas” un equipo, pero el atacante siga moviendose por otros.

3. **Comprar tiempo** para investigar con rigor.

    La contención **no resuelve** el incidente, pero te permite ganar aire para analizar evidencias, delimitar alcance y preparar erradicación y recuperación sin ir “a ciegas”.

4. **Proteger activos criticos**: identidad, copias de seguridad, servicios esenciales.

    Hay activos que, si caen, empeoran todo: por ejemplo, la identidad (AD/SSO), los repositorios de backups o el plano de gestion (hypervisor, EDR, herramientas de despliegue). Contener tambien es **blindar** esos puntos.

5. **Preservar evidencia** cuando sea necesario (sobre todo evidencias volatiles).

    En incidentes reales, un cierre brusco puede eliminar conexiones, procesos y datos de memoria que son clave para entender el vector de entrada o la persistencia. Por eso, muchas veces se captura “lo minimo viable” antes de aislar.

Una idea importante (y muy repetida en guias de respuesta a incidentes) es que la contención sirve para **limitar impacto** y, a la vez, permitir que el equipo trabaje con informacion suficiente para erradicar y recuperar con criterio.

!!! tip "Idea para alumnado"
    Contener no es “arreglar” el incidente. Es **poner el freno** para que el problema no crezca mientras investigáis y preparáis erradicación y recuperación.

### 2. Contención a corto plazo y a largo plazo

Una forma muy práctica (y realista) de explicarlo es separar dos estrategias:

- **Contención a corto plazo (táctica)**: acciones inmediatas para frenar el impacto ya.
- **Contención a largo plazo (estratégica)**: acciones para sostener el control mientras se investiga y evitar recaídas.

| Tipo de contención        | Objetivo                           |     Horizonte | Riesgo típico                               | Ejemplos                                           |
|---------------------------|------------------------------------|--------------:|---------------------------------------------|----------------------------------------------------|
| Corto plazo (táctica)     | Parar el daño inmediatamente       | Minutos-horas | Cortar demasiado y tumbar servicios         | Aislar host, bloquear IoC, deshabilitar cuenta     |
| Largo plazo (estratégica) | Evitar reentrada y mejorar postura |  Días-semanas | Ser demasiado lenta y permitir persistencia | Segmentación, MFA, rotación de secretos, hardening |

!!! example "Ejemplo rapido"
    Si detectas un equipo que hace conexiones a un dominio malicioso:
    
    - Corto plazo: aislas el equipo y bloqueas el dominio en proxy/DNS.
    - Largo plazo: revisas por que pudo salir esa conexion (reglas de salida, EDR, parches, privilegios) y endureces controles para que no vuelva a pasar.

### 3. Principios de oro antes de “tocar botones”

Hay cinco principios que debéis interiorizar (porque son los que evitan desastres):

- **Evidencia primero (cuando aplique)**: si vais a perder memoria, conexiones o procesos, hay que valorar captura rápida.

    En muchos casos la evidencia mas valiosa es volatil: conexiones activas, procesos en ejecucion, credenciales en memoria, etc. Por eso, antes de “apagar por si acaso”, pensad: ¿voy a perder datos que necesito para entender el vector de entrada o la persistencia?

- **Rapidez con cabeza**: contención improvisada puede multiplicar el incidente.

    Contener rapido no es “hacer cosas al azar”. Es aplicar un plan: aislar, bloquear, rotar credenciales, registrar acciones y seguir un playbook. Si no, puedes dejar agujeros (por ejemplo, aislas un equipo pero el atacante sigue con las mismas credenciales en otros).

- **Menor impacto posible**: frenar sin romper lo crítico.

    La contención es un equilibrio entre seguridad y continuidad. Si cortas demasiado, puedes tumbar un servicio esencial y crear un incidente “doble”: el de seguridad y el de disponibilidad. Por eso se prioriza: activos criticos primero, y medidas reversibles cuando se pueda.

- **Cortar el acceso del atacante**: si no cortáis credenciales/tokens, el atacante vuelve.

    Un patron muy comun es contener un equipo pero no la identidad: el atacante conserva sesion, token, VPN o una cuenta de servicio, y reentra en cuanto puede. Si hay sospecha de compromiso de credenciales, la contención debe incluir identidad.

- **Comunicación y escalado**: la contención es técnica, pero también organizativa.

    Durante contención, la dirección y el negocio piden respuestas. Es normal. Lo importante es comunicar **hechos y siguientes pasos**, sin especular. Dar una conclusion prematura “para tranquilizar” suele empeorar la situacion mas tarde.

!!! warning "Atención"
    “Apago el servidor y listo” puede ser una contención… pero también puede ser:
    
    - una pérdida de evidencia,
    - una caída de negocio innecesaria,
    - y un examen suspendido por no documentar ni justificar.

### 4. Flujo de decisión: ¿qué contengo y cómo?

“¿Qué hago primero?”. La respuesta correcta es: depende, pero con un flujo claro.

```mermaid
flowchart TD
    A[Detectáis comportamiento anómalo] --> B{¿Hay daño activo?}
    B -- Sí: cifrado/exfiltración/propagación --> C[Contención táctica inmediata]
    B -- No: sospecha/incertidumbre --> D[Preservar evidencia mínima]
    D --> E[Contención selectiva]
    C --> F{¿Evidencia volátil crítica?}
    F -- Sí --> D
    F -- No --> G[Reducir superficie: bloquear IoC / aislar]
    E --> H[Investigar: alcance y vector]
    G --> H
    H --> I{¿Hay compromiso de identidad?}
    I -- Sí --> J[Cortar acceso: cuentas, tokens, MFA]
    I -- No --> K[Contención por capa: red/endpoint/servicio]
    J --> L[Plan de contención a largo plazo]
    K --> L
```

!!! note "Nota"
    En clase, este flujo se puede usar como guion de role-play:
    
    ```
    - un grupo hace de SOC,
    - otro de sistemas,
    - otro de dirección,
    - y alguien (siempre hay alguien) de “usuario que lo abrió todo”.
    ```

#### 4.1. Indicadores, alcance y cuarentena (lo que suele marcar la diferencia)

En contención hay una idea muy potente: **no basta con “ver el sintoma”**, hay que usarlo para descubrir el resto del incidente.

1. **Identificar indicadores (IoC)**.

    Los indicadores de compromiso (IoC) son “pistas” observables: hash de un binario, una clave de registro, un servicio nuevo, una URL maliciosa, conexiones a un dominio concreto, etc. Con una lista inicial de IoC puedes buscar en el resto del entorno para descubrir otros equipos afectados.

2. **Delimitar la población afectada**.

    El objetivo es responder a: ¿qué equipos, cuentas y servicios están tocados? Si solo aislas el primer equipo detectado (el “paciente 0”) y no buscas mas, es facil que el atacante ya se haya movido lateralmente.

3. **Poner en cuarentena de forma segura**.

    Aislar no siempre significa apagar. Opciones tipicas (segun el escenario) son:
    
    - desconectar red (por ejemplo, cable o puerto switch),
    - aislar con reglas (DNS, firewall, ACL),
    - o cuarentena desde EDR.
    
    Si necesitas evidencia volatil, valora primero una captura rapida y luego aisla.

4. **Preservar evidencia con imagenes cuando aplique**.

    Cuando el objetivo es investigar con rigor, se suelen tomar imagenes (disco y, a veces, memoria) para analizarlas sin “pisar” el sistema original. Esto es mas facil cuando hay playbooks y herramientas listas, porque el tiempo durante un incidente es oro.

### 5. Catálogo de medidas de contención por capas

Para que os resulte aplicable en laboratorio, agrupamos por capas: red, identidad, endpoint y servicios.

#### 5.1. Red

* **Segmentación / cuarentena** (VLAN, ACL, microsegmentación).
* **Bloqueo de IoC** en firewall/proxy/DNS (IPs, dominios, URLs).
* **Corte de rutas** entre segmentos para limitar movimiento lateral.
* **Limitación de egress** (salida a Internet) a lo estrictamente necesario.

MITRE define la segmentación como control para limitar flujo y restringir movimiento lateral. ([attack.mitre.org][1])

#### 5.2. Identidad

* **Deshabilitar cuentas comprometidas** y cortar sesiones activas.
* **Reset forzado de contraseñas** y rotación de credenciales privilegiadas.
* **Revocar tokens** (SSO/OAuth), claves API y secretos de servicios.
* **Aplicar MFA** (especialmente en cuentas de administración).

#### 5.3. Endpoint (equipos)

* **Aislamiento desde EDR** o cuarentena por red.
* **Bloqueo por hash** / firma / regla (si se dispone).
* **Detención controlada de procesos** maliciosos (si no compromete evidencia).
* **Deshabilitar ejecución** de macros o binarios sospechosos temporalmente.

#### 5.4. Servicios y aplicaciones

* Poner un servicio en **modo mantenimiento** (siempre coordinado).
* **Rotación de secretos** de despliegue y acceso a base de datos.
* Activación temporal de **reglas WAF** o rate-limiting.
* Deshabilitar funcionalidades expuestas hasta parcheo.


### 6. Contención por escenarios: mini playbooks

Un playbook es un procedimiento predefinido. En RA4 se espera que existan procedimientos detallados.

#### 6.1. Ransomware (cifrado y posible extorsión)

CISA recomienda una combinación de prevención y respuesta, incluyendo aislamiento y checklist de respuesta. ([cisa.gov][2])
NCSC mantiene guías específicas para mitigar malware y ransomware. ([ncsc.gov.uk][3])

**Contención táctica (minutos-horas):**

1. Aislar equipos afectados (EDR / VLAN cuarentena / desconectar red).
2. Proteger backups: evitar acceso desde cuentas comprometidas.
3. Cortar credenciales comprometidas (usuarios y admins).
4. Bloquear IoC conocidos (dominios/IP) si se identifican.
5. Registrar acciones y preservar evidencia mínima si es viable.

**Contención estratégica (días):**

* Segmentación para frenar movimiento lateral.
* MFA y endurecimiento de accesos remotos.
* Revisión de privilegios y cuentas de servicio.

#### 6.2. Compromiso de credenciales (phishing / password spraying)

**Contención táctica:**

1. Deshabilitar cuentas sospechosas y revocar sesiones.
2. Reset forzado + activar MFA.
3. Revisar reglas de reenvío y accesos a correo (si aplica).
4. Bloquear origen si hay fuerza bruta evidente.

**Contención estratégica:**

* Acceso condicional, PAM, mínimo privilegio, detección de anomalías.

#### 6.3. Web comprometida (webshell / defacement)

**Contención táctica:**

1. Sacar el servicio de Internet o poner mantenimiento (coordinado).
2. Copiar logs, artefactos web y evidencias de integridad.
3. Rotar secretos (API keys, credenciales DB, despliegue).
4. Bloquear rutas, IoC y revisar persistencia.

**Contención estratégica:**

* WAF, hardening, parcheo, pipeline seguro y control de cambios.

#### 6.4. Exfiltración / C2

**Contención táctica:**

1. Bloquear comunicaciones C2 (proxy/firewall/DNS).
2. Aislar hosts implicados.
3. Preservar evidencias de red (logs, proxy, DNS).

**Contención estratégica:**

* Control de salida (egress), DLP si aplica, segmentación y mejora de detecciones.


### 7. Matriz de decisiones: “contener mucho” vs “contener fino”

| Decisión                                   | Ventaja            | Riesgo                           | Cuándo usar                                        |
|--------------------------------------------|--------------------|----------------------------------|----------------------------------------------------|
| Contención agresiva (corte amplio)         | Detiene rápido     | Tumbar negocio, perder evidencia | Daño activo grave (cifrado/exfiltración)           |
| Contención selectiva (quirúrgica)          | Menos impacto      | Puede dejar persistencia         | Incidente localizado, alta criticidad del servicio |
| Contención “por identidad” (cortar acceso) | Corta reentrada    | Impacto en usuarios              | Compromiso de credenciales o sospecha fuerte       |
| Contención “por red” (segmentar)           | Limita lateralidad | Compleja de diseñar              | Entornos medianos/grandes o incidentes recurrentes |

!!! success "Indicador de madurez"
    Una organización madura no improvisa: tiene playbooks, segmentación razonable y un flujo de escalado claro.


### 8. Errores típicos (lo que no debéis hacer)

1. **Formatear o reinstalar sin investigar**: destruye evidencia y no aprendéis nada.
2. **Aislar solo el “paciente 0”** cuando ya hay movimiento lateral.
3. **No cortar credenciales**: el atacante vuelve.
4. **Bloquear IoC a ciegas** y dejar fuera a usuarios o servicios legítimos.
5. **No documentar**: en un incidente real y en el módulo, si no está registrado, no existe.


### 9. Checklist de contención (primeros 30–60 minutos)

1. Identificar alcance inicial (sistemas, cuentas, servicios).
2. Valorar evidencia volátil (si procede): ¿se pierde si apagáis/aisláis?
3. Aislar sistemas afectados con el menor impacto posible.
4. Cortar accesos del atacante (cuentas/tokens/secretos).
5. Bloquear IoC (red/EDR/proxy/DNS) si se conocen.
6. Proteger backups y activos críticos.
7. Escalar y comunicar según procedimiento.
8. Documentar: qué, cuándo, quién, por qué.

CISA publica listas y guías de respuesta para ransomware que incluyen checklist y acciones recomendadas. ([cisa.gov][2])


### 10. Actividades de aula recomendadas

A continuación, actividades pensadas para que alumnos y alumnas practiquéis contención de forma realista:

1. **Caso guiado: aislamiento sin perder evidencia**

    * Objetivo: decidir qué capturar antes de aislar.
    * Evidencias: logs + tabla de acciones.

2. **Diseño de segmentación mínima viable**

    * Objetivo: proponer segmentos, justificar flujos permitidos y prohibidos.
    * Referencia conceptual: segmentación como mitigación. ([attack.mitre.org][1])

3. **Playbook de ransomware**

    * Objetivo: redactar procedimiento corto/largo plazo y roles.
    * Referencia: guía StopRansomware. ([cisa.gov][2])

4. **Simulación de war room**

    * Objetivo: aplicar escalado, comunicación, decisiones y registro.
    * Entrega: acta de decisiones + timeline.


## Glosario mínimo

* **IoC (Indicator of Compromise)**: indicador observable de posible compromiso.
* **EDR**: solución de detección y respuesta en endpoint.
* **C2 (Command & Control)**: infraestructura de mando y control del atacante.
* **Segmentación**: dividir la red en segmentos para limitar movimiento lateral. ([attack.mitre.org][1])
* **Token**: credencial temporal (SSO/OAuth) que permite acceso sin contraseña.

## Referencias y bibliografía

* Normativa del módulo, RA3 y RA4 (contención, procedimientos y escalado).
* NIST SP 800-61 Rev. 3: recomendaciones de respuesta a incidentes integradas con gestión de riesgo. ([csrc.nist.gov][4])
* CISA #StopRansomware Guide (guía y checklist de respuesta). ([cisa.gov][2])
* UK NCSC: mitigación de malware y ransomware (guía práctica). ([ncsc.gov.uk][3])
* MITRE ATT&CK Mitigation M1030: Network Segmentation. ([attack.mitre.org][1])

## Presentación

Puedes acceder a la presentación de esta unidad aquí:

[Presentación IS-U3.3 - Contención de incidentes](https://revilofe.github.io/slides/section2-is/IS-U3.3.-ContencionDeIncidentes.html)

## Recursos adicionales

* Plantilla de playbook (para completar en clase): objetivos, pasos, roles, evidencias y checklist.
* Tabla de “acciones vs impacto” para debatir contención selectiva frente a agresiva.


[1]: https://attack.mitre.org/mitigations/M1030/?utm_source=chatgpt.com "Network Segmentation, Mitigation M1030 - Enterprise"
[2]: https://www.cisa.gov/stopransomware/ransomware-guide?utm_source=chatgpt.com "StopRansomware Guide"
[3]: https://www.ncsc.gov.uk/guidance/mitigating-malware-and-ransomware-attacks?utm_source=chatgpt.com "Mitigating malware and ransomware attacks - NCSC.GOV.UK"
[4]: https://csrc.nist.gov/pubs/sp/800/61/r3/final?utm_source=chatgpt.com "SP 800-61 Rev. 3, Incident Response Recommendations and ..."
