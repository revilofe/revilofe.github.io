# Curso Docker - Módulo 3

## Almacenamiento y Redes

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice Módulo 3

* Volúmenes y persistencia de datos
* Bind mounts para desarrollo
* Redes Docker
* Comunicación entre contenedores
* Ejemplo práctico: WordPress + MySQL

---

## 1. Persistencia de Datos


### Contenedores Efímeros

* Los datos en contenedores son temporales.
* Se pierden al eliminar el contenedor.
* Necesitamos mecanismos de persistencia.

Note: Por diseño, los contenedores son efímeros. Los datos creados dentro de un contenedor se pierden cuando lo eliminamos. Para aplicaciones con estado (bases de datos, uploads, configuraciones) necesitamos persistencia más allá del ciclo de vida del contenedor.


### Opciones de Almacenamiento

* **Volúmenes Docker**: Gestionados por Docker.
* **Bind Mounts**: Directorios del host.
* **tmpfs**: Almacenamiento en memoria (temporal).

Note: Docker ofrece tres tipos de almacenamiento. Volúmenes son gestionados por Docker, ideales para producción. Bind mounts mapean directorios del host, perfectos para desarrollo. tmpfs almacena en memoria RAM, útil para datos temporales sensibles.


### Volúmenes Docker

```bash
$ docker volume create miweb
$ docker volume ls
DRIVER    VOLUME NAME
local     miweb

$ docker run -d --name web \
  -v miweb:/usr/local/apache2/htdocs \
  httpd:2.4
```

Note: Los volúmenes Docker son la forma recomendada de persistir datos. Se crean con docker volume create y se montan en contenedores con -v. Docker los gestiona completamente en /var/lib/docker/volumes/.


### Persistencia de Volúmenes

```bash
$ docker exec web bash -c \
  'echo "<h1>Hola</h1>" > /usr/local/apache2/htdocs/index.html'

$ docker rm -f web

$ docker run -d --name web2 \
  -v miweb:/usr/local/apache2/htdocs \
  -p 8080:80 httpd:2.4

$ curl http://localhost:8080
<h1>Hola</h1>
```

Note: Los datos en volúmenes persisten más allá del ciclo de vida del contenedor. Creamos archivo, eliminamos contenedor, creamos nuevo contenedor con mismo volumen y el archivo sigue ahí.


### Bind Mounts

```bash
$ mkdir ~/web
$ echo "<h1>Curso Docker</h1>" > ~/web/index.html

$ docker run -d --name web \
  -v /home/usuario/web:/usr/local/apache2/htdocs \
  -p 8080:80 \
  httpd:2.4
```

Note: Bind mounts mapean directorios del host al contenedor. Requieren paths absolutos. Son perfectos para desarrollo porque podemos editar archivos en el host y ver cambios inmediatamente en el contenedor.


### Comandos de Volúmenes

```bash
$ docker volume ls              # Listar
$ docker volume create nombre   # Crear
$ docker volume inspect nombre  # Información
$ docker volume rm nombre       # Eliminar
$ docker volume prune          # Limpiar no usados
```

Note: Docker proporciona comandos completos para gestionar volúmenes. Podemos listarlos, crear nuevos, ver detalles, eliminar específicos o limpiar todos los que no estén en uso.

---

## 2. Redes Docker


### Conceptos de Red

* Contenedores tienen su propia interfaz de red.
* Necesitan comunicarse entre sí y con el exterior.
* Docker proporciona aislamiento de red.
* Diferentes tipos de redes disponibles.

Note: Docker crea una red virtual completa para contenedores. Cada contenedor obtiene su propia interfaz de red, IP y tabla de enrutamiento. Por defecto están aislados pero podemos conectarlos.


### Tipos de Redes

* **bridge**: Red por defecto, comunicación local.
* **host**: Usa directamente red del host.
* **none**: Sin red, aislamiento total.
* **Definidas por usuario**: Con DNS automático.

Note: Bridge es la red por defecto. Host elimina el aislamiento de red. None desactiva networking completamente. Las redes definidas por usuario son las mejores porque proporcionan resolución DNS automática.


### Redes Por Defecto

```bash
$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
a1b2c3d4e5f6   bridge    bridge    local
f6e5d4c3b2a1   host      host      local
b2a1f6e5d4c3   none      null      local
```

Note: Docker crea automáticamente tres redes: bridge (red por defecto donde se conectan contenedores), host (red del anfitrión), y none (sin red).


### Creando Redes Personalizadas

```bash
$ docker network create mi_red

$ docker network ls
NETWORK ID     NAME      DRIVER    SCOPE
8f7e6d5c4b3a   mi_red    bridge    local

$ docker network inspect mi_red
```

