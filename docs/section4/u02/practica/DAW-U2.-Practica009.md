---
title: "UD 2 - P9: Construcción de imagen Docker con página web estática"
description: "Creación de imágenes Docker personalizadas para servidor web estático"
summary: "Actividad práctica para crear imágenes Docker desde diferentes bases y desplegar una página web estática."
authors:
    - Eduardo Fdez
date: 2025-01-13
icon: "material/file-document-edit"
permalink: /daw/unidad2/p2.9
categories:
    - DAW
tags:
    - Docker
    - Dockerfile
    - Imágenes
    - Apache
    - Nginx
    - Web estática
---

## Relación 2.9

### Descripción

**Actividad:** *Construcción de imágenes Docker con página web estática*

En esta práctica aprenderás a crear tus propias imágenes Docker personalizadas utilizando Dockerfiles. Crearás tres versiones diferentes de una imagen para servir una página web estática, cada una partiendo de una imagen base diferente.

#### Objetivo general

Aprender a:

- Escribir Dockerfiles para crear imágenes personalizadas.
- Utilizar diferentes imágenes base según las necesidades.
- Comprender la diferencia entre imágenes base de SO vs. imágenes de servicio.
- Gestionar el contexto de construcción de imágenes.
- Optimizar el tamaño de las imágenes Docker.
- Construir y etiquetar imágenes personalizadas.

---

### Contexto de trabajo

En Docker, las imágenes se crean a partir de un archivo llamado **Dockerfile** que contiene instrucciones para construir la imagen. El directorio donde se encuentra el Dockerfile y los archivos necesarios se llama **contexto de construcción**.

**Conceptos clave:**

- **Imagen base:** Imagen de partida sobre la que construyes tu imagen personalizada
- **Dockerfile:** Archivo con instrucciones para construir la imagen
- **Contexto:** Directorio con los archivos necesarios para la construcción
- **Capas:** Cada instrucción del Dockerfile crea una capa en la imagen

**Páginas web a usar:**

Para esta práctica, crea una página HTML simple en un directorio llamado `public_html`:

