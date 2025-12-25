---
title: "UD 4 - 4.1 Diagramas de Casos de Uso"
description: Diagramas de casos de uso en UML
summary: Diagramas de casos de uso en UML para representar requisitos funcionales del sistema
authors:
    - Eduardo Fdez
date: 2024-02-02
icon: material/file-document-outline
permalink: /edes/unidad4/4.1
categories:
    - EDES
tags:
    - UML
    - Diagramas
    - Casos de Uso
    - Requisitos

# Relacionado con la tabla de contenidos
toc: true
toc_label: "Contenido"
toc_icon: "file-code"
---

## 4.1. Diagramas de Casos de Uso

### 1. Introducción

El **diagrama de casos de uso** es uno de los diagramas incluidos en UML 2.5, estando este clasificado dentro del grupo de diagramas de comportamiento. Es, con total seguridad, el diagrama más conocido y es utilizado para representar los actores externos que interactúan con el sistema de información y a través de qué funcionalidades (casos de uso o requisitos funcionales) se relacionan. Dicho de otra manera, muestra de manera visual las distintas funciones que puede realizar un usuario (más bien un tipo de usuario) de un Sistema de Información.

En este documento se incluye información sobre cómo construir este diagrama.

Lo primero es saber cuál es su finalidad. El diagrama de casos de uso, dependiendo de la profundidad que le demos, puede ser utilizado para muchos fines, entre ellos podemos encontrar los siguientes:

- **Representar los requisitos funcionales.**

- **Representar los actores que se comunican con el sistema.** Normalmente los actores del sistema son los usuarios y otros sistemas externos que se relacionan con el sistema. En el caso de los usuarios hay que entender el actor como un "perfil", pudiendo existir varios usuarios que actúan como el mismo actor.

- **Representar las relaciones entre requisitos funcionales y actores.**

- **Guiar el desarrollo del sistema.** Crear un punto de partida sobre el que empezar a desarrollar el sistema.

- **Comunicarse de forma precisa entre cliente y desarrollador.** Simplifica la forma en que todos los partícipes del desarrollo, incluyendo el cliente, perciben cómo el sistema funcionará y ofrecerá una visión general común del mismo.

### 2. Elementos de un diagrama de casos de uso

Un diagrama de casos de uso está compuesto, principalmente, de 3 elementos: **Actores**, **Casos de uso** y **Relaciones**.

#### 2.1. Actor

Como ya hemos comentado en la presentación, un **actor** es algo o alguien externo al sistema que interactúa de forma directa con el sistema. Cuando decimos que interactúa nos referimos a que aporta información, recibe información, inicia una acción...

Se representan con una imagen de un "muñeco de palo" con el nombre del actor debajo.

<figure markdown>
  ![Representación actor](assets/EDES-U4.1.-DiagramaCasoUso-img01.gif)
  <figcaption>Representación de un actor</figcaption>
</figure>

Existen dos tipos de actores: Los **usuarios** y los **sistemas**.

No hay que entender los usuarios como personas singulares, sino como **"perfiles o roles"** que identifican a un tipo de usuario, pero no al usuario en sí. Por ejemplo, en una aplicación de gestión de nóminas, un actor de este tipo podría ser "gestor de nóminas" que se encarga de emitir y firmar nóminas. Este rol podría ser tomado, por ejemplo, por cualquier individuo del personal de recursos humanos y, además, por el jefe de la empresa. Es un ejemplo muy sencillo, pero como puedes ver, un actor no representa a una única persona o a un único usuario.

<figure markdown>
  ![Ejemplo de actor](assets/EDES-U4.1.-DiagramaCasoUso-img02.gif)
  <figcaption>Ejemplo de actor en un diagrama</figcaption>
</figure>

Por otro lado, los actores pueden ser **otros sistemas** que también interactúan con nuestro propio sistema. Un ejemplo podría ser, en nuestra aplicación de nóminas, un sistema que almacene las nóminas firmadas a modo de archivo. En este caso cuando se firma la nómina se recibe la misma por el sistema de archivo, por tanto el caso de uso se relaciona con el actor.

En ocasiones este tipo de actores no se representa con un "hombre de palo" porque puede dar la sensación de que es un usuario y queda poco intuitivo.

#### 2.2. Caso de uso

Un **caso de uso** se utiliza para representar una de las funcionalidades que realiza el sistema. Es una secuencia de acciones que hace el sistema y que producen un resultado que puede percibir un usuario.

