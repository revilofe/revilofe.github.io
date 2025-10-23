# Curso Docker - Módulo 2

## Imágenes Docker

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice Módulo 2

* Registros de imágenes: Docker Hub
* Gestión de imágenes
* Organización de imágenes por capas
* Creación de contenedores desde imágenes
* Ejemplo práctico: MediaWiki

---

## 1. Docker Hub y Registros


### ¿Qué es Docker Hub?

* Registro público de imágenes Docker.
* Repositorio central de imágenes oficiales.
* Más de 100,000 imágenes públicas disponibles.
* Permite crear repositorios propios.

Note: Docker Hub es el registro oficial y público de imágenes Docker. Es como GitHub pero para imágenes de contenedores. Contiene imágenes oficiales verificadas de aplicaciones populares (Ubuntu, MySQL, nginx, etc.) y millones de imágenes públicas creadas por la comunidad. Es gratuito para repositorios públicos y ofrece planes de pago para repositorios privados. Cualquiera puede crear una cuenta y subir sus propias imágenes para compartirlas con el mundo o usarlas en sus proyectos.


### Componentes del Sistema Docker

* **Imagen**: Plantilla de solo lectura.
* **Contenedor**: Instancia ejecutable de una imagen.
* **Registro**: Almacén de imágenes.
* **Docker Engine**: Motor que gestiona todo.

Note: Recordemos los componentes principales del ecosistema Docker. Las imágenes son plantillas inmutables que contienen el sistema de archivos y configuración de una aplicación. Los contenedores son instancias en ejecución creadas a partir de imágenes. El registro es donde se almacenan y distribuyen las imágenes, siendo Docker Hub el más popular. Y el Docker Engine es el daemon que coordina todo: descarga imágenes, crea contenedores, gestiona redes y volúmenes. Todos estos componentes trabajan juntos para proporcionar la plataforma Docker completa.


### Nomenclatura de Imágenes

* Formato: `usuario/nombre:etiqueta`
* **usuario**: Creador de la imagen (opcional para oficiales).
* **nombre**: Nombre significativo de la imagen.
* **etiqueta**: Versión o variante (default: `latest`).

Note: Entender la nomenclatura de imágenes es crucial. Una imagen completa se identifica con tres partes: usuario/nombre:etiqueta. El usuario es quien creó la imagen; las imágenes oficiales de Docker Hub no tienen usuario, solo nombre. El nombre describe qué contiene la imagen. La etiqueta especifica la versión o variante específica. Si no indicamos etiqueta, Docker usa 'latest' por defecto. Por ejemplo: ubuntu:20.04, mysql:8.0, josedom24/miapp:v1. Esta nomenclatura permite versionar y organizar imágenes de forma clara.


### Imágenes Oficiales

* Sin nombre de usuario en Docker Hub.
* Verificadas y mantenidas por Docker Inc.
* Actualizaciones regulares de seguridad.
* Ejemplos: `ubuntu`, `nginx`, `mysql`, `python`.

Note: Las imágenes oficiales son especiales en Docker Hub. No llevan prefijo de usuario, solo el nombre de la aplicación. Son creadas y mantenidas por Docker Inc. o por los equipos oficiales de cada proyecto. Pasan por un proceso de revisión riguroso, reciben actualizaciones de seguridad regulares y siguen mejores prácticas. Son la opción más confiable para aplicaciones populares. Por ejemplo, 'nginx' es oficial, mientras que 'usuario/nginx' sería una imagen comunitaria. Siempre que sea posible, preferir imágenes oficiales por su calidad y seguridad.


### Etiquetas de Versión

* `latest`: Última versión disponible.
* Versiones específicas: `2.4`, `8.0.25`, `20.04`.
* Variantes: `alpine`, `slim`, `fpm`.
* Combinaciones: `python:3.9-alpine`.

Note: Las etiquetas permiten especificar exactamente qué versión queremos. 'latest' apunta siempre a la última versión, pero puede cambiar con el tiempo, por lo que no es recomendable para producción. Las versiones específicas (como mysql:8.0 o ubuntu:20.04) son más estables y predecibles. Las variantes indican diferentes configuraciones: 'alpine' son versiones minimalistas basadas en Alpine Linux, 'slim' son versiones reducidas, 'fpm' incluyen PHP-FPM, etc. Podemos combinar versión y variante como python:3.9-alpine para precisión máxima.


### Buscando Imágenes en Docker Hub

