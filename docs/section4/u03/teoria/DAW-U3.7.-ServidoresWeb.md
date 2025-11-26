---
title: "UD 3 - 3.7 Servidores Web y de Aplicaciones"
description: Configuración y gestión de servidores web Apache y Nginx, servidores de aplicaciones Tomcat, gestores de bases de datos
summary: Funcionamiento de servidores web, instalación y configuración de Apache y Nginx, virtual hosts, servidores de aplicaciones Java Tomcat, gestores de bases de datos
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: "material/file-document-outline"
permalink: /daw/unidad3/3.7
categories:
    - DAW
tags:
    - Apache
    - Nginx
    - Tomcat
    - Servidores Web
    - Virtual Hosts
    - Bases de Datos
---

## 3.7. Servidores Web y de Aplicaciones

En las unidades anteriores hemos aprendido cómo se generan las páginas web dinámicas mediante código ejecutado en el servidor. Hemos visto lenguajes como PHP, Python y Java, y cómo se integran con HTML para producir contenido personalizado. Sin embargo, hay una pieza fundamental que aún no hemos explorado en profundidad: **¿qué software ejecuta realmente todo este código en el servidor?**

Cuando decimos "el servidor hace esto" o "el código se ejecuta en el servidor", ¿a qué nos referimos exactamente? La respuesta está en los **servidores web** y los **servidores de aplicaciones**, el software que actúa como intermediario entre las peticiones de los usuarios y el código de nuestras aplicaciones.

Estos programas son el corazón pulsante de cualquier aplicación web. Sin ellos, nuestro código PHP o Java sería solo texto inerte en un disco duro. Ellos son los que escuchan las peticiones HTTP, invocan nuestro código, gestionan las conexiones, sirven archivos estáticos, y mucho más. Entender cómo funcionan, cómo configurarlos y cómo desplegarlos es **absolutamente esencial** para cualquier profesional del despliegue de aplicaciones web.

### 1. ¿Qué es un servidor web y por qué lo necesitamos?

Antes de sumergirnos en las tecnologías específicas, comprendamos exactamente qué es un servidor web y qué papel juega en el ecosistema de aplicaciones web.

#### 1.1. Definición y función fundamental

Un **servidor web** es un programa informático que:

1. **Se ejecuta continuamente** en un ordenador (el servidor físico)
2. **Escucha en un puerto específico** (típicamente el 80 para HTTP, 443 para HTTPS)
3. **Espera peticiones de clientes** (navegadores web, aplicaciones móviles, otros servidores)
4. **Procesa cada petición** según su configuración
5. **Devuelve una respuesta** al cliente (HTML, imágenes, JSON, etc.)

**Analogía del mundo real:**

Imaginad un servidor web como un **recepcionista en un hotel**:

- Está siempre en el mostrador (ejecutándose continuamente)
- Escucha a los huéspedes que llegan (peticiones entrantes)
- Entiende qué necesita cada huésped (interpreta la petición HTTP)
- Les dirige a la habitación correcta o les proporciona lo que piden (sirve archivos o ejecuta código)
- Mantiene registro de quién entra y sale (logs de acceso)

#### 1.2. Contenido estático vs. contenido dinámico

Los servidores web pueden manejar dos tipos fundamentales de contenido:

**Contenido estático:**

Son archivos que **ya existen** en el sistema de archivos del servidor y se envían directamente al cliente sin procesamiento:

- Archivos HTML predefinidos
- Imágenes (JPEG, PNG, GIF, SVG)
- Hojas de estilo CSS
- Scripts JavaScript
- Archivos PDF
- Videos y audio

**Proceso con contenido estático:**

```
Cliente solicita: GET /imagenes/logo.png
    ↓
Servidor web → Lee el archivo del disco
    ↓
Servidor web → Envía el archivo directamente
    ↓
Cliente recibe la imagen
```

**Contenido dinámico:**

Es contenido que se **genera en el momento** de la petición, ejecutando código:

- Páginas PHP que consultan bases de datos
- Aplicaciones Python/Django
- Servlets Java
- APIs REST que devuelven JSON

**Proceso con contenido dinámico:**

```
Cliente solicita: GET /productos.php
    ↓
Servidor web → Identifica que es código dinámico
    ↓
Servidor web → Delega a PHP-FPM / mod_php
    ↓
PHP ejecuta el código → Consulta base de datos
    ↓
PHP genera HTML
    ↓
Servidor web → Envía el HTML generado
    ↓
Cliente recibe la página
```

La **gran diferencia** es que el contenido estático es muy rápido (solo lectura de disco), mientras que el dinámico requiere procesamiento (más lento, pero mucho más potente).

#### 1.3. ¿Por qué no ejecutar el código directamente?

Podríais preguntaros: *¿Por qué necesitamos un servidor web? ¿No podemos ejecutar nuestro código PHP o Python directamente?*

La respuesta es que **sí podríamos**, pero perderíamos funcionalidades cruciales que el servidor web proporciona:

**Funcionalidades esenciales del servidor web:**

1. **Gestión de conexiones TCP/IP**: Maneja múltiples clientes simultáneamente
2. **Protocolo HTTP completo**: Interpreta cabeceras, métodos, códigos de estado
3. **Enrutamiento**: Decide qué hacer con cada URL
4. **Seguridad**: HTTPS, control de acceso, protección contra ataques
5. **Caché**: Almacena contenido para servirlo más rápido
6. **Compresión**: Reduce el tamaño de las respuestas (gzip)
7. **Logs**: Registro de accesos y errores
8. **Virtual Hosts**: Múltiples sitios en un mismo servidor
9. **Balanceo de carga**: Distribuye peticiones entre varios backends
10. **Límites de recursos**: Control de ancho de banda, timeouts, etc.

Sin un servidor web, tendríamos que implementar todo esto en nuestro código. Los servidores web son **especialistas** en estas tareas, probados durante décadas, optimizados y seguros.

### 2. Apache HTTP Server: el veterano robusto

**Apache HTTP Server** (comúnmente llamado simplemente "Apache") es el servidor web más veterano y uno de los más utilizados en la historia de Internet. Creado en 1995, ha sido el pilar de millones de sitios web durante casi tres décadas.

#### 2.1. Historia y relevancia

Apache nació de un proyecto llamado "NCSA HTTPd" en 1995. Un grupo de desarrolladores creó "Apache" (un juego de palabras: "A patchy server" - un servidor remendado) aplicando parches al servidor original.

**Datos históricos:**

- **1996-2009**: Apache era el servidor web más usado en Internet (más del 50% del mercado)
- **Actualidad**: Aunque Nginx ha ganado cuota, Apache sigue siendo extremadamente popular
- **Filosofía**: Open source, gratuito, mantenido por la Apache Software Foundation

**¿Por qué Apache tuvo tanto éxito?**

1. **Gratuito y open source**: Sin costes de licencia
2. **Multiplataforma**: Funciona en Linux, Windows, macOS, etc.
3. **Extremadamente configurable**: Se puede adaptar a casi cualquier necesidad
4. **Modular**: Solo activas las funcionalidades que necesitas
5. **Comunidad masiva**: Documentación, tutoriales, soporte extenso
6. **Integración con PHP**: mod_php integra PHP directamente en Apache
7. **Estabilidad probada**: Décadas de uso en producción

#### 2.2. Arquitectura modular de Apache

La característica más distintiva de Apache es su **arquitectura modular**. Apache en sí es un núcleo pequeño, y las funcionalidades se añaden mediante **módulos**.

**Módulos comunes:**

- **mod_php**: Ejecuta código PHP directamente en Apache
- **mod_ssl**: Soporte para HTTPS
- **mod_rewrite**: Reescritura de URLs (crucial para URLs amigables)
- **mod_proxy**: Actúa como proxy/reverse proxy
- **mod_headers**: Manipulación de cabeceras HTTP
- **mod_auth**: Autenticación
- **mod_deflate**: Compresión de respuestas
- **mod_security**: Firewall de aplicaciones web

