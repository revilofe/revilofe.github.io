---
title: "UD 3 - 3.8 Despliegue de Aplicaciones Web"
description: Despliegue de aplicaciones web, escalabilidad vertical y horizontal, contenedores Docker, Kubernetes, cloud computing, CI/CD
summary: Conceptos de despliegue web, escalabilidad y balanceo de carga, contenedores Docker y Kubernetes, despliegue en cloud AWS/Azure/GCP, introducción a CI/CD
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: 
permalink: /daw/unidad3/3.8
categories:
    - DAW
tags:
    - Despliegue
    - Escalabilidad
    - Docker
    - Kubernetes
    - Cloud
    - CI/CD
    - DevOps
---

## 3.8. Despliegue de Aplicaciones Web

Hemos recorrido un largo camino juntos en esta unidad. Aprendimos cómo funciona el desarrollo web, las arquitecturas que lo sustentan, los protocolos de comunicación, cómo se genera contenido dinámico, los lenguajes y frameworks disponibles, y cómo configurar servidores web y de aplicaciones. Pero hay una pregunta crucial que aún debemos responder: **¿cómo llevamos todo este conocimiento a producción? ¿Cómo hacemos que nuestra aplicación esté disponible para miles o millones de usuarios en Internet?**

La respuesta está en el **despliegue de aplicaciones web**, el proceso mediante el cual una aplicación pasa del entorno de desarrollo al entorno de producción, lista para ser usada por usuarios reales. Este no es un simple "copiar archivos al servidor"; es un proceso complejo que involucra infraestructura, escalabilidad, disponibilidad, seguridad y automatización.

En esta unidad final, exploraremos las estrategias modernas de despliegue, desde los conceptos fundamentales hasta las tecnologías más avanzadas como Docker, Kubernetes y cloud computing. Este conocimiento es **esencial** para convertirse en un profesional completo del desarrollo y despliegue de aplicaciones web.

### 1. El concepto de despliegue: más que copiar archivos

Cuando empezamos a programar, "desplegar" una aplicación parecía simple: copias tus archivos a un servidor y listo. Pero en el mundo real profesional, el despliegue es un proceso mucho más sofisticado.

#### 1.1. ¿Qué significa realmente desplegar?

**Desplegar** (deploy) una aplicación web significa hacer que esté **disponible, funcional y accesible** para los usuarios finales en un entorno de producción. Esto implica mucho más que solo transferir archivos.

**Componentes del despliegue:**

**1. Software necesario**

Una aplicación web no funciona sola. Necesita un ecosistema completo de software:

- **Sistema operativo**: Linux (Ubuntu, CentOS), Windows Server
- **Servidor web**: Apache, Nginx, IIS
- **Runtime del lenguaje**: PHP, Python, JVM (Java), Node.js, .NET
- **Servidor de aplicaciones** (si aplica): Tomcat, Gunicorn, Passenger
- **Gestor de bases de datos**: MySQL, PostgreSQL, MongoDB
- **Dependencias**: Librerías, frameworks, paquetes (npm, pip, composer, maven)

Cada pieza debe estar instalada, configurada y funcionando correctamente.

**2. Hardware adecuado**

El servidor físico (o virtual) debe tener recursos suficientes:

- **CPU**: Procesador capaz de manejar la carga de trabajo
- **RAM**: Memoria suficiente para la aplicación y sus procesos
- **Almacenamiento**: Discos con capacidad y velocidad adecuadas
- **Red**: Ancho de banda para el tráfico esperado

La pregunta clave es: **¿cuántos recursos necesitas?** Esto depende de:
- Número de usuarios concurrentes
- Complejidad de las operaciones
- Tamaño de la base de datos
- Cantidad de peticiones por segundo

**3. Dependencias del proyecto**

Tu aplicación probablemente no funciona sola. Depende de:

- **Frameworks**: Laravel, Django, Spring Boot, Express
- **Librerías**: bibliotecas de terceros que usas
- **Assets**: Imágenes, fuentes, archivos estáticos
- **Configuraciones**: Archivos de configuración específicos del entorno

Todas estas dependencias deben estar presentes y en las versiones correctas.

**4. Configuración del entorno**

No basta con tener el software instalado. Debe estar **configurado** correctamente:

- Variables de entorno (credenciales de BD, API keys)
- Permisos de archivos y directorios
- Firewall y puertos abiertos
- Certificados SSL/TLS
- DNS apuntando al servidor

#### 1.2. Entornos de despliegue

En el ciclo de vida profesional, una aplicación pasa por múltiples entornos antes de llegar a producción:

**Desarrollo (Development)**

Donde los desarrolladores escriben y prueban código localmente:
- En sus propias máquinas
- Base de datos local
- Configuración laxa para debugging
- Datos de prueba ficticios

**Pruebas/Testing**

Entorno dedicado para testing:
- Pruebas automatizadas (unit, integration, E2E)
- QA manual
- Datos de prueba más realistas
- Configuración similar a producción

**Staging/Pre-producción**

Réplica exacta de producción para pruebas finales:
- Misma configuración que producción
- Mismo hardware (o similar)
- Datos anonimizados de producción
- Última barrera antes de release

**Producción (Production)**

El entorno real donde los usuarios acceden:
- Máxima disponibilidad
- Configuración optimizada para rendimiento
- Datos reales
- Monitorización exhaustiva
- Backups regulares

**Flujo típico:**

```
Desarrollo → Testing → Staging → Producción
   ↓            ↓         ↓           ↓
  Local    CI/CD Tests  Pruebas   Usuarios
                        finales    reales
```

#### 1.3. Retos del despliegue

Desplegar aplicaciones web presenta múltiples desafíos:

**"Funciona en mi máquina"**

El problema clásico: la aplicación funciona perfectamente en el portátil del desarrollador pero falla en producción. ¿Por qué?

- Versiones diferentes de PHP/Python/Node
- Extensiones o módulos que faltan
- Bases de datos con configuraciones distintas
- Rutas de archivos hardcodeadas
- Variables de entorno no definidas

**Downtime durante el despliegue**

Tradicionalmente, desplegar significaba:
1. Detener el servidor
2. Actualizar el código
3. Reiniciar el servidor
4. ¡El sitio estuvo inaccesible 5-10 minutos!

Esto ya no es aceptable. Los usuarios modernos esperan disponibilidad 24/7.

**Rollback complicado**

Si el despliegue introduce un bug crítico, necesitas volver a la versión anterior **rápidamente**. Sin un proceso automatizado, esto puede ser caótico.

**Escalabilidad**

Si tu aplicación tiene éxito, crecerá. ¿Puede tu infraestructura crecer con ella? ¿Puedes añadir más servidores fácilmente?

**Seguridad**

Cada despliegue es un punto de vulnerabilidad potencial. ¿Cómo aseguras que el proceso de despliegue no introduce brechas de seguridad?

**Las soluciones modernas** (contenedores, orquestación, CI/CD, cloud) existen precisamente para resolver estos problemas.

### 2. Escalabilidad: crecer sin límites

Uno de los desafíos más importantes en el despliegue es la **escalabilidad**: la capacidad de tu aplicación para manejar un aumento de carga sin degradar el rendimiento.

#### 2.1. ¿Por qué necesitamos escalabilidad?

Imaginad que lanzáis una aplicación web que se vuelve viral. El primer día tenéis 100 usuarios. Al segundo, 10,000. Al tercero, 100,000. Si vuestro servidor solo puede manejar 1,000 usuarios concurrentes, **vuestro sitio se caerá**.

La escalabilidad es la diferencia entre:
- **Éxito**: Tu aplicación crece con la demanda
- **Fracaso**: Tu servidor colapsa cuando más lo necesitas

**Casos reales:**

- **Twitter** durante eventos masivos (SuperBowl, elecciones)
- **Sitios de comercio electrónico** durante Black Friday
- **Servicios de streaming** cuando lanzan series populares
- **Sitios de noticias** durante breaking news

#### 2.2. Escalabilidad Vertical (Scale Up)

La escalabilidad vertical consiste en **hacer más potente el servidor existente**.

**¿Cómo funciona?**

Aumentas los recursos de tu servidor actual:
- Más CPUs o cores
- Más RAM
- Discos más rápidos (SSD, NVMe)
- Mejor conexión de red

**Ejemplo:**

