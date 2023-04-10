---
title: "UD 9 - 9.1 Acceso a BBDD"
description: Acceso a BBDD
summary: Acceso a BBDD
authors:
    - Eduardo Fdez
date: 2022-04-11
icon: material/software
permalink: /prog/unidad9/9.1
categories:
    - PROG
tags:
    - Software
    - JDBC
    - DAO
---

# Introducción

## Qué es una base de datos y su importancia en el desarrollo de software.

Una base de datos es un conjunto organizado de información que se almacena y se gestiona en un sistema informático. Está diseñada para almacenar, recuperar y gestionar grandes cantidades de datos de manera eficiente y confiable. Las bases de datos se utilizan en una amplia variedad de aplicaciones informáticas, desde simples aplicaciones de escritorio hasta sistemas empresariales complejos.

En el desarrollo de software, las bases de datos son una herramienta fundamental para almacenar y gestionar información. Permiten a los desarrolladores crear aplicaciones que almacenan y acceden a datos de manera eficiente y segura. Además, las bases de datos permiten que varios usuarios accedan a los mismos datos al mismo tiempo, lo que es especialmente importante en entornos empresariales donde muchos usuarios necesitan acceder a la misma información.

La importancia de las bases de datos en el desarrollo de software radica en que permiten a los desarrolladores crear aplicaciones que pueden manejar grandes cantidades de información de manera eficiente y escalable. Las bases de datos también permiten a los desarrolladores implementar una lógica de negocio más sofisticada, lo que les permite crear aplicaciones más robustas y flexibles.

En resumen, las bases de datos son una herramienta crucial para el desarrollo de software, ya que permiten a los desarrolladores almacenar y gestionar grandes cantidades de información de manera eficiente y confiable. La capacidad de almacenar y acceder a información de manera eficiente es una necesidad en cualquier aplicación de software moderna, y las bases de datos son la solución más común y eficaz para esta necesidad.

## El lenguaje de programación Kotlin y su uso en la programación de aplicaciones que acceden a bases de datos.

En la programación de aplicaciones que acceden a bases de datos, Kotlin es un lenguaje de programación muy útil, ya que tiene soporte integrado para la conexión y el acceso a bases de datos a través del API JDBC (Java Database Connectivity). Además, Kotlin tiene una sintaxis concisa y expresiva, lo que facilita la creación de código que interactúa con las bases de datos.

El uso de Kotlin en la programación de aplicaciones que acceden a bases de datos permite a los desarrolladores crear aplicaciones más seguras, confiables y escalables. Kotlin ofrece características de seguridad como la prevención de nulos y la inmutabilidad, lo que reduce la posibilidad de errores y mejora la confiabilidad del código. Además, Kotlin es altamente escalable y fácil de mantener, lo que lo hace ideal para proyectos empresariales complejos.

En resumen, Kotlin es un lenguaje de programación moderno y seguro que se utiliza cada vez más en el desarrollo de aplicaciones informáticas. En la programación de aplicaciones que acceden a bases de datos, Kotlin es una opción popular y efectiva debido a su soporte integrado para el acceso a bases de datos y su sintaxis concisa y expresiva. El uso de Kotlin en la programación de aplicaciones que acceden a bases de datos permite a los desarrolladores crear aplicaciones más seguras, confiables y escalables.

# Características y métodos de acceso a sistemas gestores de bases de datos relacionales
Los sistemas gestores de bases de datos relacionales son herramientas fundamentales en el desarrollo de software, ya que permiten el almacenamiento y acceso a grandes cantidades de información de manera estructurada y eficiente. Para poder utilizarlos adecuadamente, es importante conocer sus características y métodos de acceso.

En este punto, se abordará en detalle las características de los sistemas gestores de bases de datos relacionales, así como los diferentes métodos de acceso a las bases de datos, como JDBC y ORM. Además, se discutirán las ventajas y desventajas de cada método de acceso para que los alumnos puedan elegir el que mejor se adapte a sus necesidades. Con este conocimiento, los alumnos estarán capacitados para utilizar bases de datos en sus proyectos de programación con Kotlin.

## Sistema gestor de bases de datos relacional y sus características

Un sistema gestor de bases de datos relacional (RDBMS, por sus siglas en inglés) es un tipo de software que se utiliza para almacenar, organizar y manipular datos en una base de datos relacional. Este tipo de sistema gestor de bases de datos utiliza un modelo de datos relacional para organizar los datos en tablas con filas y columnas, y utiliza claves primarias y foráneas para establecer relaciones entre las tablas.

Entre las características principales de los sistemas gestores de bases de datos relacionales, podemos destacar las siguientes:

Estructura basada en tablas: Los datos se almacenan en tablas con filas y columnas. Cada columna tiene un nombre y un tipo de datos que define el tipo de información que se puede almacenar.

Relaciones entre tablas: Los sistemas gestores de bases de datos relacionales permiten establecer relaciones entre las tablas utilizando claves primarias y foráneas. Esto permite que los datos se puedan relacionar entre sí de manera efectiva y eficiente.

Consultas complejas: Los sistemas gestores de bases de datos relacionales permiten realizar consultas complejas utilizando el lenguaje SQL (Structured Query Language). Esto permite que los datos se puedan buscar, filtrar y ordenar de manera efectiva y eficiente.

Integridad de los datos: Los sistemas gestores de bases de datos relacionales tienen mecanismos integrados para garantizar la integridad de los datos, como las restricciones de integridad referencial y las validaciones de datos.

Escalabilidad: Los sistemas gestores de bases de datos relacionales son altamente escalables y se pueden utilizar para gestionar grandes volúmenes de datos.

Entre los métodos de acceso a sistemas gestores de bases de datos relacionales, podemos destacar los siguientes:

API JDBC: La API JDBC (Java Database Connectivity) es una API estándar de Java que permite el acceso a bases de datos relacionales desde aplicaciones Java.

ORM (Object-Relational Mapping): El ORM es una técnica que permite mapear objetos de una aplicación a tablas de una base de datos relacional. Esto permite acceder a la base de datos utilizando objetos y métodos, en lugar de utilizar SQL directamente.

En resumen, un sistema gestor de bases de datos relacional es un software utilizado para almacenar, organizar y manipular datos en una base de datos relacional. Los sistemas gestores de bases de datos relacionales tienen características como una estructura basada en tablas, relaciones entre tablas, consultas complejas, integridad de los datos y escalabilidad. Los métodos de acceso a sistemas gestores de bases de datos relacionales incluyen la API JDBC y el ORM.

##  Métodos de acceso a bases de datos

**JDBC (Java Database Connectivity)**: JDBC es una API estándar de Java que permite a las aplicaciones Java acceder a bases de datos relacionales. Proporciona una interfaz común para que las aplicaciones se conecten a bases de datos, realicen consultas y actualicen datos. JDBC es ampliamente utilizado y está soportado por la mayoría de los sistemas gestores de bases de datos relacionales.

