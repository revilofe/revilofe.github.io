---
title: "UD 3 - 3.4 Acoplamiento y Cohesión"
description: Acoplamiento y Cohesión en el Diseño de Software
summary: Principios de diseño de software - Alta cohesión y bajo acoplamiento
authors:
    - Eduardo Fdez
date: 2024-11-03
icon:   
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

### Introducción

En el desarrollo de software, dos conceptos fundamentales que determinan la calidad del diseño son el **acoplamiento** y la **cohesión**. Estos principios nos ayudan a crear sistemas más mantenibles, comprensibles y flexibles.

!!! note "Principio clave"
    Un buen diseño de software debe buscar **bajo acoplamiento** y **alta cohesión**.

**Objetivos de un buen diseño**:
- **Bajo acoplamiento**: Minimizar las dependencias entre módulos
- **Alta cohesión**: Maximizar la relación entre los elementos dentro de un mismo módulo

## 1. Cohesión

### 1.1. ¿Qué es la cohesión?

La **cohesión** es una medida que indica cuán relacionados están los elementos dentro de un mismo módulo, clase o componente. Una alta cohesión significa que los elementos del módulo están fuertemente relacionados y trabajan juntos para cumplir un propósito específico y bien definido.

### 1.2. Tipos de cohesión

La cohesión se puede clasificar en diferentes niveles, **ordenados de menor a mayor calidad**:

| Nivel  | Tipo                    | Calidad       |
|--------|-------------------------|---------------|
| 1      | Cohesión coincidental   | ❌ La peor     |
| 2      | Cohesión lógica         | 🔴 Muy baja   |
| 3      | Cohesión temporal       | 🟠 Baja       |
| 4      | Cohesión procedimental  | 🟡 Media-baja |
| 5      | Cohesión comunicacional | 🟢 Media      |
| 6      | Cohesión secuencial     | 🔵 Alta       |
| 7      | Cohesión funcional      | ✅ La mejor    |

#### 1.2.1. Cohesión coincidental (la peor)
Los elementos están agrupados sin ninguna relación aparente. Es el nivel más bajo de cohesión.

**Ejemplo:**
```kotlin
class Utilidades {
    fun calcularIva(precio: Double): Double {
        return precio * 0.21
    }
    
    fun enviarEmail(destinatario: String, mensaje: String) {
        // código para enviar email
    }
    
    fun ordenarArray(array: List<Int>): List<Int> {
        return array.sorted()
    }
}
```

#### 1.2.2. Cohesión lógica
Los elementos están relacionados porque realizan actividades del mismo tipo, aunque no necesariamente relacionadas.

**Ejemplo:**
```kotlin
class Operaciones {
    fun ejecutar(tipo: String, datos: List<Int>): Int {
        return when (tipo) {
            "suma" -> datos[0] + datos[1]
            "resta" -> datos[0] - datos[1]
            "multiplicacion" -> datos[0] * datos[1]
            else -> 0
        }
    }
}
```

#### 1.2.3. Cohesión temporal
Los elementos están agrupados porque se ejecutan en el mismo momento temporal.

**Ejemplo:**
```kotlin
class Inicializador {
    fun inicializarSistema() {
        cargarConfiguracion()
        conectarBaseDatos()
        iniciarLogger()
        cargarCache()
    }
    
    private fun cargarConfiguracion() {}
    private fun conectarBaseDatos() {}
    private fun iniciarLogger() {}
    private fun cargarCache() {}
}
```

#### 1.2.4. Cohesión procedimental
Los elementos están agrupados porque siguen una secuencia de pasos en un procedimiento.

**Ejemplo:**
```kotlin
class ProcesadorPedido {
    fun procesarPedido(pedido: Pedido) {
        validarStock(pedido)
        calcularTotal(pedido)
        aplicarDescuento(pedido)
        generarFactura(pedido)
    }
    
    private fun validarStock(pedido: Pedido) {}
    private fun calcularTotal(pedido: Pedido) {}
    private fun aplicarDescuento(pedido: Pedido) {}
    private fun generarFactura(pedido: Pedido) {}
}
```

