# U3.3 - Identificación de Clases y Buenas Prácticas

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice I

- 1. Introducción
- 2. Fundamentos de la Identificación
- 3. Objetivos de un Buen Modelo de Clases
- 4. Proceso Iterativo de Identificación
- 5. Técnica de Identificación de Nombres


## Índice II

- 6. Fuentes de Clases
- 7. Errores Comunes al Identificar Clases
- 8. Cómo Identificar Relaciones entre Clases
- 9. Buenas Prácticas para Diagramas Efectivos
- 10. Proceso Completo: Ejemplo Paso a Paso

---

## 1. Introducción


### 1.1. La Importancia de Identificar Clases

* Paso crucial en el diseño orientado a objetos.
* Base para sistemas estructurados y mantenibles.
* Un mal modelo puede generar problemas de mantenimiento.
* Define la arquitectura conceptual del sistema.
* Afecta la escalabilidad y colaboración.

Note: La identificación de clases es el cimiento de cualquier sistema orientado a objetos. Un buen diseño inicial ahorra mucho tiempo y esfuerzo a largo plazo. Es vital entender que cada decisión aquí impacta directamente en la calidad y el futuro del software.

---

## 2. Fundamentos de la Identificación


### 2.1. ¿Qué Buscamos al Identificar Clases?

* **Entidades del dominio**: Objetos relevantes del problema.
* **Responsabilidades claras**: Qué debe hacer cada objeto.
* **Colaboraciones**: Cómo trabajan juntas las clases.
* Representar el mundo real en el sistema digital.
* Enfocarse en la información relevante para el sistema.

Note: Al identificar clases, no buscamos replicar la realidad, sino modelar el dominio del problema desde la perspectiva del sistema. Es fundamental preguntarse si la información es necesaria para los requisitos del sistema.

---

## 3. Objetivos de un Buen Modelo de Clases


### 3.1. Construcción Eficiente

* Construir el sistema de forma rápida y económica.
* Satisfacer los requisitos actuales.
* Identificar las clases mínimas necesarias.
* Enfocarse en los requisitos actuales.
* Evitar la sobre-ingeniería prematura.

Note: El primer objetivo es ser pragmático. No hay que sobre-diseñar ni anticipar necesidades futuras que quizás nunca lleguen. La simplicidad inicial reduce la complejidad y acelera el desarrollo.


### 3.2. Mantenibilidad

* Sistema fácil de mantener y adaptar a futuros requisitos.
* Objetivo a largo plazo.
* **Alta cohesión**: Cada clase con responsabilidad clara.
* **Bajo acoplamiento**: Pocas dependencias entre clases.
* **Encapsulamiento**: Detalles internos ocultos.

Note: La mantenibilidad es clave para la vida útil del software. Un sistema bien diseñado es más fácil de entender, modificar y extender. El equilibrio entre eficiencia y mantenibilidad es el desafío del buen diseño.

---

## 4. Proceso Iterativo de Identificación


### 4.1. ¿Por qué es Iterativo?

* No es un proceso lineal de "una sola pasada".
* Requiere múltiples refinamientos.
* **Aprendizaje progresivo**: Descubrimiento de nuevas clases.
* **Requisitos evolutivos**: Se aclaran y refinan.
* **Validación continua**: Cada iteración corrige el modelo.

Note: Es un error común intentar la perfección en el primer intento. Aceptar que el modelo inicial será imperfecto y que mejorará con cada ciclo de refinamiento es fundamental para un proceso de diseño efectivo.


### 4.2. Fases del Proceso Iterativo I

* **Fase 1: Identificación Inicial (Divergencia)**
    * Objetivo: Generar un conjunto amplio de candidatos.
    * Actividades: Análisis de sustantivos, brainstorming.
    * Resultado: Lista extensa de candidatos (muchos falsos positivos).

Note: En esta primera fase, la cantidad es más importante que la calidad. Se busca recopilar todas las posibles clases sin juzgarlas, para luego filtrarlas.


### 4.2. Fases del Proceso Iterativo II

