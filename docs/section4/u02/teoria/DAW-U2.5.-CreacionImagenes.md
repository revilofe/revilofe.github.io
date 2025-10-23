---
title: "UD 2 - 2.5 Creación de imágenes Docker"
description: Crear imágenes personalizadas con Dockerfile
summary: Dockerfile, construcción de imágenes, distribución
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: 
permalink: /daw/unidad2/2.5
categories:
    - DAW
tags:
    - Docker
    - Dockerfile
    - Imágenes personalizadas
---

## 2.5. Creación de imágenes Docker

Hasta ahora hemos trabajado con imágenes predefinidas descargadas de Docker Hub. En esta sección aprenderemos a crear nuestras propias imágenes personalizadas para empaquetar nuestras aplicaciones.

### 1. Métodos de creación de imágenes

Existen dos métodos principales para crear imágenes Docker:

1. **Desde un contenedor**: Modificar un contenedor y guardarlo como imagen
2. **Desde un Dockerfile**: Definir la construcción mediante un archivo de texto (recomendado)

### 2. Crear imágenes desde un contenedor

#### 2.1. Proceso

1. Crear y modificar un contenedor
2. Guardar los cambios como nueva imagen con `docker commit`

**Ejemplo:**

```bash
# Crear contenedor base
$ docker run -it --name mi_contenedor ubuntu bash

# Dentro del contenedor, instalar software
root@abc123:/# apt-get update
root@abc123:/# apt-get install -y apache2
root@abc123:/# exit

# Crear imagen desde el contenedor
$ docker commit mi_contenedor mi_apache:v1

# Verificar
$ docker images
REPOSITORY   TAG   IMAGE ID      CREATED         SIZE
mi_apache    v1    1234567890ab  5 seconds ago   200MB
```

#### 2.2. Limitaciones

- **No reproducible**: No se documenta cómo se creó la imagen
- **No versionable**: Difícil de mantener cambios
- **No automatizable**: Proceso manual y propenso a errores

!!! warning "No recomendado para producción"
    Este método es útil para experimentación, pero para producción siempre usa Dockerfiles.

### 3. Dockerfile

Un **Dockerfile** es un archivo de texto que contiene instrucciones para construir una imagen Docker de forma automatizada y reproducible.

#### 3.1. Estructura básica

```dockerfile
# Imagen base
FROM ubuntu:22.04

# Información del mantenedor
LABEL maintainer="tu@email.com"

# Actualizar sistema e instalar paquetes
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copiar archivos
COPY index.html /var/www/html/

# Puerto a exponer
EXPOSE 80

# Comando al iniciar contenedor
CMD ["nginx", "-g", "daemon off;"]
```

#### 3.2. Instrucciones principales

**FROM**: Imagen base

```dockerfile
FROM ubuntu:22.04
FROM python:3.11-slim
FROM node:18-alpine
```

**LABEL**: Metadatos de la imagen

```dockerfile
LABEL maintainer="admin@ejemplo.com"
LABEL version="1.0"
LABEL description="Mi aplicación web"
```

**RUN**: Ejecutar comandos durante la construcción

```dockerfile
RUN apt-get update
RUN pip install flask
RUN npm install

# Mejor práctica: combinar comandos para reducir capas
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean
```

**COPY**: Copiar archivos del host a la imagen

```dockerfile
COPY app.py /app/
COPY . /app/
COPY --chown=www-data:www-data html/ /var/www/html/
```

**ADD**: Similar a COPY pero con funcionalidades extra

```dockerfile
ADD archivo.tar.gz /app/  # Descomprime automáticamente
ADD https://ejemplo.com/file.txt /tmp/  # Descarga URLs
```

!!! tip "Preferir COPY sobre ADD"
    Usa COPY a menos que necesites las funcionalidades especiales de ADD.

**WORKDIR**: Establecer directorio de trabajo

```dockerfile
WORKDIR /app
RUN python setup.py install  # Se ejecuta en /app
```