* Desde la web: https://hub.docker.com
* Desde terminal: `docker search nombre`
* Filtros por estrellas, oficiales, automatizadas.
* Leer siempre la documentación de la imagen.

Note: Hay dos formas principales de buscar imágenes. La más completa es usar la web de Docker Hub donde podemos ver descripciones detalladas, documentación, versiones disponibles y estadísticas. Desde terminal usamos 'docker search' seguido del término de búsqueda, pero da información limitada. Podemos filtrar por número de estrellas, si son oficiales, o si tienen build automático. Es crucial leer la documentación de cada imagen en Docker Hub antes de usarla para entender qué variables de entorno acepta, qué puertos expone, dónde almacena datos, etc.

---

## 2. Gestión de Imágenes


### Comandos Principales

* `docker images`: Listar imágenes locales.
* `docker pull`: Descargar imagen.
* `docker rmi`: Eliminar imagen.
* `docker search`: Buscar en Docker Hub.
* `docker inspect`: Información detallada.

Note: Estos son los comandos esenciales para gestionar imágenes. 'docker images' muestra todas las imágenes que tenemos descargadas localmente con su tamaño, ID y fecha de creación. 'docker pull' descarga una imagen específica de Docker Hub sin crear un contenedor. 'docker rmi' elimina imágenes locales (solo si no hay contenedores usándolas). 'docker search' busca imágenes en Docker Hub desde terminal. 'docker inspect' muestra información técnica detallada de una imagen en formato JSON. Dominar estos comandos es fundamental para trabajar eficientemente con Docker.


### Descargando Imágenes

```bash
$ docker pull ubuntu:20.04
20.04: Pulling from library/ubuntu
d5fd17ec1767: Pull complete
Digest: sha256:47f14534bda...
Status: Downloaded newer image for ubuntu:20.04
docker.io/library/ubuntu:20.04
```

Note: El comando 'docker pull' descarga una imagen sin ejecutarla. Es útil cuando queremos preparar imágenes con anticipación o asegurarnos de tener la última versión. Docker muestra el progreso de descarga de cada capa. Cada línea con un hash representa una capa de la imagen descargándose. El Digest es un hash SHA256 que identifica unívocamente esta versión exacta de la imagen. Una vez descargada, la imagen queda en nuestro registro local lista para crear contenedores instantáneamente sin necesidad de descargarla de nuevo.


### Listando Imágenes Locales

```bash
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
ubuntu        20.04     d5fd17ec1767   2 weeks ago   72.8MB
ubuntu        latest    f63181f19b2f   2 weeks ago   72.8MB
nginx         alpine    51696c87e77e   3 weeks ago   23.4MB
mysql         8.0       ecac195d15af   4 weeks ago   516MB
```

Note: El comando 'docker images' muestra nuestro registro local de imágenes. Para cada imagen vemos el nombre del repositorio, la etiqueta, un ID único (hash corto), cuándo fue construida originalmente y su tamaño en disco. Notemos que podemos tener múltiples versiones de la misma imagen (ubuntu con tags 20.04 y latest). El tamaño mostrado es el tamaño descomprimido; las imágenes comparten capas, así que el espacio real en disco suele ser menor que la suma de todos los tamaños.


### Eliminando Imágenes

```bash
$ docker rmi ubuntu:20.04
Untagged: ubuntu:20.04
Untagged: ubuntu@sha256:47f14534bda...
Deleted: sha256:d5fd17ec1767...
Deleted: sha256:4693057ce236...
```

Note: Para eliminar una imagen usamos 'docker rmi' seguido del nombre:tag o el IMAGE ID. Docker primero quita las etiquetas (tags) asociadas a la imagen, luego elimina las capas que no sean compartidas con otras imágenes. Si intentamos eliminar una imagen que está siendo usada por algún contenedor (aunque esté parado), Docker nos dará un error. Debemos primero eliminar los contenedores con 'docker rm'. Para forzar la eliminación podemos usar 'docker rmi -f', pero no es recomendable.


### Información Detallada de Imágenes

```bash
$ docker inspect ubuntu:20.04
[{
    "Id": "sha256:d5fd17ec1767...",
    "Created": "2024-01-15T00:20:47.973Z",
    "Architecture": "amd64",
    "Os": "linux",
    "Size": 72787459,
    "RootFS": {
        "Type": "layers",
        "Layers": [...]
    }
}]
```

