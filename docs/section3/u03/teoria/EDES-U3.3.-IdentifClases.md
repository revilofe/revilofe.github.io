---
title: "UD 3 - 3.3 Identificación de Clases"
description: Identificación de Clases en UML
summary: Técnicas, métodos y buenas prácticas para identificar clases a partir de requisitos
authors:
    - Eduardo Fdez
date: 2025-11-03
icon: "material/file-document-outline"
permalink: /edes/unidad3/3.3
categories:
    - EDES
tags:
    - EDES
    - UML
    - Identificación de Clases
    - Análisis
    - Buenas Prácticas
    
---

## 3.3 Identificación de Clases y Buenas Prácticas

### 1. Introducción

La **identificación de clases** es uno de los pasos más importantes y desafiantes en el diseño orientado a objetos. De hecho, es el paso que diferencia a los buenos diseñadores de los mediocres. Un buen modelo de clases es la base para un sistema bien estructurado, mantenible y escalable, mientras que un mal modelo puede condenar a un proyecto a ser un desastre de mantenimiento.

!!! note "Principio fundamental"
    Cada comportamiento que requiera el sistema debe ser proporcionado por los objetos de las clases que elijamos. Si olvidas una clase importante, algunos comportamientos no estarán representados. Si creas clases innecesarias, tu modelo se vuelve confuso y difícil de mantener.

Este documento se centra en **cómo identificar clases**, **cómo relacionarlas** y las **buenas prácticas** para crear diagramas de clases efectivos.

**¿Por qué es tan importante?** Porque la fase de identificación de clases:

- Define la **arquitectura conceptual** de tu sistema
- Determina cómo será de **fácil o difícil** mantener el código después
- Establece las bases para la **escalabilidad** futura
- Facilita o complica la **colaboración** entre desarrolladores
- Afecta el **desempeño** y la **eficiencia** del sistema resultante

### 2. Fundamentos de la Identificación

#### 2.1. ¿Qué buscamos al identificar clases?

Al identificar clases, buscamos responder estas preguntas fundamentales:

1. **¿Qué entidades existen en nuestro dominio?** - ¿Cuáles son los objetos conceptuales o físicos relevantes?

    - Ejemplos: Cliente, Producto, Pedido, Empresa
   
2. **¿Qué responsabilidades tiene cada entidad?** - ¿Qué debe saber hacer cada objeto?

    - Ejemplos: Un Cliente debe poder realizar una compra, una Factura debe poder calcular su total

3. **¿Cómo colaboran las entidades para cumplir los requisitos?** - ¿Cómo trabajan juntas?

    - Ejemplos: Un Cliente crea un Pedido que contiene Productos

Buscamos representar:

1. **Entidades del dominio**: Objetos que existen en el mundo real o conceptual del problema. Son los más fáciles de identificar.

2. **Responsabilidades claras**: Qué debe hacer cada clase en el sistema. Cada clase debe tener una razón clara de ser.

3. **Colaboraciones** entre clases: Cómo las clases trabajan juntas para cumplir los requisitos del sistema. Una clase no debería actuar en aislamiento.

#### 2.2. Consideraciones importantes

Es importante recordar que los objetos son realmente cosas dentro de un programa. Cuando hablamos sobre "libros" y "copias", por ejemplo, realmente nos referimos a la **representación digital de estas cosas dentro de nuestro sistema**, no a los libros y copias físicas en el mundo real.

Las consecuencias de esto son que hay que tener cuidado con la siguiente pregunta: **¿qué información de la realidad es realmente importante para nuestro sistema?**

Es clave:

- **No almacenar información** que es definitivamente irrelevante para nuestro sistema (ej: el color del cartel de una tienda)
- **No perder la visión** del hecho de que ¡los objetos son el sistema! Trabajan dentro del programa, no son el mundo real
- **Mantener el enfoque** en lo que el sistema necesita, no en todo lo que existe en el mundo real (ej: un sistema de biblioteca quizás no necesita la información de empleados de mantenimiento, aunque estos existan en el mundo real)

**La clave**: Modelar el dominio del problema desde la perspectiva del sistema, no modelar la realidad en su totalidad.

!!! tip "Consejo práctico"
    Siempre pregúntate: "¿Esta información es necesaria para que el sistema cumpla sus requisitos?" Si la respuesta es no, probablemente no necesites una clase para representarla.

### 3. Objetivos de un Buen Modelo de Clases

Cuando diseñas un modelo de clases, en realidad estás persiguiendo **dos objetivos que a menudo están en tensión**:

**Objetivo 1: Construcción Eficiente**

Construir, lo más rápido y barato posible, un sistema que satisfaga nuestros requisitos actuales.

!!! tip "Principio"
    Cada comportamiento que requiera el sistema debe ser proporcionado por los objetos de las clases que elijamos

**Estrategias**:

- **Identificar las clases mínimas necesarias**: La solución más simple que funcione. No sobre-diseñes.
- **Enfocarse en los requisitos actuales**: No anticipar necesidades futuras imaginarias. Solo diseña para lo que sabes que necesitas hoy.
- **Evitar sobre-ingeniería prematura**: No añadas complejidad sin justificación presente. La complejidad complejidad adicional, y esto cuesta tiempo y dinero.

**¿Por qué esto importa?** Porque cada clase adicional innecesaria incrementa la complejidad del sistema, ralentiza el desarrollo, y aumenta la probabilidad de errores. Es tentador crear "clases generales" que "podrían ser útiles en el futuro", pero a menudo resultan siendo innecesarias o inútiles cuando ese futuro llega.

**Objetivo 2: Mantenibilidad**

Construir un sistema que sea fácil de mantener y adaptar a futuros requisitos. Este es el objetivo a largo plazo.

!!! tip "Principio"
    Un buen modelo de clases está formado por módulos encapsulados, con acoplamiento débil (pocas dependencias entre módulos) y cohesión fuerte

**Características clave**:

- **Alta cohesión**: Cada clase tiene una responsabilidad clara y bien definida. Si necesitas cambiar algo, sabes exactamente dónde mirar.
- **Bajo acoplamiento**: Las clases tienen pocas dependencias entre sí. Un cambio en una clase no causa un efecto dominó en todas las demás.
- **Encapsulamiento**: Los detalles internos están ocultos. Otras clases interactúan con la interfaz pública, no con los detalles internos.

**¿Por qué esto importa?** Porque con el tiempo, el código pasa más tiempo siendo mantenido que siendo escrito inicialmente. Un sistema con buena cohesión y bajo acoplamiento es más fácil de entender, más fácil de modificar, y más fácil de extender.

**El equilibrio**: La clave es encontrar un equilibrio entre estos dos objetivos. No puede ser tan simple que sea rígido e imposible de mantener. Pero tampoco puede ser tan complejo que sea difícil de entender y construir.


### 4. Proceso Iterativo de Identificación: El Ciclo del Diseño

La identificación de clases no es un proceso lineal de "una sola pasada". Es un **proceso iterativo** que requiere **múltiples refinamientos** hasta alcanzar un modelo satisfactorio.

#### 4.1. ¿Por qué es iterativo?

**Razones fundamentales**:

1. **Aprendizaje progresivo**: A medida que profundizas en el dominio, descubres nuevas clases o descartas las innecesarias
2. **Requisitos evolutivos**: Los requisitos se aclaran y refinan durante el proceso
3. **Descubrimiento de relaciones**: Las relaciones entre clases emergen gradualmente
4. **Validación continua**: Cada iteración valida y corrige el modelo anterior

!!! warning "Error común"
    Muchos principiantes intentan crear el modelo perfecto en el primer intento. Esto es imposible y contraproducente. Acepta que tu primer modelo será imperfecto y que mejorará con cada iteración.

#### 4.2. Las Fases del Proceso Iterativo
Cada iteración del proceso de identificación de clases puede dividirse en varias fases clave:


##### 4.2.1. Fase 1: Identificación Inicial (Divergencia)

**Objetivo**: Generar un conjunto amplio de candidatos a clases sin ser demasiado crítico

**Actividades**:

- Análisis de sustantivos en los requisitos
- Brainstorming con el equipo
- Investigación del dominio
- Consulta con expertos del dominio

**Duración**: 30-60 minutos para proyectos pequeños

**Resultado esperado**: Lista extensa de 20-50 candidatos a clases (incluye muchos falsos positivos, está bien)

**Ejemplo**:
Para un sistema de biblioteca, podrías identificar: Libro, Copia, Usuario, Préstamo, Bibliotecario, Estantería, Editorial, Autor, Catálogo, FichaBibliográfica, CodigoDewey, MultaPorRetraso, etc.

##### 4.2.2. Fase 2: Filtrado y Refinamiento (Convergencia)

**Objetivo**: Eliminar candidatos inapropiados y consolidar los válidos

**Actividades**:

- Aplicar criterios de descarte (ver sección 5.3)
- Agrupar conceptos similares
- Identificar atributos vs clases
- Detectar redundancias

**Duración**: 60-90 minutos

**Resultado esperado**: Lista reducida de 10-20 clases sólidas

**Ejemplo continuado**: 
Después del filtrado para la biblioteca:

- ✅ Mantener: Libro, Copia, Usuario, Préstamo
- ❌ Descartar: Bibliotecario (es un rol de Usuario), Estantería (detalle físico irrelevante)
- ❌ Descartar: FichaBibliográfica (es solo una representación de Libro)
- 🔄 Convertir: MultaPorRetraso → atributo calculado de Préstamo

##### 4.2.3. Fase 3: Identificación de Relaciones

**Objetivo**: Establecer cómo las clases colaboran entre sí

**Actividades**:

- Identificar asociaciones entre clases
- Determinar multiplicidad
- Establecer herencia si aplica
- Definir dependencias

**Duración**: 45-60 minutos

**Resultado esperado**: Diagrama con clases conectadas

**Ejemplo**:
```
Usuario 1 ─────── * Préstamo
Préstamo * ─────── 1 Copia
Copia * ─────── 1 Libro
```

##### 4.2.4. Fase 4: Enriquecimiento (Añadir Detalles)

**Objetivo**: Agregar atributos y métodos a las clases

**Actividades**:

- Identificar atributos de cada clase
- Definir métodos principales
- Establecer visibilidad (public, private, protected)
- Agregar tipos de datos

**Duración**: 60-120 minutos

**Resultado esperado**: Diagrama de clases completo con atributos y métodos

##### 4.2.5. Fase 5: Validación y Revisión

**Objetivo**: Verificar que el modelo cumple los requisitos

**Actividades**:

- Recorrer casos de uso con el modelo
- Verificar que todas las funcionalidades están cubiertas
- Revisar principios de diseño (cohesión, acoplamiento)
- Obtener feedback de stakeholders

**Duración**: 30-45 minutos

**Resultado esperado**: Modelo validado listo para implementación

#### 4.3. Número de Iteraciones

**¿Cuántas iteraciones son normales?**

- **Proyectos pequeños**: 2-3 iteraciones
- **Proyectos medianos**: 3-5 iteraciones
- **Proyectos grandes**: 5-10+ iteraciones

