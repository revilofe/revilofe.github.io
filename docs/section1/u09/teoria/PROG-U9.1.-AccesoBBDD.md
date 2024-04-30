---
title: "UD 9 - 9.1 Acceso a BBDD"
description: Acceso a BBDD
summary: Acceso a BBDD
authors:
    - Eduardo Fdez
date: 2022-04-11
icon:   
permalink: /prog/unidad9/9.1
categories:
    - PROG
tags:
    - Software
    - JDBC
    - DAO
---
## 9.1. Acceso a bases de datos
A lo largo de este tema, se abordará el acceso a bases de datos relacionales desde aplicaciones desarrolladas en Kotlin. Se explicará qué es una base de datos y su importancia en el desarrollo de software, se describirá el lenguaje de programación Kotlin y su uso en la programación de aplicaciones que acceden a bases de datos, y se detallarán las características y métodos de acceso a sistemas gestores de bases de datos relacionales. Además, se explicará cómo programar conexiones con bases de datos, cómo almacenar, recuperar, mostrar, borrar y modificar información almacenada, y cómo crear aplicaciones para posibilitar la gestión de información en bases de datos.

### 1. Introducción
En el desarrollo de aplicaciones de software, es común la necesidad de almacenar y acceder a grandes cantidades de información de manera eficiente y segura. Para ello, se utilizan bases de datos, que son sistemas de almacenamiento de información que permiten organizar, gestionar y recuperar datos de manera estructurada. Las bases de datos son fundamentales en el desarrollo de aplicaciones empresariales, sitios web, aplicaciones móviles y otros tipos de software, ya que permiten almacenar y acceder a información de manera eficiente y escalable.

#### 1.1. Qué es una base de datos y su importancia en el desarrollo de software.

Una base de datos es un conjunto organizado de información que se almacena y se gestiona en un sistema informático. Está diseñada para almacenar, recuperar y gestionar grandes cantidades de datos de manera eficiente y confiable. Las bases de datos se utilizan en una amplia variedad de aplicaciones informáticas, desde simples aplicaciones de escritorio hasta sistemas empresariales complejos.  Además, las bases de datos permiten que varios usuarios accedan a los mismos datos al mismo tiempo, lo que es especialmente importante en entornos empresariales donde muchos usuarios necesitan acceder a la misma información.

La importancia de las bases de datos en el desarrollo de software radica en que permiten a los desarrolladores crear aplicaciones que pueden manejar grandes cantidades de información de manera eficiente y escalable. Las bases de datos también permiten a los desarrolladores implementar una lógica de negocio más sofisticada, lo que les permite crear aplicaciones más robustas y flexibles.

#### 1.2. Kotlin y su uso para acceder a bases de datos.

En la programación de aplicaciones que acceden a bases de datos, Kotlin al igual que Java, es un lenguaje de programación muy útil, ya que tiene soporte integrado para la conexión y el acceso a bases de datos a través del API JDBC (Java Database Connectivity). Además, Kotlin tiene una sintaxis concisa y expresiva, lo que facilita la creación de código que interactúa con las bases de datos.

El uso de Kotlin en la programación de aplicaciones que acceden a bases de datos permite a los desarrolladores crear aplicaciones más seguras, confiables y escalables. Kotlin ofrece características de seguridad como la prevención de nulos y la inmutabilidad, lo que reduce la posibilidad de errores y mejora la confiabilidad del código. Además, Kotlin es altamente escalable y fácil de mantener, lo que lo hace ideal para proyectos empresariales complejos.

### 2. Sistema gestor de bases de datos relacional y sus características

Un sistema gestor de bases de datos relacional (RDBMS, por sus siglas en inglés) es un tipo de software que se utiliza para almacenar, organizar y manipular datos en una base de datos relacional. Este tipo de sistema gestor de bases de datos utiliza un modelo de datos relacional para organizar los datos en tablas con filas y columnas, y utiliza claves primarias y foráneas para establecer relaciones entre las tablas.

Entre las características principales de los sistemas gestores de bases de datos relacionales, podemos destacar las siguientes:

- **Estructura basada en tablas**: Los datos se almacenan en tablas con filas y columnas. Cada columna tiene un nombre y un tipo de datos que define el tipo de información que se puede almacenar.  
- **Relaciones entre tablas**: Los sistemas gestores de bases de datos relacionales permiten establecer relaciones entre las tablas utilizando claves primarias y foráneas. Esto permite que los datos se puedan relacionar entre sí de manera efectiva y eficiente.  
- **Consultas complejas**: Los sistemas gestores de bases de datos relacionales permiten realizar consultas complejas utilizando el lenguaje SQL (Structured Query Language). Esto permite que los datos se puedan buscar, filtrar y ordenar de manera efectiva y eficiente.  
- **Integridad de los datos**: Los sistemas gestores de bases de datos relacionales tienen mecanismos integrados para garantizar la integridad de los datos, como las restricciones de integridad referencial y las validaciones de datos.  
- **Escalabilidad**: Los sistemas gestores de bases de datos relacionales son altamente escalables y se pueden utilizar para gestionar grandes volúmenes de datos.

###  3. Métodos de acceso a bases de datos relacionales
Existen varios métodos para acceder a bases de datos relacionales desde aplicaciones de software. Algunos de los métodos más comunes son:

- **JDBC (Java Database Connectivity)**: JDBC es una API estándar de Java que permite a las aplicaciones Java acceder a bases de datos relacionales. Proporciona una interfaz común para que las aplicaciones se conecten a bases de datos, realicen consultas y actualicen datos. JDBC es ampliamente utilizado y está soportado por la mayoría de los sistemas gestores de bases de datos relacionales.  
- **ORM (Object-Relational Mapping)**: Los ORM son frameworks que se construyen sobre JDBC y que permite mapear objetos de una aplicación a tablas de una base de datos relacional. Esto permite acceder a la base de datos utilizando objetos y métodos, en lugar de utilizar SQL directamente. El ORM proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos. El ORM utiliza un lenguaje de consulta específico del ORM (como HQL en Hibernate) que se traduce automáticamente en SQL para interactuar con la base de datos. El ORM es una técnica popular para el acceso a bases de datos en las aplicaciones actuales, por ejemplo: [Hibernate](https://hibernate.org/) en Java o [Exposed](https://github.com/JetBrains/Exposed) en Kotlin.  
- **JPA (Java Persistence API)**: JPA es una API de persistencia estándar de Java que permite a las aplicaciones Java acceder a bases de datos relacionales. JPA es una especificación que define una interfaz común para interactuar con diferentes sistemas gestores de bases de datos. JPA utiliza el ORM para mapear objetos de una aplicación a tablas de una base de datos relacional.  
- **Spring Data**: Spring Data es un proyecto de Spring Framework que proporciona una abstracción de acceso a datos para aplicaciones Java. Spring Data utiliza diferentes tecnologías de acceso a bases de datos, como JDBC, JPA y el ORM. Spring Data proporciona una interfaz común para acceder a diferentes sistemas gestores de bases de datos relacionales.

#### 3.1. Ventajas y desventajas de cada método de acceso a bases de datos relacionales.   

##### 3.1.1. JDBC (Java Database Connectivity):   

**Ventajas**:   
- Es una API estándar de Java y está soportada por la mayoría de los sistemas gestores de bases de datos relacionales.  
- Proporciona una interfaz común para que las aplicaciones se conecten a bases de datos, realicen consultas y actualicen datos.  
- Permite un control más granular sobre las consultas y las transacciones.    

**Desventajas**:   
- Requiere una cantidad significativa de código para interactuar con la base de datos.    
- Puede ser propenso a errores si se maneja incorrectamente.   
- No proporciona una abstracción de acceso a datos orientada a objetos.   

##### 3.1.2. ORM (Object-Relational Mapping):   

**Ventajas**:   
- Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.   
- Reduce significativamente la cantidad de código requerido para interactuar con la base de datos.   
- Proporciona una abstracción de acceso a datos orientada a objetos.   

**Desventajas**:   
- Puede haber una sobrecarga de rendimiento debido al mapeo de objetos a tablas de base de datos.   
- El ORM puede generar consultas SQL subóptimas.   
- La curva de aprendizaje inicial puede ser empinada.   

##### 3.1.3. JPA (Java Persistence API):   

**Ventajas**:   
- Proporciona una interfaz de persistencia estándar de Java para acceder a bases de datos relacionales.   
- Abstrae las diferencias entre los sistemas gestores de bases de datos subyacentes.    
- Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.   

**Desventajas**:   
- Puede ser más lento que JDBC si se requiere un control granular sobre las consultas y las transacciones.  
- El ORM utilizado por JPA puede generar consultas SQL subóptimas.   
- La curva de aprendizaje inicial puede ser empinada.   

##### 3.1.4. Spring Data:   

**Ventajas**:   
- Proporciona una abstracción de acceso a datos para aplicaciones Java.   
- Abstrae las diferencias entre los sistemas gestores de bases de datos subyacentes.   
- Proporciona una interfaz orientada a objetos para acceder a los datos de la base de datos.   

**Desventajas**:   
- Puede ser más lento que JDBC si se requiere un control granular sobre las consultas y las transacciones.   
- La curva de aprendizaje inicial puede ser empinada.   
- La configuración inicial puede ser más compleja que con JDBC.   


### 4. Trabajar con base de datos
Para trabajar con bases de datos en Kotlin, es necesario utilizar una librería que permita la conexión y el acceso a la base de datos. Una de las librerías más comunes para trabajar con bases de datos en Kotlin es JDBC (Java Database Connectivity), que es una API estándar de Java que permite a las aplicaciones Java acceder a bases de datos relacionales.

#### 4.1. Conectarnos a bases de datos
El establecimiento de conexiones con bases de datos es la primera tarea en el desarrollo de aplicaciones con acceso a datos. Para que una aplicación pueda interactuar con una base de datos, primero debe establecer una conexión con ella. Esta operación es una de las más costosas, y por eso existen varias implementaciones de los llamados pools de conexiones (por ejemplo [HikariCP](https://github.com/brettwooldridge/HikariCP)) que nos permiten optimizar esta tarea.

Para establecer una conexión con una base de datos utilizando Kotlin y JDBC, se requiere importar la librería JDBC en el proyecto. Luego, se debe cargar el driver JDBC específico para el gestor de base de datos que se va a utilizar, mediante la función `Class.forName("nombre_del_controlador")`. A continuación, se crea una instancia de la clase `Connection` que representa la conexión con la base de datos, mediante la función `DriverManager.getConnection(url, usuario, contraseña)`.

Para configurar la conexión, se deben proporcionar tres parámetros:   

1. la URL de la base de datos, que incluye el nombre del servidor, el puerto y el nombre de la base de datos.   
2. el nombre de usuario para acceder a la base de datos.    
3. la contraseña correspondiente.    
4. otras opciones de configuración.   

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

#### 4.2. Almacenar información

La inserción de registros en una base de datos, cuando estamos programando en un lenguaje orientado a objetos, suele coincidir con la inserción de la información de un objeto en una tabla. 

El proceso mediante el cual se inserta la información de un objeto que represente un registro en la tabla y utilizar el método de inserción de JDBC para agregarlo a la tabla, se puede ver en los siguientes pasos:

1. Crear una clase que represente la tabla y sus columnas.   
2. Crear una instancia de la clase y establecer los valores de las propiedades.   
3. Crear una conexión con la base de datos.   
4. Crear una sentencia `SQL INSERT` que especifique la tabla y los valores a insertar.   
5. Crear el objeto `PreparedStatement` para insertar la instancia en la tabla.   
4. Ejecutar la sentencia SQL utilizando un objeto `PreparedStatement`.   

A continuación se muestra un ejemplo de cómo insertar un registro en una tabla `mytable` utilizando un objeto instanciado de la clase `MyTable` que representa la tabla:

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

En este ejemplo, se crea una conexión con la base de datos utilizando el método `DriverManager.getConnection`. Luego, se crea una sentencia `SQL INSERT` utilizando un objeto `PreparedStatement`. Se crea una clase `MyTable` que representa la tabla y sus columnas, se crea una instancia de la clase . Se utiliza un objeto `PreparedStatement` para especificar los valores a insertar en las columnas de la tabla usando los métodos `setString`, `setInt` y `setDouble`. Finalmente, se ejecuta la sentencia utilizando el método `executeUpdate`.

#### 4.3. Recuperar y mostrar información.   

En el desarrollo de aplicaciones, es común necesitar recuperar y mostrar información almacenada en una base de datos. Para ello, se requiere conocer las técnicas y herramientas necesarias para conectarse a la base de datos, ejecutar consultas SQL y mapear los resultados a objetos en el lenguaje de programación utilizado.

En este punto, nos enfocaremos en cómo crear programas en Kotlin, aspecto que no difiere de como se hace en java, para recuperar información almacenada en bases de datos relacionales utilizando JDBC. Explicaremos cómo ejecutar consultas SQL y mapear los resultados a objetos Kotlin para que puedan ser mostrados al usuario. Además, también hablaremos sobre cómo manejar errores y excepciones que puedan surgir durante el proceso.

##### 4.3.1. Recuperar registros de la base de datos.   
Para recuperar registros de una tabla de la base de datos utilizando Kotlin y JDBC, necesitamos ejecutar una consulta SQL que seleccione los registros que deseamos recuperar. Esta consulta se puede ejecutar mediante un objeto `Statement` de JDBC, que se crea a partir de la conexión a la base de datos:

```kotlin
val statement = connection.createStatement()
val query = "SELECT id, nombre, email FROM usuario"
val resultSet = statement.executeQuery(query)
```

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

##### 4.3.2. Mostrar los resultados al usuario.   
A la hora de trabajar con la información y mostrarla al usuario final, es importante tener en cuenta la sensibilidad de la información almacenada en la base de datos y asegurarnos de cumplir con las normas de privacidad y seguridad de la información.

Para mostrar los resultados al usuario, podemos imprimirlos en la consola, mostrarlos en una interfaz de usuario o hacer cualquier otra cosa que queramos con ellos, dependiendo del tipo de aplicación que estemos desarrollando y de las necesidades del usuario. Algunas opciones comunes incluyen:

- Mostrar los resultados en una tabla: podemos crear una tabla en la interfaz de usuario de nuestra aplicación y agregar cada registro como una fila en la tabla. Esto permite al usuario ver todos los datos de una manera clara y ordenada.    
- Mostrar los resultados en una lista: si la cantidad de registros es pequeña, podemos mostrarlos en una lista simple. Esto es especialmente útil si solo necesitamos mostrar algunos datos de cada registro, como el nombre y la fecha.    
- Mostrar los resultados en un gráfico: si los datos son numéricos, podemos mostrarlos en un gráfico para que el usuario pueda ver visualmente las tendencias y las comparaciones entre los registros.   

#### 4.4. Eliminar y actualizar la información almacenada.   

En el desarrollo de aplicaciones, es muy común la necesidad de modificar o eliminar información almacenada en una base de datos. Para ello, es necesario contar con los conocimientos y herramientas adecuadas para realizar estas operaciones de manera segura y eficiente.

En este sentido, el lenguaje de programación Kotlin y la API JDBC ofrecen una serie de funcionalidades para llevar a cabo operaciones de modificación y eliminación en bases de datos relacionales. Es importante conocer cómo funcionan estos métodos para poder implementarlos correctamente en nuestras aplicaciones y evitar errores o problemas de seguridad en el manejo de la información almacenada.

En este apartado se abordarán los aspectos fundamentales de la realización de modificaciones y eliminaciones en una base de datos.

##### 4.4.1. Eliminar registros.

Para eliminar registros de una tabla en una base de datos utilizando Kotlin y JDBC, es necesario construir y ejecutar una consulta SQL de eliminación. Por ejemplo, si queremos eliminar un registro de la tabla `usuarios` que tenga un cierto identificador único. Hay que tener cuidado con la cláusula `WHERE`, ya que podemos tener un problema si no se establece adecuadamente. La consulta SQL podría ser algo como:

```Kotlin
DELETE FROM usuarios WHERE id = ?
```
Luego, en Kotlin, podemos crear una conexión a la base de datos y ejecutar la consulta utilizando la interfaz `PreparedStatement` de JDBC, como se explicó en puntos anteriores. La diferencia aquí es que en lugar de utilizar un método `executeQuery()`, utilizaremos el método `executeUpdate()` que indica que estamos realizando una operación de actualización. Además, deberemos proporcionar el valor del identificador único como parámetro en el objeto `PreparedStatement`.

```Kotlin
val id = 1
val query = "DELETE FROM usuarios WHERE id = ?"
val preparedStatement = connection.prepareStatement(query)
preparedStatement.setInt(1, id)
val rowsDeleted = preparedStatement.executeUpdate()
```
Estas operaciones tienen la clave en la sintaxis correcta de la consulta SQL y en la configuración correcta de los parámetros en el objeto `PreparedStatement`. Una vez que se tiene la conexión a la base de datos, se puede crear un objeto `PreparedStatement` con la consulta SQL y los parámetros correspondientes. Luego, se utiliza el método `executeUpdate()` para ejecutar la consulta y eliminar los registros. 

Por último, siempre será importante comprobar el resultado de la ejecución del método`executeUpdate()` y hacer el tratamiento que se estime oporturno en función del resultado obtenido. Por ejemplo, en este caso, el método `executeUpdate()` devuelve la cantidad de filas afectadas por la sentencia ejecutada, que en este caso debería ser `1` si se encontró y eliminó el registro correspondiente.

##### 4.4.2. Actualizar registros.  

Para actualizar registros en una tabla de la base de datos utilizando Kotlin y JDBC, primero es necesario establecer una conexión a la base de datos y crear una declaración SQL que actualice los campos necesarios. La declaración SQL debe incluir la cláusula `WHERE` para identificar los registros que se deben actualizar.

Por ejemplo, si tenemos una tabla llamada `usuarios` con los campos `nombre`, `apellido` y `email`, y queremos actualizar el email de un usuario en particular, podemos crear una declaración SQL como la siguiente:

```SQL
UPDATE usuarios SET email = 'nuevo_email@example.com' WHERE nombre = 'Juan' AND apellido = 'Pérez';
```
Una vez que se tiene la declaración SQL, se debe utilizar el objeto `Statement` de JDBC para ejecutarla. El método `executeUpdate()` se utiliza para ejecutar la declaración y actualizar los registros correspondientes.


```kotlin
val statement = connection.createStatement()
val updateCount = statement.executeUpdate(sql)
```

Como comentamos anteriormente, el método `executeUpdate()` devuelve la cantidad de filas afectadas por la sentencia ejecutada, que en este caso debería ser `1` si se encontró y actualizó el registro correspondiente. Siempre será importante comprobar el resultado de la ejecución del método`executeUpdate()` y hacer el tratamiento que se estime oporturno en función del resultado obtenido.

Para realizar un ejemplo más completo de cómo utilizar una consulta SQL para actualizar registros. Supongamos que queremos actualizar un registro en la tabla `users`:

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
statement.close()
connection.close()
```

En este ejemplo, primero se establece una conexión con la base de datos utilizando los detalles de conexión adecuados. Luego, se crea una consulta SQL para actualizar el nombre del usuario con `id = 1` en la tabla `users`. Sobre el objeto conexión se utiliza el método `prepareStatement` para crear un objeto `PreparedStatement`. Luego, se establecen los valores de los parámetros de la consulta utilizando los métodos set correspondientes de la clase `PreparedStatement` y se ejecuta la consulta utilizando el método `executeUpdate` de la clase `PreparedStatement`. Se verifica si se ha actualizado algún registro y se la sentencia y la conexión a la base de datos.

#### 4.5. Consulta de información almacenada.

Al desarrollar una aplicación que requiere acceder y manipular datos almacenados en una base de datos, es común que necesitemos realizar consultas más complejas para obtener la información requerida. Las consultas pueden involucrar operadores lógicos para filtrar resultados y funciones de agregación para realizar cálculos en los datos. Es importante que los programadores tengan conocimientos sólidos en la creación y ejecución de consultas SQL utilizando JDBC en Kotlin para obtener resultados precisos y eficientes. En esta sección, se explicará cómo crear consultas más complejas utilizando Kotlin y JDBC y se demostrará cómo utilizar operadores lógicos y funciones de agregación en las consultas SQL.

##### 4.5.1. Consultas complejas.
Para crear consultas más complejas utilizando Kotlin y JDBC, se pueden concatenar distintas cláusulas de SQL en una sola sentencia. Por ejemplo, para realizar una consulta que seleccione registros de una tabla que cumplan ciertas condiciones y los ordene por un campo en particular, se puede utilizar la siguiente sintaxis:

```kotlin
val query = "SELECT * FROM tabla WHERE condicion ORDER BY campo"
val statement = connection.createStatement()
val resultSet = statement.executeQuery(query)
```
En este ejemplo, `tabla` es el nombre de la tabla que se desea consultar, `condicion` es una expresión que define las condiciones que deben cumplir los registros seleccionados, y `campo` es el nombre del campo por el cual se deben ordenar los resultados. La consulta se ejecuta mediante el método `executeQuery()` del objeto `Statement`.


##### 4.5.2. Utilizar operadores lógicos y funciones de agregación en las consultas.

Para utilizar operadores lógicos y funciones de agregación en las consultas SQL, se puede utilizar la sintaxis estándar de SQL en la cadena de consulta. Por ejemplo, para realizar una consulta que seleccione registros de una tabla que cumplan ciertas condiciones y calcule la suma de los valores de un campo en particular, se puede utilizar la siguiente sintaxis:

Supongamos que tenemos una tabla llamada "ventas" que contiene información sobre las ventas realizadas en una tienda, con las siguientes columnas:

- `id`: identificador único de la venta.
- `fecha`: fecha en que se realizó la venta.
- `monto`: monto total de la venta.
- `tipo`: tipo de venta, puede ser "efectivo" o "tarjeta".
- `sucursal`: sucursal en la que se realizó la venta.

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

### 5. Crear aplicaciones para posibilitar la gestión de información
Al desarrollar aplicaciones que requieren almacenamiento de datos, es fundamental comprender cómo interactuar con bases de datos para almacenar información de manera efectiva y segura.

Un ejemplo de aplicación que permite la gestión de información en una base de datos podría ser un sistema de gestión de inventario para una tienda. La interfaz de usuario podría permitir al usuario agregar nuevos productos al inventario, actualizar la información de los productos existentes, eliminar productos, y realizar consultas para buscar productos por nombre, categoría, precio, etc.

Para implementar estas funcionalidades, se podría utilizar JDBC para establecer la conexión con la base de datos y ejecutar consultas SQL para agregar, actualizar o eliminar registros. Además, se podría utilizar una librería de UI como JavaFX para diseñar la interfaz de usuario y permitir al usuario interactuar con la base de datos de manera sencilla y visual.

Para manejar errores en la aplicación, se podría implementar validaciones en la interfaz de usuario para asegurarse de que los datos ingresados por el usuario son correctos y cumplen con las restricciones de la base de datos. Además, se podrían implementar mecanismos de manejo de excepciones en el código para manejar errores que puedan surgir durante la ejecución de consultas o actualizaciones en la base de datos.

#### 5.1. Gestión de información.

Para crear aplicaciones que permitan la gestión de información en una base de datos, es necesario diseñar una interfaz de usuario que permita al usuario interactuar con la base de datos de manera intuitiva y eficiente. La interfaz debe permitir realizar operaciones básicas como crear, leer, actualizar y eliminar registros.

Una vez que se ha diseñado la interfaz, se puede utilizar Kotlin y JDBC para implementar las funcionalidades. Por ejemplo, se puede utilizar JDBC para establecer la conexión con la base de datos y realizar consultas y actualizaciones en la misma.

CRUD es un acrónimo que se utiliza para describir las cuatro operaciones básicas de la gestión de datos: Crear, Leer, Actualizar y Eliminar (en inglés, Create, Read, Update, Delete).

Por lo tanto, al crear una aplicación para la gestión de la información presente en bases de datos relacionales, es común que se implementen estas cuatro operaciones CRUD para permitir al usuario realizar acciones como crear nuevos registros, leer la información almacenada, actualizar registros existentes o eliminar datos no deseados. A través de una interfaz de usuario adecuada, estas operaciones se pueden realizar de manera sencilla y eficiente, lo que mejora la experiencia del usuario y facilita la gestión de la información en la base de datos.

#### 5.2. Un CRUD para gestionar la información

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

#### 5.3. Manejar los errores.

Al trabajar con JDBC es importante tener en cuenta que pueden ocurrir diversas excepciones durante todo el proceso de establecimiento de conexión, ejecución de sentencia, recuperación de resultados, etc, y que indicarán distintos tipos de errores, como falta de conexión con el servidor, credenciales incorrectas, error de tipos, errores propios de base de datos por inconsistencias, etc. Por lo tanto, se debe utilizar una estructura `try-catch` para manejar estas excepciones. En los ejemplos anteriores se han podido ver como se han utilizado estos bloques try-catch para encerrar las operaciones relacionadas con JDBC.


##### 5.3.1. Manejar errores de conexión

Para manajar los posibles errores que se puedan producir al realizar la conexión tendremos que manejar las excepciones `SQLException` y `ClassNotFoundException`, que pueden ocurrir al intentar establecer la conexión o cargar el driver JDBC correspondiente. Además, se imprime un mensaje de error para cada una de estas excepciones. En la práctica, es importante identificar las excepciones que pueden ocurrir específicamente para el gestor de base de datos que se esté utilizando, y manejarlas adecuadamente.

Para manejar errores de conexión de una manera más efectiva, podemos utilizar un bloque `try-catch-finally` para asegurarnos de `Statements`, `ResultSets`, y `Connections` se cierre correctamente, incluso si se produce un error al establecer la conexión. Además, podemos lanzar una excepción personalizada en caso de que se produzca un error para informar al usuario del problema. Aquí te presento una ṕosible función para obtener una conexión `getConnection` que utiliza este enfoque:

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

> You should explicitly close `Statements`, `ResultSets`, and `Connections` when you no longer need them,

##### 5.3.2. Manejo de errores en la inserción

Es importante manejar los errores de inserción de datos en una base de datos para garantizar la integridad de la información. Para manejar estos errores en Kotlin y JDBC, podemos utilizar bloques `try-catch`.

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

Si el código de error es `1062`, significa que se ha violado una restricción de clave única, en este caso, la restricción de correo electrónico único. Mostramos un mensaje de error indicando que el correo electrónico ya está registrado. Estos códigos de error son específicos de cada DBMS, por tanto hay que consultar la documetnación del motor de base de datos para identificar los posibles códigos de error.

Si se produce cualquier otro tipo de excepción, mostramos un mensaje genérico con el mensaje de error devuelto por la base de datos.

##### 5.3.3. Manejo de errores de eliminación.   

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

##### 5.3.4. Manejar errores de actualización.

Al igual que en el caso de la eliminación de registros, es importante manejar correctamente los errores que puedan surgir al actualizar registros en una base de datos. Algunos de los errores más comunes son la falta de permisos para realizar la actualización, el incumplimiento de restricciones de integridad referencial o de validación, o la falta de conexión a la base de datos.


Dentro del bloque `catch`, se puede proporcionar información sobre el error al usuario o registrar el error en un archivo de registro para su posterior análisis. Es importante asegurarse de que el usuario sea informado adecuadamente sobre los errores que puedan ocurrir durante la actualización de registros.

### 6. Un CRUD aplicando el patrón DAO

#### 6.1. Patrón DAO 
El patrón DAO (Data Access Object) es un patrón de diseño que se utiliza para abstraer la capa de acceso a datos de una aplicación. El objetivo principal del patrón DAO es separar la lógica de acceso a datos de la lógica de negocio de la aplicación, lo que permite una mayor flexibilidad y mantenibilidad del código.

#### 6.2. Ejemplo
A continuación veremos un ejemplo en Kotlin de una implementación básica de un sistema CRUD (Create, Read, Update, Delete) usando un patrón DAO (Data Access Object) y servicios. Este código implementa una arquitectura básica de DAO y servicios para interactuar con una base de datos H2 y realizar operaciones CRUD en una tabla de usuarios. Se puede resumir en el siguiente extracto:

La clase `UserEntity` define el modelo de datos para el usuario con tres atributos: `id` (de tipo `UUID`), `name` y `email`.

La interfaz `UserDAO` define las operaciones que se pueden realizar con la base de datos para los usuarios, como crear (`create`), obtener todos los usuarios (`getAll`), obtener un usuario por su id (`getById`), actualizar (`update`) y eliminar (`delete`) un usuario. Se podrían crear más metodos en función de las necesidades, por ejemplo `getByEmail`.

La clase `UserDAOH2` implementa la interfaz `UserDAO` y define las operaciones de base de datos específicas de la implementación de H2. La clase tiene una dependencia de `DataSource`, que es una fuente de conexión de base de datos que se utiliza para realizar operaciones en la base de datos.

La interfaz `UserService` define las operaciones que se pueden realizar con los usuarios a nivel de servicio, que son crear (`create`), obtener todos los usuarios (`getAll`), obtener un usuario por su id (`getById`), actualizar (`update`) y eliminar (`delete`) un usuario. Igualmente, se podrían crear más metodos en función de las necesidades, por ejemplo `getByEmail`.

La clase `UserServiceImpl` implementa la interfaz `UserService` y utiliza un objeto de la clase `UserDAOH2` para interactuar con la base de datos.

La clase `DataSourceFactory` es una factoría que proporciona instancias de `DataSource` según el tipo de fuente de datos especificado.

En la función `main` se prueba todo el código, para ello se crea una instancia de la base de datos, se crea una instancia de `UserDAOH2`, se crea una instancia de `UserServiceImpl` y se realizan algunas operaciones CRUD en la base de datos utilizando `UserServiceImpl`. La salida se imprime en la consola.

Ver el código aquí: [Servicio de usuario, haciendo uso del patron DAO](https://github.com/revilofe/UserService)

Mas información en [CRUD](https://github.com/joseluisgs/Programacion-08-2022-2023#crud)

### 7. Resumiendo
- Las bases de datos son una herramienta crucial para el desarrollo de software, ya que permiten a los desarrolladores almacenar y gestionar grandes cantidades de información de manera eficiente y confiable. La capacidad de almacenar y acceder a información de manera eficiente es una necesidad en cualquier aplicación de software moderna, y las bases de datos son la solución más común y eficaz para esta necesidad.    
- Kotlin es un lenguaje de programación moderno y seguro que se utiliza cada vez más en el desarrollo de aplicaciones informáticas. En la programación de aplicaciones que acceden a bases de datos, Kotlin es una opción popular y efectiva debido a su soporte integrado para el acceso a bases de datos y su sintaxis concisa y expresiva. El uso de Kotlin en la programación de aplicaciones que acceden a bases de datos permite a los desarrolladores crear aplicaciones más seguras, confiables y escalables.    
- Un sistema gestor de bases de datos relacional es un software utilizado para almacenar, organizar y manipular datos en una base de datos relacional. Los sistemas gestores de bases de datos relacionales tienen características como una estructura basada en tablas, relaciones entre tablas, consultas complejas, integridad de los datos y escalabilidad. Los métodos de acceso a sistemas gestores de bases de datos relacionales incluyen la API JDBC y el ORM.    
- Los métodos de acceso a bases de datos incluyen JDBC, ORM, JPA y Spring Data. JDBC proporciona una interfaz común para acceder a bases de datos relacionales desde aplicaciones Java. El ORM y JPA proporcionan una interfaz orientada a objetos para acceder a los datos de la base de datos. Spring Data proporciona una abstracción de acceso a datos para aplicaciones Java. Los diferentes métodos de acceso a bases de datos tienen sus propias ventajas y desventajas. Es importante elegir el método adecuado según las necesidades de la aplicación. Si se requiere un control más granular sobre las consultas y las transacciones, JDBC puede ser la mejor opción. Si se busca una abstracción de acceso a datos orientada a objetos, ORM, JPA o Spring Data pueden ser la mejor opción.    
- Debemos elegir la forma de mostrar los resultados que mejor se adapte a las necesidades de nuestros usuarios y al tipo de aplicación que estamos desarrollando. Es importante que la presentación de los datos sea clara y fácil de entender para que los usuarios puedan interactuar con ellos de manera efectiva.     
- Es importante manejar adecuadamente los errores que se producen durante la interación de base de datos, por ejemplo al conectarnos, al inserción de datos, etc. Podemos utilizar bloques try-catch en Kotlin y JDBC para capturar y manejar estas excepciones de forma adecuada.    

### 8. Ejemplo
- [Servicio de usuario, haciendo uso del patron DAO](https://github.com/revilofe/UserService)

## Fuente y bibliografía
- [The DTO Pattern](https://www.baeldung.com/java-dto-pattern)
- [Programación - 08 Programación con Bases de Datos - José Luis González](https://github.com/joseluisgs/Programacion-08-2022-2023)
- [Librería SQLDeLight]https://github.com/joseluisgs/Programacion-08-2022-2023#sqldelight