Note: Crear redes personalizadas es simple con docker network create. Estas redes proporcionan resolución DNS automática, permitiendo que contenedores se comuniquen por nombre.


### Conectando Contenedores a Red

```bash
$ docker run -d --name web --network mi_red nginx
$ docker run -d --name db --network mi_red mysql

# Desde web podemos acceder a db por nombre
$ docker exec web ping db
PING db (172.18.0.3): 56 data bytes
```

Note: Contenedores en la misma red pueden comunicarse por nombre gracias al DNS automático de Docker. No necesitamos saber IPs, solo nombres de contenedor.


### Ventajas de Redes Personalizadas

* Resolución DNS automática por nombre.
* Mejor aislamiento entre aplicaciones.
* Fácil conexión/desconexión en caliente.
* Configuración de red más flexible.

Note: Las redes definidas por usuario son superiores a la red bridge por defecto. DNS automático, mejor aislamiento, y mayor flexibilidad hacen que sean la opción recomendada para aplicaciones serias.

---

## 3. Ejemplo: WordPress + MySQL


### Arquitectura de la Aplicación

* Contenedor WordPress (aplicación web).
* Contenedor MySQL (base de datos).
* Red privada para comunicación segura.
* Volúmenes para persistir datos.
* Solo WordPress expuesto públicamente.

Note: WordPress es un ejemplo perfecto de aplicación multi-contenedor. Separamos la aplicación web de la base de datos, los conectamos en una red privada, usamos volúmenes para datos críticos, y solo exponemos el puerto web.


### Paso 1: Crear Red

```bash
$ docker network create red_wp
```

Note: Primero creamos una red dedicada para nuestra aplicación WordPress. Esto aísla nuestros contenedores de otros en el sistema y permite comunicación segura entre WordPress y MySQL.


### Paso 2: Desplegar MySQL

```bash
$ docker run -d --name mysql_wp \
  --network red_wp \
  -v mysql_data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=wordpress \
  -e MYSQL_USER=wpuser \
  -e MYSQL_PASSWORD=wppass \
  mariadb
```

Note: Desplegamos MariaDB conectándolo a red_wp. Usamos un volumen para persistir datos de la base de datos. Configuramos con variables de entorno: contraseña root, base de datos, usuario y contraseña. No mapeamos puerto 3306 porque solo WordPress accederá internamente.


### Paso 3: Desplegar WordPress

```bash
$ docker run -d --name wordpress \
  --network red_wp \
  -v wp_data:/var/www/html \
  -e WORDPRESS_DB_HOST=mysql_wp \
  -e WORDPRESS_DB_USER=wpuser \
  -e WORDPRESS_DB_PASSWORD=wppass \
  -e WORDPRESS_DB_NAME=wordpress \
  -p 80:80 \
  wordpress
```

Note: Desplegamos WordPress en la misma red. Usamos volumen para persistir contenido. La variable WORDPRESS_DB_HOST usa el nombre del contenedor MySQL (mysql_wp). Docker lo resuelve automáticamente a la IP correcta. Solo WordPress expone puerto público (80).


### Verificando la Instalación

```bash
$ docker ps
CONTAINER ID   IMAGE       PORTS                NAMES
abc123def456   wordpress   0.0.0.0:80->80/tcp   wordpress
def456ghi789   mariadb     3306/tcp             mysql_wp

# Acceder en navegador
http://localhost
```

Note: Verificamos que ambos contenedores están ejecutándose. WordPress expone puerto 80 mapeado a nuestro host. MySQL expone 3306 pero solo internamente en la red Docker. Accedemos a http://localhost y vemos el asistente de instalación de WordPress.


### ¿Por Qué Funciona?

* Ambos contenedores en red `red_wp`.
* DNS automático: `mysql_wp` se resuelve a IP.
* Puerto 3306 accesible dentro de la red.
* WordPress conecta a `mysql_wp:3306` sin IPs.
* Volúmenes persisten datos importantes.

Note: La magia está en la red Docker. Ambos contenedores están en red_wp y pueden comunicarse. Docker resuelve 'mysql_wp' a su IP automáticamente. MySQL no expone puerto públicamente, solo dentro de la red Docker. Los volúmenes garantizan que los datos sobreviven si recreamos contenedores.


### Gestión y Mantenimiento

```bash
# Ver logs de WordPress
$ docker logs wordpress

# Acceder a MySQL
$ docker exec -it mysql_wp mysql -u wpuser -p

# Backup de volúmenes
$ docker run --rm -v mysql_data:/data \
  -v $(pwd):/backup ubuntu \
  tar czf /backup/mysql_backup.tar.gz /data
```

