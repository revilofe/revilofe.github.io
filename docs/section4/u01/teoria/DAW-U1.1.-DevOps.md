---
title: "UD 1 - 1.1 DevOps y términos relacionados"
description: Introducción a DevOps y sus términos clave
summary: Introducción al perfil DevOps, sus funciones y conceptos asociados como CI/CD.
authors:
    - Eduardo Fdez
date: 2025-09-24
icon:   
permalink: /deaw/unidad1/1.1
categories:
    - DAW
tags:
    - DevOps
    - CI/CD
    - Despliegue
---

## 1.1. DevOps y términos relacionados

### 1. ¿Qué es DevOps?

**DevOps** es la unión de dos mundos que tradicionalmente estaban separados:
- **Dev (Desarrollo):** programadores, que crean aplicaciones.
- **Ops (Operaciones):** administradores de sistemas, que se encargan de que esas aplicaciones funcionen en los servidores.

El objetivo de DevOps es **mejorar la colaboración entre ambos** para que las aplicaciones lleguen más rápido al usuario, con mayor calidad y menos errores.

Un ingeniero o perfil DevOps no solo instala servidores, también:
- Automatiza despliegues.
- Supervisa el rendimiento de aplicaciones.
- Configura sistemas en la nube.
- Define buenas prácticas para asegurar que el software se entrega de forma continua.

En resumen, DevOps busca que los alumnos entiendan **cómo pasar del código en el IDE al software funcionando en un servidor real**.



### 2. ¿Por qué es importante DevOps?

- Porque hoy en día las empresas necesitan **entregar software constantemente** (actualizaciones de apps, parches de seguridad, nuevas funcionalidades).
- Porque evita problemas clásicos como *“en mi ordenador funciona, pero en producción no”*.
- Porque permite que el software sea **más seguro y confiable**.
- Porque prepara al alumnado para un perfil muy demandado en el mercado laboral.



### 3. Términos clave en DevOps

#### 3.1. CI – Integración Continua (*Continuous Integration*)

- Consiste en **unir de forma frecuente** el código de todos los programadores en un repositorio común.
- Cada vez que alguien hace un cambio, el sistema **lanza pruebas automáticas** para comprobar que todo funciona.
- ¿Por qué es importante?
    - Detecta errores pronto.
    - Evita “sorpresas” al final del proyecto.
    - Permite avanzar todos juntos en lugar de que cada uno trabaje aislado.

Ejemplo: al hacer un *push* en GitHub, se ejecutan tests que verifican si el código compila y pasa las pruebas.



#### 3.2. CD – Entrega Continua (*Continuous Delivery*) y Despliegue Continuo (*Continuous Deployment*)

- **Entrega Continua (Continuous Delivery):**  
  El software siempre está listo para ser desplegado. Es decir, en cualquier momento, con un solo clic, podría ponerse en producción.

- **Despliegue Continuo (Continuous Deployment):**  
  Es el siguiente paso: el sistema despliega automáticamente las nuevas versiones en producción sin intervención manual.

¿Para qué sirve?
- Para que los usuarios reciban las mejoras rápidamente.
- Para reducir riesgos: se despliegan cambios pequeños y frecuentes, no “grandes actualizaciones” que pueden fallar.



#### 3.3. Otras prácticas relacionadas

- **Automatización:** scripts y herramientas que evitan repetir tareas manuales.
- **Infraestructura como código (IaC):** configurar servidores y redes con código (por ejemplo, con Ansible o Terraform).
- **Monitorización:** controlar el estado de los servidores y aplicaciones (con Grafana, Prometheus, etc.).
- **Contenedores:** empaquetar aplicaciones con Docker o Kubernetes para que se ejecuten igual en cualquier entorno.



### 4. Conexión con el módulo de Despliegue de Aplicaciones Web

En el módulo vamos a trabajar con:
- **Servidores web y de aplicaciones**, donde desplegar software.
- **Tecnologías de virtualización y contenedores** (como Docker).
- **Control de versiones e integración continua** (Git y GitHub Actions).
- **Documentación y automatización** para que los despliegues sean rápidos, seguros y reproducibles:contentReference[oaicite:0]{index=0}.

Por tanto, conocer DevOps y sus términos es la **base** para entender el resto de unidades del módulo.



## Bibliografía y fuentes
- Humble, J. & Farley, D. *Continuous Delivery*. Addison-Wesley.
- Atlassian: [¿Qué es DevOps?](https://www.atlassian.com/devops)
- Red Hat: [Guía sobre DevOps](https://www.redhat.com/es/topics/devops)
- Normativa oficial módulo **0614. Despliegue de aplicaciones web**:contentReference[oaicite:1]{index=1}  

