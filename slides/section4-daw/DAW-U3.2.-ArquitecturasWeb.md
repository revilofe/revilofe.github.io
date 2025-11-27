# DAW-U3.2 - Arquitecturas Web y Fundamentos del Despliegue

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

1. Introducción
2. Arquitectura Cliente-Servidor
3. Evolución de la Web
4. Arquitecturas Web Principales
   4.1. Arquitectura Monolítica
   4.2. Arquitectura de Capas
   4.3. Arquitectura de Microservicios
   4.4. Arquitectura Serverless
   4.5. Comparativa de Arquitecturas


## Índice II

5. Patrón MVC
6. Principios SOLID
7. Otros Patrones de Diseño
8. Resumen y Conclusiones
10. Preguntas

---

## 1. Introducción

Note: Bienvenidos a la unidad sobre Arquitecturas Web y Fundamentos del Despliegue. En esta unidad exploraremos las diferentes arquitecturas que sustentan las aplicaciones web modernas, desde el clásico modelo cliente-servidor hasta arquitecturas avanzadas como microservicios y serverless. También repasaremos patrones de diseño clave como MVC y principios de diseño de software como SOLID. Al final de esta unidad, tendréis una comprensión sólida de cómo estructurar y desplegar aplicaciones web escalables y mantenibles.


### Arquitecturas Web Modernas

**¿Por qué es importante la arquitectura?**

- Determina cómo desplegamos aplicaciones
- Afecta escalabilidad y rendimiento
- Define estrategias de mantenimiento
- Impacta en costes operativos

Note: Bienvenidos a la unidad sobre Arquitecturas Web. Este tema es fundamental porque cada decisión arquitectónica tiene implicaciones directas en cómo desplegamos y mantenemos nuestras aplicaciones. No es solo teoría: lo que aprendáis aquí lo aplicaréis en cada despliegue que hagáis. Una buena arquitectura facilita el escalado, mejora el rendimiento y reduce costes operativos.

---

## 2. Arquitectura Cliente-Servidor

Note: Iniciamos con el modelo base de la web: Cliente-Servidor. Este patrón es la piedra angular sobre la que se construyen todas las aplicaciones web modernas. Entender sus fundamentos, ventajas y desventajas es crucial antes de explorar arquitecturas más complejas.


### Fundamentos

**El modelo base de la web**

- Cliente: navegador web que solicita servicios
- Servidor: sistema que proporciona recursos
- Red: Internet como medio de comunicación
- Protocolo: HTTP/HTTPS para la comunicación

Note: El modelo Cliente-Servidor es la base sobre la que se construye toda la web. Aunque es un concepto simple, su implementación puede ser muy compleja. El cliente, típicamente un navegador, realiza peticiones HTTP al servidor. El servidor procesa estas peticiones, accede a bases de datos si es necesario, y devuelve respuestas. Este modelo es extremadamente flexible y escalable, lo que explica su éxito durante décadas.


### Ventajas del Modelo

**¿Por qué es tan exitoso?**

1. **Centralización**: Control unificado de datos y lógica
2. **Escalabilidad**: Añadir servidores según demanda
3. **Portabilidad**: Funciona en cualquier dispositivo
4. **Mantenimiento**: Actualizaciones centralizadas

Note: La centralización es clave: cuando actualizamos el servidor, todos los clientes se benefician inmediatamente sin necesidad de reinstalar nada. La escalabilidad nos permite crecer añadiendo más servidores. La portabilidad significa que la misma aplicación funciona en Windows, Mac, Linux, móviles y tablets sin cambios. Y el mantenimiento centralizado reduce enormemente la complejidad operativa.


### Desventajas y Soluciones

**Problemas comunes y cómo resolverlos**

| Problema              | Solución                        |
|-----------------------|---------------------------------|
| Congestión de tráfico | Balanceadores de carga, CDN     |
| Fallo del servidor    | Clusters, alta disponibilidad   |
| Costes de hardware    | Virtualización, cloud computing |
<!-- .element.table: style="font-size:75%;" -->

Note: Ninguna arquitectura es perfecta. El modelo cliente-servidor tiene desventajas, pero todas tienen solución. La congestión se mitiga con balanceadores de carga y CDNs. Los fallos del servidor se previenen con clusters y redundancia. Los costes se optimizan con virtualización y cloud. Muchas de estas técnicas las habéis visto en unidades anteriores con Docker y CI/CD.

---

## 3. Evolución de la Web

Note: Antes de profundizar en arquitecturas específicas, es vital entender cómo ha evolucionado la web. Cada etapa de esta evolución ha traído nuevas necesidades y soluciones arquitectónicas. Desde las páginas estáticas de Web 1.0 hasta las aplicaciones inteligentes y distribuidas de Web 3.0 y más allá.


