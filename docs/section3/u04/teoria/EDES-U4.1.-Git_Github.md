---
title: "UD 4 - 4.1 Sistemas de control de versiones"
description: Sistemas de control de versiones
summary: Sistemas de control de versiones
authors:
    - Eduardo Fdez
date: 2022-09-18
icon:   
permalink: /edes/unidad4/4.1
categories:
    - EDES
tags:
    - EDES
    - GIT
    - GitHub
---
## Git & GitHub

### 1. Introducción
Un sistema de control de versiones es una herramienta que permite llevar un registro de los cambios realizados en el código fuente de un proyecto. Esto es útil para poder volver a versiones anteriores del código, comparar cambios, ver quién ha modificado algo, etc.

#### 1.1. Historia
Los sistemas de control de versiones han evolucionado mucho a lo largo del tiempo. Los primeros sistemas de control de versiones eran locales, es decir, no permitían trabajar en paralelo con otros desarrolladores. Con el tiempo, han ido apareciendo sistemas de control de versiones distribuidos, que permiten trabajar en paralelo, colaborar con otros desarrolladores, etc.

#### 1.2. Ventajas
Los sistemas de control de versiones tienen varias ventajas:
- Permiten llevar un registro de los cambios realizados en el código.
- Permiten trabajar en paralelo con otros desarrolladores.
- Permiten colaborar en proyectos de código abierto.
- Permiten volver a versiones anteriores del código.
- Permiten comparar cambios, ver quién ha modificado algo, etc.
- Permiten trabajar sin conexión a internet.
- Permiten tener un historial completo de los cambios realizados en el código.
- Permiten trabajar con ramas, etiquetas, etc.
- Permiten automatizar tareas, como pruebas, despliegues, etc.

#### 1.3. Desventajas
Los sistemas de control de versiones tienen algunas desventajas:
- Pueden ser complicados de usar.
- Pueden requerir mucho espacio en disco.
- Pueden requerir mucho tiempo para aprender a usarlos.
- Pueden requerir mucho tiempo para configurarlos.
- Pueden requerir mucho tiempo para mantenerlos.
- Pueden requerir mucho tiempo para solucionar problemas.
- Pueden requerir mucho tiempo para migrar de un sistema a otro.

#### 1.4. Tipos
Hay varios tipos de sistemas de control de versiones:
- **Sistemas de control de versiones locales**: Son sistemas de control de versiones que almacenan el código en un único lugar, como un disco duro, un servidor, etc. Ejemplos: RCS, SCCS, etc.
- **Sistemas de control de versiones centralizados**: Son sistemas de control de versiones que almacenan el código en un único lugar, como un servidor central. Ejemplos: CVS, Subversion, etc.
- **Sistemas de control de versiones distribuidos**: Son sistemas de control de versiones que almacenan el código en varios lugares, como en el disco duro de cada desarrollador, en un servidor central, etc. Ejemplos: Git, Mercurial, Bazaar, etc.
- **Sistemas de control de versiones en la nube**: Son sistemas de control de versiones que almacenan el código en la nube, es decir, en servidores remotos. Ejemplos: GitHub, GitLab, Bitbucket, etc.

### 2. Git
Git es un sistema de control de versiones distribuido, es decir, cada usuario tiene una copia completa del repositorio en su máquina. Esto permite trabajar sin conexión a internet y tener un historial completo de los cambios.


#### 2.1. Configuración
Git permite configurar varios parámetros, como el nombre del usuario, el correo electrónico, el editor de texto, alias, los ficheros que no se deben incluir en el repositorio, etc.

##### 2.1.2. Configuración del usuario
La configuración del usuario incluye parámetros como el nombre del usuario, el correo electrónico, el editor de texto, etc.

```bash
La como el nombre del usuario, el correo electrónico, el editor de texto, etc.

```bash
# Configurar el nombre del usuario
git config --global user.name "Nombre Apellido"

# Configurar el correo electrónico
git config --global user.email "

