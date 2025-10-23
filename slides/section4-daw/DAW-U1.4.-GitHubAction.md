# U1.4 - GitHub Actions

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Introducción a GitHub Actions


### 1.1. ¿Qué es GitHub Actions?

* Plataforma de **automatización** integrada en GitHub.
* Permite **ejecutar tareas** automáticamente en tu repositorio.
* Responde a **eventos** como push, pull request, etc.
* Herramienta clave para implementar **CI/CD**.
* No requiere configuración de servidores externos.

Note: GitHub Actions revoluciona la automatización al estar completamente integrado en la plataforma. Es como tener un robot que trabaja 24/7 en tu proyecto, ejecutando tareas cada vez que ocurre algo en el repositorio.


### 1.2. Ventajas principales

* **Integrado** directamente en GitHub.
* **Automatización** completa del flujo de trabajo.
* **Gratuito** para repositorios públicos.
* **Miles de acciones** reutilizables en Marketplace.
* **Fácil configuración** con archivos YAML.

Note: A diferencia de Jenkins o Travis CI, no necesitas mantener servidores. GitHub se encarga de toda la infraestructura, tú solo defines qué hacer.


### 1.3. ¿Para qué sirve?

* Ejecutar **tests** automáticamente en cada commit.
* Compilar y **desplegar** aplicaciones.
* Generar **documentación** automáticamente.
* Mantener el repositorio con tareas programadas.
* Crear **releases** y publicar paquetes.

Note: Piensa en GitHub Actions como el "mayordomo" de tu repositorio que realiza todas las tareas repetitivas por ti.

---

## 2. Conceptos fundamentales


### 2.1. Los 5 pilares

Los cinco conceptos clave que debes dominar:

1. **Workflow** (Flujo de trabajo)
2. **Event** (Evento disparador)
3. **Job** (Trabajo a realizar)
4. **Step** (Paso individual)
5. **Action** (Acción reutilizable)

Note: Estos cinco conceptos forman la base de GitHub Actions. Entenderlos es como aprender las notas musicales antes de tocar una canción.


### 2.2. Workflow (Flujo de trabajo)

* Proceso automatizado definido en archivo YAML.
* Se guarda en `.github/workflows/` del repositorio.
* Puede contener uno o varios **jobs**.
* Define QUÉ hacer, CUÁNDO y CÓMO.
* Cada repositorio puede tener múltiples workflows.

Note: Un workflow es como una receta de cocina: tiene ingredientes (eventos), instrucciones (steps) y un resultado final.


### 2.3. Event (Evento)

* Actividad que **dispara** la ejecución del workflow.
* Ejemplos: `push`, `pull_request`, `schedule`, `release`.
* Puede activarse manualmente con `workflow_dispatch`.
* Se pueden filtrar por ramas o paths específicos.
* Múltiples eventos pueden activar el mismo workflow.

Note: Los eventos son los "desencadenantes". Es como configurar una alarma: defines cuándo suena y qué ocurre cuando lo hace.


### 2.4. Job (Trabajo)

* Conjunto de **steps** que se ejecutan juntos.
* Corre en una máquina virtual (runner).
* Por defecto, múltiples jobs corren en **paralelo**.
* Usa `needs:` para definir **dependencias** entre jobs.
* Cada job es independiente a menos que lo indiques.

Note: Los jobs son como estaciones de trabajo en una fábrica. Pueden trabajar simultáneamente o esperarse entre sí.


### 2.5. Step (Paso)

* Tarea individual dentro de un job.
* Dos tipos: ejecutar comando (`run`) o usar acción (`uses`).
* Se ejecutan **secuencialmente** en orden.
* Comparten el mismo sistema de archivos.
* Pueden tener nombre descriptivo con `name:`.

Note: Los steps son las instrucciones específicas, como "mezcla ingredientes", "hornea 30 minutos", "deja enfriar".


### 2.6. Action (Acción)