#### 1.2.5. Cohesión comunicacional
Los elementos trabajan sobre los mismos datos o contribuyen a la misma salida.

**Ejemplo:**
```kotlin
class InformeCliente {
    fun generarInforme(cliente: Cliente): String {
        val datos = obtenerDatosCliente(cliente)
        val estadisticas = calcularEstadisticas(datos)
        return formatearInforme(datos, estadisticas)
    }
    
    private fun obtenerDatosCliente(cliente: Cliente): DatosCliente = DatosCliente()
    private fun calcularEstadisticas(datos: DatosCliente): Estadisticas = Estadisticas()
    private fun formatearInforme(datos: DatosCliente, estadisticas: Estadisticas): String = ""
}
```

#### 1.2.6. Cohesión secuencial
La salida de un elemento es la entrada del siguiente, formando una cadena de procesamiento.

**Ejemplo:**
```kotlin
class ProcesadorTexto {
    fun procesar(texto: String): String {
        val textoLimpio = eliminarEspacios(texto)
        val textoNormalizado = normalizar(textoLimpio)
        val textoValidado = validar(textoNormalizado)
        return textoValidado
    }
    
    private fun eliminarEspacios(texto: String): String = texto.trim()
    private fun normalizar(texto: String): String = texto.lowercase()
    private fun validar(texto: String): String = texto
}
```

#### 1.2.7. Cohesión funcional (la mejor)
Todos los elementos del módulo están relacionados para cumplir una única función bien definida.

**Ejemplo:**
```kotlin
class CalculadoraImpuestos(private val tasaIva: Double) {
    
    fun calcularIva(baseImponible: Double): Double {
        return baseImponible * tasaIva
    }
    
    fun calcularTotalConIva(baseImponible: Double): Double {
        return baseImponible + calcularIva(baseImponible)
    }
    
    fun obtenerBaseDesdeTotal(totalConIva: Double): Double {
        return totalConIva / (1 + tasaIva)
    }
}
```

### 1.3. Ventajas de la alta cohesión

#### Beneficios principales:

- ✅ **Comprensibilidad**: Es más fácil entender qué hace un módulo cuando todas sus partes están relacionadas
- ✅ **Mantenibilidad**: Los cambios en un módulo cohesivo afectan a un área específica y bien definida
- ✅ **Reutilización**: Los módulos cohesivos son más fáciles de reutilizar en otros contextos
- ✅ **Robustez**: Menor probabilidad de efectos secundarios no deseados
- ✅ **Testabilidad**: Más fácil de probar de forma independiente

## 2. Acoplamiento

### 2.1. ¿Qué es el acoplamiento?

El **acoplamiento** es una medida del grado de interdependencia entre módulos. Un bajo acoplamiento significa que los módulos son relativamente independientes entre sí, lo que facilita los cambios y el mantenimiento.

### 2.2. Tipos de acoplamiento

**Ordenados de peor a mejor** (de mayor a menor acoplamiento):

| Nivel  | Tipo                      | Fuerza          | Descripción                      |
|--------|---------------------------|-----------------|----------------------------------|
| 1      | Acoplamiento de contenido | ❌ Muy fuerte    | Modifica internos de otro módulo |
| 2      | Acoplamiento común        | 🔴 Fuerte       | Comparten datos globales         |
| 3      | Acoplamiento externo      | 🟠 Medio-fuerte | Dependen de formatos externos    |
| 4      | Acoplamiento de control   | 🟡 Medio        | Controla el flujo de otro módulo |
| 5      | Acoplamiento de datos     | ✅ Débil         | Comunicación solo por parámetros |

#### 2.2.1. Acoplamiento de contenido (el peor)
Un módulo modifica o depende del funcionamiento interno de otro módulo.

