---
title: "UD 3 - 3.3 Identificación de Clases"
description: Identificación de Clases en UML
summary: Técnicas y métodos para identificar clases a partir de requisitos
authors:
    - Eduardo Fdez
date: 2025-11-03
icon:   
permalink: /edes/unidad3/3.3
categories:
    - EDES
tags:
    - EDES
    - UML
    - Identificación de Clases
    - Análisis
    
---

## 3.3 Identificación de Clases

### 1. Introducción

Los **diagramas de clases de UML** se utilizan para documentar la estructura estática del sistema; esto es, qué clases hay y cómo están relacionadas. La técnica del diagrama de clase se ha vuelto fundamental en los métodos orientados a objetos.

El diagrama de clase describe:
- Los tipos de objetos que hay en el sistema
- Las diversas clases de relaciones estáticas que existen entre ellos
- Los atributos y operaciones (métodos) de una clase
- Las restricciones según la forma en que se conecten los objetos

### 2. Clases y Objetos

#### 2.1. ¿Qué es un objeto?

Un **objeto** es:

- La pieza básica de la POO (Programación Orientada a Objetos)
- Representa un objeto del mundo real, por ejemplo: un automóvil, un estudiante, una cuenta bancaria
- Cada objeto es especializado y solo se encarga de su tarea
- Pueden ser entidades físicas y conceptuales, por ejemplo: un libro, una cuenta bancaria
- Se comunican con otros objetos pasándose mensajes, por ejemplo: "retirar dinero", "consultar saldo"

#### 2.2. ¿Qué son las clases?

Una **clase** describe un conjunto de objetos con un rol o roles equivalentes en un sistema. Los objetos y su división en clases a menudo derivan de una de las siguientes fuentes:

1. **Cosas tangibles o "del mundo real"**: Avión, auto, televisor, computador, etc.
2. **Roles o Papeles**: Gerente, cliente, vendedor, profesor, etc.
3. **Organizaciones**: Universidad, empresa, departamento, etc.
4. **Interacciones**: Transacción, matrícula, contrato, etc.
5. **Eventos o incidencias**: Vuelo, accidente, suceso, etc.

> **Nota importante**: Estas categorías se solapan, y las dos primeras son fuentes de objetos y de clases mucho más comunes que las dos últimas.

#### 2.3. Consideraciones importantes

Es importante recordar que los objetos son realmente cosas dentro de un programa de computador. Cuando hablamos sobre "libros" y "copias", por ejemplo, realmente nos referimos a la representación de estas cosas dentro de nuestro sistema.

Las consecuencias de esto son que hay que tener cuidado:

- **No almacenar información** que es definitivamente irrelevante para nuestro sistema
- **No perder la visión** del hecho de que ¡los objetos son el sistema!

Por otra parte, existen algunos errores comunes al identificar clases y objetos: la clase "System". Consiste en crear una clase que representa el sistema en su totalidad, es decir inventarse una clase, a menudo llamada `[Cualquier_cosa]System`, que implementa todo el comportamiento interesante del sistema. 

**¿Por qué está mal?** Porque tales diseños son muy difíciles de mantener: tienden a tener presunciones sobre cómo será utilizado el sistema. En Orientación a Objetos, todo el negocio es el sistema; ¡este es el tema!

### 3. Identificación de Objetos y Clases

#### 3.1. Objetivos

La construcción de un modelo de clases incluye la identificación de las clases que deberían existir en nuestro sistema. Hay dos objetivos fundamentales:

* **Objetivo 1:** Construcción eficiente

    Construir, lo más rápido y barato posible, un sistema que satisfaga nuestros requisitos actuales.

    > **Principio**: "Cada comportamiento que requiera el sistema debe ser proporcionado por los objetos de las clases que elijamos"

* **Objetivo 2:** Mantenibilidad

    Construir un sistema que sea fácil de mantener y adaptar a futuros requisitos.

    > **Principio**: "Un buen modelo de clases está formado por módulos encapsulados, con acoplamiento débil (pocas dependencias entre módulos) y cohesión fuerte"

#### 3.2. Proceso iterativo

En la práctica, es improbable que construya correctamente un modelo de clases la primera vez. La colección de clases en su modelo de diseño es una de las cosas que probablemente cambiará a lo largo de las iteraciones de desarrollo.

**Patrón común**:

1. Primero identificará las clases más importantes de los objetos del dominio (aquellas que pertenecen de manera obvia al problema)
2. Luego las clases que se introducen para resolver el problema (más difíciles de identificar)