### De Web 1.0 a Web 4.0

**Un viaje de 30 años**

- **Web 1.0** (1991-2004): Páginas estáticas
- **Web 2.0** (2004-2010): Redes sociales y colaboración
- **Web 3.0** (2015-presente): Inteligencia artificial y APIs
- **Web 4.0** (futuro): IA avanzada y realidad aumentada

Note: La web ha evolucionado dramáticamente. Web 1.0 eran solo páginas HTML estáticas sin interacción. Web 2.0 trajo las redes sociales y contenido generado por usuarios. Web 3.0 introdujo APIs robustas, microservicios e inteligencia artificial. Web 4.0 es el futuro: interfaces naturales, realidad aumentada y personalización extrema. Entender esta evolución nos ayuda a comprender por qué las arquitecturas modernas son como son.


### Web 1.0: Los Orígenes

**La web estática (1991-2004)**

- Solo lectura, sin interacción
- HTML simple, sin bases de datos
- Actualización manual del contenido
- Diseño muy básico

Note: Web 1.0 era puramente informativa. Imagináos una biblioteca digital donde solo podéis leer, nunca escribir ni interactuar. Las páginas eran ficheros HTML estáticos almacenados en servidores. No había formularios complejos, ni bases de datos, ni personalización. Cada cambio requería editar manualmente los archivos HTML. Era limitada, pero fue revolucionaria en su momento.


### Web 2.0: La Revolución Social

**La web participativa (2004-2010)**

- Contenido generado por usuarios
- AJAX: interactividad sin recargar
- Plataformas colaborativas
- Redes sociales: Facebook, Twitter, YouTube

Note: Web 2.0 cambió todo. Los usuarios pasaron de ser consumidores pasivos a creadores de contenido. AJAX permitió actualizar partes de la página sin recargarla completa, mejorando enormemente la experiencia. Surgieron las redes sociales, los blogs, los wikis. Las aplicaciones web empezaron a parecerse a aplicaciones de escritorio en funcionalidad y responsividad.


### Web 3.0: Inteligencia y Servicios

**La web semántica (2015-presente)**

- APIs robustas y microservicios
- Machine learning y personalización
- Internet de las Cosas (IoT)
- Blockchain y descentralización
- Datos estructurados y semánticos

Note: Web 3.0 está marcada por la inteligencia artificial y la interconexión de servicios. Las APIs REST permiten que aplicaciones se comuniquen eficientemente. El machine learning personaliza experiencias. IoT conecta dispositivos físicos a internet. Blockchain introduce descentralización. Los datos están más estructurados y las máquinas pueden "entenderlos" mejor. Vivimos en esta era actualmente.

---

## 4.1. Arquitectura Monolítica

Note: Comenzamos con la arquitectura más simple: el monolito. Aunque a menudo se critica, el monolito sigue siendo relevante, especialmente para proyectos pequeños o MVPs. Entender sus ventajas y desventajas es crucial antes de saltar a arquitecturas más complejas.


### Características

**Todo en un solo bloque**

- Todos los componentes en un proceso
- Comparten memoria y recursos
- Despliegue como unidad única
- Una única base de código

Note: La arquitectura monolítica es el enfoque tradicional donde toda la aplicación forma un bloque único. La interfaz, la lógica de negocio y el acceso a datos están en la misma aplicación. Se despliega todo junto, se ejecuta en el mismo proceso, comparte memoria. Es el approach más simple para empezar un proyecto.


### Ventajas del Monolito

**¿Cuándo es la mejor opción?**

- ✅ Desarrollo inicial rápido
- ✅ Depuración más sencilla
- ✅ Testing directo
- ✅ Rendimiento en memoria excelente
- ✅ Ideal para proyectos pequeños y MVPs

Note: Los monolitos no son malos. De hecho, para proyectos pequeños o MVPs son la mejor opción. El desarrollo es rápido porque no hay complejidad distribuida. La depuración es más sencilla: todo el código está en un lugar. Los tests end-to-end son directos. Y el rendimiento es excelente porque las llamadas internas son en memoria, no por red. Muchos proyectos exitosos empiezan como monolitos.


### Desventajas del Monolito

**Problemas al crecer**

- ❌ Escalabilidad limitada: todo o nada
- ❌ Complejidad creciente difícil de manejar
- ❌ Acoplamiento fuerte entre componentes
- ❌ Despliegues arriesgados: todo a la vez
- ❌ Stack tecnológico único

Note: Los problemas aparecen cuando el monolito crece. No podéis escalar solo la parte que lo necesita: debéis replicar toda la aplicación. La complejidad crece exponencialmente. Un cambio pequeño requiere redesplegar todo. Un error en cualquier parte puede tumbar toda la aplicación. Y estáis atados a una sola tecnología para todo. La clave es mantener un monolito bien diseñado o migrar a tiempo.

