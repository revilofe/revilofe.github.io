# DAW-U3.5 - Funcionamiento de una Web Dinámica

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

1. La evolución: de lo estático a lo dinámico
2. Páginas web estáticas
3. Páginas web dinámicas
4. Cómo funciona una página web dinámica

## Índice II

5. Tecnologías de generación web
6. PHP: el lenguaje de la web
7. Python: elegancia y versatilidad
8. Java: robustez empresarial
9. Node.js: JavaScript en todas partes
10. Comparativa de tecnologías

---

## 1. La evolución: de lo estático a lo dinámico

Note: La web no nació siendo dinámica. Cuando Tim Berners-Lee creó la primera página web en 1991, era simplemente HTML estático. La evolución hacia páginas dinámicas responde a necesidades de personalización e interactividad que surgieron cuando la web empezó a usarse para algo más que documentos académicos. Hoy veremos cómo generamos contenido que se adapta a cada usuario en tiempo real.


### 1.1. El contexto histórico

**De documentos académicos a aplicaciones complejas**

- Años 90: páginas estáticas simples
- Mediados 90s: surge la necesidad de personalización
- Hoy: aplicaciones web complejas y dinámicas
- Futuro: serverless, edge computing

Note: En los años 90, la web era un conjunto de documentos estáticos interconectados. Pero pronto surgieron necesidades: ¿cómo mostrar contenido personalizado? ¿Cómo procesar formularios? ¿Cómo crear tiendas online? Estas preguntas llevaron al desarrollo de tecnologías de servidor que ejecutan código y generan páginas dinámicamente.


### 1.2. La pregunta fundamental

**¿Cómo se genera el contenido que vemos?**

- ¿De dónde sale tu feed personalizado?
- ¿Cómo se actualiza tu saldo bancario?
- ¿Por qué cada usuario ve contenido diferente?
- La respuesta: **generación dinámica**

Note: Esta es la pregunta clave que responderemos hoy. Cuando entráis en vuestras redes sociales, cada uno ve contenido diferente. Vuestro feed no existe como archivo en el servidor esperándoos, se construye en el momento exacto en que lo solicitáis. Ese proceso de construcción bajo demanda es la esencia de las páginas dinámicas.

---

## 2. Páginas web estáticas

Note: Antes de entender lo dinámico, debemos comprender lo estático. Las páginas estáticas fueron el origen de la web y aún hoy tienen su lugar. Son simples, rápidas y seguras, pero tienen limitaciones evidentes.


### 2.1. ¿Qué es una página estática?

**Contenido fijo predefinido**

- Archivos HTML guardados en el servidor
- El mismo contenido para todos los usuarios
- Sin procesamiento, solo lectura y envío
- Como un libro impreso: fijo e inmutable

Note: Una página estática es simplemente un archivo HTML que existe en el servidor. Cuando un usuario la pide, el servidor lee ese archivo del disco y lo envía. No hay procesamiento, no hay generación, no hay personalización. Todos reciben exactamente el mismo contenido. Es como tener libros impresos: el texto es el que es.


### 2.2. El proceso simple

**Flujo de una página estática**

1. Usuario solicita `index.html`
2. Servidor lee el archivo del disco
3. Servidor envía el contenido
4. Todos reciben lo mismo

Note: El flujo es extremadamente simple. El navegador pide un archivo, el servidor lo lee y lo envía. No hay intermediarios, no hay ejecución de código, no hay consultas a bases de datos. Esta simplicidad es su mayor ventaja: son rapidísimas. Pero también su mayor limitación: son completamente inflexibles.


### 2.3. Características clave

**Ventajas de las páginas estáticas**

- ✅ Velocidad excepcional
- ✅ Seguridad máxima
- ✅ Hosting económico
- ✅ Escalabilidad perfecta
- ✅ SEO excelente

Note: Las páginas estáticas tienen ventajas importantes que las hacen valiosas aún hoy. Son las más rápidas posibles porque no hay procesamiento. Son extremadamente seguras porque no ejecutan código. El hosting es barato, incluso gratuito. Pueden servir millones de usuarios sin problemas. Los buscadores las indexan fácilmente. Por eso sitios como blogs o portfolios simples suelen ser estáticos.