!!! tip "Consejo práctico"
    No intentes perfeccionar cada detalle en las primeras iteraciones. Es mejor tener un modelo "suficientemente bueno" rápidamente y refinarlo después, que buscar la perfección desde el inicio.

#### 4.4. Criterios para Detener las Iteraciones

¿Cuándo sabes que tu modelo está "suficientemente bueno"?

**Indicadores de que puedes detenerte**:

- Todos los requisitos funcionales están cubiertos
- No hay clases obviamente faltantes
- No hay clases claramente redundantes
- Las relaciones tienen sentido
- Los nombres son claros y consistentes
- El equipo está de acuerdo con el modelo
- Los expertos del dominio validan el modelo

**Indicadores de que necesitas más iteraciones**:

- Hay funcionalidades sin clase responsable
- Hay clases "sospechosamente" vacías (sin responsabilidades claras)
- Las relaciones son confusas o contradictorias
- El modelo tiene más de 50 clases (probablemente sobre-diseñado)
- Los stakeholders no entienden el modelo

### 5. Técnica de Identificación de Nombres: El Método Fundamental

La **técnica de análisis de sustantivos** (Noun Extraction) es el método más utilizado para identificar clases candidatas a partir de documentos de requisitos.

#### 5.1. Fundamentos del Método

**Principio básico**: En lenguaje natural, los sustantivos suelen representar conceptos (clases) del dominio, mientras que los verbos representan acciones (métodos).

**Base lingüística**:

- **Sustantivos** → Potenciales clases u objetos
- **Verbos** → Potenciales métodos o relaciones
- **Adjetivos** → Potenciales atributos o estados
- **Adverbios** → Restricciones o calificadores

**¿Por qué funciona este método?**

Porque el lenguaje humano refleja naturalmente la estructura conceptual del dominio. Cuando un experto del dominio describe un sistema, usa sustantivos para referirse a las entidades importantes y verbos para describir lo que hacen.

#### 5.2. Proceso Paso a Paso

El proceso de análisis de sustantivos consta de varios pasos claros:

**Paso 1: Preparar el texto**

Obtén una descripción textual de los requisitos del sistema. Puede ser:

- Documento de requisitos formal
- Historias de usuario
- Transcripción de entrevistas
- Descripción del problema

**Ejemplo de texto inicial**:

> "Una biblioteca necesita un sistema para gestionar préstamos de libros. Los usuarios se registran proporcionando su nombre, dirección y número de identificación. Cada libro tiene un título, autor, ISBN y puede tener múltiples copias físicas. Un usuario puede tomar prestada una copia durante 14 días. El bibliotecario debe poder ver qué copias están disponibles y cuáles prestadas. Si un usuario devuelve tarde, se le cobra una multa de 0.50€ por día."

**Paso 2: Identificar todos los sustantivos**

Subraya o marca todos los sustantivos:

> "Una **biblioteca** necesita un **sistema** para gestionar **préstamos** de **libros**. Los **usuarios** se registran proporcionando su **nombre**, **dirección** y **número de identificación**. Cada **libro** tiene un **título**, **autor**, **ISBN** y puede tener múltiples **copias físicas**. Un **usuario** puede tomar prestada una **copia** durante 14 **días**. El **bibliotecario** debe poder ver qué **copias** están **disponibles** y cuáles **prestadas**. Si un **usuario** devuelve tarde, se le cobra una **multa** de 0.50€ por **día**."

**Paso 3: Crear lista de candidatos**

Lista completa de sustantivos únicos:

1. Biblioteca
2. Sistema
3. Préstamo
4. Libro
5. Usuario
6. Nombre
7. Dirección
8. Número de identificación
9. Título
10. Autor
11. ISBN
12. Copia (física)
13. Día
14. Bibliotecario
15. Disponible (estado)
16. Prestada (estado)
17. Multa

**Paso 4: Aplicar filtros de descarte**

Ahora aplicamos criterios sistemáticos para eliminar candidatos inapropiados.

#### 5.3. Criterios de Descarte: ¿Qué NO es una clase?

**Criterio 1: Redundancia**

❌ **Descartar**: Conceptos que son sinónimos o representan lo mismo

En nuestro ejemplo:

- "Usuario" y "Bibliotecario": El bibliotecario es un tipo de usuario (rol). Solución: Una clase Usuario con atributo `rol` o `esEmpleado`

**Criterio 2: Atributos disfrazados**

❌ **Descartar**: Conceptos que son propiedades simples de otra entidad, no entidades independientes

En nuestro ejemplo, descarta:

- "Nombre": Es un atributo de Usuario, no una clase
- "Dirección": Es un atributo de Usuario
- "Número de identificación": Es un atributo de Usuario
- "Título": Es un atributo de Libro
- "Autor": **¡CUIDADO!** Podría ser clase si necesitamos gestionar información de autores
- "ISBN": Es un atributo de Libro
- "Día": Es un valor primitivo (número o fecha)

**¿Cuándo un concepto debe ser atributo vs clase?**

Regla general:

- **Atributo**: Si solo necesitas el valor (ej: nombre = "Juan")
- **Clase**: Si necesitas múltiples propiedades o comportamientos del concepto

**Ejemplo**: 

- Si "Autor" solo es un string con el nombre → Atributo
- Si "Autor" tiene biografía, nacionalidad, otros libros, fechas → Clase

**Criterio 3: Valores o estados**

❌ **Descartar**: Estados o valores que son propiedades, no objetos

En nuestro ejemplo, descartamos:

- "Disponible": Es un estado de Copia (atributo booleano `disponible`)
- "Prestada": También es un estado de Copia

**Criterio 4: Detalles de implementación o infraestructura**

❌ **Descartar**: Conceptos técnicos que no son del dominio del problema

En nuestro ejemplo, descartamos:

- "Sistema": Es demasiado genérico, no es una entidad del dominio

**Criterio 5: Entidades externas fuera del alcance**

❌ **Descartar**: Conceptos que existen pero están fuera del alcance del sistema

En nuestro ejemplo, descartamos:

- "Biblioteca" (el edificio físico): Si el sistema solo gestiona préstamos, el edificio no es relevante

**Criterio 6: Operaciones o servicios**

❌ **Descartar**: Verbos nominalizados que representan acciones, no entidades

Por ejemplo: "Gestión", "Procesamiento", "Validación" suelen ser servicios, no clases del dominio

**Paso 5: Lista refinada de clases candidatas**

Después del filtrado:

Clases válidas:

1. Libro - Entidad del dominio con múltiples propiedades
2. Copia - Representación física de un libro específico
3. Usuario - Persona que usa el sistema
4. Préstamo - Transacción importante del dominio
5. Multa - Concepto con lógica de negocio (cálculo, pago)

**Análisis de decisiones**:

¿Por qué Copia Y Libro?

- Copia: Instancia física específica (puede estar prestada, dañada, tiene número de serie)
- Libro: Concepto abstracto del libro (título, ISBN, autor)
- Relación: Un Libro tiene múltiples Copias

¿Por qué Préstamo es una clase?

- Representa una transacción importante
- Tiene atributos: fechaPréstamo, fechaDevoluciónEsperada, fechaDevoluciónReal
- Tiene comportamiento: calcularDíasRetraso(), estáVencido()

¿Por qué Multa es una clase y no un atributo de Préstamo?
- Puede ser discutible. Ambas opciones son válidas:

    - Como clase: Si las multas tienen ciclo de vida independiente (pueden pagarse después, tener historial)
    - Como atributo calculado: Si solo es un monto que se calcula al devolver

En este caso, para simplicidad, Multa podría ser un método `calcularMulta()` en Préstamo.

**Lista final**:

1. Libro
2. Copia
3. Usuario
4. Préstamo

¡De 17 candidatos iniciales, quedamos con 4 clases sólidas!

#### 5.4. Reglas Prácticas para Identificar Clases

**Regla 1: "El test del sustantivo concreto"**

¿Puedes señalar ejemplos concretos de este concepto?

- "Ese libro" → Sí, es una clase
- "Esa persona" → Sí, es una clase
- "Ese nombre" → No, es un dato simple

**Regla 2: "El test de las múltiples propiedades"**

¿Este concepto tiene más de 2-3 propiedades relevantes?
- Libro: título, autor, ISBN, editorial, año → Sí, es una clase
- Título: solo es un string → No, es un atributo

**Regla 3: "El test del comportamiento"**

¿Este concepto tiene comportamiento (métodos) significativo?
- Préstamo: calcularRetraso(), devolver(), renovar() → Sí, es una clase
- ISBN: no tiene comportamiento → No, es un atributo

**Regla 4: "El test de la independencia"**

¿Este concepto puede existir independientemente?
- Usuario: puede existir sin préstamos → Probablemente una clase
- Dirección: no tiene sentido sin un Usuario → Probablemente un atributo

!!! tip "Consejo de experto"
    Cuando dudes si algo debería ser una clase o un atributo, empieza haciéndolo atributo. Es más fácil convertir un atributo en clase después (refactoring) que simplificar una clase innecesaria.


### 6. Fuentes de Clases: Más Allá de los Sustantivos

Aunque el análisis de sustantivos es la técnica principal, existen otras fuentes valiosas para identificar clases.

#### 6.1. Categorías de Objetos según su Origen

Las clases que identificamos suelen caer en estas categorías generales:

**1. Cosas Tangibles o "del Mundo Real"**

**Descripción**: Objetos físicos que existen en el mundo real

**Ejemplos**:

- Sistema de transporte: Autobús, Camión, Bicicleta
- Sistema médico: Bisturí, Camilla, Máquina de rayos X
- Sistema manufacturero: Máquina, Herramienta, Producto físico

**Cuándo son clases**: Cuando necesitas rastrear propiedades físicas o ubicación

**Ejemplo detallado - Sistema de flota de vehículos**:
```kotlin
class Vehiculo(
    val matricula: String,
    val modelo: String,
    val año: Int,
    var kilometraje: Int,
    var ubicacionActual: Coordenadas
) {
    fun registrarMantenimiento(tipo: String, costo: Double)
    fun calcularDepreciacion(): Double
}
```

**2. Roles o Papeles**

**Descripción**: Las funciones que las personas desempeñan en el sistema

**Ejemplos**:

- Sistema educativo: Estudiante, Profesor, Administrativo
- Sistema hospital: Paciente, Médico, Enfermero
- Sistema empresarial: Gerente, Empleado, Cliente

**Característica clave**: Una misma persona puede tener múltiples roles

**Ejemplo**:
```kotlin
// Opción A: Roles como clases separadas (si tienen comportamientos muy diferentes)
abstract class Persona(val nombre: String, val dni: String)
class Estudiante(nombre: String, dni: String, val matricula: String) : Persona(nombre, dni)
class Profesor(nombre: String, dni: String, val departamento: String) : Persona(nombre, dni)

// Opción B: Rol como atributo (si el comportamiento es similar)
class Usuario(
    val nombre: String,
    val dni: String,
    val roles: MutableList<Rol>  // Un usuario puede tener múltiples roles
)
enum class Rol { ESTUDIANTE, PROFESOR, ADMINISTRATIVO }
```

