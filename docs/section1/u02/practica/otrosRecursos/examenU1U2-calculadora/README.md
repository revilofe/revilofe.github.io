# Actividad: **Práctica Calculadora Básica en Python**

**ID actividad:** PROG-2425-PRUEBA-U1-U2

**Agrupamiento de la actividad**: Individual

---

### Descripción:

La actividad consiste en completar y corregir el desarrollo de una calculadora "algo especial" en Python, aplicando los conceptos estudiados en las Unidades 1 y 2. El código que debéis analizar y modificar está en "src/calculadora_alumnos.py". También existe una copia que no debéis modificar, "src/calculadora_alumnos_original.py", es un backup del programa, por si realizáis muchos cambios y necesitáis consultar el problema que se os propuso originalmente.

La calculadora permitirá realizar operaciones aritméticas básicas y deberá cumplir con el principio de "Separación de Responsabilidades" (SRP). Debéis leer y analizar el código provisto, corregir errores y desarrollar las partes incompletas, asegurando la gestión de excepciones.

### Objetivo:

- Leer y analizar la documentación del código para comprender su funcionamiento y aplicar correcciones o completar las partes faltantes de la aplicación.
- Planificar y desarrollar un programa interactivo en Python, estructurando las funciones de manera que cada una tenga una única responsabilidad.
- Aplicar estructuras de control condicional y bucles para resolver problemas de forma eficiente.
- Implementar el manejo de excepciones para asegurar el correcto funcionamiento del programa y prevenir errores en su ejecución.
- Ejecutar pruebas unitarias para validar el comportamiento de las funciones, comprobando que cumplen con los requerimientos establecidos.
- Depurar y revisar el código para mejorar su claridad, consistencia y funcionalidad, y asegurar una documentación adecuada.

### Trabajo a realizar:

1. **Completar las funciones** siguientes, aplicando la documentación y estructura indicadas en el código inicial:
   - **limpiar_pantalla()**: Debe limpiar la pantalla según el sistema operativo.
   - **pausa()**: Pausar la ejecución con un mensaje.
   - **mostrar_error()**: Muestra errores específicos gestionando `IndexError` y otras excepciones.
   - **es_resultado_negativo()**: Verifica si el resultado de la operación debe ser negativo.
   - **multiplicar()** y **dividir()**: Realizan operaciones usando solo sumas y restas.
   - **potencia()**: Calcula el exponente de un número usando multiplicaciones sucesivas. Soporta los operadores `**` y `exp`.
   - **calcular_operacion()**: Llama a las funciones específicas para realizar las operaciones aritméticas.
   - **realizar_calculo()**: Permite realizar operaciones en secuencia, capturando números y operadores del usuario.
   - **sumar()** y **restar()**: Desarrollo completo con documentación para funciones que reciben dos números `float` y devuelven el resultado de la suma o resta de estos.
   - **test para la función es_resultado_negativo()**: Crear las pruebas unitarias para comprobar el buen funcionamiento de la función `es_resultado_negativo()`.

2. **Organización del Código y Documentación**:
   - Todos los programas deben tener la función `main()` para organizar el flujo del programa.
   - Utilizar `DocStrings` para documentar cada función. Puedes usar el formato que prefieras (Google, reStructuredText, NumPy, o Epytext).

3. **Organización del Repositorio en GitHub**:
   - Los archivos de código se encuentran ubicados en la carpeta `src`.
   - Las pruebas unitarias están en la carpeta `tests`.

4. **Pruebas Unitarias**:
   - Ejecutar pruebas unitarias para verificar el correcto funcionamiento de las funciones **realizar_calculo()**, **multiplicar()**, **dividir()**, **potencia()**, y **es_resultado_negativo()**.

