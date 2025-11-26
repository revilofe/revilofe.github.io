---
title: "UD 2 - 2.4 Docker Compose"
description: Gestión de aplicaciones multi-contenedor con Docker Compose
summary: Docker Compose, docker-compose.yml, orquestación
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: "material/file-document-outline"
permalink: /daw/unidad2/2.4
categories:
    - DAW
tags:
    - Docker
    - Docker Compose
    - Orquestación
---

## 2.4. Docker Compose

Docker Compose es una herramienta que nos permite definir y ejecutar aplicaciones Docker multi-contenedor. Mediante un archivo YAML definimos todos los servicios, redes y volúmenes de nuestra aplicación, y con un solo comando podemos crear e iniciar todos los servicios.

### 1. ¿Qué es Docker Compose?

Docker Compose simplifica enormemente el trabajo con aplicaciones que requieren múltiples contenedores. En lugar de ejecutar múltiples comandos `docker run` con numerosas opciones, definimos toda la configuración en un archivo `docker-compose.yml`.

**Ventajas:**

- **Simplicidad**: Un solo archivo de configuración
- **Reproducibilidad**: Mismo entorno en cualquier máquina
- **Gestión centralizada**: Iniciar/detener toda la aplicación con un comando
- **Versionado**: El archivo puede controlarse con Git
- **Escalabilidad**: Fácil escalar servicios

### 2. Instalación de Docker Compose

Docker Compose v2 viene integrado como plugin de Docker. Se instala automáticamente con Docker Desktop o Docker Engine reciente.

**Verificar instalación:**

```bash
$ docker compose version
Docker Compose version v2.20.2
```

**Sintaxis:**

- Docker Compose v2: `docker compose` (plugin)
- Docker Compose v1: `docker-compose` (binario independiente)

En este curso usaremos la sintaxis v2: `docker compose`

### 3. El archivo docker-compose.yml

El archivo `docker-compose.yml` es el corazón de Docker Compose. Define toda tu aplicación en un formato legible y versionable.

#### 3.1. Estructura básica

Esta es la estructura mínima de un archivo `docker-compose.yml`:

```yaml
version: '3.8'  # Versión de docker-compose (opcional en v2)

services:
  # Definición de servicios (contenedores)
  servicio1:
    image: nginx
    ports:
      - "80:80"
  
  servicio2:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secreto

volumes:
  # Definición de volúmenes

networks:
  # Definición de redes
```

**Explicación de cada sección:**

**1. `version: '3.8'`**

- Define la versión del formato del archivo
- `3.8` es una versión moderna y compatible
- En Docker Compose v2 es opcional (usa la más reciente si no se especifica)
- Versiones anteriores: `2.x`, `3.0`, `3.1`... hasta `3.8`

!!! tip "¿Qué versión usar?"
    Usa `3.8` o simplemente omite la línea. Docker Compose v2 la ignora pero ayuda a la documentación.

**2. `services:`**

La sección más importante. Aquí defines cada **servicio** (contenedor) de tu aplicación.

```yaml
services:
  servicio1:      # Nombre del servicio (tú lo eliges)
    image: nginx  # Imagen Docker a usar
    ports:        # Puertos a mapear
      - "80:80"   # host:contenedor
```

**¿Qué es un servicio?**

Un servicio es un contenedor que cumple una función específica:
- `web`: Servidor web (nginx, apache)
- `db`: Base de datos (mysql, postgres)
- `cache`: Sistema de caché (redis, memcached)
- `app`: Tu aplicación personalizada

**3. `volumes:`**

Define volúmenes nombrados para persistir datos.

```yaml
volumes:
  mi_volumen:    # Nombre del volumen
  otro_volumen:
    driver: local  # Opcional: tipo de driver
```

Si no defines nada aquí pero usas volúmenes en los servicios, Docker los crea automáticamente.

**4. `networks:`**

Define redes personalizadas para comunicación entre servicios.

```yaml
networks:
  mi_red:        # Nombre de la red
  otra_red:
    driver: bridge  # Opcional: tipo de red
```

Si no defines redes, Docker Compose crea automáticamente una red `default` donde todos los servicios pueden comunicarse.

**Equivalencia con comandos Docker:**

Este docker-compose.yml:
```yaml
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

Es equivalente a:
```bash
$ docker network create mi-app_default
$ docker run -d --name web --network mi-app_default -p 8080:80 nginx
```

!!! note "Ventaja de Compose"
    En lugar de recordar y escribir comandos largos, defines todo en un archivo y ejecutas `docker compose up`.

#### 3.2. Ejemplo completo: WordPress (explicado línea por línea)

Este ejemplo muestra una aplicación completa con base de datos y servidor web.

```yaml
version: '3.8'

services:
  db:
    image: mysql:8.0
    volumes:
      - db_data:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    networks:
      - wordpress_net
    restart: always

  wordpress:
    image: wordpress:latest
    depends_on:
      - db
    ports:
      - "8080:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_NAME: wordpress
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
    volumes:
      - wp_data:/var/www/html
    networks:
      - wordpress_net
    restart: always

