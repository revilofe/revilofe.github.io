---
title: "UD 3 - P5: XML"
summary: XML
description: XML
authors:
    - Diego Cano
date: 2024-10-24
icon: "material/file-document-edit"
permalink: /prog/unidad3/p3.5
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - XML
---
## P3.5 - Práctica de XML

### **1. Manejo de Archivos XML**

Completa el código del ejemplo ***"Gestión de usuarios"*** para ampliar la funcionalidad del programa implementando las siguientes funciones: 

1. `mostrar_datos`: que mostrará de forma organizada el contenido del archivo XML.

2. `inicializar_datos`: que copiará el contenido del archivo origen (`datos_usuarios_orig.xml`) a otro archivo destino (`datos_usuarios.xml`).

3. `crear_arbol`: que generará un nuevo árbol XML vacío con un nodo raíz especificado, permitiendo inicializar un archivo XML en caso de que no exista o esté corrupto.

Al finalizar la actividad, deberás integrar estas funciones en el programa principal (`main`) y probarlas en diferentes escenarios.

---

#### **Instrucciones**

1. **Preparar el Entorno**:

   - Asegúrate de tener los archivos `datos_usuarios_orig.xml` y `datos_usuarios.xml` en el mismo directorio que tu código.

   - Si no existe, crea el archivo `datos_usuarios_orig.xml` con el siguiente contenido inicial:

   ```xml
   <usuarios>
       <usuario>
           <id>1</id>
           <nombre>Juan</nombre>
           <edad>30</edad>
       </usuario>
       <usuario>
           <id>2</id>
           <nombre>Ana</nombre>
           <edad>25</edad>
       </usuario>
   </usuarios>
   ```

   Con esta modificación que vas a realizar en el programa, el archivo `datos_usuarios.xml` puede estar vacío o no existir al comenzar.

2. **Implementar la Función `mostrar_datos`**:

   - Crea una función llamada `mostrar_datos` que reciba la raíz del árbol XML y muestre su contenido de forma organizada en consola.

   - La función debe:
   
     - Imprimir los datos de cada usuario con el formato: `ID: <id>, Nombre: <nombre>, Edad: <edad>`.

     - Mostrar un mensaje si no hay usuarios en el archivo.

   - Ejemplo de salida si el archivo contiene datos:

     ```
     --- Contenido Actual del XML ---
     ID: 1, Nombre: Juan, Edad: 30
     ID: 2, Nombre: Ana, Edad: 25
     --- Fin del Contenido ---
     ```

3. **Implementar la Función `inicializar_datos`**:

   - Crea una función llamada `inicializar_datos` que copie el contenido de `datos_usuarios_orig.xml` a `datos_usuarios.xml`.

   - La función debe manejar los siguientes errores:
   
     - El archivo origen no existe.

     - El archivo origen tiene un formato XML inválido.

   - Si la copia es exitosa, debe mostrar el mensaje:
   
     ```
     Datos inicializados desde 'datos_usuarios_orig.xml' a 'datos_usuarios.xml'.
     ```

4. **Implementar la Función `crear_arbol`**:

   - Crea una función llamada `crear_arbol` que reciba el nombre del nodo raíz y genere un nuevo árbol XML vacío.

   - La función debe retornar el árbol inicializado.

   - Ejemplo de uso:
   
     ```python
     arbol = crear_arbol("usuarios")
     ```

     Esto creará un árbol XML vacío con un nodo raíz llamado `<usuarios>`.

5. **Modificar la Función `main`**:

   - Asegúrate de que `main` siga este flujo de ejecución:
   
     1. Limpiar la consola.

     2. Ejecutar la función `inicializar_datos` para copiar el contenido inicial.

     3. Cargar los datos desde `datos_usuarios.xml` utilizando la función `cargar_xml`.

     4. Si el archivo no se pudo cargar, utilizar `crear_arbol` para inicializar un nuevo archivo XML vacío.

     5. Mostrar el contenido inicial del archivo XML utilizando `mostrar_datos`.

     6. Realizar una pausa hasta que se pulse una tecla.

     7. Realizar las siguientes operaciones, mostrando los datos al finalizar cada operación y realizando una pausa:
     
        - Actualizar la edad de un usuario.

        - Insertar un nuevo usuario.

        - Eliminar un usuario.

     8. Guardar los datos modificados nuevamente en `datos_usuarios.xml`.

     9. **A tener en cuenta a la hora de implementar el código**: *siempre que se muestran los datos se realiza una pausa*.

6. **Prueba tu Programa**:

   - Asegúrate de que las funciones cumplen con lo esperado en estos escenarios:
   
     - `datos_usuarios_orig.xml` no existe ("*ERROR* El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")

     - `datos_usuarios_orig.xml` tiene un formato inválido ("*ERROR* El archivo origen '{archivo_origen}' tiene un formato XML inválido.")

     - `datos_usuarios.xml` no contiene usuarios ("*ERROR* No hay usuarios en el archivo XML.")

---

### **Salida esperada del programa**

```python
Datos inicializados desde 'src/otros/datos_usuarios_orig.xml' a 'src/otros/datos_usuarios.xml'.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---

Presione una tecla para continuar . . .

Usuario con ID 1 actualizado.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 31
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Usuario Pedro añadido con éxito.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 31
ID: 2, Nombre: Ana, Edad: 25
ID: 3, Nombre: Pedro, Edad: 40
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Usuario con ID 2 eliminado.

--- Contenido Actual del XML ---
ID: 1, Nombre: Juan, Edad: 31
ID: 3, Nombre: Pedro, Edad: 40
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Operaciones completadas. Archivo actualizado.
```

---

### **Notas Adicionales**

- Utiliza las funciones auxiliares `limpiar_consola` y `pausar` para mejorar la legibilidad en consola.
- En caso de errores, imprime mensajes claros y específicos.
- Asegúrate de probar tu programa en diferentes escenarios para validarlo correctamente.
