# U1.1 - DevOps

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---  

## Índice

---

## 1. ¿Qué es DevOps?


### 1.1. Definición

* DevOps unifica el desarrollo de software (Dev) y las operaciones de TI (Ops).
* Es un conjunto de prácticas, herramientas y una filosofía cultural.
* Tradicionalmente Dev y Ops trabajaban separados.
* **Dev:** desarrollan y prueban el código.
* **Ops:** despliegan y mantienen aplicaciones en servidores.

Note: DevOps rompe la barrera entre desarrollo y operaciones, permitiendo colaboración fluida entre ambos equipos.


### 1.2. Objetivo de DevOps

* Mejorar la colaboración entre desarrolladores y administradores.
* Entregar aplicaciones más rápido al usuario.
* Aumentar la calidad del software.
* Reducir errores en producción.
* Agilizar el ciclo de vida del desarrollo.

Note: El objetivo principal es acelerar el flujo desde el código en desarrollo hasta el software funcionando en producción.


### 1.3. Funciones del perfil DevOps

* Automatiza despliegues de aplicaciones.
* Supervisa el rendimiento de sistemas.
* Configura infraestructura en la nube.
* Define buenas prácticas para CI/CD.
* Garantiza entrega continua de software.

Note: Un ingeniero DevOps no solo instala aplicaciones, sino que automatiza y mejora todo el proceso de entrega de software.

---

## 2. Importancia de DevOps


### 2.1. ¿Por qué es importante?

* Las empresas necesitan entregar software constantemente.
* Evita el problema: "en mi ordenador funciona, pero en producción no".
* Reduce errores humanos mediante automatización.
* Hace el software más seguro y confiable.
* Facilita la colaboración entre equipos.

Note: DevOps responde a la necesidad del mercado de actualizaciones frecuentes, parches de seguridad y nuevas funcionalidades.


### 2.2. Beneficios clave

* Agiliza la entrega de valor al cliente.
* Mejora la calidad del código.
* Aumenta la productividad del equipo.
* Perfil muy demandado en el mercado laboral.
* Permite responder rápido a cambios del negocio.

Note: DevOps se ha convertido en estándar en la industria, siendo uno de los perfiles más demandados actualmente.

---

## 3. Términos clave en DevOps


### 3.1. CI – Integración Continua

* **Continuous Integration (CI):** Integrar código frecuentemente.
* Cada cambio se integra en un repositorio común.
* Se lanzan pruebas automáticas tras cada cambio.
* Solo se integra si pasa las pruebas.
* Detecta errores temprano en el desarrollo.

Note: CI evita sorpresas al final del proyecto y permite a todos los desarrolladores avanzar juntos en lugar de trabajar aislados.


### 3.2. Ventajas de CI

* Evita conflictos de integración grandes.
* Reduce tiempo de detección de errores.
* Mejora la calidad del código.
* Facilita el trabajo en equipo.
* Ejemplo: ejecutar tests al hacer push en GitHub.

Note: CI es fundamental para mantener la calidad del código cuando múltiples desarrolladores trabajan simultáneamente.


### 3.3. CD – Entrega Continua

* **Continuous Delivery:** El software siempre está listo para desplegarse.
* Con un clic puede ponerse en producción.
* El despliegue puede ser manual o automatizado.
* El equipo decide cuándo hacer el despliegue.
* Reduce riesgos con cambios pequeños y frecuentes.

Note: La Entrega Continua garantiza que siempre hay una versión estable lista para producción.


### 3.4. CD – Despliegue Continuo

* **Continuous Deployment:** Despliegue automático en producción.
* Sin intervención manual del equipo.
* Cada cambio que pasa las pruebas se despliega automáticamente.
* Los usuarios reciben mejoras rápidamente.
* Mayor automatización que Continuous Delivery.

Note: El Despliegue Continuo es el nivel más avanzado de automatización en CI/CD.

---

