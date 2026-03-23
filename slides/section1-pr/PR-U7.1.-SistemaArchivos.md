# PR-U7.1 - Sistema de archivos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: En esta presentación situamos la unidad 7.1 dentro del **RA5**. El
objetivo es que el alumnado entienda por qué un programa necesita
**persistencia**, cómo se organiza un **sistema de archivos** y qué papel tienen
los **flujos de entrada/salida** y las APIs de Kotlin y Java.


### Índice I

- 1. Persistencia y necesidad de almacenar datos
- 2. Qué es un sistema de archivos
- 2.1. Conceptos básicos: fichero, directorio, ruta y metadatos
- 2.2. Rutas absolutas y relativas

Note: En esta primera parte conectamos memoria y persistencia. Después
aterrizamos la idea de **sistema de archivos** y fijamos el vocabulario mínimo
que luego necesitaremos: **fichero**, **directorio**, **ruta** y
**metadatos**.


### Índice II

- 3. Ficheros de texto y binarios. Tipos de acceso
- 4. Flujos de entrada/salida
- 5. Consola: `System.in`, `System.out` y `System.err`
- 6. APIs: `kotlin.io`, `java.io` y `java.nio.file`
- 7. Buenas prácticas y resumen

Note: La segunda mitad baja a lo operativo: distinguimos tipos de ficheros y
de acceso, vemos qué significa trabajar con un **flujo**, repasamos los
canales estándar de consola y terminamos con las **APIs** y las primeras
**buenas prácticas**.

---

## 1. ¿Por qué necesitamos almacenar datos?

Note: Abrimos el tema con una idea muy simple: la **memoria** del programa es
rápida, pero temporal. Si cerramos la aplicación, los datos desaparecen. Por
eso necesitamos mecanismos de **entrada/salida** que permitan conservar y
recuperar información.


### 1.1. Memoria temporal frente a persistencia

- Las variables guardan datos mientras el programa se ejecuta
- Al terminar la aplicación, lo almacenado en memoria se pierde
- Muchas aplicaciones necesitan conservar datos entre sesiones
- Ahí aparece la necesidad de **persistencia**

![Programa y persistencia](assets/PROG-U7.1.-Programa.png) <!-- .element: style="max-width: 50%;" -->

Note: Conviene insistir en que una variable no es un almacén permanente. Sirve
durante la ejecución, pero no cuando el programa termina. La **persistencia**
permite que las notas, incidencias, configuraciones o informes sigan estando
disponibles después.


### 1.2. Cuándo hace falta guardar información

- Cuando los datos no vienen fijos en el código
- Cuando el usuario no puede reintroducir todo cada vez
- Cuando hace falta registrar actividad o incidencias
- Cuando el programa lee configuración al arrancar
- Cuando se exportan resultados a un informe

Note: Estos ejemplos acercan el concepto al trabajo real. Una app de notas,
una configuración, un log o un informe son casos claros donde la memoria no
basta. La palabra clave aquí es **persistir** la información fuera del proceso.

---

## 2. ¿Qué es un sistema de archivos?

Note: En esta sección explicamos el mecanismo que ofrece el sistema operativo
para organizar información en discos, SSD o memorias USB. El alumnado debe
visualizarlo como una estructura jerárquica de **carpetas**, **ficheros** y
**rutas**.


### 2.1. Organización jerárquica de la información

- El sistema operativo organiza datos en soportes persistentes
- Normalmente se representa como una jerarquía de carpetas
- Dentro de esa jerarquía encontramos ficheros y subdirectorios
- Las rutas permiten localizar cada elemento

![Jerarquía de carpetas y archivos](assets/PROG-U7.1.-carpetasArchivos.png) <!-- .element: style="max-width: 48%;" -->

Note: La metáfora de árbol ayuda mucho: unas carpetas contienen otras y, al
final, localizamos cada fichero por su posición en esa jerarquía. Desde un
programa podemos crear, leer, mover, copiar o borrar sin conocer el detalle
físico del dispositivo.


### 2.2. Conceptos básicos del tema

- **Fichero**: unidad de información almacenada
- **Directorio**: contenedor para organizar ficheros y carpetas
- **Ruta**: secuencia que identifica una localización
- **Directorio de trabajo**: referencia para rutas relativas
- **Metadatos**: nombre, tamaño, fecha o permisos