volumes:
  db_data:
  wp_data:

networks:
  wordpress_net:
```

**Análisis detallado del servicio `db` (MySQL):**

```yaml
db:                              # Nombre del servicio
  image: mysql:8.0               # Usar MySQL versión 8.0
```

- El nombre `db` es como llamarás a este servicio
- Otros servicios pueden conectarse usando este nombre como hostname

```yaml
  volumes:
    - db_data:/var/lib/mysql     # Persistir base de datos
```

- `db_data`: Nombre del volumen (definido abajo)
- `/var/lib/mysql`: Directorio dentro del contenedor donde MySQL guarda datos
- **Resultado**: Los datos sobreviven aunque elimines el contenedor

```yaml
  environment:
    MYSQL_ROOT_PASSWORD: rootpass
    MYSQL_DATABASE: wordpress
    MYSQL_USER: wpuser
    MYSQL_PASSWORD: wppass
```

**Explicación de cada variable:**

- `MYSQL_ROOT_PASSWORD`: Contraseña del superusuario root
- `MYSQL_DATABASE`: Crea automáticamente la BD "wordpress" al iniciar
- `MYSQL_USER`: Crea el usuario "wpuser"
- `MYSQL_PASSWORD`: Contraseña para wpuser

!!! warning "Seguridad"
    En producción, NUNCA pongas contraseñas en el archivo YAML. Usa archivos `.env` o Docker secrets.

```yaml
  networks:
    - wordpress_net                # Conectar a red personalizada
```

- Une este servicio a la red `wordpress_net`
- Permite comunicación privada con WordPress

```yaml
  restart: always                  # Reiniciar siempre si se detiene
```

**Opciones de restart:**

- `no`: No reiniciar (default)
- `always`: Siempre reiniciar, incluso si se detuvo manualmente
- `on-failure`: Solo si falla (código de salida != 0)
- `unless-stopped`: Siempre, excepto si se detuvo manualmente

**Análisis del servicio `wordpress`:**

```yaml
wordpress:
  image: wordpress:latest
```

- Usa la última versión de WordPress
- Incluye Apache y PHP configurados

```yaml
  depends_on:
    - db
```

**¿Qué hace depends_on?**

- Asegura que `db` se inicie ANTES que `wordpress`
- No espera a que MySQL esté "listo", solo a que el contenedor esté "iniciado"
- Orden de inicio: 1º db, 2º wordpress

!!! note "Importante"
    `depends_on` no garantiza que MySQL esté aceptando conexiones, solo que el contenedor se inició. WordPress reintentará conectar automáticamente.

```yaml
  ports:
    - "8080:80"
```

- Puerto 8080 de tu ordenador → Puerto 80 del contenedor
- Accedes desde navegador: `http://localhost:8080`
- Solo WordPress necesita puerto expuesto (MySQL es privado)

```yaml
  environment:
    WORDPRESS_DB_HOST: db          # ¡Nombre del servicio MySQL!
    WORDPRESS_DB_NAME: wordpress
    WORDPRESS_DB_USER: wpuser
    WORDPRESS_DB_PASSWORD: wppass
```

**¡Magia de Docker Compose!**

- `WORDPRESS_DB_HOST: db` usa el **nombre del servicio**
- Docker Compose tiene un DNS interno que resuelve `db` → IP del contenedor MySQL
- WordPress conecta automáticamente a la base de datos

**Flujo de conexión:**

```
WordPress busca: db
       ↓
DNS de Compose resuelve: db = 172.18.0.2
       ↓
WordPress conecta: mysql://172.18.0.2:3306
       ↓
MySQL responde
```

```yaml
  volumes:
    - wp_data:/var/www/html
```

- Persiste archivos de WordPress (temas, plugins, uploads)
- Si actualizas WordPress, los archivos se mantienen

**Definición de volúmenes:**

```yaml
volumes:
  db_data:      # Volumen para MySQL
  wp_data:      # Volumen para WordPress
```

- Docker gestiona estos volúmenes automáticamente
- Los crea si no existen
- Persisten aunque elimines los contenedores

**Definición de red:**

```yaml
networks:
  wordpress_net:   # Red privada para la aplicación
```

- Crea una red bridge aislada
- Solo los contenedores de esta aplicación pueden comunicarse
- Otras aplicaciones en el mismo host no pueden acceder

**Resumen visual:**

```
┌─────────────────────────────────────────┐
│    Red: wordpress_net (172.18.0.0/16)   │
│                                         │
│  ┌──────────────┐    ┌──────────────┐   │
│  │  wordpress   │    │     db       │   │
│  │  (Apache)    │───▶│   (MySQL)    │   │
│  │  172.18.0.3  │    │  172.18.0.2  │   │
│  │  Puerto 8080 │    │  Puerto 3306 │   │
│  └──────┬───────┘    └──────┬───────┘   │
│         │                   │           │
│    ┌────▼────┐         ┌────▼────┐      │
│    │ wp_data │         │ db_data │      │
│    └─────────┘         └─────────┘      │
└─────────────────────────────────────────┘
                    ▲
                    │ Puerto 8080
              [Tu navegador]
```

