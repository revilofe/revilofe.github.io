---
title: "UD 4 - P4: Git/Github Rebase II"
description: Git/Github
summary: Git/Github
authors:
    - Eduardo Fdez
date: 2022-10-23
icon:   
permalink: /edes/unidad4/p4.4
categories:
    - EDES
tags:
    - Software
    - git
    - github
---

## Relación 4.1.4: Integración de ramas - Rebase II

### Objetivos
* Ver nuevos usos de GitHub y de "git rebase"
* Aprender a usar "git fork"
* Gestionar ficheros que no sean programas

### Descripción de la práctica

En esta práctica vamos a duplicar el repositorio [https://github.com/ging-moocs/MOOC_git_mod6-tf_agenda](https://github.com/ging-moocs/MOOC_git_mod6-tf_agenda) haciendo un "fork" en su cuenta de GitHub y clonarlo en un directorio local del mismo nombre. Este repositorio contiene solo el fichero tf-agenda.txt con texto plano. Es una agenda telefónica muy sencilla, con 3 teléfonos, creada en 4 commits, cuyo único objetivo es practicar con "git rebase --interactive ..."

*Contenido de la agenda*
```
$ cat tf_agenda.txt 
  John: 913-677-899;
  Eva:  915-768-455;
  Mary: 918-789-221;
```

*Lista de commits*
```
$ git log --oneline
  9eaa103 Add Mary tf
  71e69ce Add Eva tf
  1204dc8 Add Eva pending-tf
  f6e660e Add John tf
```

En el primer commit se introdujo el teléfono de John. En el segundo solo el nombre de Eva, pero se dejó el teléfono pendiente tal y como indica el mensaje del commit. En el tercero se añade el teléfono de Eva solamente. Y en el cuarto se introduce el teléfono de Mary.

En esta práctica se rehacen los commits de la rama master utilizando "git rebase --interactive …". Se deben juntar los commits 2 (1204dc8 Add Eva pending-tf) y 3 (71e69ce Add Eva tf) en uno solo, y corregir el teléfono de Mary (918-789-221) por el número 918-555-555. Debe quedar así:

```
$ cat tf_agenda.txt 
  John: 913-677-899;
  Eva:  915-768-455;
  Mary: 918-555-555;
```

```
$ git log --online
2eb1703 Add Mary tf   fixed
4716ce5 Add Eva tf    integrated
f6e660e Add John tf
```

Finalizar subiendo la rama master local (regenerada) a la rama corrected_tf_agenda del repositorio origin, que se creará porque no existe. El repositorio origen en Github tendrá ahora tanto la rama master, como la nueva corrected_tf_agenda.


### Tareas a realizar

#### Paso 1: Copiar el repositorio a tu cuenta

Lo primero que debemos hacer es copiar el repositorio [https://github.com/ging-moocs/MOOC_git_mod6-tf_agenda](https://github.com/ging-moocs/MOOC_git_mod6-tf_agenda) en nuestra cuenta. Para ello hacemos click sobre el botón "Fork" que se muestra en la web de Github en la esquina superior derecha de la página del repositorio.

#### Paso 2: Clonar el repositorio

A continuación clonamos el repositorio copiado en nuestro ordenador

```
$ git clone  git@github.com:<mi_usuario_de_github>/MOOC_git_mod6-tf_agenda 
$ cd MOOC_git_mod6-tf_agenda 
```

#### Paso 3: Juntar los commits 2 y 3 en uno solo

Ahora vamos a utilizar "git rebase --interactive f6e660e" para juntar los commits 2 (1204dc8 Add Eva pending-tf) y 3 (71e69ce Add Eva tf) en uno solo, y corregir el teléfono de Mary (918-789-221) por el número 918-555-555.

```
$ git rebase -i f6e660e
```

La opción --interactive (equivalente a -i) permite rehacer interactivamente los 3 últimos commits de la rama master. f6e660e es equivalente a HEAD\~3: referencia al tercer commit del grafo de commits, en dirección a la raíz, relativo al que está en el directorio de trabajo. Al invocar este comando, se abre el editor por defecto (normalmente nano o vi) con este script (los comentarios (empiezan por #) contienen instrucciones)

```
pick 1204dc8 Add Eva pending-tf
pick 71e69ce Add Eva tf
pick 9eaa103 Add Mary tf

# Rebase f6e660e..9eaa103 onto f6e660e
#
# Commands:
#  p, pick = use commit
#  r, reword = use commit, but edit the commit message
#  e, edit = use commit, but stop for amending
#  s, squash = use commit, but meld into previous commit
#  f, fixup = like "squash", but discard this commit's log message
#  x, exec = run command (the rest of the line) using shell
#
# These lines can be re-ordered; they are executed from top to bottom.
#
# If you remove a line here THAT COMMIT WILL BE LOST.
#
# However, if you remove everything, the rebase will be aborted.
#
# Note that empty commits are commented out

```
El script está en las 3 primeras líneas, que siguiendo las instrucciones (comentarios) modificamos para que junte los commits 2 y 3, y además nos abra el editor en el commit 4.

```
pick 1204dc8 Add Eva pending-tf
squash 71e69ce Add Eva tf
edit 9eaa103 Add Mary tf

...
```

Al cerrar la edición del fichero con el nuevo script, Git integra los commits 2 y 3 automáticamente (sabe que tiene que dejar el código del commit 3), pero nos abre el editor para que editemos el mensaje asociado al nuevo commit en la historia



```
# This is a combination of 2 commits.
# The first commit's message is:

Add Eva pending-tf

# This is the 2nd commit message:

Add Eva tf

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# Date:      Fri Jan 11 18:58:54 2019 +0100
#
# rebase in progress; onto f6e660e
# You are currently editing a commit while rebasing branch 'master' on 'f6e660e'.
#
# Changes to be committed:
#       modified:   tf_agenda.txt
#

```

Dejamos el segundo mensaje añadiendo la palabra "integrated" al final (para indicar que se han integrado los dos commits) y cerramos la edición para que el rebase continúe. El script indica que queremos editar el commit 4 por lo que Git devuelve control a la shell (sin finalizar el rebase) dando el siguiente mensaje

```
[detached HEAD 4716ce5] Add Eva tf    integrated
 Date: Fri Jan 11 18:58:54 2019 +0100
 1 file changed, 1 insertion(+)
Stopped at 9eaa1031b1c5eb7d52a19970a3a0967193d0b5a3... Add Mary tf
You can amend the commit now, with

	git commit --amend 

Once you are satisfied with your changes, run

	git rebase --continue
```


Git nos deja en el commit 4 de la rama master original, indicándonos que debemos modificar el código de dicho commit con un "amend" y continuar el rebase. La opción --amend rehace el commit anterior, en vez de crear uno nuevo. Editamos el fichero tf_agenda.txt para cambiar el teléfono de Mary por 918-555-555 y una vez modificado hacemos amend al commit 4 con:

```
$ git add tf_agenda.txt
$ git commit --amend
```

Antes de cerrar el nuevo commit 4, Git nos abre el editor con el mensaje asociado al commit para que lo podamos modificar, le añadimos la palabra  "fixed" al final (para indicar que hemos corregido el commit) y cerramos la edición para que el amend finalice

```
[detached HEAD 2eb1703] Add Mary tf   fixed
 Date: Fri Jan 11 19:01:44 2019 +0100
 1 file changed, 1 insertion(+)
```

Y con el commit 4 corregido con el amend, continuamos el rebase para que finalice

``` 
$  git rebase --continue
   Successfully rebased and updated refs/heads/master.
```

**Estado final de la rama master:**

Después del rebase, tanto el contenido de la agenda en tf_agenda.txt, como los commits de la rama master han quedado tal y como se pedía: commits 2 y 3 integrados y commit 4 corregido

```
$ cat tf_agenda.txt 
  John: 913-677-899;
  Eva:  915-768-455;
  Mary: 918-555-555;
```

```
$ git log --online
  2eb1703 Add Mary tf fixed
  4716ce5 Add Eva tf integrated
  f6e660e Add John tf
```

Si alguna vez se equivoca uno al rehacer una rama, se puede utilizar el reflog para arreglarlo: [https://git-scm.com/docs/git-reflog](https://git-scm.com/docs/git-reflog).



#### Paso 4: Subir los cambios a una nueva rama
Para finalizar, vamos a subir la rama "master" local (regenerada) a la rama "corrected_tf_agenda" del repositorio origin, la cual se creará porque no existe. El repositorio "origin" en Github tendrá ahora tanto la rama master, como la nueva "corrected_tf_agenda".

```
$ git checkout -b corrected_tf_agenda
$ git push origin corrected_tf_agenda
```

Si hubiésemos querido subir la nueva rama master del repositorio local a la rama master del repositorio origin (repositorio origen de la clonación) deberíamos usar el comando "git push --force …” porque los commits son incompatibles. Utilizando la opción --force o -f se sobre-escriben los commits antiguos.

**¡Atencion!** los commits antiguos se pierden al sobre-escribirlos y no podrán ser recuperados en ese repositorio. En un desarrollo real no se deben compartir repositorios, ni ramas que vayan a ser sobre-escritas posteriormente. Los commits añadidos por terceros a las copias del repositorio no sobreescrito serán incompatibles con los commits nuevos creados sobre las antiguas ramas.

### Entrega
* Añade la URL de los repositorios a la tarea.
* Recuerda que el repositorio tiene que ser publico.
* El nombre del repositorio sera: ID_XXXX_tf_agenda
    - ID es el identificador de la tarea
    - XXXX tus iniciales

* Asegurate que funciona y:
  * **10%:**  Existe el repositorio **MOOC_git_mod6-tf_agenda**
  * **20%:**  El primer commit de la rama **corrected_tf_agenda** el original:    f6e660e Add John tf
  * **35%:**  El segundo commit de la rama **corrected_tf_agenda** es "Add Eva tf    integrated" y contiene los 2 originales integrados
  * **35%:**  El tercer commit de la rama **corrected_tf_agenda** es "Add Mary tf   fixed" y contiene el original corregido

### Apoyo

* https://revilofe.github.io

### Fuente

Juan Quemada, DIT - UPM


