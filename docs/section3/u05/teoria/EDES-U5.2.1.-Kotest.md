---
title: "UD 3 - 3.3 Kotest"
description: Kotest
summary: Kotest
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
  - kotest
---

## 3.2.1. Introducción a Kotest

### 1. Información general

[Kotest](https://kotest.io/)  es un framework de pruebas escrito en Kotlin, diseñado para ser multiplataforma, con soporte para JVM, JavaScript y Kotlin/Native. Su arquitectura modular permite una alta flexibilidad y reutilización en diferentes entornos de desarrollo, incluyendo aplicaciones web, móviles y de back-end.

El framework se organiza en tres componentes principales:

- **Framework de pruebas**: constituye el núcleo del sistema de pruebas, permitiendo definir, organizar y ejecutar los casos de prueba. Soporta múltiples estilos de escritura de tests, lo que facilita su adaptación a distintas preferencias o convenciones.

- **Biblioteca de [asserciones](https://www.baeldung.com/introduction-to-assertj)**: proporciona una colección extensa de funciones de aserción, diseñadas para verificar condiciones que deben cumplirse al ejecutar los tests. Estas aserciones son expresivas, idiomáticas y pueden utilizarse de forma independiente con otros frameworks de pruebas, como JUnit.

- **Pruebas basadas en propiedades (property testing)**: permite validar propiedades generales del sistema bajo prueba generando automáticamente datos de entrada aleatorios. Esta técnica resulta especialmente útil para descubrir errores que no se detectan fácilmente mediante pruebas con datos estáticos.

Cada uno de estos subproyectos puede utilizarse de forma independiente, integrándose sin dificultad con otros frameworks de pruebas existentes. Por ejemplo, es posible emplear únicamente la biblioteca de aserciones de Kotest junto con JUnit como motor de ejecución.

Aunque Kotest permite desarrollar y ejecutar pruebas en cualquiera de las plataformas soportadas por Kotlin (JVM, JavaScript, Native), en este documento nos centraremos en su uso en la plataforma JVM, por ser la más habitual en entornos empresariales y educativos.


### 2. Pruebas en JVM

Kotest utiliza la plataforma JUnit en la JVM. Entonces, en un proyecto [Maven](https://search.maven.org/artifact/io.kotest/kotest-runner-junit5-jvm), podemos activarlo usando las siguientes sentencias dentro del fichero `build.gradle.kts`

```kotlin
dependencies {
    testImplementation(kotlin("test"))
    testImplementation("io.kotest:kotest-runner-junit5-jvm:5.5.4")
    testImplementation("io.kotest:kotest-runner-junit5:5.5.4")
    testImplementation("io.kotest:kotest-assertions-core:5.5.4")
    testImplementation("io.kotest:kotest-property:5.5.4")
}
```
ten en cuenta que estamos estableciendo la version `5.5.4`, [aqui](https://search.maven.org/artifact/io.kotest/kotest-runner-junit5-jvm) puedes consultar cuál es la última versión.

### 3. Estilos de prueba

Kotest proporciona muchos estilos de prueba diferentes. Veamos ejemplos de algunos los estilos más usados.

#### 3.1. Especificaciones de comportamiento

Podemos escribir pruebas similares a [BDD](https://es.wikipedia.org/wiki/Desarrollo_guiado_por_comportamiento), en este estilo se usan las palabras clave `given` (Bajo unas condiciones), `when` (cuando se cumpla tal cosa) y `then` (entonces sucederá):

```kotlin
// src/main/kotlin/com/example/Domain.kt
package com.example

// Clase para gestionar pagos con tarjeta
data class CardPayment(
    val cardNumber: String,
    val amount: Double
) {
    fun pay(balanceProvider: BalanceProvider): Boolean {
        val balance = balanceProvider.getBalance(cardNumber)
        return if (balance >= amount) {
            balanceProvider.debit(cardNumber, amount)
            true
        } else {
            false
        }
    }
}

// Interfaz para obtención y débito de balance
interface BalanceProvider {
    fun getBalance(cardNumber: String): Double
    fun debit(cardNumber: String, amount: Double)
}

// Implementación de BalanceProvider para pruebas (almacén en memoria)
class InMemoryBalanceProvider(initialBalances: Map<String, Double>) : BalanceProvider {
    private val balances = initialBalances.toMutableMap()

    override fun getBalance(cardNumber: String): Double = balances[cardNumber] ?: 0.0

    override fun debit(cardNumber: String, amount: Double) {
        val current = balances[cardNumber] ?: 0.0
        if (amount <= 0) throw IllegalArgumentException("Amount must be positive")
        if (current < amount) throw IllegalStateException("Insufficient balance")
        balances[cardNumber] = current - amount
    }
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/CardPaymentTests.kt
package com.example.tests

import io.kotest.core.spec.style.BehaviorSpec
        import io.kotest.matchers.booleans.shouldBeTrue
        import com.example.CardPayment
        import com.example.InMemoryBalanceProvider

class CardPaymentTests : BehaviorSpec({
    given("I have sufficient balance") {
        val cardNumber = "1111-2222-3333-4444"
        val initialBalances = mapOf(cardNumber to 500.0)
        val balanceProvider = InMemoryBalanceProvider(initialBalances)

        `when`("I make a card payment of 150.0") {
            val payment = CardPayment(cardNumber, 150.0)

            then("The card payment should be successful") {
                val result = payment.pay(balanceProvider)
                result.shouldBeTrue()
            }
        }
    }
})

```

#### 3.2. Especificaciones mediante `should`

Podemos crear pruebas usando la palabra clave `should` (Debería cumplirse):

```kotlin
// src/main/kotlin/com/example/Domain.kt
package com.example

// Clase para representar dinero y conversión de divisas
data class Money(
    val amount: Double,
    val currency: Currency
) {
    fun convertTo(target: Currency, rateProvider: ExchangeRateProvider): Money {
        val rate = rateProvider.getRate(currency, target)
        return Money(amount * rate, target)
    }
}

enum class Currency { USD, EUR, GBP, JPY }

// Interfaz para obtención de tipos de cambio
interface ExchangeRateProvider {
    fun getRate(from: Currency, to: Currency): Double
}

// Implementación de ExchangeRateProvider para pruebas (tipos de cambio en memoria)
class InMemoryExchangeRateProvider(
    private val rates: Map<Pair<Currency, Currency>, Double>
) : ExchangeRateProvider {
    override fun getRate(from: Currency, to: Currency): Double {
        return rates[Pair(from, to)]
            ?: if (from == to) 1.0 else throw IllegalArgumentException("Rate not found for $from to $to")
    }
}


// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/MoneyTests.kt
package com.example.tests

import io.kotest.core.spec.style.ShouldSpec
        import io.kotest.matchers.shouldBe
        import com.example.Money
        import com.example.Currency
        import com.example.InMemoryExchangeRateProvider

class MoneyTests : ShouldSpec({
    should("Convert input money to the target currency") {
        // Datos iniciales: 100 USD a EUR con tasa 0.85
        val initialAmount = 100.0
        val sourceCurrency = Currency.USD
        val targetCurrency = Currency.EUR
        val rates = mapOf(
            Pair(sourceCurrency, targetCurrency) to 0.85
        )
        val rateProvider = InMemoryExchangeRateProvider(rates)
        val money = Money(initialAmount, sourceCurrency)

        // Ejecución: convertir a EUR
        val converted = money.convertTo(targetCurrency, rateProvider)

        // Verificación: debe ser 100 * 0.85 = 85 EUR
        converted.amount.shouldBe(85.0)
        converted.currency.shouldBe(targetCurrency)
    }
})
```

Podemos agrupar pruebas relacionadas en un bloque de `context`:

```Kotlin
// src/main/kotlin/com/example/Domain.kt
package com.example

// --- Dominio de pagos con tarjeta ---

data class CardPayment(
    val cardNumber: String,
    val amount: Double
) {
    fun pay(balanceProvider: BalanceProvider): Boolean {
        val balance = balanceProvider.getBalance(cardNumber)
        return if (balance >= amount) {
            balanceProvider.debit(cardNumber, amount)
            true
        } else {
            false
        }
    }
}

interface BalanceProvider {
    fun getBalance(cardNumber: String): Double
    fun debit(cardNumber: String, amount: Double)
}

class InMemoryBalanceProvider(initialBalances: Map<String, Double>) : BalanceProvider {
    private val balances = initialBalances.toMutableMap()
    override fun getBalance(cardNumber: String) = balances[cardNumber] ?: 0.0
    override fun debit(cardNumber: String, amount: Double) {
        val current = balances[cardNumber] ?: 0.0
        require(amount > 0) { "Amount must be positive" }
        require(current >= amount) { "Insufficient balance" }
        balances[cardNumber] = current - amount
    }
}

// --- Dominio de transferencias bancarias ---

interface BankTransferService {
    fun transfer(fromAccount: String, toAccount: String, amount: Double): Boolean
}

class InMemoryBankTransferService(
    initialAccounts: Map<String, Double>
) : BankTransferService {
    private val accounts = initialAccounts.toMutableMap()
    override fun transfer(fromAccount: String, toAccount: String, amount: Double): Boolean {
        val fromBalance = accounts[fromAccount] ?: 0.0
        require(amount > 0) { "Amount must be positive" }
        if (fromBalance < amount) return false
        accounts[fromAccount] = fromBalance - amount
        accounts[toAccount] = accounts.getOrDefault(toAccount, 0.0) + amount
        return true
    }
}

// --- Servicio que une ambos casos ---

class PaymentService(
    private val balanceProvider: BalanceProvider,
    private val bankTransferService: BankTransferService
) {
    fun payWithCard(payment: CardPayment): Boolean =
        payment.pay(balanceProvider)

    fun transfer(from: String, to: String, amount: Double): Boolean =
        bankTransferService.transfer(from, to, amount)
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/PaymentTests.kt
package com.example.tests

import io.kotest.core.spec.style.ShouldSpec
        import io.kotest.matchers.booleans.shouldBeTrue
        import com.example.CardPayment
        import com.example.InMemoryBalanceProvider
        import com.example.InMemoryBankTransferService
        import com.example.PaymentService

class PaymentTests : ShouldSpec({
    context("CardPayments") {
        should("Make a card payment") {
            val cardNumber = "5555-6666-7777-8888"
            val initialBalances = mapOf(cardNumber to 200.0)
            val balanceProvider = InMemoryBalanceProvider(initialBalances)
            val bankService = InMemoryBankTransferService(emptyMap())
            val paymentService = PaymentService(balanceProvider, bankService)

            // Ejecutar pago con tarjeta de 50.0
            val result = paymentService.payWithCard(CardPayment(cardNumber, 50.0))
            result.shouldBeTrue()
        }
    }

    context("BankTransfers") {
        should("Make an external bank transfer") {
            val fromAccount = "acct-123"
            val toAccount = "acct-456"
            val initialAccounts = mapOf(fromAccount to 300.0, toAccount to 100.0)
            val balanceProvider = InMemoryBalanceProvider(emptyMap())
            val bankService = InMemoryBankTransferService(initialAccounts)
            val paymentService = PaymentService(balanceProvider, bankService)

            // Ejecutar transferencia de 120.0
            val result = paymentService.transfer(fromAccount, toAccount, 120.0)
            result.shouldBeTrue()
        }
    }
})

```

#### 3.3. Especificaciones de características (`features`)

A continuación, veamos cómo se pueden escribir pruebas basadas en [Cucumber](https://www.baeldung.com/cucumber-rest-api-testing), una herramienta de uso común para las pruebas de aceptación del usuario, basadas en las palabras clave  `feature` (funcionalidad) y `scenario` (escenario):

```Kotlin
// --- Dominio de HomePage (signup/signin) ---

class HomePage {
    private val users = mutableMapOf<String, String>()

    fun signup(email: String, password: String): Boolean {
        if (users.containsKey(email)) return false
        users[email] = password
        return true
    }

    fun signin(email: String, password: String): Boolean =
        users[email] == password
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/HomePageTests.kt
package com.example.tests

import io.kotest.core.spec.style.FeatureSpec
        import io.kotest.matchers.booleans.shouldBeTrue
        import io.kotest.matchers.booleans.shouldBeFalse
        import com.example.HomePage

class HomePageTests : FeatureSpec({
    feature("signup") {
        scenario("should allow user to signup with email") {
            val homePage = HomePage()
            val result = homePage.signup("user@example.com", "securePass")
            result.shouldBeTrue()
        }
        scenario("should not allow signup with existing email") {
            val homePage = HomePage()
            homePage.signup("user@example.com", "pass1")
            val duplicate = homePage.signup("user@example.com", "pass2")
            duplicate.shouldBeFalse()
        }
    }

    feature("signin") {
        scenario("should allow user with valid credentials to login") {
            val homePage = HomePage()
            homePage.signup("user2@example.com", "password")
            val loginResult = homePage.signin("user2@example.com", "password")
            loginResult.shouldBeTrue()
        }
        scenario("should reject user with invalid credentials") {
            val homePage = HomePage()
            homePage.signup("user3@example.com", "pass123")
            val loginFail = homePage.signin("user3@example.com", "wrongPass")
            loginFail.shouldBeFalse()
        }
    }
})
```

#### 3.4. Especificaciones mediante descripciones (`describe`)

Usando `describe`, podemos escribir pruebas en un estilo muy popular entre los desarrolladores de Javascript y Ruby, de hecho será el que usaremos en nuestros ejemplos:

```Kotlin
// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/PaymentDescribeSpecTests.kt
package com.example.tests

import io.kotest.core.spec.style.DescribeSpec
import io.kotest.matchers.booleans.shouldBeTrue
import com.example.CardPayment
import com.example.InMemoryBalanceProvider
import com.example.InMemoryBankTransferService
import com.example.PaymentService

class PaymentTests : DescribeSpec({
    describe("CardPayments") {
        it("Should make a card payment") {
            val cardNumber = "9999-8888-7777-6666"
            val balanceProvider = InMemoryBalanceProvider(mapOf(cardNumber to 150.0))
            val bankService = InMemoryBankTransferService(emptyMap())
            val service = PaymentService(balanceProvider, bankService)
            val payment = CardPayment(cardNumber, 75.0)

            val result = service.payWithCard(payment)

            result.shouldBeTrue()
        }
    }
    describe("BankTransfers") {
        it("Should make an external bank transfer") {
            val from = "acct-A"
            val to = "acct-B"
            val bankService = InMemoryBankTransferService(mapOf(from to 500.0, to to 50.0))
            val balanceProvider = InMemoryBalanceProvider(emptyMap())
            val service = PaymentService(balanceProvider, bankService)

            val result = service.transfer(from, to, 200.0)

            result.shouldBeTrue()
        }
    }
})
```

### 4. Assertions

Anteriormente hemos visto que Kotest tiene bibliotecas destinadas a aserciones, las afirmaciones que tienen que cumplirse tras realizar el test. Estas bibliotecas nos brindan varias funciones de *comparación* para escribir las afirmaciones que deben cumplirse en nuestras pruebas. Hay dos grandes categorías de bibliotecas de aserciones:

* Core matchers
* External matchers

Veamos algunos ejemplos de comparadores que permite la *[biblioteca kotest-assertions-core](https://search.maven.org/search?q=g:io.kotest%20AND%20a:kotest-assertions-core)*:

```kotlin
class AssertionExamples : StringSpec({
    "should verify object equality with shouldBe" {
        val result = 42
        val expected = 42
        // Verifica que result.equals(expected)
        result.shouldBe(expected)
    }

    "should verify boolean expression is true with shouldBeTrue" {
        val result = (5 > 2)
        // Verifica que la expresión sea true
        result.shouldBeTrue()
    }

    "should verify object type with shouldBeTypeOf" {
        val result: Any = 3.14
        // Verifica que result sea exactamente Double
        result.shouldBeTypeOf<Double>()
    }

    "should verify map contains given key with shouldContainKey" {
        val map = mapOf("a" to 1, "b" to 2)
        val key = "a"
        // Verifica que el mapa contenga la clave 'a'
        map.shouldContainKey(key)
    }

    "should verify map contains given values with shouldContainValues" {
        val map = mapOf(1 to "one", 2 to "two", 3 to "three")
        val values = listOf("two", "three")
        // Verifica que el mapa contenga los valores 'two' y 'three'
        map.shouldContainValues(values)
    }

    "should verify string contains substring with shouldContain" {
        val text = "Hello Kotest Framework"
        // Verifica que la cadena contenga 'Kotest'
        text.shouldContain("Kotest")
    }

    "should verify string equality ignoring case with shouldBeEqualIgnoringCase" {
        val actual = "KoTeSt"
        val other = "kotest"
        // Verifica igualdad ignorando mayúsculas/minúsculas
        actual.shouldBeEqualIgnoringCase(other)
    }

    "should verify file size with shouldHaveFileSize" {
        // Crea un archivo temporal de ejemplo
        val file = File("temp.txt").apply {
            writeText("Kotest")
        }
        // Verifica que el tamaño del archivo sea 6 bytes ("Kotest" tiene 6 caracteres)
        file.shouldHaveFileSize(6)
        file.delete()
    }

    "should verify date ordering with shouldBeBefore" {
        val date1 = LocalDate.parse("2025-05-01")
        val date2 = LocalDate.parse("2025-05-10")
        // Verifica que date1 sea anterior a date2
        date1.shouldBeBefore(date2)
    }
})
```

Además del módulo central `kotest-assertions-core`, Kotest ofrece un ecosistema de módulos de aserciones especializadas que cubren multitud de escenarios más allá de la igualdad de objetos o condiciones básicas. Estos módulos se publican por separado y se añaden como dependencias cuando los necesitas; a continuación tienes los más habituales y un breve ejemplo de qué aportan:

| Módulo                          | Artefacto                                | Qué añade                                          | Ejemplo de uso                                             |
| ------------------------------- | ---------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------- |
| JSON                            | `io.kotest:kotest-assertions-json`       | Aserciones para comparar estructuras JSON          | `jsonString.shouldMatchJson("{ \"a\": 1 }")`               |
| XML                             | `io.kotest:kotest-assertions-xml`        | Aserciones sobre documentos XML                    | `xml.shouldHaveXPath("/root/element")`                     |
| JDBC / Bases de datos           | `io.kotest:kotest-assertions-db`         | Matchers para `ResultSet`, comprobaciones de filas | `resultSet.shouldHaveRows(3)`                              |
| Java Time (fechas y horas)      | `io.kotest:kotest-assertions-time`       | Aserciones para `LocalDate`, `Instant`, `Duration` | `instant.shouldBeAfter(otherInstant)`                      |
| Coroutines                      | `io.kotest:kotest-assertions-coroutines` | Aserciones para flujos y suspending functions      | `flow.shouldEmit(listOf(1,2,3))`                           |
| Spring / Testcontainers / Mockk | `io.kotest:kotest-extensions-*`          | Integraciones específicas con frameworks externos  | `@KotestSpringExtension` para tests con contexto de Spring |
| Arrow (programación funcional)  | `io.kotest:kotest-assertions-arrow`      | Matchers para `Option`, `Either`, `Validated`      | `either.shouldBeRight(42)`                                 |

Para integralos, en tu `build.gradle.kts`, simplemente añade la dependencia correspondiente:

```kotlin
dependencies {
  testImplementation("io.kotest:kotest-assertions-core:5.8.0")
  testImplementation("io.kotest:kotest-assertions-json:5.8.0")
  testImplementation("io.kotest:kotest-assertions-db:5.8.0")
  // …otros módulos según necesidad
}
```

Luego podrás importar sus funciones y matchers de forma natural:

```kotlin
import io.kotest.assertions.json.shouldMatchJson
import io.kotest.assertions.db.shouldHaveRows
```


### 5. Pruebas de excepciones

Por otro lado, probar excepciones con Kotest es muy sencillo:

```Kotlin
// src/main/kotlin/com/example/Validation.kt
package com.example

// Excepción personalizada para validación de entrada
class ValidationException(message: String) : RuntimeException(message)

// Componente que procesa y valida entradas
object InputProcessor {
    /**
     * Procesa una entrada de texto. Lanza ValidationException si la entrada no cumple el formato.
     */
    fun process(input: String) {
        // Regla de validación: la entrada debe tener al menos 5 caracteres y no contener espacios al inicio
        if (input.length < 5) {
            throw ValidationException("Invalid input: length must be at least 5 characters")
        }
        if (input.startsWith(" ")) {
            throw ValidationException("Invalid input: must not start with whitespace")
        }
        // Lógica de procesamiento (simulada)
        println("Processed: $input")
    }
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/ExceptionTests.kt
package com.example.tests

import io.kotest.assertions.throwables.shouldThrow
        import io.kotest.core.spec.style.StringSpec
        import io.kotest.matchers.string.shouldStartWith
        import com.example.InputProcessor
        import com.example.ValidationException

class ExceptionTests : StringSpec({
    "should throw ValidationException for short input" {
        val exception = shouldThrow<ValidationException> {
            // Input de longitud menor a 5 dispara la excepción
            InputProcessor.process("abc")
        }
        // Verifica que el mensaje comience con "Invalid input"
        exception.message.shouldStartWith("Invalid input")
    }

    "should throw ValidationException for leading whitespace" {
        val exception = shouldThrow<ValidationException> {
            // Input que empieza con espacio dispara la excepción
            InputProcessor.process(" hello")
        }
        exception.message.shouldStartWith("Invalid input")
    }

    "should process valid input without exception" {
        // Para un input válido, no debe lanzar excepción
        InputProcessor.process("helloWorld")
    }
})

```

### 6. Ganchos de ciclo de vida

Podemos usar ganchos de ciclo de vida para configurar o desmontar el escenario necesario de objetos antes o después de las pruebas. Estos ganchos (`beforeTest` y `afterTest`) son muy similares a los métodos de instalación y desmontaje del framework Junit. Veamos un ejemplo:

```Kotlin
// src/main/kotlin/com/example/TransactionDomain.kt
package com.example

// Representación de una transacción financiera
data class Transaction(
    val id: Int,
    val amount: Double,
    val description: String
)

// Repositorio en memoria para gestionar transacciones
class TransactionRepository {
    private val transactions = mutableListOf<Transaction>()

    /** Añade una transacción */
    fun add(transaction: Transaction) {
        transactions.add(transaction)
    }

    /** Devuelve todas las transacciones registradas */
    fun getAll(): List<Transaction> = transactions.toList()

    /** Elimina todas las transacciones */
    fun clear() {
        transactions.clear()
    }
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tests/TransactionStatementSpec.kt
package com.example.tests

import io.kotest.core.spec.style.ShouldSpec
        import io.kotest.matchers.collections.shouldHaveSize
        import com.example.Transaction
        import com.example.TransactionRepository

class TransactionStatementSpec : ShouldSpec({
    // Repositorio compartido entre hooks y tests
    val repo = TransactionRepository()

    beforeTest {
        // Se ejecuta antes de cada test: añadimos dos transacciones de ejemplo
        repo.add(Transaction(1, 100.0, "Deposit"))
        repo.add(Transaction(2, -50.0, "Withdrawal"))
    }

    afterTest { _, _ ->
        // Se ejecuta después de cada test: limpiamos todas las transacciones
        repo.clear()
    }

    context("Transaction statement") {
        should("contain the added transactions") {
            val statement = repo.getAll()
            // Esperamos exactamente 2 transacciones en el estado
            statement.shouldHaveSize(2)
        }

        should("preserve the order of transactions") {
            val statement = repo.getAll()
            // La primera debe ser depósito, la segunda retiro
            statement[0].description shouldBe "Deposit"
            statement[1].description shouldBe "Withdrawal"
        }
    }
})
```

### 7. Pruebas basadas en datos

Las pruebas basadas en datos en Kotest son similares a las [pruebas parametrizadas en Junit5](https://www.baeldung.com/parameterized-tests-junit-5). Podemos proporcionar varias entradas a un solo caso de prueba para verificar diferentes ejemplos en lugar de escribir varias pruebas con solo datos de entrada diferentes. Podemos usar la función `useData` de la [biblioteca kotest-framework-datatest-jvm](https://search.maven.org/search?q=g:io.kotest%20AND%20a:kotest-framework-datatest-jvm) para proporcionar datos a las pruebas.

Veamos un ejemplo:

```kotlin
// src/main/kotlin/com/example/tax/TaxDomain.kt
package com.example.tax

/**
 * Clases de impuesto disponibles.
 */
enum class TaxClass {
    ONE,   // Tipo impositivo reducido
    TWO,   // Tipo impositivo estándar
    THREE  // Tipo impositivo especial
}

/**
 * Calcula el impuesto a pagar según la renta y la clase de impuesto.
 * - ONE: 30% de la renta
 * - TWO: 35% de la renta
 * - THREE: 20% de la renta
 */
fun calculateTax(income: Long, taxClass: TaxClass): Long = when (taxClass) {
    TaxClass.ONE -> (income * 0.30).toLong()
    TaxClass.TWO -> (income * 0.35).toLong()
    TaxClass.THREE -> (income * 0.20).toLong()
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/tax/IncomeTaxTests.kt
package com.example.tax

import io.kotest.core.spec.style.FunSpec
import io.kotest.data.blocking.withData
import io.kotest.matchers.shouldBe

/**
 * Datos de prueba para distintos escenarios de cálculo de impuesto.
 */
data class TaxTestData(val income: Long, val taxClass: TaxClass, val expectedTaxAmount: Long)

/**
 * Tests parametrizados para la función calculateTax usando Kotest FunSpec y withData.
 */
class IncomeTaxTests : FunSpec({
    withData(
        // income, taxClass, expectedTaxAmount
        TaxTestData(1000, TaxClass.ONE, 300),
        TaxTestData(1000, TaxClass.TWO, 350),
        TaxTestData(1000, TaxClass.THREE, 200),
        TaxTestData(5000, TaxClass.ONE, 1500),
        TaxTestData(5000, TaxClass.TWO, 1750),
        TaxTestData(5000, TaxClass.THREE, 1000)
    ) { (income, taxClass, expectedTaxAmount) ->
        // Ejecución y verificación
        calculateTax(income, taxClass) shouldBe expectedTaxAmount
    }
})
```

### 8. Pruebas no deterministas

A veces, necesitamos probar funciones que no devuelven resultados sincrónicamente. Desafortunadamente, es complicado probar tales funciones, ya que tenemos que escribir código especial para esperar los resultados utilizando técnicas como funciones callback o dormir el hilo.

Kotest proporciona algunas funciones útiles que podemos usar para escribir este tipo de pruebas no deterministas de forma declarativa.

Veamos un ejemplo de la función `eventually` :

```kotlin
class TransactionTests : ShouldSpec({
    // Creamos el repositorio que simula el procesamiento asíncrono
    val transactionRepo = TransactionRepo()

    should("Should make transaction complete") {
        // El bloque `eventually` reintenta la aserción hasta que pase o expire el tiempo máximo
        eventually({
            // Tiempo total máximo de espera: 5.000 ms
            duration = 5000
            // Intervalo entre cada intento: 1.000 ms
            interval = FixedInterval(1000)
        }) {
            // Esta aserción se verificará repetidamente:
            // llamamos a getStatus(120) y esperamos que devuelva "COMPLETE"
            transactionRepo.getStatus(120) shouldBe "COMPLETE"
        }
    }
})
```

Aquí, nuestra prueba verificará el estado de la transacción `transactionRepo.getStatus` cada segundo (interval), hasta llegar a 5 segundos (duration).

### 9. Mocking

Podemos integrar cualquier biblioteca de simulación como [mockk](https://www.baeldung.com/kotlin/mockk) con Kotest, biblioteca que veremos mas adelante. Kotest no proporciona su propia biblioteca de simulación:

```kotlin
// src/main/kotlin/com/example/exchange/Domain.kt
package com.example.exchange

/**
 * Representa una cantidad de dinero en una moneda.
 */
data class Money(val amount: Long, val currency: String)

/**
 * Interfaz para obtener la tasa de cambio de un par de monedas.
 */
interface ExchangeRateProvider {
    /**
     * Devuelve la tasa para el par indicado, p.ej. "USDEUR".
     */
    fun rate(pair: String): Double
}

/**
 * Servicio que realiza conversiones de moneda usando un ExchangeRateProvider.
 */
class ExchangeService(private val rateProvider: ExchangeRateProvider) {
    /**
     * Convierte la cantidad `money` a la `targetCurrency`.
     * Calcula amount * tasa y devuelve la parte entera.
     */
    fun exchange(money: Money, targetCurrency: String): Long {
        val pair = money.currency + targetCurrency
        val rate = rateProvider.rate(pair)
        return (money.amount * rate).toLong()
    }
}

/**
 * Implementación en memoria de ExchangeRateProvider.
 * Recibe un mapa de pares de moneda (por ejemplo "USDEUR") a tasa.
 */
class InMemoryExchangeRateProvider(
    private val rates: Map<String, Double>
) : ExchangeRateProvider {
    override fun rate(pair: String): Double =
        rates[pair] ?: throw IllegalArgumentException("Rate not found for pair $pair")
}

// #######################
// ########## TEST #######
// #######################
// src/test/kotlin/com/example/exchange/ExchangeServiceTest.kt
package com.example.exchange

import io.kotest.core.spec.style.FunSpec
        import io.kotest.matchers.shouldBe
        import io.mockk.every
        import io.mockk.mockk

class ExchangeServiceTest : FunSpec({
    // Mock del proveedor de tasas
    val exchangeRateProvider = mockk<ExchangeRateProvider>()
    // Servicio bajo prueba
    val service = ExchangeService(exchangeRateProvider)

    test("Exchanges money using rate from exchange rate service (mocked)") {
        every { exchangeRateProvider.rate("USDEUR") } returns 0.9
        service.exchange(Money(1200, "USD"), "EUR") shouldBe 1080
    }

    test("Exchanges money using in-memory provider without mock") {
        // Proveedor real con datos en memoria
        val rates = mapOf("USDEUR" to 0.9, "EURUSD" to 1.1)
        val realProvider = InMemoryExchangeRateProvider(rates)
        val realService = ExchangeService(realProvider)
        realService.exchange(Money(500, "USD"), "EUR") shouldBe 450
    }
})

```

### 10. Cobertura de pruebas

Podemos integrar [Jacoco](https://www.baeldung.com/jacoco) con Kotest para medir la cobertura de las pruebas. Para integrar, debemos asegurarnos de que los informes de cobertura de prueba se generen después de ejecutar las pruebas unitarias:

```kotlin
tasks.test {
    finalizedBy(tasks.jacocoTestReport)
}
```

Podemos encontrar el informe HTML de cobertura de prueba dentro del *directorio `$buildDir/reports/jacoco/test`* .

### 11. Agrupación de pruebas con etiquetas

A veces, queremos ejecutar solo ciertas pruebas en un entorno específico. Por ejemplo, es posible que deseemos evitar ejecutar algunas pruebas lentas como parte de la verificación de una pull request git. Para hacer eso, primero debemos etiquetar nuestras pruebas:

```kotlin
// Definimos un tag de aplicación “SlowTest”
val SlowTest = NamedTag("SlowTest")

@Tags(SlowTest)      // 👉 asignamos el tag “SlowTest” a toda la clase
class SlowTests : ShouldSpec({

    should("perform a slow operation") {
        // … código de test que tarda, p.ej. llamadas reales a base de datos
    }

})
```

### 12. Conclusión

Kotest ofrece un ecosistema flexible, expresivo y modular que, combinado con buenas prácticas (interfaces, mocks, ganchos, tags), permite diseñar suites de pruebas claras, aisladas y adaptables a distintos entornos (unitarios, integración, lentos). Se ha podido comprender no solo la sintaxis, sino la estrategia global de testing en Kotlin, desde casos sencillos hasta escenarios avanzados.

Algunos ejemplos de código se pueden encontrar [en GitHub](https://github.com/Baeldung/kotlin-tutorials/tree/master/kotlin-kotest/kotest) 

### 13. Recursos

* [¿Cómo elaborar casos de prueba?](https://surprograma.github.io/libro-disenio-oop/docs/pruebas-automatizadas/elaborar-casos-prueba/)
* [Test unitario avanzado](http://wiki.uqbar.org/wiki/articles/testeo-unitario-avanzado.html)

## Fuentes

* [Introduction to Kotest](https://www.baeldung.com/kotlin/kotest)
* [Ejemplos de uso de Kotest](https://github.com/Baeldung/kotlin-tutorials/tree/master/kotlin-kotest/kotest)
* [Ejemplos de test en kotlin](https://github.com/Baeldung/kotlin-tutorials/tree/master/kotlin-testing).