**¿Cuál elegir?** Depende de si los roles tienen comportamiento significativamente diferente.

**3. Organizaciones**

**Descripción**: Grupos, departamentos, empresas

**Ejemplos**:

- Universidad, Facultad, Departamento
- Empresa, Sucursal, Área
- Hospital, Servicio, Unidad

**Ejemplo - Sistema universitario**:
```kotlin
class Universidad(val nombre: String, val rector: Persona) {
    private val facultades: MutableList<Facultad> = mutableListOf()
    fun agregarFacultad(facultad: Facultad)
}

class Facultad(
    val nombre: String,
    val decano: Profesor,
    val universidad: Universidad
) {
    private val departamentos: MutableList<Departamento> = mutableListOf()
}
```

**4. Interacciones y Transacciones**

**Descripción**: Eventos o transacciones que ocurren entre entidades

**Ejemplos**:

- Comercio: Venta, Compra, Devolución
- Finanzas: Transferencia, Pago, Depósito
- Educación: Matrícula, Calificación, Asistencia

**Por qué son clases**: Representan momentos importantes con datos asociados

**Ejemplo - Sistema de ventas**:
```kotlin
class Venta(
    val numero: String,
    val fecha: LocalDateTime,
    val cliente: Cliente,
    val vendedor: Empleado,
    val items: List<ItemVenta>,
    var estado: EstadoVenta
) {
    fun calcularTotal(): Double = items.sumOf { it.subtotal }
    fun aplicarDescuento(porcentaje: Double)
    fun procesar(): Boolean
    fun cancelar(motivo: String)
}

enum class EstadoVenta { PENDIENTE, PROCESADA, CANCELADA, DEVUELTA }
```

**5. Eventos o Incidencias**

**Descripción**: Sucesos que ocurren y necesitan ser registrados

**Ejemplos**:

- Sistema de vuelos: Vuelo, Retraso, Cancelación
- Sistema de seguridad: Incidente, Alerta, Acceso
- Sistema de salud: Cita, Emergencia, Alta

**Diferencia con Transacciones**: Los eventos suelen ser menos estructurados y más orientados a registro/logging

**Ejemplo - Sistema de aeropuerto**:
```kotlin
class Vuelo(
    val numero: String,
    val origen: Aeropuerto,
    val destino: Aeropuerto,
    var horaSalidaProgramada: LocalDateTime,
    var horaSalidaReal: LocalDateTime?,
    var estado: EstadoVuelo
) {
    private val incidentes: MutableList<Incidente> = mutableListOf()
    
    fun reportarRetraso(minutos: Int, motivo: String) {
        incidentes.add(Incidente(tipo = TipoIncidente.RETRASO, descripcion = motivo))
        estado = EstadoVuelo.RETRASADO
    }
}

class Incidente(
    val timestamp: LocalDateTime = LocalDateTime.now(),
    val tipo: TipoIncidente,
    val descripcion: String
)
```

#### 6.2. Otras Fuentes para Identificar Clases

**Fuente 1: Diagramas existentes**

Si estás trabajando en un sistema existente:

- Diagramas E-R de la base de datos actual
- Diagramas de arquitectura
- Documentación técnica previa

**Fuente 2: Interfaces de usuario (wireframes, mockups)**

Los elementos visuales a menudo revelan clases:

- Formulario de "Registro de Cliente" → Clase Cliente
- Tabla de "Productos" → Clase Producto
- Pantalla de "Detalle de Pedido" → Clase Pedido

**Fuente 3: Casos de uso**

Cada caso de uso involucra actores y entidades:

- "Cliente realiza un pedido" → Cliente, Pedido
- "Sistema genera factura" → Factura
- "Administrador aprueba solicitud" → Administrador, Solicitud

**Fuente 4: Glosario del dominio**

Muchas organizaciones tienen glosarios de términos del negocio:

- Términos técnicos específicos del dominio
- Jerga del sector
- Conceptos legales o regulatorios

**Ejemplo - Dominio bancario**:

- CDT (Certificado de Depósito a Término)
- SEPA (Single Euro Payments Area)
- Swift Code

Estos términos especializados suelen ser clases importantes.

**Fuente 5: Expertos del dominio**

Las entrevistas con usuarios o expertos revelan:

- Conceptos que no aparecen en documentación formal
- Reglas de negocio no escritas
- Excepciones y casos especiales

!!! tip "Mejora práctica"
    Crea una lista de "Conceptos del Dominio" mientras entrevistas a expertos. Pregunta específicamente: "¿Qué conceptos son más importantes en tu trabajo diario?"

#### 6.3. Patrones Comunes de Clases

Con la experiencia, empezarás a reconocer patrones de clases que aparecen frecuentemente:

**Patrón 1: Entidad-Detalle**

- Entidad principal: Factura, Pedido, Orden
- Detalle: ItemFactura, ItemPedido, LineaOrden

**Patrón 2: Contenedor-Contenido**

- Contenedor: Carrito, Paquete, Contenedor
- Contenido: Producto, Artículo, Item

**Patrón 3: Maestro-Transacción**

- Maestro: Cliente, Producto, Cuenta
- Transacción: Venta, Movimiento, Operación

**Patrón 4: Catálogo-Instancia**

- Catálogo: TipoProducto, Plantilla, Modelo
- Instancia: Producto, Documento, Artículo

Reconocer estos patrones acelera la identificación de clases.

### 7. Errores Comunes al Identificar Clases y Cómo Evitarlos

Aprender de los errores comunes te ahorrará tiempo y frustración.

#### 7.1. Error 1: Sobre-diseño (Too Many Classes)

**Descripción**: Crear demasiadas clases, especialmente clases que podrían ser atributos

**Síntomas**:

- Clases con solo 1-2 atributos simples
- Clases que nunca tienen más de una instancia
- Jerarquías de herencia muy profundas (>3 niveles)

**Ejemplo del error**:
```kotlin
// ❌ MAL: Sobre-diseño
class Nombre(val primer: String, val segundo: String)
class Apellido(val paterno: String, val materno: String)
class Persona(val nombre: Nombre, val apellido: Apellido)

// ✅ MEJOR: Simplificado
class Persona(
    val nombre: String,
    val apellidoPaterno: String,
    val apellidoMaterno: String
)
```

**Cómo evitarlo**:

- Aplicar regla: "Si tiene menos de 3 propiedades Y no tiene comportamiento → Atributo"
- Preguntarse: "¿Realmente necesito gestionar esto independientemente?"

#### 7.2. Error 2: Sub-diseño (Missing Classes)

**Descripción**: No identificar clases importantes, dejando funcionalidad sin hogar

**Síntomas**:

- Métodos muy largos con mucha lógica
- Clases "Dios" con decenas de métodos
- Código difícil de entender o mantener

**Ejemplo del error**:
```kotlin
// ❌ MAL: Falta clase Préstamo
class Biblioteca {
    fun prestarLibro(usuario: Usuario, libro: Libro, dias: Int) {
        // 50 líneas de lógica aquí...
        // validar usuario, verificar disponibilidad,
        // registrar fecha, calcular fecha devolución,
        // actualizar inventario, enviar notificación...
    }
}

// ✅ MEJOR: Con clase Préstamo
class Prestamo(
    val usuario: Usuario,
    val copia: Copia,
    val fechaPrestamo: LocalDate,
    val diasPrestamo: Int
) {
    fun calcularFechaDevolucion(): LocalDate
    fun estaVencido(): Boolean
    fun devolver()
}
```

**Cómo evitarlo**:

- Si un método tiene >20 líneas, probablemente falta una clase
- Buscar "verbos importantes" que podrían ser clases (Préstamo, Reserva, Pedido)

#### 7.3. Error 3: Confundir Clases con Atributos

**Descripción**: Hacer clases de conceptos que deberían ser atributos simples

**Regla general**:

- **Atributo**: Valor simple sin comportamiento
- **Clase**: Múltiples propiedades O comportamiento complejo

**Ejemplos correctos e incorrectos**:

```kotlin
// ❌ MAL: Email no necesita ser clase aquí
class Email(val direccion: String)
class Usuario(val email: Email)

// ✅ MEJOR: Email como String
class Usuario(val email: String)

// ✅ PERO: Email como clase si tiene validación compleja
class Email(val direccion: String) {
    init {
        require(direccion.matches(Regex("^[^@]+@[^@]+\\.[^@]+$"))) { "Email inválido" }
    }
    fun dominio(): String = direccion.substringAfter("@")
    fun esEmpresarial(): Boolean = dominio().endsWith(".com") || dominio().endsWith(".org")
}
```

**Criterio de decisión**:

- Sin comportamiento → Atributo
- Con validación/comportamiento → Clase

#### 7.4. Error 4: Modelar Detalles de Implementación

**Descripción**: Incluir clases técnicas en el modelo conceptual

**Ejemplo del error**:
```kotlin
// ❌ MAL: Clases técnicas en modelo de dominio
class DatabaseConnection
class JSONParser
class HTTPClient
class LoggerService

// En un diagrama de clases de dominio no deberían aparecer
```

**Por qué está mal**: El diagrama de clases de dominio debe representar conceptos del negocio, no detalles técnicos.

**Solución**: 

- Modelo de dominio: Solo clases del negocio
- Diagrama de arquitectura: Clases técnicas aparte

#### 7.5. Error 5: Usar Nombres Genéricos o Vagos

**Descripción**: Clases con nombres como "Gestor", "Manejador", "Datos"

**Ejemplos de nombres malos**:

- GestorDatos
- ManejadorUsuarios
- ProcesadorInformacion
- ObjetoGeneral

**Por qué está mal**: No comunican responsabilidad clara

**Ejemplos de nombres buenos**:

- RepositorioUsuarios (almacenamiento)
- ValidadorCredenciales (validación)
- ServicioAutenticacion (lógica de negocio)
- CalculadoraPrecios (cálculo específico)

!!! tip "Consejo de nomenclatura"
    Usa nombres que reflejen claramente la responsabilidad y el propósito de la clase. Si necesitas usar "Gestor" o "Manejador", probablemente no has entendido bien la responsabilidad.

#### 7.6. Error 6: Ignorar la Multiplicidad

**Descripción**: No pensar en cuántas instancias existirán de cada clase

**Preguntas importantes**:

- ¿Cuántos X puede tener Y?
- ¿X puede existir sin Y?
- ¿La relación es uno-a-uno, uno-a-muchos, muchos-a-muchos?

**Ejemplo**:
```
// ❌ MAL: No especificar multiplicidad
Usuario ──── Préstamo

// ✅ BIEN: Especificar
Usuario 1 ────── * Préstamo
(Un usuario puede tener muchos préstamos)
```

#### 7.7. Error 7: No Validar con Escenarios Reales

**Descripción**: Crear modelo sin verificar que funciona para casos reales

**Cómo evitarlo**:
Recorre el modelo con ejemplos concretos:

**Ejemplo - Sistema de biblioteca**:

- "Ana presta el libro 'Don Quijote' el 1 de febrero"

    - ¿Tengo clase Usuario para Ana? ✅
    - ¿Tengo clase Libro para Don Quijote? ✅
    - ¿Tengo clase Préstamo para registrar la transacción? ✅
    - ¿Puedo calcular cuándo debe devolverlo? ✅

Si no puedes "recorrer" tus casos de uso con el modelo, falta algo.

!!! warning "Consejo de prevención"
    El 80% de estos errores se evitan con revisión por pares. Pide a un compañero que revise tu modelo antes de implementar.


### 8. Cómo Identificar Relaciones entre Clases: Conectando el Modelo

Las clases no existen aisladas - colaboran para cumplir los requisitos del sistema. Identificar las relaciones correctamente es tan importante como identificar las clases mismas.

#### 8.1. Tipos de Relaciones y Cuándo Usar Cada Una

Ya conoces los tipos de relaciones de secciones anteriores. Aquí nos enfocamos en **cómo identificarlas** en los requisitos.

**Herencia (Generalización): "Es un"**

**Cómo identificarla en el texto**:

- Palabras clave: "es un tipo de", "es una clase de", "se categoriza como"
- Ejemplo: "Un **profesor** es un tipo de **empleado**"
- Ejemplo: "Existen dos tipos de **cuenta**: **CuentaAhorro** y **CuentaCorriente**"

**Proceso de identificación**:

1. Busca clasificaciones o taxonomías
2. Identifica superclase (concepto general)
3. Identifica subclases (conceptos específicos)
4. Verifica que subclases comparten características de la superclase

**Ejemplo**:
```
"En la universidad hay diferentes tipos de personal: profesores, administrativos y personal de mantenimiento. Todos tienen nombre, DNI y fecha de contratación."

Análisis:
- Superclase: Personal (o Empleado)
- Subclases: Profesor, Administrativo, PersonalMantenimiento
- Atributos compartidos: nombre, DNI, fechaContratación
```

Diagrama:
```
          ┌──────────┐
          │ Empleado │
          └────△─────┘
               │
       ┌───────┼─────────┐
       │       │         │
┌──────┴───┐  ┌┴──────┐ ┌┴─────────────┐
│ Profesor │  │ Admin │ │ Mantenimiento│
└──────────┘  └───────┘ └──────────────┘
```

**Composición: "Es parte de" (dependencia fuerte)**

**Cómo identificarla**:

- Palabras clave: "consiste en", "contiene", "está compuesto de"
- Característica: La parte NO puede existir sin el todo
- Ejemplo: "Un **coche** tiene un **motor**. Si destruyes el coche, el motor deja de tener sentido en el sistema."

**Regla práctica**: Pregúntate "¿Tiene sentido que la parte exista sin el todo?"

- Composición: Motor sin Coche → No tiene sentido
- No composición: Empleado sin Empresa → Sí tiene sentido (puede cambiar de empresa)

**Ejemplo**:
```
"Una factura contiene varias líneas de factura. Cada línea especifica un producto, cantidad y precio."

Análisis:

- Todo: Factura
- Parte: LineaFactura
- Justificación: Una LineaFactura sin Factura no tiene sentido
```

Diagrama:
```
┌─────────┐        ┌──────────────┐
│ Factura │♦──────*│ LineaFactura │
└─────────┘        └──────────────┘
```

**Agregación: "Tiene un" (dependencia débil)**

**Cómo identificarla**:

- Palabras clave: "tiene", "contiene", "incluye"
- Característica: La parte PUEDE existir independientemente del todo
- Ejemplo: "Un **departamento** tiene **empleados**. Los empleados pueden cambiar de departamento."

**Ejemplo**:
```
"Un equipo de fútbol tiene jugadores. Los jugadores pueden ser transferidos a otros equipos."

Análisis:

- Todo: Equipo
- Parte: Jugador
- Justificación: Jugador puede existir sin Equipo específico
```

Diagrama:
```
┌────────┐        ┌──────────┐
│ Equipo │◇──────*│ Jugador  │
└────────┘        └──────────┘
```

**Asociación: Relación general**

**Cómo identificarla**:

- Es la relación por defecto si no es herencia, composición o agregación
- Palabras clave: "está relacionado con", "tiene relación con"
- Ejemplo: "Un **cliente** hace **pedidos**"

**Dependencia: Uso temporal**

**Cómo identificarla**:

- La clase usa a otra temporalmente (como parámetro, variable local)
- No mantiene referencia permanente
- Ejemplo: "El **calculador de impuestos** usa la información del **producto** para calcular el impuesto"

#### 8.2. Identificar Multiplicidad

La **multiplicidad** especifica cuántas instancias de una clase pueden estar asociadas con instancias de otra.

**Preguntas para identificar multiplicidad**:

Para la relación "Cliente ─── Pedido":

1. **De Cliente a Pedido**: "¿Cuántos pedidos puede tener un cliente?"

    - Respuesta: Cero o muchos (`0..*` o `*`)
   
2. **De Pedido a Cliente**: "¿Cuántos clientes puede tener un pedido?"

    - Respuesta: Exactamente uno (`1`)

Resultado:
```
Cliente 1 ────── * Pedido
```

**Técnica de identificación sistemática**:

**Paso 1**: Para cada relación, formula las preguntas en ambas direcciones

**Paso 2**: Usa esta tabla de decisión:

| Situación                 | Multiplicidad  | Notación     |
|---------------------------|----------------|--------------|
| Exactamente uno           | uno            | `1`          |
| Cero o uno (opcional)     | cero o uno     | `0..1`       |
| Uno o más (al menos uno)  | uno a muchos   | `1..*`       |
| Cero o más                | cero a muchos  | `*` o `0..*` |
| Rango específico          | rango          | `2..5`       |

**Ejemplo completo - Sistema universitario**:

```
"Un estudiante puede matricularse en varias asignaturas (mínimo 1, máximo 8). Una asignatura tiene entre 5 y 50 estudiantes."
```

Análisis: 

- Estudiante → Asignatura: 1 a 8 estudiantes por asignatura
- Asignatura → Estudiante: 5 a 50 estudiantes por asignatura

Diagrama:
```
┌───────────┐ 1..8    5..50 ┌────────────┐
│ Estudiante│───────────────│ Asignatura │
└───────────┘   matricula   └────────────┘
```

#### 8.3. Navegabilidad: Direccionalidad de las Relaciones

La **navegabilidad** indica qué clase "conoce" a la otra.

**Tipos de navegabilidad**:

**1. Bidireccional (ambas direcciones)**
```
Usuario ←→ Pedido
```
- Usuario conoce sus Pedidos
- Pedido conoce su Usuario

**2. Unidireccional (una dirección)**
```
Usuario → Pedido
```
- Usuario conoce sus Pedidos
- Pedido NO conoce su Usuario (no lo necesita)

**3. No navegable**
```
Usuario ─ Pedido
```
- Ninguno tiene referencia directa al otro
- Pueden estar conectados por una tercera clase

**¿Cómo decidir la navegabilidad?**

Pregunta clave: "¿Necesito acceder desde A a B? ¿Y desde B a A?"

**Ejemplo**:
```kotlin
// Bidireccional
class Usuario(val nombre: String) {
    val pedidos: MutableList<Pedido> = mutableListOf()
}

class Pedido(val numero: String, val usuario: Usuario)

// Unidireccional (solo Usuario → Pedido)
class Usuario(val nombre: String) {
    val pedidos: MutableList<Pedido> = mutableListOf()
}

class Pedido(val numero: String)  // No tiene referencia a Usuario
```

**Recomendación**: Comienza con unidireccional (menor acoplamiento). Añade bidireccionalidad solo si realmente la necesitas.

#### 8.4. Relaciones Muchos a Muchos: El Caso Especial

Las relaciones **muchos a muchos** (`* ─── *`) son comunes pero requieren atención especial.

**Problema**: En implementación, necesitan una clase intermedia (tabla de unión)

**Ejemplo - Matriculación**:
```
"Un estudiante se matricula en varias asignaturas. Una asignatura tiene varios estudiantes."
```

**Modelado simple** (conceptual):
```
Estudiante * ─────── * Asignatura
```

**Modelado detallado** (con clase de asociación):
```
┌───────────┐ 1     * ┌─────────────┐
│ Estudiante│─────────│ Matricula   │
└───────────┘         │─────────────│
                      │ - fecha     │
                      │ - semestre  │
                      └──────┬──────┘
                             │
                            *│
                      ┌──────┴──────┐
                      │ Asignatura  │
                      └─────────────┘
```

**¿Cuándo crear clase intermedia?**

**Crea clase intermedia si**: 

- La relación tiene atributos propios (fecha, calificación, etc.)
- La relación tiene comportamiento propio (métodos)
- Necesitas almacenar información histórica

**No creates clase intermedia si**:

- La relación es pura sin información adicional
- Puedes usar listas simples en ambas clases

**Ejemplo en código**:

```kotlin
// Sin clase intermedia (relación pura)
class Estudiante(val nombre: String) {
    val asignaturas: MutableList<Asignatura> = mutableListOf()
}

class Asignatura(val nombre: String) {
    val estudiantes: MutableList<Estudiante> = mutableListOf()
}

// Con clase intermedia (con información adicional)
class Estudiante(val nombre: String)

class Asignatura(val nombre: String)

class Matricula(
    val estudiante: Estudiante,
    val asignatura: Asignatura,
    val fecha: LocalDate,
    val semestre: String,
    var calificacion: Double? = null
) {
    fun aprobo(): Boolean = (calificacion ?: 0.0) >= 5.0
}
```

#### 8.5. Proceso Paso a Paso para Identificar Relaciones

**Paso 1: Listar todas las clases**

Ejemplo: Usuario, Producto, Carrito, Pedido, ItemPedido

**Paso 2: Para cada par de clases, pregúntate**:

- "¿Existe una relación lógica entre estas dos clases?"
- "¿Una necesita conocer a la otra para funcionar?"

**Paso 3: Para cada relación identificada**:

- ¿Qué tipo de relación es? (herencia, composición, asociación, etc.)
- ¿Cuál es la multiplicidad?
- ¿Es navegable? ¿En qué dirección?

**Paso 4: Documentar**:

- Dibuja la relación en el diagrama
- Añade multiplicidad
- Opcionalmente, añade nombre a la relación

**Ejemplo completo - E-Commerce**:

```
Clases: Usuario, Carrito, Producto, Pedido

Análisis:

1. Usuario - Carrito: 

    - Relación: Composición (♦)
    - Multiplicidad: 1 Usuario tiene 1 Carrito
    - Navegabilidad: Usuario → Carrito
   
2. Carrito - Producto:

    - Relación: Agregación (◇) o Asociación con clase intermedia
    - Multiplicidad: 1 Carrito tiene * Productos
    - Mejor: Crear ItemCarrito intermedio
   
3. Usuario - Pedido:

    - Relación: Asociación
    - Multiplicidad: 1 Usuario realiza * Pedidos
    - Navegabilidad: Bidireccional

4. Pedido - Producto:

    - Relación: Asociación con clase intermedia (ItemPedido)
    - Multiplicidad: 1 Pedido tiene * ItemPedido, 1 Producto en * ItemPedido
```

