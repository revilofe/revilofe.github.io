## Polimorfismo en la Herencia

Para explicar este concepto, primero crearemos una clase `Padre` con la propiedad `numAleatorio` y los métodos `dameNumero()` y `dameTamanio()`. 
Luego, crearemos la clase `Hija` que hereda de `Padre` y tiene sus propios atributos y métodos.

* Clase Padre:

```kotlin
import kotlin.random.Random

open class Padre {
    val numAleatorio: Int = Random.nextInt(100, 1000)

    open fun dameNumero(): Int {
        return numAleatorio
    }

    fun dameTamanio(texto: String): Int {
        return texto.length
    }
}
```

En este código, la clase `Padre` genera un número aleatorio al inicializarse. La función `dameNumero()` simplemente devuelve ese número, 
y la función `dameTamanio()` devuelve la longitud del texto recibido.

* Clase Hija:

```kotlin
class Hija(var descripcion: String = "Clase Derivada") : Padre() {
    var contador: Int = 0

    override fun dameNumero(): Int {
        contador++
        println("Mostramos descripcion desde la función dameNumero() -> $descripcion")
        return contador
    }

    fun muestraDescripcion() {
        println(descripcion)
    }
}
```

La clase `Hija` hereda de `Padre` y sobreescribe el método `dameNumero()` para incrementar y devolver el valor de 
su propio contador y también mostrar por pantalla su propiedad `descripcion`. 
También tiene un método `muestraDescripcion()` que imprime su descripción.

* Programa principal:

```kotlin
fun main() {
    val padre1 = Padre()
    println("Info de padre1:")
    println("--------------")
    println("dameNumero() en padre: ${padre1.dameNumero()}")
    println("numAleatorio = ${padre1.numAleatorio}")
    println("numAleatorio = ${padre1.numAleatorio}")
    println("numAleatorio = ${padre1.numAleatorio}")
    println("dameTamanio('padre1 como Padre') = ${padre1.dameTamanio("padre1 como Padre")}")

    println()

    val padre2 : Padre = Hija()
    println("Info de padre2:")
    println("--------------")
    println("dameNumero() en padre2: ${padre2.dameNumero()}")
    println("numAleatorio = ${padre2.numAleatorio}")
    println("dameNumero() en padre2: ${padre2.dameNumero()}")
    println("dameNumero() en padre2: ${padre2.dameNumero()}")
    println("dameNumero() en padre2: ${padre2.dameNumero()}")
    println("numAleatorio = ${padre2.numAleatorio}")
    println("dameTamanio('padre2 como Padre instanciado con Hija()') = ${padre2.dameTamanio("padre2 como Padre instanciado con Hija()")}")
    
    // El objeto padre2 es de tipo Padre y no puede llamar a muestraDescripcion(), 
    // que es un método propio de la clase Hija
    // padre2.muestraDescripcion()
    // Tampoco puede acceder directamente a contador, ya que es una propiedad 
    // de la clase Hija.
    //println("contador = ${padre2.contador}")
}
```

En la función `main`, creamos ***instancias*** de ambas clases y mostramos sus comportamientos mediante llamadas a sus métodos.

  ```
  Nota: La clase `Hija` no puede acceder directamente a `numAleatorio` de `Padre` si fuera privada, así que en este caso, `numAleatorio` 
  está declarada como pública. 
  
  Además, el método `dameNumero()` en la clase `Hija` sobreescribe el método de la clase `Padre`, lo cual se permite en Kotlin gracias a 
  que la clase `Padre` y el método `dameNumero()` están marcados como `open`.
  ```

Si ejecutamos el programa, lo que estámos observando es un concepto central en la programación orientada a objetos llamado ***"polimorfismo"***. 
Este concepto permite que una variable de un tipo de clase `base` *(superclase)* pueda referenciar a un objeto de una clase `derivada` *(subclase)*, 
y al llamar a métodos sobrescritos, se invocarán las implementaciones de la `subclase`.

En nuestro caso, tenemos:

```kotlin
val padre2: Padre = Hija()
```

Aquí, `padre2` es una referencia de tipo `Padre`, pero apunta a una instancia de `Hija`. 
Esto es posible porque `Hija` es una subclase de `Padre` y, por lo tanto, hereda todas sus propiedades y comportamientos. 
Sin embargo, al sobrescribir el método `dameNumero()` en `Hija`, cuando este método se llama en la instancia `padre2`, 
se ejecuta la versión de `Hija` del método, no la de `Padre`. ***Esto es una manifestación de polimorfismo***.

