---
title: Tratamiento de ficheros JSON.

description: Tratamiento de ficheros JSON.

authors:
    - Diego Cano.

date: 2024-03-08

tags:
  - JSON
  - Gson
  - kotlin
---
# Tratamiento de ficheros JSON

## Introducción

Para leer un archivo JSON en Kotlin, primero necesitamos agregar una dependencia para manejar JSON, como `Gson` o `kotlinx.serialization`.

Aquí tenéis un ejemplo usando `Gson`, que es una biblioteca popular para la conversión entre objetos Java y su representación JSON.

Primero, debemos asegurarnos de incluir Gson en nuestro proyecto. Si estamos usando Gradle, podemos añadir la siguiente línea al archivo `build.gradle` en la sección de dependencias:

```gradle
implementation 'com.google.code.gson:gson:2.8.8'
```

Ahora, supongamos que tenemos un archivo JSON llamado `data.json` con el siguiente contenido:

```json
{
  "nombre": "Juan",
  "edad": 30
}
```

Aquí tenemos un ejemplo de código en Kotlin para leer este archivo y convertirlo en un objeto de Kotlin:

```kotlin
import com.google.gson.Gson
import java.io.FileReader

// Definimos una clase que represente la estructura del JSON
data class Usuario(val nombre: String, val edad: Int)

fun main() {
    // Creamos una instancia de Gson
    val gson = Gson()

    // Abrimos el archivo JSON
    FileReader("data.json").use { reader ->
        // Convertimos el JSON en un objeto de la clase Usuario
        val usuario = gson.fromJson(reader, Usuario::class.java)

        // Imprimimos los datos del usuario
        println("Nombre: ${usuario.nombre}, Edad: ${usuario.edad}")
    }
}
```

Este código define una clase `Usuario` que representa la estructura del archivo JSON. Luego, utiliza `FileReader` para leer el archivo `data.json`, y Gson para convertir el contenido JSON en una instancia de `Usuario`. Finalmente, imprime los datos del usuario.

## Ejemplo simple con una lista

#### 1. Supongamos que tenemos un archivo JSON llamado `usuarios.json` que contiene una lista de usuarios, cada uno con su nombre y edad, como en el siguiente ejemplo:

```json
[
  {
    "nombre": "Juan",
    "edad": 30
  },
  {
    "nombre": "Ana",
    "edad": 25
  }
]
```

#### 2. Para leer este archivo y convertirlo en una lista de objetos en Kotlin, primero necesitamos definir la clase que representa la estructura de un usuario, igual que antes. Luego, podemos usar `Gson` para convertir la lista JSON en una lista de objetos `Usuario`:

```kotlin
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.FileReader

// La clase Usuario permanece igual
data class Usuario(val nombre: String, val edad: Int)

fun main() {
    // Creamos una instancia de Gson
    val gson = Gson()

    // Abrimos el archivo JSON
    FileReader("usuarios.json").use { reader ->
        // Creamos un tipo para la lista de usuarios
        val usuarioListType = object : TypeToken<List<Usuario>>() {}.type

        // Convertimos el JSON en una lista de objetos Usuario
        val usuarios: List<Usuario> = gson.fromJson(reader, usuarioListType)

        // Imprimimos los datos de los usuarios
        usuarios.forEach { usuario ->
            println("Nombre: ${usuario.nombre}, Edad: ${usuario.edad}")
        }
    }
}
```

En este código, la clave está en `TypeToken<List<Usuario>>().type`. Esto es necesario porque en tiempo de ejecución, la información genérica de Java se borra debido a la implementación de generics mediante type erasure. `TypeToken` permite a `Gson` entender que queremos deserializar el JSON en una `List<Usuario>`.

Este enfoque nos permite manejar archivos JSON más complejos que contengan colecciones de objetos. Podemos seguir expandiendo este concepto para trabajar con estructuras aún más complejas, como listas anidadas o mapas.

## Ejemplo con listas que pueden contener valores nulos

Imaginad que queremos manejar un archivo JSON con recetas, donde cada receta tiene una lista de ingredientes, pero algunos pueden ser `null`... podemos definir una clase `Receta` que contenga una lista de ingredientes. Luego, al deserializar el JSON, podemos filtrar y almacenar solo aquellos ingredientes que no sean `null`.

#### 1. Supongamos que el archivo JSON tiene este formato:

```json
[
  {
    "nombre": "Receta 1",
    "ingredientes": ["Harina", null, "Azúcar", "Levadura", null]
  },
  {
    "nombre": "Receta 2",
    "ingredientes": [null, "Tomate", "Queso", null, "Orégano"]
  }
]
```

#### 2. A continuación, pasamos a definir las clases en Kotlin y leer el archivo JSON filtrando los valores `null`:

```kotlin
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.FileReader

// Define la clase Receta
data class Receta(val nombre: String, val ingredientes: List<String?>)

fun main() {
    val gson = Gson()

    // Define el tipo para la lista de recetas
    val recetaListType = object : TypeToken<List<Receta>>() {}.type

    FileReader("recetas.json").use { reader ->
        // Deserializa el JSON a una lista de Recetas
        val recetas: List<Receta> = gson.fromJson(reader, recetaListType)

        // Filtra los ingredientes nulos y almacena las recetas con ingredientes no nulos
        val recetasFiltradas = recetas.map { receta ->
            receta.copy(ingredientes = receta.ingredientes.filterNotNull())
        }

        // Imprime las recetas con ingredientes no nulos
        recetasFiltradas.forEach { receta ->
            println("Receta: ${receta.nombre}")
            receta.ingredientes.forEach { ingrediente ->
                println(" - $ingrediente")
            }
        }
    }
}
```

#### 3. Este código realiza lo siguiente:

1. Define una clase `Receta` que representa la estructura de cada receta en el JSON, incluyendo una lista de ingredientes que puede contener valores `null`.
2. Lee el archivo JSON y lo deserializa en una lista de objetos `Receta`.
3. Utiliza `map` para crear una nueva lista de recetas donde cada receta ha sido copiada con una nueva lista de ingredientes que solo incluye aquellos que no son `null` (usando `filterNotNull`).

De esta manera, cada receta en `recetasFiltradas` tendrá solo los ingredientes no nulos, y podremos trabajar con estos datos de manera más limpia en nuestra aplicación.

## Ejemplo con una lista de elementos, siempre fijos, pero con posibilidad de valores nulos

En este ejemplo abordamos un fichero JSON con la siguiente estructura:

```json
[
  {
    "nombre": "Receta 1",
    "ingrediente1": "Harina", 
    "ingrediente2": "Azúcar",
    "ingrediente3": "Levadura",
    "ingrediente4": null,
    "ingrediente5": null,
    "ingrediente6": null, 
    "ingrediente7": null,
    "ingrediente8": null,
    "ingrediente9": null,
    "ingrediente10": null
  },
  {
    "nombre": "Receta 2",
    "ingrediente1": "Tomate", 
    "ingrediente2": "Queso",
    "ingrediente3": "Jamón",
    "ingrediente4": "Orégano",
    "ingrediente5": null,
    "ingrediente6": null, 
    "ingrediente7": null,
    "ingrediente8": null,
    "ingrediente9": null,
    "ingrediente10": null
  }
]
```

Para manejar un archivo JSON como el anterior, donde cada receta tiene hasta 10 ingredientes específicamente nombrados, y algunos pueden ser `null`, necesitaremos un enfoque un poco diferente. La idea es deserializar cada receta a un objeto que contenga estos ingredientes como campos, y luego transformar esos campos en una lista, excluyendo los valores `null`.

#### 1. Vamos a modificar la clase `Receta` para que refleje esta estructura y luego procesaremos los ingredientes para obtener solo los no nulos:

```kotlin
import com.google.gson.Gson
import com.google.gson.reflect.TypeToken
import java.io.FileReader

data class RecetaRaw(
    val nombre: String,
    val ingrediente1: String?,
    val ingrediente2: String?,
    val ingrediente3: String?,
    val ingrediente4: String?,
    val ingrediente5: String?,
    val ingrediente6: String?,
    val ingrediente7: String?,
    val ingrediente8: String?,
    val ingrediente9: String?,
    val ingrediente10: String?
    // Añade más campos si tienes hasta 15 ingredientes.
)

data class Receta(
    val nombre: String,
    val ingredientes: List<String>
)

fun main() {
    val gson = Gson()

    val recetaListType = object : TypeToken<List<RecetaRaw>>() {}.type

    FileReader("recetas.json").use { reader ->
        // Deserializa el JSON a una lista de RecetaRaw
        val recetasRaw: List<RecetaRaw> = gson.fromJson(reader, recetaListType)

        // Transforma RecetaRaw en Receta, filtrando los ingredientes nulos
        val recetas = recetasRaw.map { raw ->
            Receta(
                nombre = raw.nombre,
                ingredientes = listOfNotNull(
                    raw.ingrediente1,
                    raw.ingrediente2,
                    raw.ingrediente3,
                    raw.ingrediente4,
                    raw.ingrediente5,
                    raw.ingrediente6,
                    raw.ingrediente7,
                    raw.ingrediente8,
                    raw.ingrediente9,
                    raw.ingrediente10
                    // Añade más elementos aquí si tienes hasta 15 ingredientes.
                )
            )
        }

        // Imprime las recetas y sus ingredientes
        recetas.forEach { receta ->
            println("Receta: ${receta.nombre}")
            receta.ingredientes.forEach { ingrediente ->
                println(" - $ingrediente")
            }
        }
    }
}
```

