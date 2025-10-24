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

### 2. Crear imágenes desde un contenedor (docker commit)

Este método consiste en modificar manualmente un contenedor y luego guardarlo como imagen.

#### 2.1. Proceso paso a paso

**Paso 1: Crear contenedor base**

```bash
$ docker run -it --name mi_contenedor ubuntu bash
root@abc123:/#
```

- Crea un contenedor interactivo desde Ubuntu
- Te conecta a su shell
- Ahora estás "dentro" del contenedor

**Paso 2: Instalar software (dentro del contenedor)**

```bash
root@abc123:/# apt-get update
Get:1 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
...
Reading package lists... Done

root@abc123:/# apt-get install -y apache2
Reading package lists... Done
Building dependency tree... Done
The following NEW packages will be installed:
  apache2 apache2-bin apache2-data apache2-utils
...
Setting up apache2 (2.4.52-1ubuntu4)

root@abc123:/# echo "Hola desde mi servidor" > /var/www/html/index.html

root@abc123:/# exit
exit
```

**¿Qué hemos hecho?**

1. Actualizamos la lista de paquetes
2. Instalamos Apache (servidor web)
3. Creamos un archivo HTML personalizado
4. Salimos del contenedor

**Paso 3: Guardar los cambios como imagen**

```bash
$ docker commit mi_contenedor mi_apache:v1
sha256:1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
```

- `docker commit`: Crea una imagen desde un contenedor
- `mi_contenedor`: Nombre del contenedor con las modificaciones
- `mi_apache:v1`: Nombre y etiqueta de la nueva imagen

**¿Qué ha pasado?**

Docker ha tomado todos los cambios del contenedor (Apache instalado + archivo HTML) y los ha guardado como una nueva imagen.

**Paso 4: Verificar la imagen creada**

```bash
$ docker images
REPOSITORY   TAG   IMAGE ID      CREATED         SIZE
mi_apache    v1    1234567890ab  5 seconds ago   200MB
ubuntu       latest f63181f19b2f  2 weeks ago     72.9MB
```

**Observa:**
- La imagen `mi_apache` ocupa 200MB (Ubuntu 72.9MB + Apache + nuestros cambios)
- La imagen se creó hace 5 segundos

**Paso 5: Probar la imagen creada**

```bash
$ docker run -d -p 8080:80 --name test_apache mi_apache:v1 apache2ctl -D FOREGROUND
abc123def456

$ curl http://localhost:8080
Hola desde mi servidor
```

¡Funciona! Hemos creado nuestra primera imagen personalizada.

#### 2.2. Añadir información a la imagen

```bash
$ docker commit \
  --author "Tu Nombre <tu@email.com>" \
  --message "Instalado Apache 2.4 con página personalizada" \
  mi_contenedor \
  mi_apache:v1
```

**Opciones útiles:**

- `--author`: Quién creó la imagen
- `--message` o `-m`: Descripción de los cambios
- `--change`: Modificar configuración (CMD, EXPOSE, etc.)

**Ejemplo con --change:**

```bash
$ docker commit \
  --change='CMD ["apache2ctl", "-D", "FOREGROUND"]' \
  --change='EXPOSE 80' \
  mi_contenedor \
  mi_apache:v2
```

Ahora la imagen v2 ya tiene definido el comando y el puerto.

#### 2.3. Limitaciones y problemas

**❌ Problema 1: No es reproducible**

```bash
# Tu compañero no sabe cómo creaste la imagen
$ docker history mi_apache:v1
IMAGE          CREATED         CREATED BY      SIZE      COMMENT
1234567890ab   2 minutes ago   /bin/bash       127MB     # ¿Qué se hizo aquí?
f63181f19b2f   2 weeks ago     ...             72.9MB
```

No hay registro de qué comandos ejecutaste.

**❌ Problema 2: No es versionable**

Si quieres modificar algo, debes:
1. Crear contenedor desde la imagen
2. Hacer cambios manualmente
3. Hacer commit de nuevo
4. Esperar recordar qué hiciste la vez anterior

