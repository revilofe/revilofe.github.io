# Curso Docker - Módulo 1

## Introducción a Contenedores Docker

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice Módulo 1

* Instalación de Docker
* El "Hola Mundo" de Docker  
* Ejecución simple de contenedores
* Ejecutando contenedores interactivos
* Creando contenedores demonio
* Contenedores con servidor web
* Configuración con variables de entorno

---

## 1. Instalación de Docker


### ¿Qué es Docker?

* Plataforma de contenedores ligeros.
* Permite empaquetar aplicaciones con sus dependencias.
* Facilita el despliegue en cualquier entorno.
* Aislamiento sin la sobrecarga de una VM completa.

Note: Docker es una plataforma que permite desarrollar, enviar y ejecutar aplicaciones dentro de contenedores. Los contenedores son entornos ligeros y portables que incluyen todo lo necesario para ejecutar una aplicación: código, runtime, herramientas del sistema, bibliotecas y configuraciones. A diferencia de las máquinas virtuales tradicionales, los contenedores comparten el kernel del sistema operativo host, lo que los hace mucho más ligeros y rápidos de arrancar.


### Versiones de Docker

* **Docker Community Edition (CE)**: Versión gratuita.
* **Docker Enterprise Edition (EE)**: Versión comercial.
* Soportado en Linux, Windows y macOS.
* Instalación desde repositorios oficiales recomendada.

Note: Existen dos versiones principales de Docker. Docker CE es la versión de código abierto y gratuita, ideal para desarrolladores y pequeños equipos. Docker EE es la versión empresarial con soporte comercial, funcionalidades de seguridad avanzadas y certificación. Para este curso trabajaremos con Docker CE. Docker puede instalarse en múltiples sistemas operativos, aunque funciona de forma nativa en Linux. En Windows y macOS se ejecuta dentro de una máquina virtual ligera.


### Instalación en Debian/Ubuntu

* Actualizar repositorios: `apt-get update`
* Instalar paquetes necesarios
* Añadir repositorio oficial de Docker
* Instalar docker-ce
* Verificar instalación: `docker --version`

Note: Para instalar Docker en sistemas Debian o Ubuntu, primero actualizamos los repositorios del sistema. Luego instalamos paquetes que permiten usar repositorios HTTPS. Agregamos la clave GPG oficial de Docker y añadimos el repositorio de Docker a las fuentes de APT. Finalmente instalamos docker-ce (Community Edition). Para verificar que la instalación fue exitosa, ejecutamos docker --version que debe mostrar la versión instalada.


### Permisos de Usuario

* Por defecto, solo root puede ejecutar docker.
* Añadir usuario al grupo docker: `usermod -aG docker usuario`
* Cerrar sesión y volver a entrar.
* Verificar con: `docker ps`

Note: Tras la instalación, solo el usuario root puede ejecutar comandos docker por defecto. Esto es un inconveniente para el uso diario. Para permitir que usuarios normales ejecuten docker sin sudo, debemos añadirlos al grupo docker usando el comando usermod -aG docker seguido del nombre de usuario. Es importante cerrar la sesión actual y volver a iniciarla para que los cambios de grupo surtan efecto. Podemos verificar ejecutando docker ps sin sudo.


### Verificar Instalación

```bash
$ docker --version
Docker version 20.10.24+dfsg1, build 297e128

$ docker ps
CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES
```

Note: Una vez instalado Docker, es fundamental verificar que todo funciona correctamente. El comando docker --version nos muestra la versión instalada de Docker. El comando docker ps lista los contenedores en ejecución, aunque inicialmente no tendremos ninguno. Si ambos comandos funcionan sin errores, Docker está correctamente instalado y configurado. La versión puede variar dependiendo del sistema operativo y la fecha de instalación.

---

## 2. Hola Mundo en Docker


### Primer Contenedor

* Docker Hub: registro público de imágenes.
* Comando: `docker run hello-world`
* Descarga automática si no existe localmente.
* Ejecuta y muestra mensaje de bienvenida.

Note: El tradicional "Hola Mundo" en Docker se hace ejecutando docker run hello-world. Este comando busca la imagen hello-world localmente. Si no la encuentra, la descarga automáticamente desde Docker Hub, el registro público oficial de imágenes Docker. Una vez descargada, crea un contenedor desde esa imagen, lo ejecuta, muestra un mensaje de bienvenida explicando cómo funciona Docker, y luego el contenedor se detiene automáticamente. Es el ejemplo más simple para verificar que Docker funciona correctamente.


### ¿Qué Sucede Internamente? I

1. Cliente docker contacta al daemon docker.
2. Daemon busca la imagen localmente.
3. Si no existe, la descarga de Docker Hub.
4. Daemon crea un contenedor desde la imagen.

