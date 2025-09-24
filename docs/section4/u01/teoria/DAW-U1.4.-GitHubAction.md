---
title: "UD 1 - 1.4 GitHub Actions"
description: Introducción a la integración y entrega continua con GitHub Actions
summary: Qué son las GitHub Actions, cómo se estructuran los workflows y cómo podemos usarlas en proyectos de despliegue de aplicaciones web.
authors:
    - Eduardo Fdez
date: 2025-09-24
icon:   
permalink: /deaw/unidad1/1.4
categories:
    - DAW
tags:
    - GitHub
    - CI/CD
    - DevOps
    - Automatización
    - Actions
---

## 1.4. GitHub Actions

En esta unidad vamos a aprender a **automatizar tareas dentro de un repositorio de GitHub** usando **GitHub Actions**.  Algo fundamental para cualquier perfil DevOps y para entender cómo se integran las prácticas de **CI/CD** en el flujo de trabajo de desarrollo.

GitHub Actions es una herramienta de **integración continua (CI)** y **entrega continua (CD)** que permite automatizar procesos como:  

- Ejecutar **tests** cada vez que hacemos un commit.  
- Compilar y desplegar una aplicación automáticamente.  
- Generar documentación o informes de calidad de código.  
- Mantener actualizado el repositorio con tareas automáticas.  
- Desplegar aplicaciones en la nube.

Piensa en GitHub Actions como un **robot que trabaja en tu proyecto**: tú defines qué debe hacer, cuándo y cómo, y él se encarga de ejecutarlo. Ese trabajo que se automatiza se llama pipeline o **workflow** en el contexto de GitHub Actions. 


### 1. Concepto clave: Workflow

Un **workflow** es un **flujo de trabajo automatizado** que se define en un fichero `.yml` dentro del directorio `.github/workflows` de tu repositorio.  

Cada workflow responde a **eventos** (ej: un push, un pull request, o una ejecución manual) y se compone de uno o varios **jobs** con **steps** que ejecutan acciones.  

> 📌 Metáfora:  
> - **on:** → cuándo se ejecuta (ej. "cuando alguien toca el timbre").  
> - **jobs:** → qué tareas realizar (ej. "abrir la puerta, dar la bienvenida").  
> - **steps:** → pasos concretos dentro de cada tarea (ej. "caminar hacia la puerta", "abrir", "saludar").  

### 2. Estructura básica de un workflow

En el siguiente ejemplo tenemos un workflow muy simple que se ejecuta en cada push a la rama `main` o cuando se lanza manualmente. Este workflow tiene un solo job que corre en una máquina virtual con Ubuntu y realiza dos pasos: clonar el repositorio y ejecutar un comando que imprime un mensaje.

```yaml
name: CI Demo              # Nombre del workflow (aparece en la pestaña Actions)

on:                        # Eventos que lo activan
  push:                    # Se ejecuta en cada push
    branches:
      - main               # Solo en la rama main
  workflow_dispatch:        # También se puede lanzar manualmente

jobs:                      # Conjunto de trabajos
  build:                   # Nombre del job
    runs-on: ubuntu-latest # Sistema operativo donde corre

    steps:                 # Pasos dentro del job
      - name: Checkout repo
        uses: actions/checkout@v3    # Acción prehecha para clonar el repositorio

      - name: Run a command
        run: echo "Hola, GitHub Actions"   # Comando que se ejecuta en la shell
````

Como ves, un workflow es básicamente un script en YAML que define **qué hacer y cuándo hacerlo**. Vamos a desglosar sus partes.

#### 2.1. Partes explicadas

En un workflow tenemos varias secciones clave:

1. **`name`** → El título del workflow, solo informativo.
2. **`on`** → Qué evento lo dispara: `push`, `pull_request`, `schedule` (cron), `workflow_dispatch` (manual).
3. **`jobs`** → Conjunto de trabajos que se ejecutan, pueden ser en paralelo o en cadena.
4. **`runs-on`** → Sistema operativo del runner (máquina virtual donde se ejecuta el workflow).
5. **`steps`** → Lista de pasos secuenciales dentro del job.
    
    * `uses:` → Usar acciones predefinidas (ej: checkout, configurar Python, Node…).
    * `run:` → Ejecutar comandos en shell.
    * `with:` → Parámetros de configuración de una acción.

Aquí se ha mostrado un pequeño workflow de ejemplo, pero las posibilidades son enormes. Puedes consultar la documentación de [GhitHub Actions](https://docs.github.com/es/actions) para mas posibilidades. Ademas puedes combinar múltiples jobs, usar matrices para probar en varios entornos, y aprovechar miles de acciones disponibles en el [GitHub Marketplace de Actions](https://github.com/marketplace?type=actions)

#### 2.2. Ejemplo con instalación de dependencias
Vamos a ver un ejemplo más práctico. Imagina que tienes un proyecto en Node.js y quieres que cada vez que alguien haga un push o un pull request, se instalen las dependencias y se ejecuten los tests automáticamente.

```yaml
name: CI Pipeline