---

## 4.2. Arquitectura de Capas

Note: La arquitectura de capas es una evolución del monolito que mejora la organización del código. Aunque sigue siendo un monolito, divide la aplicación en capas lógicas con responsabilidades claras. Esto facilita el mantenimiento y la escalabilidad dentro de los límites del monolito.


### División Lógica

**Separación de responsabilidades**

- **Presentación**: Interfaz de usuario
- **Lógica de negocio**: Reglas y procesamiento
- **Acceso a datos**: Interacción con BD
- **Persistencia**: Almacenamiento

Note: La arquitectura de capas es una evolución del monolito que busca mejorar la organización. Dividimos la aplicación en capas lógicas, cada una con una responsabilidad clara. La capa de presentación maneja la UI, la lógica de negocio contiene las reglas, el acceso a datos gestiona la BD, y la persistencia se encarga del almacenamiento. Sigue siendo un monolito, pero mejor organizado.


### Principios Fundamentales

**Reglas de comunicación**

1. Cada capa solo habla con la inmediata inferior
2. Dependencias unidireccionales
3. Ocultación de detalles de implementación
4. Alta cohesión, bajo acoplamiento

Note: Las reglas son claras: la comunicación fluye de arriba abajo. La presentación llama a lógica de negocio, que llama a acceso a datos. Nunca al revés. Esto crea dependencias unidireccionales que facilitan cambios. Cada capa oculta sus detalles de implementación. Y buscamos alta cohesión dentro de cada capa y bajo acoplamiento entre ellas.


### Ventajas de las Capas

**Mejor organización**

- Estructura clara y predecible
- Mantenibilidad mejorada
- Reutilización de capas
- Testing por capas independientes
- Equipos pueden especializarse por capa

Note: Las ventajas son significativas. La estructura clara facilita que nuevos desarrolladores entiendan el código. Un cambio en la presentación no afecta necesariamente a otras capas. Podéis reutilizar capas en diferentes contextos. Y los equipos pueden especializarse: un equipo en frontend, otro en backend, otro en datos. Es especialmente útil en organizaciones medianas.

---

## 4.3. Arquitectura de Microservicios

Note: Los microservicios representan un cambio radical en la forma de construir aplicaciones. En lugar de un solo monolito, tenemos muchos servicios pequeños e independientes que colaboran. Esta arquitectura es ideal para aplicaciones grandes y complejas, pero viene con su propio conjunto de desafíos.


### Concepto Fundamental

**Servicios pequeños y autónomos**

- Cada servicio hace una cosa específica
- Desarrollo y despliegue independientes
- Comunicación ligera (HTTP/REST)
- Descentralización total
- Diseñados para fallar gracefully

Note: Los microservicios representan un cambio de paradigma. En lugar de una aplicación grande, tenemos muchas aplicaciones pequeñas que colaboran. Cada microservicio se enfoca en un dominio específico del negocio: autenticación, pagos, inventario, etc. Se desarrollan, despliegan y escalan independientemente. Se comunican mediante APIs REST ligeras. Y asumen que los fallos ocurrirán.


### Ejemplo Real: Netflix

**Cientos de microservicios trabajando juntos**

- Servicio de autenticación
- Servicio de recomendaciones
- Servicio de streaming
- Servicio de suscripciones
- Servicio de análisis y métricas

Note: Netflix es el ejemplo clásico de microservicios a gran escala. Tienen cientos de microservicios independientes. Uno se encarga solo de autenticar usuarios. Otro de generar recomendaciones personalizadas usando machine learning. Otro gestiona el streaming de video. Otro las suscripciones y pagos. Cada servicio es mantenido por un equipo pequeño y autónomo que puede desplegar cambios sin afectar a otros servicios.


### Ventajas de Microservicios

**Escalabilidad y flexibilidad máximas**

- ✅ Agilidad: equipos autónomos
- ✅ Escalado granular: solo lo necesario
- ✅ Resiliencia: un fallo no tumba todo
- ✅ Libertad tecnológica por servicio
- ✅ Despliegue continuo facilitado

Note: Las ventajas son impresionantes. Los equipos trabajan de forma autónoma, lo que acelera el desarrollo. Podéis escalar solo el servicio de pagos si está sobrecargado, sin tocar los demás. Si el servicio de recomendaciones falla, el resto sigue funcionando. Cada equipo puede elegir la mejor tecnología para su problema. Y podéis desplegar cambios continuamente sin riesgo. Es ideal para organizaciones grandes y aplicaciones complejas.


### Desventajas de Microservicios