Note: Este vocabulario aparece en toda la unidad. Conviene remarcar que la
**extensión** ayuda a identificar un fichero, pero no demuestra por sí sola su
contenido real. Es una convención útil, no una garantía absoluta.


### 2.3. Rutas absolutas y relativas

- La ruta absoluta parte desde la raíz del sistema
- La ruta relativa parte del directorio de trabajo actual
- Las rutas relativas facilitan la portabilidad del proyecto
- Una ruta absoluta escrita a mano suele fallar en otro equipo

```text
Windows: C:\Usuarios\ana\documentos\notas.txt
Linux/macOS: /home/ana/documentos/notas.txt
Relativas: datos/notas.txt o ./config/app.properties
```

Note: La comparación es importante porque luego afecta al código. En proyectos
educativos y profesionales suele convenir trabajar con **rutas relativas** para
que el programa no dependa de una carpeta concreta de un único ordenador.

---

## 3. Ficheros, directorios y tipos de acceso

Note: Una vez ubicado el sistema de archivos, diferenciamos tipos de datos y
formas de acceso. Esto prepara el terreno para entender por qué no se trabaja
igual con una línea de texto que con una secuencia de **bytes**.


### 3.1. Texto, binario y lectura humana

- Los ficheros de texto almacenan caracteres
- Suelen servir para configuraciones, CSV, logs o informes
- Los ficheros binarios no son legibles a simple vista
- Son habituales en imágenes, audio o datos serializados
- La forma de leer y escribir cambia según el tipo

Note: El punto clave es que el tipo de contenido condiciona la API y el
tratamiento. Cuando hablamos de **texto** solemos pensar en caracteres y
líneas; cuando hablamos de **binario**, pensamos en bytes y estructuras no
legibles directamente.


### 3.2. Acceso secuencial y acceso aleatorio

- El acceso secuencial procesa los datos en orden
- Normalmente se lee de principio a fin
- El acceso aleatorio permite saltar a una posición concreta
- En esta unidad empezamos por los casos secuenciales

Note: Aquí interesa que el alumnado entienda la idea general, no tanto la
implementación. El acceso **secuencial** es el más frecuente al principio
porque simplifica la lectura y la escritura de texto.

---

## 4. ¿Qué es un flujo de entrada/salida?

Note: Esta es una de las ideas centrales del tema. Un **flujo** es una
abstracción que modela el paso de datos entre una **fuente** y un **destino**.
Esa idea sirve para teclado, pantalla, ficheros, red o memoria.


### 4.1. Fuente, destino y secuencia de datos

- Un flujo representa datos que circulan secuencialmente
- Entre una fuente y un destino hay operaciones repetidas
- Las acciones típicas son abrir, leer, escribir y cerrar
- El mismo modelo se reutiliza en muchos contextos

![Modelo de flujos](assets/PROG-U7.1.-Flujos.png) <!-- .element: style="max-width: 52%;" -->

Note: El valor didáctico del concepto está en la unificación: aunque cambie el
dispositivo físico, seguimos pensando en una secuencia de datos y en operaciones
parecidas. Eso reduce la complejidad mental del alumnado.


### 4.2. Tipos de flujos que encontraremos

- Flujos de **caracteres** para texto
- Flujos de **bytes** para datos binarios
- Flujos de **objetos** cuando serializamos estructuras
- La abstracción permite trabajar de forma uniforme

Note: Conviene subrayar que no todos los flujos transportan lo mismo. El tipo
de dato condiciona las clases y métodos que veremos después. La definición a
retener es: un flujo permite leer o escribir datos secuencialmente.

---

## 5. Entrada estándar, salida estándar y error

Note: Antes de trabajar con ficheros, es útil recordar que un programa ya hace
**entrada/salida** cuando usa la consola. Así conectamos la teoría con algo que
el alumnado conoce desde las primeras prácticas.


### 5.1. Los tres canales básicos de consola

- **Entrada estándar**: normalmente el teclado
- **Salida estándar**: normalmente la consola
- **Salida de error**: canal específico para mensajes de error
- En la JVM aparecen como `System.in`, `System.out` y `System.err`

![Flujos estándar](assets/PROG-U7.1.-FlujosEstandar.png) <!-- .element: style="max-width: 45%;" -->

Note: Es importante distinguir **salida normal** y **salida de error**, porque
no son exactamente lo mismo aunque ambas se vean en consola. Esta separación
será útil cuando el alumnado trabaje con scripts, redirecciones o depuración.