### 4. El comando docker compose

#### 4.1. Comandos principales (explicados)

**Iniciar toda la aplicación:**

```bash
$ docker compose up -d
[+] Running 4/4
 ✔ Network wordpress_default       Created
 ✔ Volume "wordpress_db_data"      Created
 ✔ Container wordpress-db-1        Started
 ✔ Container wordpress-wordpress-1 Started
```

**Análisis de la salida:**

- `Network wordpress_default Created`: Creó la red automáticamente
- `Volume "wordpress_db_data" Created`: Creó los volúmenes
- `Container wordpress-db-1 Started`: Inició MySQL primero (por depends_on)
- `Container wordpress-wordpress-1 Started`: Luego inició WordPress

**Opciones de `docker compose up`:**

```bash
# Iniciar en primer plano (ver logs directamente)
$ docker compose up

# Iniciar en segundo plano (detached)
$ docker compose up -d

# Forzar recreación de contenedores
$ docker compose up -d --force-recreate

# Construir imágenes antes de iniciar
$ docker compose up -d --build

# Iniciar solo un servicio específico
$ docker compose up -d db
```

!!! tip "¿Cuándo usar --force-recreate?"
    Cuando cambias el docker-compose.yml y los cambios no se aplican. Fuerza a recrear todos los contenedores aunque no hayan cambiado.

**Ver logs de los servicios:**

```bash
$ docker compose logs
wordpress-db-1         | 2024-01-23 17:00:00 [Note] mysqld: ready for connections.
wordpress-wordpress-1  | WordPress not found... copying files from /usr/src/wordpress
```

**Opciones de logs:**

```bash
# Ver solo los últimos 50 líneas
$ docker compose logs --tail 50

# Seguir logs en tiempo real (como tail -f)
$ docker compose logs -f

# Logs de un servicio específico
$ docker compose logs wordpress

# Logs con timestamps
$ docker compose logs -t

# Combinar opciones
$ docker compose logs -f --tail 100 db
```

**Interpretación de los logs:**

```bash
wordpress-db-1         | [Nota] MySQL está listo
     ↑                   ↑
Nombre del servicio    Mensaje del contenedor
```

**Ver estado de los servicios:**

```bash
$ docker compose ps
NAME                    IMAGE              COMMAND                  SERVICE      CREATED         STATUS          PORTS
wordpress-db-1          mysql:8.0          "docker-entrypoint.s…"   db           2 minutes ago   Up 2 minutes    3306/tcp
wordpress-wordpress-1   wordpress:latest   "docker-entrypoint.s…"   wordpress    2 minutes ago   Up 2 minutes    0.0.0.0:8080->80/tcp
```

**Explicación de las columnas:**

- `NAME`: Nombre del contenedor (Compose lo genera automáticamente)
- `IMAGE`: Imagen utilizada
- `SERVICE`: Nombre del servicio en docker-compose.yml
- `STATUS`: Estado actual (Up, Exited, Restarting)
- `PORTS`: Puertos mapeados

**Formato del nombre de contenedor:**

```
wordpress-db-1
    ↑    ↑ ↑
    │    │ └─ Número de réplica (si escalas)
    │    └─── Nombre del servicio
    └──────── Nombre del proyecto (carpeta actual)
```

**Gestión de servicios:**

**Detener sin eliminar:**

```bash
$ docker compose stop
[+] Stopping 2/2
 ✔ Container wordpress-wordpress-1  Stopped
 ✔ Container wordpress-db-1         Stopped
```

- Detiene los contenedores pero no los elimina
- Los datos persisten
- Puedes reiniciarlos con `docker compose start`

**Iniciar servicios detenidos:**

```bash
$ docker compose start
[+] Running 2/2
 ✔ Container wordpress-db-1         Started
 ✔ Container wordpress-wordpress-1  Started
```

- Inicia contenedores que fueron detenidos con `stop`
- Mucho más rápido que `up` (no recrea contenedores)

**Reiniciar servicios:**

```bash
$ docker compose restart
[+] Restarting 2/2
 ✔ Container wordpress-db-1         Restarted
 ✔ Container wordpress-wordpress-1  Restarted
```

- Equivale a `stop` seguido de `start`
- Útil para aplicar cambios de configuración

**Pausar/Reanudar (congela el proceso):**

```bash
# Pausar (congela procesos)
$ docker compose pause

# Reanudar
$ docker compose unpause
```

- `pause`: Congela los procesos (siguen en memoria pero no ejecutan)
- `unpause`: Descongela y continúan donde se quedaron
- Rara vez usado, más útil para debugging

**Diferencia entre stop y pause:**

```
stop:   Proceso termina → libera recursos → puede tardar
pause:  Proceso congela → mantiene memoria → instantáneo
```

**Eliminar todo:**

```bash
$ docker compose down
[+] Running 3/3
 ✔ Container wordpress-wordpress-1  Removed
 ✔ Container wordpress-db-1         Removed
 ✔ Network wordpress_default        Removed
```

**¿Qué hace `docker compose down`?**

