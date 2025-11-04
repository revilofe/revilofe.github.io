---
title: "UD 3 - 3.3 Identificación de Clases"
description: Identificación de Clases en UML
summary: Técnicas, métodos y buenas prácticas para identificar clases a partir de requisitos
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

Es importante recordar que los objetos son realmente cosas dentro de un programa de computador. Cuando hablamos sobre "libros" y "copias", por ejemplo, realmente nos referimos a la **representación digital de estas cosas dentro de nuestro sistema**, no a los libros y copias físicas en el mundo real.

Las consecuencias de esto son que hay que tener cuidado con la siguiente pregunta: **¿qué información de la realidad es realmente importante para nuestro sistema?**

Es crucial:

- **No almacenar información** que es definitivamente irrelevante para nuestro sistema (ej: el color del cartel de una tienda)
- **No perder la visión** del hecho de que ¡los objetos son el sistema! Trabajan dentro del programa, no son el mundo real
- **Mantener el enfoque** en lo que el sistema necesita, no en todo lo que existe en el mundo real (ej: un sistema de biblioteca quizás no necesita la información de empleados de mantenimiento)

**La clave**: Modelar el dominio del problema desde la perspectiva del sistema, no modelar la realidad en su totalidad.

### 3. Objetivos de un Buen Modelo de Clases

Cuando diseñas un modelo de clases, en realidad estás persiguiendo **dos objetivos que a menudo están en tensión**:

**Objetivo 1: Construcción Eficiente**

Construir, lo más rápido y barato posible, un sistema que satisfaga nuestros requisitos actuales.

!!! tip "Principio"
    Cada comportamiento que requiera el sistema debe ser proporcionado por los objetos de las clases que elijamos

**Estrategias**:

- **Identificar las clases mínimas necesarias**: La solución más simple que funcione. No sobre-diseñes.
- **Enfocarse en los requisitos actuales**: No anticipar necesidades futuras imaginarias. Solo diseña para lo que sabes que necesitas hoy.
- **Evitar sobre-ingeniería prematura**: No añadas complejidad sin justificación presente. La complejidad es una deuda técnica.

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

### 4. Proceso Iterativo de Identificación

En la práctica, es **improbable que construya correctamente un modelo de clases la primera vez**. La colección de clases en su modelo de diseño es una de las cosas que probablemente cambiará a lo largo de las iteraciones de desarrollo.

#### 4.1. Patrón común de desarrollo

1. **Primera iteración**: Identificar las clases más importantes de los objetos del dominio
   - Aquellas que pertenecen de manera obvia al problema
   - Sustantivos principales del enunciado

2. **Segunda iteración**: Añadir clases que se introducen para resolver el problema
   - Más difíciles de identificar
   - Controladores, gestores, servicios

3. **Iteraciones posteriores**: Refinar y ajustar
   - Eliminar redundancias
   - Mejorar relaciones
   - Ajustar responsabilidades

### 5. Técnica de Identificación de Nombres

La técnica más común y efectiva para identificar clases es el **análisis de sustantivos**. Es una técnica pragmática y fácil de aplicar que funciona bien en la práctica. La idea es simple: los sustantivos en la descripción del problema frecuentemente corresponden a entidades del dominio, que a su vez se convierten en clases.

Sin embargo, no todos los sustantivos se convierten en clases, y ese es el verdadero desafío de esta técnica. Procede en dos etapas fundamentales:

#### 5.1. Etapa 1: Identificar clases candidatas

En esta etapa, eres liberal y no descartas nada. El objetivo es capturar todas las posibilidades, incluso si algunas resultan no siendo clases.

##### 5.1.1. Estrategias principales

1. **Análisis de documentos textuales**
   - Obtener descripción clara del problema (requisitos, casos de uso, historias de usuario, conversaciones con clientes)
   - La documentación puede ser formal (requisitos oficiales) o informal (notas, conversaciones)
   - Las entrevistas con usuarios y stakeholders son especialmente valiosas
   - Leer cuidadosamente toda la documentación disponible

2. **Extracción de sustantivos**
   - Extraer **todos** los sustantivos de la descripción, sin discriminar
   - Los sustantivos son candidatos potenciales a clases de objetos
   - Hacer una lista completa sin descartar nada al principio
   - Incluir tanto sustantivos explícitos como implícitos (aquellos que podrías inferir del contexto)

