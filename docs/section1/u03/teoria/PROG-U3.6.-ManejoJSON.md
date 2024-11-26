---
title: "UD 3 - 3.6 Manejo de JSON"
description: Manejo de JSON
summary: JSON
authors:
    - Diego Cano
date: 2024-11-24
icon: 
permalink: /prog/unidad3/3.5
categories:
    - PROG
tags:
    - Software
    - JSON
---

## 3.6. JSON

Los archivos JSON *(JavaScript Object Notation)* son un formato de datos ligero utilizado para intercambiar información de manera sencilla. 
En Python, se gestionan principalmente con el módulo integrado `json`, que permite leer, escribir y manipular datos JSON de forma sencilla.

---

### 1. Conceptos básicos de JSON

Un archivo JSON está estructurado en pares clave-valor, similar a un diccionario de Python. Puede contener objetos *(estructuras anidadas)* y listas.

Ejemplo de JSON, nombre del archivo: `datos.json`
:
```json
{
    "nombre": "Juan",
    "edad": 30,
    "habilidades": ["Python", "JavaScript"],
    "activo": true
}
```

---

### 2. JSON en Python

#### 2.1. Importar el módulo `json`

El módulo `json` está disponible en la biblioteca estándar de Python, por lo que no necesitamos instalar nada adicional.

```python
import json
```

#### 2.2. Leer archivos JSON

##### **2.2.1. Leer JSON desde un archivo**

Se usa `json.load()` para convertir el contenido del archivo JSON en un objeto de Python *(normalmente un diccionario o una lista)*.

Ejemplo:

```python
import json

# Leer el archivo JSON
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

# Acceder a los datos
print(datos["nombre"])  # Ejemplo: 'Juan'
```

##### **2.2.2. Leer JSON desde una cadena de caracteres**

Para leer JSON desde una cadena, se usa `json.loads()`.

Ejemplo:

```python
import json

cadena_json = '{"nombre": "Juan", "edad": 30}'
datos = json.loads(cadena_json)

print(datos["edad"])  # 30
```

#### 2.3. Escribir archivos JSON

##### **2.3.1. Escribir JSON en un archivo**

Se usa `json.dump()` para convertir un objeto de Python a JSON y escribirlo en un archivo.

Ejemplo:

```python
import json

datos = {
    "nombre": "Ana",
    "edad": 25,
    "habilidades": ["HTML", "CSS"],
    "activo": False
}

# Escribir datos en un archivo JSON
with open("salida.json", "w") as archivo:
    json.dump(datos, archivo, indent = 4)  # `indent` para una salida legible
```

##### **2.3.2. Convertir objetos Python a cadenas JSON**

Para convertir datos de Python a una cadena JSON, se usa `json.dumps()`.

Ejemplo:

```python
import json

datos = {"nombre": "Pedro", "edad": 40}

# Convertir a cadena JSON
cadena_json = json.dumps(datos, indent = 2)
print(cadena_json)
```

Salida:

```json
{
  "nombre": "Pedro",
  "edad": 40
}
```

#### 2.4. Manipular datos JSON

Después de cargar un archivo JSON como un objeto de Python *(como un diccionario o lista)*, podemos manipular los datos con las operaciones estándar de Python.

Ejemplo:

```python
import json

# Leer el archivo JSON
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)

# Modificar los datos
datos["edad"] += 1
datos["habilidades"].append("SQL")

# Escribir los cambios de nuevo al archivo
with open("datos.json", "w") as archivo:
    json.dump(datos, archivo, indent = 4)
```

#### 2.5. Manejo de errores

Cuando trabajamos con JSON, es importante manejar **posibles excepciones** para evitar errores inesperados.

Ejemplo:

```python
import json

try:
    with open("datos.json", "r") as archivo:
        datos = json.load(archivo)
except FileNotFoundError:
    print("*ERROR* Archivo no encontrado.")
except json.JSONDecodeError:
    print("*ERROR* Problemas al decodificar el archivo JSON.")
except Exception as e:
    print(f"*ERROR* {e}.")
```