```
Servidor inicial:
- 2 cores CPU
- 4GB RAM
- 100GB HDD
→ Soporta 1,000 usuarios concurrentes

Después de escalar verticalmente:
- 16 cores CPU
- 64GB RAM
- 500GB SSD
→ Soporta 8,000 usuarios concurrentes
```

**Ventajas de la escalabilidad vertical:**

- **Simplicidad**: Solo un servidor que mantener
- **Sin cambios en la aplicación**: Tu código sigue funcionando igual
- **Menor latencia**: Todo está en una máquina, sin red de por medio
- **Más fácil de depurar**: No hay complejidad distribuida

**Desventajas importantes:**

- **Límite físico**: Hay un máximo de RAM o CPU que puedes poner
- **Downtime**: Cambiar hardware requiere apagar el servidor
- **Coste exponencial**: Los servidores de alta gama son **muy** caros
- **Single Point of Failure**: Si ese servidor falla, todo se cae
- **No hay redundancia**: Un solo servidor es un riesgo

**¿Cuándo usar Scale Up?**

- Aplicaciones pequeñas a medianas
- Presupuesto limitado
- Arquitectura legacy que no puede distribuirse
- Cuando el límite vertical aún no se ha alcanzado

#### 2.3. Escalabilidad Horizontal (Scale Out)

La escalabilidad horizontal consiste en **añadir más servidores** en lugar de hacer uno más potente.

**¿Cómo funciona?**

En lugar de un servidor gigante, tienes muchos servidores más pequeños trabajando juntos:

```
Antes (1 servidor):
[Servidor Potente]
- 16 cores
- 64GB RAM
→ Soporta 8,000 usuarios

Después (4 servidores):
[Servidor 1] [Servidor 2] [Servidor 3] [Servidor 4]
Cada uno:
- 4 cores
- 16GB RAM
→ Juntos soportan 10,000+ usuarios
```

**Ventajas de la escalabilidad horizontal:**

- **Escalabilidad casi infinita**: Puedes seguir añadiendo servidores
- **Sin downtime**: Añades servidores sin detener los existentes
- **Alta disponibilidad**: Si un servidor falla, los otros continúan
- **Coste lineal**: Más capacidad = más servidores económicos
- **Distribución geográfica**: Servidores en diferentes ubicaciones

**Desventajas:**

- **Complejidad**: Arquitectura distribuida es más difícil
- **Sincronización**: Datos y sesiones deben compartirse
- **Latencia de red**: Comunicación entre servidores añade delay
- **Más difícil de depurar**: Problemas distribuidos son complejos

**Componentes necesarios para Scale Out:**

**1. Balanceador de carga**: Distribuye las peticiones entre servidores

```
                [Balanceador de Carga]
                        |
        +---------------+---------------+
        |               |               |
   [Servidor 1]   [Servidor 2]   [Servidor 3]
```

**2. Almacenamiento compartido**: Base de datos centralizada o distribuida

**3. Gestión de sesiones**: Las sesiones deben persistir entre servidores

#### 2.4. Balanceadores de carga: el director de tráfico

Un **balanceador de carga** (load balancer) es un componente que distribuye inteligentemente las peticiones entrantes entre múltiples servidores.

**Algoritmos de balanceo:**

**Round Robin**

Las peticiones se distribuyen secuencialmente:
```
Petición 1 → Servidor 1
Petición 2 → Servidor 2
Petición 3 → Servidor 3
Petición 4 → Servidor 1  (vuelta al inicio)
```

Simple y justo, pero no considera la carga actual de cada servidor.

**Least Connections**

Envía la petición al servidor con menos conexiones activas:
```
Servidor 1: 10 conexiones
Servidor 2: 5 conexiones  ← Nueva petición va aquí
Servidor 3: 8 conexiones
```

Mejor distribución de la carga real.

**IP Hash**

El mismo cliente siempre va al mismo servidor:
```
Cliente IP 192.168.1.10 → hash → Servidor 2 (siempre)
```

Mantiene afinidad de sesión.

**Weighted**

Servidores más potentes reciben más peticiones:
```
Servidor 1 (potente): peso 3
Servidor 2 (medio):   peso 2
Servidor 3 (débil):   peso 1
```

**Tipos de balanceadores:**

**Software**:
- Nginx
- HAProxy
- Apache mod_proxy_balancer
- Traefik

