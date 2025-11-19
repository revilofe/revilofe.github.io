---
title: "UD 3 - 3.6 Lenguajes y Frameworks en Entorno Servidor"
description: Lenguajes de programación del lado del servidor, plataformas web y frameworks para el desarrollo de servicios
summary: Tipos de ejecución de lenguajes servidor, plataformas LAMP/WISA, tecnologías para desarrollo de servicios, integración código con HTML
authors:
    - Eduardo Fdez
date: 2025-11-19
icon: 
permalink: /daw/unidad3/3.6
categories:
    - DAW
tags:
    - Lenguajes Servidor
    - Frameworks
    - LAMP
    - WISA
    - Plataformas Web
---

## 3.6. Lenguajes y Frameworks en Entorno Servidor

En la unidad anterior exploramos cómo funcionan las páginas web dinámicas y vimos ejemplos en diferentes lenguajes como PHP, Python, Java y Node.js. Sin embargo, había una pregunta que quedó pendiente: **¿cómo se ejecutan realmente estos lenguajes en el servidor? ¿Qué diferencias hay entre ellos a nivel técnico?**

Además, cuando desarrollamos aplicaciones web profesionales, raramente escribimos todo el código desde cero. En su lugar, utilizamos **frameworks** que nos proporcionan estructura, herramientas y soluciones a problemas comunes. Pero, ¿cómo elegir entre tantas opciones disponibles?

En esta unidad vamos a profundizar en el ecosistema técnico del desarrollo backend: desde cómo se ejecuta el código en el servidor hasta las plataformas completas que integran todos los componentes necesarios. Este conocimiento es esencial no solo para desarrollar aplicaciones, sino también para **desplegarlas correctamente**, que es el objetivo principal de este módulo.

### 1. La ejecución del código: más que solo ejecutar un script

Cuando aprendemos a programar, normalmente ejecutamos nuestros programas directamente: escribimos código en Python y lo ejecutamos con `python script.py`, o compilamos código Java con `javac` y lo ejecutamos con `java`. Parece simple. Pero en el entorno web del servidor, la ejecución es más compleja porque el código debe **integrarse con el servidor web** y responder a peticiones HTTP.

No todos los lenguajes se ejecutan de la misma manera, y entender estas diferencias es crucial para comprender el rendimiento, las limitaciones y las ventajas de cada tecnología.

#### 1.1. Lenguajes de guiones (Scripting Languages)

Los **lenguajes de guiones** o **interpretados** son aquellos cuyo código se ejecuta directamente a partir de su código fuente, sin necesidad de una compilación previa completa. Un intérprete lee el código línea por línea (o en bloques) y lo ejecuta sobre la marcha.

**Lenguajes de este tipo:**
- **PHP**: El más popular para web
- **Python**: Cada vez más usado
- **Ruby**: Con frameworks como Rails
- **Perl**: Históricamente importante, menos usado hoy
- **ASP clásico**: Predecesor de ASP.NET

**¿Cómo funciona la ejecución?**

Cuando el servidor web (Apache, Nginx) recibe una petición para un script PHP, por ejemplo:

1. **El servidor web detecta** que es un archivo `.php` (por configuración)
2. **Pasa el archivo** al intérprete de PHP (puede ser mod_php, PHP-FPM, o similar)
3. **El intérprete lee el código fuente** del archivo PHP
4. **Ejecuta el código línea por línea**, generando salida HTML
5. **Devuelve el HTML generado** al servidor web
6. **El servidor web envía** la respuesta al cliente

**Ejemplo del proceso con PHP:**