on: [push, pull_request, workflow_dispatch]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

Este workflow:

* Se ejecuta cuando alguien hace un **push**, un **pull request**, o de forma **manual**.
* Usa una máquina virtual con **Ubuntu**.
* Descarga el repositorio, instala Node.js, instala las dependencias y ejecuta los tests.


#### 2.3. Chuleta visual

Con la intención de que te quede claro, aquí tienes una chuleta visual con la estructura básica de un workflow:

```
# WORKFLOW (.github/workflows/*.yml)
│
├── name: "Nombre del workflow"
│
├── on: (Evento que lo dispara)
│   ├── push, pull_request
│   ├── schedule (cron)
│   └── workflow_dispatch (manual)
│
└── jobs:
    └── <job_id>:
        ├── runs-on: ubuntu-latest
        └── steps:
            ├── uses: acciones prehechas (ej: checkout)
            ├── run: comandos shell
            └── with: parámetros de configuración
```


> **Recuerda:**
> Un workflow no es más que un **script en YAML** que GitHub ejecuta automáticamente en servidores en la nube cuando ocurre un evento que tú defines.


### 3. Marketplace de Actions 

Como comentamos, GitHub Actions permite usar **acciones predefinidas** creadas por la comunidad o por empresas. Estas acciones son bloques de código reutilizables que realizan tareas comunes, como configurar entornos, desplegar aplicaciones, enviar notificaciones, etc. Antes de crear un workflow desde cero, es buena idea revisar si ya existe una acción que haga lo que necesitas. Esto ahorra tiempo y esfuerzo.