### 4. Técnica: Identificación de Nombres

#### 4.1. Identificación de clases candidatas

Esta técnica procede en dos etapas fundamentales:

##### 4.1.1. Etapa 1: Identificar clases candidatas

**Estrategias principales**:

1. **Análisis de documentos textuales**: Se obtiene principalmente de algún documento textual que describa el sistema
2. **Extracción de sustantivos**: Se extraen todos los sustantivos de la descripción del problema o de algún otro documento similar
3. **Identificación de candidatos**: Los sustantivos en la descripción del problema son los posibles candidatos a clases de objetos

**Ejemplo**: En un sistema de reservaciones que vende boletos para funciones en varios teatros, las clases candidatas serían:
- Sistema de Reservaciones
- Boletos
- Función
- Teatro

**Reglas**:
- Considérelos en forma singular
- No incluya frases que contengan "o" como candidatas

##### 4.1.2. Etapa 2: Descartar candidatas inapropiadas

Durante esta etapa, se debe identificar entidades físicas al igual que entidades conceptuales. **No se debe tratar de diferenciar entre clases y características de las clases durante esta etapa.**

Descarte las candidatas que son inapropiadas por cualquier razón, renombrando las clases restantes si es necesario.

##### 4.1.3. Razones para descartar una clase candidata:

Las siguientes son algunas razones comunes para descartar una clase candidata:

1. **Redundante:** Cuando a la misma clase se le ha dado más de un nombre.

    **Ejemplo**: "préstamo" y "préstamo a corto plazo" 
   
    **Acción**: Probablemente solo difieren en valores de atributos. Elija un nombre que abarque todas las descripciones.

2. **Impreciso:** Cuando no se puede indicar de forma no ambigua lo que significa un nombre.

    **Ejemplo**: "Cuenta" (¿Cuenta bancaria, cuenta de usuario, cuenta de ahorros?)

    **Acción**: Eliminar la ambigüedad antes de considerarla clase.

3. **Un evento u operación:** Cuando el nombre hace referencia a algo que se hace para, por o en el sistema.

    **Ejemplo**: "Reserva de asiento", "Compra de boleto"

    **Pregunta clave**: ¿La instancia del evento u operación tiene estado, comportamiento e identidad?

    **Conceptos fundamentales**:
        - **Estado**: Todos los datos (atributos) que encapsula un objeto en un momento determinado
        - **Comportamiento**: La manera como actúa y reacciona un objeto, en función de sus cambios de estado y el paso de mensajes
        - **Identidad**: A los objetos se les hace referencia por un nombre (el valor de una variable en un programa cliente)

4. **Metalenguaje:** Cuando el nombre forma parte de la manera en que se definen las cosas.

    **Ejemplo**: Los nombres "requisitos" y "sistema" se utilizan como parte del lenguaje de modelado, en vez de representar objetos en el dominio del problema.

5. **Fuera del alcance del sistema:** Cuando el nombre es relevante para describir cómo funciona el sistema pero no hace referencia a algo interno del sistema.

    **Ejemplo**: "Usuario del sistema", "Administrador del sistema"

6. **Un atributo:** Cuando está claro que un nombre hace referencia a algo sencillo, sin un comportamiento interesante, que es un atributo de otra clase.

    **Ejemplo**: "Color", "Tamaño", "Precio"


#### 4.2. Identificación de clases relevantes

A partir de las clases candidatas se deben seleccionar las clases relevantes tomando en cuenta las siguientes consideraciones:

1. **Relevancia al problema**: Todas las clases deben tener sentido en el área de la aplicación. La relevancia al problema debe ser el único criterio para la selección.

2. **Eliminar redundancias**: Se deben eliminar clases redundantes, si estas expresan la misma información. La clase más descriptiva debe ser guardada.

3. **Agrupar características**: Se agrupan las características que definen a un sustantivo.

4. **Considerar clases implícitas**: Dado que no todas las clases se describen de manera explícita, siendo algunas implícitas en la aplicación, será necesario añadir clases que pueden ser identificadas por nuestro conocimiento del área.

#### 4.3. Buena práctica: Dos listas

Si se duda si mantener una clase, una buena práctica es mantener dos listas:

1. **Lista de candidatos firmes**: Clases de las que se está seguro
2. **Lista de candidatos dudosos**: Clases que tienen que ser definidas todavía

