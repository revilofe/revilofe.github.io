## **Prueba Práctica 02: Análisis de datos en un censo**

### **Contexto:**

Se ha proporcionado un archivo **JSON** que contiene información de un censo de una población. Cada registro tiene los siguientes campos:

- **Nombre**: Nombre de la persona.
- **Edad**: Edad de la persona.
- **Ciudad**: Ciudad donde vive.
- **Profesión**: Profesión de la persona.

El objetivo es trabajar con estos datos en memoria y generar estadísticas útiles sobre ellos, utilizando las estructuras de datos y funcionalidades avanzadas de Python como **conjuntos** y **diccionarios**.

### **Tareas a realizar**

Deberás completar las funciones siguientes:

#### **1. `cargar_datos()`**

Realiza la carga de los datos *(censo_info.json)* en una estructura de datos adecuada, manejando los posibles errores que se puedan producir.

#### **2. `obtener_ciudades_unicas()`**

- **Entrada:** Recibe la lista de datos cargados.
- **Salida:** Devuelve un conjunto con las ciudades únicas registradas en el censo.
- **Ejemplo de salida:** `{"Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao"}`

#### **3. `contar_profesiones()`**

- **Entrada:** Recibe la lista de datos cargados.
- **Salida:** Devuelve un diccionario con las profesiones como claves y la cantidad de personas que las ejercen como valores.
- **Ejemplo de salida:**

    ```python
    {
        "Ingeniero": 4,
        "Médico": 3,
        "Abogado": 2,
        "Profesor": 5
    }
    ```

#### **4. `agrupar_personas_por_edad()`**

- **Entrada:** Recibe la lista de datos cargados.
- **Salida:** Devuelve un diccionario en el que:
  - Las claves son las edades.
  - Los valores son conjuntos con los nombres de las personas de esa edad.
- **Ejemplo de salida:**

    ```python
    {
        25: {"Juan", "Pedro"},
        30: {"Ana", "Luis"},
        40: {"Carmen", "Jose"}
    }
    ```

#### **5. Crear la función `buscar_personas_por_ciudad()`**

- **Entrada:** Recibe la lista de datos cargados y una ciudad.
- **Salida:** Devuelve un conjunto con los nombres de las personas que viven en esa ciudad.
- **Ejemplo de salida:** Si la ciudad es `"Madrid"`: `{"Juan", "Carmen", "Luis"}`

#### **6. `mostrar_estadisticas()`**

- **Entrada:** Recibe la lista de datos cargados.
- **Requisitos:**
  - Invocar las funciones creadas anteriormente y mostrar los resultados de cada una:
    1. **Ciudades únicas.** (ordenadas alfabéticamente)
    2. **Número de personas por profesión.**
    3. **Personas agrupadas por edad.**
    4. **Búsqueda por ciudad**:
       - Solicitar al usuario una ciudad para buscar personas.
       - Mostrar los nombres de las personas que viven allí o indicar que no hay resultados.

### **Ejemplo de salida del programa:**

Al ejecutar el programa, debe cargar los datos del archivo y generar las estadísticas solicitadas en el ejercicio, con una salida similar a la siguiente:

```plaintext

1. Ciudades únicas:
   Barcelona, Bilbao, Cádiz, Madrid, Sevilla y Valencia.

2. Número de personas por profesión:

   Abogado: 2
   Estudiante: 1
   Ingeniero: 7
   Médico: 4
   Profesor: 7

3. Personas agrupadas por edad:

   22: Lucia - Raul - Maria.
   25: Pedro - Juan.
   28: Eva - Sara - Manuel.
   30: Julia - Luis - Ana - Laura.
   33: Juani - Alberto.
   35: Irene - Victor - Pablo.
   40: Jose - Elena - David - Carmen.

Introduce una ciudad para buscar personas: Cádiz

4. Personas en Cádiz:
   Ana
   Juani
   Manuel
   Sara

```

### **Pautas importantes:**

1. **Modularización del código:**
   - Implementa las funciones descritas y las que necesites o veas necesarias para implementar tu solución.
   - Evita escribir toda la lógica en la función `main()`.

2. **Errores y excepciones:**
   - Asegúrate de manejar correctamente los errores al leer el archivo JSON.

3. **Ejemplo del archivo JSON:**
   Utiliza el archivo proporcionado en el enunciado como entrada para probar tu programa.

4. **Descripción del formato de salida de cada apartado:** 

- La lista de ciudades está ordenada alfabéticamente a la hora de mostrarse. Ademá, si no hay ciudades debe mostrar "No existen!", si solo hubiera una ciudad debe mostrar por ejemplo "Cádiz.". Por último, si hay más de una ciudad las debe mostrar como en el ejemplo.

- El número de personas por profesión debe mostrarse ordenadas alfabéticamente por la clave. Para hacer esto de forma más sencilla, podéis crear un nuevo diccionario con las claves ordenadas del diccionario original.

- Las personas agrupadas por edad también deben aparecer por las claves ordenadas y con el separador " - " entre los nombres, finalizando cada línea con un punto (".").

- Las personas de una ciudad deben aparecer de forma ordenada alfabéticamente en líneas diferentes.