**ORM (Object-Relational Mapping)**: El ORM es una técnica que permite mapear objetos de una aplicación a tablas de una base de datos relacional. El ORM proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos. El ORM utiliza un lenguaje de consulta específico del ORM (como HQL en Hibernate) que se traduce automáticamente en SQL para interactuar con la base de datos. El ORM es una técnica popular para el acceso a bases de datos en aplicaciones Java.

**JPA (Java Persistence API)**: JPA es una API de persistencia estándar de Java que permite a las aplicaciones Java acceder a bases de datos relacionales. JPA es una especificación que define una interfaz común para interactuar con diferentes sistemas gestores de bases de datos. JPA utiliza el ORM para mapear objetos de una aplicación a tablas de una base de datos relacional.

**Spring Data**: Spring Data es un proyecto de Spring Framework que proporciona una abstracción de acceso a datos para aplicaciones Java. Spring Data utiliza diferentes tecnologías de acceso a bases de datos, como JDBC, JPA y el ORM. Spring Data proporciona una interfaz común para acceder a diferentes sistemas gestores de bases de datos relacionales.

En resumen, los métodos de acceso a bases de datos incluyen JDBC, ORM, JPA y Spring Data. JDBC proporciona una interfaz común para acceder a bases de datos relacionales desde aplicaciones Java. El ORM y JPA proporcionan una interfaz orientada a objetos para acceder a los datos de la base de datos. Spring Data proporciona una abstracción de acceso a datos para aplicaciones Java. Los diferentes métodos de acceso a bases de datos tienen sus propias ventajas y desventajas, y es importante elegir el método adecuado según las necesidades de la aplicación.


## Ventajas y desventajas de cada método de acceso a bases de datos relacionales.

### JDBC (Java Database Connectivity):
**Ventajas**:
* Es una API estándar de Java y está soportada por la mayoría de los sistemas gestores de bases de datos relacionales.
* Proporciona una interfaz común para que las aplicaciones se conecten a bases de datos, realicen consultas y actualicen datos.
* Permite un control más granular sobre las consultas y las transacciones.

**Desventajas:**
* Requiere una cantidad significativa de código para interactuar con la base de datos.
* Puede ser propenso a errores si se maneja incorrectamente.
* No proporciona una abstracción de acceso a datos orientada a objetos.


### ORM (Object-Relational Mapping):
**Ventajas**:
* Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.
* Reduce significativamente la cantidad de código requerido para interactuar con la base de datos.
* Proporciona una abstracción de acceso a datos orientada a objetos.

**Desventajas:**
* Puede haber una sobrecarga de rendimiento debido al mapeo de objetos a tablas de base de datos.
* El ORM puede generar consultas SQL subóptimas.
* La curva de aprendizaje inicial puede ser empinada.


### JPA (Java Persistence API):
**Ventajas**:
* Proporciona una interfaz de persistencia estándar de Java para acceder a bases de datos relacionales.
* Abstrae las diferencias entre los sistemas gestores de bases de datos subyacentes.
* Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.

**Desventajas:**
* Puede ser más lento que JDBC si se requiere un control granular sobre las consultas y las transacciones.
* El ORM utilizado por JPA puede generar consultas SQL subóptimas.
* La curva de aprendizaje inicial puede ser empinada.


### Spring Data:
**Ventajas**:
* Proporciona una abstracción de acceso a datos para aplicaciones Java.
* Abstrae las diferencias entre los sistemas gestores de bases de datos subyacentes.
* Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.

**Desventajas:**
* Puede ser más lento que JDBC si se requiere un control granular sobre las consultas y las transacciones.
* La curva de aprendizaje inicial puede ser empinada.
* La configuración inicial puede ser más compleja que con JDBC.

En resumen, cada método de acceso a bases de datos tiene sus propias ventajas y desventajas. Es importante elegir el método adecuado según las necesidades de la aplicación. Si se requiere un control más granular sobre las consultas y las transacciones, JDBC puede ser la mejor opción. Si se busca una abstracción de acceso a datos orientada a objetos, ORM, JPA o Spring Data pueden ser la mejor opción.

# Programar conexiones con bases de datos
La programación de conexiones con bases de datos es una tarea crucial en el desarrollo de aplicaciones con acceso a datos. Para que una aplicación pueda interactuar con una base de datos, primero debe establecer una conexión con ella.

En este proceso de conexión, se establecen los detalles de cómo la aplicación accederá a la base de datos, incluyendo la dirección de la base de datos, las credenciales de inicio de sesión y otras opciones de configuración.

En esta sección, se explicará cómo programar una conexión con una base de datos utilizando Kotlin y JDBC. También se demostrará cómo configurar la conexión y manejar errores de conexión para asegurar una experiencia de usuario fluida.

## Establecer conexión

Para establecer una conexión con una base de datos utilizando Kotlin y JDBC, se requiere importar la librería JDBC en el proyecto. Luego, se debe cargar el driver JDBC específico para el gestor de base de datos que se va a utilizar, mediante la función `Class.forName("nombre_del_controlador")`. A continuación, se crea una instancia de la clase `Connection` que representa la conexión con la base de datos, mediante la función `DriverManager.getConnection(url, usuario, contraseña)`.

## Configurar conexión

Para configurar la conexión, se deben proporcionar tres parámetros:
1.- la URL de la base de datos, que incluye el nombre del servidor, el puerto y el nombre de la base de datos;
2.- el nombre de usuario para acceder a la base de datos;
3.- la contraseña correspondiente.
La URL puede variar dependiendo del gestor de base de datos que se esté utilizando y del tipo de conexión (por ejemplo, si se usa SSL o no).

Un ejemplo de código en Kotlin para establecer una conexión con una base de datos MySQL sería:

```kotlin
import java.sql.*

fun main() {
    val url = "jdbc:mysql://localhost:3306/mydatabase"
    val usuario = "usuario"
    val contraseña = "contraseña"

    try {
        Class.forName("com.mysql.cj.jdbc.Driver")
        val conexion = DriverManager.getConnection(url, usuario, contraseña)
        println("Conexión exitosa")
        conexion.close()
    } catch (e: SQLException) {
        println("Error en la conexión: ${e.message}")
    } catch (e: ClassNotFoundException) {
        println("No se encontró el driver JDBC: ${e.message}")
    }
}
```
## Manejar errores de conexión

Al manejar errores de conexión, es importante tener en cuenta que pueden ocurrir diversas excepciones que indiquen distintos tipos de errores, como falta de conexión con el servidor, credenciales incorrectas, etc. Por lo tanto, se debe utilizar una estructura `try-catch` para manejar estas excepciones. En el ejemplo de código anterior, se utilizan dos bloques catch para manejar las excepciones `SQLException` y `ClassNotFoundException`, que pueden ocurrir al intentar establecer la conexión o cargar el driver JDBC correspondiente. Además, se imprime un mensaje de error para cada una de estas excepciones. En la práctica, es importante identificar las excepciones que pueden ocurrir específicamente para el gestor de base de datos que se esté utilizando, y manejarlas adecuadamente.


