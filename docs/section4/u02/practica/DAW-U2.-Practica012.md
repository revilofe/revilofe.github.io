---
title: "UD 2 - P12: Construcción de imagen Docker con aplicación Java y Tomcat"
description: "Creación de imágenes Docker para desplegar aplicaciones Java con Apache Tomcat"
summary: "Actividad práctica para crear imágenes Docker que despliegan aplicaciones Java (WAR) en Tomcat."
authors:
    - Eduardo Fdez
date: 2025-01-13
icon: "material/file-document-edit"
permalink: /daw/unidad2/p2.12
categories:
    - DAW
tags:
    - Docker
    - Dockerfile
    - Java
    - Tomcat
    - WAR
    - Despliegue
---

## Relación 2.12

### Descripción

**Actividad:** *Construcción de imagen Docker con aplicación Java y Tomcat*

En esta práctica aprenderás a crear imágenes Docker para desplegar aplicaciones Java (archivos WAR) utilizando Apache Tomcat como servidor de aplicaciones. Comprenderás cómo funciona Tomcat en contenedores y cómo automatizar el despliegue de aplicaciones Java.

#### Objetivo general

Aprender a:

- Trabajar con el servidor de aplicaciones Apache Tomcat en Docker.
- Construir imágenes personalizadas para aplicaciones Java.
- Desplegar archivos WAR automáticamente.
- Configurar Tomcat mediante variables de entorno.
- Acceder y usar la interfaz de administración de Tomcat.
- Gestionar aplicaciones Java en contenedores.

---

### Contexto de trabajo

**Apache Tomcat** es un servidor de aplicaciones Java muy popular que ejecuta aplicaciones web Java (Servlets y JSP). Las aplicaciones se empaquetan en archivos WAR (Web Application Archive) que Tomcat puede desplegar automáticamente.

**Conceptos clave:**

- **WAR (Web Application Archive):** Archivo comprimido con una aplicación Java web
- **webapps:** Directorio donde Tomcat despliega las aplicaciones
- **Manager App:** Interfaz web de administración de Tomcat
- **Variables de entorno:** Para configurar usuarios y contraseñas

**Arquitectura:**

```
┌──────────────────────────┐
│   Contenedor Tomcat      │
│                          │
│  ┌───────────────────┐   │
│  │  Apache Tomcat    │   │
│  │  (Puerto 8080)    │   │
│  │                   │   │
│  │  /webapps/        │   │
│  │   ├── sample.war  │   │
│  │   └── manager/    │   │
│  └───────────────────┘   │
│                          │
└──────────────────────────┘
```

---

### 📦 Obtención de la aplicación de ejemplo

#### Opción 1: Usar la aplicación sample de Tomcat

Puedes descargar la aplicación de ejemplo directamente del repositorio de Tomcat:

```bash
wget https://tomcat.apache.org/tomcat-9.0-doc/appdev/sample/sample.war
```

#### Opción 2: Crear una aplicación simple

Si prefieres crear tu propia aplicación, aquí tienes un ejemplo básico:

**Estructura de la aplicación:**

```
mi-app/
└── WEB-INF/
    ├── web.xml
    └── classes/
        └── HolaMundo.class
```

**Archivo `web.xml`:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee 
         http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="3.1">
    
    <display-name>Mi Aplicación Docker</display-name>
    <description>Aplicación Java simple para Docker</description>
    
    <welcome-file-list>
        <welcome-file>index.jsp</welcome-file>
    </welcome-file-list>
