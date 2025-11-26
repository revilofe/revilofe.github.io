---
title: "UD 5 - 5.3.1 Logging Code"
description: Logging Code
summary: Logging Code
authors:
  - Eduardo Fdez
date: 2024-04-16
icon: "material/file-document-outline"
permalink: /edes/unidad3/3.3.1
categories:
  - EDES
tags:
  - EDES
  - Logging
  - Debug
---

## 5.3.1. Logging


### 1. Introducción al registro de eventos (logging)

El registro de eventos o *logging* es una práctica fundamental en el desarrollo de software profesional. Consiste en registrar mensajes que informan sobre el estado de ejecución de una aplicación, permitiendo a los desarrolladores y administradores obtener información sobre el comportamiento interno del sistema sin necesidad de interactuar directamente con él.

El logging cumple varias funciones: permite conocer qué está haciendo el programa en cada momento, detectar errores, analizar patrones de uso, rastrear fallos en producción y realizar auditorías. Es especialmente útil en aplicaciones complejas o en aquellas que deben mantenerse a largo plazo.

A diferencia de otras técnicas de depuración como los mensajes `println`, el logging está diseñado para ofrecer información estructurada, configurable y filtrable, adecuada tanto para la fase de desarrollo como para la fase de despliegue.

#### 1.1. ¿Qué es un sistema de logging?

Un sistema de logging es una herramienta que gestiona la creación, filtrado, formato y destino de los mensajes de registro generados por una aplicación. Permite capturar información útil durante la ejecución del programa y enviarla a distintos lugares, como la consola, un archivo de texto, un servidor remoto o una base de datos.

La mayoría de los lenguajes de programación modernos cuentan con bibliotecas o marcos de trabajo que permiten realizar logging de forma estructurada y configurable. Estas herramientas permiten definir distintos niveles de importancia para los mensajes, configurar qué información se registra y establecer cómo y dónde se almacena esa información.

### 2. Características comunes de los sistemas de logging

Aunque existen diversas implementaciones, los sistemas de logging modernos comparten una serie de características esenciales que permiten una gestión eficaz de los mensajes de registro:

* **Niveles de log:** Los niveles permiten clasificar los mensajes según su gravedad o importancia. Los niveles más comunes, de menor a mayor detalle, son:

  - `TRACE`: mensajes muy detallados, útiles para el análisis minucioso de la ejecución.
  - `DEBUG`: mensajes de depuración, utilizados durante el desarrollo para comprender el flujo del programa.
  - `INFO`: mensajes informativos que describen acciones normales del sistema.
  - `WARN`: advertencias que indican condiciones no críticas pero potencialmente problemáticas.
  - `ERROR`: errores que afectan al funcionamiento del sistema pero no provocan su parada inmediata.
  - `FATAL` (en algunas herramientas): errores graves que provocan la detención de la aplicación.

  El uso de niveles permite filtrar qué mensajes se muestran o almacenan según el entorno (desarrollo, pruebas, producción).

* **Appenders:** Un *appender* es el componente que define el destino del mensaje de log. Puede ser la consola, un archivo, un flujo de red, una base de datos, entre otros. Un sistema de logging puede tener múltiples appenders activos al mismo tiempo.

* **Filtros:** Los filtros permiten definir reglas para aceptar o rechazar mensajes antes de ser enviados a un appender. Esto permite, por ejemplo, registrar en consola solo los mensajes de nivel `INFO` y superiores, pero guardar en fichero también los de nivel `DEBUG`.

* **Formato de mensajes:** Los sistemas de logging permiten personalizar el formato en el que se presentan los mensajes. Esto puede incluir la fecha y hora, el hilo de ejecución, el nivel de log, el nombre del logger, el mensaje, e incluso información contextual adicional.

* **Jerarquía de loggers:** En muchos frameworks, como Logback, los loggers se organizan jerárquicamente por nombre, generalmente siguiendo el paquete de clases. Esto permite aplicar configuraciones específicas a partes concretas de la aplicación.

