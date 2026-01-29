# U1.4.1 - Docker en GitHub Actions

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## 1. Flujo básico Docker + GitHub Actions

Note: En esta sección aprenderemos cómo integrar Docker en nuestros workflows de GitHub Actions. Veremos el flujo mínimo necesario para construir y subir imágenes Docker desde nuestros repositorios, entendiendo cada uno de los pasos necesarios y cómo se ejecutan dentro del runner de GitHub Actions.


### 1.1. Objetivo del workflow

* **Construir** una imagen Docker desde el repositorio.
* **Subirla** a un registry (Docker Hub).
* Automatizar el proceso en cada cambio del código.
* Integrar Docker en el pipeline de CI/CD.

Note: El objetivo fundamental es **automatizar el proceso de construcción y publicación de imágenes Docker**. Esto significa que cada vez que hacemos cambios en nuestro código, GitHub Actions se encargará automáticamente de construir una nueva versión de la imagen y subirla al registry, sin intervención manual. Es la base de un pipeline moderno de CI/CD.


### 1.2. Pasos típicos del workflow

Los cuatro pasos esenciales:

1. **`actions/checkout`**: Descargar el código del repositorio.
2. **`docker login`**: Autenticarse en Docker Hub.
3. **`docker build`**: Construir la imagen desde el Dockerfile.
4. **`docker push`**: Subir la imagen al registry.

Note: Estos cuatro pasos representan el **flujo mínimo razonable** para trabajar con Docker en GitHub Actions. El primero obtiene el código fuente, el segundo nos autentica en el registry donde queremos publicar, el tercero construye la imagen Docker usando nuestro Dockerfile, y el cuarto la publica para que esté disponible públicamente o en nuestro equipo.


### 1.3. Ejemplo de workflow básico I

```yaml
runs-on: ubuntu-latest
steps:
  - uses: actions/checkout@v4

  - name: Login Docker Hub
    uses: docker/login-action@v3
    with:
      username: ${{ secrets.DOCKERHUB_USERNAME }}
      password: ${{ secrets.DOCKERHUB_PASSWORD }}
```

Note: En este primer fragmento vemos dos pasos fundamentales. **`actions/checkout@v4`** clona nuestro repositorio en el runner para tener acceso al código fuente y al Dockerfile. **`docker/login-action@v3`** utiliza credenciales almacenadas de forma segura en los secretos del repositorio para autenticarnos en Docker Hub. Nunca deberíamos poner las credenciales directamente en el código del workflow por seguridad.


### 1.3. Ejemplo de workflow básico II

```yaml
  - name: Build
    run: docker build . -t usuario/imagen:tag

  - name: Push
    run: docker push usuario/imagen:tag
```

Note: Aquí completamos el workflow con los dos pasos finales. **`docker build`** construye la imagen usando el Dockerfile del directorio actual (`.`) y le asigna un tag que incluye nuestro usuario y el nombre de la imagen. **`docker push`** sube esa imagen al registry. El tag que usamos debe coincidir exactamente entre el build y el push para que funcione correctamente.


### 1.4. Flujo completo

```yaml
name: Docker Build & Push

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_PASSWORD }}
      - run: docker build . -t usuario/imagen:tag
      - run: docker push usuario/imagen:tag
```

Note: Este es el **workflow completo y funcional** que integra todos los pasos anteriores. Se ejecutará automáticamente en cada push al repositorio, construirá la imagen y la publicará en Docker Hub. Es un ejemplo perfecto para que el alumnado vea cómo todas las piezas encajan y le ponga cara a qué hace cada paso dentro del runner de GitHub Actions.

---

## 2. Docker en ubuntu-latest

Note: En este punto... 


### 2.1. ¿Hace falta instalar Docker?

* En **ubuntu-latest**: Docker ya viene instalado.
* Los comandos `docker` funcionan directamente.
* **No necesitas**: `apt install docker` ni configuración.
* El daemon de Docker ya está activo y listo.

Note: Esta es una pregunta muy común del alumnado. En los **runners hospedados por GitHub** con `ubuntu-latest`, Docker ya viene preinstalado y configurado. Por eso en los workflows no aparece ningún paso de instalación o arranque del daemon. Esto simplifica enormemente nuestros workflows y nos permite centrarnos en el proceso de build y push.


### 2.2. Único caso especial

* **Runners self-hosted**: Máquinas propias del centro.
    
    * Sí necesitan instalación de Docker.
    * Configuración manual del daemon.
    * Gestión de permisos y usuarios.

Note: El **único caso donde sí habría que instalar Docker** es si usáramos un runner self-hosted, es decir, una máquina propia del centro o de la empresa en lugar de las máquinas virtuales que proporciona GitHub. En ese caso, tendríamos que encargarnos nosotros mismos de instalar Docker, arrancar el daemon y configurar los permisos necesarios.


### 2.3. Verificación en el runner

```yaml
- name: Verificar Docker
  run: |
    docker --version
    docker info
```

Note: Si queremos verificar que Docker está disponible y funcionando correctamente en el runner, podemos añadir un step que ejecute estos comandos. **`docker --version`** nos mostrará la versión instalada y **`docker info`** nos dará información detallada del daemon. Esto puede ser útil para debugging o para documentar qué versión estamos usando.

---

## 3. Versionado de acciones

Note: Seguinos por.... 


### 3.1. ¿Qué son los hashes largos?

Ejemplos reales de referencias:

