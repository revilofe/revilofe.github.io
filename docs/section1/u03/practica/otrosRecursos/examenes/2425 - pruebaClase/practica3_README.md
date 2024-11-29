## **Prueba Práctica 03: Gestión de Tareas**

En esta práctica, implementarás funciones para gestionar una lista de tareas predefinidas. El programa contará con un menú interactivo que permitirá:

1. **Filtrar tareas**: Seleccionar solo las tareas con un estado específico.
2. **Mostrar todas las tareas**: Listar todas las tareas en formato legible.
3. **Mostrar la siguiente tarea**: Recorrer las tareas (filtradas o completas) secuencialmente con un iterador.
4. **Salir**: Finalizar el programa.

### **Detalles Técnicos**

#### **1. Lista de Tareas**
Se proporciona la función `crear_tareas_ejemplo()` que genera una lista predefinida de tareas con los siguientes atributos:
- `ID`: Número único de identificación.
- `Descripción`: Texto breve que describe la tarea.
- `Estado`: Estado actual de la tarea (`Pendiente`, `En Proceso`, `Completada`).

#### **2. Menú**
El programa debe implementar las siguientes opciones:
- **Opción 1: Filtrar tareas**
  - Solicita al usuario un estado (`Pendiente`, `En Proceso`, `Completada`) o presiona ENTER para eliminar el filtro.
  - Filtra las tareas según el estado introducido.
  - Reinicia el iterador con las tareas filtradas.

- **Opción 2: Mostrar todas las tareas**
  - Utiliza una función para generar una cadena con todas las tareas formateadas.
  - **Restricción**: Esta función debe utilizar `join`.

- **Opción 3: Mostrar la siguiente tarea**
  - Muestra la siguiente tarea del iterador. Si no hay más tareas, reinicia el iterador y lo notifica.
  - **Restricción**: Implementa el recorrido con el iterador y el método `next()`.

- **Opción 4: Salir**
  - Finaliza el programa.

### **Tareas a realizar:**

Se te proporciona un esqueleto del programa, con algunas funciones ya terminadas. Pero debes completar las siguientes:

1. **`obtener_tareas`**
   - Toma una lista de tareas y retorna una cadena con todas las tareas en formato:
     ```
     ID: 1, Descripción: Estudiar Python, Estado: Pendiente
     ID: 2, Descripción: Terminar proyecto, Estado: En Proceso
     ...
     ```
   - **Obligatorio**: Usa `join` para separar las tareas en diferentes líneas.

2. **`mostrar_tarea`**
   - Recibe un diccionario que representa una tarea y la muestra en formato:
     ```
     ID: 1, Descripción: Estudiar Python, Estado: Pendiente
     ```

3. **`filtrar_tareas_por_estado`**
   - Recibe una lista de tareas y un estado, y retorna una tupla con las tareas que coinciden.

4. **`main` Lógica de Filtrado (Opción 1 del Menú)**
   - Filtra las tareas por estado si el usuario introduce un estado válido. Si no introduce nada, elimina el filtro.
   - Reinicia el iterador con la nueva lista de tareas.

5. **`main` Lógica de Mostrar Tareas (Opción 2 del Menú)**
   - Utiliza `obtener_tareas` para mostrar todas las tareas en formato legible.

6. **`main` Lógica de Mostrar Siguiente Tarea (Opción 3 del Menú)**
   - Muestra la siguiente tarea del iterador. Si no hay más tareas, reinicia el iterador e informa al usuario.

### **Ejemplo de Ejecución**

#### **Menú Principal**
```
Menú:
----
1. Filtrar tareas 
2. Mostrar todas las tareas
3. Mostrar siguiente tarea
4. Salir
Elige una opción:
```

#### **Opción 1: Filtrar tareas**
- **Input**: en proceso
- **Resultado**: Filtra las tareas por el estado `En Proceso`. Las tareas filtradas serán:

  ```
  ID: 2, Descripción: Terminar proyecto, Estado: En Proceso
  ID: 6, Descripción: Actualizar currículum, Estado: En Proceso
  
  Presione una tecla para continuar . . . 
  ```

#### **Opción 2: Mostrar todas las tareas**

```
ID: 1, Descripción: Estudiar Python, Estado: Pendiente
ID: 2, Descripción: Terminar proyecto, Estado: En Proceso
ID: 3, Descripción: Revisar correos, Estado: Completada
ID: 4, Descripción: Planificar reunión, Estado: Pendiente
ID: 5, Descripción: Comprar libros, Estado: Pendiente
ID: 6, Descripción: Actualizar currículum, Estado: En Proceso
ID: 7, Descripción: Organizar escritorio, Estado: Completada
ID: 8, Descripción: Preparar presentación, Estado: Pendiente   

Presione una tecla para continuar . . . 
```

#### **Opción 3: Mostrar siguiente tarea**
- **Primera vez**:

  ```
  Siguiente tarea:
  ID: 1, Descripción: Estudiar Python, Estado: Pendiente
  
  Presione una tecla para continuar . . . 
  ```

- **Si no existen más tareas**:

  ```
  No hay más tareas! Se ha reiniciado el iterador...

  Presione una tecla para continuar . . . 
  ```