Note: Cuando ejecutamos docker run, el cliente docker envía la petición al daemon docker, que es el servicio que se ejecuta en segundo plano y gestiona los contenedores. El daemon primero busca la imagen especificada en el registro local. Si no encuentra la imagen localmente, se conecta a Docker Hub y la descarga automáticamente. Una vez que tiene la imagen disponible, el daemon crea un nuevo contenedor a partir de ella.


### ¿Qué Sucede Internamente? II

5. Daemon ejecuta el comando en el contenedor.
6. Daemon captura la salida y la envía al cliente.
7. Cliente muestra la salida en el terminal.
8. Contenedor se detiene tras completar su tarea.

Note: Continuando con el proceso, el daemon ejecuta el comando predefinido en la imagen dentro del contenedor recién creado. Captura toda la salida estándar y de errores del contenedor y la envía de vuelta al cliente docker. El cliente muestra esta información en nuestro terminal. Finalmente, cuando el comando termina su ejecución, el contenedor se detiene automáticamente, aunque permanece en el sistema hasta que decidamos eliminarlo.


### Ejecutando hello-world

```bash
$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to
work correctly.
```

Note: Este es el output típico al ejecutar docker run hello-world por primera vez. Primero vemos el mensaje "Unable to find image" indicando que la imagen no existe localmente. Luego muestra el progreso de descarga "Pulling from library/hello-world". Una vez descargada, ejecuta el contenedor que imprime un mensaje explicativo de cómo funciona Docker. Este mensaje confirma que Docker está instalado correctamente y que el daemon puede comunicarse con Docker Hub, descargar imágenes y ejecutar contenedores.


### Verificar Contenedores

```bash
$ docker ps -a
CONTAINER ID IMAGE        COMMAND  CREATED       STATUS
c2d5b6e2c6af hello-world  "/hello" 2 minutes ago Exited (0)
```

Note: El comando docker ps lista los contenedores en ejecución. Con la opción -a mostramos todos los contenedores, incluyendo los detenidos. Podemos ver que nuestro contenedor hello-world tiene estado "Exited (0)", lo que significa que terminó correctamente. Cada contenedor tiene un ID único, muestra la imagen de la que se creó, el comando que ejecutó, cuándo fue creado y su estado actual. Este contenedor permanece en el sistema aunque esté detenido, ocupando un espacio mínimo.

---

## 3. Ejecución Simple de Contenedores


### Comando docker run

* Crea y ejecuta un contenedor desde una imagen.
* Sintaxis: `docker run [opciones] imagen [comando]`
* Si la imagen no existe, se descarga automáticamente.
* El contenedor ejecuta el comando y se detiene.

Note: El comando docker run es el más fundamental en Docker. Combina varios pasos en uno: crea un nuevo contenedor desde una imagen especificada y lo ejecuta inmediatamente. Si la imagen no está disponible localmente, Docker la descarga automáticamente de Docker Hub. Podemos especificar un comando a ejecutar dentro del contenedor. Una vez que el comando termina, el contenedor se detiene, aunque permanece en el sistema para futura referencia o reinicio.


### Ejemplo con Ubuntu

```bash
$ docker run ubuntu echo 'Hello world'
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
8387d9ff0016: Pull complete
Status: Downloaded newer image for ubuntu:latest
Hello world
```

Note: En este ejemplo creamos un contenedor desde la imagen ubuntu y ejecutamos el comando echo 'Hello world'. Como no teníamos la imagen ubuntu localmente, Docker la descarga primero desde Docker Hub. La imagen ubuntu contiene un sistema operativo Ubuntu minimalista. Una vez descargada, crea el contenedor, ejecuta el comando echo que imprime el mensaje, y luego el contenedor se detiene inmediatamente. Este ejemplo demuestra cómo podemos ejecutar comandos arbitrarios dentro de contenedores.


### Verificando el Contenedor Creado

```bash
$ docker ps -a
CONTAINER ID IMAGE   COMMAND              CREATED      STATUS
3bbf39d0ec26 ubuntu  "echo 'Hello wo…"   31 secs ago  Exited (0)
```

Note: Al ejecutar docker ps -a vemos todos los contenedores incluyendo los detenidos. Nuestro contenedor ubuntu aparece con estado "Exited (0)", indicando que terminó correctamente. Podemos ver el comando que ejecutó, cuándo fue creado y su ID único. Docker asigna automáticamente un nombre aleatorio al contenedor si no especificamos uno. Este contenedor podría reiniciarse más tarde, aunque típicamente los contenedores que ejecutan un comando simple se eliminan después.


### Listando Imágenes Descargadas

```bash
$ docker images
REPOSITORY   TAG      IMAGE ID      CREATED      SIZE
ubuntu       latest   f63181f19b2f  7 days ago   72.9MB
hello-world  latest   bf756fb1ae65  13 months    13.3kB
```

