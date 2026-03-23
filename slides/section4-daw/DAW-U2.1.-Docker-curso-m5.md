# Curso Docker - Módulo 5

## Creación de Imágenes Docker

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice Módulo 5

* Creación de imágenes desde contenedores
* Dockerfile: construcción automatizada
* Instrucciones principales de Dockerfile
* Mejores prácticas
* Distribución de imágenes
* Ciclo de vida de aplicaciones

---

## 1. Introducción


### ¿Por Qué Crear Imágenes Propias?

* Empaquetar nuestras aplicaciones.
* Incluir dependencias específicas.
* Configuraciones personalizadas.
* Distribución fácil y reproducible.

Note: Hasta ahora hemos usado imágenes existentes de Docker Hub. Pero para nuestras aplicaciones necesitamos crear imágenes personalizadas que incluyan nuestro código, todas las dependencias, y configuraciones específicas. Esto permite distribuir y desplegar aplicaciones fácilmente.


### Dos Métodos de Creación

* **Desde contenedor**: Modificar y guardar.
* **Desde Dockerfile**: Automatizado y reproducible.

Note: Hay dos formas de crear imágenes. Podemos modificar un contenedor existente y guardarlo como imagen (docker commit), útil para experimentar. O escribir un Dockerfile que automatiza toda la construcción, que es el método recomendado para producción porque es reproducible y documentado.


### Método 1: Docker Commit

```bash
$ docker run -it --name temporal ubuntu bash
root@abc123:/# apt update && apt install -y nginx
root@abc123:/# exit

$ docker commit temporal mi_nginx:v1
sha256:def456ghi789...

$ docker images
REPOSITORY   TAG    IMAGE ID
mi_nginx     v1     def456ghi789
```

Note: Docker commit guarda el estado actual de un contenedor como nueva imagen. Es rápido para experimentar pero no documentado ni reproducible. No sabremos qué cambios se hicieron al mirar la imagen. Por eso Dockerfile es preferible.

---

## 2. Dockerfile


### ¿Qué es un Dockerfile?

* Archivo de texto con instrucciones.
* Automatiza la construcción de imágenes.
* Reproducible, documentado y versionable.
* Formato: `INSTRUCCION argumentos`

Note: Un Dockerfile es un script que define cómo construir una imagen paso a paso. Cada línea es una instrucción que añade una capa a la imagen. Es la forma estándar y profesional de crear imágenes: totalmente reproducible, auto-documentada, y versionable en Git.


### Estructura Básica

```dockerfile
# syntax=docker/dockerfile:1
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y nginx
COPY index.html /var/www/html/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Note: Un Dockerfile típico comienza con FROM (imagen base), continúa con RUN (ejecutar comandos), COPY (copiar archivos), EXPOSE (documentar puertos), y termina con CMD (comando por defecto al ejecutar contenedor).


### Instrucción FROM

```dockerfile
FROM ubuntu:22.04
FROM python:3.11-slim
FROM node:18-alpine
FROM nginx:alpine
```

Note: FROM especifica la imagen base desde la que construimos. Es la primera instrucción del Dockerfile. Elegir una buena imagen base es crucial: Ubuntu/Debian para máxima compatibilidad, Alpine para mínimo tamaño, o imágenes específicas de lenguaje que ya incluyen runtime necesario.


### Instrucción RUN

```dockerfile
RUN apt-get update && apt-get install -y \
    nginx \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*
```

Note: RUN ejecuta comandos durante la construcción de la imagen. Cada RUN crea una nueva capa. Es mejor combinar múltiples comandos relacionados con && para minimizar capas. Siempre limpiar caches y archivos temporales al final de cada RUN para reducir tamaño.


### Instrucción COPY

```dockerfile
COPY app.py /app/
COPY requirements.txt /app/
COPY ./src /app/src/
COPY config/ /etc/myapp/
```

Note: COPY copia archivos y directorios del contexto de build al contenedor. El contexto es el directorio desde donde ejecutamos docker build. COPY solo puede acceder a archivos dentro del contexto. Es más simple y recomendado que ADD para casos normales.


### Instrucción ADD

```dockerfile
ADD https://example.com/file.tar.gz /tmp/
ADD archive.tar.gz /app/
```

Note: ADD es similar a COPY pero con funcionalidades extra: puede descargar archivos desde URLs y extraer automáticamente archivos tar/zip. Para casos simples usar COPY. Usar ADD solo cuando necesitemos estas funcionalidades específicas.


### Instrucción WORKDIR

```dockerfile
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