**Ventaja de los módulos:**

Solo cargas lo que necesitas, ahorrando memoria y mejorando el rendimiento. Si no necesitas PHP, no cargas mod_php. Si no necesitas SSL, no cargas mod_ssl.

**Listar módulos activos:**

```bash
# Ver módulos habilitados
apache2ctl -M

# Habilitar un módulo
sudo a2enmod rewrite

# Deshabilitar un módulo
sudo a2dismod php7.4

# Reiniciar Apache para aplicar cambios
sudo systemctl restart apache2
```

#### 2.3. Instalación de Apache en Linux

La instalación de Apache en sistemas basados en Debian/Ubuntu es extremadamente sencilla:

```bash
# Actualizar repositorios
sudo apt update

# Instalar Apache
sudo apt install apache2

# Verificar que está corriendo
sudo systemctl status apache2

# Habilitar inicio automático al arrancar el sistema
sudo systemctl enable apache2
```

**Verificar la instalación:**

Abre un navegador y accede a:
- `http://localhost` (si estás en el mismo servidor)
- `http://IP_DEL_SERVIDOR` (desde otro equipo)

Deberías ver la **página por defecto de Apache**, que confirma que el servidor está funcionando correctamente.

#### 2.4. Estructura de directorios de Apache

Apache organiza sus archivos de configuración de forma estructurada:

```
/etc/apache2/
├── apache2.conf          # Configuración principal
├── ports.conf            # Puertos en los que escucha
├── mods-available/       # Módulos disponibles
├── mods-enabled/         # Módulos habilitados (enlaces simbólicos)
├── sites-available/      # Configuraciones de sitios disponibles
├── sites-enabled/        # Sitios habilitados (enlaces simbólicos)
├── conf-available/       # Configuraciones adicionales disponibles
└── conf-enabled/         # Configuraciones adicionales habilitadas

/var/www/                 # Directorio raíz para sitios web
└── html/                 # Sitio por defecto
    └── index.html        # Página por defecto

/var/log/apache2/         # Logs
├── access.log            # Registro de accesos
└── error.log             # Registro de errores
```

**Filosofía de configuración:**

- Los archivos en `*-available/` contienen configuraciones posibles
- Los archivos en `*-enabled/` son enlaces simbólicos a los que realmente se usan
- Esto permite activar/desactivar fácilmente configuraciones sin borrar archivos

#### 2.5. Configuración básica de Apache

El archivo principal es `/etc/apache2/apache2.conf`. Veamos las directivas más importantes:

**ServerRoot**: Directorio base de configuración

```apache
ServerRoot "/etc/apache2"
```

**Listen**: Puerto y dirección IP donde escucha

```apache
# Escuchar en el puerto 80 de todas las interfaces
Listen 80

# Escuchar solo en una IP específica
Listen 192.168.1.100:80

# También escuchar en HTTPS
Listen 443
```

**DocumentRoot**: Directorio donde están los archivos del sitio web

```apache
DocumentRoot "/var/www/html"
```

Todos los archivos servidos vienen de este directorio. Por ejemplo:
- `http://miserver/index.html` → `/var/www/html/index.html`
- `http://miserver/imagenes/logo.png` → `/var/www/html/imagenes/logo.png`

**ServerName**: Nombre del servidor

```apache
ServerName www.ejemplo.local
```

Esto define cómo el servidor se identifica a sí mismo.

**DirectoryIndex**: Archivos que se buscan cuando se solicita un directorio

```apache
DirectoryIndex index.html index.php
```

Si pides `http://miserver/`, Apache buscará en este orden:
1. `index.html`
2. `index.php`
3. Si no encuentra ninguno, puede mostrar un listado del directorio (si está habilitado)

**Timeout**: Tiempo máximo de espera

```apache
Timeout 300
```

Segundos que el servidor esperará antes de cerrar una conexión inactiva.

**KeepAlive**: Conexiones persistentes