Para manejar errores de conexión de una manera más efectiva, podemos utilizar un bloque `try-catch-finally` para asegurarnos de que la conexión se cierre correctamente, incluso si se produce un error al establecer la conexión. Además, podemos lanzar una excepción personalizada en caso de que se produzca un error para informar al usuario del problema. Aquí te presento una ṕosible función para obtener una conexión `getConnection` que utiliza este enfoque:

```kotlin
import java.sql.Connection
import java.sql.DriverManager
import java.sql.SQLException

// Datos de conexión a la base de datos
val url = "jdbc:mysql://localhost:3306/nombre_de_la_base_de_datos"
val user = "usuario"
val password = "contraseña"

// Función para establecer la conexión
fun getConnection(): Connection {
    var connection: Connection? = null
    try {
        connection = DriverManager.getConnection(url, user, password)
    } catch (e: SQLException) {
        throw SQLException("Error al establecer la conexión con la base de datos: ${e.message}")
    } finally {
        if (connection != null) {
            try {
                connection.close()
            } catch (e: SQLException) {
                throw SQLException("Error al cerrar la conexión con la base de datos: ${e.message}")
            }
        }
    }
    return connection
}
```

En este ejemplo, utilizamos un bloque `try-catch` para capturar la excepción `SQLException` si se produce un error al establecer la conexión. Si se produce un error, lanzamos una excepción personalizada con un mensaje de error descriptivo para informar al usuario del problema.

En el bloque `finally`, cerramos la conexión utilizando el método `close` y también capturamos la excepción `SQLException` en caso de que se produzca un error al cerrar la conexión.

Con este código, hemos mejorado el manejo de errores de conexión en nuestro programa, lo que nos permite informar al usuario de los problemas que puedan surgir al interactuar con la base de datos.

# Escribir código para almacenar información en bases de datos

Al desarrollar aplicaciones que requieren almacenamiento de datos, es fundamental comprender cómo interactuar con bases de datos para almacenar información de manera efectiva y segura. En este sentido, una de las tareas más importantes es el proceso de escritura de datos en la base de datos.

En este punto, nos centraremos en cómo escribir código para almacenar información en bases de datos utilizando Kotlin y JDBC. Para ello, exploraremos cómo insertar registros en tablas de bases de datos utilizando objetos Java Database Connectivity (JDBC), la cual es una API estándar de Java que proporciona una interfaz para acceder a una variedad de bases de datos relacionales. También veremos cómo manejar errores de inserción y cómo validar los datos antes de guardarlos en la base de datos.

## Explicar cómo insertar registros en una tabla de la base de datos utilizando Kotlin y JDBC

Para insertar registros en una tabla de la base de datos utilizando Kotlin y JDBC, se debe seguir los siguientes pasos:

Crear una conexión con la base de datos.
Crear una sentencia SQL INSERT que especifique la tabla y los valores a insertar.
Ejecutar la sentencia SQL utilizando un objeto PreparedStatement.
A continuación se muestra un ejemplo de cómo insertar un registro en una tabla utilizando Kotlin y JDBC:

```Kotlin
val conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "username", "password")
val stmt = conn.prepareStatement("INSERT INTO mytable (column1, column2, column3) VALUES (?, ?, ?)")
stmt.setString(1, "value1")
stmt.setInt(2, 2)
stmt.setDouble(3, 3.14)
stmt.executeUpdate()
```

En este ejemplo, se crea una conexión con la base de datos utilizando el método `DriverManager.getConnection`. Luego, se crea una sentencia `SQL INSERT` utilizando un objeto `PreparedStatement`. Se utilizan los métodos `setString`, `setInt` y `setDouble` para especificar los valores a insertar en las columnas de la tabla. Finalmente, se ejecuta la sentencia utilizando el método `executeUpdate`.


## Utilizar JDBC para inserción en tablas

Para crear un objeto que represente un registro en la tabla y utilizar el método de inserción de JDBC para agregarlo a la tabla, se puede seguir los siguientes pasos:

* Crear una clase que represente la tabla y sus columnas.
* Crear una instancia de la clase y establecer los valores de las propiedades.
* Utilizar un objeto PreparedStatement para insertar la instancia en la tabla.

A continuación se muestra un ejemplo de cómo insertar un registro en una tabla `mytable``utilizando un objeto instanciado de la clase `MyTable` que representa la tabla:

```Kotlin

data class MyTable(val column1: String, val column2: Int, val column3: Double)

val myRecord = MyTable("value1", 2, 3.14)

val conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "username", "password")
val stmt = conn.prepareStatement("INSERT INTO mytable (column1, column2, column3) VALUES (?, ?, ?)")

stmt.setString(1, myRecord.column1)
stmt.setInt(2, myRecord.column2)
stmt.setDouble(3, myRecord.column3)

stmt.executeUpdate()

```

En este ejemplo, se crea una clase `MyTable` que representa la tabla y sus columnas. Se crea una instancia de la clase y se establecen los valores de las propiedades. Luego, se utiliza un objeto `PreparedStatement` para insertar la instancia en la tabla utilizando los métodos `setString`, `setInt` y `setDouble`.

## Manejo de errores en la inserción

Es importante manejar los errores de inserción de datos en una base de datos para garantizar la integridad de la información. Para manejar estos errores en Kotlin y JDBC, podemos utilizar bloques `try-catch`.

Cuando intentamos insertar un registro en una tabla y se produce un error, JDBC lanzará una excepción `SQLException`. Podemos capturar esta excepción con un bloque `try-catch` y tomar las medidas adecuadas según el tipo de error.

Por ejemplo, si estamos insertando un registro en una tabla que tiene una restricción de clave primaria y el registro que estamos intentando insertar ya existe en la tabla, JDBC lanzará una `SQLException` indicando que se viola la restricción de clave primaria. En este caso, podemos capturar la excepción y mostrar un mensaje al usuario informándole del error y pidiéndole que modifique los datos del registro.

Un ejemplo de manejo de errores de inserción en Kotlin y JDBC podría ser el siguiente:

```kotlin

