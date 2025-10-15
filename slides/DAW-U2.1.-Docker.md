# U2.1 - Docker

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---  

## Índice

---

## 1. Conceptos Fundamentales de Docker

---

### 1.1. ¿Qué es Docker?


#### Definición

* Docker es una plataforma de código abierto para desplegar aplicaciones.
* Permite empaquetar apps en entornos aislados llamados contenedores.
* Alternativa eficiente a la virtualización tradicional con máquinas virtuales.
* Eslogan: "Build, Ship and Run Any App, Anywhere".
* Usa contenedores para lograr portabilidad y eficiencia.

Note: Presenta Docker como tecnología central de contenedores. Explica que permite encapsular aplicaciones para ser ejecutadas en cualquier entorno de forma eficiente.


#### Propósito

* Automatiza el despliegue de aplicaciones con contenedores.
* Aísla apps del entorno para mayor flexibilidad y portabilidad.
* Favorece entornos DevOps más ágiles y productivos.
* Reduce problemas de dependencia entre entornos.
* Permite desarrollar una vez y desplegar en cualquier parte.

Note: Explica cómo Docker mejora el flujo DevOps y facilita la entrega continua de software aislando aplicaciones del entorno subyacente.


#### Contenedores

* Son entornos autocontenidos que ejecutan una app o proceso.
* Comparten el kernel del sistema operativo anfitrión.
* Contienen su sistema de archivos, librerías y configuración.
* Permiten ejecutar servicios como bases de datos o apps web.
* También se pueden usar para herramientas de consola o scripts.

Note: Define qué es un contenedor en contraste con una máquina virtual. Enfatiza que no emula hardware sino que encapsula el entorno de ejecución.

---

### 1.2. Contenedores vs. Máquinas Virtuales



#### Diferencias de Arquitectura

* MV emulan hardware y ejecutan un sistema operativo completo.
* Los contenedores comparten el kernel del sistema anfitrión.
* Las MV necesitan un hipervisor para gestionar recursos.
* Los contenedores se ejecutan como procesos aislados.
* Contenedores arrancan en segundos; MV tardan más.

Note: Compara la arquitectura base entre MV y contenedores. Destaca eficiencia de los contenedores gracias a la ausencia de emulación.


#### Ventajas de los Contenedores

* Imágenes muy ligeras (ej. nginx:alpine pesa 15MB).
* Menor consumo de memoria y recursos.
* Rápido arranque, en milisegundos o segundos.
* Muy portables entre plataformas y entornos.
* Fáciles de compartir, replicar y desplegar.

Note: Resalta los beneficios clave de los contenedores frente a las MV, centrándose en eficiencia, portabilidad y velocidad.


#### Desventajas

* Menor aislamiento en comparación con MV (comparten kernel).
* Migrar apps complejas puede requerir reestructuración.
* Almacenamiento no persistente por defecto.
* Mayor complejidad si no se siguen buenas prácticas.

Note: Detalla las principales limitaciones de los contenedores, especialmente en seguridad, persistencia y mantenimiento inicial.

---

### 1.3. Arquitectura y Componentes de Docker


#### Componentes Principales

* Docker Engine (motor que ejecuta contenedores).
* Imágenes Docker (plantillas inmutables de contenedores).
* Docker Hub (registro público de imágenes).

Note: Describe brevemente los tres componentes esenciales del ecosistema Docker.


#### Docker Engine

* Consta de cliente (CLI), daemon (dockerd) y API REST.
* Dockerd gestiona contenedores, imágenes, redes y volúmenes.
* CLI se comunica con el daemon vía `/var/run/docker.sock`.
* La API REST permite control remoto de las operaciones.

Note: Explica cómo funciona el motor Docker como sistema cliente-servidor y sus tres partes principales.


#### Imágenes Docker

* Son plantillas inmutables, de solo lectura.
* Definen el entorno base para crear contenedores.
* Se crean desde archivos Dockerfile.
* Varias instancias (contenedores) pueden surgir de una imagen.
* Reutilizables y compartibles entre equipos y proyectos.

Note: Explica que las imágenes son el punto de partida de los contenedores. Son reutilizables y definidas mediante Dockerfile.


#### Contenedores Docker