### 2.4. Las limitaciones críticas

**Por qué necesitamos algo más**

- ❌ Sin personalización
- ❌ Sin interacción real
- ❌ Actualización manual y tediosa
- ❌ Sin datos dinámicos
- ❌ Funcionalidad muy limitada

Note: Pero las limitaciones son obvias. Todos ven lo mismo: no puedes mostrar el nombre del usuario ni su saldo bancario. No hay login, no hay formularios funcionales, no hay comentarios. Cada cambio requiere editar archivos manualmente y subirlos. No puedes conectar con bases de datos. No puedes crear tiendas online, redes sociales, o aplicaciones complejas.


### 2.5. Ejemplo de código estático

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Mi Portfolio</title>
</head>
<body>
    <h1>Bienvenidos a mi portfolio</h1>
    <p>Soy un desarrollador con 5 años de experiencia...</p>
    <ul>
        <li>Aplicación de gestión</li>
        <li>Tienda online</li>
        <li>Blog personal</li>
    </ul>
</body>
</html>
```

Note: Este es un ejemplo típico de página estática. Es HTML puro. El nombre, los años de experiencia, los proyectos, todo está escrito directamente en el código. Si queréis cambiar "5 años" por "6 años", tenéis que editar el HTML manualmente y volver a subirlo. Imaginad mantener así una web con miles de páginas o que cambia constantemente. Imposible.

---

## 3. Páginas web dinámicas

Note: Las páginas dinámicas revolucionaron la web. Permitieron crear aplicaciones reales, no solo documentos. La clave es que se generan mediante código que se ejecuta en el servidor, lo que abre posibilidades infinitas.


### 3.1. ¿Qué es una página dinámica?

**Contenido generado en el momento**

- Se construye cuando se solicita
- El servidor ejecuta código
- Puede consultar bases de datos
- Personalizada para cada situación

Note: Una página dinámica no existe como archivo. Se genera en el momento exacto en que la pedís. El servidor ejecuta código (PHP, Python, Java, etc.) que construye el HTML específicamente para esa petición. Ese código puede consultar bases de datos, hacer cálculos, tomar decisiones y personalizar el contenido. Es como un chef que prepara cada plato al momento según las preferencias del cliente.


### 3.2. El cambio de paradigma

**De archivos a programación**

- No se leen archivos, se ejecuta código
- El código toma decisiones
- Acceso a bases de datos
- Personalización por usuario
- Procesamiento de formularios

Note: El cambio fundamental es que pasamos de simplemente leer archivos a ejecutar programas. Este código puede consultar qué usuario está logueado, buscar sus datos en la base de datos, calcular recomendaciones personalizadas, procesar el formulario que acaba de enviar y generar HTML único para él. Es programación completa en el servidor.


### 3.3. Comparación visual

**Estático vs Dinámico**

**Estático:**
```html
<h1>Bienvenido a nuestra web</h1>
<p>Últimas noticias del 15 de noviembre</p>
```

**Dinámico:**
```php
<h1>Bienvenido, <?php echo $nombreUsuario; ?></h1>
<p>Últimas noticias del <?php echo date('d/m/Y'); ?></p>
```

Note: Aquí vemos la diferencia claramente. En la versión estática, el HTML está escrito directamente. En la dinámica, hay código PHP que se ejecuta en el servidor. Ese código obtiene el nombre del usuario de la sesión y la fecha actual, e inserta esos valores en el HTML. Cada usuario verá su propio nombre y la fecha actual. El navegador recibe HTML normal, pero fue generado dinámicamente.


### 3.4. Características fundamentales

**Capacidades de las páginas dinámicas**

- Contenido variable por usuario
- Interactividad real (login, formularios)
- Conexión con bases de datos
- Lógica de negocio compleja
- Actualización sencilla

Note: Las páginas dinámicas tienen capacidades que las estáticas no pueden soñar. Pueden mostrar contenido diferente a cada usuario. Pueden procesar formularios y guardar datos. Pueden conectarse a bases de datos para almacenar y recuperar información. Pueden ejecutar lógica de negocio: calcular precios, aplicar descuentos, verificar permisos. Y lo mejor: actualizar datos en la base de datos automáticamente actualiza todo el sitio.

---

## 4. Cómo funciona una página web dinámica

Note: Ahora viene lo fascinante: entender el proceso completo. Desde que hacéis clic en un enlace hasta que veis la página, pasan muchas cosas. Vamos a desgranar cada paso para que comprendáis exactamente qué ocurre en esos milisegundos.


### 4.1. Los actores del proceso

**Quiénes participan**

1. **Cliente (navegador)**: solicita y renderiza
2. **Servidor web**: recibe peticiones HTTP
3. **Módulo de ejecución**: ejecuta código
4. **Base de datos**: almacena información
5. **Sistema de archivos**: guarda scripts

Note: Primero identifiquemos a los participantes. El navegador del usuario hace peticiones y muestra resultados. El servidor web (Apache, Nginx) recibe esas peticiones y decide qué hacer. El módulo de ejecución (PHP-FPM, Gunicorn, Tomcat) ejecuta el código dinámico. La base de datos responde a consultas. Y el sistema de archivos almacena los scripts y recursos. Todos colaboran en cada petición.


### 4.2. Paso 1: El usuario solicita

**Iniciando el proceso**

```
Usuario hace clic: https://redsocial.com/perfil/ana
```

**Petición HTTP:**
```http
GET /perfil/ana HTTP/1.1
Host: redsocial.com
Cookie: session_id=abc123
```

Note: Todo empieza cuando el usuario hace clic. El navegador envía una petición HTTP GET al servidor. Incluye la URL solicitada, el host, cookies de sesión, y otros headers. Esta petición viaja por Internet hasta el servidor web en el puerto 80 o 443.


### 4.3. Paso 2: El servidor recibe

**Tomando decisiones**

- Servidor web recibe la petición
- Analiza la URL: `/perfil/ana`
- ¿Es estático o dinámico?
  - `/imagen.jpg` → estático, servir directamente
  - `/perfil/ana` → dinámico, necesita procesamiento

Note: El servidor web analiza la petición. Si fuera un archivo estático como una imagen, simplemente lo leería y enviaría. Pero `/perfil/ana` es una página dinámica. El servidor web sabe que no puede manejarla solo, necesita ayuda del módulo de ejecución correspondiente.


### 4.4. Paso 3: Delegación al módulo

**Pasando el testigo**

- Servidor identifica la tecnología
- PHP → mod_php / PHP-FPM
- Python → Gunicorn / uWSGI
- Java → Tomcat
- Node.js → proceso Node

Note: El servidor web delega al módulo apropiado según la configuración. Si es PHP, llama a PHP-FPM. Si es Python, a Gunicorn. Si es Java, redirige a Tomcat. Le dice: "Ejecuta el script en /perfil/ana y dame el resultado". Ahora el control pasa al código de aplicación.


### 4.5. Paso 4: Ejecución del código (I)

**El código toma control**

```php
// 1. Obtener parámetros
$username = $_GET['usuario']; // "ana"