3. **Identificación de candidatos**
   - Listar todos los sustantivos encontrados
   - Incluir tanto entidades físicas (Cliente, Producto) como conceptuales (Pedido, Transacción)
   - No juzgar en esta etapa; eso viene después

##### 5.1.2. Ejemplo práctico

**Enunciado**: "En un sistema de reservaciones que vende boletos para funciones en varios teatros, los clientes pueden reservar asientos. Cada función está en un teatro específico y tiene una hora de inicio, duración y aforo máximo. Los boletos tienen un precio que varía según la ubicación del asiento. El sistema genera reportes de ocupación."

**Sustantivos encontrados (clases candidatas)**:
- Sistema de Reservaciones ← Metalenguaje, probablemente no sea clase
- Boletos ← ✓ Sí, es una entidad importante
- Función ← ✓ Sí, es una entidad importante
- Teatro ← ✓ Sí, es una entidad importante
- Clientes ← ✓ Sí, es una entidad importante
- Asientos ← ✓ Sí, es una entidad importante
- Hora de inicio ← ← Probablemente sea atributo de Función
- Duración ← Probablemente sea atributo de Función
- Aforo máximo ← Probablemente sea atributo de Teatro o Función
- Precio ← ← Probablemente sea atributo de Boleto
- Ubicación del asiento ← Probablemente sea parte de Asiento
- Reportes ← ¿Clase o resultado de una operación?
- Ocupación ← Probablemente sea atributo calculado

**Resultado de esta etapa**: Una larga lista sin filtrar

##### 5.1.3. Reglas iniciales

- Considérelos en forma **singular**: "Boleto" en lugar de "Boletos"
- **No incluya frases** que contengan "o" como candidatas (son alternativas, no clases)
  - ❌ "Cliente o Administrador" → ✓ "Cliente", ✓ "Administrador"
- Durante esta etapa, **no diferenciar** entre clases y atributos todavía
- No preocuparse si la lista tiene redundancias; las eliminaremos después

#### 5.2. Etapa 2: Descartar candidatas inapropiadas

Esta es la etapa más crítica y donde se requiere más criterio. Hay que analizar **cada candidata** y determinar honestamente si realmente debe ser una clase. Esta es donde los buenos diseñadores se diferencian de los mediocres: en la capacidad de hacer juicios correctos sobre qué mereceSer una clase.

##### 5.2.1. Razones para descartar una clase candidata

**1. Redundante**

Cuando a la misma clase conceptual se le ha dado más de un nombre en la descripción, o cuando es una especialización trivial de otra clase.

**Ejemplo**: 
- "Préstamo de estudiante" y "Préstamo de trabajador" (el tipo de persona es un detalle, no un concepto diferente)
- "Usuario registrado" y "Cliente" (son lo mismo desde diferentes perspectivas)

**Pregunta clave**: ¿Realmente son conceptos diferentes en el dominio, o es la misma cosa con diferentes adjetivos?

**Acción**: Probablemente solo difieren en valores de atributos. Elija un nombre que abarque todas las descripciones.

---

**2. Impreciso**

Cuando no se puede indicar de forma clara y no ambigua lo que significa un nombre. La ambigüedad sugiere que el concepto no está bien definido.

**Ejemplo**: 
- "Cuenta" (¿Cuenta bancaria? ¿Cuenta de usuario? ¿Cuenta de ahorros? ¿Cuenta de email?)
- "Registro" (demasiado genérico; ¿registro de qué?)
- "Datos" (tan vago que es inútil)

**Pregunta clave**: ¿Todos los interesados entienden exactamente lo mismo cuando dicen este nombre?

**Acción**: Eliminar la ambigüedad antes de considerarla clase. Renombrar a algo específico como "CuentaBancaria", "CuentaUsuario", "RegistroAcceso".

---

**3. Un evento u operación**

Cuando el nombre hace referencia a algo que **se hace** para, por o en el sistema; es decir, cuando es un verbo disfrazado de sustantivo.

**Ejemplo**: 
- "Reserva de asiento" (la acción es reservar, no crear una clase separada)
- "Compra de boleto" (el acto de comprar)
- "Validación" (una acción, no una entidad)