```php
<?php
// Archivo: productos.php
// El intérprete PHP leerá y ejecutará este código

// 1. Conectar a la base de datos
$db = new PDO('mysql:host=localhost;dbname=tienda', 'user', 'pass');

// 2. Consultar productos
$productos = $db->query('SELECT * FROM productos WHERE stock > 0')->fetchAll();

// 3. Generar HTML dinámicamente
?>
<!DOCTYPE html>
<html>
<head>
    <title>Productos Disponibles</title>
</head>
<body>
    <h1>Catálogo de Productos</h1>
    <div class="productos">
        <?php foreach ($productos as $producto): ?>
            <article class="producto">
                <h2><?php echo htmlspecialchars($producto['nombre']); ?></h2>
                <p>Precio: <?php echo number_format($producto['precio'], 2); ?>€</p>
                <p>Stock: <?php echo $producto['stock']; ?> unidades</p>
                <button>Añadir al carrito</button>
            </article>
        <?php endforeach; ?>
    </div>
</body>
</html>
```

Cada vez que un usuario solicita esta página, el intérprete PHP **lee y ejecuta todo el código de nuevo**. No hay código precompilado esperando; el intérprete procesa el archivo fuente directamente.

**Ventajas de los lenguajes de guiones:**

- **Desarrollo rápido**: No hay paso de compilación; escribes código y lo pruebas inmediatamente
- **Portabilidad extrema**: El mismo código fuente funciona en cualquier sistema con el intérprete
- **Flexibilidad**: Puedes modificar el código en producción sin recompilar
- **Facilidad de despliegue**: Solo copias los archivos fuente al servidor
- **Ideal para prototipado**: Cambios rápidos e iteración ágil

**Desventajas que debemos considerar:**

- **Rendimiento inferior**: Interpretar código es más lento que ejecutar código compilado
- **Errores en tiempo de ejecución**: Muchos errores solo se descubren al ejecutar esa línea específica
- **Sin optimización de compilador**: No hay optimizaciones previas del código
- **Consumo de recursos**: El intérprete debe estar activo para cada petición

!!! note "Caché de bytecode"
    Lenguajes como PHP y Python tienen sistemas de caché de bytecode (OpCache para PHP, .pyc para Python) que pre-compilan el código a un formato intermedio. Esto mejora significativamente el rendimiento, aunque sigue siendo interpretado al final.

#### 1.2. Lenguajes compilados a código nativo

Los **lenguajes compilados a código nativo** transforman completamente el código fuente en **código máquina** (binario) específico para el procesador y sistema operativo donde se ejecutarán. El resultado es un archivo ejecutable que el sistema operativo puede ejecutar directamente sin ningún intermediario.

**Lenguajes de este tipo:**
- **C**: El lenguaje de bajo nivel por excelencia
- **C++**: Con capacidades orientadas a objetos
- **Go (Golang)**: Moderno y diseñado para servicios
- **Rust**: Enfoque en seguridad y rendimiento

**¿Por qué no son comunes para web tradicional?**

Aunque estos lenguajes son extremadamente rápidos, tienen desventajas significativas para el desarrollo web tradicional:

**Problemas técnicos:**

1. **Integración compleja con servidores web**: Apache y Nginx están diseñados para trabajar con scripts o servidores de aplicaciones, no con binarios arbitrarios

2. **Falta de portabilidad**: Un ejecutable compilado para Linux x86_64 no funciona en Windows ni en Linux ARM

3. **Sin gestión de peticiones**: El código compilado normalmente se ejecuta una vez y termina; no está diseñado para escuchar peticiones HTTP continuamente

4. **Recompilación necesaria**: Cada cambio requiere recompilar todo el proyecto

**Sin embargo, hay una excepción moderna importante:**

Lenguajes como **Go** y **Rust** se compilan a código nativo pero están **diseñados para servicios web**. Incluyen servidores HTTP en sus bibliotecas estándar, lo que les permite actuar como servidores de aplicaciones completos.

**Ejemplo en Go:**

