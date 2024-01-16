---
title: "UD 4 - POO2: Ejercicios básicos de POO"
summary: POO
description: POO
authors:
    - Diego Cano
date: 2024-01-16
icon: 
permalink: /prog/unidad4/p4.2
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - POO
---
## P4.2 - Ejercicios básicos de POO 6 al 10

### **Ejercicio 6**

   1. Realizar el ejercicio 1 de Conjuntos de los "Ejercicios básicos con Kotlin" (Ejercicio 3.3.1) orientado a objetos.

   2. Te proporciono algunas pistas de una posible solución:

      ```
      /**
      * Clase Compra
      * @param cliente cliente que realizo la compra
      * @param dia dia de la compra
      * @param monto monto de la compra
      * @constructor Crea una compra con cliente, dia y monto
      */
      ```
      ```
      /**
       * Clase Cliente
       * @param nombre nombre del cliente
       * @param domicilio domicilio del cliente
       * @constructor Crea un cliente con nombre y domicilio
       */
       ```
      ```      
      /**
       * Clase Domicilio
       * @param calle calle del domicilio
       * @param numero numero del domicilio
       * @constructor Crea un domicilio con calle y numero
       */
      ```
      
   3. La clase Domicilio tendrá un método llamado dirCompleta()que retornará el domicilio completo con la calle y el número.

   4. Las clases Compra, Cliente y Domicilio se establecerán como data class, es decir, delante de class incluirán el modificador data en la declaración de dichas clases.

   5. Para entender mejor que es una data class, visualizar el siguiente enlace: [Data classes](https://revilofe.github.io/section1/u04/teoria/PROG-U4.3.-kotlinPOO/#data-classes)

      ```
      /**
       * Clase RepositorioCompras
       * @constructor Crea un repositorio de compras
       */
      ```

   6. La clase `RepositorioCompras` tendrá un método para agregar una compra al repositorio y un método domicilios para retornar los domicilios de cada cliente al cual se le debe enviar una factura de compra.
      Esta función retorna una estructura que contenga cada domicilio una sola vez.

### **Ejercicio 7**

   1. Se quiere crear una clase `Cuenta` la cual se caracteriza por tener asociado un número de cuenta y un saldo disponible. 

   2. Además, se puede consultar el saldo disponible, recibir abonos y realizar pagos.

   3. Crear también una clase Persona, que se caracteriza por un DNI y una lista de cuentas bancarias.

   4. La `Persona` puede tener asociada hasta 3 cuentas bancarias, y debe tener un método que permita añadir cuentas *(hasta 3 el máximo permitido)*. 

   5. También debe contener un método que devuelva si la persona es morosa *(si tienen alguna cuenta con saldo negativo)*.

   6. En el programa principal, instanciar un objeto Persona con un DNI cualquiera, así como dos objetos cuenta, una sin saldo inicial y otra con 700 euros.
      La persona recibe la nómina mensual, por lo que ingresa 1100 euros en la primera cuenta, pero tiene que pagar el alquiler de 750 euros con la segunda.
      Imprimir por pantalla si la persona es morosa.

   8. Posteriormente hacer una transferencia de una cuenta a otra *(de forma que todos los saldos sean positivos)* y mostrar por pantalla el estado de la persona.

### **Ejercicio 8**

   1. Queremos mantener una colección de los libros que hemos ido leyendo, poniéndoles una calificación según nos haya gustado más o menos al leerlo.

   2. Para ello, crear la clase `Libro`, cuyos atributos son el `título`, el `autor`, el `número de páginas` y la `calificación` que le damos entre 0 y 10.

   3. Posteriormente, crear una clase `ConjuntoLibros`, que almacena un conjunto de libros *(con un vector de un tamaño fijo)*.
      Se pueden añadir libros que no existan *(siempre que haya espacio)*, eliminar libros por título o autor, mostrar por pantalla los libros con la mayor y menor calificación y,
      por último, mostrar un contenido de todo el conjunto.

   4. En el programa principal realizar las siguientes operaciones: crear dos libros, añadirlos al conjunto, eliminarlos por los dos criterios *(título y autor)* hasta que el conjunto
      esté vacío, volver a añadir un libro y mostrar el contenido final.

### **Ejercicio 9**

   1. Realizar un programa para gestionar una Lista de tareas con POO.

   2. El programa debe mostrar un menú en el que se pueda agregar (por defecto una nueva tarea tendrá el estado pendiente), eliminar y cambiar el estado de una tarea. También será posible mostrar la lista de tareas (todas las tareas), mostrar la lista de tareas pendientes y la lista de tareas ya realizadas.

   3. Una tarea debe tener una descripción y un estado que indique si está pendiente o ya fue realizada (en este caso, deberá mostrar la fecha, con formato DD-MM-AAAA HH:MM:SS, en la que se marcó cómo realizada)

   4. Os muestro un ejemplo de cómo generar una fecha:

      ```
      import java.time.LocalDateTime
      import java.time.format.DateTimeFormatter
      fun main() {
          val fechaHoraActual: LocalDateTime = LocalDateTime.now()
          // Formatear la fecha y hora para imprimir
          val formatter: DateTimeFormatter = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
          val fechaFormateada: String = fechaHoraActual.format(formatter)
          println("Fecha y Hora Actual: $fechaFormateada")
      }
      ```

### **Ejercicio 10**

   1. Realizar el juego del 3 en raya con POO.