Esto evita perder información mientras se está distinguiendo las cosas seguras de las que están por fijar.

### 5. Representación Gráfica en UML

#### 5.1. Notación de clase

Una clase se representa con una figura rectangular dividida en tres partes:

```
┌─────────────────────────┐
│     Nombre de Clase     │  ← Parte superior
├─────────────────────────┤
│     Atributos           │  ← Parte media
├─────────────────────────┤
│     Métodos             │  ← Parte inferior
└─────────────────────────┘
```

1. **Parte superior:** Nombre de la clase

    Ejemplo: `Libro`

2. **Parte media:** Atributos, señalando alcance, nombre y tipo.

    Ejemplo: `+ autor : String`

3. **Parte inferior:** Métodos, señalando lista de argumentos y tipo de retorno.

    Ejemplo: `+ setAutor(autor: String) : Unit`

#### 5.2. Ejemplo completo: Clase Libro

**Diagrama UML:**

![Ejemplo de clase Libro](assets/ejemplo-clase-libro.svg)

**Representación textual:**

```
┌────────────────────────────────────────┐
│                 Libro                  │
├────────────────────────────────────────┤
│ - autor : String                       │
│ - titulo : String                      │
│ - cantidadLibros : Int                 │
├────────────────────────────────────────┤
│ + Libro()                              │
│ + Libro(autor: String, titulo: String) │
│ + setAutor(autor: String) : Unit       │
│ + getAutor() : String                  │
│ + setTitulo(titulo: String) : Unit     │
│ + getTitulo() : String                 │
│ + getNumeroEjemplares() : Int          │
│ + toString() : String                  │
└────────────────────────────────────────┘
```

**Implementación en Kotlin:**

```kotlin
class Libro {
    private var autor: String
    private var titulo: String
    
    companion object {
        private var cantidadLibros: Int = 0
        
        fun getCantidadLibros(): Int = cantidadLibros
    }
    
    constructor() : this("NA", "NT")
    
    constructor(autor: String, titulo: String) {
        this.autor = autor
        this.titulo = titulo
        cantidadLibros++
    }
    
    fun setAutor(autor: String) {
        this.autor = autor
    }
    
    fun getAutor(): String = autor
    
    fun setTitulo(titulo: String) {
        this.titulo = titulo
    }
    
    fun getTitulo(): String = titulo
    
    override fun toString(): String {
        return "Datos de libro: $titulo\n$autor"
    }
}
```

### 6. Atributos y Métodos

El sistema que se construye consistirá en una colección de objetos que interactúan para completar los requisitos del sistema. Es necesario identificar los atributos y los métodos que cada clase debería tener.

#### 6.1. Tipos de Atributos

##### 6.1.1. Atributos de clase
Son aquellos que representan valores comunes a todas las instancias de una clase. Pueden tener un valor inicial.

**Ejemplos en Kotlin:**
```kotlin
companion object {
    private var promedioEdades: Double = 0.0
    private var numeroAlumnos: Int = 0
}
```

##### 6.1.2. Atributos de instancia
Son aquellos que representan valores propios de un solo objeto que lo diferencia de otros elementos de su misma clase. Pueden tener un valor por defecto.

**Ejemplos en Kotlin:**
```kotlin
private var nombre: String = ""
private var numeroPuertas: Int = 4
```

##### 6.1.3. Constantes
Representan valores inmutables en tiempo y espacio. En Kotlin se definen con `const val` o `val`.

**Ejemplos en Kotlin:**
```kotlin
const val MAX: Int = 20

companion object {
    const val PI: Double = 3.1415
}
```

> **Convención**: El nombre de las constantes debe escribirse totalmente en mayúsculas.

#### 6.2. Tipos de Métodos

##### 6.2.1. Métodos de clase
Son acciones que no requieren de un objeto específico para su realización. Los métodos de clase solo tienen acceso a los atributos de clase.

**Ejemplo en Kotlin:**
```kotlin
companion object {
    fun sumar(x: Int, y: Int): Int {
        return x + y
    }
}
```

##### 6.2.2. Métodos de instancia
Son acciones que requieren de un objeto específico. Los métodos de instancia tienen acceso a todos los miembros de la clase, tanto atributos de clase como atributos de instancia.

**Ejemplo en Kotlin:**
```kotlin
fun getNombre(): String {
    return nombre
}
```

### 7. Diagrama de Clases

