# U1.3 - Git y GitHub

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---  

## Índice

---

## 1. Control de Versiones


### 1.1. ¿Qué es el control de versiones?

* Sistema que registra cambios en archivos a lo largo del tiempo.
* Permite recuperar versiones específicas del proyecto.
* Invaluable para rastrear la evolución del software.
* Facilita revertir errores.
* Esencial para coordinar trabajo de múltiples personas.

Note: Sin control de versiones, el desarrollo colaborativo sería caótico y propenso a pérdida de trabajo.


### 1.2. Importancia

* Evita pérdida de trabajo.
* Permite trabajar en paralelo sin conflictos.
* Facilita la experimentación con ramas.
* Proporciona historial completo de cambios.
* Fundamental en desarrollo profesional.

Note: El control de versiones es tan fundamental como saber programar en el desarrollo moderno.

---

## 2. Introducción a Git


### 2.1. ¿Qué es Git?

* Software de control de versiones distribuido.
* Diseñado por Linus Torvalds en 2005.
* Creado para gestionar el desarrollo del núcleo Linux.
* Cada desarrollador tiene copia completa del historial.
* Permite trabajo offline y desconectado.

Note: Git revolucionó el control de versiones al hacerlo distribuido en lugar de centralizado.


### 2.2. Ventajas de Git

* Sistema distribuido: cada clon es un backup completo.
* Muy rápido en operaciones locales.
* Ramificación y fusión eficientes.
* Integridad de datos garantizada (SHA-1).
* Desarrollo no lineal facilitado.

Note: La naturaleza distribuida de Git fomenta el desarrollo paralelo y agiliza la gestión de ramas.

---

## 3. Conceptos clave en Git


### 3.1. Repositorio (Repository)

* Corazón del proyecto.
* Almacena todos los datos y el historial completo.
* Base de datos con todas las versiones.
* Al clonar, obtienes copia de casi todos los datos.
* Puede ser local o remoto.

Note: Un repositorio es como una base de datos que contiene toda la historia del proyecto.


### 3.2. Commit (Confirmación)

* Punto de control en el desarrollo.
* "Instantánea" del proyecto en un momento específico.
* Identificado por hash SHA-1 único de 40 caracteres.
* Incluye metadatos: autor, fecha, mensaje.
* Los mensajes deben ser claros y concisos.

Note: Cada commit es inmutable y representa un estado específico del proyecto.


### 3.3. Rama (Branch)

* Líneas de desarrollo independientes.
* Una de las características más potentes de Git.
* Permite trabajar sin afectar la base de código principal.
* Crear y destruir ramas es rápido y económico.
* Rama principal típicamente llamada `main` o `master`.

Note: Las ramas permiten experimentar, desarrollar nuevas funciones o corregir errores de forma aislada.


### 3.4. Área de Preparación (Staging Area)

* Zona intermedia antes del commit.
* Seleccionas qué cambios incluir en el próximo commit.
* Permite construir la instantánea con precisión.
* También llamada "Index".
* Archivos preparados se consideran "staged".

Note: El staging area permite tener control preciso sobre qué cambios se incluyen en cada commit.


### 3.5. Directorio de Trabajo (Working Directory)

* Copia de los archivos del proyecto en tu máquina.
* Donde realizas las modificaciones directamente.
* Archivos extraídos del repositorio para uso.
* Archivos modificados se consideran "modified".
* Estado antes de preparar cambios.

Note: El directorio de trabajo es tu espacio para hacer cambios antes de confirmarlos.


### 3.6. HEAD

* Puntero a la referencia de rama actual.
* Representa el último commit de la rama activa.
* Será el padre del próximo commit.
* Se mueve automáticamente con cada nuevo commit.
* Puede apuntar a cualquier commit específico.

Note: HEAD marca tu posición actual en el historial del proyecto.

---

## 4. Ciclo de vida de archivos


### 4.1. Flujo de trabajo básico

1. **Modificar archivos** en el directorio de trabajo.
2. **Preparar archivos** añadiéndolos al staging area.
3. **Confirmar cambios** realizando un commit.

Note: Este flujo se repite constantemente durante el desarrollo.


### 4.2. Estados de archivos

* **Confirmado (Committed):** Datos almacenados en el repositorio local.
* **Modificado (Modified):** Archivo modificado pero no preparado.
* **Preparado (Staged):** Archivo marcado para el próximo commit.

