---
title: "UD 5 - 5.2.1 Kotest"
description: Framework de pruebas para Kotlin con estilos de especificación, aserciones y utilidades para automatizar tests.
summary: Introducción práctica a Kotest en JVM: configuración, estilos de prueba, aserciones, hooks, datos, excepciones y pruebas asíncronas.
authors:
  - Eduardo Fdez
date: 2026-03-27
icon: "material/file-document-outline"
permalink: /edes/unidad3/3.2.1
categories:
  - EDES
tags:
  - EDES
  - Kotlin
  - Kotest
  - testing
---

## 5.2.1 Kotest

Después de entender qué es una prueba unitaria y cómo encaja TDD, toca ver una herramienta concreta para llevarlo a código. En este apartado trabajaremos con **Kotest**, uno de los frameworks de pruebas más utilizados en proyectos Kotlin.

Desde el punto de vista de la programación didáctica, este documento se vincula con la normativa de la unidad porque desarrolla cómo implementar pruebas automáticas, estructurar casos de prueba y trabajar con herramientas reales del ecosistema Kotlin.

| Código | Descripción |
| --- | --- |
| RA3 | Verifica el funcionamiento de programas diseñando y realizando pruebas. |
| CE b | Se han definido casos de prueba. |
| CE f | Se han efectuado pruebas unitarias de clases y funciones. |
| CE g | Se han implementado pruebas automáticas. |
| CE i | Se han utilizado dobles de prueba para aislar los componentes durante las pruebas. |

!!! abstract "Qué vas a aprender en este apartado"
    - Identificar qué aporta Kotest en un proyecto Kotlin sobre JVM.
    - Reconocer varios estilos de especificación y cuándo usarlos.
    - Aplicar aserciones, hooks y pruebas basadas en datos.
    - Comprobar excepciones y escenarios asíncronos con una sintaxis expresiva.

### 1. Qué es Kotest y por qué nos interesa

