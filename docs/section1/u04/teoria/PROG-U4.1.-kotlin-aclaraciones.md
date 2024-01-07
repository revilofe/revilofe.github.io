---
title: "UD 4 - 4.1 kotlin"
description: kotlin
summary: kotlin
authors:
    - Eduardo Fdez
date: 2022-11-14
icon: 
permalink: /prog/unidad4/4.1
categories:
    - PROG
    - kotlin
tags:
    - Software
    - kotlin
---
# Aclaraciones sobre [Kotlin]

En este punto vamos a ver algunas aclaraciones sobre el lenguaje de programación [Kotlin]. Se basa en las principales dudas que nos pueden surgir al empezar a programar en este lenguaje y que han sido extraídas de las preguntas que el alumnado ha realizado durante los distintos cursos.

## Aclaraciones sobre el lenguaje

### Funciones lambda

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

### Notación de llamado las funciones cuando se utilizan lambdas

En Kotlin, cuando llamas a una función que toma una lambda como parámetro, puedes usar dos formas: con o sin paréntesis. La que ya mostré es la forma sin paréntesis, pero si prefieres usar paréntesis, puedes hacerlo también. Aquí te muestro cómo sería:

```kotlin
val numeros = listOf(1, 2, 3, 4, 5)
val pares = numeros.filter({ it % 2 == 0 }) //tambien se puede poner numeros.filter { it % 2 == 0 }
println(pares)  // Esto imprimirá: [2, 4]
```

En esta versión, simplemente colocas la lambda entre paréntesis después de `filter`. Funciona exactamente igual que la versión sin paréntesis. Es más una cuestión de estilo y preferencia personal que de funcionalidad.

En Kotlin, cuando una función tiene una lambda como último parámetro, puedes optar por usar la "sintaxis de lambda fuera de los paréntesis", que es lo que hicimos en los ejemplos de más arriba. Pero si te sientes más cómodo con los paréntesis, ¡adelante!

### ¿Qué es un receiver en kotlin?

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

### ¿Qué es `it` en kotlin?

En Kotlin, `it` es un nombre implícito que se usa para referirse al parámetro único de una lambda cuando dicho parámetro no se declara de manera explícita. Es una forma conveniente y concisa de trabajar con lambdas que solo requieren un parámetro. Aquí te explico un poco más:

1. **Uso en Lambdas**: Cuando tienes una lambda que acepta un solo parámetro, puedes usar `it` para referirte a ese parámetro sin necesidad de declararlo. Por ejemplo:

   val lista = listOf(1, 2, 3)
   val cuadrados = lista.map { it * it }

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

## Reference

* [https://kotlinlang.org/docs/reference/](https://kotlinlang.org/docs/reference/)
* [https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209](https://code.tutsplus.com/series/kotlin-from-scratch--cms-1209)
* [https://www.packtpub.com/application-development/programming-kotlin](https://www.packtpub.com/application-development/programming-kotlin)
* [https://learnxinyminutes.com/docs/kotlin/](https://learnxinyminutes.com/docs/kotlin/)
* [https://gist.github.com/dodyg/5823184](https://gist.github.com/dodyg/5823184)
* [https://gist.github.com/dodyg/5616605](https://gist.github.com/dodyg/5616605)
* [https://github.com/Zhuinden/guide-to-kotlin](https://github.com/Zhuinden/guide-to-kotlin)
* [https://superkotlin.com/kotlin-mega-tutorial/](https://superkotlin.com/kotlin-mega-tutorial/)
* [https://revilofe.github.io/IESRA-DAM-Prog/#/](https://revilofe.github.io/IESRA-DAM-Prog/#/)

## Fuente

* [Apuntes de kotlin](https://github.com/alxgcrz/_kotlin_)
* [Kotlinlang](https://kotlinlang.org)

## License

[![Licencia de Creative Commons](https://i.creativecommons.org/l/by-sa/4.0/80x15.png)](http://creativecommons.org/licenses/by-sa/4.0/)
Esta obra está bajo una [licencia de Creative Commons Reconocimiento-Compartir Igual 4.0 Internacional](http://creativecommons.org/licenses/by-sa/4.0/).
