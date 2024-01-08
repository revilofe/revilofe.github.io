---
title: "UD 4 - 4.1.1 Aclaraciones kotlin "
description: kotlin
summary: kotlin
authors:
    - Eduardo Fdez
date: 2024-01-08
icon: 
permalink: /prog/unidad4/4.1.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
# Aclaraciones sobre [Kotlin]

En este punto vamos a ver algunas aclaraciones sobre el lenguaje de programación [Kotlin]. Se basa en las principales dudas que nos pueden surgir al empezar a programar en este lenguaje y que han sido extraídas de las preguntas que el alumnado ha realizado durante los distintos cursos.

## 1. Aclaraciones sobre el lenguaje

### 1.1. Funciones lambda

Imagina que tienes una lista de números y quieres quedarte solo con los que son pares. En Kotlin, puedes hacer esto fácilmente con `filter`.

La firma o signatura de la función `filter` en Kotlin es la siguiente:

```kotlin
fun <T> Iterable<T>.filter(predicate: (T) -> Boolean): List<T>
```

Aquí te desgloso lo que significa cada parte:

* `fun`: Indica que se trata de una función.
* `<T>`: Es un parámetro de tipo genérico. Esto significa que `filter` puede trabajar con listas de cualquier tipo de elementos, como `Int`, `String`, `YourCustomClass`, etc.
* `Iterable<T>`: Indica que `filter` es una función de extensión para la interfaz `Iterable<T>`. Dado que `List<T>` implementa `Iterable<T>`, puedes usar `filter` con cualquier lista.
* `predicate: (T) -> Boolean`: Es el parámetro que toma `filter`. Es una función lambda que toma un elemento de tipo `T` y devuelve un `Boolean`. Si la lambda devuelve `true`, el elemento se incluye en la lista resultante; si devuelve `false`, se excluye.
* `List<T>`: Es el tipo de retorno de `filter`. Devuelve una nueva lista que contiene solo los elementos que cumplen con el predicado.

Esta signatura refleja la versatilidad y el poder de `filter` en Kotlin: puedes usarla con cualquier tipo de lista y definir cualquier condición para filtrar los elementos de esa lista.

Por tanto, la función `filter` se utiliza para filtrar elementos de una lista basándose en una condición que defines. Funciona así: pasas una lambda (un tipo de función anónima) a `filter`, y esta lambda debe devolver `true` o `false` para cada elemento. Si devuelve `true`, el elemento se mantiene en la lista resultante; si devuelve `false`, se descarta.

Aquí tienes un ejemplo sencillo:

```kotlin
val numeros = listOf(1, 2, 3, 4, 5)
val pares = numeros.filter { it % 2 == 0 }
println(pares)  // Imprimirá: [2, 4]
```

En este código, `{ it % 2 == 0 }` es una lambda que chequea si un número es par. `it` es una referencia al elemento actual de la lista que se está procesando.

Ahora, sobre cómo está implementada `filter` internamente: es una función de extensión de la interfaz `List`. Utiliza un bucle para iterar sobre los elementos de la lista y aplica la lambda a cada uno. Si la lambda devuelve `true`, el elemento se agrega a una nueva lista. Finalmente, esta nueva lista filtrada se devuelve.

Si bien el código exacto de la implementación puede variar, conceptualmente es algo así:

```kotlin
fun <T> List<T>.filter(predicate: (T) -> Boolean): List<T> {
    val resultado = mutableListOf<T>()
    for (item in this) {
        if (predicate(item)) {
            resultado.add(item)
        }
    }
    return resultado
}
```

Espero que esto te ayude a entender mejor cómo funciona `filter` y en general cualquier función o método que utiliza lambdas entre sus parámetros.

### 1.2. Notación para llamar a las funciones cuando se utilizan lambdas

En Kotlin, cuando llamas a una función que toma una lambda como parámetro, puedes usar dos formas: con o sin paréntesis. La que ya mostré es la forma sin paréntesis, pero si prefieres usar paréntesis, puedes hacerlo también. Aquí te muestro cómo sería:

```kotlin
val numeros = listOf(1, 2, 3, 4, 5)
val pares = numeros.filter({ it % 2 == 0 }) //tambien se puede poner numeros.filter { it % 2 == 0 }
println(pares)  // Esto imprimirá: [2, 4]
```