Note: El comando 'docker inspect' devuelve información completa sobre una imagen en formato JSON. Incluye el ID completo de la imagen, cuándo fue creada, para qué arquitectura está construida (amd64, arm64, etc.), el sistema operativo, tamaño exacto, las capas que componen el sistema de archivos raíz, variables de entorno predefinidas, puertos expuestos, el comando por defecto que ejecuta, y mucho más. Esta información es invaluable cuando necesitamos entender exactamente cómo está construida una imagen o para debugging.


### Etiquetando Imágenes

```bash
$ docker tag ubuntu:20.04 miubuntu:v1
$ docker images
REPOSITORY    TAG       IMAGE ID
ubuntu        20.04     d5fd17ec1767
miubuntu      v1        d5fd17ec1767
```

Note: Podemos crear nuevas etiquetas para imágenes existentes con 'docker tag'. Esto no crea una copia de la imagen, solo añade un nuevo nombre/tag que apunta a la misma imagen (notemos que ambas comparten el mismo IMAGE ID). Esto es útil para versionado local, renombrar imágenes antes de subirlas a un registro, o crear alias. Por ejemplo, podríamos etiquetar una imagen como 'miapp:produccion' para claridad. Las etiquetas son punteros ligeros; podemos tener múltiples etiquetas apuntando a la misma imagen sin ocupar espacio adicional.


### Limpieza de Imágenes

```bash
$ docker image prune
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y

$ docker image prune -a
WARNING! This will remove all images without containers.
```

Note: Con el tiempo acumulamos imágenes que no usamos, ocupando espacio. 'docker image prune' elimina imágenes "colgadas" (dangling) que son capas huérfanas sin etiqueta, generalmente resultantes de reconstrucciones. Con '-a' elimina todas las imágenes que no están siendo usadas por ningún contenedor existente (útil para limpieza profunda). Con '--filter' podemos ser más selectivos, por ejemplo eliminando solo imágenes creadas hace más de 24 horas. Es buena práctica ejecutar prune periódicamente para liberar espacio en disco.

---

## 3. Organización por Capas


### Arquitectura en Capas

* Las imágenes están compuestas de capas apiladas.
* Cada capa representa un cambio en el sistema de archivos.
* Las capas son de solo lectura.
* Se reutilizan entre imágenes similares.

Note: Las imágenes Docker usan un sistema de archivos en capas, que es fundamental para su eficiencia. Cada imagen está compuesta de múltiples capas apiladas unas sobre otras. Cada capa representa un conjunto de cambios: archivos añadidos, modificados o eliminados. Las capas son inmutables (solo lectura), por lo que pueden compartirse de forma segura entre diferentes imágenes. Si dos imágenes comparten capas base (por ejemplo, ambas basadas en Ubuntu), esas capas se almacenan una sola vez. Esto ahorra espacio en disco y acelera la descarga de imágenes.


### Ventajas del Sistema de Capas

* Ahorro de espacio en disco.
* Descargas más rápidas (capas compartidas).
* Construcción incremental eficiente.
* Cache entre builds de imágenes.

Note: El sistema de capas proporciona múltiples beneficios. Ahorra espacio porque capas comunes se almacenan una sola vez. Por ejemplo, si tenemos 10 imágenes basadas en Ubuntu, la capa base de Ubuntu se guarda una sola vez. Las descargas son más rápidas porque Docker solo descarga las capas que no tenemos. La construcción de imágenes es incremental: si modificamos algo, solo se reconstruyen las capas afectadas y las posteriores. El sistema de cache hace que reconstruir imágenes sea casi instantáneo si no hay cambios.


### Visualizando Capas

```bash
$ docker history ubuntu:20.04
IMAGE          CREATED       CREATED BY                      SIZE
d5fd17ec1767   2 weeks ago   /bin/sh -c #(nop)  CMD ["/b…   0B
<missing>      2 weeks ago   /bin/sh -c mkdir -p /run/sy…   0B
<missing>      2 weeks ago   /bin/sh -c set -xe  && echo…   25.9MB
<missing>      2 weeks ago   /bin/sh -c #(nop) ADD file:…   47.0MB
```

Note: El comando 'docker history' muestra las capas de una imagen en orden cronológico inverso (de más reciente a más antigua). Para cada capa vemos cuándo fue creada, el comando que la generó, y cuánto espacio ocupa. Las capas con 0B típicamente son metadatos (CMD, ENV, EXPOSE). Las capas marcadas como '<missing>' son capas compartidas que fueron creadas en otro lugar. Esto nos ayuda a entender cómo se construyó la imagen y dónde está el mayor peso. Es útil para optimizar imágenes identificando qué comandos generan las capas más grandes.


