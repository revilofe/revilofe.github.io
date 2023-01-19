---
title: "UD 3 - P3: Git/Github Rebase I"
description: Git/Github
summary: Git/Github
authors:
    - Eduardo Fdez
date: 2022-10-23
icon: material/software
permalink: /edes/unidad3/p3.3
categories:
    - EDES
tags:
    - Software
    - git
    - github
---

## Relación 3.1.3: Integración de ramas - Rebase I

### Objetivos
* Continuar practicando con repositorios locales y remotos, commits y ramas, pero integrando con rebase.

### Descripción de la práctica

Reutilizar la cuenta y el repositorio my_calculator en GitHub tal y como quedó en la entrega anterior. Crear una nueva rama que parta del primer commit de main "x^3 button" con el nombre "ops". Crear dos commits en la nueva rama "ops", el primero añade el botón x^2 y el segundo con el botón 1/x. Integrar la nueva rama ops en la rama main utilizando "git rebase ...".

Para terminar se deben subir los nuevos commits integrados en la rama "main" a un nuevo repositorio en su cuenta de GitHub, denominado "my_calculator_2".

El grafo de commits es más fácil de seguir cuando se integra con rebase, ya que todos los commits de la rama lateral pasan a main y todo queda en main. En cambio se pierde algo de la historia del proyecto, porque desaparecen las ramas laterales donde se suelen desarrollar las nuevas funcionalidades. Rebase tiene además la opción interactiva que permite rehacer la rama que se integra y sus commits. Por esta razón hay personas que prefieren el rebase frente al merge para integrar desarrollos.

¡Cuidado! Las ramas que se hayan compartido con terceros no deben modificarse con rebase, porque si un tercero ha descargado la rama, deberá repetir el rebase en su repositorio local.

### Tareas a realizar

#### Paso 1: Clonar el repositorio "my calculator"

El primer paso será clonar en un repositorio local el repositorio "my_calculator" de GitHub en un directorio "my_calculator_2". Se debe haber terminado el desarrollo de la práctica anterior previamente a la realización de esta entrega.

```
$ git clone git@github.com:<mi_usuario_de_github>/my_calculator   my_calculator_2 
$ cd my_calculator_2
``` 

#### Paso 2: Nueva rama

El siguiente paso será crear una rama de nombre "ops" que comience después del primer commit (con mensaje "x^3 button") de la rama "main" y restaurarla en el directorio de trabajo, para poder trabajar sobre ella. Es necesario consultar el id del commit "x^3 button" para poder crear la rama a partir del mismo

```
$ git log --oneline # Lista los commits existentes incluyendo su id
$ git checkout -b ops <id_de_commit> # Crea una nueva rama llamada "ops" a partir del commit indicado
```


#### Paso 3: Funcionalidad x^2
Crear un commit en la rama "ops", que añada a la calculadora del fichero index.html el botón x^2 que eleve un número al cuadrado.

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Calculator</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>Calculadora de ……su nombre y apellidos……</h1>
		Number:
		<input type="text" id="n1">
		<p>
			<button onclick="square()"> x^2 </button>
			<button onclick="cube()"> x^3 </button>
		</p>
		<script type="text/javascript">
			function cube() {
				var num = document.getElementById("n1");
				num.value = Math.pow(num.value, 3);
			}
			function square() {
				var num = document.getElementById("n1");
				num.value = Math.pow(num.value, 2);
			}
		</script>
	</body>
