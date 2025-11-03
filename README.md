# revilofe.github.io

Repositorio de material educativo para formación profesional en desarrollo de aplicaciones web y ciberseguridad.

Este repositorio contiene documentación, prácticas, presentaciones y recursos educativos organizados por módulos temáticos para estudiantes de ciclos formativos de desarrollo de aplicaciones web.

## 📚 Módulos Disponibles

### 🎯 Programación (section1)
Contenido básico de programación con Python, Kotlin y otros lenguajes.
- **U1**: Primer programa en Python
- **U2**: Estructuras de control
- **U3**: Estructuras de datos
- **U4**: Kotlin: POO y estructuras de datos
- **U5**: Kotlin: PPO y creación de e.d.
- **U6**: Kotlin: Creación de programas con POO
- **U7**: Kotlin: Entrada/Salida y GUI
- **U9**: Acceso a base de datos relacionales

### 🔒 Incidentes de Seguridad (section2)
Contenido sobre gestión de incidentes de ciberseguridad.
- **U0**: Nos conocemos
- **U1**: Principios generales y planes de seguridad
- **U2**: Detección y análisis de incidentes
- **U3**: Investigación de incidentes

### 🛠️ Entornos de Desarrollo (section3)
Herramientas y metodologías para desarrollo de software.
- **U1**: Introducción al desarrollo de software
- **U2**: Entornos de desarrollo integrado
- **U3**: Pruebas y Depuración
- **U4**: SCV, refactorización y documentación
- **U5**: Pruebas y Depuración (actualizado)

### 🚀 Despliegue de Aplicaciones Web (section4)
Tecnologías para despliegue y DevOps.
- **U1**: Documentación y Control de versiones
- **U2**: Contenedores Docker

## 📁 Estructura del Repositorio

```
├── docs/                          # Documentación principal (MkDocs)
│   ├── section1/                  # Programación
│   │   ├── u01/                   # Unidades didácticas
│   │   │   ├── index.md           # Descripción de la unidad
│   │   │   ├── teoria/            # Contenidos teóricos
│   │   │   ├── practica/          # Prácticas y ejercicios
│   │   │   └── gift/              # Preguntas para cuestionarios
│   │   └── ...
│   ├── section2/                  # Incidentes de seguridad
│   ├── section3/                  # Entornos de desarrollo
│   └── section4/                  # Despliegue web
├── slides/                        # Presentaciones (Reveal.js)
│   ├── section1-pr/               # Slides de programación
│   ├── section2-is/               # Slides de seguridad
│   ├── section3-ed/               # Slides de entornos desarrollo
│   └── section4-daw/              # Slides de despliegue
├── mkdocs.yml                     # Configuración de MkDocs
├── AGENTS.md                      # Guía para agentes/contribuidores
└── README.md                      # Este archivo
```

## 🎯 Cómo Usar el Contenido

### Documentación
1. La documentación principal está en `/docs/`
2. Se genera automáticamente con MkDocs
3. Cada módulo tiene unidades didácticas con teoría y práctica

### Presentaciones
1. Las slides están en `/slides/`
2. Formato Reveal.js (HTML + Markdown)
3. Abrir los archivos `.html` en un navegador

### Contenido por Módulo
- **Teoría**: Contenidos conceptuales y explicaciones
- **Práctica**: Ejercicios y actividades evaluables
- **Slides**: Presentaciones complementarias

## 🤝 Cómo Contribuir

### Requisitos Previos
- Conocimientos básicos de Git y GitHub
- Familiaridad con Markdown
- Experiencia en desarrollo web (opcional)

### Proceso de Contribución

1. **Fork del repositorio**
   ```bash
   # Haz fork en GitHub y clona tu fork
   git clone https://github.com/TU_USUARIO/revilofe.github.io.git
   cd revilofe.github.io
   ```

2. **Crear una rama para tus cambios**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # o
   git checkout -b fix/correccion-error
   ```

3. **Realizar cambios siguiendo la estructura**
   - Documentación: `/docs/sectionX/uXX/teoria/` o `/practica/`
   - Slides: `/slides/sectionX-XX/`
   - Mantener consistencia en nomenclatura

4. **Convenciones de nomenclatura**
   - **Documentos**: `MODULO-UX.Y.-Tema.md`
   - **Slides**: `MODULO-UX.Y.-Tema.html/.md`
   - **Prácticas**: `MODULO-UX.-PracticaYYY.md`

5. **Validar cambios**
   ```bash
   # Verificar que MkDocs funciona
   mkdocs serve
   
   # Verificar slides abriendo archivos .html
   ```

6. **Commit y push**
   ```bash
   git add .
   git commit -m "Descripción clara de los cambios"
   git push origin feature/nueva-funcionalidad
   ```

7. **Crear Pull Request**
   - Ve a GitHub y crea un PR desde tu rama
   - Describe claramente qué cambios introduces
   - Espera revisión y feedback

### Tipos de Contribuciones

- ✅ **Correcciones**: Errores tipográficos, enlaces rotos
- ✅ **Mejoras**: Claridad, ejemplos adicionales
- ✅ **Nuevo contenido**: Teoría, prácticas, slides
- ✅ **Actualizaciones**: Tecnologías, mejores prácticas
- ✅ **Traducción**: Si aplica

### Guías de Estilo

- **Markdown**: Usar sintaxis clara y consistente
- **Código**: Incluir ejemplos funcionales
- **Enlaces**: Verificar que funcionen
- **Imágenes**: Optimizar tamaño y formato

### Contacto

Para preguntas o sugerencias:
- Crear un Issue en GitHub
- Revisar AGENTS.md para guías detalladas

---

**Nota**: El seguimiento de cambios locales en `workspace.xml` se puede prevenir con:
```bash
git update-index --assume-unchanged .idea/workspace.xml
# Para revertir: git update-index --no-assume-unchanged .idea/workspace.xml
```
