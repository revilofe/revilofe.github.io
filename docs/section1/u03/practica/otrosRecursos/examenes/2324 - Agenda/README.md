# 📒 Agenda 📚
  ------

## Práctica para realizar esta semana

### La fecha de entrega es el próximo ```viernes, 1 de diciembre```.

   ```
   * RA1: Conoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.
      - CE: a), b), c), d), e), f), g), h) e i).

   * RA3: Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.
      - CE: a), b), c), d), e), f) y g).

   * RA6: Escribe programas que manipulen información seleccionando y utilizando tipos avanzados de datos.
      - CE: a), b), c), d) y e).
   ```

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
