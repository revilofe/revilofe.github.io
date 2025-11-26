---
title: "UD 3 - 3.4 Acoplamiento y Cohesión"
description: Acoplamiento y Cohesión en el Diseño de Software
summary: Principios de diseño de software - Alta cohesión y bajo acoplamiento
authors:
    - Eduardo Fdez
date: 2024-11-03
icon: "material/file-document-outline"
permalink: /edes/unidad3/3.4
categories:
    - EDES
tags:
    - EDES
    - Diseño de Software
    - Acoplamiento
    - Cohesión
    - Principios SOLID

---


## 3.4 Acoplamiento y Cohesión en el Diseño de Software

### 1. Introducción

En el desarrollo de software, dos conceptos fundamentales que determinan la **calidad, mantenibilidad y flexibilidad** del diseño son el **acoplamiento** y la **cohesión**. Estos principios no son opcionales en un buen diseño: son los pilares sobre los que se construyen sistemas que perduran en el tiempo, que pueden adaptarse a nuevos requisitos, y que no se convierten en "código espagueti" imposible de mantener.

#### 1.1. El problema del código espagueti

Imagina que estás construyendo un sistema con múltiples módulos que interactúan entre sí. Si cada módulo está fuertemente acoplado a los otros (es decir, si un cambio en un módulo requiere cambios en cascada en todos los demás), entonces tu sistema es **frágil y difícil de mantener**. Por otro lado, si cada módulo tiene baja cohesión (es decir, si sus funciones están desconectadas y sin propósito común), entonces es **difícil de entender** qué hace realmente cada módulo.

**Escenario real**: Imagina que te toca mantener un sistema donde:

- Cambiar el formato de una fecha en la base de datos requiere modificar 47 clases diferentes
- Una clase llamada `Usuario` también se encarga de enviar emails, validar contraseñas, generar PDFs y conectarse a Twitter
- No puedes probar un módulo sin arrancar toda la aplicación, incluyendo la base de datos y servicios externos

Estos son síntomas claros de **alto acoplamiento** y **baja cohesión**.

#### 1.2. El equilibrio ideal

El equilibrio ideal es: **bajo acoplamiento** (módulos independientes) y **alta cohesión** (cada módulo tiene un propósito claro y unificado).

!!! note "Principio clave"
    Un buen diseño de software debe buscar **bajo acoplamiento** y **alta cohesión**.

**Objetivos de un buen diseño**:

- **Bajo acoplamiento**: Minimizar las dependencias entre módulos para que puedan evolucionar independientemente
- **Alta cohesión**: Maximizar la relación entre los elementos dentro de un mismo módulo para que tengan un propósito común
- **Mantenibilidad**: El código debe ser fácil de entender y modificar
- **Flexibilidad**: El sistema debe adaptarse a nuevos requisitos sin refactorización masiva
- **Testeabilidad**: Cada módulo debe poder probarse de forma aislada
- **Reusabilidad**: Los módulos bien diseñados pueden reutilizarse en otros contextos

#### 1.3. Beneficios tangibles

Cuando aplicas correctamente estos principios, obtienes:

**Menos bugs**: Cambios localizados = menos efectos colaterales  
**Desarrollo más rápido**: Entender y modificar código es más fácil  
**Testing más simple**: Puedes probar módulos de forma independiente  
**Trabajo en equipo más eficiente**: Diferentes desarrolladores pueden trabajar en módulos diferentes sin conflictos  
**Menor deuda técnica**: El código no se degrada con el tiempo  
**Costes de mantenimiento reducidos**: Menos tiempo debuggeando, más tiempo agregando valor  

#### 1.3. Estructura del documento

En este documento exploraremos en profundidad:

1. **Cohesión**: Qué es, tipos, cómo medirla y mejorarla
2. **Acoplamiento**: Tipos, niveles, estrategias de reducción
3. **La relación entre ambos**: Matriz de calidad y trade-offs
4. **Principios SOLID**: Cómo se relacionan con cohesión y acoplamiento
5. **Métricas**: Cómo medir objetivamente la calidad del diseño
6. **Casos prácticos**: Refactorización paso a paso de código real
7. **Herramientas**: Cómo automatizar la detección de problemas

Comenzaremos con la cohesión, el principio que muchos consideran el más importante de los dos.


### 2. Cohesión: El Pegamento que une un módulo

#### 2.1. ¿Qué es la cohesión?

La **cohesión** es una medida que indica **cuán relacionados y enfocados están los elementos dentro de un mismo módulo, clase o componente**. En términos simples: ¿los elementos de esta clase trabajan juntos hacia un objetivo común, o cada uno hace lo suyo?

##### 2.1.1. Definición formal

**Cohesión** = Grado en que las responsabilidades de un módulo están relacionadas entre sí.

Una alta cohesión significa que:

- Los elementos del módulo están **fuertemente relacionados** en su propósito
- Todos trabajan **hacia un objetivo común**
- La clase o módulo tiene **una responsabilidad clara y única**
- Cambiar la lógica de una parte **afecta naturalmente** a las otras partes, porque todas están relacionadas
- El nombre del módulo describe perfectamente todo lo que hace

Una baja cohesión indica:

- Los elementos están **débilmente relacionados** o sin relación alguna
- El módulo hace **múltiples cosas no relacionadas**
- Es difícil darle un **nombre descriptivo** sin usar "Y" o "Manager"
- Cambios en una parte **no deberían afectar** a otras partes (porque no están relacionadas)

##### 2.1.2. Analogías del mundo real

**Analogía 1 - Equipo de fútbol**: 

Imagina un equipo de fútbol bien organizado:

- Los **defensas** trabajan juntos para defender (alta cohesión defensiva)
- Los **atacantes** trabajan juntos para anotar (alta cohesión ofensiva)
- Todo el **equipo** trabaja junto para ganar (cohesión del equipo completo)

¿Qué pasaría si los defensas también tuvieran que cocinar el almuerzo, reparar el autobús y vender entradas? Eso sería baja cohesión - están haciendo tareas no relacionadas.

**Analogía 2 - Caja de herramientas**:

- **Alta cohesión**: Una caja contiene solo herramientas de carpintería (martillo, sierra, clavos, nivel)
- **Baja cohesión**: La misma caja contiene un martillo, una calculadora, un libro de cocina y una pelota de tenis

**Analogía 3 - Restaurante**:

- **Alta cohesión**: El chef se enfoca en cocinar, el camarero en servir, el cajero en cobrar
- **Baja cohesión**: El chef también repara el aire acondicionado, hace la contabilidad y limpia el baño

##### 2.1.3. ¿Por qué importa la cohesión?

La cohesión es crucial porque:

1. **Comprensión**: Es más fácil entender qué hace un módulo cuando todo está relacionado
2. **Mantenimiento**: Cambios en un concepto afectan solo a un módulo
3. **Reusabilidad**: Módulos cohesivos son más fáciles de reutilizar
4. **Testing**: Es más fácil probar una responsabilidad única
5. **Documentación**: Un módulo cohesivo se auto-documenta

!!! tip "Regla práctica"
    Si no puedes describir qué hace tu clase en una frase simple sin usar "Y", probablemente tiene baja cohesión.

##### 2.1.4. Señales de baja cohesión

Identifica problemas de cohesión cuando:

- La clase tiene más de 10-15 métodos públicos
- El nombre de la clase incluye "Manager", "Handler", "Util", "Helper"
- La clase cambia frecuentemente por razones no relacionadas
- Los métodos de la clase usan diferentes subconjuntos de atributos
- Hay métodos estáticos que no usan ningún atributo de instancia
- Cuesta trabajo decidir dónde agregar nueva funcionalidad

##### 2.1.5. Ejemplo introductorio

Veamos un ejemplo concreto para ilustrar la diferencia:

**BAJA COHESIÓN** - Clase que hace de todo:

```kotlin
class Usuario(
    val nombre: String,
    var email: String,
    private var password: String
) {
    // Responsabilidad 1: Gestión de datos del usuario
    fun actualizarEmail(nuevoEmail: String) {
        email = nuevoEmail
    }
    
    // Responsabilidad 2: Autenticación
    fun validarPassword(pwd: String): Boolean {
        return password == pwd
    }
    
    // Responsabilidad 3: Envío de emails
    fun enviarEmailBienvenida() {
        println("Enviando email a $email")
    }
    
    // Responsabilidad 4: Persistencia
    fun guardarEnBaseDatos() {
        println("INSERT INTO usuarios...")
    }
    
    // Responsabilidad 5: Generación de reportes
    fun generarReportePDF(): ByteArray {
        return byteArrayOf() // Genera PDF
    }
    
    // Responsabilidad 6: Logging
    fun registrarAccion(accion: String) {
        println("[LOG] Usuario $nombre: $accion")
    }
}
```

**Problemas**:

- La clase tiene 6 responsabilidades diferentes
- Si cambia el sistema de email, hay que modificar Usuario
- Si cambia la base de datos, hay que modificar Usuario
- Si cambia el formato de PDF, hay que modificar Usuario
- No se puede probar la validación de password sin tener lógica de email

**ALTA COHESIÓN** - Responsabilidades separadas:

```kotlin
// Solo datos y validación básica del dominio
class Usuario(
    val id: Int,
    var nombre: String,
    var email: String
) {
    fun actualizarEmail(nuevoEmail: String) {
        require(nuevoEmail.contains("@")) { "Email inválido" }
        email = nuevoEmail
    }
}

// Solo autenticación
class ServicioAutenticacion {
    fun validarCredenciales(email: String, password: String): Boolean {
        // Lógica de autenticación
        return true
    }
}

// Solo emails
class ServicioEmail {
    fun enviarBienvenida(usuario: Usuario) {
        println("Enviando bienvenida a ${usuario.email}")
    }
}

// Solo persistencia
class RepositorioUsuarios {
    fun guardar(usuario: Usuario) {
        println("INSERT INTO usuarios VALUES (${usuario.id}, '${usuario.nombre}')")
    }
    
    fun buscarPorEmail(email: String): Usuario? {
        // Búsqueda en BD
        return null
    }
}

// Solo reportes
class GeneradorReportes {
    fun generarPDFUsuario(usuario: Usuario): ByteArray {
        return byteArrayOf() // Genera PDF
    }
}

// Solo logging
class ServicioAuditoria {
    fun registrarAccion(usuarioId: Int, accion: String) {
        println("[${java.time.LocalDateTime.now()}] Usuario $usuarioId: $accion")
    }
}
```

**Beneficios**:

- Cada clase tiene una responsabilidad única y clara
- Cambios en email no afectan a persistencia
- Se puede testear cada servicio independientemente
- Fácil de extender (nueva notificación = nueva clase)
- Nombres descriptivos que explican el propósito

En las siguientes secciones, exploraremos los diferentes tipos de cohesión y cómo identificarlos en tu código.


#### 2.2. Tipos de cohesión: De la peor a la mejor

La cohesión se puede clasificar en diferentes niveles, **ordenados de menor a mayor calidad**. Entender estos niveles te ayudará a identificar y mejorar la cohesión en tu código. Piensa en esta clasificación como una escala de calidad donde debes aspirar a los niveles superiores.

##### 2.2.1. Tabla resumen de tipos de cohesión

| Nivel | Tipo                    | Calidad      | Descripción breve                                | Esfuerzo de mantenimiento |
|-------|-------------------------|--------------|--------------------------------------------------|---------------------------|
| 1     | Cohesión coincidental   | ❌ La peor    | Elementos agrupados sin ninguna relación lógica | Muy alto                  |
| 2     | Cohesión lógica         | 🔴 Muy baja  | Elementos relacionados por tipo, pero no función| Alto                      |
| 3     | Cohesión temporal       | 🟠 Baja      | Elementos ejecutados en el mismo momento        | Alto                      |
| 4     | Cohesión procedimental  | 🟡 Media-baja| Elementos que siguen una secuencia              | Medio-alto                |
| 5     | Cohesión comunicacional | 🟢 Media     | Elementos que comparten datos de entrada/salida | Medio                     |
| 6     | Cohesión secuencial     | 🔵 Alta      | Salida de uno es entrada del siguiente          | Bajo                      |
| 7     | Cohesión funcional      | La mejor   | Todos enfocados en una única función            | Muy bajo                  |

!!! warning "Objetivo de diseño"
    Siempre debemos aspirar a **cohesión funcional** (nivel 7) o, como mínimo, a **cohesión secuencial** (nivel 6). Los niveles 1-4 indican serios problemas de diseño.


##### 2.2.2. Cohesión Coincidental (Nivel 1 - ❌ La peor)

**Definición**: Los elementos están agrupados sin ninguna relación aparente. Es como meter cosas al azar en una caja simplemente porque hay espacio.

**Características**:

- No hay razón lógica para que los elementos estén juntos
- Cambios en un elemento no afectan a otros
- Difícil de entender, mantener y reutilizar
- Imposible de documentar coherentemente

**Ejemplo típico**: La temida clase `Utilidades` o `Utils`

```kotlin
// ❌ COHESIÓN COINCIDENTAL - Elementos sin relación
class Utilidades {
    // Matemáticas
    fun calcularIva(precio: Double): Double {
        return precio * 0.21
    }
    
    // Comunicación
    fun enviarEmail(destinatario: String, mensaje: String) {
        println("Enviando email a $destinatario: $mensaje")
    }
    
    // Algoritmos
    fun ordenarArray(array: List<Int>): List<Int> {
        return array.sorted()
    }
    
    // Fecha/hora
    fun obtenerFechaActual(): String {
        return java.time.LocalDate.now().toString()
    }
    
    // Validaciones
    fun esEmailValido(email: String): Boolean {
        return email.contains("@")
    }
    
    // Generación de IDs
    fun generarId(): String {
        return java.util.UUID.randomUUID().toString()
    }
}

// Uso confuso - ¿qué hace realmente esta clase?
val utils = Utilidades()
val precio = utils.calcularIva(100.0)
utils.enviarEmail("user@example.com", "Hola")
val lista = utils.ordenarArray(listOf(3, 1, 2))
```

**Problemas identificados**:

- No puedes describir qué hace la clase en una frase
- Agregar nueva funcionalidad es arbitrario (¿va aquí o en otra clase?)
- Testing es difícil (muchos mocks diferentes)
- Imposible de documentar coherentemente

**Solución - Separar por dominios**:

```kotlin
// Alta cohesión - cada clase tiene un propósito claro
class CalculadoraPrecios {
    private val tasaIVA = 0.21
    
    fun calcularIva(precio: Double): Double = precio * tasaIVA
    fun calcularPrecioFinal(precioBase: Double): Double = precioBase + calcularIva(precioBase)
}

class ServicioEmail {
    fun enviar(destinatario: String, mensaje: String) {
        println("Enviando email a $destinatario: $mensaje")
    }
    
    fun enviarConPlantilla(destinatario: String, plantilla: String, datos: Map<String, String>) {
        val mensaje = procesarPlantilla(plantilla, datos)
        enviar(destinatario, mensaje)
    }
    
    private fun procesarPlantilla(plantilla: String, datos: Map<String, String>): String {
        // Lógica de plantillas
        return plantilla
    }
}

class UtilidadesColecciones {
    fun <T: Comparable<T>> ordenar(lista: List<T>): List<T> = lista.sorted()
    fun <T: Comparable<T>> ordenarDescendente(lista: List<T>): List<T> = lista.sortedDescending()
    fun <T> filtrarDuplicados(lista: List<T>): List<T> = lista.distinct()
}

class ServicioFechas {
    fun obtenerFechaActual(): java.time.LocalDate = java.time.LocalDate.now()
    fun formatearFecha(fecha: java.time.LocalDate, formato: String): String {
        return fecha.toString() // Simplificado
    }
}

class ValidadorEmail {
    fun esValido(email: String): Boolean {
        return email.matches(Regex("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"))
    }
}

class GeneradorIdentificadores {
    fun generarUUID(): String = java.util.UUID.randomUUID().toString()
    fun generarIdNumerico(): Long = System.currentTimeMillis()
}
```

**Beneficios de la refactorización**:

- Cada clase tiene un propósito claro
- Fácil de localizar funcionalidad
- Testing más simple (mocks específicos)
- Fácil de documentar

**Cuándo se produce**:

- Prisas en el desarrollo ("lo pongo donde sea")
- Falta de planificación
- Código legacy sin refactorizar
- Clases "cajón de sastre"


##### 2.2.2. Cohesión Lógica (Nivel 2 - 🔴 Muy baja)

**Definición**: Los elementos están relacionados porque realizan actividades del mismo **tipo**, aunque no necesariamente están relacionadas funcionalmente. Es como agrupar todas las operaciones de "entrada/salida" juntas, aunque trabajen con conceptos completamente diferentes.

**Características**:

- Elementos agrupados por categoría lógica, no por colaboración
- Normalmente controlados por un parámetro que selecciona la operación
- Estructura típica: `if/else` o `when` para decidir qué hacer
- Difícil de extender (hay que modificar la clase cada vez)

**Ejemplo típico**: Clase con un método que hace cosas diferentes según un parámetro

```kotlin
// ❌ COHESIÓN LÓGICA - Operaciones del mismo tipo pero no relacionadas
class Operaciones {
    fun ejecutar(tipo: String, datos: List<Int>): Int {
        return when(tipo) {
            "SUMA" -> {
                datos.sum()
            }
            "PROMEDIO" -> {
                if (datos.isEmpty()) 0 else datos.sum() / datos.size
            }
            "MAXIMO" -> {
                datos.maxOrNull() ?: 0
            }
            "ORDENAR" -> {
                datos.sorted().first()
            }
            "BUSCAR" -> {
                datos.find { it > 10 } ?: -1
            }
            else -> 0
        }
    }
}

// Uso confuso - ¿qué hace "ejecutar"?
val ops = Operaciones()
val suma = ops.ejecutar("SUMA", listOf(1, 2, 3))
val max = ops.ejecutar("MAXIMO", listOf(1, 2, 3))
val ordenado = ops.ejecutar("ORDENAR", listOf(3, 1, 2))
```

**Problemas**:

- Método "ejecutar" es demasiado genérico
- Difícil de extender (agregar nueva operación requiere modificar la clase)
- Viola el Principio de Abierto/Cerrado
- Testing complejo (hay que probar todos los casos)
- No se puede reutilizar una operación específica sin la clase completa

**Otro ejemplo común**: Handler de eventos

```kotlin
// ❌ COHESIÓN LÓGICA - Handler que maneja eventos no relacionados
class ManejadorEventos {
    fun manejar(evento: String, datos: Any) {
        when(evento) {
            "USUARIO_CREADO" -> {
                val usuario = datos as Usuario
                enviarEmailBienvenida(usuario)
                crearDirectorioUsuario(usuario)
                registrarEnAuditoria(usuario)
            }
            "PEDIDO_REALIZADO" -> {
                val pedido = datos as Pedido
                enviarConfirmacionPedido(pedido)
                actualizarInventario(pedido)
                notificarAlmacen(pedido)
            }
            "PAGO_RECIBIDO" -> {
                val pago = datos as Pago
                enviarRecibo(pago)
                actualizarContabilidad(pago)
            }
        }
    }
    
    private fun enviarEmailBienvenida(usuario: Usuario) { }
    private fun crearDirectorioUsuario(usuario: Usuario) { }
    private fun registrarEnAuditoria(usuario: Usuario) { }
    private fun enviarConfirmacionPedido(pedido: Pedido) { }
    private fun actualizarInventario(pedido: Pedido) { }
    private fun notificarAlmacen(pedido: Pedido) { }
    private fun enviarRecibo(pago: Pago) { }
    private fun actualizarContabilidad(pago: Pago) { }
}
```

**Solución - Separar por responsabilidad funcional**:

```kotlin
// Cohesión funcional - Operaciones matemáticas separadas
interface OperacionNumerica {
    fun ejecutar(datos: List<Int>): Int
}

class OperacionSuma : OperacionNumerica {
    override fun ejecutar(datos: List<Int>): Int = datos.sum()
}

class OperacionPromedio : OperacionNumerica {
    override fun ejecutar(datos: List<Int>): Int {
        return if (datos.isEmpty()) 0 else datos.sum() / datos.size
    }
}

class OperacionMaximo : OperacionNumerica {
    override fun ejecutar(datos: List<Int>): Int = datos.maxOrNull() ?: 0
}

// Uso claro y extensible
val suma = OperacionSuma().ejecutar(listOf(1, 2, 3))
val promedio = OperacionPromedio().ejecutar(listOf(1, 2, 3))
val maximo = OperacionMaximo().ejecutar(listOf(1, 2, 3))

// Para eventos, usar el patrón Observer/Event Handler
interface ManejadorEvento<T> {
    fun manejar(dato: T)
}

class ManejadorUsuarioCreado : ManejadorEvento<Usuario> {
    override fun manejar(usuario: Usuario) {
        enviarEmailBienvenida(usuario)
        crearDirectorioUsuario(usuario)
        registrarEnAuditoria(usuario)
    }
    
    private fun enviarEmailBienvenida(usuario: Usuario) { }
    private fun crearDirectorioUsuario(usuario: Usuario) { }
    private fun registrarEnAuditoria(usuario: Usuario) { }
}

class ManejadorPedidoRealizado : ManejadorEvento<Pedido> {
    override fun manejar(pedido: Pedido) {
        enviarConfirmacionPedido(pedido)
        actualizarInventario(pedido)
        notificarAlmacen(pedido)
    }
    
    private fun enviarConfirmacionPedido(pedido: Pedido) { }
    private fun actualizarInventario(pedido: Pedido) { }
    private fun notificarAlmacen(pedido: Pedido) { }
}

// Sistema de despacho de eventos
class DispatcherEventos {
    private val manejadores = mutableMapOf<String, ManejadorEvento<Any>>()
    
    fun <T> registrar(evento: String, manejador: ManejadorEvento<T>) {
        @Suppress("UNCHECKED_CAST")
        manejadores[evento] = manejador as ManejadorEvento<Any>
    }
    
    fun <T> disparar(evento: String, dato: T) {
        manejadores[evento]?.manejar(dato as Any)
    }
}
```

**Beneficios**:

- Cada manejador tiene cohesión funcional
- Fácil de extender (nuevo evento = nueva clase)
- Testing simple (una clase a la vez)
- Respeta Open/Closed Principle


##### 2.2.3. Cohesión Temporal (Nivel 3 - 🟠 Baja)

**Definición**: Los elementos están agrupados porque se ejecutan en el **mismo momento** o durante la misma **fase del programa**, pero no están relacionados funcionalmente.

**Características**:

- Elementos ejecutados juntos por timing, no por relación lógica
- Típico en métodos de inicialización o limpieza
- Agrupa tareas que "casualmente" ocurren juntas
- Difícil de reutilizar parcialmente

**Ejemplo típico**: Método de inicialización que hace de todo

```kotlin
// ❌ COHESIÓN TEMPORAL - Todo se ejecuta al inicio, pero no está relacionado
class Aplicacion {
    fun inicializar() {
        // 1. Configurar logging
        System.setProperty("log.level", "INFO")
        println("Logger inicializado")
        
        // 2. Conectar base de datos
        conectarBaseDatos()
        println("Base de datos conectada")
        
        // 3. Cargar configuración
        val config = cargarConfiguracion()
        println("Configuración cargada: $config")
        
        // 4. Inicializar caché
        inicializarCache()
        println("Caché inicializada")
        
        // 5. Registrar servicios
        registrarServicios()
        println("Servicios registrados")
        
        // 6. Verificar licencia
        verificarLicencia()
        println("Licencia verificada")
        
        // 7. Limpiar archivos temporales
        limpiarTemporales()
        println("Temporales limpiados")
    }
    
    private fun conectarBaseDatos() { }
    private fun cargarConfiguracion(): Map<String, String> = mapOf()
    private fun inicializarCache() { }
    private fun registrarServicios() { }
    private fun verificarLicencia() { }
    private fun limpiarTemporales() { }
}
```

**Problemas**:

- Si falla uno, fallan todos
- No puedes inicializar solo una parte
- Difícil de testear (necesitas todo el contexto)
- No puedes reutilizar componentes individuales
- Orden de ejecución puede ser arbitrario

**Otro ejemplo**: Método de limpieza

```kotlin
// ❌ COHESIÓN TEMPORAL - Todo se limpia al final
class SistemaVentas {
    fun cerrarDia() {
        // Todas estas cosas pasan "al cierre del día"
        generarReporteDiario()
        enviarEmailsResumen()
        cerrarConexionesBD()
        archivarLogs()
        limpiarCacheMemoria()
        respaldarDatos()
        reiniciarContadores()
    }
    
    private fun generarReporteDiario() { }
    private fun enviarEmailsResumen() { }
    private fun cerrarConexionesBD() { }
    private fun archivarLogs() { }
    private fun limpiarCacheMemoria() { }
    private fun respaldarDatos() { }
    private fun reiniciarContadores() { }
}
```

**Solución - Separar por responsabilidad funcional**:

```kotlin
// Alta cohesión - Cada inicializador tiene su responsabilidad
interface Inicializador {
    fun inicializar()
    fun nombre(): String
}

class InicializadorLogger : Inicializador {
    override fun inicializar() {
        System.setProperty("log.level", "INFO")
        println("Logger inicializado")
    }
    
    override fun nombre() = "Logger"
}

class InicializadorBaseDatos : Inicializador {
    override fun inicializar() {
        // Lógica específica de BD
        println("Base de datos conectada")
    }
    
    override fun nombre() = "Base de Datos"
}

class InicializadorCache : Inicializador {
    override fun inicializar() {
        // Lógica específica de caché
        println("Caché inicializada")
    }
    
    override fun nombre() = "Caché"
}

// Coordinador que maneja el orden y dependencias
class GestorInicializacion {
    private val inicializadores = mutableListOf<Inicializador>()
    
    fun agregar(inicializador: Inicializador) {
        inicializadores.add(inicializador)
    }
    
    fun inicializarTodo() {
        inicializadores.forEach { init ->
            try {
                println("Iniciando ${init.nombre()}...")
                init.inicializar()
                println("✓ ${init.nombre()} listo")
            } catch (e: Exception) {
                println("✗ Error en ${init.nombre()}: ${e.message}")
            }
        }
    }
    
    fun inicializarSolo(nombre: String) {
        inicializadores
            .find { it.nombre() == nombre }
            ?.inicializar()
    }
}

// Uso
fun main() {
    val gestor = GestorInicializacion()
    gestor.agregar(InicializadorLogger())
    gestor.agregar(InicializadorBaseDatos())
    gestor.agregar(InicializadorCache())
    
    // Inicializar todo
    gestor.inicializarTodo()
    
    // O inicializar solo uno
    gestor.inicializarSolo("Caché")
}
```

**Beneficios**:

- Cada inicializador puede testearse independientemente
- Puedes inicializar componentes selectivamente
- Fácil de extender (nuevo inicializador = nueva clase)
- Manejo de errores individualizado
- Orden de inicialización explícito y configurable

**Cuándo es aceptable**:

- En scripts de setup muy simples
- Cuando realmente TODAS las operaciones deben ocurrir juntas
- Como punto de entrada que delega a componentes especializados



##### 2.2.4. Cohesión Procedimental (Nivel 4 - 🟡 Media-baja)

**Definición**: Los elementos están relacionados porque siguen una **secuencia específica de pasos** en un proceso, pero cada paso puede trabajar con datos diferentes y no estar funcionalmente relacionado.

**Características**:

- Elementos ejecutados en orden específico
- Cada paso puede trabajar con datos diferentes
- La relación es de "flujo de control", no de "propósito común"
- Similar a un procedimiento o algoritmo paso a paso

**Ejemplo típico**: Procesamiento de pedidos con pasos secuenciales