```yaml
uses: docker/login-action@f4ef78c080cd8ba55a85445d5b36e214a81df20a
uses: docker/build-push-action@3b5e8027fcad23fda98b2e3ac259d8d67585f671
```

* Los códigos largos son **SHA de commits**.
* Identifican una versión exacta del código de la acción.
* Esa versión **nunca cambia**.

Note: Lo que va detrás de la `@` en las acciones puede parecer misterioso al principio. Estos **códigos alfanuméricos largos son SHA de commits** del repositorio de la acción. Cada commit tiene un identificador único que nunca cambia. Cuando usamos un SHA, estamos diciendo "quiero ejecutar exactamente este código, no importa qué cambios hagan los desarrolladores de la acción en el futuro".


### 3.2. Tres formas de referenciar

Lo que va detrás de `@` puede ser:

1. **Rama** → `@main`, `@master`
2. **Versión etiquetada** → `@v3`, `@v5`
3. **Commit concreto (SHA)** → `@f4ef78c0...`

Note: Tenemos **tres formas de referenciar una acción**. Usar una rama como `@main` significa que siempre ejecutarás la última versión disponible en esa rama, lo cual puede ser arriesgado si introducen cambios incompatibles. Usar una versión etiquetada como `@v3` es más estable pero aún recibe actualizaciones menores. Usar el SHA de un commit específico te garantiza ejecutar exactamente ese código, sin sorpresas.


### 3.3. Ventajas del SHA

* **Reproducible**: Siempre ejecutas la misma versión.
* **Seguro**: Evita cambios inesperados en la acción.
* **Auditable**: Sabes exactamente qué código se ejecuta.
* **Supply chain security**: Control total de dependencias.

Note: Las **ventajas de usar SHA** son principalmente de seguridad y reproducibilidad. Si una acción se ve comprometida o introduce un bug en una nueva versión, tú seguirás usando la versión que has validado. En entornos productivos con alto foco en seguridad, especialmente en la supply chain (cadena de suministro del software), pinear por SHA es una práctica recomendada.


### 3.4. Inconvenientes del SHA

* **Te quedas congelado**: No recibes actualizaciones.
* **Sin correcciones**: Los bugfixes no llegan automáticamente.
* **Mantenimiento manual**: Debes actualizar conscientemente.
* **Menos legible**: Difícil saber qué versión es.

Note: El principal **inconveniente de usar SHA** es que te quedas congelado en esa versión. Si los desarrolladores publican una corrección de seguridad o un bugfix importante, no lo recibirás automáticamente. Tendrás que actualizar manualmente el SHA en tu workflow. Además, los SHA no son legibles para humanos, a diferencia de `@v3` que inmediatamente te dice que estás en la versión 3.

---

## 4. @v3 vs @SHA


### 4.1. Cuándo usar @v3

Ejemplos más legibles:

```yaml
uses: docker/login-action@v3
uses: docker/build-push-action@v5
```

* **Más legible** y sencillo para proyectos docentes.
* Permite actualizaciones dentro de esa versión mayor.
* **Recomendado para aprendizaje** y desarrollo.

Note: Para **proyectos educativos y de aprendizaje**, como los que desarrollamos en clase, usar referencias como `@v3` o `@v5` es lo más recomendable. Son fáciles de leer, entender y recordar. Además, recibirás automáticamente mejoras y correcciones de bugs dentro de esa versión mayor, sin necesidad de actualizar manualmente tu workflow.


### 4.2. Cuándo usar @SHA

* **Entornos productivos** con foco en seguridad.
* Cuando necesitas **garantías absolutas** de reproducibilidad.
* **Cumplimiento normativo** (compliance).
* Proyectos con auditorías de seguridad estrictas.

Note: El **pin por SHA es para entornos de producción** donde la seguridad y la reproducibilidad son críticas. Por ejemplo, en aplicaciones bancarias, sanitarias o gubernamentales donde se requieren auditorías estrictas de qué código se ejecuta exactamente. También es útil cuando necesitas garantizar que un pipeline funcione exactamente igual dentro de 6 meses, sin importar qué cambios hayan hecho los desarrolladores de las acciones.


### 4.3. Recomendación para el aula

Para el módulo DAW:

* **Usar @v3, @v4, @v5**: Versiones etiquetadas.
* **Dejar @SHA**: Como tema avanzado.
* **Explicar el concepto**: Pero no complicar workflows iniciales.

Note: Nuestra **recomendación para el aula** es clara: empezad con versiones etiquetadas tipo `@v3`. Son perfectas para aprender, desarrollar proyectos y entender los conceptos. Podéis mencionar el pin por SHA como una práctica avanzada para cuando entréis en "ligas mayores" de seguridad en vuestras carreras profesionales, pero no compliquéis vuestros primeros workflows con ello.


### 4.4. Actualización de versiones

```yaml
# Actualización fácil con versiones
- uses: docker/login-action@v3  # Actualizar a v4
- uses: docker/login-action@v4

# Actualización con SHA
- uses: docker/login-action@f4ef78c0...  # Buscar nuevo SHA
- uses: docker/login-action@1a2b3c4d...  # Nuevo hash
```

Note: Aquí vemos la **diferencia práctica a la hora de actualizar**. Con versiones etiquetadas, simplemente cambias `v3` por `v4` y listo. Con SHA, tienes que ir al repositorio de la acción, buscar el commit correspondiente a la nueva versión, copiar su hash completo y reemplazarlo. Es más trabajo, pero también más control.