Formalmente hablando, un caso de uso es una clasificación de comportamiento que especifica una unidad de funcionalidad completa y que está realizada por uno o más sujetos que se relacionan con el caso de uso colaborando para ello con uno o más actores y que produce un resultado que tiene alguna utilidad para cualquier de esos actores.

Se representan con una elipse que incluye en su interior el nombre del caso de uso.

<figure markdown>
  ![Representación de un caso de uso](assets/EDES-U4.1.-DiagramaCasoUso-img03.gif)
  <figcaption>Representación de un caso de uso</figcaption>
</figure>

Existen muchos ejemplos de casos de uso. Algunos podrían ser: **Crear pedido**, **Listar productos**, **Enviar correo**. Cualquier acción que realice la aplicación.

!!! note "Nota importante sobre UML 2.5"
    Las especificaciones anteriores a UML 2.5 requerían que un caso de uso sea invocado por un actor. En UML 2.5 esto se eliminó, lo que significa que podría haber algunas situaciones en las que la funcionalidad del sistema la inicie el propio sistema y, al mismo tiempo, brinde resultados útiles a un actor. Por ejemplo, el sistema podría notificar a un cliente que se envió la orden, programar la limpieza y el archivo de la información del usuario, solicitar información de otro sistema, etc.

#### 3.3. Relaciones

Las **relaciones** conectan los casos de uso con los actores o los casos de uso entre sí.

Cuando conectan un actor con un caso de uso representa que ese actor interactúa de alguna manera con ese caso de uso y se representa con una línea continua con la identificación `<<communicates>>`.

Cuando conectan casos de uso entre sí se pueden diferenciar dos tipos de relaciones: `<<include>>` y `<<extends>>`. En español a veces se usa la nomenclatura `<<usa>>` y `<<extiende>>`:

##### 3.3.1 Relación include

`<<include>>`: Se utiliza para representar que un caso de uso utiliza siempre a otro caso de uso. Es decir, un caso de uso se ejecutará obligatoriamente (lo incluye, lo usa). Se representa con una flecha discontinua que va desde el caso de uso de origen al caso de uso que se incluye.

<figure markdown>
  ![Relación include entre dos casos de uso](assets/EDES-U4.1.-DiagramaCasoUso-img04.gif)
  <figcaption>Relación include entre dos casos de uso</figcaption>
</figure>

Un uso típico de este tipo de relaciones se produce cuando dos casos de uso comparten una funcionalidad. Esa funcionalidad es extraída de los dos y se crea un caso de uso nuevo que se relaciona con los anteriores con un include.

<figure markdown>
  ![Ejemplo de uso de include](assets/EDES-U4.1.-DiagramaCasoUso-img05.gif)
  <figcaption>Ejemplo de uso de include</figcaption>
</figure>

En este ejemplo, los casos de uso **emitir factura** y **enviar producto** ejecutarán ambos el caso de uso **autenticación**.

##### 3.3.2. Relación extend

`<<extend>>`: Este tipo de relaciones se utilizan cuando un caso de uso tiene un comportamiento opcional, reflejado en otro caso de uso. Es decir, un caso de uso puede ejecutar, normalmente dependiendo de alguna condición o flujo del programa, otro caso de uso. Se representa con una flecha discontinua que va desde el caso de uso opcional al original.

<figure markdown>
  ![Relación extend entre dos casos de uso](assets/EDES-U4.1.-DiagramaCasoUso-img06.gif)
  <figcaption>Relación extend entre dos casos de uso</figcaption>
</figure>

Un ejemplo de esta relación podría ser la siguiente:

<figure markdown>
  ![Ejemplo de relaciones extend](assets/EDES-U4.1.-DiagramaCasoUso-img07.png)
  <figcaption>Ejemplo de relaciones extend</figcaption>
</figure>

En este supuesto el caso de uso **Hacer pedido** puede dar lugar (o no) a otros dos casos de uso: **Enviar notificación SMS** y **Enviar notificación email**. Se supone que, cuando un usuario hace un pedido, el sistema le permite elegir si quiere que se envíe una notificación de ese pedido por SMS o por email.

##### 3.3.3. Relación de generalización

**Generalización**: existe otra relación denominada generalización que consiste en hacer que un elemento herede el comportamiento de otro. Aunque se puede utilizar entre casos de uso, es más común utilizarlo entre actores, haciendo que uno de los actores tenga acceso a las funcionalidades de otro. Se representa con una flecha con la punta hueca que va desde el elemento que hereda al elemento heredado:

<figure markdown>
  ![Generalización entre dos actores](assets/EDES-U4.1.-DiagramaCasoUso-img08.png)
  <figcaption>Generalización entre dos actores</figcaption>