```apache
KeepAlive On
MaxKeepAliveRequests 100
KeepAliveTimeout 5
```

Permite múltiples peticiones sobre la misma conexión TCP, mejorando el rendimiento.

**ErrorLog y CustomLog**: Configuración de logs

```apache
ErrorLog ${APACHE_LOG_DIR}/error.log
CustomLog ${APACHE_LOG_DIR}/access.log combined
```

#### 2.6. Gestión del servicio Apache

**Comandos esenciales:**

```bash
# Iniciar Apache
sudo systemctl start apache2

# Detener Apache
sudo systemctl stop apache2

# Reiniciar Apache (detiene y vuelve a iniciar)
sudo systemctl restart apache2

# Recargar configuración sin detener (preferible)
sudo systemctl reload apache2

# Ver estado
sudo systemctl status apache2

# Ver logs en tiempo real
sudo tail -f /var/log/apache2/error.log
sudo tail -f /var/log/apache2/access.log
```

**Verificar sintaxis de configuración:**

Antes de reiniciar Apache, **siempre** verifica que la configuración es correcta:

```bash
sudo apache2ctl configtest
```

Si devuelve `Syntax OK`, puedes reiniciar con seguridad. Si hay errores, te los mostrará y podrás corregirlos antes de causar una caída del servidor.

#### 2.7. Virtual Hosts: múltiples sitios en un servidor

Los **Virtual Hosts** (hosts virtuales) son una de las funcionalidades más poderosas de Apache. Permiten alojar **múltiples sitios web** en un único servidor físico.

**¿Cómo funciona?**

Cuando llega una petición HTTP, incluye una cabecera `Host` que indica qué sitio se está solicitando:

```http
GET /index.html HTTP/1.1
Host: www.ejemplo.com
```

Apache lee esta cabecera y decide qué Virtual Host debe manejar la petición.

**Tipos de Virtual Hosts:**

**1. Basados en nombre (Name-based)**

Varios dominios comparten la misma IP. Apache diferencia por el `ServerName`.

```apache
# Sitio 1: www.ejemplo.com
<VirtualHost *:80>
    ServerName www.ejemplo.com
    DocumentRoot /var/www/ejemplo
    
    ErrorLog ${APACHE_LOG_DIR}/ejemplo_error.log
    CustomLog ${APACHE_LOG_DIR}/ejemplo_access.log combined
</VirtualHost>

# Sitio 2: www.tienda.com
<VirtualHost *:80>
    ServerName www.tienda.com
    DocumentRoot /var/www/tienda
    
    ErrorLog ${APACHE_LOG_DIR}/tienda_error.log
    CustomLog ${APACHE_LOG_DIR}/tienda_access.log combined
</VirtualHost>
```

**2. Basados en IP (IP-based)**

Cada sitio tiene su propia IP:

```apache
# Sitio en IP 192.168.1.10
<VirtualHost 192.168.1.10:80>
    ServerName www.ejemplo.com
    DocumentRoot /var/www/ejemplo
</VirtualHost>

# Sitio en IP 192.168.1.11
<VirtualHost 192.168.1.11:80>
    ServerName www.tienda.com
    DocumentRoot /var/www/tienda
</VirtualHost>
```

**3. Basados en puerto**

Diferentes puertos para diferentes sitios:

```apache
Listen 8080
Listen 8081

<VirtualHost *:8080>
    ServerName www.ejemplo.com
    DocumentRoot /var/www/ejemplo
</VirtualHost>

<VirtualHost *:8081>
    ServerName www.tienda.com
    DocumentRoot /var/www/tienda
</VirtualHost>
```

**Ejemplo completo de Virtual Host:**

