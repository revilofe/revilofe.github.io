---
title: Atributos de clase vs Propiedades.

description: Diferencia entre atributo de clase y propiedad.

authors:
    - Eduardo Fdez.

date: 2024-02-05

tags:
  - atributo de clase
  - propiedad
  - kotlin
---
# Atributos de clase vs Propiedades

En el vasto universo de la programación, el manejo de las propiedades y atributos de clase es un pilar fundamental que varía significativamente entre diferentes lenguajes. 
Esta dicotomía es particularmente intrigante en Kotlin, un lenguaje que entrelaza de manera única estos conceptos, presentando un enfoque distintivo que se distancia de 
otros lenguajes de programación más tradicionales. En este contexto, exploraremos en profundidad cómo Kotlin redefine la gestión de propiedades y atributos de clase, 
contrastándolo con su contraparte en C#, donde la distinción entre ambos es más evidente y ortodoxa.

A continuación, se desglosarán las diferencias fundamentales y las similitudes entre estas dos potencias de la programación, enfocándonos en cómo cada una maneja la encapsulación, 
la validación y el control de acceso a los datos de una clase. Con el fin de ilustrar estos conceptos de manera práctica, se presentará un ejemplo comparativo, 
demostrando cómo se definen y se manipulan los atributos de clase y las propiedades en C# y en Kotlin. Este análisis no solo resaltará las peculiaridades sintácticas y 
estructurales de cada lenguaje sino que también profundizará en la filosofía de diseño y los patrones de programación que cada uno promueve, proporcionando así una comprensión 
integral de sus capacidades y idiosincrasias.

### C#

En C#, un atributo de clase es una variable que pertenece a la clase, mientras que una propiedad es una forma de acceder y 
controlar el acceso a ese atributo. Las propiedades pueden ofrecer un control más detallado sobre cómo se accede o se modifica 
un atributo, por ejemplo, validando datos antes de asignarlos.

Esto un ejemplo simple de cómo definir un atributo de clase y su propiedad:

```csharp
using System;

public class Coche
{
    // Atributo de clase privado
    private string color;

    // Propiedad pública para acceder y asignar el atributo 'color'
    public string Color
    {
        get
        {
            // Aquí se puede agregar lógica adicional al obtener el color
            return color;
        }
        set
        {
            // Aquí se puede validar el valor antes de asignarlo al atributo 'color'
            if (value == null)
                throw new ArgumentNullException("El color no puede ser nulo.");
            else
                color = value;
        }
    }
    
    // Constructor de la clase
    public Coche(string inicialColor)
    {
        // Asignar un color inicial al coche a través de la propiedad
        Color = inicialColor;
    }
}

class Program
{
    static void Main()
    {
        // Crear una instancia de Coche con un color inicial
        Coche miCoche = new Coche("Rojo");
        
        // Mostrar el color actual del coche
        Console.WriteLine("El color del coche es: " + miCoche.Color);
        
        // Cambiar el color del coche
        miCoche.Color = "Azul";
        
        // Mostrar el nuevo color del coche
        Console.WriteLine("El nuevo color del coche es: " + miCoche.Color);
    }
}
```

En este ejemplo, `color` es un atributo de clase privado de la clase `Coche`. La propiedad `Color` permite acceder y modificar el atributo `color`. 
Nota cómo la propiedad `Color` proporciona un método `get` para obtener el valor del color y un método `set` para cambiar el color, incluyendo una 
validación para asegurarse de que el nuevo color no sea nulo antes de asignarlo al atributo `color`.

### Kotlin

Ahora realizamos el mismo código en Kotlin y después mostramos las diferencias.

```kotlin
class Coche(inicialColor: String) {
    // Atributo de clase con propiedad incorporada
    var color: String = inicialColor
        set(value) {
            // Validar el valor antes de asignarlo al atributo 'color'
            if (value.isEmpty()) {
                throw IllegalArgumentException("El color no puede estar vacío.")
            }
            field = value
        }
    
    init {
        // Validación adicional o lógica de inicialización si es necesario
    }
}

fun main() {
    // Crear una instancia de Coche con un color inicial
    val miCoche = Coche("Rojo")
    
    // Mostrar el color actual del coche
    println("El color del coche es: ${miCoche.color}")
    
    // Cambiar el color del coche
    miCoche.color = "Azul"
    
    // Mostrar el nuevo color del coche
    println("El nuevo color del coche es: ${miCoche.color}")
}
```

Diferencias y características de Kotlin en relación con C# en este contexto:

1. **Propiedades Incorporadas**:
    - Kotlin maneja atributos de clase y propiedades como una sola entidad, a diferencia de C# que los maneja por separado.
      En Kotlin, al definir un `var` (variable mutable) o `val` (variable inmutable), estás creando automáticamente una propiedad
      con su getter y setter correspondiente. Esto reduce la cantidad de código necesario para definir propiedades simples.

2. **Palabras Clave `field`**:
    - En el setter de Kotlin, usas `field` para referirte al respaldo del campo de la propiedad. Es una palabra clave especial
      que solo se puede usar dentro de los accesores de las propiedades (getters y setters).

3. **Inicialización de Propiedades**:
    - En Kotlin, las propiedades pueden ser inicializadas directamente en su declaración o en el bloque de inicialización `init`.
      Esto ofrece una sintaxis más concisa y clara.

4. **Verificación de Nulos y Validación**:
    - Kotlin tiene un sistema de tipos que distingue entre referencias que pueden ser nulas y las que no pueden serlo.
      En este ejemplo, el tipo `String` no admite nulos. Si se intenta asignar un valor nulo a `color`, el programa no compilará.
    - La validación en el `setter` se hace de manera similar a C#, pero lanzando una `IllegalArgumentException` si el valor es inválido.

5. **Sintaxis de Funciones y Clases**:
    - La sintaxis de Kotlin es más concisa. Por ejemplo, no es necesario especificar el tipo de retorno para funciones que no retornan un valor (equivalente a `void` en C#).

Kotlin, con su diseño moderno, ofrece un enfoque más compacto y expresivo, especialmente útil para definir propiedades y realizar validaciones. 
El idioma promueve un código más seguro y menos propenso a errores en tiempo de ejecución gracias a su manejo de nulos y su sistema de tipos.