// 2. Verificar sesión
if (!isset($_SESSION['usuario_id'])) {
    header('Location: /login');
    exit();
}
```

Note: El código dinámico comienza su ejecución. Primero obtiene el nombre de usuario de la URL. Luego verifica si el usuario actual está logueado consultando la sesión. Si no está logueado, le redirige a la página de login. Esta es lógica de negocio: tomar decisiones según condiciones.


### 4.5. Paso 4: Ejecución del código (II)

**Consultando datos**

```php
// 3. Conectar a base de datos
$db = new PDO('mysql:host=localhost;dbname=redsocial');

// 4. Consultar usuario
$stmt = $db->prepare('SELECT * FROM usuarios WHERE username = ?');
$stmt->execute([$username]);
$usuario = $stmt->fetch();

// 5. Consultar publicaciones
$stmt = $db->prepare('SELECT * FROM posts WHERE usuario_id = ?');
$posts = $stmt->fetchAll();
```

Note: Ahora viene la parte crucial: consultar la base de datos. El código conecta a MySQL y ejecuta consultas SQL. Primero busca los datos del usuario Ana. Luego busca sus publicaciones recientes. Estas consultas pueden tardar milisegundos o más, dependiendo de la complejidad y los índices.


### 4.5. Paso 4: Ejecución del código (III)

**Generando HTML**

```php
<!DOCTYPE html>
<html>
<head>
    <title>Perfil de <?php echo $usuario['nombre']; ?></title>