En esta versión, simplemente colocas la lambda entre paréntesis después de `filter`. Funciona exactamente igual que la versión sin paréntesis. Es más una cuestión de estilo y preferencia personal que de funcionalidad.

En Kotlin, cuando una función tiene una lambda como último parámetro, puedes optar por usar la "sintaxis de lambda fuera de los paréntesis", que es lo que hicimos en los ejemplos de más arriba. Pero si te sientes más cómodo con los paréntesis, ¡adelante!

### 1.3. ¿Qué es un receiver en kotlin?

En Kotlin, un "receiver" se refiere a un tipo especial de parámetro que está disponible dentro del cuerpo de una función de extensión o una lambda con receptor. Es una forma poderosa y flexible de añadir funcionalidades a clases existentes o de crear DSLs (Domain-Specific Languages). Veamos cada caso:

1. **Funciones de Extensión**: Cuando defines una función de extensión para una clase, el "receiver" es la instancia de esa clase sobre la cual se invoca la función. Por ejemplo:

    ```kotlin
    fun String.exclamar() = this + "!"
    ```
    
    Aquí, `String` es el receiver. Dentro de exclamar, puedes usar this para referirte a la instancia específica de String sobre la que se llama a la función. Si haces `val saludo = "Hola".exclamar()`, `this` dentro de exclamar será `"Hola"`.   

2. **Lambdas con Receptor**: Son similares a las funciones de extensión, pero en forma de lambda. Dentro de estas lambdas, tienes acceso directo a los métodos y propiedades del receiver. Un ejemplo común es con las builders en Kotlin, como en apply:

    ```kotlin
    val lista = ArrayList<String>().apply {
        add("Uno")
        add("Dos")
    }
    ```

    En este caso, `ArrayList<String>()` es el receiver para la lambda pasada a `apply`. Dentro de la lambda, puedes llamar directamente a métodos como `add` sin necesidad de especificar el objeto (no necesitas decir `this.add("Uno")`, simplemente `add("Uno")` funciona).

Por tanto, el receiver en Kotlin proporciona un contexto adicional dentro de una función de extensión o una lambda, permitiéndote acceder y modificar las propiedades y métodos del objeto sobre el cual se invoca la función o lambda. Esto hace que el código sea más conciso y legible, y es una parte fundamental de cómo Kotlin maneja muchas de sus características más elegantes y potentes.

### 1.4. ¿Qué es `it` en kotlin?

En Kotlin, `it` es un nombre implícito que se usa para referirse al parámetro único de una lambda cuando dicho parámetro no se declara de manera explícita. Es una forma conveniente y concisa de trabajar con lambdas que solo requieren un parámetro. Aquí te explico un poco más:

1. **Uso en Lambdas**: Cuando tienes una lambda que acepta un solo parámetro, puedes usar `it` para referirte a ese parámetro sin necesidad de declararlo. Por ejemplo:
    ```kotlin
   val lista = listOf(1, 2, 3)
   val cuadrados = lista.map { it * it }
    ```
   
   En este caso, la lambda pasada a `map` tiene un parámetro (cada elemento de la lista), y usamos `it` para referirnos a ese parámetro. Es equivalente a escribir `{ numero -> numero * numero }`, pero más conciso.   

2. **Cuándo se Utiliza**: `it` se utiliza automáticamente solo cuando la lambda tiene un solo parámetro. Si la lambda tiene más de un parámetro o si quieres nombrar explícitamente el parámetro por claridad, entonces no se puede usar `it`.   

3. **Legibilidad**: Aunque `it` es útil para mantener el código conciso, en algunos casos puede ser menos legible, especialmente si el cuerpo de la lambda es largo o complejo. En tales situaciones, puede ser mejor dar un nombre explícito al parámetro para hacer el código más fácil de entender.   

Para darle un nombre a `it` en una lambda en Kotlin, simplemente defines explícitamente el parámetro de la lambda. Esto se hace colocando el nombre del parámetro seguido de una flecha (`->`) al principio de la lambda. Aquí te muestro cómo hacerlo con un ejemplo:Supongamos que tienes una lista y quieres aplicar una operación a cada elemento. Usando `it`, lo harías así:

```kotlin
val numeros = listOf(1, 2, 3)
val cuadrados = numeros.map { it * it }
```