**Archivo `public_html/index.html`:**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Docker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        .info {
            background-color: #e3f2fd;
            padding: 15px;
            border-left: 4px solid #2196F3;
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>¡Bienvenido a mi servidor Docker!</h1>
        <div class="info">
            <p><strong>Servidor:</strong> <span id="server">Cargando...</span></p>
            <p><strong>Versión:</strong> <span id="version">Versión 1</span></p>
        </div>
        <p>Esta página está siendo servida desde un contenedor Docker que he creado yo mismo.</p>
        <p>Práctica de construcción de imágenes Docker - Módulo DAW</p>
    </div>
    
    <script>
        // Detectar el servidor
        document.getElementById('server').textContent = window.location.hostname;
    </script>
</body>
</html>
```

---

### 🔹 Parte 1: Imagen desde sistema operativo base (Debian)

#### Tarea 1.1: Preparación del contexto

1. Crea un directorio para esta versión: `~/imagen_web_v1`.

2. Dentro del directorio, crea:
   
    - Un directorio `public_html` con el archivo `index.html` proporcionado
    - Un archivo `Dockerfile` (lo crearás en la siguiente tarea)

3. Verifica la estructura:
   
    ```
    imagen_web_v1/
    ├── Dockerfile
    └── public_html/
        └── index.html
    ```

#### Tarea 1.2: Creación del Dockerfile desde Debian

1. Investiga la sintaxis básica de un Dockerfile consultando la documentación oficial.

2. Crea un archivo `Dockerfile` que:
   
    - Use como imagen base `debian:stable-slim`
    - Actualice los repositorios e instale Apache2
    - Limpie la caché de apt para reducir el tamaño de la imagen
    - Establezca `/var/www/html/` como directorio de trabajo
    - Copie el contenido de `public_html` al directorio de trabajo
    - Exponga el puerto 80
    - Defina el comando para iniciar Apache en primer plano

3. **Pistas sobre instrucciones Dockerfile:**
   
    - `FROM` - Define la imagen base
    - `RUN` - Ejecuta comandos durante la construcción
    - `WORKDIR` - Establece el directorio de trabajo
    - `COPY` - Copia archivos del contexto a la imagen
    - `EXPOSE` - Documenta qué puerto usa el contenedor
    - `CMD` - Comando que se ejecuta al iniciar el contenedor

4. **Para Apache:**
   
    - Paquete a instalar: `apache2`
    - Comando para iniciar: `apache2ctl -D FOREGROUND`
    - Directorio web: `/var/www/html/`

#### Tarea 1.3: Construcción y prueba de la imagen

1. Investiga el comando de Docker para construir imágenes desde un Dockerfile.

2. Construye la imagen con:
   
    - Nombre: `tu_usuario/web_estatica`
    - Etiqueta: `v1`

3. Verifica que la imagen se ha creado correctamente.

4. Anota el tamaño de la imagen.

5. Crea un contenedor desde tu imagen:
   
    - Mapea el puerto 80 del contenedor al puerto 8080 del host
    - Nombre del contenedor: `web_v1`

6. Accede desde el navegador y verifica que funciona.

7. **Preguntas de reflexión:**
   
    - ¿Cuánto ocupa la imagen?
    - ¿Por qué es importante limpiar la caché de apt?
    - ¿Qué diferencia hay entre CMD y RUN?

---

### 🔹 Parte 2: Imagen desde Apache

#### Tarea 2.1: Dockerfile desde imagen de Apache

1. Crea un nuevo directorio: `~/imagen_web_v2`.

2. Copia el directorio `public_html` en este nuevo directorio.

3. Crea un nuevo `Dockerfile` que:
   
    - Use como imagen base `httpd:2.4`
    - Copie el contenido de `public_html` al DocumentRoot de Apache
    - Exponga el puerto 80

4. **Información de la imagen httpd:**
   
    - DocumentRoot: `/usr/local/apache2/htdocs/`
    - No necesitas instalar nada (ya tiene Apache)
    - No necesitas especificar CMD (hereda el de la imagen base)

#### Tarea 2.2: Construcción y comparación

1. Construye la nueva imagen:
   
    - Nombre: `tu_usuario/web_estatica`
    - Etiqueta: `v2`

2. Compara el tamaño de esta imagen con la versión 1.

3. Crea un contenedor:
   
    - Puerto 8081 del host → puerto 80 del contenedor
    - Nombre: `web_v2`

4. Verifica que funciona correctamente.

5. **Preguntas de análisis:**
   
    - ¿Qué imagen es más pequeña? ¿Por qué?
    - ¿Qué ventajas tiene usar una imagen especializada?
    - ¿Cuántas líneas tiene cada Dockerfile?

---

### 🔹 Parte 3: Imagen desde Nginx

#### Tarea 3.1: Dockerfile desde imagen de Nginx

1. Crea un nuevo directorio: `~/imagen_web_v3`.

2. Copia el directorio `public_html` en este nuevo directorio.

3. Crea un nuevo `Dockerfile` que:
   
    - Use como imagen base `nginx:1.24`
    - Copie el contenido de `public_html` al directorio web de Nginx
    - Exponga el puerto 80

4. **Información de la imagen nginx:**
   
    - Directorio web: `/usr/share/nginx/html`
    - No necesitas instalar nada
    - No necesitas especificar CMD

#### Tarea 3.2: Construcción y comparación final

1. Construye la imagen:
   
    - Nombre: `tu_usuario/web_estatica`
    - Etiqueta: `v3`

2. Crea un contenedor:
   
    - Puerto 8082 del host → puerto 80 del contenedor
    - Nombre: `web_v3`

3. Verifica que funciona.

4. Lista todas tus imágenes y compara los tamaños.

5. **Tabla comparativa:**

| Aspecto | Versión 1 (Debian) | Versión 2 (httpd) | Versión 3 (nginx) |
|---------|-------------------|-------------------|-------------------|
| Imagen base | | | |
| Tamaño imagen | | | |
| Líneas Dockerfile | | | |
| Paquetes instalados | | | |
| Tiempo construcción | | | |

---

### 🔹 Parte 4: Optimización y buenas prácticas

#### Tarea 4.1: Inspección de imágenes

1. Investiga cómo ver el historial de capas de una imagen.

2. Examina el historial de cada una de tus tres imágenes.

3. Identifica qué instrucciones crean las capas más grandes.

#### Tarea 4.2: Buenas prácticas

Investiga y documenta:

1. **Multi-stage builds:**
   
    - ¿Qué son?
    - ¿Para qué se usan?
    - ¿Cómo ayudan a reducir el tamaño?

2. **Orden de instrucciones:**
   
    - ¿Por qué es importante el orden de las instrucciones?
    - ¿Qué es la caché de capas?
    - ¿Cómo aprovechar la caché para construcciones más rápidas?

3. **Seguridad:**
   
    - ¿Por qué no ejecutar como root?
    - ¿Cómo especificar un usuario diferente?
    - ¿Por qué son importantes las imágenes slim/alpine?

#### Tarea 4.3: Dockerfile mejorado

Crea una cuarta versión (v4) del Dockerfile que incorpore:

- Uso de imagen alpine (nginx:alpine)
- Metadatos con LABEL
- Usuario no root
- Mejor gestión de capas

---

### 🔹 Parte 5: Gestión de imágenes

#### Tarea 5.1: Operaciones con imágenes

Practica los siguientes comandos (investiga la sintaxis):

1. **Listar imágenes:**
   
    - Todas las imágenes
    - Solo las tuyas (filtro por nombre)
    - Con formato personalizado

2. **Eliminar imágenes:**
   
    - Eliminar una imagen específica
    - Eliminar imágenes sin usar (dangling)
    - Eliminar todas las imágenes de un repositorio

3. **Etiquetar imágenes:**
   
    - Crear nuevas etiquetas
    - Cambiar la etiqueta de una imagen
    - Usar tags con números de versión

4. **Inspeccionar imágenes:**
   
    - Ver la configuración completa
    - Ver solo ciertos campos
    - Ver el historial de construcción

#### Tarea 5.2: Exportar e importar

1. Investiga cómo guardar una imagen en un archivo tar.

2. Exporta tu mejor imagen a un archivo.

3. Elimina la imagen original.

4. Importa la imagen desde el archivo tar.

5. Verifica que funciona correctamente.

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Los 3 (o 4) archivos Dockerfile creados
    - Todos los comandos de Docker utilizados
    - Capturas de pantalla:
        - Construcción de cada imagen
        - Listado de imágenes con tamaños
        - Página web funcionando desde cada versión
        - Historial de capas de las imágenes
    - Tabla comparativa completa
    - Respuestas a todas las preguntas de reflexión
    - Documentación sobre buenas prácticas

2. **Archivos del proyecto:**
   
    - Directorio `public_html` con index.html
    - Dockerfile de cada versión (v1, v2, v3, v4)
    - Script de construcción automatizada (opcional)

---

### Evaluación

Se evaluará:

- Correcta sintaxis de los Dockerfiles.
- Funcionamiento de las imágenes creadas.
- Comprensión de diferencias entre imágenes base.
- Análisis comparativo de tamaños y complejidad.
- Aplicación de buenas prácticas.
- Documentación clara y completa.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Documentación oficial de Dockerfile: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
- Best practices para Dockerfiles: [https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)
- Imagen oficial de Apache: [https://hub.docker.com/_/httpd](https://hub.docker.com/_/httpd)
- Imagen oficial de Nginx: [https://hub.docker.com/_/nginx](https://hub.docker.com/_/nginx)
- Imagen oficial de Debian: [https://hub.docker.com/_/debian](https://hub.docker.com/_/debian)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.9.-ImagenesEstaticas.html){ .md-button }
