
# Guía del Repositorio para Agentes

Este repositorio contiene material educativo para distintos módulos de formación profesional. La documentación está dirigida a **alumnos y alumnas** y debe ser didáctica, clara y pedagógica.

## 1. Estructura del Repositorio

### 1.1. Carpeta `docs/`

Contiene la documentación principal en formato MkDocs Material. Está organizada por módulos:

- **section1**: Módulo de "Programación"
- **section2**: Módulo de "Incidentes de seguridad"
- **section3**: Módulo de "Entornos de desarrollo"
- **section4**: Módulo de "Despliegue de aplicaciones web"

#### Estructura de cada section:

```
sectionX/
├── index.md                    # Descripción del módulo, contenidos y planificación
├── recursos                    # Recursos genéricos para el módulo (Normativa, libros de texto, otros documentos, plantillas, guías, etc.)
│   ├── MODULO Normativa.txt    # Normativa del módulo, con los Resultados de aprendizaje y sus criterios de evaluación
│   └── ...                     # Otros archivos que pueden servir para generar documentación, prácticas, etc. Como el libro de texto del módulo
└── uXX/                        # Unidades didácticas (u01, u02, u03...)
    ├── index.md                # Descripción de la unidad, contenidos y planificación
    ├── gift/                   # [OPCIONAL] Preguntas en formato GIFT para cuestionarios, exámenes, etc.
    │   ├── MODULO-UX.Y.-Tema.gift  # Habrá un archivo GIFT por cada archivo teoria de la unidad
    │   └── ...                  # Otros archivos GIFT para la unidad
    ├── teoria/                 # Contenidos teóricos
    │   ├── MODULO-UX.Y.-Tema.md
    │   ├── assets/             # Imágenes y recursos multimedia
    │   └── OtrosRecursos/      # Archivos adicionales (PDFs, plantillas, etc.)
    └── practica/               # Prácticas y ejercicios (singular en section1, 3, 4; "practicas" en section2)
        ├── MODULO-UX.-PracticaYYY.md
        ├── assets/             # Imágenes y recursos multimedia
        └── OtrosRecursos/      # Archivos adicionales necesarios
```

!!! note "Nota sobre nomenclatura de carpetas"
    **Inconsistencia actual**: La mayoría de módulos usan `practica/` (singular), pero section2 usa `practicas/` (plural).
    
    **Recomendación**: Usar `practica/` (singular) de forma consistente en todos los módulos.

### 1.2. Carpeta `slides/`

Contiene presentaciones en formato Reveal.js (HTML + Markdown) que complementan los contenidos de `docs/`.

**Estructura organizativa:**

Las slides están organizadas en subdirectorios por módulo:

```
slides/
├── section1-pr/           # Programación
│   ├── assets/            # Recursos (imágenes) específicos del módulo
│   ├── PR-*.html          # Presentaciones HTML
│   └── PR-*.md            # Fuentes Markdown
├── section2-is/           # Incidentes de Seguridad
│   ├── assets/
│   ├── IS-*.html
│   └── IS-*.md
├── section3-ed/           # Entornos de Desarrollo
│   ├── assets/
│   ├── ED-*.html
│   └── ED-*.md
├── section4-daw/          # Despliegue de Aplicaciones Web
│   ├── assets/
│   ├── DAW-*.html
│   └── DAW-*.md
├── dist/                  # Recursos compartidos de Reveal.js
├── plugin/                # Plugins de Reveal.js
└── css/                   # Estilos compartidos
```

**Nomenclatura de archivos:**
- section1-pr: `PR-UX.Y.-NombreDescriptivo`
- section2-is: `IS-UX.Y.-NombreDescriptivo`
- section3-ed: `ED-UX.Y.-NombreDescriptivo`
- section4-daw: `DAW-UX.Y.-NombreDescriptivo`

Donde:
- `X` = número de unidad
- `Y` = número de punto dentro de la unidad
- Ejemplo: `DAW-U2.1.-Docker` → Despliegue de Aplicaciones Web, Unidad 2, punto 1, tema Docker

Cada tema tiene dos archivos:
- `.md` (fuente en Markdown)
- `.html` (presentación Reveal.js generada)

**Rutas en archivos HTML:**

Los archivos HTML dentro de los subdirectorios de módulos utilizan rutas relativas a la carpeta padre:
- `href="../dist/..."` para recursos de Reveal.js
- `href="../plugin/..."` para plugins
- `href="../custom.css"` para CSS personalizado
- Las referencias a assets dentro del mismo módulo usan rutas relativas: `assets/imagen.png`

**Configuración de las presentaciones:**

Todas las presentaciones HTML incluyen:
- `custom.css`: CSS personalizado que fuerza la visualización de la barra de progreso y los números de diapositiva (ubicado en `slides/custom.css`)
- Configuración en `Reveal.initialize()`:
  - `margin: 0.1` - Margen del 10% alrededor del contenido
  - `progress: true` - Barra de progreso visible
  - `slideNumber: 'c/t'` - Número de diapositiva actual/total
  - `showSlideNumber: 'all'` - Mostrar en todas las diapositivas