**❌ Problema 3: No es automatizable**

No puedes incluirlo en CI/CD porque requiere intervención manual.

**❌ Problema 4: Difícil de mantener**

```bash
# Después de 3 meses...
$ docker images
REPOSITORY   TAG
mi_apache    v1    # ¿Qué había aquí?
mi_apache    v2    # ¿Qué cambió de v1 a v2?
mi_apache    v3    # ¿Esta es la buena?
```

#### 2.4. ¿Cuándo usar docker commit?

**✅ Casos válidos:**

1. **Debugging rápido**: Probar algo temporalmente
2. **Experimentación**: Testear configuraciones
3. **Backup temporal**: Guardar estado antes de cambios arriesgados

**Ejemplo de debugging:**

```bash
# Tu app falla en producción
$ docker commit contenedor_produccion debug:snapshot
$ docker run -it debug:snapshot bash
# Investigas el problema...
```

**❌ NO usar para:**

- Producción
- Compartir con el equipo
- Cualquier cosa que necesite mantenimiento

!!! warning "Resumen"
    `docker commit` es útil para experimentación y debugging, pero **siempre usa Dockerfile** para crear imágenes de producción o que necesites mantener en el tiempo.

### 3. Dockerfile (El método correcto)

Un **Dockerfile** es un archivo de texto que contiene instrucciones para construir una imagen Docker de forma automatizada y reproducible.

**¿Por qué es mejor que docker commit?**

- ✅ **Reproducible**: Cualquiera puede construir la misma imagen
- ✅ **Versionable**: Se guarda en Git con tu código
- ✅ **Documentado**: El archivo ES la documentación
- ✅ **Automatizable**: CI/CD puede construir automáticamente
- ✅ **Mantenible**: Fácil de modificar y actualizar

#### 3.1. Estructura básica (ejemplo comentado)

Vamos a crear un servidor web Nginx paso a paso:

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

**Análisis línea por línea:**

**Línea 1-2: FROM**
```dockerfile
FROM ubuntu:22.04
```
- Primera instrucción (obligatoria)
- Define la imagen base
- Todo lo que hagas se construye SOBRE esta imagen
- `ubuntu:22.04` = Ubuntu versión 22.04 LTS

**Línea 4-5: LABEL**
```dockerfile
LABEL maintainer="tu@email.com"
```
- Metadatos de la imagen (opcional pero recomendado)
- Puedes añadir múltiples labels
- Se puede ver con `docker inspect`

**Línea 7-11: RUN**
```dockerfile
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

**¿Por qué todo en un solo RUN?**

Cada instrucción RUN crea una nueva CAPA en la imagen. Si lo hicieras así:

```dockerfile
# ❌ MAL: Crea 4 capas innecesarias
RUN apt-get update           # Capa 1: 40MB
RUN apt-get install nginx    # Capa 2: 100MB
RUN apt-get clean            # Capa 3: 0MB (pero la capa 2 sigue ocupando)
RUN rm -rf /var/lib/...      # Capa 4: 0MB
```

Resultado: 140MB en la imagen final.

Con un solo RUN:
```dockerfile
# ✅ BIEN: Una sola capa
RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

Resultado: 60MB en la imagen final (eliminó archivos temporales en la misma capa).

**Línea 13-14: COPY**
```dockerfile
COPY index.html /var/www/html/
```
- Copia archivos de tu ordenador a la imagen
- `index.html`: Archivo en el mismo directorio que el Dockerfile
- `/var/www/html/`: Destino dentro de la imagen

**Línea 16-17: EXPOSE**
```dockerfile
EXPOSE 80
```
- **Documenta** qué puertos usa el contenedor
- NO abre el puerto automáticamente
- Es solo informativo (pero importante)

