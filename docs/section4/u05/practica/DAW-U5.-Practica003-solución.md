---
title: "UD 5 - P3 (Solución): Informe RA3 sobre el despliegue (WildFly contenedor + Gradle)"
summary: Respuestas orientativas a las preguntas (a-i) del RA3 para la práctica P5.3.
description: Documento de apoyo con posibles respuestas. Puede variar según tu ejecución real de la P5.2, tus rutas y tus logs.
authors:
    - Eduardo Fdez
date: 2026-01-28
icon: "material/file-document-edit"
permalink: /daw/unidad5/p5.3-solucion
categories:
    - DAW
tags:
    - RA3
    - Solución
    - WildFly
    - Gradle
    - Docker
---

## Solución orientativa P5.3 (a-i)

!!! warning "Importante"
    Estas respuestas son **orientativas**. En tu entrega deben aparecer tus
    **evidencias reales**: tus comandos, tus rutas, tus logs y tus URLs.

### a) Componentes y funcionamiento de los servicios del servidor

**Respuesta posible**

En mi despliegue de la P5.2 intervienen estos componentes:

1. **Cliente**: navegador o `curl`, que lanza una petición HTTP.
2. **Docker**: ejecuta el contenedor `wildfly` y expone puertos al host.
3. **WildFly**: servidor de aplicaciones que arranca en modo standalone.
4. **Aplicación WAR**: artefacto desplegado (API REST) que vive en WildFly.
5. **Puertos**:
   
   - **8080**: tráfico de aplicaciones (peticiones REST).
   - **9990**: consola/gestión (administración).

Flujo de petición (ejemplo):

1. `curl` llama a `http://localhost:8080/.../api/.../hello`.
2. Docker redirige `localhost:8080` al puerto 8080 del contenedor.
3. WildFly recibe la petición y la enruta a la aplicación desplegada.
4. La capa REST (JAX-RS / Jakarta REST) ejecuta el recurso y genera respuesta.
5. WildFly devuelve la respuesta al cliente (JSON o texto).

**Evidencias típicas**

- `docker ps` mostrando el contenedor y los puertos publicados.
- `docker logs -f wildfly` mostrando el despliegue y el acceso.
- Respuesta del endpoint (`curl`).

### b) Archivos principales de configuración y bibliotecas compartidas

**Respuesta posible**

En el contenedor de WildFly, el archivo principal de configuración suele estar
en:

- `/opt/jboss/wildfly/standalone/configuration/standalone.xml`

Ahí se podrían ajustar cosas como:

- Puertos y bindings.
- Datasources y pools de conexiones.
- Seguridad (realms, roles).
- Logging y niveles de log.

Sobre bibliotecas compartidas:

En el `build.gradle.kts` de la práctica se usa:

- `compileOnly("jakarta.platform:jakarta.jakartaee-api:10.0.0")`

Esto es “provided” porque **WildFly ya incluye** la API de Jakarta EE. Ventaja:

- El WAR pesa menos y evita duplicar librerías que ya están en el servidor.
- Menos riesgo de conflictos de versiones con el runtime del servidor.

**Evidencias típicas**

- Captura/salida de `docker exec -it wildfly ls .../standalone/configuration`.
- Fragmento del `build.gradle.kts` donde se ve `compileOnly`.

### c) Cooperación con el servidor web (proxy / reverse proxy)

**Respuesta posible**

En producción pondría un servidor web frontal (por ejemplo, Nginx) para:

- Terminar TLS (HTTPS) y aplicar políticas de seguridad.
- Hacer reverse proxy hacia WildFly.
- No exponer la consola de administración (9990) hacia fuera.

Ejemplo de configuración Nginx:

```nginx
server {
    listen 80;
    server_name ejemplo.local;

    location /api/ {
        proxy_pass http://127.0.0.1:8080/myproject/module/backend/api/;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Con esto:

- El alumnado consumiría `http://ejemplo.local/api/...` en vez de conocer la
  ruta completa de WildFly.
- **9990 no se publica** al exterior; solo se usa internamente/por VPN.

**Evidencias típicas**

- Fragmento de `nginx.conf` o `sites-enabled`.
- Explicación de qué puertos publicarías en Docker y cuáles no.

### d) Mecanismos de seguridad del servidor de aplicaciones

**Respuesta posible**

Medidas aplicadas en P5.2:

- Creación de **usuario de administración** con `add-user.sh`.

Medidas que añadiría para producción (ejemplos):