Note: El comando docker images lista todas las imágenes que tenemos descargadas localmente en nuestro registro local. Para cada imagen vemos su nombre (repository), la etiqueta de versión (tag), un ID único, cuándo fue creada originalmente y su tamaño en disco. Las imágenes permanecen en nuestro sistema después de su primer uso, así que la próxima vez que creemos un contenedor desde ellas no necesitaremos descargarlas de nuevo, haciendo el proceso mucho más rápido.


### Imágenes vs Contenedores

* **Imagen**: Plantilla de solo lectura, reusable.
* **Contenedor**: Instancia ejecutable de una imagen.
* Una imagen puede generar múltiples contenedores.
* Los contenedores son efímeros, las imágenes persisten.

Note: Es crucial entender la diferencia entre imágenes y contenedores. Una imagen es como una plantilla o una clase en programación orientada a objetos: es de solo lectura y puede usarse muchas veces. Un contenedor es como una instancia de esa clase: es una ejecución particular de la imagen con su propio estado y datos. Podemos crear múltiples contenedores desde la misma imagen, cada uno independiente. Los contenedores son efímeros (temporales), mientras que las imágenes persisten hasta que las eliminemos explícitamente.

---

## 4. Contenedores Interactivos


### Modo Interactivo

* Opción `-i`: Mantiene STDIN abierto.
* Opción `-t`: Asigna un pseudo-terminal.
* Combinación `-it`: Sesión interactiva completa.
* Permite interactuar con el contenedor en tiempo real.

Note: El modo interactivo nos permite trabajar dentro de un contenedor como si estuviéramos en una sesión de terminal normal. La opción -i (interactive) mantiene la entrada estándar (STDIN) abierta incluso si no está conectada, permitiendo enviar comandos. La opción -t (tty) asigna un pseudo-terminal, proporcionando una experiencia de línea de comandos completa. Juntas (-it) permiten una sesión interactiva donde podemos ejecutar comandos, ver resultados y trabajar como en un sistema Linux normal.


### Creando Contenedor Interactivo

```bash
$ docker run -it --name contenedor1 ubuntu bash
root@2bfa404bace0:/#
```

Note: Este comando crea un contenedor interactivo desde la imagen ubuntu. La opción --name le asigna un nombre específico (contenedor1) en lugar de uno aleatorio. El comando bash al final indica que queremos ejecutar el intérprete de comandos bash dentro del contenedor. Una vez iniciado, nos encontramos dentro del contenedor con un prompt de root. Podemos ejecutar cualquier comando disponible en Ubuntu. El identificador después de @ es el ID del contenedor.


### Trabajando Dentro del Contenedor

```bash
root@2bfa404bace0:/# ls
bin boot dev etc home lib media mnt opt proc root

root@2bfa404bace0:/# ps aux
USER PID %CPU %MEM COMMAND
root   1  0.0  0.0 /bin/bash

root@2bfa404bace0:/# cat /etc/os-release
NAME="Ubuntu"
```

Note: Una vez dentro del contenedor interactivo, podemos ejecutar comandos como en cualquier sistema Linux. El comando ls muestra la estructura de directorios típica de Linux. Con ps aux vemos los procesos en ejecución; notablemente, solo hay uno: nuestro bash. Esto demuestra lo ligeros que son los contenedores comparados con VMs completas. Podemos ver información del sistema con cat /etc/os-release. Es un entorno Ubuntu completo pero mínimo, con solo lo esencial instalado.


### Saliendo del Contenedor

* Comando `exit` para salir.
* También funciona Ctrl+D.
* El contenedor se detiene al salir.
* Estado cambia a "Exited".

Note: Para salir de un contenedor interactivo, simplemente escribimos exit o presionamos Ctrl+D. Cuando salimos, el contenedor se detiene automáticamente porque su proceso principal (bash) ha terminado. El contenedor permanece en el sistema pero con estado "Exited". Esto es importante: el contenedor no se elimina, solo se detiene. Podemos verificarlo con docker ps -a. Todos los cambios que hicimos dentro del contenedor (archivos creados, paquetes instalados) permanecen guardados en ese contenedor detenido.


### Reiniciando Contenedor Detenido

```bash
$ docker start contenedor1
contenedor1

$ docker attach contenedor1
root@2bfa404bace0:/#
```

Note: Podemos reiniciar un contenedor detenido con docker start seguido del nombre o ID del contenedor. Esto arranca el contenedor nuevamente ejecutando su proceso principal (bash en nuestro caso). Sin embargo, start no nos conecta automáticamente al contenedor. Para eso usamos docker attach que nos reconecta a la sesión del contenedor en ejecución. Volveremos a ver el mismo prompt y todos los archivos y cambios que hicimos anteriormente seguirán ahí, demostrando la persistencia del estado del contenedor.


### Ejecutando Comandos sin attach

```bash
$ docker start contenedor1
contenedor1

$ docker exec contenedor1 ls -al
total 64
drwxr-xr-x   1 root root 4096 Jan 28 19:12 .
drwxr-xr-x   1 root root 4096 Jan 28 19:12 ..
```

