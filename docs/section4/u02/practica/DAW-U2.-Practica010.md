---
title: "UD 2 - P10: Construcción de imagen Docker con aplicación PHP"
description: "Creación de imágenes Docker para aplicaciones PHP dinámicas"
summary: "Actividad práctica para crear imágenes Docker con PHP y desplegar aplicaciones dinámicas."
authors:
    - Eduardo Fdez
date: 2025-01-13
icon: "material/file-document-edit"
permalink: /daw/unidad2/p2.10
categories:
    - DAW
tags:
    - Docker
    - Dockerfile
    - PHP
    - Apache
    - Imágenes
---

## Relación 2.10

### Descripción

**Actividad:** *Construcción de imágenes Docker con aplicación PHP*

En esta práctica crearás imágenes Docker personalizadas para servir aplicaciones PHP dinámicas. Crearás dos versiones: una desde un sistema operativo base instalando todos los componentes, y otra desde una imagen especializada de PHP.

#### Objetivo general

Aprender a:

- Construir imágenes para aplicaciones dinámicas con PHP.
- Instalar y configurar PHP en imágenes Docker.
- Utilizar imágenes especializadas de PHP.
- Gestionar extensiones de PHP en Docker.
- Comparar diferentes enfoques de construcción de imágenes.

---

### Contexto de trabajo

PHP es un lenguaje de programación del lado del servidor muy utilizado para desarrollo web. Requiere un servidor web (como Apache o Nginx) y el intérprete de PHP instalado.

**Aplicación de ejemplo:**

Usa esta sencilla aplicación PHP en un directorio llamado `app`:

**Archivo `app/index.php`:**
```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Aplicación PHP en Docker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background-color: rgba(255, 255, 255, 0.95);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            color: #333;
        }
        h1 {
            color: #667eea;
            text-align: center;
        }
        .info-box {
            background-color: #f0f0f0;
            padding: 15px;
            margin: 15px 0;
            border-radius: 8px;
            border-left: 4px solid #667eea;
        }
        .php-info {
            background-color: #e3f2fd;
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background-color: #667eea;
            color: white;
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            margin: 10px 5px;
        }
        .btn:hover {
            background-color: #764ba2;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐘 Mi Aplicación PHP en Docker</h1>
        
        <div class="info-box">
            <h2>Información del Sistema</h2>
            <div class="php-info">
                <p><strong>Versión de PHP:</strong> <?php echo phpversion(); ?></p>
                <p><strong>Sistema Operativo:</strong> <?php echo PHP_OS; ?></p>
                <p><strong>Servidor Web:</strong> <?php echo $_SERVER['SERVER_SOFTWARE']; ?></p>
                <p><strong>Fecha y Hora del Servidor:</strong> <?php echo date('Y-m-d H:i:s'); ?></p>
            </div>
        </div>

        <div class="info-box">
            <h2>Extensiones PHP Cargadas</h2>
            <p>Total de extensiones: <strong><?php echo count(get_loaded_extensions()); ?></strong></p>
            <details>
                <summary>Ver todas las extensiones</summary>
                <ul style="columns: 3; list-style-type: none;">
                    <?php 
                    $extensions = get_loaded_extensions();
                    sort($extensions);
                    foreach($extensions as $ext) {
                        echo "<li>✓ $ext</li>";
                    }
                    ?>
                </ul>
            </details>
        </div>

        <div class="info-box">
            <h2>Variables del Servidor</h2>
            <table>
                <thead>
                    <tr>
                        <th>Variable</th>
                        <th>Valor</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>DOCUMENT_ROOT</td>
                        <td><?php echo $_SERVER['DOCUMENT_ROOT']; ?></td>
                    </tr>
                    <tr>
                        <td>SERVER_ADDR</td>
                        <td><?php echo $_SERVER['SERVER_ADDR'] ?? 'N/A'; ?></td>
                    </tr>
                    <tr>
                        <td>SERVER_PORT</td>
                        <td><?php echo $_SERVER['SERVER_PORT']; ?></td>
                    </tr>
                    <tr>
                        <td>REMOTE_ADDR</td>
                        <td><?php echo $_SERVER['REMOTE_ADDR']; ?></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div style="text-align: center; margin-top: 20px;">
            <a href="info.php" class="btn">Ver phpinfo() completo</a>
            <a href="test.php" class="btn">Probar funciones PHP</a>
        </div>

        <p style="text-align: center; margin-top: 30px; color: #888;">
            <small>Práctica de Docker - Construcción de Imágenes con PHP</small>
        </p>
    </div>
</body>
</html>
```