**Ejemplo (MAL):**
```kotlin
class Cliente {
    var nombre: String = ""
    var saldo: Double = 0.0  // Debería ser privado
}

class GestorClientes {
    fun actualizarSaldo(cliente: Cliente, cantidad: Double) {
        // Accede directamente a los atributos internos
        cliente.saldo += cantidad  // Viola la encapsulación
    }
}
```

#### 2.2.2. Acoplamiento común
Varios módulos comparten datos globales.

**Ejemplo (MAL):**
```kotlin
// Variable global (objeto companion o top-level)
object ConfiguracionGlobal {
    var modo: String = "produccion"
    var debug: Boolean = false
}

class ServicioA {
    fun procesar() {
        if (ConfiguracionGlobal.debug) {
            println("Modo debug activado")
        }
    }
}

class ServicioB {
    fun ejecutar() {
        if (ConfiguracionGlobal.modo == "produccion") {
            // hacer algo
        }
    }
}
```

#### 2.2.3. Acoplamiento externo
Los módulos dependen de formatos externos impuestos (APIs, protocolos).

**Ejemplo:**
```kotlin
import java.net.URL

class ClienteAPI {
    fun obtenerDatos(): Map<String, Any> {
        // Acoplado al formato JSON de la API externa
        val response = URL("https://api.ejemplo.com/datos").readText()
        // Parsing JSON (requiere librería como Gson o kotlinx.serialization)
        return emptyMap()  // Simplificado para el ejemplo
    }
}
```

#### 2.2.4. Acoplamiento de control
Un módulo controla el flujo de ejecución de otro pasándole información de control.

**Ejemplo (MEJORABLE):**
```kotlin
class Procesador {
    fun procesar(datos: List<String>, tipoProcesamiento: String): List<String> {
        return when (tipoProcesamiento) {
            "rapido" -> procesamientoRapido(datos)
            "completo" -> procesamientoCompleto(datos)
            else -> emptyList()
        }
    }
    
    private fun procesamientoRapido(datos: List<String>): List<String> = datos
    private fun procesamientoCompleto(datos: List<String>): List<String> = datos
}
```

#### 2.2.5. Acoplamiento de datos (el mejor)
Los módulos se comunican solo mediante parámetros de datos simples.

**Ejemplo (BIEN):**
```kotlin
class CalculadoraDescuento {
    fun calcularDescuento(precioBase: Double, porcentaje: Double): Double {
        return precioBase * (porcentaje / 100)
    }
}

class CarritoCompra(private val calculadora: CalculadoraDescuento) {
    
    fun aplicarDescuento(precio: Double, descuento: Double): Double {
        return calculadora.calcularDescuento(precio, descuento)
    }
}
```

### 2.3. Consecuencias del alto acoplamiento

#### Problemas principales:

- ❌ **Efecto dominó**: Un cambio en un módulo requiere cambios en otros módulos
- ❌ **Dificultad para probar**: Es difícil probar módulos de forma aislada
- ❌ **Menor reutilización**: Los módulos no pueden usarse independientemente
- ❌ **Mayor complejidad**: El sistema se vuelve más difícil de entender y mantener
- ❌ **Rigidez**: Dificulta la evolución y adaptación del sistema

### 2.4. Estrategias para reducir el acoplamiento

#### 2.4.1. Uso de interfaces
```kotlin
interface ServicioNotificacion {
    fun enviar(destinatario: String, mensaje: String)
}

class EmailNotificacion : ServicioNotificacion {
    override fun enviar(destinatario: String, mensaje: String) {
        println("Enviando email a $destinatario: $mensaje")
    }
}

class SMSNotificacion : ServicioNotificacion {
    override fun enviar(destinatario: String, mensaje: String) {
        println("Enviando SMS a $destinatario: $mensaje")
    }
}

class GestorPedidos(private val notificador: ServicioNotificacion) {
    
    fun confirmarPedido(cliente: String) {
        // Bajo acoplamiento: no depende de una implementación específica
        notificador.enviar(cliente, "Pedido confirmado")
    }
}
```

