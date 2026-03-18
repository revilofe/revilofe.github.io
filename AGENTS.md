# Guía mínima del repositorio

Este repositorio contiene material educativo para formación profesional en
formato MkDocs Material y Reveal.js. El público objetivo son alumnos y alumnas,
por lo que todo el contenido debe ser didáctico, claro, progresivo y en
español de España.

## Proyecto

- `docs/`: documentación principal del sitio.
- `slides/`: presentaciones Reveal.js asociadas a teoría.
- `includes/`: fragmentos reutilizables.
- `mkdocs.yml`: navegación y configuración del sitio.

## Módulos y prefijos

| Sección    | Módulo                         | Prefijo en `docs/` | Prefijo en `slides/` |
|------------|--------------------------------|--------------------|----------------------|
| `section1` | Programación                   | `PROG-`            | `PR-`                |
| `section2` | Incidentes de seguridad        | `IS-`              | `IS-`                |
| `section3` | Entornos de desarrollo         | `EDES-`            | `ED-`                |
| `section4` | Despliegue de aplicaciones web | `DAW-`             | `DAW-`               |

## Regla operativa principal

Las reglas detalladas del repositorio se han movido a skills especializadas.
Antes de crear o modificar contenido, usar la skill correspondiente a la tarea.
`AGENTS.md` solo mantiene el mapa del proyecto, el flujo de trabajo y las
reglas globales.

## Skills del proyecto

Mapa rápido de uso: `skills/README.md`

- `repo-structure-guide`: ubicar archivos, assets y carpetas.
- `theory-content-writer`: crear o reescribir teoría.
- `practice-content-writer`: crear prácticas y soluciones.
- `mermaid-diagram-creator`: crear diagramas Mermaid y UML didácticos.
- `reveal-slides-creator`: generar slides Reveal.js desde teoría.
- `slides-linker`: enlazar presentaciones en los 4 puntos obligatorios.
- `gift-quiz-generator`: generar cuestionarios GIFT desde teoría.
- `frontmatter-metadata-enforcer`: validar o corregir frontmatter YAML.
- `markdown-style-enforcer`: aplicar estilo Markdown y MkDocs.
- `pedagogical-language-checker`: asegurar tono didáctico e inclusivo.
- `naming-conventions-enforcer`: validar nombres de archivos y carpetas.
- `content-workflow-checklist`: revisar flujo, integración y validación final.

## Workflow recomendado

1. Localizar destino con `repo-structure-guide`.
2. Validar nombres con `naming-conventions-enforcer`.
3. Crear contenido con `theory-content-writer` o
   `practice-content-writer`.
4. Revisar metadatos con `frontmatter-metadata-enforcer`.
5. Revisar formato con `markdown-style-enforcer`.
6. Ajustar tono con `pedagogical-language-checker`.
7. Si hace falta apoyo visual o UML, usar `mermaid-diagram-creator`.
8. Si hay teoría, valorar `reveal-slides-creator` y
   `gift-quiz-generator`.
9. Si hay slides, ejecutar `slides-linker`.
10. Cerrar con `content-workflow-checklist`.

## Reglas globales

- Intentan asociar los temas a un RAZ, y sus criterios de evaluación (a,b,c,..), según normativa que puedes encontrar en la carpeta `docs/sectionX/recursos/YYY Normativa.txt` haciendo referencia al RA y a los identificadores y descriptores de los CE.
- Mantener la estructura ya existente del repositorio.
- Si hay una inconsistencia histórica entre carpetas o prefijos, seguir la
  convención que ya use la carpeta afectada y no forzar migraciones implícitas.
- Usar español de España y lenguaje inclusivo.
- No crear teoría, práctica, slides o cuestionarios sin validar nomenclatura,
  metadatos y estilo.
- Las slides deben existir siempre como pareja `.md` y `.html`.
- Los enlaces a slides desde `docs/` usan URLs absolutas.
- Si se crea una presentación, debe enlazarse en los 4 puntos obligatorios.
- Si se crea teoría nueva, comprobar si requiere también slides, GIFT y entrada
  en `mkdocs.yml`.

## Plantillas útiles del repositorio

- Teoría: `docs/section2/u03/teoria/IS-U3.5.1.-Contencion.md`
- Práctica: `docs/section2/u02/practica/IS-U2.-Practica001.md`
- Slides: `slides/section2-is/IS-U2.2.1.-SOC-ServiciosYHerramientas.md`
- GIFT: `docs/section2/u02/gift/IS-U2.4.2.-ComoEscribirInformesTecnicos.gift`

## Criterio de cierre

Antes de terminar cualquier tarea editorial:

- revisar estructura y nombres,
- revisar metadatos y estilo,
- revisar enlaces y rutas a assets,
- actualizar navegación si aplica,
- validar que el contenido resultante sea didáctico y usable.