GitHub ofrece un **Marketplace de Actions**: [https://github.com/marketplace](https://github.com/marketplace)

Aquí encontrarás **acciones ya preparadas** por la comunidad y empresas, listas para usar en tus workflows.  

Ejemplos muy utilizados:

- **actions/checkout** → Clona el repositorio en el runner (¡casi siempre es el primer paso!).  
- **actions/setup-node** → Configura Node.js en la máquina virtual.  
- **actions/setup-python** → Configura Python.  
- **peaceiris/actions-gh-pages** → Publica contenido en GitHub Pages automáticamente.  
- **stefanzweifel/git-auto-commit-action** → Hace commits automáticos con cambios generados en el workflow.  

> Ventaja: no tienes que reinventar la rueda.  
> Solo declaras `uses:` y aprovechas el trabajo ya hecho.  

#### 3.1. Ejemplo práctico: Actualizar README automáticamente

Con este ejemplo vamos a ver cómo **actualizar el README.md automáticamente** cada vez que se ejecuten tests. Esto es útil para mostrar el estado del proyecto, resultados de tests, cobertura de código, etc.

Supongamos que queremos que, cada vez que ejecutemos tests, el **resultado se escriba en el README.md**.  

Para eso usaremos:
- Un **script en Python** (`update_readme.py`) que modifica el archivo.  
- La acción `git-auto-commit-action` para guardar el cambio en el repo.  

**Workflow (ci.yml):**

```yaml
name: CI con auto-commit

on: [push, workflow_dispatch]

permissions:
  contents: write   # Da permiso al bot para hacer push

jobs:
  test-and-update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - run: pip install pytest

      - name: Ejecutar script de tests y actualizar README
        run: python update_readme.py

      - name: Commit automático del README
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update README con estado de tests"
          file_pattern: README.md
````

Con este workflow, se puede ver **cómo GitHub Actions ejecuta código propio, modifica archivos y guarda cambios automáticamente**.


#### 3.2. Ejemplo práctico: Despliegue automático en GitHub Pages

Teniendo en cuenta el punto visto anteriormente relacionado con la documentación de los proyectos, vamos a ver otro ejemplo práctico muy útil.

Por ejemplo, si tienes documentación en Markdown con **MkDocs** o una presentación en **Reveal.js**, puedes desplegarla con un workflow.

Haremos uso de la acción `peaceiris/actions-gh-pages`, con la que podemos **desplegar una web estática en GitHub Pages automáticamente** cada vez que hagamos un push a la rama `main`.

**Workflow:**

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ "main" ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Instalar dependencias
        run: pip install mkdocs

      - name: Build site
        run: mkdocs build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

Con este ejemplo, cada vez que hagan un `push` a `main`, su web de documentación se actualiza sola. Para ello, los pasos que siguen son:
1. Clonan el repo.
2. Instalan MkDocs.
3. Generan la web estática en la carpeta `site/`.
4. Despliegan el contenido de la carpeta `site/` a GitHub Pages, haciendo push a la rama `gh-pages` usando la acción `peaceiris/actions-gh-pages`.
5. Usan el token secreto que GitHub proporciona automáticamente para autenticar el despliegue.
6. Publican en la rama `gh-pages` (configurada en las opciones del repositorio para GitHub Pages).
7. ¡Listo! La web está actualizada sin tocar nada más.


### 4. GitHub Actions en CI/CD real

En un proyecto real de despliegue de aplicaciones web, Actions se puede usar para:

* **CI (Integración Continua):**
    
    * Lanzar tests automáticamente con cada commit.
    * Analizar calidad de código (linters, seguridad, dependencias).

* **CD (Entrega/Despliegue Continuo):**
    
    * Desplegar la aplicación en un servidor remoto, contenedor Docker o en la nube (AWS, Azure, GCP).
    * Generar y publicar documentación automáticamente.
    * Crear imágenes Docker y subirlas a un registro.


### 5. Actividad didáctica básica

**Objetivo:** Que los alumnos creen su **primer workflow** en GitHub Actions.

**Instrucciones:**

1. Crea un repositorio nuevo en GitHub con un `README.md`.
2. Añade la carpeta `.github/workflows/` y dentro un archivo `hello.yml` con:

```yaml
name: Hola Mundo

on: workflow_dispatch

jobs:
  say-hello:
    runs-on: ubuntu-latest
    steps:
      - name: Saludar
        run: echo "Hola, GitHub Actions!!"
```

3. Ve a la pestaña **Actions** y lanza el workflow manualmente con *Run Workflow*.
4. Observa el log de ejecución.

Entregable: Captura de pantalla mostrando el workflow ejecutado.


## Bibliografía y fuentes
1. [What is CI/CD? A Beginner’s Guide to Continuous Integration and Continuous Delivery](https://www.redhat.com/en/topics/devops/what-is-ci-cd)
2. [GitHub Actions Documentation](https://docs.github.com/en/actions)
3. [GitHub Actions Marketplace](https://github.com/marketplace)
4. [GitHub Actions Cheat Sheet](https://github.github.io/actions-cheat-sheet/actions-cheat-sheet.pdf)