Diagrama resultante:
```
       ┌─────────┐
       │ Usuario │
       └────┬────┘
            │1
            │tiene
           ♦│
       ┌────┴────────┐
       │  Carrito    │
       └─────┬───────┘
             │1
             │contiene
             │
            *│
       ┌─────┴──────────┐
       │  ItemCarrito   │
       └────────────────┘
             │*
             │referencia
             │1
       ┌─────┴──────────┐
       │   Producto     │
       └────────────────┘
```

!!! tip "Consejo práctico"
    No intentes identificar todas las relaciones de golpe. Hazlo iterativamente:
    1. Primeras relaciones obvias
    2. Refinamiento y relaciones secundarias
    3. Validación con casos de uso


### 9. Buenas Prácticas para Crear Diagramas de Clases Efectivos

Crear un buen diagrama de clases va más allá de la notación correcta. Requiere aplicar principios de diseño que resulten en sistemas mantenibles.

#### 9.1. Principio de Responsabilidad Única (SRP - Single Responsibility Principle)

**Definición**: Una clase debe tener una, y solo una, razón para cambiar. En otras palabras, cada clase debe tener una única responsabilidad bien definida.

**¿Por qué es importante?**

- Facilita el mantenimiento: Cambios en un aspecto no afectan otros
- Mejora la comprensión: Es más fácil entender qué hace una clase
- Reduce acoplamiento: Menos dependencias entre clases
- Facilita testing: Más fácil probar una responsabilidad única

**Señales de violación del SRP**:

- Clase con más de 10-15 métodos públicos
- Nombre de clase con "Y" o "Gestor" (ej: "GestorUsuariosYPermisos")
- Clase que cambia por múltiples razones diferentes
- Métodos que no están relacionados entre sí

**Ejemplo de violación**:

```kotlin
// ❌ MAL: Clase con múltiples responsabilidades
class Usuario(
    val nombre: String,
    var email: String,
    var password: String
) {
    // Responsabilidad 1: Gestión de usuario
    fun cambiarEmail(nuevoEmail: String) {
        email = nuevoEmail
    }
    
    // Responsabilidad 2: Autenticación
    fun validarPassword(pass: String): Boolean {
        return password == pass
    }
    
    // Responsabilidad 3: Envío de emails
    fun enviarEmailBienvenida() {
        // Lógica de envío de email
        println("Enviando email a $email")
    }
    
    // Responsabilidad 4: Persistencia
    fun guardarEnBaseDatos() {
        // Lógica de guardado
        println("Guardando usuario en BD")
    }
    
    // Responsabilidad 5: Logging
    fun registrarAccion(accion: String) {
        println("Usuario $nombre realizó: $accion")
    }
}
```

**Problemas de este diseño**:

- Si cambia la forma de enviar emails, hay que modificar Usuario
- Si cambia la base de datos, hay que modificar Usuario
- Si cambia el sistema de logging, hay que modificar Usuario
- La clase tiene demasiadas razones para cambiar

**Solución aplicando SRP**:

```kotlin
// ✅ BIEN: Responsabilidades separadas

// Responsabilidad 1: Representar un usuario (entidad del dominio)
class Usuario(
    val id: Int,
    var nombre: String,
    var email: String
) {
    fun cambiarEmail(nuevoEmail: String) {
        email = nuevoEmail
    }
}

// Responsabilidad 2: Autenticación
class ServicioAutenticacion {
    fun validarCredenciales(email: String, password: String): Boolean {
        // Lógica de validación
        return true
    }
    
    fun cambiarPassword(usuario: Usuario, nuevaPassword: String) {
        // Lógica de cambio de contraseña
    }
}

// Responsabilidad 3: Comunicación
class ServicioEmail {
    fun enviarBienvenida(usuario: Usuario) {
        println("Enviando email de bienvenida a ${usuario.email}")
    }
    
    fun enviarRecuperacionPassword(usuario: Usuario) {
        println("Enviando email de recuperación a ${usuario.email}")
    }
}

// Responsabilidad 4: Persistencia
class RepositorioUsuarios {
    private val usuarios = mutableListOf<Usuario>()
    
    fun guardar(usuario: Usuario) {
        usuarios.add(usuario)
    }
    
    fun buscarPorEmail(email: String): Usuario? {
        return usuarios.find { it.email == email }
    }
}

// Responsabilidad 5: Auditoría
class ServicioAuditoria {
    fun registrarAccion(usuario: Usuario, accion: String) {
        println("[${java.time.LocalDateTime.now()}] Usuario ${usuario.nombre}: $accion")
    }
}
```

**Beneficios del diseño refactorizado**:

- Cada clase tiene una responsabilidad clara
- Cambios en email no afectan a autenticación
- Cambios en BD no afectan a logging
- Más fácil de testear (puedes mockear cada servicio)
- Más fácil de extender (nuevo tipo de notificación = nueva clase)

**Diagrama comparativo**:

```
❌ ANTES:
┌─────────────────────────┐
│       Usuario           │
│─────────────────────────│
│ - nombre                │
│ - email                 │
│ - password              │
│─────────────────────────│
│ + cambiarEmail()        │
│ + validarPassword()     │
│ + enviarEmailBienvenida()│
│ + guardarEnBaseDatos()  │
│ + registrarAccion()     │
└─────────────────────────┘

✅ DESPUÉS:
┌──────────┐     usa    ┌───────────────────┐
│ Usuario  │────────────│ ServicioAuth      │
└──────────┘            └───────────────────┘
     │ usa
     ├────────────────────┐
     │                    │
┌────┴──────────┐  ┌──────┴──────────────┐
│ServicioEmail  │  │ RepositorioUsuarios │
└───────────────┘  └─────────────────────┘
     │
     │ usa
┌────┴──────────────┐
│ServicioAuditoria  │
└───────────────────┘
```

#### 9.2. Alta Cohesión

**Definición**: Los elementos dentro de una clase deben estar fuertemente relacionados entre sí. Una clase cohesiva hace una cosa y la hace bien.

**Medidas de cohesión**:

- **Cohesión funcional** (mejor): Todos los métodos trabajan hacia un objetivo común
- **Cohesión secuencial**: Los métodos se ejecutan en secuencia
- **Cohesión comunicacional**: Los métodos usan los mismos datos
- **Cohesión temporal**: Los métodos se ejecutan al mismo tiempo
- **Cohesión lógica** (peor): Los métodos solo están agrupados por ser similares

**Ejemplo de baja cohesión**:

```kotlin
// ❌ MAL: Baja cohesión
class UtilidadesVarias {
    fun calcularIVA(precio: Double): Double {
        return precio * 0.21
    }
    
    fun validarEmail(email: String): Boolean {
        return email.contains("@")
    }
    
    fun formatearFecha(fecha: LocalDate): String {
        return fecha.toString()
    }
    
    fun conectarBaseDatos(): Connection {
        // Lógica de conexión
        return mockConnection()
    }
}
```

**Problema**: Los métodos no están relacionados entre sí. No hay un concepto unificador.

**Ejemplo de alta cohesión**:

```kotlin
// ✅ BIEN: Alta cohesión
class CalculadoraPrecios {
    private val tasaIVA = 0.21
    
    fun calcularIVA(precioBase: Double): Double {
        return precioBase * tasaIVA
    }
    
    fun calcularPrecioFinal(precioBase: Double): Double {
        return precioBase + calcularIVA(precioBase)
    }
    
    fun calcularDescuento(precio: Double, porcentaje: Double): Double {
        return precio * (porcentaje / 100.0)
    }
    
    fun calcularPrecioConDescuento(
        precioBase: Double, 
        porcentajeDescuento: Double
    ): Double {
        val descuento = calcularDescuento(precioBase, porcentajeDescuento)
        val precioConDescuento = precioBase - descuento
        return calcularPrecioFinal(precioConDescuento)
    }
}
```

**Por qué es cohesiva**: Todos los métodos están relacionados con el cálculo de precios.

#### 9.3. Bajo Acoplamiento

**Definición**: Las clases deben depender lo menos posible de otras clases. Cada dependencia es un "cable" que conecta dos clases - menos cables = más flexibilidad.

**Tipos de acoplamiento (de peor a mejor)**:

1. **Acoplamiento de contenido**: Una clase modifica datos internos de otra (muy malo)
2. **Acoplamiento común**: Clases comparten datos globales (malo)
3. **Acoplamiento de control**: Una clase controla el flujo de otra (malo)
4. **Acoplamiento de datos**: Clases comparten datos mediante parámetros (aceptable)
5. **Acoplamiento de mensaje**: Clases se comunican solo mediante interfaces (bueno)
6. **Sin acoplamiento**: Clases independientes (ideal, pero poco práctico)

**Señales de alto acoplamiento**:

- Clases que usan muchos métodos de otras clases
- Cambios en una clase requieren cambios en muchas otras
- Clases que conocen detalles internos de otras
- Jerarquías de dependencia profundas

**Ejemplo de alto acoplamiento**:

```kotlin
// ❌ MAL: Alto acoplamiento
class Pedido(val cliente: Cliente) {
    fun procesarPago() {
        // Accede directamente a detalles internos del cliente
        if (cliente.tarjetaCredito.saldo > calcularTotal()) {
            cliente.tarjetaCredito.saldo -= calcularTotal()
            cliente.historialCompras.add(this)
            cliente.puntosFidelidad += calcularPuntos()
        }
    }
    
    private fun calcularTotal(): Double = 100.0
    private fun calcularPuntos(): Int = 10
}

class Cliente(
    val tarjetaCredito: TarjetaCredito,
    val historialCompras: MutableList<Pedido>,
    var puntosFidelidad: Int
)
```

**Problemas**:

- Pedido conoce la estructura interna de Cliente
- Pedido conoce la estructura de TarjetaCredito
- Si cambias Cliente, probablemente debes cambiar Pedido

**Ejemplo de bajo acoplamiento**:

```kotlin
// ✅ BIEN: Bajo acoplamiento usando interfaces
interface ProcesadorPagos {
    fun procesarPago(monto: Double): Boolean
}

interface GestorPuntos {
    fun agregarPuntos(puntos: Int)
}

class Pedido(
    private val procesadorPagos: ProcesadorPagos,
    private val gestorPuntos: GestorPuntos
) {
    fun procesarPago() {
        val exito = procesadorPagos.procesarPago(calcularTotal())
        if (exito) {
            gestorPuntos.agregarPuntos(calcularPuntos())
        }
    }
    
    private fun calcularTotal(): Double = 100.0
    private fun calcularPuntos(): Int = 10
}

class Cliente : ProcesadorPagos, GestorPuntos {
    private val tarjetaCredito: TarjetaCredito = TarjetaCredito()
    private var puntosFidelidad: Int = 0
    
    override fun procesarPago(monto: Double): Boolean {
        return tarjetaCredito.cobrar(monto)
    }
    
    override fun agregarPuntos(puntos: Int) {
        puntosFidelidad += puntos
    }
}
```