</html>
```

Una vez añadido el código del nuevo nuevo botón a la calculadora, comprobar que funciona correctamente, registrar los cambios en el índice y crear el nuevo commit.

```
$ git add index.html
$ git commit -m "x^2 button"
```
#### Paso 4: Funcionalidad 1/x

Crear un commit en la rama "ops", que añada a la calculadora del fichero index.html el botón 1/x que divida 1 entre el número introducido.

```html
<!DOCTYPE html>
<html>
	<head>
		<title>Calculator</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>Calculadora de ……su nombre y apellidos……</h1>
		Number:
		<input type="text" id="n1">
		<p>
			<button onclick="inverse()"> 1/x </button>
			<button onclick="square()"> x^2 </button>
			<button onclick="cube()"> x^3 </button>
		</p>
		<script type="text/javascript">
			function cube() {
				var num = document.getElementById("n1");
				num.value = Math.pow(num.value, 3);
			}
			function square() {
				var num = document.getElementById("n1");
				num.value = Math.pow(num.value, 2);
			}
			function inverse() {
				var num = document.getElementById("n1");
				num.value = 1/num.value;
			}
		</script>
	</body>
</html>
```

Una vez añadido el código del nuevo nuevo botón a la calculadora, comprobar que funciona correctamente, registrar los cambios en el índice y crear el nuevo commit.

```
$ git add index.html
$ git commit -m "1/x button"
```

#### Paso 5: Integrar la rama "ops" en "main"

Integrar la rama ops en la rama main con "git rebase" para crear una calculadora con cinco
botones: x^2, x^3, x^4, sin(x) y 1/x.

"git rebase …" realiza la integración ejecutando un bucle, donde cada iteración traslada un commit de la rama origen a su nueva base. El traslado implica integrar el código del commit con el de su nueva base. Si la integración tiene conflictos, git indica el error y finaliza.

"git status" muestra los ficheros con conflictos. Los conflictos deben resolverse entonces con el editor.

Primero comprobamos el id del commit que queremos integrar en main (el de "1/x button")
```
git log --oneline
```

Nos cambiamos a la rama "main" y ejecutamos

```
$ git checkout main
$ git rebase <id del commit>
```

Como hemos modificado el mismo fichero y las mismas líneas que en los commits posteriores de la rama "main" surgirán conflictos.
Debemos editar el fichero index.html para eliminar los conflictos.

Una vez resueltos, se debe comprobar primero que la integración funciona correctamente. Después se debe continuar la integración (rebase) añadiendo los cambios al índice y continuando el rebase:

```
$ git add index.html
$ git rebase --continue
```

Una vez generado un commit, git pasa a intentar integrar el siguiente de la rama origen. Y así hasta el último de la rama origen. Es necesario guardar los cambios en el editor que sale al hacer el rebase para que se apliquen.

Este proceso habrá que repetirlo dos veces: la primera vez para el botón x^4 y la segunda para el botón sin(x).

El resultado final de index.html tendrá los 5 botones: x^2, x^3, x^4, sin(x) y 1/x.

#### Paso 6: Subir todas las ramas del repositorio local a un nuevo repositorio en GitHub.

Creamos un nuevo repositorio en Github llamado "my_calculator_2". Por último, subimos los cambios realizados en ambas ramas a Github.

```
$ git remote set-url origin git@github.com:<mi_usuario_de_github>/my_calculator_2
$ git push --all
```

La opción --force o -f permite subir un repositorio incompatible, pero ¡Cuidado borra el existente! Se debe utilizar solo en casos en que no hay otra solución.


### Entrega
* Añade la URL de los repositorios a la tarea.
* Recuerda que el repositorio tiene que ser publico.
* El nombre del repositorio sera: ID_XXXX_my_calculator y ID_XXXX_my_calculator_2 donde
    - ID es el identificador de la tarea
    - XXXX tus iniciales

* Asegurate que funciona y:
    * **10%:**  Existe el repositorio my_calculator2
    * **30%:**  Los tres primeros commits de main son los originales: "x^3 button", "x^4 button" y "sin(x) button"
    * **30%:**  El cuarto commit de la rama main es "x^2 button" y contiene lo pedido
    * **30%:**  El quinto commit de la rama main es "1/x button" y contiene lo pedido

### Apoyo

* https://revilofe.github.io

### Fuente

Juan Quemada, DIT - UPM