* **Fase 2: Filtrado y Refinamiento (Convergencia)**
    * Objetivo: Eliminar candidatos inapropiados.
    * Actividades: Aplicar criterios de descarte, agrupar conceptos.
    * Resultado: Lista reducida de clases sólidas.

Note: Aquí se aplica la lógica y los criterios de diseño para depurar la lista inicial, transformando los candidatos en clases viables para el modelo.


### 4.2. Fases del Proceso Iterativo III

* **Fase 3: Identificación de Relaciones**
    * Objetivo: Establecer cómo colaboran las clases.
    * Actividades: Identificar asociaciones, multiplicidad, herencia.
    * Resultado: Diagrama con clases conectadas.

Note: Las relaciones son el pegamento del modelo. Sin ellas, las clases son islas. Esta fase define la interacción y la estructura del sistema.


### 4.2. Fases del Proceso Iterativo IV

* **Fase 4: Enriquecimiento (Añadir Detalles)**
    * Objetivo: Agregar atributos y métodos a las clases.
    * Actividades: Definir propiedades, operaciones, visibilidad.
    * Resultado: Diagrama de clases completo.

Note: Una vez que la estructura y las relaciones están claras, se añaden los detalles internos de cada clase, definiendo su estado y comportamiento.


### 4.2. Fases del Proceso Iterativo V

* **Fase 5: Validación y Revisión**
    * Objetivo: Verificar que el modelo cumple requisitos.
    * Actividades: Recorrer casos de uso, revisar principios de diseño.
    * Resultado: Modelo validado listo para implementación.

Note: La validación es crucial. Un modelo debe ser probado contra los requisitos del sistema para asegurar que es funcional y robusto.

---

## 5. Técnica de Identificación de Nombres


### 5.1. Fundamentos del Método (Análisis de Sustantivos)

* Método más usado para identificar clases candidatas.
* **Sustantivos** → Potenciales clases u objetos.
* **Verbos** → Potenciales métodos o relaciones.
* **Adjetivos** → Potenciales atributos o estados.
* El lenguaje humano refleja la estructura conceptual.


Note: Esta técnica aprovecha cómo las personas describen el mundo. Los sustantivos son los "actores" o "cosas" del sistema, mientras que los verbos son las "acciones" que realizan.


### 5.2. Proceso Paso a Paso I

* **Paso 1: Preparar el texto**
    * Obtener descripción textual de requisitos.
    * Ej: Documento de requisitos, historias de usuario.

* **Paso 2: Identificar todos los sustantivos**
    * Subrayar o marcar cada sustantivo.


Note: La calidad del texto de origen es fundamental. Un texto claro y conciso facilita mucho la identificación inicial.


### 5.2. Proceso Paso a Paso II

* **Paso 3: Crear lista de candidatos**
    * Listar todos los sustantivos únicos.
    * No ser crítico en esta fase.

* **Paso 4: Aplicar filtros de descarte**
    * Eliminar candidatos inapropiados.
    * Usar criterios sistemáticos.


Note: La lista inicial será larga y contendrá muchos elementos que no serán clases. El filtrado es donde se aplica el conocimiento de diseño.


### 5.3. Criterios de Descarte I

* **Criterio 1: Redundancia**
    * Conceptos sinónimos o que representan lo mismo.
    * Ej: "Usuario" y "Bibliotecario" (Bibliotecario es un rol).

* **Criterio 2: Atributos disfrazados**
    * Propiedades simples de otra entidad.
    * Ej: "Nombre", "Dirección" (atributos de Usuario).


Note: Es común confundir roles con clases o atributos con clases. Un rol puede ser un atributo o una subclase, dependiendo de su complejidad.


### 5.3. Criterios de Descarte II

* **Criterio 3: Valores o estados**
    * Estados o valores que son propiedades, no objetos.
    * Ej: "Disponible", "Prestada" (estados de Copia).

* **Criterio 4: Detalles de implementación**
    * Conceptos técnicos no del dominio del problema.
    * Ej: "Sistema" (demasiado genérico).


