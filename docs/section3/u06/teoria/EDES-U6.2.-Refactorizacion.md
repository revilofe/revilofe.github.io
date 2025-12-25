---
title: "UD 6 - 6.2 Refactorización"
description: Refactorización de código
summary: Refactorización de código
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: "material/file-document-outline"
permalink: /edes/unidad6/4.1
categories:
    - EDES
tags:
    - EDES
    - GIT
    - GitHub
---
## 6.2. Malos olores y Refactorización

En el desarrollo de software, los "malos olores" y la refactorización son conceptos clave para mejorar la calidad del código y facilitar su mantenimiento a lo largo del tiempo. Los "malos olores" son señales de problemas en el diseño del código, como duplicación, métodos largos o clases grandes, que pueden dificultar la comprensión y modificación del código. La refactorización, por otro lado, es el proceso de reestructurar el código existente sin cambiar su comportamiento externo, con el objetivo de mejorar su legibilidad, estructura y eficiencia.

### 1. Malos olores (Code Smells)

Los malos olores del código son señales que nos indican que el código fuente no está bien estructurado y que puede ser mejorado, por tanto son síntomas de problemas en el diseño del código fuente que al igual que los malos olores de la vida real, son desagradables y deben ser eliminados.

El término fue acuñado por Kent Beck y popularizado por Martin Fowler en su libro "Refactoring: Improving the Design of Existing Code", se refieren a ciertas características del código que sugieren la necesidad de refactorización. No son errores en sí mismos; el código aún funciona, pero presenta problemas en términos de mantenibilidad, legibilidad, escalabilidad o eficiencia. Identificar estos "malos olores" es el primer paso para mejorar la calidad del código a través de la refactorización.

#### 1.1. Ejemplos de Malos Olores
Aquí algunos ejemplos comunes de "malos olores" en el código:

1. **Duplicación de Código**
Cuando el mismo código aparece en más de un lugar, cualquier cambio futuro en la lógica podría requerir cambios en múltiples ubicaciones, aumentando el riesgo de inconsistencias.

2. **Métodos Largos**
Un método que hace demasiado o es demasiado largo puede ser difícil de entender y mantener. Idealmente, un método debería realizar una sola función o tarea.

3. **Clase Grande**
Una clase con demasiadas responsabilidades es difícil de entender, mantener y testear. Seguir el principio de responsabilidad única puede ayudar a mantener las clases enfocadas y manejables.

4. **Lista Larga de Parámetros**
Métodos o funciones que requieren una gran cantidad de parámetros pueden ser difíciles de entender y propensos a errores. En algunos casos, es mejor agrupar estos parámetros en un objeto propio.

5. **Comentarios Excesivos**
Si bien documentar el código es importante, una abundancia de comentarios puede indicar que el código no es lo suficientemente claro. Código bien estructurado y nombrado adecuadamente a menudo puede ser autoexplicativo.

6. **Código Muerto**
Código que ya no se utiliza, como métodos, variables o clases no referenciadas, agrega desorden sin proporcionar valor, haciendo más difícil navegar y entender el código base.

7. **Envidia de Características**
Sucede cuando una clase utiliza extensamente los métodos o datos de otra clase. En estos casos, parte de la funcionalidad tal vez pertenezca en realidad a la otra clase.

8. **Cadena de Mensajes**
Ocurre cuando un cliente pregunta a un objeto por otro objeto, que a su vez solicita a otro objeto, creando una cadena de dependencias. Esto viola el principio de ocultamiento de información y puede hacer el sistema frágil a cambios.

9. **Cambio Divergente**
Se da cuando una clase es comúnmente modificada en diferentes maneras por diferentes razones. Si hay múltiples razones para cambiar una clase, tal vez debería dividirse en varias clases.

10. **Cambio de Tiro**
Sucede cuando un cambio en una clase requiere cambios en muchas otras clases. Este patrón de dependencias sugiere una alta interdependencia dentro del código.


### 2. Refactorización (Refactoring)

Refactorizar en el desarrollo de software se refiere al proceso de reestructurar el código existente sin cambiar su comportamiento externo. Este proceso tiene como objetivo mejorar la legibilidad, la estructura y la eficiencia del código, así como facilitar su mantenimiento y expansión futura. La refactorización es una parte esencial de la programación ágil y se realiza de manera continua para asegurar que el código se mantenga limpio, comprensible y adaptable a nuevos requisitos.