</head>
<body>
    <h1><?php echo $usuario['nombre']; ?></h1>
    <p><?php echo $usuario['bio']; ?></p>
    <?php foreach ($posts as $post): ?>
        <article>
            <p><?php echo $post['contenido']; ?></p>
        </article>
    <?php endforeach; ?>
</body>
</html>
```

Note: Finalmente, el código genera el HTML mezclando estructura estática con datos dinámicos. Inserta el nombre del usuario, su biografía, y recorre sus publicaciones creando un artículo por cada una. El resultado es un documento HTML completo y único para esta petición específica.


### 4.6. Paso 5: Consultas a base de datos

**El rol crucial de la BD**

```sql
-- Obtener usuario
SELECT * FROM usuarios WHERE username = 'ana';

-- Obtener publicaciones
SELECT * FROM posts 
WHERE usuario_id = 42 
ORDER BY fecha DESC 
LIMIT 10;
```

Note: Las consultas a la base de datos son críticas. La BD busca en sus tablas, aplica filtros, ordena resultados y devuelve datos. El rendimiento depende de índices, optimización de consultas y carga del servidor. Una consulta mal optimizada puede hacer que la página tarde segundos en lugar de milisegundos.


### 4.7. Paso 6: Respuesta HTTP

**Enviando el resultado**

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8
Set-Cookie: session_id=abc123

<!DOCTYPE html>
<html>
<head>
    <title>Perfil de Ana García</title>
...
```

Note: El módulo PHP devuelve el HTML generado al servidor web, que construye la respuesta HTTP completa. Incluye el código de estado (200 OK), headers como Content-Type, cookies, y el body con el HTML. Esta respuesta viaja de vuelta al navegador del usuario.


### 4.8. Paso 7: Renderizado en el navegador

**El navegador toma control**

1. Recibe la respuesta HTTP
2. Parsea el HTML
3. Construye el DOM
4. Descarga CSS, JS, imágenes
5. Renderiza visualmente
6. Ejecuta JavaScript del cliente

Note: El navegador recibe el HTML. Para él, no hay diferencia entre una página estática y una dinámica: ambas son HTML. Parsea el documento, construye el árbol DOM, descarga recursos adicionales, aplica estilos CSS, ejecuta JavaScript del cliente y finalmente renderiza la página visualmente. El usuario ve su página personalizada sin saber todo lo que acaba de ocurrir.


### 4.9. Diferencias en tiempo de respuesta

**El coste de la funcionalidad**

**Página estática:**
```
Petición → Leer archivo → Enviar
Tiempo: 5-20 ms
```

**Página dinámica:**
```
Petición → Código → BD → Generar HTML → Enviar
Tiempo: 50-500 ms
```

Note: Las páginas dinámicas son más lentas, no hay vuelta de hoja. Pero esta diferencia es aceptable porque la funcionalidad obtenida lo justifica. Los usuarios esperan algo de delay para operaciones complejas. Además, con buenas prácticas (caché, consultas optimizadas, código eficiente), podemos minimizar este tiempo. El hardware moderno también ayuda: 100-200ms es imperceptible para el usuario.

---

## 5. Tecnologías de generación web

Note: Ahora que entendemos el proceso, exploremos las tecnologías que lo hacen posible. A lo largo de la historia, han surgido múltiples lenguajes y frameworks. Cada uno tiene sus fortalezas y casos de uso ideales.


### 5.1. Panorama general

**Las principales familias**

1. **PHP**: WordPress, Facebook inicial
2. **Python**: Instagram, Spotify
3. **Java**: aplicaciones empresariales
4. **JavaScript/Node.js**: Netflix, LinkedIn
5. **Ruby**: GitHub, Shopify
6. **C#/ASP.NET**: entornos Microsoft

Note: Todas estas tecnologías resuelven el mismo problema: ejecutar código en el servidor que genera HTML dinámicamente. La elección depende del equipo, requisitos del proyecto, ecosistema de librerías y preferencias. No hay una opción "mejor", sino opciones más adecuadas para cada contexto.