* Son instancias en ejecución de una imagen.
* Aislados, modificables, y con red y volúmenes propios.
* Pueden crearse, iniciarse, detenerse o eliminarse fácilmente.
* Cambios no persistentes salvo que se usen volúmenes.
* Su ciclo de vida es efímero por defecto.

Note: Resume el funcionamiento de los contenedores como instancias activas de imágenes. Se detallan sus propiedades y el comportamiento efímero.

---

### 1.4. Almacenamiento en Docker


#### Naturaleza Efímera

* Por defecto, los datos dentro del contenedor se pierden al borrarlo.
* Alternativas: volúmenes, bind mounts y almacenamiento en memoria.
* Se recomienda usar volúmenes para persistencia de datos.
* Volúmenes permiten compartir datos entre host y contenedor.
* Datos persistentes son clave en apps como bases de datos.

Note: Detalla cómo Docker maneja el almacenamiento. Subraya que los contenedores son efímeros y que se deben usar mecanismos externos para persistir información.

---

## 2. Instalación y Comandos Básicos de Docker CLI

---

### 2.1. Instalación y configuración inicial


#### Requisitos Previos

* Revisar la documentación oficial según el sistema operativo.
* Docker requiere kernel Linux moderno o WSL2 en Windows.
* En Windows/macOS se recomienda Docker Desktop.
* En Linux, instalar Docker Engine desde repositorio oficial.

Note: Explica la necesidad de consultar la documentación para instalar Docker. Aclara que varía según el sistema operativo y se deben cumplir requisitos como el kernel compatible.


#### Instalación y Comprobación

* En Ubuntu: `sudo apt install docker-ce`.
* Verifica con `docker --version`.
* Prueba de ejecución: `docker run hello-world`.
* Si todo va bien, Docker está funcionando correctamente.

```bash
$ docker run hello-world
````

Note: Describe el proceso básico de instalación y la verificación con `hello-world`. Este comando descarga una imagen de prueba y la ejecuta.


#### Permisos de Usuario

* Solo root o usuarios del grupo `docker` pueden ejecutar Docker.
* Añade tu usuario al grupo:

```bash
sudo usermod -aG docker $USER
```

* Cierra sesión y vuelve a iniciar para aplicar cambios.

Note: Indica cómo evitar el uso constante de `sudo` para ejecutar Docker añadiendo el usuario al grupo adecuado.

---

### 2.2. Manejo del ciclo de vida de contenedores


#### Crear y Ejecutar Contenedores

* Usa `docker run` para crear y ejecutar un contenedor.
* Combina `docker create` y `docker start`.
* Ejemplo: `docker run ubuntu`.

Note: Explica que `docker run` es la forma rápida de lanzar contenedores. Equivale a crear e iniciar en una sola instrucción.


#### Modos de Ejecución

* **Interactivo:** `-it` abre terminal para interacción.
* **Detenido:** `-d` lo ejecuta en segundo plano (daemon).
* Combinar opciones según el uso necesario.

Note: Explica los modos principales: interactivo (para acceso tipo consola) y en background (para servicios).


#### Identificación y Nombres

* Docker asigna un ID y nombre automático al contenedor.
* Se puede nombrar con `--name`.
* Nombres e IDs se usan en operaciones posteriores.

Note: Señala cómo se identifican los contenedores, y la utilidad de asignar un nombre personalizado.


#### Visualizar Contenedores

* Ver activos: `docker ps` o `docker container ls`.
* Ver todos (incluso detenidos): `docker ps -a`.

Note: Explica cómo listar contenedores activos y también los que han sido detenidos. Diferencia entre ambos modos.


#### Operaciones Básicas

* `docker start`: inicia un contenedor detenido.
* `docker stop`: detiene uno en ejecución.
* `docker rm`: elimina un contenedor detenido.
* `docker kill`: lo fuerza a detenerse.

Note: Describe operaciones esenciales para controlar el ciclo de vida de los contenedores.


#### Inspección y Logs

* `docker inspect <id/nombre>` muestra info detallada.
* `docker logs <id/nombre>` muestra la salida del contenedor.
* `docker logs -f` sigue los logs en tiempo real.

Note: Explica cómo ver la configuración e información interna de un contenedor, así como sus salidas estándar.

---

### 2.3. Comandos avanzados y acceso


#### Acceder a la Shell

* `docker exec -it <id/nombre> /bin/bash`
* Permite entrar en un contenedor ya en ejecución.
* Útil para depuración o administración.

Note: Presenta el comando para acceder a la shell del contenedor y poder ejecutar instrucciones desde dentro.


#### Mapeo de Puertos

* Redirige puertos del host al contenedor.
* Sintaxis: `-p host:contenedor`.
* Ejemplo: `-p 8080:80` expone puerto 80 como 8080.

Note: Explica cómo exponer puertos del contenedor hacia fuera para servicios como servidores web.


#### Variables de Entorno

* Usar `-e VARIABLE=VALOR` en `docker run`.
* Ideal para pasar credenciales o configuración.
* Las variables afectan el comportamiento del contenedor.

Note: Comenta el uso de variables de entorno para configurar la app en el momento de ejecución.


#### Crear Imagen desde Contenedor

* `docker commit` guarda el estado actual como imagen.
* Útil para prototipos o estados modificados.
* Mejor `Dockerfile` a `docker commit`

```bash
docker commit contenedor nueva-imagen
```

Note: Muestra cómo convertir un contenedor con modificaciones en una nueva imagen. Se recomienda usar `Dockerfile` para producción.

---

## 3. Creación y Optimización de Imágenes (Dockerfile)

---

### 3.1. Introducción al Dockerfile


#### ¿Qué es un Dockerfile?

* Archivo de texto con instrucciones para construir imágenes.
* Automatiza la creación del entorno del contenedor.
* Cada línea representa una instrucción ejecutada al construir.
* Similar a un script de instalación paso a paso.
* Se utiliza con `docker build`.

Note: Presenta el Dockerfile como la receta o script para crear imágenes. Ayuda a mantener consistencia y automatización en entornos.


#### Sintaxis básica

* Cada instrucción en mayúscula (ej. `FROM`, `RUN`, `COPY`).
* Se ejecutan en orden, creando capas intermedias.
* Las imágenes se generan capa a capa.
* El orden influye en la eficiencia de caché.

Note: Explica cómo se interpreta el Dockerfile. El orden de las instrucciones impacta en el rendimiento y cacheado.

---

### 3.2. Instrucciones esenciales del Dockerfile


#### FROM

* Define la imagen base del contenedor.
* Ejemplo: `FROM python:3.11-slim`.
* Primer paso obligatorio de todo Dockerfile.

Note: Indica la imagen de la cual partimos. Puede ser oficial o personalizada.


#### RUN

* Ejecuta comandos en la imagen en construcción.
* Ejemplo: instalar paquetes con `apt`, `pip`, etc.
* Cada RUN crea una nueva capa.

```dockerfile
RUN apt update && apt install -y curl
````