* Bloque de código reutilizable.
* Disponibles en GitHub Marketplace.
* Pueden ser públicas o privadas.
* Ejemplo: `actions/checkout@v3` clona el repo.
* Aceptan parámetros con `with:`.

Note: Las actions son como herramientas prefabricadas. En lugar de reinventar la rueda, usas lo que otros ya crearon y probaron.


### 2.7. Runner (Ejecutor)

* Máquina virtual donde se ejecuta el workflow.
* GitHub proporciona runners con diferentes sistemas operativos.
* Opciones: `ubuntu-latest`, `windows-latest`, `macos-latest`.
* También puedes usar self-hosted runners propios.
* Se especifica con `runs-on:`.

Note: El runner es el "escenario" donde ocurre toda la acción. GitHub te da máquinas gratis, pero debes elegir el sistema operativo adecuado.

---

## 3. Estructura de un Workflow


### 3.1. Anatomía básica

```yaml
name: Mi Workflow

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: echo "Hola GitHub Actions!"
```

Note: Esta es la estructura mínima. Nombre descriptivo, cuándo ejecutarse, qué máquina usar, y qué pasos seguir.


### 3.2. Eventos comunes

```yaml
on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Cada día a las 2 AM
  workflow_dispatch:      # Ejecución manual
```

Note: Puedes combinar múltiples eventos. Los filtros de ramas evitan ejecuciones innecesarias y ahorran minutos de tu cuota.


### 3.3. Variables de entorno

```yaml
env:
  NODE_VERSION: '18'
  APP_NAME: 'mi-aplicacion'

jobs:
  build:
    steps:
      - name: Usar variable
        run: echo "Versión ${{ env.NODE_VERSION }}"
```

Note: Las variables de entorno evitan repetir valores y facilitan el mantenimiento del workflow.


### 3.4. Estructura completa

```yaml
name: CI Pipeline
on: [push, pull_request]
env:
  NODE_VERSION: '18'
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ env.NODE_VERSION }}
      - run: npm ci
      - run: npm test
```

Note: Este ejemplo muestra un pipeline CI real: clona el código, configura Node.js, instala dependencias y ejecuta tests.

---

## 4. Ejemplos prácticos


### 4.1. Tests automáticos

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test
```

Note: Este es el caso de uso más común: ejecutar tests en cada cambio para asegurar que nada se rompió.


### 4.2. Deploy a GitHub Pages

```yaml
name: Deploy Documentación

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: pip install mkdocs
      - run: mkdocs build
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```

Note: Cada vez que hagas push a main, tu documentación se actualiza automáticamente. Perfecto para proyectos con MkDocs.


### 4.3. Jobs con dependencias

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: npm run lint
  
  test:
    needs: lint  # Espera a que 'lint' termine
    runs-on: ubuntu-latest
    steps:
      - run: npm test
  
  deploy:
    needs: [lint, test]  # Espera a ambos
    runs-on: ubuntu-latest
    steps:
      - run: ./deploy.sh
```

Note: Con 'needs' defines el orden de ejecución. Deploy solo ocurre si lint y test pasan exitosamente.

---

## 5. Conceptos avanzados


### 5.1. Secretos

* Valores cifrados configurados en **Settings → Secrets**.
* Se usan para API keys, contraseñas, tokens.
* GitHub los enmascara automáticamente en los logs.
* Se acceden con `${{ secrets.NOMBRE }}`.
* Nunca los incluyas directamente en el código.

Note: Los secretos son fundamentales para seguridad. GitHub los protege y nunca aparecen en texto plano en los logs.


### 5.2. Uso de secretos

```yaml
steps:
  - name: Deploy con credenciales
    run: ./deploy.sh
    env:
      API_KEY: ${{ secrets.API_KEY }}
      DB_PASSWORD: ${{ secrets.DB_PASSWORD }}
```

Note: Así se usan los secretos de forma segura. Nunca hagas commit de credenciales reales en el código.


