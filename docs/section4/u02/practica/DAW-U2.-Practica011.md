---
title: "UD 2 - P11: Construcción de imagen Docker con PHP y base de datos"
description: "Creación de imágenes Docker configurables para aplicaciones PHP con MariaDB"
summary: "Actividad práctica para crear imágenes Docker que se conectan a bases de datos usando variables de entorno."
authors:
    - Eduardo Fdez
date: 2025-01-13
icon: 
permalink: /daw/unidad2/p2.11
categories:
    - DAW
tags:
    - Docker
    - Dockerfile
    - PHP
    - MariaDB
    - Variables de entorno
    - Base de datos
---

## Relación 2.11

### Descripción

**Actividad:** *Construcción de imagen Docker con PHP y base de datos*

En esta práctica crearás una imagen Docker personalizada para una aplicación PHP que se conecta a una base de datos MariaDB. Aprenderás a construir imágenes configurables mediante variables de entorno y a inicializar bases de datos automáticamente.

#### Objetivo general

Aprender a:

- Construir imágenes configurables con variables de entorno.
- Conectar aplicaciones PHP con bases de datos.
- Instalar extensiones PHP para acceso a bases de datos.
- Crear scripts de inicialización para contenedores.
- Gestionar dependencias entre contenedores.
- Inicializar bases de datos automáticamente.

---

### Contexto de trabajo

Las aplicaciones web modernas normalmente necesitan acceder a bases de datos. En Docker, esto implica:

- **Imagen de aplicación:** Contiene el código PHP y las extensiones necesarias
- **Imagen de base de datos:** Contenedor separado con MariaDB/MySQL
- **Variables de entorno:** Para configurar la conexión de forma flexible
- **Script de inicialización:** Para preparar la base de datos al iniciar

**Arquitectura de la aplicación:**

```
┌─────────────────────┐          ┌──────────────────────┐
│   Contenedor PHP    │─────────▶│  Contenedor MariaDB  │
│  (Tu imagen)        │          │  (Imagen oficial)    │
│                     │          │                      │
│  - Apache + PHP     │          │  - Base de datos     │
│  - App PHP          │          │  - Puerto 3306       │
│  - Script init      │          │  - Volumen datos     │
│  - Puerto 80        │          │                      │
└─────────────────────┘          └──────────────────────┘
```

---

### 📦 Archivos de la aplicación

Se te proporcionan todos los archivos necesarios. Créalos en un directorio `build/`:

#### Archivo `build/app/index.php`:

```php
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestión de Usuarios - Docker</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
        }
        .content {
            padding: 30px;
        }
        .info-box {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 15px;
            margin: 20px 0;
            border-radius: 5px;
        }
        .success {
            background: #d4edda;
            border-left-color: #28a745;
            color: #155724;
        }
        .error {
            background: #f8d7da;
            border-left-color: #dc3545;
            color: #721c24;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        thead {
            background: #667eea;
            color: white;
        }
        th, td {
            padding: 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        tbody tr:hover {
            background: #f5f5f5;
        }
        tbody tr:nth-child(even) {
            background: #f9f9f9;
        }
        .db-info {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .db-card {
            background: #e3f2fd;
            padding: 15px;
            border-radius: 8px;
            border-left: 3px solid #2196F3;
        }
        .db-card strong {
            display: block;
            color: #1976D2;
            margin-bottom: 5px;
            font-size: 0.9em;
        }
        .db-card span {
            font-size: 1.1em;
            font-weight: 600;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🗄️ Gestión de Usuarios</h1>
            <p>Aplicación PHP + MariaDB en Docker</p>
        </div>
        
        <div class="content">
            <h2>Información de Conexión</h2>
            <div class="db-info">
                <div class="db-card">
                    <strong>Host de Base de Datos:</strong>
                    <span><?php echo getenv('DB_HOST') ?: 'No configurado'; ?></span>
                </div>
                <div class="db-card">
                    <strong>Base de Datos:</strong>
                    <span><?php echo getenv('DB_NAME') ?: 'No configurado'; ?></span>
                </div>
                <div class="db-card">
                    <strong>Usuario:</strong>
                    <span><?php echo getenv('DB_USER') ?: 'No configurado'; ?></span>
                </div>
            </div>

            <?php
            // Leer credenciales desde variables de entorno
            $host = getenv('DB_HOST');
            $user = getenv('DB_USER');
            $pass = getenv('DB_PASS');
            $db = getenv('DB_NAME');

            // Intentar conectar a la base de datos
            $conn = new mysqli($host, $user, $pass, $db);

            if ($conn->connect_error) {
                echo '<div class="info-box error">';
                echo '<h3>❌ Error de Conexión</h3>';
                echo '<p><strong>Error:</strong> ' . htmlspecialchars($conn->connect_error) . '</p>';
                echo '<p><strong>Código:</strong> ' . $conn->connect_errno . '</p>';
                echo '</div>';
            } else {
                echo '<div class="info-box success">';
                echo '<h3>✅ Conexión Exitosa</h3>';
                echo '<p>Conectado correctamente a la base de datos MariaDB</p>';
                echo '</div>';

                // Consultar usuarios
                $sql = 'SELECT * FROM users';
                $users = [];

                if ($result = $conn->query($sql)) {
                    while ($data = $result->fetch_object()) {
                        $users[] = $data;
                    }
                    $result->free();
                }

                if (count($users) > 0) {
                    echo '<h2>Lista de Usuarios</h2>';
                    echo '<table>';
                    echo '<thead><tr><th>ID</th><th>Usuario</th><th>Email</th><th>Fecha Registro</th></tr></thead>';
                    echo '<tbody>';
                    foreach ($users as $user) {
                        echo '<tr>';
                        echo '<td>' . htmlspecialchars($user->id) . '</td>';
                        echo '<td>' . htmlspecialchars($user->username) . '</td>';
                        echo '<td>' . htmlspecialchars($user->email) . '</td>';
                        echo '<td>' . htmlspecialchars($user->created_at ?? 'N/A') . '</td>';
                        echo '</tr>';
                    }
                    echo '</tbody>';
                    echo '</table>';
                    echo '<div class="info-box">';
                    echo '<p><strong>Total de usuarios:</strong> ' . count($users) . '</p>';
                    echo '</div>';
                } else {
                    echo '<div class="info-box">';
                    echo '<p>⚠️ No hay usuarios registrados en la base de datos.</p>';
                    echo '</div>';
                }

                mysqli_close($conn);
            }
            ?>

            <div class="info-box" style="margin-top: 30px; background: #fff3cd; border-left-color: #ffc107;">
                <h3>ℹ️ Información Técnica</h3>
                <p><strong>PHP Version:</strong> <?php echo phpversion(); ?></p>
                <p><strong>Extensión MySQLi:</strong> <?php echo extension_loaded('mysqli') ? '✓ Cargada' : '✗ No cargada'; ?></p>
                <p><strong>Servidor:</strong> <?php echo $_SERVER['SERVER_SOFTWARE']; ?></p>
            </div>
        </div>
    </div>
</body>
</html>
```

#### Archivo `build/schema.sql`:

```sql
-- Crear tabla de usuarios
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Insertar usuarios de ejemplo
INSERT INTO users (username, email, password) VALUES
('admin', 'admin@example.com', 'admin123'),
('maria_garcia', 'maria@example.com', 'pass456'),
('juan_lopez', 'juan@example.com', 'pass789'),
('ana_martinez', 'ana@example.com', 'pass321'),
('carlos_rodriguez', 'carlos@example.com', 'pass654');

-- Mensaje de confirmación
SELECT 'Base de datos inicializada correctamente' AS mensaje;
```

#### Archivo `build/script.sh`:

```bash
#!/bin/bash

echo "====================================="
echo "Iniciando script de configuración..."
echo "====================================="

# Mostrar variables de entorno (sin contraseñas)
echo "Host de BD: ${DB_HOST}"
echo "Usuario de BD: ${DB_USER}"
echo "Nombre de BD: ${DB_NAME}"
echo ""

# Esperar a que MariaDB esté disponible
echo "Esperando a que MariaDB esté disponible..."
COUNTER=0
MAX_TRIES=30

while ! mysql -u "${DB_USER}" -p"${DB_PASS}" -h "${DB_HOST}" -e ";" 2>/dev/null; do
    COUNTER=$((COUNTER + 1))
    if [ $COUNTER -gt $MAX_TRIES ]; then
        echo "ERROR: No se pudo conectar a MariaDB después de $MAX_TRIES intentos"
        exit 1
    fi
    echo "Intento $COUNTER/$MAX_TRIES - MariaDB no está lista aún, esperando..."
    sleep 2
done

echo "✓ MariaDB está disponible!"
echo ""

# Inicializar la base de datos
echo "Inicializando base de datos..."
if mysql -u "${DB_USER}" -p"${DB_PASS}" -h "${DB_HOST}" "${DB_NAME}" < /opt/schema.sql; then
    echo "✓ Base de datos inicializada correctamente"
else
    echo "ERROR: Fallo al inicializar la base de datos"
    exit 1
fi

echo ""
echo "====================================="
echo "Iniciando servidor Apache..."
echo "====================================="

# Iniciar Apache en primer plano
apache2ctl -D FOREGROUND
```

