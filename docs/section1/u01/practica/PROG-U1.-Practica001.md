---
title: "UD 1 - P1: Mi primer programa - Windows"
summary: Mi primer programa
description: Mi primer programa
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: 
permalink: /prog/unidad1/p1.1
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

## P1.1 - Mi primer programa - Windows

A continuación, ofrecemos una guía paso a paso para aquellos usuarios principiantes interesados en aprender Python con Windows.

### 1. Configurar el entorno de desarrollo

Si eres un usuario principiante y no estás familiarizado con Python, te recomendamos [instalar Python desde Microsoft Store](https://www.microsoft.com/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab). La instalación a través de Microsoft Store utiliza el intérprete de Python3 básico, pero controla el establecimiento de la configuración del valor PATH para el usuario actual (lo que evita la necesidad de contar con acceso de administrador) y, además, proporciona actualizaciones automáticas. Resulta especialmente útil si te encuentras en un entorno educativo o en un departamento de una organización que restringe los permisos o el acceso administrativo en la máquina.

### 2. Instalar Python

Para instalar Python con Microsoft Store:

1. Ve al menú **Inicio** (icono de Windows de la esquina inferior izquierda), escribe "Microsoft Store" y selecciona el vínculo para abrir Store.
2. Una vez que lo hayas abierto, selecciona **Buscar** en el menú superior derecho y escribe "Python". Seleccione la versión de Python que quiera usar en los resultados de la opción Aplicaciones. Se recomienda usar la más reciente, a menos que tenga una razón para no hacerlo (por ejemplo, alinearse con la versión que se usó en un proyecto existente en el que planea trabajar). Una vez que haya determinado qué versión quiere instalar, seleccione  **Obtener** .
3. Una vez que Python haya completado el proceso de descarga e instalación, abre Windows PowerShell mediante el menú **Inicio** (icono de Windows de la esquina inferior izquierda). Cuando PowerShell esté abierto, escribe `Python --version` para confirmar que Python3 está instalado en la máquina.
4. La instalación de Microsoft Store de Python incluye  **PIP** , el administrador de paquetes estándar. PIP te permite instalar y administrar paquetes adicionales que no forman parte de la biblioteca estándar de Python. Para confirmar que también dispones de PIP para instalar y administrar paquetes, escribe `pip --version`.

### 3. Instalar Visual Studio Code

Al usar VS Code como editor de texto/entorno de desarrollo integrado (IDE), puedes aprovechar [IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) (una ayuda de finalización de código), el [detector de errores](https://code.visualstudio.com/docs/python/linting) (permite evitar que se produzcan errores en el código), el [soporte técnico de depuración](https://code.visualstudio.com/docs/python/debugging) (ayuda a buscar errores en el código después de ejecutarlo), los [fragmentos de código](https://code.visualstudio.com/docs/editor/userdefinedsnippets) (plantillas para pequeños bloques de código reutilizables) y las [pruebas unitarias](https://code.visualstudio.com/docs/python/unit-testing) (para probar la interfaz del código con distintos tipos de entrada).

VS Code también contiene un [terminal integrado](https://code.visualstudio.com/docs/editor/integrated-terminal) que te permite abrir una línea de comandos de Python con el símbolo del sistema de Windows, PowerShell o cualquier otra herramienta que prefieras, y establece un flujo de trabajo sin interrupciones entre el editor de código y la línea de comandos.

1. Para instalar VS Code, descarga VS Code para Windows: [https://code.visualstudio.com](https://code.visualstudio.com/).
2. Una vez instalado VS Code, también debes instalar la extensión de Python. Para instalar la extensión de Python, puedes seleccionar el [vínculo para VS Code de Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python) o abrir VS Code y buscar **Python** en el menú de extensiones (Control + Mayús + X).
3. Python es un lenguaje interpretado y, para ejecutar el código de Python, debes indicar a VS Code el intérprete que debe usar. Se recomienda usar la versión más reciente de Python, a menos que tenga una razón específica para elegir alguna diferente. Después de instalar la extensión de Python, selecciona un intérprete de Python 3. Para ello, abre la **paleta de comandos** (Control + Mayús + P) y empieza a escribir el comando **Python: Select Interpreter** para buscarlo y, luego, selecciónalo. También puedes usar la opción **Select Python Environment** (Seleccionar entorno de Python) en la barra de estado inferior si está disponible (es posible que ya se muestre un intérprete seleccionado). El comando presenta una lista de los intérpretes disponibles que VS Code puede buscar automáticamente, incluidos los entornos virtuales. Si no ves el intérprete que quieres, consulta [Configuración de los entornos de Python](https://code.visualstudio.com/docs/python/environments).
   ![Select Python interpreter in VS Code](https://learn.microsoft.com/es-es/windows/images/interpreterselection.gif)
4. Para abrir el terminal en VS Code, selecciona  **Ver** > **Terminal** , o bien usa el acceso directo **Control + `** (mediante el carácter de tilde aguda). El terminal predeterminado es PowerShell.
5. En el terminal de VS Code, simplemente escribe el comando `python` para abrir Python.
6. Para probar el intérprete de Python, escribe `print("Hello World")`. Python devolverá la instrucción "Hola mundo".
   ![Python command line in VS Code](https://learn.microsoft.com/es-es/windows/images/python-in-vscode.png)

### 4. Instalar GIT (opcional)

Si planeas colaborar con otras personas en el código de Python u hospedar el proyecto en un sitio de código abierto (como GitHub), VS Code admite el [control de versiones con GIT](https://code.visualstudio.com/docs/editor/versioncontrol#_git-support). La pestaña Control de código fuente de VS Code realiza un seguimiento de todos los cambios y tiene comandos GIT comunes (agregar, confirmar, enviar cambios e incorporar cambios) integrados directamente en la interfaz de usuario. Primero, debes instalar GIT para alimentar el panel de control de código fuente.

1. Descarga e instala GIT para Windows desde el [sitio web git-scm](https://git-scm.com/download/win).
2. Se incluye un asistente para instalación que te formulará una serie de preguntas sobre la configuración de la instalación de GIT. Te recomendamos que uses todas las opciones de configuración predeterminadas, a menos que tengas un motivo concreto para cambiar algo.
3. Si nunca has trabajado con GIT, las [guías de GitHub](https://guides.github.com/) pueden resultarte de ayuda para empezar.

### 5. Tutorial de Hola mundo para algunos aspectos básicos de Python
Python, según su creador Guido van Rossum, es un "lenguaje de programación de alto nivel y su filosofía de diseño básico trata sobre la legibilidad del código y una sintaxis que permite a los programadores expresar conceptos en unas pocas líneas de código".

Python es un lenguaje interpretado. A diferencia de los lenguajes compilados, en los que el código que escribes debe traducirse en código máquina para que lo ejecute el procesador del equipo, el código de Python se pasa a un intérprete y se ejecuta directamente. Solo tienes que escribir el código y ejecutarlo. Probémoslo.

1. Con la línea de comandos de PowerShell abierta, escribe `python` para ejecutar el intérprete de Python 3. (Algunas instrucciones prefieren usar el comando `py` o `python3` y también deberían funcionar). Sabrá que se ha ejecutado correctamente porque se mostrará un aviso >>> con tres símbolos de "mayor que" .
2. Hay varios métodos integrados que permiten realizar modificaciones en las cadenas de Python. Crea una variable con `variable = 'Hello World!'`. Presiona Entrar para que se muestre una nueva línea.
3. Imprime la variable con `print(variable)`. Se mostrará el texto "Hello World!".
4. Averigua la longitud (el número de caracteres que se usan) de la variable de cadena con `len(variable)`. Se mostrará que se usan 12 caracteres. (Ten en cuenta que el espacio en blanco se cuenta como un carácter en la longitud total).
5. Convierte la variable de cadena en letras mayúsculas: `variable.upper()`. Convierte la variable de cadena en letras minúsculas: `variable.lower()`.
6. Cuenta el número de veces que se usa la letra "l" en la variable de cadena: `variable.count("l")`.
7. Busca un carácter específico en la variable de cadena. En este caso, buscaremos el signo de exclamación con `variable.find("!")`. Se mostrará que el signo de exclamación se encuentra en el carácter undécimo de la cadena.
8. Reemplaza el signo de exclamación por un signo de interrogación: `variable.replace("!", "?")`.
9. Para salir de Python, puedes escribir `exit()` o `quit()`, o seleccionar Control-Z.

![PowerShell screenshot of this tutorial](https://learn.microsoft.com/es-es/windows/images/hello-world-basics.png)

Lo que acabas de ver, son algunos de los métodos de modificación de cadenas integrados de Python. Ahora intenta crear un archivo de programa de Python y ejecutarlo con VS Code.

### 6. Tutorial Hola mundo para usar Python con VS Code

El equipo de VS Code ha elaborado el excelente tutorial [Introducción a Python](https://code.visualstudio.com/docs/python/python-tutorial#_start-vs-code-in-a-project-workspace-folder) en el que se explica cómo crear un programa Hola mundo con Python, ejecutar el archivo de programa, configurar y ejecutar el depurador e instalar paquetes como *matplotlib* y *NumPy* para crear un trazado gráfico dentro de un entorno virtual.

1. Abre PowerShell y crea una carpeta vacía denominada "hello", navega a esta carpeta y ábrela en VS Code:
   **Consola**Copiar

   ```
   mkdir hello
   cd hello
   code .
   ```
2. Una vez que se abra VS Code y se muestre la nueva carpeta *Hello* en la ventana **Explorador** del lado izquierdo, abra una ventana de línea de comandos en el panel inferior de VS Code. Para ello, presione **Control + `** (mediante el carácter de tilde aguda) o seleccione  **Ver** > **Terminal** . Al iniciar VS Code en una carpeta, esa carpeta se convierte en tu "área de trabajo". VS Code almacena la configuración específica de esa área de trabajo en. vscode/settings.json, que es independiente de la configuración de usuario que se almacena globalmente.
3. Continúa con el tutorial en la documentación de VS Code: [Creación de un archivo de código fuente de Hola mundo de Python](https://code.visualstudio.com/docs/python/python-tutorial#_create-a-python-hello-world-source-code-file).


## Fuente
* [Introducción a Python](https://learn.microsoft.com/es-es/windows/python/)
* [Introducción para principiantes](https://learn.microsoft.com/es-es/windows/python/beginners)