### 5.3. Artefactos

* Permiten guardar archivos generados durante el workflow.
* Se pueden compartir entre jobs.
* Útil para builds, reportes, logs.
* Retención configurable con `retention-days`.
* Se descargan desde la interfaz de GitHub.

Note: Los artefactos son como un "buzón" donde dejas archivos para usar después o descargar manualmente.


### 5.4. Subir y descargar artefactos

```yaml
# Job 1: Subir
- uses: actions/upload-artifact@v3
  with:
    name: build-output
    path: dist/
    retention-days: 7

# Job 2: Descargar
- uses: actions/download-artifact@v3
  with:
    name: build-output
```

Note: Esto permite que un job compile la aplicación y otro job la despliegue sin recompilar.


### 5.5. Caché

* Acelera workflows reutilizando dependencias.
* Evita descargar node_modules, paquetes, etc.
* Se invalida automáticamente si cambian dependencias.
* Ahorra tiempo y minutos de cuota.
* Especialmente útil para proyectos grandes.

Note: La caché puede reducir el tiempo de ejecución de 5 minutos a 30 segundos en proyectos grandes.


### 5.6. Uso de caché

```yaml
- name: Cache npm dependencies
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-

- run: npm ci
```

Note: La key usa el hash del package-lock.json, así se invalida solo cuando cambian las dependencias.


### 5.7. Matrix Strategy

* Ejecuta el mismo job en múltiples configuraciones.
* Útil para probar en diferentes versiones o sistemas operativos.
* Ahorra código duplicado.
* Corre todas las combinaciones en paralelo.
* Ejemplo: Node 16, 18, 20 en Ubuntu, Windows, macOS.

Note: La matriz es como hacer pruebas cruzadas. GitHub crea automáticamente todas las combinaciones posibles.


### 5.8. Ejemplo de matriz

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node-version: [16, 18, 20]
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm test
```

Note: Esto ejecuta 6 jobs (2 OS × 3 versiones de Node). Perfecto para asegurar compatibilidad multiplataforma.


### 5.9. Condiciones (if)

* Controlan cuándo se ejecuta un step o job.
* Evalúan expresiones booleanas.
* Acceso a contextos como `github`, `env`, `secrets`.
* Funciones especiales: `success()`, `failure()`, `always()`.
* Permiten lógica compleja en workflows.

Note: Las condiciones añaden inteligencia a tus workflows. Puedes ejecutar pasos solo en ciertas circunstancias.


### 5.10. Ejemplos de condiciones

```yaml
steps:
  - name: Solo en main
    if: github.ref == 'refs/heads/main'
    run: echo "Rama principal"
  
  - name: Solo si falló
    if: failure()
    run: echo "Algo salió mal"
  
  - name: Siempre ejecutar
    if: always()
    run: echo "Cleanup"
```

Note: 'always()' es útil para tareas de limpieza que deben ejecutarse incluso si el workflow falla.

---

## 6. Pipeline CI/CD completo


### 6.1. Estructura del pipeline

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run lint
  
  test:
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm test
```

Note: Un pipeline CI/CD real tiene múltiples etapas: lint, test, build, deploy. Cada una depende del éxito de la anterior.


### 6.2. Build y Deploy

```yaml
  build:
    needs: [lint, test]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm run build
      - uses: actions/upload-artifact@v3
        with:
          name: build-files
          path: dist/
  
  deploy:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v3
      - run: ./deploy.sh
```

Note: El deploy solo ocurre en main y después de que todo lo anterior pase. Los artefactos conectan build con deploy.

---

## 7. Limitaciones y costes


### 7.1. Planes de GitHub

| Plan | Minutos/mes | Almacenamiento |
|------|-------------|----------------|
| Free | 2,000 | 500 MB |
| Pro | 3,000 | 1 GB |
| Team | 3,000 | 2 GB |
| Enterprise | 50,000 | 50 GB |