**Referencias a las slides desde `docs/`:**

Cada vez que añada una nueva slide o presentación, deberá actualizar las referencias en la documentación. Suponiendo que añadimos el punto Y de la unidad X de la sectionZ, lo normal es que quede enlaza en los distintos index.md afectados:
- doc/index.md (índice principal del repositorio)
- docs/sectionZ/index.md (índice del módulo)
- docs/sectionZ/uXX/index.md (índice de la unidad)
- docs/sectionZ/uXX/teoria/MODULO-UX.Y.-Tema.md (al final del documento de teoría correspondiente)
- docs/sectionZ/uXX/practica/MODULO-UX.-PracticaYYY.md (al final del documento de práctica correspondiente)



Las referencias a presentaciones desde la documentación usan URLs absolutas:
- `https://revilofe.github.io/slides/section1-pr/PR-UX.Y.-NombreArchivo.html`
- `https://revilofe.github.io/slides/section2-is/IS-UX.Y.-NombreArchivo.html`
- `https://revilofe.github.io/slides/section3-ed/ED-UX.Y.-NombreArchivo.html`
- `https://revilofe.github.io/slides/section4-daw/DAW-UX.Y.-NombreArchivo.html`

**Gestión de assets:**

Cada módulo tiene su propia carpeta `assets/` con las imágenes específicas del módulo. Los archivos compartidos entre módulos (como logos) se duplican en cada carpeta assets correspondiente para mantener la independencia de cada módulo.

### 1.3. Otros directorios