Note: No siempre necesitamos conectarnos interactivamente a un contenedor. El comando docker exec nos permite ejecutar comandos en un contenedor que ya está en ejecución, sin necesidad de attach. En este ejemplo, ejecutamos ls -al dentro de contenedor1 y vemos el resultado directamente en nuestra terminal. Esto es muy útil para tareas puntuales como verificar archivos, ejecutar scripts o hacer comprobaciones rápidas sin entrar en una sesión interactiva completa.


### Reiniciar vs Start

* `docker restart`: Para y vuelve a iniciar el contenedor.
* Útil para aplicar cambios de configuración.
* Equivale a `stop` seguido de `start`.

Note: El comando docker restart es útil cuando necesitamos reiniciar un contenedor completamente. Lo que hace internamente es ejecutar docker stop seguido de docker start. Esto es particularmente útil cuando hemos modificado configuraciones o archivos de configuración en el contenedor y necesitamos que la aplicación los recargue. Por ejemplo, si cambiamos la configuración de un servidor web dentro del contenedor, un restart asegura que esos cambios se apliquen correctamente.


### Inspeccionando Contenedores

```bash
$ docker inspect contenedor1
[{
    "Id": "178871769ac2...",
    "Created": "2021-01-28T19:12:21.76Z",
    "Path": "bash",
    "State": {
        "Status": "exited",
        "Running": false,
    }
}]
```

Note: El comando docker inspect proporciona información detallada sobre un contenedor en formato JSON. Muestra datos como el ID completo del contenedor, cuándo fue creado, qué comando ejecuta, su estado actual, configuración de red, volúmenes montados, variables de entorno, puertos mapeados y mucha más información técnica. Esta información es invaluable para debugging y para entender exactamente cómo está configurado un contenedor. Es especialmente útil cuando trabajamos con configuraciones complejas o cuando necesitamos diagnosticar problemas.

---

## 5. Contenedores Demonio


### ¿Qué es un Contenedor Demonio?

* Ejecuta procesos en segundo plano.
* Opción `-d` (detached mode).
* No bloquea el terminal.
* Útil para servicios de larga duración.

Note: Un contenedor demonio es aquel que se ejecuta en segundo plano, sin ocupar nuestro terminal. Usamos la opción -d (detached) para crear estos contenedores. A diferencia de los contenedores interactivos que vimos antes, un contenedor demonio se inicia, se desconecta de nuestro terminal, y sigue ejecutándose independientemente. Esto es ideal para servicios como servidores web, bases de datos o cualquier aplicación que debe ejecutarse continuamente. Podemos seguir usando nuestra terminal para otros comandos mientras el contenedor trabaja en segundo plano.


### Creando un Contenedor Demonio

```bash
$ docker run -d --name contenedor2 ubuntu \
  bash -c "while true; do echo hello world; sleep 1; done"
7b6c3b1c0d650445b35a1107ac54610b
```

Note: Este comando crea un contenedor demonio que ejecuta un bucle infinito. El script bash imprime "hello world" cada segundo indefinidamente. La opción -d hace que se ejecute en background. Docker devuelve el ID completo del contenedor y nos devuelve el control del terminal inmediatamente. El contenedor sigue ejecutándose en segundo plano. Este tipo de contenedor es útil para entender cómo funcionan los servicios que deben ejecutarse continuamente, como servidores web o workers.


### Listando Contenedores en Ejecución

```bash
$ docker ps
CONTAINER ID IMAGE  COMMAND              CREATED    STATUS
7b6c3b1c0d65 ubuntu "bash -c 'while..." 1 min ago  Up 1 minute
```

Note: El comando docker ps sin la opción -a muestra solo los contenedores que están actualmente en ejecución. Podemos ver nuestro contenedor demonio con estado "Up", indicando cuánto tiempo lleva ejecutándose. A diferencia de los contenedores que ejecutan un comando simple y terminan, este contenedor seguirá en ejecución indefinidamente porque su comando es un bucle infinito. Podemos ver parte del comando que está ejecutando, el tiempo que lleva activo, y su estado de salud.


### Viendo los Logs del Contenedor

```bash
$ docker logs contenedor2
hello world
hello world
hello world
```

Note: Aunque el contenedor se ejecuta en segundo plano, podemos ver su salida con docker logs. Este comando muestra todo lo que el contenedor ha escrito en su salida estándar y salida de errores. En nuestro ejemplo, vemos múltiples líneas de "hello world" que el bucle ha estado imprimiendo. Los logs son cruciales para depurar problemas y monitorizar el comportamiento de nuestras aplicaciones en contenedores. Sin logs, sería muy difícil saber qué está pasando dentro de un contenedor en background.


### Siguiendo Logs en Tiempo Real

