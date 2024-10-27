---
title: "UD 2 - 2.2 Gestión de módulos y extensiones "
description: Gestión de módulos y extensiones
summary: Gestión de módulos y extensiones
authors:
    - Eduardo Fdez
date: 2024-10-21
icon:   
permalink: /edes/unidad2/2.2
categories:
    - EDES
tags:
    - EDES
    - IDE
    - Modulos
---

## 2.2. Gestión de módulos y extensiones

Los **módulos** y **extensiones** son pequeños complementos o "plugins" que puedes agregar a tu IDE para dotarlo de nuevas funcionalidades.

En este punto aprenderemos qué son los módulos y extensiones, cómo instalarlos, gestionarlos y por qué son fundamentales para mejorar nuestra productividad.

### 1. Introducción

Cuando trabajamos con entornos de desarrollo integrados (IDEs, aunque alguna veces nos referiremos con IDES tambien a editores potentes como Visual Studio Code, Fleet) como **Visual Studio Code** o los de **JetBrains** (IntelliJ IDEA, PyCharm, Fleet), una de sus grandes ventajas es la **flexibilidad**. Esta flexibilidad se consigue a través de los **módulos** y **extensiones** que podemos añadir para personalizar y ampliar las capacidades del IDE. 

### 2. ¿Qué son los módulos y las extensiones?

#### 2.1. Definición

Los **módulos** y **extensiones** son pequeños complementos o "plugins" que puedes agregar a tu IDE para dotarlo de nuevas funcionalidades. Estas funcionalidades pueden incluir:

- Soporte para nuevos lenguajes de programación.   
- Herramientas de depuración avanzadas.   
- Integración con frameworks populares (como React o Django).   
- Herramientas de diseño de interfaces gráficas.   
- Conexión con bases de datos o servidores.   

En resumen, permiten **personalizar** el entorno según tus necesidades, añadiendo únicamente las herramientas que vas a utilizar en tu proyecto. Así, no sobrecargas el IDE con funciones que no necesitas.   

#### 2.2. Ejemplo práctico de extensiones en Visual Studio Code

Visual Studio Code es conocido por ser un **editor** ligero y altamente extensible. Por defecto, cuando lo instalas, solo incluye las herramientas más básicas, pero puedes adaptarlo a casi cualquier tipo de desarrollo añadiendo extensiones.    

**Ejemplo**: Imagina que quieres desarrollar una página web utilizando **HTML, CSS y JavaScript**. Al abrir Visual Studio Code, notarás que el soporte para estos lenguajes es básico. Sin embargo, al agregar extensiones específicas, puedes tener un entorno completamente optimizado para el desarrollo web.   

### 3. Instalación de extensiones en Visual Studio Code

Aunque se dan instrucciones para instalar extensiones y módulos en distintos IDES, al final se proporcionan enlaces a la documentación oficial de los productos para seguir los pasos. Esta información puede variar con el tiempo, por lo que es recomendable consultar la documentación oficial para obtener la información más actualizada.

#### 3.1. Acceso al Marketplace de extensiones

1. Abre Visual Studio Code.   
2. En el panel de la izquierda, verás un ícono de **cuadrado** con otro más pequeño en la esquina (es el icono del **Marketplace de Extensiones**). Haz clic en él.   
3. Se abrirá una barra de búsqueda donde podrás buscar extensiones para añadir.   

#### 3.2. Instalación de una extensión

Supongamos que estás desarrollando en **Python** y necesitas añadir soporte completo para este lenguaje.

1. En el Marketplace de Extensiones, escribe "Python" en la barra de búsqueda.    
2. Selecciona la extensión llamada **Python** (desarrollada por Microsoft) de los resultados.   
3. Haz clic en el botón **Instalar**. En unos segundos, tu IDE tendrá completo soporte para Python, incluyendo autocompletado, depuración y análisis de errores.   

#### 3.3. Instalación de linting y formateadores de código
Los **linters** y **formateadores de código** son extensiones que te ayudan a mantener un código limpio y consistente.
    - linters: Verifican tu código en busca de errores y malas prácticas. Por ejemplo, si escribiste una variable que nunca usas, el linter te lo indicará, o por ejemplo si tienes una variable que no sigue la convención de nombres.
    - Formateadores: Ajustan automáticamente el formato de tu código según unas reglas predefinidas. Por ejemplo si tienes un código con sangrías incorrectas, el formateador lo corregirá.