---

## 6. PHP: el lenguaje de la web

Note: PHP es sin duda el lenguaje más ubicuo en desarrollo web. A pesar de críticas ocasionales, PHP impulsa una parte masiva de Internet. Su diseño específico para la web lo hizo extremadamente accesible.


### 6.1. Por qué PHP tuvo éxito

**Diseño para la web**

- Creado específicamente para la web (1995)
- Código incrustado directamente en HTML
- Curva de aprendizaje suave
- Hosting universal y económico
- Ecosistema masivo

Note: PHP fue diseñado desde el principio para la web. Su propuesta era simple: permitir incrustar código directamente en HTML. Esto lo hizo extremadamente accesible para principiantes. Cualquier hosting ofrecía PHP. El ecosistema creció exponencialmente con WordPress, Drupal, y más recientemente Laravel. Esta ubicuidad lo convirtió en el rey de la web.


### 6.2. Ejemplo básico PHP

```php
<!DOCTYPE html>
<html>
<body>
    <h1>Hola Mundo desde PHP</h1>
    <?php
    $nombre = "Estudiante";
    $hora = date('H');
    
    if ($hora < 12) {
        $saludo = "Buenos días";
    } else {
        $saludo = "Buenas tardes";
    }
    
    echo "<p>$saludo, $nombre!</p>";
    ?>
</body>
</html>
```

Note: Este ejemplo muestra lo fundamental de PHP: mezclar HTML con código. Todo entre `<?php` y `?>` se ejecuta en el servidor. Aquí creamos variables, tomamos decisiones con if-else, y generamos HTML dinámicamente. El navegador solo recibe el HTML final, nunca ve el código PHP.


### 6.3. PHP moderno: Laravel

**Framework PHP actual**

```php
// Ruta
Route::get('/perfil/{username}', function ($username) {
    $usuario = Usuario::where('username', $username)->first();
    return view('perfil', ['usuario' => $usuario]);
});
```

```blade
<!-- Vista Blade -->
<h1>{{ $usuario->nombre }}</h1>
@foreach($usuario->posts as $post)
    <article>{{ $post->contenido }}</article>
@endforeach
```

Note: Laravel es el framework PHP más popular actualmente. Proporciona estructura, ORM para bases de datos, sistema de plantillas, routing, autenticación y mucho más. El código es mucho más limpio y mantenible que PHP puro. Blade es su motor de plantillas que permite sintaxis elegante para generar HTML.


### 6.4. Ventajas y desventajas de PHP

**Ventajas:**
- ✅ Hosting universal y económico
- ✅ Curva de aprendizaje suave
- ✅ Ecosistema enorme (WordPress, Laravel)
- ✅ Documentación exhaustiva

**Desventajas:**
- ❌ Inconsistencias históricas
- ❌ Rendimiento inferior a compilados
- ❌ Prácticas antiguas persisten

Note: PHP tiene ventajas claras: hosting barato, fácil de aprender, ecosistema gigantesco. Pero también desventajas: el lenguaje tiene inconsistencias por decisiones históricas, el rendimiento no es el mejor, y muchas prácticas antiguas e inseguras persisten en código legacy. Aun así, PHP moderno con Laravel es profesional y potente.

---

## 7. Python: elegancia y versatilidad

Note: Python se ha convertido en uno de los lenguajes más queridos para desarrollo web. Su sintaxis elegante y frameworks potentes como Django y Flask lo hacen ideal para aplicaciones complejas.


### 7.1. Django: batteries included

**Framework completo**

```python
# Modelo
class Usuario(models.Model):
    username = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    bio = models.TextField()

# Vista
def perfil(request, username):
    usuario = get_object_or_404(Usuario, username=username)
    posts = usuario.posts.all()[:10]
    return render(request, 'perfil.html', {
        'usuario': usuario,
        'posts': posts
    })
```

Note: Django es un framework "batteries included": viene con todo lo necesario. Define modelos que se mapean a tablas de base de datos. Las vistas son funciones que procesan peticiones y devuelven respuestas. Django maneja automáticamente migraciones, panel de administración, autenticación y más.


