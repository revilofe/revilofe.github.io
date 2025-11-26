---
title: "UD 2 - P2: Despliegue de aplicación Temperaturas con Docker"
description: "Despliegue de una aplicación de microservicios con Docker"
summary: "Actividad práctica para desplegar una aplicación de microservicios utilizando redes y variables de entorno en Docker."
authors:
    - Eduardo Fdez
date: 2025-01-12
icon: "material/file-document-edit"
permalink: /daw/unidad2/p2.2
categories:
    - DAW
tags:
    - Docker
    - Microservicios
    - Redes
    - API REST
    - Aplicaciones sin estado
---

## Relación 2.2

### Descripción

**Actividad:** *Despliegue de la aplicación Temperaturas*

En esta práctica desplegarás una aplicación completa basada en **arquitectura de microservicios**. La aplicación Temperaturas permite consultar las temperaturas mínimas y máximas de todos los municipios de España, y está compuesta por dos microservicios independientes que se comunican entre sí.

#### Objetivo general

Aprender a:

- Comprender y desplegar aplicaciones basadas en microservicios.
- Establecer comunicación entre contenedores mediante redes Docker.
- Trabajar con APIs REST en entornos contenerizados.
- Configurar aplicaciones mediante variables de entorno.
- Diferenciar entre aplicaciones con estado y sin estado.

---

### Contexto de trabajo

La aplicación **Temperaturas** es una aplicación de microservicios que consta de dos componentes:

**Microservicio Frontend:**

- Aplicación web desarrollada en Python.
- Proporciona una interfaz web para búsquedas y visualización de resultados.
- Realiza peticiones HTTP al microservicio backend.
- Escucha en el puerto 3000/tcp.
- Imagen Docker: `iesgn/temperaturas_frontend`

**Microservicio Backend:**

- API REST que proporciona datos sobre municipios y temperaturas.
- Escucha en el puerto 5000/tcp.
- Imagen Docker: `iesgn/temperaturas_backend`

**Comunicación entre microservicios:**

El frontend se conecta al backend utilizando el nombre `temperaturas-backend`. Esta comunicación se realiza internamente en la red Docker, sin necesidad de exponer el backend al exterior.

---

### 🔹 Parte 1: Despliegue básico de la aplicación

#### Tarea 1.1: Preparación del entorno

1. Crea una red Docker personalizada llamada `red_temperaturas` para la comunicación entre los microservicios.

2. Investiga en Docker Hub la documentación de las imágenes:
   
    - `iesgn/temperaturas_backend`
    - `iesgn/temperaturas_frontend`
   
    Identifica qué puertos utilizan y qué variables de entorno están disponibles.

#### Tarea 1.2: Despliegue del microservicio backend

1. Despliega el contenedor del microservicio backend con las siguientes características:
   
    - Nombre del contenedor: `temperaturas-backend`
    - Conectado a la red `red_temperaturas`
    - Ejecutando en modo daemon (segundo plano)

2. Verifica que el contenedor está en ejecución.

3. Inspecciona el contenedor para identificar su dirección IP dentro de la red.

#### Tarea 1.3: Despliegue del microservicio frontend

1. Despliega el contenedor del microservicio frontend con las siguientes características:
   
    - Nombre del contenedor: `temperaturas-frontend`
    - Conectado a la red `red_temperaturas`
    - Puerto 80 del host mapeado al puerto 3000 del contenedor
    - Ejecutando en modo daemon

