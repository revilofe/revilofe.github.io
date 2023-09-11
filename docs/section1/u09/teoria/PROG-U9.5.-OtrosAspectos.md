---
title: "UD 9 - 9.5 Otros aspectos"
description: Otros aspectos
summary: Otros aspectos
authors:
    - Eduardo Fdez
date: 2022-04-11
icon:   
permalink: /prog/unidad9/9.5
categories:
    - PROG
tags:
    - Software
    - JDBC
    - DAO
---
## Otros aspectos a tener en cuenta

Supongamos que estás desarrollando una aplicación de comercio electrónico que necesita una base de datos para almacenar información de productos, pedidos, usuarios y pagos. La aplicación debe ser capaz de mostrar la información de productos a los usuarios, permitirles agregar productos a su carrito de compras, realizar pagos y gestionar los pedidos realizados.

Para interactuar con la base de datos, puedes utilizar un lenguaje de programación como Java o Kotlin y un sistema de gestión de bases de datos como MySQL o PostgreSQL, entre otros...

Al diseñar la base de datos, debes tener en cuenta la **relación entre los objetos de la aplicación y las tablas de la base de datos**. En este caso, por ejemplo, la tabla de productos debe contener información como el nombre, la descripción, el precio y la cantidad disponible, mientras que la tabla de pedidos debe contener información sobre los productos comprados, la dirección de envío, el estado del pedido, etc.

Para simplificar la interacción con la base de datos, puedes utilizar un ORM (Object-Relational Mapping) como Hibernate o Spring Data JPA, que te permitirá mapear las clases de la aplicación con las tablas de la base de datos y realizar operaciones CRUD (Create, Read, Update, Delete) sobre los objetos de la aplicación sin tener que escribir SQL directamente.

Para garantizar la integridad de los datos, es importante definir **restricciones de integridad** en la base de datos, como claves primarias, claves foráneas y restricciones de unicidad. Además, se debe **decidir si la gestión de la integridad se delegará completamente a la base de datos o si se realizará por código en la aplicación**.

En cuanto a la generación de identificadores, se puede optar por utilizar identificadores autonuméricos (como la columna id con AUTO_INCREMENT en MySQL) o identificadores UUID (Universally Unique Identifier), que son cadenas de caracteres aleatorias y únicas. La elección depende del caso de uso específico y de la preferencia del desarrollador.

Es importante **cerrar adecuadamente las conexiones y otros objetos relacionados con la base de datos, como los Statement y ResultSet**, para evitar fugas de memoria y mejorar el rendimiento de la aplicación. Para ello, se pueden utilizar bloques try-catch-finally o recursos try-with-resources.

En cuanto a la **gestión de transacciones**, se puede optar por utilizar transacciones explícitas, que son creadas y gestionadas por la aplicación, o transacciones implícitas, que son gestionadas por la base de datos. En cualquier caso, es importante garantizar que las operaciones se realicen en una transacción única y que se gestionen correctamente las excepciones.

Por último, en aplicaciones de alta concurrencia o gran carga de trabajo, es importante utilizar un **pool de conexiones** para optimizar el uso de los recursos de la base de datos y evitar el exceso de conexiones abiertas. El pool de conexiones es un conjunto de conexiones preestablecidas y listas para su uso, que se gestionan automáticamente y se reutilizan para minimizar el tiempo de espera y mejorar el rendimiento de la aplicación.

### Profundizamos en los puntos anteriores

#### Desfase Objeto-Relacional (ORM):

El desfase objeto-relacional (ORM) se refiere a la discrepancia entre los objetos utilizados en la programación orientada a objetos y las relaciones utilizadas en los sistemas de bases de datos relacionales. Para manejar esta discrepancia, se han desarrollado herramientas ORM que permiten mapear objetos a relaciones de base de datos y viceversa. Algunas herramientas ORM populares incluyen Hibernate, Entity Framework, SQLAlchemy y Sequelize. En kotlin la mas conocíada se llama Exposed.