### 7.2. Plantilla Django

```django
<!DOCTYPE html>
<html>
<body>
    <h1>{{ usuario.nombre }}</h1>
    <p>@{{ usuario.username }}</p>
    <p>{{ usuario.bio }}</p>
    
    <h2>Publicaciones</h2>
    {% if posts %}
        {% for post in posts %}
            <article>
                <p>{{ post.contenido }}</p>
                <small>{{ post.fecha|timesince }} atrás</small>
            </article>
        {% endfor %}
    {% else %}
        <p>Sin publicaciones.</p>
    {% endif %}
</body>
</html>
```

Note: El sistema de plantillas de Django es potente. Usa `{{ variable }}` para mostrar valores y `{% tag %}` para lógica. Incluye filtros útiles como `timesince` que calcula tiempo transcurrido. La sintaxis es clara y segura: escapa HTML automáticamente para prevenir XSS.


### 7.3. Flask: el microframework

**Minimalista y flexible**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/perfil/<username>')
def perfil(username):
    usuario = Usuario.query.filter_by(username=username).first()
    posts = usuario.posts.limit(10).all()
    return render_template('perfil.html', 
                          usuario=usuario, 
                          posts=posts)

if __name__ == '__main__':
    app.run()
```

Note: Flask es el opuesto de Django: minimalista. Proporciona lo básico (routing, templates) y tú añades lo que necesites. Es perfecto para proyectos pequeños, microservicios, o cuando quieres control total. Más flexible pero requiere más decisiones del desarrollador.


### 7.4. Ventajas y desventajas de Python

**Ventajas:**
- ✅ Sintaxis limpia y legible
- ✅ Excelente para apps complejas
- ✅ Fuerte en ML e IA
- ✅ Gran ecosistema científico

**Desventajas:**
- ❌ Hosting menos común
- ❌ Rendimiento (aunque mejora con PyPy)
- ❌ GIL limita concurrencia

Note: Python brilla por su elegancia y potencia para aplicaciones complejas. Es especialmente fuerte si necesitáis machine learning o análisis de datos. Pero el hosting es menos común que PHP, el rendimiento no es óptimo, y el Global Interpreter Lock limita la concurrencia en CPython.

---

## 8. Java: robustez empresarial

Note: Java ha sido durante décadas la opción preferida para aplicaciones empresariales de gran escala. Su robustez, rendimiento y ecosistema maduro lo hacen ideal para sistemas críticos.


### 8.1. JSP: el enfoque clásico

**JavaServer Pages**

```jsp
<%@ page contentType="text/html;charset=UTF-8" %>
<!DOCTYPE html>
<html>
<body>
    <h1>Hola desde JSP</h1>
    <%
        String nombre = "Estudiante";
        int hora = LocalTime.now().getHour();
        String saludo = hora < 12 ? "Buenos días" : "Buenas tardes";
    %>
    <p><%= saludo %>, <%= nombre %>!</p>
    
    <ul>
    <%
        String[] langs = {"Java", "Python", "JavaScript"};
        for (int i = 0; i < langs.length; i++) {
            out.println("<li>" + langs[i] + "</li>");
        }
    %>
    </ul>
</body>
</html>
```

Note: JSP es el equivalente Java de PHP: código embebido en HTML. Usa `<% %>` para código Java y `<%= %>` para imprimir valores. Es más verboso que PHP pero aprovecha toda la potencia de Java y su ecosistema.


### 8.2. Spring Boot: framework moderno

**Arquitectura MVC**

```java
@Entity
public class Usuario {
    @Id
    private Long id;
    private String username;
    private String nombre;
    @OneToMany
    private List<Post> posts;
}

@Controller
public class PerfilController {
    @GetMapping("/perfil/{username}")
    public String perfil(@PathVariable String username, Model model) {
        Usuario usuario = usuarioRepo.findByUsername(username);
        model.addAttribute("usuario", usuario);
        return "perfil";
    }
}
```

Note: Spring Boot es el framework Java moderno. Define entidades JPA que mapean a base de datos. Los controladores manejan peticiones y preparan datos para las vistas. Spring maneja inyección de dependencias, transacciones, seguridad y más. Es potente pero tiene curva de aprendizaje.


### 8.3. Plantilla Thymeleaf

```html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>
    <h1 th:text="${usuario.nombre}">Nombre</h1>
    <p th:text="${usuario.bio}">Biografía</p>
    
    <div th:if="${#lists.isEmpty(posts)}">
        <p>Sin publicaciones.</p>
    </div>
    
    <div th:each="post : ${posts}">
        <article>
            <p th:text="${post.contenido}"></p>
        </article>
    </div>