* **Configuración externa:** Es habitual que la configuración del logging se gestione desde archivos externos (como `logback.xml`), lo que permite cambiar el comportamiento del sistema sin modificar el código fuente.

### 3. Herramientas de logging más comunes

En el ecosistema Java y Kotlin, existen varias bibliotecas ampliamente utilizadas para la gestión de logs. Algunas de las más destacadas son:

* **SLF4J (Simple Logging Facade for Java):** No es un sistema de logging en sí, sino una fachada que permite utilizar distintas implementaciones (como Logback o Log4j) a través de una misma API. Esto facilita el desacoplamiento del código respecto a la herramienta concreta utilizada.

* **Logback:** Es una implementación moderna y potente compatible con SLF4J. Ofrece alto rendimiento, amplia capacidad de configuración, múltiples tipos de appenders, soporte para rotación de logs y filtros sofisticados. Está diseñada como sucesora natural de Log4j y es ampliamente usada en entornos profesionales. Es la herramienta que se utilizará en este curso.

* **Log4j:** Fue durante muchos años el sistema de logging más extendido en el ecosistema Java. Aunque sigue siendo usado, ha sido reemplazado progresivamente por Logback debido a mejoras en rendimiento y configuración.

* **Java Util Logging (JUL):** Es la implementación estándar incluida en Java. Aunque funcional, ofrece menos flexibilidad que las bibliotecas anteriores y es menos utilizada en aplicaciones modernas.

* **Kotlin Logging:** Biblioteca ligera que permite usar SLF4J en Kotlin con una sintaxis más idiomática.

### 4. Ventajas del uso de un sistema de logging

El uso de un sistema de logging estructurado aporta múltiples beneficios en el desarrollo y mantenimiento de software:

* Permite detectar errores sin necesidad de detener la aplicación.
* Facilita el diagnóstico de problemas en entornos de producción.
* Mejora la trazabilidad de acciones realizadas por los usuarios o el sistema.
* Proporciona una herramienta poderosa para el análisis retrospectivo de fallos.
* Reduce la dependencia de técnicas poco escalables como la impresión directa por consola.

### 5. Logback: sistema de logging recomendado

Logback es el sistema de logging que se utilizará como referencia a lo largo del módulo. Es una herramienta madura, compatible con SLF4J, que permite:

- Definir múltiples niveles de log. Ej: `TRACE`, `DEBUG`, `INFO`, `WARN`, `ERROR`.
- Personalizar el formato de los mensajes. Ej: `%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n`
- Registrar mensajes en distintos destinos (consola, archivo, red). Ej: `<appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">` y `<appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">`
- Filtrar mensajes según criterios definidos. Ej: Si quiero filtrar haciendo uso de filter los logs de nivel `DEBUG` y superiores, puedo usar `<filter class="ch.qos.logback.classic.filter.LevelFilter">` y `<level>DEBUG</level>`.
- Gestionar la rotación y archivo de logs antiguos. Ej: `<rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">` y `<maxHistory>7</maxHistory>`. Se abre un nuevo archivo de log por día y se han mantenido los logs de los últimos 7 días.
- Activar o desactivar logs sin modificar el código fuente. Ej: `<root level="DEBUG">` y `<appender-ref ref="CONSOLE" />`. Se aplicará a toda la aplicación.

La configuración de logback se realiza mediante un archivo externo (`logback.xml`), lo que permite mantener separados el código de negocio y las decisiones de registro.

En los siguientes apartados se explicará paso a paso cómo integrar logback en un proyecto y cómo utilizarlo para mejorar la observabilidad y mantenibilidad del software desarrollado.

### 6. Guía configuración de Logback

El registro o *logging* es una herramienta fundamental en el desarrollo de software. Permite registrar información sobre el funcionamiento de un programa, lo cual es muy útil para:

- Detectar errores.
- Analizar el comportamiento de la aplicación.
- Realizar un seguimiento del uso en producción.
- Sustituir las típicas sentencias `println()` de depuración por un sistema más potente, configurable y profesional.

En esta guía aprenderás a configurar **logback**, una de las bibliotecas más utilizadas para la gestión de logs en entornos que utilizan la JVM, como Kotlin o Java.