Note: WORKDIR establece el directorio de trabajo para instrucciones subsecuentes. Es como cd pero para Dockerfile. El directorio se crea automáticamente si no existe. Es mejor que usar RUN cd porque WORKDIR se mantiene entre instrucciones.


### Instrucción ENV

```dockerfile
ENV NODE_ENV=production
ENV PORT=8080
ENV DATABASE_URL=postgresql://localhost/mydb
ENV PATH="/app/bin:${PATH}"
```

Note: ENV define variables de entorno que estarán disponibles durante el build y en el contenedor en ejecución. Útil para configuración por defecto. Pueden sobrescribirse al ejecutar contenedor con -e. También útil para modificar PATH añadiendo directorios personalizados.


### Instrucción EXPOSE

```dockerfile
EXPOSE 80
EXPOSE 8080/tcp
EXPOSE 53/udp
EXPOSE 8000-8010
```

Note: EXPOSE documenta qué puertos usa la aplicación. NO publica el puerto automáticamente, es solo metadato informativo. Los usuarios sabrán qué puerto mapear con -p al ejecutar el contenedor. Puede especificar protocolo (tcp/udp) y rangos.


### Instrucciones CMD y ENTRYPOINT

```dockerfile
# CMD - comando por defecto, puede sobrescribirse
CMD ["python", "app.py"]

# ENTRYPOINT - comando fijo
ENTRYPOINT ["python"]
CMD ["app.py"]  # argumentos por defecto

# Usuario puede pasar argumentos diferentes
# docker run imagen otro_script.py
```

Note: CMD define el comando por defecto al ejecutar contenedor. Puede sobrescribirse completamente. ENTRYPOINT define comando fijo; lo que pasemos al contenedor se añade como argumentos. Combinar ambos permite flexibilidad: ENTRYPOINT como ejecutable, CMD como argumentos por defecto sobrescribibles.


### Instrucción USER

```dockerfile
RUN useradd -m -u 1000 appuser
USER appuser
WORKDIR /home/appuser
COPY --chown=appuser:appuser . .
```

Note: Por seguridad, no ejecutar aplicaciones como root. Crear usuario específico y cambiar a él con USER. Todo lo que sigue se ejecutará con ese usuario. --chown en COPY asegura que archivos copiados tengan permisos correctos.

---

## 3. Construyendo Imágenes


### Comando docker build

```bash
$ docker build -t mi_app:v1 .
$ docker build -t mi_app:latest -f Dockerfile.prod .
$ docker build --no-cache -t mi_app:v2 .
```

Note: docker build construye imagen desde Dockerfile. -t especifica nombre y tag. El punto (.) es el contexto de build. -f permite especificar Dockerfile alternativo. --no-cache fuerza reconstrucción sin usar cache de capas anteriores.


### Contexto de Build

```bash
# Estructura del proyecto
.
├── Dockerfile
├── app.py
├── requirements.txt
├── src/
│   ├── module1.py
│   └── module2.py
└── static/
    └── styles.css

$ docker build -t myapp .
```

Note: El contexto de build es el directorio pasado a docker build (el punto). Docker envía todo el contexto al daemon. COPY y ADD solo pueden acceder archivos dentro del contexto. Mantener contexto pequeño para builds rápidos.


### Archivo .dockerignore

```
# .dockerignore
.git
.gitignore
node_modules
*.log
.env
.vscode
__pycache__
*.pyc
.pytest_cache
coverage/
```

Note: El archivo .dockerignore funciona como .gitignore, excluyendo archivos/directorios del contexto de build. Excluir archivos innecesarios (repos git, node_modules, caches, logs) acelera builds y reduce tamaño de imagen final.


### Cache de Capas

```dockerfile
# ✅ Buen orden - cache eficiente
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# ❌ Mal orden - cache inútil
COPY . .
RUN pip install -r requirements.txt
```