**Complejidad distribuida**

- ❌ Complejidad operacional alta
- ❌ Overhead de DevOps significativo
- ❌ Consistencia de datos compleja
- ❌ Latencia de red entre servicios
- ❌ Depuración difícil
- ❌ Costes mayores

Note: Pero no todo es positivo. La complejidad operacional es enorme: gestionar cien servicios es mucho más difícil que gestionar uno. Necesitáis un equipo DevOps maduro y herramientas de automatización sofisticadas. Mantener consistencia de datos entre servicios es un desafío. La latencia de red añade overhead. Depurar errores que cruzan múltiples servicios es complejo. Y los costes en infraestructura y personal son mayores. Por eso la recomendación es: no empezar con microservicios.

---

## 4.4. Arquitectura Serverless

Note: La arquitectura serverless es la más reciente y revolucionaria. Permite ejecutar código sin gestionar servidores. El proveedor cloud se encarga de toda la infraestructura. Solo subís funciones que responden a eventos. Es ideal para cargas de trabajo intermitentes o impredecibles. Veamos sus características, ventajas y desventajas.


### Sin Servidores

**El proveedor gestiona la infraestructura**

- Cero gestión de servidores
- Escalado automático completo
- Pago solo por ejecución real
- Arquitectura orientada a eventos
- Funciones efímeras

Note: Serverless no significa sin servidores, sino sin gestión de servidores. El proveedor cloud (AWS, Azure, Google) se encarga de toda la infraestructura. Vosotros solo subís código en forma de funciones. El escalado es completamente automático: si llegan mil peticiones simultáneas, se crean mil instancias. Y solo pagáis por los milisegundos que realmente se ejecuta vuestro código. Es event-driven: las funciones responden a eventos.


### Servicios Populares

**Plataformas serverless principales**

- **AWS Lambda**: El pionero y más popular
- **Azure Functions**: Integrado con Azure
- **Google Cloud Functions**: Ecosistema Google
- **Cloudflare Workers**: Edge computing

Note: AWS Lambda fue el pionero y sigue siendo el más usado. Permite ejecutar código sin gestionar servidores. Azure Functions se integra perfectamente con el ecosistema Microsoft. Google Cloud Functions ofrece el poder de la infraestructura de Google. Cloudflare Workers ejecuta funciones en el edge, cerca del usuario final. Todos comparten el mismo modelo: subes código, pagas por uso, escalado automático.


### Ventajas y Desventajas I

**Cuándo usar serverless**

✅ **Ventajas:**
- Costes optimizados (pago por uso)
- Sin mantenimiento de infraestructura
- Escalado automático perfecto

Note: Serverless es perfecto para cargas de trabajo intermitentes o impredecibles. Si tenéis un servicio que se usa esporádicamente, serverless es ideal: solo pagáis cuando se usa. No os preocupáis de servidores, parches, escalado. Pero tiene desventajas: quedáis atados al proveedor, hay latencia inicial en funciones que llevan tiempo sin ejecutarse, y si el uso es muy alto y constante, puede salir más caro que servidores dedicados. Es ideal para microservicios específicos, no para aplicaciones enteras.


### Ventajas y Desventajas II

**Cuándo usar serverless**

❌ **Desventajas:**
- Vendor lock-in fuerte
- Cold starts (latencia inicial)
- Límites de ejecución
- Costes impredecibles con mucho uso

Note: Serverless es perfecto para cargas de trabajo intermitentes o impredecibles. Si tenéis un servicio que se usa esporádicamente, serverless es ideal: solo pagáis cuando se usa. No os preocupáis de servidores, parches, escalado. Pero tiene desventajas: quedáis atados al proveedor, hay latencia inicial en funciones que llevan tiempo sin ejecutarse, y si el uso es muy alto y constante, puede salir más caro que servidores dedicados. Es ideal para microservicios específicos, no para aplicaciones enteras.

---

## 4.5. Comparativa de Arquitecturas

Nota: Ahora que hemos visto las principales arquitecturas web, es hora de compararlas. Cada una tiene sus pros y contras. No hay una arquitectura "mejor": la elección depende del contexto del proyecto, el equipo, los requisitos de escalabilidad, y los recursos disponibles. Veamos una tabla resumen y cuándo elegir cada una.


### Tabla Resumen

| Aspecto       | Monolito    | Capas       | Microservicios  | Serverless    |
|---------------|-------------|-------------|-----------------|---------------|
| Complejidad   | 🟢 Baja     | 🟡 Media    | 🔴 Alta         | 🟡 Media      |
| Escalabilidad | 🔴 Limitada | 🟡 Buena    | 🟢 Excelente    | 🟢 Automática |
| Mantenimiento | 🔴 Complejo | 🟡 Moderado | 🟢 Ágil         | 🟢 Mínimo     |
| Coste         | 🟢 Bajo     | 🟡 Moderado | 🔴 Alto         | 🟡 Variable   |
<!-- .element.table: style="font-size:75%;" -->