---

## 5. Tags y digest


### 5.1. Dos formas de identificar imágenes

Una imagen Docker se identifica de dos formas:

1. **Por tag** (etiqueta): `kruhale/springboot:latest`
2. **Por digest** (hash): `sha256:1fdfb4c1b7f9...`

* El **tag** es un nombre humano y **mutable**.
* El **digest** es un hash criptográfico e **inmutable**.

Note: Las **imágenes Docker tienen dos identidades**. Los tags son como apodos o nombres comerciales, fáciles de recordar pero que pueden cambiar. Hoy `latest` puede apuntar a una imagen, mañana a otra diferente después de un nuevo build. El digest, en cambio, es como el DNI o huella dactilar de la imagen: un hash criptográfico único que identifica exactamente ese contenido. Si cambia aunque sea un byte, el digest cambia.


### 5.2. Tags humanos

```yaml
kruhale/springboot:latest
kruhale/springboot:v1.0
kruhale/springboot:2024-12-09
```

* **Legibles**: Fáciles de recordar y usar.
* **Mutables**: Pueden apuntar a diferentes imágenes.
* **Convenientes**: Para desarrollo y despliegue rápido.
* **Riesgosos**: `latest` no garantiza qué versión es.

Note: Los **tags son prácticos y legibles**. Puedes usar `latest` para la versión más reciente, `v1.0` para una versión específica, o incluir la fecha como `2024-12-09`. Sin embargo, ten en cuenta que `latest` es especialmente traicionero: no significa "la más estable" ni "la de producción", simplemente significa "la última que se subió". Mañana podría ser una versión totalmente diferente.


### 5.3. Digest: el DNI de la imagen

```yaml
kruhale/springboot@sha256:1fdfb4c1b7f9e9f2e26a0bfb0e2a0c7f...
```

* **Inmutable**: Si el contenido cambia, cambia el digest.
* **Verificable**: Garantiza la integridad de la imagen.
* **Seguro**: Sabes exactamente qué estás ejecutando.
* **Trazable**: Para auditorías y compliance.

Note: El **digest es el DNI de la imagen**. Es un hash SHA-256 del contenido completo de la imagen. Si cambias aunque sea un byte en cualquier capa de la imagen, el digest será completamente diferente. Esto permite **verificar la integridad**: puedes estar seguro de que la imagen que estás descargando y ejecutando es exactamente la que esperas, sin modificaciones ni manipulaciones.


### 5.4. Metáfora para clase

* **Tag**: El apodo ("latest", "v1.0", "stable").
    
    * Fácil de usar pero puede cambiar.

* **Digest**: El DNI de la imagen.
    
    * Único, inmutable, verificable.

Note: Para que quede claro en el aula, usamos esta **metáfora**: el tag es como un apodo o nombre artístico que puede cambiar o que varias personas pueden compartir. El digest es como tu número de DNI: único, inmutable e intransferible. Si alguien te pide tu DNI, sabes que estás identificándote de forma inequívoca. Lo mismo con las imágenes Docker.


### 5.5. Uso del digest en workflows

```yaml
- name: Build and push
  id: push
  uses: docker/build-push-action@v5
  with:
    push: true
    tags: usuario/imagen:latest

- name: Usar digest
  run: |
    echo "Digest: ${{ steps.push.outputs.digest }}"
```

Note: En nuestros workflows, podemos **capturar el digest** de la imagen que acabamos de construir usando `outputs.digest` del step de build. Esto es extremadamente útil para los siguientes pasos del pipeline, como generar attestations, desplegues controlados, o simplemente para logging y trazabilidad. El digest nos da la certeza absoluta de qué imagen estamos procesando.

---

## 6. docker/metadata-action


### 6.1. ¿Qué hace metadata-action?

```yaml
- name: Extract metadata (tags, labels) for Docker
  id: meta
  uses: docker/metadata-action@v5
  with:
    images: kruhale/springboot
    tags: |
      type=sha,format=short
      type=raw,value=latest
```

* Genera **tags automáticamente** según reglas.
* Crea **labels** estándar OCI.
* Simplifica la gestión de versiones.

Note: **`docker/metadata-action`** es una acción extremadamente útil que automatiza la generación de tags y labels para nuestras imágenes. En lugar de escribir manualmente todos los tags que queremos aplicar, definimos reglas y la acción los genera por nosotros. Por ejemplo, puede crear automáticamente un tag con el SHA corto del commit, otro con `latest`, otro con la versión del release, etc.


### 6.2. Tipos de tags automáticos

Tipos de tags que puede generar:

* **`type=sha`**: Tag basado en el hash del commit.
* **`type=raw`**: Tag estático (ej: `latest`).
* **`type=ref`**: Tag basado en rama o PR.
* **`type=semver`**: Tag basado en versión semántica.

Note: La acción soporta **múltiples tipos de tags** según tus necesidades. `type=sha` crea un tag único para cada commit, perfecto para trazabilidad. `type=raw` te permite definir tags estáticos como `latest` o `stable`. `type=ref` usa el nombre de la rama o pull request. `type=semver` extrae automáticamente versiones del tipo `v1.2.3` si usas tags de Git con versionado semántico.


### 6.3. Labels OCI estándar

```yaml
- id: meta
  uses: docker/metadata-action@v5
  with:
    images: kruhale/springboot
```

Genera automáticamente:

* `org.opencontainers.image.created`: Fecha de creación.
* `org.opencontainers.image.source`: URL del repositorio.
* `org.opencontainers.image.revision`: SHA del commit.