En este caso, `it` se refiere implícitamente a cada elemento de la lista `numeros`. Pero si prefieres darle un nombre explícito al parámetro, lo haces de la siguiente manera:

```kotlin
val cuadrados = numeros.map { numero -> numero * numero }
```

Aquí, `numero` es el nombre que le has dado al parámetro que antes se referenciaba con `it`. Esto puede hacer que tu código sea más legible, especialmente si la lambda es compleja o si estás trabajando con varias lambdas y quieres evitar confusiones.

Nombrar los parámetros de las lambdas es una buena práctica cuando el contexto no es inmediatamente claro o cuando la lambda es lo suficientemente compleja como para beneficiarse de una mayor claridad.

Por tanto, `it` es una herramienta útil en Kotlin que ayuda a mantener las lambdas simples y concisas cuando solo tienen un parámetro. Es parte de lo que hace a Kotlin un lenguaje expresivo y agradable de usar.

### 1.5. Manejo de nulos y operador Elvis.

Controlar los nulos es una parte crucial en Kotlin, y es uno de los aspectos donde este lenguaje realmente brilla, gracias a su sistema de tipos que distingue entre referencias que pueden ser nulas (`nullable`) y las que no pueden serlo (`non-nullable`). Veamos cómo puedes manejar los nulos y usar el operador Elvis en Kotlin:

1. **Tipos Nulables y No Nulables**:
    En Kotlin, una variable no puede ser nula a menos que se declare explícitamente como nulable. Se agrega un signo de interrogación (`?`) al tipo para indicar que puede ser nula.

    ```kotin
    var nombre: String = "Cirolele"  // No puede ser nula
    var apellido: String? = null     // Puede ser nula
    ```   
     
2. **Chequeo de Nulos**:
    Antes de usar una variable nulable, debes verificar si es nula.
    ```kotin
    if (apellido != null) {
        println(apellido.length)
    }
    ```   
     
3. **Operador de Llamada Segura (`?.`)**:
   Permite acceder de forma segura a las propiedades y métodos de una referencia nulable. Si la referencia es nula, no se ejecuta el método o propiedad y devuelve nulo.
    ```kotin
    println(apellido?.length)  // Imprime el largo si no es nulo, sino imprime null
    ```    
  
4. **Operador Elvis (`?:`)**:
   Este operador se utiliza para proporcionar un valor por defecto en caso de que la expresión a su izquierda sea nula. Es como decir "usa esto, pero si es nulo, entonces usa aquello".
    ```kotin
    val longitud = apellido?.length ?: 0  // Si apellido es nulo, usa 0
    ```
    El operador Elvis es extremadamente útil para evitar el anidamiento excesivo de declaraciones `if` y proporcionar valores predeterminados de manera concisa.   
   
5. **Operador de Aserto No Nulo (`!!`)**:   
   Convierte cualquier valor a un tipo no nulable, lanzando una excepción `NullPointerException` si el valor es nulo.   
   Debe usarse con cuidado, ya que va en contra de la seguridad de nulos que Kotlin intenta proporcionar.
   ```kotin
   val nombreNoNulo: String = nombre!!  // Lanza NullPointerException si nombre es nulo
   ```   

6. **let con Nulos**:
   El método `let` puede ser útil para trabajar con valores nulables. Si el objeto es nulo, el bloque no se ejecuta.
    ```kotin
    apellido?.let {
        println("El apellido tiene ${it.length} caracteres")
    }
    ```

Aprender a controlar los nulos en Kotlin te ayuda a escribir código más seguro y menos propenso a errores en tiempo de ejecución. Recuerda, Kotlin está diseñado para minimizar la posibilidad de `NullPointerException`, y aprovechar estas características te permite escribir un código más robusto y limpio.

### 1.6. Diferencia entre Listas y Arrays
 Las listas y los arrays son dos estructuras de datos comunes en Kotlin. Aunque son similares, tienen algunas diferencias importantes que es importante conocer. Veamos cuáles son:
- **Listas**: Una lista es una colección ordenada de elementos. Puedes agregar o quitar elementos de una lista después de su creación. En Kotlin, las listas son inmutables por defecto, lo que significa que no puedes modificarlas después de su creación. Para crear una lista mutable, debes usar `mutableListOf` en lugar de `listOf`. Por ejemplo:

   ```kotlin
   val lista = listOf("A", "B", "C")  // Lista inmutable
   val listaMutable = mutableListOf("A", "B", "C")  // Lista mutable
   ```