---

### 🔹 Parte 1: Comprensión de la arquitectura

#### Tarea 1.1: Análisis de los archivos proporcionados

1. Lee detenidamente cada archivo proporcionado.

2. Responde en tu documentación:
   
    **Sobre index.php:**
    - ¿Cómo obtiene las credenciales de la base de datos?
    - ¿Por qué es mejor usar variables de entorno que hardcodear las credenciales?
    - ¿Qué extensión PHP usa para conectarse a MariaDB?
   
    **Sobre schema.sql:**
    - ¿Qué estructura tiene la tabla users?
    - ¿Cuántos usuarios de ejemplo se insertan?
    - ¿Por qué es útil tener un archivo SQL separado?
   
    **Sobre script.sh:**
    - ¿Qué hace el bucle `while`?
    - ¿Por qué es necesario esperar a que MariaDB esté disponible?
    - ¿Qué comando inicia Apache?
    - ¿Por qué `-D FOREGROUND`?

#### Tarea 1.2: Estructura del proyecto

1. Crea la estructura de directorios:

```
proyecto_php_bd/
├── build/
│   ├── Dockerfile
│   ├── script.sh
│   ├── schema.sql
│   └── app/
│       └── index.php
└── docker-compose.yml
```

2. Coloca cada archivo proporcionado en su ubicación correspondiente.

3. Verifica que `script.sh` tiene permisos de ejecución en el host (aunque se configurará en el Dockerfile).

---

### 🔹 Parte 2: Creación del Dockerfile

#### Tarea 2.1: Diseño del Dockerfile

Tu Dockerfile debe realizar las siguientes tareas (investiga la sintaxis necesaria):

1. **Imagen base:**
   
    - Partir de `php:7.4-apache` o `php:8.2-apache`

2. **Instalación de dependencias:**
   
    - Instalar el cliente de MariaDB (`mariadb-client`)
    - Instalar la extensión PHP `mysqli`
    - Habilitar la extensión `mysqli`

3. **Copia de archivos:**
   
    - Copiar `app/` al DocumentRoot de Apache
    - Copiar `script.sh` a `/usr/local/bin/`
    - Copiar `schema.sql` a `/opt/`

4. **Variables de entorno:**
   
    - Definir `DB_USER` con valor por defecto
    - Definir `DB_PASS` con valor por defecto
    - Definir `DB_NAME` con valor por defecto
    - Definir `DB_HOST` con valor por defecto

5. **Permisos y configuración:**
   
    - Dar permisos de ejecución a `script.sh`
    - Exponer el puerto 80

6. **Comando de inicio:**
   
    - Establecer que al iniciar el contenedor se ejecute `script.sh`

#### Tarea 2.2: Construcción de la imagen

1. Investiga los comandos necesarios para:
   
    - Instalar paquetes en la imagen PHP
    - Instalar extensiones PHP (consulta la documentación de la imagen oficial)
    - Usar `docker-php-ext-install` y `docker-php-ext-enable`

2. Construye tu imagen:
   
    - Nombre: `tu_usuario/app_php_bd`
    - Etiqueta: `v1`

3. Verifica que la imagen se ha creado y anota su tamaño.

---

### 🔹 Parte 3: Despliegue con Docker Compose

#### Tarea 3.1: Creación del docker-compose.yml

Crea un archivo `docker-compose.yml` que defina:

**Servicio de aplicación PHP (`app`):**
- Tu imagen personalizada
- Puerto 8080 del host → puerto 80 del contenedor
- Variables de entorno para conexión a BD
- Dependencia del servicio de base de datos
- Política de reinicio

**Servicio de base de datos (`db`):**
- Imagen `mariadb`
- Variables de entorno para crear la BD
- Volumen Docker para persistir los datos
- Política de reinicio

**Volumen:**
- Define un volumen Docker para los datos de MariaDB

#### Tarea 3.2: Despliegue y pruebas

1. Despliega el escenario con Docker Compose.