**Pregunta clave**: ¿La instancia del evento u operación tiene estado, comportamiento e identidad que persista en el tiempo?

**Conceptos fundamentales**:
- **Estado**: Todos los datos (atributos) que encapsula un objeto en un momento determinado
- **Comportamiento**: La manera como actúa y reacciona un objeto (sus métodos)
- **Identidad**: A los objetos se les hace referencia por un nombre único o identificador

**Regla de decisión**: 
- Si solo representa una acción momentánea sin persistencia → Probablemente sea un **método**, no una clase
  - Ejemplo: "validar email" es un método de la clase Usuario
- Si tiene datos que persisten y un ciclo de vida → Puede ser una clase
  - Ejemplo: "Reserva" con fecha, asiento, cliente, estado → Es una clase porque persiste y tiene lógica

---

**4. Metalenguaje**

Cuando el nombre forma parte de la manera en que se definen o habla sobre las cosas, pero no es parte del dominio del problema.

**Ejemplo**: 
- "Requisitos" (son parte de cómo se especifica el sistema, no parte del dominio)
- "Sistema" (es metalenguaje; todo es parte del sistema)
- "Modelo" (es como referimos al diseño, no es una entidad del dominio)
- "Diagrama" (es una herramienta de modelado, no una clase del sistema)

**Pregunta clave**: ¿Es esto una cosa del mundo real/dominio, o es cómo hablamos sobre el sistema?

**Acción**: Eliminar estos términos de la lista de candidatas.

---

**5. Fuera del alcance del sistema**

Cuando el nombre es relevante para describir cómo funciona el sistema pero no hace referencia a algo **que el sistema gestiona** o con lo que el sistema interactúa directamente.

**Ejemplo**: 
- "Usuario del sistema" (la persona que usa el sistema desde afuera)
- "Administrador del sistema" (rol externo al dominio del problema)
- "Cliente externo" (alguien fuera del sistema)

**Pregunta clave**: ¿El sistema necesita recordar y gestionar información sobre esto? ¿O solo es el "actuar" que usa el sistema?

**Decisión**: 
- Si el sistema **gestiona información** sobre estos → Sí es una clase
  - Ejemplo: En un sistema de tienda, Cliente sí es una clase porque guardamos información sobre clientes
- Si solo **interactúan** con el sistema → No es una clase interna, es un actor externo
  - Ejemplo: El "usuario del sistema" que está usando un cajero automático quizás se represente como una clase, o quizás solo sea una interacción

---

**6. Un atributo**

Cuando está claro que un nombre hace referencia a algo **sencillo sin comportamiento interesante**, que es más bien una propiedad de otra clase.

**Ejemplo**: 
- "Color" (es una propiedad de Producto, no una clase propia)
- "Tamaño" (es una propiedad de Prenda, no una clase)
- "Precio" (es una propiedad de Producto)
- "Nombre" (es una propiedad de Persona)
- "Fecha" (es una propiedad de Evento)

**Pregunta clave**: ¿Este concepto tiene comportamiento propio? ¿O es simplemente un valor que caracteriza a otro objeto?

**Acción**: Estos serán atributos de otras clases, no clases por sí mismos.

**Excepción importante**: Si el atributo tiene comportamiento complejo o múltiples propiedades propias, puede ser una clase:
- Ejemplo: "Dirección" con calle, ciudad, código postal, país, y métodos para validar y formatear
- Ejemplo: "Dinero" con cantidad y moneda, y métodos para conversiones y operaciones
- Estos son "value objects" que merecen ser clases en sí mismos

---

#### 5.3. Identificación de clases relevantes

A partir de las clases candidatas se deben seleccionar las clases relevantes tomando en cuenta:

1. **Relevancia al problema**: Todas las clases deben tener sentido en el área de la aplicación.

2. **Eliminar redundancias**: Se deben eliminar clases redundantes, si expresan la misma información.

3. **Agrupar características**: Se agrupan las características que definen a un sustantivo.

4. **Considerar clases implícitas**: Añadir clases que no se mencionan explícitamente pero son necesarias por conocimiento del dominio.

#### 5.4. Buena práctica: Dos listas

Si se duda si mantener una clase, una buena práctica es mantener **dos listas**:

1. **Lista de candidatos firmes**: Clases de las que se está seguro
   - Tienen responsabilidades claras
   - Aparecen frecuentemente en los requisitos
   - Son conceptos centrales del dominio

2. **Lista de candidatos dudosos**: Clases que tienen que ser definidas todavía
   - Pueden ser útiles pero no está claro
   - Requieren más análisis
   - Podrían convertirse en atributos o métodos

!!! tip "Ventaja"
    Evita perder información mientras se está distinguiendo las cosas seguras de las que están por fijar.

### 6. Fuentes de Clases

Los objetos y su división en clases a menudo derivan de las siguientes fuentes:

#### 6.1. Cosas tangibles o "del mundo real"

**Ejemplos**: Avión, auto, televisor, computador, libro, producto

**Características**:
- Fáciles de identificar
- Corresponden a objetos físicos
- Suelen ser sustantivos concretos

#### 6.2. Roles o Papeles

**Ejemplos**: Gerente, cliente, vendedor, profesor, estudiante, usuario

**Características**:
- Representan personas con un rol específico
- Pueden tener comportamientos asociados al rol
- Importante definir qué hace ese rol en el sistema

#### 6.3. Organizaciones

**Ejemplos**: Universidad, empresa, departamento, equipo

**Características**:
- Agrupan otros objetos
- Tienen estructura jerárquica
- Pueden tener responsabilidades colectivas

#### 6.4. Interacciones

**Ejemplos**: Transacción, matrícula, contrato, pedido, reserva

**Características**:
- Representan relaciones entre otras clases
- Suelen tener fecha/hora
- Almacenan información sobre la interacción

#### 6.5. Eventos o incidencias

**Ejemplos**: Vuelo, accidente, suceso, notificación

**Características**:
- Ocurren en un momento específico
- Pueden tener consecuencias en el sistema
- Menos comunes que las otras categorías

!!! note "Nota importante"
    Las categorías 1 y 2 (tangibles y roles) son fuentes mucho más comunes que las últimas.

### 7. Errores Comunes al Identificar Clases

#### 7.1. Error: La clase "System"

**Descripción**: Crear una clase que representa el sistema en su totalidad, a menudo llamada `[Cualquier_cosa]System`, que implementa todo el comportamiento interesante del sistema.

**Ejemplo**:
```
┌─────────────────────┐
│  BibliotecaSystem   │
├─────────────────────┤
│ - libros            │
│ - usuarios          │
│ - prestamos         │
├─────────────────────┤
│ + prestarLibro()    │
│ + devolverLibro()   │
│ + buscarLibro()     │
│ + registrarUsuario()│
└─────────────────────┘
```

**¿Por qué está mal?**
- Concentra toda la lógica en una sola clase
- Viola el principio de responsabilidad única
- Difícil de mantener y extender
- Tiene presunciones sobre cómo será utilizado el sistema

**Solución correcta**: Distribuir responsabilidades entre múltiples clases:
- `Libro` con sus atributos y métodos propios
- `Usuario` con su información
- `Prestamo` como clase de interacción
- `Biblioteca` como contenedor, si es necesario

#### 7.2. Error: Clases demasiado genéricas

**Ejemplos**: "Objeto", "Item", "Cosa", "Elemento"

**Problema**: No aportan significado al modelo

**Solución**: Usar nombres específicos del dominio

#### 7.3. Error: Clases que son solo datos

**Descripción**: Clases sin comportamiento, solo con getters y setters

**Problema**: Violan el principio de encapsulamiento

**Solución**: Añadir lógica de negocio relevante a cada clase

#### 7.4. Error: Incluir detalles de implementación prematuramente

**Ejemplos**: "ArrayList", "HashMap", "Database"

**Problema**: Mezclar diseño con implementación

**Solución**: Enfocarse en el dominio del problema, no en la tecnología

### 8. Cómo Identificar Relaciones entre Clases

Una vez identificadas las clases, el siguiente paso es determinar cómo se relacionan.

#### 8.1. Preguntas clave para identificar relaciones

**Para Asociación**:
- ¿Una clase necesita conocer o usar otra clase?
- ¿Hay una conexión lógica entre ellas?

**Para Agregación**:
- ¿Una clase "tiene" objetos de otra clase?
- ¿Las partes pueden existir sin el todo?