Note: Docker cachea cada capa. Si una capa no cambia, reutiliza cache. Ordenar instrucciones de menos a más frecuente cambio optimiza builds. Copiar requirements.txt primero y luego código: cambios en código no invalidan cache de instalación de dependencias.

---

## 4. Ejemplo Completo


### Aplicación Python/Flask

```python
# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hola desde Docker!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```


### Dependencias

```
# requirements.txt
Flask==3.0.0
gunicorn==21.2.0
```


### Dockerfile Optimizado

```dockerfile
# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Variables de entorno
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Crear usuario no-root
RUN useradd -m -u 1000 appuser

# Directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias (para cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de aplicación
COPY --chown=appuser:appuser app.py .

# Cambiar a usuario no-root
USER appuser

# Puerto
EXPOSE 5000

# Comando por defecto
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Note: Dockerfile completo siguiendo mejores prácticas: imagen base slim, usuario no-root, orden optimizado para cache, limpieza de pip cache, variables de entorno apropiadas, y gunicorn para producción en lugar del servidor de desarrollo de Flask.


### Construcción

```bash
$ docker build -t flask_app:v1 .

[+] Building 25.3s (12/12) FINISHED
 => [1/7] FROM python:3.11-slim
 => [2/7] RUN useradd -m -u 1000 appuser
 => [3/7] WORKDIR /app
 => [4/7] COPY requirements.txt .
 => [5/7] RUN pip install -r requirements.txt
 => [6/7] COPY app.py .
 => [7/7] USER appuser
 => exporting to image
```

Note: El build muestra progreso de cada paso del Dockerfile. Docker descarga imagen base si no la tiene, ejecuta cada instrucción secuencialmente, y cachea cada capa. En builds subsecuentes, las capas sin cambios se reutilizan de cache, acelerando enormemente el proceso.


### Ejecución

```bash
$ docker run -d -p 5000:5000 --name myapp flask_app:v1

$ curl http://localhost:5000
<h1>Hola desde Docker!</h1>

$ docker logs myapp
[2024-01-28 10:15:30] [INFO] Starting gunicorn 21.2.0
[2024-01-28 10:15:30] [INFO] Listening at: http://0.0.0.0:5000
```

Note: Ejecutamos contenedor desde nuestra imagen personalizada. La aplicación funciona exactamente como la desarrollamos, con todas las dependencias correctas incluidas. Gunicorn proporciona un servidor production-ready en lugar del servidor de desarrollo de Flask.

---

## 5. Mejores Prácticas


### Usar Imágenes Base Pequeñas

```dockerfile
# ❌ Grande (1.1 GB)
FROM ubuntu:22.04

# ✅ Mediana (150 MB)
FROM python:3.11-slim

# ✅ Pequeña (50 MB)
FROM python:3.11-alpine
```

Note: Elegir imágenes base apropiadas. Ubuntu es grande pero muy compatible. Slim es buen compromiso: razonablemente pequeña y compatible. Alpine es la más pequeña pero usa musl en lugar de glibc, lo que puede causar incompatibilidades con algunos paquetes.


### Minimizar Número de Capas

```dockerfile
# ❌ Muchas capas
RUN apt-get update
RUN apt-get install -y nginx
RUN apt-get install -y curl
RUN rm -rf /var/lib/apt/lists/*

# ✅ Una capa optimizada
RUN apt-get update && \
    apt-get install -y nginx curl && \
    rm -rf /var/lib/apt/lists/*
```

Note: Cada RUN, COPY, ADD crea una capa. Combinar comandos relacionados reduce capas y tamaño de imagen. Importante: limpiar caches y temporales en el MISMO RUN donde se crean, no en RUN separado (ya estarían en capa anterior).


### Multi-stage Builds

```dockerfile
# Stage 1: Build
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

Note: Multi-stage builds usan múltiples FROM en un Dockerfile. Compilamos con imagen completa con herramientas, copiamos solo artefactos finales a imagen ligera para producción. Resultado: imágenes de producción minimalistas sin herramientas de build.


### Seguridad: No Root

```dockerfile
# Crear usuario
RUN groupadd -r appgroup && \
    useradd -r -g appgroup appuser

# Cambiar ownership
COPY --chown=appuser:appgroup app.py .

# Cambiar a usuario no-root
USER appuser
```

Note: Por seguridad, nunca ejecutar aplicaciones como root. Crear usuario y grupo específicos, asignar ownership correcto a archivos, y cambiar a ese usuario. Si alguien compromete aplicación, tendrá permisos limitados del usuario, no root completo.


### Usar .dockerignore

```
**/.git
**/.gitignore
**/.vscode
**/node_modules
**/*.log
**/.env
**/coverage
**/__pycache__
```

Note: Siempre usar .dockerignore para excluir archivos innecesarios. Reduce contexto de build, acelera transferencia al daemon, y evita incluir archivos sensibles (.env) o grandes (node_modules) en imagen.


### Especificar Versiones

```dockerfile
# ❌ Vago
FROM python
RUN pip install flask

