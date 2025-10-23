# Ejemplo 2: Despliegue de la aplicación Temperaturas

En este ejemplo vamos a desplegar con Docker Compose la aplicación *Temperaturas*, que estudiamos en el módulo de redes: [Ejemplo 2: Despliegue de la aplicación Temperaturas](../modulo3/temperaturas.md).

Puedes encontrar el fichero `docker-compose.yaml` en en este [directorio](https://github.com/josedom24/curso_docker_ies/tree/main/ejemplos/modulo4/ejemplo2) del repositorio. 


En este caso el fichero `docker-compose.yaml` puede tener esta forma:

```yaml
version: '3.1'
services:
  frontend:
    container_name: temperaturas-frontend
    image: iesgn/temperaturas_frontend
    restart: always
    ports:
      - 8081:3000
    environment:
      TEMP_SERVER: temperaturas-backend:5000
    depends_on:
      - backend
  backend:
    container_name: temperaturas-backend
    image: iesgn/temperaturas_backend
    restart: always
```

Como hicimos en el ejemplo anterior, aunque no es necesario porque es valor por defecto, declaramos la variable de entorno `TEMP_SERVER: temperaturas-backend:5000`. Como indicábamos también, podríamos uso del nombre del servicio, de esta manera quedaría como `TTEMP_SERVER: backend:5000`.

Para crear el escenario:

```bash
$ docker compose up -d
[+] Running 3/3
 ✔ Network temperaturas_default     Created                                                      0.3s 
 ✔ Container temperaturas-backend   Started                                                      0.2s 
 ✔ Container temperaturas-frontend  Started                                                      0.2s 
```

Para listar los contenedores:

```bash
$ docker compose ps
NAME                    IMAGE                         COMMAND            SERVICE    CREATED          STATUS          PORTS
temperaturas-backend    iesgn/temperaturas_backend    "python3 app.py"   backend    20 seconds ago   Up 18 seconds   5000/tcp
temperaturas-frontend   iesgn/temperaturas_frontend   "python3 app.py"   frontend   20 seconds ago   Up 17 seconds   0.0.0.0:8081->3000/tcp, :::8081->3000/tcp
```
---

* [Ejemplo 3: Despliegue de Wordpress + mariadb](wordpress.md)
