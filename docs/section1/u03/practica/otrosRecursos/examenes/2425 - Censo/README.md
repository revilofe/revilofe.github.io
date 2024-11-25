## **Análisis de datos en un censo**

### **Contexto:**

Se ha proporcionado un archivo **JSON** que contiene información de un censo de una población. Cada registro tiene los siguientes campos:

- **Nombre**: Nombre de la persona.
- **Edad**: Edad de la persona.
- **Ciudad**: Ciudad donde vive.
- **Profesión**: Profesión de la persona.

El objetivo es trabajar con estos datos en memoria y generar estadísticas útiles sobre ellos, utilizando las estructuras de datos y funcionalidades avanzadas de Python como **conjuntos** y **diccionarios**.

### **Tareas:**

1. **Crear la función `cargar_datos()`**:
   - Debe recibir como argumento la ruta a un archivo JSON y cargar los datos en memoria.
   - El archivo JSON contiene una lista de personas.
   - Si ocurre algún error al leer el archivo, debe mostrar un mensaje de error adecuado.

2. **Crear la función `generar_estadistica()`**:
   - Debe recibir como argumento la estructura de datos cargada y realizar las siguientes tareas:
     - Listar todas las **ciudades únicas** registradas en el censo.
     - Contar cuántas personas tienen cada **profesión**.
     - Agrupar a las personas que tienen la misma edad, mostrando el grupo de nombres por edad.
     - Permitir buscar personas por ciudad, devolviendo un conjunto con los nombres de las personas que viven en dicha ciudad.
   - La función debe mostrar los resultados de estas operaciones.

### **Formato esperado de salida:**

**Ejemplo de estadísticas generadas:**

1. **Ciudades únicas**:  
   `{"Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao"}`

2. **Número de personas por profesión**:  
   ```python
   {
       "Ingeniero": 4,
       "Médico": 3,
       "Abogado": 2,
       "Profesor": 5
   }
   ```

3. **Personas agrupadas por edad**:  
   ```python
   {
       25: {"Juan", "Pedro"},
       30: {"Ana", "Luis"},
       40: {"Carmen", "Jose"}
   }
   ```

4. **Búsqueda por ciudad**:  
   - Ciudad: `"Madrid"`
   - Resultado: `{"Juan", "Carmen", "Luis"}`

### **Estructura del archivo JSON:**

Nombre del archivo: `agenda.json`

```json
[
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"},
    {"nombre": "Ana", "edad": 30, "ciudad": "Barcelona", "profesion": "Médico"},
    {"nombre": "Pedro", "edad": 25, "ciudad": "Madrid", "profesion": "Profesor"},
    {"nombre": "Luis", "edad": 30, "ciudad": "Valencia", "profesion": "Abogado"},
    {"nombre": "Carmen", "edad": 40, "ciudad": "Madrid", "profesion": "Médico"},
    {"nombre": "Jose", "edad": 40, "ciudad": "Bilbao", "profesion": "Ingeniero"},
    {"nombre": "Maria", "edad": 22, "ciudad": "Sevilla", "profesion": "Ingeniero"},
    {"nombre": "Pablo", "edad": 35, "ciudad": "Bilbao", "profesion": "Profesor"},
    {"nombre": "Eva", "edad": 28, "ciudad": "Barcelona", "profesion": "Médico"},
    {"nombre": "Raul", "edad": 22, "ciudad": "Valencia", "profesion": "Profesor"},
    {"nombre": "Laura", "edad": 30, "ciudad": "Sevilla", "profesion": "Ingeniero"},
    {"nombre": "Elena", "edad": 40, "ciudad": "Madrid", "profesion": "Abogado"},
    {"nombre": "Alberto", "edad": 33, "ciudad": "Bilbao", "profesion": "Profesor"},
    {"nombre": "Sara", "edad": 28, "ciudad": "Barcelona", "profesion": "Ingeniero"},
    {"nombre": "Victor", "edad": 35, "ciudad": "Sevilla", "profesion": "Profesor"},
    {"nombre": "Julia", "edad": 30, "ciudad": "Valencia", "profesion": "Ingeniero"},
    {"nombre": "David", "edad": 40, "ciudad": "Madrid", "profesion": "Profesor"},
    {"nombre": "Lucia", "edad": 22, "ciudad": "Bilbao", "profesion": "Ingeniero"},
    {"nombre": "Irene", "edad": 35, "ciudad": "Sevilla", "profesion": "Médico"},
    {"nombre": "Manuel", "edad": 28, "ciudad": "Barcelona", "profesion": "Profesor"}
]
```

### **IMPORTANTE:**
- Modulariza tu código creando las funciones solicitadas y un ejemplo de su funcionamiento en el main.
- Utiliza **conjuntos** para las ciudades únicas y los nombres por edad.
- Usa **diccionarios** para contar las profesiones y agrupar a las personas por edad.
- Documenta y Comenta, si es necesario, claramente tu código para explicar lo que hace cada parte.