#### 6.1. Añadir las dependencias al proyecto

Para utilizar logback en tu proyecto, necesitas incluir las siguientes dependencias:

Si estás utilizando **Gradle con Kotlin DSL (`build.gradle.kts`)**, añade lo siguiente dentro del bloque `dependencies`:

```kotlin
dependencies {
    implementation("org.slf4j:slf4j-api:2.0.9")
    implementation("ch.qos.logback:logback-classic:1.4.11")
}
```

> 💡 Estas bibliotecas proporcionan la interfaz estándar de logging (`slf4j`) y su implementación mediante logback.

Tras añadir las dependencias, sincroniza tu proyecto para que estén disponibles.


#### 6.2. Crear el archivo de configuración `logback.xml`

Logback se configura mediante un archivo XML llamado `logback.xml`. Este archivo define los siguientes elementos:

- **Appenders**: los destinos donde se escriben los logs (por ejemplo, consola o fichero).
- **Loggers**: qué partes de la aplicación generan logs.
- **Root Logger**: la configuración por defecto que se aplica si no se especifica otra.

**Ubicación del archivo:** Debe colocarse en la ruta `src/main/resources/logback.xml`

##### 6.2.1. Ejemplo de configuración básica:

Este ejemplo define dos appenders (consola y fichero) y un logger raíz con nivel de log `DEBUG`:

```xml
<configuration>

    <!-- Appender que muestra los logs en la consola -->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Appender que guarda los logs en un archivo con rotación diaria -->
    <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <file>logs/app.log</file>

        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>logs/app.%d{yyyy-MM-dd}.log</fileNamePattern>
            <maxHistory>7</maxHistory>
        </rollingPolicy>

        <encoder>
            <pattern>%d{yyyy-MM-dd HH:mm:ss} %-5level %logger - %msg%n</pattern>
        </encoder>
    </appender>

    <!-- Logger raíz: se aplicará a toda la aplicación -->
    <root level="DEBUG">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="FILE" />
    </root>

</configuration>
```

##### 6.2.2. Explicación de elementos clave:

- `<appender name="CONSOLE" ...>`: envía los mensajes a la consola.
- `<appender name="FILE" ....>`: envía los mensajes a un archivo.
- `<file>logs/app.log</file>`: define el archivo de salida para los logs.
- `<fileNamePattern>`: crea un nuevo archivo de log por día.
- `<maxHistory>`: mantiene los logs de los últimos 7 días. 
- `<root level="DEBUG">`: indica que se registrarán mensajes de nivel DEBUG o superior.
- `<appender-ref ref="CONSOLE" />`: asocia el appender de consola al logger raíz. Desde este punto, todos los mensajes de log generados por la aplicación se enviarán a la consola.
- `<appender-ref ref="FILE" />`: asocia el appender de archivo al logger raíz. Desde este punto, todos los mensajes de log generados por la aplicación se guardarán en el archivo `logs/app.log`.


#### 6.3. Uso del sistema de logging en el código

Para registrar mensajes en la aplicación, se utiliza una instancia del logger. A continuación se muestra cómo hacerlo:

```kotlin
import org.slf4j.LoggerFactory

val logger = LoggerFactory.getLogger("MiAplicacion")

fun main() {
    logger.trace("Mensaje TRACE")
    logger.debug("Mensaje DEBUG")
    logger.info("Mensaje INFO")
    logger.warn("Mensaje WARN")
    logger.error("Mensaje ERROR")
}
```

En este ejemplo, se crea un logger con el nombre "MiAplicacion". Luego, se registran mensajes de distintos niveles. Dependiendo de la configuración del archivo `logback.xml`, algunos de estos mensajes pueden no aparecer en la consola o en el archivo.


##### 6.3.1. Niveles de log (de menor a mayor gravedad):

| Nivel   | Uso principal                                                                 |
|---------|--------------------------------------------------------------------------------|
| TRACE   | Información extremadamente detallada.                                         |
| DEBUG   | Información útil para depurar durante el desarrollo.                          |
| INFO    | Mensajes informativos sobre el funcionamiento normal del programa.           |
| WARN    | Advertencias que no detienen el programa, pero requieren atención.            |
| ERROR   | Errores que afectan el funcionamiento y deben ser corregidos.                 |

