# U1.2 - Documentación

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---  

## Índice

---

## 1. ¿Qué es la documentación de software?


### 1.1. Definición

* Todo aquello que explica y acompaña a un programa.
* Permite que otras personas entiendan el código.
* Permite que tú mismo entiendas tu código en el futuro.
* Facilita el uso y mantenimiento del software.
* Es tan importante como el código mismo.

Note: Un buen programa sin documentación es como un coche sin manual: funciona pero nadie sabrá cómo aprovecharlo al máximo.


### 1.2. Tres preguntas clave

* **¿Qué hace el programa?** Funcionalidad, requisitos y propósito.
* **¿Cómo está hecho y por qué?** Arquitectura, diseño y tecnologías.
* **¿Cómo se usa o mantiene?** Instrucciones para usuarios y desarrolladores.

Note: La documentación debe responder estas tres preguntas fundamentales para ser completa y útil.

---

## 2. Tipos de documentación


### 2.1. Documentación interna

* Comentarios especiales dentro del código fuente.
* Se escriben con sintaxis específica (ej: `/** ... */`).
* Se transforman en manuales automáticamente con herramientas.
* Explican cómo funciona el código.
* Dirigida a programadores y desarrolladores.

Note: La documentación interna ayuda a otros desarrolladores (o a ti mismo en el futuro) a entender el código.


### 2.2. Documentación externa

* Manuales de usuario, guías de instalación.
* Páginas web, wikis de proyecto.
* Documentación de API.
* Tutoriales y ejemplos de uso.
* Dirigida a usuarios finales y administradores.

Note: La documentación externa explica cómo usar la aplicación, no cómo está hecha internamente.


### 2.3. Ambas son necesarias

* Una ayuda al programador.
* La otra ayuda al usuario final.
* También beneficia al equipo de desarrollo y mantenimiento.
* Se complementan mutuamente.
* Ninguna puede sustituir a la otra.

Note: Un proyecto completo necesita tanto documentación interna como externa.

---

## 3. Herramientas de documentación


### 3.1. KDoc (Kotlin)

* Forma oficial de documentar en Kotlin.
* Usa comentarios `/** ... */`.
* Permite etiquetas: `@param`, `@return`, etc.
* Se combina con **Dokka** para generar HTML.
* Estándar en proyectos Kotlin.

Note: KDoc es la herramienta nativa para documentación interna en Kotlin.


### 3.2. Javadoc (Java)

* Estándar en Java desde hace décadas.
* Mismo formato que KDoc.
* Etiquetas: `@param`, `@throws`, `@return`.
* Genera páginas HTML navegables.
* Muy usado en bibliotecas y frameworks.

Note: Javadoc es el referente de documentación en el ecosistema Java.


### 3.3. Dokka (Kotlin y JVM)

* Herramienta moderna para Kotlin y lenguajes JVM.
* Convierte comentarios KDoc en web de documentación.
* Admite salida en HTML, Markdown, Jekyll.
* Se integra fácilmente con Gradle.
* Soporte para múltiples módulos.

Note: Dokka es más versátil que Javadoc y soporta mejor los proyectos multi-módulo.


### 3.4. Doxygen (multilenguaje)

* Compatible con C, C++, Java, Python, PHP.
* Muy flexible y potente.
* Genera documentación en HTML, PDF, LaTeX.
* Ideal para proyectos grandes.
* Perfecto cuando se mezclan varios lenguajes.

Note: Doxygen es la opción más versátil cuando trabajas con múltiples lenguajes de programación.


### 3.5. MkDocs (documentación externa)

* Convierte archivos Markdown en web profesional.
* No documenta código, sino manuales y guías.
* Muy usado para documentación de usuario.
* Fácil despliegue en GitHub Pages.
* Temas personalizables y extensible.

Note: MkDocs es ideal para crear sitios web de documentación externa de aspecto profesional.


### 3.6. Markdown

* Formato de texto ligero y fácil de aprender.
* Compatible con muchas plataformas (GitHub, GitLab).
* Se usa en README.md, wikis y blogs.
* Convertible a HTML, PDF con herramientas como Pandoc.
* No es específico de ningún lenguaje.

Note: Markdown se ha convertido en el estándar de facto para documentación externa simple.


### 3.7. Otras herramientas