[Kotest](https://kotest.io/) es un framework de pruebas para Kotlin. Su principal ventaja es que permite escribir tests de forma bastante expresiva y cercana al dominio del problema, algo especialmente útil cuando queremos que los tests sirvan también como documentación.

Kotest se apoya en tres grandes bloques:

- **framework de pruebas**: organiza y ejecuta los casos de prueba;
- **biblioteca de aserciones**: ofrece comparadores y matchers legibles;
- **pruebas basadas en propiedades**: generan datos para validar reglas generales del sistema.

Aunque soporta varias plataformas de Kotlin, en este tema nos centraremos en **JVM**, porque es el entorno más habitual en clase y en muchos proyectos empresariales.

!!! note "Idea importante"
    Kotest no sustituye a Kotlin ni a JUnit como lenguaje o plataforma. Lo que aporta es una forma más cómoda y expresiva de definir y ejecutar pruebas sobre JVM.

### 2. Configuración básica en un proyecto JVM

En un proyecto Gradle con Kotlin DSL, una configuración mínima suele incluir el motor de ejecución y el módulo de aserciones. Conviene declarar la versión en una variable para mantenerla en un único sitio.

```kotlin
val kotestVersion = "x.y.z"

dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.kotest:kotest-runner-junit5-jvm:$kotestVersion")
    testImplementation("io.kotest:kotest-assertions-core:$kotestVersion")
    testImplementation("io.kotest:kotest-property:$kotestVersion")
}
```

Además, si el proyecto usa JUnit 5 como plataforma, el *runner* de Kotest se integra sin problemas.

Lo práctico aquí no es memorizar los artefactos, sino entender la idea:

- un módulo ejecuta los tests;
- otro aporta aserciones;
- y puedes añadir extensiones o módulos específicos según tus necesidades.

### 3. Estilos de prueba

Kotest ofrece varios estilos. No se trata de que uno sea "el correcto" y el resto no, sino de elegir el que mejor comunica el comportamiento que quieres describir.

#### 3.1. `BehaviorSpec`: estilo BDD

Este estilo usa una narrativa cercana a **given / when / then**, muy útil cuando el comportamiento se entiende como una historia o escenario.

```kotlin
import io.kotest.core.spec.style.BehaviorSpec
import io.kotest.matchers.booleans.shouldBeTrue

class CardPaymentTests : BehaviorSpec({
    given("una tarjeta con saldo suficiente") {
        val cardNumber = "1111-2222-3333-4444"
        val provider = InMemoryBalanceProvider(mapOf(cardNumber to 500.0))

        `when`("se realiza un pago de 150 euros") {
            val payment = CardPayment(cardNumber, 150.0)

            then("el pago se procesa correctamente") {
                payment.pay(provider).shouldBeTrue()
            }
        }
    }
})
```

Este estilo funciona bien cuando quieres destacar el contexto y la consecuencia.

#### 3.2. `ShouldSpec`: pruebas centradas en lo esperado

`ShouldSpec` resulta muy legible cuando cada test expresa algo que el sistema **debería** hacer.

```kotlin
import io.kotest.core.spec.style.ShouldSpec
import io.kotest.matchers.shouldBe

class MoneyTests : ShouldSpec({
    should("convertir una cantidad a otra divisa") {
        val rates = mapOf(Pair(Currency.USD, Currency.EUR) to 0.85)
        val provider = InMemoryExchangeRateProvider(rates)
        val money = Money(100.0, Currency.USD)

        val converted = money.convertTo(Currency.EUR, provider)

        converted.amount shouldBe 85.0
        converted.currency shouldBe Currency.EUR
    }
})
```

Dentro de `ShouldSpec` es frecuente agrupar casos relacionados con `context`.

```kotlin
class PaymentTests : ShouldSpec({
    context("pagos con tarjeta") {
        should("aceptar un pago cuando hay saldo") {
            val cardNumber = "5555-6666-7777-8888"
            val balanceProvider = InMemoryBalanceProvider(mapOf(cardNumber to 200.0))
            val bankService = InMemoryBankTransferService(emptyMap())
            val paymentService = PaymentService(balanceProvider, bankService)

            paymentService.payWithCard(CardPayment(cardNumber, 50.0)).shouldBeTrue()
        }
    }

    context("transferencias bancarias") {
        should("realizar una transferencia externa") {
            val from = "acct-123"
            val to = "acct-456"
            val bankService = InMemoryBankTransferService(mapOf(from to 300.0, to to 100.0))
            val balanceProvider = InMemoryBalanceProvider(emptyMap())
            val paymentService = PaymentService(balanceProvider, bankService)

            paymentService.transfer(from, to, 120.0).shouldBeTrue()
        }
    }
})
```

#### 3.3. `FeatureSpec`: funcionalidades y escenarios

Si quieres representar funcionalidades con varios escenarios, `FeatureSpec` encaja bastante bien.

```kotlin
import io.kotest.core.spec.style.FeatureSpec
import io.kotest.matchers.booleans.shouldBeFalse
import io.kotest.matchers.booleans.shouldBeTrue

class HomePageTests : FeatureSpec({
    feature("signup") {
        scenario("permite registrar un correo nuevo") {
            val homePage = HomePage()
            homePage.signup("user@example.com", "securePass").shouldBeTrue()
        }

        scenario("rechaza un correo ya existente") {
            val homePage = HomePage()
            homePage.signup("user@example.com", "pass1")

            homePage.signup("user@example.com", "pass2").shouldBeFalse()
        }
    }
})
```

#### 3.4. `DescribeSpec`: un estilo muy usado en este bloque

`DescribeSpec` es especialmente popular porque recuerda al estilo usado en ecosistemas como JavaScript o Ruby y encaja muy bien con ejemplos de dominio.

```kotlin
import io.kotest.core.spec.style.DescribeSpec
import io.kotest.matchers.booleans.shouldBeTrue

class PaymentDescribeSpecTests : DescribeSpec({
    describe("un servicio de pagos") {
        it("procesa un pago con tarjeta") {
            val cardNumber = "9999-8888-7777-6666"
            val balanceProvider = InMemoryBalanceProvider(mapOf(cardNumber to 150.0))
            val bankService = InMemoryBankTransferService(emptyMap())
            val service = PaymentService(balanceProvider, bankService)

            service.payWithCard(CardPayment(cardNumber, 75.0)).shouldBeTrue()
        }

        it("realiza una transferencia externa") {
            val from = "acct-A"
            val to = "acct-B"
            val bankService = InMemoryBankTransferService(mapOf(from to 500.0, to to 50.0))
            val balanceProvider = InMemoryBalanceProvider(emptyMap())
            val service = PaymentService(balanceProvider, bankService)

            service.transfer(from, to, 200.0).shouldBeTrue()
        }
    }
})
```

### 4. Aserciones

Las **aserciones** son las comprobaciones que indican si el resultado del test es correcto. Kotest incorpora una biblioteca muy amplia de *matchers*.

#### 4.1. Algunos matchers frecuentes

```kotlin
import io.kotest.core.spec.style.StringSpec
import io.kotest.matchers.booleans.shouldBeTrue
import io.kotest.matchers.collections.shouldContainValues
import io.kotest.matchers.maps.shouldContainKey
import io.kotest.matchers.shouldBe
import io.kotest.matchers.string.shouldBeEqualIgnoringCase
import io.kotest.matchers.string.shouldContain
import io.kotest.matchers.types.shouldBeTypeOf

class AssertionExamples : StringSpec({
    "compara igualdad con shouldBe" {
        val result = 42
        result shouldBe 42
    }

    "comprueba expresiones booleanas" {
        (5 > 2).shouldBeTrue()
    }

    "verifica tipos concretos" {
        val value: Any = 3.14
        value.shouldBeTypeOf<Double>()
    }

    "comprueba claves y valores en mapas" {
        val map = mapOf("a" to 1, "b" to 2)
        map.shouldContainKey("a")

        val words = mapOf(1 to "one", 2 to "two", 3 to "three")
        words.shouldContainValues(listOf("two", "three"))
    }

    "trabaja con cadenas" {
        "Hello Kotest Framework".shouldContain("Kotest")
        "KoTeSt".shouldBeEqualIgnoringCase("kotest")
    }
})
```

#### 4.2. Módulos especializados de aserciones

Además del módulo central, Kotest ofrece módulos para escenarios concretos:

| Módulo | Ejemplo de uso | Para qué sirve |
| --- | --- | --- |
| `kotest-assertions-json` | `json.shouldMatchJson("{\"a\":1}")` | Comparar estructuras JSON |
| `kotest-assertions-xml` | `xml.shouldHaveXPath("/root/item")` | Verificar XML |
| `kotest-assertions-db` | `resultSet.shouldHaveRows(3)` | Aserciones sobre JDBC |
| `kotest-assertions-time` | `date1.shouldBeBefore(date2)` | Trabajar con fechas y horas |
| `kotest-extensions-*` | integración con Spring, MockK, etc. | Extender Kotest |

Una dependencia adicional podría quedar así:

```kotlin
val kotestVersion = "x.y.z"

dependencies {
    testImplementation("io.kotest:kotest-assertions-core:$kotestVersion")
    testImplementation("io.kotest:kotest-assertions-json:$kotestVersion")
    testImplementation("io.kotest:kotest-assertions-db:$kotestVersion")
}
```

### 5. Pruebas de excepciones

Comprobar excepciones es una necesidad habitual. Kotest lo resuelve de forma bastante directa con `shouldThrow`.

```kotlin
import io.kotest.assertions.throwables.shouldThrow
import io.kotest.core.spec.style.StringSpec
import io.kotest.matchers.string.shouldStartWith

class ValidationException(message: String) : RuntimeException(message)

object InputProcessor {
    fun process(input: String) {
        if (input.length < 5) {
            throw ValidationException("Invalid input: length must be at least 5 characters")
        }
        if (input.startsWith(" ")) {
            throw ValidationException("Invalid input: must not start with whitespace")
        }
    }
}

class ExceptionTests : StringSpec({
    "lanza una excepción para una entrada demasiado corta" {
        val exception = shouldThrow<ValidationException> {
            InputProcessor.process("abc")
        }

        exception.message.shouldStartWith("Invalid input")
    }

    "lanza una excepción si la entrada comienza con espacio" {
        val exception = shouldThrow<ValidationException> {
            InputProcessor.process(" hello")
        }

        exception.message.shouldStartWith("Invalid input")
    }
})
```

En la práctica, esto ayuda a comprobar reglas de validación sin necesidad de usar bloques `try/catch` que harían el test más ruidoso.

### 6. Ganchos de ciclo de vida

Los *hooks* de ciclo de vida permiten preparar y limpiar el escenario antes o después de cada prueba.

```kotlin
import io.kotest.core.spec.style.ShouldSpec
import io.kotest.matchers.collections.shouldHaveSize

data class Transaction(val id: Int, val amount: Double, val description: String)

class TransactionRepository {
    private val transactions = mutableListOf<Transaction>()

    fun add(transaction: Transaction) {
        transactions.add(transaction)
    }

    fun getAll(): List<Transaction> = transactions.toList()

    fun clear() {
        transactions.clear()
    }
}

class TransactionStatementSpec : ShouldSpec({
    val repo = TransactionRepository()

    beforeTest {
        repo.add(Transaction(1, 100.0, "Deposit"))
        repo.add(Transaction(2, -50.0, "Withdrawal"))
    }

    afterTest {
        repo.clear()
    }

    context("extracto de transacciones") {
        should("contener dos movimientos de ejemplo") {
            repo.getAll().shouldHaveSize(2)
        }
    }
})
```

Estos ganchos son útiles, pero conviene no abusar de ellos. Si el contexto compartido es demasiado grande, el test deja de ser fácil de leer.

### 7. Pruebas basadas en datos

Cuando la lógica es la misma y lo que cambia son los valores de entrada, las pruebas basadas en datos ayudan a evitar duplicación.

```kotlin
import io.kotest.core.spec.style.FunSpec
import io.kotest.data.blocking.withData
import io.kotest.matchers.shouldBe

enum class TaxClass { ONE, TWO, THREE }

fun calculateTax(income: Long, taxClass: TaxClass): Long = when (taxClass) {
    TaxClass.ONE -> (income * 0.30).toLong()
    TaxClass.TWO -> (income * 0.35).toLong()
    TaxClass.THREE -> (income * 0.20).toLong()
}

data class TaxTestData(
    val income: Long,
    val taxClass: TaxClass,
    val expectedTaxAmount: Long
)

class IncomeTaxTests : FunSpec({
    withData(
        TaxTestData(1000, TaxClass.ONE, 300),
        TaxTestData(1000, TaxClass.TWO, 350),
        TaxTestData(1000, TaxClass.THREE, 200),
        TaxTestData(5000, TaxClass.ONE, 1500),
        TaxTestData(5000, TaxClass.TWO, 1750),
        TaxTestData(5000, TaxClass.THREE, 1000)
    ) { (income, taxClass, expectedTaxAmount) ->
        calculateTax(income, taxClass) shouldBe expectedTaxAmount
    }
})
```

Lo relevante aquí es que el comportamiento se expresa una sola vez y los datos cambian de forma ordenada.

### 8. Pruebas no deterministas y asíncronas

A veces necesitamos comprobar comportamientos que no ocurren justo en el instante en el que lanzamos la acción. En esos casos, Kotest ofrece utilidades como `eventually`.

```kotlin
import io.kotest.assertions.nondeterministic.eventually
import io.kotest.core.spec.style.ShouldSpec
import io.kotest.matchers.shouldBe
import java.util.concurrent.CopyOnWriteArrayList

class TransactionRepo {
    private val processed = CopyOnWriteArrayList<String>()

    fun markProcessed(id: String) {
        Thread {
            Thread.sleep(200)
            processed += id
        }.start()
    }

    fun isProcessed(id: String): Boolean = id in processed
}

class TransactionTests : ShouldSpec({
    val repo = TransactionRepo()

    should("marcar una transacción como completada") {
        repo.markProcessed("tx-001")

        eventually {
            repo.isProcessed("tx-001") shouldBe true
        }
    }
})
```

Esto evita estrategias poco fiables como meter `Thread.sleep()` en mitad del test y esperar que el tiempo elegido coincida con la realidad.

### 9. Criterios para elegir un estilo y usar Kotest con sentido

Kotest ofrece muchas opciones, pero no conviene usarlas todas a la vez. En clase y en proyectos reales suele funcionar mejor esta idea:

- elige un estilo de especificación y sé consistente;
- prioriza la legibilidad sobre la sofisticación;
- comparte contexto solo cuando realmente simplifique;
- usa *matchers* expresivos para que el fallo explique qué ocurrió;
- automatiza los escenarios repetitivos con datos cuando proceda.

### 10. Conclusión

## Fuentes y referencias

- [Documentación oficial de Kotest](https://kotest.io/docs/)
- [Kotest en Maven Central](https://search.maven.org/search?q=g:io.kotest)
- [JUnit 5 User Guide](https://junit.org/junit5/docs/current/user-guide/)

Kotest es útil porque permite escribir tests que se leen mejor, se organizan mejor y expresan el comportamiento de una forma más cercana al dominio del problema. No se trata solo de ejecutar pruebas, sino de **hacer que esas pruebas ayuden a pensar y a comunicar**.

Si recuerdas una idea de este apartado, que sea esta: **Kotest aporta valor cuando convierte los tests en documentación ejecutable del comportamiento esperado**.