Note: Esta tabla resume las diferencias clave. Los monolitos son simples pero escalan mal. Las capas mejoran la organización pero siguen siendo monolitos. Los microservicios ofrecen máxima flexibilidad pero alta complejidad. Serverless minimiza operaciones pero puede ser costoso con mucho uso. No hay una arquitectura "mejor": la elección depende del tamaño del proyecto, del equipo, de los requisitos de escalabilidad, y de los recursos disponibles.


### ¿Cuál Elegir?

**Depende del contexto**

- **Monolito**: Proyectos pequeños, MVPs, equipos pequeños
- **Capas**: Aplicaciones empresariales tradicionales
- **Microservicios**: Aplicaciones grandes y complejas
- **Serverless**: Funcionalidades específicas, cargas variables

Note: La pregunta del millón: ¿cuál elegir? Para proyectos pequeños y MVPs, un monolito bien diseñado es perfecto. Para aplicaciones empresariales medianas con requisitos claros, arquitectura de capas es ideal. Para organizaciones grandes con aplicaciones complejas y equipos múltiples, microservicios. Y serverless es perfecto para funcionalidades específicas o cargas de trabajo variables. Y recordad: podéis combinarlas. Un monolito para el core, algunos microservicios para funciones específicas, y funciones serverless para tareas puntuales.

---

## 5. Patrón MVC

Note: El patrón Modelo-Vista-Controlador (MVC) es uno de los patrones de diseño más influyentes en el desarrollo web. Introducido en los años 70, sigue siendo relevante hoy en día. MVC separa la aplicación en tres componentes principales, cada uno con responsabilidades claras. Esta separación facilita el mantenimiento, la escalabilidad y la reutilización del código.


### Modelo-Vista-Controlador

**Separación de responsabilidades clásica**

- **Modelo**: Datos y lógica de negocio
- **Vista**: Presentación al usuario
- **Controlador**: Coordinador entre Modelo y Vista

Note: El patrón MVC es fundamental en desarrollo web y ha sido usado durante décadas. Separa la aplicación en tres componentes con responsabilidades claras. El Modelo encapsula los datos y la lógica de negocio. La Vista se encarga de presentar información al usuario. Y el Controlador coordina entre ambos: recibe acciones del usuario, las procesa con el Modelo, y selecciona la Vista apropiada. Esta separación facilita mantenimiento, testing y reutilización.


### Componente: Modelo

**El corazón de los datos**

- Encapsula datos de la aplicación
- Contiene lógica de negocio
- Gestiona acceso a base de datos
- Notifica cambios a las Vistas
- Independiente de la presentación

Note: El Modelo es el corazón de la aplicación. Contiene todos los datos y las reglas de negocio. Por ejemplo, en una tienda online, el Modelo de Producto tendría atributos como nombre, precio, stock, y métodos como calcularDescuento o verificarDisponibilidad. El Modelo accede a la base de datos para persistir y recuperar información. Y cuando cambia, notifica a las Vistas registradas para que se actualicen. Crucialmente, el Modelo no sabe nada sobre cómo se presenta: es completamente independiente de la UI.


### Componente: Vista

**La presentación**

- Responsable de la UI
- Renderiza datos del Modelo
- Múltiples vistas para el mismo Modelo
- Sin lógica de negocio
- Reacciona a cambios del Modelo

Note: La Vista se encarga exclusivamente de presentar información al usuario. Toma datos del Modelo y los renderiza en HTML, JSON, o el formato que sea necesario. Podéis tener múltiples Vistas para el mismo Modelo: una versión web, una móvil, una para API. La Vista no contiene lógica de negocio: solo presenta. Cuando el Modelo cambia, la Vista se actualiza automáticamente. Esta separación permite cambiar completamente el diseño sin tocar la lógica de negocio.


### Componente: Controlador

**El coordinador**

- Gestiona peticiones del usuario
- Interpreta acciones
- Solicita datos al Modelo
- Selecciona la Vista apropiada
- Coordina el flujo de la aplicación

Note: El Controlador es el intermediario que coordina todo. Recibe las peticiones del usuario: un clic, un formulario enviado, una URL visitada. Interpreta qué quiere hacer el usuario, valida los datos de entrada, y decide qué operación ejecutar. Luego solicita al Modelo los datos necesarios o que realice una actualización. Finalmente, selecciona qué Vista usar para mostrar la respuesta. El Controlador es el cerebro que coordina Modelo y Vista.