try {
    val statement = connection.createStatement()
    val query = "INSERT INTO customers (name, email) VALUES ('John Doe', 'johndoe@email.com')"
    statement.executeUpdate(query)
} catch (e: SQLException) {
    when (e.errorCode) {
        1062 -> {
            // Violation of unique key constraint
            println("Error: The email address is already registered.")
        }
        else -> {
            // Other SQL exceptions
            println("Error: ${e.message}")
        }
    }
}
```

En este ejemplo, estamos insertando un registro en la tabla `customers` con los valores `John Doe` y `johndoe@email.com`. Si se produce un error durante la inserción, capturamos la excepción `SQLException` y comprobamos el código de error devuelto por la base de datos.

Si el código de error es `1062`, significa que se ha violado una restricción de clave única, en este caso, la restricción de correo electrónico único. Mostramos un mensaje de error indicando que el correo electrónico ya está registrado. Estos códigos de error son especificos de cada DBMS, por tanto hay que consultar la documetnación del motor de base de datos para identificar los posibles códigos de error.

Si se produce cualquier otro tipo de excepción, mostramos un mensaje genérico con el mensaje de error devuelto por la base de datos.

En resumen, es importante manejar adecuadamente los errores de inserción de datos en una base de datos para garantizar la integridad de la información. Podemos utilizar bloques try-catch en Kotlin y JDBC para capturar y manejar estas excepciones de forma adecuada.

# Crear programas para recuperar y mostrar información almacenada en bases de datos.
En el desarrollo de aplicaciones, es común necesitar recuperar y mostrar información almacenada en una base de datos. Para ello, se requiere conocer las técnicas y herramientas necesarias para conectarse a la base de datos, ejecutar consultas SQL y mapear los resultados a objetos en el lenguaje de programación utilizado.

En este punto, nos enfocaremos en cómo crear programas en Kotlin para recuperar información almacenada en bases de datos relacionales utilizando JDBC. Explicaremos cómo ejecutar consultas SQL y mapear los resultados a objetos Kotlin para que puedan ser mostrados al usuario. Además, también hablaremos sobre cómo manejar errores y excepciones que puedan surgir durante el proceso.

¡Comencemos!

## Recuperar registros de una tabla de la base de datos utilizando Kotlin y JDBC.

Para recuperar registros de una tabla de la base de datos utilizando Kotlin y JDBC, necesitamos ejecutar una consulta SQL que seleccione los registros que deseamos recuperar. Esta consulta se puede ejecutar mediante un objeto Statement de JDBC, que se crea a partir de la conexión a la base de datos:

```kotlin
val statement = connection.createStatement()
val query = "SELECT * FROM mi_tabla"
val resultSet = statement.executeQuery(query)
```

## Utilizar una consulta SQL para recuperar registros y cómo mapear los resultados a objetos en Kotlin.

Una vez que tenemos los resultados de la consulta en un objeto `ResultSet`, podemos mapearlos a objetos en Kotlin. Para hacer esto, necesitamos iterar sobre los resultados y crear un objeto para cada registro. Por ejemplo, si tenemos una tabla usuarios con columnas `id`, `nombre` y `email`, podemos crear una clase `Usuario` en Kotlin y mapear cada registro de la siguiente manera:

```Kotlin
data class Usuario(val id: Int, val nombre: String, val email: String)

val usuarios = mutableListOf<Usuario>()
while (resultSet.next()) {
    val id = resultSet.getInt("id")
    val nombre = resultSet.getString("nombre")
    val email = resultSet.getString("email")
    usuarios.add(Usuario(id, nombre, email))
}

```

## Mostrar los resultados al usuario.


A la hora de trabajar con la información y mostrarla al usuario final, es importante tener en cuenta la sensibilidad de la información almacenada en la base de datos y asegurarnos de cumplir con las normas de privacidad y seguridad de la información.

Para mostrar los resultados al usuario, podemos imprimirlos en la consola, mostrarlos en una interfaz de usuario o hacer cualquier otra cosa que queramos con ellos, dependiendo del tipo de aplicación que estemos desarrollando y de las necesidades del usuario. Algunas opciones comunes incluyen:

Mostrar los resultados en una tabla: podemos crear una tabla en la interfaz de usuario de nuestra aplicación y agregar cada registro como una fila en la tabla. Esto permite al usuario ver todos los datos de una manera clara y ordenada.

Mostrar los resultados en una lista: si la cantidad de registros es pequeña, podemos mostrarlos en una lista simple. Esto es especialmente útil si solo necesitamos mostrar algunos datos de cada registro, como el nombre y la fecha.

Mostrar los resultados en un gráfico: si los datos son numéricos, podemos mostrarlos en un gráfico para que el usuario pueda ver visualmente las tendencias y las comparaciones entre los registros.

Por ejemplo, podemos imprimir los nombres de los usuarios de la siguiente manera.

```kotlin
for (usuario in usuarios) {
    println(usuario.nombre)
}
```

En resumen, debemos elegir la forma de mostrar los resultados que mejor se adapte a las necesidades de nuestros usuarios y al tipo de aplicación que estamos desarrollando. Es importante que la presentación de los datos sea clara y fácil de entender para que los usuarios puedan interactuar con ellos de manera efectiva.


# Efectuar borrados y modificaciones sobre la información almacenada.

En el desarrollo de aplicaciones, es muy común la necesidad de modificar o eliminar información almacenada en una base de datos. Para ello, es necesario contar con los conocimientos y herramientas adecuadas para realizar estas operaciones de manera segura y eficiente.

En este sentido, el lenguaje de programación Kotlin y la API JDBC ofrecen una serie de funcionalidades para llevar a cabo operaciones de modificación y eliminación en bases de datos relacionales. Es importante conocer cómo funcionan estos métodos para poder implementarlos correctamente en nuestras aplicaciones y evitar errores o problemas de seguridad en el manejo de la información almacenada.

En este apartado se abordarán los aspectos fundamentales de la realización de modificaciones y eliminaciones en una base de datos, desde la ejecución de consultas SQL hasta la gestión de errores en caso de que surjan problemas durante la operación.

## Eliminar registros de una tabla de la base de datos utilizando Kotlin y JDBC.
Para eliminar registros de una tabla en una base de datos utilizando Kotlin y JDBC, es necesario construir y ejecutar una consulta SQL de eliminación. Por ejemplo, si queremos eliminar un registro de la tabla `usuarios` que tenga un cierto identificador único, la consulta SQL podría ser algo como:

```Kotlin
DELETE FROM usuarios WHERE id = ?
```
Luego, en Kotlin, podemos crear una conexión a la base de datos y ejecutar la consulta utilizando la interfaz ```PreparedStatement``` de JDBC, como se explicó en puntos anteriores. La diferencia aquí es que en lugar de utilizar un método `executeQuery()`, utilizaremos el método `executeUpdate()` que indica que estamos realizando una operación de actualización. Además, deberemos proporcionar el valor del identificador único como parámetro en el objeto `PreparedStatement`.

```Kotlin
val id = 1
val query = "DELETE FROM usuarios WHERE id = ?"
val preparedStatement = connection.prepareStatement(query)
preparedStatement.setInt(1, id)
val rowsDeleted = preparedStatement.executeUpdate()
```

El método `executeUpdate()` devuelve la cantidad de filas afectadas por la consulta, que en este caso debería ser `1` si se encontró y eliminó el registro correspondiente.

## Utilizar una consulta SQL para eliminar registros.

Para demostrar cómo utilizar una consulta SQL para eliminar registros, el ejemplo anterior ya proporciona la solución. La clave está en la sintaxis correcta de la consulta SQL y en la configuración correcta de los parámetros en el objeto `PreparedStatement`. Una vez que se tiene la conexión a la base de datos, se puede crear un objeto `PreparedStatement` con la consulta SQL y los parámetros correspondientes. Luego, se utiliza el método `executeUpdate()` para ejecutar la consulta y eliminar los registros. No hay que olvidar comprobar el valor devuelto por el método `executeUpdate()`, como veremos ahora.

## Describir cómo manejar errores de eliminación.
Para manejar errores de eliminación, podemos utilizar las mismas técnicas que se describieron para manejar errores de inserción. Es importante tener en cuenta que si se intenta eliminar un registro que no existe, la consulta SQL no afectará ninguna fila y el método `executeUpdate()` devolverá `0`. Por lo tanto, es una buena práctica verificar el valor devuelto por este método y manejar el caso en el que se intenta eliminar un registro que no existe.

Un ejemplo completo podría ser:
```kotlin
//Eliminar un registro de la tabla
try {
    // Crear la conexión
    val connection = DriverManager.getConnection(url, user, password)

    // Crear la sentencia SQL para eliminar el registro
    val sql = "DELETE FROM usuarios WHERE id = ?"

    // Crear el objeto PreparedStatement y establecer el valor del parámetro
    val statement = connection.prepareStatement(sql)
    statement.setInt(1, 1)

    // Ejecutar la sentencia y obtener el número de registros eliminados
    val rowsDeleted = statement.executeUpdate()

    // Comprobar si se ha eliminado el registro correctamente
    if (rowsDeleted > 0) {
        println("El usuario ha sido eliminado correctamente.")
    } else {
        println("No se ha eliminado ningún usuario.")
    }

    // Cerrar la conexión
    statement.close()
    connection.close()

} catch (e: SQLException) {
    println("Se ha producido un error al intentar eliminar el usuario.")
    println("Mensaje de error: ${e.message}")
}