Existen extensiones que te permiten utilizar estas herramientas en Visual Studio Code y Pycharm. A continuación, te proporciono una URL para seguir los pasos a través de un articulo:
    - [Configurar linter y formatter en VSC](https://leanmind.es/es/blog/como-configurar-linter-y-formatter-de-python-en-vscode/)

Estas extensiones no solo te ayudarán a escribir código más rápido, sino que también te aseguran que sigues buenas prácticas en tu proyecto.

#### 3.4. Instalación de múltiples extensiones para un proyecto web

Si estás desarrollando una aplicación web en **JavaScript** con el framework **React**, podrías necesitar varias extensiones.

1. Busca e instala:
    - **ESLint**: Para verificar y corregir errores de estilo de código en JavaScript.   
    - **Prettier**: Para formatear tu código automáticamente según unas reglas predefinidas.   
    - **React**: Para tener snippets y autocompletado específicos de React.

### 4. Gestión de módulos en JetBrains (IntelliJ IDEA, PyCharm)

Los entornos de JetBrains también permiten una gran personalización mediante **módulos** y **plugins**. Estos módulos se instalan y gestionan directamente desde el IDE, y están orientados a proyectos más complejos o lenguajes específicos.   

#### 4.1. ¿Qué es un módulo en JetBrains?

Un **módulo** en JetBrains es un conjunto de archivos y configuraciones que añaden soporte para ciertos lenguajes o frameworks en tu proyecto. Si trabajas con **Python**, puedes instalar el módulo de Python, y además añadir un modulo para Django si trabajas con este framework. O si estas en IntelliJ IDEA  y trabajas con **Java** o **kotlin**, puedes instalar un módulo para soportar el framework Spring. IntelliJ IDEA y PyCharm tienen módulos específicos para cada lenguaje y framework, lo que te permite personalizar tu entorno de desarrollo según tus necesidades.

#### 4.2. Instalación de módulos en IntelliJ IDEA

1. Abre IntelliJ IDEA.   
2. Dirígete a la barra superior y selecciona `File > Project Structure`.   
3. En la ventana de estructura de proyecto, selecciona la opción **Modules** y haz clic en **+** para añadir un nuevo módulo.   
4. Elige el tipo de módulo que quieres instalar, por ejemplo, **Java**, **Kotlin**, o **Spring**. Sigue las indicaciones del asistente para configurarlo.    
  
#### 4.3. Instalación de plugins en JetBrains (PyCharm)

Además de los módulos, JetBrains permite la instalación de **plugins** que amplían las capacidades de su IDE de forma similar a las extensiones de Visual Studio Code.

1. En la barra superior, ve a `File > Settings` (o `Preferences` en Mac).   
2. Selecciona la opción **Plugins**.   
3. En el campo de búsqueda, escribe el nombre del plugin que necesitas. Por ejemplo, si trabajas con Kotest (framework de pruebas unitarias para kotlin), puedes buscar el plugin Kotest.   
4. Haz clic en **Instalar** y reinicia el IDE para que los cambios se apliquen.   

#### 4.3. Instalación de linting y formateadores de código
Como hemos dicho, los **linters** y **formateadores de código** son extensiones que te ayudan a mantener un código limpio y consistente.

Existen extensiones que te permiten utilizar estas herramientas en Pycharm. A continuación, te proporciono una URL para seguir los pasos a través de un articulos.
     - [Configurar linter y formatter en pycharm](https://leanmind.es/es/blog/como-configurar-un-linter-y-formatter-en-pycharm/)

### 5. Desinstalación y actualización de extensiones y módulos

#### 5.1. Desinstalación en Visual Studio Code

Si en algún momento ya no necesitas una extensión, puedes desinstalarla fácilmente.   

1. Abre el panel de extensiones en Visual Studio Code (`Ctrl + Shift + X`).   
2. Encuentra la extensión que deseas desinstalar.   
3. Haz clic en el botón de la **papelera** que aparece junto a su nombre.   

#### 5.2. Actualización de extensiones en Visual Studio Code

Visual Studio Code te notificará automáticamente cuando haya actualizaciones disponibles para tus extensiones. Solo tienes que hacer clic en el botón de **Actualizar** que aparecerá junto a la extensión en el Marketplace.   

#### 5.3. Gestión de módulos y plugins en JetBrains

Desde `File > Settings > Plugins`, puedes gestionar tus plugins instalados: desactivarlos temporalmente, actualizarlos o desinstalarlos por completo. Esto te permite mantener tu IDE optimizado y evitar sobrecargarlo con funcionalidades innecesarias.   

### 6. Enlaces y recursos de interés
Siguiendo los siguientes enlaces podrás instalar extensiones y plugins en Visual Studio Code y los IDEs de JetBrains:   


#### 6.1. Extensiónes en Visual Studio Code

- [Extensiones en markeplace](https://code.visualstudio.com/docs/editor/extension-marketplace)
- [Using extensions in Visual Studio Code](https://code.visualstudio.com/docs/introvideos/extend)
- [Instalación de la extensión de Python](https://learn.microsoft.com/es-es/training/modules/python-install-vscode/5-exercise-install-python-extension?pivots=linux)

#### 6.2. Extensiónes en herramientas Jetbrains

- [Instalando plugins en pycharm](https://www.jetbrains.com/help/pycharm/managing-plugins.html)
- [Plugins en pycharm](https://www.jetbrains.com/help/pycharm/plugins-settings.html)
- [Instalando plugins en IDEA](https://www.jetbrains.com/help/idea/managing-plugins.html)
- [Plugins en IDEA](https://www.jetbrains.com/help/idea/plugins-settings.html)


### 7. Conclusión

La gestión de **módulos** y **extensiones** es una parte fundamental para personalizar tu entorno de desarrollo y ajustarlo a las necesidades de tu proyecto. Tanto en **Visual Studio Code** como en los **IDEs de JetBrains**, puedes añadir o eliminar funcionalidades según lo que vayas necesitando. Esto te permite trabajar de forma más eficiente, ahorrando tiempo y mejorando la calidad de tu código. ¡Aprovecha todas las herramientas a tu disposición para hacer que tu entorno de desarrollo sea perfecto para ti!