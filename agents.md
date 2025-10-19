
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

**Nomenclatura de archivos:**
- section1: `PR-UX.Y.-NombreDescriptivo`
- section2: `IS-UX.Y.-NombreDescriptivo`
- section3: `ED-UX.Y.-NombreDescriptivo`
- section4: `DAW-UX.Y.-NombreDescriptivo`

Donde:
- `X` = número de unidad
- `Y` = número de punto dentro de la unidad
- Ejemplo: `DAW-U2.1.-Docker` → Despliegue de Aplicaciones Web, Unidad 2, punto 1, tema Docker

Cada tema tiene dos archivos:
- `.md` (fuente en Markdown)
- `.html` (presentación Reveal.js generada)

**Configuración de las presentaciones:**

Todas las presentaciones HTML incluyen:
- `custom.css`: CSS personalizado que fuerza la visualización de la barra de progreso y los números de diapositiva
- Configuración en `Reveal.initialize()`:
  - `margin: 0.1` - Margen del 10% alrededor del contenido
  - `progress: true` - Barra de progreso visible
  - `slideNumber: 'c/t'` - Número de diapositiva actual/total
  - `showSlideNumber: 'all'` - Mostrar en todas las diapositivas

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

[Ejemplos si procede]

<figure markdown>   
  ![](assets/nombre-imagen.png)   
  <figcaption>Descripción de la imagen</figcaption>   
</figure>

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