1. Detiene todos los contenedores
2. Elimina los contenedores
3. Elimina la red creada
4. **NO** elimina volúmenes (datos persisten)

**Opciones de down:**

```bash
# Eliminar también los volúmenes (¡PIERDES LOS DATOS!)
$ docker compose down -v
[+] Running 5/5
 ✔ Container wordpress-wordpress-1  Removed
 ✔ Container wordpress-db-1         Removed
 ✔ Volume wordpress_db_data         Removed  ⚠️
 ✔ Volume wordpress_wp_data         Removed  ⚠️
 ✔ Network wordpress_default        Removed

# Eliminar también las imágenes descargadas
$ docker compose down --rmi all
```

!!! danger "¡Cuidado con -v!"
    `docker compose down -v` elimina TODOS los datos. Úsalo solo en desarrollo o si estás seguro de tener backup.

**Ejecutar comandos en servicios:**

```bash
$ docker compose exec wordpress bash
root@abc123:/var/www/html#
```

**¿Qué hace `exec`?**

- `exec`: Ejecuta un comando en un contenedor que **ya está corriendo**
- `wordpress`: Nombre del servicio (no del contenedor)
- `bash`: Comando a ejecutar (abre una shell)

**Diferencia con `docker exec`:**

```bash
# Docker Compose (usa nombre de servicio)
$ docker compose exec wordpress bash

# Docker nativo (usa nombre de contenedor)
$ docker exec -it wordpress-wordpress-1 bash
```

Compose es más sencillo porque usa el nombre del servicio, no necesitas saber el nombre completo del contenedor.

**Opciones útiles de exec:**

```bash
# Ejecutar como usuario específico
$ docker compose exec -u www-data wordpress bash

# Ejecutar comando sin shell interactiva
$ docker compose exec wordpress ls -la

# Ver variables de entorno
$ docker compose exec wordpress env

# Ejecutar comando en MySQL
$ docker compose exec db mysql -u root -p
```

**Ejemplo práctico: Backup de base de datos:**

```bash
# Hacer backup de MySQL
$ docker compose exec db mysqldump -u root -prootpass wordpress > backup.sql

# Restaurar backup
$ docker compose exec -T db mysql -u root -prootpass wordpress < backup.sql
```

- `-T`: Desactiva la asignación de pseudo-TTY (necesario para redirecciones)

**Ejecutar comandos one-off (contenedores temporales):**

```bash
$ docker compose run --rm wordpress wp --info
```

**¿Qué hace `run`?**

- Crea un **nuevo contenedor temporal**
- Ejecuta el comando
- Con `--rm` lo elimina al terminar
- Diferente de `exec` (que usa un contenedor existente)

**Cuándo usar `run` vs `exec`:**

- `exec`: Para contenedores en ejecución (más común)
- `run`: Para tareas puntuales o testing

**Escalar servicios (múltiples réplicas):**

```bash
$ docker compose up -d --scale web=3
[+] Running 4/4
 ✔ Container proyecto-web-1  Started
 ✔ Container proyecto-web-2  Started
 ✔ Container proyecto-web-3  Started
 ✔ Container proyecto-db-1   Started
```

**¿Qué significa escalar?**

- Crea 3 réplicas del servicio `web`
- Útil para balanceo de carga
- Cada réplica es un contenedor independiente

**Requisitos para escalar:**

```yaml
services:
  web:
    image: nginx
    # ❌ NO funciona con puertos específicos
    # ports:
    #   - "8080:80"  # Solo un contenedor puede usar 8080
    
    # ✅ Funciona sin puertos o con puertos dinámicos
    expose:
      - "80"  # Puerto interno, sin mapeo host
```

!!! warning "Limitación"
    No puedes escalar servicios que mapean puertos específicos (como `8080:80`) porque solo un contenedor puede usar ese puerto del host.

**Ver réplicas escaladas:**

```bash
$ docker compose ps
NAME            SERVICE   STATUS    PORTS
proyecto-web-1  web       Up        80/tcp
proyecto-web-2  web       Up        80/tcp
proyecto-web-3  web       Up        80/tcp
proyecto-db-1   db        Up        3306/tcp
```

#### 4.2. Opciones útiles (casos de uso reales)

**Especificar archivo compose diferente:**

```bash
$ docker compose -f mi-compose.yml up -d
```

**¿Cuándo usar esto?**

- Tienes varios archivos compose (desarrollo, testing, producción)
- El archivo no se llama `docker-compose.yml`

**Estructura típica de proyecto:**

```
proyecto/
├── docker-compose.yml           # Desarrollo (default)
├── docker-compose.prod.yml      # Producción
├── docker-compose.test.yml      # Testing
└── docker-compose.override.yml  # Sobrescribe valores (automático)
```

**Usar múltiples archivos (combinar configuraciones):**

```bash
$ docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

**¿Cómo funciona?**

1. Lee `docker-compose.yml` (base)
2. Lee `docker-compose.prod.yml`
3. Combina ambos (el segundo sobrescribe valores duplicados)

**Ejemplo práctico:**

**docker-compose.yml** (base):
```yaml
services:
  web:
    image: nginx
    volumes:
      - ./app:/usr/share/nginx/html