## 4. Pipeline CI/CD


### 4.1. Etapas del Pipeline

![Pipeline DevOps](assets/DAW-U1.1.-DevOps-CicloVida.png)

Note: Un pipeline CI/CD es el flujo automatizado que va desde el código fuente hasta la producción.


### 4.2. Etapa: Code y Commit

* **Code:** Escritura del código fuente.
* Desarrolladores implementan nuevas funciones.
* Corrección de errores existentes.
* **Related Code:** Código relacionado que debe actualizarse.
* **Commit:** Guardar cambios en el control de versiones (Git).

Note: El commit marca el punto de partida que activa el pipeline automatizado.


### 4.3. CI Pipeline

* **Build:** Compilación del código fuente.
* Asegura que todo se une correctamente.
* **Unit Tests:** Pruebas unitarias de componentes.
* **Integration Tests:** Verificar interacción entre módulos.
* Valida dependencias y comunicación.

Note: El CI Pipeline valida que el código funciona correctamente antes de avanzar al despliegue.


### 4.4. CD Pipeline

* **Review:** Validación manual o automática.
* Asegura cumplimiento de estándares de calidad.
* **Staging:** Despliegue en entorno de pruebas.
* Simula el entorno de producción.
* **Production:** Despliegue final para usuarios.

Note: El CD Pipeline garantiza un despliegue controlado y seguro en producción.

---

## 5. Prácticas relacionadas


### 5.1. Automatización

* Scripts y herramientas para evitar tareas manuales.
* Reduce errores humanos.
* Aumenta la velocidad de entrega.
* Libera tiempo del equipo para tareas de mayor valor.
* Permite reproducibilidad y consistencia.

Note: La automatización es el pilar fundamental de DevOps para lograr eficiencia.


### 5.2. Infraestructura como Código (IaC)

* Configurar servidores y redes con código.
* Herramientas: Ansible, Terraform.
* Versionado de la infraestructura.
* Despliegues reproducibles.
* Facilita la escalabilidad.

Note: IaC permite tratar la infraestructura con las mismas prácticas que el código de aplicación.


### 5.3. Monitorización

* Controlar el estado de servidores y aplicaciones.
* Herramientas: Grafana, Prometheus.
* Detectar problemas proactivamente.
* Optimizar rendimiento.
* Recopilar métricas para mejora continua.

Note: La monitorización permite detectar y resolver problemas antes de que afecten a los usuarios.


### 5.4. Contenedores

* Empaquetar aplicaciones con sus dependencias.
* Herramientas: Docker, Kubernetes.
* Ejecución consistente en cualquier entorno.
* Facilita el despliegue y escalado.
* Aislamiento entre aplicaciones.

Note: Los contenedores resuelven el problema de "funciona en mi máquina" al garantizar consistencia entre entornos.

---

## 6. Conexión con el módulo


### 6.1. Temas a trabajar

* Servidores web y de aplicaciones.
* Tecnologías de virtualización y contenedores (Docker).
* Control de versiones e integración continua (Git, GitHub Actions).
* Documentación y automatización de despliegues.
* Despliegues rápidos, seguros y reproducibles.

Note: Este módulo se centra en las prácticas y herramientas DevOps aplicadas al despliegue de aplicaciones web.


### 6.2. Base del módulo

* DevOps es la base para todo el módulo.
* Conocer estos conceptos es fundamental.
* Se aplicarán en todas las unidades siguientes.
* Perfil profesional muy demandado.
* Habilidades esenciales para el mercado laboral actual.

Note: Dominar DevOps abre muchas oportunidades profesionales en el desarrollo de software moderno.

---

## Bibliografía

* Humble, J. & Farley, D. Continuous Delivery. Addison-Wesley.
* Atlassian: ¿Qué es DevOps?
* Red Hat: Guía sobre DevOps

Note: Se recomienda consultar estas fuentes para profundizar en los conceptos de DevOps.