### Capas en Contenedores

* Contenedor = Imagen + Capa de Lectura-Escritura.
* Cambios se escriben en la capa superior.
* La imagen base permanece inmutable.
* Al eliminar el contenedor, se pierde la capa R/W.

Note: Cuando creamos un contenedor desde una imagen, Docker añade una capa delgada de lectura-escritura encima de todas las capas de solo lectura de la imagen. Todos los cambios que hagamos en el contenedor (crear archivos, instalar paquetes, modificar configuraciones) se escriben en esta capa superior. Las capas de la imagen original permanecen intactas y compartidas. Esto significa que múltiples contenedores de la misma imagen comparten las capas base pero cada uno tiene su propia capa de cambios. Al eliminar un contenedor, perdemos su capa R/W pero la imagen persiste.


### Copy-on-Write (CoW)

* Sistema de archivos eficiente.
* Modificación de archivo: se copia a capa superior.
* El original permanece en capa inferior.
* Invisible para el usuario, transparente.

Note: Docker usa una estrategia Copy-on-Write para eficiencia. Cuando un contenedor necesita modificar un archivo que existe en una capa inferior (de la imagen), Docker primero copia ese archivo a la capa de lectura-escritura del contenedor y luego lo modifica ahí. El archivo original en la capa de la imagen permanece intacto. Desde dentro del contenedor, el usuario ve el archivo modificado porque la capa superior tiene prioridad. Este mecanismo es transparente y permite que múltiples contenedores compartan de forma segura las mismas capas base mientras mantienen sus propios cambios.


### Tamaños Virtuales vs Reales

```bash
$ docker ps -s
CONTAINER ID   IMAGE    SIZE
a2d1ce6990d8   ubuntu   52B (virtual 72.9MB)
```

Note: Cuando vemos el tamaño de un contenedor con 'docker ps -s', vemos dos valores: el tamaño real y el virtual. El tamaño real (52B en este ejemplo) es el espacio que ocupa la capa de lectura-escritura del contenedor, es decir, los cambios que hemos hecho. El tamaño virtual (72.9MB) es el tamaño total incluyendo todas las capas de la imagen base. El tamaño virtual es compartido entre todos los contenedores de la misma imagen, por lo que crear muchos contenedores de la misma imagen no multiplica este espacio.


### Ejemplo de Compartición de Capas

```bash
$ docker run -d --name web1 nginx
$ docker run -d --name web2 nginx
$ docker run -d --name web3 nginx
# Tres contenedores, pero las capas de nginx se
# almacenan solo una vez
```

Note: Este ejemplo ilustra la eficiencia del sistema de capas. Creamos tres contenedores desde la imagen nginx. Aunque tenemos tres contenedores ejecutándose, las capas de la imagen nginx se almacenan una sola vez en disco. Cada contenedor solo añade su pequeña capa de lectura-escritura. Si la imagen nginx ocupa 140MB, tres contenedores no ocupan 420MB, sino 140MB más el espacio de las tres capas R/W (típicamente muy pequeñas si no hacemos cambios significativos). Esto hace que Docker sea extremadamente eficiente en uso de recursos.


### Inspeccionando Capas

```bash
$ docker inspect ubuntu:20.04
...
"RootFS": {
    "Type": "layers",
    "Layers": [
        "sha256:9f32931c9d28...",
        "sha256:dbf2c0f42a39...",
        "sha256:02473afd360b..."
    ]
}
```

Note: El comando 'docker inspect' muestra las capas que componen el sistema de archivos raíz de una imagen en la sección RootFS. Cada capa se identifica por un hash SHA256 único. Podemos ver cuántas capas tiene una imagen y sus identificadores. Esto es útil para entender la estructura de la imagen y para verificación de integridad. Si dos imágenes comparten capas, veremos los mismos hashes SHA256 en ambas, confirmando que están reutilizando esas capas.

---

## 4. Creación de Contenedores desde Imágenes


### Tipos de Imágenes Comunes

* **Sistemas Operativos**: ubuntu, debian, centos, alpine.
* **Servicios**: nginx, apache, mysql, redis, postgresql.
* **Aplicaciones**: wordpress, nextcloud, mediawiki.

Note: En Docker Hub encontramos tres categorías principales de imágenes. Primero, imágenes de sistemas operativos base como Ubuntu, Debian, CentOS o Alpine Linux. Estas se usan como punto de partida para crear nuestras propias imágenes. Segundo, imágenes de servicios individuales como servidores web (nginx, Apache), bases de datos (MySQL, PostgreSQL, Redis), o servicios de mensajería. Tercero, aplicaciones completas listas para usar como WordPress, Nextcloud o MediaWiki. Cada categoría tiene casos de uso diferentes y todas son valiosas en el ecosistema Docker.


