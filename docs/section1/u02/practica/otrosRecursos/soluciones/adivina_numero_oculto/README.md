# Prueba de Programación - Juego de "Adivina el Número Oculto"

Este repositorio contiene una prueba práctica para evaluar tus habilidades de programación. Debes completar un programa de consola que permite a un usuario adivinar un número oculto mediante varias pistas. Para realizar esta tarea, utiliza la documentación interna y los comentarios que se encuentran en cada función.

## Objetivo

El objetivo de la prueba es que completes las funciones del programa según las especificaciones y la documentación interna que se te proporciona. Esto incluye manejar errores y seguir las instrucciones precisas para cada sección.

## Estructura del Proyecto

El proyecto contiene las siguientes funciones clave, algunas de las cuales ya están parcialmente desarrolladas o documentadas:

- `limpiar_pantalla()`: Limpia la consola según el sistema operativo.
- `pausa()`: Realiza una pausa en el programa, ya sea por tiempo o esperando a que el usuario presione ENTER.
- `mostrar_titulo(seccion, intentos=0)`: Muestra el título correspondiente a una sección del juego.
- `mostrar_error(msjError)`: Muestra un mensaje de error y pausa la ejecución.
- `evaluar_diferencia(numero, numero_oculto, frio, caliente)`: Evalúa la distancia entre el número ingresado y el oculto y retorna un código numérico.
- `obtener_pista(numero, numero_oculto, intentos, frio, caliente)`: Proporciona una pista sobre si el número está "Frío", "Caliente" o "Te Quemas" y si el número oculto es mayor o menor.
- `pedir_numero_usuario(mensaje, minimo=None, maximo=None)`: Solicita al usuario un número entero válido.
- `adivina_el_numero(numero_oculto, total_intentos, minimo, maximo, frio, caliente)`: Gestiona el proceso de adivinación permitiendo al usuario ingresar números.
- `configurar_rangos_numeros()`, `configurar_pistas(minimo, maximo)`, `configurar_intentos(rango_numero_oculto)`: Configuran los parámetros del juego.
- `configurar_juego()`: Configura todos los parámetros del juego de una vez.
- `mostrar_configuracion()`, `mostrar_menu()`, `comprobar_opcion()`, `elegir_opcion_menu()`: Funciones para mostrar y gestionar el menú del juego.
- `jugar(numero_oculto, intentos, frio, caliente)`: Ejecuta el proceso completo del juego y muestra los resultados al finalizar.
- `genera_numero_oculto()`: Genera el número oculto a adivinar.
- `main()`: Función principal que organiza el flujo completo del programa.

## Instrucciones para Completar la Prueba

1. **Documentación y Comentarios**:
   - Cada función incluye documentación interna (`docstrings`) que describe los parámetros, el valor de retorno y notas adicionales sobre su funcionamiento.
   - Lee los `docstrings` cuidadosamente para entender qué debe hacer cada función.
   - Algunos comentarios indican líneas específicas o pasos que debes completar.

2. **Uso de la Función `mostrar_error()`**:
   - No uses `print()` directamente para mostrar errores. En su lugar, usa la función `mostrar_error()` que ya está definida para este propósito.

3. **Funciones Clave para Completar**:
   - Las funciones `limpiar_pantalla()`, `pausa()`, `mostrar_titulo()`, `evaluar_diferencia()`, `obtener_pista()`, `adivina_el_numero()`, y `configurar_*()` tienen tareas específicas que debes desarrollar.
   - Sigue las instrucciones en los comentarios y ajusta cada función según las especificaciones.

4. **Pruebas y Validaciones**:
   - Asegúrate de que cada función cumple con su propósito y realiza pruebas para verificar que funcionan correctamente.
   - Las funciones deben manejar errores y restricciones tal como se indica en sus descripciones (por ejemplo, valores fuera del rango permitido).

5. **Sigue las Convenciones**:
   - Mantén el estilo y la estructura del código de acuerdo a lo ya proporcionado.
   - Usa variables y estructuras de control claras para facilitar la lectura y el mantenimiento del código.

## Recomendaciones

- **Prueba paso a paso**: Ejecuta el programa después de completar cada función para verificar que el flujo general es correcto.
- **Observa los detalles**: Los mensajes de salida deben coincidir exactamente con lo que se pide en la documentación.
- **Evita modificar las funciones terminadas**: Algunas funciones, como `pedir_numero_usuario`, ya están completas y no deben cambiarse.

## Ejecución del Programa

Para ejecutar el programa en tu terminal, asegúrate de tener Python instalado y luego ejecuta:

```bash
python main.py
