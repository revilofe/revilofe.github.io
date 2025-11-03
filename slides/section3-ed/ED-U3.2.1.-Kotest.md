
## U3.2.1 - Introducción a Kotest

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Introducción a Kotest


### ¿Qué es Kotest?

* Framework de pruebas escrito en Kotlin.
* Multiplataforma: JVM, JS y Native.
* Compuesto por tres subproyectos: 
   * Núcleo de pruebas.
   * Biblioteca de aserciones.
   * Pruebas de propiedad.
* Compatible con otros frameworks.
* Usaremos plataforma JVM.

Note: Introduce Kotest como framework versátil para pruebas. Menciona los tres componentes principales y su uso independiente. Aclara que se centrará en JVM.


### Configuración en JVM

* Usa la plataforma JUnit.
* En `build.gradle.kts` se incluyen dependencias:

```kotlin
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.kotest:kotest-runner-junit5-jvm:5.5.4")
    testImplementation("io.kotest:kotest-runner-junit5:5.5.4")
    testImplementation("io.kotest:kotest-assertions-core:5.5.4")
    testImplementation("io.kotest:kotest-property:5.5.4")
}
```

Note: Muestra cómo integrar Kotest con un proyecto JVM usando Gradle. Se indican las dependencias necesarias, usando la versión 5.5.4 como referencia.

---

## Estilos de prueba en Kotest


### Estilo BDD (BehaviorSpec)

* Usa bloques `given`, `when`, `then`.
* Similar a pruebas de comportamiento.

```kotlin
class CardPaymentTests : BehaviorSpec({
    given("I have sufficient balance") {
        `when`("I make a card payment") {
            then("The card payment should be successful") {
                // test code
            }
        }
    }
})
```

Note: Presenta el estilo BehaviorSpec, útil para expresar escenarios en lenguaje natural. Aporta claridad en pruebas orientadas a comportamiento.


### Estilo ShouldSpec

* Usa `should` para describir expectativas.
* Se agrupan con bloques `context`.

```kotlin
class PaymentTests : ShouldSpec({
    context("CardPayments") {
        should("Make a card payment") {
            // test code
        }
    }
})
```

Note: Explica cómo usar el estilo ShouldSpec para organizar y agrupar pruebas de manera intuitiva, centrado en lo que "debería ocurrir".


### Estilo FeatureSpec

* Usa `feature` y `scenario`.
* Inspirado en pruebas tipo Cucumber.

```kotlin
class HomePageTests : FeatureSpec({
    feature("signup") {
        scenario("should allow user to signup with email") {
            // test code
        }
    }
})
```

Note: Describe cómo estructurar pruebas basadas en escenarios, facilitando validaciones desde la perspectiva del usuario final.


### Estilo DescribeSpec

* Usa `describe` e `it`.
* Estilo común en JS y Ruby.

```kotlin
class PaymentTests : DescribeSpec({
    describe("CardPayments") {
        it("Should make a card payment") {
            // test code
        }
    }
})
```

Note: Se muestra DescribeSpec, estilo que se utilizará en los ejemplos del curso. Favorece una descripción clara y jerárquica.

---

## Aserciones en Kotest


### ¿Qué son las aserciones?

* Verifican condiciones esperadas tras ejecutar un test.
* Kotest tiene su propia biblioteca de aserciones.
* Dos categorías:
  
  * Core matchers.
  * External matchers.
* Permiten comparaciones expresivas y precisas.

Note: Explica el propósito de las aserciones en pruebas. Presenta las categorías disponibles en Kotest y su rol en la validación de resultados esperados.


### Ejemplos de aserciones core

```kotlin
result.shouldBe(expected)
result.shouldBeTrue()
result.shouldBeTypeOf<Double>()
result.shouldContain("substring")
```

* Comparación directa de resultados.
* Validación de tipos, textos, mapas, fechas, archivos.
* Uso sencillo y claro.

Note: Muestra varios ejemplos comunes. Se busca que el alumno reconozca cómo expresar condiciones claras y reutilizables.

