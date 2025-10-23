
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
└── uXX/                        # Unidades didácticas (u01, u02, u03...)
    ├── index.md                # Descripción de la unidad, contenidos y planificación
    ├── teoria/                 # Contenidos teóricos
    │   ├── MODULO-UX.Y.-Tema.md
    │   ├── assets/             # Imágenes y recursos multimedia
    │   └── OtrosRecursos/      # Archivos adicionales (PDFs, plantillas, etc.)
    └── practica/               # Prácticas y ejercicios
        ├── MODULO-UX.-PracticaYYY.md
        ├── assets/             # Imágenes y recursos multimedia
        └── OtrosRecursos/      # Archivos adicionales necesarios
```

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

**Formato de las slides**
A continuación explicamos el proceso de creación de presentaciones de diapositivas sobre contendios, que normalmente serán de los módulos de informática. Generará slides siguiendo una estructura de markdown precisa (MUY IMPORTANTE SEGUIR LA NOTACIÓN MARKDOWN).

sigue concienzudamente estas reglas:

- El contenido a generar son un conjunto de slides, formadas por  grupos de slides denominadas  <<secciones>>, y dentro de cada sección hay varias slides relacionadas con la sección. 
- Las secciones comienzan con títulos de nivel dos  (##).
- Las secciones contienen distintas slides que hablan sobre conceptos o contenido relacionado con el titulo de la sección.
- El comienzo de un grupo de slides o sección, puede ser una sola slide con el titulo de la sección, sin ningún contenido mas.
- Cada grupo de slides o sección se delimitará con una línea horizontal (---). 
- Usa --- solo para separar grupos de slides o sección  
- Cada slide de una sección ,en la que se tratará temas relacionados con la sección, continuará con títulos de nivel tres (###).
- Una slide de un mismo grupo (misma sección) se separarán con 2 lineas en blanco de la siguiente slide, y se distinguirán por títulos sin números de slide. IMPORTANTE: No te olvides nunca las 2 lineas en blanco para separar las slides de un grupo de lides o seccion.
- Una slide con contenido es: una lista de máximo siete viñetas, con tamaño de linea limitadas a 80 caracteres máximo. 
- Una slide con contenido tambien pueden contener código fuente en un determinado lenguaje de programación, en cuyo caso el codigo fuente incluirá comentarios sobre aclaraciones del código de ejemplo. 
- Cuando se esá tratando un concepto o un área concreta de un punto de unidad, puede quedarse corto con solo una slide con contenido, en cuyo caso se podra generar una segunda, tercera, etc. slide con el mismo titulo e identificandolas con el mismo titulo pero con número romanos I, II, III, etc.  
- Al final de TODAS las slides, se crearán notas para el presentador, mas extensas y en las que se describirá el contenido de cada uno de los puntos de las slide o información adicional que no cabe en la  slide.
- Las notas vendrán identificadas y precedidas por la palabra "Note:"
- Las notas deben contener todos los comentarios necesarios que el profesor debe hacer para que ningún contenido se deje sin cubrir sobre el punto tratado en en la slide.
- Todas las interacciones y contenido proporcionado estarán en español.

IMPORTANTE:
- SIEMPRE genera el resultado en markdown.
- NUNCA generes mas de 7 lineas (viñetas) por slide.
- NUNCA generes líneas de mas de 80 caracteres.
- RESPETA las separaciones de slides (2 lineas en blanco ) y secciones (---), tal como se indica.

Un ejemplo sería el siguiente:
            """""""
            ## U4.1 - Kotlin Básico    

            ---

            ![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

            ---

            ## Indice

            ---

            ## Introducción


            ### Kotlin

            * Kotlin: un lenguaje de programación moderno y versátil.
            * Desarrollado por JetBrains, lanzado en 2011.
            * Interoperable con Java, popular en desarrollo Android.

            Note: Presenta Kotlin, su origen y su popularidad, especialmente en el desarrollo de Android y su interoperabilidad con Java.


            ### Características de Kotlin

            * Sintaxis concisa y expresiva.
            * Seguridad de tipos nulos integrada.
            * Soporta programación funcional y orientada a objetos.

            Note: Resalta las características clave de Kotlin, como la sintaxis concisa, la seguridad de tipos nulos y el soporte para paradigmas de programación.


            ### Configuración del Entorno de Kotlin

            * Kotlin puede ser usado con IntelliJ IDEA, Android Studio, o cualquier editor de texto.
            * Compilador de Kotlin disponible para línea de comandos.
            * Kotlin Playground: para experimentar en línea.

            Note: Ofrece opciones para configurar el entorno de desarrollo para Kotlin, incluyendo IDE's y herramientas en línea.


            ### Estructura Básica de un Programa en Kotlin

            * Todo programa en Kotlin comienza con la función `main`.
            * `main` es el punto de entrada del programa.

            ```Kotlin
                //Programa "hola mundo" en Kotlin
                fun main() {
                    println("Hola, Kotlin!")
                }
            ```
            Note: Explica la estructura básica de un programa en Kotlin, destacando la función `main` como punto de entrada.


            ### Ejemplo de Programa en Kotlin

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


            ### Compilación y Ejecución

            * Kotlin se compila a bytecode de Java, ejecutable en la JVM.
            * Uso del comando `kotlinc` para compilar.
            * Ejecución a través de la JVM o herramientas de Kotlin.

            Note: Detalla cómo compilar y ejecutar programas en Kotlin, explicando la relación con la JVM.

            ---

            ## Variables en Kotlin


            ### Introducción

            * Kotlin maneja dos tipos de variables: `val` y `var`.
            * `val` para valores inmutables, `var` para mutables.
            * Fuerte inferencia de tipos.

            Note: Introduce los conceptos básicos de variables en Kotlin. Explica la diferencia entre `val` (inmutable) y `var` (mutable). No tiene porque tener tipo explicito, pero siempre tendra un tipo implicito. 



            ### Variables Inmutables: `val`

            * `val` se usa para declarar una constante.
            * Una vez asignado, su valor no puede cambiar.

            ```Kotlin
                // Definición de una variable no mutable
                val saludo = "Hola Mundo"
            ```

            Note: Explica el uso de `val` para inmutalbes. La diferencia con constantes, es que las constantes siempre tienen valor, mientras las inmutables pueden no estar asignadas, y una vez se asignas no cambiarán de valor. Muestra ejemplos con y sin especificación de tipo.



            ### Variables Mutables: `var`

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

Como  has visto en el ejemplo:   
* --- se utiliza para separar secciones 
* 2 lineas en blanco para separar las slides dentro de una sección. 


La forma en la que trabajaras para generar las slides, será la siguiente:

1. Piensa los grandes grupos de contenidos, que serán las secciones o grupo de slides.
2. Piensa el contenido de cada sección, y por tanto que slides tendrán cada sección. 
3. Genera las slides de cada sección, hasta completar todas las secciones.


**Configuración de las presentaciones:**

Todas las presentaciones HTML incluyen:
- `custom.css`: CSS personalizado que fuerza la visualización de la barra de progreso y los números de diapositiva (ubicado en `slides/custom.css`)
- Configuración en `Reveal.initialize()`:
  - `margin: 0.1` - Margen del 10% alrededor del contenido
  - `progress: true` - Barra de progreso visible
  - `slideNumber: 'c/t'` - Número de diapositiva actual/total
  - `showSlideNumber: 'all'` - Mostrar en todas las diapositivas

**Referencias a las slides desde `docs/`:**

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
icon: 
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

Es un texto de explicativo de como generar la documentación siguiendo este patrón:
- Ser claro y concisos.
    - Usar listas para organizar ideas, pero no abusar de ellas.
        - Asegurarse de que cada punto aporta valor.
        - Dividir el contenido en secciones lógicas.
    - Incluir definiciones cuando sea necesario.
- Incluir ejemplos visuales.
- Usar subtítulos para organizar la información.

Tambien se pueden incluir listas de numeradas:
1. Primer punto importante
2. Segundo punto relevante
   
    - Y anidar las viñetas si es necesario
    
3. Tercer punto clave


- Se pueden incluir citas en bloque para resaltar definiciones o ideas clave:
> La programación es el proceso de crear un conjunto de instrucciones que le dicen a una computadora cómo

Se pueden incluir bloques de código para ilustrar ejemplos prácticos:

También es importante incluir imágenes o diagramas para ilustrar conceptos complejos.

[Ejemplos si procede]

<figure markdown>   
  ![](assets/nombre-imagen.png)   
  <figcaption>Descripción de la imagen</figcaption>   
</figure>

#### 1.1. Subconcepto o ejemplo práctico

[Explicación detallada del subconcepto]


### 2. Segundo concepto

[Continuar con estructura similar]
```


### 2.3. Estructura de prácticas

Los archivos de práctica (`practica/`) deben incluir:

```markdown
---
title: "UD X - PY: Título de la práctica"
summary: Resumen de la práctica
description: Descripción detallada
authors:
    - Eduardo Fdez
date: YYYY-MM-DD
icon: 
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

### 2.4. Convenciones de estilo

**Elementos de Markdown:**

- Usar `###` para secciones principales, `####` para subsecciones
- Incluir imágenes con `<figure markdown>` y `<figcaption>`
- Usar admonitions para notas importantes:
  ```markdown
  !!! note "Nota"
      Texto de la nota
  
  !!! warning "Atención"
      Texto de advertencia
  
  !!! tip "Consejo"
      Texto de consejo
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

### 2.5. Metadatos obligatorios

Todos los documentos deben incluir el bloque YAML al inicio con:

- `title`: Título completo
- `description`: Descripción SEO
- `summary`: Resumen breve
- `authors`: Autor(es)
- `date`: Fecha de creación/modificación
- `permalink`: URL amigable
- `categories`: Categoría del módulo
- `tags`: Etiquetas relevantes

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