Note: Podemos ver logs para debugging, acceder a MySQL directamente desde el contenedor, y hacer backups de los volúmenes. La separación de datos (volúmenes) y aplicación (contenedores) facilita el mantenimiento.

---

## 4. Más Ejemplos de Redes


### Ejemplo: Aplicación con Frontend y Backend

```bash
$ docker network create app_network

$ docker run -d --name backend \
  --network app_network \
  -e DATABASE_URL=postgresql://db:5432/mydb \
  my_backend_image

$ docker run -d --name frontend \
  --network app_network \
  -e API_URL=http://backend:5000 \
  -p 80:80 \
  my_frontend_image
```

Note: Podemos crear arquitecturas complejas con múltiples servicios. Frontend se comunica con backend usando el nombre 'backend' como hostname. Backend podría conectarse a una base de datos usando 'db' como hostname. Todo gracias al DNS de Docker.


### Múltiples Redes

```bash
$ docker network create frontend_net
$ docker network create backend_net

$ docker run -d --name api \
  --network frontend_net \
  --network backend_net \
  api_image

$ docker run -d --name web \
  --network frontend_net \
  -p 80:80 \
  web_image

$ docker run -d --name db \
  --network backend_net \
  postgres
```

Note: Un contenedor puede estar en múltiples redes. Aquí 'api' está en dos redes: puede comunicarse con 'web' vía frontend_net y con 'db' vía backend_net. Pero 'web' y 'db' están aislados entre sí. Esto proporciona segmentación de red avanzada.


### Desconectar de Red

```bash
$ docker network disconnect mi_red contenedor1
$ docker network connect otra_red contenedor1
```

Note: Podemos conectar y desconectar contenedores de redes en caliente, sin necesidad de reiniciarlos. Esto proporciona flexibilidad para cambiar arquitecturas de red dinámicamente.

---

## Resumen Módulo 3


### Almacenamiento: Conceptos Clave

* Contenedores efímeros requieren persistencia externa.
* Volúmenes Docker: mejor opción para producción.
* Bind mounts: ideales para desarrollo local.
* Datos críticos siempre en volúmenes/bind mounts.

Note: El almacenamiento es fundamental para aplicaciones con estado. Aprendimos a usar volúmenes Docker gestionados por Docker para producción, y bind mounts que mapean directorios del host para desarrollo. Siempre debemos identificar qué datos necesitan persistir.


### Redes: Conceptos Clave

* Redes personalizadas con DNS automático.
* Comunicación por nombre, no por IP.
* Aislamiento y seguridad entre aplicaciones.
* Solo exponer servicios públicos necesarios.

Note: Las redes Docker permiten que contenedores se comuniquen de forma segura. Las redes definidas por usuario proporcionan DNS automático, haciendo la configuración robusta y simple. Podemos crear arquitecturas complejas con segmentación de red apropiada.


### Arquitectura Multi-Contenedor

* Separar servicios en contenedores independientes.
* Conectar via redes Docker privadas.
* Persistir datos con volúmenes.
* Exponer solo endpoints públicos necesarios.

Note: El patrón demostrado con WordPress es universal: separar componentes en contenedores, conectarlos en redes privadas, usar volúmenes para persistencia, y exponer solo lo necesario públicamente. Este es el fundamento de arquitecturas de microservicios.


### Comandos Esenciales

* `docker volume create/ls/rm/inspect`
* `docker network create/ls/inspect`
* `-v` para montar volúmenes y bind mounts
* `--network` para conectar a redes

Note: Dominamos comandos esenciales para almacenamiento y redes. Estos comandos son fundamentales para cualquier despliegue Docker más allá de contenedores individuales simples.


### Próximo Módulo

**Módulo 4: Docker Compose**

* Definir infraestructura como código.
* Gestionar múltiples contenedores fácilmente.
* Archivo docker-compose.yaml.
* Orquestación simplificada.

Note: Hasta ahora hemos gestionado contenedores individualmente con comandos docker. Esto funciona pero se vuelve tedioso. En el próximo módulo aprenderemos Docker Compose que permite definir aplicaciones multi-contenedor en un archivo YAML y gestionarlas con comandos simples.


### ¡Gracias!

¿Preguntas sobre el Módulo 3?

Note: Esto concluye el módulo sobre almacenamiento y redes. Hemos cubierto fundamentos para construir aplicaciones reales con Docker. Os animo a practicar creando vuestras propias aplicaciones multi-contenedor, experimentando con diferentes configuraciones de red y almacenamiento.