```

**docker-compose.prod.yml** (producción):
```yaml
services:
  web:
    volumes:
      - /var/www/produccion:/usr/share/nginx/html  # Sobrescribe volumen
    restart: always                                  # Añade restart
```

**Resultado combinado:**
```yaml
services:
  web:
    image: nginx
    volumes:
      - /var/www/produccion:/usr/share/nginx/html  # Del prod
    restart: always                                  # Del prod
```

**Especificar nombre de proyecto:**

```bash
$ docker compose -p mi_proyecto up -d
```

**¿Para qué sirve el nombre de proyecto?**

- Docker usa el nombre de la carpeta actual por defecto
- Con `-p` puedes cambiarlo
- Afecta al nombre de contenedores, redes y volúmenes

**Ejemplo:**

```bash
# Sin -p (usa nombre de carpeta "wordpress")
$ docker compose up -d
# Crea: wordpress-db-1, wordpress-wordpress-1

# Con -p
$ docker compose -p sitio-cliente up -d
# Crea: sitio-cliente-db-1, sitio-cliente-wordpress-1
```

**Ventaja:** Puedes tener múltiples instancias de la misma aplicación:

```bash
$ cd wordpress/
$ docker compose -p cliente1 up -d
$ docker compose -p cliente2 up -d
$ docker compose -p cliente3 up -d
```

Ahora tienes 3 WordPress independientes corriendo.

**Construir imágenes antes de iniciar:**

```bash
$ docker compose up -d --build
[+] Building 5.2s (12/12) FINISHED
[+] Running 2/2
 ✔ Container proyecto-web-1  Started
```

**¿Cuándo usar `--build`?**

- Cuando tu docker-compose.yml usa `build:` en lugar de `image:`
- Has modificado tu Dockerfile o código
- Quieres asegurar que usa la última versión del código

**Ejemplo con build:**

```yaml
services:
  app:
    build: ./app        # Construir desde Dockerfile en ./app
    ports:
      - "3000:3000"
```

```bash
# Primera vez: construye la imagen
$ docker compose up -d --build

# Modificas código...

# Reconstruir con cambios
$ docker compose up -d --build
```

**Forzar recreación de contenedores:**

```bash
$ docker compose up -d --force-recreate
```

**¿Cuándo usar `--force-recreate`?**

- Cambias docker-compose.yml pero los contenedores no se actualizan
- Quieres empezar "limpio" sin perder volúmenes
- Debugging de problemas extraños

**Diferencia con `down` + `up`:**

```bash
# Opción 1: down + up (elimina todo y vuelve a crear)
$ docker compose down
$ docker compose up -d

# Opción 2: force-recreate (mantiene volúmenes y redes)
$ docker compose up -d --force-recreate
```

**Ver configuración resultante (debugging):**

```bash
$ docker compose config
```

**¿Para qué sirve?**

- Muestra el YAML resultante después de combinar archivos
- Útil para verificar que las variables de entorno se expandieron correctamente
- Debugging cuando algo no funciona como esperas

**Ejemplo:**

```bash
$ docker compose -f docker-compose.yml -f docker-compose.prod.yml config
# Muestra el YAML final combinado
```

**Validar archivo sin ejecutar:**

```bash
$ docker compose config --quiet
```

- Si el archivo tiene errores, muestra el error
- Si está correcto, no muestra nada
- Útil en CI/CD para validar antes de desplegar


### 5. Definición de servicios (opciones explicadas)

Esta sección explica todas las opciones disponibles para configurar servicios.

#### 5.1. image vs build

**Opción 1: Usar imagen existente**

```yaml
services:
  web:
    image: nginx:latest
```

- Usa imagen pública de Docker Hub
- No necesita Dockerfile
- Rápido de iniciar

**Opción 2: Construir desde Dockerfile**

```yaml
services:
  app:
    build:
      context: ./app           # Directorio con el Dockerfile
      dockerfile: Dockerfile   # Nombre del Dockerfile (opcional)
```

**Explicación:**

- `context`: Directorio donde está el Dockerfile y código fuente
- `dockerfile`: Si tu Dockerfile se llama diferente (ej: Dockerfile.prod)

**Ejemplo de estructura:**

```
proyecto/
├── docker-compose.yml
└── app/
    ├── Dockerfile
    ├── package.json
    └── src/
```

**Opciones avanzadas de build:**

```yaml
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
      args:                    # Argumentos de build
        NODE_VERSION: 18
        BUILD_ENV: production
      target: production       # Stage de multi-stage build
```

#### 5.2. container_name

```yaml
services:
  web:
    container_name: mi_nginx_custom
```

**¿Cuándo usar container_name?**

- Quieres un nombre específico en lugar del generado automáticamente
- Facilita identificar el contenedor

**Sin container_name:**
```
proyecto-web-1  # Compose genera: carpeta-servicio-replica
```

**Con container_name:**
```
mi_nginx_custom  # Tu nombre personalizado
```

!!! warning "Limitación"
    Si usas `container_name`, NO puedes escalar ese servicio (solo puede haber un contenedor con ese nombre).

#### 5.3. command (sobrescribir comando)

```yaml
services:
  web:
    image: nginx
    command: nginx -g 'daemon off;'