```go
package main

import (
    "database/sql"
    "encoding/json"
    "fmt"
    "log"
    "net/http"
    
    _ "github.com/go-sql-driver/mysql"
)

type Producto struct {
    ID     int     `json:"id"`
    Nombre string  `json:"nombre"`
    Precio float64 `json:"precio"`
    Stock  int     `json:"stock"`
}

func main() {
    // Este binario compilado incluye un servidor HTTP completo
    
    http.HandleFunc("/api/productos", func(w http.ResponseWriter, r *http.Request) {
        // Conectar a base de datos
        db, err := sql.Open("mysql", "user:pass@tcp(localhost:3306)/tienda")
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        defer db.Close()
        
        // Consultar productos
        rows, err := db.Query("SELECT id, nombre, precio, stock FROM productos WHERE stock > 0")
        if err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        defer rows.Close()
        
        // Construir respuesta JSON
        var productos []Producto
        for rows.Next() {
            var p Producto
            rows.Scan(&p.ID, &p.Nombre, &p.Precio, &p.Stock)
            productos = append(productos, p)
        }
        
        // Enviar JSON
        w.Header().Set("Content-Type", "application/json")
        json.NewEncoder(w).Encode(productos)
    })
    
    fmt.Println("Servidor escuchando en puerto 8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}
```

Este programa se compila a un **único ejecutable binario** que:
- Incluye el servidor HTTP
- Gestiona las conexiones
- Es extremadamente rápido
- Consume muy poca memoria

Se ejecuta directamente: `./servidor-productos` y ya está sirviendo peticiones.

**Ventajas de lenguajes compilados modernos:**

- **Rendimiento excepcional**: El más rápido posible
- **Consumo mínimo de recursos**: Ideal para microservicios
- **Binario único**: Todo el servidor en un solo archivo
- **Detección temprana de errores**: Muchos errores se capturan en compilación
- **Sin dependencias runtime**: No necesita intérprete instalado

**Desventajas:**

- **Curva de aprendizaje**: Más complejos que lenguajes de scripting
- **Tiempo de compilación**: Cada cambio requiere recompilar
- **Menos flexibilidad**: Más rigidez en tipos y estructuras

#### 1.3. Lenguajes compilados a código intermedio: el equilibrio perfecto

Los **lenguajes de código intermedio** representan un punto medio entre los interpretados y los compilados a nativo. El código fuente se compila a un **formato intermedio** (bytecode) que luego ejecuta una **máquina virtual**.

**Lenguajes de este tipo:**
- **Java**: Con la JVM (Java Virtual Machine)
- **C#**: Con el CLR (.NET Runtime)
- **Kotlin**: También usa la JVM
- **Scala**: También usa la JVM

**¿Cómo funciona este modelo?**

El proceso tiene dos etapas claramente diferenciadas:

**Etapa 1: Compilación (una vez, durante el desarrollo/despliegue)**

```bash
# Código fuente Java
javac MiServlet.java

# Resultado: MiServlet.class (bytecode)
```

El compilador (`javac`) lee el código fuente y genera archivos `.class` que contienen **bytecode** Java. Este bytecode no es código máquina nativo, sino instrucciones para la JVM.

**Etapa 2: Ejecución (cada petición)**

Cuando llega una petición HTTP:

1. **El servidor de aplicaciones** (Tomcat, WildFly) ya está ejecutando la JVM
2. **La JVM carga el bytecode** de la clase necesaria (si no está ya cargada)
3. **El JIT compiler** (Just-In-Time) puede compilar bytecode a código nativo en memoria
4. **Se ejecuta el código** (interpretado o compilado JIT)
5. **Se genera la respuesta** HTML o JSON

**Ejemplo con Java Servlets:**

```java
// Archivo: ProductosServlet.java
package com.tienda.servlets;

import javax.servlet.*;
import javax.servlet.http.*;
import java.io.*;
import java.sql.*;
import java.util.*;

public class ProductosServlet extends HttpServlet {
    
    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        try {
            // Conectar a base de datos
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/tienda", "user", "pass");
            
            // Consultar productos
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(
                "SELECT * FROM productos WHERE stock > 0");
            
            // Generar HTML
            out.println("<!DOCTYPE html>");
            out.println("<html>");
            out.println("<head><title>Productos</title></head>");
            out.println("<body>");
            out.println("<h1>Catálogo de Productos</h1>");
            out.println("<div class='productos'>");
            
            while (rs.next()) {
                out.println("<article class='producto'>");
                out.println("<h2>" + rs.getString("nombre") + "</h2>");
                out.println("<p>Precio: " + rs.getDouble("precio") + "€</p>");
                out.println("<p>Stock: " + rs.getInt("stock") + " unidades</p>");
                out.println("<button>Añadir al carrito</button>");
                out.println("</article>");
            }
            
            out.println("</div>");
            out.println("</body>");
            out.println("</html>");
            
            // Cerrar recursos
            rs.close();
            stmt.close();
            conn.close();
            
        } catch (Exception e) {
            out.println("<h1>Error: " + e.getMessage() + "</h1>");
        }
    }
}
```