**Para Composición**:
- ¿Una clase es "parte integral" de otra?
- ¿Las partes desaparecen si el todo desaparece?

**Para Herencia**:
- ¿Una clase "es un tipo de" otra clase?
- ¿Comparte características y comportamiento?

**Para Dependencia**:
- ¿Una clase usa temporalmente otra?
- ¿La usa solo como parámetro o variable local?

#### 8.2. Análisis de verbos para relaciones

Al igual que los sustantivos identifican clases, los **verbos** en los requisitos ayudan a identificar:

1. **Métodos**: Acciones que realiza una clase
   - "El usuario **envía** un mensaje" → método `enviar()` en clase Usuario
   
2. **Relaciones**: Conexiones entre clases
   - "El profesor **imparte** cursos" → relación entre Profesor y Curso

#### 8.3. Ejemplo práctico de identificación de relaciones

**Enunciado**: "Un cliente compra productos de diferentes categorías. Cada producto tiene un precio y un stock. El cliente añade productos a su carrito de compras antes de finalizar la orden."

**Relaciones identificadas**:

1. **Cliente - CarritoCompras**: Composición (1:1)
   - El carrito pertenece al cliente y desaparece con él

2. **CarritoCompras - Producto**: Asociación (1:*)
   - El carrito contiene múltiples productos

3. **Producto - Categoria**: Asociación (1:1 o *:1)
   - Un producto pertenece a una categoría

4. **Cliente - Orden**: Asociación (1:*)
   - Un cliente puede tener múltiples órdenes

### 9. Buenas Prácticas para Crear Diagramas de Clases

#### 9.1. Principios de diseño

**1. Principio de Responsabilidad Única (SRP)**

Cada clase debe tener una única razón para cambiar.

**Ejemplo correcto**:
```
Clase Usuario
- Atributos de usuario
- Métodos de gestión de usuario

Clase AutenticacionService
- Validar credenciales
- Gestionar sesiones
```

**Ejemplo incorrecto**: Una clase `Usuario` que también maneja autenticación, persistencia en base de datos y envío de emails.

**2. Principio Abierto/Cerrado (OCP)**

Las clases deben estar abiertas para extensión pero cerradas para modificación.

**Técnica**: Usar herencia e interfaces para añadir funcionalidad sin modificar código existente.

**3. Principio de Sustitución de Liskov (LSP)**

Las subclases deben ser sustituibles por sus clases base.

**Ejemplo**: Si tienes una clase `Ave`, y creas `Pinguino` que hereda de `Ave`, pero no puede implementar `volar()`, entonces la jerarquía está mal diseñada.

**4. Principio de Segregación de Interfaces (ISP)**

Es mejor tener múltiples interfaces específicas que una interfaz general grande.

**5. Principio de Inversión de Dependencias (DIP)**

Depender de abstracciones, no de implementaciones concretas.

#### 9.2. Cohesión y acoplamiento

**Alta Cohesión**

Las responsabilidades de una clase están fuertemente relacionadas.

**Ejemplo de alta cohesión**:
```
Clase Libro
- titulo
- autor
- isbn
- obtenerTitulo()
- obtenerAutor()
```

**Ejemplo de baja cohesión**:
```
Clase Utilidades
- validarEmail()
- calcularFactorial()
- conectarBaseDatos()
- enviarEmail()
```

**Bajo Acoplamiento** 

Las clases tienen pocas dependencias entre sí.

**Técnicas para reducir acoplamiento**:

- Usar interfaces
- Inyección de dependencias
- Patrones de diseño (Factory, Strategy, Observer)

#### 9.3. Nomenclatura efectiva

**Nombres de clases**:

- Sustantivos en singular
- Descriptivos y específicos
- PascalCase: `CarritoCompras`, `OrdenDeCompra`

**Evitar**:

- Nombres genéricos: `Gestor`, `Manager`, `Handler` (a menos que sean realmente necesarios)
- Abreviaturas confusas
- Nombres muy largos

**Nombres de atributos**:

- Sustantivos descriptivos
- camelCase: `nombreCompleto`, `fechaNacimiento`
- Evitar prefijos innecesarios: `strNombre` incorrecto, `nombre` correcto

**Nombres de métodos**:

- Verbos que describen la acción
- camelCase: `calcularTotal()`, `enviarEmail()`
- Getters/Setters: `getNombre()`, `setNombre()`

#### 9.4. Organización visual del diagrama

**1. Distribución espacial**

- **Herencia**: Clases padre arriba, hijas abajo
- **Composición/Agregación**: Contenedor a la izquierda, contenido a la derecha
- **Asociaciones**: Minimizar cruces de líneas

**2. Agrupación lógica**

- Agrupar clases relacionadas cerca unas de otras
- Usar colores o regiones para separar módulos
- Capas: Presentación, Lógica de Negocio, Datos

**3. Niveles de abstracción**

- **Diagrama de alto nivel**: Solo nombres de clases
- **Diagrama detallado**: Con atributos y métodos principales
- **Diagrama completo**: Todos los detalles

**Ejemplo de progresión**:

**Nivel 1 - Alto nivel**:
```
┌──────────┐     ┌──────────┐
│ Cliente  │────→│ Pedido   │
└──────────┘     └──────────┘
```

**Nivel 2 - Medio**:
```
┌──────────────┐     ┌────────────────┐
│   Cliente    │     │    Pedido      │
├──────────────┤     ├────────────────┤
│ - nombre     │────→│ - fecha        │
│ - email      │     │ - total        │
└──────────────┘     └────────────────┘
```

**Nivel 3 - Detallado**: Con todos los métodos

#### 9.5. División de diagramas grandes

**Estrategias**:

1. **Por módulos funcionales**
   - Diagrama de gestión de usuarios
   - Diagrama de gestión de productos
   - Diagrama de gestión de pedidos

2. **Por capas**
   - Diagrama de capa de presentación
   - Diagrama de capa de lógica de negocio
   - Diagrama de capa de acceso a datos

3. **Por paquetes**
   - Cada paquete tiene su propio diagrama
   - Un diagrama general muestra las relaciones entre paquetes

#### 9.6. Uso efectivo de colores

**Convención sugerida**:

- 🔵 **Azul**: Clases del dominio (entidades principales)
- 🟢 **Verde**: Servicios y controladores
- 🟡 **Amarillo**: Utilidades y helpers
- 🔴 **Rojo**: Excepciones y errores
- 🟣 **Morado**: Interfaces
- 🟠 **Naranja**: Clases abstractas

**Beneficios**:
- Identificación rápida del tipo de clase
- Mejor comprensión visual
- Facilita la navegación en diagramas complejos

### 10. Proceso Completo: Ejemplo Paso a Paso

Veamos un ejemplo completo del proceso de identificación de clases para un **Sistema de Gestión de Biblioteca**.

#### 10.1. Paso 1: Análisis del enunciado

**Enunciado**:

"La biblioteca necesita un sistema para gestionar sus libros y préstamos. Los usuarios pueden registrarse proporcionando su nombre, dirección y teléfono. Cada libro tiene un título, autor, ISBN y una o más copias físicas. Los usuarios registrados pueden solicitar el préstamo de una copia disponible por un período de 14 días. El bibliotecario puede extender el período de préstamo si no hay reservas pendientes. El sistema debe registrar la fecha de préstamo y devolución."

#### 10.2. Paso 2: Extraer sustantivos

**Sustantivos encontrados**:
- Biblioteca
- Sistema
- Libros
- Préstamos
- Usuarios
- Nombre
- Dirección
- Teléfono
- Título
- Autor
- ISBN
- Copias físicas
- Período
- Días
- Bibliotecario
- Reservas
- Fecha de préstamo
- Fecha de devolución

#### 10.3. Paso 3: Analizar cada candidato