[Desfase objeto-relacional](https://github.com/joseluisgs/Programacion-08-2022-2023#el-desfase-objeto-relacional)

#### Gestión de la integridad, por código o delegación a base de datos:

La integridad referencial se refiere a la consistencia de los datos almacenados en la base de datos. Puede ser gestionada por el código de la aplicación o delegada a la base de datos. La gestión de la integridad referencial por código implica que la aplicación es responsable de mantener la consistencia de los datos, mientras que la delegación a la base de datos significa que la base de datos se encarga de hacer cumplir las restricciones de integridad. Ambos enfoques tienen ventajas y desventajas, y la elección depende del contexto de la aplicación.

[Gestión de integridad](https://github.com/joseluisgs/Programacion-08-2022-2023#gesti%C3%B3n-de-integridad-por-c%C3%B3digo-o-delegaci%C3%B3n-en-la-base-de-datos)

#### Identificadores: autonuméricos vs UUID:

Los identificadores son una parte importante de cualquier sistema de bases de datos, ya que se utilizan para identificar de forma única cada fila en una tabla. Los identificadores pueden ser autonuméricos, lo que significa que la base de datos genera un valor único automáticamente cada vez que se inserta una nueva fila en la tabla. Otra opción son los identificadores UUID, que son identificadores únicos universalmente y generados por software. Ambos enfoques tienen ventajas y desventajas, es cuestión de diseño.

[Añutonuméricos vs UIDS](https://github.com/joseluisgs/Programacion-08-2022-2023#autonum%C3%A9ricos-vs-uuid)

#### Cierre de objetos: Conexiones, Statement, conexiones a base de datos:

Es importante cerrar correctamente los objetos de base de datos como conexiones y declaraciones (Statement) para evitar fugas de memoria y problemas de rendimiento. En algunos lenguajes de programación como Java, se utiliza la cláusula try-with-resources para asegurarse de que los objetos se cierren correctamente. En kotlin se usa `use{}` para asegurarnos que estos elementos quedan cerrados.

[Conexión/Desconexión a base de datos](https://github.com/joseluisgs/Programacion-08-2022-2023#conexi%C3%B3n-a-la-base-de-datos)

#### Gestión de transacciones:

Las transacciones se utilizan para garantizar que las operaciones en la base de datos se completen de forma coherente. Las transacciones permiten que varias operaciones se agrupen en una sola unidad lógica, lo que significa que si una operación falla, todas las operaciones realizadas en la transacción se deshacen. La gestión de transacciones es una parte importante del diseño de cualquier sistema de bases de datos, y se pueden utilizar diferentes enfoques como transacciones explícitas, transacciones implícitas y transacciones distribuidas.

[Transacciones](https://github.com/joseluisgs/Programacion-08-2022-2023#transacciones)

#### Pool de conexiones:

El pool de conexiones es una técnica utilizada para mejorar el rendimiento de las aplicaciones que interactúan con una base de datos. En lugar de crear una nueva conexión cada vez que se necesita acceder a la base de datos, se utiliza un pool de conexiones predefinido que permite reutilizar las conexiones existentes. Esto reduce la sobrecarga de la creación y eliminación de conexiones y mejora el rendimiento general del sistema.

## SQLDeLight

[SqlDeLight](https://cashapp.github.io/sqldelight/2.0.0-alpha05/) es una librería que nos permite generar código Kotlin para realizar [operaciones CRUD sobre una base de datos](https://cashapp.github.io/sqldelight/2.0.0-alpha05/jvm_sqlite/).

- [Librería SQLDeLight](https://github.com/joseluisgs/Programacion-08-2022-2023#sqldelight)
- [SQLDelight on the Server](https://ryanharter.com/blog/2020/08/sqldelight-on-the-server/)

## Fuente y bibliografía

- [Programación - 08 Programación con Bases de Datos - José Luis González](https://github.com/joseluisgs/Programacion-08-2022-2023)