Este código se compila una vez a bytecode (`ProductosServlet.class`). Ese bytecode se despliega en Tomcat y se ejecuta cada vez que llega una petición.

**Ventajas del modelo de código intermedio:**

- **Buen rendimiento**: Cercano al código nativo, especialmente con JIT
- **Portabilidad**: El mismo bytecode funciona en cualquier plataforma con JVM/CLR
- **Optimizaciones**: El JIT puede optimizar el código en tiempo de ejecución
- **Gestión automática de memoria**: Garbage collection
- **Detección de errores**: Muchos errores en compilación, no en ejecución
- **Ecosistema empresarial**: Herramientas maduras, frameworks robustos

**Desventajas:**

- **Tiempo de arranque**: La JVM tarda en iniciar (aunque se mitiga con contenedores nativos modernos)
- **Consumo de memoria**: La JVM necesita memoria base
- **Complejidad**: Más complejo que lenguajes de scripting

#### 1.4. Tabla comparativa de modelos de ejecución

| Aspecto                 | Interpretado      | Código Nativo    | Código Intermedio    |
|:------------------------|:------------------|:-----------------|:---------------------|
| **Ejemplos**            | PHP, Python, Ruby | C, C++, Go, Rust | Java, C#, Kotlin     |
| **Compilación previa**  | No (o mínima)     | Sí, completa     | Sí, a bytecode       |
| **Portabilidad código** | Total             | Nula             | Total (con VM)       |
| **Rendimiento**         | Bajo-Medio        | Máximo           | Alto                 |
| **Tiempo inicio**       | Instantáneo       | Instantáneo      | Lento (JVM)          |
| **Memoria base**        | Bajo              | Mínimo           | Alto (VM)            |
| **Detección errores**   | En ejecución      | En compilación   | En compilación       |
| **Ideal para**          | Web tradicional   | Microservicios   | Aplicaciones grandes |
| **Curva aprendizaje**   | Suave             | Media-Alta       | Media-Alta           |

!!! tip "Eligiendo el modelo correcto"
    - **Interpretado**: Ideal para proyectos pequeños-medianos, desarrollo rápido, hosting compartido
    - **Nativo compilado**: Microservicios de alto rendimiento, sistemas con recursos limitados
    - **Intermedio**: Aplicaciones empresariales grandes, cuando necesitas robustez y rendimiento

### 2. Plataformas web: el stack completo

Ahora que entendemos cómo se ejecutan los lenguajes, hablemos de las **plataformas web completas**. Una aplicación web profesional no es solo código; necesita múltiples componentes trabajando juntos. Estos componentes forman lo que llamamos un **stack tecnológico** o **plataforma web**.

#### 2.1. Los cuatro pilares de una plataforma web

Una plataforma web completa necesita cuatro elementos fundamentales:

**1. Sistema Operativo**

El sistema operativo es la base sobre la que corre todo lo demás. Gestiona el hardware, los procesos, la memoria y proporciona servicios a las aplicaciones.

**Opciones principales:**
- **Linux**: Ubuntu, CentOS, Debian, RHEL
- **Windows Server**: Para entornos Microsoft
- **macOS Server**: Menos común en producción

