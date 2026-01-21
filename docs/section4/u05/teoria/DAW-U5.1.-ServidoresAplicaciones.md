---
title: "UD 5 - 5.1 Servidores de aplicaciones"
description: Conceptos, arquitectura y despliegue en servidores de aplicaciones, con foco en RA3.
summary: Servidores de aplicaciones, despliegue, JavaEE, Node.js, buenas practicas y CI/CD.
authors:
    - Eduardo Fdez
date: 2025-02-01
icon: "material/file-document-outline"
permalink: /daw/unidad5/5.1
categories:
    - DAW
tags:
    - Servidores de aplicaciones
    - Despliegue
    - JavaEE
    - Node.js
    - CI/CD
---

## 5.1. Servidores de aplicaciones

En la unidad 3 vimos la base de las arquitecturas web, el protocolo HTTP y los servidores web. En esta unidad damos un paso mas: trabajamos con **servidores de aplicaciones**, su papel en la arquitectura, su configuracion y el despliegue seguro de aplicaciones, alineado con el **RA3** del modulo.

### 1. Resultado de aprendizaje y criterios de evaluacion (RA3)

El **RA3** establece que el alumnado debe ser capaz de implantar aplicaciones web en servidores de aplicaciones, configurarlas con seguridad y documentar el proceso.

#### 1.1. Criterios de evaluacion asociados

- a) Describir componentes y funcionamiento de los servicios del servidor.
- b) Identificar archivos principales de configuracion y bibliotecas compartidas.
- c) Configurar cooperacion con el servidor web.
- d) Activar mecanismos de seguridad del servidor de aplicaciones.
- e) Configurar y usar componentes web del servidor de aplicaciones.
- f) Ajustar parametros necesarios para el despliegue.
- g) Probar funcionamiento y rendimiento de la aplicacion.
- h) Elaborar documentacion de administracion y recomendaciones.
- i) Usar virtualizacion, nube o contenedores en el despliegue.

!!! info "Relacion con la unidad 3"
    En la unidad 3 ya tratamos servidores web, despliegue y seguridad basica. Aqui ampliamos esos conceptos con **servidores de aplicaciones** y un enfoque practico en **configuracion, seguridad y pruebas**.

### 2. Concepto y papel del servidor de aplicaciones

#### 2.1. Definicion y ubicacion en la arquitectura

Un servidor de aplicaciones es una plataforma software que permite **ejecutar aplicaciones web** y ofrecer servicios adicionales al servidor web, como gestion de sesiones, seguridad, transacciones, recursos compartidos y logs.

Suele situarse entre el servidor web y el servidor de bases de datos, actuando como intermediario para procesar **logica de negocio** y peticiones dinamicas.

<figure markdown>
  ![](../assets/application-server1.webp)
  <figcaption>Ubicacion del servidor de aplicaciones en una arquitectura clasica.</figcaption>
</figure>

#### 2.2. Terminologia basica

Esta terminología la usaremos durante la unidad:

| Termino           | Descripcion                                           |
|-------------------|-------------------------------------------------------|
| Servidor web      | Sirve contenido estatico y gestiona peticiones HTTP.  |
| Cliente web       | Navegador o app que solicita recursos.                |
| HTTPS             | Protocolo seguro entre cliente y servidor.            |
| JSON              | Formato de intercambio de datos entre servicios.      |
| Logica de negocio | Reglas del dominio y procesamiento de datos.          |
| Aplicacion        | Software que consume datos y los presenta al usuario. |

#### 2.3. Por que necesitamos servidores de aplicaciones

Los servidores web son ligeros y eficientes para contenido estático, pero **las peticiones dinámicas** requieren mas potencia y servicios avanzados. El servidor de aplicaciones aporta:

- Ejecución de lógica de negocio.
- Gestion de sesiones y usuarios.
- Pools de conexiones y recursos compartidos.
- Transacciones distribuidas y servicios de mensajeria.
- Diagnostico, registros y seguridad avanzada.

#### 2.4. Optimización del tráfico y seguridad

El servidor de aplicaciones mejora el rendimiento y reduce riesgos al separar el trafico dinámico del estático. Tambien añade una capa extra de protección frente a ataques, ya que las peticiones llegan filtradas antes de tocar los datos sensibles.

<figure markdown>
  ![](../assets/serv_apl.png)
  <figcaption>Servidor de aplicaciones como capa de seguridad y control.</figcaption>
</figure>

### 3. Funcionamiento general en una arquitectura web

En esta sección vemos como interactúan el servidor web y el servidor de aplicaciones en una arquitectura web típica.

#### 3.1. Flujo de peticiones en un servidor Java

En un servidor JavaEE, el flujo tipico es este:

1. El cliente abre un navegador y solicita una página.
2. El servidor web recibe la petición HTTP.
3. Si es contenido estático, responde directamente.
4. Si es contenido dinámico, reenvía la petición al servidor de aplicaciones.
5. El servidor de aplicaciones convierte la petición en una solicitud de servlet.
6. El servlet consulta la base de datos o ejecuta logica de negocio.
7. La respuesta vuelve al servidor web, que la entrega al cliente.

<figure markdown>
  ![](../assets/capas.webp)
  <figcaption>Capas de servidor web y servidor de aplicaciones.</figcaption>
</figure>

#### 3.2. Servidor web vs servidor de aplicaciones

| Aspecto             | Servidor de aplicaciones       | Servidor web              |
|---------------------|--------------------------------|---------------------------|
| Diseñado para       | HTTP y logica de negocio       | HTTP y contenido estatico |
| Almacena            | Logica de negocio              | Archivos estaticos        |
| Consumo de recursos | Alto                           | Bajo                      |
| Soporta             | EJB, transacciones, clustering | Servlets, JSP, JSON       |

!!! definition "Servlet"
    Un **servlet** es un programa Java que se ejecuta en un servidor web y genera contenido dinámico. Es mas eficiente que CGI porque usa hilos y no procesos por petición.

#### 3.3. Servicios comunes del servidor de aplicaciones

- Contenedor web (servlets, JSP, frameworks).
- Gestion de sesiones y autenticación.
- Conectores y pools de conexiones.
- Gestion de transacciones y mensajería.
- Logs, diagnostico y monitorización.

### 4. Despliegue de aplicaciones web

#### 4.1. Que es el despliegue y que entornos existen

El despliegue consiste en mover cambios entre entornos de trabajo. Los mas habituales son:

- Entorno local.
- Entorno de desarrollo.
- Entorno de preproducción.
- Entorno de producción.

El flujo mas habitual es avanzar cambios de izquierda a derecha, hasta llegar a produccion.

<figure markdown>
  ![](../assets/deploy.png)
  <figcaption>Modelo clásico de despliegue entre entornos.</figcaption>
</figure>

#### 4.2. Pasos del proceso de despliegue

1. **Planificación** del despliegue y sus reglas.
2. **Desarrollo** en entornos locales o de desarrollo.
3. **Pruebas** progresivas en entornos intermedios.
4. **Despliegue** en producción.
5. **Supervision** tras el lanzamiento.

#### 4.3. Tipos de despliegue

- **Metadatos**: cambios en código, plantillas o configuraciones.
- **Contenido**: textos, imágenes y recursos editables.

#### 4.4. Ventajas de trabajar con multiples entornos

- Reducción del riesgo en producción.
- Ahorro de tiempo en pruebas.
- Mejor gestion de contenidos sensibles al tiempo.

### 5. Buenas prácticas de despliegue

#### 5.1. Usar control de versiones (Git)

Git permite trabajar en equipo y recuperar versiones estables en caso de error. Sin control de versiones, el riesgo de conflictos aumenta de forma critica.

#### 5.2. Trabajar en ramas

Separar funcionalidades en ramas evita interferencias entre tareas y facilita las pruebas previas a producción.

#### 5.3. Desarrollar en local antes de desplegar

Trabajar en local acelera pruebas y reduce el numero de despliegues necesarios para validar un cambio.

#### 5.4. Revisar diferencias antes de producir

Comparar entorno de desarrollo y producción antes de lanzar evita errores de ultima hora y despliegues fallidos.

#### 5.5. Limitar permisos de despliegue

En equipos grandes, es recomendable que solo perfiles senior puedan desplegar en producción para reducir riesgos.

#### 5.6. Gestionar errores y rollback

Si algo falla en producción, no hay que entrar en pánico. Hay que evaluar si un rollback es viable y aplicar un plan de contingencia.

#### 5.7. Escoger la mejor franja de despliegue

El mejor momento suele ser cuando hay menos usuarios activos y el equipo esta disponible para reaccionar.

!!! warning "Sin un plan, el despliegue se convierte en improvisación"
    Define responsables, horario de despliegue y protocolo de rollback. Esto reduce el impacto de incidencias en producción.

### 6. Despliegue de aplicaciones Java

#### 6.1. Servlets y JSP

En aplicaciones JavaEE, los servlets y las paginas JSP gestionan peticiones HTTP y generan contenido dinamico.

#### 6.2. Estructura basica de una aplicacion JavaEE

Una aplicación web JavaEE suele contener:

- Directorio raiz con paginas HTML o JSP.
- Directorio `WEB-INF` con configuración y clases.
- Recursos (imágenes, CSS, JS) en la estructura necesaria.

Cada aplicación web se considera un **contexto** dentro del servidor.

#### 6.3. Empaquetamiento en WAR

El formato **WAR** es el estandar para distribuir aplicaciones web JavaEE. Se crea empaquetando el directorio de la aplicacion con la herramienta `jar`.

#### 6.4. Despliegue de WAR

Los servidores JavaEE permiten desplegar un WAR desde consola de administracion o copiandolo en un directorio de despliegue.