### Comando por Defecto

* Todas las imágenes tienen un comando predefinido.
* Se ejecuta al crear el contenedor.
* Puede sobrescribirse especificando otro comando.
* Ejemplo: `ubuntu` ejecuta `bash` por defecto.

Note: Cada imagen Docker tiene definido un comando que se ejecuta por defecto cuando creamos un contenedor. Por ejemplo, la imagen ubuntu ejecuta bash, mientras que nginx ejecuta el servidor web nginx. Este comando está definido en la imagen con las instrucciones CMD o ENTRYPOINT del Dockerfile. Podemos sobrescribir el comando por defecto especificándolo al final de 'docker run'. Por ejemplo, 'docker run ubuntu' ejecuta bash, pero 'docker run ubuntu echo hola' ejecuta echo en su lugar. Entender esto es clave para usar imágenes correctamente.


### Imágenes de Sistemas Operativos

```bash
$ docker run -it ubuntu bash
root@container:/#

$ docker run -it centos bash
[root@container /]#

$ docker run -it alpine sh
/ #
```

Note: Las imágenes de sistemas operativos proporcionan un entorno Linux mínimo. Ubuntu y CentOS incluyen bash y herramientas GNU estándar, siendo más pesadas pero familiares. Alpine Linux es minimalista (solo 5MB), usa el shell sh y herramientas BusyBox, siendo perfecta para contenedores de producción por su tamaño reducido y menor superficie de ataque. Podemos usar estas imágenes base para experimentar con diferentes distribuciones, instalar software, o como base para construir nuestras propias imágenes personalizadas. Cada una tiene sus ventajas según el caso de uso.


### Imágenes de Servicios I

* Servicios preconfigurados y listos para usar.
* Siguen mejores prácticas de contenedorización.
* Documentación detallada en Docker Hub.
* Ejemplos: MySQL, PostgreSQL, MongoDB, Redis.

Note: Las imágenes de servicios contienen aplicaciones servidor preconfiguradas y optimizadas para ejecutarse en contenedores. Los mantenedores de estas imágenes han hecho el trabajo pesado: instalación, configuración, optimización de seguridad, y seguimiento de mejores prácticas. Por ejemplo, la imagen oficial de MySQL viene con scripts de inicialización que configuran la base de datos automáticamente usando variables de entorno. Siempre debemos leer la documentación en Docker Hub de cada imagen para entender cómo configurarla correctamente y qué puertos/volúmenes usa.


### Imágenes de Servicios II: Ejemplo MySQL

```bash
$ docker run -d \
  --name mysql-server \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=mydb \
  -p 3306:3306 \
  mysql:8.0
```

Note: Este ejemplo muestra cómo desplegar MySQL usando variables de entorno para configuración inicial. MYSQL_ROOT_PASSWORD establece la contraseña del usuario root (obligatoria). MYSQL_DATABASE crea automáticamente una base de datos al iniciar. Mapeamos el puerto 3306 para acceso externo. La imagen se encarga de todo lo demás: instalar MySQL, configurarlo, inicializar la base de datos y arrancar el servidor. En minutos tenemos un servidor MySQL funcional. Esto demuestra el poder de Docker: simplifica despliegues complejos a un solo comando.


### Aplicaciones Completas

* Incluyen múltiples componentes integrados.
* Requieren configuración adicional (base de datos).
* Variables de entorno para personalización.
* Ejemplo: WordPress, Nextcloud, GitLab.

Note: Las imágenes de aplicaciones completas contienen aplicaciones web funcionales. Por ejemplo, WordPress incluye Apache y PHP preconfigurados. Sin embargo, estas aplicaciones suelen necesitar componentes adicionales como bases de datos que debemos proporcionar por separado. Usamos variables de entorno para configurar la conexión a la base de datos y otras opciones. Más adelante, con Docker Compose, aprenderemos a orquestar múltiples contenedores (aplicación + base de datos) fácilmente. Estas imágenes son perfectas para pruebas rápidas o despliegues sencillos.


### Comando vs Entrypoint

* **CMD**: Comando por defecto, puede sobrescribirse.
* **ENTRYPOINT**: Comando fijo, argumentos adicionales.
* Combinados: ENTRYPOINT + CMD como args por defecto.
* Afecta cómo pasamos comandos al contenedor.

