---
title: "UD 6 - P1: CI/CD y documentación con GitHub Actions"
description: "Mejorando un workflow con GitHub Actions para generar y publicar documentación"
summary: "Actividad práctica para automatizar tests y documentación multi-formato con GitHub Actions y buenas prácticas de control de versiones."
authors:
  - Eduardo Fdez
date: 2025-10-02
icon:
permalink: /deaw/unidad6/p1.1
categories:
  - DAWeb
tags:
  - CI/CD
  - GitHub Actions
  - Documentación
  - Control de versiones
---

## Relación 1.1

### Descripción

**Actividad:** *Mejorando un Workflow con GitHub Actions*

Vas a partir de un **repositorio base** (visto en clase) que contiene:

* `main.py` — programa sencillo.
* `test_main.py` — test unitario.
* `update_readme.py` — ejecuta los tests y actualiza el `README.md`.
* `.github/workflows/ci.yml` — *workflow* básico que ejecuta el script y realiza *commit* automático usando `git-auto-commit-action`.

#### Objetivo general

Aprender, de forma incremental, a:

* Generar y versionar documentación **en distintos formatos**.
* Automatizar su **generación y actualización** con **GitHub Actions** (CI/CD).
* Documentar el proceso (herramientas, comandos, *workflow*, evidencia en *commits* y acceso por SSH).

---

### Contexto de trabajo

En la primera parte, trabajarás **sobre tu *fork*** del repositorio base. Deberás ejecutar y **entender** el script y el *workflow* inicial, y después **mejorarlo**. 

Para la segunda y tercera parte, debes usar **tu propio proyecto**, el que usarás para desarrollar el proyecto intemodular que se realizará durante el ciclo.

Se espera un nivel mínimo común (Parte 1 y 2) y la posibilidad de profundizar (Parte 3 opcional).

---

### 🔹 Parte 1: Workflow básico (comprensión y validación)

1. **Clona** tu *fork* del repositorio base.
2. **Lee y comprende**:

    * Qué hace `update_readme.py`.
    * Qué hace el *job* definido en `.github/workflows/ci.yml`.

3. **Ejecuta el workflow manualmente** (evento `workflow_dispatch` desde la pestaña *Actions*):

    * Fuerza **tests correctos** para ver el mensaje ✅ en `README.md`.
    * Fuerza **tests fallidos** para ver el mensaje ❌ en `README.md`.

4. Observa el ciclo: **evento → ejecución → modificación → *commit* automático** y confirma en el historial de *commits*.

> Esta parte ya la has debido hacer en clase. Te ha servido para tener una primera toma de contacto y entender que todo el proceso o preguntar las dudas para llegar a entenderlo. No se entrega. 

---

### 🔹 Parte 2: Mejora obligatoria (nivel básico)

#### A. Trabajo técnico, para generación automático de documentación multi-formato

Prepara tu proyecto intermodular para **la generación de documentación en HTML y al menos otro formato adicional** de forma automática con GitHubActions y el uso de otras herramientas que se ajusten a las tecnologías que uses.

Sugerencias para Python:

* Formato / Estilo de documentación: **reStructuredText** o **Google Style**. Para ello tendrás que revisar las guías de estilo de la herramienta que elijas. Tendrás que revisar las guías de estilo del lenguaje que uses.
* **Sphinx** o **pdoc** (HTML). Tendrás que revisar el funcionamiento de la herramienta que elijas.
* Segundo formato: **PDF** (vía `sphinxcontrib-rsvgconverter`/LaTeX) o **Markdown** (por ejemplo con **pdoc** o **pandoc**).

**Requisitos mínimos:**

1. Estilo de documentación seleccionado.
2. Documenta algún código básico para que la herramienta pueda generar documentación, y asi comprobar que funciona.
2. Estudia y prepara la herramienta elegida para generar documentación en **HTML** y **otro formato**.
2. Genera documentación **localmente** (fuera de GitHub) y comprueba que funciona.
3. Extiende todo al *workflow*:   

    * Instala dependencias (`pip install ...`).
    * **Genera documentación** en `docs/` (por ejemplo `docs/_build/html/index.html`).
    * **Genera un segundo formato** (p. ej., `docs/pdf/report.pdf` o `docs/md/report.md`).
    * **Sube artefactos** del *job* (Action `actions/upload-artifact`) *o* **hace commit** de `docs/` al repositorio (con `git-auto-commit-action`), dejando claro en los mensajes de *commit* qué se genera y por qué.


> Entregables de esta parte: enlaces repositorio, con el `docs/` (HTML + otro formato) y el flujo que los genera.   

> El lenguaje de programación es libre y dependerá del proyecto que te plantees hacer. Es my posible que sea Java + JS.   

> Si tienes que generar algun script que complemente el flujo del action para generar la documentación, tu decides el lenguaje. No tiene porque ser Python.   

> El profesor clonará el repositorio y ejecutará el workflow para comprobar que funciona correctamente.


#### B. Documentación del proceso y preguntas (evidencias)

**Actualiza tu `README.md`** para que incluya, con enlaces, **toda** esta información:

Ten en cuenta que el `README.md` es la **carta de presentación** de tu proyecto, y debe ser claro y completo.

* a) **Herramientas** usadas para generar documentación y **comandos** ejecutados.
* b) **Ejemplos de código documentado** (enlace al fuente) y fragmento con las etiquetas/estructura usadas (docstrings, `@param`, `@return`, Kdoc, reStructuredText o Google Style, Estilo según JavaDoc.
* c) **Formatos generados** (HTML + otro) y **enlaces** a cada uno.
* d) **Explicación breve** del *workflow* (pasos del job, eventos que lo disparan).
* e) **Mensajes de *commit*** que evidencien la mejora: claros, descriptivos, en imperativo.
* f) **Evidencia de configuración SSH** para GitHub (clave pública añadida, prueba `ssh -T git@github.com`).
* g) **Cómo clonar/usar** el repositorio para reproducir la generación de documentación.