#### 6.5. Maven como herramienta de build

Maven simplifica la compilacion, pruebas y despliegue de proyectos.

<figure markdown>
  ![](../assets/maven-logo.png)
  <figcaption>Maven y sus ciclos de build.</figcaption>
</figure>

Ciclos habituales en Maven:

- validate
- compile
- test
- package
- integration-test
- verify
- install
- deploy

Ejemplo de ejecucion:

```bash
mvn package
```

Maven utiliza un archivo `pom.xml` para definir dependencias y estructura del proyecto.

### 7. Despliegue de aplicaciones Node.js con Express

#### 7.1. Node.js

Node.js es un **entorno de ejecucion** para JavaScript en el servidor. No es un lenguaje ni un framework.

<figure markdown>
  ![](../assets/nodejs-new-pantone-black.svg)
  <figcaption>Node.js como entorno de ejecucion.</figcaption>
</figure>

#### 7.2. Express

Express es un framework ligero que simplifica la creacion de APIs y aplicaciones web en Node.js.

<figure markdown>
  ![](../assets/express-logo.png)
  <figcaption>Express como framework de Node.js.</figcaption>
</figure>

#### 7.3. npm y gestion de paquetes

npm es el gestor de paquetes por defecto en Node.js. Permite instalar dependencias, publicar paquetes y definir scripts.

<figure markdown>
  ![](../assets/npm-logo.png)
  <figcaption>npm como gestor de paquetes.</figcaption>
</figure>

Un ejemplo de `package.json` con scripts seria:

```json
{
  "scripts": {
    "build": "tsc",
    "format": "prettier --write **/*.ts",
    "format-check": "prettier --check **/*.ts",
    "lint": "eslint src/**/*.ts",
    "pack": "ncc build",
    "test": "jest",
    "all": "npm run build && npm run format && npm run lint && npm run pack && npm test"
  }
}
```

### 8. CI/CD en el despliegue moderno

#### 8.1. Concepto general

CI/CD es un conjunto de practicas que automatizan integracion, pruebas, distribucion y despliegue.

<figure markdown>
  ![](../assets/ci-cd-flow-desktop.png)
  <figcaption>Flujo general de CI/CD.</figcaption>
</figure>

#### 8.2. Diferencias entre CI, CD y despliegue continuo

- **CI**: integra cambios frecuentes y ejecuta pruebas automatizadas.
- **CD**: distribuye artefactos listos para produccion.
- **Despliegue continuo**: publica en produccion sin intervencion manual.

#### 8.3. Integracion continua

<figure markdown>
  ![](../assets/ci.png)
  <figcaption>Integracion continua.</figcaption>
</figure>

La CI evita conflictos al integrar cambios a diario y validar con pruebas automatizadas.

#### 8.4. Distribucion continua

<figure markdown>
  ![](../assets/cd.png)
  <figcaption>Distribucion continua.</figcaption>
</figure>

La CD automatiza la entrega de artefactos listos para desplegar en produccion.

#### 8.5. Implementacion continua

<figure markdown>
  ![](../assets/cd2.png)
  <figcaption>Implementacion continua.</figcaption>
</figure>

El despliegue continuo publica cambios automaticamente tras superar pruebas.

### 9. Evidencias habituales para evaluar el RA3

- Esquemas o explicaciones del servidor de aplicaciones.
- Configuracion localizada y justificada (server.xml, context.xml, etc.).
- Integracion con servidor web mediante proxy o reverse proxy.
- Usuarios, roles y accesos configurados y probados.
- Aplicacion desplegada y funcionando con logs correctos.
- Ajustes aplicados (puertos, rutas, variables, permisos).
- Pruebas de funcionamiento y rendimiento basicas.
- Documentacion reproducible de la instalacion y uso.
- Despliegue en contenedor o nube si aplica.

## Referencias y bibliografia

- [What is an application server? (I)](https://www.itpro.co.uk/strategy/29643/what-is-an-application-server)
- [What is an application server? (II)](https://www.serverwatch.com/guides/application-server/)
- [What is deployment in software and web development](https://umbraco.com/knowledge-base/deployment/)
- [Simple y rapido. Entiende que es Maven en menos de 10 min.](https://www.javiergarzas.com/2014/06/maven-en-10-min.html)
- [Maven in 5 Minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html)
- [Apuntes JavaEE](http://www.jtech.ua.es/j2ee/restringido/cw/sesion01-apuntes.html)
- [Que es Node.js y por que deberia usarlo](https://kinsta.com/es/base-de-conocimiento/que-es-node-js/)
- [Que son la integracion y la distribucion continuas (CI/CD)](https://www.redhat.com/es/topics/devops/what-is-ci-cd)

## Recursos adicionales

- Documentacion oficial de Apache Tomcat y WildFly.
- Guias de despliegue de Node.js en produccion.