Note: Además de tags, la acción genera automáticamente **labels estándar OCI** (Open Container Initiative). Estos labels son metadatos que se añaden a la imagen y proporcionan información valiosa: cuándo se creó, desde qué repositorio, qué commit específico, quién es el autor, etc. Es información crucial para trazabilidad y auditorías.


### 6.4. Integración con build-push

```yaml
- uses: docker/metadata-action@v5
  id: meta
  with:
    images: kruhale/springboot

- uses: docker/build-push-action@v5
  with:
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
    push: true
```

Note: El **patrón de uso típico** es generar los metadatos en un step y luego usarlos en el build. La acción `metadata-action` genera dos outputs importantes: `tags` (una lista de todos los tags que debemos aplicar) y `labels` (todos los labels OCI). Estos se pasan directamente a `build-push-action`, que los aplica a la imagen durante la construcción.


### 6.5. Patrón recomendado

Define siempre al menos:

1. **Tag inmutable** por commit (`type=sha`).
2. **Tag flotante** (`latest` o `develop`).
3. **Labels automáticos** para trazabilidad.

Note: El **buen patrón didáctico** que recomendamos es definir explícitamente al menos dos tipos de tags: uno inmutable basado en el commit (para trazabilidad y rollback) y uno flotante como `latest` (para facilitar despliegues). Los labels automáticos siempre deben incluirse porque añaden valor sin coste. Este enfoque equilibra usabilidad y trazabilidad.


### 6.6. Valores por defecto

* La acción tiene **valores por defecto**.
* Normalmente **no deja tags vacío**.
* Pero es mejor ser **explícito** en la configuración.
* Facilita la comprensión del workflow.

Note: Aunque `metadata-action` tiene valores por defecto y no deja los tags vacíos si no defines ninguno, es **mejor ser explícito**. Definir claramente qué tags quieres ayuda a que cualquiera que lea tu workflow (incluido tu yo del futuro) entienda exactamente qué está pasando. La claridad es más importante que ahorrar dos líneas de YAML.

---

## 7. Provenance y attestation


### 7.1. ¿Qué es una attestation?

* **Documento firmado** que describe cómo se construyó un artefacto.
* Incluye información del **repositorio**, **workflow**, **commit**.
* **GitHub la firma** usando la identidad del workflow.
* Proporciona **trazabilidad** y **seguridad**.

Note: Una **attestation de build** es como un certificado notarial para tu imagen Docker. Es un documento firmado digitalmente que certifica: "Esta imagen (identificada por su digest) fue construida en este repositorio específico, usando este workflow de GitHub Actions concreto, desde este commit particular, en esta fecha y hora". GitHub firma este certificado usando la identidad del workflow, proporcionando una prueba criptográfica de su autenticidad.


### 7.2. Información incluida

Una attestation contiene:

* **Digest** de la imagen (su DNI).
* **Repositorio** de origen.
* **Workflow** que la construyó.
* **Commit** específico del código fuente.
* **Fecha y hora** de construcción.
* **Firma digital** de GitHub.

Note: La **información en una attestation** es muy completa. El digest identifica inequívocamente la imagen. El repositorio y workflow indican dónde y cómo se construyó. El commit específico permite rastrear exactamente qué código fuente se usó. La fecha y hora dan contexto temporal. Y la firma digital de GitHub garantiza que nadie ha manipulado esta información, actuando como un sello de autenticidad.


### 7.3. Utilidad práctica

Trazabilidad:

* Saber **exactamente de dónde** salió una imagen.
* Rastrear el **código fuente** usado en la build.

Seguridad:

* Exigir "solo imágenes con attestation válida".
* Verificar la **cadena de suministro** del software.

Note: Las **utilidades prácticas** son dobles. Para trazabilidad, puedes responder preguntas como "¿qué versión del código está corriendo en producción?" o "¿cuándo se construyó esta imagen?". Para seguridad, puedes establecer políticas como "solo ejecutar imágenes con attestation válida generada desde nuestros repositorios oficiales", evitando que se ejecuten imágenes de origen desconocido o modificadas.


### 7.4. Supply chain security

* Parte de la **cadena de suministro** del software.
* Previene **imágenes manipuladas** o de origen dudoso.
* Cumple con normativas de seguridad modernas.
* Fundamental en entornos **regulados** o críticos.

Note: Las attestations son fundamentales para la **supply chain security** (seguridad de la cadena de suministro). En el desarrollo moderno, no solo escribes código, también usas imágenes base, librerías y herramientas de terceros. Las attestations permiten verificar cada eslabón de esta cadena. Son especialmente importantes en sectores regulados como banca, salud o gobierno, donde debes poder demostrar el origen y la integridad de todo tu software.

---

## 8. attest-build-provenance


### 8.1. La acción de attestation

```yaml
- name: Generate artifact attestation
  uses: actions/attest-build-provenance@v3
  with:
    subject-name: index.docker.io/kruhale/springboot
    subject-digest: ${{ steps.push.outputs.digest }}
    push-to-registry: true
```

* **`subject-name`**: Referencia de la imagen en el registry.
* **`subject-digest`**: DNI de la imagen (inmutable).
* **`push-to-registry`**: Subir la attestation al registry.