**Línea 19-20: CMD**
```dockerfile
CMD ["nginx", "-g", "daemon off;"]
```
- Comando que se ejecuta al iniciar el contenedor
- Formato JSON (recomendado): `["ejecutable", "param1", "param2"]`
- Solo puede haber UN CMD (si hay varios, solo el último cuenta)

#### 3.2. Construir la imagen

**Paso 1: Crear el Dockerfile**

Crea un directorio de trabajo:

```bash
$ mkdir mi-nginx
$ cd mi-nginx
```

Crea el archivo `Dockerfile` (sin extensión):

```bash
$ nano Dockerfile
# Pega el contenido anterior
```

Crea el archivo `index.html`:

```bash
$ echo "<h1>¡Hola desde mi Dockerfile!</h1>" > index.html
```

**Estructura del directorio:**
```
mi-nginx/
├── Dockerfile
└── index.html
```

**Paso 2: Construir la imagen**

```bash
$ docker build -t mi-nginx:v1 .
[+] Building 45.3s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                      0.0s
 => => transferring dockerfile: 234B                                      0.0s
 => [internal] load .dockerignore                                         0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04           1.2s
 => [1/4] FROM docker.io/library/ubuntu:22.04@sha256:...                  5.3s
 => => resolve docker.io/library/ubuntu:22.04@sha256:...                  0.0s
 => => sha256:... 72.9MB / 72.9MB                                         3.5s
 => [internal] load build context                                         0.0s
 => => transferring context: 52B                                          0.0s
 => [2/4] RUN apt-get update && apt-get install -y nginx...             35.2s
 => [3/4] COPY index.html /var/www/html/                                  0.1s
 => exporting to image                                                    3.3s
 => => exporting layers                                                   3.3s
 => => writing image sha256:abc123def456...                               0.0s
 => => naming to docker.io/library/mi-nginx:v1                            0.0s
```

**Análisis de la salida:**

1. `load build definition`: Lee el Dockerfile
2. `load metadata`: Obtiene info de la imagen base (ubuntu:22.04)
3. `FROM`: Descarga Ubuntu (5.3s)
4. `RUN`: Instala Nginx (35.2s - lo más lento)
5. `COPY`: Copia index.html (0.1s - muy rápido)
6. `exporting`: Guarda la imagen final

**Explicación del comando:**

```bash
$ docker build -t mi-nginx:v1 .
       ↑       ↑     ↑       ↑
       │       │     │       └─ Contexto (directorio actual)
       │       │     └───────── Etiqueta (tag)
       │       └─────────────── Nombre de la imagen
       └─────────────────────── Comando de construcción
```

- `.`: Punto indica el directorio actual como contexto de build
  - Docker envía todos los archivos de este directorio al daemon
  - Por eso el Dockerfile debe estar aquí

**Paso 3: Verificar la imagen**

```bash
$ docker images
REPOSITORY   TAG   IMAGE ID       CREATED         SIZE
mi-nginx     v1    abc123def456   2 minutes ago   168MB
ubuntu       22.04 f63181f19b2f   2 weeks ago     72.9MB
```

**Paso 4: Ejecutar un contenedor**

```bash
$ docker run -d -p 8080:80 --name test_nginx mi-nginx:v1
abc123def456

$ curl http://localhost:8080
<h1>¡Hola desde mi Dockerfile!</h1>
```

¡Funciona perfectamente!

**Ventaja sobre docker commit:**

Si tu compañero quiere la misma imagen:

```bash
# Le envías solo 2 archivos: Dockerfile + index.html
# Él ejecuta:
$ docker build -t mi-nginx:v1 .
# Y obtiene EXACTAMENTE la misma imagen
```

#### 3.3. Instrucciones principales del Dockerfile (explicadas)

##### FROM - La imagen base

```dockerfile
FROM ubuntu:22.04
FROM python:3.11-slim
FROM node:18-alpine
```

**¿Qué hace FROM?**

Define la imagen base sobre la que construir. Es como elegir el "sistema operativo" de tu contenedor.

**Opciones comunes:**

