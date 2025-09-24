# 1. ACTIVIDAD BASE: "GitHub Actions + Python Script + Auto Commit"

## 📝 Preparación del repositorio base

Estructura:

```
mi-proyecto-actions/
 ├── main.py
 ├── test_main.py
 ├── update_readme.py   👈 nuevo script
 └── README.md
```

### README.md inicial

```markdown
# Mi Proyecto con GitHub Actions

Este proyecto sirve para aprender a usar GitHub Actions 🚀

## Estado de los tests
*Aún no ejecutados...*
```

### main.py

```python
def saludo(nombre: str) -> str:
    return f"Hola, {nombre}!"
```

### test\_main.py

```python
from main import saludo

def test_saludo():
    assert saludo("Mundo") == "Hola, Mundo!"
```

---

## 🐍 Script en Python (`update_readme.py`)

Este script ejecuta los tests y actualiza el README:

```python
import subprocess

def run_tests():
    try:
        subprocess.check_call(["pytest", "-q"])
        return "✅ Tests correctos"
    except subprocess.CalledProcessError:
        return "❌ Tests fallidos"

def update_readme(status: str):
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_lines.append(line)
        if line.strip() == "## Estado de los tests":
            new_lines.append(status + "\n")
            break

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

if __name__ == "__main__":
    status = run_tests()
    update_readme(status)
```

👉 Lo que hace:

1. Ejecuta los tests con `pytest`.
2. Según el resultado, genera un estado ✅ o ❌.
3. Modifica el `README.md` justo debajo de la sección `## Estado de los tests`.

---

## ⚙️ Workflow (`.github/workflows/ci.yml`)

```yaml
name: CI con AutoCommit

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  test-and-update:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repo
        uses: actions/checkout@v3

      - name: Configurar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar dependencias
        run: pip install pytest

      - name: Ejecutar script de tests y actualizar README
        run: python update_readme.py

      - name: Commit automático del README
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Update README con estado de tests"
          file_pattern: README.md
```

---

## 🚦 Flujo de la actividad

1. Alumno hace un **push** en `main`.
2. El workflow ejecuta el script en Python.
3. El script corre los tests y modifica el `README.md`.
4. La acción `git-auto-commit-action` hace commit automático con los cambios.
5. El alumno ve en el repo cómo el `README.md` se actualiza con:
    
    * ✅ Tests correctos
    * ❌ Tests fallidos

---

## 📑 Entregable del alumno

* Enlace a su repositorio con el `README.md` actualizado automáticamente.
* Evidencia de haber provocado un test fallido y un test correcto.
* Explicación breve de:
    
    * Qué hace el script.
    * Qué hace el workflow.
    * Qué aporta GitHub Actions a un proyecto real.

---

👉 Con esta versión los alumnos **programan un pequeño script** y ven cómo GitHub Actions:

* Ejecuta código propio.
* Modifica el repositorio automáticamente.
* Se integra con acciones externas (auto-commit).


---

# 3. MEJORAS

La idea es que no solo no repitais el ejemplo, sino que **investigueis, mejoreis y veais el potencial real de GitHub Actions**. Para ello se piden funcionalidades **extra e imaginativas**. Aqui teneis varias propuestas, de más sencillas a más potentes, todas pensadas para que veais ventajas prácticas:

---

## 💡 Mejoras propuestas para el Action

### 1. **Historial en el README**

* Que en lugar de sobrescribir el estado, **guarden un histórico** en el README:
  
  ```markdown
  ## Estado de los tests
  - ✅ 2025-09-22 18:00 - Tests correctos
  - ❌ 2025-09-22 17:45 - Tests fallidos
  ```
* 👉 Les enseña a **manejar fechas** y a **modificar archivos de forma acumulativa**.

---

### 2. **Generar un `report.md` con detalles**

* Crear un archivo `test-report.md` con:
    
    * Número total de tests.
    * Tests pasados y fallidos.
    * Tiempo de ejecución.
* 👉 Les muestra cómo **exportar resultados de procesos** y tener **documentación viva** del proyecto.

---

### 3. **Badges automáticos en README**

* Añadir un **badge** dinámico al README con el estado:
    
    * Verde = Tests correctos
    * Rojo = Tests fallidos