| Candidato        | ¿Clase?   | Razón                                    |
|------------------|-----------|------------------------------------------|
| Biblioteca       | ❌ No      | Contenedor general, puede ser opcional   |
| Sistema          | ❌ No      | Metalenguaje                             |
| Libros           | ✅ Sí      | Entidad principal del dominio            |
| Préstamos        | ✅ Sí      | Interacción importante con estado        |
| Usuarios         | ✅ Sí      | Rol principal                            |
| Nombre           | ❌ No      | Atributo de Usuario                      |
| Dirección        | ⚠️ Quizás | Podría ser clase si es compleja          |
| Teléfono         | ❌ No      | Atributo de Usuario                      |
| Título           | ❌ No      | Atributo de Libro                        |
| Autor            | ⚠️ Quizás | Podría ser clase si almacenamos más info |
| ISBN             | ❌ No      | Atributo de Libro                        |
| Copias físicas   | ✅ Sí      | Importante distinguir libro de copia     |
| Período          | ❌ No      | Atributo calculado                       |
| Días             | ❌ No      | Valor numérico                           |
| Bibliotecario    | ✅ Sí      | Rol con permisos especiales              |
| Reservas         | ✅ Sí      | Funcionalidad importante                 |
| Fecha préstamo   | ❌ No      | Atributo de Préstamo                     |
| Fecha devolución | ❌ No      | Atributo de Préstamo                     |

#### 10.4. Paso 4: Clases finales

**Clases firmes**:
1. `Libro` - Información del libro
2. `CopiaLibro` - Ejemplar físico específico
3. `Usuario` - Usuario registrado
4. `Bibliotecario` - Usuario con permisos especiales (¿herencia de Usuario?)
5. `Prestamo` - Registro de préstamo
6. `Reserva` - Registro de reserva

**Clases opcionales para considerar**:
- `Autor` - Si necesitamos más información sobre autores
- `Direccion` - Si la dirección es compleja (calle, ciudad, código postal, país)

#### 10.5. Paso 5: Identificar relaciones

1. `Libro` **1:*** `CopiaLibro` (Composición)
   - Un libro tiene múltiples copias
   
2. `Usuario` **1:*** `Prestamo` (Asociación)
   - Un usuario puede tener múltiples préstamos

3. `CopiaLibro` **1:*** `Prestamo` (Asociación)
   - Una copia puede estar en múltiples préstamos (en diferentes momentos)

4. `Bibliotecario` **es un** `Usuario` (Herencia)
   - Bibliotecario hereda de Usuario con permisos adicionales

5. `Usuario` **1:*** `Reserva` (Asociación)
   - Un usuario puede hacer múltiples reservas

6. `Libro` **1:*** `Reserva` (Asociación)
   - Un libro puede tener múltiples reservas

#### 10.6. Paso 6: Definir atributos y métodos

**Clase Usuario**:
```
+ nombre: String
+ direccion: String
+ telefono: String
+ email: String
+ fechaRegistro: Date
+ prestarLibro(copia: CopiaLibro): Prestamo
+ reservarLibro(libro: Libro): Reserva
```

**Clase Libro**:
```
+ isbn: String
+ titulo: String
+ autor: String
+ editorial: String
+ anioPublicacion: Int
+ obtenerCopiasDisponibles(): List<CopiaLibro>
+ estaDisponible(): Boolean
```

**Clase Prestamo**:
```
+ fechaPrestamo: Date
+ fechaDevolucionPrevista: Date
+ fechaDevolucionReal: Date?
+ usuario: Usuario
+ copia: CopiaLibro
+ extenderPeriodo(dias: Int): Boolean
+ marcarDevuelto(): void
+ estaVencido(): Boolean
```

### 11. Validación del Modelo de Clases

Una vez creado el modelo, es importante validarlo:

#### 11.1. Preguntas de validación

**Para cada clase**:
- ¿Tiene una responsabilidad clara?
- ¿Tiene sentido en el dominio del problema?
- ¿Es necesaria para cumplir los requisitos?
- ¿Puede existir independientemente?

**Para el modelo completo**:
- ¿Cubre todos los requisitos funcionales?
- ¿Es extensible para futuros requisitos?
- ¿Hay clases redundantes?
- ¿Las relaciones tienen sentido?

#### 11.2. Técnicas de validación

**1. Walkthrough de escenarios**

Recorrer casos de uso con el diagrama:
- "Un usuario quiere tomar prestado un libro"
- ¿Qué clases se involucran?
- ¿Tienen los métodos necesarios?

**2. Revisión por pares**

- Presentar el diagrama a otros desarrolladores
- Explicar las decisiones de diseño
- Recibir feedback

**3. Prototipado**

- Implementar las clases principales
- Verificar que el diseño funciona en la práctica
- Ajustar según necesidad

### 12. Checklist Final

Antes de finalizar tu diagrama de clases, verifica:

**Identificación de Clases**

