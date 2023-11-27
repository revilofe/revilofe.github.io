# Actividad: 📒 Agenda 📚

**ID actividad:** pe-Agenda-u1u2u3

**Agrupamiento de la actividad**: Individual

---

## Descripción:

   1. El programa debe estar correctamente documentado (Docstrings y comentarios). [UD 2 - 2.5 Documentar el código](https://revilofe.github.io/section1/u02/teoria/PROG-U2.5.-Documentar/)

   2. Observad que las funciones existentes en el código del programa no están completamente bien documentadas.

   3. Debes intentar ajustarte lo máximo posible a lo que se pide en los comentarios ```TODO``` que observarás en el programa ```agenda.py```.

   4. Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

   5. Además, tu programa deberá pasar correctamente las ```pruebas unitarias``` que se adjuntan en el fichero ```test_agenda.py``` de la carpeta ```test```.

   6. Debido al punto anterior, estás obligado a desarrollar los métodos que se importan y prueban en los tests unitarios: ```pedir_email()```, ```validar_email()``` y ```validar_telefono()```

   ### Comentarios TODO que debes resolver:

   * Línea 42
   ```
   #TODO: Crear un conjunto con las posibles opciones del menú de la agenda
   OPCIONES_MENU = ?
   #TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()
   ```

   * Línea 60
   ```
   #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
   ```

   * Línea 72
   ```
   #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado...
   ```

   * Línea 88
   ```
   #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
   ```

   * Línea 94
   ```
   #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 6
        if opcion in ?:
   ```

   * Línea 110
   ```
   #TODO: Asignar una estructura de datos vacía para trabajar con la agenda...
   contactos = ?
   ```

   * Línea 113
   ```
   #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
   #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
   cargar_contactos(?)
   ```

   * Línea 117
   ```
   #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
   # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
   # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
   # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
   #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
   # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
   # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
   # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
   # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
   # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactos, el telófono se mostrará como +34-600100100. 
   #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.
   agregar_contacto(?)
   ```

   * Línea 133
   ```
   #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
   eliminar_contacto(?)
   ```

   * Línea 139
   ```
   #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
   # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
   #
   # AGENDA (6)
   # ------
   # Nombre: Antonio Amargo (aamargo@gmail.com)
   # Teléfonos: niguno
   # ......
   # Nombre: Daniela Alba (danalba@gmail.com)
   # Teléfonos: +34-600606060 / +34-670898934
   # ......
   # Nombre: Laura Iglesias (liglesias@gmail.com)
   # Teléfonos: 666777333 / 666888555 / 607889988
   # ......
   # ** resto de contactos **
   #
   #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
   mostrar_contactos(?)
   ```

   * Línea 161
   ```
   #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
   # AGENDA
   # ------
   # 1. Nuevo contacto
   # 2. Modificar contacto
   # 3. Eliminar contacto
   # 4. Vaciar agenda
   # 5. Cargar agenda inicial
   # 6. Mostrar contactos por criterio
   # 7. Mostrar la agenda completa
   # 8. Salir
   #
   # >> Seleccione una opción: 
   #
   #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
   #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
   agenda(?)
   ```


## Objetivo:

* Aplicar conocimientos de estructuras de datos y control de flujo en un contexto práctico.
* Desarrollar habilidades de depuración y resolución de problemas en programación.
* Fomentar la creatividad y la innovación en el diseño de algoritmos y soluciones.

## Trabajo a realizar:

1. Documentar correctamente, controlar errores y excepciones en el código del juego proporcionado.
2. Implementar las mejoras requeridas para el programa.
3. Realizar los test unitarios de nuevas funciones que implementéis en el código y sean susceptibles de realizarse cómo hemos visto en clase.

Aclaración: 
- El programa entregado debe funcionar correctamente y cumplir los test unitarios.
- No se puede modificar el código de las funciones proporcionadas para que hagan algo distinto, pero si se puede añadir código en las funciones proporcionadas siempre que el funcionamiento sea el mismo.

## Recursos

* Apuntes dados en clase.
* Recursos y ejemplos vistos en clase.

## Permitido y Prohibido

* Permitido el uso de apuntes, ejemplos y recursos vistos en clase.
* Prohibido el uso de cualquier otro recurso: apuntes de compañeros, ayuda de compañeros, copilot, chatgpt, etc.

El uso de cualquier recurso prohibido supondrá la calificación de 0 en la actividad.

## Evaluación y calificación

Práctica para realizar en casa (30%) que se entregará esta semana. Esta práctica se evaluará con una calificación de 0 a 10 puntos.

La prueba especifica (60%) consistirá en dos pruebas: la práctica, dónde tenéis que analizar y actualizar un programa en Python para que cumpla con los requisitos especificados en el enunciado, y la teórica, que consiste en un cuestionario de preguntas sobre los contenidos de las unidades 1, 2 y 3.
- La parte práctica, este ejercicio, se evaluará con una calificación de 0 a 10 puntos. (80%)
- La parte teórica, que se realizará otro dia, y se evaluará con una calificación de 0 a 10 puntos. (20%)

El 10% restante corresponde al examen práctico ya realizado al finalizar la unidad 1. Esta práctica se evaluará con una calificación de 0 a 10 puntos.

### RA y CE evaluados:

* RA1: Conoce la estructura de un programa informático identificando y relacionando los elementos propios del lenguaje de programación utilizado.
* RA3: Escribe y depura código analizando y utilizando las estructuras de control del lenguaje.
* RA6: Escribe programas que manipulen información seleccionando y utilizando tipos avanzados de datos. (no todos los criterios de evaluación).

### Conlleva 
Presentación: SI, se evaluará con el profesor.

### Rubrica:

* El programa funciona adecuadamente.
* Las mejoras solicitadas se han implementado adecuadamente
* Trabajo con Variables, Constantes y Tipos de Datos y sus operadores. 
* Comentarios y Documentación en el Código 
* Herramientas de Desarrollo y Entornos Integrados
* Identificación y uso de las Estructuras de Control y Flujo del Programa
* Manejo de Errores y Excepciones
* Desarrollo, Prueba y Depuración de Programas
* Trabajo con Librerías y Estructuras de Datos Avanzadas (Listas, Tuplas, Diccionarios, Conjuntos, etc.)


## Entrega

> **La entrega tiene que cumplir las condiciones de entrega para poder ser calificada. En caso de no cumplirlas podría calificarse como no entregada.**

* **Conlleva la entrega de URL a repositorio:** El proyecto se entregará en un repositorio GitHub, trabajando por proyectos y dejando constancia de las acciones realizadas.

### La fecha de entrega es el próximo ```viernes, 1 de diciembre```.