# Configurar el editor de texto
git config --global core.editor "nano"
```

##### 2.1.2. Configuración de .gitingore
Git permite configurar un archivo .gitignore para especificar qué archivos o carpetas no se deben incluir en el repositorio. Esto es útil para evitar subir archivos temporales, logs, etc.

```bash
# Crear un archivo .gitignore
touch .gitignore

# Añadir patrones al archivo .gitignore
echo "*.log" >> .gitignore
```

##### 2.1.3. Configuración de alias
Git permite configurar alias para los comandos más utilizados. Esto es útil para abreviar los comandos y hacerlos más fáciles de recordar.

```bash 
# Configurar un alias
git config --global alias.<nombre> <comando>

# Ver los alias configurados
git config --global --get-regexp alias
```

#### 2.2. Espacios de trabajo
Git tiene tres espacios de trabajo: el directorio de trabajo, el área de preparación y el repositorio.

* El directorio de trabajo es donde se modifican los archivos.
* El área de preparación es donde se preparan los cambios que se van a incluir en el próximo commit.
* El repositorio es donde se almacenan los commits.

##### 2.2.1. Directorio de trabajo
El directorio de trabajo es donde se modifican los archivos.

```bash
# Ver el estado del directorio de trabajo
git status

# Ver los cambios realizados en el directorio de trabajo
git diff
```

##### 2.2.2. Área de preparación
El área de preparación es donde se preparan los cambios que se van a incluir en el próximo commit. También se le conoce como "staging area" o "index".

```bash
# Añadir un archivo al área de preparación
git add <archivo>

# Ver el estado del área de preparación
git status
```

##### 2.2.3. Repositorio
El repositorio es donde se almacenan los commits.

```bash
# Hacer un commit
git commit -m "Mensaje del commit"

# Ver el historial de commits
git log
```

##### 2.2.4. Head
Git tiene un puntero especial llamado HEAD que apunta al commit actual. Nos indica en qué punto de la historia del código estamos.

```bash
# Ver el commit actual
git show HEAD
```

#### 2.3. Comandos básicos
Los comandos básicos de Git nos permiten inicializar un repositorio, registrar cambios, ver el estado del repositorio, ver el historial de commits, etc.

```bash
# Inicializar un repositorio. En un nuevo directorio, ejecutar:
git init

# Para registrar cambios. Añadir un archivo al index. 
git add <archivo>
git add . # Añadir todos los archivos

# Hacer un commit. Ahora el archivo está en el HEAD, pero no en el repositorio remoto.
git commit -m "Mensaje del commit"

# Ver el estado del repositorio
git status

# Ver el historial de commits
git log
```

#### 2.4. Ramas
Las ramas son una forma de trabajar en paralelo en el mismo repositorio. Nos permiten trabajar en nuevas funcionalidades, arreglar errores, etc. de forma aislada.

Por defecto, al crear el repositorio Git crea una rama llamada "master", que es la rama principal, pero se pueden crear otras ramas. 

Respecto a las ramas, se pueden crear, eliminar, fusionar, etc. 

Lo habitual es trabajar en una rama para desarrollar nuevas funcionalidades, arreglar errores, etc, y cuando se ha terminado, fusionarla con la rama principal.

```bash
# Crear una rama
git branch <nombre>

# Cambiar a una rama
git checkout <nombre>

# Crear una rama y cambiar a ella
git checkout -b <nombre>

# Fusionar una rama con la rama actual
git merge <nombre>

# Eliminar una rama
git branch -d <nombre>
```

Ten en cuenta que las ramas son locales, es decir, no se suben al repositorio remoto. Para subir una rama al repositorio remoto, hay que hacer un push.

```bash
# Subir una rama al repositorio remoto
git push origin <nombre_rama>
```

#### 2.4.1. Rebase
El rebase es una forma de fusionar dos ramas de forma lineal, es decir, sin crear un commit de fusión. Es decir, se cogen los commits de una rama y se aplican sobre la otra rama. Nos permite llevar un conjunto de cambios a un punto de la historia del código diferente.

```bash
# Cambiar a la rama que se quiere rebase
git checkout <rama>