```bash
$ docker logs -f contenedor2
hello world
hello world
hello world
(continúa mostrando nuevas líneas...)
```

Note: La opción -f (follow) con docker logs funciona similar al comando tail -f en Linux. Muestra los logs existentes y luego continúa mostrando las nuevas líneas a medida que el contenedor las genera, en tiempo real. Esto es extremadamente útil durante el desarrollo y debugging, permitiéndonos ver exactamente qué está haciendo nuestra aplicación momento a momento. Para salir del modo follow, presionamos Ctrl+C, lo cual solo cierra el visualizador de logs pero no afecta al contenedor que sigue ejecutándose.


### Detener un Contenedor Demonio

```bash
$ docker stop contenedor2
contenedor2

$ docker ps -a
CONTAINER ID IMAGE  COMMAND     CREATED  STATUS
7b6c3b1c0d65 ubuntu "bash -c..." 5 min   Exited (137)
```

Note: Para detener un contenedor en ejecución usamos docker stop seguido del nombre o ID del contenedor. Docker envía una señal SIGTERM al proceso principal del contenedor, dándole tiempo (por defecto 10 segundos) para terminar limpiamente. Si el proceso no termina en ese tiempo, Docker envía SIGKILL para forzar la detención. El contenedor pasa a estado "Exited" pero permanece en el sistema. Podemos reiniciarlo más tarde con docker start si lo necesitamos, y mantendrá todos sus datos y configuración.


### Eliminando Contenedores

```bash
$ docker rm contenedor2
contenedor2

$ docker ps -a
CONTAINER ID IMAGE COMMAND CREATED STATUS
(contenedor2 ya no aparece)
```

Note: El comando docker rm elimina permanentemente un contenedor del sistema. Solo podemos eliminar contenedores que están detenidos; si intentamos eliminar uno en ejecución, Docker nos dará un error. Para forzar la eliminación de un contenedor en ejecución, podemos usar docker rm -f. Al eliminar un contenedor, perdemos todos los cambios que hicimos dentro de él (archivos creados, configuraciones modificadas, etc.), pero la imagen desde la que se creó permanece intacta y podemos crear nuevos contenedores desde ella.

---

## 6. Contenedor con Servidor Web


### Imagen httpd de Apache

* Imagen oficial de Apache HTTP Server.
* Versión 2.4 disponible con etiqueta `httpd:2.4`.
* Lista para servir contenido web.
* DocumentRoot en `/usr/local/apache2/htdocs/`.

Note: Docker Hub contiene muchas imágenes oficiales de aplicaciones populares. Una de ellas es httpd, que contiene el servidor web Apache HTTP Server. Al especificar la etiqueta 2.4 nos aseguramos de usar la versión 2.4 de Apache. Esta imagen viene preconfigurada y lista para servir páginas web. El directorio donde Apache busca los archivos HTML por defecto es /usr/local/apache2/htdocs/. Esta imagen es un excelente ejemplo de cómo Docker facilita el despliegue de servicios complejos con un solo comando.


### Creando Servidor Web en Docker

```bash
$ docker run -d --name my-apache-app \
  -p 8080:80 httpd:2.4
```

Note: Este comando crea un contenedor con Apache en modo demonio. La parte más importante es la opción -p 8080:80 que mapea puertos. El formato es puerto_host:puerto_contenedor. Esto significa que el puerto 80 dentro del contenedor (donde Apache escucha por defecto) se mapea al puerto 8080 de nuestro host. Así podemos acceder al servidor web desde nuestro navegador en localhost:8080 o usando la IP de nuestra máquina. Sin este mapeo de puertos, no podríamos acceder al servidor desde fuera del contenedor.


### Mapeo de Puertos

* Formato: `-p puerto_host:puerto_contenedor`
* Permite acceso desde el exterior al contenedor.
* Múltiples puertos: `-p 8080:80 -p 443:443`
* Nunca accedemos directamente a la IP del contenedor.

Note: El mapeo de puertos es fundamental en Docker. Los contenedores tienen su propia interfaz de red y direcciones IP en una red virtual privada. No accedemos directamente a estas IPs internas. En su lugar, mapeamos puertos del host a puertos del contenedor. Podemos mapear múltiples puertos añadiendo múltiples opciones -p. Por ejemplo, para un servidor web con HTTPS necesitaríamos -p 8080:80 -p 8443:443. También podemos dejar que Docker asigne un puerto aleatorio usando solo -p 80 sin especificar el puerto del host.


### Accediendo al Servidor Web

* Abrir navegador en `http://localhost:8080`
* O usar la IP del host: `http://192.168.1.100:8080`
* Verás la página por defecto de Apache.

Note: Una vez que el contenedor está en ejecución y los puertos están mapeados, podemos acceder al servidor web desde cualquier navegador. Si estamos en la misma máquina donde corre Docker, usamos localhost:8080. Si accedemos desde otra máquina en la red, usamos la IP del host donde está Docker, por ejemplo 192.168.1.100:8080. Veremos la página por defecto de Apache "It works!". Esto confirma que Apache está funcionando correctamente dentro del contenedor y que el mapeo de puertos está configurado apropiadamente.