- **Arrays**: Un array es una estructura de datos que contiene una colección de elementos del mismo tipo. Los arrays son representados por la clase `Array` y son mutables por defecto, lo que significa que puedes modificarlos después de su creación. Para crear un array inmutable, debes usar `arrayOf` en lugar de `arrayOf`. Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")  // Array mutable
    val arrayInmutable = arrayOf("A", "B", "C")  // Array inmutable      
    ```

  En Kotlin el uso de arrays es muy similar al de las listas.  Puedes acceder a los elementos de un array usando el operador de indexación (`[]`). Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")
    println(array[0])  // Imprime "A"
    ```

  También puedes modificar los elementos de un array usando el operador de indexación. Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")
    array[0] = "D"
    println(array[0])  // Imprime "D"
    ```
  Los arrays también tienen un método `size` que devuelve el número de elementos en el array. Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")
    println(array.size)  // Imprime 3
    ```

  Los arrays también tienen un método `get` que devuelve el elemento en el índice especificado. Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")
    println(array.get(0))  // Imprime "A"
    ```

  Los arrays también tienen un método `set` que establece el elemento en el índice especificado. Por ejemplo:

    ```kotlin
    val array = arrayOf("A", "B", "C")
    array.set(0, "D")
    println(array.get(0))  // Imprime "D"
    ```

  Los arrays también tienen un método `contains` que devuelve `true` si el array contiene el elemento especificado. Por ejemplo:

   ```kotlin
    val array = arrayOf("A", "B", "C")
    println(array.contains("A"))  //
    ```

Por tanto, la principal diferencia entre un Array y una List en Kotlin radica en su tamaño y mutabilidad:

- **Tamaño**:   

  * Array: El tamaño de un Array es fijo una vez que se ha inicializado. No puedes agregar o eliminar elementos.
  * List: Las listas pueden ser fijas (inmutables) o variables (mutables). Una List inmutable (listOf) no permite modificar su tamaño ni sus elementos, mientras que una MutableList (mutableListOf) permite tanto cambiar elementos existentes como agregar o quitar elementos, modificando así su tamaño.

- **Mutabilidad**:   

  * Array: Puede modificar los elementos existentes (es mutable en sus elementos), pero no su tamaño.
  * List: Dependiendo de si es una List o MutableList, puede ser inmutable (no permite modificaciones en sus elementos ni en tamaño) o mutable (permite todo tipo de modificaciones).

- **Uso**:  

  * Array: Más adecuado para tamaños fijos y operaciones de bajo nivel, donde el tamaño es conocido y no cambiará.
  * List: Preferible para colecciones cuyo tamaño puede cambiar, o cuando se necesita una colección inmutable.
  
- **Tipos de Datos**:   

  * Array: Puede almacenar tipos primitivos de manera más eficiente (como IntArray, ByteArray).
  * List: Trabaja con objetos, incluso para tipos primitivos (como List<Int>).

Resumiendo, si necesitas una colección de tamaño fijo o eficiencia para tipos primitivos, un Array puede ser la mejor elección. Si requieres flexibilidad en el tamaño o quieres trabajar con colecciones inmutables, entonces una List sería más adecuada.


### 1.7. Como crear listas

En Kotlin, hay varias formas de crear listas. Cada una tiene sus propias características y usos, y es importante conocerlas para poder elegir la más adecuada para cada situación. Veamos cómo crear listas en Kotlin:
1. **Listas Inmutables Vacías**: Para crear una lista inmutable y vacía, usas `emptyList`. Por ejemplo:
    ```kotlin
    val emptyList = emptyList<String>() // Una lista vacía de Strings
   ```
2. **Listas Inmutables**: Usas `listOf` para crear listas inmutables. Si tienes `val readOnlyList = listOf("John", "Doe")`, no puedes agregar o quitar elementos de `readOnlyList`. `listOfNotNull` se usa para excluir nulos, como en `val filteredList = listOfNotNull("A", "B", null)`, resultando en una lista con "A" y "B" solamente.
3. **Listas Mutables**: Con `mutableListOf`, creas listas a las que puedes agregar o quitar elementos después. Por ejemplo:

   ```kotlin
   var mutableList = mutableListOf("Sydney", "Tokyo")
   mutableList.add("New York") // Ahora mutableList contiene Sydney, Tokyo y New York
   ```

   `arrayListOf` es similar, pero específicamente crea un `ArrayList`.
4. **Conversión a Listas**: Puedes convertir otras estructuras como `Map` a `List` con `toList`. Por ejemplo, al convertir un `Map` de direcciones:

   ```kotlin
   val userAddressMap = mapOf("A" to "India", "B" to "Australia")
   val addressList = userAddressMap.toList() // Convierte el Map a una List de Pares
   ```
5. **Constructores de Listas**: `List(size) { lambda }` crea una lista inmutable con un tamaño definido y elementos inicializados por la lambda. `MutableList` es similar pero mutable. Por ejemplo:

   ```kotlin
   val myList = List(3) { it * 2 } // Crea una lista [0, 2, 4]
   ```

   `buildList` permite construir una lista inmutable con un bloque mutable. Ejemplo:

   ```kotlin
   val builtList = buildList {
       add("One")
       add("Two")
   } // Crea una lista ["One", "Two"]
   ```

Cada uno de estos métodos tiene usos específicos, dependiendo de si necesitas modificar la lista después de su creación o si necesitas inicializarla de una manera particular.

### 2.7 Listas de listas

Crear matrices o listas bidimensionales en Kotlin es bastante sencillo. Una lista bidimensional es básicamente una lista de listas. Aquí te muestro cómo puedes hacerlo:

1. **Creación de una Lista Bidimensional Manualmente**: Puedes crear una lista bidimensional manualmente definiendo una lista de listas. Por ejemplo, para crear una matriz 2x3:

   ```kotin
   val matriz = listOf(
       listOf(1, 2, 3),
       listOf(4, 5, 6)
   )
   // Aquí matriz es una lista de dos listas, cada una con tres elementos.
   ```
2. **Creación Dinámica**: Si quieres crear una matriz con tamaños dinámicos, puedes usar bucles para inicializarla. Por ejemplo, crear una matriz de 3x3:

   ```kotin
   val filas = 3
   val columnas = 3
   val matrizDinamica = List(filas) { MutableList(columnas) { 0 } }
   // Crea una matriz 3x3 con todos los elementos inicializados a 0.
   ```
3. **Acceso y Modificación de Elementos**: Puedes acceder o modificar los elementos de la matriz usando índices. Por ejemplo, para cambiar un elemento:

   ```kotin
   matrizDinamica[0][1] = 10  // Cambia el segundo elemento de la primera fila a 10
   ```

   Y para leer un elemento:

   ```kotin
   val elemento = matrizDinamica[0][1]  // Lee el segundo elemento de la primera fila
   ```
4. **Iteración sobre Elementos**: Puedes iterar sobre los elementos de la matriz utilizando bucles anidados:

   ```kotin
   for (fila in matrizDinamica) {
       for (elemento in fila) {
           println(elemento)
       }
   }
   ```

Estas son las formas básicas de trabajar con matrices o listas bidimensionales en Kotlin. Puedes adaptar estos ejemplos según tus necesidades específicas, como cambiar el tipo de datos almacenados o modificar la forma de inicialización.

## 3. Reference

* [https://kotlinlang.org/docs/reference/](https://kotlinlang.org/docs/reference/)
* [https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209](https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209)
* [https://www.packtpub.com/application-development/programming-kotlin](https://www.packtpub.com/application-development/programming-kotlin)
* [https://learnxinyminutes.com/docs/kotlin/](https://learnxinyminutes.com/docs/kotlin/)
* [https://gist.github.com/dodyg/5823184](https://gist.github.com/dodyg/5823184)
* [https://gist.github.com/dodyg/5616605](https://gist.github.com/dodyg/5616605)
* [https://github.com/Zhuinden/guide-to-kotlin](https://github.com/Zhuinden/guide-to-kotlin)
* [https://superkotlin.com/kotlin-mega-tutorial/](https://superkotlin.com/kotlin-mega-tutorial/)
* [https://revilofe.github.io/IESRA-DAM-Prog/#/](https://revilofe.github.io/IESRA-DAM-Prog/#/)

## 4. Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)