* **JSDoc:** Específica para JavaScript.
* **Docusaurus:** Sitios web de documentación modernos (Facebook).
* **Wiki GitHub:** Funcionalidad integrada en repositorios.
* **PyDoc:** Documentación para Python desde docstrings.

Note: Existen muchas herramientas especializadas según el lenguaje y necesidades del proyecto.

---

## 4. Diferencias clave


### 4.1. Documentación de código vs. externa

* **KDoc + Dokka / Javadoc:** Documentan el código fuente.
* **Doxygen:** Vale para muchos lenguajes y proyectos grandes.
* **MkDocs:** Hace manuales externos y sitios web.
* **Markdown:** Formato ligero para documentación rápida.

Note: Cada herramienta tiene su propósito específico y se debe elegir según la necesidad.


### 4.2. Cuándo usar cada una

* **Explicar cómo funciona una función:** KDoc + Dokka/Javadoc.
* **Explicar cómo instalar o usar tu aplicación:** MkDocs + Markdown.
* **Proyecto multilenguaje:** Doxygen.
* **Documentación rápida:** Markdown en README.md.

Note: Elige la herramienta adecuada según el tipo de documentación que necesites.

---

## 5. Ejemplo práctico


### 5.1. Ejemplo en Kotlin con KDoc

```kotlin
/**
 * Calcula el área de un círculo.
 *
 * @param radio Radio del círculo en cm.
 * @return Área del círculo en cm².
 */
fun areaCirculo(radio: Double): Double {
    return Math.PI * radio * radio
}
```

Note: Este ejemplo muestra la sintaxis básica de KDoc con descripción, parámetros y valor de retorno.


### 5.2. Resultado con Dokka

Al ejecutar Dokka, obtendremos una página HTML que explica:

* Qué hace la función.
* Qué parámetros recibe y su significado.
* Qué devuelve y en qué unidades.
* Navegación fácil entre funciones relacionadas.
* Búsqueda integrada.

Note: Dokka genera documentación profesional y navegable automáticamente desde los comentarios KDoc.

---

## 6. Buenas prácticas


### 6.1. Documentación interna

* Documenta funciones públicas y clases principales.
* Sé claro y conciso en las descripciones.
* Explica el "por qué", no solo el "qué".
* Usa etiquetas estándar (@param, @return, @throws).
* Mantén la documentación actualizada con el código.

Note: La documentación interna debe enfocarse en ayudar a otros desarrolladores a usar tu código correctamente.


### 6.2. Documentación externa

* Incluye guía de instalación paso a paso.
* Proporciona ejemplos de uso comunes.
* Explica la arquitectura general del sistema.
* Incluye FAQ con problemas comunes.
* Mantén un changelog con los cambios de versión.

Note: La documentación externa debe permitir a un usuario nuevo entender y usar tu aplicación sin ayuda adicional.


### 6.3. README.md

* Primera impresión de tu proyecto.
* Debe incluir: descripción, instalación, uso básico.
* Enlaces a documentación más detallada.
* Información de licencia y contribución.
* Badges de estado (build, tests, cobertura).

Note: Un buen README es fundamental para que otros desarrolladores se interesen en tu proyecto.

---

## 7. Conexión con DevOps


### 7.1. Documentación en el ciclo DevOps

* Parte fundamental del proceso de desarrollo.
* Facilita el onboarding de nuevos miembros.
* Reduce dependencia de personas específicas.
* Mejora la mantenibilidad del código.
* Permite auditorías y revisiones efectivas.

Note: En DevOps, la documentación es tan importante como la automatización y las pruebas.


### 7.2. Automatización de documentación

* Generar documentación en el pipeline CI/CD.
* Desplegar automáticamente en GitHub Pages.
* Validar que el código esté documentado.
* Generar changelog automáticamente.
* Mantener la documentación siempre actualizada.

Note: La generación automática de documentación asegura que siempre esté sincronizada con el código.

---

## Resumen

* La documentación es esencial para cualquier proyecto de software.
* Existen herramientas específicas para cada lenguaje y propósito.
* Documentación interna y externa se complementan.
* Elegir la herramienta adecuada según las necesidades.
* Mantener la documentación actualizada es clave.

Note: Una buena documentación es signo de un proyecto profesional y mantenible a largo plazo.