#### 2.6. Ejemplo Completo

##### **2.6.1. Fichero JSON inicial (`datos.json`)**

Este es el contenido inicial del archivo JSON que usaremos:

```json
{
    "usuarios": [
        {"id": 1, "nombre": "Juan", "edad": 30},
        {"id": 2, "nombre": "Ana", "edad": 25}
    ]
}
```

##### **2.6.2. Operaciones que el programa de ejemplo va a realizar**

El código realiza las siguientes operaciones:

1. Carga los datos desde el archivo JSON con manejo de excepciones.
2. Actualiza la edad de un usuario.
3. Inserta un nuevo usuario.
4. Elimina un usuario por su `id`.
5. Guarda los cambios en el archivo.

##### **2.6.3. Código en Python**

```python
import json


def cargar_json(nombre_fichero: str) -> dict:
    """
    Carga el contenido de un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.

    Returns:
        (dict): Contenido del archivo JSON como un diccionario, o None si no se pudo cargar.
    """
    try:
        with open(nombre_fichero, "r") as archivo:
            return json.load(archivo)
        
    except FileNotFoundError:
        print(f"*ERROR* El archivo {nombre_fichero} no existe.")
    
    except json.JSONDecodeError:
        print("*ERROR* El archivo JSON tiene un formato incorrecto.")

    except Exception as e:
        print(f"*ERROR* Problemas al cargar los datos {e}.")

    return None


def guardar_json(nombre_fichero: str, datos: dict):
    """
    Guarda los datos en un fichero JSON.

    Args:
        nombre_fichero (str): Nombre del fichero JSON.
        datos (dict): Datos a guardar.
    """
    try:
        with open(nombre_fichero, "w") as archivo:
            json.dump(datos, archivo, indent = 4)

    except PermissionError:
        print(f"*ERROR* No tienes permisos para escribir en el archivo '{nombre_fichero}'.")

    except TypeError as e:
        print(f"*ERROR* Los datos no son serializables a JSON. Detalle: {e}")        

    except Exception as e:
        print(f"*ERROR* Problemas al guardar los datos: {e}")


def actualizar_usuario(datos: dict, id_usuario: int, nueva_edad: int):
    """
    Actualiza la edad de un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a actualizar.
        nueva_edad (int): Nueva edad del usuario.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            usuario["edad"] = nueva_edad
            print(f"Usuario con ID {id_usuario} actualizado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")


def insertar_usuario(datos: dict, nuevo_usuario: dict):
    """
    Inserta un nuevo usuario.

    Args:
        datos (dict): Diccionario con los datos actuales.
        nuevo_usuario (dict): Diccionario con los datos del nuevo usuario.
    """
    datos["usuarios"].append(nuevo_usuario)
    print(f"Usuario {nuevo_usuario['nombre']} añadido con éxito.")


def eliminar_usuario(datos: dict, id_usuario: int):
    """
    Elimina un usuario dado su ID.

    Args:
        datos (dict): Diccionario con los datos actuales.
        id_usuario (int): ID del usuario a eliminar.
    """
    for usuario in datos["usuarios"]:
        if usuario["id"] == id_usuario:
            datos["usuarios"].remove(usuario)
            print(f"Usuario con ID {id_usuario} eliminado.")
            return
    
    print(f"Usuario con ID {id_usuario} no encontrado.")


def main():
    """
    Función principal que realiza las operaciones de gestión de un archivo JSON.
    """
    # Nombre del fichero JSON
    nombre_fichero = "src/otros/datos_usuarios.json"

    # 1. Cargar datos desde el fichero JSON
    datos = cargar_json(nombre_fichero)
    
    if datos is None:
        # Inicializamos datos vacíos si hay error
        datos = {"usuarios": []}

    # 2. Actualizar la edad de un usuario
    actualizar_usuario(datos, id_usuario = 1, nueva_edad = 31)

    # 3. Insertar un nuevo usuario
    nuevo_usuario = {"id": 3, "nombre": "Pedro", "edad": 40}
    insertar_usuario(datos, nuevo_usuario)

    # 4. Eliminar un usuario
    eliminar_usuario(datos, id_usuario = 2)

    # 5. Guardar los datos de nuevo en el fichero JSON
    guardar_json(nombre_fichero, datos)

    print("Operaciones completadas. Archivo actualizado.\n")


if __name__ == "__main__":
    main()
```