# ✅ Específico
FROM python:3.11.7-slim
RUN pip install flask==3.0.0
```

Note: Especificar siempre versiones exactas de imagen base y dependencias. Evita sorpresas por cambios en nuevas versiones. 'latest' puede cambiar, rompiendo builds. Versiones específicas garantizan reproducibilidad.

---

## 6. Distribución


### Docker Hub: Login y Push

```bash
# Login en Docker Hub
$ docker login
Username: miusuario
Password: 
Login Succeeded

# Tag imagen con usuario
$ docker tag flask_app:v1 miusuario/flask_app:v1
$ docker tag flask_app:v1 miusuario/flask_app:latest

# Push a Docker Hub
$ docker push miusuario/flask_app:v1
$ docker push miusuario/flask_app:latest
```

Note: Para compartir imágenes públicamente, las subimos a Docker Hub. Necesitamos cuenta gratuita. Etiquetamos imagen con nuestro usuario de Docker Hub y hacemos push. Otros pueden descargarla con docker pull miusuario/flask_app.


### Registros Privados

* **Docker Registry**: Auto-hospedado open source.
* **AWS ECR**: Elastic Container Registry.
* **Google GCR**: Google Container Registry.
* **Azure ACR**: Azure Container Registry.
* **GitLab Registry**: Incluido con repositorios.

Note: Para imágenes privadas empresariales, usar registros privados. Docker Registry es solución open source auto-hospedada. Proveedores cloud ofrecen registros integrados con sus servicios. GitLab proporciona registro gratuito integrado con cada proyecto.


### Versionado Semántico

```bash
# Desarrollo
$ docker build -t myapp:dev .

# Versión específica
$ docker build -t myapp:1.2.3 .
$ docker tag myapp:1.2.3 myapp:1.2
$ docker tag myapp:1.2.3 myapp:1
$ docker tag myapp:1.2.3 myapp:latest

# Push todas las etiquetas
$ docker push myapp --all-tags
```

Note: Seguir versionado semántico (MAJOR.MINOR.PATCH). Mantener múltiples etiquetas: versión completa (1.2.3), minor (1.2), major (1), y latest. En producción, usar versiones específicas para reproducibilidad. latest solo para desarrollo o CI/CD.

---

## 7. Ciclo de Vida


### Flujo Desarrollo → Producción

1. Desarrollar código localmente.
2. Escribir Dockerfile.
3. Construir imagen: `docker build -t app:v1 .`
4. Probar localmente: `docker run app:v1`
5. Push a registro: `docker push app:v1`
6. Pull en producción: `docker pull app:v1`
7. Desplegar: `docker run app:v1`

Note: El ciclo de vida con Docker es limpio y predecible. Desarrollamos localmente, empaquetamos en imagen con Dockerfile, probamos localmente, subimos a registro, descargamos en producción, desplegamos. Lo que funciona en desarrollo funcionará idénticamente en producción: mismo entorno, mismas dependencias.


### Integración Continua

```yaml
# .gitlab-ci.yml
build:
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

deploy:
  script:
    - docker pull $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    - docker stop myapp || true
    - docker rm myapp || true
    - docker run -d --name myapp $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