```

**¿Para qué sirve?**

- Sobrescribe el CMD definido en la imagen
- Útil para cambiar comportamiento sin modificar la imagen

**Ejemplos prácticos:**

```yaml
# Desarrollo: Iniciar con live reload
services:
  app:
    image: node:18
    command: npm run dev

# Producción: Iniciar en modo producción
services:
  app:
    image: node:18
    command: npm start
```

**Formato array (recomendado):**

```yaml
command: ["npm", "run", "dev"]
# Mejor que:
command: npm run dev
```

#### 5.4. ports (mapeo de puertos)

```yaml
services:
  web:
    ports:
      - "8080:80"      # host:contenedor
      - "443:443"
      - "127.0.0.1:3000:3000"  # solo localhost
```

**Formatos disponibles:**

1. **Corto:** `"8080:80"`
   - Puerto 8080 del host → puerto 80 del contenedor

2. **Con IP:** `"127.0.0.1:8080:80"`
   - Solo accesible desde localhost (más seguro)

3. **Rango:** `"3000-3005:3000-3005"`
   - Mapea múltiples puertos

**expose vs ports:**

```yaml
services:
  backend:
    expose:
      - "3000"    # Accesible solo desde otros servicios
    ports:
      - "8080:80" # Accesible desde el host
```

- `expose`: Puerto interno (solo contenedores de la red)
- `ports`: Puerto expuesto al host (accesible desde tu navegador)

#### 5.5. environment (variables de entorno)

**Formato inline:**

```yaml
services:
  db:
    environment:
      MYSQL_ROOT_PASSWORD: secreto
      MYSQL_DATABASE: midb
      DEBUG: "true"    # Entrecomillar true/false
```

**Formato array:**

```yaml
environment:
  - MYSQL_ROOT_PASSWORD=secreto
  - MYSQL_DATABASE=midb
```

**Usar archivo .env:**

```yaml
services:
  app:
    env_file:
      - .env           # Archivo con variables
      - .env.local     # Puede ser múltiples
```

**Archivo .env:**
```env
DB_HOST=db
DB_USER=admin
DB_PASS=secreto123
```

**Interpolación de variables:**

```yaml
services:
  app:
    environment:
      DB_HOST: ${DB_HOST:-db}  # Usa variable o 'db' por defecto
      API_KEY: ${API_KEY}      # Obligatoria (falla si no existe)
```

!!! tip "Buena práctica"
    - Usa `.env` para configuración local
    - Añade `.env` a `.gitignore`
    - Crea `.env.example` con valores de ejemplo para el equipo

#### 5.6. volumes (persistencia)

**Volumen nombrado:**

```yaml
services:
  db:
    volumes:
      - db_data:/var/lib/mysql

volumes:
  db_data:  # Definido abajo
```

**Bind mount (ruta del host):**

```yaml
services:
  web:
    volumes:
      - ./html:/usr/share/nginx/html      # Relativo
      - /var/log/nginx:/var/log/nginx     # Absoluto
```

**Volumen de solo lectura:**

```yaml
volumes:
  - ./config:/etc/app/config:ro  # :ro = read-only
```

**Sintaxis larga (más opciones):**

```yaml
volumes:
  - type: bind
    source: ./app
    target: /usr/src/app
    read_only: false
  
  - type: volume
    source: db_data
    target: /var/lib/mysql
```

#### 5.7. networks (redes)

```yaml
services:
  frontend:
    networks:
      - frontend_net    # Solo en esta red
  
  backend:
    networks:
      - frontend_net    # En ambas redes
      - backend_net
  
  db:
    networks:
      - backend_net     # Solo backend (más seguro)

networks:
  frontend_net:
  backend_net:
```

**Resultado:**
```
frontend ←→ backend ←→ db
(frontend_net) (ambas) (backend_net)
```

- `frontend` NO puede hablar directamente con `db` (mayor seguridad)

#### 5.8. depends_on (orden de inicio)

```yaml
services:
  web:
    depends_on:
      - db
      - cache
```

**¿Qué hace depends_on?**

1. Inicia `db` y `cache` primero
2. Luego inicia `web`
3. **NO** espera a que estén "listos", solo a que inicien

**Limitación:**

```yaml
depends_on:
  - db    # Espera a que el contenedor inicie
          # NO espera a que MySQL acepte conexiones