Note: RUN se utiliza para preparar el entorno, instalar dependencias, ejecutar scripts de instalación, etc.


#### COPY y ADD

* `COPY`: copia archivos desde el host al contenedor. **Recomendado**.
* `ADD`: copia y además puede descomprimir archivos.
* Sintaxis: `COPY origen destino`.

```dockerfile
COPY app.py /app/
```

Note: COPY es más predecible y preferible a ADD, salvo que se necesite extracción automática.


#### CMD y ENTRYPOINT I

* CMD: comando por defecto al ejecutar la imagen.
* ENTRYPOINT: define el proceso principal del contenedor.
* Se pueden combinar para mayor flexibilidad.

```dockerfile
CMD ["python", "app.py"]
```

Note: CMD y ENTRYPOINT definen cómo se comporta el contenedor al iniciarse.


#### CMD y ENTRYPOINT II

* El contenido de CMD se pasa por parametro a ENTRYPOINT.
* Si ENTRYPOINT no existe, se usa CMD.
* Cuando se llama a un comando desde `docker run` se sustituye por CMD
* Por tanto, si solo se define CMD, puedo cambiar el comando al lanzar el contenedor.

Note: CMD puede ser sobrescrito por el usuario.


#### WORKDIR y ENV

* WORKDIR: define el directorio de trabajo por defecto dentro del contenedor
* ENV: define variables de entorno dentro del contenedor.
* Puedo ver con `env` como las variables se han definido en el contendor.

```dockerfile
WORKDIR /app
ENV DEBUG true
```

Note: Estas instrucciones permiten definir contexto de ejecución y configuración del contenedor.

---

### 3.3. Buenas prácticas y optimización


#### Orden lógico y limpieza

