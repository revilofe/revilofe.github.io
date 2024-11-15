# Actividad: **Simulador del Euromillón**

## Objetivo
Desarrollar un programa en Python que simule el sorteo del Euromillón. El programa permitirá a un jugador seleccionar sus números y estrellas, generará los números ganadores de manera aleatoria, y mostrará los resultados del sorteo junto con los aciertos del jugador.

---

## Requisitos del Programa

1. **Configuración del Juego**:

   - El juego debe permitir elegir un rango de números y estrellas basado en los siguientes valores:
      * Números del 1 al 50 (se seleccionan 5 números).
      * Estrellas del 1 al 12 (se seleccionan 2 estrellas).

2. **Flujo del Programa**:

   - Limpiar la pantalla antes de iniciar el juego.
   - Pedir al jugador cuántos números y estrellas quiere jugar (dentro de un rango razonable, por ejemplo podemos configurar un rango de un mínimo de 5 números y 2 estrellas, con un máximo del doble del valor mínimo).
   - Solicitar al jugador que seleccione sus números y estrellas, garantizando que no pueda repetir números (utilizar un conjunto para esta tarea).
   - Generar los números y estrellas premiadas de manera aleatoria (simular el sorteo).
   - Comparar los números y estrellas del jugador con los números y estrellas premiados.
   - Mostrar los resultados del sorteo, incluyendo los números y estrellas jugados, los números premiados y la cantidad de aciertos en cada categoría.

3. **Restricciones**:

   - El programa debe impedir que el jugador seleccione un número o estrella fuera del rango permitido.
   - No se puede repetir un número o estrella ya seleccionada.
   - El programa debe manejar errores de entrada de datos (por ejemplo, si el jugador introduce un valor no numérico).

4. **Resultado Final**:

   - Mostrar los números y estrellas jugados.
   - Mostrar los números y estrellas premiados.
   - Indicar cuántos números y cuántas estrellas ha acertado el jugador.

---

## Guía Paso a Paso

### Paso 1: Definir la Configuración del Juego ###

- Define un diccionario llamado `CONFIG` que almacene los valores mínimos, máximos y totales de los números y estrellas que se pueden seleccionar *(será un diccionario cuyo valor de las claves "bombo" y "estrellas" será a su vez otro diccionario con pares claves-valor para configurar el min, max y total de bombo y estrellas)*.

### Paso 2: Crear las Funciones Principales ###

1. **Limpieza de Pantalla y Pausa**:

   - Crea una función `limpiar_pantalla` que limpie la consola.
   - Crea una función `pausa` que detenga el programa hasta que el jugador presione ENTER.

2. **Entrada de Datos**:

   - Diseña una función **`preguntar_total`** que pregunte al usuario cuántos elementos quiere jugar, dentro de un rango predefinido.

     La función recibe dos argumentos, ***`desc`***, con la descripción del tipo de elemento ("números", "estrellas") y ***`min`***, con el valor mínimo permitido.

     Cómo se ha comentado previamente, el rango máximo no se pasa por parámetro a la función, sino que se establece como el doble del valor mínimo que se pasa cómo segundo argumento de la función.

     Por último, la función ***retornará la cantidad*** (número entero válido y dentro del rango) seleccionada por el usuario.

     Un ejemplo de llamada de esta función será el siguiente:

     ```python
     total_numeros = preguntar_total("números", CONFIG["bombo"]["total"])
     ```

     La ejecución de este código mostrará lo siguiente y esperará que el usuario introduzca un valor:

     ```
     Total de números a jugar (5-10)? >>
     ```
     
   - Diseña una función **`pedir_numero`** que valide que el número ingresado esté dentro de un rango y no sea repetido.

     La función recibe un ***`mensaje`*** que se mostrará al usuario, el valor ***`mínimo`*** permitido y el ***`máximo`***.

     ***Retornará un número entero*** válido ingresado por el usuario dentro del rango. Mientras que no sea así, se mostrará el mensaje de error correspondiente y se volverá a pedir el número.

     Un ejemplo de llamada de esta función será el siguiente:

     ```python
     total = pedir_numero(f"Total de {desc} a jugar ({min}-{max})? >> ", min, max)
     ```

     La ejecución de este código mostrará lo siguiente y esperará que el usuario introduzca un número entero válido dentro del rango: 

     ```
     Total de números a jugar (5-10)? >> rtyr
     *ERROR* Número no válido!
     Total de números a jugar (5-10)? >> 66
     *ERROR* El número debe estar entre el 5 y el 10!
     Total de números a jugar (5-10)? >> 
     ```

   - Diseña una función **`solicitar_numeros`** que permita al jugador seleccionar un conjunto de números únicos.

     Los argumentos que recibe esta función son:
     * ***`desc`***: Descripción del tipo de número ("el número", "la estrella")
     * ***`total`***: Cantidad total de números que el usuario debe ingresar.
     * ***`min`***: Valor mínimo permitido.
     * ***`max`***: Valor máximo permitido.

     Esta función debe crear un bucle con llamadas a la función `pedir_numero`, donde irá agregando a un conjunto los números que va ingresando el usuario.
     Si el usuario selecciona un número que ya existe, no se insertará en el conjunto gracias a las propiedades de los mismos.

     Además, dentro del bucle, después de pedir el número y agregarlo al conjunto, debe mostrar la lista de números ordenada *(para esto podéis utilizar la función `sorted`)*

     Un ejemplo de llamada de esta función será el siguiente:

     ```python
     print(f"\n### Seleccione {total_numeros} números del {CONFIG["bombo"]["min"]} al {CONFIG["bombo"]["max"]} ###")
     numeros = solicitar_numeros("el número", total_numeros, CONFIG["bombo"]["min"], CONFIG["bombo"]["max"])
     ```

     La ejecución de este código mostrará lo siguiente y esperará que el usuario introduzca un número entero válido dentro del rango: 

     ```
     ### Seleccione 5 números del 1 al 50 ###
     Dame el número #1#>> 33
     [33]
     Dame el número #2#>> 12
     [12, 33]
     Dame el número #3#>> 47
     [12, 33, 47]
     Dame el número #4#>> 8
     [8, 12, 33, 47]
     Dame el número #5#>> 2
     [2, 8, 12, 33, 47]
     ```     