#### 2.4.2. Inyección de dependencias
```kotlin
class BaseDatos {
    fun guardar(datos: String) {
        println("Guardando en BD: $datos")
    }
}

class ServicioPedidos(private val bd: BaseDatos) {  // Dependencia inyectada
    
    fun crearPedido(pedido: String) {
        // Procesar pedido
        bd.guardar(pedido)
    }
}

// Uso
fun main() {
    val bd = BaseDatos()
    val servicio = ServicioPedidos(bd)  // Inyección de dependencia
    servicio.crearPedido("Pedido #123")
}
```

#### 2.4.3. Patrón Facade
```kotlin
class SistemaFacturacion {
    fun generarFactura() {}
}

class SistemaInventario {
    fun actualizarStock() {}
}

class SistemaEnvios {
    fun programarEnvio() {}
}

/**
 * Simplifica la interacción con múltiples subsistemas
 */
class FachadaPedidos {
    private val facturacion = SistemaFacturacion()
    private val inventario = SistemaInventario()
    private val envios = SistemaEnvios()
    
    fun procesarPedidoCompleto(pedido: Pedido) {
        facturacion.generarFactura()
        inventario.actualizarStock()
        envios.programarEnvio()
    }
}
```

## 3. Relación entre Acoplamiento y Cohesión

### 3.1. El equilibrio ideal

El objetivo es lograr:
- **Alta cohesión**: Cada módulo tiene una responsabilidad clara y única
- **Bajo acoplamiento**: Los módulos son lo más independientes posible

### 3.2. Matriz de calidad del diseño

| Cohesión \ Acoplamiento | Bajo Acoplamiento     | Alto Acoplamiento   |
|-------------------------|-----------------------|---------------------|
| **Alta Cohesión**       | ✅ Excelente           | ⚠️ Bueno            |
| **Baja Cohesión**       | ⚠️ Regular            | ❌ Malo              |

### 3.3. Ejemplo comparativo

**Diseño MALO (baja cohesión, alto acoplamiento):**
```kotlin
class Sistema {
    private val conexionBd = "mysql://localhost"
    
    fun procesarPedido(pedido: Pedido) {
        // Muchas responsabilidades mezcladas
        if (validarStock(pedido)) {
            calcularPrecio(pedido)
            actualizarBd(pedido)
            enviarEmail(pedido.cliente)
            generarFacturaPdf(pedido)
        }
    }
    
    private fun validarStock(pedido: Pedido): Boolean = true
    private fun calcularPrecio(pedido: Pedido) {}
    private fun actualizarBd(pedido: Pedido) {}
    private fun enviarEmail(cliente: String) {}
    private fun generarFacturaPdf(pedido: Pedido) {}
}
```

**Diseño BUENO (alta cohesión, bajo acoplamiento):**
```kotlin
class ValidadorStock {
    fun validar(pedido: Pedido): Boolean = true
}

class CalculadoraPrecios {
    fun calcular(pedido: Pedido): Double = 100.0
}

class RepositorioPedidos {
    fun guardar(pedido: Pedido) {}
}

class ServicioNotificaciones {
    fun notificarCliente(cliente: String, mensaje: String) {
        println("Notificando a $cliente: $mensaje")
    }
}

class GeneradorFacturas {
    fun generar(pedido: Pedido): ByteArray = ByteArray(0)
}

class ProcesadorPedidos(
    private val validador: ValidadorStock,
    private val calculadora: CalculadoraPrecios,
    private val repositorio: RepositorioPedidos,
    private val notificador: ServicioNotificaciones,
    private val generador: GeneradorFacturas
) {
    
    fun procesar(pedido: Pedido) {
        if (validador.validar(pedido)) {
            val precio = calculadora.calcular(pedido)
            repositorio.guardar(pedido)
            notificador.notificarCliente(
                pedido.cliente,
                "Pedido confirmado. Total: $precio"
            )
            generador.generar(pedido)
        }
    }
}

// Clases de datos necesarias
data class Pedido(val cliente: String, val items: List<String>)
data class Cliente(val nombre: String)
data class DatosCliente(val info: String = "")
data class Estadisticas(val total: Int = 0)
```