- **includes/**: Archivos reutilizables (abreviaturas, snippets)
- **mkdocs.yml**: Configuración del sitio MkDocs

## 2. Patrón de Documentación

### 2.1. Público objetivo

La documentación está dirigida a **alumnos y alumnas** de formación profesional. Debe ser:

- **Didáctica**: Explicar conceptos de forma progresiva
- **Clara**: Usar lenguaje sencillo y directo
- **Práctica**: Incluir ejemplos y ejercicios
- **Inclusiva**: Usar lenguaje no sexista (alumnos y alumnas, estudiantes)

### 2.2. Estructura de documentos teóricos

Los archivos de teoría (`teoria/`) deben seguir esta estructura:

```markdown

---
title: "UD X - X.Y Título del tema"
description: Breve descripción
summary: Resumen corto
authors:
    - Eduardo Fdez
date: YYYY-MM-DD
icon: "material/file-document-outline"
permalink: /modulo/unidadX/X.Y
categories:
    - MODULO
tags:
    - Tag1
    - Tag2
---

## X.Y. Título del tema

[Introducción al tema que explique el contexto y objetivo]

### 1. Primer concepto

[Explicación clara del concepto]

#### 1.1. Subconcepto o ejemplo práctico

[Explicación detallada del subconcepto]

### 2. Segundo concepto

[Continuar con estructura similar]

```

Ademas:

- Es un texto que representa un patrón a seguir, y ademas es explicativo de como generar la documentación siguiendo este patrón, y MUY IMPORTANTE respetando los saltos de línea y numero de espacios de indentación. (4 espacios):

```markdown

Aconsejamos una lista de cosas, deben seguirse para generar documentos claros y didácticos:

- Ser claro y concisos.
  
    - Como es otro bloque de identación, 4 espacios mas. y una linea en blanco antes y despues del bloque identado.
    - La identación será de 4 espacios.
    - Usar listas para organizar ideas, pero no abusar de ellas.
  
        - Como es otro bloque de identación, 4 espacios mas. y una linea en blanco antes y despues del bloque.
        - Asegurarse de que cada punto aporta valor.
        - Dividir el contenido en secciones lógicas.
        
    - Incluir definiciones cuando sea necesario.
    
- Incluir ejemplos visuales.
- Usar subtítulos para organizar la información.
```

- Tambien se pueden incluir listas de numeradas, en este formato y y IMPORTANTE respetando los saltos de línea y numero de espacios de indentación. (4 espacios):

```markdown

A continuación un listado: 

1. Primer punto importante
2. Segundo punto relevante
   
    - Como es otro bloque de identación, 4 espacios mas. y una linea en blanco antes y despues del bloque identado.
    - Y anidar las viñetas si es necesario
    
3. Tercer punto clave
```
   
- Se pueden incluir citas en bloque para resaltar definiciones o ideas clave:
```markdown

> La programación es el proceso de crear un conjunto de instrucciones que le dicen a una computadora cómo
```
- Se pueden incluir bloques de código para ilustrar ejemplos prácticos:
- También es importante incluir imágenes o diagramas para ilustrar conceptos complejos.

[Ejemplos si procede]

```markdown
<figure markdown>   
  ![](assets/nombre-imagen.png)   
  <figcaption>Descripción de la imagen</figcaption>   
</figure>
```

### 2.3. Estructura de las Slides

Los archivos de slides (`slides/`) se explican a continuación:

#### 2.3.1. Formato de las slides**
A continuación explicamos el proceso de creación de presentaciones de diapositivas sobre contenidos, que normalmente serán de los módulos de informática. Generará slides siguiendo una estructura de markdown precisa (MUY IMPORTANTE SEGUIR LA NOTACIÓN MARKDOWN).

Sigue concienzudamente estas REGLAS para GENERAR LAS SLIDES:

- El contenido a generar son un conjunto de slides, formadas por grupos de slides denominadas  "secciones", y dentro de cada sección hay varias slides relacionadas con la sección.
- El título principal de las slides será de nivel 1 (#).
- Las secciones comienzan con títulos de nivel dos  (##).
- Las secciones contienen distintas slides que hablan sobre conceptos o contenido relacionado con el titulo de la sección.
- El comienzo de un grupo de slides o sección, puede ser una sola slide con el titulo de la sección, sin ningún contenido mas.
- Cada grupo de slides o sección se delimitará con una línea horizontal (---).
- Usa --- solo para separar grupos de slides o sección
- Cada slide de una sección ,en la que se tratará temas relacionados con la sección, continuará con títulos de nivel tres (###).
- Una slide de un mismo grupo (misma sección) se separarán con 2 lineas en blanco de la siguiente slide. IMPORTANTE: No te olvides nunca las 2 lineas en blanco para separar las slides de un grupo de lides o seccion.
- Una slide con contenido es: una lista de máximo siete viñetas, con tamaño de linea limitadas a 80 caracteres máximo.
- Una slide con contenido tambien pueden contener código fuente en un determinado lenguaje de programación, en cuyo caso el codigo fuente incluirá comentarios sobre aclaraciones del código de ejemplo. Siempre que sea posible, introducelo.
- Cuando se esá tratando un concepto o un área concreta de un punto de unidad, puede quedarse corto con solo una slide con contenido, en cuyo caso se podra generar una segunda, tercera, etc. slide con el mismo titulo e identificandolas con el mismo titulo pero con número romanos I, II, III, etc.
- Al generar las slides a partir de un documento, utiliza la misma enumeración de los puntos que la que viene en el documento. Es decir , si el documento tiene un punto 1.1, 1.2, 1.3, etc., las slides generadas tendrán los mismos títulos y numeración.
- Si un punto tiene subpuntos, estos se tratarán en slides independientes dentro de la misma sección, con el mismo título y numeración que el punto, pero añadiendo el subpunto. Por ejemplo, si el punto es 1.3 y tiene subpuntos 1.3.1, 1.3.2, etc., cada subpunto se tratará en una slide independiente, con el título 1.3.1, 1.3.2, etc.
- Si un punto tiene subpuntos, y estos a su vez tienen subpuntos, estos se tratarán en slides independientes dentro de la misma sección, con el mismo título y numeración que el subpunto, pero añadiendo el subpunto. Por ejemplo, si el punto es 1.3.1 y tiene subpuntos.
- Al final de TODAS las slides, se crearán notas para el presentador, mas extensas y en las que se describirá el contenido de cada uno de los puntos de las slide o información adicional que no cabe en la  slide.
- Las notas vendrán identificadas y precedidas por la palabra "Note: " y a continuación el texto, Ej: "Note: Esto es una nota extensa que continuará....." y serán super completas y detalladas, para que el profesor pueda explicar todo el contenido de la slide sin dejar nada sin cubrir.
- Las notas deben contener todos los comentarios necesarios que el profesor debe hacer para que ningún contenido se deje sin cubrir sobre el punto tratado en en la slide. Por tanto, es importante que en las notas se expliquen todos los conceptos que aparecen en la slide, y se den ejemplos si es necesario.
- Todas las interacciones y contenido proporcionado estarán en español de España, con un tono relajado y amistoso, pero sin perder la formalidad necesaria para un entorno educativo.

IMPORTANTE:
- COMTEMPLA TODO TODO TODO el contenido del documento original de Teoria ¡¡¡¡¡no dejes nada sin cubrir!!!!!!.
- SIEMPRE genera el resultado en markdown.
- NUNCA generes mas de 7 lineas (viñetas) por slide.
- NUNCA generes líneas de mas de 80 caracteres.
- RESPETA las separaciones de slides (2 lineas en blanco ) y secciones (---), tal como se indica.

Un ejemplo sería el siguiente:

"""""""
# U4.1 - Kotlin Básico    

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Indice

---

## 1. Introducción


### 1.1. Kotlin

* Kotlin: un lenguaje de programación moderno y versátil.
* Desarrollado por JetBrains, lanzado en 2011.
* Interoperable con Java, popular en desarrollo Android.

Note: Presenta Kotlin, su origen y su popularidad, especialmente en el desarrollo de Android y su interoperabilidad con Java.


### 1.1. Características de Kotlin

A continuación, las características principales de Kotlin:

* Sintaxis concisa y expresiva.
* Seguridad de tipos nulos integrada.

    * operador `?` para manejar valores nulos.
    * Evita errores comunes de null pointer exceptions.

* Soporta programación funcional y orientada a objetos.

Note: Resalta las características clave de Kotlin, como la sintaxis concisa, la seguridad de tipos nulos y el soporte para paradigmas de programación.


### 1.2. Configuración del Entorno de Kotlin

* Kotlin puede ser usado con IntelliJ IDEA, Android Studio, o cualquier editor de texto.
* Compilador de Kotlin disponible para línea de comandos.
* Kotlin Playground: para experimentar en línea.

Note: Ofrece opciones para configurar el entorno de desarrollo para Kotlin, incluyendo IDE's y herramientas en línea.


### 1.3. Estructura Básica de un Programa en Kotlin

* Todo programa en Kotlin comienza con la función `main`.
* `main` es el punto de entrada del programa.

```Kotlin
    //Programa "hola mundo" en Kotlin
    fun main() {
        println("Hola, Kotlin!")
    }
```
Note: Explica la estructura básica de un programa en Kotlin, destacando la función `main` como punto de entrada.


### 1.4. Ejemplo de Programa en Kotlin

* Un programa simple que imprime un mensaje.
* Uso de `println` para mostrar salida en consola.

```Kotlin
    //Programa "hola mundo" en Kotlin. Uso de una variable

    fun main() {
        
        val saludo = "Bienvenidos a Kotlin"
        println(saludo)
    }
```

Note: Muestra un ejemplo de programa que declara una variable y la imprime. Ideal para entender la declaración de variables y la salida estándar.


### 1.5. Compilación y Ejecución

* Kotlin se compila a bytecode de Java, ejecutable en la JVM.
* Uso del comando `kotlinc` para compilar.
* Ejecución a través de la JVM o herramientas de Kotlin.

Note: Detalla cómo compilar y ejecutar programas en Kotlin, explicando la relación con la JVM.

---

## 2. Variables en Kotlin


### 2.1. Introducción

* Kotlin maneja dos tipos de variables: `val` y `var`.
* `val` para valores inmutables, `var` para mutables.
* Fuerte inferencia de tipos.

Note: Introduce los conceptos básicos de variables en Kotlin. Explica la diferencia entre `val` (inmutable) y `var` (mutable). No tiene porque tener tipo explicito, pero siempre tendra un tipo implicito. 



### 2.2. Variables Inmutables: `val` I

* `val` se usa para declarar una variable no mutable.
* Una vez asignado, su valor no puede cambiar.

```Kotlin
    // Definición de una variable no mutable
    val saludo = "Hola Mundo"
```

Note: Explica el uso de `val` para inmutalbes. La diferencia con constantes, es que las constantes siempre tienen valor, mientras las inmutables pueden no estar asignadas, y una vez se asignas no cambiarán de valor. Muestra ejemplos con y sin especificación de tipo.


### 2.2. Variables Inmutables: `val` II

* `const val` se puede usar para definir una constante.
* Su valor se define en tiempo de compilación, su valor no puede cambiar.

```Kotlin
    // Definición de una constante
    const val PREFIJO = "tde_"
```

Note: Explica el uso de `val` para inmutalbes. La diferencia con constantes, es que las constantes siempre tienen valor, mientras las inmutables pueden no estar asignadas, y una vez se asignas no cambiarán de valor. Muestra ejemplos con y sin especificación de tipo.


### 2.3. Variables Mutables: `var`

* `var` permite cambiar el valor de la variable.
* Útil cuando se necesita modificar el valor.

```Kotlin
    // Definición de una variable mutable
    var edad = 30
    edad = 31
```

Note: Detalla el uso de `var` para variables que pueden cambiar. Muestra un ejemplo de cómo se puede modificar el valor. 

---
"""""""

IMPORTANTE!!!!!! Como  has visto en el ejemplo:

1. SIEMPRE usar """---""" para separar secciones de los documentos de slides.
2. SIEMPRE usar """2 lineas en blanco""" para separar las slides dentro de una sección de los documentos de slides.
3. En los documentos de slides no aparecerá """----""" ni """2 lineas en blanco""" en ningun otro lugar que no sea para separar secciones o slides respectivamente. Ya que si no, se romperá el formato de las slides.


El PLAN DE TRABAJO con el que trabajarás para generar las slides, será la siguiente:

1. Piensa los grandes grupos de contenidos, que serán las secciones o grupo de slides.
2. Piensa el contenido de cada sección, y por tanto que slides tendrán cada sección.
3. Genera las slides de cada sección, hasta completar todas las secciones.
4. Antes de terminar, asegurate haber contemplado todo el contenido del documento origen desde el que generamos las slides.


### 2.4. Estructura de prácticas

Los archivos de práctica (`practica/`) deben incluir:

```markdown
---
title: "UD X - PY: Título de la práctica"
summary: Resumen de la práctica
description: Descripción detallada
authors:
    - Eduardo Fdez
date: YYYY-MM-DD
icon: "material/file-document-edit"
permalink: /modulo/unidadX/pY
categories:
    - MODULO
tags:
    - Software
    - Ejercicios
---

## PX.Y - Título de la práctica

[Introducción a la práctica]

### 1. Objetivos

- Objetivo 1
- Objetivo 2

### 2. Pasos a seguir

#### 2.1. Paso 1

[Instrucciones claras y numeradas]

[Capturas de pantalla si es necesario]

#### 2.2. Paso 2

[Continuar con estructura similar]

### 3. Ejercicios

[Ejercicios propuestos para los alumnos y alumnas]
```

Los archivos de práctica (`practica/otrosRecursos)/`) pueden incluir ficheros adicionales necesarios para completar la práctica, como plantillas, datos de ejemplo, etc., asi como el ejercicio resuelto. Se generará un fichero con el mismo nombre y la extensión -solución.md, que contendrá la solución al ejercicio propuesto.

### 2.5. Generación de preguntas tipo test en formato Gift, para evaluar la teoría

Las preguntas para cuestionarios se generarán en formato GIFT, siguiendo estas pautas:

Este tipo de preguntas se utilizarán para examinar la parte teorica. Deben redactarse en español de España y con un estilo relajado y amistoso, pero sin perder la formalidad necesaria para un entorno educativo.

Lo siguiente es la descripción básica del formato GIFT para preguntas de opción múltiple (cuatro opciones y solo una correcta):

- Lo primero que nos encontramos es el agrupador de la pregunta que irá encerrado entre doble dos puntos (::).  A continuación irá la pregunta. Un ejemplo sería: "::Agrupación::Pregunta". La agrupación suele ser el Resultado de aprendizaje y el criterio de evaluación al que pertenece la pregunta, con una estructura similar a la siguiente: "RA_X.CE_Y. Descripción corta del RA y CE".
- A continuación, se escribe la pregunta, que será lo más descriptiva posible.  Aunque no tiene por qué ser una pregunta, puede plantear  una situación práctica o ejemplo relacionado con el contenido del archivo teoria al que acompaña.
- Las posibles respuestas se encierran entre llaves {}.
- Las respuestas incorrectas iran prefijadas de la tilde (~), y la correcta del signo igual (=).
- Las respuestas incorrectas restan -33.3333 puntos, y se refleja después del símbolo tilde (~) encerrando entre el simbolo porcentaje (%) el porcentaje que resta, y a continuación la respuesta erronea. Por ejemplo: ~%-33.3333%Madrid #Incorrecta, Madrid es capital de España.
- La retroalimentación debe ir después de la respuesta, precedida del símbolo almohadilla (#), y debe clarificar al alumno porque es o no es correcta la respuesta. Por ejemplo: ~%-33.3333%Madrid #Incorrecta, Madrid es capital de España.

Aquí tienes un ejemplo completo de la sintaxis siguiendo las pautas:

```gift
::RA_X.CE_Y. Conoce las capitales de Europa::
¿Capital de Francia? {
=París #Correcto, París es la capital de Francia desde que se estableció la capitalidad en el siglo X.
~%-33.3333%Madrid #Incorrecto, Madrid es capital de España.
~%-33.3333%Roma #Incorrecto, Roma es la capital de Italia
~%-33.3333%Lóndres #Incorrecto, Lóndres es la capital de Inglaterra.
}
```
Ahora te presento un ejemplo de como quiero que generes las preguntas en formato GIFT. Las preguntas tienen que estar planteadas con un enfoque en la claridad y la retroalimentación educativa. Preguntas con un estilo práctico y relacionada con el contenido del archivo teoria al que acompaña, es decir, basadas en un supuestos prácticos del mundo real sobre la base del contenido del archivo teoria al que acompaña:

```gift
::CE 1.4 – Transpiladores para la web::
Quieres ejecutar lógica de negocio del cliente en el navegador, pero el equipo escribe en TypeScript. ¿Qué estrategia encaja según tu conocimiento?
{
 =Transpilar a JavaScript para que el navegador lo ejecute. #Correcto: La transpilación es una técnica que nos permite convertir código escrito en un lenguaje a otro lenguaje, en este caso a JavaScript, que es el lenguaje nativo de los navegadores web. 
 ~%-33.3333%Compilar a .exe y subir el binario al servidor web. #Incorrecto: el navegador no ejecuta .exe por seguridad. Aunque con WebAssembly podríamos ejecutar código nativo, no es el caso de .exe.
 ~%-33.3333%Generar bytecode JVM y traspilarlo al formato que permita cargarlo directamente en el navegador. #Incorrecto: los navegadores no tienen una JVM nativa, ni podemos traspilar bytecode JVM a JavaScript de forma directa, por lo que esta opción no es viable.
 ~%-33.3333%Interpretar TypeScript directamente en el motor JS del cliente. #Incorrecto: Los navegadores no interpretan TypeScript de forma nativa, por lo que es necesario transpilarlo a JavaScript antes de su ejecución.
}
```

Además de las anteriores, también puede haber un porcentaje de preguntas basadas en definiciones o conceptos clave del tema tratado en el archivo teoria al que acompaña, pero siempre intentando que las respuestas incorrectas sean respuestas que puedan parecer correctas, para evitar que se pueda responder correctamente por descarte de las respuestas incorrectas.

IMPORTANTE Y OBLIGATORIO seguir las siguientes reglas al generar los archivos GIFT:
- Las normas específicas del formato GIFT.
- Cualquier caracter usado en el formato GIFT que pueda generar conflicto, como los símbolos de porcentaje (%), tilde (~), igual (=), almohadilla (#), llaves ({, }), o dos puntos (::), deben ser escapados con una barra invertida (\) para evitar errores de interpretación.
- Evitar un tono demasiado formal o complicado.
- Proporcionar respuestas o retroalimentaciones formativas y completas, evitando retroalimentación genérica.
- IMPORTANTE: De las posibles respuestas a la pregunta generada, las respuestas incorrectas tienen que ser repuestas que puedan parecer correctas, ya que si no es así, se podrá responder correctamente por descarte de las respuestas incorrectas.
- Las preguntas deben estar relacionadas con el contenido del archivo teoria al que acompañan. Esto es importante, ya que no se trata de generar preguntas aleatorias, sino preguntas que evalúen el conocimiento adquirido en el tema tratado en el archivo teoria. Preguntas con respuestas que no tengan relación con el contenido del archivo teoria no serán aceptadas. En el feedback de las respuestas, se debe explicar claramente por qué la respuesta correcta es correcta y por qué las respuestas incorrectas no lo son, haciendo referencia a los conceptos clave del tema tratado en el archivo teoria.
- Las preguntas tienen que plantear situaciones prácticas o ejemplos relacionados con el contenido del archivo teoria, de forma que se evalúe no solo el conocimiento teórico, sino también la capacidad de aplicar ese conocimiento en situaciones prácticas. No hacer referencia en las preguntas a "según la unidad vista", "según lo visto en el texto", "según lo que dice la unidad"; etc., sinó a los conceptos y ejemplos tratados en el archivo teoria.
- Cada archivo GIFT contendrá al menos 15 preguntas de opción múltiple relacionadas con el contenido del archivo teoria al que acompañan.
- Las preguntas tienen que cubrir los conceptos clave del tema tratado en el archivo teoria.
- Las preguntas tienen que ser basadas en supuestos prácticos o ejemplos del contenido del archivo teoria, de forma que además de evaluar el conocimiento teórico, se evalúe la capacidad de aplicar ese conocimiento en situaciones prácticas.
- En la carpeta sectionZ/u0X/gift habrá un archivo formato gift con nombre MODULO-UX.Y.-Tema.gift por cada archivo MODULO-UX.Y.-Tema.md contenido en la carpeta sectionZ/u0X/teoria/ . Por tanto el nombre del archivo GIFT será el mismo que el del archivo teoria al que acompaña, pero con la extensión .gift. Por ejemplo: MODULO-UX.Y.-Tema.gift.
- El archivo GIFT se ubicará en la carpeta gifts/ al mismo nivel que la carpeta teoria/ del módulo correspondiente.

### 2.6. Convenciones de estilo en los documentos de TEORIA generados 

**Elementos de Markdown:**

- Usar `### X. ` para secciones principales X, `#### X.Y. ` para subsecciones X.Y, `##### X.Y.Z. ` para subsubsecciones X.Y.Z, y asi sucesivamente.
- No usar "---" para separar bloques.
- No usar emoticonos en el texto.
- Incluir imágenes con `<figure markdown>` y `<figcaption>`
    ```
    <figure markdown="span">
      ![Image title](https://dummyimage.com/600x400/){ width="300" }
      <figcaption>Image caption</figcaption>
    </figure>
    ```
- Usar admonitions para alertas de puntos importantes durante los desarrollos del tema:
  ```markdown
  !!! note "Nota"
      Texto de la nota
  
  !!! warning "Atención"
      Texto de advertencia
  
  !!! tip "Consejo"
      Texto de consejo
  
  !!! quote "Cita"
      "Texto de la cita"
  
  !!! success "Indicador de madurez"
      Texto exitoso
  
  !!! example "Ejemplo"
      Texto del ejemplo

  !!! info "Información"
      Texto informativo
  
  !!! danger "Peligro"
      Texto de peligro
  
  !!! question "Pregunta"
      Texto de la pregunta
  
  !!! abstract "Resumen"
      Texto del resumen
  
  !!! definition "Definición"
      Texto de la definición
  
  ```

**Código:**

- Bloques de código con sintaxis específica:
  ````markdown
  ```python
  # Código Python
  ```
  
  ```kotlin
  // Código Kotlin
  ```
  ````

**Lenguaje:**

- Dirigirse a "alumnos y alumnas" o "estudiantes"
- Usar segunda persona del plural cuando sea apropiado ("debéis", "podéis")
- Evitar tecnicismos innecesarios
- Incluir glosario de términos técnicos cuando sea necesario
- Usar ejemplos prácticos y casos de uso reales
- Enlazar y encadenar cada uno de los conceptos explicados con otros conceptos relacionados ya explicados en otros temas o unidades del mismo módulo, o de otros módulos, para facilitar la comprensión y el aprendizaje significativo.
- Dar una introducción clara y que enlace cada punto tratado con el siguiente punto a tratar, para facilitar la comprensión y el aprendizaje significativo. 
- Evitar que hay puntos que quedan como una simple lista de cosas sin una introducción clara y sin un cierre que enlace con el siguiente punto a tratar.

### 2.7. Metadatos obligatorios

#### 2.7.1. Metadatos en documentos de TEORÍA

Todos los documentos de teoría deben incluir el bloque YAML al inicio con:

- `title`: Título completo del documento
- `description`: Descripción para SEO (recomendado: 150-160 caracteres)
- `summary`: Resumen breve del contenido
- `authors`: Autor(es) del documento
- `date`: Fecha de creación/última modificación (formato YYYY-MM-DD)
- `icon`: **Icono del documento** → `"material/file-document-outline"`
- `permalink`: URL amigable para el documento
- `categories`: Categoría del módulo
- `tags`: Etiquetas relevantes para búsqueda y clasificación

**Ejemplo de metadatos completos para teoría:**

```yaml
---
title: "UD 2 - 2.4.1 Documentación de incidentes"
description: "Aprende qué documentar en un incidente de seguridad y por qué es crucial"
summary: "Guía completa sobre gestión y documentación de incidentes de seguridad"
authors:
    - Eduardo Fdez
date: 2025-11-25
icon: "material/file-document-outline"
permalink: /is/unidad-2/2.4.1-documentacion-de-incidentes
categories:
    - "Incidentes de seguridad"
tags:
    - "Incidentes"
    - "Documentación"
    - "Seguridad"
---
```

#### 2.7.2. Metadatos en documentos de PRÁCTICA

Todos los documentos de práctica deben incluir el bloque YAML al inicio con:

- `title`: Título de la práctica
- `description`: Descripción breve de la práctica
- `summary`: Resumen de los objetivos
- `authors`: Autor(es) del documento
- `date`: Fecha de creación/última modificación
- `icon`: **Icono de práctica** → `"material/file-document-edit"`
- `permalink`: URL amigable
- `categories`: Categoría del módulo
- `tags`: Etiquetas relevantes

**Ejemplo de metadatos completos para práctica:**

```yaml
---
title: "UD 2 - P1: Taxonomía"
description: "Práctica sobre taxonomía de incidentes de seguridad"
summary: "Clasificación práctica de incidentes según taxonomía"
authors:
    - Eduardo Fdez
date: 2023-12-11
icon: "material/file-document-edit"
permalink: /is/unidad2/p2.1
categories:
    - IS
tags:
    - Incidentes
    - Taxonomía
---
```

!!! warning "Importante: Campo icon obligatorio"
    El campo `icon` es **obligatorio** en todos los documentos:
    
    - **Teoría**: `icon: "material/file-document-outline"`
    - **Práctica**: `icon: "material/file-document-edit"`
    
    Este campo permite la correcta visualización de iconos en MkDocs Material.


### 2.8. Normativa sobre el módulo

Todos los módulos deben incluir en la carpeta `recursos/` un archivo llamado:
MODULO Normativa.txt, en donde MODULO es el nombre del módulo correspondiente, y que contendrá la normativa oficial del módulo, con los Resultados de aprendizaje y sus criterios de evaluación. Este archivo servirá de referencia para generar la documentación, prácticas, cuestionarios, exámenes, etc.

Ej: Para el módulo de programación, "docs/section1/recursos/PRO Normativa.txt"

Lo normal esque tanto la teoría, como la practica haga referencia a los Resultados de aprendizaje y sus criterios de evaluación, por lo que es importante que este archivo esté siempre actualizado y disponible.

## 3. Flujo de trabajo para crear contenido

1. **Identificar el módulo y unidad** donde se creará el contenido
2. **Determinar el tipo**: ¿teoría o práctica?
3. **Crear el archivo** con la nomenclatura correcta: `MODULO-UX.Y.-Tema.md`
4. **Incluir metadatos YAML** completos
5. **Desarrollar el contenido** siguiendo el patrón correspondiente
6. **Agregar assets** en la carpeta `assets/` si es necesario
7. **Actualizar `mkdocs.yml`** para incluir el nuevo contenido en la navegación
8. **Revisar** que el lenguaje sea inclusivo y didáctico

## 4. Herramientas y comandos útiles

- **Visualizar el sitio localmente**: `mkdocs serve`
- **Construir el sitio**: `mkdocs build`
- **Validar enlaces**: Revisar que todos los enlaces internos funcionen

## 5. Principios pedagógicos

Al crear o modificar documentación, recordar:

1. **Progresión**: Ir de lo simple a lo complejo
2. **Ejemplos reales**: Usar casos prácticos relevantes
3. **Refuerzo**: Incluir ejercicios al final de cada tema
4. **Visual**: Usar diagramas e imágenes para clarificar conceptos
5. **Retroalimentación**: Proporcionar soluciones o pistas para los ejercicios
6. **Motivación**: Explicar por qué es importante cada concepto

## 6. Lista de verificación de estructura

Para verificar que un nuevo contenido cumple con la estructura y estándares del repositorio, usa esta checklist:

### 6.1. Verificación de módulo completo

- [ ] Existe `docs/sectionX/index.md` con descripción del módulo
- [ ] Existe `docs/sectionX/recursos/MODULO Normativa.txt` con los RA y CE
- [ ] Todas las unidades tienen su carpeta `uXX/`

### 6.2. Verificación de unidad

- [ ] Existe `docs/sectionX/uXX/index.md` con planificación de la unidad
- [ ] Existe carpeta `teoria/` con documentos de contenido
- [ ] Existe carpeta `practica/` (o `practicas/`) con ejercicios
- [ ] [Opcional] Existe carpeta `gift/` con cuestionarios

### 6.3. Verificación de documentos de teoría

- [ ] Nomenclatura correcta: `MODULO-UX.Y.-NombreDescriptivo.md`
- [ ] Metadatos YAML completos al inicio del archivo
- [ ] Campo `icon: "material/file-document-outline"` presente
- [ ] Estructura con títulos jerárquicos (##, ###, ####)
- [ ] Enlaces entre conceptos relacionados
- [ ] Uso de admonitions para resaltar información importante
- [ ] Imágenes en carpeta `assets/` con referencias correctas
- [ ] Lenguaje inclusivo y didáctico
- [ ] Enlace a slide correspondiente (si existe)

### 6.4. Verificación de documentos de práctica

- [ ] Nomenclatura correcta: `MODULO-UX.-PracticaYYY.md` (sin punto Y)
- [ ] Metadatos YAML completos al inicio del archivo
- [ ] Campo `icon: "material/file-document-edit"` presente
- [ ] Descripción clara de objetivos
- [ ] Instrucciones paso a paso
- [ ] Criterios de evaluación definidos
- [ ] Recursos necesarios listados
- [ ] Tiempo estimado indicado

### 6.5. Verificación de slides

- [ ] Archivo `.md` fuente en `slides/sectionX-XX/`
- [ ] Archivo `.html` generado correspondiente
- [ ] Nomenclatura correcta: `MODULO-UX.Y.-NombreDescriptivo`
- [ ] Rutas relativas correctas (`../dist/`, `../plugin/`, `../custom.css`)
- [ ] Configuración de Reveal.js completa
- [ ] Assets en carpeta `assets/` del módulo
- [ ] Referencias a la slide desde documentos de teoría actualizadas

### 6.6. Verificación de integración

- [ ] Nuevo contenido añadido a `mkdocs.yml` en sección `nav`
- [ ] Enlaces internos funcionan correctamente
- [ ] Enlaces a slides usan URLs absolutas
- [ ] Imágenes se visualizan correctamente
- [ ] `mkdocs serve` funciona sin errores
- [ ] `mkdocs build` genera el sitio sin warnings críticos

### 6.7. Comandos de verificación rápida

```bash
# Verificar metadatos con icon en teoría
grep -r '^icon: "material/file-document-outline"' docs/sectionX/*/teoria/*.md

# Verificar metadatos con icon en práctica
grep -r '^icon: "material/file-document-edit"' docs/sectionX/*/practica*/*.md

# Verificar estructura de una unidad
ls -la docs/sectionX/uXX/

# Verificar slides de un módulo
ls slides/sectionX-XX/

# Probar el sitio localmente
mkdocs serve
```

## 7. Nomenclatura y convenciones adicionales

### 7.1. Nomenclatura de archivos de práctica

**Importante**: Los archivos de práctica NO incluyen el punto Y (tema), solo la unidad X:

- ✅ Correcto: `IS-U2.-Practica001.md` (Incidentes, Unidad 2, Práctica 1)
- ❌ Incorrecto: `IS-U2.1.-Practica001.md` (no se usa punto de tema)

**Formato**: `MODULO-UX.-PracticaYYY.md`
- `MODULO` = Prefijo del módulo (IS, PR, EDES, DAW)
- `X` = Número de unidad
- `YYY` = Número de práctica con ceros a la izquierda (001, 002, ...)

### 7.2. Consistencia en carpetas

| Elemento                    | Convención                | Ejemplo                                   |
|-----------------------------|---------------------------|-------------------------------------------|
| Carpeta de teoría           | `teoria/`                 | `docs/section2/u02/teoria/`               |
| Carpeta de práctica         | `practica/` (recomendado) | `docs/section1/u01/practica/`             |
| Carpeta de assets           | `assets/`                 | `docs/section2/u02/teoria/assets/`        |
| Carpeta de recursos         | `OtrosRecursos/`          | `docs/section2/u02/teoria/OtrosRecursos/` |
| Carpeta GIFT                | `gift/` (opcional)        | `docs/section2/u02/gift/`                 |


### 7.2. Nomenclatura de archivos de slides

| Elemento                        | Convención              | Ejemplo                                   |
|---------------------------------|-------------------------|-------------------------------------------|
| Carpeta de slides del modulo ZZ | `sectionX-ZZ/`          | `slides/section2-is/`                     |
| Carpeta de assets de slides     | `sectionX-ZZ/assets/`   | `slides/section2-is/assets`               |