5. **IMPORTANTE: Aclaraciones sobre las operaciones de Multiplicar, Dividir y Potencia**:

   - ***No será posible la utilización de los operadores de Python para multiplicar, dividir o realizar la exponenciación de un número***. Deben ser cálculos realizados con **sumas y restas EXCLUSIVAMENTE**.

   - Habrá que ***tener en cuenta el signo*** de los números con los que se realiza el cálculo para proporcionar un resultado final correcto.

   - Las funciones recibirán argumentos de tipo float, pero ***trabajarán internamente con los números convertidos a enteros***, previamente realizando un **redondeo**:
   
       * Si recibe un número de 6.78, pasará a ser 7 para realizar los cálculos.
       * Si recibe un número de 1.48, pasará a ser 1 para realizar los cálculos.

   - Tras lo comentado anteriormente, remarcar que las 3 funciones ***reciben argumentos tipo `float`***, trabajan internamente solo con tipos `int` y ***retornan un número tipo `int`***.

   - Para la potencia, como premisa de funcionamiento para simplificar la programación, aunque lejos de la realidad matemática, ***si recibe un exponente negativo, el resultado será 0***.

   - También cabe destacar que ***cualquier número elevado a 0 dará como resultado 1***.

   - Ejemplo de cálculo de multiplicaciones:
       
       * 17.88 x 3.44 => 18 x 3 => 18 + 18 + 18 = **54**
       * 4.77 x -125.09 => 5 x -125 => - (125 + 125 + 125 + 125 + 125) = **-625** (cuidado con el signo que previamente debéis gestionarlo)
   - Para realizar las divisiones, debemos ir restando el dividendo por el divisor, mientras el resultado sea mayor que el dividendo:
   
       * 25.77 : 6.02 => 26 : 6 => 26 - 6 = 20; 20 - 6 = 14; 14 - 6 = 8; 8 - 6 = 2 => el resultado de la división es **4**.
       * 25.77 : -6.02 => 26 : 6 => 26 - 6 = 20; 20 - 6 = 14; 14 - 6 = 8; 8 - 6 = 2 => el resultado de la división es **-4** (cuidado con el signo que previamente debéis gestionarlo).

   - Para realizar las potencias será OBLIGATORIO el uso de la función multiplicar(), que previamente habréis desarrollado.
       
       * 2.33 ** 3.9996 => 2 ** 4 => 2 * 2 * 2 * 2 = **16**.
       * -2.33 ** 3.9996 => 2 ** 4 => 2 * 2 * 2 * 2 = **-16** (cuidado con el signo que previamente debéis gestionarlo).
       * -2.33 ** 0 => **1**.
       * -2.33 ** -6 => **0**.

7. **BONUS extra** *(opcional)*:
   - *IMPORTANTE*: Este cambio debéis realizarlo en un archivo nuevo que debéis llamar `calculadora_alumnos_bonus.py`.
   - De manera opcional, si termináis todo, podéis modificar el programa para que se muestre un menú, en vez de usar comandos en línea. Por ejemplo:

     ```
     Menú
     1. Realizar un cálculo secuencial.
     2. Lista de operaciones disponibles para el cálculo.
     3. Reiniciar resultado (CE).
     4. Configurar número de decimales.
     5. Salir.
     ```

     La opción 1, entraría en el cálculo secuencial directamente (lo que antes hacíamos mediante el comando `calculo`):

     ```
     ## Ingrese número, operador, 'resultado', 'cancelar' o <ENTER> para finalizar el cálculo ##
   
            (Cálculo = 0.00) >>
     ```

     La opción 2 mostraría las operaciones disponibles (lo que antes ejecutaba el comando `lista`). Pero solo deberá mostrar las operaciones y comandos disponibles dentro del cálculo secuencial (ya que los comandos `calculo`, `ce`, `decimales <N>` y `cadena vacía + <ENTER>` ya estarían integrados en el menú al realizar la modificación que os solicitamos en el BONUS y su lógica anterior debe ser eliminada):

     ```
     Operaciones disponibles:
         + => Suma
         - => Resta
         x o * => Multiplicación
         / o : => División
         ** exp => Potencia
         cancelar => vovler sin actualizar el resultado de la calculadora
         cadena vacía + <ENTER> => volver al menú actualizando el resultado de la calculadora
     ```

     La opción 3 reinicia a 0 el resultado de la calculadora *(lo que hacía anteriormente el comando `ce`)*.

     La opción 4 configura el número de decimales con el que se muestra el RESULTADO almacenado de la calculadora y los cálculos intermedios *(lo que hacía anteriormente el comando `decimales <N>`)*.

     La opción 5 sale de la aplicación *(lo que hacíamos previamente con `cadena vacía + <ENTER>`)*.
---