> 📌 El nivel configurado en el archivo XML determina qué mensajes se mostrarán. Si el nivel es `DEBUG`, no se mostrarán mensajes `TRACE`.

Hay que tener en cuenta que el uso de niveles de log adecuados es fundamental para evitar la saturación de información y facilitar la identificación de problemas. Por ejemplo, en producción es recomendable usar `INFO` o `WARN`, mientras que en desarrollo se puede utilizar `DEBUG` o `TRACE`.

#### 6.4. Verificar que el sistema de logs funciona

Una vez configurado el archivo `logback.xml` y añadido el código de logging:

- Ejecuta el programa.    
- Deberías ver los mensajes en la **consola** con formato personalizado.    
- Se creará un archivo `logs/app.log` con los mismos mensajes.    
- Si ejecutas el programa varios días, se generará un archivo nuevo por día.    
- Si el programa se ejecuta durante más de 7 días, los archivos más antiguos se eliminarán automáticamente.
- Si no ves los mensajes esperados, revisa la configuración del archivo `logback.xml` y asegúrate de que está en la ruta correcta (`src/main/resources/`).
- Asegúrate de que las dependencias de `logback` y `slf4j` están correctamente añadidas al proyecto y sincronizadas.
- Verifica que el logger se inicializa correctamente y que no hay errores en la consola al iniciar la aplicación.
- Comprueba que el nivel de log configurado en `logback.xml` es compatible con los mensajes que intentas registrar. Por ejemplo, si el nivel es `INFO`, no se mostrarán los mensajes de nivel `DEBUG` o `TRACE`.


#### 6.5. Buenas prácticas al utilizar logging
A continuación se presentan algunas buenas prácticas a seguir al implementar un sistema de logging en tu aplicación:    

- **Usa siempre un logger por clase**. No uses un logger global para toda la aplicación.
- **Evita imprimir directamente con `println()`**. Usa siempre el sistema de logs.
- **No abuses del nivel `DEBUG` o `TRACE`** en producción. Usa niveles adecuados.
- **No incluyas datos sensibles** (contraseñas, datos personales) en los logs.
- **Organiza los logs por paquetes o clases**, si tu aplicación es grande.
- **No olvides limpiar los logs antiguos**. Configura la rotación y eliminación automática de logs viejos.
- **Usa un formato claro y legible** para los mensajes de log. Incluye información relevante como la fecha, el nivel de log y el mensaje.
- **No uses logs para controlar el flujo del programa**. Los logs son para registrar información, no para tomar decisiones en el código.
- **No olvides documentar el uso de logs** en tu código. Explica qué información se registra y por qué es relevante.
- **Revisa los logs regularmente**. No esperes a que ocurra un problema para mirar los logs. Mantén un seguimiento activo de la información registrada.
- **Configura alertas** para ciertos niveles de log (como `ERROR` o `FATAL`) para recibir notificaciones inmediatas en caso de problemas críticos.
- **Utiliza herramientas de análisis de logs** para facilitar la búsqueda y el análisis de grandes volúmenes de datos. Herramientas como ELK Stack (Elasticsearch, Logstash, Kibana) o Splunk pueden ser muy útiles.
- Puedes usar condiciones como `if (logger.isDebugEnabled)` para evitar cálculos innecesarios en producción. Por ejemplo: 

```kotlin
if (logger.isDebugEnabled) {
    logger.debug("El resultado es: ${calculoLargo()}")
}
```

Desde de lo que hemos visto, podemos concluir que implementar un sistema de logs desde el inicio del desarrollo mejora la trazabilidad del código, facilita la resolución de errores y prepara la aplicación para un entorno profesional. **Logback**, junto con **SLF4J**, ofrece una solución flexible y potente para la gestión de mensajes de log.

### 7. Recursos y fuentes

* [Logback](https://logback.qos.ch/manual/)