```

En este ejemplo, se utiliza un bloque `try-catch` para manejar cualquier excepción de SQL que pueda ocurrir al intentar eliminar un registro de la tabla usuarios. Dentro del bloque `try`, se establece la conexión con la base de datos, se crea una sentencia SQL para eliminar el registro con `id` `1` y se crea un objeto `PreparedStatement` para ejecutar la sentencia. A continuación, se utiliza la función `executeUpdate()` para eliminar el registro y se obtiene el número de registros eliminados. Si se ha eliminado el registro correctamente, se muestra un mensaje indicando que el registro ha sido eliminado. De lo contrario, se muestra un mensaje indicando que no se ha eliminado ningún registro. Finalmente, se cierra la conexión y se maneja cualquier excepción de SQL que pueda ocurrir en el bloque `catch`.


## Actualizar registros de una tabla de la base de datos utilizando Kotlin y JDBC.

Para actualizar registros en una tabla de la base de datos utilizando Kotlin y JDBC, primero es necesario establecer una conexión a la base de datos y crear una declaración SQL que actualice los campos necesarios. La declaración SQL debe incluir la cláusula "WHERE" para identificar los registros que se deben actualizar.

Por ejemplo, si tenemos una tabla llamada `usuarios` con los campos `nombre`, `apellido` y `email`, y queremos actualizar el email de un usuario en particular, podemos crear una declaración SQL como la siguiente:

```SQL
UPDATE usuarios SET email = 'nuevo_email@example.com' WHERE nombre = 'Juan' AND apellido = 'Pérez';
```
Una vez que se tiene la declaración SQL, se debe utilizar el objeto Statement de JDBC para ejecutarla. El método `executeUpdate()` se utiliza para ejecutar la declaración y actualizar los registros correspondientes.

Para ejecutar la consulta, se utiliza el método executeUpdate() de la misma forma que en el ejemplo anterior.

```kotlin
val statement = connection.createStatement()
val updateCount = statement.executeUpdate(sql)
```

## Demostrar cómo utilizar una consulta SQL para actualizar registros.

Para demostrar cómo utilizar una consulta SQL para actualizar registros, podemos utilizar un ejemplo similar al anterior. Supongamos que queremos actualizar un registro en la tabla `users` de la base de datos utilizando Kotlin y JDBC:

```kotlin
// Establecer una conexión con la base de datos
val connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydatabase", "root", "password")

// Crear una consulta SQL para actualizar el nombre del usuario con id = 1
val sql = "UPDATE users SET name = ? WHERE id = ?"

// Crear un objeto que represente los valores actualizados
val name = "John"
val id = 1

// Utilizar el método "prepareStatement" de la conexión para crear un objeto PreparedStatement
val statement = connection.prepareStatement(sql)

// Establecer los valores de los parámetros de la consulta utilizando los métodos set correspondientes de la clase PreparedStatement
statement.setString(1, name)
statement.setInt(2, id)

// Ejecutar la consulta utilizando el método "executeUpdate" de la clase PreparedStatement
val rowsUpdated = statement.executeUpdate()

// Verificar si se ha actualizado algún registro
if (rowsUpdated > 0) {
    println("El registro ha sido actualizado exitosamente.")
} else {
    println("No se ha actualizado ningún registro.")
}