# Hacer el rebase
git rebase <rama>
```

#### 2.4.2. Resolución de conflictos
Cuando se fusionan dos ramas que han modificado el mismo archivo, puede haber conflictos. Estos se deben resolver manualmente.

```bash
# Ver las ramas fusionadas y no fusionadas
git branch --merged
git branch --no-merged

# Resolver conflictos
git mergetool

# Ver si hay conflictos pendientes
git status

```

#### 2.4. Tags
Los tags son una forma de marcar un punto en la historia del repositorio. Se pueden usar para versiones, releases, etc.

```bash
# Crear un tag
git tag <nombre>

# Subir un tag a un repositorio remoto
git push --tags

# Ver los tags
git tag

# Ver el historial de un tag
git show <nombre>

# Cambiar a un tag
git checkout <nombre>

# Crear una rama a partir de un tag
git checkout -b <nombre> <tag>

# Fusionar un tag con la rama actual
git merge <nombre>

# Eliminar un tag
git tag -d <nombre>

```

#### 2.4. Repositorios remotos
Cuantos más desarrolladores trabajen en un proyecto, más útil será tener un repositorio remoto. Los cambios inicialmente se realizan en un repositorio local, y luego se suben a un repositorio remoto.

Un repositorio remoto es una copia del repositorio local en un servidor. Git permite trabajar con varios repositorios remotos, como GitHub, GitLab, Bitbucket, etc. Veremos github más adelante.

```bash
# Clonar un repositorio remoto. 
git clone <url>

# Si no se clonó el repositorio de uno existente, podemos conectar el repositorio local a un repositorio remoto. Para añadir un repositorio remoto. El nombre por defecto es "origin"
git remote add <nombre> <url>

# Ver los repositorios remotos
git remote -v

# Subir los cambios que están en el HEAD del repositorio local, a un repositorio remoto
git push <nombre> <rama>

# Descargar cambios de un repositorio remoto al repositorio local
git pull <nombre> <rama>
```

#### 2.7. Flujo de trabajo
El flujo de trabajo típico con Git es el siguiente:

1. Crear un repositorio local con `git init` o clonar un repositorio remoto con `git clone /path/to/repository`.
2. Añadir archivos al repositorio con `git add`.
3. Hacer un commit con `git commit`.
4. Crear una rama con `git branch`.
5. Cambiar a la rama con `git checkout`.
6. Hacer cambios, añadir, hacer commits, etc.
7. Fusionar la rama con `git merge`.


### 3. GitHub
GitHub es una plataforma de desarrollo colaborativo que utiliza Git como sistema de control de versiones. Permite alojar proyectos, realizar seguimiento de problemas, tareas y solicitudes de funciones, y dar seguimiento a todos los cambios en el código. 

#### 3.1. Repositorios
Un repositorio es un lugar donde se almacena el código fuente de un proyecto. Puede ser público o privado, y puede tener varios colaboradores.

```bash
# Crear un repositorio
git init
git add .
git commit -m "Primer commit"
git remote add origin <url>
git push -u origin master
```


#### 3.2. Issues
Las issues son una forma de realizar un seguimiento de tareas, mejoras, errores, etc. Se pueden asignar a usuarios, etiquetar, comentar, etc. 

#### 3.3. Pull Requests
Un pull request es una forma de proponer cambios en un repositorio. Se pueden revisar, comentar, aprobar, rechazar, etc.

### 4. Conclusiones
Git y GitHub son herramientas muy útiles para el desarrollo de software. Permiten llevar un control de los cambios realizados en el código, trabajar en paralelo, colaborar con otros desarrolladores, etc.
    


## Recursos

* [Git la guía sencilla](http://rogerdudler.github.io/git-guide/index.es.html)
* [Git en entornos distribuidos](https://git-scm.com/book/es/v2/Git-en-entornos-distribuidos-Flujos-de-trabajo-distribuidos)


## Fuente