### 5.2. Kotlin sobre la JVM: entrada y salida simples

- Kotlin ofrece funciones de más alto nivel para consola
- `print()` y `println()` escriben en salida estándar
- `readln()` y `readlnOrNull()` leen desde entrada estándar
- Son cómodas para ejemplos y ejercicios iniciales

```kotlin
fun main() {
    print("Introduce tu nombre: ")
    val nombre = readln()
    println("Hola, $nombre")
}
```

Note: Este ejemplo no usa ficheros todavía, pero sí muestra una operación
completa de **entrada/salida**: el programa lee desde teclado y escribe en
pantalla. Sirve para conectar la consola con el concepto general de flujo.

---

## 6. APIs que usaremos en la unidad

Note: Ahora situamos las bibliotecas principales. La idea no es memorizar todo
ya, sino saber qué familia de APIs resuelve cada tipo de necesidad cuando
trabajamos con consola, rutas, ficheros y flujos.


### 6.1. `kotlin.io`: utilidades de alto nivel

- Lectura desde consola con `readln()` y `readlnOrNull()`
- Lectura de texto con `readText()` y `readLines()`
- Escritura simple con `writeText()` y `appendText()`
- Resulta cómoda para tareas frecuentes y ejemplos cortos

Note: Esta familia es útil para empezar porque reduce el ruido sintáctico.
Permite trabajar pronto con lectura y escritura sin entrar todavía en detalles
más bajos de la plataforma Java.


### 6.2. `java.io` y `java.nio.file`

- `java.io` es la API clásica de Java para ficheros y flujos
- Aquí aparece la clase `File`
- `java.nio.file` es la API más moderna para rutas y operaciones
- Destacan `Path` y `Files` para un trabajo más robusto

![APIs de Kotlin y Java](assets/PROG-U7.1.-BibliotecaKotlin.png) <!-- .element: style="max-width: 52%;" -->

Note: Conviene presentar estas dos APIs como complementarias. Kotlin hereda la
potencia del ecosistema Java y añade utilidades de más alto nivel. En la unidad
iremos moviéndonos entre **`kotlin.io`**, **`java.io`** y **`java.nio.file`**.

---

## 7. De la teoría a la práctica

Note: Antes de cerrar, hacemos la traducción directa del tema a un programa
real. El alumnado debe reconocer en el ejemplo varias ideas a la vez:
**entrada**, **salida**, **persistencia** y uso de una librería adecuada.


### 7.1. Ejemplo guiado: guardar una incidencia

```kotlin
import java.io.File

fun main() {
    print("Escribe una incidencia: ")
    val incidencia = readln()

    File("incidencias.txt").appendText("$incidencia\n")
    println("Incidencia guardada")
}
```

- Lee una incidencia desde teclado
- Escribe confirmación en consola
- Guarda información en un fichero de texto
- Usa una ruta relativa dentro del proyecto

Note: Este ejemplo resume bien el tema. Leemos por **entrada estándar**,
mostramos mensaje por **salida estándar** y persistimos el dato en un
**fichero**. Además, se usa una ruta relativa, que es una buena práctica dentro
de un proyecto.


### 7.2. Buenas prácticas iniciales

- Usa rutas relativas cuando trabajes en un proyecto
- Distingue claramente texto y binario
- Valida la entrada antes de guardarla
- No des por hecho que un fichero existe
- Maneja con cuidado errores de lectura y escritura
- Usa APIs de alto nivel cuando simplifiquen el código

Note: Este bloque final sirve como lista de control. También conviene remarcar
un error frecuente: **tener una ruta** escrita como texto no significa que el
**fichero exista** realmente en el sistema.

---

## 8. Resumen

Note: Cerramos recuperando las ideas esenciales del apartado 7.1. El alumnado
debería salir de aquí con un mapa mental claro antes de entrar en consola,
clase `File` y lectura/escritura de ficheros en los siguientes subtemas.


### 8.1. Ideas clave para continuar la unidad

- La memoria no basta cuando necesitamos persistencia
- El sistema de archivos organiza información con rutas y carpetas
- La entrada/salida se modela mediante flujos
- Consola y ficheros forman parte del mismo problema general
- Kotlin y Java aportan APIs específicas para resolverlo

Note: Si esta slide queda clara, el grupo ya tiene la base conceptual del tema.
La siguiente etapa será aplicar estas ideas en ejercicios con **consola**,
**`File`** y lectura/escritura real de información.