```apache
# Archivo: /etc/apache2/sites-available/mitienda.conf

<VirtualHost *:80>
    # Nombre principal del sitio
    ServerName www.mitienda.com
    
    # Nombres alternativos (alias)
    ServerAlias mitienda.com *.mitienda.com
    
    # Directorio raíz del sitio
    DocumentRoot /var/www/mitienda
    
    # Configuración del directorio
    <Directory /var/www/mitienda>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    # Logs específicos del sitio
    ErrorLog ${APACHE_LOG_DIR}/mitienda_error.log
    CustomLog ${APACHE_LOG_DIR}/mitienda_access.log combined
    
    # Configuración de PHP (si es necesario)
    <FilesMatch \.php$>
        SetHandler application/x-httpd-php
    </FilesMatch>
</VirtualHost>
```

**Activar el Virtual Host:**

```bash
# Crear el directorio del sitio
sudo mkdir -p /var/www/mitienda

# Crear una página de prueba
echo "<h1>Bienvenido a Mi Tienda</h1>" | sudo tee /var/www/mitienda/index.html

# Habilitar el sitio
sudo a2ensite mitienda.conf

# Recargar Apache
sudo systemctl reload apache2

# Añadir entrada al /etc/hosts para pruebas locales
echo "127.0.0.1 www.mitienda.com" | sudo tee -a /etc/hosts
```

Ahora accediendo a `http://www.mitienda.com` verás tu sitio.

!!! tip "Desactivar sitios"
    Para desactivar un sitio sin borrar su configuración:
    ```bash
    sudo a2dissite mitienda.conf
    sudo systemctl reload apache2
    ```

### 3. Nginx: el servidor web moderno de alto rendimiento

**Nginx** (pronunciado "engine-x") es el servidor web moderno que ha revolucionado el panorama desde su lanzamiento en 2004. Fue diseñado específicamente para resolver problemas de rendimiento que Apache tenía con miles de conexiones simultáneas.

#### 3.1. Historia y filosofía

Nginx fue creado por Igor Sysoev en Rusia para resolver el problema **C10K** (servir 10,000 clientes concurrentes). Apache, con su arquitectura basada en procesos/hilos, no escalaba bien para muchísimas conexiones simultáneas.

**Filosofía de diseño:**

- **Arquitectura asíncrona y basada en eventos**: Un solo proceso puede manejar miles de conexiones
- **Bajo consumo de memoria**: Mucho más eficiente que Apache
- **Alto rendimiento para contenido estático**: Extremadamente rápido sirviendo archivos
- **Proxy inverso excepcional**: Ideal para arquitecturas modernas

**Cuota de mercado actual:**

- Nginx ha superado a Apache en muchos rankings
- Es el servidor preferido para sitios de alto tráfico
- Usado por Netflix, Airbnb, WordPress.com, GitHub

#### 3.2. Nginx vs Apache: ¿cuál elegir?

| Aspecto                  | Apache                           | Nginx                     |
|:-------------------------|:---------------------------------|:--------------------------|
| **Rendimiento estático** | Bueno                            | Excelente                 |
| **Memoria**              | Mayor consumo                    | Menor consumo             |
| **Concurrencia**         | Buena                            | Excepcional               |
| **Configuración**        | Más compleja                     | Más simple                |
| **Módulos**              | Muchísimos                       | Menos, pero suficientes   |
| **`.htaccess`**          | Sí                               | No (todo en config)       |
| **PHP integrado**        | Sí (mod_php)                     | No (usa PHP-FPM)          |
| **Flexibilidad**         | Máxima                           | Menor                     |
| **Uso ideal**            | Hosting compartido, flexibilidad | Alto tráfico, APIs, proxy |

**¿Cuándo usar Apache?**

- Hosting compartido tradicional
- Necesitas `.htaccess`
- Máxima compatibilidad con software legacy
- Necesitas la enorme variedad de módulos de Apache

**¿Cuándo usar Nginx?**

- Aplicaciones de alto tráfico
- Servir contenido estático
- Como proxy inverso
- Arquitecturas modernas con APIs
- Eficiencia de recursos es crítica

#### 3.3. Instalación de Nginx

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install nginx

# Iniciar Nginx
sudo systemctl start nginx

# Habilitar inicio automático
sudo systemctl enable nginx