// Cerrar la conexión a la base de datos
connection.close()
```

En este ejemplo, primero se establece una conexión con la base de datos utilizando los detalles de conexión adecuados. Luego, se crea una consulta SQL para actualizar el nombre del usuario con `id = 1` en la tabla `users`. Se crea un objeto que representa el valor actualizado para el nombre y se utiliza el método `prepareStatement` de la conexión para crear un objeto `PreparedStatement`. Luego, se establecen los valores de los parámetros de la consulta utilizando los métodos set correspondientes de la clase `PreparedStatement` y se ejecuta la consulta utilizando el método `executeUpdate` de la clase `PreparedStatement`. Se verifica si se ha actualizado algún registro y se cierra la conexión a la base de datos.



## Manejar errores de actualización.

Al igual que en el caso de la eliminación de registros, es importante manejar correctamente los errores que puedan surgir al actualizar registros en una base de datos. Algunos de los errores más comunes son la falta de permisos para realizar la actualización, el incumplimiento de restricciones de integridad referencial o de validación, o la falta de conexión a la base de datos.

Para manejar estos errores, se puede utilizar un bloque `try-catch` que capture las excepciones de tipo `SQLException` que puedan surgir al ejecutar la actualización.

```kotlin
try {
    val statement = connection.createStatement()
    val updateCount = statement.executeUpdate(sql)
} catch (e: SQLException) {
    // Manejar la excepción de forma adecuada
}
```
Dentro del bloque `catch`, se puede proporcionar información sobre el error al usuario o registrar el error en un archivo de registro para su posterior análisis. Es importante asegurarse de que el usuario sea informado adecuadamente sobre los errores que puedan ocurrir durante la actualización de registros.


# Crear aplicaciones que ejecuten consultas sobre bases de datos

Al desarrollar una aplicación que requiere acceder y manipular datos almacenados en una base de datos, es común que necesitemos realizar consultas más complejas para obtener la información requerida. Las consultas pueden involucrar operadores lógicos para filtrar resultados y funciones de agregación para realizar cálculos en los datos. Es importante que los programadores tengan conocimientos sólidos en la creación y ejecución de consultas SQL utilizando JDBC en Kotlin para obtener resultados precisos y eficientes. Además, es fundamental saber cómo manejar errores durante la ejecución de las consultas para evitar errores en tiempo de ejecución o vulnerabilidades en la seguridad de la aplicación. En esta sección, se explicará cómo crear consultas más complejas utilizando Kotlin y JDBC, se demostrará cómo utilizar operadores lógicos y funciones de agregación en las consultas SQL, y se describirá cómo manejar errores en las consultas.

## Crear consultas más complejas utilizando Kotlin y JDBC.
Para crear consultas más complejas utilizando Kotlin y JDBC, se pueden concatenar distintas cláusulas de SQL en una sola sentencia. Por ejemplo, para realizar una consulta que seleccione registros de una tabla que cumplan ciertas condiciones y los ordene por un campo en particular, se puede utilizar la siguiente sintaxis:

```kotlin
val query = "SELECT * FROM tabla WHERE condicion ORDER BY campo"
val statement = connection.createStatement()
val resultSet = statement.executeQuery(query)
```
En este ejemplo, `tabla` es el nombre de la tabla que se desea consultar, `condicion` es una expresión que define las condiciones que deben cumplir los registros seleccionados, y `campo` es el nombre del campo por el cual se deben ordenar los resultados. La consulta se ejecuta mediante el método `executeQuery()` del objeto `Statement`.


## Utilizar operadores lógicos y funciones de agregación en las consultas SQL.

Para utilizar operadores lógicos y funciones de agregación en las consultas SQL, se puede utilizar la sintaxis estándar de SQL en la cadena de consulta. Por ejemplo, para realizar una consulta que seleccione registros de una tabla que cumplan ciertas condiciones y calcule la suma de los valores de un campo en particular, se puede utilizar la siguiente sintaxis:

```kotlin
val query = "SELECT SUM(campo) FROM tabla WHERE condicion"
val statement = connection.createStatement()
val resultSet = statement.executeQuery(query)
```

En este ejemplo, `SUM` es una función de agregación que se utiliza para calcular la suma de los valores de un `campo` en particular, y `condicion` es una expresión que define las condiciones que deben cumplir los registros seleccionados. La consulta se ejecuta mediante el método `executeQuery()` del objeto `Statement`.


## Manejar errores en las consultas
Para manejar errores en las consultas, se pueden utilizar estructuras de control de flujo como `try-catch`. Por ejemplo, si se produce un error al ejecutar una consulta, se puede capturar la excepción correspondiente y tomar medidas para manejarla adecuadamente. Por ejemplo:

```kotlin
try {
    val query = "SELECT * FROM tabla WHERE condicion"
    val statement = connection.createStatement()
    val resultSet = statement.executeQuery(query)
    // procesar resultados
} catch (e: SQLException) {
    // manejar el error
    println("Error al ejecutar la consulta: ${e.message}")
}
```
En este ejemplo, se utiliza un bloque `try-catch` para capturar excepciones del tipo `SQLException`, que se producen cuando hay un error al ejecutar una consulta. Si se produce un error, se muestra un mensaje de error en la consola.

## Un ejemplo más completo

En este ejemplo vamos a mostrar cómo utilizar operadores lógicos y funciones de agregación en una consulta SQL utilizando Kotlin y JDBC. En este ejemplo, supongamos que tenemos una tabla llamada "ventas" que contiene información sobre las ventas realizadas en una tienda, con las siguientes columnas:

id: identificador único de la venta.
fecha: fecha en que se realizó la venta.
monto: monto total de la venta.
tipo: tipo de venta, puede ser "efectivo" o "tarjeta".
sucursal: sucursal en la que se realizó la venta.
Supongamos que queremos obtener el monto total de las ventas realizadas en la sucursal "A" durante el mes de enero, y que fueron pagadas con tarjeta de crédito. Para hacer esto, podemos utilizar una consulta SQL con operadores lógicos y funciones de agregación, de la siguiente manera:

```kotlin
val consulta = "SELECT SUM(monto) FROM ventas WHERE sucursal = 'A' AND tipo = 'tarjeta' AND MONTH(fecha) = 1"

try {
    val statement = conexion.createStatement()
    val resultados = statement.executeQuery(consulta)

    while (resultados.next()) {
        val montoTotal = resultados.getDouble(1)
        println("Monto total de ventas en sucursal A pagadas con tarjeta en enero: $montoTotal")
    }

    resultados.close()
    statement.close()
} catch (ex: SQLException) {
    println("Error al ejecutar consulta: ${ex.message}")
}
```

En este ejemplo, la consulta SQL utiliza el operador lógico `AND` para combinar varias condiciones en la cláusula `WHERE`: la `sucursal` debe ser `A`, el `tipo` de venta debe ser `tarjeta`, y el `mes` de la fecha debe ser `1` (que representa el mes de enero). Además, la función de agregación `SUM` se utiliza para sumar los montos totales de todas las ventas que cumplen con estas condiciones.

Si la consulta se ejecuta correctamente, el resultado se muestra por consola. Si ocurre un error, se muestra un mensaje de error.


# Crear aplicaciones para posibilitar la gestión de información presente en bases de datos relacionales


## Diseñar una interfaz de usuario para permitir la gestión de información en una base de datos.

Para crear aplicaciones que permitan la gestión de información en una base de datos, es necesario diseñar una interfaz de usuario que permita al usuario interactuar con la base de datos de manera intuitiva y eficiente. La interfaz debe permitir realizar operaciones básicas como crear, leer, actualizar y eliminar registros.

Una vez que se ha diseñado la interfaz, se puede utilizar Kotlin y JDBC para implementar las funcionalidades. Por ejemplo, se puede utilizar JDBC para establecer la conexión con la base de datos y realizar consultas y actualizaciones en la misma.

CRUD es un acrónimo que se utiliza para describir las cuatro operaciones básicas de la gestión de datos: Crear, Leer, Actualizar y Eliminar (en inglés, Create, Read, Update, Delete).

Por lo tanto, al crear una aplicación para la gestión de la información presente en bases de datos relacionales, es común que se implementen estas cuatro operaciones CRUD para permitir al usuario realizar acciones como crear nuevos registros, leer la información almacenada, actualizar registros existentes o eliminar datos no deseados. A través de una interfaz de usuario adecuada, estas operaciones se pueden realizar de manera sencilla y eficiente, lo que mejora la experiencia del usuario y facilita la gestión de la información en la base de datos.

## Como crear un CRUD para gestioanr la información

Las operaciones del CRUD son fundamentales en la mayoría de las aplicaciones de gestión de bases de datos, ya que permiten al usuario interactuar con los datos de una manera intuitiva y eficiente. Un ejemplo de un CRUD para gestionar el acceso a una tabla `users`


```Kotlin
import java.sql.*

// Definir constantes para la conexión
const val DB_URL = "jdbc:mysql://localhost:3306/mydatabase"
const val USER = "root"
const val PASS = "mypassword"

// Función para establecer una conexión a la base de datos
fun getConnection(): Connection? {
    var conn: Connection? = null
    try {
        conn = DriverManager.getConnection(DB_URL, USER, PASS)
    } catch (ex: SQLException) {
        ex.printStackTrace()
    }
    return conn
}

// Función para cerrar una conexión a la base de datos
fun closeConnection(conn: Connection?) {
    try {
        conn?.close()
    } catch (ex: SQLException) {
        ex.printStackTrace()
    }
}