Note: El modelo de clases debe centrarse en el dominio del problema, no en la implementación técnica. Los estados suelen ser atributos booleanos o enums.


### 5.3. Criterios de Descarte III

* **Criterio 5: Entidades externas fuera de alcance**
    * Conceptos que existen pero no son relevantes para el sistema.
    * Ej: "Biblioteca" (el edificio físico).

* **Criterio 6: Operaciones o servicios**
    * Verbos nominalizados que representan acciones.
    * Ej: "Gestión", "Procesamiento" (suelen ser servicios).


Note: Mantener el enfoque en el alcance del sistema es crucial para evitar clases innecesarias. Las operaciones son métodos, no clases.


### 5.4. Reglas Prácticas para Identificar Clases

* **Regla 1: "El test del sustantivo concreto"**
    * ¿Puedes señalar ejemplos concretos? (Ej: "Ese libro").
* **Regla 2: "El test de las múltiples propiedades"**
    * ¿Tiene más de 2-3 propiedades relevantes? (Ej: Libro).
* **Regla 3: "El test del comportamiento"**
    * ¿Tiene comportamiento significativo? (Ej: Préstamo).
* **Regla 4: "El test de la independencia"**
    * ¿Puede existir independientemente? (Ej: Usuario).


Note: Estas reglas actúan como un filtro rápido para validar si un candidato es una clase o no. Si dudas, empieza como atributo; es más fácil refactorizar.

---

## 6. Fuentes de Clases


### 6.1. Categorías de Objetos I

* **1. Cosas Tangibles o "del Mundo Real"**
    * Objetos físicos que existen.
    * Ej: Autobús, Camilla, Herramienta.
    * Clases si necesitas rastrear propiedades físicas.

* **2. Roles o Papeles**
    * Funciones que las personas desempeñan.
    * Ej: Estudiante, Profesor, Paciente.
    * Pueden ser clases o atributos/enums.


Note: Las clases pueden surgir de diversas fuentes. Las cosas tangibles son las más obvias, mientras que los roles requieren un análisis más profundo para decidir si son clases o atributos.


### 6.1. Categorías de Objetos II

* **3. Organizaciones**
    * Grupos, departamentos, empresas.
    * Ej: Universidad, Facultad, Sucursal.

* **4. Interacciones y Transacciones**
    * Eventos o transacciones entre entidades.
    * Ej: Venta, Compra, Matrícula, Calificación.
    * Representan momentos importantes con datos.

Note: Las organizaciones estructuran el sistema, y las interacciones capturan los eventos clave del negocio.


### 6.1. Categorías de Objetos III

* **5. Eventos o Incidencias**
    * Sucesos que ocurren y necesitan ser registrados.
    * Ej: Vuelo, Retraso, Incidente, Cita.
    * Menos estructurados que las transacciones.

Note: Los eventos son importantes para el registro y la auditoría, capturando lo que sucede en el sistema.


### 6.2. Otras Fuentes para Identificar Clases

* **Diagramas existentes**: E-R, arquitectura, documentación.
* **Interfaces de usuario**: Wireframes, mockups (Ej: Formulario de Cliente → Clase Cliente).
* **Casos de uso**: Actores y entidades involucradas (Ej: "Cliente realiza pedido" → Cliente, Pedido).
* **Glosario del dominio**: Términos técnicos específicos.
* **Expertos del dominio**: Conceptos no documentados, reglas de negocio.

Note: No solo los requisitos textuales son fuente de clases. Cualquier artefacto del proyecto o conocimiento de expertos puede revelar entidades importantes.


### 6.3. Patrones Comunes de Clases

* **Entidad-Detalle**: Factura - ItemFactura.
* **Contenedor-Contenido**: Carrito - Producto.
* **Maestro-Transacción**: Cliente - Venta.
* **Catálogo-Instancia**: TipoProducto - Producto.
* Reconocer patrones acelera la identificación.

Note: Con la experiencia, se identifican patrones recurrentes que simplifican el proceso de diseño y aseguran soluciones probadas.

---

## 7. Errores Comunes al Identificar Clases