### Verificando el Contenedor

```bash
$ docker ps
CONTAINER ID IMAGE      COMMAND          PORTS
9c3effd891e3 httpd:2.4  "httpd-foreg..." 0.0.0.0:8080->80/tcp
```

Note: Al ejecutar docker ps vemos nuestro contenedor web en ejecución. La columna PORTS es particularmente interesante: muestra 0.0.0.0:8080->80/tcp, que indica que el puerto 8080 de todas las interfaces de red del host (0.0.0.0) está mapeado al puerto 80 del contenedor. El proceso que se ejecuta es httpd-foreground, que es el servidor Apache en modo foreground (necesario para que el contenedor no termine inmediatamente). Este contenedor puede ejecutarse indefinidamente sirviendo páginas web.


### Viendo Logs de Apache

```bash
$ docker logs my-apache-app
AH00558: httpd: Could not reliably determine...
[core:notice] [pid 1] AH00094: Command line: 'httpd'
192.168.1.10 - - [28/Jan/2024:10:15:30] "GET / HTTP/1.1" 200
```

Note: Los logs de Apache dentro del contenedor son accesibles con docker logs. Vemos mensajes de inicio de Apache y registros de acceso HTTP. Cada petición HTTP que hacemos al servidor queda registrada aquí, mostrando la IP del cliente, la fecha/hora, el método HTTP, la ruta solicitada y el código de respuesta. Estos logs son esenciales para depuración y monitorización. Con la opción -f podemos seguir los logs en tiempo real, viendo cada petición a medida que ocurre, muy útil durante el desarrollo.


### Modificando Contenido del Servidor I

* Método 1: Acceder interactivamente

```bash
$ docker exec -it my-apache-app bash
root@cf3cd01a4993:/usr/local/apache2#
root@cf3cd01a4993:/usr/local/apache2# cd htdocs/
root@cf3cd01a4993:/usr/local/apache2/htdocs# \
  echo "<h1>Curso Docker</h1>" > index.html
```

Note: Podemos modificar el contenido del servidor web de varias formas. La primera es acceder interactivamente al contenedor con docker exec -it seguido del nombre y bash. Una vez dentro, navegamos al directorio htdocs y modificamos o creamos archivos HTML. En este caso, reemplazamos el index.html predeterminado con uno nuevo que muestra "Curso Docker". Al salir del contenedor con exit, los cambios persisten y podemos verlos inmediatamente recargando la página en el navegador.


### Modificando Contenido del Servidor II

* Método 2: Comando directo

```bash
$ docker exec my-apache-app bash -c \
  'echo "<h1>Curso Docker</h1>" > \
  /usr/local/apache2/htdocs/index.html'
```

Note: El segundo método para modificar archivos es ejecutar el comando directamente sin entrar en una sesión interactiva. Usamos docker exec con bash -c para ejecutar un comando de shell completo. Este método es más eficiente cuando sabemos exactamente qué queremos hacer y no necesitamos explorar o hacer cambios múltiples. Es perfecto para scripts de automatización o cuando queremos hacer cambios rápidos sin la sobrecarga de una sesión interactiva completa.


### Copiando Archivos al Contenedor

```bash
$ docker cp index.html \
  my-apache-app:/usr/local/apache2/htdocs/
```

Note: Docker también permite copiar archivos directamente desde el host al contenedor usando docker cp. La sintaxis es similar a scp de Linux: archivo_origen destino. Podemos copiar archivos individuales o directorios completos. Esto es muy útil cuando tenemos contenido web desarrollado en nuestro host que queremos desplegar en el contenedor. También funciona a la inversa: podemos copiar archivos desde el contenedor al host, útil para backups o para extraer logs y datos.

---

## 7. Configuración con Variables de Entorno


### ¿Qué son las Variables de Entorno?

* Parámetros de configuración del contenedor.
* Se definen al crear el contenedor con `-e`.
* Permiten personalizar comportamiento sin modificar imagen.
* Disponibles para procesos dentro del contenedor.

Note: Las variables de entorno son pares clave-valor que configuran el comportamiento de las aplicaciones dentro de los contenedores. En lugar de modificar archivos de configuración dentro de la imagen o el contenedor, podemos pasar configuraciones como variables de entorno al crear el contenedor. Esto hace las imágenes más reutilizables y flexibles. Por ejemplo, podemos usar la misma imagen de base de datos pero con diferentes contraseñas o nombres de bases de datos según el entorno (desarrollo, testing, producción).


### Definiendo Variables de Entorno

```bash
$ docker run -it --name prueba \
  -e USUARIO=prueba ubuntu bash

root@91e81200c633:/# echo $USUARIO
prueba
```

