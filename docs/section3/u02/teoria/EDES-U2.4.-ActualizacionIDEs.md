---
title: "UD 2 - 2.4 Actualización de IDE's"
description: Personalización del entorno
summary: Personalización del entorno
authors:
    - Eduardo Fdez
date: 2024-10-21
icon: "material/file-document-outline"
permalink: /edes/unidad2/2.4
categories:
    - EDES
tags:
    - EDES
    - IDE
    - Actualizacion
---

## 2.3. Actualización de IDE's
La **actualización** de los **entornos de desarrollo integrado (IDEs)** es una tarea importante para mantener el software actualizado y seguro. En este punto, veremos cómo configurar las actualizaciones automáticas y manuales en **Visual Studio Code** y los IDEs de **JetBrains** (IntelliJ IDEA, PyCharm, Fleet) para asegurarte de que siempre estás utilizando la última versión disponible.

### 1. Introducción

Mantener tu **entorno de desarrollo integrado (IDE)** actualizado es fundamental para garantizar que siempre estés utilizando las últimas herramientas, características y correcciones de seguridad. Tanto **JetBrains** (con **PyCharm** para Python y **IntelliJ IDEA** para Kotlin) como **Visual Studio Code** ofrecen sistemas de actualización automáticos y manuales que permiten que el entorno se mantenga eficiente y libre de errores. En este punto aprenderemos a configurar el sistema de actualizaciones en ambos entornos.

### 2. ¿Por qué es importante actualizar tu IDE?

Actualizar tu IDE garantiza que estés trabajando con la última versión del software, lo que te proporciona:

- **Nuevas características**: Cada actualización suele incluir nuevas funcionalidades que mejoran la productividad.    
- **Correcciones de errores**: Los desarrolladores del IDE solucionan errores conocidos para mejorar la estabilidad del entorno.    
- **Mejoras de seguridad**: Las actualizaciones corrigen vulnerabilidades que podrían comprometer la seguridad del entorno y los proyectos en los que trabajas.    
- **Compatibilidad con nuevas tecnologías**: Las actualizaciones permiten que el IDE soporte nuevos lenguajes o frameworks, mejorando tu flujo de trabajo.     

### 3. Configuración de actualizaciones en JetBrains (PyCharm e IntelliJ IDEA)

En los IDEs de JetBrains, como **PyCharm** y **IntelliJ IDEA**, puedes configurar las actualizaciones de varias maneras. Estas incluyen la actualización automática del propio IDE y de los **plugins** que tengas instalados.      

### 3.1. Configuración de actualizaciones automáticas del IDE

Aunque si has instalado la aplicación externa **JetBrains Toolbox**, esta se encargará de mantener actualizados todos tus IDEs de JetBrains, también puedes configurar las actualizaciones directamente en el IDE.   