# Verificar estado
sudo systemctl status nginx
```

Accede a `http://localhost` y verás la página de bienvenida de Nginx.

#### 3.4. Estructura de Nginx

```
/etc/nginx/
├── nginx.conf              # Configuración principal
├── sites-available/        # Sitios disponibles
├── sites-enabled/          # Sitios habilitados (enlaces)
├── conf.d/                 # Configuraciones adicionales
└── snippets/               # Fragmentos reutilizables

/var/www/                   # Directorio web por defecto
└── html/
    └── index.nginx-debian.html

/var/log/nginx/             # Logs
├── access.log
└── error.log
```

#### 3.5. Configuración básica de Nginx

El archivo `/etc/nginx/nginx.conf` contiene la configuración global:

```nginx
user www-data;
worker_processes auto;  # Procesos worker (normalmente 1 por CPU)
pid /run/nginx.pid;

events {
    worker_connections 1024;  # Conexiones por worker
}

http {
    # Configuración HTTP
    include /etc/nginx/mime.types;
    default_type application/octet-stream;
    
    # Logs
    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;
    
    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    
    # Gzip
    gzip on;
    gzip_types text/plain text/css application/json application/javascript;
    
    # Incluir configuraciones de sitios
    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}
```

**Server Block (equivalente a Virtual Host):**

```nginx
# Archivo: /etc/nginx/sites-available/ejemplo

server {
    listen 80;
    listen [::]:80;
    
    server_name www.ejemplo.com ejemplo.com;
    root /var/www/ejemplo;
    index index.html index.php;
    
    # Logs específicos
    access_log /var/log/nginx/ejemplo_access.log;
    error_log /var/log/nginx/ejemplo_error.log;
    
    # Servir archivos estáticos
    location / {
        try_files $uri $uri/ =404;
    }
    
    # PHP con PHP-FPM
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.1-fpm.sock;
    }
    
    # Denegar acceso a archivos ocultos
    location ~ /\. {
        deny all;
    }
}
```

**Activar el sitio:**

```bash
# Crear enlace simbólico
sudo ln -s /etc/nginx/sites-available/ejemplo /etc/nginx/sites-enabled/

# Verificar configuración
sudo nginx -t

# Recargar Nginx
sudo systemctl reload nginx
```

### 4. Servidores de aplicaciones: Tomcat para Java

Mientras que Apache y Nginx son **servidores web**, **Tomcat** es un **servidor de aplicaciones** especializado en ejecutar aplicaciones Java.

#### 4.1. ¿Qué es un servidor de aplicaciones?

Un servidor de aplicaciones va más allá de un servidor web. Proporciona:

- **Contenedor de Servlets/JSP**: Ejecuta código Java web
- **Gestión de ciclo de vida**: Carga, inicia, detiene aplicaciones
- **Pool de conexiones**: Gestiona conexiones a bases de datos eficientemente
- **Gestión de sesiones**: Maneja sesiones de usuario
- **Clustering**: Distribución de carga entre múltiples instancias
- **Transacciones**: Soporte para transacciones distribuidas

#### 4.2. Apache Tomcat

**Tomcat** es el servidor de aplicaciones Java más popular. Es la implementación de referencia para:
- **Servlets**
- **JavaServer Pages (JSP)**

**Arquitectura:**

```
[Cliente Web]
    ↓
[Servidor Web: Apache/Nginx] (Opcional, como proxy)
    ↓
[Tomcat] ← Ejecuta Servlets/JSP
    ↓
[Base de Datos]
```

Tomcat puede funcionar solo o detrás de Apache/Nginx como proxy inverso.

#### 4.3. Instalación de Tomcat

**Requisitos:**
- Java JDK instalado

```bash
# Instalar JDK
sudo apt install default-jdk

# Verificar Java
java -version

# Descargar Tomcat (ejemplo versión 10)
wget https://downloads.apache.org/tomcat/tomcat-10/v10.1.15/bin/apache-tomcat-10.1.15.tar.gz

# Extraer
sudo tar xzf apache-tomcat-10.1.15.tar.gz -C /opt/

# Crear enlace simbólico
sudo ln -s /opt/apache-tomcat-10.1.15 /opt/tomcat

# Crear usuario tomcat
sudo useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat

# Cambiar permisos
sudo chown -R tomcat:tomcat /opt/tomcat
```