```kotlin
// ❌ COHESIÓN PROCEDIMENTAL - Pasos en secuencia pero conceptualmente diferentes
class ProcesadorPedido {
    fun procesarPedido(pedido: Pedido): Boolean {
        // Paso 1: Validar datos del pedido
        if (!validarDatosCliente(pedido.cliente)) {
            println("Cliente inválido")
            return false
        }
        
        // Paso 2: Verificar stock
        if (!verificarDisponibilidadStock(pedido.items)) {
            println("Stock insuficiente")
            return false
        }
        
        // Paso 3: Calcular precio total
        val total = calcularPrecioTotal(pedido.items)
        
        // Paso 4: Procesar pago
        if (!procesarPago(pedido.cliente, total)) {
            println("Pago rechazado")
            return false
        }
        
        // Paso 5: Actualizar inventario
        actualizarInventario(pedido.items)
        
        // Paso 6: Enviar confirmación por email
        enviarEmailConfirmacion(pedido.cliente.email, pedido)
        
        // Paso 7: Registrar en auditoría
        registrarEnAuditoria(pedido)
        
        println("Pedido procesado exitosamente")
        return true
    }
    
    private fun validarDatosCliente(cliente: Cliente): Boolean {
        return cliente.nombre.isNotEmpty() && cliente.email.contains("@")
    }
    
    private fun verificarDisponibilidadStock(items: List<ItemPedido>): Boolean {
        return items.all { it.cantidad <= obtenerStock(it.productoId) }
    }
    
    private fun calcularPrecioTotal(items: List<ItemPedido>): Double {
        return items.sumOf { it.precio * it.cantidad }
    }
    
    private fun procesarPago(cliente: Cliente, monto: Double): Boolean {
        // Lógica de pago
        return true
    }
    
    private fun actualizarInventario(items: List<ItemPedido>) {
        items.forEach { item ->
            println("Reduciendo stock de ${item.productoId} en ${item.cantidad}")
        }
    }
    
    private fun enviarEmailConfirmacion(email: String, pedido: Pedido) {
        println("Enviando confirmación a $email")
    }
    
    private fun registrarEnAuditoria(pedido: Pedido) {
        println("Registrando pedido ${pedido.id} en auditoría")
    }
    
    private fun obtenerStock(productoId: String): Int = 100
}

// Clases de datos
data class Pedido(val id: String, val cliente: Cliente, val items: List<ItemPedido>)
data class Cliente(val nombre: String, val email: String)
data class ItemPedido(val productoId: String, val cantidad: Int, val precio: Double)
```

**Problemas**:

- Mezcla responsabilidades: validación, cálculo, comunicación, persistencia
- Difícil de testear (necesitas mockear muchas cosas)
- Difícil de reutilizar pasos individuales
- Cambios en un paso pueden requerir cambios en la clase completa
- Viola el Principio de Responsabilidad Única

**Otro ejemplo**: Generación de reportes

```kotlin
// ❌ COHESIÓN PROCEDIMENTAL - Secuencia de pasos heterogéneos
class GeneradorReporte {
    fun generarReporteVentas(fecha: String): String {
        // Paso 1: Conectar a base de datos
        val conexion = conectarBaseDatos()
        
        // Paso 2: Consultar datos
        val ventas = consultarVentas(conexion, fecha)
        
        // Paso 3: Calcular estadísticas
        val total = ventas.sumOf { it.monto }
        val promedio = total / ventas.size
        
        // Paso 4: Formatear datos
        val textoFormateado = formatearDatos(ventas, total, promedio)
        
        // Paso 5: Generar PDF
        val pdf = generarPDF(textoFormateado)
        
        // Paso 6: Guardar en disco
        guardarArchivo(pdf, "reporte_$fecha.pdf")
        
        // Paso 7: Enviar por email
        enviarPorEmail(pdf, "gerente@empresa.com")
        
        return "Reporte generado"
    }
    
    private fun conectarBaseDatos(): String = "conexion"
    private fun consultarVentas(conexion: String, fecha: String): List<Venta> = listOf()
    private fun formatearDatos(ventas: List<Venta>, total: Double, promedio: Double): String = ""
    private fun generarPDF(texto: String): ByteArray = byteArrayOf()
    private fun guardarArchivo(datos: ByteArray, nombre: String) {}
    private fun enviarPorEmail(datos: ByteArray, destinatario: String) {}
}

data class Venta(val id: String, val monto: Double)
```

**Solución - Separar por dominios y usar composición**:

```kotlin
// Alta cohesión - Cada componente tiene una responsabilidad clara

// 1. Validación de pedidos
class ValidadorPedido {
    fun validarCliente(cliente: Cliente): ResultadoValidacion {
        val errores = mutableListOf<String>()
        
        if (cliente.nombre.isEmpty()) {
            errores.add("Nombre del cliente requerido")
        }
        
        if (!cliente.email.matches(Regex("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$"))) {
            errores.add("Email inválido")
        }
        
        return if (errores.isEmpty()) {
            ResultadoValidacion.Exitoso
        } else {
            ResultadoValidacion.Fallido(errores)
        }
    }
    
    fun validarItems(items: List<ItemPedido>): ResultadoValidacion {
        if (items.isEmpty()) {
            return ResultadoValidacion.Fallido(listOf("El pedido debe tener al menos un item"))
        }
        
        val errores = items.flatMap { item ->
            when {
                item.cantidad <= 0 -> listOf("Cantidad debe ser mayor a 0")
                item.precio <= 0 -> listOf("Precio debe ser mayor a 0")
                else -> emptyList()
            }
        }
        
        return if (errores.isEmpty()) {
            ResultadoValidacion.Exitoso
        } else {
            ResultadoValidacion.Fallido(errores)
        }
    }
}

sealed class ResultadoValidacion {
    object Exitoso : ResultadoValidacion()
    data class Fallido(val errores: List<String>) : ResultadoValidacion()
}

// 2. Gestión de inventario
class GestorInventario {
    private val inventario = mutableMapOf<String, Int>()
    
    fun verificarDisponibilidad(items: List<ItemPedido>): ResultadoDisponibilidad {
        val noDisponibles = items.filter { item ->
            (inventario[item.productoId] ?: 0) < item.cantidad
        }
        
        return if (noDisponibles.isEmpty()) {
            ResultadoDisponibilidad.Disponible
        } else {
            ResultadoDisponibilidad.NoDisponible(noDisponibles.map { it.productoId })
        }
    }
    
    fun reservar(items: List<ItemPedido>): Boolean {
        items.forEach { item ->
            val stockActual = inventario[item.productoId] ?: 0
            inventario[item.productoId] = stockActual - item.cantidad
        }
        return true
    }
    
    fun liberar(items: List<ItemPedido>) {
        items.forEach { item ->
            val stockActual = inventario[item.productoId] ?: 0
            inventario[item.productoId] = stockActual + item.cantidad
        }
    }
}

sealed class ResultadoDisponibilidad {
    object Disponible : ResultadoDisponibilidad()
    data class NoDisponible(val productos: List<String>) : ResultadoDisponibilidad()
}

// 3. Cálculo de precios
class CalculadoraPrecios {
    fun calcularTotalPedido(items: List<ItemPedido>): Double {
        return items.sumOf { calcularSubtotal(it) }
    }
    
    fun calcularSubtotal(item: ItemPedido): Double {
        return item.precio * item.cantidad
    }
    
    fun aplicarDescuento(total: Double, porcentaje: Double): Double {
        return total * (1 - porcentaje / 100)
    }
    
    fun calcularImpuestos(total: Double, tasaImpuesto: Double = 0.21): Double {
        return total * tasaImpuesto
    }
}

// 4. Procesamiento de pagos
class ServicioPagos {
    fun procesar(cliente: Cliente, monto: Double): ResultadoPago {
        // Lógica de integración con pasarela de pago
        println("Procesando pago de $monto para ${cliente.nombre}")
        
        return if (monto > 0) {
            ResultadoPago.Aprobado("TX-${System.currentTimeMillis()}")
        } else {
            ResultadoPago.Rechazado("Monto inválido")
        }
    }
}

sealed class ResultadoPago {
    data class Aprobado(val transaccionId: String) : ResultadoPago()
    data class Rechazado(val razon: String) : ResultadoPago()
}

// 5. Notificaciones
class ServicioNotificaciones {
    fun enviarConfirmacionPedido(cliente: Cliente, pedido: Pedido) {
        println("Enviando confirmación a ${cliente.email}")
        println("Detalles del pedido: ${pedido.id}")
    }
    
    fun enviarNotificacionPagoRechazado(cliente: Cliente, razon: String) {
        println("Notificando rechazo de pago a ${cliente.email}: $razon")
    }
}

// 6. Auditoría
class ServicioAuditoria {
    fun registrarPedidoProcesado(pedido: Pedido, resultado: String) {
        println("[AUDITORIA] Pedido ${pedido.id}: $resultado - ${java.time.LocalDateTime.now()}")
    }
}

// 7. Orquestador - Coordina el flujo usando componentes cohesivos
class OrquestadorPedidos(
    private val validador: ValidadorPedido,
    private val gestorInventario: GestorInventario,
    private val calculadora: CalculadoraPrecios,
    private val servicioPagos: ServicioPagos,
    private val notificaciones: ServicioNotificaciones,
    private val auditoria: ServicioAuditoria
) {
    fun procesarPedido(pedido: Pedido): ResultadoProcesamiento {
        // Paso 1: Validar
        val validacionCliente = validador.validarCliente(pedido.cliente)
        if (validacionCliente is ResultadoValidacion.Fallido) {
            return ResultadoProcesamiento.Error("Validación fallida: ${validacionCliente.errores}")
        }
        
        val validacionItems = validador.validarItems(pedido.items)
        if (validacionItems is ResultadoValidacion.Fallido) {
            return ResultadoProcesamiento.Error("Items inválidos: ${validacionItems.errores}")
        }
        
        // Paso 2: Verificar stock
        val disponibilidad = gestorInventario.verificarDisponibilidad(pedido.items)
        if (disponibilidad is ResultadoDisponibilidad.NoDisponible) {
            return ResultadoProcesamiento.Error("Productos no disponibles: ${disponibilidad.productos}")
        }
        
        // Paso 3: Calcular total
        val total = calculadora.calcularTotalPedido(pedido.items)
        
        // Paso 4: Procesar pago
        val resultadoPago = servicioPagos.procesar(pedido.cliente, total)
        if (resultadoPago is ResultadoPago.Rechazado) {
            notificaciones.enviarNotificacionPagoRechazado(pedido.cliente, resultadoPago.razon)
            return ResultadoProcesamiento.Error("Pago rechazado: ${resultadoPago.razon}")
        }
        
        // Paso 5: Reservar inventario
        gestorInventario.reservar(pedido.items)
        
        // Paso 6: Notificar
        notificaciones.enviarConfirmacionPedido(pedido.cliente, pedido)
        
        // Paso 7: Auditar
        auditoria.registrarPedidoProcesado(pedido, "EXITOSO")
        
        return ResultadoProcesamiento.Exitoso(pedido.id)
    }
}

sealed class ResultadoProcesamiento {
    data class Exitoso(val pedidoId: String) : ResultadoProcesamiento()
    data class Error(val mensaje: String) : ResultadoProcesamiento()
}

// Uso
fun main() {
    val orquestador = OrquestadorPedidos(
        validador = ValidadorPedido(),
        gestorInventario = GestorInventario(),
        calculadora = CalculadoraPrecios(),
        servicioPagos = ServicioPagos(),
        notificaciones = ServicioNotificaciones(),
        auditoria = ServicioAuditoria()
    )
    
    val pedido = Pedido(
        id = "PED-001",
        cliente = Cliente("Juan Pérez", "juan@example.com"),
        items = listOf(
            ItemPedido("PROD-1", 2, 50.0),
            ItemPedido("PROD-2", 1, 100.0)
        )
    )
    
    val resultado = orquestador.procesarPedido(pedido)
    println(resultado)
}
```

**Beneficios de la refactorización**:

- Cada clase tiene cohesión funcional
- Testing independiente de cada componente
- Fácil de reutilizar (por ejemplo, CalculadoraPrecios en otros contextos)
- Cambios localizados (cambiar cálculo de precios no afecta validación)
- Respeta SRP y Open/Closed Principle


##### 2.2.5. Cohesión Comunicacional (Nivel 5 - 🟢 Media)

**Definición**: Los elementos están relacionados porque trabajan con el **mismo conjunto de datos** (misma entrada y/o salida), aunque realizan operaciones diferentes sobre esos datos.

**Características**:
- Todos los elementos acceden a las mismas estructuras de datos
- Realizan operaciones diferentes sobre los mismos datos
- Mejor que cohesión procedimental, pero aún no ideal
- Puede indicar que falta una abstracción

**Ejemplo típico**: Clase que hace múltiples operaciones sobre los mismos datos

```kotlin
// ⚠️ COHESIÓN COMUNICACIONAL - Operaciones diferentes sobre los mismos datos
class ProcesadorArchivo {
    fun procesarArchivo(nombreArchivo: String) {
        val contenido = leerArchivo(nombreArchivo)
        
        // Operación 1: Contar líneas
        val numLineas = contarLineas(contenido)
        println("Líneas: $numLineas")
        
        // Operación 2: Contar palabras
        val numPalabras = contarPalabras(contenido)
        println("Palabras: $numPalabras")
        
        // Operación 3: Buscar patrón
        val coincidencias = buscarPatron(contenido, "error")
        println("Coincidencias: $coincidencias")
        
        // Operación 4: Calcular estadísticas
        val estadisticas = calcularEstadisticas(contenido)
        println("Estadísticas: $estadisticas")
    }
    
    private fun leerArchivo(nombre: String): String {
        return "Contenido del archivo de ejemplo con algunas palabras"
    }
    
    private fun contarLineas(contenido: String): Int {
        return contenido.lines().size
    }
    
    private fun contarPalabras(contenido: String): Int {
        return contenido.split(Regex("\\s+")).size
    }
    
    private fun buscarPatron(contenido: String, patron: String): Int {
        return Regex(patron).findAll(contenido).count()
    }
    
    private fun calcularEstadisticas(contenido: String): String {
        val caracteres = contenido.length
        val lineas = contarLineas(contenido)
        val palabras = contarPalabras(contenido)
        return "Chars: $caracteres, Líneas: $lineas, Palabras: $palabras"
    }
}
```

**Problemas**:

- `procesarArchivo` hace demasiadas cosas no relacionadas
- Difícil de extender (agregar nueva operación requiere modificar la clase)
- No puedes usar una operación sin las otras
- Testing complejo

**Solución - Separar operaciones en clases especializadas**:

```kotlin
// Alta cohesión - Cada analizador tiene su propósito específico

// 1. Abstracción base para análisis
interface AnalizadorTexto {
    fun analizar(texto: String): Any
}

// 2. Contador de líneas
class ContadorLineas : AnalizadorTexto {
    override fun analizar(texto: String): Int {
        return texto.lines().size
    }
    
    fun contarLineasNoVacias(texto: String): Int {
        return texto.lines().count { it.isNotBlank() }
    }
}

// 3. Contador de palabras
class ContadorPalabras : AnalizadorTexto {
    override fun analizar(texto: String): Int {
        return texto.split(Regex("\\s+")).size
    }
    
    fun contarPalabrasUnicas(texto: String): Int {
        return texto.split(Regex("\\s+")).distinct().size
    }
    
    fun obtenerPalabrasUnicas(texto: String): Set<String> {
        return texto.split(Regex("\\s+")).toSet()
    }
}

// 4. Buscador de patrones
class BuscadorPatrones : AnalizadorTexto {
    override fun analizar(texto: String): Map<String, Int> {
        // Por defecto busca patrones comunes
        return buscarMultiples(texto, listOf("error", "warning", "info"))
    }
    
    fun buscar(texto: String, patron: String): Int {
        return Regex(patron, RegexOption.IGNORE_CASE).findAll(texto).count()
    }
    
    fun buscarMultiples(texto: String, patrones: List<String>): Map<String, Int> {
        return patrones.associateWith { patron ->
            buscar(texto, patron)
        }
    }
    
    fun encontrarOcurrencias(texto: String, patron: String): List<String> {
        return Regex(patron, RegexOption.IGNORE_CASE)
            .findAll(texto)
            .map { it.value }
            .toList()
    }
}

// 5. Calculador de estadísticas
class CalculadorEstadisticas {
    fun calcular(texto: String): Estadisticas {
        val contadorLineas = ContadorLineas()
        val contadorPalabras = ContadorPalabras()
        
        return Estadisticas(
            caracteres = texto.length,
            lineas = contadorLineas.analizar(texto) as Int,
            lineasNoVacias = contadorLineas.contarLineasNoVacias(texto),
            palabras = contadorPalabras.analizar(texto) as Int,
            palabrasUnicas = contadorPalabras.contarPalabrasUnicas(texto)
        )
    }
}

data class Estadisticas(
    val caracteres: Int,
    val lineas: Int,
    val lineasNoVacias: Int,
    val palabras: Int,
    val palabrasUnicas: Int
) {
    override fun toString(): String {
        return """
            |Estadísticas del texto:
            |  Caracteres: $caracteres
            |  Líneas: $lineas (no vacías: $lineasNoVacias)
            |  Palabras: $palabras (únicas: $palabrasUnicas)
        """.trimMargin()
    }
}

// 6. Lector de archivos (responsabilidad única: I/O)
class LectorArchivos {
    fun leer(nombreArchivo: String): String {
        // En producción: java.io.File(nombreArchivo).readText()
        return "Contenido del archivo de ejemplo con error y warning"
    }
}

// 7. Uso composicional - cada herramienta independiente
fun main() {
    val lector = LectorArchivos()
    val contenido = lector.leer("archivo.txt")
    
    // Usar solo lo que necesitas
    val contadorLineas = ContadorLineas()
    println("Líneas: ${contadorLineas.analizar(contenido)}")
    
    val contadorPalabras = ContadorPalabras()
    println("Palabras: ${contadorPalabras.analizar(contenido)}")
    println("Palabras únicas: ${contadorPalabras.contarPalabrasUnicas(contenido)}")
    
    val buscador = BuscadorPatrones()
    println("Errores encontrados: ${buscador.buscar(contenido, "error")}")
    
    val calculador = CalculadorEstadisticas()
    println(calculador.calcular(contenido))
}
```

**Beneficios**:

- Cada clase es independiente y reutilizable
- Testing simple (una funcionalidad a la vez)
- Fácil de extender (nuevo análisis = nueva clase)
- Puedes componer análisis según necesites


##### 2.2.6. Cohesión Secuencial (Nivel 6 - 🔵 Alta)

**Definición**: Los elementos están relacionados porque la **salida de uno es la entrada del siguiente**, formando una cadena de procesamiento donde los datos fluyen naturalmente de un paso al otro.

**Características**:
- Pipeline de transformaciones
- Cada función toma el resultado de la anterior
- Flujo de datos claro y unidireccional
- Alta cohesión, buen diseño

**Ejemplo**: Pipeline de procesamiento de imágenes

```kotlin
// COHESIÓN SECUENCIAL - Transformaciones encadenadas
class ProcesadorImagen {
    private val ruta: String
    
    constructor(ruta: String) {
        this.ruta = ruta
    }
    
    // Paso 1: Cargar imagen
    fun cargar(): ImagenCargada {
        println("Cargando imagen de $ruta")
        return ImagenCargada(ruta, byteArrayOf(1, 2, 3))
    }
    
    // Paso 2: Redimensionar (toma ImagenCargada)
    fun redimensionar(imagen: ImagenCargada, ancho: Int, alto: Int): ImagenRedimensionada {
        println("Redimensionando a ${ancho}x${alto}")
        return ImagenRedimensionada(imagen.datos, ancho, alto)
    }
    
    // Paso 3: Aplicar filtro (toma ImagenRedimensionada)
    fun aplicarFiltro(imagen: ImagenRedimensionada, filtro: Filtro): ImagenFiltrada {
        println("Aplicando filtro $filtro")
        return ImagenFiltrada(imagen.datos, filtro)
    }
    
    // Paso 4: Comprimir (toma ImagenFiltrada)
    fun comprimir(imagen: ImagenFiltrada, calidad: Int): ImagenComprimida {
        println("Comprimiendo con calidad $calidad")
        return ImagenComprimida(imagen.datos, calidad)
    }
    
    // Paso 5: Guardar (toma ImagenComprimida)
    fun guardar(imagen: ImagenComprimida, rutaDestino: String) {
        println("Guardando en $rutaDestino")
    }
    
    // API fluent para encadenar operaciones
    fun procesarCompleto(ancho: Int, alto: Int, filtro: Filtro, calidad: Int, destino: String) {
        val cargada = cargar()
        val redimensionada = redimensionar(cargada, ancho, alto)
        val filtrada = aplicarFiltro(redimensionada, filtro)
        val comprimida = comprimir(filtrada, calidad)
        guardar(comprimida, destino)
    }
}

// Tipos específicos para cada etapa del pipeline
data class ImagenCargada(val ruta: String, val datos: ByteArray)
data class ImagenRedimensionada(val datos: ByteArray, val ancho: Int, val alto: Int)
data class ImagenFiltrada(val datos: ByteArray, val filtro: Filtro)
data class ImagenComprimida(val datos: ByteArray, val calidad: Int)

enum class Filtro { BLANCO_Y_NEGRO, SEPIA, BLUR, SHARPEN }

// Uso
fun main() {
    val procesador = ProcesadorImagen("foto.jpg")
    procesador.procesarCompleto(
        ancho = 800,
        alto = 600,
        filtro = Filtro.SEPIA,
        calidad = 85,
        destino = "foto_procesada.jpg"
    )
}
```

**Ejemplo mejorado con patrón Builder/Pipeline**:

```kotlin
// COHESIÓN SECUENCIAL - Pipeline funcional
class PipelineImagen(private val rutaOrigen: String) {
    private var imagen: ByteArray = byteArrayOf()
    private var ancho: Int = 0
    private var alto: Int = 0
    
    fun cargar(): PipelineImagen {
        println("Cargando $rutaOrigen")
        imagen = byteArrayOf(1, 2, 3) // Simulado
        return this
    }
    
    fun redimensionar(nuevoAncho: Int, nuevoAlto: Int): PipelineImagen {
        println("Redimensionando a ${nuevoAncho}x${nuevoAlto}")
        ancho = nuevoAncho
        alto = nuevoAlto
        return this
    }
    
    fun aplicarFiltro(filtro: Filtro): PipelineImagen {
        println("Aplicando filtro $filtro")
        // Transformación de imagen
        return this
    }
    
    fun comprimir(calidad: Int): PipelineImagen {
        println("Comprimiendo (calidad: $calidad)")
        return this
    }
    
    fun guardar(rutaDestino: String): Boolean {
        println("Guardando en $rutaDestino")
        return true
    }
    
    // API fluent
    companion object {
        fun desde(ruta: String) = PipelineImagen(ruta)
    }
}

// Uso fluent
fun main() {
    PipelineImagen.desde("foto.jpg")
        .cargar()
        .redimensionar(800, 600)
        .aplicarFiltro(Filtro.SEPIA)
        .comprimir(85)
        .guardar("foto_procesada.jpg")
}
```

**Otro ejemplo**: Procesamiento de texto

```kotlin
// COHESIÓN SECUENCIAL - Transformaciones de texto
class ProcesadorTexto(private val textoOriginal: String) {
    fun eliminarEspaciosExtras(): ProcesadorTexto {
        val textoLimpio = textoOriginal.replace(Regex("\\s+"), " ").trim()
        return ProcesadorTexto(textoLimpio)
    }
    
    fun convertirAMinusculas(): ProcesadorTexto {
        return ProcesadorTexto(textoOriginal.lowercase())
    }
    
    fun eliminarPuntuacion(): ProcesadorTexto {
        val sinPuntuacion = textoOriginal.replace(Regex("[^\\w\\s]"), "")
        return ProcesadorTexto(sinPuntuacion)
    }
    
    fun dividirEnPalabras(): List<String> {
        return textoOriginal.split(Regex("\\s+"))
    }
    
    fun obtenerTexto(): String = textoOriginal
    
    companion object {
        fun procesar(texto: String) = ProcesadorTexto(texto)
    }
}

// Uso
fun main() {
    val palabras = ProcesadorTexto.procesar("  Hola,    Mundo!!!  ")
        .eliminarEspaciosExtras()
        .eliminarPuntuacion()
        .convertirAMinusculas()
        .dividirEnPalabras()
    
    println(palabras) // [hola, mundo]
}
```

**Beneficios de la cohesión secuencial**:

- Flujo de datos claro y predecible
- Fácil de entender (entrada → procesamiento → salida)
- Fácil de testear cada transformación
- Composable (puedes agregar/quitar pasos)


##### 2.2.7. Cohesión Funcional (Nivel 7 - La mejor)

**Definición**: **Todos los elementos del módulo contribuyen a una única tarea o función bien definida**. Es el nivel más alto de cohesión y el objetivo que debemos buscar.

**Características**:

- Una sola responsabilidad bien definida
- Todos los elementos colaboran hacia un único objetivo
- El nombre de la clase describe perfectamente su propósito
- Fácil de entender, mantener, testear y reutilizar

**Ejemplo**: Clase con cohesión funcional perfecta

```kotlin
// COHESIÓN FUNCIONAL - Responsabilidad única y clara
class ValidadorEmail {
    private val patronEmail = Regex("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$")
    
    fun esValido(email: String): Boolean {
        return email.matches(patronEmail)
    }
    
    fun validar(email: String): ResultadoValidacion {
        return when {
            email.isBlank() -> ResultadoValidacion.Invalido("Email no puede estar vacío")
            !email.contains("@") -> ResultadoValidacion.Invalido("Email debe contener @")
            !email.matches(patronEmail) -> ResultadoValidacion.Invalido("Formato de email inválido")
            else -> ResultadoValidacion.Valido
        }
    }
    
    fun extraerDominio(email: String): String? {
        return if (esValido(email)) {
            email.substringAfter("@")
        } else {
            null
        }
    }
}

sealed class ResultadoValidacion {
    object Valido : ResultadoValidacion()
    data class Invalido(val razon: String) : ResultadoValidacion()
}
```

**Análisis**:

- Una responsabilidad: validar emails
- Todos los métodos están relacionados con emails
- Nombre descriptivo y claro
- Fácil de testear
- Reutilizable en cualquier contexto

**Más ejemplos de cohesión funcional**:

```kotlin
// COHESIÓN FUNCIONAL - Calculadora de fechas
class CalculadorFechas {
    fun agregarDias(fecha: java.time.LocalDate, dias: Int): java.time.LocalDate {
        return fecha.plusDays(dias.toLong())
    }
    
    fun calcularDiferenciaEnDias(fecha1: java.time.LocalDate, fecha2: java.time.LocalDate): Long {
        return java.time.temporal.ChronoUnit.DAYS.between(fecha1, fecha2)
    }
    
    fun esFechaLaboral(fecha: java.time.LocalDate): Boolean {
        val diaSemana = fecha.dayOfWeek
        return diaSemana != java.time.DayOfWeek.SATURDAY && 
               diaSemana != java.time.DayOfWeek.SUNDAY
    }
    
    fun proximoDiaLaboral(fecha: java.time.LocalDate): java.time.LocalDate {
        var siguiente = fecha.plusDays(1)
        while (!esFechaLaboral(siguiente)) {
            siguiente = siguiente.plusDays(1)
        }
        return siguiente
    }
}

// COHESIÓN FUNCIONAL - Formateador de números
class FormateadorNumeros(private val locale: java.util.Locale = java.util.Locale("es", "ES")) {
    fun formatearDecimal(numero: Double, decimales: Int = 2): String {
        return String.format(locale, "%.${decimales}f", numero)
    }
    
    fun formatearPorcentaje(numero: Double): String {
        return String.format(locale, "%.2f%%", numero * 100)
    }
    
    fun formatearMoneda(monto: Double, simbolo: String = "€"): String {
        return "${formatearDecimal(monto, 2)} $simbolo"
    }
}

// COHESIÓN FUNCIONAL - Generador de IDs
class GeneradorIdentificadores {
    fun generarUUID(): String {
        return java.util.UUID.randomUUID().toString()
    }
    
    fun generarIdCorto(longitud: Int = 8): String {
        val caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return (1..longitud)
            .map { caracteres.random() }
            .joinToString("")
    }
    
    fun generarIdConPrefijo(prefijo: String): String {
        val timestamp = System.currentTimeMillis()
        val aleatorio = (1000..9999).random()
        return "$prefijo-$timestamp-$aleatorio"
    }
}
```

**Indicadores de cohesión funcional**:

- Puedes describir la clase en una frase sin usar "Y"
- Todos los métodos usan la mayoría de los atributos
- Cambios en un método probablemente afecten a otros (porque están relacionados)
- No hay métodos "huérfanos" que no encajan
- El nombre de la clase es un sustantivo específico (no "Manager", "Handler", "Util")

!!! tip "Regla de oro"
    Si una clase tiene cohesión funcional, respeta automáticamente el Principio de Responsabilidad Única (SRP).


#### 2.3. Cómo mejorar la cohesión

Ahora que conoces los tipos de cohesión, veamos estrategias prácticas para mejorar la cohesión en tu código existente.

##### 2.3.1. Identificar señales de baja cohesión

**Checklist de diagnóstico**:

- [ ] ¿La clase tiene más de 7-10 métodos públicos?
- [ ] ¿El nombre incluye "Manager", "Handler", "Util", "Helper", "Service"?
- [ ] ¿Cuesta trabajo decidir un nombre descriptivo?
- [ ] ¿Hay grupos de métodos que usan diferentes subconjuntos de atributos?
- [ ] ¿La clase cambia frecuentemente por razones no relacionadas?
- [ ] ¿Hay métodos estáticos que no usan atributos de instancia?
- [ ] ¿Necesitas usar "Y" para describir lo que hace la clase?

Si respondiste "sí" a 3 o más preguntas, tu clase tiene problemas de cohesión.

##### 2.3.2. Técnicas de refactorización

**Técnica 1: Extract Class**

Cuando una clase hace demasiadas cosas, extrae funcionalidad en nuevas clases.

```kotlin
// Antes: Baja cohesión
class Usuario(
    var nombre: String,
    var email: String,
    var password: String,
    var ultimoLogin: java.time.LocalDateTime,
    var intentosFallidos: Int
) {
    fun actualizarNombre(nuevoNombre: String) { nombre = nuevoNombre }
    fun actualizarEmail(nuevoEmail: String) { email = nuevoEmail }
    fun validarPassword(pwd: String): Boolean = password == pwd
    fun cambiarPassword(nuevaPassword: String) { password = nuevaPassword }
    fun registrarIntento() { intentosFallidos++ }
    fun resetearIntentos() { intentosFallidos = 0 }
    fun bloquearCuenta() { /* lógica */ }
    fun registrarLogin() { ultimoLogin = java.time.LocalDateTime.now() }
}

// Después: Alta cohesión
data class Usuario(
    val id: Int,
    var nombre: String,
    var email: String
)

class GestorAutenticacion {
    private val passwords = mutableMapOf<Int, String>()
    private val intentos = mutableMapOf<Int, Int>()
    private val bloqueos = mutableSetOf<Int>()
    
    fun validarPassword(usuarioId: Int, password: String): Boolean {
        return passwords[usuarioId] == password
    }
    
    fun cambiarPassword(usuarioId: Int, nuevaPassword: String) {
        require(nuevaPassword.length >= 8) { "Password muy corta" }
        passwords[usuarioId] = nuevaPassword
    }
    
    fun registrarIntentoFallido(usuarioId: Int) {
        intentos[usuarioId] = (intentos[usuarioId] ?: 0) + 1
        if ((intentos[usuarioId] ?: 0) >= 3) {
            bloquearCuenta(usuarioId)
        }
    }
    
    fun bloquearCuenta(usuarioId: Int) {
        bloqueos.add(usuarioId)
    }
    
    fun estaBloqueado(usuarioId: Int): Boolean = usuarioId in bloqueos
}

class RegistroActividad {
    private val logins = mutableMapOf<Int, java.time.LocalDateTime>()
    
    fun registrarLogin(usuarioId: Int) {
        logins[usuarioId] = java.time.LocalDateTime.now()
    }
    
    fun obtenerUltimoLogin(usuarioId: Int): java.time.LocalDateTime? {
        return logins[usuarioId]
    }
}
```

**Técnica 2: Reagrupar métodos por dominio**

Analiza qué métodos trabajan con qué datos y agrúpalos.

```kotlin
// Antes: Métodos mezclados
class GestorPedidos {
    fun validarDireccion(direccion: String): Boolean { /* ... */ }
    fun calcularEnvio(peso: Double): Double { /* ... */ }
    fun aplicarDescuento(total: Double, codigo: String): Double { /* ... */ }
    fun validarStock(producto: String, cantidad: Int): Boolean { /* ... */ }
    fun generarFactura(pedido: Pedido): ByteArray { /* ... */ }
}

// Después: Separados por dominio
class ValidadorDatos {
    fun validarDireccion(direccion: String): Boolean { /* ... */ }
    fun validarStock(producto: String, cantidad: Int): Boolean { /* ... */ }
}

class CalculadoraPreciosEnvio {
    fun calcularEnvio(peso: Double): Double { /* ... */ }
    fun aplicarDescuento(total: Double, codigo: String): Double { /* ... */ }
}

class GeneradorDocumentos {
    fun generarFactura(pedido: Pedido): ByteArray { /* ... */ }
}
```

**Técnica 3: Aplicar el Principio de Responsabilidad Única**

Pregúntate: ¿Esta clase tiene una sola razón para cambiar?

```kotlin
// Antes: Múltiples responsabilidades
class Reporte {
    private val datos: List<Venta> = listOf()
    
    fun cargarDatos() { /* BD */ }
    fun calcularTotal(): Double { /* cálculo */ }
    fun generarPDF(): ByteArray { /* PDF */ }
    fun enviarPorEmail(destinatario: String) { /* email */ }
}

// Después: Una responsabilidad por clase
class RepositorioVentas {
    fun cargarVentas(): List<Venta> { /* BD */ return listOf() }
}

class AnalizadorVentas {
    fun calcularTotal(ventas: List<Venta>): Double { /* cálculo */ return 0.0 }
}

class GeneradorReportePDF {
    fun generar(ventas: List<Venta>): ByteArray { /* PDF */ return byteArrayOf() }
}

class ServicioEmailReportes {
    fun enviar(pdf: ByteArray, destinatario: String) { /* email */ }
}
```


### 3. Acoplamiento: La dependencia entre módulos

#### 3.1. ¿Qué es el acoplamiento?

El **acoplamiento** es una medida del **grado de interdependencia entre módulos**. Indica cuánto conoce un módulo sobre la estructura interna de otro módulo y cuánto depende de él.

##### 3.1.1. Definición formal

**Acoplamiento** = Grado de dependencia que un módulo tiene respecto a otros módulos.

**Alto acoplamiento** significa:
- Los módulos están fuertemente conectados
- Cambios en un módulo requieren cambios en otros
- Difícil de reutilizar módulos de forma independiente
- Testing complejo (necesitas muchos mocks)
- Sistema frágil (cambios causan efectos en cascada)

**Bajo acoplamiento** significa:
- Los módulos son independientes
- Cambios localizados en un módulo
- Fácil de reutilizar y testear
- Sistema robusto y flexible

##### 3.1.2.  Analogías del mundo real

**Analogía 1 - Componentes de computadora**:
- **Bajo acoplamiento**: USB (puedes conectar cualquier dispositivo USB a cualquier puerto USB)
- **Alto acoplamiento**: CPU soldada a la placa madre (cambiar una requiere cambiar la otra)

**Analogía 2 - Muebles**:
- **Bajo acoplamiento**: Muebles modulares IKEA (puedes reemplazar una pieza sin afectar las demás)
- **Alto acoplamiento**: Mueble de madera maciza (todo es una sola pieza)

**Analogía 3 - Restaurante**:
- **Bajo acoplamiento**: Cocina solo conoce el pedido (no sabe quién lo pidió ni cómo pagará)
- **Alto acoplamiento**: Chef que también toma pedidos, cobra y limpia mesas

##### 3.1.3.  ¿Por qué importa el acoplamiento?

El acoplamiento es crítico porque:

1. **Mantenibilidad**: Cambios en un módulo no deberían romper otros
2. **Testeabilidad**: Módulos desacoplados son fáciles de probar
3. **Reusabilidad**: Módulos independientes pueden reutilizarse
4. **Comprensión**: Menos dependencias = más fácil de entender
5. **Desarrollo paralelo**: Equipos pueden trabajar en módulos diferentes

!!! warning "Acoplamiento inevitable"
    Es imposible tener acoplamiento cero (los módulos deben comunicarse). El objetivo es minimizarlo y hacerlo explícito.

##### 3.1.4.  Señales de alto acoplamiento

Identifica problemas cuando:

- ❌ Cambiar una clase requiere cambiar 5-10 clases más
- ❌ No puedes testear una clase sin instanciar otras 10
- ❌ Una clase accede directamente a atributos de otra
- ❌ Muchas clases importan la misma clase concreta
- ❌ Cambios en la base de datos rompen la UI
- ❌ No puedes reutilizar un módulo sin arrastrar medio proyecto

##### 3.1.5.  Ejemplo introductorio

```kotlin
// ❌ ALTO ACOPLAMIENTO - Dependencias directas y rígidas
class ProcesadorPedido {
    private val baseDatos = BaseDatosMySQL()  // Dependencia concreta
    private val emailSender = ServidorEmailSMTP()  // Dependencia concreta
    private val logger = LoggerArchivo()  // Dependencia concreta
    
    fun procesar(pedido: Pedido) {
        // Fuertemente acoplado a implementaciones específicas
        baseDatos.conectar("localhost", "user", "password")
        baseDatos.guardar("INSERT INTO pedidos...")
        
        emailSender.configurar("smtp.gmail.com", 587)
        emailSender.enviar("cliente@example.com", "Pedido confirmado")
        
        logger.escribir("/var/log/app.log", "Pedido procesado: ${pedido.id}")
    }
}

class BaseDatosMySQL {
    fun conectar(host: String, user: String, pwd: String) { /* ... */ }
    fun guardar(sql: String) { /* ... */ }
}

class ServidorEmailSMTP {
    fun configurar(servidor: String, puerto: Int) { /* ... */ }
    fun enviar(destinatario: String, mensaje: String) { /* ... */ }
}

class LoggerArchivo {
    fun escribir(ruta: String, mensaje: String) { /* ... */ }
}
```

**Problemas**:
- Cambiar de MySQL a PostgreSQL requiere modificar ProcesadorPedido
- No puedes testear sin una BD real, servidor SMTP real, etc.
- No puedes reutilizar ProcesadorPedido con otro sistema de email
- Conoce detalles de implementación (hosts, puertos, rutas)

```kotlin
// BAJO ACOPLAMIENTO - Dependencias mediante interfaces
interface RepositorioPedidos {
    fun guardar(pedido: Pedido)
}

interface ServicioEmail {
    fun enviar(destinatario: String, mensaje: String)
}

interface Logger {
    fun log(mensaje: String)
}

class ProcesadorPedido(
    private val repositorio: RepositorioPedidos,
    private val emailService: ServicioEmail,
    private val logger: Logger
) {
    fun procesar(pedido: Pedido) {
        // Desacoplado de implementaciones específicas
        repositorio.guardar(pedido)
        emailService.enviar(pedido.cliente.email, "Pedido confirmado")
        logger.log("Pedido procesado: ${pedido.id}")
    }
}

// Implementaciones concretas
class RepositorioPedidosMySQL : RepositorioPedidos {
    override fun guardar(pedido: Pedido) { /* MySQL */ }
}

class RepositorioPedidosPostgreSQL : RepositorioPedidos {
    override fun guardar(pedido: Pedido) { /* PostgreSQL */ }
}

class ServicioEmailSMTP : ServicioEmail {
    override fun enviar(destinatario: String, mensaje: String) { /* SMTP */ }
}

class LoggerArchivo : Logger {
    override fun log(mensaje: String) { /* File */ }
}

class LoggerConsola : Logger {
    override fun log(mensaje: String) { println(mensaje) }
}

// Uso con inyección de dependencias
fun main() {
    val procesador = ProcesadorPedido(
        repositorio = RepositorioPedidosMySQL(),
        emailService = ServicioEmailSMTP(),
        logger = LoggerConsola()
    )
    
    procesador.procesar(Pedido("P001", Cliente("Juan", "juan@example.com"), listOf()))
}
```

**Beneficios**:
- Cambiar implementaciones no requiere modificar ProcesadorPedido
- Testing fácil con mocks
- Reutilizable con cualquier combinación de servicios
- Respeta el Principio de Inversión de Dependencias

En las siguientes secciones exploraremos los diferentes tipos de acoplamiento y estrategias para reducirlo.


#### 3.2. Tipos de acoplamiento: De peor a mejor

El acoplamiento, al igual que la cohesión, se clasifica en diferentes niveles. Conocer estos tipos te ayudará a identificar y reducir el acoplamiento en tu código.

##### 3.2.1. Tabla resumen de tipos de acoplamiento

| Nivel | Tipo                    | Calidad     | Descripción breve                                    |
|-------|-------------------------|-------------|------------------------------------------------------|
| 1     | Acoplamiento de contenido | ❌ La peor | Un módulo modifica o depende del interior de otro    |
| 2     | Acoplamiento común      | 🔴 Muy malo | Módulos comparten datos globales                     |
| 3     | Acoplamiento externo    | 🟠 Malo     | Dependencia de formato externo compartido            |
| 4     | Acoplamiento de control | 🟡 Regular  | Un módulo controla el flujo de otro con flags        |
| 5     | Acoplamiento de estampado | 🟢 Aceptable | Módulos comparten estructura de datos compleja      |
| 6     | Acoplamiento de datos   | 🔵 Bueno    | Módulos comparten solo datos simples                |
| 7     | Acoplamiento de mensaje | La mejor | Comunicación solo por paso de mensajes/interfaces    |



##### 3.2.2. Acoplamiento de Contenido (Nivel 1 - ❌ La peor)

**Definición**: Un módulo **modifica o accede directamente al interior de otro módulo**, incluyendo sus variables privadas, flujo de control interno, o datos locales.

**Características**:
- Un módulo referencia o altera directamente el contenido de otro
- Acceso a variables privadas/internas
- Saltos a mitad del código de otro módulo
- Extremadamente frágil y difícil de mantener

**Ejemplo típico**: Acceso a miembros privados (simulado con reflexión)

```kotlin
// ❌ ACOPLAMIENTO DE CONTENIDO - Accediendo a privados
class Usuario(private var saldo: Double) {
    fun depositar(monto: Double) {
        if (monto > 0) {
            saldo += monto
        }
    }
    
    fun obtenerSaldo(): Double = saldo
}

class HackerCuenta {
    fun modificarSaldoDirectamente(usuario: Usuario, nuevoSaldo: Double) {
        // En algunos lenguajes esto sería posible con reflexión
        // En Kotlin: acceso mediante reflection (muy malo)
        val campo = Usuario::class.java.getDeclaredField("saldo")
        campo.isAccessible = true
        campo.setDouble(usuario, nuevoSaldo)
        println("Saldo modificado directamente: $nuevoSaldo")
    }
}

// Uso problemático
fun main() {
    val usuario = Usuario(100.0)
    val hacker = HackerCuenta()
    
    println("Saldo inicial: ${usuario.obtenerSaldo()}")
    hacker.modificarSaldoDirectamente(usuario, 1000000.0)
    println("Saldo después de hack: ${usuario.obtenerSaldo()}")
}
```