// Función para crear un nuevo registro en la tabla de la base de datos
fun createRecord(name: String, email: String) {
    val conn = getConnection()
    val sql = "INSERT INTO users (name, email) VALUES (?, ?)"
    try {
        val stmt = conn?.prepareStatement(sql)
        stmt?.setString(1, name)
        stmt?.setString(2, email)
        stmt?.executeUpdate()
        stmt?.close()
    } catch (ex: SQLException) {
        ex.printStackTrace()
    } finally {
        closeConnection(conn)
    }
}

// Función para leer todos los registros de la tabla de la base de datos
fun readAllRecords(): List<User> {
    val conn = getConnection()
    val sql = "SELECT * FROM users"
    val userList = mutableListOf<User>()
    try {
        val stmt = conn?.createStatement()
        val rs = stmt?.executeQuery(sql)
        while (rs?.next() == true) {
            val id = rs.getInt("id")
            val name = rs.getString("name")
            val email = rs.getString("email")
            userList.add(User(id, name, email))
        }
        rs?.close()
        stmt?.close()
    } catch (ex: SQLException) {
        ex.printStackTrace()
    } finally {
        closeConnection(conn)
    }
    return userList
}

// Función para actualizar un registro existente en la tabla de la base de datos
fun updateRecord(id: Int, name: String, email: String) {
    val conn = getConnection()
    val sql = "UPDATE users SET name = ?, email = ? WHERE id = ?"
    try {
        val stmt = conn?.prepareStatement(sql)
        stmt?.setString(1, name)
        stmt?.setString(2, email)
        stmt?.setInt(3, id)
        stmt?.executeUpdate()
        stmt?.close()
    } catch (ex: SQLException) {
        ex.printStackTrace()
    } finally {
        closeConnection(conn)
    }
}

// Función para eliminar un registro existente en la tabla de la base de datos
fun deleteRecord(id: Int) {
    val conn = getConnection()
    val sql = "DELETE FROM users WHERE id = ?"
    try {
        val stmt = conn?.prepareStatement(sql)
        stmt?.setInt(1, id)
        stmt?.executeUpdate()
        stmt?.close()
    } catch (ex: SQLException) {
        ex.printStackTrace()
    } finally {
        closeConnection(conn)
    }
}

// Clase para representar un registro de la tabla de la base de datos
data class User(val id: Int, val name: String, val email: String)

fun main() {
    // Crear un nuevo registro en la tabla de la base de datos
    createRecord("Juan", "juan@example.com")

    // Leer todos los registros de la tabla de la base de datos
    val userList = readAllRecords()
    for (user in userList) {
        println(user)
    }

    // Actualizar un registro existente en la tabla de la base de datos
    updateRecord(1, "Juan Perez", "juan.perez@example.com")

    // Leer todos los registros de la tabla de la base de datos nuevamente
    val updatedUserList = readAllRecords()
    for (user in updatedUserList) {
        println(user)
    }

    // Eliminar un registro existente en la tabla de la base de datos
    deleteRecord(1)

    // Leer todos los registros de la tabla de la base de datos nuevamente
    val finalUserList = readAllRecords()
    for (user in finalUserList) {
        println(user)
    }
}
```

Para empezar, la función `getConnection()` se utiliza para establecer una conexión con la base de datos. Esta función utiliza los valores de las constantes `DB_URL`, `USER` y `PASS` para conectarse a la base de datos mydatabase. Para usar esta función, solo tienes que llamarla en tu código:

```kotlin
val conn = getConnection()
```

La función `closeConnection()` se utiliza para cerrar la conexión con la base de datos. Esta función se llama al final de cada operación de base de datos para asegurarse de que se cierra la conexión y se liberan los recursos utilizados. Para usar esta función, solo tienes que llamarla en tu código y pasarle la conexión como argumento:

```kotlin
closeConnection(conn)
```

La función `createRecord()` se utiliza para crear un nuevo registro en la tabla de la base de datos. Esta función toma dos parámetros: name y email, que son los valores que se insertarán en la tabla users. Para usar esta función, solo tienes que llamarla en tu código y pasarle los valores que quieres insertar:

```kotlin
createRecord("John Doe", "john.doe@example.com")
```

La función `readAllRecords()` se utiliza para leer todos los registros de la tabla de la base de datos y devolver una lista de objetos User. Esta función no toma ningún parámetro. Para usar esta función, solo tienes que llamarla en tu código:

```kotlin
val userList = readAllRecords()
```

La función `updateRecord()` se utiliza para actualizar un registro existente en la tabla de la base de datos. Esta función toma tres parámetros: id, name y email, que son los nuevos valores que se actualizarán en la tabla users. id es el identificador del registro que se va a actualizar. Para usar esta función, solo tienes que llamarla en tu código y pasarle los valores que quieres actualizar:

```kotlin
updateRecord(1, "Jane Doe", "jane.doe@example.com")
```

La función `deleteRecord()` se utiliza para eliminar un registro existente en la tabla de la base de datos. Esta función toma un parámetro: id, que es el identificador del registro que se va a eliminar. Para usar esta función, solo tienes que llamarla en tu código y pasarle el valor que quieres eliminar:

```kotlin
deleteRecord(1)
```

## Describir cómo manejar errores en la aplicación.

Para manejar errores en la aplicación, es importante validar los datos ingresados por el usuario y verificar que cumplan con los requisitos de la base de datos, como el tipo de datos y las restricciones de integridad. Además, se deben manejar adecuadamente los errores que puedan surgir durante la ejecución de consultas o actualizaciones en la base de datos.

Un ejemplo de aplicación que permite la gestión de información en una base de datos podría ser un sistema de gestión de inventario para una tienda. La interfaz de usuario podría permitir al usuario agregar nuevos productos al inventario, actualizar la información de los productos existentes, eliminar productos, y realizar consultas para buscar productos por nombre, categoría, precio, etc.

Para implementar estas funcionalidades, se podría utilizar JDBC para establecer la conexión con la base de datos y ejecutar consultas SQL para agregar, actualizar o eliminar registros. Además, se podría utilizar una librería de UI como JavaFX para diseñar la interfaz de usuario y permitir al usuario interactuar con la base de datos de manera sencilla y visual.

Para manejar errores en la aplicación, se podría implementar validaciones en la interfaz de usuario para asegurarse de que los datos ingresados por el usuario son correctos y cumplen con las restricciones de la base de datos. Además, se podrían implementar mecanismos de manejo de excepciones en el código para manejar errores que puedan surgir durante la ejecución de consultas o actualizaciones en la base de datos.

## Gestionar información aplicando patrón DAO
El siguiente código en Kotlin es una implementación básica de un sistema CRUD (Create, Read, Update, Delete) usando un patrón DAO (Data Access Object) y servicios.

En resumen, la clase `UserEntity` define el modelo de datos para el usuario con tres atributos: `id` (de tipo `UUID`), `name` y `email`.

La interfaz `UserDAO` define las operaciones que se pueden realizar con la base de datos para los usuarios, como crear (`create`), obtener todos los usuarios (`getAll`), obtener un usuario por su id (`getById`), actualizar (`update`) y eliminar (`delete`) un usuario. Se podrían crear más metodos en función de las necesidades, por ejemplo `getByEmail`.

La clase `UserDAOH2` implementa la interfaz `UserDAO` y define las operaciones de base de datos específicas de la implementación de H2. La clase tiene una dependencia de `DataSource`, que es una fuente de conexión de base de datos que se utiliza para realizar operaciones en la base de datos.

La interfaz `UserService` define las operaciones que se pueden realizar con los usuarios a nivel de servicio, que son crear (`create`), obtener todos los usuarios (`getAll`), obtener un usuario por su id (`getById`), actualizar (`update`) y eliminar (`delete`) un usuario. Igualmente, se podrían crear más metodos en función de las necesidades, por ejemplo `getByEmail`.

La clase `UserServiceImpl` implementa la interfaz `UserService` y utiliza un objeto de la clase `UserDAOH2` para interactuar con la base de datos.

La clase `DataSourceFactory` es una factoría que proporciona instancias de `DataSource` según el tipo de fuente de datos especificado.

En la función `main` se prueba todo el código, para ello se crea una instancia de la base de datos, se crea una instancia de `UserDAOH2`, se crea una instancia de `UserServiceImpl` y se realizan algunas operaciones CRUD en la base de datos utilizando `UserServiceImpl`. La salida se imprime en la consola.


```kotlin