Aunque veremos como, recomendamos revisar la [documentación oficial de JetBrains](https://www.jetbrains.com/help/idea/update.html) para obtener información actualizada sobre cómo configurar las actualizaciones.  

1. **Accede a las configuraciones de actualización**:  
     - Abre **PyCharm** o **IntelliJ IDEA**.  
     - Dirígete a la barra superior y selecciona `File > Settings` (o `Preferences` en macOS).  
     - En el menú lateral, navega hasta `Appearance & Behavior > System Settings > Updates`.  
2. **Configuración de las actualizaciones automáticas**:  
     - Verás varias opciones para gestionar las actualizaciones. Marca la casilla que dice **Automatically check updates for**:  
        - **New versions**: Esto garantiza que el IDE busque automáticamente nuevas versiones del software.  
        - **Plugins**: También puedes activar la búsqueda automática de actualizaciones para los **plugins** instalados.  
     - **Ejemplo**: Imagina que estás trabajando con el plugin de **Kotlin** en IntelliJ IDEA. Al habilitar las actualizaciones automáticas, cada vez que haya una mejora o corrección en el plugin, se te notificará o se actualizará automáticamente según tu configuración.  
3. **Opciones avanzadas**:  
     - Puedes elegir entre varias opciones de actualización:  
        - **Release updates**: Solo recibes actualizaciones estables y probadas.  
        - **Early access program (EAP)**: Si te interesa probar nuevas funcionalidades antes de que se lancen oficialmente, puedes optar por las versiones EAP, que incluyen las últimas características, pero pueden ser menos estables.  
4. **Instalación de actualizaciones**:  
     - Cuando haya una actualización disponible, JetBrains mostrará una notificación. Puedes elegir instalarla de inmediato o postergarla hasta que finalices tu trabajo.  

### 3.2. Actualización de plugins

1. Dirígete a `File > Settings > Plugins` (o `Preferences` en macOS).  
2. En la pestaña de **Installed**, puedes ver todos los plugins que tienes instalados. Si hay actualizaciones disponibles, verás un botón para actualizar cada plugin individualmente o todos a la vez.  
     - **Ejemplo**: Si tienes el plugin de **pytest** en PyCharm, al recibir una actualización, se te notificará en este apartado, y podrás actualizarlo en segundos para obtener las últimas mejoras.  

### 4. Configuración de actualizaciones en Visual Studio Code

En **Visual Studio Code**, las actualizaciones del editor y de las extensiones también son clave para mantener un flujo de trabajo estable y eficiente. Este IDE es conocido por su capacidad de adaptarse a múltiples lenguajes y tecnologías a través de sus extensiones.

### 4.1. Configuración de actualizaciones automáticas del editor

Aunque veremos como, recomendamos revisar la [documentación oficial de Visual Studio Code](https://code.visualstudio.com/updates/) para obtener información actualizada sobre cómo configurar las actualizaciones.

1. **Accede a las configuraciones de actualización**:  
     - Abre Visual Studio Code.  
     - Ve a `Archivo > Preferencias > Configuración` o utiliza el atajo `Ctrl + ,` (en Windows/Linux) o `Cmd + ,` (en macOS).  
     - En la barra de búsqueda, escribe **update**.  
2. **Configuración de las actualizaciones automáticas**:  
     - Localiza la opción **Update: Mode** y elige una de las siguientes configuraciones:  
        - **Default**: Visual Studio Code se actualizará automáticamente cuando se detecten nuevas versiones.  
        - **Manual**: Si prefieres instalar las actualizaciones tú mismo, puedes desactivar las actualizaciones automáticas y hacerlo manualmente cuando lo consideres necesario.  
3. **Verificar y aplicar actualizaciones manualmente**:
     - Para comprobar si hay actualizaciones manualmente, ve a `Ayuda > Buscar actualizaciones`. Si hay una nueva versión disponible, se te dará la opción de descargarla e instalarla.  
     - **Ejemplo**: Si quieres asegurarte de estar utilizando la última versión de Visual Studio Code cuando estés trabajando en un proyecto Python, puedes forzar la búsqueda de actualizaciones antes de comenzar una nueva fase del proyecto.  

### 4.2. Actualización de extensiones

Visual Studio Code es famoso por su uso de extensiones para añadir funcionalidades. A continuación te mostramos cómo mantener estas extensiones actualizadas.

1. **Acceder a la lista de extensiones**:
     - Haz clic en el icono de **Extensiones** en la barra lateral izquierda o usa `Ctrl + Shift + X`.
     - Aquí verás todas las extensiones instaladas. Si alguna necesita actualizarse, aparecerá un ícono de actualización junto a su nombre.
2. **Actualizar extensiones automáticamente**:
     - **Extensiones actualizadas automáticamente**: De manera predeterminada, Visual Studio Code actualiza las extensiones de forma automática. Puedes verificar o cambiar esta configuración en `Archivo > Preferencias > Configuración`, buscando la opción **Extensions: Auto Update**. Asegúrate de que esté marcada para mantener siempre las extensiones al día.
3. **Ejemplo práctico**:
     - Imagina que tienes instalada la extensión de **Python** y la de **Kotlin** en Visual Studio Code. Si ambas reciben actualizaciones (mejoras en el autocompletado, soporte para nuevas características de lenguaje), el IDE actualizará estas extensiones automáticamente, y no tendrás que preocuparte por hacerlo manualmente.

### 5. Recursos adicionales
- [documentación oficial sobre actualización de JetBrains](https://www.jetbrains.com/help/idea/update.html)
- [documentación oficial sobre actualización de Visual Studio Code](https://code.visualstudio.com/updates/)
- [Herramienta de actualización: JetBrains Toolbox](https://www.jetbrains.com/toolbox-app/)


### 5. Conclusión

Mantener tu entorno de desarrollo actualizado es fundamental para garantizar un flujo de trabajo eficiente, estable y seguro. Tanto en **JetBrains** como en **Visual Studio Code**, las actualizaciones automáticas y manuales te permiten acceder a las últimas mejoras y soluciones de problemas, asegurando que siempre trabajes con las mejores herramientas disponibles.

Recuerda que, además de las actualizaciones del IDE en sí, también es esencial mantener actualizadas las **extensiones** y **plugins**, ya que son las que te permiten añadir funcionalidades clave para tus proyectos en **Python** y **Kotlin**. ¡Dedica unos minutos a configurar correctamente el sistema de actualización y disfrutarás de un entorno optimizado para tus proyectos de desarrollo!