Note: **`actions/attest-build-provenance`** es la acción que genera y publica la attestation. Los tres parámetros clave son: `subject-name` que identifica de qué imagen estamos hablando usando su nombre en el registry, `subject-digest` que es el DNI inmutable de la imagen (no usamos el tag porque puede cambiar), y `push-to-registry` que indica que queremos subir esta attestation junto con la imagen al registry para que esté disponible públicamente.


### 8.2. Workflow completo

```yaml
- name: Build and push Docker image
  id: push
  uses: docker/build-push-action@v5
  with:
    push: true
    tags: ${{ steps.meta.outputs.tags }}

- name: Generate artifact attestation
  uses: actions/attest-build-provenance@v3
  with:
    subject-name: index.docker.io/kruhale/springboot
    subject-digest: ${{ steps.push.outputs.digest }}
    push-to-registry: true
```

Note: Este es el **workflow completo** que primero construye y sube la imagen, y luego genera su attestation. Es crucial el orden: primero hacemos push de la imagen (y capturamos su digest), y luego generamos la attestation usando ese digest. La attestation se sube al mismo registry que la imagen, quedando vinculada a ella de forma permanente.


### 8.3. Permisos necesarios

```yaml
permissions:
  id-token: write
  attestations: write
  contents: read
```

* **`id-token: write`**: Para obtener token OIDC.
* **`attestations: write`**: Para crear attestations.
* **`contents: read`**: Para leer el código del repositorio.

Note: Para que las attestations funcionen, el workflow necesita **permisos específicos**. `id-token: write` permite al workflow obtener un token de identidad OIDC que GitHub usa para firmar la attestation. `attestations: write` permite crear y publicar attestations. `contents: read` es el permiso básico para leer el código del repositorio. Estos permisos se declaran al inicio del workflow en la sección `permissions`.


### 8.4. Ventaja sobre workflow simple

Workflow sin attestation:

* Solo sube la imagen a Docker Hub.

Workflow con attestation:

* Sube la imagen + **certificado firmado** de cómo se construyó.
* Añade **capa de seguridad** y trazabilidad extra.
* Permite **verificación posterior** de la autenticidad.

Note: La **diferencia clave** es que un workflow básico solo sube bits (la imagen), mientras que un workflow con attestation sube bits más un certificado de autenticidad firmado. Es como la diferencia entre enviar un paquete sin rastro versus enviarlo con seguimiento certificado. La attestation permite a cualquiera verificar posteriormente que esa imagen fue realmente construida en tu repositorio, desde tu workflow oficial, sin manipulaciones.


### 8.5. Verificación de attestations

```bash
# Listar attestations de una imagen
gh attestation list oci://kruhale/springboot:latest

# Verificar una attestation específica
gh attestation verify oci://kruhale/springboot@sha256:1fdfb4c1...
```

Note: Una vez generadas, las **attestations pueden verificarse** usando la CLI de GitHub (`gh`). Puedes listar todas las attestations asociadas a una imagen, ver su contenido, y verificar su firma digital. Esto es útil para auditorías, debugging, o simplemente para confirmar que una imagen proviene de donde dice provenir. La verificación comprueba la firma criptográfica contra la identidad del workflow que la generó.


### 8.6. Mensaje para el alumnado

* No solo subo imágenes al registry.
* También subo un **certificado de autenticidad**.
* Demuestra **cómo y desde dónde** se construyó.
* Es el **siguiente nivel** de profesionalidad.

Note: El mensaje clave para el alumnado es que pasar de "subir imágenes" a "subir imágenes con attestations" es pasar de un workflow funcional a un workflow profesional. Es demostrar que no solo sabes automatizar, sino que entiendes la importancia de la trazabilidad y la seguridad en la cadena de suministro del software. Es una diferencia que valorarán en entornos profesionales serios.

---

## 9. docker/login-action


### 9.1. Login manual vs acción

Forma manual (shell):

```yaml
- name: Login Docker Hub (forma manual)
  run: echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
```

Con acción:

```yaml
- name: Login Docker Hub
  uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_PASSWORD }}
```

Note: Podemos hacer login en Docker Hub de **dos formas**: manualmente con comandos shell o usando la acción especializada. La forma manual funciona, pero es más propensa a errores: problemas con comillas, pipes, caracteres especiales en passwords, etc. La acción `docker/login-action` encapsula toda esta complejidad en una interfaz limpia y probada.


### 9.2. Ventajas de usar la acción

* **Menos errores**: No lidiar con comillas y pipes.
* **Más seguro**: Gestión estandarizada de credenciales.
* **Más limpio**: Workflows más legibles.
* **Mejor documentado**: Opciones claras y ejemplos.

Note: Las **ventajas de la acción especializada** son múltiples. No tienes que recordar la sintaxis exacta de `docker login` ni preocuparte por escapar caracteres especiales. La gestión de secretos es más estándar y segura. El workflow queda más limpio y declarativo. Y tienes mejor documentación con ejemplos probados por miles de usuarios.


### 9.3. Soporte para múltiples registries

```yaml
- uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

* Docker Hub (por defecto)
* GitHub Container Registry (`ghcr.io`)
* Amazon ECR
* Google Container Registry
* Azure Container Registry

Note: La acción **soporta múltiples registries**, no solo Docker Hub. Puedes usarla para autenticarte en GitHub Container Registry (ghcr.io) usando tu propio usuario de GitHub y un token generado automáticamente. También funciona con los registries de los grandes proveedores cloud como AWS ECR, Google GCR o Azure ACR. Simplemente cambias el parámetro `registry` y ajustas las credenciales.


### 9.4. Autenticación en GitHub Container Registry

```yaml
- name: Login GHCR
  uses: docker/login-action@v3
  with:
    registry: ghcr.io
    username: ${{ github.actor }}
    password: ${{ secrets.GITHUB_TOKEN }}