```

Note: Docker se integra perfectamente con CI/CD. Cada commit dispara build de imagen, tests en contenedor, push a registro. En deployment, pull de imagen y despliegue automático. Esto garantiza que lo que funciona en tests funciona en producción.


### Actualización de Aplicación

```bash
# Construir nueva versión
$ docker build -t myapp:v2 .

# Push a registro
$ docker push myapp:v2

# En producción: pull nueva versión
$ docker pull myapp:v2

# Estrategia blue-green
$ docker run -d --name myapp-v2 -p 8080:80 myapp:v2
# Verificar que funciona
$ docker stop myapp-v1
$ docker rm myapp-v1
```

Note: Actualizar aplicaciones es simple con Docker. Construimos nueva versión de imagen, la subimos a registro, en producción descargamos nueva versión y la desplegamos. Podemos usar estrategias como blue-green deployment: levantar nueva versión en paralelo, verificar, y luego detener vieja versión. Rollback es igual de simple: volver a versión anterior.

---

## Resumen Módulo 5


### Creación de Imágenes

* Dockerfile automatiza construcción reproducible.
* Instrucciones principales: FROM, RUN, COPY, CMD.
* Cache de capas acelera builds.
* Documentado y versionable.

Note: Aprendimos a crear imágenes personalizadas con Dockerfile. Esto nos permite empaquetar nuestras aplicaciones con todas sus dependencias de forma reproducible. El Dockerfile es código que documenta exactamente cómo construir la imagen.


### Mejores Prácticas

* Imágenes base pequeñas (slim, alpine).
* Minimizar número de capas.
* Multi-stage builds para producción.
* Nunca ejecutar como root.
* Usar .dockerignore.
* Versiones específicas.

Note: Seguir mejores prácticas produce imágenes más pequeñas, rápidas, seguras y mantenibles. Estas prácticas son estándar en la industria y separan profesionales de aficionados.


### Distribución

* Docker Hub para imágenes públicas.
* Registros privados para empresas.
* Versionado semántico.
* Integración con CI/CD.

Note: Las imágenes se distribuyen via registros. Docker Hub para open source, registros privados para código propietario. El versionado adecuado es crucial. Docker se integra perfectamente en pipelines de CI/CD modernos.


### Ciclo de Vida Completo

1. Desarrollar aplicación.
2. Dockerizar con Dockerfile.
3. Probar localmente.
4. Versionar y distribuir.
5. Desplegar en cualquier entorno.

Note: El ciclo completo con Docker garantiza consistencia desde desarrollo hasta producción. "Funciona en mi máquina" ya no es un problema: si funciona en desarrollo, funcionará en producción porque es exactamente el mismo entorno en el contenedor.


### Fin del Curso de Docker

¡Felicidades! Has completado el curso completo.

**Habilidades adquiridas:**
* Contenedores e imágenes
* Volúmenes y redes
* Docker Compose
* Creación de imágenes con Dockerfile
* Mejores prácticas

Note: Felicidades por completar el curso completo de Docker. Ahora tienes habilidades fundamentales para trabajar profesionalmente con contenedores: crear, gestionar, conectar, persistir datos, orquestar con Compose, y construir imágenes personalizadas siguiendo mejores prácticas. Estas habilidades son altamente demandadas en la industria.


### Próximos Pasos

* Practicar dockerizando vuestras aplicaciones.
* Explorar Docker Swarm o Kubernetes.
* Aprender sobre Docker en producción.
* Contribuir a proyectos open source con Docker.

Note: Continuad aprendiendo y practicando. Dockerizad vuestras propias aplicaciones, experimentad con diferentes arquitecturas. Explorad orquestadores como Kubernetes para gestionar contenedores a escala. Aprended sobre monitoring, logging y seguridad en producción. Y contribuid a la comunidad open source que hace Docker posible.


### ¡Gracias por participar!

¿Preguntas finales?

Note: Muchas gracias por seguir este curso completo de Docker. Los contenedores son fundamentales en desarrollo de software moderno y las habilidades que habéis adquirido os servirán durante toda vuestra carrera. Continuad experimentando, construid proyectos reales, y no dejéis de aprender. ¡Éxito en vuestro camino con Docker y la tecnología de contenedores!