Cuando hacemos llamadas a métodos a través de una referencia de tipo `Padre`, como `padre2`, sucede lo siguiente:

1. **Acceso a Métodos y Propiedades:**
    - Si el método o la propiedad existe en la clase `Padre` y no está sobrescrito en `Hija`, se accede a la versión de `Padre`.
    - Si el método está sobrescrito en `Hija`, como `dameNumero()`, se accede a la versión de `Hija`,
      incluso si la llamada se realiza a través de una referencia de tipo `Padre`.

2. **Acceso Restringido a Miembros Específicos de la Subclase:**
    - No podemos acceder directamente a miembros específicos de `Hija` (como `contador` o `muestraDescripcion()`) a través de una
      referencia de tipo `Padre` sin un casting explícito. Esto es porque, según la definición de `Padre`, esos miembros no existen.

En resumen, el tipo de la referencia *(`Padre` en este caso)* determina qué propiedades y métodos están accesibles. 
Sin embargo, el tipo real del objeto al que apunta la referencia *(una instancia de `Hija`)* determina qué implementaciones de 
métodos se ejecutan cuando se invocan. 

Esto permite el diseño de sistemas flexibles y extensibles donde puedes usar objetos de diferentes subclases de manera intercambiable, 
siempre que compartan una interfaz común definida por su clase base.

*** Casting

Si ahora en el `main` realizamos un ***Casting*** de `padre2` como `Hija`:

```kotlin
fun main() {

    ...    

    // Casting de padre2 a Hija en línea para llamar a
    // contador y muestraDescripcion() directamente.
    val padre2ComoHija = (padre2 as Hija)
    println("Info de padre2ComoHija:")
    println("--------------")
    println("dameNumero() en padre2ComoHija: ${padre2ComoHija.dameNumero()}")
    println("dameNumero() en padre2ComoHija: ${padre2ComoHija.dameNumero()}")
    println("dameNumero() en padre2ComoHija: ${padre2ComoHija.dameNumero()}")
    padre2ComoHija.muestraDescripcion()
    println("contador = ${padre2ComoHija.contador}")
    println("numAleatorio = ${padre2ComoHija.numAleatorio}")
    println("numAleatorio = ${padre2ComoHija.numAleatorio}")
    println("dameTamanio('padre2 con Casting a Hija') = ${padre2ComoHija.dameTamanio("padre2 con Casting a Hija")}")
}
```

La capacidad de `padre2ComoHija` para acceder a `numAleatorio` directamente después del casting a `Hija` se debe a cómo funciona la herencia en la POO. 
Cuando hacemos un casting de una referencia de una clase base (`Padre`) a una clase derivada (`Hija`), no estamos cambiando el objeto en sí, 
sino cómo nos referimos a ese objeto en nuestro código.

Aquí están los puntos clave:

1. **Herencia:**
   - `Hija` es una subclase de `Padre`, lo que significa que una instancia de `Hija` hereda todos los campos y métodos públicos o protegidos de `Padre`.
     En nuestro caso, `numAleatorio` es un campo público en `Padre`, por lo que también es accesible a través de cualquier instancia de `Hija`.

2. **Casting:**
   - Al hacer `(padre2 as Hija)`, estamos diciéndole al compilador: "Trata `padre2`, que sabes que es de tipo `Padre`, como si fuera de tipo `Hija`".
     Esto es seguro porque `padre2` es realmente una instancia de `Hija`. Después de este casting, podemos acceder, no solo a los miembros de `Hija`,
     sino también a todos los miembros accesibles de `Padre` (como `numAleatorio`) a través de la referencia `padre2ComoHija`.

3. **Acceso a los Miembros de Clase:**
   - `numAleatorio` es un miembro de `Padre` que es accesible en `Hija` debido a la herencia. Cuando hacemos el casting de `padre2` a `Hija`,
     estamos simplemente proporcionando una referencia de tipo `Hija` al mismo objeto.
     El objeto no cambia, ni sus miembros. Por lo tanto, `padre2ComoHija` tiene acceso a `numAleatorio` porque `Hija` tiene acceso a los miembros
     públicos de `Padre`.

El hecho de que podamos acceder a `numAleatorio` a través de `padre2ComoHija` es un reflejo de estos principios de herencia y polimorfismo en la 
programación orientada a objetos. El objeto no ha cambiado, solo la forma en que nos referimos a él en nuestro código, permitiéndonos acceder a  
más de sus funcionalidades a través del tipo más específico (`Hija`).