</figure>

### 4. Identificación de actores y casos de uso

Para identificar actores y casos de uso se ha seguido como ejemplo la actividad propuesta para tal fin por la metodología de desarrollo RUP (Rational Unified Process).

Se ha dividido la entrada en tres apartados:

1. Identificar actores.
2. Identificar casos de uso.
3. Describir cómo interactúan los actores y los casos de uso.

#### 4.1. Identificar actores

Encontrar actores es uno de los primeros pasos para definir los casos de uso del sistema. Cada tipo de fenómeno externo con el que el sistema debe interactuar está representado por un actor.

Como ya comentamos durante la explicación de qué es un diagrama de casos de uso, un actor es cualquier cosa que intercambia datos con el sistema. Un actor puede ser un usuario, un hardware externo u otro sistema.

Las siguientes preguntas nos ayudarán a encontrar los actores que interactuarán con el sistema:

- ¿Qué grupos de usuarios requieren ayuda del sistema para realizar sus tareas?

- ¿Qué grupos de usuarios se necesitan para ejecutar las funciones principales más obvias del sistema?

- ¿Qué grupos de usuarios están obligados a realizar funciones secundarias, como el mantenimiento y la administración del sistema?

- ¿Con qué hardware externo debe interactuar el sistema?

- ¿Con qué otros sistemas debe interactuar el sistema?

- ¿Alguna entidad (usuario u otro sistema) necesita ser informado sobre los cambios que ocurren dentro del sistema?

Estas preguntas nos pueden ayudar a encontrar actores. También podemos consultar el documento de requisitos funcionales del sistema, si existiese, para complementar la lista de actores identificados y casos de uso a los que daría lugar.

#### 4.2. Identificar casos de uso

Cuando se hayan identificado y descrito los actores, el modelo de casos de uso se realiza al identificar los casos de uso necesarios. Dado que los casos de uso son iniciados por los actores, una buena manera de identificar los casos de uso es considerar, para cada actor, de qué manera interactúa ese actor con el sistema, qué funcionalidad proporciona el sistema para ese actor.

Para encontrar casos de uso, se deben tener en cuenta las siguientes preguntas:

- ¿Qué funciones requiere un actor particular del sistema?

- ¿El sistema almacena y recupera información? Si es así, ¿qué actores provocan esta necesidad?

- ¿Se deben notificar al sistema los cambios externos? Si es así, ¿qué los notifica?

- ¿El sistema debe notificar a los actores sobre los cambios internos?

#### 4.3. Describir cómo interactúan los actores y los casos de uso

Una vez que se hayan identificado actores y casos de uso, es importante escribir al menos un breve resumen de cada uno. Es común que esta descripción se realice en formato de **especificación de casos de uso**.

La especificación de un caso de uso describe cómo interactúan los actores con el sistema. La descripción se centra en el comportamiento que es visible para el actor. No describe los detalles de cómo el sistema implementará ese comportamiento; eso lo hará en etapas posteriores del desarrollo, cuando entremos en el diseño del sistema.

El nivel de detalle de una especificación de casos de uso varía mucho. En algunos casos, una oración puede ser suficiente. En otros casos, se necesita más información. En la mayoría de los casos, tenemos un formato normal donde describimos los distintos campos de la especificación de un caso de uso.

Una especificación típica de un caso de uso incluye toda o parte de la siguiente información:

- **Nombre del caso de uso**: Un nombre breve, descriptivo y único.

- **Actores**: Los actores que participan en el caso de uso.

- **Precondiciones**: Condiciones que deben cumplirse para que el caso de uso pueda iniciarse.

- **Flujo principal**: Una descripción de paso a paso de lo que ocurre durante el caso de uso, centrada en la interacción entre el sistema y los actores.

- **Flujos alternativos**: Variaciones del flujo principal debido a decisiones o excepciones.

- **Postcondiciones**: Condiciones que serán verdaderas al finalizar el caso de uso.

- **Requisitos especiales**: Requisitos no funcionales que se aplican al caso de uso (rendimiento, seguridad, etc.).

### 4. Especificación de casos de uso

A continuación se muestra un ejemplo de especificación de caso de uso:

**Caso de Uso: Realizar Préstamo**

**Descripción:**
Este caso de uso describe el proceso mediante el cual un bibliotecario registra un préstamo de un libro a un socio.

**Actores:**
- Bibliotecario (Actor Principal)
- Socio (Actor Secundario)