2. Observa los logs de ambos contenedores:
   
    - ¿Aparece el mensaje de "MariaDB está disponible"?
    - ¿Se inicializa correctamente la base de datos?
    - ¿Hay algún error?

3. Accede a la aplicación web (http://localhost:8080).

4. Verifica que:
   
    - La conexión a la BD es exitosa
    - Se muestran los usuarios de la tabla
    - Los datos de conexión son correctos

---

### 🔹 Parte 4: Configuración y personalización

#### Tarea 4.1: Modificación de variables de entorno

1. Detén el escenario.

2. Modifica el `docker-compose.yml` para usar diferentes credenciales:
   
    - Cambiar nombre de usuario
    - Cambiar contraseña
    - Cambiar nombre de la base de datos

3. Vuelve a desplegar y verifica que funciona con las nuevas credenciales.

4. **Pregunta:** ¿Qué pasó con los datos anteriores? ¿Por qué?

#### Tarea 4.2: Archivo .env

1. Crea un archivo `.env` con todas las variables de configuración:

```env
# Configuración de la base de datos
MYSQL_ROOT_PASSWORD=mi_password_root_seguro
MYSQL_DATABASE=usuarios_db
MYSQL_USER=usuario_app
MYSQL_PASSWORD=password_seguro

# Configuración de la aplicación
APP_DB_HOST=db
APP_DB_USER=usuario_app
APP_DB_PASS=password_seguro
APP_DB_NAME=usuarios_db

# Puertos
APP_PORT=8080
```

2. Modifica tu `docker-compose.yml` para usar las variables del archivo `.env`.

3. Despliega y verifica que funciona correctamente.

#### Tarea 4.3: Agregar más datos

1. Accede al contenedor de MariaDB.

2. Conéctate a la base de datos con el cliente mysql.

3. Inserta manualmente 3 usuarios adicionales:

```sql
INSERT INTO users (username, email, password) VALUES
('nuevo_usuario1', 'nuevo1@example.com', 'pass001'),
('nuevo_usuario2', 'nuevo2@example.com', 'pass002'),
('nuevo_usuario3', 'nuevo3@example.com', 'pass003');
```

4. Recarga la página web y verifica que aparecen los nuevos usuarios.

---

### 🔹 Parte 5: Persistencia y gestión de datos

#### Tarea 5.1: Verificación de persistencia

1. Detén todos los contenedores.

2. Elimina solo los contenedores (manteniendo el volumen).

3. Vuelve a desplegar el escenario.

4. Verifica que los datos persisten (incluyendo los usuarios que agregaste manualmente).

5. **Pregunta:** ¿Por qué los datos insertados desde la web persisten pero el script se ejecuta de nuevo?

#### Tarea 5.2: Reinicio limpio

1. Detén y elimina todo el escenario incluyendo volúmenes.

2. Vuelve a desplegarlo.

3. Verifica que solo aparecen los 5 usuarios iniciales del `schema.sql`.

4. Documenta el proceso y explica qué sucedió.

#### Tarea 5.3: Backup de la base de datos

1. Investiga cómo hacer un backup de una base de datos MySQL/MariaDB dentro de un contenedor Docker.

2. Realiza un backup de tu base de datos a un archivo SQL.

3. Guarda el archivo de backup en el host.

4. Elimina el escenario completo (con volúmenes).

5. Recrea el escenario.

6. Restaura el backup en la nueva base de datos.

7. Verifica que todos los datos se restauraron correctamente.

---

### 🔹 Parte 6: Mejoras y optimización

#### Tarea 6.1: Mejora del script de inicialización

Modifica `script.sh` para que:

1. Solo inicialice la base de datos si está vacía (no sobrescribir datos existentes).

2. **Pista:** Puedes verificar si la tabla existe antes de ejecutar el schema.sql:

```bash
# Verificar si la tabla existe
TABLE_EXISTS=$(mysql -u "${DB_USER}" -p"${DB_PASS}" -h "${DB_HOST}" "${DB_NAME}" \
  -sse "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='${DB_NAME}' AND table_name='users';")

if [ "$TABLE_EXISTS" -eq "0" ]; then
    echo "Inicializando base de datos (primera vez)..."
    mysql -u "${DB_USER}" -p"${DB_PASS}" -h "${DB_HOST}" "${DB_NAME}" < /opt/schema.sql
else
    echo "Base de datos ya inicializada, omitiendo schema.sql"
fi
```

3. Reconstruye la imagen y prueba que funciona correctamente.

#### Tarea 6.2: Healthchecks

Añade healthchecks a tu `docker-compose.yml`:

**Para la aplicación PHP:**
- Verificar que el puerto 80 responde
- Intervalo de 30 segundos

**Para MariaDB:**
- Verificar con mysqladmin ping
- Intervalo de 10 segundos

#### Tarea 6.3: Añadir funcionalidad a la aplicación

Crea un nuevo archivo `build/app/agregar.php` que permita:

1. Mostrar un formulario HTML para agregar usuarios.
2. Procesar el formulario e insertar datos en la BD.
3. Redirigir a index.php después de insertar.

**Requisitos:**
- Validar que los campos no estén vacíos
- Validar formato de email
- Mostrar mensajes de error/éxito

---

### 🔹 Parte 7: Análisis y documentación

#### Tarea 7.1: Preguntas de reflexión

1. **Sobre variables de entorno:**
   
    - ¿Por qué es mejor usar variables de entorno que hardcodear valores?
    - ¿Qué riesgos de seguridad existen al usar variables de entorno?
    - ¿Cómo mejorarías la seguridad de las credenciales?

2. **Sobre el script de inicialización:**
   
    - ¿Por qué necesitamos esperar a que MariaDB esté lista?
    - ¿Qué pasaría si no esperamos?
    - ¿Hay alternativas mejores al bucle while?

3. **Sobre la arquitectura:**
   
    - ¿Por qué separar la aplicación y la BD en contenedores diferentes?
    - ¿Cuáles son las ventajas?
    - ¿Cuáles son las desventajas?

4. **Sobre persistencia:**
   
    - ¿Por qué es importante persistir los datos de la BD?
    - ¿Qué pasa si no usas volúmenes?
    - ¿Cuándo usarías volúmenes vs bind mounts?

#### Tarea 7.2: Diagrama de la arquitectura

Crea un diagrama que muestre:

1. Los dos contenedores y sus componentes.
2. Las variables de entorno que usa cada uno.
3. El volumen de persistencia.
4. La red que los conecta.
5. Los puertos expuestos.
6. El flujo de datos desde el navegador hasta la BD.

---

## Entregables

1. **Documentación en formato Markdown o PDF** con:
   
    - Dockerfile completo y comentado
    - Archivo docker-compose.yml completo
    - Script script.sh mejorado (opcional)
    - Archivo .env
    - Todos los comandos utilizados
    - Capturas de pantalla:
        - Construcción de la imagen
        - Despliegue con Docker Compose
        - Aplicación funcionando mostrando usuarios
        - Logs de inicialización
        - Healthchecks funcionando
        - Verificación de persistencia
        - Backup y restauración
    - Respuestas a todas las preguntas
    - Diagrama de arquitectura

2. **Archivos del proyecto:**
   
    - Directorio `build/` completo
    - Dockerfile
    - docker-compose.yml
    - .env
    - Cualquier mejora adicional (agregar.php, etc.)

---

### Evaluación

Se evaluará:

- Correcta construcción de la imagen con extensiones PHP.
- Funcionamiento de la aplicación con la base de datos.
- Uso apropiado de variables de entorno.
- Implementación correcta del script de inicialización.
- Verificación de persistencia de datos.
- Proceso de backup y restauración.
- Comprensión de la arquitectura multi-contenedor.
- Calidad de la documentación.

---

### Condiciones de entrega

Las publicadas en la plataforma Moodle del curso.

---

### Recursos de apoyo

- Imagen oficial de PHP: [https://hub.docker.com/_/php](https://hub.docker.com/_/php)
- Extensiones PHP con Docker: [https://github.com/docker-library/docs/blob/master/php/README.md](https://github.com/docker-library/docs/blob/master/php/README.md)
- Imagen oficial de MariaDB: [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb)
- Variables de entorno en Docker Compose: [https://docs.docker.com/compose/environment-variables/](https://docs.docker.com/compose/environment-variables/)
- MySQL/MariaDB en contenedores: [https://dev.mysql.com/doc/refman/8.0/en/docker-mysql-more-topics.html](https://dev.mysql.com/doc/refman/8.0/en/docker-mysql-more-topics.html)

---

### Presentación de la práctica

[:fontawesome-solid-file-pdf: Descargar presentación](https://revilofe.github.io/slides/section4-daw/DAW-U2.11.-PHPBaseDatos.html){ .md-button }