</body>
</html>
```

Note: Thymeleaf es el motor de plantillas común en Spring. Usa atributos HTML especiales con prefijo `th:`. Es potente y mantiene el HTML válido incluso sin procesar. Los diseñadores pueden trabajar con las plantillas directamente en el navegador.


### 8.4. Ventajas y desventajas de Java

**Ventajas:**
- ✅ Rendimiento excelente
- ✅ Tipado fuerte previene errores
- ✅ Ideal para aplicaciones grandes
- ✅ Ecosistema empresarial maduro

**Desventajas:**
- ❌ Verbosidad del código
- ❌ Curva de aprendizaje pronunciada
- ❌ Configuración compleja

Note: Java es la opción empresarial por excelencia. El rendimiento es excelente, el tipado fuerte previene muchos errores, y es ideal para sistemas grandes con múltiples equipos. Pero el código es verboso, la curva de aprendizaje es pronunciada y la configuración puede ser compleja, aunque Spring Boot mejora esto significativamente.

---

## 9. Node.js: JavaScript en todas partes

Note: Node.js revolucionó el desarrollo web al permitir usar JavaScript tanto en frontend como en backend. Esto unificó el stack tecnológico y facilitó compartir código y conocimiento.


### 9.1. Express: framework minimalista

**JavaScript en el servidor**

```javascript
const express = require('express');
const app = express();

app.set('view engine', 'ejs');

app.get('/perfil/:username', async (req, res) => {
    const usuario = await Usuario.findOne({
        where: { username: req.params.username }
    });
    
    if (!usuario) {
        return res.status(404).send('Usuario no encontrado');
    }
    
    res.render('perfil', { usuario });
});

app.listen(3000);
```

Note: Express es el framework Node.js más popular. Es minimalista: proporciona routing, middleware y poco más. Tú añades lo que necesites. El código es JavaScript asíncrono con async/await. Es muy flexible y permite diferentes arquitecturas.


### 9.2. Plantilla EJS

```html
<!DOCTYPE html>
<html>
<body>
    <h1><%= usuario.nombre %></h1>
    <p>@<%= usuario.username %></p>
    <p><%= usuario.bio %></p>
    
    <h2>Publicaciones</h2>
    <% if (usuario.Posts && usuario.Posts.length > 0) { %>
        <% usuario.Posts.forEach(post => { %>
            <article>
                <p><%= post.contenido %></p>
                <small><%= new Date(post.fecha).toLocaleString() %></small>
            </article>
        <% }); %>
    <% } else { %>
        <p>Sin publicaciones.</p>
    <% } %>
