## **Prueba Práctica 01: Matriz Ordenada**

En esta práctica trabajarás con **matrices** en Python, diseñando un programa modular que permita al usuario crear, ordenar y mostrar matrices. Además, guardarás la configuración y los resultados en un fichero **JSON** para consolidar el manejo de estructuras avanzadas.

Tu programa deberá utilizar un **diccionario** para almacenar la configuración del programa, como los límites de las dimensiones de la matriz, los valores permitidos y el formato de salida de los números. Esta configuración debe ser consultada a lo largo del programa, en lugar de usar valores codificados directamente.

### **Tareas a realizar**

1. **Definir las dimensiones de la matriz:**
   - Solicita al usuario las dimensiones de la matriz.
   - Las dimensiones deben cumplir con un límite mínimo y máximo definido en el diccionario de configuración.

   **Ejemplo:**
   ```
   Dime las dimensiones de la matriz...
   Filas >> 2
   Columnas >> 2
   ```

2. **Recopilar los elementos de la matriz:**
   - Solicita al usuario que introduzca los elementos de la matriz uno por uno.
   - Los valores deben estar dentro de un rango mínimo y máximo definido en el diccionario de configuración.
   - Almacena los elementos en una estructura que represente la matriz.

   **Ejemplo:**
   ```
   Dame los elementos:
   >> 4.789
   >> -0.8938
   >> -6.8
   >> 3.9987
   ```

3. **Crear y mostrar la matriz original:**
   - Imprime la matriz con un formato que alinee todos los números correctamente.
   - El formato de salida para los valores (tamaño y número de decimales) debe estar definido en el diccionario de configuración.

   **Ejemplo:**
   ```
                         4.79 -0.89
   Matriz 2x2 original: -6.80  4.00
   ```

4. **Ordenar los elementos de la matriz:**
   - Una buena práctica para ordenar los valores de la matriz puede ser extraerlos a una única lista, ordenarlos y reconstruir de nuevo la matriz con los valores ordenados respetando las dimensiones originales.

5. **Mostrar la matriz ordenada:**
   - Imprime la matriz ordenada usando el mismo formato que la original.

   **Ejemplo:**
   ```
                        -6.80 -0.89
   Matriz 2x2 ordenada:  4.00  4.79
   ```

6. **Guardar en un fichero JSON:**
   - Almacena en un fichero JSON:
     - La configuración del programa.
     - La matriz original.
     - La matriz ordenada.

   - Si el archivo ya existe, debe sobrescribirse.

### **Requisitos adicionales**

1. **Uso de un diccionario:**
   - Define un diccionario de configuración para almacenar:
     - Los límites de las dimensiones de la matriz ***(1 a 10)***.
     - Los valores mínimo y máximo permitidos en la matriz ***(-9.98 a 9.98)***.
     - El formato de salida de los números ***(número de decimales = 2 y tamaño total = 5)***.
   - No uses valores codificados directamente en el programa. Consulta siempre los límites desde el diccionario.

2. **Gestión de errores:**
   - Valida todas las entradas del usuario:
     - Si introduce un valor fuera de rango o no válido, muestra un mensaje de error y vuelve a pedir la entrada.

3. **Modularidad:**
   - Divide tu programa en funciones independientes. Algunas sugerencias:
     - **`pedir_dimensiones`**: Solicita las dimensiones de la matriz al usuario.
     - **`generar_matriz`**: Recopila los valores y genera la matriz.
     - **`ordenar_matriz`**: Ordena los valores y reestructura la matriz.
     - **`mostrar_matriz`**: Muestra cualquier matriz formateada.
     - **`guardar_json`**: Guarda la información en un fichero JSON.

### **Preguntas a responder**

Debes responder a estas preguntas editando este mismo fichero, y debajo de cada una...

1. **¿Por qué es más adecuado usar un diccionario en lugar de una lista para almacenar la configuración del programa?**



2. **¿Cuándo utilizarías un conjunto y para qué?**. Proporciona un ejemplo de cualquiera de los 3 ejercicios que has realizado.



3. **¿Sería más adecuado almacenar la información de la matriz en una tupla de tuplas? Responde "Sí" o "No" y razona tu respuesta.**



