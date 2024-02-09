---
title: "UD 3 - 3.3 Depuración"
description: Depuración
summary: Depuración
authors:
  - Eduardo Fdez
date: 2023-01-15
icon:   
permalink: /edes/unidad3/3.3
categories:
  - EDES
tags:
  - EDES
  - Software
  - Debug
---
## Depuración

Una de las habilidades más importantes que adquirirá cuando esté aprendiendo a programar es la depuración. Aunque puede ser frustrante, la depuración es una de las partes más intelectualmente gratificantes, desafiantes e interesantes de la programación.

La depuración puede ser vista como un trabajo de detective. El programador se enfrenta a pistas y tiene que inferir los procesos y eventos que generaron los resultados que ve.

La depuración también es como una ciencia experimental. Una vez que se tiene una idea de lo que está mal, se modifica el programa y se intenta nuevamente. Si la hipótesis era correcta, se puede predecir el resultado de la modificación y así estar un paso más cerca de un programa totalmente funcional. Si la hipótesis era incorrecta, se tiene que encontrar una nueva. Como Sherlock Holmes señaló:

> Cuando todo aquello que es imposible ha sido eliminado, lo que quede, por muy improbable que parezca, es la verdad.
> — A. Conan Doyle

Para algunas personas, la programación y la depuración son lo mismo. Es decir, la programación es el proceso de depurar gradualmente un programa hasta que haga lo que desea. Lo ideal es comenzar con un programa que funcione y hacer pequeñas modificaciones, depurándolas a medida que avanza.

A medida que comience a escribir programas más extensos, es posible que pase más tiempo depurando. Más código significa más posibilidades de cometer un error y más lugares dónde se pueden esconder los errores.

### Uso de println y logging para depurar
Muchos programadores principiantes utilizan la técnica de depuración más simple y efectiva: agregar al programa sentencias de impresión a consola. Por ejemplo, si no está seguro de qué valor tiene una variable, puede imprimirlo en la consola para verlo.

```kotlin
fun main() {
    val x = 5
    val y = 7
    val z = x + y
    println("z es $z")
}
```
Mostrar el valor de `z` en la consola le permitirá ver si el cálculo es correcto. Si no lo es, puede mostrar los valores de `x` e `y` para ver si son correctos. Si no lo son, puede mostrar los valores de las variables que los inicializan, y así sucesivamente. Este tipo de salida se llama **trazas**.

Mostrar la información de depuración en la consola es una técnica efectiva, pero tiene dos desventajas.        

- La primera es que a veces es difícil encontrar el equilibrio entre mostrar demasiada información y no mostrar suficiente. Si muestra demasiada información, la consola se llenará de mensajes y será difícil encontrar lo que está buscando. Si no muestra suficiente información, puede pasar por alto la pista que necesita.
- La segunda desventaja es que, una vez que haya encontrado y corregido el error, debe eliminar o comentar las sentencias de impresión. Si no lo hace, el programa se llenará de mensajes de depuración que no necesita. Esto no es un problema en programas pequeños, pero en programas grandes, puede ser difícil recordar qué mensajes de depuración son importantes y cuáles no.

El uso de sistemas de registro o logging es una técnica más avanzada que puede ayudar a superar estas desventajas. En lugar de imprimir mensajes en la consola, puede registrarlos en un archivo. Esto le permite controlar la cantidad de información que se muestra y le permite activar o desactivar los mensajes de depuración sin tener que modificar el código.

Los sistemas de registro también pueden mostrar mensajes de depuración en diferentes niveles. Por ejemplo, puede mostrar mensajes de depuración solo cuando está depurando un programa, pero no cuando está en producción. O puede mostrar mensajes de depuración solo cuando ocurre un error. O puede mostrar mensajes de depuración solo cuando ocurre un error y solo en ciertas partes del programa.

Los niveles de registro son una forma de controlar la cantidad de información que se muestra. Los niveles de registro más comunes son:
- **DEBUG**: mensajes de depuración que muestran información detallada sobre el estado del programa.
- **INFO**: mensajes informativos que muestran información sobre el estado del programa.
- **WARN**: mensajes de advertencia que muestran información sobre un posible problema.
- **ERROR**: mensajes de error que muestran información sobre un problema que ha ocurrido.
- **FATAL**: mensajes de error que muestran información sobre un problema que ha causado que el programa se detenga.
- **TRACE**: mensajes de depuración que muestran información detallada sobre el estado del programa.
- **OFF**: no se muestran mensajes de registro.
- **ALL**: se muestran todos los mensajes de registro.