##### **2.6.4. Explicación paso a paso**

1. **Función `cargar_json`:**
   - Lee el contenido del archivo JSON.
   - Maneja excepciones como `FileNotFoundError` y `JSONDecodeError` para evitar fallos en caso de problemas con el archivo.

2. **Función `guardar_json`:**
   - Guarda el objeto Python en el archivo JSON.
   - Usa `json.dump` con `indent = 4` para que sea legible.

3. **Función `actualizar_usuario`:**
   - Busca un usuario por su `id` y actualiza su edad si existe.
   - Muestra un mensaje si no encuentra al usuario.

4. **Función `insertar_usuario`:**
   - Agrega un nuevo usuario al listado.

5. **Función `eliminar_usuario`:**
   - Elimina un usuario por su `id` si existe.
   - Muestra un mensaje si no lo encuentra.

6. **Ejecución principal:**
   - Carga el JSON inicial.
   - Realiza las operaciones necesarias (actualizar, insertar, eliminar).
   - Guarda los datos actualizados en el archivo.

##### **2.6.5. Resultado final (`datos.json`)**

Después de ejecutar el programa, el archivo `datos.json` tendrá el siguiente contenido:

```json
{
    "usuarios": [
        {
            "id": 1,
            "nombre": "Juan",
            "edad": 31
        },
        {
            "id": 3,
            "nombre": "Pedro",
            "edad": 40
        }
    ]
}
```

#### 2.7. Conclusión - JSON en Python

- El manejo de archivos JSON en Python es sencillo y flexible gracias al módulo `json`. Este permite trabajar con datos estructurados de forma legible y eficiente. 
- Con las funciones `load`, `loads`, `dump` y `dumps`, podemos realizar operaciones comunes como leer, escribir y manipular datos JSON en nuestros programas. 

#### 2.8. Opciones avanzadas

##### **2.8.1. Serialización de Objetos**

La serialización es el proceso de convertir un objeto en memoria *(como una lista, diccionario, o incluso objetos más complejos)* en un formato que pueda ser fácilmente almacenado o transmitido, como un archivo JSON, XML o binario. En el contexto de JSON, serializar un objeto significa convertirlo a una cadena en formato JSON para:
	1.	Almacenamiento persistente: Guardarlo en un archivo o base de datos.
	2.	Transmisión de datos: Enviarlo a través de una red, como en una API o un servicio web.
	3.	Compatibilidad: Interoperar con otros sistemas que usen JSON.

Deserialización, por el contrario, es el proceso inverso: convertir la representación JSON de vuelta a un objeto en memoria.

**¿Qué es un Objeto Serializable?**

Un objeto serializable es aquel que puede ser convertido directamente a un formato de almacenamiento/transmisión *(en este caso, JSON)*. En Python, los objetos básicos como str, int, float, list, dict, bool, y None son serializables a JSON de manera directa.

Sin embargo, no todos los tipos de objetos en Python son serializables por defecto. Por ejemplo, objetos como datetime, set, o instancias de clases personalizadas necesitan una forma específica de ser convertidos.

##### **2.8.2. Serializar objetos personalizados**

El módulo `json` puede serializar objetos personalizados usando el argumento `default`.

**Ejemplo:**

```python
import json
from datetime import datetime

# Crear un objeto con un tipo no JSON serializable
datos = {
    "evento": "Reunión",
    "fecha": datetime.now()
}

# Serializador personalizado
def convertir(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convertir a formato ISO 8601
    raise TypeError("Tipo no serializable")

# Serializar el objeto
cadena_json = json.dumps(datos, default = convertir, indent = 4)
print(cadena_json)
```

