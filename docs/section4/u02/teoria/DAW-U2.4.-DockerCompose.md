---
title: "UD 2 - 2.4 Docker Compose"
description: Gestión de aplicaciones multi-contenedor con Docker Compose
summary: Docker Compose, docker-compose.yml, orquestación
authors:
    - Eduardo Fdez
date: 2025-01-23
icon: 
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

El archivo `docker-compose.yml` define la estructura de nuestra aplicación.

#### 3.1. Estructura básica

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

#### 3.2. Ejemplo completo: WordPress

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

### 4. El comando docker compose

#### 4.1. Comandos principales

**Iniciar servicios:**

```bash
# Crear e iniciar contenedores en segundo plano
$ docker compose up -d

# Ver logs
$ docker compose logs

# Seguir logs en tiempo real
$ docker compose logs -f
```

**Gestión de servicios:**

```bash
# Ver estado de servicios
$ docker compose ps

# Detener servicios
$ docker compose stop

# Iniciar servicios detenidos
$ docker compose start

# Reiniciar servicios
$ docker compose restart

# Pausar servicios
$ docker compose pause

# Reanudar servicios pausados
$ docker compose unpause
```

**Eliminar servicios:**

```bash
# Detener y eliminar contenedores
$ docker compose down

# Eliminar también volúmenes
$ docker compose down -v

# Eliminar también imágenes
$ docker compose down --rmi all
```

**Ejecutar comandos en servicios:**

```bash
# Ejecutar comando en servicio
$ docker compose exec wordpress bash

# Ejecutar como usuario específico
$ docker compose exec -u www-data wordpress bash
```

**Escalar servicios:**

```bash
# Crear 3 instancias del servicio web
$ docker compose up -d --scale web=3
```

#### 4.2. Opciones útiles

```bash
# Especificar archivo compose diferente
$ docker compose -f mi-compose.yml up -d

# Usar múltiples archivos
$ docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Especificar nombre de proyecto
$ docker compose -p mi_proyecto up -d

# Construir imágenes antes de iniciar
$ docker compose up -d --build

# Forzar recreación de contenedores
$ docker compose up -d --force-recreate
```

### 5. Definición de servicios

#### 5.1. Opciones comunes

```yaml
services:
  mi_servicio:
    # Imagen a utilizar
    image: nginx:latest
    
    # O construir desde Dockerfile
    build:
      context: ./app
      dockerfile: Dockerfile
    
    # Nombre del contenedor
    container_name: mi_nginx
    
    # Comando a ejecutar
    command: nginx -g 'daemon off;'
    
    # Puertos a exponer
    ports:
      - "8080:80"
      - "443:443"
    
    # Variables de entorno
    environment:
      ENV_VAR: valor
      OTRA_VAR: otro_valor
    
    # O desde archivo
    env_file:
      - .env
    
    # Volúmenes
    volumes:
      - datos:/data
      - ./config:/etc/nginx/conf.d
    
    # Redes
    networks:
      - frontend
      - backend
    
    # Dependencias
    depends_on:
      - db
      - cache
    
    # Política de reinicio
    restart: always
    # Opciones: no, always, on-failure, unless-stopped
    
    # Límites de recursos
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
```

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

### 9. Buenas prácticas

1. **Usar variables de entorno** para configuración sensible
2. **Versionar el docker-compose.yml** en Git
3. **No versionar .env** con secretos
4. **Nombrar servicios descriptivamente**
5. **Usar depends_on** para definir dependencias
6. **Especificar versiones** de imágenes (no `:latest`)
7. **Definir health checks** para servicios críticos
8. **Documentar** el archivo compose con comentarios

### 10. Archivo .env

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