##### Cuestionario a responder (inclúyelo al final del `README.md`)

Las preguntas son obligatorias y clave para la evaluación, por tanto responde de forma clara y concisa y cociente. 

|   CE  | Pregunta de evaluación asociada a la actividad                                                                                                                                                                                                                                                                  |
| :---: |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a** | **Identificación de herramientas de generación de documentación.** ¿Qué herramienta o generador (p. ej., Sphinx, pdoc, Javadoc, Doxygen, Dokka) utilizaste en el *workflow* para crear la documentación en `/docs`?                                                                                             |
| **b** | **Documentación de componentes.** Muestra un fragmento del código con comentarios/docstrings estructurados (p. ej., `:param`, `:return:` o etiquetas equivalentes) que haya sido procesado por la herramienta. Comenta que estilo de documentación has utlicado: (p. ej., reStructuredText, Google Style, KDoc) |
| **c** | **Multiformato.** ¿Qué **segundo formato** (además de HTML) generaste? Explica la **configuración** o **comandos** del *workflow* y herramientas que lo producen.                                                                                                                                               |
| **d** | **Colaboración.** Explica cómo **GitHub** facilita mantener la documentación (actualizaciones del `README.md` y de `/docs`) cuando colaboran varias personas (PRs, *reviews*, *checks* de CI, protección de ramas).                                                                                             |
| **e** | **Control de versiones.** Muestra **mensajes de *commit*** que evidencien el nuevo *workflow*. ¿Son claros y descriptivos? Justifícalo.  Ademas de un conjunto de mensajes de tus commits.                                                                                                                      |
| **f** | **Accesibilidad y seguridad.** ¿Qué medidas/configuración del repositorio garantizan que solo personal autorizado accede al código y la documentación? (p. ej., repositorio privado, equipos, roles, claves/secretos, *branch protection*).                                                                     |
| **g** | **Instalación/uso documentados.** Indica **dónde** en el `README.md` explicas el funcionamiento del *workflow* y **dónde** detallas las herramientas y comandos de documentación.                                                                                                                               |
| **h** | **Integración continua.** Justifica por qué el *workflow* utilizado es **CI**. ¿Qué **evento** dispara automáticamente la generación/actualización de la documentación (p. ej., `push`, `pull_request`, `workflow_dispatch`)?                                                                                   |

> Aunque se habla de herramientas de documentación para Python, puedes usar cualquier lenguaje y herramienta que permita generar documentación en varios formatos.    

> Sugerencia: añade una sección final de **Conclusiones** en tu `README.md` resumiendo qué aprendiste sobre herramientas de documentación, CI/CD y control de versiones.

---

### 🔹 Parte 3 (opcional, nivel intermedio)

**Publicación de documentación con MkDocs en GitHub Pages**

* Crea un sitio con **MkDocs** (o **MkDocs Material**).
* Añade un *workflow* que construya el sitio y lo publique con **`peaceiris/actions-gh-pages`** en la rama `gh-pages`.
* Incluye en el `README.md` el **enlace público** a la documentación.

---

## Entregables

1. **Enlace a tu repositorio** con el *workflow* funcionando (Runs visibles en *Actions*). Si el repositorio es privado, añade al profesor como colaborador.
2. **Documentación** generada (HTML + otro formato) accesible desde el repositorio.
3. **`README.md` actualizado** con:  

    * Herramientas y comandos utilizados.
    * Explicación del *workflow* y eventos.
    * Enlaces a documentación y artefactos.
    * Respuestas al **cuestionario (a–h)**.
    * Evidencias de *commits* y acceso por **SSH**.

4. (Opcional) **Enlace a GitHub Pages** si implementas MkDocs.

---

### Evaluación

Se evaluará los entregables y las respuestas al cuestionario.

---

### Condiciones de entrega

Las publicadas en la moodle del curso.

---

### Apoyo

* GitHub Actions (documentación): [https://docs.github.com/actions](https://docs.github.com/actions)
* Acciones útiles:

    * `actions/checkout`: [https://github.com/actions/checkout](https://github.com/actions/checkout)
    * `actions/setup-python`: [https://github.com/actions/setup-python](https://github.com/actions/setup-python)
    * `actions/upload-artifact`: [https://github.com/actions/upload-artifact](https://github.com/actions/upload-artifact)
    * `stefanzweifel/git-auto-commit-action`: [https://github.com/stefanzweifel/git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action)
    * `peaceiris/actions-gh-pages`: [https://github.com/peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)

* Generadores de documentación:

    * **Sphinx** (Python): [https://www.sphinx-doc.org](https://www.sphinx-doc.org)
    * **pdoc** (Python): [https://pdoc.dev](https://pdoc.dev)
    * **Doxygen** (multi-lenguaje): [https://www.doxygen.nl](https://www.doxygen.nl)
    * **Javadoc** (Java): [https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)
    * **Dokka** (Kotlin/Java): [https://kotlinlang.org/docs/dokka-overview.html](https://kotlinlang.org/docs/dokka-overview.html)
    * **Pandoc** (multi-formato): [https://pandoc.org](https://pandoc.org)

* Publicación:

    * **MkDocs**: [https://www.mkdocs.org](https://www.mkdocs.org)
    * **MkDocs Material**: [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