Note: Entender estos estados es fundamental para trabajar eficientemente con Git.

---

## 5. Comandos Git esenciales


### 5.1. Configuración inicial

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
git config --global core.editor "code --wait"
git config --global color.ui auto
```

Note: Configura Git con tu identidad antes de empezar. Solo necesitas hacerlo una vez por máquina.


### 5.2. Crear repositorio

```bash
# Inicializar nuevo repositorio
mkdir mi-proyecto
cd mi-proyecto
git init

# O clonar uno existente
git clone https://github.com/usuario/repo.git
```

Note: Git init crea un repositorio vacío, mientras que git clone descarga uno existente.


### 5.3. Verificar estado

```bash
git status
```

* Muestra estado del directorio de trabajo.
* Indica archivos modificados.
* Muestra archivos preparados para commit.
* Lista archivos no rastreados.

Note: git status es uno de los comandos más usados, ejecútalo frecuentemente para saber dónde estás.


### 5.4. Añadir cambios

```bash
# Añadir archivo específico
git add archivo.txt

# Añadir todos los cambios
git add .

# Añadir archivos con patrón
git add *.js
```

Note: git add prepara los cambios para el próximo commit, dándote control sobre qué incluir.


### 5.5. Confirmar cambios

```bash
# Commit con mensaje
git commit -m "Descripción clara del cambio"

# Commit añadiendo todos los modificados
git commit -am "Mensaje"

# Modificar último commit
git commit --amend
```

Note: Los mensajes de commit deben ser descriptivos y comenzar con verbo en imperativo.


### 5.6. Ver diferencias

```bash
# Diferencias no preparadas
git diff

# Diferencias preparadas
git diff --staged

# Diferencias entre commits
git diff commit1 commit2
```

Note: git diff es esencial para revisar cambios antes de confirmarlos.


### 5.7. Historial de commits

```bash
# Ver historial
git log

# Historial compacto
git log --oneline

# Historial con gráfico
git log --graph --oneline --all
```

Note: git log te permite navegar por la historia del proyecto y entender su evolución.

---

## 6. Trabajo con ramas


### 6.1. Gestión de ramas

```bash
# Listar ramas
git branch

# Crear nueva rama
git branch nueva-funcionalidad

# Cambiar a rama
git checkout nueva-funcionalidad

# Crear y cambiar en un comando
git checkout -b nueva-funcionalidad
```

Note: Las ramas permiten desarrollar múltiples funcionalidades en paralelo sin interferencias.


### 6.2. Fusión de ramas

```bash
# Fusionar rama en la actual
git merge nombre-rama

# Fusionar sin fast-forward
git merge --no-ff nombre-rama

# Abortar fusión con conflictos
git merge --abort
```

Note: El merge integra cambios de una rama en otra, a veces requiere resolver conflictos.


### 6.3. Estrategias de ramificación

* **Git Flow:** Ramas main, develop, feature, release, hotfix.
* **GitHub Flow:** Ramas main y feature, deploy continuo.
* **GitLab Flow:** Similar a GitHub Flow con entornos.

Note: Elegir una estrategia de ramificación ayuda a organizar el trabajo en equipo.

---

## 7. Trabajo remoto


### 7.1. Repositorios remotos

```bash
# Ver remotos configurados
git remote -v

# Añadir remoto
git remote add origin https://github.com/usuario/repo.git

# Eliminar remoto
git remote remove origin
```

Note: Los remotos son versiones del proyecto alojadas en servidores como GitHub.


### 7.2. Sincronizar cambios

```bash
# Descargar cambios sin fusionar
git fetch origin

# Descargar y fusionar
git pull origin main

