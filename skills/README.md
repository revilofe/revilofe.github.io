# Skills del proyecto

Esta carpeta documenta el mapa de uso de las skills editoriales del proyecto.
Las skills reales están instaladas fuera del repositorio y se exponen aquí a
través de `.codex/skills/`.

## Skills disponibles

- `repo-structure-guide`
  - Decide dónde debe ir cada archivo, asset o recurso.
- `theory-content-writer`
  - Crea o reescribe documentos de teoría.
- `practice-content-writer`
  - Crea prácticas, pasos, ejercicios y soluciones.
- `reveal-slides-creator`
  - Genera presentaciones Reveal.js desde teoría.
- `mermaid-diagram-creator`
  - Genera diagramas Mermaid y UML para teoría, prácticas y slides.
- `slides-linker`
  - Añade enlaces de una presentación en los 4 puntos obligatorios.
- `gift-quiz-generator`
  - Genera bancos de preguntas en formato GIFT.
- `frontmatter-metadata-enforcer`
  - Revisa y corrige metadatos YAML.
- `markdown-style-enforcer`
  - Normaliza estilo Markdown y sintaxis MkDocs.
- `pedagogical-language-checker`
  - Ajusta tono didáctico, claridad e inclusión.
- `naming-conventions-enforcer`
  - Verifica nombres de archivos, carpetas y prefijos.
- `content-workflow-checklist`
  - Hace la revisión final de estructura e integración.

## Flujo recomendado

1. `repo-structure-guide`
2. `naming-conventions-enforcer`
3. `theory-content-writer` o `practice-content-writer`
4. `frontmatter-metadata-enforcer`
5. `markdown-style-enforcer`
6. `pedagogical-language-checker`
7. `mermaid-diagram-creator` si hace falta apoyo visual o UML
8. `reveal-slides-creator` y/o `gift-quiz-generator` si aplica
9. `slides-linker` si hay presentación
10. `content-workflow-checklist`

## Ubicación real de las skills

- Carpeta base: `.codex/skills/`
- Ejemplo:
  - `.codex/skills/reveal-slides-creator/SKILL.md`
  - `.codex/skills/mermaid-diagram-creator/SKILL.md`
  - `.codex/skills/theory-content-writer/SKILL.md`
  - `.codex/skills/gift-quiz-generator/SKILL.md`

## Criterio de uso

- Usar una skill específica cuando la tarea ya encaje claramente en ella.
- Combinar varias skills solo cuando la tarea recorra varias fases del flujo.
- No duplicar reglas en documentos del repo si ya viven en una skill.