**Archivo `app/info.php`:**
```php
<?php
phpinfo();
?>
```

**Archivo `app/test.php`:**
```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Test de Funciones PHP</title>
    <style>
        body { font-family: Arial; max-width: 800px; margin: 50px auto; padding: 20px; }
        .test { background: #f0f0f0; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .success { border-left: 4px solid #4CAF50; }
        .info { border-left: 4px solid #2196F3; }
        h1 { color: #333; }
        pre { background: #263238; color: #aed581; padding: 10px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>Pruebas de Funciones PHP</h1>
    
    <div class="test success">
        <h3>✓ Cálculo Matemático</h3>
        <p>Resultado de 15 + 27 * 3 = <strong><?php echo 15 + 27 * 3; ?></strong></p>
    </div>

    <div class="test success">
        <h3>✓ Manipulación de Cadenas</h3>
        <?php
        $texto = "Docker y PHP funcionando perfectamente";
        echo "<p>Texto original: $texto</p>";
        echo "<p>En mayúsculas: " . strtoupper($texto) . "</p>";
        echo "<p>Longitud: " . strlen($texto) . " caracteres</p>";
        ?>
    </div>

    <div class="test success">
        <h3>✓ Trabajo con Arrays</h3>
        <?php
        $tecnologias = array("Docker", "PHP", "Apache", "MySQL", "Linux");
        echo "<p>Tecnologías: " . implode(", ", $tecnologias) . "</p>";
        echo "<p>Total: " . count($tecnologias) . " tecnologías</p>";
        ?>
    </div>

    <div class="test info">
        <h3>ℹ Información del Entorno</h3>
        <pre><?php
        echo "PHP Version: " . PHP_VERSION . "\n";
        echo "Zend Engine: " . zend_version() . "\n";
        echo "Memory Limit: " . ini_get('memory_limit') . "\n";
        echo "Max Execution Time: " . ini_get('max_execution_time') . "s\n";
        echo "Upload Max Filesize: " . ini_get('upload_max_filesize') . "\n";
        ?></pre>
    </div>

    <div class="test info">
        <h3>ℹ Fecha y Hora</h3>
        <?php
        date_default_timezone_set('Europe/Madrid');
        echo "<p>Fecha actual: " . date('d/m/Y') . "</p>";
        echo "<p>Hora actual: " . date('H:i:s') . "</p>";
        echo "<p>Día de la semana: " . date('l') . "</p>";
        ?>
    </div>

    <div style="text-align: center; margin-top: 20px;">
        <a href="index.php" style="padding: 10px 20px; background: #667eea; color: white; text-decoration: none; border-radius: 5px;">Volver al inicio</a>
    </div>
</body>
</html>
```

---

### 🔹 Parte 1: Imagen desde Debian (instalando PHP)

#### Tarea 1.1: Preparación del contexto

1. Crea un directorio para esta versión: `~/imagen_php_v1`.

2. Dentro crea un directorio `app` con los tres archivos PHP proporcionados:
   
    - `index.php`
    - `info.php`
    - `test.php`

3. Verifica la estructura:
   
    ```
    imagen_php_v1/
    ├── Dockerfile
    └── app/
        ├── index.php
        ├── info.php
        └── test.php
    ```

#### Tarea 1.2: Creación del Dockerfile desde Debian

1. Investiga qué paquetes necesitas instalar en Debian para:
   
    - Servidor web Apache
    - PHP y su módulo para Apache
    - Librerías de PHP necesarias

2. Crea un `Dockerfile` que:
   
    - Use como imagen base `debian:stable-slim`
    - Actualice repositorios e instale Apache2 y PHP
    - Elimine el `index.html` por defecto de Apache
    - Limpie la caché de apt
    - Copie los archivos de `app/` al DocumentRoot de Apache
    - Exponga el puerto 80
    - Inicie Apache en primer plano