Note: CMD y ENTRYPOINT son instrucciones en Dockerfiles que definen qué se ejecuta en el contenedor. CMD define el comando por defecto que puede sobrescribirse completamente al especificar otro comando en 'docker run'. ENTRYPOINT define un comando fijo; cualquier cosa que pasemos en 'docker run' se añade como argumentos a ese comando. Muchas imágenes usan ambos: ENTRYPOINT para el ejecutable principal y CMD para argumentos por defecto. Por ejemplo, una imagen podría tener ENTRYPOINT ["mysql"] y CMD ["-h", "localhost"], permitiéndonos sobrescribir los argumentos pero manteniendo mysql como comando base.


### Verificando Comando por Defecto

```bash
$ docker inspect ubuntu:latest
...
"Cmd": [
    "/bin/bash"
],
...
```

Note: Podemos ver qué comando ejecutará una imagen por defecto usando 'docker inspect'. En la sección Cmd o Entrypoint veremos el comando definido. Para Ubuntu es /bin/bash. Para nginx es el script que inicia nginx en foreground. Para MySQL es el script de inicialización y arranque del servidor. Conocer el comando por defecto nos ayuda a entender cómo usar correctamente la imagen y si necesitamos sobrescribirlo para nuestro caso de uso particular.


### Listando Puertos Expuestos

```bash
$ docker inspect nginx
...
"ExposedPorts": {
    "80/tcp": {}
},
...
```

Note: Las imágenes declaran qué puertos usan con la instrucción EXPOSE en el Dockerfile. Esto es informativo; el puerto no se publica automáticamente. Podemos ver los puertos expuestos con 'docker inspect' en la sección ExposedPorts. Por ejemplo, nginx expone el puerto 80 (HTTP) y a veces el 443 (HTTPS). MySQL expone el 3306. Esta información nos indica qué puertos debemos mapear con '-p' al crear el contenedor para acceder al servicio desde fuera. Es parte de la documentación implícita de la imagen.

---

## 5. Ejemplo: MediaWiki


### ¿Qué es MediaWiki?

* Software wiki usado por Wikipedia.
* Aplicación web escrita en PHP.
* Requiere servidor web y base de datos.
* Imagen disponible en Docker Hub: `mediawiki`.

Note: MediaWiki es el motor wiki que impulsa Wikipedia. Es una aplicación web potente y completa escrita en PHP que permite crear y gestionar wikis. Requiere un servidor web (típicamente Apache con PHP) y una base de datos (MySQL o MariaDB). La imagen oficial en Docker Hub incluye Apache y PHP preconfigurados, simplificando enormemente el despliegue. Usaremos esta imagen para demostrar conceptos importantes: versionado con etiquetas, despliegue de aplicaciones complejas, y buenas prácticas con Docker.


### Etiquetas Disponibles de MediaWiki

* `latest`: Última versión estable (1.41.x).
* `1.41.0`, `1.40.2`, `1.39.6`: Versiones específicas.
* `1.41.0-fpm`: Con PHP-FPM en lugar de Apache.
* `1.41.0-fpm-alpine`: Basada en Alpine Linux.

Note: La imagen mediawiki demuestra bien el uso de etiquetas para versiones y variantes. La etiqueta 'latest' apunta a la última versión estable. Podemos especificar versiones exactas como 1.41.0. Las variantes '-fpm' incluyen PHP-FPM para usar con nginx en lugar de Apache integrado. Las variantes '-alpine' están basadas en Alpine Linux, siendo mucho más pequeñas. Podemos combinar versión y variante como '1.41.0-fpm-alpine'. Esto nos da control total sobre exactamente qué versión y configuración desplegamos.


### Desplegando MediaWiki Última Versión

```bash
$ docker run -d \
  --name mediawiki1 \
  -p 8080:80 \
  mediawiki:latest

$ docker ps
CONTAINER ID   IMAGE             PORTS
f3a2bc5d8e1a   mediawiki:latest  0.0.0.0:8080->80/tcp
```

Note: Desplegamos MediaWiki con un comando simple. La etiqueta 'latest' descarga la última versión disponible. Mapeamos el puerto 80 del contenedor (donde Apache escucha) al puerto 8080 de nuestro host. En pocos segundos tenemos un servidor MediaWiki ejecutándose. Podemos acceder en http://localhost:8080 y veremos el asistente de configuración de MediaWiki. Este ejemplo muestra lo rápido que es probar aplicaciones complejas con Docker, sin necesidad de instalar dependencias o configurar servicios en nuestro host.