**¿Qué sucede aquí?**

   - El diccionario `datos` contiene:
      
      * "evento": una cadena (str), que es serializable de manera directa.
      
      * "fecha": un objeto de tipo datetime, que no es serializable por defecto.

   - La función `json.dumps()` intenta serializar cada valor del diccionario.
   
      * Al llegar a "fecha", detecta que es un tipo datetime (no serializable directamente).
      
      * Llama a la función proporcionada en el argumento default, que es `convertir`.

   - La función `convertir`:
   
      * Verifica si el objeto es de tipo datetime con `isinstance(obj, datetime)`.
      
      * Si lo es, lo convierte al formato ISO 8601 utilizando el método `isoformat()`.

      * Si no puede convertir el objeto, lanza un ***TypeError***.
   
   - Finalmente, `json.dumps()` crea la cadena JSON con el formato que podemos observar en ***Salida***.

**Salida:**

```json
{
    "evento": "Reunión",
    "fecha": "2024-11-22T12:34:56.789123"
}
```

**El argumento default**
	- Sirve como un callback que json.dumps() llama cada vez que encuentra un objeto no serializable.
	- Si no proporcionas este argumento y se encuentra un tipo no serializable, json.dumps() lanza una excepción TypeError.
	- Útil para convertir tipos personalizados, como datetime, set, o incluso instancias de clases.

##### **2.8.3. Ordenar claves**

Para ordenar las claves del JSON, usa el argumento `sort_keys`.

**Ejemplo:**

```python
import json

datos = {"z": 1, "a": 2, "m": 3}
cadena_json = json.dumps(datos, sort_keys = True, indent = 2)
print(cadena_json)
```

**¿Qué sucede aquí?:**
	- `datos` es un diccionario que contiene:
	    * "z": 1
	    * "a": 2
	    * "m": 3
	- Cuando usamos el argumento `sort_keys = True`:
	    * Python ordena las claves del diccionario alfabéticamente (a, m, z) antes de convertirlo a JSON.
	    * Esto es útil cuando queremos garantizar un orden consistente de las claves en el JSON, especialmente en archivos o transmisiones donde el orden importa.
	- El resultado es el que se muestra en ***Salida***.
	- Sin `sort_keys = True`, el orden de las claves en el JSON seguiría el orden original del diccionario.

**Salida:**

```json
{
  "a": 2,
  "m": 3,
  "z": 1
}
```

**El argumento sort_keys**
	- No afecta la estructura o contenido del JSON, solo su presentación.
	- Es puramente estético o práctico, por ejemplo, para facilitar la lectura o las comparaciones en pruebas automatizadas.

##### **2.8.4. Conclusión - Opciones avanzadas**

La serialización personalizada y la ordenación de claves son características avanzadas pero muy útiles del módulo json. Permiten:
	1.	Adaptabilidad: Serializar tipos personalizados como datetime, o incluso tus propias clases.
	2.	Consistencia: Ordenar las claves del JSON para garantizar un formato estándar, útil en pruebas, depuración o contratos API.
	3.	Flexibilidad: Personalizar la salida del JSON para que cumpla con los requisitos específicos de tu aplicación.

Al dominar estas técnicas, podemos aprovechar al máximo el módulo json en proyectos de cualquier complejidad.

---

### 3. JSON en Kotlin

El formato JSON en Kotlin es similar al de Python: se utiliza para representar pares clave-valor y listas. Es compatible con las estructuras de datos de Kotlin, como `Map` y `List`.

En Kotlin, estos datos se pueden mapear a clases de datos (`data class`) para trabajar con ellos de forma estructurada.

#### 3.1. Importar y configurar Gson

Kotlin no tiene soporte nativo para JSON, pero librerías como **Gson** permiten manejarlo fácilmente.

##### **3.1.1. Configuración del proyecto**

