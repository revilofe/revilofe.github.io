# Curso Docker - Módulo 4

## Docker Compose

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice Módulo 4

* Introducción a Docker Compose
* Archivo docker-compose.yaml
* Comandos docker compose
* Gestión de volúmenes y redes
* Ejemplos prácticos

---

## 1. Introducción a Docker Compose


### ¿Qué es Docker Compose?

* Herramienta para aplicaciones multi-contenedor.
* Define servicios en archivo YAML.
* Un comando para levantar toda la infraestructura.
* Perfecto para desarrollo y testing.

Note: Docker Compose simplifica la gestión de aplicaciones con múltiples contenedores. En lugar de ejecutar múltiples comandos docker run con opciones complejas, definimos todo en un archivo docker-compose.yaml y lo levantamos con un solo comando.


### Ventajas de Docker Compose

* Infraestructura como código (versionable).
* Fácil de compartir con el equipo.
* Reproducible en cualquier entorno.
* Simplifica enormemente el desarrollo local.

Note: Docker Compose trata la infraestructura como código. El archivo docker-compose.yaml puede versionarse en Git, compartirse con el equipo, y garantiza que todos trabajen con la misma configuración. Es especialmente valioso para desarrollo local.


### Instalación

```bash
# En Linux
$ sudo apt install docker-compose-plugin

# Verificar instalación
$ docker compose version
Docker Compose version v2.20.0
```

Note: Docker Compose v2 viene como plugin de Docker. Se instala con el gestor de paquetes del sistema. La versión antigua se llamaba docker-compose (con guión), la nueva es docker compose (con espacio, sin guión).

---

## 2. Archivo docker-compose.yaml


### Estructura Básica

```yaml
version: '3.8'

services:
  web:
    image: nginx
    ports:
      - "80:80"
  
  db:
    image: mysql
    environment:
      MYSQL_ROOT_PASSWORD: password
```

Note: El archivo docker-compose.yaml tiene una estructura clara y declarativa. Definimos servicios (contenedores), cada uno con su configuración: imagen, puertos, variables de entorno, volúmenes, redes, etc.


### Sección services

```yaml
services:
  webapp:
    image: nginx:alpine
    container_name: mi_web
    ports:
      - "8080:80"
    networks:
      - mi_red
    volumes:
      - ./html:/usr/share/nginx/html
```

Note: Cada servicio representa un contenedor. Especificamos imagen a usar, nombre del contenedor, puertos mapeados, redes a las que se conecta, y volúmenes a montar. Es el equivalente declarativo de un comando docker run.


### Variables de Entorno

```yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: mydb
      MYSQL_USER: user
      MYSQL_PASSWORD: userpass
```

Note: Las variables de entorno se definen en la sección environment de cada servicio. Es mucho más limpio y mantenible que pasar múltiples opciones -e en la línea de comandos.


### Volúmenes

```yaml
services:
  db:
    image: mysql
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:
```

Note: Los volúmenes se definen en dos lugares: en el servicio indicamos dónde montarlo, y en la sección volumes global declaramos su creación. Docker Compose gestiona automáticamente la creación de volúmenes nombrados.


### Redes

```yaml
services:
  web:
    networks:
      - frontend
  api:
    networks:
      - frontend
      - backend

networks:
  frontend:
  backend:
```

Note: Podemos definir múltiples redes para segmentar servicios. Un servicio puede estar en varias redes. Docker Compose crea automáticamente las redes con driver bridge y DNS habilitado.


### Dependencias entre Servicios

```yaml
services:
  web:
    image: wordpress
    depends_on:
      - db
  
  db:
    image: mysql
```

Note: depends_on indica el orden de inicio. Docker Compose iniciará 'db' antes que 'web'. Sin embargo, no espera a que el servicio esté "listo", solo a que el contenedor se inicie. Para esperar a que esté completamente operativo, necesitamos health checks.

---

## 3. Comandos Docker Compose


### Levantar Servicios

```bash
$ docker compose up
$ docker compose up -d         # modo detached
$ docker compose up --build    # rebuild imágenes
```

Note: docker compose up lee el archivo docker-compose.yaml del directorio actual y crea/inicia todos los servicios. Con -d ejecuta en background. --build fuerza reconstrucción de imágenes si hay Dockerfiles. Crea automáticamente redes y volúmenes necesarios.


### Detener y Eliminar

```bash
$ docker compose stop         # Detener sin eliminar
$ docker compose start        # Reiniciar servicios parados
$ docker compose down         # Detener y eliminar contenedores
$ docker compose down -v      # También eliminar volúmenes
```

Note: stop detiene contenedores pero los mantiene. start los reinicia. down detiene y elimina contenedores y redes, pero preserva volúmenes por seguridad. Con -v también elimina volúmenes, útil para empezar completamente desde cero.