### Flujo de Ejecución MVC

**¿Cómo trabajan juntos?**

1. Usuario interactúa con la Vista
2. Vista notifica al Controlador
3. Controlador procesa la petición
4. Controlador solicita al Modelo
5. Modelo ejecuta lógica de negocio
6. Modelo notifica cambios
7. Controlador selecciona Vista
8. Vista renderiza respuesta

Note: Veamos el flujo completo con un ejemplo: un usuario hace clic en "Añadir al carrito". La Vista notifica este evento al Controlador. El Controlador interpreta la acción, valida que el producto existe, y le pide al Modelo que lo añada al carrito. El Modelo verifica disponibilidad, actualiza el carrito en la BD, y notifica el cambio. El Controlador selecciona la Vista de "Carrito actualizado". La Vista renderiza el carrito con el nuevo producto. Todo fluye de forma organizada y cada componente cumple su rol.


### MVC en Web Tradicional

**Renderizado en servidor**

- Servidor genera HTML completo
- Cada acción recarga la página
- No es reactivo
- Mayor latencia
- Tecnologías: Laravel, Django, Rails

Note: En aplicaciones web tradicionales, el servidor hace todo el trabajo pesado. Cuando hacéis una petición, el servidor ejecuta el Controlador, consulta el Modelo, genera el HTML completo con la Vista, y lo envía al navegador. Cada interacción requiere una petición al servidor y la página se recarga completamente. No es reactivo como las SPAs modernas. Frameworks como Laravel, Django o Rails implementan este patrón perfectamente. Aunque menos moderno, sigue siendo válido para muchas aplicaciones.


### MVC Moderno: SPAs

**JavaScript en el navegador**

- Gran parte del MVC en cliente
- Servidor proporciona datos (JSON)
- Interactividad sin recargas
- Frameworks: Angular, Vue, React
- Renderizado reactivo

Note: Las Single Page Applications modernas cambiaron el juego. Ahora gran parte de la lógica MVC se ejecuta en el navegador con JavaScript. El servidor principalmente proporciona APIs que devuelven datos en JSON, no HTML completo. La aplicación puede actualizar partes de la página sin recargarla entera, ofreciendo una experiencia más fluida. Frameworks como Angular implementan MVVM, Vue.js y React tienen aproximaciones similares. Es más complejo pero ofrece mejor experiencia de usuario.

---

## 6. Principios SOLID

Note: Los principios SOLID son cinco reglas fundamentales para diseñar software orientado a objetos de calidad. Introducidos por Robert C. Martin, estos principios ayudan a crear código que es fácil de mantener, extender y probar. Aunque se aplican principalmente en programación orientada a objetos, los conceptos subyacentes son útiles en cualquier paradigma de programación.


### Los Cinco Pilares

**Diseño de software de calidad**

- **S**: Single Responsibility Principle
- **O**: Open/Closed Principle
- **L**: Liskov Substitution Principle
- **I**: Interface Segregation Principle
- **D**: Dependency Inversion Principle

Note: Los principios SOLID son cinco reglas fundamentales para diseñar software orientado a objetos de calidad. Son guías, no leyes absolutas, pero seguirlas mejora significativamente la mantenibilidad, extensibilidad y testabilidad del código. Los veremos uno por uno. Estos principios aplican no solo a clases individuales, sino también a arquitecturas completas: un microservicio debe tener una sola responsabilidad, las interfaces deben estar bien segregadas, etc.


### S: Responsabilidad Única

**Una clase, una razón para cambiar**

- Cada clase debe enfocarse en una funcionalidad
- Facilita mantenimiento
- Reduce acoplamiento
- Hace cambios más seguros

**Ejemplo:** `UserRepository` solo accede a datos de usuarios, no valida contraseñas ni envía emails

Note: El primer principio dice que una clase debe tener una, y solo una, razón para cambiar. Si tenéis una clase User que gestiona datos, valida contraseñas, envía emails y genera reportes, tiene cuatro razones para cambiar. Es mejor separarla: UserRepository para datos, PasswordValidator para validación, EmailService para emails. Cada clase hace una cosa y la hace bien. Esto facilita encontrar bugs, hacer cambios, y escribir tests.


### O: Abierto/Cerrado

**Abierto para extensión, cerrado para modificación**

- Añadir funcionalidad sin modificar código existente
- Logrado mediante abstracción e interfaces
- Reduce riesgo de bugs
- Facilita evolución del código

**Ejemplo:** Sistema de pagos que acepta nuevos métodos sin modificar el procesador

