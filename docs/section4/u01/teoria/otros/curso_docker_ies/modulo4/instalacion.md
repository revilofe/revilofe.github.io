# Creando escenarios multicontenedor con Docker Compose

Como visto hasta ahora en muchas ocasiones necesitamos correr varios contenedores para que nuestra aplicación funcione. En cualquiera de estos casos es necesario tener varios contenedores:

* Necesitamos varios servicios para que la aplicación funcione: Partiendo del principio de que cada contenedor ejecuta un sólo proceso, si necesitamos que la aplicación use varios servicios (web, base de datos, proxy inverso, ...) cada uno de ellos se implementará en un contenedor.
* Si tenemos construida nuestra aplicación con microservicios, cada uno de ellos se podrá implementar en un contenedor independiente.

Cuando trabajamos con escenarios donde necesitamos correr varios contenedores podemos utilizar [Docker Compose](https://docs.docker.com/compose/) para gestionarlos.

Vamos a definir el escenario en un fichero llamado `docker-compose.yaml` y vamos a gestionar el ciclo de vida de la aplicación y de todos los contenedores que necesitamos con el comando `docker compose`.

## Docker Compose V2

Como vemos en la página principal de Docker Compose, el pasado mes de julio de 2023 la versión V1 de Compose dejo de recibir actualizaciones. Por esta razón es muy conveniente usar la versión Compose V2 que viene integrada en Docker CLI.

En Compose V1 no podíamos hacer uso de Docker Compose utilizando el Docker CLI y teníamos que instalar un programa independiente, escrito en python, que se llama **docker-compose**. Sin embargo, con Compose V2 se incluye en el Docker CLI la posibilidad de trabajar con Compose usando el subcomando `docker compose`.

Hay algunas diferencias entre las dos versiones, pero se ha mantenido en un alto porcentaje la compatibilidad y por tanto podemos seguir usando los ficheros `docker-compose.yaml` de Compose V1 y en la versión 2.

## Ventajas de usar Docker Compose

* Hacer todo de manera **declarativa** para que no tenga que repetir todo el proceso cada vez que construyo el escenario.
* Poner en funcionamiento todos los contenedores que necesita mi aplicación de una sola vez y debidamente configurados.
* Garantizar que los contenedores **se arrancan en el orden adecuado**. Por ejemplo: mi aplicación no podrá funcionar debidamente hasta que no esté el servidor de bases de datos funcionando en marcha.
* Asegurarnos de que hay **comunicación** entre los contenedores que pertenecen a la aplicación.

---

* [El fichero docker-compose.yaml](docker-compose.md)