La elección del sistema operativo tiene implicaciones importantes:
- **Coste**: Linux es gratuito; Windows Server requiere licencia
- **Compatibilidad**: Algunos frameworks prefieren Linux (.NET Core funciona mejor), otros requieren Windows (.NET Framework clásico)
- **Rendimiento**: Linux suele ser más eficiente para servidores web
- **Familiaridad**: Depende de la experiencia del equipo

**2. Servidor Web**

El servidor web es el software que escucha peticiones HTTP y las procesa. Es la primera línea de contacto con los clientes.

**Los dos dominantes:**

- **Apache HTTP Server**: El veterano, extremadamente configurable, con módulos para todo
- **Nginx**: El moderno, diseñado para alto rendimiento y concurrencia

**También importantes:**
- **IIS (Internet Information Services)**: Servidor web de Microsoft para Windows
- **LiteSpeed**: Alternativa comercial de alto rendimiento
- **Caddy**: Moderno, con HTTPS automático

**3. Sistema Gestor de Bases de Datos (SGBD)**

Toda aplicación web necesita almacenar datos de forma persistente. El SGBD es responsable de esto.

**Bases de datos relacionales (SQL):**
- **MySQL / MariaDB**: Las más populares para web
- **PostgreSQL**: Más avanzada, con características empresariales
- **SQL Server**: De Microsoft, robusto
- **Oracle**: Empresarial, costoso

**Bases de datos NoSQL:**
- **MongoDB**: Documentos JSON
- **Redis**: Clave-valor, en memoria
- **Cassandra**: Distribuida, escalable

**4. Lenguaje de Programación / Framework**

El lenguaje que ejecuta la lógica de negocio y genera las respuestas dinámicas.

Ya los hemos explorado: PHP, Python, Java, Node.js, Ruby, C#, Go, etc.

#### 2.2. LAMP: La plataforma que construyó la web

**LAMP** es el acrónimo más famoso del desarrollo web. Representa:

- **L**inux
- **A**pache
- **M**ySQL (o MariaDB)
- **P**HP (o Perl, o Python)

**¿Por qué LAMP tuvo tanto éxito?**

LAMP se popularizó en los años 2000 por varias razones poderosas:

1. **Todo es Open Source y gratuito**: Sin costes de licencia
2. **Fácil de aprender**: PHP es accesible para principiantes
3. **Hosting universal**: Prácticamente todo proveedor de hosting ofrece LAMP
4. **Comunidad masiva**: Toneladas de documentación, tutoriales, soluciones
5. **Rendimiento suficiente**: Para la mayoría de aplicaciones web
6. **Ecosistema maduro**: WordPress, Drupal, Joomla, etc.

**Arquitectura típica de LAMP:**

```
Internet
    ↓
[Firewall]
    ↓
[Linux Server]
    ↓
[Apache Web Server] ← Escucha puerto 80/443
    ↓
[mod_php / PHP-FPM] ← Ejecuta código PHP
    ↓
[MySQL Database] ← Almacena datos
```

**Flujo de una petición en LAMP:**

1. Usuario solicita: `http://mitienda.com/producto.php?id=42`
2. **Linux** recibe la conexión TCP en el puerto 80
3. **Apache** procesa la petición HTTP
4. Apache ve que es `.php` y lo pasa a **mod_php**
5. **PHP** ejecuta el script, conecta a **MySQL**, consulta el producto #42
6. MySQL devuelve los datos del producto
7. PHP genera HTML con esos datos
8. Apache envía el HTML al usuario

**Ejemplo de configuración LAMP:**

```bash
# Instalar LAMP en Ubuntu
sudo apt update
sudo apt install apache2 mysql-server php libapache2-mod-php php-mysql

# Verificar Apache
systemctl status apache2

# Verificar MySQL
systemctl status mysql

# Verificar PHP
php -v

# Crear un archivo PHP de prueba
echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/info.php

# Acceder a: http://localhost/info.php
```

**Variantes modernas de LAMP:**

- **LEMP**: Linux + Nginx + MySQL + PHP (Nginx se pronuncia "Engine-X")
- **LAPP**: Linux + Apache + PostgreSQL + PHP
- **MEAN**: MongoDB + Express + Angular + Node.js (todo JavaScript)
- **MERN**: MongoDB + Express + React + Node.js