### Manual de uso de la aplicación explicado con ejemplos

 - [Manual de uso de la calculadora](manual_de_uso_con_ejemplos.md)

---

### Recursos

- [U1: Introducción a la programación en Python](https://revilofe.github.io/section1/u01/).
- [U2: Sentencias condicionales y repetitivas](https://revilofe.github.io/section1/u02/).

---

### Evaluación y calificación

**Conlleva presentación**: SI

---

### Rúbrica de Evaluación:

| **Función**             | **Dificultad (1-5)** | **Descripción de la Dificultad**                                                                          | **0** | **1** | **2** | **3** | **4** | **5** | **Criterios de Evaluación Aplicables**                         |
|-------------------------|----------------------|----------------------------------------------------------------------------------------------------------|-------|-------|-------|-------|-------|-------|----------------------------------------------------------------|
| `limpiar_pantalla`      | 1                    | Desarrollo parcial. Corregir implementación y gestionar las excepciones.                                 |       |       |       |       |       |       |                                                                |
| `pausa`                 | 1                    | Desarrollo completo para pausar el programa con el mensaje `Presione ENTER para continuar...`            |       |       |       |       |       |       |                                                                |
| `mostrar_error`         | 3                    | Corregir errores y completar el código gestionando las excepciones `IndexError` y `Exception`.           |       |       |       |       |       |       | RA3.d, RA3.h                                                   |
| `sumar`                 | 2                    | Desarrollo completo, incluida la documentación; recibe dos números `float` y retorna la suma de ambos.   |       |       |       |       |       |       | RA3.g                                                          |
| `restar`                | 2                    | Desarrollo completo, incluida la documentación; recibe dos números `float` y retorna la resta de ambos.  |       |       |       |       |       |       | RA3.g                                                          |
| `es_resultado_negativo` | 1                    | Desarrollo completo. Verifica si el resultado de una operación debe ser negativo.                        |       |       |       |       |       |       | RA3.g                                                          |
| `multiplicar`           | 5                    | Desarrollo completo. Realiza multiplicación usando sumas sucesivas y ajusta el signo para el resultado.  |       |       |       |       |       |       | RA1.d, RA1.e, RA1.g, RA1.i, RA3.a, RA3.b, RA3.e               |
| `dividir`               | 5                    | Desarrollo completo. Realiza división usando restas sucesivas, maneja excepción división entre cero.     |       |       |       |       |       |       | RA1.d, RA1.e, RA1.g, RA1.i, RA3.a, RA3.b, RA3.e, RA3.h        |
| `potencia`              | 5                    | Desarrollo completo y documentación. Calcula potencias usando multiplicaciones.                          |       |       |       |       |       |       | RA1.d, RA1.e, RA1.g, RA1.i, RA3.a, RA3.b, RA3.e, RA3.g        |
| `pedir_entrada`         | 1                    | Desarrollo parcial para eliminar espacios por delante y por detrás y conversión a minúsculas.            |       |       |       |       |       |       |                                                                |
| `calcular_operacion`    | 3                    | Desarrollo parcial. Realiza operaciones llamando a funciones específicas según el operador.              |       |       |       |       |       |       | RA1.g, RA3.a                                                   |
| `obtener_operaciones`   | 1                    | Desarrollo parcial. Devuelve una cadena con la lista de operaciones disponibles en la calculadora.       |       |       |       |       |       |       |                                                                |
| `realizar_calculo`      | 5                    | Corregir errores y desarrollo parcial. Realiza el cálculo secuencial.                                    |       |       |       |       |       |       | RA1.d, RA1.e, RA1.g, RA3.a, RA3.b, RA3.d, RA3.e               |
| `main`                  | 5                    | Corrige los errores y desarrollo parcial. Organiza el flujo principal del programa.                      |       |       |       |       |       |       | RA1.d, RA1.e, RA1.g, RA3.a, RA3.b, RA3.d, RA3.e               |
| Uso de `mostrar_error`  | 2                    | Corrige los errores y desarrollo parcial. Organiza el flujo principal del programa.                      |       |       |       |       |       |       |                                                                |
| Uso de `return` único   | 3                    | Controla que cada función tenga un único `return` para simplificar el flujo y la legibilidad.            |       |       |       |       |       |       | RA3.c                                                          |
| Uso de `constantes`     | 1                    | Usar adecuadamente las constantes dentro del código.                                                     |       |       |       |       |       |       | RA1.f                                                          |
| Cálculo de `decimales`  | 2                    | Implementar la lógica de actualización de las posiciones decimales del resultado y el cálculo intermedio.|       |       |       |       |       |       | RA1.a, RA3.g                                                   |
| `Pruebas unitarias`     | 5                    | Comprobación del cumplimiento correcto de las pruebas unitarias.                                         |       |       |       |       |       |       | RA3.i                                                          |
| Creación de un `test`   | 2                    | Controla el uso de constantes predefinidas (`MENSAJES_ERROR`, `OPERADORES`) en toda la aplicación.       |       |       |       |       |       |       | RA3.i                                                          |

---

### Condiciones de entrega

> **La entrega tiene que cumplir las condiciones de entrega para poder ser calificada. En caso de no cumplirlas podría calificarse como no entregada.**

- Cumple la fecha y hora de entrega.
- **Entrega en GitHub Classroom**: La actividad se debe entregar utilizando el assignment creado en GitHub Classroom, que está basado en el siguiente repositorio de plantilla: [DAM-DAWB-PROG-2425_Prueba_U1-U2_Calculadora](https://github.com/dcanoIESRafaelAlberti/DAM-DAWB-PROG-2425_Prueba_U1-U2_Calculadora.git).
  - El repositorio ya incluye la estructura base con carpetas como `src` y `tests`. Los estudiantes deben añadir sus soluciones en la carpeta correspondiente.
  - Asegúrate de que el profesor tiene permisos para acceder a tu repositorio. Si no se puede acceder, es equivalente a no haber entregado la actividad.
- **Estructura del repositorio**:
    - **Carpeta `src`**: Contendrá los programas correspondientes a los ejercicios solicitados.
    - **Carpeta `tests`**: Contendrá las pruebas unitarias para verificar el correcto funcionamiento de las soluciones.
    - **Carpeta `.github/workflows`**: No debe eliminarse ni modificarse su contenido.
    - **Fichero `requirements.txt`**: No debe eliminarse ni modificarse su contenido.
- **Id del documento a entregar:** El nombre del repositorio será generado automáticamente por GitHub Classroom, por lo que no es necesario que los estudiantes lo modifiquen.

---

### Ten en cuenta

**Custodia** de tu documentación:

- Es responsabilidad del alumnado la custodia y guarda de los trabajos, documentos, y cualquier otro material que realice durante las prácticas o en clase, por tanto, tendrán que asegurarse que quedan a salvo siempre que abandonen el aula, no siendo responsabilidad del profesorado la perdida de este material.
- Asegúrate de mantener copias seguras en servicios como Google Drive, GitHub, GitLab, Bitbucket, etc.

**Fecha y defensa** de las entregas de prácticas/trabajos/ejercicios:

- Las prácticas tendrán una fecha de entrega clara, **que no se podrá cambiar bajo ninguna circunstancia**. Quedando a elección del profesor posibles excepciones justificadas.
- Como norma general, la entrega consistirá en:
    1. Subida a la plataforma (por defecto) en fecha.
    2. Defensa en clase (si se solicita). Como regla general:
        - Los ejercicios individuales se corregirán en clase delante del profesor, defendiendo el trabajo.
        - Los ejercicios en grupo se podrán presentar en grupo o un componente del grupo de forma aleatoria. El método será elegido por el profesor.Corrección de las actividades. Como regla general:

**Causas para no corregir** una entrega (ejercicio, práctica, examen):

- No se cumplen las condiciones de entrega.
- Se ha detectado la posibilidad de copiado de todo o parte de la prueba. Esto incluye textos (total o parcial) de internet y/o sin hacer referencia a la fuente.
    - **Atención** OJO con Chat GPT, Copilot, etc. -> Asegurate de saber que haces.
- Se entrega fuera de plazo (aunque sean unos segundos).
- En caso de entrega a través de GitHub:
    - Añadir en el archivo `README.md` instrucciones para compilar y ejecutar el código, descripción de la aplicación, autoría y referencias.
- En caso de código:
    - Si el código no compila.