1. Añade la dependencia de Gson al archivo `build.gradle.kts`:

```kotlin
dependencies {
    implementation("com.google.code.gson:gson:2.8.9")
}
```

2. Importa la librería Gson en tu código:

```kotlin
import com.google.gson.Gson
```

#### 3.2. Leer archivos JSON

##### **3.2.1. Leer JSON desde un archivo**

Usamos la clase `File` de Kotlin para leer el archivo como texto y luego `Gson` para convertirlo en objetos de Kotlin.

**Ejemplo:**

```kotlin
import com.google.gson.Gson
import java.io.File

data class Usuario(val id: Int, val nombre: String, var edad: Int)
data class Datos(val usuarios: MutableList<Usuario>)

fun cargarJson(nombreFichero: String): Datos? {
    return try {
        val json = File(nombreFichero).readText()
        Gson().fromJson(json, Datos::class.java)
    } catch (e: Exception) {
        println("Error al cargar el archivo: ${e.message}")
        null
    }
}
```

Este código:
- Lee el archivo JSON como texto.
- Usa `Gson().fromJson()` para convertir el texto JSON en un objeto `Datos` (con una lista de `Usuario`).

##### **3.2.2. Leer JSON desde una cadena**

Podemos trabajar con cadenas JSON directamente en lugar de un archivo. 

**Ejemplo:**

```kotlin
val cadenaJson = """
    {"usuarios": [{"id": 1, "nombre": "Juan", "edad": 30}]}
"""
val datos = Gson().fromJson(cadenaJson, Datos::class.java)
println(datos.usuarios[0].nombre) // Salida: Juan
```

#### 3.3. Escribir archivos JSON

##### **3.3.1. Escribir JSON en un archivo**

Usamos `Gson().toJson()` para convertir un objeto Kotlin a JSON y luego lo guardamos con `File.writeText()`.

**Ejemplo:**

```kotlin
fun guardarJson(nombreFichero: String, datos: Datos) {
    try {
        val json = Gson().toJson(datos)
        File(nombreFichero).writeText(json)
    } catch (e: Exception) {
        println("Error al guardar los datos: ${e.message}")
    }
}
```

##### **3.3.2. Convertir objetos Kotlin a cadenas JSON**

Si no queremos guardar los datos en un archivo, podemos simplemente convertirlos a una cadena JSON.

**Ejemplo:**

```kotlin
val datos = Datos(mutableListOf(Usuario(1, "Juan", 30)))
val cadenaJson = Gson().toJson(datos)
println(cadenaJson)
```

**Salida:**

```json
{
  "usuarios": [
    {
      "id": 1,
      "nombre": "Juan",
      "edad": 30
    }
  ]
}
```

#### 3.4. Manipular datos JSON

Una vez que los datos JSON se cargan en un objeto Kotlin, podemos manipularlos fácilmente como cualquier otra colección.

##### **3.4.1. Actualizar un dato**

Actualiza la edad de un usuario específico buscando su `id`:

```kotlin
fun actualizarUsuario(datos: Datos, idUsuario: Int, nuevaEdad: Int) {
    val usuario = datos.usuarios.find { it.id == idUsuario }
    if (usuario != null) {
        usuario.edad = nuevaEdad
        println("Usuario con ID $idUsuario actualizado.")
    } else {
        println("Usuario con ID $idUsuario no encontrado.")
    }
}
```

##### **3.4.2. Insertar un nuevo usuario**

Añade un nuevo usuario a la lista:

```kotlin
fun insertarUsuario(datos: Datos, nuevoUsuario: Usuario) {
    datos.usuarios.add(nuevoUsuario)
    println("Usuario ${nuevoUsuario.nombre} añadido con éxito.")
}
```

##### **3.4.3. Eliminar un usuario**

Elimina un usuario de la lista buscando su `id`:

```kotlin
fun eliminarUsuario(datos: Datos, idUsuario: Int) {
    val usuario = datos.usuarios.find { it.id == idUsuario }
    if (usuario != null) {
        datos.usuarios.remove(usuario)
        println("Usuario con ID $idUsuario eliminado.")
    } else {
        println("Usuario con ID $idUsuario no encontrado.")
    }
}
```

#### 3.5. Manejo de errores

Usamos bloques `try-catch` para manejar excepciones al leer o escribir archivos JSON.

**Ejemplo:**

```kotlin
fun cargarJsonSeguro(nombreFichero: String): Datos? {
    return try {
        val json = File(nombreFichero).readText()
        Gson().fromJson(json, Datos::class.java)
    } catch (e: FileNotFoundException) {
        println("Archivo no encontrado: $nombreFichero")
        null
    } catch (e: JsonSyntaxException) {
        println("Error en el formato del archivo JSON.")
        null
    }
}
```

#### 3.6. Ejemplo completo

Con todas las piezas juntas, el flujo completo de operaciones sería:

```kotlin
fun main() {
    val nombreFichero = "datos.json"

    // 1. Cargar datos desde el fichero JSON
    val datos = cargarJson(nombreFichero) ?: Datos(mutableListOf())

    // 2. Actualizar la edad de un usuario
    actualizarUsuario(datos, idUsuario = 1, nuevaEdad = 31)

    // 3. Insertar un nuevo usuario
    val nuevoUsuario = Usuario(id = 3, nombre = "Pedro", edad = 40)
    insertarUsuario(datos, nuevoUsuario)

    // 4. Eliminar un usuario
    eliminarUsuario(datos, idUsuario = 2)

    // 5. Guardar los datos de nuevo en el fichero JSON
    guardarJson(nombreFichero, datos)

    println("Operaciones completadas. Archivo actualizado.")
}
```

#### 3.7. Resultado final

Después de ejecutar el programa, el archivo `datos.json` se verá así:
```json
{
  "usuarios": [
    {"id": 1, "nombre": "Juan", "edad": 31},
    {"id": 3, "nombre": "Pedro", "edad": 40}
  ]
}
```

#### 3.8. JSON en un `Map<String, Any>`

Si necesitamos mayor flexibilidad, podemos deserializar el JSON en un `Map`. Esto es útil si no conocemos la estructura del JSON o prefirimos manipular los datos dinámicamente.

##### **3.8.1. Deserialización a un `Map`**

Con **Gson**, podemos hacerlo utilizando un `TypeToken`:

```kotlin
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.File

fun cargarJsonComoMap(nombreFichero: String): Map<String, Any>? {
    return try {
        val json = File(nombreFichero).readText()
        val tipo = object : TypeToken<Map<String, Any>>() {}.type
        Gson().fromJson<Map<String, Any>>(json, tipo)
    } catch (e: Exception) {
        println("*ERROR* Problemas al cargar el JSON como Map: ${e.message}")
        null
    }
}

fun main() {
    val nombreFichero = "datos.json"
    val datosComoMap = cargarJsonComoMap(nombreFichero)
    if (datosComoMap != null) {
        println("\nDatos cargados como Map:")
        datosComoMap.forEach { (clave, valor) ->
            println("$clave: $valor")
        }
    }
}
```

##### **3.8.2. Ejemplo de Salida**

Dado este archivo `datos.json`:

```json
{
    "usuarios": [
        {"id": 1, "nombre": "Juan", "edad": 30},
        {"id": 2, "nombre": "Ana", "edad": 25}
    ]
}
```

**Salida del Programa**:

```
Datos cargados como Map:
usuarios: [{id=1.0, nombre=Juan, edad=30.0}, {id=2.0, nombre=Ana, edad=25.0}]
```

#### 3.9. Conclusión - JSON en Kotlin

El manejo de JSON en Kotlin es muy sencillo gracias a librerías como Gson. Al igual que en Python, podemos realizar operaciones como leer, escribir, actualizar e insertar datos con un enfoque modular y utilizando clases de datos (`data class`) para estructurar los datos.