#### 2.3. WISA: La alternativa de Microsoft

**WISA** representa el stack de Microsoft:

- **W**indows Server
- **I**IS (Internet Information Services)
- **S**QL Server
- **A**SP.NET

**¿Cuándo tiene sentido WISA?**

WISA es la elección natural cuando:

1. **Ya estás en el ecosistema Microsoft**: Empresas que usan Windows, Active Directory, Office 365
2. **Necesitas integración con productos Microsoft**: SharePoint, Dynamics, Azure
3. **Tu equipo conoce .NET**: Desarrolladores con experiencia en C#
4. **Aplicaciones empresariales complejas**: .NET es muy robusto para esto

**Arquitectura WISA:**

```
Internet
    ↓
[Windows Server]
    ↓
[IIS Web Server] ← Escucha puerto 80/443
    ↓
[ASP.NET Runtime / .NET Core] ← Ejecuta código C#
    ↓
[SQL Server] ← Almacena datos
```

**Ventajas de WISA:**

- **Integración perfecta**: Todo el stack diseñado para funcionar junto
- **Herramientas profesionales**: Visual Studio es excepcional
- **Rendimiento**: ASP.NET Core es muy rápido
- **Soporte empresarial**: Microsoft ofrece soporte comercial
- **Seguridad**: Actualizaciones de seguridad integradas con Windows Update

**Desventajas:**

- **Coste**: Licencias de Windows Server y SQL Server son caras
- **Menos flexible**: Más cerrado que el ecosistema open source
- **Dependencia**: Estás atado al ecosistema Microsoft

#### 2.4. Otras combinaciones populares

**WAMP (Windows + Apache + MySQL + PHP)**

Popular para **desarrollo local** en Windows. Herramientas como **XAMPP** y **WampServer** facilitan la instalación de todo el stack con un solo instalador.

Ideal para desarrolladores que trabajan en Windows pero despliegan en Linux.

**JAM Stack (JavaScript + APIs + Markup)**

Arquitectura moderna que precompila todo a HTML estático, usa JavaScript para interactividad y se conecta a APIs para datos dinámicos.

- **J**avaScript: React, Vue, Angular
- **A**PIs: Servicios backend (propios o terceros)
- **M**arkup: HTML generado estáticamente

**Ventajas del JAM Stack:**
- Extremadamente rápido (todo estático)
- Muy seguro (no hay servidor dinámico)
- Escalable (CDN puede servir todo)
- Económico (hosting estático es barato)

**Serverless Stack**

No hay servidor que mantener. Funciones individuales se ejecutan en respuesta a eventos.

- **AWS Lambda** + API Gateway + DynamoDB
- **Google Cloud Functions** + Firestore
- **Azure Functions** + Cosmos DB

### 3. Frameworks: no reinventar la rueda

Con la plataforma elegida, el siguiente paso es decidir si usar un **framework**. Los frameworks proporcionan estructura, herramientas y soluciones a problemas comunes del desarrollo web.

#### 3.1. ¿Qué es un framework y por qué usarlo?

Un **framework** es un conjunto de bibliotecas, convenciones y herramientas que proporciona una estructura para desarrollar aplicaciones.

**Diferencia entre librería y framework:**

- **Librería**: Tú llamas al código de la librería cuando lo necesitas
- **Framework**: El framework llama a tu código según su estructura (Inversión de Control)

**Ventajas de usar frameworks:**

- **Productividad**: Funcionalidades comunes ya implementadas
- **Mejores prácticas**: Estructuras probadas y seguras
- **Comunidad**: Documentación, tutoriales, plugins
- **Mantenibilidad**: Código más estructurado y legible
- **Seguridad**: Protección contra vulnerabilidades comunes incluida

#### 3.2. Frameworks principales por lenguaje

