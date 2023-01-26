---
title: "UD 3 - 3.2 Test de unidad y TDD"
description: Relación entre software y hardware
summary: Relación entre software y hardware
authors:
- Eduardo Fdez
date: 2022-09-18
icon: material/security
permalink: /edes/unidad1/1.1
categories:
- EDES
tags:
- EDES
- Software
- Hardware
---

## Introducción a Kotest

### 1. Información general

[Kotest](https://kotest.io/) es un framework de pruebas multiplataforma escrito en Kotlin. Consta de 3 subproyectos principales:

* Framework para pruebas
* Biblioteca de aserciones
* Pruebas de propiedad

Podemos usar cada proyecto independientemente, integrándolos con otros framework de prueba. Por ejemplo, es posible usar las aserciones de Kotest en lugar de otros frameworks de [asserciones](https://www.baeldung.com/introduction-to-assertj).

Podemos ejecutar pruebas Kotest en JVM, Javascript o Native. Esto nos permite utilizar la misma biblioteca de pruebas para el desarrollo web, móvil y back-end. Nos centraremos en la plataforma JVM .

### 2. Pruebas en JVM

Kotest utiliza la plataforma JUnit en la JVM. Entonces, en un proyecto [Maven](https://search.maven.org/artifact/io.kotest/kotest-runner-junit5-jvm) , podemos activarlo usando las siguientes sentencias dentro del fichero `build.gradle.kts`

```kotlin
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.kotest:kotest-runner-junit5-jvm:5.5.4")
    testImplementation("io.kotest:kotest-runner-junit5:5.5.4")
    testImplementation("io.kotest:kotest-assertions-core:5.5.4")
    testImplementation("io.kotest:kotest-property:5.5.4")
}
```
ten en cuenta que estamos estableciendo la version `5.5.4`, [aqui](https://search.maven.org/artifact/io.kotest/kotest-runner-junit5-jvm) puedes consultar cual es la última versión.

### 3. Estilos de prueba

Kotest proporciona muchos estilos de prueba diferentes. Veamos ejemplos de algunos los estilos más usados.

#### 3.1. Especificaciones de comportamiento

Podemos escribir pruebas similares a [BDD](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_comportamiento), en este estilo se usan las palabras clave `given` (Bajo unas condiciones) , `when` (cuando se cumpla tal cosa) y `then` (entonces sucederá):

```kolin
// En una situación en el que tengo suficiente balance,
// cuando se realice un pago
// el pago se debe realizar sin problemas. 
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

### 3.2. debe especificar

Podemos crear pruebas usando la palabra clave `should` (Debería cumplirse) :

```kotlin
// Debería convertir el dinero de entrada a la moneda destino.
class MoneyTests : ShouldSpec({
    should("Convert input money to the target currency") {
        // test code
    }
})
```

Podemos agrupar pruebas relacionadas en un bloque de `context`:

```Kotlin
class PaymentTests : ShouldSpec({
    context("CardPayments") {
        should("Make a card payment") {
            // test code
        }
    }
    context("BankTransfers") {
        should("Make an external bank transfer") {
            // test code
        }
    }
})
```

### 3.3. Especificaciones de características

A continuación, veamos cómo se pueden escribir pruebas basadas en [Cucumber](https://www.baeldung.com/cucumber-rest-api-testing), una herramienta de uso común para las pruebas de aceptación del usuario, basadas en las palabras clave  `feature` (funcionalidad) y `scenario` (escenario):

```Kotlin
class HomePageTests : FeatureSpec({
    feature("signup") {
        scenario("should allow user to signup with email") {
            // test code
        }
    }
    feature("signin") {
        scenario("should allow user with valid credentials to login") {
            // test code
        }
    }
})
```

### 3.4. Describir especificaciones

Usando `describe`, podemos escribir pruebas en un estilo muy popular entre los desarrolladores de Javascript y Ruby, de hecho será el que usaremos en nuestros ejemplos:

```Kotlin
class PaymentTests : DescribeSpec({
    describe("CardPayments") {
        it("Should make a card payment") {
            // test code
        }
    }
    describe("BankTransfers") {
        it("Should make an external bank transfer") {
            // test code
        }
    }
})
```

### 4. Assertions

Anteriormente hemos visto que Kotest tiene bibliotecas separadas destinadas a aserciones, las afirmaciones que tienen que cumplirse tras realizar el test. Estas bibliotecas nos brindan varias funciones de *comparación* para escribir afirmaciones fluidas en nuestras pruebas. Hay dos grandes categorías de bibliotecas de aserciones:

* Core matchers
* External matchers

Veamos algunos ejemplos de comparadores que permite la *[biblioteca kotest-assertions-core](https://search.maven.org/search?q=g:io.kotest%20AND%20a:kotest-assertions-core)*:

```kotlin
// verify actual object is equal to expected object
result.shouldBe(expected)

// verify actual expression is true
result.shouldBeTrue()

// verify actual object is of given type
result.shouldBeTypeOf<Double>()

// verify actual map contains the given key
result.shouldContainKey(key)

// verify actual map contains the given values
result.shouldContainValues(values)

// verify actual string contains the given substring
result.shouldContain("substring")

// verify actual string is equal to the given string ignoring case
result.shouldBeEqualIgnoringCase(otherString)

// verify actual file should have the given size
result.shouldHaveFileSize(size)

// verify actual date is after the given date
result.shouldBeBefore(otherDate)Copiar
```

Además del módulo principal de aserciones, existen varios otros módulos que proporcionan comparadores para una amplia variedad de escenarios, por ejemplo, comparadores JSON, coincidencias JDBC, etc, y por supuesto tienen muchas mas opciones y deberíamos revisar la biblioteca buscando aquella que necesitamos para nuestro test.

### 5. Pruebas de excepciones

Por otro lado, probar excepciones con Kotest es muy sencillo:

```Kotlin
val exception = shouldThrow<ValidationException> {
   // test code
}
exception.message should startWith("Invalid input")
```

### 6. Ganchos de ciclo de vida

Podemos usar ganchos de ciclo de vida para configurar o desmontar el escenario necesario de objetos antes o después de las pruebas. Estos ganchos son muy similares a los métodos de instalación y desmontaje del framework Junit. Veamos un ejemplo:

```Kotlin
class TransactionStatementSpec : ShouldSpec({
    beforeTest {
      // add transactions. Se ejecutará antes del test
    }
    afterTest { (test, result) ->
      // delete transactions. Se ejecutará después del test
    }
})
```

## 7. Pruebas basadas en datos

Las pruebas basadas en datos en Kotest son similares a las [pruebas parametrizadas en Junit5](https://www.baeldung.com/parameterized-tests-junit-5) . Podemos proporcionar varias entradas a un solo caso de prueba para verificar diferentes ejemplos en lugar de escribir varias pruebas con solo datos de entrada diferentes. Podemos usar la función `useData` de la [biblioteca kotest-framework-datatest-jvm](https://search.maven.org/search?q=g:io.kotest%20AND%20a:kotest-framework-datatest-jvm) para proporcionar datos a las pruebas.

Veamos un ejemplo:

```kotlin
data class TaxTestData(val income: Long, val taxClass: TaxClass, val expectedTaxAmount: Long)

class IncomeTaxTests : FunSpec({
    withData(
      TaxTestData(1000, ONE, 300),
      TaxTestData(1000, TWO, 350),
      TaxTestData(1000, THREE, 200)
    ) { (income, taxClass, expectedTaxAmount) ->
        calculateTax(income, taxClass) shouldBe expectedTaxAmount
    }
})
```

## 8. Pruebas no deterministas

A veces, necesitamos probar funciones que no devuelven resultados sincrónicamente. Desafortunadamente, es complicado probar tales funciones, ya que tenemos que escribir código especial para esperar los resultados utilizando técnicas como funciones callback o dormir el hilo.

Kotest proporciona algunas funciones útiles que podemos usar para escribir este tipo de pruebas no deterministas de forma declarativa.

Veamos un ejemplo de la función `eventually` :

```kotlin
class TransactionTests : ShouldSpec({
    val transactionRepo = TransactionRepo()

    should("Should make transaction complete") {
        eventually({
            duration = 5000
            interval = FixedInterval(1000)
        }) {
            transactionRepo.getStatus(120) shouldBe "COMPLETE"
        }
    }
})
```

Aquí, nuestra prueba verificará el estado de la transacción `transactionRepo.getStatus` cada segundo, hasta llegar a 5 segundos.

## 9. Mocking

Podemos integrar cualquier biblioteca de simulación como [mockk](https://www.baeldung.com/kotlin/mockk) con Kotest, biblioteca que veremos mas adelante. Kotest no proporciona su propia biblioteca de simulación:

```kotlin
class ExchangeServiceTest : FunSpec({
    val exchangeRateProvider = mockk<ExchangeRateProvider>()
    val service = ExchangeService(exchangeRateProvider)

    test("Exchanges money using rate from exchange rate service") {
        every { exchangeRateProvider.rate("USDEUR") } returns 0.9
        service.exchange(Money(1200, "USD"), "EUR") shouldBe 1080
    }
})
```

## 10. Cobertura de pruebas

Podemos integrar [Jacoco](https://www.baeldung.com/jacoco) con Kotest para medir la cobertura de la prueba. Para integrar, debemos asegurarnos de que los informes de cobertura de prueba se generen después de ejecutar las pruebas unitarias:

```kotlin
tasks.test {
    finalizedBy(tasks.jacocoTestReport)
}
```

Podemos encontrar el informe HTML de cobertura de prueba dentro del *directorio `$buildDir/reports/jacoco/test`* .

## 11. Agrupación de pruebas con etiquetas

A veces, queremos ejecutar solo ciertas pruebas en un entorno específico. Por ejemplo, es posible que deseemos evitar ejecutar algunas pruebas lentas como parte de la verificación de una pull request git. Para hacer eso, primero debemos etiquetar nuestras pruebas:

```kotlin
@Tags(NamedTag("SlowTest"))
class SlowTests : ShouldSpec({})
```

### 12. Conclusión

Se han visto varias funcionalidades básicas proporcionadas por el marco Kotest. y los ejemplos de código se pueden encontrar [en GitHub](https://github.com/Baeldung/kotlin-tutorials/tree/master/kotlin-testing) .

## Recursos

* [¿Qué es TDD?](https://www.digite.com/es/agile/desarrollo-dirigido-por-pruebas-tdd/)
* [¿Cómo elaborar casos de prueba?](https://surprograma.github.io/libro-disenio-oop/docs/pruebas-automatizadas/elaborar-casos-prueba/)
* [Test unitario avanzado](http://wiki.uqbar.org/wiki/articles/testeo-unitario-avanzado.html)
* [Diseño de Software](https://surprograma.github.io/libro-disenio-oop/docs/intro/)

## Fuente

* [TDD Veloz](https://www.youtube.com/watch?v=8MGtLPFtbQ8)