#### 2. Explicación del código:

- Este código primero deserializa el JSON en una lista de `RecetaRaw`, que contiene todos los campos posibles para los ingredientes, incluidos los `null`. 

- Luego, mapea esta lista a una nueva lista de `Receta`, donde cada `Receta` tiene un nombre y una lista de ingredientes que solo incluye los valores no nulos (utilizando `listOfNotNull` para filtrar los `null`).

- De esta manera, podemos manejar fácilmente el JSON proporcionado, asegurándonos de que solo los ingredientes válidos (no nulos) se incluyan en la lista de ingredientes de cada receta.

## Ejemplo con kotlinx.serialization

Vamos a ver, por último, un ejemplo más general de lectura y escritura de archivos JSON en Kotlin, utilizando la biblioteca kotlinx.serialization, que es parte del ecosistema de Kotlin y ofrece una forma nativa de serializar y deserializar datos.

#### 1. Insertar las dependencias necesarias:

Para usar kotlinx.serialization, primero debemos agregar las dependencias necesarias a nuestro proyecto. Si estamos utilizando Gradle, podemos incluir lo siguiente en el archivo `build.gradle`:

```gradle
plugins {
    id 'org.jetbrains.kotlin.plugin.serialization' version '1.5.0'
}

dependencies {
    implementation 'org.jetbrains.kotlinx:kotlinx-serialization-json:1.2.1'
}
```

Siempre debemos asegurarnos de usar las versiones más recientes de las dependencias.

Ahora, veamos cómo podríamos leer y escribir un archivo JSON que contiene una lista de objetos. Usaremos un ejemplo simple de una lista de usuarios, donde cada usuario tiene un nombre y una edad.

#### 2. Definimos la clase de datos `Usuario` y agregamos una `Anotación` para la serialización:

```kotlin
import kotlinx.serialization.*
import kotlinx.serialization.json.*

@Serializable
data class Usuario(val nombre: String, val edad: Int)
```

#### 3. Lectura de un archivo JSON

Para leer un archivo JSON y convertirlo en una lista de objetos `Usuario`, podríamos hacer lo siguiente:

```kotlin
import java.io.File

fun leerUsuariosDeJSON(archivo: String): List<Usuario> {
    val contenido = File(archivo).readText()
    return Json.decodeFromString(ListSerializer(Usuario.serializer()), contenido)
}

val usuarios = leerUsuariosDeJSON("usuarios.json")
usuarios.forEach {
    println("Nombre: ${it.nombre}, Edad: ${it.edad}")
}
```

Este código lee todo el contenido del archivo `usuarios.json` como un `String` y luego utiliza `Json.decodeFromString` para deserializar este `String` en una lista de objetos `Usuario`.

#### 4. Escritura a un archivo JSON

Para escribir una lista de objetos `Usuario` en un archivo JSON, podemos hacer lo siguiente:

```kotlin
fun escribirUsuariosAJSON(usuarios: List<Usuario>, archivo: String) {
    val contenido = Json.encodeToString(ListSerializer(Usuario.serializer()), usuarios)
    File(archivo).writeText(contenido)
}

// Lista de ejemplo para escribir en el archivo
val listaDeUsuarios = listOf(
    Usuario("Juan", 30),
    Usuario("Ana", 25)
)

escribirUsuariosAJSON(listaDeUsuarios, "nuevos_usuarios.json")
```

Este código serializa una lista de objetos `Usuario` a un `String` JSON utilizando `Json.encodeToString` y luego escribe este `String` en un archivo llamado `nuevos_usuarios.json`.

Este ejemplo cubre tanto la lectura como la escritura de datos JSON en Kotlin usando la biblioteca kotlinx.serialization, que proporciona una forma integrada y eficiente de trabajar con JSON en aplicaciones Kotlin.