* Usando [shields.io](https://shields.io/) o generando un badge local en SVG.
* 👉 Entienden cómo **mejorar la comunicación del estado** de un proyecto.

---

### 4. **Notificaciones externas**

* Enviar el resultado a:
    
    * **Slack/Discord** (webhook sencillo).
    * **Email** (con una acción de envío).
* 👉 Descubren que Actions también sirve para **integrar con herramientas externas**.

---

### 5. **Ejecutar en múltiples entornos (matrix)**

* Hacer que los tests se ejecuten en:
    
    * Varias versiones de Python (`3.8`, `3.9`, `3.10`).
    * O en Linux y Windows.
* 👉 Ven la potencia del `strategy.matrix` y comprueban compatibilidad multiplataforma.

---

### 6. **Programar ejecución automática**

* Añadir `schedule` para que se ejecute cada día a medianoche.
* El README mostraría:
  
  ```
  ✅ Última comprobación automática: 2025-09-22 00:00
  ```
* 👉 Aprenden a **programar tareas recurrentes**.

---

### 7. **Generar una página web de resultados**

* Publicar los resultados en GitHub Pages (`gh-pages`) usando `peaceiris/actions-gh-pages`.
* 👉 Visualizan cómo GitHub Actions puede hacer **CI/CD real** (tests + despliegue).

---

### 8. **Crear Issues automáticos si fallan los tests**

* Si un test falla → abrir un **issue automático** en el repositorio:
  
  ```yaml
  - uses: actions/github-script@v7
    with:
      script: |
        github.issues.create({
          owner: context.repo.owner,
          repo: context.repo.repo,
          title: "❌ Tests fallidos",
          body: "Se han detectado errores en los tests. Revisa el último commit."
        })
  ```
* 👉 Aprenden a **automatizar la gestión de incidencias**.

---

## 🎯 Aprendizaje con estas mejoras

Con estas extensiones conseguireis:

* Experimentar **cómo GitHub Actions conecta piezas del desarrollo real** (tests, docs, issues, notificaciones, despliegues).
* Entender la **ventaja competitiva** de CI/CD: feedback inmediato, documentación viva y automatización.
* Pasar de un ejemplo didáctico a un flujo de trabajo que se parece mucho al que usan empresas reales.

---

# 3 ACTIVIDAD A ENTREGAR: *Mejorando un Workflow con GitHub Actions*
La siguiente actividad está diseñada para que aprendais a usar GitHub Actions de forma práctica, empezando por un workflow básico y luego añadiendo mejoras progresivas. La idea es que podais avanzar a vuestro ritmo, alcanzando un nivel mínimo común pero con la posibilidad de explorar funcionalidades más avanzadas si lo desea.

### 🎯 Objetivos de aprendizaje

* Comprender la estructura de un workflow (`on`, `jobs`, `steps`).
* Ejecutar tests automáticamente en GitHub.
* Automatizar la actualización del `README.md` con el resultado.
* Explorar mejoras progresivas para descubrir el potencial de GitHub Actions.

---

## 📝 Contexto

Partimos de un **repositorio base** que contiene:

* Un programa sencillo (`main.py`).
* Un test unitario (`test_main.py`).
* Un script (`update_readme.py`) que ejecuta los tests y modifica el `README.md`.
* Un workflow básico (`ci.yml`) que ejecuta el script y hace commit automático con `git-auto-commit-action`.

---

## 🔹 Parte 1: Workflow básico

1. El alumno clona el repositorio base.
2. Comprende el contenido del script y del workflow.
3. Ejecuta el workflow manualmente y comprueba que el `README.md` se actualiza con:
    
    * ✅ *Tests correctos*
    * ❌ *Tests fallidos*

Con esto aprenden el ciclo **evento → ejecución → modificación → commit automático**.

---

## 🔹 Parte 2: Mejoras obligatorias (nivel básico)

Cada alumno debe implementar esta mejora:

* **Generar la documentación en HTML y otro fomato adicional:** volcandola posteriormente en un archivo `docs/report.html` o similar.

Aquí refuerzan el aprendizaje sobre **edición de archivos** y **automatización de documentación**.

---

## 🔹 Parte 3: Mejoras opcionales (nivel intermedio)

Los alumnos más avanzados pueden añadir:

* **Página de documentación con MKdocs en GitHub Pages** con `peaceiris/actions-gh-pages`.

Aquí experimentan con **automatización multiplataforma** y **despliegues automáticos**.

---


## 📑 Entregables

Cada alumno debe entregar:

1. Enlace a su repositorio con el workflow funcionando.
2. Evidencia en el historial de commits de:
    
    * La mejora relacionada con la documentación, implementada.
    * Al menos una ejecución del workflow básico funcionando.

3. Documentación em README.md explicando:
    
    * Qué hace su workflow.
    * Qué mejoras ha implementado.
    * Qué ventajas aporta GitHub Actions al trabajo en equipo.

---

## 📌 Evaluación (rúbrica simplificada)

* ✅ Repositorio creado correctamente.
* ✅ Buen uso git: Ramas, Merges, Commits + comentarios.
* ✅ Workflow básico funciona y genera documentación.
* ✅ Mejora implementada.
* ✅ Usa más de una herramienta para generar documentación.
* ✅ Genera documentación en varios formatos.
* ✅ Explicación clara del funcionamiento y ventajas. README.md.
* 🔝 Extra: despliegue en GitHub Pages.