* Ordenar instrucciones: primero lo menos cambiante.
* Fusiona instrucciones con `&&`
* Limpieza tras instalaciones: `rm -rf /var/lib/apt/lists/*`.
* Reduce tamaño y mejora uso de caché.

```dockerfile
RUN apt-get update && apt-get install -y nodejs && rm -rf /var/lib/apt/lists/*
```

Note: El orden influye en la reutilización de capas. Elimina archivos temporales para mantener la imagen ligera.


#### Multietapa (multi-stage builds)

* Permite compilar en una imagen y copiar a otra más liviana.
* Reduce el tamaño final de la imagen.

```dockerfile
FROM golang:alpine AS build
WORKDIR /app
COPY . .
RUN go build -o myapp

FROM alpine
COPY --from=build /app/myapp /myapp
```

Note: Muestra cómo separar fases de compilación y ejecución. Muy útil en lenguajes compilados.


#### `.dockerignore`

* Similar a `.gitignore`, evita copiar archivos innecesarios.
* Mejora velocidad de build y reduce tamaño.

```dockerignore
*.log
__pycache__/
node_modules/
```

Note: `.dockerignore` es fundamental para evitar subir archivos temporales o pesados a la imagen.


#### Uso de imágenes ligeras

* Usar versiones `alpine`, `slim` cuando sea posible.
* Menor superficie de ataque y tamaño.

```dockerfile
FROM node:18-alpine
```

Note: Recomienda imágenes pequeñas para producción. Reduce vulnerabilidades y mejora eficiencia.


#### Uso de etiquetas y versiones

* Siempre especificar versiones (`python:3.11`, no `latest`).
* Facilita reproducibilidad y control de cambios.

Note: Explica la importancia de no usar `latest` para evitar builds impredecibles. Las versiones garantizan estabilidad.

---

## 4. Persistencia y Redes Avanzadas

---

### 4.1. Manejo de la Persistencia de Datos


#### Naturaleza efímera y necesidad de persistencia

* Los contenedores son **efímeros**: al eliminar el contenedor, **se pierden** los datos internos.
* Para conservar datos entre reinicios o recreaciones: **Volúmenes** y **Bind Mounts**.
* Objetivo: separar **código/estado** del ciclo de vida del contenedor.

Note: Motiva por qué no basta con el filesystem interno y presenta los dos mecanismos soportados por Docker.


#### Volúmenes I

* **Objeto gestionado por Docker**: su ciclo de vida es independiente del contenedor.
* Persisten aunque borres el contenedor; pueden **reutilizarse** entre varios contenedores.
* Acceso al contenido a través de contenedores; gestión con `docker volume *`.

```bash
# Crear y listar volúmenes
docker volume create datos-app
docker volume ls
````

Note: Recalca que volúmenes = opción recomendada para datos de aplicaciones/BDD por rendimiento, aislamiento y portabilidad.


#### Volúmenes II

* Montaje con `--mount` (verboso y claro) o `-v` (atajo).
* Ejemplo `--mount`:

```bash
docker run -dit --name miapache-php \
  --mount type=volume,source=vol-web,target=/var/www/html \
  miapache-php
```

Note: Muestra ambas sintaxis y cuándo elegir cada una.


#### Volúmenes III

* Volumen anónimo con `-v`. Luego tendras que consultarlos:

```bash
docker run -d -v /var/lib/mysql mariadb
```

* Eliminar:

```bash
docker volume rm datos-app
```

Note: Recuerda no borrar volúmenes usados.


#### Bind Mounts I

* **Mapean un directorio del host** dentro del contenedor.
* Ideales para **desarrollo** (código del host visible dentro del contenedor).
* Cambios en el host se reflejan **al instante**.

```bash
# Mapea el directorio actual a htdocs de Apache
docker run -dit --name miapache -p 5555:80 \
  -v "$PWD":/usr/local/apache2/htdocs httpd