### Ver Estado y Logs

```bash
$ docker compose ps
$ docker compose logs
$ docker compose logs -f web     # seguir logs de un servicio
$ docker compose logs --tail=50  # últimas 50 líneas
```

Note: ps muestra el estado de todos los servicios. logs muestra los logs de todos los servicios o de uno específico. Con -f seguimos los logs en tiempo real. --tail limita el número de líneas mostradas.


### Ejecutar Comandos

```bash
$ docker compose exec web bash
$ docker compose exec db mysql -u root -p
$ docker compose run --rm web ls -la
```

Note: exec ejecuta comandos en servicios en ejecución, similar a docker exec. run crea un nuevo contenedor temporal para ejecutar un comando (útil para tareas one-off). --rm elimina el contenedor tras ejecutar.


### Escalar Servicios

```bash
$ docker compose up -d --scale web=3
```

Note: Podemos escalar servicios creando múltiples instancias. Útil para testing de balanceo de carga o alta disponibilidad. Cada instancia es un contenedor independiente del mismo servicio.

---

## 4. Ejemplo Completo: WordPress


### docker-compose.yaml

```yaml
version: '3.8'

services:
  db:
    image: mariadb:10.6
    volumes:
      - db_data:/var/lib/mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    networks:
      - backend

  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    volumes:
      - wp_data:/var/www/html
    ports:
      - "80:80"
    restart: always
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress
    networks:
      - backend

volumes:
  db_data:
  wp_data:

networks:
  backend:
```

Note: Este archivo completo define toda la infraestructura de WordPress. Dos servicios (db y wordpress), volúmenes para persistencia, red para comunicación, variables de entorno para configuración. restart: always reinicia contenedores automáticamente si se caen.


### Desplegar la Aplicación

```bash
$ docker compose up -d

[+] Running 5/5
 ✔ Network wordpress_backend        Created
 ✔ Volume "wordpress_db_data"       Created
 ✔ Volume "wordpress_wp_data"       Created
 ✔ Container wordpress-db-1         Started
 ✔ Container wordpress-wordpress-1  Started
```

Note: Un solo comando levanta toda la aplicación. Docker Compose crea automáticamente la red, los volúmenes, y los contenedores en el orden correcto (db primero por depends_on). En segundos tenemos WordPress completo funcionando.


### Verificar Estado

```bash
$ docker compose ps
NAME                    IMAGE         STATUS
wordpress-db-1          mariadb:10.6  Up 2 minutes
wordpress-wordpress-1   wordpress     Up 2 minutes

$ docker compose logs wordpress
wordpress-wordpress-1  | WordPress started
```

Note: Verificamos que ambos servicios están ejecutándose correctamente. Podemos ver logs individuales o de todos los servicios. Accedemos a http://localhost y WordPress está listo para configurar.


### Gestión Diaria

```bash
# Reiniciar servicio específico
$ docker compose restart wordpress

# Ver logs en tiempo real
$ docker compose logs -f

# Actualizar imágenes
$ docker compose pull
$ docker compose up -d

# Backup de volúmenes
$ docker compose down
$ cp -r /var/lib/docker/volumes/wordpress_* ~/backup/
```

Note: La gestión es simple y centralized. Reiniciamos servicios individuales, seguimos logs, actualizamos imágenes con pull y recreamos contenedores. Para backups, detenemos servicios y copiamos volúmenes.

---

## 5. Características Avanzadas


### Variables desde Archivo .env

```
# .env
MYSQL_ROOT_PASSWORD=supersecret
MYSQL_DATABASE=mydb
WP_VERSION=latest
```

```yaml
# docker-compose.yaml
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
  wordpress:
    image: wordpress:${WP_VERSION}
```

Note: Docker Compose lee automáticamente un archivo .env en el mismo directorio. Podemos usar variables con ${VARIABLE}. Esto es perfecto para mantener secretos fuera del archivo yaml versionado. El .env nunca debe versionarse en Git.


### Múltiples Archivos Compose

```bash
# docker-compose.yaml - configuración base
# docker-compose.override.yaml - desarrollo
# docker-compose.prod.yaml - producción

# Usar archivo específico
$ docker compose -f docker-compose.yaml \
  -f docker-compose.prod.yaml up -d
```

Note: Podemos tener múltiples archivos compose para diferentes entornos. Un archivo base con configuración común, y archivos de override para desarrollo, testing, producción. Esto evita duplicación y facilita mantenimiento.


### Health Checks

```yaml
services:
  db:
    image: mysql
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
```