**Precondiciones:**
- El socio debe estar registrado en el sistema.
- El libro debe estar disponible para préstamo.
- El socio no debe tener más de 3 libros prestados simultáneamente.
- El socio no debe tener multas pendientes.

**Flujo Principal:**

1. El bibliotecario inicia el proceso de préstamo.
2. El sistema solicita la identificación del socio.
3. El bibliotecario introduce el código del socio.
4. El sistema verifica que el socio existe y muestra su información.
5. El sistema solicita la identificación del libro.
6. El bibliotecario introduce el código del libro.
7. El sistema verifica que el libro está disponible.
8. El sistema registra el préstamo con la fecha actual y calcula la fecha de devolución (15 días).
9. El sistema actualiza el estado del libro a "prestado".
10. El sistema muestra un mensaje de confirmación con la fecha de devolución.
11. El caso de uso finaliza.

**Flujos Alternativos:**

**A1: El socio no existe (paso 4)**

1. El sistema muestra un mensaje de error indicando que el socio no está registrado.
2. El sistema vuelve al paso 2.

**A2: El socio tiene multas pendientes (paso 4)**

1. El sistema muestra un mensaje indicando que el socio tiene multas pendientes.
2. El sistema pregunta si se desea gestionar las multas.
3. El caso de uso finaliza.

**A3: El libro no está disponible (paso 7)**

1. El sistema muestra un mensaje indicando que el libro no está disponible.
2. El sistema ofrece la opción de reservar el libro.
3. El caso de uso finaliza.

**A4: El socio ha alcanzado el límite de préstamos (paso 4)**

1. El sistema muestra un mensaje indicando que el socio tiene el máximo de libros prestados.
2. El caso de uso finaliza.

**Postcondiciones:**
- El préstamo queda registrado en el sistema.
- El libro cambia su estado a "prestado".
- Se ha establecido una fecha de devolución.

**Requisitos Especiales:**
- El sistema debe responder en menos de 2 segundos para cada operación.
- Todas las operaciones deben quedar registradas en un log para auditoría.

### 5. Ejemplo completo: Sistema de tienda online

Vamos a ver un ejemplo completo de un diagrama de casos de uso para un sistema de tienda online.

**Descripción del Sistema:**

Una tienda online que permite a los usuarios buscar productos, añadirlos al carrito y realizar compras. Los administradores pueden gestionar productos, pedidos y usuarios.

**Funcionalidades Principales:**

**Registrarse en la tienda:** Un nuevo usuario puede crear una cuenta proporcionando su correo electrónico y una contraseña.

**Iniciar sesión:** Un usuario registrado puede iniciar sesión en la tienda para acceder a su cuenta y realizar compras.

**Buscar productos:** Los usuarios pueden buscar productos por nombre, categoría o precio.

**Ver detalles de un producto:** Al seleccionar un producto, el sistema muestra información detallada como descripción, precio, disponibilidad y opiniones de otros clientes.

**Añadir producto al carrito:** Los usuarios pueden agregar productos al carrito de compras.

**Ver carrito de compras:** Los usuarios pueden revisar los productos que han añadido al carrito antes de proceder con la compra.

**Realizar compra:** Los usuarios pueden finalizar su compra proporcionando información de pago y dirección de envío. Este proceso incluye realizar el pago.

**Realizar pagos:** El sistema procesa el pago usando una pasarela de pago externa.

**Ver historial de compras:** Los usuarios pueden consultar un listado de todas las compras realizadas anteriormente.

**Ver estado del pedido:** Si el usuario está consultando el historial de compras, puede seleccionar un pedido específico para ver su estado actual (en preparación, enviado, entregado).

**Cambiar contraseña:** Los usuarios pueden actualizar su contraseña desde la configuración de su cuenta.

**Cerrar sesión:** Los usuarios pueden cerrar su sesión de manera segura.

**Gestionar cuenta:** Los usuarios pueden acceder a la configuración de su cuenta, donde pueden cambiar su contraseña o cerrar sesión.

**Administrar productos:** El administrador puede agregar nuevos productos, eliminar productos existentes o actualizar la información de los productos.

**Administrar pedidos:** El administrador de la tienda puede ver y actualizar el estado de los pedidos de los clientes.

**Administrar usuarios:** El administrador de la tienda puede ver y actualizar los datos de los usuarios registrados en la tienda.

**Actores:**

- **Usuario:** Cliente que navega y compra en la tienda.
- **Administrador:** Gestiona productos, pedidos y usuarios.

**Casos de Uso Principales:**

**Para el Usuario:**