```

**Solución:** Tu aplicación debe reintentar conexiones.

**Opción avanzada (Compose v2.1+):**

```yaml
services:
  web:
    depends_on:
      db:
        condition: service_healthy  # Espera al healthcheck

  db:
    healthcheck:
      test: ["CMD", "mysqladmin", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5
```

#### 5.9. restart (política de reinicio)

```yaml
services:
  web:
    restart: always
```

**Opciones:**

- `no`: No reiniciar (por defecto)
- `always`: Siempre reiniciar, incluso después de `docker compose stop`
- `on-failure`: Solo si falla (exit code != 0)
- `unless-stopped`: Siempre excepto si se detuvo manualmente

**¿Cuándo usar cada una?**

- `always`: Servicios críticos de producción
- `on-failure`: Desarrollo (evita loops de reinicio)
- `unless-stopped`: Balance entre ambos
- `no`: Tareas que ejecutan y terminan

#### 5.10. deploy (límites de recursos)

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.5'      # Máximo 50% de un CPU
          memory: 512M     # Máximo 512 MB RAM
        reservations:
          cpus: '0.25'     # Mínimo reservado
          memory: 256M
```

!!! note "Solo en Swarm mode"
    La sección `deploy` es principalmente para Docker Swarm. En Compose regular, muchas opciones no funcionan. Para limitar recursos localmente, usa `docker run` con `--cpus` y `--memory`.

### 6. Almacenamiento con Docker Compose

#### 6.1. Volúmenes nombrados

```yaml
services:
  db:
    image: postgres
    volumes:
      - pg_data:/var/lib/postgresql/data

volumes:
  pg_data:  # Docker gestiona este volumen
```

#### 6.2. Bind mounts

```yaml
services:
  web:
    image: nginx
    volumes:
      - ./html:/usr/share/nginx/html  # Ruta relativa
      - /var/log/nginx:/var/log/nginx  # Ruta absoluta
```

#### 6.3. Volúmenes con opciones

```yaml
services:
  web:
    volumes:
      - type: bind
        source: ./config
        target: /etc/nginx/conf.d
        read_only: true
      
      - type: volume
        source: web_data
        target: /data
        volume:
          nocopy: true

volumes:
  web_data:
```

### 7. Redes con Docker Compose

#### 7.1. Red predeterminada

Docker Compose crea automáticamente una red para la aplicación.

```yaml
services:
  web:
    image: nginx
  
  db:
    image: mysql
# Ambos están en la misma red y pueden comunicarse por nombre
```

#### 7.2. Redes personalizadas

```yaml
services:
  frontend:
    image: nginx
    networks:
      - frontend_net
  
  backend:
    image: node
    networks:
      - frontend_net
      - backend_net
  
  db:
    image: mysql
    networks:
      - backend_net

networks:
  frontend_net:
  backend_net:
```

### 8. Ejemplos prácticos

#### 8.1. Aplicación web con base de datos

```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
    depends_on:
      - app
    networks:
      - frontend

  app:
    build: ./app
    environment:
      DB_HOST: db
      DB_NAME: myapp
      DB_USER: user
      DB_PASS: pass
    depends_on:
      - db
    networks:
      - frontend
      - backend

  db:
    image: mariadb:10.6
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: myapp
      MYSQL_USER: user
      MYSQL_PASSWORD: pass
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - backend

volumes:
  db_data:

networks:
  frontend:
  backend:
```

#### 8.2. Stack de monitorización

```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      GF_SECURITY_ADMIN_PASSWORD: admin
    depends_on:
      - prometheus

volumes:
  prometheus_data:
  grafana_data:
```

### 9. Buenas prácticas (explicadas)

Es importante seguir buenas prácticas para mantener tus archivos Docker Compose limpios, seguros y eficientes.

!!!success "Checklist de buenas prácticas"

- [ ] Variables sensibles en .env
- [ ] .env en .gitignore
- [ ] Versiones específicas de imágenes
- [ ] Nombres de servicios descriptivos
- [ ] Healthchecks en servicios críticos
- [ ] Límites de recursos definidos
- [ ] Configuración de logging
- [ ] Múltiples archivos para entornos
- [ ] Comentarios explicativos
- [ ] README con instrucciones

A continuación, se explican algunas de estas prácticas con ejemplos.

#### 9.1. Gestión de secretos

**❌ MAL:**
```yaml
services:
  db:
    environment:
      MYSQL_ROOT_PASSWORD: mi_password_secreto  # ¡Nunca hagas esto!
```

**✅ BIEN:**

Opción 1: Archivo .env (no versionado)
```yaml
services:
  db:
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
```

**.env:**
```env
DB_PASSWORD=mi_password_secreto
```

**.gitignore:**
```
.env
```

Opción 2: Docker secrets (producción)
```yaml
services:
  db:
    secrets:
      - db_password
    environment:
      MYSQL_ROOT_PASSWORD_FILE: /run/secrets/db_password

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

#### 9.2. Versionado

**❌ MAL:**
```yaml
services:
  web:
    image: nginx:latest  # 'latest' puede cambiar
```

**✅ BIEN:**
```yaml
services:
  web:
    image: nginx:1.25.3  # Versión específica
```

**¿Por qué?**

- `latest` puede cambiar en cualquier momento
- Tus compañeros pueden tener versiones diferentes
- Dificulta reproducir bugs
- Puede romper tu aplicación sin aviso


#### 9.3. Nombres descriptivos

**❌ MAL:**
```yaml
services:
  s1:
    image: nginx
  s2:
    image: mysql
```

**✅ BIEN:**
```yaml
services:
  frontend_web:
    image: nginx
  backend_database:
    image: mysql
```

#### 9.4. Orden y organización

```yaml
services:
  # 1. Servicios frontend (los que exponemos)
  web:
    image: nginx
    ports:
      - "80:80"
    depends_on:
      - app
  
  # 2. Servicios de aplicación
  app:
    build: ./app
    depends_on:
      - db
      - cache
  
  # 3. Servicios de datos (los más internos)
  db:
    image: postgres
  
  cache:
    image: redis
```

#### 9.5. Healthchecks

Añade healthchecks para saber cuándo un servicio está realmente listo:

```yaml
services:
  db:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s      # Cada cuánto verificar
      timeout: 5s        # Tiempo máximo de respuesta
      retries: 5         # Intentos antes de marcar como unhealthy
      start_period: 30s  # Tiempo de gracia al iniciar
  
  app:
    depends_on:
      db:
        condition: service_healthy  # Espera a que esté healthy
```

#### 9.6. Límites de recursos

Previene que un servicio consuma todos los recursos:

```yaml
services:
  app:
    image: node:18
    deploy:
      resources:
        limits:
          cpus: '1.0'      # Máximo 1 CPU
          memory: 1G       # Máximo 1GB RAM
        reservations:
          cpus: '0.5'      # Mínimo garantizado
          memory: 512M
```

#### 9.7. Logging

Configura logs para no llenar el disco:

```yaml
services:
  app:
    logging:
      driver: "json-file"
      options:
        max-size: "10m"    # Máximo 10MB por archivo
        max-file: "3"      # Máximo 3 archivos (30MB total)
```

#### 9.8. Múltiples entornos

**Estructura recomendada:**

```
proyecto/
├── docker-compose.yml          # Base (común a todos)
├── docker-compose.dev.yml      # Desarrollo
├── docker-compose.prod.yml     # Producción
├── .env.example                # Ejemplo de variables
└── .gitignore                  # Ignora .env
```

**docker-compose.yml** (base):
```yaml
services:
  app:
    build: ./app
    environment:
      NODE_ENV: ${NODE_ENV}
```

**docker-compose.dev.yml**:
```yaml
services:
  app:
    volumes:
      - ./app:/usr/src/app  # Live reload
    command: npm run dev
    ports:
      - "3000:3000"
```

**docker-compose.prod.yml**:
```yaml
services:
  app:
    command: npm start
    restart: always
    ports:
      - "80:3000"
```

**Uso:**

```bash
# Desarrollo
$ docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d

# Producción
$ docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

#### 9.9. Documentación

Añade comentarios explicativos:

```yaml
services:
  web:
    image: nginx:1.25.3
    ports:
      - "80:80"           # HTTP
      - "443:443"         # HTTPS
    volumes:
      # Contenido estático del sitio
      - ./html:/usr/share/nginx/html:ro
      # Configuración personalizada de nginx
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    networks:
      - frontend
    # Reiniciar siempre en caso de fallo
    restart: unless-stopped
```

#### 9.10. Validación pre-commit

Crea un script para validar antes de commit:

**validate.sh:**
```bash
#!/bin/bash
# Validar sintaxis de docker-compose.yml
docker compose config --quiet
if [ $? -eq 0 ]; then
  echo "✅ docker-compose.yml es válido"
else
  echo "❌ docker-compose.yml tiene errores"
  exit 1
fi
```

#### 9.11. README del proyecto

Incluye instrucciones claras:

**README.md:**
```markdown
# Mi Proyecto

## Requisitos
- Docker 24.0+
- Docker Compose 2.20+

## Configuración inicial

1. Copiar variables de entorno:
   ```bash
   cp .env.example .env
   ```

2. Editar .env con tus valores

3. Iniciar servicios:
   ```bash
   docker compose up -d
   ```

4. Acceder a http://localhost:8080


#### 9.12. Archivo .env

Usar archivo `.env` para variables de entorno:

**.env:**
```env
DB_PASSWORD=secreto
DB_USER=usuario
APP_PORT=8080
```

**docker-compose.yml:**
```yaml
services:
  db:
    environment:
      MYSQL_PASSWORD: ${DB_PASSWORD}
      MYSQL_USER: ${DB_USER}
  
  web:
    ports:
      - "${APP_PORT}:80"
```

### Resumen

En esta sección hemos aprendido:

- ✅ Qué es Docker Compose y sus ventajas
- ✅ Estructura del archivo docker-compose.yml
- ✅ Comandos principales de docker compose
- ✅ Definir servicios, volúmenes y redes
- ✅ Gestionar aplicaciones multi-contenedor
- ✅ Buenas prácticas con Docker Compose

### Recursos adicionales

- [Documentación Docker Compose](https://docs.docker.com/compose/)
- [Referencia docker-compose.yml](https://docs.docker.com/compose/compose-file/)
- [Curso Docker IES - Módulo 4](../u01/teoria/OtrosRecursos/curso_docker_ies/modulo4/)

!!! tip "Siguiente paso"
    En la siguiente sección aprenderemos a crear nuestras propias imágenes Docker mediante Dockerfiles.