Note: El principio Abierto/Cerrado es poderoso: deberíais poder añadir nueva funcionalidad sin modificar código que ya funciona. Se logra usando interfaces y herencia. Por ejemplo, si tenéis un procesador de pagos, en lugar de tener un if para cada tipo de pago (tarjeta, PayPal, transferencia), definís una interfaz PaymentMethod y cada tipo la implementa. Para añadir criptomonedas, solo creáis CryptoPayment implementando la interfaz. El procesador no cambia.


### L: Sustitución de Liskov

**Las subclases deben ser intercambiables**

- Objetos de subclases sustituyen a los de superclase
- Sin romper la funcionalidad del programa
- Garantiza consistencia de comportamiento
- Fundamental para polimorfismo correcto

**Ejemplo:** Si `Pinguino` hereda de `Ave`, no debería tener método `volar()` porque no vuela

Note: El principio de Liskov dice que si una clase B hereda de A, debería poder usar B donde se usa A sin problemas. El ejemplo clásico: si tenéis una clase Ave con método volar(), y Pingüino hereda de Ave, hay un problema: los pingüinos no vuelan. Si alguien llama volar() en un Pingüino, ¿qué pasa? Lanza excepción? Hace nada? Viola el contrato de Ave. Mejor tener Volador como interfaz separada que solo implementan aves que vuelan.


### I: Segregación de Interfaces

**Interfaces específicas, no generales**

- Muchas interfaces pequeñas mejor que una grande
- Clientes no dependen de métodos que no usan
- Facilita implementación
- Reduce impacto de cambios

**Ejemplo:** `IWorkable` e `IFeedable` en lugar de `IWorker` con todos los métodos

Note: El principio de segregación dice: mejor tener muchas interfaces específicas que una gorda con todo. Si tenéis una interfaz IWorker con métodos work(), eat(), sleep(), ¿qué pasa con un Robot que hereda IWorker? No come ni duerme. Mejor tener IWorkable con work(), IFeedable con eat(), ISleepable con sleep(). Cada clase implementa solo lo que necesita. Interfaces pequeñas y cohesivas son más flexibles y fáciles de implementar.


### D: Inversión de Dependencias

**Depender de abstracciones, no de concreciones**

- Módulos de alto nivel no dependen de bajo nivel
- Ambos dependen de abstracciones
- Facilita cambio de implementaciones
- Mejora testabilidad (inyección de dependencias)

**Ejemplo:** Servicio depende de `IDatabase`, no de `MySQLDatabase` concreta

Note: El último principio es crucial: no deberíais depender de implementaciones concretas, sino de abstracciones. Un servicio de usuarios no debería depender directamente de MySQLDatabase. Debería depender de una interfaz IDatabase. Luego podéis inyectar MySQLDatabase, PostgreSQLDatabase o MockDatabase para tests. Esto hace el código flexible: cambiar de base de datos no requiere modificar el servicio. Y facilita testing: inyectáis un mock en lugar de una BD real.


### SOLID en la Práctica

**¿Cuándo aplicarlos?**

- No son dogmas, son guías
- Aplicar con criterio, no religiosamente
- En microservicios: S es crítico
- En capas: D es fundamental
- En cualquier arquitectura: O facilita extensibilidad

Note: Los principios SOLID son guías, no leyes absolutas. No debéis aplicarlos ciegamente en todo momento. Usad criterio. En microservicios, el principio S es crítico: cada servicio debe tener una responsabilidad única. En arquitecturas de capas, D es fundamental para desacoplar capas. En cualquier arquitectura, O facilita añadir funcionalidad sin romper lo existente. Con la experiencia aprenderéis cuándo aplicar cada principio y cuándo no vale la pena la abstracción extra.

---

## 7. Otros Patrones de Diseño

Note: Además de SOLID, existen docenas de patrones de diseño catalogados. Estos patrones son soluciones probadas a problemas comunes en el diseño de software. Se dividen en tres categorías principales: creacionales, estructurales y de comportamiento. Cada categoría aborda diferentes aspectos del diseño orientado a objetos. Veamos un resumen de los más importantes.


### Categorías Principales

**Soluciones a problemas comunes**

- **Creacionales**: Cómo se crean objetos
  - Singleton, Factory, Builder
  
- **Estructurales**: Cómo se componen objetos
  - Adapter, Decorator, Facade
  
- **Comportamiento**: Cómo interactúan objetos
  - Observer, Strategy, Command

Note: Además de SOLID, existen docenas de patrones de diseño catalogados. Se dividen en tres categorías. Los creacionales tratan sobre la creación de objetos: Singleton garantiza una única instancia, Factory delega la creación a subclases, Builder construye objetos complejos paso a paso. Los estructurales organizan la composición: Adapter convierte interfaces, Decorator añade funcionalidad dinámicamente, Facade simplifica subsistemas complejos. Los de comportamiento gestionan interacciones: Observer notifica cambios, Strategy encapsula algoritmos, Command encapsula peticiones.