1. **Distribuciones Linux:**
```dockerfile
FROM ubuntu:22.04        # Ubuntu completo (72MB)
FROM debian:11           # Debian (124MB)
FROM alpine:3.18         # Alpine (5MB - muy ligero)
FROM scratch             # Imagen vacía (0MB - para binarios estáticos)
```

2. **Imágenes con lenguajes:**
```dockerfile
FROM python:3.11         # Python 3.11 completo (~900MB)
FROM python:3.11-slim    # Python sin extras (~ 120MB)
FROM python:3.11-alpine  # Python en Alpine (~50MB)
```

3. **Imágenes con servidores:**
```dockerfile
FROM nginx:1.25
FROM node:18
FROM php:8.2-fpm
```

**¿Cuál elegir?**

- **Alpine**: Mínima, rápida, pero puede tener problemas de compatibilidad
- **Slim**: Balance entre tamaño y compatibilidad
- **Completa**: Si necesitas todas las herramientas

**Ejemplo de multi-stage (avanzado):**
```dockerfile
FROM node:18 AS builder   # Etapa de construcción
# ... compilar código ...

FROM nginx:alpine         # Etapa final (solo producción)
COPY --from=builder ...   # Copiar solo lo necesario
```

##### LABEL - Metadatos de la imagen

```dockerfile
LABEL maintainer="admin@ejemplo.com"
LABEL version="1.0"
LABEL description="Mi aplicación web"
```

**¿Para qué sirve LABEL?**

Añade metadatos (información) a la imagen. No afecta al funcionamiento, solo proporciona información.

**Usos comunes:**

```dockerfile
# Información del mantenedor
LABEL maintainer="nombre@empresa.com"

# Versión de la aplicación
LABEL version="2.3.1"

# Descripción
LABEL description="API REST para gestión de usuarios"

# Múltiples labels en una línea
LABEL version="1.0" \
      description="Mi app" \
      author="Tu Nombre"
```

**Ver los labels:**

```bash
$ docker inspect mi-imagen | grep -A 10 Labels
"Labels": {
    "maintainer": "nombre@empresa.com",
    "version": "2.3.1",
    "description": "API REST para gestión de usuarios"
}
```

**Labels útiles para organización:**

```dockerfile
LABEL org.opencontainers.image.authors="equipo@empresa.com"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.created="2024-01-23"
LABEL org.opencontainers.image.source="https://github.com/user/repo"
```

##### RUN - Ejecutar comandos durante construcción

```dockerfile
RUN apt-get update
RUN pip install flask
RUN npm install
```

**¿Qué hace RUN?**

Ejecuta comandos DURANTE la construcción de la imagen (en tiempo de `docker build`).

**⚠️ Concepto importante: CAPAS**

Cada instrucción RUN crea una nueva capa en la imagen. Las capas son inmutables.

**Ejemplo visual:**

```
Imagen final
├── Capa 3: RUN npm install        (100MB)
├── Capa 2: RUN pip install flask  (50MB)
├── Capa 1: RUN apt-get update     (40MB)
└── Capa 0: FROM ubuntu            (72MB)
Total: 262MB
```

**❌ MAL - Múltiples RUN separados:**

```dockerfile
FROM ubuntu:22.04

RUN apt-get update                    # Capa 1: 40MB
RUN apt-get install -y nginx          # Capa 2: 100MB  
RUN apt-get clean                     # Capa 3: 0MB
RUN rm -rf /var/lib/apt/lists/*       # Capa 4: 0MB

# Problema: Las capas 2, 3 y 4 ocupan 100MB
# Aunque limpies en capas posteriores, la capa 2 sigue ahí
```