```

Note: Enfatiza la rapidez de iteración en dev y que dependen de la estructura del host.


#### Bind Mounts II

* Sintaxis extendida con `--mount type=bind`:

```bash
docker run --mount type=bind,source="$PWD/src",target=/var/www/html ...
```

* Requisitos: rutas **existentes** en el host; heredan **permisos** del host.
* Tips:
    
    * SELinux: añade `:z`/`:Z` con `-v` si procede.
    * Solo lectura: `-v "$PWD":/app:ro` o `--mount,readonly`.

Note: Da “gotchas”: permisos/SELinux/solo-lectura y necesidad de que la ruta exista.


#### Casos de uso

* **Bases de datos, logs, artefactos persistentes → Volúmenes.**
* **Código fuente, assets en caliente → Bind Mounts.**
* Regla práctica: producción ≈ **volúmenes**; desarrollo ≈ **bind mounts**.

Note: Resume decisión rápida para el día a día del alumnado y justifica la elección.

---

### 4.2. Configuración de Redes (Networking)


#### Aislamiento

* Docker usa **namespaces** de red y pares **veth** para aislar contenedores.
* Bridge `docker0`: NAT mediante **iptables** para tráfico saliente y publicación de puertos.
* Cada contenedor tiene su **stack IP** aislado.

Note: Explica el “cómo” básico: namespaces + veth + NAT; fija el vocabulario que aparecerá en comandos.


#### Modos de red I (bridge / host)

* **bridge (por defecto)**:
    
    * Red privada en el host, NAT para salida.
    * Acceso externo con `-p HOST:CONT`.
    * Para poder usar DNS de contenedores, el usaurio debe crear la red bridge.

* **host**:
    
    * Comparte la red del host (sin NAT), por tanto contenedores accesibles. Ignora `-p`.
    * Mejor latencia; cuidado con **colisiones de puertos**.


Note: Contrasta rendimiento vs. aislamiento y cuándo elegir cada modo.


#### Modos de red II (none)

* **none**:
    
    * Sin red (solo loopback). Útil para jobs offline.

```bash
docker run -d --name web -p 8080:80 nginx:alpine           # bridge
docker run -d --name metrica --network host node:alpine    # host
docker run -d --name job --network none busybox sleep 60   # none
```

Note: Contrasta rendimiento vs. aislamiento y cuándo elegir cada modo.


#### Modos de red III (macvlan / overlay)

Avanzado

* **macvlan**:
    
    * Cada contenedor obtiene **MAC/IP propias** en la LAN.
    * Útil para integrar con redes físicas o appliances L2.
* **overlay**:
    
    * Red **multi-host** distribuida (VXLAN) para clústeres (p.ej., Swarm).
    * Contenedores en hosts distintos se ven “como si” compartieran LAN.

Note: Presenta casos típicos: macvlan para visibilidad L2; overlay para orquestadores.


#### Redes definidas por usuario I

* Mejor práctica: crear redes **bridge de usuario**.
* Beneficios:
    
    * **DNS interno** entre contenedores por **nombre**.
    * Aislamiento por red; políticas de exposición controladas.

```bash
docker network create mired
docker run -d --name api --network mired miapi
docker run -d --name web --network mired -p 8080:80 miweb
```

Note: Diferencia explícita: el bridge por defecto no resuelve nombres; las redes de usuario sí.


#### Redes definidas por usuario II

* Inspeccionar, conectar y desconectar:

```bash
docker network ls
docker network inspect mired
docker network connect mired otro-contenedor
docker network disconnect mired api
```

* Múltiples redes por contenedor y **aliases** de servicio.
* En Compose, los nombres de **servicio** actúan como hosts DNS.

Note: Enseña operaciones típicas y relación directa con Compose.


#### Enlace de contenedores I (Legacy `--link`)

* `--link` está **obsoleto**: alteraba `/etc/hosts` y pasaba variables de entorno.
* Solo tenía sentido en el bridge por defecto (sin DNS).

```bash
# Obsoleto: evitar en producción
docker run --link db:dbalias app
```

Note: Desaconseja su uso, justifica por qué y deja rastro histórico.


#### Enlace de contenedores II (DNS moderno)

* Con redes de usuario, usa **DNS integrado**:
    
    * Conecta por **nombre de contenedor** o **servicio Compose**.
* Ejemplo WordPress:

```yaml
services:
  db:
    image: mariadb
  web:
    image: wordpress
    environment:
      WORDPRESS_DB_HOST: db   # nombre del servicio