data class UserEntity(var id: UUID = UUID.randomUUID(), var name: String, var email: String)


interface UserDAO {
    fun create(user: UserEntity):UserEntity
    fun getAll(): List<UserEntity>
    fun getById(id: UUID): UserEntity?
    fun update(user: UserEntity):UserEntity
    fun delete(id: UUID)
}


class UserDAOH2(private val dataSource: DataSource) : UserDAO {

    override fun create(user: UserEntity): UserEntity {
        val sql = "INSERT INTO tuser (id, name, email) VALUES (?, ?, ?)"
        return dataSource.connection.use { conn ->
            conn.prepareStatement(sql).use { stmt ->
                stmt.setString(1, user.id.toString())
                stmt.setString(2, user.name)
                stmt.setString(3, user.email)
                user
            }
        }
    }

    override fun getById(id: UUID): UserEntity? {
        val sql = "SELECT * FROM tuser WHERE id = ?"
        return dataSource.connection.use { conn ->
            conn.prepareStatement(sql).use { stmt ->
                stmt.setString(1, id.toString())
                val rs = stmt.executeQuery()
                if (rs.next()) {
                    UserEntity(
                        id = UUID.fromString(rs.getString("id")),
                        name = rs.getString("name"),
                        email = rs.getString("email")
                    )
                } else {
                    null
                }
            }
        }
    }

    override fun getAll(): List<UserEntity> {
        val sql = "SELECT * FROM tuser"
        return dataSource.connection.use { conn ->
            conn.prepareStatement(sql).use { stmt ->
                val rs = stmt.executeQuery()
                val users = mutableListOf<UserEntity>()
                while (rs.next()) {
                    users.add(
                        UserEntity(
                            id = UUID.fromString(rs.getString("id")),
                            name = rs.getString("name"),
                            email = rs.getString("email")
                        )
                    )
                }
                users
            }
        }
    }

    override fun update(user: UserEntity):UserEntity {
        val sql = "UPDATE tuser SET name = ?, email = ? WHERE id = ?"
        return dataSource.connection.use { conn ->
            conn.prepareStatement(sql).use { stmt ->
                stmt.setString(1, user.name)
                stmt.setString(2, user.email)
                stmt.setString(3, user.id.toString())
                stmt.executeUpdate()
                user
            }
        }
    }

    override fun delete(id: UUID) {
        val sql = "DELETE FROM tuser WHERE id = ?"
        dataSource.connection.use { conn ->
            conn.prepareStatement(sql).use { stmt ->
                stmt.setString(1, id.toString())
                stmt.executeUpdate()
            }
        }
    }
}


interface UserService {
    fun create(user: UserEntity): UserEntity
    fun getById(id: UUID): UserEntity?
    fun update(user: UserEntity): UserEntity
    fun delete(id: UUID)
    fun getAll(): List<UserEntity>
}


class UserServiceImpl(private val userDao: UserDAO) : UserService {
    override fun create(user: UserEntity): UserEntity {
        return userDao.create(user)
    }

    override fun getById(id: UUID): UserEntity? {
        return userDao.getById(id)
    }

    override fun update(user: UserEntity): UserEntity {
        return userDao.update(user)
    }

    override fun delete(id: UUID) {
        userDao.delete(id)
    }

    override fun getAll(): List<UserEntity> {
        return userDao.getAll()
    }
}


object DataSourceFactory {
    enum class DataSourceType {
        HIKARI,
        JDBC
    }

    fun getDS(dataSourceType: DataSourceType): DataSource {
        return when (dataSourceType) {
            DataSourceType.HIKARI -> {
                val config = HikariConfig()
                config.jdbcUrl = "jdbc:h2:./default"
                config.username = "user"
                config.password = "user"
                config.driverClassName = "org.h2.Driver"
                config.maximumPoolSize = 10
                config.isAutoCommit = true
                config.transactionIsolation = "TRANSACTION_REPEATABLE_READ"
                HikariDataSource(config)
            }

            DataSourceType.JDBC -> TODO()
        }
    }
}


fun main() {
    // Creamos la instancia de la base de datos
    val dataSource = DataSourceFactory.getDS(DataSourceFactory.DataSourceType.HIKARI)

    // Creamos la instancia de UserDAO
    val userDao = UserDAOH2(dataSource)

    // Creamos la instancia de UserService
    val userService = UserServiceImpl(userDao)

    // Creamos un nuevo usuario
    val newUser = UserEntity(name = "John Doe", email = "johndoe@example.com")
    var createdUser = userService.create(newUser)
    println("Created user: $createdUser")

    // Obtenemos un usuario por su ID
    val foundUser = userService.getById(createdUser.id)
    println("Found user: $foundUser")

    // Actualizamos el usuario
    val updatedUser = foundUser!!.copy(name = "Jane Doe")
    val savedUser = userService.update(updatedUser)
    println("Updated user: $savedUser")

    val otherUser = UserEntity(name = "Eduardo Fernandez", email = "eferoli@gmail.com")
    createdUser = userService.create( otherUser)
    println("Created user: $createdUser")


    // Obtenemos todos los usuarios
    var allUsers = userService.getAll()
    println("All users: $allUsers")

    // Eliminamos el usuario
    userService.delete(savedUser.id)
    println("User deleted")

    // Obtenemos todos los usuarios
    allUsers = userService.getAll()
    println("All users: $allUsers")

    // Eliminamos el usuario
    userService.delete(otherUser.id)
    println("User deleted")
}

```

En resumen, este código implementa una arquitectura básica de DAO y servicios para interactuar con una base de datos H2 y realizar operaciones CRUD en una tabla de usuarios.

## Fuente y bibliografía