**✅ BIEN - Un solo RUN combinado:**

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Una sola capa que ocupa solo 60MB
# Los archivos temporales se eliminan en la MISMA capa
```

**Formato de RUN:**

1. **Shell form** (usa `/bin/sh -c`):
```dockerfile
RUN apt-get update
RUN echo "Hola" > /tmp/archivo.txt
```

2. **Exec form** (no usa shell):
```dockerfile
RUN ["apt-get", "update"]
RUN ["/bin/bash", "-c", "echo Hola"]
```

**Buenas prácticas con RUN:**

```dockerfile
# ✅ Ordenar paquetes alfabéticamente (fácil de mantener)
RUN apt-get update && apt-get install -y \
    curl \
    git \
    nginx \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# ✅ Usar && para que falle si algo sale mal
RUN cd /app && npm install  # Si cd falla, no ejecuta npm install

# ❌ Sin && puede ejecutar en lugar equivocado
RUN cd /app
RUN npm install  # Esto se ejecuta donde sea que esté, no necesariamente en /app

# ✅ Usar cache de APT para acelerar builds
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && apt-get install -y nginx
```

**Ejemplo completo Python:**

```dockerfile
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Instalar paquetes Python
RUN pip install --no-cache-dir \
    flask==2.3.0 \
    psycopg2-binary==2.9.5 \
    gunicorn==20.1.0
```

**¿Por qué `--no-cache-dir` en pip?**

Sin `--no-cache-dir`, pip guarda archivos de caché que ocupan espacio innecesario en la imagen.

##### COPY - Copiar archivos a la imagen

```dockerfile
COPY app.py /app/
COPY . /app/
COPY --chown=www-data:www-data html/ /var/www/html/
```

**¿Qué hace COPY?**

Copia archivos/directorios de tu ordenador (contexto de build) a la imagen.

**Sintaxis:**
```dockerfile
COPY <origen> <destino>
```

- `<origen>`: Ruta relativa al directorio donde está el Dockerfile
- `<destino>`: Ruta absoluta dentro de la imagen

**Ejemplos prácticos:**

```dockerfile
# Copiar un archivo
COPY app.py /usr/src/app/app.py

# Copiar con nombre diferente
COPY config.yml /etc/myapp/config.yaml

# Copiar directorio completo
COPY src/ /usr/src/app/

# Copiar todo el directorio actual
COPY . /usr/src/app/

# Copiar múltiples archivos
COPY requirements.txt package.json /app/

# Copiar con permisos de usuario específico
COPY --chown=www-data:www-data html/ /var/www/html/
```

**¿Qué es el contexto de build?**

```
mi-proyecto/
├── Dockerfile       ← Aquí estamos
├── app.py
├── requirements.txt
└── src/
    ├── main.py
    └── utils.py
```

```bash
$ docker build -t mi-app .
                        ↑
                    Contexto = directorio actual
```

**Rutas relativas al contexto:**

```dockerfile
COPY app.py /app/              # Copia mi-proyecto/app.py
COPY src/main.py /app/         # Copia mi-proyecto/src/main.py
COPY ../fuera.txt /app/        # ❌ ERROR: No puede copiar fuera del contexto
```

**Usar .dockerignore:**

Crea un archivo `.dockerignore` para excluir archivos:

```
# .dockerignore
node_modules/
.git/
*.log
.env
__pycache__/
```

Esto acelera el build porque Docker no envía estos archivos al daemon.

**Orden importa (caché):**

```dockerfile
# ❌ MAL: Invalida caché cada vez que cambias código
COPY . /app/
RUN pip install -r requirements.txt

# ✅ BIEN: Solo invalida caché si cambian dependencias
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app/
```

**¿Por qué es mejor?**

1. Build inicial:
   - COPY requirements.txt ✓
   - RUN pip install ✓ (tarda 2 min)
   - COPY . ✓

2. Cambias código (NO requirements.txt):
   - COPY requirements.txt ✓ (usa caché)
   - RUN pip install ✓ (usa caché - no tarda nada)
   - COPY . ✓ (copia nuevo código)

##### ADD - COPY con superpoderes

```dockerfile
ADD archivo.tar.gz /app/  # Descomprime automáticamente
ADD https://ejemplo.com/file.txt /tmp/  # Descarga URLs
```

**Diferencias entre COPY y ADD:**

| Característica | COPY | ADD |
|----------------|------|-----|
| Copiar archivos locales | ✅ | ✅ |
| Descomprimir tar.gz | ❌ | ✅ |
| Descargar URLs | ❌ | ✅ |
| Simplicidad | ✅ | ❌ |
| Recomendado | ✅ | Solo si necesitas sus features |

**Ejemplo ADD descomprimiendo:**

```dockerfile
# Tienes archivo.tar.gz en tu directorio
ADD archivo.tar.gz /app/