**Beneficios**:

- Pedido no conoce detalles internos de Cliente
- Puedes cambiar la implementación de Cliente sin afectar Pedido
- Puedes probar Pedido con mocks de las interfaces
- Más flexible: podrías usar diferentes procesadores de pago

**Estrategias para reducir acoplamiento**:

1. **Usar interfaces** en vez de clases concretas
2. **Inyección de dependencias** en vez de crear objetos dentro de la clase
3. **Ley de Demeter** ("no hables con extraños")
4. **Ocultamiento de información** (encapsulación fuerte)

#### 9.4. Ley de Demeter (Principio del Mínimo Conocimiento)

**Definición**: Un objeto solo debería llamar métodos de:

- Sí mismo
- Sus parámetros
- Objetos que crea
- Sus componentes directos

**No debería llamar** métodos de objetos retornados por otros métodos.

**Violación clásica**:

```kotlin
// ❌ MAL: Violación de Ley de Demeter
class Pedido(val cliente: Cliente) {
    fun obtenerCiudadCliente(): String {
        // Encadenamiento excesivo
        return cliente.getDireccion().getCiudad().getNombre()
    }
}
```

**Problemas**:

- Pedido conoce 3 niveles de la estructura de Cliente
- Si cambias cualquier nivel intermedio, Pedido se rompe

**Solución**:

```kotlin
// ✅ BIEN: Respeta Ley de Demeter
class Cliente {
    private val direccion: Direccion = Direccion()
    
    // Método de conveniencia que oculta la estructura interna
    fun obtenerCiudad(): String {
        return direccion.obtenerNombreCiudad()
    }
}

class Pedido(val cliente: Cliente) {
    fun obtenerCiudadCliente(): String {
        // Solo un nivel de acceso
        return cliente.obtenerCiudad()
    }
}
```

#### 9.5. Encapsulamiento Efectivo

**Principios de encapsulamiento**:

1. **Ocultar datos**: Atributos privados, acceso mediante métodos
2. **Ocultar implementación**: No exponer detalles internos
3. **Exponer comportamiento**: Interfaces públicas claras

**Ejemplo de mal encapsulamiento**:

```kotlin
// ❌ MAL: Expone demasiado
class CuentaBancaria {
    var saldo: Double = 0.0  // Público - cualquiera puede modificar
    var movimientos: MutableList<Double> = mutableListOf()  // Mutable y público
}

// Uso problemático
val cuenta = CuentaBancaria()
cuenta.saldo = 1000000.0  // ¡Fraude! Modificación directa
cuenta.movimientos.clear()  // ¡Borró el historial!
```

**Ejemplo de buen encapsulamiento**:

```kotlin
// ✅ BIEN: Encapsulamiento apropiado
class CuentaBancaria(private var saldo: Double = 0.0) {
    private val movimientos: MutableList<Movimiento> = mutableListOf()
    
    // Acceso controlado al saldo
    fun obtenerSaldo(): Double = saldo
    
    // Modificación controlada con validación
    fun depositar(monto: Double) {
        require(monto > 0) { "El monto debe ser positivo" }
        saldo += monto
        movimientos.add(Movimiento(tipo = "DEPOSITO", monto = monto))
    }
    
    fun retirar(monto: Double): Boolean {
        require(monto > 0) { "El monto debe ser positivo" }
        return if (saldo >= monto) {
            saldo -= monto
            movimientos.add(Movimiento(tipo = "RETIRO", monto = monto))
            true
        } else {
            false
        }
    }
    
    // Vista de solo lectura del historial
    fun obtenerHistorial(): List<Movimiento> = movimientos.toList()
}

data class Movimiento(
    val tipo: String,
    val monto: Double,
    val fecha: LocalDateTime = LocalDateTime.now()
)
```

**Beneficios**:

- No se puede modificar el saldo directamente
- Validaciones aseguran integridad de datos
- Historial inmutable desde el exterior
- Cambios internos no afectan a clientes de la clase

#### 9.6. Favorecer Composición sobre Herencia

**Regla general**: Usa composición (tener un) en vez de herencia (ser un) cuando sea posible.

**¿Por qué?**

- Mayor flexibilidad
- Menor acoplamiento
- Evita jerarquías frágiles
- Más fácil de cambiar en runtime

**Ejemplo de abuso de herencia**:

```kotlin
// ❌ CUESTIONABLE: Herencia para reutilizar código
class ArrayList {
    fun add(elemento: Any) { }
    fun remove(elemento: Any) { }
    fun size(): Int = 0
}

class Pila : ArrayList() {
    fun push(elemento: Any) = add(elemento)
    fun pop(): Any? {
        if (size() > 0) {
            val elem = get(size() - 1)
            remove(elem)
            return elem
        }
        return null
    }
}
```

**Problema**: Pila expone métodos de ArrayList que no deberían estar disponibles (add, remove directos)

**Mejor con composición**:

```kotlin
// ✅ MEJOR: Composición
class Pila {
    private val elementos = mutableListOf<Any>()
    
    fun push(elemento: Any) {
        elementos.add(elemento)
    }
    
    fun pop(): Any? {
        return if (elementos.isNotEmpty()) {
            elementos.removeAt(elementos.size - 1)
        } else {
            null
        }
    }
    
    fun size(): Int = elementos.size
    
    fun isEmpty(): Boolean = elementos.isEmpty()
}
```

**Cuándo sí usar herencia**:

- Hay una relación "es-un" genuina
- La subclase ES un tipo más específico de la superclase
- Polimorfismo es esencial
- Ejemplo: Perro ES un Animal

**Cuándo usar composición**:

- Relación "tiene-un" o "usa-un"
- Quieres reutilizar código pero no hay relación "es-un"
- Necesitas cambiar comportamiento en runtime
- Ejemplo: Coche TIENE un Motor


### 10. Proceso Completo: Ejemplo Paso a Paso

Para consolidar todos los conceptos, vamos a realizar un análisis completo desde cero de un sistema real.

#### 10.1. Enunciado del Problema: Sistema de Gestión de Gimnasio

**Descripción del sistema**:

> "Un gimnasio necesita un sistema para gestionar sus operaciones. Los clientes se registran proporcionando nombre, teléfono y fecha de nacimiento. Cada cliente puede contratar diferentes tipos de membresías: mensual, trimestral o anual. Las membresías tienen un precio y fecha de inicio y vencimiento.
>
> El gimnasio ofrece clases grupales como yoga, spinning y pilates. Cada clase tiene un instructor asignado, un horario específico (día y hora), capacidad máxima y sala donde se imparte. Los clientes pueden reservar plazas en las clases, pero no pueden exceder la capacidad máxima.
>
> Los instructores son empleados del gimnasio con nombre, especialidad y horarios de disponibilidad. Un instructor puede impartir múltiples clases, pero no puede tener dos clases al mismo tiempo.
>
> El gimnasio tiene diferentes salas (Sala A, B, C) con capacidades diferentes. El sistema debe registrar la asistencia de clientes a las clases para generar estadísticas."

#### 10.2. Paso 1: Análisis de Sustantivos

**Sustantivos identificados** (marcados en el texto):

1. Gimnasio
2. Sistema
3. Operaciones
4. Clientes
5. Nombre
6. Teléfono
7. Fecha de nacimiento
8. Tipos de membresías
9. Membresía
10. Mensual, trimestral, anual (tipos)
11. Precio
12. Fecha de inicio
13. Fecha de vencimiento
14. Clases grupales
15. Yoga, spinning, pilates (tipos)
16. Instructor
17. Horario
18. Día
19. Hora
20. Capacidad máxima
21. Sala
22. Reserva
23. Plaza
24. Empleados
25. Especialidad
26. Horarios de disponibilidad
27. Salas (A, B, C)
28. Capacidades
29. Asistencia
30. Estadísticas

#### 10.3. Paso 2: Filtrado de Candidatos

Aplicamos los criterios de descarte:

**Descartar por ser demasiado genéricos**:

- Sistema: Demasiado genérico
- Operaciones: No es una entidad concreta
- Estadísticas: Es un resultado, no una entidad

**Descartar por ser atributos**:

- Nombre: Atributo de Cliente
- Teléfono: Atributo de Cliente
- Fecha de nacimiento: Atributo de Cliente
- Precio: Atributo de Membresía
- Fecha de inicio: Atributo de Membresía
- Fecha de vencimiento: Atributo de Membresía
- Horario, Día, Hora: Atributos de Clase
- Capacidad máxima: Atributo de Clase/Sala
- Especialidad: Atributo de Instructor

**Descartar por redundancia**:

- Empleados: Instructor ES un empleado (usar solo Instructor)
- Plaza: Es la misma entidad que Reserva

**Considerar tipos como enums o subclases**:
- Tipos de membresías (mensual, trimestral, anual): Enum o atributo
- Tipos de clases (yoga, spinning, pilates): Atributo o catálogo

**Clases candidatas finales**:

1. **Cliente**: Entidad principal del dominio
2. **Membresía**: Representa contrato de servicio
3. **Clase**: Actividad grupal que se ofrece
4. **Instructor**: Persona que imparte clases
5. **Sala**: Espacio físico donde ocurren las clases
6. **Reserva**: Asociación entre Cliente y Clase
7. **Asistencia**: Registro de que un cliente asistió a una clase
8.  **Gimnasio**: Podría ser la clase principal del sistema

#### 10.4. Paso 3: Definir Responsabilidades

**Cliente**:

- Responsabilidad: Representar un miembro del gimnasio
- Atributos: id, nombre, teléfono, fechaNacimiento
- Métodos: obtenerEdad(), tieneMembresiActiva()

**Membresía**:

- Responsabilidad: Gestionar el contrato de servicio
- Atributos: id, tipo, precio, fechaInicio, fechaVencimiento, cliente
- Métodos: estaVigente(), renovar(), calcularPrecio()

**Clase**:

- Responsabilidad: Representar una actividad programada
- Atributos: id, nombre, instructor, sala, horario, capacidadMaxima
- Métodos: tieneEspacioDisponible(), obtenerNumeroReservas()

**Instructor**:

- Responsabilidad: Persona que imparte clases
- Atributos: id, nombre, especialidad
- Métodos: puedeImpartir(clase), tieneDisponibilidad(horario)

**Sala**:

- Responsabilidad: Espacio físico
- Atributos: id, nombre, capacidad
- Métodos: estaDisponible(horario)

**Reserva**:

- Responsabilidad: Asociar cliente con clase
- Atributos: id, cliente, clase, fechaReserva
- Métodos: cancelar(), confirmar()

**Asistencia**:

- Responsabilidad: Registrar asistencia real
- Atributos: id, reserva, fechaAsistencia, asistio
- Métodos: marcarAsistencia()

#### 10.5. Paso 4: Identificar Relaciones

**Cliente - Membresía**:

- Tipo: Composición (♦) o Asociación fuerte
- Multiplicidad: 1 Cliente tiene 0..1 Membresía activa (puede tener historial de varias)
- Navegabilidad: Cliente → Membresía