El **Diagrama de Clases** es el diagrama principal de análisis y diseño de un sistema. En él se especifica la estructura de clases del sistema, con relaciones entre clases y estructuras de herencia.

#### 7.1. Objetivo según la fase

Los diagramas de clases pueden ser desarrollados en diferentes fases del ciclo de vida del software:

- **Durante el análisis del sistema**: El diagrama se desarrolla buscando una solución ideal
- **Durante el diseño**: Se usa el mismo diagrama y se modifica para satisfacer los detalles de las implementaciones

#### 7.2. Conceptos: Rol y Multiplicidad

Unos de los aspectos más importantes de una relación entre clases son el **rol** y la **multiplicidad**. Estos conceptos se representan en los extremos de la línea que une las clases relacionadas, y se describen a continuación:

* **Rol:** Indica el papel que juega una clase en la relación. Es decir, describe la semántica que tiene la relación en el sentido indicado.
* **Multiplicidad:** Indica cuántas instancias de una clase pueden estar asociadas con una instancia de otra clase en la relación. Es decir, define la cardinalidad de la relación.

| Notación | Significado                 |
|----------|-----------------------------|
| `1`      | Uno y solo uno              |
| `0..1`   | Cero o uno                  |
| `M..N`   | Desde M hasta N             |
| `*`      | Muchos                      |
| `n`      | Exactamente n               |
| `0..*`   | Cero o muchos               |
| `1..*`   | Uno o muchos (al menos uno) |

**Ejemplo de notación:**

```
┌─────────┐   Se imparte   ┌─────────┐
│  Curso  │1 ───────────→ *│  Clase  │
└─────────┘+curso   +clases└─────────┘

```

En el ejemplo anterior:

* El rol de la clase `Curso` es `curso`, y el rol de la clase `Clase` es `clases`. 
* La multiplicidad indica que un `curso` puede impartir muchas `clases`, pero cada `clase` pertenece a un solo `curso`.

### 8. Relaciones entre Clases

Una **relación** en un diagrama de clases se representa mediante una línea que une dos o más clases. Las relaciones más comunes pueden ser:

![Relaciones](assets/relaciones.png)

- Asociación (binaria, reflexiva, n-aria)
- Agregación
- Composición
- Generalización/Especialización
- Dependencia


#### 8.1. Asociación Binaria

Una asociación binaria conecta dos clases. Se representa con una línea sólida entre las dos clases.


**Diagrama:**

```
┌────────────┐  Consta De   ┌─────────┐
│ Matricula  │1 ─────────→ *│  Curso  │
└────────────┘              └─────────┘
  -matricula                  -cursos
```

**Implementación en Kotlin:**

```kotlin
class Matricula(n: Int) {
    private val cursos: Array<Curso?> = arrayOfNulls(n)
    
    // ... resto de métodos
}

class Curso(private val matricula: Matricula) {
    
    // ... resto de métodos
}
```

#### 8.2. Asociación Reflexiva

Una clase se relaciona consigo misma.

**Diagrama:**

```
┌──────────────┐
│  Trabajador  │
└──────────────┘
  ↑           ↓
  │           │ Supervisor De
  │           │
-jefe 0..1  0..* -subordinado
```

**Implementación en Kotlin:**

```kotlin
class Trabajador(
    private val jefe: Trabajador?,
    n: Int
) {
    private val subordinados: Array<Trabajador?> = arrayOfNulls(n)
    
    // ... resto de métodos
}
```

#### 8.3. Asociación N-aria

Involucra más de dos clases.

**Diagrama:**

```
┌──────────┐  Contenido En    ┌──────────────┐
│ Articulo │1 ─────────────→ *│ OrdenCompra  │
└──────────┘                  └──────────────┘
  -articulo                     -ordenC
                                   │
                                ┌──┴────┐
                                │ItemOC │
                                └───────┘
```

**Implementación en Kotlin:**

```kotlin
class Articulo {
    // ... atributos y métodos
}

class OrdenCompra {
    private val items: Array<ItemOC?> = arrayOfNulls(100)
    
    inner class ItemOC(private val articulo: Articulo) {
        // ... métodos de ItemOC
    }
}
```

#### 8.4. Asociación de Agregación

Representa una relación de "tiene un" donde las partes pueden existir independientemente del todo. Se representa con un **rombo vacío**.

**Diagrama:**

```
┌───────────┐  Es Accesorio De    ┌────────┐
│ Automovil │◇──────────────────→ │ Radio  │
└───────────┘                     └────────┘
  -automovil 1     0..1 -radio
```