```

* No necesitas crear secrets adicionales.
* Usa el **token automático** del workflow.
* Imagen: `ghcr.io/usuario/nombre-imagen:tag`

Note: Un caso especial interesante es **GitHub Container Registry**. No necesitas crear secretos manualmente porque GitHub proporciona automáticamente un token (`GITHUB_TOKEN`) a cada workflow. Simplemente usas `github.actor` (tu usuario de GitHub) como username y el token automático como password. Las imágenes se publican bajo `ghcr.io/tu-usuario/nombre-imagen`.


### 9.5. Logout automático

* La acción hace **logout automático** al terminar el job.
* Limpia las credenciales del runner.
* No dejan rastro entre diferentes workflows.
* Seguridad adicional en runners compartidos.

Note: Algo muy importante para seguridad: la acción hace **logout automático** al finalizar el job. Esto significa que las credenciales no quedan almacenadas en el runner después de que tu workflow termina. Es especialmente importante en los runners compartidos de GitHub, donde múltiples workflows de diferentes usuarios pueden ejecutarse en la misma máquina virtual. Limpieza automática = menos vectores de ataque.

---

## 10. docker/build-push-action


### 10.1. Build manual vs acción

Versión manual (shell):

```yaml
- run: docker build . -t usuario/imagen:tag
- run: docker push usuario/imagen:tag
```

Con acción:

```yaml
- name: Build and push
  uses: docker/build-push-action@v5
  with:
    context: .
    file: ./Dockerfile
    push: true
    tags: usuario/imagen:tag
```

Note: Similar al login, podemos construir y subir imágenes **manualmente con comandos** o usando la acción especializada. Los comandos directos son perfectos para entender los fundamentos de Docker, pero la acción `build-push-action` es la versión industrial que aporta características avanzadas que veremos a continuación.


### 10.2. Ventajas de la acción

* Usa **Buildx / BuildKit** por debajo.
* Soporte **multi-arquitectura** (amd64, arm64, etc.).
* **Mejor gestión de cachés** para builds más rápidas.
* Expone **outputs** (digest, metadata, etc.).
* Configuración **declarativa** en YAML.

Note: Las **ventajas clave** de usar la acción son tecnológicas. Usa Buildx y BuildKit, las tecnologías modernas de Docker que permiten builds en paralelo, mejor uso de caché y construcción multi-arquitectura. Puedes construir una imagen que funcione tanto en Intel/AMD (amd64) como en ARM (arm64) para Raspberry Pi o Macs con chip M1/M2. Además, expone información útil como el digest de la imagen construida.


### 10.3. Construcción multi-plataforma

```yaml
- uses: docker/build-push-action@v5
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: usuario/imagen:latest
```

* Una sola build genera imágenes para **múltiples arquitecturas**.
* Docker selecciona automáticamente la correcta al descargar.
* Útil para **Raspberry Pi**, **Macs M1/M2**, **servidores ARM**.

Note: La **construcción multi-plataforma** es una característica potente. Con una sola ejecución del workflow, generas imágenes para diferentes arquitecturas de CPU. Cuando alguien hace `docker pull`, Docker descarga automáticamente la versión correcta para su arquitectura. Esto es fundamental en 2024 donde tenemos diversidad de hardware: desde servidores Intel hasta Raspberry Pi ARM pasando por los nuevos Macs con chip Apple Silicon.


### 10.4. Gestión de caché

```yaml
- uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: usuario/imagen:latest
    cache-from: type=gha
    cache-to: type=gha,mode=max
```

* **Caché entre builds** para acelerar construcciones.
* `type=gha`: Usa el sistema de caché de GitHub Actions.
* Reduce tiempo y coste de builds repetitivas.

Note: La **gestión de caché** puede reducir drásticamente los tiempos de build. `cache-from` y `cache-to` con `type=gha` utilizan el sistema de caché de GitHub Actions para almacenar y reutilizar las capas de Docker entre diferentes ejecuciones del workflow. Si tu imagen usa una imagen base pesada o instala muchas dependencias, estas se cachean y solo se reconstruyen cuando realmente cambian. Esto ahorra tiempo y minutos de runner (que en repos privados cuestan dinero).


### 10.5. Outputs disponibles

```yaml
- name: Build and push
  id: build
  uses: docker/build-push-action@v5
  with:
    push: true

- name: Usar outputs
  run: |
    echo "Digest: ${{ steps.build.outputs.digest }}"
    echo "Metadata: ${{ steps.build.outputs.metadata }}"
```

* **digest**: Hash SHA-256 de la imagen construida.
* **metadata**: Información adicional sobre la build.

Note: La acción expone **outputs útiles** que podemos usar en steps posteriores. El más importante es `digest`, el identificador inmutable de la imagen que acabamos de construir. Esto es crucial para encadenar con otras acciones como las attestations que vimos antes. También expone `metadata` con información adicional sobre la build que puede ser útil para logging o notificaciones.


### 10.6. Patrón completo recomendado

```yaml
- uses: docker/setup-buildx-action@v3
- uses: docker/login-action@v3
  with:
    username: ${{ secrets.DOCKERHUB_USERNAME }}
    password: ${{ secrets.DOCKERHUB_PASSWORD }}