**Iniciar Tomcat:**

```bash
# Iniciar
sudo /opt/tomcat/bin/startup.sh

# Verificar
curl http://localhost:8080

# Detener
sudo /opt/tomcat/bin/shutdown.sh
```

Accede a `http://localhost:8080` y verás la página de inicio de Tomcat.

#### 4.4. Desplegar una aplicación en Tomcat

Las aplicaciones Java web se empaquetan en archivos **WAR** (Web Application Archive).

```bash
# Copiar el WAR al directorio webapps
sudo cp mi-aplicacion.war /opt/tomcat/webapps/

# Tomcat lo despliega automáticamente
# La aplicación estará disponible en:
# http://localhost:8080/mi-aplicacion/
```

### 5. Gestores de bases de datos

Toda aplicación web necesita almacenar datos. Los gestores de bases de datos son el componente que hace esto posible.

#### 5.1. MySQL/MariaDB

**MySQL** es el gestor de bases de datos más popular en aplicaciones web.

```bash
# Instalar MySQL
sudo apt install mysql-server

# Segurizar instalación
sudo mysql_secure_installation

# Acceder
sudo mysql -u root -p

# Crear base de datos
CREATE DATABASE mitienda;

# Crear usuario
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON mitienda.* TO 'webapp'@'localhost';
FLUSH PRIVILEGES;
```

#### 5.2. PostgreSQL

**PostgreSQL** es más robusto y con más características avanzadas.

```bash
# Instalar
sudo apt install postgresql postgresql-contrib

# Acceder
sudo -u postgres psql

# Crear base de datos
CREATE DATABASE mitienda;

# Crear usuario
CREATE USER webapp WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE mitienda TO webapp;
```

#### 5.3. MongoDB

**MongoDB** es NoSQL, ideal para datos flexibles.

```bash
# Instalar
sudo apt install mongodb

# Iniciar
sudo systemctl start mongodb

# Acceder
mongo
```

## Resumen de la unidad

En esta unidad hemos comprendido:

1. **Los servidores web** son el software que ejecuta nuestras aplicaciones, escucha peticiones HTTP y devuelve respuestas.

2. **Apache** es el veterano robusto, extremadamente configurable con su arquitectura modular, ideal para hosting tradicional.

3. **Virtual Hosts** permiten alojar múltiples sitios en un solo servidor, diferenciando por nombre de dominio o IP.

4. **Nginx** es el servidor moderno de alto rendimiento, con arquitectura asíncrona, ideal para alto tráfico y como proxy.

5. **Tomcat** es el servidor de aplicaciones Java que ejecuta Servlets y JSP, esencial para aplicaciones Java EE.

6. **Los gestores de bases de datos** (MySQL, PostgreSQL, MongoDB) almacenan y gestionan los datos de nuestras aplicaciones.

Este conocimiento es fundamental para desplegar y administrar aplicaciones web en producción.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Apache Software Foundation. (2024). *Apache HTTP Server Documentation*. [https://httpd.apache.org/docs/](https://httpd.apache.org/docs/)
- NGINX Inc. (2024). *NGINX Documentation*. [https://nginx.org/en/docs/](https://nginx.org/en/docs/)
- Apache Tomcat. (2024). *Tomcat Documentation*. [https://tomcat.apache.org/](https://tomcat.apache.org/)

## Recursos adicionales

- [DigitalOcean Apache Tutorials](https://www.digitalocean.com/community/tags/apache) - Guías prácticas
- [Nginx Beginner's Guide](https://nginx.org/en/docs/beginners_guide.html) - Guía oficial
- [Tomcat Setup Guide](https://tomcat.apache.org/tomcat-10.1-doc/setup.html) - Configuración completa