**Otro ejemplo**: Dependencia de implementación interna

```kotlin
// ❌ ACOPLAMIENTO DE CONTENIDO - Dependiendo de detalles internos
class CarritoCompras {
    // Mal diseño: lista internal expuesta
    internal val items = mutableListOf<Producto>()
    
    fun agregar(producto: Producto) {
        items.add(producto)
    }
}

class CalculadoraDescuentos {
    fun aplicarDescuentoMasivo(carrito: CarritoCompras) {
        // Acoplamiento fuerte: accedemos a internal
        carrito.items.forEach { producto ->
            producto.precio *= 0.9  // 10% descuento
        }
    }
}

data class Producto(var nombre: String, var precio: Double)
```

**Problemas**:
- Rompe completamente la encapsulación
- Cualquier cambio interno rompe el código dependiente
- Imposible de mantener o refactorizar
- Bugs difíciles de rastrear

**Solución - Respetar encapsulación y usar API pública**:

```kotlin
// BAJO ACOPLAMIENTO - Solo API pública
class Usuario(private var saldo: Double) {
    fun depositar(monto: Double): Boolean {
        return if (monto > 0) {
            saldo += monto
            true
        } else {
            false
        }
    }
    
    fun retirar(monto: Double): Boolean {
        return if (monto > 0 && saldo >= monto) {
            saldo -= monto
            true
        } else {
            false
        }
    }
    
    fun obtenerSaldo(): Double = saldo
}

class CarritoCompras {
    private val items = mutableListOf<Producto>()
    
    fun agregar(producto: Producto) {
        items.add(producto)
    }
    
    fun obtenerItems(): List<Producto> = items.toList()  // Copia defensiva
    
    fun aplicarDescuentoTodos(porcentaje: Double) {
        items.forEach { it.aplicarDescuento(porcentaje) }
    }
}

data class Producto(val nombre: String, private var precio: Double) {
    fun obtenerPrecio(): Double = precio
    
    fun aplicarDescuento(porcentaje: Double) {
        if (porcentaje in 0.0..100.0) {
            precio *= (1 - porcentaje / 100)
        }
    }
}
```


##### 3.2.3. Acoplamiento Común (Nivel 2 - 🔴 Muy malo)

**Definición**: Dos o más módulos **comparten datos globales**. Cualquiera puede leer y modificar estos datos, creando dependencias ocultas.

**Características**:
- Variables globales compartidas
- Singletons mutables compartidos
- Estado global compartido
- Efectos colaterales difíciles de rastrear

**Ejemplo típico**: Variables globales

```kotlin
// ❌ ACOPLAMIENTO COMÚN - Variables globales compartidas
object ConfiguracionGlobal {
    var nombreUsuario: String = ""
    var idioma: String = "es"
    var modoDebug: Boolean = false
    var tasaImpuesto: Double = 0.21
}

class ServicioFacturacion {
    fun generarFactura(monto: Double): Double {
        // Depende del estado global
        val impuesto = monto * ConfiguracionGlobal.tasaImpuesto
        return monto + impuesto
    }
}

class ServicioReportes {
    fun generarReporte(): String {
        // También depende del estado global
        return "Reporte generado en ${ConfiguracionGlobal.idioma} " +
               "para ${ConfiguracionGlobal.nombreUsuario}"
    }
}

class PanelAdmin {
    fun cambiarTasaImpuesto(nuevaTasa: Double) {
        // Modifica estado global - afecta a TODOS
        ConfiguracionGlobal.tasaImpuesto = nuevaTasa
        println("Tasa de impuesto cambiada globalmente a $nuevaTasa")
    }
}
```

**Problemas**:
- Cambios en ConfiguracionGlobal afectan a múltiples clases
- Testing complicado (estado compartido entre tests)
- Difícil rastrear quién modifica qué
- Condiciones de carrera en programación concurrente
- Imposible tener configuraciones diferentes simultáneamente

**Otro ejemplo**: Singleton mutable

```kotlin
// ❌ ACOPLAMIENTO COMÚN - Singleton mutable
object CacheGlobal {
    private val cache = mutableMapOf<String, Any>()
    
    fun guardar(clave: String, valor: Any) {
        cache[clave] = valor
    }
    
    fun obtener(clave: String): Any? = cache[clave]
    
    fun limpiar() {
        cache.clear()
    }
}

class ServicioUsuarios {
    fun buscarUsuario(id: String): Usuario? {
        // Usa caché global
        val cached = CacheGlobal.obtener("usuario_$id")
        if (cached != null) return cached as Usuario
        
        val usuario = cargarDesdeBD(id)
        CacheGlobal.guardar("usuario_$id", usuario)
        return usuario
    }
    
    private fun cargarDesdeBD(id: String): Usuario {
        return Usuario(100.0)  // Simulado
    }
}

class ServicioProductos {
    fun buscarProducto(id: String): Producto? {
        // También usa el mismo caché global
        val cached = CacheGlobal.obtener("producto_$id")
        if (cached != null) return cached as Producto
        
        val producto = cargarDesdeBD(id)
        CacheGlobal.guardar("producto_$id", producto)
        return producto
    }
    
    private fun cargarDesdeBD(id: String): Producto {
        return Producto("Producto", 50.0)  // Simulado
    }
}
```

**Solución - Inyección de dependencias**:

```kotlin
// BAJO ACOPLAMIENTO - Configuración inyectada
data class Configuracion(
    val nombreUsuario: String,
    val idioma: String,
    val modoDebug: Boolean,
    val tasaImpuesto: Double
)

class ServicioFacturacion(private val config: Configuracion) {
    fun generarFactura(monto: Double): Double {
        val impuesto = monto * config.tasaImpuesto
        return monto + impuesto
    }
}

class ServicioReportes(private val config: Configuracion) {
    fun generarReporte(): String {
        return "Reporte generado en ${config.idioma} para ${config.nombreUsuario}"
    }
}

// Caché como dependencia inyectable
interface Cache {
    fun guardar(clave: String, valor: Any)
    fun obtener(clave: String): Any?
    fun limpiar()
}

class CacheMemoria : Cache {
    private val cache = mutableMapOf<String, Any>()
    
    override fun guardar(clave: String, valor: Any) {
        cache[clave] = valor
    }
    
    override fun obtener(clave: String): Any? = cache[clave]
    
    override fun limpiar() {
        cache.clear()
    }
}

class ServicioUsuarios(private val cache: Cache) {
    fun buscarUsuario(id: String): Usuario? {
        val cached = cache.obtener("usuario_$id")
        if (cached != null) return cached as Usuario
        
        val usuario = cargarDesdeBD(id)
        cache.guardar("usuario_$id", usuario)
        return usuario
    }
    
    private fun cargarDesdeBD(id: String): Usuario = Usuario(100.0)
}

// Uso
fun main() {
    val config = Configuracion(
        nombreUsuario = "Admin",
        idioma = "es",
        modoDebug = false,
        tasaImpuesto = 0.21
    )
    
    val facturacion = ServicioFacturacion(config)
    val reportes = ServicioReportes(config)
    
    val cache = CacheMemoria()
    val usuarios = ServicioUsuarios(cache)
}
```

**Beneficios**:
- Configuración explícita (no global)
- Testing fácil (cada test con su configuración)
- Sin efectos colaterales ocultos
- Concurrencia segura


##### 3.2.4. Acoplamiento Externo (Nivel 3 - 🟠 Malo)

**Definición**: Módulos dependen de un **formato, protocolo o convención externa** compartida (formato de archivo, estructura de BD, protocolo de comunicación).

**Características**:
- Dependencia de formato de datos externo
- Múltiples módulos conocen la misma estructura externa
- Cambios en el formato externo afectan a todos
- Típico en sistemas legacy

**Ejemplo típico**: Múltiples clases dependiendo del mismo formato de archivo

```kotlin
// ❌ ACOPLAMIENTO EXTERNO - Formato CSV hardcodeado en múltiples lugares
class LectorUsuarios {
    fun leer(archivo: String): List<Usuario> {
        // Lee CSV con formato: id,nombre,email
        val lineas = archivo.split("\n")
        return lineas.map { linea ->
            val partes = linea.split(",")
            Usuario(partes[1], partes[2])
        }
    }
}

class ValidadorUsuarios {
    fun validar(archivo: String): Boolean {
        // También conoce el formato CSV
        val lineas = archivo.split("\n")
        return lineas.all { linea ->
            val partes = linea.split(",")
            partes.size == 3 && partes[2].contains("@")
        }
    }
}

class ExportadorUsuarios {
    fun exportar(usuarios: List<Usuario>): String {
        // También genera el mismo formato CSV
        return usuarios.mapIndexed { index, usuario ->
            "${index + 1},${usuario.nombre},${usuario.email}"
        }.joinToString("\n")
    }
}
```

**Problemas**:
- Cambiar el formato CSV requiere modificar 3 clases
- No hay punto único de responsabilidad
- Difícil mantener consistencia

**Solución - Encapsular el formato en una abstracción**:

```kotlin
// BAJO ACOPLAMIENTO - Formato encapsulado
interface FormatoUsuario {
    fun parsear(contenido: String): List<Usuario>
    fun serializar(usuarios: List<Usuario>): String
}

class FormatoCSVUsuario : FormatoUsuario {
    override fun parsear(contenido: String): List<Usuario> {
        val lineas = contenido.split("\n").filter { it.isNotBlank() }
        return lineas.map { linea ->
            val partes = linea.split(",")
            Usuario(partes[1].trim(), partes[2].trim())
        }
    }
    
    override fun serializar(usuarios: List<Usuario>): String {
        return usuarios.mapIndexed { index, usuario ->
            "${index + 1},${usuario.nombre},${usuario.email}"
        }.joinToString("\n")
    }
}

class FormatoJSONUsuario : FormatoUsuario {
    override fun parsear(contenido: String): List<Usuario> {
        // Parseo JSON (simulado)
        return listOf()
    }
    
    override fun serializar(usuarios: List<Usuario>): String {
        return usuarios.joinToString(",\n", "[\n", "\n]") { usuario ->
            """  {"nombre": "${usuario.nombre}", "email": "${usuario.email}"}"""
        }
    }
}

class GestorUsuarios(private val formato: FormatoUsuario) {
    fun importar(contenido: String): List<Usuario> {
        return formato.parsear(contenido)
    }
    
    fun exportar(usuarios: List<Usuario>): String {
        return formato.serializar(usuarios)
    }
    
    fun validar(contenido: String): Boolean {
        return try {
            val usuarios = formato.parsear(contenido)
            usuarios.all { it.email.contains("@") }
        } catch (e: Exception) {
            false
        }
    }
}

// Uso
fun main() {
    // Con CSV
    val gestorCSV = GestorUsuarios(FormatoCSVUsuario())
    val usuariosCSV = gestorCSV.importar("1,Juan,juan@example.com\n2,Ana,ana@example.com")
    
    // Con JSON (mismo gestor, diferente formato)
    val gestorJSON = GestorUsuarios(FormatoJSONUsuario())
    val exportadoJSON = gestorJSON.exportar(usuariosCSV)
    println(exportadoJSON)
}
```

**Beneficios**:
- Cambiar formato solo requiere cambiar una clase
- Fácil agregar nuevos formatos (XML, YAML, etc.)
- Gestor desacoplado del formato específico


##### 3.2.5. Acoplamiento de Control (Nivel 4 - 🟡 Regular)

**Definición**: Un módulo **controla el comportamiento de otro** pasando flags o parámetros de control que determinan qué hace el módulo llamado.

**Características**:
- Un módulo dice a otro QUÉ hacer (no CÓMO)
- Flags booleanos o códigos de operación
- El llamador conoce la lógica interna del llamado
- Viola el principio de "Tell, Don't Ask"

**Ejemplo típico**: Métodos con flags booleanos

```kotlin
// ❌ ACOPLAMIENTO DE CONTROL - Flag controla el comportamiento
class ServicioEmail {
    fun enviar(
        destinatario: String,
        mensaje: String,
        urgente: Boolean,
        conCopia: Boolean,
        adjuntar: Boolean
    ) {
        println("Enviando email a $destinatario")
        println("Mensaje: $mensaje")
        
        if (urgente) {
            println("Marcando como urgente")
        }
        
        if (conCopia) {
            println("Enviando copia a admin@empresa.com")
        }
        
        if (adjuntar) {
            println("Adjuntando archivo")
        }
    }
}

// Uso confuso
fun main() {
    val servicio = ServicioEmail()
    servicio.enviar("user@example.com", "Hola", true, false, true)  // ¿Qué significa esto?
    servicio.enviar("otro@example.com", "Mensaje", false, true, false)
}
```

**Problemas**:
- El llamador conoce detalles de implementación
- Métodos difíciles de leer (`true`, `false` no descriptivos)
- Difícil de extender (nuevo comportamiento = nuevo flag)

**Solución - Polimorfismo o clases especializadas**:

```kotlin
// BAJO ACOPLAMIENTO - Polimorfismo y composición
interface ConfiguracionEmail {
    fun aplicar(builder: EmailBuilder)
}

class EmailBuilder {
    var destinatario: String = ""
    var mensaje: String = ""
    var prioridad: Prioridad = Prioridad.NORMAL
    var copias: List<String> = emptyList()
    var adjuntos: List<String> = emptyList()
    
    fun build(): Email = Email(destinatario, mensaje, prioridad, copias, adjuntos)
}

enum class Prioridad { BAJA, NORMAL, ALTA, URGENTE }

data class Email(
    val destinatario: String,
    val mensaje: String,
    val prioridad: Prioridad,
    val copias: List<String>,
    val adjuntos: List<String>
)

class ConfiguracionEmailUrgente : ConfiguracionEmail {
    override fun aplicar(builder: EmailBuilder) {
        builder.prioridad = Prioridad.URGENTE
        builder.copias = listOf("admin@empresa.com", "manager@empresa.com")
    }
}

class ConfiguracionEmailConAdjunto(private val rutaArchivo: String) : ConfiguracionEmail {
    override fun aplicar(builder: EmailBuilder) {
        builder.adjuntos = listOf(rutaArchivo)
    }
}

class ServicioEmail {
    fun enviar(email: Email) {
        println("Enviando email a ${email.destinatario}")
        println("Mensaje: ${email.mensaje}")
        println("Prioridad: ${email.prioridad}")
        
        if (email.copias.isNotEmpty()) {
            println("Con copia a: ${email.copias.joinToString()}")
        }
        
        if (email.adjuntos.isNotEmpty()) {
            println("Adjuntos: ${email.adjuntos.joinToString()}")
        }
    }
}

// Uso más claro
fun main() {
    val servicio = ServicioEmail()
    
    // Email simple
    val emailSimple = EmailBuilder().apply {
        destinatario = "user@example.com"
        mensaje = "Hola"
    }.build()
    servicio.enviar(emailSimple)
    
    // Email urgente con configuración
    val builderUrgente = EmailBuilder().apply {
        destinatario = "user@example.com"
        mensaje = "¡Urgente!"
    }
    ConfiguracionEmailUrgente().aplicar(builderUrgente)
    servicio.enviar(builderUrgente.build())
    
    // Email con adjunto
    val builderAdjunto = EmailBuilder().apply {
        destinatario = "user@example.com"
        mensaje = "Documento adjunto"
    }
    ConfiguracionEmailConAdjunto("/ruta/documento.pdf").aplicar(builderAdjunto)
    servicio.enviar(builderAdjunto.build())
}
```