</body>
</html>
```

Note: EJS (Embedded JavaScript) es un motor de plantillas simple para Node.js. Similar a PHP o JSP, permite embeber JavaScript en HTML. Usa `<%= %>` para imprimir valores y `<% %>` para lógica. La sintaxis es familiar para quien conoce JavaScript.


### 9.3. Ventajas y desventajas de Node.js

**Ventajas:**
- ✅ Un lenguaje para todo (JS everywhere)
- ✅ Excelente para I/O intensivo
- ✅ NPM: mayor ecosistema de paquetes
- ✅ Ideal para tiempo real

**Desventajas:**
- ❌ Single-threaded (aunque asíncrono)
- ❌ JavaScript propenso a errores
- ❌ Menos maduro para enterprise tradicional

Note: Node.js permite usar JavaScript en backend y frontend, compartir código y usar las mismas librerías. Excelente para aplicaciones I/O intensivas y tiempo real (chats, streaming). NPM es el mayor ecosistema de paquetes del mundo. Pero es single-threaded (aunque asíncrono), JavaScript puede ser propenso a errores sin TypeScript, y es menos maduro que Java para aplicaciones empresariales tradicionales.

---

## 10. Comparativa de tecnologías

Note: Finalmente, comparemos todas estas tecnologías para que tengáis una visión clara de cuándo usar cada una. No hay una opción "mejor", sino opciones más adecuadas según el contexto.


### 10.1. Tabla comparativa

| Tecnología | Ventaja Principal | Ideal Para |
|:-----------|:------------------|:-----------|
| **PHP** | Hosting universal | CMS, e-commerce |
| **Python** | Elegancia, versatilidad | Apps complejas, ML |
| **Java** | Robustez empresarial | Banca, grandes empresas |
| **Node.js** | JavaScript everywhere | APIs, tiempo real |
| **Ruby** | Productividad dev | Startups, MVPs |
| **C#** | Integración Microsoft | Entornos Windows |

Note: Cada tecnología tiene su nicho. PHP domina CMS y e-commerce. Python brilla en aplicaciones complejas y ciencia de datos. Java es el rey enterprise. Node.js es perfecto para APIs y tiempo real. Ruby acelera el desarrollo de MVPs. C# domina entornos Microsoft. La elección depende del proyecto, equipo y contexto.


### 10.2. Criterios de elección

**¿Qué considerar?**

- Experiencia del equipo
- Requisitos del proyecto
- Ecosistema de librerías
- Hosting disponible
- Escalabilidad futura
- Presupuesto
- Comunidad y soporte

Note: No elijas tecnología por hype. Considera la experiencia de tu equipo: es mejor usar lo que conocen bien. Analiza requisitos: ¿necesitas ML? Python. ¿Aplicación enterprise? Java. Verifica el ecosistema: ¿hay librerías para lo que necesitas? Considera hosting: ¿puedes desplegarlo fácilmente? Piensa en escalabilidad futura. Y valora comunidad y soporte.


### 10.3. Tendencias actuales

**El panorama hoy**

- Frameworks modernos en todos los lenguajes
- Arquitecturas de microservicios
- Serverless y edge computing
- TypeScript ganando terreno
- JAMstack para sitios estáticos mejorados

Note: Las tendencias actuales incluyen frameworks modernos que mejoran la experiencia de desarrollo en todos los lenguajes. Arquitecturas de microservicios donde diferentes servicios usan diferentes tecnologías. Serverless que abstrae servidores. Edge computing para latencia mínima. TypeScript añadiendo tipado a JavaScript. Y JAMstack combinando lo mejor de estático y dinámico.

---

## Resumen

**Lo esencial de páginas dinámicas**

- Evolución: de estático a dinámico
- Proceso: petición → código → BD → HTML → respuesta
- Tecnologías: PHP, Python, Java, Node.js
- Elección según contexto y requisitos

Note: Hemos visto el viaje completo desde páginas estáticas a dinámicas. Entendimos el proceso paso a paso de generación de contenido. Exploramos las principales tecnologías con sus ventajas. Lo importante es que todas resuelven el mismo problema: ejecutar código en el servidor para generar HTML personalizado. La elección depende de vuestro contexto específico.


## Conclusiones

**Páginas dinámicas: la base de la web moderna**

Sin generación dinámica no existirían:
- Redes sociales
- Comercio electrónico
- Banca online
- Aplicaciones web complejas

**La columna vertebral de Internet**

Note: Las páginas dinámicas son absolutamente fundamentales. Sin ellas, no tendríamos redes sociales, tiendas online, banca por Internet, ni la mayoría de servicios que usamos diariamente. Entender cómo funcionan es esencial para cualquier profesional del desarrollo y despliegue de aplicaciones web. Ahora tenéis las bases para trabajar con cualquiera de estas tecnologías.

---

## Preguntas

**¿Dudas sobre páginas web dinámicas?**

- ¿Proceso de generación?
- ¿Diferencias entre tecnologías?
- ¿Cuándo usar cada una?
- ¿Optimización y rendimiento?

Note: Es momento de resolver vuestras dudas. ¿Hay algo del proceso de generación que no quedó claro? ¿Dudas sobre cuándo usar PHP vs Python vs Java? ¿Preguntas sobre optimización y rendimiento? Este es un tema fundamental, así que asegurémonos de que lo domináis.