los sistemas de registro también pueden mostrar mensajes de depuración en diferentes partes del programa. Por ejemplo, puede mostrar mensajes de depuración solo en ciertas clases o paquetes. O puede mostrar mensajes de depuración solo en ciertas partes del programa, como cuando se ejecuta una función específica.

Los lenguajes de programación modernos suelen tener bibliotecas de registro que facilitan el uso de sistemas de registro. Por ejemplo, Kotlin tiene una biblioteca de registro llamada `logback`. Esta biblioteca le permite controlar la cantidad de información que se muestra y le permite mostrar mensajes de depuración en diferentes niveles y partes del programa.

### Depuración por bisección

Una forma de reducir el tiempo de depuración es la técnica denominada "depurar por bisección". Por ejemplo, si hay 100 líneas en su programa y las revisa una a la vez, serían 100 revisiones.

Es mejor tratar de dividir el problema en dos. Busque en la mitad del programa o un valor intermedio que pueda verificar. Agregue una sentencia de impresión (o algo que permita verificar) y ejecute el programa.

Si esta verificación es incorrecta, debe haber un problema en la primera mitad del programa. Si es correcta, el problema está en la segunda mitad.

Cada vez que realiza una verificación como esta, reduce a la mitad el número de líneas que debe revisar. Después de seis pasos (que es mucho menos que 100), se reduciría a una o dos líneas de código, al menos en teoría.

En la práctica, no siempre se conoce dónde está la "mitad del programa", y no siempre es posible verificarlo. No tiene sentido contar líneas y encontrar el punto medio exacto. En su lugar, piense en los lugares del programa donde puede haber errores y en los lugares donde es fácil verificar. Luego, elija un lugar en donde usted crea que las posibilidades de encontrar un error antes o después de esta verificación son más o menos las mismas.

### Depuración de patito de goma

Otra técnica de depuración es la "depuración del patito de goma". Si está atascado en un problema, si le explica el problema a otra persona, a veces puede encontrar la respuesta incluso antes de terminar de hacer la pregunta. Generalmente no es necesaria otra persona, incluso se podría hablar con un pato de goma. Sí, un patito de goma. Es una técnica que a menudo funciona. Incluso si no resuelve el problema, puede ayudar a aclarar el problema. Este es el origen de la conocida estrategia llamada depuración del pato de goma. Esto es real, vea https://en.wikipedia.org/wiki/Rubber_duck_debugging.

El método de depuración del patito de goma es un término informal utilizado en ingeniería de software para describir un método de revisión de código. El nombre es una referencia a una historia del libro The Pragmatic Programmer en donde un programador toma un patito de goma y revisa su código forzándose a sí mismo a explicarlo, línea por línea, al pato. Existen otros muchos términos para esta técnica, que a menudo tienen que ver con objetos inanimados.

Muchos programadores han tenido la experiencia de explicar un problema de programación a alguien más, posiblemente a alguien que no sabe nada sobre programación, y encontrar la solución en el proceso de explicar el problema. Al comparar lo que supuestamente hace el código con lo que hace en realidad, cualquier incongruencia resulta evidente. Usando un objeto inanimado, el programador puede tratar de lograr el mismo efecto sin tener que hablar con otra persona.

### Checks de sanidad y consistencia

Los checks de sanidad y consistencia son una forma de depuración que se realiza durante el desarrollo de software. Estos checks ayudan a prevenir errores lógicos y asegurar la coherencia de los datos en tus programas.

**sanity check**, imagina una función que calcula la raíz cuadrada de un número. Un sanity check sería verificar que el número de entrada no sea negativo antes de realizar el cálculo, ya que la raíz cuadrada de un número negativo no es un número real en matemáticas básicas.

```kotlin 
fun calcularRaizCuadrada(numero: Double): Double {
    if (numero < 0) {
        throw IllegalArgumentException("El número no puede ser negativo.")
    }
    return kotlin.math.sqrt(numero)
}
```