### 7.1. Error 1: Sobre-diseño (Demasiadas Clases)

* Crear clases que podrían ser atributos.
* Síntomas: Clases con 1-2 atributos, jerarquías profundas.
* Evitar: Si <3 propiedades Y sin comportamiento → Atributo.

Note: El sobre-diseño añade complejidad innecesaria. Es mejor empezar simple y refactorizar a clase si el concepto gana complejidad.


### 7.2. Error 2: Sub-diseño (Clases Faltantes)

* No identificar clases importantes.
* Síntomas: Métodos muy largos, clases "Dios".
* Solución: Buscar "verbos importantes" que sean clases (Ej: Préstamo).

Note: El sub-diseño lleva a código difícil de mantener. Si un método hace demasiado, probablemente falta una clase que encapsule esa responsabilidad.


### 7.3. Error 3: Confundir Clases con Atributos

* Hacer clases de conceptos que deberían ser atributos simples.
* Atributo: Valor simple sin comportamiento.
* Clase: Múltiples propiedades O comportamiento complejo.

Note: La clave es el comportamiento. Si un concepto solo almacena un valor, es un atributo. Si tiene lógica o múltiples propiedades, puede ser una clase.


### 7.4. Error 4: Modelar Detalles de Implementación

* Incluir clases técnicas en el modelo conceptual.
* Ej: `DatabaseConnection`, `JSONParser`.
* El modelo de dominio debe representar conceptos del negocio.

Note: Separar el dominio del problema de los detalles técnicos es fundamental para un modelo de clases limpio y comprensible.


### 7.5. Error 5: Nombres Genéricos o Vagos

* Clases con nombres como "Gestor", "Manejador", "Datos".
* No comunican responsabilidad clara.
* Usar nombres que reflejen propósito (Ej: `RepositorioUsuarios`).

Note: Un buen nombre es descriptivo y comunica la responsabilidad de la clase. Evitar nombres genéricos mejora la legibilidad y el entendimiento.


### 7.6. Error 6: Ignorar la Multiplicidad

* No especificar cuántas instancias se relacionan.
* Preguntas: ¿Cuántos X puede tener Y? ¿X puede existir sin Y?
* Esencial para entender las restricciones del dominio.

Note: La multiplicidad es crucial para definir las reglas de negocio y cómo se implementarán las relaciones en el código.


### 7.7. Error 7: No Validar con Escenarios Reales

* Crear modelo sin verificar su funcionamiento.
* Recorrer el modelo con ejemplos concretos.
* Si no puedes "recorrer" casos de uso, falta algo.

Note: La validación con escenarios reales es la prueba de fuego del modelo. Asegura que el diseño es funcional y cumple con los requisitos.

---

## 8. Cómo Identificar Relaciones entre Clases


### 8.1. Herencia (Generalización): "Es un"

* **Identificación**: Palabras clave "es un tipo de", clasificaciones.
* **Proceso**: Buscar taxonomías, identificar superclase y subclases.
* **Ejemplo**: Profesor es un tipo de Empleado.

Note: La herencia modela relaciones de especialización/generalización. La flecha apunta a la superclase.


### 8.2. Composición: "Es parte de" (Fuerte)

* **Identificación**: Palabras clave "consiste en", "contiene".
* **Característica**: La parte NO puede existir sin el todo.
* **Regla**: ¿Tiene sentido que la parte exista sin el todo?
* **Ejemplo**: Motor en Coche (si destruyes el coche, el motor no tiene sentido).

Note: La composición es una relación de pertenencia fuerte, donde el ciclo de vida de la parte depende del todo.


### 8.3. Agregación: "Tiene un" (Débil)

* **Identificación**: Palabras clave "tiene", "incluye".
* **Característica**: La parte PUEDE existir independientemente del todo.
* **Ejemplo**: Departamento tiene Empleados (los empleados pueden cambiar de departamento).

Note: La agregación es una relación de pertenencia más débil, donde las partes pueden tener una existencia independiente.


### 8.4. Asociación: Relación General