**Beneficios**:
- Código más legible y autodocumentado
- Fácil de extender (nueva configuración = nueva clase)
- Sin flags booleanos confusos



##### 3.2.6. Acoplamiento de Estampado/Stamp (Nivel 5 - 🟢 Aceptable)

**Definición**: Los módulos comparten una **estructura de datos compleja**, pero cada módulo solo usa parte de ella.

**Características**:
- Se pasa un objeto completo pero solo se usan algunos campos
- Más acoplamiento del necesario
- Cambios en la estructura afectan a módulos que no la usan completamente

**Ejemplo típico**: Pasar objeto completo cuando solo se necesitan algunos campos

```kotlin
// ⚠️ ACOPLAMIENTO DE ESTAMPADO - Objeto completo innecesario
data class Pedido(
    val id: String,
    val cliente: Cliente,
    val items: List<ItemPedido>,
    val fechaPedido: java.time.LocalDateTime,
    val estado: EstadoPedido,
    val metodoPago: String,
    val direccionEnvio: Direccion,
    val notas: String
)

data class Cliente(val id: String, val nombre: String, val email: String)
data class ItemPedido(val productoId: String, val cantidad: Int, val precio: Double)
data class Direccion(val calle: String, val ciudad: String, val codigoPostal: String)
enum class EstadoPedido { PENDIENTE, PROCESANDO, ENVIADO, ENTREGADO }

class CalculadoraEnvio {
    // Solo necesita la dirección, pero recibe el pedido completo
    fun calcularCosto(pedido: Pedido): Double {
        val direccion = pedido.direccionEnvio
        return when (direccion.ciudad) {
            "Madrid" -> 5.0
            "Barcelona" -> 7.0
            else -> 10.0
        }
    }
}

class GeneradorEtiqueta {
    // Solo necesita nombre del cliente y dirección
    fun generar(pedido: Pedido): String {
        return """
            ${pedido.cliente.nombre}
            ${pedido.direccionEnvio.calle}
            ${pedido.direccionEnvio.ciudad}, ${pedido.direccionEnvio.codigoPostal}
        """.trimIndent()
    }
}

class ValidadorInventario {
    // Solo necesita los items
    fun verificar(pedido: Pedido): Boolean {
        return pedido.items.all { item ->
            verificarDisponibilidad(item.productoId, item.cantidad)
        }
    }
    
    private fun verificarDisponibilidad(productoId: String, cantidad: Int): Boolean = true
}
```

**Problemas**:
- Más acoplamiento del necesario
- Cambios en Pedido pueden afectar a clases que no usan esos cambios
- No está claro qué campos usa realmente cada clase

**Solución - Pasar solo lo necesario**:

```kotlin
// BAJO ACOPLAMIENTO - Solo datos necesarios
class CalculadoraEnvio {
    fun calcularCosto(direccion: Direccion): Double {
        return when (direccion.ciudad) {
            "Madrid" -> 5.0
            "Barcelona" -> 7.0
            else -> 10.0
        }
    }
}

class GeneradorEtiqueta {
    fun generar(nombreCliente: String, direccion: Direccion): String {
        return """
            $nombreCliente
            ${direccion.calle}
            ${direccion.ciudad}, ${direccion.codigoPostal}
        """.trimIndent()
    }
}

class ValidadorInventario {
    fun verificar(items: List<ItemPedido>): Boolean {
        return items.all { item ->
            verificarDisponibilidad(item.productoId, item.cantidad)
        }
    }
    
    private fun verificarDisponibilidad(productoId: String, cantidad: Int): Boolean = true
}

// Uso
fun main() {
    val pedido = Pedido(
        id = "P001",
        cliente = Cliente("C001", "Juan Pérez", "juan@example.com"),
        items = listOf(ItemPedido("PROD1", 2, 50.0)),
        fechaPedido = java.time.LocalDateTime.now(),
        estado = EstadoPedido.PENDIENTE,
        metodoPago = "Tarjeta",
        direccionEnvio = Direccion("Calle Mayor 1", "Madrid", "28001"),
        notas = ""
    )
    
    // Cada servicio recibe solo lo que necesita
    val calculadora = CalculadoraEnvio()
    val costoEnvio = calculadora.calcularCosto(pedido.direccionEnvio)
    
    val generador = GeneradorEtiqueta()
    val etiqueta = generador.generar(pedido.cliente.nombre, pedido.direccionEnvio)
    
    val validador = ValidadorInventario()
    val disponible = validador.verificar(pedido.items)
}
```

**Beneficios**:
- Dependencias explícitas y mínimas
- Cambios en Pedido no afectan a estas clases
- Más fácil de testear (menos datos que preparar)


##### 3.2.7. Acoplamiento de Datos (Nivel 6 - 🔵 Bueno)

**Definición**: Los módulos se comunican solo mediante **parámetros de datos simples** (primitivos, strings, listas simples).

**Características**:
- Parámetros simples y claros
- Sin estructuras complejas compartidas
- Mínima interdependencia
- Buen nivel de acoplamiento

**Ejemplo**:

```kotlin
// ACOPLAMIENTO DE DATOS - Parámetros simples
class Calculadora {
    fun sumar(a: Int, b: Int): Int = a + b
    
    fun calcularPorcentaje(valor: Double, porcentaje: Double): Double {
        return valor * (porcentaje / 100)
    }
}

class ValidadorTexto {
    fun esEmailValido(email: String): Boolean {
        return email.matches(Regex("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$"))
    }
    
    fun longitudValida(texto: String, minimo: Int, maximo: Int): Boolean {
        return texto.length in minimo..maximo
    }
}

class FormateadorFecha {
    fun formatear(anio: Int, mes: Int, dia: Int): String {
        return String.format("%04d-%02d-%02d", anio, mes, dia)
    }
}
```

**Ventajas**:
- Completamente desacoplado
- Fácil de entender y mantener
- Reutilizable en cualquier contexto
- Testing trivial


##### 3.2.8. Acoplamiento de Mensaje (Nivel 7 - La mejor)

**Definición**: La comunicación se realiza únicamente mediante **paso de mensajes** o a través de **interfaces**, sin conocer implementaciones concretas.

**Características**:
- Comunicación mediante interfaces
- No se conocen implementaciones
- Máxima flexibilidad
- Principio de Inversión de Dependencias

**Ejemplo perfecto**:

```kotlin
// ACOPLAMIENTO DE MENSAJE - Solo interfaces
interface RepositorioUsuarios {
    fun guardar(usuario: Usuario)
    fun buscarPorEmail(email: String): Usuario?
    fun listarTodos(): List<Usuario>
}

interface Notificador {
    fun notificar(destinatario: String, mensaje: String)
}

interface Validador {
    fun validar(dato: Any): ResultadoValidacion
}

// Servicio que solo depende de interfaces
class ServicioRegistro(
    private val repositorio: RepositorioUsuarios,
    private val notificador: Notificador,
    private val validador: Validador
) {
    fun registrar(usuario: Usuario): Boolean {
        // Validar
        val resultado = validador.validar(usuario)
        if (resultado is ResultadoValidacion.Invalido) {
            return false
        }
        
        // Guardar
        repositorio.guardar(usuario)
        
        // Notificar
        notificador.notificar(usuario.email, "Bienvenido ${usuario.nombre}")
        
        return true
    }
}

// Implementaciones intercambiables
class RepositorioUsuariosMemoria : RepositorioUsuarios {
    private val usuarios = mutableListOf<Usuario>()
    
    override fun guardar(usuario: Usuario) {
        usuarios.add(usuario)
    }
    
    override fun buscarPorEmail(email: String): Usuario? {
        return usuarios.find { it.email == email }
    }
    
    override fun listarTodos(): List<Usuario> = usuarios.toList()
}

class NotificadorEmail : Notificador {
    override fun notificar(destinatario: String, mensaje: String) {
        println("Email enviado a $destinatario: $mensaje")
    }
}

class NotificadorSMS : Notificador {
    override fun notificar(destinatario: String, mensaje: String) {
        println("SMS enviado a $destinatario: $mensaje")
    }
}

class ValidadorUsuario : Validador {
    override fun validar(dato: Any): ResultadoValidacion {
        if (dato !is Usuario) return ResultadoValidacion.Invalido("Tipo inválido")
        if (dato.nombre.isBlank()) return ResultadoValidacion.Invalido("Nombre requerido")
        if (!dato.email.contains("@")) return ResultadoValidacion.Invalido("Email inválido")
        return ResultadoValidacion.Exitoso
    }
}

// Uso con total flexibilidad
fun main() {
    // Configuración 1: Memoria + Email
    val servicio1 = ServicioRegistro(
        repositorio = RepositorioUsuariosMemoria(),
        notificador = NotificadorEmail(),
        validador = ValidadorUsuario()
    )
    
    // Configuración 2: Memoria + SMS (sin cambiar ServicioRegistro)
    val servicio2 = ServicioRegistro(
        repositorio = RepositorioUsuariosMemoria(),
        notificador = NotificadorSMS(),
        validador = ValidadorUsuario()
    )
    
    val usuario = Usuario(100.0)
    usuario.nombre = "Juan"
    usuario.email = "juan@example.com"
    
    servicio1.registrar(usuario)
}
```

**Beneficios máximos**:
- Completamente desacoplado
- Implementaciones intercambiables
- Testing con mocks trivial
- Máxima flexibilidad y extensibilidad


#### 3.3. Estrategias para reducir el acoplamiento

Para lograr un bajo acoplamiento, puedes aplicar varias estrategias y patrones de diseño. Aquí te presento algunas de las más efectivas

##### 3.3.1. Inyección de Dependencias (DI)

No crees tus dependencias, recíbelas desde fuera:

```kotlin
// ❌ Sin DI - Alto acoplamiento
class Servicio {
    private val repositorio = RepositorioMySQL()  // Dependencia concreta
    
    fun hacer() {
        repositorio.guardar()
    }
}

// Con DI - Bajo acoplamiento
class Servicio(private val repositorio: Repositorio) {  // Interfaz
    fun hacer() {
        repositorio.guardar()
    }
}
```

##### 3.3.2. Principio de Inversión de Dependencias (DIP)

Depende de abstracciones, no de concreciones:

```kotlin
// ❌ Depende de concreción
class Notificador {
    fun notificar(email: ServicioEmailSMTP) {
        email.enviar("mensaje")
    }
}

// Depende de abstracción
interface ServicioEmail {
    fun enviar(mensaje: String)
}

class Notificador(private val servicioEmail: ServicioEmail) {
    fun notificar(mensaje: String) {
        servicioEmail.enviar(mensaje)
    }
}
```

##### 3.3.3. Ley de Demeter (Principle of Least Knowledge)

No hables con extraños, solo con amigos directos:

```kotlin
// ❌ Viola Ley de Demeter
class Cliente {
    fun procesarPago(pedido: Pedido) {
        val monto = pedido.carrito.items.sumOf { it.precio }  // Cadena larga
        println("Procesando $monto")
    }
}

// Respeta Ley de Demeter
class Pedido {
    fun calcularTotal(): Double {
        return carrito.calcularTotal()
    }
}

class Cliente {
    fun procesarPago(pedido: Pedido) {
        val monto = pedido.calcularTotal()  // Solo un nivel
        println("Procesando $monto")
    }
}
```

##### 3.3.4. Facade Pattern

Simplifica interfaces complejas:

```kotlin
// Sistema complejo
class SubsistemaA { fun operacion1() {} }
class SubsistemaB { fun operacion2() {} }
class SubsistemaC { fun operacion3() {} }

// Facade simplifica el acceso
class FachadeSistema {
    private val subsistemaA = SubsistemaA()
    private val subsistemaB = SubsistemaB()
    private val subsistemaC = SubsistemaC()
    
    fun operacionSimplificada() {
        subsistemaA.operacion1()
        subsistemaB.operacion2()
        subsistemaC.operacion3()
    }
}

// Cliente solo conoce la fachada
class Cliente(private val fachada: FachadeSistema) {
    fun hacer() {
        fachada.operacionSimplificada()
    }
}
```


### 4. La relación entre Cohesión y Acoplamiento

#### 4.1. Matriz de calidad del diseño

La calidad del diseño depende de la combinación de cohesión y acoplamiento:

| Cohesión \ Acoplamiento  | **Bajo Acoplamiento**                                                                                  | **Alto Acoplamiento**                                                                     |
|--------------------------|--------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| **Alta Cohesión**        | **EXCELENTE**<br/>Módulos independientes con propósito claro<br/>Fácil mantener, testear, reutilizar | ⚠️ **BUENO**<br/>Módulos cohesivos pero dependientes<br/>Mantener es viable pero complejo |
| **Baja Cohesión**        | ⚠️ **REGULAR**<br/>Módulos independientes pero confusos<br/>Difícil entender qué hacen                 | ❌ **MALO**<br/>Módulos confusos y dependientes<br/>Código espagueti, imposible mantener   |

#### 4.2. Trade-offs y decisiones

**¿Cuándo es aceptable tener algo de acoplamiento?**

- Cuando dos módulos están intrínsecamente relacionados por el dominio
- En frameworks donde el acoplamiento está controlado por convención
- Cuando la performance es crítica y el desacoplamiento tiene coste

**¿Cuándo es aceptable tener cohesión media?**

- En clases de utilidad bien documentadas
- En coordinadores o orquestadores (su trabajo es coordinar)
- En adaptadores entre sistemas