4. **Sorteo Aleatorio**:

   - Crea una función **`sacar_bolas`** que genere un conjunto de números o estrellas al azar dentro del rango permitido.

     La función debe seleccionar al azar una cantidad de elementos **únicos** dentro de un rango y retornar el conjunto que se ha generado.
     Los parámetros de entrada de la función son el ***`mínimo`***, ***`máximo`*** y el ***`total`*** de elementos que se van a generar.

     Esta función ***retorna un conjunto de números enteros*** seleccionados al azar dentro del rango mínimo-máximo.

     Podéis hacerlo cómo vosotros queráis (os propongo que investiguéis y utilicéis la función `random.sample()` con un `range()`, pero no es obligatorio con estas funciones)

     Un ejemplo de llamada de esta función será el siguiente *(la función ***`generar_euromillon`*** os la doy realizada y debe ser llamada desde el main, depués de preguntar al jugador los números y estrellas que va a jugar)*:

     ```python
     def generar_euromillon(premiados: set, estrellas: set):
         """
         Genera los números y estrellas premiados para el sorteo del Euromillón.

         Args:
             premiados (set): Conjunto donde se almacenarán los números premiados.
             estrellas (set): Conjunto donde se almacenarán las estrellas premiadas.
         """
         premiados.update(sacar_bolas(CONFIG["bombo"]["min"], CONFIG["bombo"]["max"], CONFIG["bombo"]["total"]))
         estrellas.update(sacar_bolas(CONFIG["estrellas"]["min"], CONFIG["estrellas"]["max"], CONFIG["estrellas"]["total"]))     
     ```

     La ejecución de este código actualizará los conjuntos vacíos que se pasan cómo argumentos a la función.   

6. **Generación de Resultados**:

   - Diseña una función **`generar_euromillon`** que actualice dos conjuntos: uno con los números premiados y otro con las estrellas premiadas.

7. **Cálculo de Aciertos**:

   - Implementa una función **`obtener_aciertos`** que compare los números jugados con los números premiados y calcule la cantidad de aciertos.

     La función recibirá ***dos conjuntos***: uno con los elementos seleccionados por el usuario y otro con los premiados y retornará, mediante el
     operador ***"intersección"*** entre conjuntos, el número de elementos comunes entre ambos conjuntos.

     Un ejemplo de llamada de esta función será el siguiente:

     ```python
     aciertos_numeros = obtener_aciertos(numeros, numeros_premiados)
     ```

     La ejecución de este código retornará el número de aciertos, es decir, la cantidad de números comunes entre los dos conjuntos.

8. **Visualización de Resultados**:

   - Diseña una función ***`mostrar_resultados`*** que limpie la pantalla y muestre:
     - Los números premiados.
     - Las estrellas premiadas.
     - Los números jugados.
     - Las estrellas jugadas.
     - La cantidad de aciertos en números y estrellas.

     La ejecución de esta función mostrará los siguiente:

     ```
     RESULTADOS DEL EUROMILLÓN
     -------------------------


     Números premiados = [19, 25, 37, 39, 40]
     Estrellas premiadas = [2, 3]
     Números jugados = [5, 8, 11, 23, 41]
     Estrellas jugadas = [7, 9]


     Total de números acertados = 0
     Total de estrellas acertadas = 0
     ```   

### Paso 3: Crear la Función `main` ###

- Llama a las funciones en el orden correcto para implementar el flujo del programa:

1. Limpia la pantalla.
2. Pregunta al jugador cuántos números y estrellas quiere jugar.
3. Solicita los números y estrellas al jugador.
4. Genera los números y estrellas premiadas.
5. Realiza una pausa con el mensaje "Presiones ENTER para continuar...".
6. Muestra los resultados del sorteo.

### Paso 4: Prueba el Programa ###
- Ejecuta el programa y verifica que se cumplan los requisitos indicados.

---

## Ejemplo de Ejecución

1. **Inicio del Juego**:
   ```
   JUEGA AL EUROMILLÓN
   -------------------

   Total de números a jugar (5-10)? >> 6
   Total de estrellas a jugar (2-4)? >> 3

   ### Seleccione 6 números del 1 al 50 ###
   Dame el número #1#>> 10
   Dame el número #2#>> 25
   Dame el número #3#>> 50
   Dame el número #4#>> 12
   Dame el número #5#>> 8
   Dame el número #6#>> 30
   [8, 10, 12, 25, 30, 50]

   ### Seleccione 3 estrellas del 1 al 12 ###
   Dame la estrella #1#>> 2
   Dame la estrella #2#>> 8
   Dame la estrella #3#>> 12
   [2, 8, 12]

   Presione ENTER para continuar...
   ```

2. **Resultados**:
   ```
   RESULTADOS DEL EUROMILLÓN
   -------------------------

   Números premiados = [3, 8, 10, 25, 40]
   Estrellas premiadas = [2, 11]

   Números jugados = [8, 10, 12, 25, 30, 50]
   Estrellas jugadas = [2, 8, 12]

   Total de números acertados = 3
   Total de estrellas acertadas = 1
   ```