3. **Información útil:**
   
    - Paquetes Debian para PHP: `apache2`, `libapache2-mod-php`, `php`
    - DocumentRoot de Apache en Debian: `/var/www/html/`
    - Archivo index por defecto: `/var/www/html/index.html`

#### Tarea 1.3: Construcción y prueba

1. Construye la imagen:
   
    - Nombre: `tu_usuario/app_php`
    - Etiqueta: `v1`

2. Anota el tamaño de la imagen y el tiempo de construcción.

3. Crea un contenedor:
   
    - Puerto 8080 del host
    - Nombre: `php_app_v1`

4. Accede desde el navegador a:
   
    - `http://localhost:8080/` - Página principal
    - `http://localhost:8080/info.php` - Información de PHP
    - `http://localhost:8080/test.php` - Pruebas de PHP

5. Observa la versión de PHP que se instaló.

---

### 🔹 Parte 2: Imagen desde PHP oficial

#### Tarea 2.1: Uso de imagen especializada de PHP

1. Crea un nuevo directorio: `~/imagen_php_v2`.

2. Copia el directorio `app` en este nuevo directorio.

3. Investiga en Docker Hub la imagen oficial de PHP:
   
    - ¿Qué variantes existen?
    - ¿Cuál incluye Apache integrado?
    - ¿Qué versión de PHP usar?

4. Crea un `Dockerfile` que:
   
    - Use como imagen base `php:7.4-apache` o `php:8.2-apache`
    - Copie los archivos de app al DocumentRoot de Apache
    - Exponga el puerto 80

5. **Información de la imagen PHP:**
   
    - DocmentRoot: `/var/www/html/`
    - Apache ya está configurado y funcionando
    - No necesitas instalar nada adicional para funcionalidad básica
    - No necesitas especificar CMD

#### Tarea 2.2: Construcción y comparación

1. Construye la imagen:
   
    - Nombre: `tu_usuario/app_php`
    - Etiqueta: `v2`

2. Compara el tamaño con la versión 1.

3. Crea un contenedor:
   
    - Puerto 8081 del host
    - Nombre: `php_app_v2`

4. Accede y verifica que funciona.

5. Compara la versión de PHP entre ambas imágenes.

6. **Preguntas de análisis:**
   
    - ¿Qué Dockerfile es más sencillo?
    - ¿Qué imagen es más grande? ¿Por qué?
    - ¿Cuál se construyó más rápido?
    - ¿Qué versión de PHP tiene cada una?

---

### 🔹 Parte 3: Instalación de extensiones PHP

#### Tarea 3.1: Extensiones adicionales

1. Crea un directorio: `~/imagen_php_v3`.

2. Investiga cómo instalar extensiones PHP en la imagen oficial:
   
    - Consulta la documentación de la imagen en Docker Hub
    - Busca el script helper `docker-php-ext-install`
    - Investiga qué extensiones puedes instalar

3. Modifica el Dockerfile de la versión 2 para añadir:
   
    - Extensión `mysqli` (para MySQL/MariaDB)
    - Extensión `pdo_mysql`
    - Extensión `gd` (para manipulación de imágenes)

4. **Pista:** Las extensiones que requieren librerías del sistema necesitan que las instales primero con apt-get.

#### Tarea 3.2: Verificación de extensiones

1. Construye la imagen:
   
    - Nombre: `tu_usuario/app_php`
    - Etiqueta: `v3`

2. Crea un contenedor y accede a `info.php`.

3. Verifica en phpinfo() que las extensiones están instaladas.

4. En la página principal, verifica que aparecen en la lista de extensiones.

---

### 🔹 Parte 4: Optimización y configuración

#### Tarea 4.1: Configuración personalizada de PHP

1. Crea un archivo `php.ini` personalizado con:

```ini
[PHP]
; Configuración personalizada para desarrollo
display_errors = On
error_reporting = E_ALL
memory_limit = 256M
upload_max_filesize = 20M
post_max_size = 20M
max_execution_time = 60
date.timezone = "Europe/Madrid"
```