### Accediendo a MediaWiki

* Abrir navegador: `http://localhost:8080`
* Asistente de configuración se muestra.
* Requiere configuración de base de datos.
* Por ahora, solo verificamos que funciona.

Note: Al acceder a http://localhost:8080 vemos el asistente de instalación de MediaWiki. Nos pide configurar la base de datos y otros parámetros. Para un despliegue completo necesitaríamos un contenedor MySQL separado y configurar la conexión. Por ahora, simplemente verificamos que el contenedor funciona y sirve la aplicación correctamente. En módulos posteriores aprenderemos a usar Docker Compose para orquestar MediaWiki + MySQL fácilmente. Este ejemplo demuestra tanto las posibilidades como las limitaciones de contenedores individuales.


### Desplegando Versión Específica

```bash
$ docker run -d \
  --name mediawiki2 \
  -p 8081:80 \
  mediawiki:1.40.2

$ docker run -d \
  --name mediawiki3 \
  -p 8082:80 \
  mediawiki:1.39.6
```

Note: Aquí desplegamos diferentes versiones de MediaWiki simultáneamente usando puertos distintos. El contenedor mediawiki2 ejecuta la versión 1.40.2 en el puerto 8081. El contenedor mediawiki3 ejecuta la versión 1.39.6 en el puerto 8082. Esto es útil para probar compatibilidad, migrar entre versiones, o simplemente experimentar con diferentes versiones sin afectar otros despliegues. Cada contenedor es completamente independiente. Esto demuestra la flexibilidad de Docker para gestionar múltiples versiones de la misma aplicación.


### Verificando Versiones Instaladas

* Acceder a `http://localhost:8081` → MediaWiki 1.40.2
* Acceder a `http://localhost:8082` → MediaWiki 1.39.6
* Cada contenedor ejecuta su versión independientemente.

Note: Podemos verificar que cada contenedor ejecuta su versión correcta accediendo a los diferentes puertos. En localhost:8081 vemos MediaWiki 1.40.2, en localhost:8082 vemos la 1.39.6. El footer de la página o el asistente de instalación muestran la versión. Cada contenedor es un entorno aislado con su versión específica de MediaWiki, PHP, Apache y todas las dependencias. Esto sería extremadamente difícil de lograr instalando directamente en el host, donde solo podríamos tener una versión a la vez.


### Optimización de Descargas

```bash
# Primera imagen: descarga todas las capas
$ docker pull mediawiki:1.41.0
1.41.0: Pulling from library/mediawiki
a1d0c7532777: Pull complete
b8f2fcde5c0d: Pull complete
...

# Segunda imagen: solo descarga capas diferentes
$ docker pull mediawiki:1.40.2
1.40.2: Pulling from library/mediawiki
a1d0c7532777: Already exists
b8f2fcde5c0d: Already exists
c3d15e4a2345: Pull complete
```

Note: Este ejemplo muestra la eficiencia del sistema de capas. Al descargar mediawiki:1.41.0, Docker descarga todas sus capas. Al descargar luego mediawiki:1.40.2, vemos mensajes "Already exists" para capas que ya teníamos de la versión anterior. Solo se descargan las capas que difieren entre versiones. Esto ahorra tiempo de descarga y espacio en disco. Si las dos versiones comparten la mayoría de capas (misma imagen base, mismas dependencias), solo se descarga la pequeña diferencia. Esto hace práctico tener múltiples versiones de imágenes.


### Limpiando Contenedores

```bash
$ docker stop mediawiki1 mediawiki2 mediawiki3
$ docker rm mediawiki1 mediawiki2 mediawiki3

# O en un solo paso con -f
$ docker rm -f mediawiki1 mediawiki2 mediawiki3
```

Note: Después de experimentar, limpiamos los contenedores. 'docker stop' detiene los contenedores gracefully. 'docker rm' los elimina del sistema. Podemos especificar múltiples nombres separados por espacios. Alternativamente, 'docker rm -f' detiene y elimina en un solo paso. Recordemos que eliminar contenedores no elimina las imágenes, que permanecen disponibles para crear nuevos contenedores. Si queremos liberar espacio en disco completamente, también deberíamos ejecutar 'docker rmi' para eliminar las imágenes que no necesitamos.

---

## Resumen Módulo 2


### Conceptos Clave Aprendidos