# ADD automáticamente:
# 1. Copia el archivo
# 2. Lo descomprime
# 3. El resultado queda en /app/
```

**Ejemplo ADD descargando URL:**

```dockerfile
ADD https://github.com/user/repo/releases/download/v1.0/app.tar.gz /tmp/
```

!!! warning "No se descomprime desde URL"
    ADD solo descomprime archivos locales, NO archivos descargados de URLs.

**¿Cuándo usar ADD?**

```dockerfile
# ✅ Cuando necesites descomprimir
ADD app.tar.gz /usr/src/app/

# ❌ Para copiar archivos normales usa COPY
COPY app.py /usr/src/app/  # Más claro

# ❌ Para descargar URLs, mejor RUN con curl
RUN curl -L https://ejemplo.com/file.tar.gz | tar -xz -C /app/
```

!!! tip "Regla de oro"
    **Usa COPY** a menos que específicamente necesites descomprimir archivos locales con ADD.

##### WORKDIR - Directorio de trabajo

```dockerfile
WORKDIR /app
RUN python setup.py install  # Se ejecuta en /app
```

**¿Qué hace WORKDIR?**

Establece el directorio de trabajo para las instrucciones que vienen después (RUN, CMD, ENTRYPOINT, COPY, ADD).

**Es como hacer `cd` pero mejor:**

```dockerfile
# ❌ MAL: Usar RUN cd
RUN cd /app
RUN ls  # Esto NO está en /app, está donde estaba antes

# ✅ BIEN: Usar WORKDIR
WORKDIR /app
RUN ls  # Esto SÍ está en /app
```

**Ejemplo completo:**

```dockerfile
FROM node:18

# Crear y establecer directorio de trabajo
WORKDIR /usr/src/app

# Ahora COPY copia relativo a /usr/src/app
COPY package*.json ./

# RUN se ejecuta en /usr/src/app
RUN npm install

# COPY también usa /usr/src/app
COPY . .

# CMD se ejecuta en /usr/src/app
CMD ["node", "server.js"]
```

**WORKDIR crea el directorio si no existe:**

```dockerfile
WORKDIR /esta/ruta/no/existe/aun
# Docker automáticamente crea toda la estructura
```

**Usar múltiples WORKDIR:**

```dockerfile
WORKDIR /app
WORKDIR src      # Ahora estás en /app/src
WORKDIR ../test  # Ahora estás en /app/test
```

**¿Dónde estás si no usas WORKDIR?**

```dockerfile
FROM ubuntu:22.04
RUN pwd  # Muestra: /
```

Por defecto estás en la raíz (`/`).

##### ENV - Variables de entorno

```dockerfile
ENV APP_HOME=/app
ENV PORT=8080
ENV PYTHONUNBUFFERED=1
```

**¿Qué hace ENV?**

Define variables de entorno que estarán disponibles:
- Durante el build (en instrucciones posteriores)
- En el contenedor cuando se ejecute

**Sintaxis:**

```dockerfile
# Una variable por línea
ENV MI_VARIABLE=valor

# Múltiples variables
ENV VAR1=valor1 \
    VAR2=valor2 \
    VAR3=valor3
```

**Usar variables definidas:**

```dockerfile
ENV APP_DIR=/usr/src/app
ENV CONFIG_DIR=/etc/myapp