- [ ] He analizado todos los sustantivos del enunciado
- [ ] He descartado candidatos inapropiados
- [ ] Cada clase tiene una responsabilidad clara
- [ ] No hay clases redundantes
- [ ] Los nombres son descriptivos y específicos

**Relaciones**

- [ ] He identificado todas las relaciones necesarias
- [ ] La multiplicidad está correctamente especificada
- [ ] He elegido el tipo de relación apropiado
- [ ] No hay relaciones innecesarias

**Atributos y Métodos**

- [ ] Cada clase tiene los atributos necesarios
- [ ] Los métodos reflejan las responsabilidades
- [ ] La visibilidad está correctamente definida
- [ ] No hay atributos que deberían ser clases

**Principios de Diseño**

- [ ] Alta cohesión en cada clase
- [ ] Bajo acoplamiento entre clases
- [ ] Responsabilidad única por clase
- [ ] Buen encapsulamiento

**Representación Visual**

- [ ] El diagrama es claro y legible
- [ ] Las líneas no se cruzan excesivamente
- [ ] Hay una organización lógica
- [ ] Uso efectivo de colores (si aplica)

### 13. Conclusiones

- La identificación de clases es un **proceso iterativo** y fundamental en el diseño OO
- La **técnica de análisis de sustantivos** es una herramienta poderosa pero requiere criterio
- Es importante distinguir entre **clases, atributos y métodos**
- Un buen modelo busca **alta cohesión** y **bajo acoplamiento**
- Las **buenas prácticas** ayudan a crear sistemas mantenibles y escalables
- La **validación** del modelo es tan importante como su creación
- No existe un modelo "perfecto", pero sí modelos **buenos y malos**
- La experiencia mejora la capacidad de identificar clases correctamente

### 14. Ejercicios Prácticos

Para practicar la identificación de clases, intenta analizar estos enunciados:

#### Ejercicio 1: Sistema de Reserva de Vuelos

"Los clientes pueden buscar vuelos por origen, destino y fecha. Cada vuelo tiene un número, origen, destino, hora de salida y llegada. Los clientes pueden reservar asientos en clase turista o ejecutiva. Cada reserva debe confirmarse mediante pago con tarjeta de crédito."

**Tarea**: Identifica clases, relaciones, atributos y métodos.

#### Ejercicio 2: Sistema de Clínica Veterinaria

"La clínica atiende mascotas cuyos dueños están registrados en el sistema. Cada mascota tiene un historial médico con visitas, tratamientos y vacunas. Los veterinarios pueden prescribir medicamentos y agendar citas de seguimiento."

**Tarea**: Crea un diagrama de clases completo.

#### Ejercicio 3: Red Social Simple

"Los usuarios pueden crear perfiles, publicar mensajes, seguir a otros usuarios y dar 'me gusta' a publicaciones. Las publicaciones pueden contener texto, imágenes o ambos. Los usuarios reciben notificaciones de nuevas actividades."

**Tarea**: Identifica las clases y sus relaciones, prestando especial atención a las relaciones de muchos a muchos.

### 15. Recursos y Referencias

#### Libros recomendados
- **"UML Distilled"** - Martin Fowler (identificación práctica de clases)
- **"Applying UML and Patterns"** - Craig Larman (análisis orientado a objetos)
- **"Object-Oriented Analysis and Design"** - Grady Booch
- **"Domain-Driven Design"** - Eric Evans (modelado del dominio)

#### Sitios web útiles
- [Sitio oficial UML - OMG](https://www.uml.org/)
- [Refactoring Guru - Design Patterns](https://refactoring.guru/)
- [Martin Fowler's Blog](https://martinfowler.com/)

#### Herramientas
- **Draw.io / diagrams.net**: Para crear diagramas
- **PlantUML**: Para diagramas como código
- **Visual Paradigm**: Herramienta profesional
- **Lucidchart**: Herramienta online colaborativa

### 16. Siguiente Paso

Una vez que domines la identificación de clases, el siguiente paso es estudiar:

- **Patrones de diseño**: Soluciones probadas a problemas comunes
- **Refactorización**: Cómo mejorar diseños existentes
- **Arquitectura de software**: Organización de alto nivel del sistema
- **Principios SOLID**: Fundamentos del buen diseño OO