**Implementación en Kotlin:**

```kotlin
class Automovil(private val radio: Radio?) {
    // ... resto de métodos
}

class Radio {
    // ... atributos y métodos
}
```

> **Nota**: En la agregación, la radio puede existir independientemente del automóvil.

#### 8.5. Asociación de Composición

Representa una relación de "es parte de" donde las partes NO pueden existir sin el todo. Se representa con un **rombo relleno**.

**Diagrama:**

```
┌───────────┐  Es Parte De   ┌────────┐
│ Automovil │♦──────────────→│ Motor  │
└───────────┘                └────────┘
  -automovil 1    0 -motor
```

**Implementación en Kotlin:**

```kotlin
class Automovil {
    private val motor: Motor = Motor()
    
    // Motor como clase interna (inner class)
    inner class Motor {
        // ... métodos de Motor
    }
    
    // ... resto de métodos
}
```

> **Nota**: En la composición, el motor es parte integral del automóvil y no puede existir sin él.

#### 8.6. Asociación de Generalización/Especialización (Herencia)

Representa una relación de "es un tipo de". Se representa con una **flecha con triángulo vacío** apuntando a la superclase.

**Diagrama:**

```
         ┌──────────────┐
         │ Publicacion  │
         └──────────────┘
                △
                │ Generalización
                │
         ┌──────┴──────┐
         │    Libro    │
         └─────────────┘
       Especialización
```

**Implementación en Kotlin:**

```kotlin
open class Publicacion {
    // ... atributos y métodos base
}

class Libro : Publicacion() {
    // ... atributos y métodos específicos
    
    init {
        // Llama al constructor de la superclase
    }
}
```

> **Principio**: La subclase hereda todos los atributos y métodos de la superclase.

#### 8.7. Asociación de Dependencia

Indica que una clase usa o depende de otra clase. Se representa con una **flecha discontinua**.

**Diagrama:**

```
┌───────────┐       ┌────────────────────────────┐
│ Potencia  │- - - →│         Math               │
└───────────┘       ├────────────────────────────┤
                    │ pow(a:Double, b:Double)    │
                    └────────────────────────────┘
```

**Implementación en Kotlin:**

```kotlin
import kotlin.math.pow

class Potencia {
    companion object {
        @JvmStatic
        fun main(args: Array<String>) {
            val x = 5.0
            val y = 2.0
            val z = x.pow(y)
            println("El cuadrado de 5 es: $z")
        }
    }
}
```

> **Nota**: La dependencia es más débil que otras relaciones. La clase `Potencia` simplemente usa la funcionalidad de `Math`, pero no mantiene una referencia permanente.

#### 8.8. Comparación de Tipos de Relaciones

| Tipo de Relación | Símbolo     | Fuerza     | Descripción                           |
|------------------|-------------|------------|---------------------------------------|
| **Dependencia**  | `- - - →`   | Muy débil  | Una clase usa temporalmente otra      |
| **Asociación**   | `───→`      | Débil      | Relación estructural entre clases     |
| **Agregación**   | `◇───→`     | Media      | "Tiene un" - partes independientes    |
| **Composición**  | `♦───→`     | Fuerte     | "Es parte de" - partes dependientes   |
| **Herencia**     | `───▷`      | Muy fuerte | "Es un tipo de" - relación padre-hijo |

### 9. Conclusiones

- La identificación de clases es un **proceso iterativo** y fundamental en el diseño orientado a objetos
- Es importante distinguir entre objetos del dominio y objetos de implementación
- La **técnica de identificación de nombres** es una herramienta útil, pero requiere refinamiento
- Los diagramas de clases UML son esenciales para documentar la estructura del sistema
- Las relaciones entre clases deben elegirse cuidadosamente según el tipo de dependencia
- Un buen diseño busca **alta cohesión** y **bajo acoplamiento**

### 10. Recursos y Referencias

#### Documentación oficial
- [Sitio oficial de UML - OMG](https://www.uml.org/)
- [Diagramas UML](https://diagramasuml.com/)

#### Lenguajes de programación
- [Kotlin Programming Language](https://kotlinlang.org/)
- [Java Platform Documentation](https://docs.oracle.com/en/java/)

#### Libros recomendados
- **UML Distilled** - Martin Fowler
- **Applying UML and Patterns** - Craig Larman
- **Clean Code** - Robert C. Martin