Note: Para repos públicos es ilimitado y gratis. En privados, ten cuidado con el uso de minutos.


### 7.2. Multiplicadores de minutos

* **Linux**: 1x (el más económico)
* **Windows**: 2x (el doble de minutos)
* **macOS**: 10x (¡10 veces más costoso!)

Ejemplo: 10 minutos en macOS = 100 minutos de cuota.

Note: Usa Linux siempre que sea posible. macOS solo cuando realmente necesites probar en ese sistema operativo.

---

## 8. Debugging y buenas prácticas


### 8.1. Depuración

Tres estrategias para depurar workflows:

1. **Revisar logs** detallados en la pestaña Actions.
2. **Añadir pasos de debug** para imprimir información.
3. **Habilitar logging avanzado** con secrets especiales.

Note: Los logs de GitHub Actions son muy completos. Cada step muestra su salida y código de retorno.


### 8.2. Pasos de debug

```yaml
- name: Debug information
  run: |
    echo "Event: ${{ github.event_name }}"
    echo "Ref: ${{ github.ref }}"
    echo "SHA: ${{ github.sha }}"
    echo "Actor: ${{ github.actor }}"
    env  # Muestra todas las variables
```

Note: Estos comandos de debug te ayudan a entender qué está pasando en el workflow.


### 8.3. Debug logging avanzado

Para habilitar logs detallados, crea estos secrets:

* `ACTIONS_STEP_DEBUG` = `true`
* `ACTIONS_RUNNER_DEBUG` = `true`

Esto muestra información mucho más detallada en los logs.

Note: El debug logging es muy verboso. Úsalo solo cuando necesites investigar problemas complejos.


### 8.4. Buenas prácticas (1/2)

1. Usa **versiones específicas** de actions (`@v3`, no `@main`).
2. **Nombra claramente** workflows, jobs y steps.
3. **Limita ejecuciones** con paths y branches.
4. Usa **caché** para acelerar instalaciones.

Note: Las versiones específicas evitan sorpresas cuando una action se actualiza y rompe tu workflow.


### 8.5. Buenas prácticas (2/2)

5. Gestiona **secretos** correctamente, nunca en código.
6. Establece **timeout-minutes** para evitar ejecuciones infinitas.
7. **Documenta** workflows complejos con comentarios.
8. Reutiliza código con **actions personalizadas**.

Note: Un timeout evita que un workflow colgado consuma toda tu cuota de minutos.

---

## 9. Marketplace y recursos


### 9.1. GitHub Marketplace

* Miles de actions predefinidas y listas para usar.
* Filtrar por categorías: CI, CD, Testing, Security.
* Actions verificadas por GitHub con badge azul.
* Puedes crear y publicar tus propias actions.
* Documentación en cada action con ejemplos.

Note: El Marketplace es como una tienda de apps para workflows. Explóralo antes de crear algo desde cero.


### 9.2. Actions populares

* `actions/checkout@v3` - Clona el repositorio.
* `actions/setup-node@v3` - Configura Node.js.
* `actions/setup-python@v4` - Configura Python.
* `actions/cache@v3` - Gestión de caché.
* `docker/build-push-action@v4` - Build/push Docker.
* `peaceiris/actions-gh-pages@v3` - Deploy a GitHub Pages.

Note: Estas 6 actions cubren el 80% de los casos de uso comunes. Memoriza sus nombres.


### 9.3. Recursos de aprendizaje