**ENV**: Definir variables de entorno

```dockerfile
ENV APP_HOME=/app
ENV PORT=8080
ENV PYTHONUNBUFFERED=1
```

**EXPOSE**: Documentar puertos que usa el contenedor

```dockerfile
EXPOSE 80
EXPOSE 443
EXPOSE 8080/tcp
```

**VOLUME**: Definir puntos de montaje

```dockerfile
VOLUME /data
VOLUME ["/var/log", "/var/db"]
```

**USER**: Cambiar usuario para instrucciones siguientes

```dockerfile
USER www-data
RUN whoami  # Ejecuta como www-data
```

**CMD**: Comando por defecto al ejecutar contenedor

```dockerfile
CMD ["python", "app.py"]
CMD ["nginx", "-g", "daemon off;"]
CMD ["/bin/bash"]
```

**ENTRYPOINT**: Punto de entrada del contenedor

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argumento por defecto para ENTRYPOINT
```

### 4. Construir imágenes

#### 4.1. Comando docker build

```bash
# Sintaxis básica
$ docker build -t nombre:tag ruta_contexto

# Ejemplo
$ docker build -t mi_app:1.0 .

# Especificar Dockerfile diferente
$ docker build -t mi_app:1.0 -f Dockerfile.prod .

# Pasar argumentos de construcción
$ docker build --build-arg VERSION=1.0 -t mi_app .
```

**Opciones útiles:**

```bash
# Sin caché (construcción completa)
$ docker build --no-cache -t mi_app .

# Especificar plataforma
$ docker build --platform linux/amd64 -t mi_app .

# Ver construcción detallada
$ docker build --progress=plain -t mi_app .
```

#### 4.2. Contexto de construcción

El contexto es el conjunto de archivos enviados al daemon de Docker para la construcción.

```bash
# El punto (.) indica el directorio actual como contexto
$ docker build -t mi_app .
```

**Archivo .dockerignore:**

Excluir archivos del contexto:

```
# .dockerignore
node_modules
.git
*.log
.env
__pycache__
*.pyc
```

### 5. Ejemplos prácticos

#### 5.1. Sitio web estático con Nginx

**Dockerfile:**

```dockerfile
FROM nginx:alpine

# Copiar archivos HTML
COPY html/ /usr/share/nginx/html/

# Copiar configuración personalizada
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
```

**Construcción:**

```bash
$ docker build -t mi_web:1.0 .
$ docker run -d -p 8080:80 --name web mi_web:1.0
```

#### 5.2. Aplicación PHP

**Dockerfile:**

```dockerfile
FROM php:8.2-apache

# Instalar extensiones PHP
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Habilitar módulos Apache
RUN a2enmod rewrite

# Copiar código fuente
COPY src/ /var/www/html/

# Permisos
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
```

#### 5.3. Aplicación Python con Flask

**Dockerfile:**

```dockerfile
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Copiar requirements primero (mejor aprovechamiento del caché)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Usuario no privilegiado
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Puerto
EXPOSE 5000

# Variables de entorno
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Comando de inicio
CMD ["flask", "run", "--host=0.0.0.0"]
```

**requirements.txt:**

```
Flask==2.3.0
gunicorn==20.1.0
```

#### 5.4. Aplicación Node.js

**Dockerfile:**

```dockerfile
FROM node:18-alpine

# Directorio de trabajo
WORKDIR /usr/src/app

# Copiar package.json y package-lock.json
COPY package*.json ./

# Instalar dependencias
RUN npm ci --only=production

# Copiar código de la aplicación
COPY . .

# Usuario no privilegiado
USER node

# Puerto
EXPOSE 3000

# Comando de inicio
CMD ["node", "server.js"]
```

### 6. Multi-stage builds

Los multi-stage builds permiten crear imágenes más pequeñas usando múltiples etapas.

**Ejemplo: Aplicación Go**

```dockerfile
# Etapa 1: Construcción
FROM golang:1.20 AS builder