**Hardware**:
- F5 Networks
- Citrix ADC
- Soluciones enterprise

**Cloud**:
- AWS Elastic Load Balancer
- Azure Load Balancer
- Google Cloud Load Balancing

**Ejemplo de configuración con Nginx:**

```nginx
upstream backend {
    # Servidores backend
    server 192.168.1.10:8080 weight=3;
    server 192.168.1.11:8080 weight=2;
    server 192.168.1.12:8080 weight=1;
    
    # Health check
    server 192.168.1.13:8080 backup;
}

server {
    listen 80;
    server_name www.ejemplo.com;
    
    location / {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

#### 2.5. Clusters: trabajando en equipo

Un **cluster** es un grupo de servidores que trabajan juntos como una unidad lógica única.

**Tipos de clusters:**

**High Availability (HA) Cluster**

Objetivo: Máxima disponibilidad. Si un servidor falla, otro toma su lugar inmediatamente.

**Load Balancing Cluster**

Objetivo: Distribuir carga. Múltiples servidores atienden peticiones en paralelo.

**High Performance Computing (HPC) Cluster**

Objetivo: Máximo rendimiento. Servidores trabajan en tareas computacionalmente intensivas.

### 3. Contenedores: la revolución del despliegue

Los **contenedores** han revolucionado completamente cómo desplegamos aplicaciones. Son la solución moderna al problema "funciona en mi máquina".

#### 3.1. ¿Qué es un contenedor?

Un **contenedor** es una unidad de software que empaqueta código y todas sus dependencias para que la aplicación se ejecute de forma rápida y confiable de un entorno de computación a otro.

**Analogía del mundo real:**

Un contenedor es como un **contenedor de transporte marítimo**:

- Tamaño estándar
- Se puede mover entre barcos, trenes, camiones sin modificarlo
- El contenido está aislado y protegido
- Sabes exactamente qué hay dentro

**Diferencia con máquinas virtuales:**

```
Máquina Virtual:
[Hardware]
  ↓
[Hypervisor]
  ↓
[VM1: OS completo + App] [VM2: OS completo + App]
Peso: ~GB cada una

Contenedor:
[Hardware]
  ↓
[Sistema Operativo Host]
  ↓
[Docker Engine]
  ↓
[Contenedor 1: App] [Contenedor 2: App]
Peso: ~MB cada uno
```

**Ventajas de los contenedores:**

- **Ligeros**: MBs vs GBs de VMs
- **Rápidos**: Arrancan en segundos
- **Portables**: Funcionan igual en cualquier sitio
- **Eficientes**: Muchos contenedores en un host
- **Consistentes**: "Si funciona en Docker, funciona en producción"

#### 3.2. Docker: el estándar de contenedores

**Docker** es la plataforma de contenedores más popular del mundo.

**Conceptos clave:**

**Imagen Docker**

Una plantilla de solo lectura con las instrucciones para crear un contenedor. Es como una "receta":

```dockerfile
# Dockerfile para una app PHP
FROM php:8.1-apache

# Instalar extensiones PHP necesarias
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Copiar código de la aplicación
COPY ./src /var/www/html/

# Exponer puerto 80
EXPOSE 80
```

**Contenedor Docker**

Una instancia en ejecución de una imagen. Es la aplicación corriendo.

**Docker Hub**

Registro público de imágenes Docker. Miles de imágenes oficiales y de la comunidad.

**Ejemplo práctico:**

```bash
# Descargar imagen oficial de Nginx
docker pull nginx:latest

# Ejecutar un contenedor
docker run -d -p 8080:80 --name mi-web nginx

# Tu servidor Nginx está corriendo en http://localhost:8080

# Ver contenedores corriendo
docker ps

# Detener contenedor
docker stop mi-web

# Eliminar contenedor
docker rm mi-web
```

**Desplegar aplicación PHP con Docker:**

```dockerfile
# Dockerfile
FROM php:8.1-apache

# Instalar dependencias
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    && docker-php-ext-configure gd \
    && docker-php-ext-install gd mysqli pdo pdo_mysql

# Habilitar mod_rewrite
RUN a2enmod rewrite

# Copiar aplicación
COPY . /var/www/html/

# Permisos
RUN chown -R www-data:www-data /var/www/html