- uses: docker/metadata-action@v5
  id: meta
  with:
    images: usuario/imagen
- uses: docker/build-push-action@v5
  with:
    push: true
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
```

Note: Este es el **patrón completo y profesional** que combina todas las acciones que hemos visto. Setup-buildx para preparar el builder avanzado, login para autenticarnos, metadata para generar tags y labels automáticamente, y build-push para construir y publicar. Es más verboso que dos comandos shell, pero proporciona capacidades industriales: multi-arquitectura, caché, metadatos automáticos, outputs para encadenar, etc.

---

## 11. docker/setup-buildx-action


### 11.1. ¿Qué es Buildx?

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3
```

* **Buildx**: Cliente moderno de Docker para builds avanzadas.
* Basado en **BuildKit**, el motor de builds de nueva generación.
* Habilita características no disponibles en `docker build` clásico.

Note: **Docker Buildx** es el cliente moderno de Docker para construcción de imágenes. Está basado en BuildKit, que es el motor de builds de nueva generación de Docker, completamente rediseñado desde cero. Mientras que el `docker build` tradicional está limitado a builds simples en una sola arquitectura, Buildx desbloquea un mundo de posibilidades avanzadas.


### 11.2. Características de Buildx

* **Multi-plataforma**: Construir para varias arquitecturas.
* **Caché avanzada**: Mejor reutilización de capas.
* **Builds en paralelo**: Múltiples stages simultáneamente.
* **Outputs flexibles**: No solo imágenes (también tar, OCI, etc.).

Note: Las **características de Buildx** van mucho más allá del build tradicional. Puedes construir para múltiples arquitecturas de CPU en una sola ejecución. El sistema de caché es mucho más inteligente y granular. Puede construir stages de multi-stage builds en paralelo aprovechando mejor los CPUs modernos. Y puede generar outputs en diferentes formatos, no solo imágenes Docker sino también archives tar, formato OCI, etc.


### 11.3. ¿Cuándo es necesario?

* **Opcional** para builds sencillas.
* **Necesario** para:
    
    * Multi-plataforma (linux/amd64, linux/arm64).
    * Caché avanzada.
    * Configuraciones específicas del builder.

Note: `setup-buildx-action` **no siempre es obligatorio**. Para workflows simples que solo construyen una imagen para una arquitectura, el build clásico puede funcionar. Pero se vuelve necesario cuando quieres aprovechar características avanzadas como construir para múltiples arquitecturas simultáneamente, usar sistemas de caché avanzados, o configurar aspectos específicos del builder como el driver o el endpoint.


### 11.4. Patrón típico de uso

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v3

- name: Build and push
  uses: docker/build-push-action@v5
  with:
    platforms: linux/amd64,linux/arm64
    push: true
    tags: usuario/imagen:tag
```

Note: El **patrón típico** es activar Buildx primero con `setup-buildx-action` y luego usar `build-push-action` que automáticamente detecta y utiliza Buildx. Esto te da acceso a todas las características avanzadas sin necesidad de cambiar mucho tu workflow. Es como actualizar tu herramienta: primero la instalas/activas y luego la usas normalmente pero con más capacidades.


### 11.5. Configuración del builder

```yaml
- uses: docker/setup-buildx-action@v3
  with:
    driver: docker-container
    platforms: linux/amd64,linux/arm64
    install: true
```

* **driver**: Tipo de builder (docker-container, kubernetes, etc.).
* **platforms**: Plataformas soportadas.
* **install**: Hacer que Buildx sea el builder por defecto.

Note: Puedes **configurar aspectos específicos** del builder. El `driver` determina cómo y dónde se ejecutan las builds (docker-container es el más común). `platforms` predefine qué arquitecturas soportará. `install: true` hace que Buildx se convierta en el builder por defecto, reemplazando el clásico, lo cual es útil si también tienes pasos con comandos docker directos que quieras que aprovechen Buildx.


### 11.6. Valor educativo

* Los comandos directos: **perfectos para aprender Docker**.
* Las acciones especializadas: **versión industrial para CI/CD**.
* **Progresión pedagógica**: Primero manual, luego automatizado.

Note: En términos educativos, el mensaje es claro: **empezar con comandos directos** (`docker build`, `docker push`) es perfecto para entender los fundamentos de Docker. Una vez dominas esos conceptos, pasar a las acciones especializadas (`setup-buildx`, `build-push-action`) te lleva al siguiente nivel: construcción industrial con multi-arquitectura, caché inteligente, metadatos automáticos y mejor integración en pipelines de CI/CD. Es la progresión natural de junior a senior.

---

## 12. Resumen y buenas prácticas


### 12.1. Flujo completo profesional

```yaml
name: Docker Build, Push & Attest

on: [push]

permissions:
  contents: read
  packages: write
  id-token: write
  attestations: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - uses: docker/login-action@v3
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_PASSWORD }}
```

Note: Aquí comenzamos a montar el **workflow completo y profesional** que integra todo lo aprendido. Definimos los permisos necesarios para poder crear attestations. El job empieza con los tres pasos fundamentales: checkout del código, setup de Buildx para builds avanzadas, y login en el registry donde publicaremos.


### 12.1. Flujo completo profesional (continuación)

```yaml
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: usuario/imagen
          tags: |
            type=sha,format=short
            type=raw,value=latest
      - uses: docker/build-push-action@v5
        id: push
        with:
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          platforms: linux/amd64,linux/arm64
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