```

Note: Refuerza “usa el nombre del servicio” como patrón mental en Compose.


#### Diagnóstico de red

* Comandos útiles:

```bash
docker network ls
docker network inspect mired
docker exec -it web sh -c "ip a; ip route; cat /etc/resolv.conf"
docker exec -it web sh -c "apk add --no-cache bind-tools curl; nslookup api; curl -I http://api:8080"
```

* Revisa mapeos `-p`, conflictos de puertos, reglas de iptables/NAT.

Note: Proporciona un checklist rápido para resolver “no me resuelve / no conecta”.


#### Seguridad de red y exposición

* Publica **solo** lo necesario (`-p` / `ports:`). `EXPOSE` es **informativo**.
* Separa servicios en **redes distintas**; reduce la **ICC** (inter-container communication).
* Evita `--privileged`, reduce **capabilities** si procede.
* Filtra en el host (firewall) y usa **readonly mounts** cuando aplique.

Note: Conecta persistencia y red con hardening básico del despliegue.

---

## 5. Compartiendo Imágenes y Registros

---

### 5.1. Docker Hub y Gestión Remota


#### Panorama general

* Un **registro** almacena y distribuye **imágenes** (OCI/Docker).
* **Docker Hub** es el registro público por defecto del cliente Docker.
* Flujo típico: _build → tag → login → push → pull_.

Note: Aclara la diferencia imagen (plantilla) vs. contenedor (instancia) y el rol de un registro.


#### Buscar imágenes (docker search)

* Encuentra imágenes oficiales y de la comunidad.
* Observa **STARS** (popularidad) y **OFFICIAL**.

```bash
docker search ubuntu
docker search "postgres"
````

Note: `docker search` consulta Docker Hub salvo que especifiques otro registro en el nombre (no muestra todo el metadata de seguridad).


#### Descargar imágenes (docker pull)

* Descarga una imagen localmente (si falta se hace en `docker run`).
* Especifica **tag**; evita confiar en `:latest`.

```bash
docker pull ubuntu:20.04
docker pull nginx:1.27-alpine
```

Note: Fijar versiones mejora reproducibilidad y seguridad; `:latest` puede cambiar sin aviso.


#### Autenticación (docker login)

* Requisito para *push* y para repos **privados**.

```bash
docker login            # interactivo
docker login -u <usuario>
docker logout
```

Note: Las credenciales se guardan en el helper/config del cliente; usa 2FA/tokens personales cuando sea posible.


#### Etiquetado (docker tag)

* Formato Docker Hub: `USUARIO/REPO:TAG`.
* Puedes añadir varias **etiquetas** al mismo `IMAGE ID`.

```bash
docker tag mi-imagen:build123 joseluisgs/mi-app:v1
docker images
```

Note: El tag enlaza tu imagen local con el repositorio remoto objetivo; no copia bytes por sí mismo.


#### Publicar (docker push)

* Sube la imagen etiquetada al registro remoto.

```bash
docker push joseluisgs/mi-app:v1
```

* Verifica luego con `docker pull` desde otra máquina.

Note: Si intentas `push` sin prefijo de usuario en Docker Hub, fallará (no puedes publicar en “raíz”).


#### Buenas prácticas de publicación

* Usa **tags semánticos** (`v1.2.3`, `1.2-alpine`) y marca **inmutable**.
* Añade **LABEL** de metadatos (source, version, maintainer).
* Firma o verifica: **Docker Content Trust / Notary**.
* Automatiza *build/scan/push* en CI con análisis de CVEs.

Note: La inmutabilidad de tags evita sorpresas; si necesitas mover un tag, crea uno nuevo y depreca el antiguo.

---

### 5.2. Automatización y Registros Alternativos


#### Builds automatizados (visión general)

* Conecta un repo (GitHub/Bitbucket) a un registro para construir en cada **commit/tag**.
* Resultado: imagen construida en servidores del registro y subida automáticamente.

Note: Ideal para pipelines simples; para escenarios avanzados usa tu propio CI (GitHub Actions, GitLab CI, Jenkins) + `docker buildx`.


#### Builds automatizados (pasos típicos) I

1. Repo con `Dockerfile` (y `.dockerignore`).
2. Configura **reglas** por rama/tag.
3. Opcional: variables/secretos para el build.

Note: Coloca el Dockerfile en la raíz o indica el contexto/subcarpeta según soporte del registro.


#### Builds automatizados (pasos típicos) II

* Estrategia de tags:
    
    * Ramas → `:edge`, `:dev`.
    * Tags Git → `:1.4.2`, `:1.4`.

* Añade **escaneo de vulnerabilidades** tras el build.