2. Accede a la aplicación desde tu navegador web (http://localhost).

3. Realiza varias búsquedas de municipios y verifica que la aplicación muestra correctamente las temperaturas.

#### Tarea 1.4: Análisis de la comunicación entre microservicios

1. Desde el contenedor frontend, realiza un ping al contenedor backend usando su nombre.

2. Verifica que la resolución DNS funciona correctamente.

3. Comprueba que el frontend puede acceder al puerto 5000 del backend.

---

### 🔹 Parte 2: Aplicaciones sin estado

#### Tarea 2.1: Comprensión del concepto

La aplicación Temperaturas es una **aplicación sin estado** (*stateless*). Esto significa que no necesita almacenar datos de forma persistente para su funcionamiento.

1. Detén y elimina ambos contenedores.

2. Vuelve a crear ambos contenedores con la misma configuración.

3. Accede a la aplicación y verifica que funciona exactamente igual que antes.

4. Reflexiona sobre las ventajas de las aplicaciones sin estado en arquitecturas de microservicios.

---

### 🔹 Parte 3: Configuración personalizada

#### Tarea 3.1: Cambio del nombre del backend

El microservicio frontend utiliza una variable de entorno llamada `TEMP_SERVER` para saber cómo conectarse al backend. Por defecto, su valor es `temperaturas-backend:5000`.

1. Elimina los contenedores anteriores (mantén la red).

2. Crea un nuevo contenedor backend con el nombre `api-temperaturas` (en lugar de `temperaturas-backend`).

3. Despliega el contenedor frontend configurando la variable de entorno `TEMP_SERVER` para que apunte al nuevo nombre del backend (incluyendo el puerto).

4. Verifica que la aplicación funciona correctamente con esta nueva configuración.

#### Tarea 3.2: Cambio del puerto del backend

1. Elimina los contenedores anteriores.

2. Crea un nuevo contenedor backend:
   
    - Nombre: `temperaturas-backend`
    - Mapea el puerto 5000 del contenedor a otro puerto del host (por ejemplo, 5500)

3. Despliega el contenedor frontend con la configuración necesaria para que pueda conectarse al backend en su nuevo puerto.

4. Verifica el funcionamiento de la aplicación.

---

### 🔹 Parte 4: Análisis y documentación

#### Tarea 4.1: Análisis de la arquitectura de microservicios

Responde a las siguientes preguntas en tu documentación:

1. **Microservicios:**
   
    - ¿Qué ventajas ofrece separar la aplicación en dos microservicios (frontend y backend)?
    - ¿Cómo se comunican los microservicios entre sí?
    - ¿Qué pasaría si el microservicio backend fallara?

2. **Aplicaciones sin estado:**
   
    - ¿Qué significa que una aplicación sea "sin estado"?
    - ¿Qué ventajas tiene este tipo de aplicaciones en entornos contenerizados?
    - ¿Qué diferencias existen con la aplicación Guestbook (que sí tiene estado)?

3. **API REST:**
   
    - ¿Qué es una API REST?
    - ¿Por qué el backend se implementa como una API REST?
    - ¿Qué tipo de peticiones HTTP crees que realiza el frontend al backend?

4. **Aislamiento y seguridad:**
   
    - ¿Por qué no es necesario exponer el puerto del backend al host?
    - ¿Qué ventajas de seguridad ofrece esta configuración?
    - ¿En qué casos sería necesario exponer el backend?


#### Tarea 4.2: Comandos utilizados

Documenta todos los comandos Docker que has utilizado para:

- Crear la red
- Crear y gestionar los contenedores frontend y backend
- Verificar la comunicación entre contenedores
- Inspeccionar la configuración de red
- Probar la conectividad entre microservicios

---

### 🔹 Parte 5 (opcional): Exploración de la API

#### Tarea 5.1: Acceso directo a la API

1. Expón el puerto del backend al host.

2. Utiliza herramientas como `curl`, Postman o el navegador para realizar peticiones directas a la API del backend.

3. Identifica al menos 3 endpoints diferentes de la API.

4. Documenta las respuestas obtenidas y el formato de los datos (probablemente JSON).

---

## Entregables

1. **Documentación en formato Markdown** que incluya:
   
    - Comandos utilizados en cada tarea con explicación
    - Capturas de pantalla que demuestren:
        - La aplicación funcionando en el navegador
        - Búsquedas de diferentes municipios
        - La lista de contenedores en ejecución
        - La inspección de la red Docker
        - Pruebas de conectividad entre microservicios
    - Respuestas a las preguntas de análisis de la Parte 4
    - Comparación con la aplicación Guestbook (similitudes y diferencias)

2. **(Opcional)** Documentación de la exploración de la API si realizas la Parte 5.1.


---

### Evaluación

Se evaluará:

- La correcta implementación de la arquitectura de microservicios.
- El funcionamiento completo de la aplicación.
- La demostración de comunicación entre microservicios.
- La comprensión de conceptos de aplicaciones sin estado.
- La claridad y precisión de la documentación.
- Las respuestas al análisis técnico.
- La comparación entre diferentes arquitecturas de aplicaciones.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Docker: [https://docs.docker.com](https://docs.docker.com)
- Networking en Docker: [https://docs.docker.com/network/](https://docs.docker.com/network/)
- Variables de entorno: [https://docs.docker.com/engine/reference/commandline/run/#env](https://docs.docker.com/engine/reference/commandline/run/#env)
- Arquitectura de microservicios: [https://microservices.io/](https://microservices.io/)
- API REST: [https://restfulapi.net/](https://restfulapi.net/)
- Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

