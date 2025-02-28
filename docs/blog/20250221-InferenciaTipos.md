---
title: Inferencia de tipos.

description: Inferencia de tipos de datos en tiempo de compilación.

authors:
    - Diego Cano.

date: 2025-02-21

tags:
  - kotlin
  - tipo dato
  - compilación
---

# Inferencia de tipos

La **inferencia de tipos** es la capacidad del compilador para **deducir automáticamente** el tipo de una variable o expresión sin que tengas que especificarlo explícitamente. Es decir, Kotlin analiza el código y asigna un tipo adecuado **sin necesidad de que lo declares manualmente**.

Kotlin es un lenguaje **fuertemente tipado**, pero gracias a la inferencia de tipos, permite escribir código más limpio y sin redundancias, evitando que tengas que indicar los tipos en todas partes.

## 1. Ejemplo básico de inferencia de tipos

En Kotlin, puedes declarar variables con `val` o `var` sin especificar el tipo explícitamente:

```kotlin
val numero = 10   // El compilador infiere que es de tipo Int
val texto = "Hola Kotlin"   // El compilador infiere que es de tipo String
val esActivo = true   // El compilador infiere que es de tipo Boolean
```

Equivalente a:

```kotlin
val numero: Int = 10
val texto: String = "Hola Kotlin"
val esActivo: Boolean = true
```

En ambos casos, el tipo **es el mismo**, pero en el primer caso, **el compilador lo infiere automáticamente**.

## 2. Inferencia en funciones
La inferencia de tipos también funciona en **funciones**:

```kotlin
fun sumar(a: Int, b: Int) = a + b   // El compilador infiere que retorna un Int
```

Equivalente a:

```kotlin
fun sumar(a: Int, b: Int): Int = a + b
```

El compilador sabe que `a + b` es una suma de enteros, por lo que **no es necesario especificar el tipo de retorno**.

## 3. Inferencia en listas y colecciones
Cuando se crean listas o mapas sin especificar el tipo, el compilador infiere el tipo más adecuado:

```kotlin
val lista = listOf(1, 2, 3)  // Infiere List<Int>
val mapa = mapOf(1 to "Uno", 2 to "Dos")  // Infiere Map<Int, String>
```

Si intentas mezclar tipos en la lista:

```kotlin
val listaMixta = listOf(1, "Dos", 3.0)  // Infiere List<Any>
```

El compilador infiere el **tipo más genérico posible (`Any`)**, ya que la lista contiene enteros, cadenas y decimales.

## 4. Inferencia avanzada: Intersección de tipos (`&`)
En algunos casos, cuando un objeto puede ser de más de un tipo, **Kotlin infiere la intersección de tipos** para permitir el acceso a métodos de ambos tipos.

Ejemplo:

```kotlin
interface A { fun metodoA() }
interface B { fun metodoB() }

class MiClase : A, B {
    override fun metodoA() { println("Ejecutando metodoA") }
    override fun metodoB() { println("Ejecutando metodoB") }
}

fun procesar(obj: A & B) {
    obj.metodoA()
    obj.metodoB()
}

val miObjeto = MiClase()
procesar(miObjeto)  // El compilador infiere que miObjeto es A & B
```

🔹 Kotlin **infiera automáticamente `A & B`** al pasar `miObjeto` a la función `procesar`, lo que permite acceder a métodos de ambas interfaces **sin necesidad de hacer casting**.

---

## **Beneficios de la inferencia de tipos**
   **Código más limpio**: Evita redundancias en las declaraciones.  
   **Menos errores**: Reduce la posibilidad de errores por tipos incorrectos.  
   **Mayor flexibilidad**: Permite trabajar con expresiones complejas sin necesidad de definir tipos manualmente.  
   **Más eficiente**: Kotlin puede optimizar mejor el código basándose en los tipos inferidos.

---

## **Conclusión**
La inferencia de tipos es una **característica clave en Kotlin** que permite escribir código más conciso y legible. Aunque puedes declarar los tipos manualmente, en la mayoría de los casos **el compilador los infiere automáticamente**.

Si quieres que Kotlin infiera correctamente los tipos más adecuados, debes:
   - **Declarar las variables con valores iniciales adecuados.**
   - **Entender que la inferencia ocurre en tiempo de compilación.**
   - **Saber que en algunos casos puede ser necesario declarar explícitamente un tipo si el compilador no infiere correctamente.**