Note: Publica imágenes de producción solo desde tags Git firmados/revisionados.


#### Registros alternativos I (visión)

* **Quay** (Red Hat): público/privado, escaneo integrado.
* **Amazon ECR**: privado, integrado con IAM y AWS.
* **Google Artifact Registry/GCR**: integrado en GCP.
* **Azure ACR**: integración con Azure y RBAC.
* **Harbor** (open source, on-prem): RBAC, replicación, escaneo.

Note: Elige por integración cloud, cumplimiento (RBAC/retención), escaneo y coste.


#### Registros alternativos II (nomenclatura)

* ECR: `aws_account_id.dkr.ecr.REGION.amazonaws.com/mi-repo:tag`
* GCR/Artifact Registry: `REGION-docker.pkg.dev/PROJECT/REPO/img:tag`
* ACR: `<nombre>.azurecr.io/mi-repo:tag`
* Quay/Harbor on-prem: `registry.midominio.com/namespace/img:tag`

```bash
docker login <endpoint-del-registro>
docker pull <endpoint>/<repo>:<tag>
docker push <endpoint>/<repo>:<tag>
```

Note: La autenticación suele delegarse en el CLI cloud (aws/gcloud/az) para obtener tokens temporales.


#### Registro privado básico con `registry:2`

* Levanta un registro local sencillo (desarrollo/pruebas):

```bash
docker run -d -p 5000:5000 --restart=always --name registro registry:2
```

* Etiqueta y sube:

```bash
docker tag mi-img:v1 localhost:5000/mi-repo:v1
docker push localhost:5000/mi-repo:v1
```

Note: Úsalo en entornos controlados; por defecto no lleva TLS ni autenticación.

---

## 6. Docker Compose: Orquestación Local de Multicontenedores

---

### 6.1. Introducción y Utilidad


#### ¿Qué es Docker Compose?

* Herramienta para **definir y ejecutar** aplicaciones **multi-contenedor**.
* Un único archivo **YAML** describe servicios, redes y volúmenes.
* Un comando (`docker-compose up`) levanta todo el stack.

Note: Reemplaza múltiples `docker run` con parámetros complejos por una definición declarativa, reproducible y versionable.


#### Casos de uso

* **Desarrollo local**: levantar web + BD + cache con un solo comando.
* **CI/Test**: entornos efímeros, predecibles y aislados.
* **Despliegue sencillo** en un único host (no es orquestador distribuido).

Note: Para clúster y HA usa Swarm/Kubernetes; Compose brilla en single-host y pipelines de desarrollo.

--- 

### 6.2. Sintaxis y Configuración del Archivo `docker-compose.yml`


#### Estructura principal

* Secciones típicas: `services`, `volumes`, `networks`.
* Versión recomendada: formato v3+ (especialmente si luego migras a Swarm).

```yaml
version: "3.9"
services:
  web:
    image: nginx:alpine
volumes:
  data:
networks:
  front:
````

Note: Mantén el archivo pequeño y legible; considera dividir por entorno (`-f docker-compose.prod.yml`).


#### Definición de servicios I

Significado de algunos parametros que pueden aparecer

* `image`: imagen a usar (`mariadb:10.5`).
* `build`: ruta para construir Dockerfile (alternativa a `image`).
* `container_name`: nombre fijo (opcional).
* `ports`: mapeo `host:contenedor` (p.e. `8080:80`).
* `environment`: variables de entorno.

```yaml
services:
  api:
    build: .
    ports: ["8080:8080"]
    environment:
      - APP_ENV=dev
```

Note: Prefiere `image` para reproducibilidad; usa `build` cuando controlas el Dockerfile en el repo.


#### Definición de servicios II

* `volumes`: persistencia o bind mounts (`./src:/app`).
* `depends_on`: orden de arranque (no espera readiness).
* `networks`: asigna el servicio a redes definidas.
* `command`/`entrypoint`: sobreescriben comportamiento por defecto.

```yaml
services:
  worker:
    image: myorg/worker:1.0
    depends_on: [queue]
    volumes:
      - ./config:/app/config:ro
    command: ["python","worker.py"]
```

Note: Para readiness usa healthchecks o lógica de reintentos a nivel de aplicación/entrypoint.


#### Redes y DNS en Compose

* Las redes **de usuario** dan DNS interno (resuelve por **nombre de servicio**).
* Los servicios en la misma red se ven sin exponer puertos al host.

```yaml
networks:
  backend:
services:
  api:
    networks: [backend]
  db:
    networks: [backend]
```

Note: En redes definidas por usuario no necesitas `--link`; Compose crea un DNS interno por red.


#### Buenas prácticas de YAML/Compose

* Usa **`.env`** para credenciales no sensibles y puertos.
* Divide overrides por entorno: `-f docker-compose.yml -f docker-compose.prod.yml`.
* Añade `healthcheck` para detectar fallos del servicio.
* Nombra volúmenes y redes para facilitar mantenimiento.

```yaml
services:
  api:
    healthcheck:
      test: ["CMD","curl","-f","http://localhost:8080/health"]
      interval: 10s
      timeout: 2s
      retries: 6
```

Note: `depends_on` no espera healthcheck; usa `restart` policies y reintentos app-side.


#### Ejemplo: WordPress + MariaDB I

* Stack típico de web + base de datos con persistencia y variables de entorno.

```yaml
version: "3"
services:
  db:
    image: mariadb:10.5
    container_name: mariadb
    environment:
      - MYSQL_ROOT_PASSWORD=secret
      - MYSQL_DATABASE=wordpress
      - MYSQL_USER=manager
      - MYSQL_PASSWORD=secret
    volumes:
      - data:/var/lib/mysql
```

Note: Las variables de entorno inicializan MariaDB; el volumen `data` persiste los datos.


#### Ejemplo: WordPress + MariaDB II

```yaml
  web:
    image: wordpress:4.9.8
    container_name: wordpress
    depends_on: [db]
    environment:
      - WORDPRESS_DB_USER=manager
      - WORDPRESS_DB_PASSWORD=secret
      - WORDPRESS_DB_HOST=db
    volumes:
      - ./wordpress:/var/www/html
    ports:
      - "8080:80"

volumes:
  data:
```

Note: `WORDPRESS_DB_HOST=db` usa el **nombre del servicio** (DNS interno). El bind mount permite editar el código localmente.

---

### 6.3. Comandos Útiles con Docker Compose


#### Levantar servicios

* Primer plano (logs combinados) o en **detached**.

```bash
docker-compose up            # primer plano
docker-compose up -d         # segundo plano
```

Note: `up` crea redes/volúmenes si no existen y construye imágenes si hay `build` configurado.


#### Escalado y reconstrucción

* Escala réplicas del servicio (stateless):

```bash
docker-compose up -d --scale web=5
```

* Fuerza rebuild de imágenes:

```bash
docker-compose build
docker-compose up -d --build
```

Note: Escalar bases de datos estateless no es trivial; reserva `--scale` para componentes sin estado.


#### Parada y eliminación

```bash
docker-compose stop          # detiene, conserva contenedores
docker-compose start         # reinicia lo detenido
docker-compose rm            # elimina contenedores detenidos
docker-compose down          # detiene y elimina (redes propias también)
docker-compose down -v       # elimina también volúmenes
```

Note: `down -v` borra **datos** (irreversible). Úsalo con precaución si hay BDs.


#### Logs y acceso

```bash
docker-compose ps
docker-compose logs                 # históricos
docker-compose logs -ft             # follow + timestamp
docker-compose exec web /bin/bash   # shell dentro del contenedor
```

Note: Usa `exec` para tareas administrativas puntuales; evita instalar SSH en contenedores.


#### Multiples archivos y entornos

* Combina archivos para overrides por entorno:

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

* Variables desde `.env`:

```bash
# .env
POSTGRES_PORT=5432
```

Note: Los valores de `.env` pueden referenciarse en YAML (`${POSTGRES_PORT}`) y no deben versionar secretos sensibles.


#### Buenas prácticas con Compose

* Fija **versiones** de imágenes (no `latest`).
* Define volúmenes nombrados para **persistencia**.
* Aísla servicios por **redes** y principio de mínimo puerto expuesto.
* Mantén la app **12-Factor**: configuración vía variables de entorno.

Note: El diseño declarativo + versiones fijas mejora reproducibilidad y facilita diagnóstico en CI/CD.

---

## ¡Gracias por su atención!

Note: Finaliza la presentación invitando a preguntas. Recalca que entender estas fases facilita el trabajo con herramientas de programación y la optimización de proyectos.