# Subir cambios
git push origin main
```

Note: fetch, pull y push son fundamentales para colaborar con otros desarrolladores.


### 7.3. Buenas prácticas

* Hacer pull antes de push.
* Commits pequeños y frecuentes.
* Mensajes de commit descriptivos.
* No hacer push de código roto.
* Revisar cambios antes de confirmar.

Note: Seguir buenas prácticas evita problemas y facilita la colaboración.

---

## 8. GitHub


### 8.1. ¿Qué es GitHub?

* Plataforma basada en Git.
* Facilita colaboración y gestión de proyectos.
* Alojamiento de repositorios remotos.
* Herramientas de revisión de código.
* Integración con CI/CD.

Note: GitHub es la plataforma más popular para alojar proyectos Git y colaborar.


### 8.2. Funcionalidades principales

* **Pull Requests:** Proponer y revisar cambios.
* **Issues:** Gestionar tareas y bugs.
* **Actions:** Automatización CI/CD.
* **Projects:** Tableros de proyecto.
* **Wiki:** Documentación del proyecto.

Note: GitHub añade funcionalidades de colaboración sobre Git puro.


### 8.3. Pull Requests

* Proponer cambios de una rama a otra.
* Facilita revisión de código.
* Permite discusión sobre cambios.
* Integración con tests automáticos.
* Historial de revisiones.

Note: Los Pull Requests son fundamentales para el trabajo en equipo y revisión de código.


### 8.4. Issues

* Sistema de seguimiento de tareas.
* Reportar y gestionar bugs.
* Discutir nuevas funcionalidades.
* Asignación a miembros del equipo.
* Etiquetas y milestones para organización.

Note: Los Issues ayudan a organizar el trabajo y hacer seguimiento de problemas.

---

## 9. Flujos de trabajo


### 9.1. Git Flow

* Rama `main`: código en producción.
* Rama `develop`: integración de funcionalidades.
* Ramas `feature/*`: nuevas funcionalidades.
* Ramas `release/*`: preparación de releases.
* Ramas `hotfix/*`: correcciones urgentes.

Note: Git Flow es ideal para proyectos con releases programados y múltiples versiones en producción.


### 9.2. GitHub Flow

* Rama `main` siempre desplegable.
* Crear rama para cada funcionalidad.
* Pull Request para revisión.
* Desplegar desde rama de funcionalidad para probar.
* Merge a main tras aprobación.

Note: GitHub Flow es más simple y adecuado para despliegue continuo.


### 9.3. Elegir estrategia

* Depende del equipo y proyecto.
* Proyectos simples: GitHub Flow.
* Proyectos complejos con releases: Git Flow.
* Consistencia en el equipo es clave.

Note: No hay una estrategia única perfecta, depende del contexto del proyecto.

---

## 10. Resolución de conflictos


### 10.1. ¿Qué son los conflictos?

* Ocurren cuando Git no puede fusionar automáticamente.
* Cambios en las mismas líneas de código.
* Requieren intervención manual.
* Git marca las secciones conflictivas.

Note: Los conflictos son normales en el trabajo colaborativo, no son errores.


### 10.2. Resolver conflictos

```bash
# Git marca conflictos así:
<<<<<<< HEAD
código en tu rama
=======
código en la otra rama
>>>>>>> otra-rama

# Editar archivo y elegir qué mantener
# Después marcar como resuelto:
git add archivo-resuelto.txt
git commit
```

Note: Resolver conflictos requiere entender ambos cambios y decidir cómo integrarlos.


### 10.3. Prevenir conflictos

* Commits pequeños y frecuentes.
* Pull regularmente de la rama principal.
* Comunicación en el equipo.
* Dividir trabajo en áreas distintas.
* Fusiones frecuentes.

Note: Prevenir es mejor que curar: buenas prácticas reducen conflictos.

---

## 11. Buenas prácticas


### 11.1. Mensajes de commit

* Usar tiempo presente imperativo.
* Primera línea: resumen (max 50 caracteres).
* Línea en blanco.
* Descripción detallada si es necesario.
* Ejemplo: "Añade validación de formulario de login"

Note: Buenos mensajes de commit facilitan entender la historia del proyecto.


### 11.2. Organización

* .gitignore para archivos que no deben versionarse.
* README.md con información del proyecto.
* Estructura de ramas consistente.
* Tags para marcar versiones.
* Releases documentados.

Note: La organización del repositorio facilita el trabajo en equipo.


### 11.3. Seguridad

* No commitear contraseñas o claves API.
* Usar variables de entorno.
* Revisar cambios antes de push.
* Proteger ramas principales.
* Revisiones de código obligatorias.

Note: La seguridad es fundamental: nunca subas secretos al repositorio.

---

## Resumen

* Git es esencial en desarrollo moderno.
* Control de versiones distribuido potente y flexible.
* GitHub facilita la colaboración.
* Dominar conceptos básicos es fundamental.
* Práctica constante para mejorar.

Note: Git y GitHub son herramientas imprescindibles que todo desarrollador debe dominar.