* **Identificación**: Relación por defecto si no es otra.
* **Palabras clave**: "está relacionado con".
* **Ejemplo**: Cliente hace Pedidos.

Note: La asociación es la relación más flexible y se usa cuando no encaja en los tipos más específicos.


### 8.5. Dependencia: Uso Temporal

* **Identificación**: Una clase usa otra temporalmente.
* **Casos**: Parámetros de método, variables locales.
* **Ejemplo**: Calculador de impuestos usa información de Producto.


Note: La dependencia es la relación más débil, indicando un uso puntual sin mantener una referencia permanente.


### 8.6. Multiplicidad

* Especifica cuántas instancias se asocian.
* **Preguntas**: ¿Cuántos X puede tener Y? ¿Cuántos Y puede tener X?
* **Notación**: `1`, `0..1`, `*` (0..*), `1..*`, `n`, `m..n`.

Note: La multiplicidad es vital para definir las restricciones de negocio y la cardinalidad de las relaciones.


### 8.7. Navegabilidad

* Indica la dirección del conocimiento entre clases.
* **Bidireccional**: Ambas se conocen.
* **Unidireccional**: Solo una conoce a la otra.
* **Recomendación**: Empezar con unidireccional (menor acoplamiento).

Note: La navegabilidad impacta directamente en la implementación y el acoplamiento del sistema.


### 8.8. Relaciones Muchos a Muchos

* Comunes, pero requieren atención especial.
* **Problema**: Necesitan una clase intermedia en implementación.
* **Clase intermedia si**: La relación tiene atributos o comportamiento propio.
* **Ejemplo**: Estudiante * --- * Asignatura → Clase `Matricula`.

Note: Las relaciones muchos a muchos a menudo se resuelven con una clase de asociación que encapsula los detalles de la relación.

---

## 9. Buenas Prácticas para Diagramas Efectivos


### 9.1. Principio de Responsabilidad Única (SRP)

* Una clase debe tener una única razón para cambiar.
* **Beneficios**: Mantenimiento, comprensión, bajo acoplamiento.
* **Señales de violación**: Clase con muchos métodos, nombre con "Y".
* **Solución**: Separar responsabilidades en clases distintas.

Note: El SRP es fundamental para crear clases cohesivas y fáciles de mantener. Si una clase hace demasiado, es una señal de alerta.


### 9.2. Alta Cohesión

* Elementos dentro de una clase fuertemente relacionados.
* Una clase cohesiva hace una cosa y la hace bien.
* **Tipos**: Funcional (mejor), secuencial, comunicacional, temporal, lógica (peor).
* **Ejemplo**: `CalculadoraPrecios` (todos los métodos relacionados con precios).

Note: La alta cohesión asegura que una clase sea un módulo bien definido y enfocado, lo que facilita su comprensión y modificación.


### 9.3. Bajo Acoplamiento

* Clases deben depender lo menos posible de otras.
* Menos dependencias = más flexibilidad.
* **Tipos**: Contenido (peor), común, control, datos, mensaje (mejor).
* **Estrategias**: Usar interfaces, inyección de dependencias.

Note: El bajo acoplamiento reduce el efecto dominó de los cambios y mejora la reusabilidad y la capacidad de prueba del código.


### 9.4. Ley de Demeter (Mínimo Conocimiento)

* Un objeto solo debe llamar métodos de:
    * Sí mismo.
    * Sus parámetros.
    * Objetos que crea.
    * Sus componentes directos.
* Evitar encadenamiento excesivo de llamadas.

Note: La Ley de Demeter promueve un bajo acoplamiento al limitar el conocimiento que una clase tiene sobre la estructura interna de otras.


### 9.5. Encapsulamiento Efectivo

* **Principios**: Ocultar datos, ocultar implementación, exponer comportamiento.
* **Ejemplo**: `CuentaBancaria` con saldo privado y métodos controlados.
* **Beneficios**: Integridad de datos, validaciones, historial inmutable.

Note: El encapsulamiento protege los datos internos de una clase y asegura que las interacciones se realicen a través de una interfaz controlada.