EXPOSE 80
```

```bash
# Construir imagen
docker build -t mi-app-php .

# Ejecutar contenedor
docker run -d -p 80:80 \
  -e DB_HOST=mysql \
  -e DB_USER=root \
  -e DB_PASS=secret \
  --name webapp \
  mi-app-php
```

#### 3.3. Docker Compose: orquestación simple

**Docker Compose** permite definir y ejecutar aplicaciones multi-contenedor.

**Ejemplo: WordPress con MySQL:**

```yaml
# docker-compose.yml
version: '3.8'

services:
  # Base de datos MySQL
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: secret
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wpuser
      MYSQL_PASSWORD: wppass
    volumes:
      - db_data:/var/lib/mysql
    networks:
      - wordpress_net

  # WordPress
  wordpress:
    depends_on:
      - db
    image: wordpress:latest
    ports:
      - "8000:80"
    environment:
      WORDPRESS_DB_HOST: db:3306
      WORDPRESS_DB_USER: wpuser
      WORDPRESS_DB_PASSWORD: wppass
      WORDPRESS_DB_NAME: wordpress
    volumes:
      - wordpress_data:/var/www/html
    networks:
      - wordpress_net

volumes:
  db_data:
  wordpress_data:

networks:
  wordpress_net:
```

```bash
# Levantar toda la aplicación
docker-compose up -d

# Ver servicios corriendo
docker-compose ps

# Ver logs
docker-compose logs -f

# Detener todo
docker-compose down
```

Con un solo comando (`docker-compose up`) tienes WordPress + MySQL funcionando localmente. ¡Magia!

#### 3.4. Kubernetes: orquestación a gran escala

Cuando tienes muchos contenedores en múltiples servidores, necesitas **Kubernetes** (K8s).

**¿Qué es Kubernetes?**

Una plataforma open-source para automatizar el despliegue, escalado y gestión de aplicaciones en contenedores.

**Conceptos clave:**

**Pod**: La unidad más pequeña, uno o más contenedores que se despliegan juntos

**Deployment**: Define cómo desplegar y escalar Pods

**Service**: Expone Pods a la red

**Ingress**: Gestiona acceso externo (HTTP/HTTPS)

**Ejemplo de Deployment:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: webapp-deployment
spec:
  replicas: 3  # 3 instancias de la app
  selector:
    matchLabels:
      app: webapp
  template:
    metadata:
      labels:
        app: webapp
    spec:
      containers:
      - name: webapp
        image: mi-app:v1.0
        ports:
        - containerPort: 80
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
```

**Ventajas de Kubernetes:**

- **Auto-escalado**: Añade/quita Pods según carga
- **Self-healing**: Reinicia contenedores que fallan
- **Rolling updates**: Actualiza sin downtime
- **Load balancing**: Distribuye tráfico automáticamente
- **Service discovery**: Contenedores se encuentran entre sí
- **Gestión de secretos**: Maneja credenciales de forma segura

Kubernetes es complejo, pero para aplicaciones grandes es indispensable.

### 4. Cloud Computing: el futuro del despliegue

El **cloud computing** (computación en la nube) ha transformado radicalmente cómo desplegamos aplicaciones.

#### 4.1. ¿Qué es la nube?

La "nube" no es magia; son **servidores de otras empresas** que alquilas bajo demanda.

**Modelos de servicio:**

**IaaS (Infrastructure as a Service)**

Alquilas servidores virtuales, storage, red. Tú gestionas el resto.

Ejemplos: AWS EC2, Google Compute Engine, Azure Virtual Machines

**PaaS (Platform as a Service)**

La plataforma gestiona infraestructura, tú solo despliegas código.

Ejemplos: Heroku, Google App Engine, AWS Elastic Beanstalk

**SaaS (Software as a Service)**

Aplicaciones completas listas para usar.

Ejemplos: Gmail, Salesforce, Office 365

#### 4.2. Principales proveedores cloud

**Amazon Web Services (AWS)**

El líder del mercado, con la mayor cantidad de servicios:

- **EC2**: Servidores virtuales
- **S3**: Almacenamiento de objetos
- **RDS**: Bases de datos gestionadas
- **Lambda**: Computación serverless
- **CloudFront**: CDN global

