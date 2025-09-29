# 3. ACTIVIDAD A ENTREGAR: *Mejorando un Workflow con GitHub Actions*
La siguiente actividad está diseñada para que aprendais a usar GitHub Actions de forma práctica, empezando por un workflow básico y luego añadiendo mejoras progresivas, asi como incidir en las herramientas y proceso de documentación La idea es que podais avanzar a vuestro ritmo, alcanzando un nivel mínimo común pero con la posibilidad de explorar funcionalidades más avanzadas si lo desea.

### 🎯 Objetivos de aprendizaje

Al completar esta actividad, los alumnos serán capaces de:
1. Identificar las diferentes herramientas de generación de documentación.
2. Documentar los componentes software utilizando los generadores específicos de las plataformas.
3. Usar diferentes formatos para la documentación.
4. Utilizar herramientas colaborativas para la elaboración y mantenimiento de la documentación.
5. Instalar, configurar y usar un sistema de control de versiones.
6. Garantizar la accesibilidad y seguridad de la documentación almacenada por el sistema de control de versiones.
7. Implementar y utilizar herramientas para la integración continua del código (CI/CD).
---

## 📝 Contexto

Partiendos del **repositorio base** de la actividad de ejemplo, que contiene:

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


## 🔹 Parte 3: Documentación y Preguntas 

* (g) **Actualizar el `README.md`** para que describa:
    
    * (a) Las herramientas usadas para generar la documentación, y los comandos ejecutados para ello. (No olvidad esta documentación y markdown como herramienta de documentación).
    * (b) Ejemplos de código documentado (Enlaces), y de la generación (c) en distintos formatos (al menos uno mas, p.ej. PDF, Markdown).
        
        * La documentación que se va a generar y enlace a esta.
        * Los distintos formatos generados y enlaces a los mismos.
  
    * (g) El repositorio y como usarlo (clonarlo) para generar la documentación, el funcionamiento del workflow (d) Una explicación breve de su funcionamiento para que cualquier persona pueda entenderlo.
    * (e) Los comentarios de los commits en el sistema de control que evidencien la mejora implementada, deben ser claros y descriptivos.
    * (f) Evidenciar de la configuración del acceso al sistema de control de versiones (GitHub) a través de ssh.
---

Responde a las siguientes preguntas:

| CE    | Pregunta de Evaluación Asociada a la Actividad           |
|:------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **a** | **Se han identificado diferentes herramientas de generación de documentación**. ¿Qué herramienta o generador específico (ej., Javadoc, Doxygen) fue utilizado en el *workflow* para procesar el código y generar la documentación en la carpeta `/doc`?                                                                 |
| **b** | **Se han documentado los componentes software utilizando los generadores específicos de las plataformas**. Muestre un fragmento del código fuente y señale los comentarios estructurados (ej. etiquetas `@param` o `@return`) que permitieron a la herramienta generar la documentación.                                |
| **c** | **Se han utilizado diferentes formatos para la documentación**. ¿Qué segundo formato de documentación eligió, además de HTML? Describa la configuración o los comandos que incluyó en su *workflow* de GitHub Actions para producir ese formato adicional.                                                              |
| **d** | **Se han utilizado herramientas colaborativas para la elaboración y mantenimiento de la documentación**. Describa de qué manera el uso de GitHub facilita el mantenimiento de la documentación (específicamente la actualización del `README.md` y de los archivos en `/doc`) cuando colaboran múltiples programadores. |
| **e** | **Se ha instalado, configurado y utilizado un sistema de control de versiones**. Muestre los mensajes de los *commits* que evidencian la implementación del nuevo *workflow*. ¿Fueron estos mensajes claros y descriptivos, como lo requiere el enunciado?                                                              |
| **f** | **Se ha garantizado la accesibilidad y seguridad de la documentación almacenada por el sistema de control de versiones**. ¿Qué medidas implementó o qué configuraciones del repositorio garantizan que solo el personal autorizado pueda acceder al código y la documentación generada?                                 |
| **g** | **Se ha documentado la instalación, configuración y uso del sistema de control de versiones utilizado**. Señale en el `README.md` dónde documentó la explicación breve del funcionamiento del nuevo *workflow* y dónde se describen las herramientas y comandos utilizados para generar la documentación.               |
| **h** | **Se han utilizado herramientas para la integración continua del código**. Explique porqué se clasifica el *workflow* de GitHub Actions utilizado como una herramienta de Integración Continua (CI). ¿Qué evento específico dispara automáticamente la generación y actualización de la documentación?                  |
---

## 🔹 Parte 3: Mejoras opcionales (nivel intermedio)

Los alumnos más avanzados pueden añadir:

* **Página de documentación con MKdocs en GitHub Pages** con `peaceiris/actions-gh-pages`.

Aquí experimentarás con **automatización multiplataforma** y **despliegues automáticos**.

---

## 📑 Entregables

Cada alumno debe entregar:

1. Enlace a su repositorio con el workflow funcionando.
2. La documentación del README.md.
3. Las respuestas a las preguntas.

