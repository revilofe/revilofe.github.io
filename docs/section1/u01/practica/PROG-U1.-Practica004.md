---
title: "UD 1 - P4: Ramas y GitHub"
summary: Ramas y GitHub
description: Gestión de ramas con Git y enlazar a GitHub
authors:
    - Diego Cano
date: 2023-09-16
icon: 
permalink: /prog/unidad1/p1.4
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

## P1.4 - Gestión de ramas con Git y enlazar a GitHub

[¿Qué es una rama?](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-%C2%BFQu%C3%A9-es-una-rama%3F)

![Ramas de un proyecto](https://git-scm.com/book/en/v2/images/basic-branching-6.png)

[Procedimientos básicos para ramificar y fusionar](https://git-scm.com/book/es/v2/Ramificaciones-en-Git-Procedimientos-B%C3%A1sicos-para-Ramificar-y-Fusionar)

Vamos a comenzar la práctica donde lo dejamos en la práctica anterior, P3.

1. Abrimos Git Bash y nos movemos a la carpeta de nuestro proyecto. Ahora vamos a ejecutar un comando para crear una ***rama nueva*** y también nos va a situar en ella:

    `git checkout -b desEjercicios1`
	
    Ahora estamos en otra rama de desarrollo, no en **main** *(la rama principal)*. En esta nueva rama vamos a tener todos los ficheros de la rama main tal y cómo están en este mismo momento *(cómo si hubiéramos sacado una foto exacta)*.

2. A continuación, creamos un directorio con el nombre ejercicios1, y dentro de esta nueva carpeta, creamos un programa que se llame *prueba2.py* que solicite dos números, los sume y muestre el resultado:

	num1 = int(input("Dame un número: "))  
	num2 = int(input("Dame otro: "))  
	print("La suma " + str(num1) + " + " + str(num2) + " es igual a " + str(num1 + num2))  
	print(f"{num1} + {num2} = {num1+num2}")  

3. Añadimos el fichero al área de preparación:

	`git add .`

4. Observad que PyCharm tiene integrado Git y podéis hacerlo también desde el mismo IDE, ya que ha detectado que el proyecto está gestionado por Git *(haciendo clic con el botón derecho del ratón encima del fichero aparecen las opciones de Git)*

5. Después hacemos Commit para pasarlo al repositorio:

	`git commit -m "Creado el programa prueba2"`

6. Si nos cambiamos de nuevo a la rama main, podemos observar cómo desaparece el fichero *prueba2.py*:

	`git checkout main`  
	`ls -l`  
    `ls ejercicios1`  
	`git status`  

7. Si cambiamos a la rama desEjercicios1 volverá a aparecer *prueba2.py*:

	`git checkout desEjercicios1`  
	`ls ejercicios1`  
	`git status`  

8. Si ya hemos acabado el trabajo en nuestra rama y queremos actualizar todas las modificaciones a la rama principal, debemos ***FUSIONAR*** los cambios de la rama *desEjercicios1* con la rama *main*:

	`git checkout master`  
	`git merge desEjercicios1`
	
9. Si hay conflictos y falla hacemos lo siguiente para arreglarlo y forzar la fusión manteniendo los cambios realizados en desEjercicios1 *(en un IDE es más sencillo)*:
	
	`git merge --abort`  
	`git rebase desEjercicios1`  
	`git rebase --skip`  

10. Para ver las ramas que tengo:

	`git branch`
	
11. Si estando en la rama main creo un fichero nuevo o una modificación, pero me olvido de añadirlo con `add` y hacer `commit`, y cambio de rama... pues me estoy llevando todo los cambios a la rama a la que nos hemos cambiado por no haber hecho `commit`.

12. Si no quiero hacer Commit en ese momento porque mis cambios aún no son definitivos, podemos dejarlo en un área temporal...

	`git stash`

13. Me cambio de rama ya sin problemas y al volver de nuevo a mi rama para seguir trabajando en los cambios revierto el stash:

	`git stash pop`
	
14. También puedo hacer los `stash` que queramos con:

	`git stash save "Primer stash"`
	
15. Para ver los stash que tengo:

	`git stash list`
	
16. Para recuperar uno en concreto de la lista:

	`git stash pop stash@{2}`
	
17. Para eliminar una rama:

	`git branch -d nombreRama`
	
## Gestión del proyecto enlazado con Github

18. Lo primero que debemos hacer es ir a la página web de [GitHub](https://github.com/) y registrarnos con nuestro correo corporativo de `@g.educaand.es`

    [GitHub - Creación y configuración de la cuenta](https://git-scm.com/book/es/v2/GitHub-Creaci%C3%B3n-y-configuraci%C3%B3n-de-la-cuenta)
 
19. Después crearemos un repositorio en GitHub (para más información podéis acceder a la documentación de GitHub, [Creación de un repositorio](https://docs.github.com/es/get-started/quickstart/create-a-repo)). El nombre del repositorio puede ser el siguiente, dependiendo del curso dónde estés:

- DAM1_ProgPhyton
- DAW1A_ProgPython
- DAW1B_ProgPython

20. Ahora ya tenemos nuestro proyecto gestionado por Git en local y un repositorio en la nube. Para enlazarlos y así estar tranquilos que nuestros ficheros nunca se van a perder seguiremos las instrucciones que nos proporciona GitHub al crearnos el nuevo repositorio para conectarlo con mi repo local... por ejemplo, si lo hubiéramos llamado PruebasProgPython y mi usuario de GitHub fuera dcansib438, nos generaría un comando similar al siguiente *(lo copiamos y pegamos en Git Bash)*:

    `git remote add origin https://github.com/dcansib438/PruebasProgPhyton.git`

Para subir cambios a Github:

	`git push origin main`

Para descargar los cambios que se hayan realizado en Github, realizados desde otro ordenador u otro desarrollador distinto:

	`git pull origin main`

