---
title: "UD 3 - P4: JSON"
summary: JSON
description: JSON
authors:
    - Diego Cano
date: 2024-10-24
icon: 
permalink: /prog/unidad3/p3.4
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - JSON
---
## P3.4 - Práctica de JSON

### **1. Manejo de Archivos JSON**

Completa el código del ejemplo ***"Gestión de usuarios"*** para ampliar la funcionalidad del programa implementando las siguientes funciones: 

1. `mostrar_datos`: que mostrará de forma organizada el contenido del archivo JSON.

2. `inicializar_datos`: que copiará el contenido del archivo origen (`datos_usuarios_orig.json`) a otro archivo destino (`datos_usuarios.json`).

Al finalizar la actividad, deberás integrar estas funciones en el programa principal (`main`) y probarlas en diferentes escenarios.

#### **Instrucciones**

1. **Preparar el Entorno**:

   - Asegúrate de tener los archivos `datos_usuarios_orig.json` y `datos_usuarios.json` en el mismo directorio que tu código.

   - Si no existe, crea el archivo `datos_usuarios_orig.json` con el siguiente contenido inicial:

   ```json
   {
       "usuarios": [
           {"id": 1, "nombre": "Juan", "edad": 30},
           {"id": 2, "nombre": "Ana", "edad": 25}
       ]
   }
   ```

   Con esta modificación que vas a realizar en el programa, el archivo `datos_usuarios.json` puede estar vacío o no existir al comenzar.

3. **Implementar la Función `mostrar_datos`**:

   - Crea una función llamada `mostrar_datos` que reciba un diccionario y muestre su contenido de forma organizada en consola.

   - La función debe:
   
     - Imprimir los datos de cada usuario con el formato: `ID: <id>, Nombre: <nombre>, Edad: <edad>`.

     - Mostrar un mensaje si no hay usuarios en el archivo.

   - Ejemplo de salida si el archivo contiene datos:

     ```
     --- Contenido Actual del JSON ---
     ID: 1, Nombre: Juan, Edad: 30
     ID: 2, Nombre: Ana, Edad: 25
     --- Fin del Contenido ---
     ```

5. **Implementar la Función `inicializar_datos`**:

   - Crea una función llamada `inicializar_datos` que copie el contenido de `datos_orig.json` a `datos.json`.

   - La función debe manejar los siguientes errores:
   
     - El archivo origen no existe.

     - El archivo origen tiene un formato JSON inválido.

   - Si la copia es exitosa, debe mostrar el mensaje:
   
     ```
     Datos inicializados desde 'datos_usuarios_orig.json' a 'datos_usuarios.json'.
     ```

7. **Modificar la Función `main`**:

   - Asegúrate de que `main` siga este flujo de ejecución:
   
     1. Limpiar la consola.

     2. Ejecutar la función `inicializar_datos` para copiar el contenido inicial.

     3. Cargar los datos desde `datos_usuarios.json` utilizando la función `cargar_json`.

     4. Mostrar el contenido inicial del archivo JSON utilizando `mostrar_datos`.

     5. Realizar una pausa hasta que se pulse una tecla.

     6. Realizar las siguientes operaciones, mostrando los datos al finalizar cada operación y realizando una pausa:
     
        - Actualizar la edad de un usuario.

        - Insertar un nuevo usuario.

        - Eliminar un usuario.

     8. Guardar los datos modificados nuevamente en `datos_usuarios.json`.

     9. A tener en cuenta a la hora de implementar el código, *siempre que se muestran los datos se realiza una pausa*.

8. **Prueba tu Programa**:

   - Asegúrate de que las funciones cumplen con lo esperado en estos escenarios:
   
     - `datos_usuarios_orig.json` no existe ("*ERROR* El archivo origen '{archivo_origen}' no existe. No se realizó la copia.")

     - `datos_usuarios_orig.json` tiene un formato inválido ("*ERROR* El archivo origen '{archivo_origen}' tiene un formato JSON inválido.")

     - `datos_usuarios.json` no contiene usuarios ("*ERROR* El archivo JSON no contiene usuarios!")

10. **Salida esperada del programa**:

```python
Datos inicializados desde 'src/otros/datos_usuarios_orig.json' a 'src/otros/datos_usuarios.json'.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 30
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---

Presione una tecla para continuar . . .

Usuario con ID 1 actualizado.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 31
ID: 2, Nombre: Ana, Edad: 25
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Usuario Pedro añadido con éxito.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 31
ID: 2, Nombre: Ana, Edad: 25
ID: 3, Nombre: Pedro, Edad: 40
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Usuario con ID 2 eliminado.

--- Contenido Actual del JSON ---
ID: 1, Nombre: Juan, Edad: 31
ID: 3, Nombre: Pedro, Edad: 40
--- Fin del Contenido ---

Presione una tecla para continuar . . . 

Operaciones completadas. Archivo actualizado.
```

#### **Notas Adicionales**

- Utiliza las funciones auxiliares `limpiar_consola` y `pausar` para mejorar la legibilidad en consola.
- En caso de errores, imprime mensajes claros y específicos.
- Asegúrate de probar tu programa en diferentes escenarios para validarlo correctamente.