WORKDIR ${APP_DIR}
COPY config.yml ${CONFIG_DIR}/
```

**Ejemplos por lenguaje:**

**Python:**
```dockerfile
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1
```

- `PYTHONUNBUFFERED=1`: Logs en tiempo real
- `PYTHONDONTWRITEBYTECODE=1`: No crear archivos .pyc
- `PIP_NO_CACHE_DIR=1`: Pip sin caché (imagen más pequeña)

**Node.js:**
```dockerfile
ENV NODE_ENV=production \
    NPM_CONFIG_LOGLEVEL=warn
```

**Java:**
```dockerfile
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64 \
    PATH=$JAVA_HOME/bin:$PATH
```

**Modificar PATH:**

```dockerfile
ENV PATH=/usr/local/bin:$PATH
# Añade /usr/local/bin al principio del PATH
```

**Diferencia entre ENV en Dockerfile y -e en docker run:**

```dockerfile
# Dockerfile - valor por defecto
ENV DATABASE_HOST=localhost
```

```bash
# docker run - sobrescribe el valor
$ docker run -e DATABASE_HOST=production-db mi-app
```

**Ver variables en el contenedor:**

```bash
$ docker run mi-app env
PATH=/usr/local/bin:/usr/bin:/bin
APP_HOME=/app
PORT=8080
...
```

##### EXPOSE - Documentar puertos

```dockerfile
EXPOSE 80
EXPOSE 443
EXPOSE 8080/tcp
EXPOSE 53/udp
```

**¿Qué hace EXPOSE?**

⚠️ **IMPORTANTE**: EXPOSE NO abre puertos, solo los DOCUMENTA.

**Lo que EXPOSE hace:**

```dockerfile
EXPOSE 80
```

Es equivalente a escribir un comentario:

```dockerfile
# Esta aplicación usa el puerto 80
```

**Lo que EXPOSE NO hace:**

```bash
# Esto NO funciona solo con EXPOSE:
$ docker run mi-app
# No puedes acceder al puerto 80 desde tu navegador
```

**Para realmente exponer el puerto:**

```bash
$ docker run -p 8080:80 mi-app
              ↑
        Esto SÍ expone el puerto
```

**¿Entonces para qué sirve EXPOSE?**

1. **Documentación**: Indica qué puertos usa la app
2. **Con -P**: Mapea automáticamente puertos

```bash
$ docker run -P mi-app
# Docker automáticamente mapea TODOS los puertos en EXPOSE
# a puertos aleatorios del host
```

```bash
$ docker ps
PORTS
0.0.0.0:49153->80/tcp   # EXPOSE 80 mapeado a 49153
0.0.0.0:49154->443/tcp  # EXPOSE 443 mapeado a 49154
```

**Sintaxis:**

```dockerfile
EXPOSE 80            # Por defecto TCP
EXPOSE 80/tcp        # Explícitamente TCP
EXPOSE 53/udp        # UDP
EXPOSE 8080-8090     # Rango de puertos
```

**Ejemplo completo:**

```dockerfile
FROM nginx:alpine

# Documentar que usa puerto 80 (HTTP) y 443 (HTTPS)
EXPOSE 80 443

# Para usarlo:
# docker run -p 8080:80 -p 8443:443 mi-nginx
```

**Buena práctica:**

Aunque EXPOSE no sea técnicamente necesario, úsalo siempre para documentar:

```dockerfile
FROM node:18
WORKDIR /app
COPY . .
RUN npm install

# Documentar que la app usa puerto 3000
EXPOSE 3000

