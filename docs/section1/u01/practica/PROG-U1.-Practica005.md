---
title: "UD 1 - P5: Virtualenv con Pytest"
summary: Virtualenv con Pytest
description: Creación de un entorno virtual con Pytest
authors:
    - Diego Cano
date: 2023-09-29
icon: 
permalink: /prog/unidad1/p1.5
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

## P1.5 - Creación de un entorno virtual con Pytest

### 1. Introducción

Los `entornos virtuales` se pueden describir como directorios de instalación aislados. Este aislamiento te permite localizar la instalación de las dependencias de tu proyecto, sin obligarte a instalarlas en todo el sistema.

Se trata de un entorno Python en el que el intérprete Python, las bibliotecas y los scripts instalados en él están aislados de los instalados en otros entornos virtuales, y *(por defecto)* cualquier biblioteca instalada en un «sistema» Python, es decir, uno que esté instalado como parte de tu sistema operativo.

`Virtualenv` es una herramienta que se utiliza para crear entornos Python aislados. Crea una carpeta que contiene todos los ejecutables necesarios para usar los paquetes que necesitaría un proyecto de Python.

### 2. Pasos a seguir en la práctica

#### 2.1. Antes de nada, debemos abrir una carpeta en Visual Studio Code, donde vamos a trabajar con nuestros programas de Python. (por ejemplo en **~/Documentos/practica5**)

   Podemos hacerlo de varias formas:
  
   * Desde una terminal de tu sistema operativo, navegando donde queramos crear el directorio y usando el comando `mkdir nombreCarpeta`. Posteriormente accederemos a la nueva carpeta *(`cd`)* creada y ejecutaremos el comando `code .`.

   * A nivel gráfico, desde el `Explorador de archivos`, creando una carpeta y arrastrándola dentro de `Visual Studio Code`.

   * También podemos hacerlo desde `Visual Studio Code`, en el menú `File -> Open Folder`, navegaremos a la carpeta o la crearemos, después simplemente pulsamos en el botón `Seleccionar carpeta`.

#### 2.2. A continuación abrimos la consola dentro del IDE:

   Teclas rápidas `Ctrl+ñ` o desde el menú `View -> Terminal`

#### 2.3. Instalamos virtualenv con el siguiente comando:

   ```
   pip install virtualenv
   ```

#### 2.4. Para comprobar su versión:

   ```
   virtualenv --version
   ```
	
#### 2.5. Creamos ahora un entorno virtual:

   ```
   python -m virtualenv venv
   ```

#### 2.6. El entorno virtual crea físicamente una carpeta llamada venv, donde gestionará todas las librerías que instalemos.

#### 2.7. Para utilizar el entorno virtual debemos activarlo:

   ```
   .\venv\Scripts\activate
   ```

   * Si se produce un error que indica que "la ejecución de scripts está deshabilitada en el sistema"... debéis abrir como **Administrador** `Windows PowerShell` y ejecutar el siguiente comando:

   ```
   Set-ExecutionPolicy RemoteSigned
   ```

   * Este error ocurre porque, en PowerShell, la ejecución de scripts está deshabilitada por motivos de seguridad. Para solucionarlo, necesitas cambiar la política de ejecución para permitir la ejecución de scripts.

   * El parámetro `RemoteSigned`: Permite ejecutar scripts locales **no firmados**, pero los scripts descargados de Internet necesitarán estar firmados.

   * Si en un futuro quiers volver a la configuración original, solo tienes que ejecutar el mismo comando con el parámetro `Restricted`:

   ```
   Set-ExecutionPolicy Restricted
   ```

#### 2.8. Si queremos comprobar los paquetes instalados en el entorno virtual ejecutamos el siguiente comando:

   ```
   pip list
   ```
 
#### 2.9. Para comprobar que tenemos la última versión de pip y actualizarla:

   ```
   python -m pip install --upgrade pip
   ```

#### 2.10. Ya tenemos el entorno virtual preparado y activado para usarlo en nuestro proyecto. Vamos a instalar pytest, que nos van a ayudar a ejecutar las pruebas unitarias:

   ```
   pip install pytest
   ```
 
#### 2.11. Podemos volver a revisar los paquetes instalados y vemos cómo nos ha instalado pytest y otros paquetes necesarios:

   ```
   pip list
   ```
 	
#### 2.12. Para comprobar la versión que tenemos instalada de pytest:

   ```
   pytest --version
   ```
 
#### 2.13. Si necesitamos desactivar el entorno virtual

   ```
   deactivate
   ```
 
#### 2.14. Para exportar los paquetes que tenemos instalados, por si los queremos instalarlos en otro entorno posteriormente:

   ```
   pip freeze > requirements.txt
   ```

#### 2.15. Para importarlos en otro entorno virtual de otra carpeta o proyecto:

   ```
   pip install -r requirements.txt
   ```
 

## Fuentes:

*	[Creación de entornos virtuales](https://docs.python.org/es/3.8/library/venv.html)
* [Entornos virtuales de Python explicados con ejemplos](https://www.freecodecamp.org/espanol/news/entornos-virtuales-de-python-explicados-con-ejemplos/)