Note: Health checks permiten a Docker saber si un servicio está realmente operativo, no solo si el contenedor está corriendo. El servicio se marca como "healthy" solo si el test pasa. Otros servicios pueden esperar a que esté healthy antes de conectarse.


### Build desde Dockerfile

```yaml
services:
  web:
    build:
      context: ./app
      dockerfile: Dockerfile
    ports:
      - "8080:80"
```

Note: Docker Compose puede construir imágenes desde Dockerfiles. Especificamos el contexto (directorio) y el Dockerfile. Con docker compose build construimos las imágenes, con docker compose up --build lo hacemos automáticamente al levantar.

---

## 6. Mejores Prácticas


### Estructura de Proyecto

```
proyecto/
├── docker-compose.yaml
├── .env.example
├── .dockerignore
├── app/
│   ├── Dockerfile
│   └── src/
├── nginx/
│   └── nginx.conf
└── README.md
```

Note: Organizar proyecto con estructura clara. docker-compose.yaml en la raíz, subdirectorios para cada servicio con sus Dockerfiles y configuraciones. Incluir .env.example con variables necesarias (sin valores reales) para documentación.


### Versionado en Git

```gitignore
# .gitignore
.env
*.log
volumes/
.docker/
```

Note: Versionar docker-compose.yaml y Dockerfiles en Git. NUNCA versionar .env con secretos reales. Incluir .env.example como plantilla. Ignorar logs, volúmenes locales y otros archivos temporales.


### Nombres Explícitos

```yaml
services:
  postgres-db:
    container_name: myapp_postgres
    image: postgres:14
  
  redis-cache:
    container_name: myapp_redis
    image: redis:alpine
```

Note: Usar nombres descriptivos para servicios. container_name proporciona nombres predecibles en lugar de nombres generados. Facilita debugging y referencia desde logs o herramientas de monitorización.


### Documentación

```yaml
# docker-compose.yaml
services:
  # Base de datos principal - PostgreSQL 14
  db:
    image: postgres:14
    # Persistir datos en volumen nombrado
    volumes:
      - postgres_data:/var/lib/postgresql/data
```

Note: Comentar el archivo compose para documentar decisiones y configuraciones importantes. Ayuda a otros desarrolladores (y a tu yo futuro) a entender la arquitectura y configuración.

---

## Resumen Módulo 4


### Docker Compose Simplifica

* Un archivo define toda la infraestructura.
* Un comando levanta todo el stack.
* Ideal para desarrollo, testing y producción.
* Infraestructura como código versionable.

Note: Docker Compose transforma la gestión de aplicaciones multi-contenedor de compleja a trivial. Definimos servicios, volúmenes, redes y configuraciones en YAML, lo versionamos en Git, y cualquiera puede levantar el entorno con un comando.


### Componentes Principales

* **services**: Definición de contenedores.
* **volumes**: Almacenamiento persistente.
* **networks**: Redes para comunicación.
* **environment**: Variables de configuración.

Note: El archivo compose se estructura en secciones claras: services para contenedores, volumes para persistencia, networks para conectividad, y environment para configuración. Esta estructura declarativa es intuitiva y poderosa.


### Comandos Clave

* `docker compose up/down`: Levantar/detener.
* `docker compose logs`: Ver logs.
* `docker compose ps`: Ver estado.
* `docker compose exec`: Ejecutar comandos.

Note: Los comandos compose son intuitivos y potentes. up para iniciar todo, down para limpiar, logs para debugging, exec para acceder a servicios. Dominales es fundamental para desarrollo eficiente.


### Flujo de Trabajo

1. Definir servicios en docker-compose.yaml.
2. Versionar archivo en Git.
3. Compartir con el equipo.
4. Cada desarrollador: `docker compose up -d`
5. Entorno idéntico para todos.

Note: El flujo con Compose es simple: definir, versionar, compartir, ejecutar. Garantiza que todo el equipo trabaja con el mismo entorno, eliminando el clásico "en mi máquina funciona". Es el estándar de la industria para desarrollo local.


### Próximo Módulo

**Módulo 5: Creación de Imágenes**

* Construcción de imágenes personalizadas.
* Dockerfiles.
* Mejores prácticas de construcción.
* Distribución de imágenes.
* Ciclo de vida de aplicaciones.

Note: Hasta ahora hemos usado imágenes existentes de Docker Hub. En el último módulo aprenderemos a crear nuestras propias imágenes Docker personalizadas usando Dockerfiles, siguiendo mejores prácticas de la industria.


### ¡Gracias!

¿Preguntas sobre el Módulo 4?

Note: Docker Compose es una herramienta esencial que simplifica enormemente el desarrollo y testing. Os animo a experimentar creando vuestros propios archivos compose para vuestras aplicaciones y proyectos. Es una habilidad fundamental en desarrollo moderno.