CMD ["node", "server.js"]
```

Cuando alguien use tu imagen, sabrá qué puerto necesita mapear.

##### VOLUME - Puntos de montaje

```dockerfile
VOLUME /data
VOLUME ["/var/log", "/var/db"]
```

**¿Qué hace VOLUME?**

Define directorios que deben persistir fuera del contenedor.

**Ejemplo:**

```dockerfile
FROM postgres:15
VOLUME /var/lib/postgresql/data
```

Cuando ejecutes el contenedor, Docker creará automáticamente un volumen para ese directorio.

```bash
$ docker run -d postgres
$ docker volume ls
DRIVER    VOLUME NAME
local     abc123def456...  # Volumen anónimo creado automáticamente
```

**Es mejor usar volúmenes nombrados en docker run:**

```bash
$ docker run -v pg_data:/var/lib/postgresql/data postgres
```

##### USER - Cambiar usuario

```dockerfile
USER www-data
RUN whoami  # Ejecuta como www-data
```

**¿Qué hace USER?**

Cambia el usuario para instrucciones posteriores y para cuando se ejecute el contenedor.

**¿Por qué es importante?**

Por defecto, los contenedores ejecutan como `root`. Esto es un riesgo de seguridad.

**❌ MAL (ejecuta como root):**
```dockerfile
FROM node:18
WORKDIR /app
COPY . .
CMD ["node", "server.js"]  # Ejecuta como root
```

**✅ BIEN (ejecuta como usuario sin privilegios):**
```dockerfile
FROM node:18

# Crear usuario
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app
COPY . .
RUN chown -R appuser:appuser /app

# Cambiar a usuario sin privilegios
USER appuser

CMD ["node", "server.js"]  # Ejecuta como appuser
```

**Ejemplo Python:**
```dockerfile
FROM python:3.11-slim

RUN useradd -m -u 1000 appuser

WORKDIR /app
COPY --chown=appuser:appuser . .

USER appuser
CMD ["python", "app.py"]
```

##### CMD - Comando por defecto

```dockerfile
CMD ["python", "app.py"]
CMD ["nginx", "-g", "daemon off;"]
```

**¿Qué hace CMD?**

Define el comando que se ejecuta cuando inicias el contenedor (si no especificas otro).

**Formatos:**

```dockerfile
# Exec form (recomendado)
CMD ["ejecutable", "param1", "param2"]

# Shell form
CMD comando param1 param2
```

**Ejemplo:**

```dockerfile
FROM ubuntu:22.04
CMD ["echo", "Hola desde CMD"]
```

```bash
$ docker run mi-imagen
Hola desde CMD

$ docker run mi-imagen echo "Otro mensaje"
Otro mensaje  # CMD se reemplaza
```

**Solo puede haber UN CMD:**

```dockerfile
CMD ["echo", "uno"]
CMD ["echo", "dos"]  # Este es el que cuenta
```

##### ENTRYPOINT - Punto de entrada

```dockerfile
ENTRYPOINT ["python"]
CMD ["app.py"]  # Argumento por defecto
```

**¿Diferencia entre CMD y ENTRYPOINT?**

- **CMD**: Fácil de sobrescribir
- **ENTRYPOINT**: Difícil de sobrescribir (punto de entrada fijo)

**Ejemplo CMD:**
```dockerfile
FROM ubuntu:22.04
CMD ["echo", "Hola"]
```

```bash
$ docker run mi-imagen
Hola

$ docker run mi-imagen ls  # Fácil sobrescribir
bin  boot  dev  etc...
```

**Ejemplo ENTRYPOINT:**
```dockerfile
FROM ubuntu:22.04
ENTRYPOINT ["echo"]
CMD ["Hola"]
```

```bash
$ docker run mi-imagen
Hola

$ docker run mi-imagen "Adiós"
Adiós  # Solo cambias el argumento, no el comando
```

**Patrón ENTRYPOINT + CMD:**

```dockerfile
FROM python:3.11-slim
COPY app.py /app/
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]
```

```bash
# Ejecuta: python app.py
$ docker run mi-imagen

# Ejecuta: python otro.py
$ docker run mi-imagen otro.py

# Ejecuta: python -m pytest
$ docker run mi-imagen -m pytest
```

**Caso de uso real - Script wrapper:**

```dockerfile
FROM postgres:15

COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["postgres"]
```

El script puede hacer inicialización antes de ejecutar postgres.

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