### Patrones Arquitectónicos

**Estructuras de alto nivel**

- **MVC**: Modelo-Vista-Controlador (ya visto)
- **MVVM**: Model-View-ViewModel (frontend moderno)
- **Microservicios**: Servicios pequeños independientes
- **Event-Driven**: Arquitectura basada en eventos
- **Layered**: Arquitectura de capas

Note: Los patrones arquitectónicos operan a nivel de toda la aplicación, no de clases individuales. MVC ya lo hemos visto en detalle. MVVM es común en frameworks frontend como Vue o Angular: el ViewModel hace de intermediario reactivo entre Model y View. Microservicios son un patrón arquitectónico completo. Event-Driven estructura la aplicación en torno a eventos y reacciones. Layered organiza en capas horizontales. En proyectos reales, combinaréis múltiples patrones: arquitectura de microservicios, cada uno con MVC, usando patrones como Observer y Factory.

---

## 8. Resumen

Note: Hemos cubierto mucho terreno hoy: desde los fundamentos del modelo cliente-servidor hasta principios avanzados de diseño como SOLID. Estas arquitecturas no son solo teoría: las usaréis en cada proyecto que hagáis. Recordad que no hay una arquitectura "perfecta", solo la más adecuada para cada situación. Vamos a repasar lo fundamental y las decisiones clave que debéis considerar al elegir una arquitectura.


### Conceptos Clave

**Lo que hemos aprendido**

1. Cliente-Servidor: la base de la web
2. Evolución: de Web 1.0 a Web 4.0
3. Arquitecturas: monolito, capas, microservicios, serverless
4. MVC: separación Modelo-Vista-Controlador
5. SOLID: principios de diseño de calidad

Note: Vamos a repasar lo fundamental. El modelo Cliente-Servidor es la base de todas las aplicaciones web, con sus ventajas de centralización y escalabilidad. La web ha evolucionado de páginas estáticas a aplicaciones inteligentes distribuidas. Cada arquitectura tiene su lugar: monolitos para proyectos pequeños, microservicios para aplicaciones complejas, serverless para funciones específicas. MVC separa responsabilidades para facilitar mantenimiento. Y SOLID nos da principios para escribir código de calidad.


### Decisiones Arquitectónicas

**Factores a considerar**

- Tamaño del proyecto y del equipo
- Requisitos de escalabilidad
- Complejidad del dominio
- Recursos disponibles (dinero, tiempo, conocimiento)
- Posibilidad de evolucionar la arquitectura

Note: No existe la arquitectura perfecta universal. La elección depende de múltiples factores. Un equipo pequeño con un proyecto simple debe empezar con un monolito bien diseñado. Una organización grande con aplicación compleja puede beneficiarse de microservicios, pero solo si tienen la madurez DevOps necesaria. Considerad los recursos disponibles, no solo técnicos sino también de conocimiento. Y recordad: la arquitectura puede evolucionar. Muchos proyectos exitosos empiezan como monolitos y gradualmente extraen microservicios cuando es necesario.


### Próximos Pasos

**Aplicando lo aprendido**

- Protocolo HTTP/HTTPS en detalle
- APIs REST y servicios web
- Despliegue de diferentes arquitecturas
- Escalabilidad y alta disponibilidad
- Casos prácticos con Docker y Kubernetes

Note: Con estos fundamentos arquitectónicos, estáis preparados para las próximas unidades. Profundizaremos en cómo se comunican estas arquitecturas mediante HTTP y APIs REST. Veremos cómo desplegar monolitos, microservicios y aplicaciones serverless. Estudiaremos técnicas de escalabilidad y alta disponibilidad. Y lo pondremos todo en práctica con Docker para contenerización y Kubernetes para orquestación. Todo lo que hemos visto hoy es la base teórica que aplicaréis en despliegues reales.

---

## ¿Preguntas?

### Contacto y Recursos

- Documentación del curso
- Repositorio de prácticas
- Próxima unidad: Protocolo HTTP

**¡Gracias por vuestra atención!**

Note: Perfecto, hemos cubierto mucho contenido hoy: desde los fundamentos del modelo cliente-servidor hasta principios avanzados de diseño. Estas arquitecturas no son solo teoría: las usaréis en cada proyecto que hagáis. Recordad que no hay una arquitectura perfecta, solo la más adecuada para cada situación. Si tenéis dudas sobre cuándo usar cada arquitectura, o sobre cómo aplicar SOLID en vuestros proyectos, este es el momento de preguntar. En la próxima unidad nos sumergiremos en HTTP y HTTPS, los protocolos que permiten que estas arquitecturas se comuniquen.