Note: Usamos la opción -e o --env para definir variables de entorno al crear un contenedor. El formato es -e NOMBRE_VARIABLE=valor. Podemos definir múltiples variables añadiendo varias opciones -e. Una vez dentro del contenedor, estas variables están disponibles como variables de entorno normales de Linux, accesibles con $NOMBRE_VARIABLE. Las aplicaciones dentro del contenedor pueden leer estas variables para configurarse, por ejemplo, para conectarse a una base de datos o para cambiar comportamientos según el entorno.


### Ejemplo: MariaDB con Variables I

* Imagen `mariadb` requiere configuración inicial.
* Variable obligatoria: `MARIADB_ROOT_PASSWORD`.
* Otras opciones: `MARIADB_DATABASE`, `MARIADB_USER`.
* Documentación en Docker Hub detalla variables disponibles.

Note: La imagen oficial de MariaDB es un excelente ejemplo de uso de variables de entorno. Requiere obligatoriamente que definamos MARIADB_ROOT_PASSWORD al crear el contenedor, o fallará. Esta variable establece la contraseña del usuario root de la base de datos. Opcionalmente podemos definir MARIADB_DATABASE para crear una base de datos automáticamente, MARIADB_USER y MARIADB_PASSWORD para crear un usuario adicional. Es crucial leer la documentación en Docker Hub de cada imagen para saber qué variables necesita y acepta.


### Creando Contenedor MariaDB

```bash
$ docker run -d --name some-mariadb \
  -e MARIADB_ROOT_PASSWORD=my-secret-pw \
  mariadb

$ docker ps
CONTAINER ID IMAGE   COMMAND              PORTS
9c3effd891e3 mariadb "docker-entrypo..." 3306/tcp
```

Note: Creamos un contenedor MariaDB en modo demonio (-d) y definimos la contraseña del root con la variable de entorno MARIADB_ROOT_PASSWORD. El script de inicialización de la imagen MariaDB lee esta variable y configura la base de datos automáticamente durante el primer arranque. Podemos ver que el contenedor expone el puerto 3306 (puerto predeterminado de MySQL/MariaDB) pero no lo hemos mapeado aún, así que solo es accesible desde otros contenedores en la misma red Docker.


### Verificando Variables de Entorno

```bash
$ docker exec -it some-mariadb env
PATH=/usr/local/sbin:/usr/local/bin...
HOSTNAME=9c3effd891e3
MARIADB_ROOT_PASSWORD=my-secret-pw
HOME=/root
```

Note: Podemos ver todas las variables de entorno definidas en un contenedor con docker exec seguido del comando env. Esto lista todas las variables, tanto las que definimos explícitamente como las que Docker o la imagen establecen automáticamente. Vemos variables estándar como PATH, HOSTNAME, HOME, y nuestra variable personalizada MARIADB_ROOT_PASSWORD. Esta verificación es útil para depuración y para confirmar que las variables llegaron correctamente al contenedor.


### Accediendo a MariaDB Internamente

```bash
$ docker exec -it some-mariadb bash

root@9c3effd891e3:/# mariadb -u root \
  -p"$MARIADB_ROOT_PASSWORD"
Welcome to the MariaDB monitor...

MariaDB [(none)]>
```

Note: Podemos acceder a la base de datos MariaDB desde dentro del contenedor. Primero entramos con bash, luego usamos el cliente mariadb. Notemos cómo usamos la variable de entorno MARIADB_ROOT_PASSWORD directamente en el comando con $MARIADB_ROOT_PASSWORD. El shell bash expande esta variable antes de ejecutar el comando. Esto es una buena práctica: evitar escribir contraseñas en texto plano en los comandos y usar variables de entorno en su lugar. Una vez conectados, tenemos acceso completo a la base de datos.


### Acceso Directo con exec

```bash
$ docker exec -it some-mariadb mariadb -u root -p
Enter password:
Welcome to the MariaDB monitor...

MariaDB [(none)]>
```

Note: También podemos ejecutar directamente el cliente mariadb sin entrar primero en bash. Docker exec permite ejecutar cualquier comando disponible en el contenedor. En este caso, ejecutamos mariadb directamente. Como no pasamos la contraseña en el comando, nos la pide interactivamente. Este método es más directo cuando sabemos exactamente qué queremos hacer y no necesitamos explorar o ejecutar múltiples comandos. Es más seguro para entornos de producción donde no queremos la contraseña visible en el historial de comandos.


### Mapeando Puertos de MariaDB

```bash
$ docker rm -f some-mariadb

$ docker run -d -p 3306:3306 --name some-mariadb \
  -e MARIADB_ROOT_PASSWORD=my-secret-pw \
  mariadb
```