2. Modifica tu Dockerfile para copiar este archivo a `/usr/local/etc/php/php.ini`.

3. Construye y verifica que la configuración se aplica.

#### Tarea 4.2: Uso de variables de entorno

1. Modifica `index.php` para mostrar variables de entorno:

```php
<div class="info-box">
    <h3>Variables de Entorno</h3>
    <?php
    $env_vars = ['APP_ENV', 'APP_NAME', 'APP_VERSION'];
    foreach($env_vars as $var) {
        $value = getenv($var) ?: 'No definida';
        echo "<p><strong>$var:</strong> $value</p>";
    }
    ?>
</div>
```

2. Modifica tu Dockerfile para definir estas variables con ENV.

3. Al crear el contenedor, sobrescribe alguna variable.

4. Verifica que se muestran correctamente.

#### Tarea 4.3: Multi-stage build (avanzado)

Investiga y crea un Dockerfile multi-stage que:

1. Use una etapa de "build" para preparar la aplicación.
2. Use una etapa final más ligera.
3. Copie solo lo necesario de la etapa build.

---

### 🔹 Parte 5: Documentación y análisis

#### Tarea 5.1: Tabla comparativa

Completa esta tabla con tus resultados:

| Aspecto             | Versión 1 (Debian+PHP)  | Versión 2 (php:apache)  | Versión 3 (con ext)  |
|---------------------|-------------------------|-------------------------|----------------------|
| Imagen base         |                         |                         |                      |
| Tamaño final        |                         |                         |                      |
| Tiempo construcción |                         |                         |                      |
| Versión PHP         |                         |                         |                      |
| Líneas Dockerfile   |                         |                         |                      |
| Complejidad         |                         |                         |                      |
| Extensiones         |                         |                         |                      |

#### Tarea 5.2: Preguntas de reflexión

Responde en tu documentación:

1. **Sobre las imágenes base:**
   
    - ¿Cuándo usarías Debian vs PHP oficial?
    - ¿Qué ventajas tiene la imagen especializada?
    - ¿Qué desventajas puede tener?

2. **Sobre el tamaño:**
   
    - ¿Por qué es importante el tamaño de las imágenes?
    - ¿Cómo afecta al tiempo de despliegue?
    - ¿Qué estrategias conoces para reducir el tamaño?

3. **Sobre las extensiones:**
   
    - ¿Por qué no vienen todas las extensiones por defecto?
    - ¿Cómo decides qué extensiones instalar?
    - ¿Qué impacto tienen en el tamaño de la imagen?

4. **Sobre la configuración:**
   
    - ¿Es mejor configurar PHP en el Dockerfile o con archivos externos?
    - ¿Cuándo usar variables de entorno vs archivos de configuración?
    - ¿Cómo gestionarías diferentes configuraciones (dev/prod)?

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Los 3 archivos Dockerfile creados
    - Archivo php.ini personalizado
    - Comandos Docker utilizados
    - Capturas de pantalla:
        - Aplicación funcionando (index.php, info.php, test.php)
        - phpinfo() mostrando extensiones
        - Comparación de tamaños de imágenes
        - Variables de entorno funcionando
    - Tabla comparativa completa
    - Respuestas a todas las preguntas

2. **Archivos del proyecto:**
   
    - Directorio `app/` con los 3 archivos PHP
    - Dockerfile de cada versión
    - Archivo php.ini personalizado

---

### Evaluación

Se evaluará:

- Correcta construcción de imágenes PHP.
- Funcionamiento de todas las versiones.
- Instalación correcta de extensiones.
- Configuración personalizada de PHP.
- Análisis comparativo detallado.
- Comprensión de conceptos.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Imagen oficial de PHP: [https://hub.docker.com/_/php](https://hub.docker.com/_/php)
- Instalación de extensiones PHP: [https://github.com/docker-library/docs/blob/master/php/README.md#how-to-install-more-php-extensions](https://github.com/docker-library/docs/blob/master/php/README.md#how-to-install-more-php-extensions)
- Configuración de PHP: [https://www.php.net/manual/es/ini.core.php](https://www.php.net/manual/es/ini.core.php)
- Dockerfile best practices: [https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.10.-ImagenesPHP.html){ .md-button }