</web-app>
```

**Archivo `index.jsp` (en la raíz de mi-app/):**
```jsp
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Mi Aplicación Java en Docker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        h1 {
            color: #f5576c;
            text-align: center;
        }
        .info-box {
            background: #f0f0f0;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            border-left: 4px solid #f5576c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>☕ Aplicación Java en Docker</h1>
        
        <div class="info-box">
            <h2>Información del Servidor</h2>
            <p><strong>Servidor:</strong> <%= application.getServerInfo() %></p>
            <p><strong>Puerto:</strong> <%= request.getServerPort() %></p>
            <p><strong>Versión de Servlet:</strong> <%= application.getMajorVersion() + "." + application.getMinorVersion() %></p>
        </div>

        <div class="info-box">
            <h2>Información de la Petición</h2>
            <p><strong>Método:</strong> <%= request.getMethod() %></p>
            <p><strong>URI:</strong> <%= request.getRequestURI() %></p>
            <p><strong>IP del Cliente:</strong> <%= request.getRemoteAddr() %></p>
        </div>

        <div class="info-box">
            <h2>Información del Sistema</h2>
            <p><strong>Java Version:</strong> <%= System.getProperty("java.version") %></p>
            <p><strong>Java Vendor:</strong> <%= System.getProperty("java.vendor") %></p>
            <p><strong>OS:</strong> <%= System.getProperty("os.name") %> <%= System.getProperty("os.version") %></p>
        </div>

        <div class="info-box">
            <h2>Fecha y Hora</h2>
            <p><strong>Fecha actual:</strong> <%= new java.util.Date() %></p>
        </div>

        <div style="text-align: center; margin-top: 30px;">
            <p style="color: #888;"><small>Práctica Docker - Despliegue de aplicaciones Java</small></p>
        </div>
    </div>
</body>
</html>
```

Para empaquetar esta aplicación en un WAR:
```bash
cd mi-app
jar -cvf mi-app.war *
```

O simplemente usa la aplicación `sample.war` que descargarás.

---

### 🔹 Parte 1: Despliegue manual en Tomcat

#### Tarea 1.1: Contenedor Tomcat básico

1. Investiga la imagen oficial de Tomcat en Docker Hub:
   
    - Qué versiones están disponibles
    - Qué puertos utiliza
    - Qué imagen base recomiendan

2. Crea un contenedor Tomcat básico:
   
    - Imagen: `bitnami/tomcat:9.0`
    - Puerto 8080 del host → puerto 8080 del contenedor
    - Variables de entorno para usuario y contraseña de administración
    - Nombre: `tomcat_test`

3. **Información sobre la imagen bitnami/tomcat:**
   
    - Variable `TOMCAT_USERNAME`: Usuario administrador
    - Variable `TOMCAT_PASSWORD`: Contraseña administrador
    - Puerto por defecto: 8080
    - Directorio de despliegue: `/opt/bitnami/tomcat/webapps` o `/app`

4. Accede desde el navegador a `http://localhost:8080`.

5. Verifica que ves la página principal de Tomcat.

#### Tarea 1.2: Acceso a la administración

1. Accede a `http://localhost:8080/manager/html`.

2. Introduce el usuario y contraseña que configuraste.

3. Explora la interfaz de administración:
   
    - ¿Qué aplicaciones hay desplegadas por defecto?
    - ¿Qué información se muestra?
    - ¿Qué acciones puedes realizar?

#### Tarea 1.3: Despliegue manual de aplicación

1. Obtén el archivo `sample.war` (descárgalo o créalo).

2. Copia el archivo WAR al contenedor:
   
    - Investiga el comando de Docker para copiar archivos al contenedor
    - Copia `sample.war` al directorio `/app` o `/opt/bitnami/tomcat/webapps`

3. Espera unos segundos (Tomcat despliega automáticamente).

4. Accede a `http://localhost:8080/sample/`.

5. Verifica que la aplicación funciona correctamente.

6. Observa en el manager que ahora aparece la aplicación `sample`.

---

### 🔹 Parte 2: Construcción de imagen personalizada

#### Tarea 2.1: Dockerfile para aplicación Java

1. Crea un directorio para tu proyecto: `~/imagen_tomcat`.

2. Coloca tu archivo WAR (sample.war o mi-app.war) en este directorio.

3. Crea un `Dockerfile` que:
   
    - Use como imagen base `bitnami/tomcat:9.0`
    - Copie el archivo WAR al directorio de despliegue
    - (Opcionalmente) Establezca variables de entorno por defecto

4. **Pistas:**
   
    - Directorio de despliegue: `/opt/bitnami/tomcat/webapps`
    - No necesitas CMD (lo hereda de la imagen base)
    - El nombre del WAR determina la URL de acceso

#### Tarea 2.2: Construcción y prueba

1. Construye tu imagen:
   
    - Nombre: `tu_usuario/app_java`
    - Etiqueta: `v1`

2. Anota el tamaño de la imagen.

3. Crea un contenedor desde tu imagen:
   
    - Puerto 8081 del host
    - Configurar usuario y contraseña mediante variables de entorno
    - Nombre: `mi_app_java`

4. Accede y verifica que la aplicación se desplegó correctamente.

5. **Preguntas:**
   
    - ¿Cuánto tardó Tomcat en desplegar la aplicación?
    - ¿Aparece en el manager?
    - ¿Qué tamaño tiene tu imagen vs la imagen base?

---

### 🔹 Parte 3: Múltiples aplicaciones

#### Tarea 3.1: Imagen con varias aplicaciones

1. Obtén o crea una segunda aplicación WAR.

2. Crea un nuevo Dockerfile que despliegue ambas aplicaciones:
   
    - Copia `app1.war` al directorio de despliegue
    - Copia `app2.war` al directorio de despliegue

3. Construye la imagen:
   
    - Nombre: `tu_usuario/app_java`
    - Etiqueta: `v2`

4. Crea un contenedor y verifica que ambas aplicaciones están desplegadas.

5. Accede a ambas aplicaciones desde URLs diferentes.

#### Tarea 3.2: Gestión desde el manager

1. Accede al manager de Tomcat.

2. Practica las siguientes operaciones:
   
    - Detener una aplicación
    - Reiniciar una aplicación
    - Ver las sesiones activas
    - Eliminar (undeploy) una aplicación

3. Documenta qué sucede con cada operación.

---

### 🔹 Parte 4: Configuración avanzada

#### Tarea 4.1: Personalización de Tomcat

Investiga cómo personalizar Tomcat y crea una nueva versión que incluya:

1. **Configuración de memoria JVM:**
   
    - Variables `JAVA_OPTS` o `CATALINA_OPTS`
    - Ejemplo: `-Xms512m -Xmx1024m`

2. **Configuración de timeout:**
   
    - Modificar el tiempo de sesión
    - Configurar timeouts de conexión

3. **Variables de entorno personalizadas:**
   
    - Definir variables que tu aplicación pueda usar
    - Ejemplo: `APP_ENV=production`, `APP_VERSION=1.0`

#### Tarea 4.2: Despliegue con Docker Compose

Crea un archivo `docker-compose.yml` que:

1. Despliegue tu aplicación Tomcat.
2. Configure usuario y contraseña mediante .env.
3. Configure límites de recursos.
4. Configure healthcheck.
5. Defina volúmenes para logs (opcional).

#### Tarea 4.3: Integración con base de datos (avanzado)

Si tu aplicación Java necesita conectarse a una base de datos:

1. Modifica tu `docker-compose.yml` para incluir un servicio MariaDB/MySQL.

2. Configura tu aplicación Java para conectarse a la BD mediante variables de entorno.

3. Verifica la conectividad entre contenedores.

---

### 🔹 Parte 5: Optimización y buenas prácticas

#### Tarea 5.1: Reducción del tamaño de la imagen

Experimenta con diferentes imágenes base:

1. **Tomcat oficial (`tomcat:9.0`):**
   
    - Construye una versión con esta imagen
    - Compara el tamaño

2. **Tomcat con JRE (`tomcat:9.0-jre11`):**
   
    - Prueba esta variante más ligera
    - Compara funcionalidad y tamaño

3. **Alpine (`tomcat:9.0-jre11-alpine`):**
   
    - Prueba la versión Alpine
    - Documenta diferencias

4. Completa una tabla comparativa con los resultados.

#### Tarea 5.2: Multi-stage build para compilar aplicación

Si quieres compilar tu aplicación Java dentro de Docker:

```dockerfile
# Etapa de construcción
FROM maven:3.8-openjdk-11 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package

# Etapa final
FROM tomcat:9.0-jre11
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/
```

Investiga y crea un ejemplo similar.

#### Tarea 5.3: Seguridad

Investiga y aplica:

1. **Eliminar aplicaciones por defecto:**
   
    - Manager, host-manager, docs, examples
    - ¿Por qué es recomendable?

2. **Usuario no root:**
   
    - ¿Cómo ejecutar Tomcat con un usuario diferente?
    - ¿Qué imagen lo soporta mejor?

3. **Actualización de dependencias:**
   
    - ¿Cómo mantener la imagen actualizada?
    - ¿Qué vulnerabilidades puede tener Tomcat?

---

### 🔹 Parte 6: Análisis y documentación

#### Tarea 6.1: Comparación de imágenes

Completa esta tabla:

| Aspecto | bitnami/tomcat | tomcat:9.0 | tomcat:jre11 | tomcat:alpine |
|---------|----------------|------------|--------------|---------------|
| Tamaño base | | | | |
| Tamaño con app | | | | |
| Tiempo construcción | | | | |
| Facilidad uso | | | | |
| Documentación | | | | |
| Seguridad | | | | |

#### Tarea 6.2: Preguntas de reflexión

Responde en tu documentación:

1. **Sobre Tomcat:**
   
    - ¿Qué ventajas tiene usar Tomcat en contenedores?
    - ¿Qué desafíos presenta?
    - ¿Cuándo usarías Tomcat vs otros servidores?

2. **Sobre el despliegue de WAR:**
   
    - ¿Qué sucede cuando copias un WAR al directorio webapps?
    - ¿Cómo se relaciona el nombre del WAR con la URL?
    - ¿Qué pasa si hay errores en el despliegue?

3. **Sobre la configuración:**
   
    - ¿Por qué usar variables de entorno para credenciales?
    - ¿Cómo gestionarías diferentes entornos (dev/test/prod)?
    - ¿Qué otros métodos de configuración existen?

4. **Sobre imágenes:**
   
    - ¿Cuándo preferirías bitnami vs oficial?
    - ¿Vale la pena usar imágenes Alpine?
    - ¿Cómo elegir la versión de Java?

#### Tarea 6.3: Diagrama de arquitectura

Crea un diagrama que muestre:

1. La estructura interna del contenedor Tomcat.
2. El directorio webapps y las aplicaciones desplegadas.
3. Los puertos y su mapeo.
4. Las variables de entorno utilizadas.
5. (Si aplica) La conexión con base de datos.

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Los Dockerfiles creados (todas las versiones)
    - Archivo docker-compose.yml (si lo creaste)
    - Comandos Docker utilizados
    - Capturas de pantalla:
        - Página principal de Tomcat
        - Manager de Tomcat con aplicaciones desplegadas
        - Aplicación(es) funcionando
        - Comparación de tamaños de imágenes
        - Proceso de despliegue manual
        - Healthchecks (si los implementaste)
    - Tabla comparativa de imágenes
    - Respuestas a todas las preguntas
    - Diagrama de arquitectura

2. **Archivos del proyecto:**
   
    - Archivo(s) WAR utilizado(s)
    - Dockerfile(s)
    - docker-compose.yml (si aplica)
    - Archivos de configuración personalizados

---

### Evaluación

Se evaluará:

- Correcta construcción de imágenes con Tomcat.
- Despliegue exitoso de aplicaciones Java.
- Uso de variables de entorno para configuración.
- Comprensión del funcionamiento de Tomcat.
- Análisis comparativo de diferentes imágenes.
- Implementación de buenas prácticas.
- Calidad de la documentación.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Apache Tomcat oficial: [https://tomcat.apache.org/](https://tomcat.apache.org/)
- Imagen oficial de Tomcat: [https://hub.docker.com/_/tomcat](https://hub.docker.com/_/tomcat)
- Imagen Bitnami Tomcat: [https://hub.docker.com/r/bitnami/tomcat](https://hub.docker.com/r/bitnami/tomcat)
- Documentación de Tomcat: [https://tomcat.apache.org/tomcat-9.0-doc/](https://tomcat.apache.org/tomcat-9.0-doc/)
- Despliegue de aplicaciones WAR: [https://tomcat.apache.org/tomcat-9.0-doc/deployer-howto.html](https://tomcat.apache.org/tomcat-9.0-doc/deployer-howto.html)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.12.-AplicacionJava.html){ .md-button }