## 4. Principios de Diseño Relacionados

### 4.1. Principio de Responsabilidad Única (SRP)
Una clase debe tener una sola razón para cambiar. Este principio promueve la alta cohesión.

### 4.2. Principio de Inversión de Dependencias (DIP)
Depender de abstracciones, no de concreciones. Este principio reduce el acoplamiento.

### 4.3. Principio de Segregación de Interfaces (ISP)
Los clientes no deben depender de interfaces que no usan. Esto reduce el acoplamiento innecesario.

## 5. Métricas y Medición

### 5.1. Cómo medir la cohesión

#### LCOM (Lack of Cohesion of Methods)

**Definición**: Mide cuántos métodos de una clase utilizan los mismos atributos.

**Interpretación**:
- **LCOM bajo** → ✅ Alta cohesión (bueno)
- **LCOM alto** → ❌ Baja cohesión (malo)

**Herramientas**:
- SonarQube
- PMD
- CodeClimate
- IntelliJ IDEA Inspector

### 5.2. Cómo medir el acoplamiento

#### Métricas principales:

| Métrica  | Nombre                | Descripción                                                  |
|----------|-----------------------|--------------------------------------------------------------|
| **Ca**   | Acoplamiento aferente | Número de clases externas que dependen de esta clase         |
| **Ce**   | Acoplamiento eferente | Número de clases externas de las que depende esta clase      |
| **I**    | Inestabilidad         | I = Ce / (Ca + Ce), valores cercanos a 0 indican estabilidad |

**Interpretación de Inestabilidad (I)**:
- **I ≈ 0**: Clase estable (muchas clases dependen de ella, depende de pocas)
- **I ≈ 1**: Clase inestable (pocas clases dependen de ella, depende de muchas)

**Objetivo**: Clases de bajo nivel (utilidades, frameworks) deben tener I cercano a 0.

## 6. Conclusiones

### Puntos clave para recordar:

- ✅ La **alta cohesión** y el **bajo acoplamiento** son pilares fundamentales del buen diseño de software
- ✅ Un diseño con alta cohesión hace que cada módulo tenga un propósito claro y único
- ✅ Un diseño con bajo acoplamiento facilita el mantenimiento, las pruebas y la evolución del sistema
- ✅ Aplicar estos principios desde el inicio del desarrollo ahorra tiempo y esfuerzo a largo plazo
- ✅ Las refactorizaciones periódicas ayudan a mantener estos principios a lo largo del ciclo de vida del software

### Matriz de calidad del diseño (recordatorio):

| Cohesión \ Acoplamiento | Bajo Acoplamiento  | Alto Acoplamiento |
|-------------------------|--------------------|-------------------|
| **Alta Cohesión**       | ✅ Excelente        | ⚠️ Bueno          |
| **Baja Cohesión**       | ⚠️ Regular         | ❌ Malo            |

## 7. Recursos y Referencias

### Libros recomendados

- **[Refactoring: Improving the Design of Existing Code](https://refactoring.com/)** - Martin Fowler
  - Guía práctica sobre cómo mejorar el diseño del código existente

- **[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)** - Robert C. Martin
  - Principios de arquitectura de software limpia

- **[Clean Code](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)** - Robert C. Martin
  - Manual sobre cómo escribir código limpio y mantenible

### Artículos y recursos online

- [SOLID Principles](https://www.digitalocean.com/community/conceptual_articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
- [Principios de diseño orientado a objetos](https://www.baeldung.com/solid-principles)
- [Cohesion and Coupling - Martin Fowler](https://martinfowler.com/bliki/CouplingAndCohesion.html)

### Herramientas de análisis

- **SonarQube**: Análisis continuo de calidad de código
- **IntelliJ IDEA**: Inspecciones de código integradas
- **PMD**: Detector de problemas de código
- **CodeClimate**: Análisis de mantenibilidad

---

**Próximos temas**:
- Principios SOLID
- Patrones de Diseño
- Refactorización
- Arquitectura de Software