WORKDIR /app
COPY . .
RUN go build -o myapp

# Etapa 2: Imagen final
FROM alpine:latest

RUN apk --no-cache add ca-certificates
WORKDIR /root/

# Copiar solo el binario de la etapa anterior
COPY --from=builder /app/myapp .

CMD ["./myapp"]
```

**Ventajas:**

- Imagen final más pequeña (solo contiene lo necesario)
- Mayor seguridad (menos herramientas en producción)
- Separación construcción/ejecución

### 7. Buenas prácticas

#### 7.1. Optimización de capas

```dockerfile
# ❌ Mal: Múltiples capas
RUN apt-get update
RUN apt-get install -y package1
RUN apt-get install -y package2

# ✅ Bien: Una sola capa
RUN apt-get update && \
    apt-get install -y \
        package1 \
        package2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

#### 7.2. Orden de instrucciones

```dockerfile
# Primero lo que cambia menos (aprovecha caché)
FROM python:3.11-slim
WORKDIR /app

# Dependencias (cambian poco)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Código de la aplicación (cambia frecuentemente)
COPY . .

CMD ["python", "app.py"]
```

#### 7.3. Imágenes base pequeñas

```dockerfile
# Alpine Linux es muy ligera
FROM python:3.11-alpine
FROM node:18-alpine
FROM nginx:alpine

# Imágenes "slim" también son una buena opción
FROM python:3.11-slim
```

#### 7.4. Seguridad

```dockerfile
# No ejecutar como root
RUN useradd -m -u 1000 appuser
USER appuser

# Mantener imágenes actualizadas
RUN apt-get update && apt-get upgrade -y

# No incluir secretos en la imagen
# Usar secrets de Docker o variables de entorno en runtime
```

### 8. Distribuir imágenes

#### 8.1. Etiquetar imágenes

```bash
# Etiquetar para Docker Hub
$ docker tag mi_app:1.0 usuario/mi_app:1.0
$ docker tag mi_app:1.0 usuario/mi_app:latest

# Etiquetar para registro privado
$ docker tag mi_app:1.0 registry.ejemplo.com/mi_app:1.0
```

#### 8.2. Subir a Docker Hub

```bash
# Login
$ docker login

# Push
$ docker push usuario/mi_app:1.0
$ docker push usuario/mi_app:latest
```

#### 8.3. Registro privado

```bash
# Ejecutar registro privado
$ docker run -d -p 5000:5000 --name registry registry:2

# Etiquetar y subir
$ docker tag mi_app:1.0 localhost:5000/mi_app:1.0
$ docker push localhost:5000/mi_app:1.0

# Descargar
$ docker pull localhost:5000/mi_app:1.0
```

### 9. Argumentos de construcción

**Dockerfile:**

```dockerfile
FROM ubuntu:22.04

# Definir argumento
ARG VERSION=1.0
ARG USER=appuser

# Usar argumento
ENV APP_VERSION=${VERSION}

RUN useradd -m ${USER}
USER ${USER}

LABEL version=${VERSION}
```

**Construcción:**

```bash
$ docker build --build-arg VERSION=2.0 --build-arg USER=admin -t mi_app .
```

### Resumen

En esta sección hemos aprendido:

- ✅ Métodos para crear imágenes Docker
- ✅ Estructura y sintaxis de Dockerfiles
- ✅ Instrucciones principales del Dockerfile
- ✅ Construir imágenes con docker build
- ✅ Multi-stage builds para optimizar tamaño
- ✅ Buenas prácticas de construcción
- ✅ Distribuir imágenes en registros

### Recursos adicionales

- [Documentación Dockerfile](https://docs.docker.com/engine/reference/builder/)
- [Best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Curso Docker IES - Módulo 5](../u01/teoria/OtrosRecursos/curso_docker_ies/modulo5/)

!!! success "Fin del curso Docker"
    Has completado la introducción a Docker. Ahora estás preparado para containerizar tus aplicaciones y trabajar con contenedores en proyectos reales.
