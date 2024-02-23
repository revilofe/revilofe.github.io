# Actividad: Sistema de Reservas para Actividades Recreativas

**ID actividad:** U5-006

**Agrupamiento de la actividad**: Individual

---

### Descripción:

Esta actividad implica el diseño y desarrollo de un sistema de reservas en Kotlin para un centro recreativo que ofrece distintas actividades recreativas como natación, senderismo y ciclismo. Cada actividad tiene características únicas y está dirigida a diferentes tipos de clientes (miembros, no miembros, y grupos escolares), con tarifas y restricciones específicas para las reservas.

**Objetivo:**

* Desarrollar habilidades en la aplicación de herencia y sobreescritura de métodos en Kotlin.
* Aprender a diseñar y utilizar clases abstractas para definir comportamientos y estructuras comunes.
* Practicar la implementación y uso de interfaces para garantizar la consistencia en las clases.
* Manejar correctamente los modificadores de visibilidad para asegurar el encapsulamiento adecuado de las propiedades y métodos.
* Aplicar genéricos para manejar distintos tipos de usuarios de manera eficiente y segura en el sistema de reservas.

**Trabajo a realizar:**

1. **Definición de Clases de Actividades:**
   * Crear una clase abstracta `Actividad` con propiedades comunes (`nombre`, `capacidadMaxima`) y un método abstracto `calcularTarifa(cliente: Cliente): Double`.
   * Implementar clases `Natacion`, `Senderismo`, y `Ciclismo` que hereden de `Actividad` y sobreescriban el método `calcularTarifa` para ajustar las tarifas según el tipo de cliente.
2. **Implementación de Interfaz de Reserva:**
   * Definir una interfaz `Reservable` con un método `reservar(cliente: Cliente): Boolean` que indique si la reserva es exitosa.
3. **Gestión de Usuarios:**
   * Crear una `sealed class Cliente` con subclases `Miembro`, `NoMiembro`, y `GrupoEscolar`, añadiendo propiedades específicas como `id`, `nombre`, y `cantidadEstudiantes` para `GrupoEscolar`.
4. **Sistema de Reservas:**
   * Desarrollar una función genérica `realizarReserva` que acepte cualquier actividad que implemente `Reservable` y un `Cliente`, mostrando un mensaje sobre el estado de la reserva.

### Evaluación y calificación

**RA y CE evaluados**:

**Conlleva presentación**: NO

**Rubrica**:

* **Herencia y sobreescritura de métodos**: Evaluación de cómo se extienden las clases y se sobrescriben los métodos para adaptar comportamientos específicos.

  * 0: No implementa herencia.
  * 5: Implementa herencia pero sin sobreescritura efectiva de métodos.
  * 10: Usa herencia y sobreescritura de métodos de forma efectiva y adecuada.
* **Uso de clases abstractas**: Evaluación del uso de clases abstractas para definir una base común entre diferentes actividades.

  * 0: No utiliza clases abstractas.
  * 5: Usa clases abstractas sin explotar todo su potencial.
  * 10: Aplica clases abstractas de manera eficaz para compartir estructura y comportamiento.
* **Implementación de interfaces**: Valoración de cómo las interfaces se usan para definir contratos comunes entre diferentes clases.

  * 0: No implementa interfaces.
  * 5: Implementa interfaces pero no de manera completa.
  * 10: Implementa interfaces de manera completa y efectiva.
* **Modificadores de visibilidad**: Evaluación de cómo se utilizan los modificadores de visibilidad para proteger y exponer datos.

  * 0: Uso incorrecto de modificadores de visibilidad.
  * 5: Uso adecuado de modificadores de visibilidad con algunos errores.
  * 10: Uso correcto y estratégico de modificadores de visibilidad.
* **Uso de genéricos**: Evaluación del uso de genéricos para manejar diferentes tipos de forma segura.

  * 0: No utiliza genéricos.
  * 5: Uso limitado de genéricos.
  * 10: Uso efectivo de genéricos para mejorar la flexibilidad y seguridad del tipo.

### Entrega

* **URL a repositorio GitHub**: El proyecto completo debe ser subido a GitHub, mostrando el uso efectivo de control de versiones y trabajo en equipo.
* **Documento PDF**: Código fuente bien documentado y explicación detallada del diseño del sistema, incluyendo diagramas de clases si es necesario, siguiendo las especificaciones de entrega.

**Cumplimiento de Objetivos:**

* **Herencia y sobreescritura**: Las clases `Natacion`, `Senderismo`, y `Ciclismo` demuestran la herencia de `Actividad` y la sobreescritura del método `calcularTarifa`.
* **Clases abstractas**: `Actividad` actúa como una clase abstracta que define el esqueleto de las actividades recreativas.
* **Interfaces**: `Reservable` garantiza que todas las actividades implementen el método de reserva.
* **Modificadores de visibilidad**: El uso adecuado de `private`, `protected`, y `public` en propiedades y métodos de las clases.
* **Genéricos**: La función `realizarReserva` utiliza genéricos para permitir reservas de cualquier tipo de `Actividad` por cualquier tipo de `Cliente`.

**ubrica**:

* **Herencia y sobreescritura de métodos**: Evaluación de cómo se extienden las clases y se sobrescriben los métodos para adaptar comportamientos específicos.
  * 0: No implementa herencia.
  * 5: Implementa herencia pero sin sobreescritura efectiva de métodos.
  * 10: Usa herencia y sobreescritura de métodos de forma efectiva y adecuada.
* **Uso de clases abstractas**: Evaluación del uso de clases abstractas para definir una base común entre diferentes actividades.
  * 0: No utiliza clases abstractas.
  * 5: Usa clases abstractas sin explotar todo su potencial.
  * 10: Aplica clases abstractas de manera eficaz para compartir estructura y comportamiento.
* **Implementación de interfaces**: Valoración de cómo las interfaces se usan para definir contratos comunes entre diferentes clases.
  * 0: No implementa interfaces.
  * 5: Implementa interfaces pero no de manera completa.
  * 10: Implementa interfaces de manera completa y efectiva.
* **Modificadores de visibilidad**: Evaluación de cómo se utilizan los modificadores de visibilidad para proteger y exponer datos.
  * 0: Uso incorrecto de modificadores de visibilidad.
  * 5: Uso adecuado de modificadores de visibilidad con algunos errores.
  * 10: Uso correcto y estratégico de modificadores de visibilidad.
* **Uso de genéricos**: Evaluación del uso de genéricos para manejar diferentes tipos de forma segura.
  * 0: No utiliza genéricos.
  * 5: Uso limitado de genéricos.
  * 10: Uso efectivo de genéricos para mejorar la flexibilidad y seguridad del tipo.