* Docker Hub como registro central de imágenes.
* Nomenclatura: usuario/nombre:etiqueta.
* Gestión de imágenes: pull, rmi, inspect.
* Sistema de capas y eficiencia de almacenamiento.
* Despliegue de aplicaciones con versiones específicas.

Note: En este módulo profundizamos en las imágenes Docker. Aprendimos sobre Docker Hub, el registro público donde se almacenan y comparten imágenes. Entendimos la nomenclatura de imágenes y la importancia de las etiquetas para versionar. Dominamos los comandos para gestionar imágenes localmente. Comprendimos el sistema de capas que hace Docker tan eficiente en espacio y tiempo. Y practicamos desplegando aplicaciones reales como MediaWiki en diferentes versiones. Este conocimiento es fundamental para trabajar profesionalmente con Docker.


### Sistema de Capas: Beneficios

* Ahorro de espacio en disco.
* Descargas incrementales más rápidas.
* Reutilización entre imágenes similares.
* Contenedores ligeros compartiendo capas base.

Note: El sistema de capas es una de las características más brillantes de Docker. Las capas se comparten entre imágenes que tienen base común, ahorrando espacio significativo. Las descargas son incrementales: solo se descargan capas nuevas. Múltiples contenedores de la misma imagen comparten todas las capas de solo lectura, ocupando solo el espacio de sus pequeñas capas de cambios individuales. Esto hace que Docker sea extremadamente eficiente en recursos, permitiendo ejecutar muchos contenedores sin agotar disco o memoria. Es lo que hace práctico tener cientos de contenedores en un solo host.


### Mejores Prácticas con Imágenes

* Preferir imágenes oficiales por seguridad.
* Usar etiquetas específicas en producción, no `latest`.
* Leer documentación de la imagen en Docker Hub.
* Limpiar imágenes no usadas periódicamente.
* Entender qué puertos y volúmenes usa cada imagen.

Note: Sigamos mejores prácticas al trabajar con imágenes. Usar imágenes oficiales siempre que sea posible por su calidad y seguridad. En producción, especificar siempre versiones exactas en lugar de 'latest' para evitar sorpresas en actualizaciones. Leer la documentación completa en Docker Hub antes de usar una imagen nueva. Ejecutar 'docker image prune' periódicamente para liberar espacio. Y entender bien los requisitos de cada imagen: qué variables de entorno necesita, qué puertos expone, dónde almacena datos persistentes. Estas prácticas previenen problemas y mejoran la mantenibilidad.


### Comandos Clave del Módulo

* `docker pull`: Descargar imágenes.
* `docker images`: Listar imágenes locales.
* `docker rmi`: Eliminar imágenes.
* `docker inspect`: Ver detalles de imagen.
* `docker history`: Ver capas de imagen.

Note: Estos son los comandos fundamentales para trabajar con imágenes que hemos cubierto. 'docker pull' descarga imágenes de Docker Hub. 'docker images' lista nuestro repositorio local. 'docker rmi' elimina imágenes que no necesitamos. 'docker inspect' muestra información técnica detallada. 'docker history' revela las capas y cómo se construyó la imagen. Dominar estos comandos es esencial para gestionar eficientemente nuestras imágenes Docker y entender el sistema de capas subyacente.


### Próximo Módulo

**Módulo 3: Almacenamiento y Redes**

* Volúmenes Docker y bind mounts.
* Persistencia de datos en contenedores.
* Redes Docker y comunicación entre contenedores.
* Ejemplos prácticos multi-contenedor.

Note: En el próximo módulo abordaremos dos temas cruciales: almacenamiento y redes. Aprenderemos sobre volúmenes Docker y bind mounts para persistir datos más allá del ciclo de vida de los contenedores. Estudiaremos las redes Docker que permiten que contenedores se comuniquen entre sí de forma segura. Practicaremos con ejemplos multi-contenedor como WordPress con MySQL, donde una aplicación en un contenedor se conecta a una base de datos en otro contenedor. Este conocimiento es fundamental para despliegues reales de producción.


### ¡Gracias!

¿Preguntas sobre el Módulo 2?

Note: Esto concluye el segundo módulo del curso de Docker sobre imágenes. Hemos cubierto conceptos fundamentales que usaréis constantemente en vuestro trabajo con Docker. El sistema de capas puede parecer complejo al principio, pero es lo que hace Docker tan eficiente y potente. Os animo a experimentar descargando diferentes imágenes, explorando Docker Hub, y probando distintas versiones de aplicaciones. En el siguiente módulo construiremos sobre este conocimiento para crear sistemas más complejos con múltiples contenedores comunicándose entre sí.