Note: Para acceder a MariaDB desde fuera del contenedor (desde nuestro host o desde otra máquina), necesitamos mapear el puerto 3306. Primero eliminamos el contenedor anterior con docker rm -f (el flag -f fuerza la eliminación incluso si está en ejecución). Luego creamos un nuevo contenedor idéntico pero con -p 3306:3306 para mapear el puerto. Ahora MariaDB es accesible desde cualquier cliente MySQL/MariaDB instalado en el host o en la red, conectándose a la IP del host en el puerto 3306.


### Conectando desde el Host

```bash
$ mysql -u root -p -h 127.0.0.1
Enter password:
Welcome to the MariaDB monitor...

MariaDB [(none)]>
```

Note: Con el puerto mapeado, podemos conectarnos a MariaDB desde nuestro host usando cualquier cliente MySQL/MariaDB instalado localmente. Usamos -h 127.0.0.1 o la IP de nuestro host. Podríamos también usar -h localhost, aunque en algunos sistemas localhost se conecta via socket Unix en lugar de TCP/IP. Esto es muy útil para desarrollo: podemos usar herramientas gráficas como MySQL Workbench o phpMyAdmin instaladas en el host para gestionar la base de datos que corre en el contenedor.


### Mejores Prácticas con Variables

* Nunca hardcodear contraseñas en imágenes.
* Usar variables de entorno para configuración.
* Documentar variables necesarias y opcionales.
* Usar archivos `.env` para muchas variables.
* En producción, usar secretos de Docker o Kubernetes.

Note: Las variables de entorno son fundamentales para la configuración de contenedores, pero hay mejores prácticas que seguir. Nunca incluir contraseñas o secretos directamente en las imágenes o en Dockerfiles. Usar variables de entorno para toda configuración que pueda cambiar entre entornos. Documentar claramente qué variables necesita tu aplicación. Para muchas variables, considerar usar archivos .env. En producción, usar mecanismos más seguros como Docker secrets o Kubernetes secrets en lugar de variables de entorno simples, ya que estas son visibles con docker inspect.

---

## Resumen Módulo 1


### Conceptos Clave Aprendidos

* Instalación y configuración de Docker.
* Diferencia entre imágenes y contenedores.
* Contenedores interactivos vs demonio.
* Mapeo de puertos para acceso externo.
* Configuración con variables de entorno.

Note: En este primer módulo hemos cubierto los fundamentos esenciales de Docker. Aprendimos a instalar Docker en diferentes sistemas operativos y a verificar que funciona correctamente. Entendimos la diferencia crucial entre imágenes (plantillas) y contenedores (instancias en ejecución). Exploramos diferentes formas de ejecutar contenedores: interactivos para trabajar dentro de ellos, y demonio para servicios en background. Vimos cómo mapear puertos para acceder a servicios desde fuera del contenedor. Y aprendimos a configurar contenedores usando variables de entorno.


### Comandos Esenciales

* `docker run`: Crear y ejecutar contenedores.
* `docker ps`: Listar contenedores.
* `docker exec`: Ejecutar comandos en contenedor.
* `docker logs`: Ver salida del contenedor.
* `docker stop/start`: Controlar ciclo de vida.

Note: Estos son los comandos fundamentales que usarás constantemente al trabajar con Docker. docker run crea y ejecuta nuevos contenedores. docker ps lista contenedores en ejecución (-a para ver todos). docker exec ejecuta comandos en contenedores existentes. docker logs muestra la salida de un contenedor. docker stop y start controlan el ciclo de vida. Estos comandos son la base sobre la que construiremos en los siguientes módulos cuando trabajemos con imágenes, volúmenes, redes y Docker Compose.


### Próximo Módulo

**Módulo 2: Imágenes Docker**

* Registros de imágenes y Docker Hub
* Gestión de imágenes
* Organización por capas
* Creación de contenedores desde imágenes
* Ejemplo práctico: MediaWiki

Note: En el próximo módulo profundizaremos en las imágenes Docker. Aprenderemos sobre Docker Hub, el registro público donde se almacenan millones de imágenes. Veremos cómo gestionar imágenes localmente, entenderemos cómo se organizan por capas para eficiencia, y practicaremos creando contenedores desde diferentes imágenes. Terminaremos con un ejemplo práctico desplegando MediaWiki, una aplicación wiki completa. Este conocimiento es fundamental antes de pasar a temas más avanzados como volúmenes y redes.


### ¡Gracias!

¿Preguntas sobre el Módulo 1?

Note: Esto concluye el primer módulo del curso de Docker. Hemos establecido las bases necesarias para trabajar con contenedores. Es normal si algunos conceptos aún no están completamente claros; los consolidaremos con la práctica en los siguientes módulos. Os animo a experimentar con los comandos que hemos visto, crear vuestros propios contenedores, probar diferentes imágenes de Docker Hub y familiarizaros con el flujo de trabajo básico. En el siguiente módulo construiremos sobre estos fundamentos para trabajar más profundamente con imágenes Docker.