Para un **consistency check**, considera una aplicación que gestiona usuarios y sus roles. Un consistency check aseguraría que un usuario no se pueda asignar a un rol que no existe en el sistema.

```kotlin
fun asignarRolAUsuario(usuario: Usuario, rol: String, rolesValidos: List<String>): Boolean {
    if (!rolesValidos.contains(rol)) {
        throw IllegalArgumentException("Rol no válido.")
    }
    usuario.rol = rol
    return true
}
```

Estos ejemplos muestran cómo los checks de sanidad y consistencia ayudan a prevenir errores lógicos y asegurar la coherencia de los datos en tus programas.

### El proceso de depuración

Cuando está depurando un programa, y especialmente si está tratando de resolver un error difícil, hay cinco cosas que puede probar:

1. Lee: Examine su código, léalo y verifique que dice lo que quería decir.
2. Ejecuta: Experimente haciendo cambios y ejecutando diferentes versiones. A menudo, si muestra lo correcto en el lugar correcto del programa, el problema se vuelve obvio, pero para ello a veces tiene que desarrollar andamiaje.
3. Reflexiona: ¡Tómese un tiempo para pensar! ¿Qué tipo de error es: de sintaxis, tiempo de ejecución o semántica? ¿Qué información puede obtener de los mensajes de error o de la salida del programa? ¿Qué tipo de error podría causar el problema que estás viendo? ¿Qué cambió antes de que apareciera el problema?
4. Prueba técnicas que te permitan encontrar el error. Habla con un pato de goma, usa la depuración por bisección, etc.
5. Vuelve atrás: En ocasiones, lo mejor que puede hacer es retroceder, deshacer los cambios recientes hasta regresar a un programa que funcione y que comprenda. Una vez logrado esto, puede comenzar a reconstruir.

Los programadores principiantes a veces se atascan en una de estas actividades y olvidan las otras. Cada actividad viene con su propia forma de fallar.

Por ejemplo, leer su código podría ayudar si el problema es un error tipográfico, pero no si el problema es un malentendido conceptual. Si no comprende lo que hace su programa, puede leerlo 100 veces y nunca ver el error, porque el error está en su cabeza.

Ejecutar experimentos puede ayudar, especialmente si ejecuta pruebas pequeñas y simples, pero si ejecuta experimentos sin pensar o leer su código, puede caer en un patrón llamado "programación de caminata aleatoria", que es el proceso de hacer cambios aleatorios hasta que el programa haga lo correcto. No hace falta decir que la programación de caminata aleatoria puede llevar mucho tiempo.

La persona que programa tiene que tomarse su tiempo para pensar. La depuración es como una ciencia experimental. Debe tener al menos una hipótesis sobre la causa del problema. Si hay dos o más opciones, trate de pensar en una prueba que elimine una de ellas.

Incluso las mejores técnicas de depuración fallarán si hay demasiados errores, o si el código que está tratando de corregir es demasiado grande y complicado. A veces, la mejor opción es volver atrás, simplificando el programa hasta que llegue a algo que funcione y que comprenda. Los programadores principiantes a menudo son reacios a volver atrás porque no pueden soportar eliminar una línea de código (incluso si es incorrecto). Si le hace sentir mejor copie su programa en otro archivo antes de comenzar a eliminarlo. Luego puede copiar las piezas una por una. O lo que es mejor, utilice un sistema de gestión de versiones para poder recuperar versiones anteriores.

Encontrar un error difícil requiere leer, ejecutar, reflexionar y, a veces, volver atrás. Si se queda atascado en una de estas actividades, pruebe las otras.

## Recursos

* [Debugging code](https://www.jetbrains.com/help/idea/debugging-code.html#refreshers)
* [Using breakpoints](https://www.jetbrains.com/help/idea/using-breakpoints.html#breakpoint-statuses)

## Fuente

* [Depuración en IntelliJ Idea una guía para pricipiantes](https://codegym.cc/es/groups/posts/es.243.depuracion-en-intellij-idea-una-guia-para-principiantes)
* [Debugging in IntelliJ Idea a beginners guide](https://codegym.cc/groups/posts/243-debugging-in-intellij-idea-a-beginners-guide)