**Cliente - Reserva**:

- Tipo: Agregación (◇)
- Multiplicidad: 1 Cliente tiene * Reservas
- Navegabilidad: Bidireccional

**Clase - Reserva**:

- Tipo: Agregación (◇)
- Multiplicidad: 1 Clase tiene * Reservas
- Navegabilidad: Bidireccional

**Clase - Instructor**:

- Tipo: Asociación
- Multiplicidad: * Clases tienen 1 Instructor, 1 Instructor imparte * Clases
- Navegabilidad: Bidireccional

**Clase - Sala**:

- Tipo: Asociación
- Multiplicidad: * Clases se imparten en 1 Sala, 1 Sala tiene * Clases
- Navegabilidad: Clase → Sala

**Reserva - Asistencia**:

- Tipo: Composición (♦)
- Multiplicidad: 1 Reserva tiene 0..1 Asistencia
- Navegabilidad: Reserva → Asistencia

#### 10.6. Paso 5: Diagrama UML Resultante

```
┌─────────────┐ 1          0..1 ┌──────────────┐
│   Cliente   │♦───────────────│  Membresía   │
│─────────────│  tiene         │──────────────│
│ - id        │                │ - id         │
│ - nombre    │                │ - tipo       │
│ - telefono  │                │ - precio     │
│ - fechaNac  │                │ - fechaIni   │
│─────────────│                │ - fechaVenc  │
│+ getEdad()  │                │──────────────│
│+ tieneMembr │                │+ estaVigente │
└─────────────┘                └──────────────┘
       │1
       │
       │ realiza
       │
      *│
┌──────┴──────┐              ┌──────────────┐
│   Reserva   │*          1  │    Clase     │
│─────────────│──────────────│──────────────│
│ - id        │ para         │ - id         │
│ - fechaRes  │              │ - nombre     │
│─────────────│              │ - horario    │
│+ cancelar() │              │ - capacidad  │
└─────────────┘              │──────────────│
       │1                    │+ hayEspacio()│
       │                     └───────┬──────┘
       │ tiene                       │1
       │                             │ imparte
       │0..1                         │*
┌──────┴──────┐              ┌───────┴──────┐
│  Asistencia │              │  Instructor  │
│─────────────│              │──────────────│
│ - id        │              │ - id         │
│ - asistio   │              │ - nombre     │
│ - fecha     │              │ - especial   │
│─────────────│              │──────────────│
│+ marcar()   │              │+ puedImp()   │
└─────────────┘              └──────────────┘
                                     
                                ┌──────────┐
                                │   Sala   │
                            1  *│──────────│
                      ┌─────────│ - id     │
                      │se imp en│ - nombre │
                      │         │ - capac  │
                      │         │──────────│
                      │         │+ estaDisp│
                      │         └──────────┘
┌─────────────────────┘
│ Clase
└─────────────────────
```

#### 10.7. Paso 6: Implementación en Kotlin

```kotlin
// Enums para tipos
enum class TipoMembresia(val meses: Int, val precio: Double) {
    MENSUAL(1, 50.0),
    TRIMESTRAL(3, 130.0),
    ANUAL(12, 480.0)
}

enum class TipoClase {
    YOGA, SPINNING, PILATES, CROSSFIT
}

// Entidades principales
data class Cliente(
    val id: Int,
    var nombre: String,
    var telefono: String,
    val fechaNacimiento: LocalDate
) {
    private var membresiaActual: Membresia? = null
    private val reservas: MutableList<Reserva> = mutableListOf()
    
    fun obtenerEdad(): Int {
        return Period.between(fechaNacimiento, LocalDate.now()).years
    }
    
    fun tieneMembresiActiva(): Boolean {
        return membresiaActual?.estaVigente() ?: false
    }
    
    fun contratarMembresia(tipo: TipoMembresia): Membresia {
        val nuevaMembresia = Membresia(
            id = generarId(),
            tipo = tipo,
            cliente = this
        )
        membresiaActual = nuevaMembresia
        return nuevaMembresia
    }
    
    fun reservarClase(clase: Clase): Reserva? {
        if (!tieneMembresiActiva()) {
            println("Debe tener membresía activa para reservar")
            return null
        }
        
        if (!clase.hayEspacioDisponible()) {
            println("Clase llena")
            return null
        }
        
        val reserva = Reserva(
            id = generarId(),
            cliente = this,
            clase = clase
        )
        reservas.add(reserva)
        return reserva
    }
}

data class Membresia(
    val id: Int,
    val tipo: TipoMembresia,
    val cliente: Cliente,
    val fechaInicio: LocalDate = LocalDate.now()
) {
    val fechaVencimiento: LocalDate = fechaInicio.plusMonths(tipo.meses.toLong())
    val precio: Double = tipo.precio
    
    fun estaVigente(): Boolean {
        return LocalDate.now().isBefore(fechaVencimiento) || 
               LocalDate.now().isEqual(fechaVencimiento)
    }
    
    fun diasRestantes(): Long {
        return ChronoUnit.DAYS.between(LocalDate.now(), fechaVencimiento)
    }
    
    fun renovar(): Membresia {
        return Membresia(
            id = generarId(),
            tipo = tipo,
            cliente = cliente,
            fechaInicio = fechaVencimiento.plusDays(1)
        )
    }
}

data class Instructor(
    val id: Int,
    var nombre: String,
    var especialidad: String
) {
    private val clases: MutableList<Clase> = mutableListOf()
    
    fun agregarClase(clase: Clase) {
        clases.add(clase)
    }
    
    fun obtenerClases(): List<Clase> = clases.toList()
    
    fun tieneDisponibilidad(horario: LocalDateTime): Boolean {
        return clases.none { 
            it.horario == horario 
        }
    }
}

data class Sala(
    val id: Int,
    val nombre: String,
    val capacidad: Int
) {
    fun estaDisponible(horario: LocalDateTime): Boolean {
        // Lógica para verificar disponibilidad
        return true
    }
}

data class Clase(
    val id: Int,
    val tipo: TipoClase,
    val instructor: Instructor,
    val sala: Sala,
    val horario: LocalDateTime,
    val capacidadMaxima: Int = sala.capacidad
) {
    private val reservas: MutableList<Reserva> = mutableListOf()
    
    init {
        instructor.agregarClase(this)
    }
    
    fun hayEspacioDisponible(): Boolean {
        return reservas.size < capacidadMaxima
    }
    
    fun obtenerNumeroReservas(): Int = reservas.size
    
    fun agregarReserva(reserva: Reserva) {
        if (hayEspacioDisponible()) {
            reservas.add(reserva)
        }
    }
    
    fun obtenerPorcentajeOcupacion(): Double {
        return (reservas.size.toDouble() / capacidadMaxima) * 100
    }
}

data class Reserva(
    val id: Int,
    val cliente: Cliente,
    val clase: Clase,
    val fechaReserva: LocalDateTime = LocalDateTime.now()
) {
    private var asistencia: Asistencia? = null
    var estado: EstadoReserva = EstadoReserva.CONFIRMADA
    
    init {
        clase.agregarReserva(this)
    }
    
    fun cancelar() {
        estado = EstadoReserva.CANCELADA
    }
    
    fun marcarAsistencia() {
        asistencia = Asistencia(
            id = generarId(),
            reserva = this,
            asistio = true
        )
    }
}

enum class EstadoReserva {
    CONFIRMADA, CANCELADA, COMPLETADA
}

data class Asistencia(
    val id: Int,
    val reserva: Reserva,
    val fechaAsistencia: LocalDateTime = LocalDateTime.now(),
    var asistio: Boolean = false
)

// Función auxiliar para generar IDs
private var contadorId = 1
fun generarId(): Int = contadorId++
```

#### 10.8. Paso 7: Validación con Casos de Uso

**Caso de Uso 1**: Cliente reserva una clase

```kotlin
// Crear entidades
val cliente = Cliente(1, "Ana García", "123456789", LocalDate.of(1990, 5, 15))
val instructor = Instructor(1, "Carlos López", "Yoga")
val sala = Sala(1, "Sala A", 20)
val clase = Clase(
    id = 1,
    tipo = TipoClase.YOGA,
    instructor = instructor,
    sala = sala,
    horario = LocalDateTime.now().plusDays(1)
)

// Cliente contrata membresía
val membresia = cliente.contratarMembresia(TipoMembresia.MENSUAL)
println("Membresía vigente: ${membresia.estaVigente()}")

// Cliente reserva clase
val reserva = cliente.reservarClase(clase)
println("Reserva exitosa: ${reserva != null}")
println("Espacios ocupados: ${clase.obtenerNumeroReservas()}/${clase.capacidadMaxima}")
```

**Resultado**: ✅ El modelo permite este flujo completo

**Caso de Uso 2**: Marcar asistencia

```kotlin
// El día de la clase
reserva?.marcarAsistencia()
println("Asistencia registrada")
```

**Resultado**: ✅ El modelo soporta este caso

#### 10.9. Lecciones del Ejemplo

**Decisiones de diseño clave**:

1. **Reserva como clase separada**: Permite almacenar información adicional (fecha de reserva, estado)
2. **Asistencia como clase separada**: Diferencia entre reservar y asistir
3. **Membresía vinculada a Cliente**: Facilita verificar estado de membresía
4. **Enum para tipos**: Evita duplicación y errores de escritura

**Alternativas consideradas**:

- ¿Gimnasio como clase?: Decidimos no incluirla porque no agrega valor en este alcance
- ¿TipoClase como clase vs Enum?: Enum es suficiente; sería clase si tuviera atributos propios

### 11. Validación del Modelo de Clases: ¿Es Correcto?

Un modelo puede ser sintácticamente correcto pero semánticamente incorrecto. La validación asegura que realmente funciona.

#### 11.1. Técnicas de Validación

**1. Recorrido de Casos de Uso (CRC Cards - Class Responsibility Collaboration)**

Para cada caso de uso:

- Identifica qué clase es responsable de cada paso
- Verifica que cada responsabilidad esté asignada
- Confirma que las colaboraciones existen

**Ejemplo**:
```
Caso: "Cliente reserva una clase"
1. Cliente inicia la reserva → Responsable: Cliente
2. Verificar membresía activa → Responsable: Cliente
3. Verificar espacio disponible → Responsable: Clase
4. Crear reserva → Responsable: Sistema (o Clase Gimnasio)
5. Registrar reserva → Responsable: Reserva

✅ Todas las responsabilidades están cubiertas
```

**2. Verificación de Completitud**

Preguntas de verificación:

- ¿Todos los requisitos funcionales tienen clases responsables?
- ¿Todas las entidades del dominio están representadas?
- ¿Hay casos de uso que no pueden realizarse con el modelo actual?

**3. Verificación de Consistencia**

- ¿Hay contradicciones en las relaciones?
- ¿Las multiplicidades tienen sentido?
- ¿Los nombres son consistentes?

**4. Prueba de Escalabilidad Mental**

Imagina escenarios extremos:

- "¿Qué pasa si hay 10,000 clientes?"
- "¿Qué pasa si un cliente cancela una reserva?"
- "¿Cómo se maneja la renovación automática de membresías?"

Si no puedes responder estas preguntas con tu modelo, probablemente falta algo.

#### 11.2. Checklist de Validación

**Estructura**:

- [ ] Cada clase tiene un nombre descriptivo
- [ ] Cada clase tiene responsabilidades claras
- [ ] No hay clases redundantes
- [ ] No hay clases "Dios" (con demasiadas responsabilidades)

**Relaciones**:

- [ ] Todas las relaciones tienen multiplicidad definida
- [ ] Las relaciones tienen el tipo correcto
- [ ] No hay dependencias circulares problemáticas
- [ ] Las navegabilidades están bien definidas

**Principios de Diseño**:

- [ ] Alta cohesión en cada clase
- [ ] Bajo acoplamiento entre clases
- [ ] Responsabilidad única respetada
- [ ] Buen encapsulamiento

**Completitud**:

- [ ] Todos los casos de uso están cubiertos
- [ ] Todos los requisitos funcionales están representados
- [ ] No hay funcionalidad "huérfana" sin clase responsable

### 12. Checklist Final antes de Implementar

Usa esta lista de verificación antes de comenzar la implementación:

**Identificación de Clases**

- [ ] He analizado todos los sustantivos del enunciado
- [ ] He descartado candidatos inapropiados usando criterios sistemáticos
- [ ] Cada clase tiene una responsabilidad clara y única
- [ ] No hay clases redundantes o duplicadas
- [ ] Los nombres son descriptivos, específicos y del dominio

**Relaciones**

- [ ] He identificado todas las relaciones necesarias entre clases
- [ ] La multiplicidad está correctamente especificada en ambos extremos
- [ ] He elegido el tipo de relación apropiado (asociación, agregación, composición, herencia)
- [ ] No hay relaciones innecesarias
- [ ] Las relaciones muchos-a-muchos tienen clase intermedia si es necesario

**Atributos y Métodos**

- [ ] Cada clase tiene los atributos necesarios para cumplir su responsabilidad
- [ ] Los métodos reflejan las responsabilidades de la clase
- [ ] La visibilidad (public, private, protected) está correctamente definida
- [ ] No hay atributos que deberían ser clases
- [ ] Los tipos de datos son apropiados

**Principios de Diseño**

- [ ] Alta cohesión: Los miembros de cada clase están relacionados
- [ ] Bajo acoplamiento: Pocas dependencias entre clases
- [ ] Responsabilidad única: Cada clase hace una cosa
- [ ] Buen encapsulamiento: Datos privados, comportamiento público

**Representación Visual**

- [ ] El diagrama es claro y legible
- [ ] Las líneas no se cruzan excesivamente
- [ ] Hay una organización lógica y espaciado apropiado
- [ ] Uso efectivo de colores o agrupaciones (si aplica)

**Validación**

- [ ] He recorrido casos de uso con el modelo
- [ ] El modelo cubre todos los requisitos funcionales
- [ ] He validado con stakeholders o expertos del dominio
- [ ] He considerado escenarios edge-case

### 13. Conclusiones: Dominando la Identificación de Clases

La identificación de clases es tanto **arte como ciencia**. No existe una única solución correcta, pero sí existen soluciones mejores y peores.

#### 13.1. Puntos Clave para Recordar

**Sobre el Proceso**:

- La identificación de clases es **iterativa**, no lineal
- Empieza simple y refina gradualmente
- No busques la perfección en la primera iteración
- Valida temprano y frecuentemente

**Sobre la Técnica**:

- El análisis de sustantivos es una herramienta, no una receta mágica
- Requiere criterio y experiencia para filtrar candidatos
- Los verbos revelan métodos y relaciones
- El contexto del dominio es crucial

**Sobre el Diseño**:

- Prioriza simplicidad sobre completitud prematura
- Alta cohesión y bajo acoplamiento son tus guías
- Responsabilidad única evita clases "Dios"
- Favorece composición sobre herencia cuando sea dudoso

**Sobre la Práctica**:

- La experiencia mejora tu capacidad de identificar clases
- Estudia modelos existentes de sistemas similares
- Aprende de tus errores y refactoriza cuando sea necesario
- No temas descartar y empezar de nuevo si el modelo no funciona

#### 13.2. El Viaje Continuo

No esperes dominar la identificación de clases inmediatamente. Es una habilidad que se desarrolla con:

- **Práctica deliberada**: Analiza múltiples enunciados
- **Estudio de casos**: Aprende de sistemas reales
- **Revisión por pares**: Otros ven lo que tú no ves
- **Refactorización**: Mejora modelos existentes

#### 13.3. Próximos Pasos

Una vez que domines la identificación de clases, profundiza en:

1. **Patrones de diseño**: Soluciones probadas a problemas recurrentes

    - Creacionales: Factory, Builder, Singleton
    - Estructurales: Adapter, Decorator, Facade
    - Comportamiento: Strategy, Observer, Command

2. **Refactorización**: Mejorar diseños existentes sin cambiar funcionalidad

    - Extract Method, Extract Class
    - Move Method, Move Field
    - Simplify Conditional Expressions

3. **Arquitectura de software**: Organización de alto nivel 

    - Arquitectura en capas
    - Arquitectura hexagonal
    - Microservicios
    - Domain-Driven Design (DDD)

4. **Principios SOLID**: Fundamentos del diseño OO profesional

    - Single Responsibility
    - Open/Closed
    - Liskov Substitution
    - Interface Segregation
    - Dependency Inversion

### 14. Ejercicios Prácticos Guiados

Practica con estos ejercicios progresivos:

#### Ejercicio 1: Sistema de Reserva de Vuelos (Nivel Básico)

**Enunciado**:
> "Los clientes pueden buscar vuelos por origen, destino y fecha. Cada vuelo tiene un número, origen, destino, hora de salida y llegada. Los clientes pueden reservar asientos en clase turista o ejecutiva. Cada reserva debe confirmarse mediante pago con tarjeta de crédito."

**Tareas**:

1. Identifica candidatos a clases (lista completa de sustantivos)
2. Aplica filtros de descarte
3. Define 4-6 clases principales
4. Identifica relaciones y multiplicidad
5. Crea diagrama UML
6. Implementa en Kotlin (opcional)

**Pistas**:

- ¿Es "Cliente" diferente de "Pasajero"?
- ¿"Asiento" debería ser una clase?
- ¿Cómo manejas "clase turista" vs "clase ejecutiva"?

#### Ejercicio 2: Sistema de Clínica Veterinaria (Nivel Intermedio)

**Enunciado**:
> "La clínica atiende mascotas cuyos dueños están registrados en el sistema. Cada mascota tiene un historial médico con visitas, tratamientos y vacunas. Los veterinarios pueden prescribir medicamentos y agendar citas de seguimiento."

**Tareas**:

1. Identifica clases (incluyendo clases no mencionadas explícitamente)
2. Define relaciones complejas (ej: veterinario-mascota-dueño)
3. Identifica relaciones muchos-a-muchos
4. Crea diagrama completo con atributos y métodos
5. Implementa casos de uso: "Agendar cita" y "Registrar visita"

**Desafíos adicionales**:

- ¿Cómo representas el historial médico?
- ¿Una visita es una clase o solo un atributo?
- ¿Cómo relacionas tratamiento con medicamento?

#### Ejercicio 3: Red Social Simple (Nivel Avanzado)

**Enunciado**:
> "Los usuarios pueden crear perfiles, publicar mensajes, seguir a otros usuarios y dar 'me gusta' a publicaciones. Las publicaciones pueden contener texto, imágenes o ambos. Los usuarios reciben notificaciones de nuevas actividades."

**Tareas**:

1. Identifica todas las clases (mínimo 8)
2. Modela relaciones muchos-a-muchos correctamente
3. Identifica patrones (ej: patrón Observer para notificaciones)
4. Crea diagrama UML completo
5. Implementa sistema básico funcional

**Desafíos adicionales**:

- ¿Cómo manejas "seguir" (relación Usuario-Usuario)?
- ¿"Me gusta" es una clase o solo un contador?
- ¿Cómo se generan las notificaciones?
- ¿Publicación es clase abstracta con subclases TextoPublicacion e ImagenPublicacion?

### 15. Recursos y Referencias Ampliados

#### 15.1. Libros Fundamentales

**Para principiantes**:

- **"UML Distilled" - Martin Fowler**: Guía concisa y práctica (150 páginas, muy accesible)
- **"Head First Object-Oriented Analysis & Design"**: Aprendizaje visual con humor

**Para nivel intermedio**:

- **"Applying UML and Patterns" - Craig Larman**: Análisis OO con casos de estudio completos
- **"Object-Oriented Software Engineering" - Ivar Jacobson**: Enfoque basado en casos de uso

**Para nivel avanzado**:

- **"Domain-Driven Design" - Eric Evans**: Modelado del dominio para sistemas complejos
- **"Patterns of Enterprise Application Architecture" - Martin Fowler**: Patrones de diseño empresarial

#### 15.2. Recursos Online

**Tutoriales interactivos**:

- [Visual Paradigm UML Tutorials](https://www.visual-paradigm.com/tutorials/): Tutoriales paso a paso
- [UMLet Tutorial](https://www.umlet.com/): Herramienta simple para aprender

**Videos educativos**:

- [Derek Banas - UML Class Diagrams](https://www.youtube.com/watch?v=3cmzqZzwNDM)
- [freeCodeCamp - Object Oriented Design](https://www.youtube.com/watch?v=fJW65Wo7IHI)

**Ejercicios prácticos**:

- [Refactoring Guru - UML Exercises](https://refactoring.guru/es/design-patterns)
- [Object-Oriented Design Exercises](https://github.com/topics/oop-exercises)

#### 15.3. Herramientas Recomendadas

**Para aprender**:

- **Draw.io**: Gratuito, simple, sin instalación
- **PlantUML**: Texto a diagrama, perfecto para versionado

**Para proyectos profesionales**:

- **Visual Paradigm Community Edition**: Completo y gratuito
- **StarUML**: Buena relación calidad-precio

#### 15.4. Comunidades

- **Stack Overflow**: Tag `uml`, `class-diagram`, `oop-design`
- **Reddit**: r/learnprogramming, r/softwareengineering
- **Discord**: Servidores de Kotlin, Java, Software Architecture

### 16. Reflexión Final: El Arte del Buen Diseño

El buen diseño orientado a objetos no se aprende leyendo - se aprende **haciendo, errando y refactorizando**.

**Recuerda siempre**:

> "Todo el mundo puede crear código que una computadora entienda. Los buenos programadores escriben código que los humanos puedan entender." - Martin Fowler

La identificación de clases es el primer paso para crear ese código comprensible. No busques la perfección - busca la claridad, la simplicidad y la mantenibilidad.

**Última recomendación**: Comienza tu próximo proyecto dibujando el diagrama de clases ANTES de escribir código. Verás la diferencia.

¡Adelante, y feliz modelado! 🚀

---

**Fin del documento**