1. **No exponer 9990** a Internet (solo red interna/VPN).
2. Forzar **HTTPS** (idealmente en el frontal Nginx) y redirigir HTTP->HTTPS.
3. Gestionar credenciales con **secretos** (no en README ni en repositorio).
4. Activar logging adecuado y centralizar logs para auditoría.
5. Limitar permisos del contenedor y aplicar hardening (usuario no root,
   filesystem de solo lectura cuando sea posible).

**Evidencias típicas**

- Captura de puertos expuestos.
- Captura de que la consola solo es accesible internamente.
- Ejemplo de política de secretos.

### e) Componentes web del servidor de aplicaciones

**Respuesta posible**

- Un **WAR** es un paquete que contiene la aplicación web: clases, recursos y
  metadatos necesarios para que WildFly lo despliegue.
- La app se publica bajo un **contexto** (ruta base) definido por el WAR y/o
  configuración del servidor.
- El servidor usa un **contenedor web** para atender las peticiones y ejecutar
  los recursos REST.

Ejemplo de URL (de la práctica):

- `http://localhost:8080/myproject/module/backend/api/myservice/hello`

Desglose:

- Host: `localhost`
- Puerto: `8080`
- Contexto: `myproject/module/backend` (según el despliegue)
- Ruta API: `/api/myservice/hello`

**Evidencias típicas**

- URL probada en navegador/curl.
- Log del servidor mostrando el acceso.

### f) Parámetros necesarios para el despliegue

**Respuesta posible**

Parámetros críticos que usé en P5.2:

1. `docker run --name wildfly ...` (identifica el contenedor).
2. `-p 8080:8080` (expone la app al host).
3. `-p 9990:9990` (expone consola, solo para laboratorio).
4. `docker cp ...war wildfly:/opt/jboss/wildfly/standalone/deployments/`
   (ruta de despliegue).
5. `./gradlew clean build` (genera el WAR).
6. Nombre del WAR (`archiveBaseName`) para saber qué copiar/desplegar.

Si algo está mal:

- Si 8080 no se publica, no hay acceso desde el host.
- Si copio el WAR a otra ruta, WildFly no lo auto-despliega.
- Si el WAR se llama distinto, el `docker cp` falla o despliego una versión
  equivocada.

**Evidencias típicas**

- Capturas de comandos ejecutados y su salida.
- Nombre real del WAR en `build/libs/`.

### g) Pruebas de funcionamiento y rendimiento

**Respuesta posible**

Pruebas funcionales:

- `/hello` devuelve una respuesta correcta.
- `/pojo/list` devuelve JSON.
- `POST`, `PUT` y `DELETE` con `curl` funcionan.

Ejemplo de prueba de rendimiento con `ab`:

```sh
ab -n 200 -c 10 http://localhost:8080/myproject/module/backend/api/myservice/hello
```

Análisis básico:

- Revisaría si hay errores HTTP (4xx/5xx).
- Miraría peticiones/segundo y latencias medias.
- Si hay errores, revisaría logs del contenedor.

**Evidencias típicas**

- Salida completa de `ab`/`hey`/`wrk`.
- Logs durante la prueba.

### h) Documentación de administración y recomendaciones

**Respuesta posible**

Mini-guía:

1. Levantar WildFly:
   
   - `docker pull quay.io/wildfly/wildfly:latest`
   - `docker run -d --name wildfly -p 8080:8080 -p 9990:9990 ...`

2. Compilar y generar WAR:
   
   - `./gradlew clean build`

3. Desplegar nueva versión:
   
   - `docker cp build/libs/...war wildfly:/opt/jboss/wildfly/standalone/deployments/`
   - Revisar `docker logs -f wildfly`

4. Validar estado:
   
   - Probar endpoint de salud (por ejemplo `/hello`).
   - Revisar logs (errores, warnings, despliegue correcto).

Recomendaciones:

- No publicar 9990 fuera de laboratorio.
- Usar scripts/pipelines para evitar pasos manuales.
- Mantener evidencias y pasos en un documento reproducible.

### i) Virtualización, nube o contenedores en el despliegue

**Respuesta posible**

El contenedor mejora:

- **Reproducibilidad**: misma imagen, mismo runtime en cualquier máquina.
- **Aislamiento**: no “ensucia” el host con instalaciones de servidor.
- **Rapidez**: levantar/parar/resetear es inmediato.

Mejoras para producción (ejemplos):

1. **Volúmenes** para persistir configuración/logs:
   
   - Montar volúmenes para no perder datos al recrear contenedor.

2. **Healthcheck** y reinicio automático:
   
   - Definir `HEALTHCHECK` o usar `docker-compose` con `restart: always`.

Otras opciones:

- Limitar CPU/RAM del contenedor.
- Separar redes (front/back) y no exponer puertos internos.