**PHP:**
- **Laravel**: El más popular, elegante, completo
- **Symfony**: Muy robusto, usado en proyectos grandes
- **CodeIgniter**: Ligero y rápido
- **CakePHP**: Convención sobre configuración

**Python:**
- **Django**: "Batteries included", completo
- **Flask**: Minimalista, flexible
- **FastAPI**: Moderno, para APIs rápidas
- **Pyramid**: Flexible, escalable

**Java:**
- **Spring Boot**: El estándar de facto
- **Jakarta EE** (anteriormente Java EE): Empresarial
- **Micronaut**: Moderno, para microservicios
- **Quarkus**: Optimizado para contenedores

**JavaScript/Node.js:**
- **Express**: Minimalista, flexible
- **NestJS**: Estructurado, inspirado en Angular
- **Fastify**: Alto rendimiento
- **Hapi**: Robusto, para aplicaciones complejas

**C#:**
- **ASP.NET Core MVC**: Framework completo
- **ASP.NET Core Minimal APIs**: Minimalista
- **Blazor**: Para aplicaciones con WebAssembly

### 4. Integración código con lenguajes de marcas

Finalmente, una técnica fundamental: **combinar código de programación con HTML**. Esto es lo que permite generar páginas dinámicas.

**Hay dos enfoques principales:**

#### 4.1. Renderizado del lado del servidor (SSR)

El código se ejecuta en el servidor, genera HTML y lo envía al cliente.

**PHP embebido:**
```php
<html>
<body>
    <?php foreach ($productos as $producto): ?>
        <div class="producto">
            <h3><?= $producto->nombre ?></h3>
            <p><?= $producto->precio ?>€</p>
        </div>
    <?php endforeach; ?>
</body>
</html>
```

**Django Templates:**
```django
<html>
<body>
    {% for producto in productos %}
        <div class="producto">
            <h3>{{ producto.nombre }}</h3>
            <p>{{ producto.precio }}€</p>
        </div>
    {% endfor %}
</body>
</html>
```

#### 4.2. Renderizado del lado del cliente (CSR)

El servidor envía datos (JSON), JavaScript genera el HTML en el navegador.

```javascript
// El servidor devuelve JSON
fetch('/api/productos')
    .then(response => response.json())
    .then(productos => {
        const container = document.getElementById('productos');
        productos.forEach(producto => {
            const div = document.createElement('div');
            div.className = 'producto';
            div.innerHTML = `
                <h3>${producto.nombre}</h3>
                <p>${producto.precio}€</p>
            `;
            container.appendChild(div);
        });
    });
```

Cada enfoque tiene sus ventajas según el caso de uso.

## Resumen de la unidad

En esta unidad hemos comprendido:

1. **Tres modelos de ejecución**: Interpretado (PHP, Python), nativo (Go, Rust), intermedio (Java, C#), cada uno con ventajas específicas.

2. **Plataformas completas**: LAMP, WISA y otras combinaciones que integran OS, servidor web, base de datos y lenguaje.

3. **Frameworks esenciales**: Proporcionan estructura, productividad y mejores prácticas para cada lenguaje.

4. **Integración código-HTML**: Tanto del lado servidor como cliente, según las necesidades.

Este conocimiento es fundamental para elegir el stack tecnológico adecuado y desplegar aplicaciones correctamente.

## Referencias y bibliografía

- [Jose Luis González](https://github.com/joseluisgs). *Despliegue de aplicaciones Web - 2025 2026*. [https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026](https://github.com/joseluisgs/DespliegueAplicacionesWeb-00-2025-2026)
- Apache Software Foundation. (2024). *Apache HTTP Server Documentation*
- Microsoft. (2024). *ASP.NET Core Documentation*
- Linux Foundation. (2024). *Linux Server Administration*

## Recursos adicionales

- [XAMPP](https://www.apachefriends.org/) - Stack LAMP/WAMP fácil
- [DigitalOcean Tutorials](https://www.digitalocean.com/community/tutorials) - Guías de configuración
- [Stack Overflow Developer Survey](https://survey.stackoverflow.co/) - Tendencias de tecnologías