**Google Cloud Platform (GCP)**

Fuerte en big data y machine learning:

- **Compute Engine**: VMs
- **Cloud Storage**: Almacenamiento
- **Cloud SQL**: Bases de datos
- **Cloud Functions**: Serverless
- **BigQuery**: Análisis de datos masivos

**Microsoft Azure**

Ideal para entornos Microsoft:

- **Virtual Machines**: VMs
- **Azure SQL Database**: SQL Server en la nube
- **Azure Functions**: Serverless
- **Azure DevOps**: CI/CD integrado

#### 4.3. Despliegue en AWS (ejemplo práctico)

**Paso 1: Crear una instancia EC2**

```bash
# Usando AWS CLI
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t2.micro \
  --key-name mi-clave \
  --security-group-ids sg-0123456789abcdef0
```

**Paso 2: Conectar y configurar**

```bash
# Conectar vía SSH
ssh -i mi-clave.pem ubuntu@ec2-XX-XX-XX-XX.compute.amazonaws.com

# Instalar software
sudo apt update
sudo apt install apache2 php mysql-server

# Desplegar aplicación
sudo cp -r mi-app/* /var/www/html/
```

**Paso 3: Configurar autoscaling y load balancer**

AWS puede automáticamente añadir más instancias cuando la carga aumenta.

### 5. CI/CD: automatización del despliegue

**CI/CD** (Continuous Integration / Continuous Deployment) es la automatización completa del proceso de despliegue.

**Continuous Integration (CI)**

Integrar cambios de código frecuentemente, con tests automáticos:

```
Developer commit → Git push → CI ejecuta tests → Si pasan, merge
```

**Continuous Deployment (CD)**

Despliegue automático a producción cuando los tests pasan:

```
Tests pasan → Build automático → Deploy a staging → Tests en staging → Deploy a producción
```

**Herramientas CI/CD:**

- **Jenkins**: Open source, muy popular
- **GitLab CI**: Integrado con GitLab
- **GitHub Actions**: Integrado con GitHub
- **CircleCI**: Cloud, fácil de usar
- **Travis CI**: Popular en open source

**Ejemplo con GitHub Actions:**

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Run tests
      run: npm test
    
    - name: Build Docker image
      run: docker build -t mi-app:latest .
    
    - name: Push to Docker Hub
      run: |
        docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASS }}
        docker push mi-app:latest
    
    - name: Deploy to server
      run: |
        ssh user@server 'docker pull mi-app:latest && docker restart webapp'
```

Cada vez que haces push a main, se ejecutan automáticamente tests, build y despliegue. ¡Sin intervención manual!

## Resumen de la unidad

Hemos completado el viaje por el despliegue de aplicaciones web:

1. **Despliegue** es mucho más que copiar archivos; requiere software, hardware, dependencias y configuración correcta.

2. **Escalabilidad vertical** añade recursos a un servidor; **horizontal** añade más servidores con balanceo de carga.

3. **Contenedores Docker** resuelven "funciona en mi máquina", empaquetando todo lo necesario en una unidad portable.

4. **Kubernetes** orquesta cientos o miles de contenedores con auto-escalado y self-healing.

5. **Cloud computing** (AWS, Azure, GCP) proporciona infraestructura escalable bajo demanda.

6. **CI/CD** automatiza completamente el proceso de despliegue, desde commit hasta producción.

Este conocimiento os prepara para desplegar aplicaciones web modernas a escala profesional.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Docker Inc. (2024). *Docker Documentation*. [https://docs.docker.com/](https://docs.docker.com/)
- Kubernetes. (2024). *Kubernetes Documentation*. [https://kubernetes.io/docs/](https://kubernetes.io/docs/)
- Amazon Web Services. (2024). *AWS Documentation*. [https://docs.aws.amazon.com/](https://docs.aws.amazon.com/)

## Recursos adicionales

- [Play with Docker](https://labs.play-with-docker.com/) - Laboratorio online gratuito
- [Kubernetes Tutorials](https://kubernetes.io/docs/tutorials/) - Tutoriales oficiales
- [AWS Free Tier](https://aws.amazon.com/free/) - Capa gratuita de AWS
- [The Twelve-Factor App](https://12factor.net/) - Metodología para aplicaciones cloud-native