* [docs.github.com/actions](https://docs.github.com/actions) - Documentación oficial.
* [skills.github.com](https://skills.github.com) - Tutoriales interactivos.
* [github.com/marketplace](https://github.com/marketplace?type=actions) - Marketplace.
* [github.com/actions/starter-workflows](https://github.com/actions/starter-workflows) - Ejemplos.

Note: La documentación oficial es excelente. Los tutorials de GitHub Skills son prácticos e interactivos.

---

## 10. Casos de uso reales


### 10.1. Startup tecnológica

Uso típico en startups:

* Tests automáticos en cada PR.
* Deploy a staging tras merge a develop.
* Deploy a producción tras crear release tag.
* Reportes de seguridad semanales programados.
* Notificaciones en Slack de deployments.

Note: Las startups necesitan velocidad. GitHub Actions les permite desplegar múltiples veces al día de forma segura.


### 10.2. Proyecto open source

Uso en proyectos de código abierto:

* Validar PRs de contribuidores externos.
* Generar y publicar documentación automáticamente.
* Crear releases con changelogs automáticos.
* Análisis de código y cobertura de tests.
* Notificar en Discord/Gitter de nuevos issues.

Note: Los proyectos open source usan Actions para mantener calidad sin intervención manual constante.


### 10.3. Equipo de documentación

Uso para documentación técnica:

* Validar enlaces rotos automáticamente.
* Generar PDFs de la documentación.
* Deploy en múltiples idiomas.
* Actualizar índices de búsqueda.
* Verificar ortografía y gramática.

Note: La documentación puede ser un producto tan importante como el código. Merece su propio pipeline de calidad.

---

## 11. Errores comunes


### 11.1. Tabla de errores

| Error | Causa | Solución |
|-------|-------|----------|
| "Resource not accessible" | Permisos | Configurar `permissions:` |
| "Exit code 1" | Comando falló | Revisar logs |
| "Rate limit exceeded" | Demasiadas requests | Usar caché |
| "Artifact not found" | Expiró o nombre incorrecto | Verificar retention |
| "Invalid YAML" | Sintaxis incorrecta | Validar con linter |

Note: El 90% de los errores se resuelven leyendo los logs con atención. GitHub Actions es muy verboso en sus mensajes.

---

## 12. Conclusión


### 12.1. Resumen de conceptos clave

* **Workflow**: flujo automatizado definido en YAML.
* **Event**: cuándo se ejecuta (push, PR, schedule).
* **Job**: conjunto de steps que corren juntos.
* **Step**: tarea individual (run o uses).
* **Action**: bloque reutilizable del Marketplace.

Note: Estos cinco conceptos son tu vocabulario básico. Domínalos y podrás crear workflows complejos.


### 12.2. ¿Por qué importa para tu carrera?

* Habilidad **muy demandada** en perfiles DevOps.
* **Ahorra tiempo** automatizando tareas repetitivas.
* **Reduce errores** humanos en deployments.
* **Mejora calidad** del código con tests automáticos.
* **Acelera entregas** a producción.

Note: GitHub Actions es una skill que te diferenciará en el mercado laboral. Es estándar en la industria.


### 12.3. Próximos pasos

1. Completar las **actividades propuestas** en el tema.
2. Explorar el **Marketplace** de actions.
3. Crear workflows para **proyectos personales**.
4. Experimentar con **diferentes configuraciones**.
5. Contribuir a **proyectos open source**.

Note: La mejor forma de aprender es experimentando. Crea un repo de prueba y juega con diferentes workflows.


### 12.4. Reflexión final

> "La automatización no es el futuro, es el presente"

GitHub Actions representa el estándar actual de CI/CD:

* **Fácil de aprender**, potente de dominar.
* **Integración perfecta** con GitHub.
* **Gratuito** para uso educativo.
* **Imprescindible** en desarrollo moderno.

Note: Cada minuto que inviertas aprendiendo GitHub Actions te ahorrará horas de trabajo manual en el futuro.

---

## Bibliografía

* [GitHub Actions Documentation](https://docs.github.com/en/actions)
* [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
* [GitHub Skills](https://skills.github.com/)
* [What is CI/CD?](https://www.redhat.com/en/topics/devops/what-is-ci-cd)

Note: Estos son los recursos oficiales más completos y actualizados para aprender GitHub Actions.