!!! tip "Regla práctica"
    Prioriza siempre la alta cohesión sobre el bajo acoplamiento. Es mejor tener módulos cohesivos ligeramente acoplados que módulos desacoplados pero confusos.


### 5. Principios de Diseño Relacionados

Tantos la cohesión como el acoplamiento están influenciados por varios principios de diseño de software. Aquí exploramos algunos de los más relevantes.

#### 5.1. Principio de Responsabilidad Única (SRP)

**Definición**: Una clase debe tener una sola razón para cambiar.

**Relación**: El SRP promueve directamente la **alta cohesión**. Si una clase tiene una responsabilidad única, automáticamente tendrá alta cohesión funcional.

**Ejemplo**:

```kotlin
// SRP + Alta Cohesión
class ValidadorEmail {
    fun esValido(email: String): Boolean = email.contains("@")
    fun extraerDominio(email: String): String? = email.substringAfter("@", "")
}
```

#### 5.2. Principio de Inversión de Dependencias (DIP)

**Definición**: Depender de abstracciones, no de concreciones.

**Relación**: El DIP reduce directamente el **acoplamiento**. Al depender de interfaces en lugar de implementaciones, los módulos se vuelven independientes.

**Ejemplo**:

```kotlin
// DIP + Bajo Acoplamiento
interface Repositorio {
    fun guardar(dato: Any)
}

class Servicio(private val repositorio: Repositorio) {  // Depende de abstracción
    fun procesar(dato: Any) {
        repositorio.guardar(dato)
    }
}
```

#### 5.3. Principio de Segregación de Interfaces (ISP)

**Definición**: Los clientes no deben depender de interfaces que no usan.

**Relación**: El ISP reduce el **acoplamiento innecesario**. Interfaces pequeñas y específicas minimizan las dependencias.

**Ejemplo**:

```kotlin
// ❌ Interfaz gorda - acoplamiento innecesario
interface Trabajador {
    fun trabajar()
    fun comer()
    fun dormir()
}

class Robot : Trabajador {
    override fun trabajar() { /* OK */ }
    override fun comer() { /* No aplica */ }  // ❌
    override fun dormir() { /* No aplica */ }  // ❌
}

// Interfaces segregadas
interface Trabajador {
    fun trabajar()
}

interface SerVivo {
    fun comer()
    fun dormir()
}

class Robot : Trabajador {
    override fun trabajar() { /* OK */ }
}

class Humano : Trabajador, SerVivo {
    override fun trabajar() { /* OK */ }
    override fun comer() { /* OK */ }
    override fun dormir() { /* OK */ }
}
```


### 6. Métricas y Medición

#### 6.1. Métricas de Cohesión

##### 6.1.1. LCOM (Lack of Cohesion of Methods)

**Definición**: Mide cuántos métodos de una clase NO comparten atributos.

**Cálculo simplificado**:
```
LCOM = (Pares de métodos que NO comparten atributos) - 
       (Pares de métodos que SÍ comparten atributos)
```

**Interpretación**:

- **LCOM = 0**: Perfecta cohesión (todos los métodos usan todos los atributos)
- **LCOM bajo (< 50)**: Buena cohesión
- **LCOM alto (> 100)**: Baja cohesión (considerar dividir la clase)

**Ejemplo**:

```kotlin
// LCOM bajo - Alta cohesión
class Rectangulo(
    private var ancho: Double,
    private var alto: Double
) {
    // Todos los métodos usan ambos atributos
    fun calcularArea(): Double = ancho * alto
    fun calcularPerimetro(): Double = 2 * (ancho + alto)
    fun escalar(factor: Double) {
        ancho *= factor
        alto *= factor
    }
}

// ❌ LCOM alto - Baja cohesión
class Utilidades(
    private var contador: Int,
    private var email: String
) {
    // incrementar() solo usa contador
    fun incrementar() { contador++ }
    
    // validarEmail() solo usa email
    fun validarEmail(): Boolean = email.contains("@")
    
    // No hay métodos que usen ambos atributos - LCOM alto
}
```

#### 6.2. Métricas de Acoplamiento

Las métricas de acoplamiento miden las dependencias entre clases o módulos.

##### 6.2.1.  Acoplamiento Aferente (Ca)

**Definición**: Número de clases externas que **dependen de** esta clase.

**Interpretación**:

- **Ca alto**: Clase estable, muchas otras dependen de ella. Por lo tanto, menos propensa a cambios. Esto es bueno para clases de bajo nivel (utilidades, frameworks).
- **Ca bajo**: Clase volátil, pocas dependen de ella. Por lo tanto, más propensa a cambios. Esto es aceptable para clases de alto nivel (coordinadores).

##### 6.2.2.  Acoplamiento Eferente (Ce)

**Definición**: Número de clases externas de las que **depende** esta clase.

**Interpretación**:

- **Ce alto**: Clase dependiente, usa muchas otras
- **Ce bajo**: Clase independiente

##### 6.2.3.  Inestabilidad (I)

**Fórmula**: `I = Ce / (Ca + Ce)`

**Interpretación**:

- **I = 0**: Clase máximamente estable (muchas dependen de ella, depende de pocas)
- **I = 1**: Clase máximamente inestable (pocas dependen de ella, depende de muchas)

**Objetivo**:

- Clases de bajo nivel (utilidades, frameworks): I cercano a 0
- Clases de alto nivel (coordinadores): I puede ser mayor

**Ejemplo**:

```
Clase A:
- Ca = 5 (5 clases la usan)
- Ce = 1 (usa 1 clase)
- I = 1 / (5 + 1) = 0.16 → Muy estable

Clase B:
- Ca = 1 (1 clase la usa)
- Ce = 10 (usa 10 clases)
- I = 10 / (1 + 10) = 0.91 → Muy inestable
```

#### 6.3. Herramientas de análisis

**Para Kotlin/Java**:

- **SonarQube**: Análisis continuo de calidad, reporta LCOM, complejidad, acoplamiento
- **IntelliJ IDEA**: Inspecciones integradas, análisis de dependencias
- **Detekt**: Linter para Kotlin, detecta code smells
- **JDepend**: Analiza métricas de acoplamiento

**Comandos útiles**:

```bash
# Detekt
./gradlew detekt

# SonarQube
./gradlew sonarqube

# IntelliJ - Analyze → Inspect Code
```


### 7. Casos Prácticos de Refactorización

#### 7.1. Caso: Sistema de Pedidos

**Antes - Alto acoplamiento y baja cohesión**:

```kotlin
// ❌ Clase monolítica con múltiples responsabilidades
class SistemaVentas {
    private val conexionBD = "jdbc:mysql://localhost/ventas"
    
    fun procesarVenta(clienteId: Int, productos: List<Int>) {
        // 1. Validar cliente
        val cliente = buscarEnBD("SELECT * FROM clientes WHERE id = $clienteId")
        if (cliente == null) {
            println("Cliente no existe")
            return
        }
        
        // 2. Validar stock
        for (productoId in productos) {
            val stock = buscarEnBD("SELECT stock FROM productos WHERE id = $productoId")
            if (stock == null || stock.toInt() <= 0) {
                println("Sin stock")
                return
            }
        }
        
        // 3. Calcular total
        var total = 0.0
        for (productoId in productos) {
            val precio = buscarEnBD("SELECT precio FROM productos WHERE id = $productoId")
            total += precio?.toDouble() ?: 0.0
        }
        val impuesto = total * 0.21
        val totalFinal = total + impuesto
        
        // 4. Guardar pedido
        ejecutarSQL("INSERT INTO pedidos (cliente_id, total) VALUES ($clienteId, $totalFinal)")
        
        // 5. Enviar email
        println("Enviando email a cliente $clienteId")
        
        // 6. Generar factura PDF
        println("Generando PDF...")
    }
    
    private fun buscarEnBD(sql: String): String? = "resultado"
    private fun ejecutarSQL(sql: String) { println("Ejecutando: $sql") }
}
```

**Después - Bajo acoplamiento y alta cohesión**:

```kotlin
// Responsabilidades separadas

// 1. Entidades del dominio
data class Cliente(val id: Int, val nombre: String, val email: String)
data class Producto(val id: Int, val nombre: String, val precio: Double, val stock: Int)
data class Pedido(val id: Int, val cliente: Cliente, val items: List<ItemPedido>, val total: Double)
data class ItemPedido(val producto: Producto, val cantidad: Int)

// 2. Repositorios
interface RepositorioClientes {
    fun buscarPorId(id: Int): Cliente?
}

interface RepositorioProductos {
    fun buscarPorId(id: Int): Producto?
    fun verificarStock(id: Int, cantidad: Int): Boolean
}

interface RepositorioPedidos {
    fun guardar(pedido: Pedido): Int
}

// 3. Servicios especializados
class ValidadorPedido {
    fun validarCliente(cliente: Cliente?): Boolean = cliente != null
    fun validarStock(items: List<ItemPedido>): Boolean {
        return items.all { it.producto.stock >= it.cantidad }
    }
}

class CalculadoraPrecios {
    private val tasaImpuesto = 0.21
    
    fun calcularTotal(items: List<ItemPedido>): Double {
        val subtotal = items.sumOf { it.producto.precio * it.cantidad }
        return subtotal + (subtotal * tasaImpuesto)
    }
}

class ServicioNotificaciones {
    fun enviarConfirmacion(cliente: Cliente, pedido: Pedido) {
        println("Email enviado a ${cliente.email}: Pedido ${pedido.id} confirmado")
    }
}

class GeneradorFacturas {
    fun generar(pedido: Pedido): ByteArray {
        println("Generando factura PDF para pedido ${pedido.id}")
        return byteArrayOf()
    }
}

// 4. Orquestador con dependencias inyectadas
class ServicioPedidos(
    private val repoClientes: RepositorioClientes,
    private val repoProductos: RepositorioProductos,
    private val repoPedidos: RepositorioPedidos,
    private val validador: ValidadorPedido,
    private val calculadora: CalculadoraPrecios,
    private val notificaciones: ServicioNotificaciones,
    private val generadorFacturas: GeneradorFacturas
) {
    fun procesarPedido(clienteId: Int, productosIds: List<Int>): Pedido? {
        // 1. Buscar cliente
        val cliente = repoClientes.buscarPorId(clienteId)
        if (!validador.validarCliente(cliente)) {
            println("Cliente inválido")
            return null
        }
        
        // 2. Buscar productos
        val productos = productosIds.mapNotNull { repoProductos.buscarPorId(it) }
        val items = productos.map { ItemPedido(it, 1) }
        
        // 3. Validar stock
        if (!validador.validarStock(items)) {
            println("Stock insuficiente")
            return null
        }
        
        // 4. Calcular total
        val total = calculadora.calcularTotal(items)
        
        // 5. Crear y guardar pedido
        val pedido = Pedido(0, cliente!!, items, total)
        val pedidoId = repoPedidos.guardar(pedido)
        val pedidoGuardado = pedido.copy(id = pedidoId)
        
        // 6. Notificaciones
        notificaciones.enviarConfirmacion(cliente, pedidoGuardado)
        generadorFacturas.generar(pedidoGuardado)
        
        return pedidoGuardado
    }
}
```

**Beneficios**:

- **Alta cohesión**: Cada clase tiene una responsabilidad única
- **Bajo acoplamiento**: Dependencias mediante interfaces
- **Testeable**: Cada componente puede testearse independientemente
- **Mantenible**: Cambios localizados
- **Extensible**: Fácil agregar nuevas funcionalidades


### 8. Conclusiones

#### 8.1. Resumen de conceptos clave

**Cohesión**: Qué tan relacionados están los elementos dentro de un módulo

- **Objetivo**: Alta cohesión funcional
- **Técnica**: Una responsabilidad por clase (SRP)
- **Beneficio**: Código claro y fácil de mantener

**Acoplamiento**: Qué tan interdependientes son los módulos

- **Objetivo**: Bajo acoplamiento de mensaje
- **Técnica**: Depender de abstracciones (DIP)
- **Beneficio**: Código flexible y testeatable

**Balance ideal**: Alta cohesión + Bajo acoplamiento = Código excelente

#### 8.2. Checklist de diseño

Usa este checklist al diseñar o revisar código:

**Cohesión**:

- [ ] ¿La clase tiene un nombre descriptivo sin "Y"?
- [ ] ¿Todos los métodos están relacionados con el propósito de la clase?
- [ ] ¿Hay una razón única para que la clase cambie?
- [ ] ¿Los métodos comparten los mismos atributos?

**Acoplamiento**:

- [ ] ¿Las dependencias son interfaces, no clases concretas?
- [ ] ¿Las dependencias se inyectan, no se crean?
- [ ] ¿Se pasan solo los datos necesarios?
- [ ] ¿Se puede testear la clase sin instanciar medio proyecto?


### 9. Recursos y Referencias

#### 9.1. Libros fundamentales

- **[Refactoring: Improving the Design of Existing Code](https://refactoring.com/)** - Martin Fowler

    - Catálogo completo de refactorizaciones para mejorar diseño
  
- **[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** - Robert C. Martin

    - Principios de arquitectura limpia y desacoplada
  
- **[Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)** - Robert C. Martin

    - Manual definitivo sobre código limpio y mantenible

- **[Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns)** - Gang of Four

    - Patrones clásicos para bajo acoplamiento

#### 9.2.  Artículos esenciales

- [SOLID Principles](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
- [Coupling and Cohesion](https://martinfowler.com/bliki/CouplingAndCohesion.html) - Martin Fowler
- [Cohesion and Coupling](https://www.baeldung.com/cs/cohesion-vs-coupling) - Baeldung

#### 9.3. Herramientas recomendadas

**Análisis de código**:

- [SonarQube](https://www.sonarqube.org/) - Análisis continuo de calidad
- [IntelliJ IDEA](https://www.jetbrains.com/idea/) - Inspecciones integradas
- [Detekt](https://detekt.dev/) - Linter para Kotlin
- [PMD](https://pmd.github.io/) - Detector de code smells

**Visualización**:

- [Structure101](https://structure101.com/) - Visualización de dependencias
- [JDepend](https://github.com/clarkware/jdepend) - Métricas de acoplamiento

#### 9.4. Comunidades y foros

- [Stack Overflow - design-patterns](https://stackoverflow.com/questions/tagged/design-patterns)
- [Reddit - r/programming](https://www.reddit.com/r/programming/)
- [Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/)

