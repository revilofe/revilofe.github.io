### **Prueba Práctica: Manipulación de Matrices**

**Objetivo:**
En esta práctica, trabajarás con matrices en Python, aprendiendo a manipular y organizar datos almacenados en colecciones avanzadas como listas y diccionarios. Diseñarás un programa modular que permita al usuario crear, ordenar y mostrar matrices siguiendo unos requisitos específicos.

Además, usarás un **diccionario** para almacenar los parámetros requeridos (límites y configuraciones) tanto para las dimensiones de la matriz como para los valores que contendrá.

---

### **Descripción del programa**

El programa debe realizar las siguientes acciones:

1. **Definir las dimensiones de la matriz:**  
   
   - Solicita al usuario las dimensiones de la matriz (filas y columnas), con un mínimo de 1 y un máximo de 10.
   
   - Asegúrate de validar que las dimensiones sean correctas antes de continuar.

   **Ejemplo de entrada del usuario:**  
   
   ```
   Dime las dimensiones de la matriz...
   Filas >> 2
   Columnas >> 2
   ```

2. **Pedir los elementos de la matriz:**  
   
   - Solicita al usuario los elementos de la matriz uno por uno. Los valores deben ser **números flotantes entre -9.98 y 9.98**.
   
   - Usa un bucle para recopilar los valores y almacenarlos en una lista, que luego convertirás en una matriz (lista anidada).

   **Ejemplo de entrada del usuario:**  
   
   ```
   Dame los elementos:
   >> 4.789
   >> -0.8938
   >> -6.8
   >> 3.9987
   ```

3. **Crear la matriz original:**

   - Internamente deberás almacenar los números introducidos en la siguiente estructura de datos, según el ejemplo anterior: ((4.789, -0.8938), (-6.8, 3.9987))

4. **Mostrar la matriz original:**  
   
   - Imprime la matriz con los valores alineados, ocupando un espacio de 6 caracteres, incluidos 2 decimales.  
   
   - Asegúrate de indicar que se trata de la matriz original.

   **Ejemplo de salida:**  
   ```
                         4.79 -0.89
   Matriz 2x2 original: -6.80  4.00
   ```

5. **Ordenar los elementos de la matriz:**  
   
   - Ordena los números de la matriz de menor a mayor.

   - Pista: Una buena estrategia es, primero, extraer todos los elementos de la matriz en una lista. Y luego, ordenar esta lista y distribuir sus elementos nuevamente en filas y columnas convirtiéndolos de nuevo en una matriz de las mismas dimensiones, pero con sus elementos ordenados.

6. **Mostrar la matriz ordenada:**  
   
   - Imprime la nueva matriz ordenada con el mismo formato que la original.

   **Ejemplo de salida:**  
   ```
                        -6.80 -0.89
   Matriz 2x2 ordenada:  4.00  4.79
   ```

---

### **Requisitos adicionales**

1. **Uso de un diccionario:**

   - Debes almacenar los límites de las dimensiones y los valores de la matriz en un diccionario llamado **CONFIG**.

2. **Gestión de errores:**
   
   - Valida todas las entradas del usuario. Si introduce un valor no válido o fuera de rango, muestra un mensaje de error y solicita de nuevo la entrada.

3. **Formato de salida:**

   - Todos los números deben mostrarse con 2 decimales y alineados, ocupando al menos 6 caracteres (esta configuración también debéis incluirla en el diccionario).

4. **Modularidad:**  
   
   - Diseña tu programa dividiendo las tareas en funciones independientes. Por ejemplo:
   
     - **`generar_matriz`**: Para recopilar los elementos del usuario y construir la matriz.
     - **`mostrar_matriz`**: Para mostrar la matriz formateada.
     - **`ordenar_matriz`**: Para ordenar los elementos y reorganizar la matriz.
     - etc. 

---

### **Evaluación**

Tu programa será evaluado según los siguientes criterios:

1. **Correcto manejo de matrices:**

   - La matriz generada debe respetar las dimensiones indicadas por el usuario.
   - Los valores deben estar dentro del rango especificado.
   - La matriz ordenada debe estar correctamente organizada.

2. **Estructura del código:**
   
   - Usa funciones para organizar las tareas del programa.
   - Asegúrate de que las funciones sean específicas y reutilizables.

3. **Gestión de errores:**
   
   - Valida correctamente las entradas del usuario (dimensiones y valores).
   - Los mensajes de error deben ser claros.

4. **Formato de salida:**
   
   - Los números deben estar formateados correctamente (alineados y con 2 decimales).