#### 2.1. Objetivos de la Refactorización

- **Mejorar la legibilidad**: Hacer el código más fácil de entender para otros desarrolladores (o para uno mismo en el futuro).
- **Reducir la complejidad**: Simplificar secciones complejas del código para hacerlas más manejables.
- **Eliminar código redundante**: Unificar o eliminar repeticiones de código para reducir la posibilidad de errores y facilitar las actualizaciones.
- **Mejorar el rendimiento**: Optimizar ciertas partes del código para hacerlas más eficientes en términos de recursos y tiempo de ejecución.
- **Facilitar las pruebas**: Organizar el código de manera que sea más fácil de probar individualmente (por ejemplo, mediante pruebas unitarias).

#### 2.2. Algunos patrones de Refactorización

1. **Renombrar variables y métodos**: Cambiar nombres de variables, funciones y clases para que reflejen mejor su propósito.   
2. **Extraer métodos**: Convertir fragmentos de código repetitivo en nuevos métodos o funciones.   
3. **Introducir patrones de diseño**: Aplicar patrones de diseño establecidos para resolver problemas comunes de manera más efectiva.   
4. **Optimizar algoritmos**: Cambiar algoritmos por versiones más rápidas o más eficientes.   
5. **Reducir la dependencia entre clases**: Modificar el código para reducir el acoplamiento, aumentando así la modularidad del sistema.   

#### 2.3. Consideraciones Importantes

- **No alterar la funcionalidad**: Uno de los principios clave de la refactorización es que no debe alterar el comportamiento externo del software. Cualquier cambio que introduzca nuevas funcionalidades o altere el comportamiento existente no se considera refactorización, sino una modificación o extensión del código.
- **Realizar pruebas**: Es crucial realizar pruebas exhaustivas antes y después de la refactorización para asegurarse de que no se introduzcan errores en el proceso.

La refactorización es una práctica continua que contribuye a la salud a largo plazo del proyecto de software, facilitando la adaptación a nuevos requisitos y la incorporación de mejoras sin acumular deuda técnica.


### 3. Ejemplo de Malos Olores y Refactorización

Se presenta un ejemplo clásico de código con un "mal olor" en el desarrollo de software, específicamente el "mal olor" conocido como **Duplicación de Código**. La duplicación de código ocurre cuando bloques similares de código aparecen en más de un lugar, lo que puede llevar a errores y dificultades de mantenimiento si el código necesita ser cambiado en el futuro.

#### 3.1. Ejemplo de Duplicación de Código:

Supongamos que tenemos dos métodos en una clase que calculan el salario total de un empleado, pero cada método se utiliza en diferentes contextos dentro de la aplicación.

```kotlin
class CalculadoraSalario {

    fun calcularSalarioMensual(horasTrabajadas: Int, tarifaPorHora: Double): Double {
        val salarioBase = horasTrabajadas * tarifaPorHora
        val bonificacion = salarioBase * 0.10
        return salarioBase + bonificacion
    }

    fun calcularSalarioSemanal(horasTrabajadas: Int, tarifaPorHora: Double): Double {
        val salarioBase = horasTrabajadas * tarifaPorHora
        val bonificacion = salarioBase * 0.10
        return salarioBase + bonificacion
    }
}
```

En este ejemplo, el código para calcular el salario base y la bonificación está duplicado en ambos métodos `calcularSalarioMensual` y `calcularSalarioSemanal`. Aunque estos métodos podrían ser utilizados en diferentes contextos (uno para calcular salarios mensuales y otro para semanales), la lógica de cálculo del salario base y la bonificación es idéntica, lo que representa una duplicación innecesaria.

#### 3.2. Test de la Clase CalculadoraSalario

Los test nos garantizan que la refactorización no afecte la funcionalidad de los métodos `calcularSalarioMensual` y `calcularSalarioSemanal`. Vamos a utilizar JUnit, una de las bibliotecas más comunes para pruebas en el ecosistema de Kotlin y Java. 

Un ejemplo muy básico consistiría en:

Primero, asegúrate de tener JUnit agregado a tu proyecto. Si estás utilizando Gradle, puedes añadir la siguiente dependencia en tu archivo `build.gradle`:

```kotlin
testImplementation ("org.junit.jupiter:junit-jupiter:5.7.0")
```

A continuación, se muestra cómo podrían ser los tests para los métodos `calcularSalarioMensual` y `calcularSalarioSemanal` de la clase `CalculadoraSalario`:

```kotlin
import org.junit.jupiter.api.Assertions.assertEquals
import org.junit.jupiter.api.Test

class CalculadoraSalarioTest {

    private val calculadora = CalculadoraSalario()

    @Test
    fun `test calcular salario mensual`() {
        val horasTrabajadas = 160 // Suponiendo 40 horas a la semana, 4 semanas al mes
        val tarifaPorHora = 10.0
        // Cálculo esperado: 160 * 10 * 1.1 (bonificación del 10%) = 1760
        val resultadoEsperado = 1760.0

        val resultado = calculadora.calcularSalarioMensual(horasTrabajadas, tarifaPorHora)

        assertEquals(resultadoEsperado, resultado, "El salario mensual calculado no es correcto")
    }

    @Test
    fun `test calcular salario semanal`() {
        val horasTrabajadas = 40 // 40 horas a la semana
        val tarifaPorHora = 10.0
        // Cálculo esperado: 40 * 10 * 1.1 (bonificación del 10%) = 440
        val resultadoEsperado = 440.0

        val resultado = calculadora.calcularSalarioSemanal(horasTrabajadas, tarifaPorHora)

        assertEquals(resultadoEsperado, resultado, "El salario semanal calculado no es correcto")
    }
}
```

En estos tests:

- Se crea una instancia de `CalculadoraSalario`.
- Se define un escenario de test para cada uno de los métodos (`calcularSalarioMensual` y `calcularSalarioSemanal`), proporcionando valores de entrada para `horasTrabajadas` y `tarifaPorHora`.
- Se calcula el `resultadoEsperado` basado en la lógica conocida (incluyendo la bonificación del 10% sobre el salario base).
- Se llama al método correspondiente y se compara el resultado con el `resultadoEsperado` utilizando `assertEquals`, que verificará si la refactorización ha alterado la funcionalidad esperada.

Estos tests unitarios aseguran que los métodos `calcularSalarioMensual` y `calcularSalarioSemanal` funcionen como se espera después de cualquier refactorización, manteniendo intacta la lógica de negocio subyacente.

#### 3.3. Refactorización para Eliminar la Duplicación:

Una manera de resolver le "mal olor" comentado arriba es extrayendo la lógica duplicada a su propio método, y luego llamando a este método desde `calcularSalarioMensual` y `calcularSalarioSemanal`.

```kotlin
class CalculadoraSalario {

    private fun calcularSalarioTotal(horasTrabajadas: Int, tarifaPorHora: Double): Double {
        val salarioBase = horasTrabajadas * tarifaPorHora
        val bonificacion = salarioBase * 0.10
        return salarioBase + bonificacion
    }

    fun calcularSalarioMensual(horasTrabajadas: Int, tarifaPorHora: Double): Double {
        return calcularSalarioTotal(horasTrabajadas, tarifaPorHora)
    }

    fun calcularSalarioSemanal(horasTrabajadas: Int, tarifaPorHora: Double): Double {
        return calcularSalarioTotal(horasTrabajadas, tarifaPorHora)
    }
}
```

Ahora, la lógica de cálculo del salario se centraliza en `calcularSalarioTotal`, eliminando la duplicación y facilitando el mantenimiento. Si la fórmula para calcular el salario cambia en el futuro, solo necesitas modificarla en un lugar, reduciendo el riesgo de errores e inconsistencias.

Este ejemplo ilustra cómo identificar y corregir duplicación de código, uno de los "malos olores" más comunes en el desarrollo de software, mejorando así la calidad y mantenibilidad del código.

Identificar y corregir estos "malos olores" mejora significativamente la calidad del código, haciéndolo más limpio, entendible y fácil de mantener. La refactorización es el proceso clave para abordar estos problemas, asegurando que el software sea escalable y robusto. Los test nos asegura que la refactorización no afecte la funcionalidad de los métodos.

## Fuente

- [Refactoring Guru](https://refactoring.guru/refactoring) - Refactoring Guru
- [Refactoring: Improving the Design of Existing Code](https://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672) - Martin Fowler
- [Refactoring: Improving the Design of Existing Code](https://refactoring.com/) - Refactoring.com
- [Code Smells](https://sourcemaking.com/refactoring/smells) - Sourcemaking
- [Refactoring](https://martinfowler.com/tags/refactoring.html) - Martin Fowler
- [Refactoring](https://en.wikipedia.org/wiki/Code_refactoring) - Wikipedia