### 9.6. Favorecer Composición sobre Herencia

* Usar composición ("tener un") en vez de herencia ("ser un") cuando sea posible.
* **Beneficios**: Flexibilidad, menor acoplamiento, evita jerarquías frágiles.
* **Herencia si**: Relación "es-un" genuina, polimorfismo esencial.
* **Composición si**: Relación "tiene-un", reutilizar código sin "es-un".

Note: La composición ofrece mayor flexibilidad y menor acoplamiento que la herencia, siendo preferible en muchos escenarios de diseño.

---

## 10. Proceso Completo: Ejemplo Paso a Paso


### 10.1. Enunciado del Problema: Sistema de Gestión de Gimnasio

* Gestionar clientes (nombre, teléfono, fecha nacimiento).
* Membresías (mensual, trimestral, anual; precio, inicio, vencimiento).
* Clases grupales (yoga, spinning; instructor, horario, capacidad, sala).
* Clientes reservan plazas en clases.
* Instructores (empleados, especialidad, disponibilidad).
* Salas (capacidades diferentes).
* Registrar asistencia para estadísticas.

Note: Este es el punto de partida. Un enunciado de requisitos que debemos transformar en un modelo de clases.


### 10.2. Paso 1: Análisis de Sustantivos

* **Gimnasio, Clientes, Membresías, Clases grupales, Instructor, Sala, Reserva, Asistencia.**
* Otros sustantivos serán atributos o descartados.

Note: La primera pasada es identificar todos los sustantivos posibles, sin filtrar aún.


### 10.3. Paso 2: Filtrado de Candidatos

* **Descartar genéricos**: Sistema, Operaciones, Estadísticas.
* **Descartar atributos**: Nombre, Teléfono, Precio, Horario, etc.
* **Descartar redundancia**: Empleados (Instructor es un empleado).
* **Clases candidatas finales**: Cliente, Membresía, Clase, Instructor, Sala, Reserva, Asistencia, Gimnasio.

Note: Aplicar los criterios de descarte para refinar la lista inicial y quedarse con las entidades clave del dominio.


### 10.4. Paso 3: Definir Responsabilidades

* **Cliente**: Representar miembro (id, nombre, teléfono, fechaNacimiento).
* **Membresía**: Gestionar contrato (id, tipo, precio, fechas).
* **Clase**: Actividad programada (id, nombre, instructor, sala, horario).
* **Instructor**: Persona que imparte (id, nombre, especialidad).
* **Sala**: Espacio físico (id, nombre, capacidad).
* **Reserva**: Asociar cliente con clase (id, cliente, clase, fecha).
* **Asistencia**: Registrar asistencia (id, reserva, fecha, asistio).
* **Gimnasio**: Clase principal del sistema.

Note: Para cada clase candidata, se definen sus atributos y los métodos que encapsulan su comportamiento.


### 10.5. Paso 4: Identificar Relaciones I

* **Cliente - Membresía**: Composición (1 Cliente tiene 0..1 Membresía activa).
* **Cliente - Reserva**: Agregación (1 Cliente tiene * Reservas).
* **Clase - Reserva**: Agregación (1 Clase tiene * Reservas).

Note: Se establecen las conexiones entre las clases, definiendo el tipo de relación y su multiplicidad.


### 10.5. Paso 4: Identificar Relaciones II

* **Clase - Instructor**: Asociación (* Clases tienen 1 Instructor).
* **Clase - Sala**: Asociación (* Clases se imparten en 1 Sala).
* **Reserva - Asistencia**: Composición (1 Reserva tiene 0..1 Asistencia).

Note: Continuamos identificando las relaciones restantes, asegurando que todas las clases estén conectadas lógicamente.

---

## ¡Gracias por vuestra atención!

### Preguntas

¿Alguna pregunta sobre la identificación de clases?

Note: Abrimos espacio para preguntas. Preguntad cualquier duda sobre conceptos vistos: técnicas de identificación, criterios de descarte, tipos de relaciones, buenas prácticas, etc.