---

## Pruebas de excepciones


### Validación de excepciones esperadas

* Uso de `shouldThrow<T>()` para capturar errores.
* Permite validar tipo y contenido del mensaje.

```kotlin
val exception = shouldThrow<ValidationException> {
    // test code
}
exception.message should startWith("Invalid input")
```

Note: Se muestra cómo manejar casos donde se espera una excepción. Es útil para probar validaciones y errores de lógica del sistema.

---

## Ganchos de ciclo de vida


### Uso de `beforeTest` y `afterTest`

* Ejecutan lógica antes o después de cada prueba.
* Similares a setup/teardown de JUnit.

```kotlin
class TransactionStatementSpec : ShouldSpec({
    beforeTest {
        // Preparación
    }
    afterTest { (test, result) ->
        // Limpieza
    }
})
```

Note: Introduce cómo preparar el entorno para pruebas y limpiar después. Es fundamental para mantener pruebas aisladas y reproducibles.

---

## Pruebas basadas en datos


### Uso de `withData` y clases de datos

* Similares a pruebas parametrizadas.
* Reutiliza lógica de test con distintas entradas.

```kotlin
data class TaxTestData(val income: Long, val taxClass: TaxClass, val expectedTaxAmount: Long)

withData(
    TaxTestData(1000, ONE, 300),
    TaxTestData(1000, TWO, 350)
) { (income, taxClass, expected) ->
    calculateTax(income, taxClass) shouldBe expected
}
```

Note: Muestra cómo automatizar tests con diferentes valores de entrada sin duplicar código. Ideal para lógica con muchas combinaciones posibles.

---

## Pruebas no deterministas


### Uso de `eventually`

* Útil para funciones asincrónicas o resultados tardíos.
* Reintenta la condición durante un tiempo definido.

```kotlin
eventually({
    duration = 5000
    interval = FixedInterval(1000)
}) {
    transactionRepo.getStatus(120) shouldBe "COMPLETE"
}
```

Note: Explica cómo probar resultados que no son inmediatos. `eventually` permite reintentos con un intervalo fijo, ideal para procesos asincrónicos.

---

## Integración con Mocking


### Uso de `mockk` con Kotest

* Kotest no tiene biblioteca propia de mocks.
* Se recomienda usar `mockk`.

```kotlin
val provider = mockk<ExchangeRateProvider>()
every { provider.rate("USDEUR") } returns 0.9

val service = ExchangeService(provider)
service.exchange(Money(1200, "USD"), "EUR") shouldBe 1080
```

Note: Se muestra cómo simular comportamientos de dependencias externas. Útil para pruebas unitarias de componentes aislados.

---

## Cobertura de pruebas


### Uso de Jacoco con Kotest

* Genera informes de cobertura tras las pruebas.
* Integración sencilla en `build.gradle.kts`.

```kotlin
tasks.test {
    finalizedBy(tasks.jacocoTestReport)
}
```

* Informe HTML en `$buildDir/reports/jacoco/test`.

Note: Explica cómo medir qué parte del código ha sido probada. Ayuda a identificar qué zonas necesitan más validación.

---

## Agrupación por etiquetas


### Uso de anotaciones `@Tags`

* Permite ejecutar o excluir pruebas según contexto.
* Útil para ignorar tests lentos en Pull Requests.

```kotlin
@Tags(NamedTag("SlowTest"))
class SlowTests : ShouldSpec({})
```

Note: Permite segmentar pruebas en grupos lógicos. Es especialmente útil para ajustar las pruebas según el entorno o fase del desarrollo.

---

## Conclusión y recursos


### Resumen y próximos pasos

* Kotest ofrece múltiples estilos y flexibilidad.
* Aserciones claras y ganchos potentes.
* Soporte para pruebas no deterministas y parametrizadas.
* Integración con herramientas externas como MockK y Jacoco.
* Ejemplos disponibles en GitHub.

Note: Recapitula las características más importantes de Kotest. Invita al alumno a practicar y explorar más casos en los ejemplos proporcionados.

---