- Registrarse en la tienda
- Iniciar sesión
- Buscar productos y ver detalles de un producto
- Añadir productos al carrito y ver carrito de compras
- Realizar compra (incluye realizar pagos)
- Ver historial de compras
- Ver estado del pedido (extiende historial de compras)
- Gestionar cuenta (incluye cambiar contraseña y cerrar sesión)

**Para el Administrador:**

- Administrar productos (agregar, eliminar, actualizar productos)
- Administrar pedidos (actualizar estado de pedidos)
- Administrar usuarios (gestionar clientes registrados)

**Relaciones Clave:**

**<<include>>:**

- Realizar compra → Incluye Realizar pagos
- Gestionar cuenta → Incluye Cambiar contraseña y Cerrar sesión

**<<extend>>:**

- Ver estado del pedido → extiende Ver historial de compras

<figure markdown>
  ![Diagrama de casos de uso completo - Tienda online](assets/EDES-U4.1.-DiagramaCasoUso-img09.png)
  <figcaption>Diagrama de casos de uso completo de un sistema de tienda online</figcaption>
</figure>

El diagrama representa de manera clara cómo los usuarios interactúan con la tienda online y cómo el administrador gestiona la plataforma.

### 6. Otros ejemplos de diagramas de casos de uso

A continuación se muestran otros ejemplos adicionales de diagramas de casos de uso que ilustran diferentes escenarios y tipos de sistemas:

<figure markdown>
  ![Ejemplo adicional 1](assets/EDES-U4.1.-DiagramaCasoUso-img10.jpg)
  <figcaption>Ejemplo de diagrama de casos de uso - Sistema bancario</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 2](assets/EDES-U4.1.-DiagramaCasoUso-img11.gif)
  <figcaption>Ejemplo de diagrama de casos de uso con múltiples actores</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 3](assets/EDES-U4.1.-DiagramaCasoUso-img12.gif)
  <figcaption>Ejemplo de diagrama de casos de uso con relaciones complejas</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 4](assets/EDES-U4.1.-DiagramaCasoUso-img13.gif)
  <figcaption>Ejemplo de diagrama de casos de uso - Sistema de reservas</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 5](assets/EDES-U4.1.-DiagramaCasoUso-img14.gif)
  <figcaption>Ejemplo de diagrama de casos de uso - Sistema educativo</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 6](assets/EDES-U4.1.-DiagramaCasoUso-img15.gif)
  <figcaption>Ejemplo de diagrama de casos de uso - Sistema de gestión</figcaption>
</figure>

<figure markdown>
  ![Ejemplo adicional 7](assets/EDES-U4.1.-DiagramaCasoUso-img16.gif)
  <figcaption>Ejemplo de diagrama de casos de uso - Sistema hospitalario</figcaption>
</figure>

### 7. Herramientas para crear diagramas de casos de uso

Para crear diagramas de casos de uso, existen diversas herramientas que facilitan el proceso de modelado:

- **PlantUML:** Permite crear diagramas mediante código, lo que facilita el versionado y la integración con sistemas de control de versiones.

- **Draw.io:** Herramienta visual gratuita y online que permite crear diagramas de forma intuitiva.

- **Visual Paradigm:** Suite completa de modelado UML con funcionalidades avanzadas para desarrollo profesional.

- **StarUML:** Herramienta de modelado UML con soporte para múltiples tipos de diagramas.

- **Lucidchart:** Herramienta colaborativa online que permite trabajar en equipo en tiempo real.

- **Enterprise Architect:** Herramienta profesional completa para modelado de sistemas empresariales.

!!! tip "Recomendación"
    Para estudiantes y proyectos pequeños, se recomienda comenzar con herramientas gratuitas como PlantUML o Draw.io. Para proyectos profesionales y empresariales, herramientas como Visual Paradigm o Enterprise Architect ofrecen funcionalidades más avanzadas.

## Referencias y bibliografía

- Jacobson, I. (1992). *Object-Oriented Software Engineering: A Use Case Driven Approach*. Addison-Wesley.
- Rumbaugh, J., Jacobson, I., & Booch, G. (2004). *The Unified Modeling Language Reference Manual* (2nd ed.). Addison-Wesley.
- Rational Software Corporation. *Rational Unified Process: Best Practices for Software Development Teams*.
- [UML Use Case Diagrams - Visual Paradigm](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/what-is-use-case-diagram/)
- [PlantUML - Use Case Diagram](https://plantuml.com/es/use-case-diagram)
- [Use Case Diagram Tutorial - Lucidchart](https://www.lucidchart.com/pages/uml-use-case-diagram)