Note: Continuamos con **metadata-action** generando tags automáticos (uno por SHA del commit y otro `latest`), más todos los labels OCI estándar. Luego **build-push-action** construye para dos arquitecturas, usa el sistema de caché de GitHub Actions para acelerar builds futuras, y publica la imagen con todos los tags y labels generados. Capturamos el output en `id: push` para usar el digest después.


### 12.1. Flujo completo profesional (final)

```yaml
      - uses: actions/attest-build-provenance@v3
        with:
          subject-name: index.docker.io/usuario/imagen
          subject-digest: ${{ steps.push.outputs.digest }}
          push-to-registry: true
```

Note: Finalmente, generamos la **attestation de build** usando el digest de la imagen que acabamos de publicar. Esta attestation se sube al registry junto con la imagen, proporcionando un certificado firmado de todo el proceso de construcción. Este es el workflow completo que combina automatización, multi-arquitectura, trazabilidad y seguridad.


### 12.2. Checklist de buenas prácticas

✅ Usar acciones oficiales (`@v3`, `@v4`, `@v5`).  
✅ Almacenar credenciales en **secrets**.  
✅ Generar **tags automáticos** con metadata-action.  
✅ Incluir al menos un **tag inmutable** (SHA).  
✅ Activar **Buildx** para características avanzadas.  
✅ Usar **caché** para acelerar builds.  
✅ Generar **attestations** para trazabilidad.

Note: Este **checklist de buenas prácticas** resume lo esencial. Usa las acciones oficiales en sus versiones etiquetadas, nunca pongas credenciales en el código. Genera tags automáticamente para evitar errores manuales. Siempre incluye un tag inmutable basado en el commit para trazabilidad. Activa Buildx si necesitas multi-arquitectura. Configura caché para no desperdiciar tiempo en builds repetitivas. Y genera attestations para añadir esa capa de seguridad profesional.


### 12.3. Errores comunes a evitar

❌ Credenciales en el código del workflow.  
❌ Usar solo `latest` sin tags inmutables.  
❌ No configurar permisos para attestations.  
❌ Olvidar el login antes del push.  
❌ No usar caché en proyectos con builds lentas.  
❌ Ignorar el digest y usar solo tags mutables.

Note: Los **errores comunes** que vemos en el aula. El más grave es poner credenciales directamente en el workflow (siempre usar secrets). Usar solo `latest` sin tags inmutables hace imposible la trazabilidad. Olvidar configurar permisos de attestations resulta en errores crípticos. El orden importa: login antes de push. No configurar caché en proyectos grandes desperdicia tiempo. Y finalmente, ignorar el digest y trabajar solo con tags mutables limita tu capacidad de verificación.


### 12.4. Progresión de aprendizaje

**Nivel 1 - Básico**:

* Workflow mínimo: checkout, login, build, push.
* Uso de comandos `docker` directos.

**Nivel 2 - Intermedio**:

* Acciones especializadas (login-action, build-push-action).
* Generación de tags con metadata-action.

**Nivel 3 - Avanzado**:

* Multi-arquitectura con Buildx.
* Caché avanzada.
* Attestations de build.

Note: Recomendamos esta **progresión pedagógica** en el aula. Empezar con un workflow básico usando comandos docker directos para entender los fundamentos. Luego pasar a acciones especializadas que simplifican y potencian el workflow. Finalmente, introducir conceptos avanzados como multi-arquitectura, caché y attestations. Cada nivel construye sobre el anterior sin invalidarlo.


### 12.5. Recursos adicionales

* Documentación oficial: `docs.github.com/actions`
* Docker Actions: `github.com/docker/login-action`
* Marketplace: Miles de acciones reutilizables.
* Comunidad: Ejemplos reales en repos públicos.

Note: Para profundizar más, los **recursos adicionales** son fundamentales. La documentación oficial de GitHub Actions es excelente y está en constante actualización. Cada acción de Docker tiene su propio repositorio con documentación detallada y ejemplos. El Marketplace de GitHub Actions tiene miles de acciones para cualquier necesidad. Y no subestiméis aprender leyendo workflows reales de proyectos open source populares.


### 12.6. Para recordar

* Docker **ya está instalado** en ubuntu-latest.
* Usa **@v3, @v4, @v5** para aprender; **@SHA** para producción.
* Los **tags son mutables**, los **digest son inmutables**.
* Las **attestations** certifican cómo se construyó la imagen.
* Las **acciones especializadas** simplifican y potencian workflows.

Note: Los **puntos clave para recordar**: Docker viene preinstalado en los runners de GitHub, no necesitas instalarlo. Usa versiones etiquetadas para aprender y desarrollo. Entiende la diferencia entre tags (mutables, legibles) y digest (inmutable, verificable). Las attestations añaden un certificado de autenticidad a tus imágenes. Y las acciones especializadas de Docker no son solo azúcar sintáctico, realmente añaden capacidades que serían muy complejas de implementar manualmente.

---

## ¡Gracias!

¿Preguntas?

Note: Hemos cubierto todo el flujo de integración de Docker con GitHub Actions, desde lo más básico hasta conceptos avanzados de seguridad y trazabilidad. Recordad: empezad simple, entended los fundamentos, y luego id añadiendo complejidad según vuestras necesidades. La automatización de Docker en CI/CD es una habilidad fundamental para cualquier DevOps o desarrollador moderno. ¡Practicad con proyectos reales y consultad la documentación cuando tengáis dudas!
