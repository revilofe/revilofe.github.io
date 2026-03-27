---
title: "UD 5 - 5.2.2 MockK"
description: Biblioteca de mocking para Kotlin orientada a simular colaboraciones y comprobar interacciones en tests unitarios.
summary: Uso práctico de MockK para crear mocks, espías, capturar argumentos, simular singletons y controlar funciones con retorno Unit.
authors:
  - Eduardo Fdez
date: 2026-03-27
icon: "material/file-document-outline"
permalink: /edes/unidad3/3.2.2
categories:
  - EDES
tags:
  - EDES
  - Kotlin
  - MockK
  - mocking
  - testing
---

## 5.2.2 MockK

Cuando una unidad de código depende de otra, aparece una pregunta importante: ¿cómo probamos una clase sin tener que ejecutar siempre sus dependencias reales? Ahí es donde entra **MockK**.

En la normativa de la unidad, este contenido se relaciona con el diseño y la automatización de pruebas, ya que MockK permite aislar dependencias, construir escenarios controlados y verificar colaboraciones dentro de un test unitario.

| Código | Descripción |
| --- | --- |
| RA3 | Verifica el funcionamiento de programas diseñando y realizando pruebas. |
| CE b | Se han definido casos de prueba. |
| CE f | Se han efectuado pruebas unitarias de clases y funciones. |
| CE g | Se han implementado pruebas automáticas. |
| CE i | Se han utilizado dobles de prueba para aislar los componentes durante las pruebas. |

!!! abstract "Qué vas a aprender en este apartado"
    - Entender para qué sirve una biblioteca de mocking en Kotlin.
    - Crear mocks, spies y mocks relajados con MockK.
    - Capturar argumentos y controlar colaboraciones entre objetos.
    - Simular singletons y funciones con retorno `Unit`.

### 1. Qué problema resuelve MockK

MockK es una biblioteca de *mocking* para Kotlin. Su objetivo es permitirnos **simular colaboraciones** entre objetos durante una prueba.

En la práctica, esto sirve para:

- aislar la unidad que estamos probando;
- controlar la respuesta de dependencias externas;
- verificar que una colaboración ocurrió como esperábamos;
- evitar llamadas reales a bases de datos, servicios remotos o componentes costosos.

En Kotlin esto cobra especial importancia porque muchas clases y métodos son finales por defecto, y no todas las bibliotecas de mocking manejan bien ese escenario. MockK está pensada precisamente para encajar mejor con las características del lenguaje.

!!! note "Qué significa mockear"
    Mockear no es "falsear por falsear". Se trata de sustituir una dependencia real por un doble de prueba controlado para centrarnos en el comportamiento de la unidad que queremos verificar.

### 2. Instalación básica

La configuración mínima en Gradle suele quedar así:

```kotlin
val mockkVersion = "x.y.z"

dependencies {
    testImplementation("io.mockk:mockk:$mockkVersion")
}
```

Como criterio general, conviene consultar la documentación del proyecto para elegir una versión compatible con la versión de Kotlin y del motor de pruebas que uses.

### 3. Ejemplo básico de mock

Partimos de un servicio sencillo:

```kotlin
class TestableService {
    fun getDataFromDb(testParameter: String): String {
        error("Implementación real no disponible en este ejemplo")
    }

    fun doSomethingElse(testParameter: String): String {
        return "I don't want to!"
    }
}
```

Y ahora un test que simula su comportamiento:

```kotlin
import io.mockk.every
import io.mockk.mockk
import io.mockk.verify
import kotlin.test.Test
import kotlin.test.assertEquals

class BasicMockKTest {
    @Test
    fun givenServiceMock_whenCallingMockedMethod_thenCorrectlyVerified() {
        val service = mockk<TestableService>()

        every { service.getDataFromDb("Expected Param") } returns "Expected Output"

        val result = service.getDataFromDb("Expected Param")

        verify { service.getDataFromDb("Expected Param") }
        assertEquals("Expected Output", result)
    }
}
```

Las piezas importantes del ejemplo son:

- `mockk<T>()` crea el objeto simulado;
- `every { ... } returns ...` define su comportamiento;
- `verify { ... }` comprueba que la interacción ocurrió.

### 4. Uso de anotaciones

MockK también permite declarar mocks mediante anotaciones. Esto resulta útil cuando el test tiene varias dependencias y quieres dejar más visible qué papel juega cada una.

```kotlin
import io.mockk.InjectMockKs
import io.mockk.MockK
import io.mockk.MockKAnnotations
import kotlin.test.BeforeTest

class InjectTestService {
    lateinit var service1: TestableService
    lateinit var service2: TestableService

    fun invokeService1(): String = service1.getDataFromDb("Test Param")
}

class AnnotationMockKUnitTest {

    @MockK
    lateinit var service1: TestableService

    @MockK
    lateinit var service2: TestableService

    @InjectMockKs
    var objectUnderTest = InjectTestService()

    @BeforeTest
    fun setUp() {
        MockKAnnotations.init(this)
    }
}
```

Aquí MockK intenta inyectar los mocks en el objeto bajo prueba, normalmente por nombre y después por tipo. Esto reduce bastante el trabajo repetitivo cuando el test tiene varias colaboraciones.

### 5. Spy: mezclar comportamiento real y simulado

Un **spy** crea un objeto que conserva su comportamiento real salvo en los métodos que decidimos sustituir.

```kotlin
import io.mockk.every
import io.mockk.spyk
import kotlin.test.Test
import kotlin.test.assertEquals

class SpyKExampleTest {
    @Test
    fun givenServiceSpy_whenMockingOnlyOneMethod_thenOtherMethodsShouldBehaveAsOriginalObject() {
        val service = spyk<TestableService>()

        every { service.getDataFromDb(any()) } returns "Mocked Output"

        val firstResult = service.getDataFromDb("Any Param")
        val secondResult = service.doSomethingElse("Any Param")

        assertEquals("Mocked Output", firstResult)
        assertEquals("I don't want to!", secondResult)
    }
}
```

Esto es útil cuando la clase real tiene mucho comportamiento válido y solo necesitas intervenir en una parte concreta.

También puede declararse con anotación:

```kotlin
import io.mockk.SpyK

class SpyKUnitTest {
    @SpyK
    lateinit var service: TestableService
}
```

### 6. Mocks relajados

Por defecto, un mock lanza una excepción si llamas a un método cuyo comportamiento no has definido. Cuando ese nivel de control no compensa, MockK permite usar **mocks relajados**.

```kotlin
import io.mockk.mockk
import kotlin.test.Test
import kotlin.test.assertEquals

class RelaxedMockKExampleTest {
    @Test
    fun givenRelaxedMock_whenCallingNotMockedMethod_thenReturnDefaultValue() {
        val service = mockk<TestableService>(relaxed = true)

        val result = service.getDataFromDb("Any Param")

        assertEquals("", result)
    }
}
```

En este caso, MockK devuelve valores por defecto según el tipo de retorno. Para `String`, devuelve una cadena vacía.

La variante con anotación sería:

```kotlin
import io.mockk.RelaxedMockK

class RelaxedMockKUnitTest {
    @RelaxedMockK
    lateinit var service: TestableService
}
```

### 7. Mockear objetos `object`

Kotlin permite declarar singletons con `object`. MockK proporciona `mockkObject` para poder simular ese tipo de elementos.

```kotlin
import io.mockk.every
import io.mockk.mockkObject
import kotlin.test.Test
import kotlin.test.assertEquals

object SingletonService {
    fun getDataFromDb(testParameter: String): String = "Real Output for $testParameter"
}

class ObjectMockKTest {
    @Test
    fun givenObject_whenMockingIt_thenMockedMethodShouldReturnProperValue() {
        mockkObject(SingletonService)

        val firstResult = SingletonService.getDataFromDb("Any Param")
        assertEquals("Real Output for Any Param", firstResult)

        every { SingletonService.getDataFromDb(any()) } returns "Mocked Output"

        val secondResult = SingletonService.getDataFromDb("Any Param")
        assertEquals("Mocked Output", secondResult)
    }
}
```

Este caso aparece menos en código bien desacoplado, pero existe, especialmente en utilidades, *helpers* o adaptadores heredados.

### 8. Mockeado jerárquico

Otra posibilidad es construir un mock que ya devuelva otros mocks en sus propiedades.

```kotlin
import io.mockk.every
import io.mockk.mockk
import kotlin.test.Test
import kotlin.test.assertEquals

class Foo {
    lateinit var name: String
    lateinit var bar: Bar
}

class Bar {
    lateinit var nickname: String
}

class HierarchicalMockKTest {
    @Test
    fun givenHierarchicalClass_whenMockingIt_thenReturnProperValue() {
        val foo = mockk<Foo> {
            every { name } returns "Karol"
            every { bar } returns mockk {
                every { nickname } returns "Tomato"
            }
        }

        assertEquals("Karol", foo.name)
        assertEquals("Tomato", foo.bar.nickname)
    }
}
```

Este enfoque es útil cuando el objeto bajo prueba navega por varias propiedades encadenadas y quieres controlar ese recorrido.

### 9. Captura de argumentos

En ocasiones no basta con comprobar que se llamó a un método. También necesitamos saber **con qué argumentos** se invocó.

#### 9.1. Usando `slot`

```kotlin
import io.mockk.capture
import io.mockk.every
import io.mockk.mockk
import io.mockk.slot
import kotlin.test.Test
import kotlin.test.assertEquals

class CapturingSlotTest {
    @Test
    fun givenMock_whenCapturingParamValue_thenProperValueShouldBeCaptured() {
        val service = mockk<TestableService>()
        val slot = slot<String>()

        every { service.getDataFromDb(capture(slot)) } returns "Expected Output"

        service.getDataFromDb("Expected Param")

        assertEquals("Expected Param", slot.captured)
    }
}
```

#### 9.2. Usando una lista mutable

Si quieres almacenar varias invocaciones, una lista suele ser más cómoda:

```kotlin
import io.mockk.capture
import io.mockk.every
import io.mockk.mockk
import kotlin.test.Test
import kotlin.test.assertEquals

class CapturingListTest {
    @Test
    fun givenMock_whenCapturingParamsValues_thenProperValuesShouldBeCaptured() {
        val service = mockk<TestableService>()
        val calls = mutableListOf<String>()

        every { service.getDataFromDb(capture(calls)) } returns "Expected Output"

        service.getDataFromDb("Expected Param 1")
        service.getDataFromDb("Expected Param 2")

        assertEquals(2, calls.size)
        assertEquals("Expected Param 1", calls[0])
        assertEquals("Expected Param 2", calls[1])
    }
}
```

### 10. Stubbing de funciones que devuelven `Unit`

En Kotlin, un método que devuelve `Unit` no devuelve un valor útil, pero sigue pudiendo tener efectos laterales. MockK permite controlar ese comportamiento.

Partimos de este método:

```kotlin
class TestableServiceWithUnit {
    fun addHelloWorld(strList: MutableList<String>) {
        println("addHelloWorld() is called")
        strList += "Hello World!"
    }
}
```

#### 10.1. Hacer que no haga nada

Podemos omitir la ejecución real de varias formas:

```kotlin
every { service.addHelloWorld(any()) } returns Unit
every { service.addHelloWorld(any()) } answers { Unit }
every { service.addHelloWorld(any()) } just runs
```

La forma más legible suele ser `just runs`.

```kotlin
import io.mockk.every
import io.mockk.just
import io.mockk.mockk
import io.mockk.runs
import kotlin.test.Test
import kotlin.test.assertTrue

class UnitStubTest {
    @Test
    fun givenServiceMock_whenCallingMethodReturnsUnit_thenCorrectlyVerified() {
        val service = mockk<TestableServiceWithUnit>()
        val myList = mutableListOf<String>()

        every { service.addHelloWorld(any()) } just runs
        service.addHelloWorld(myList)

        assertTrue(myList.isEmpty())
    }
}
```

#### 10.2. Llamar a la implementación original

Si en lugar de anular el comportamiento quieres ejecutar el original, puedes usar `callOriginal()`.

```kotlin
import io.mockk.answers
import io.mockk.every
import io.mockk.mockk
import kotlin.test.Test
import kotlin.test.assertEquals

class CallOriginalTest {
    @Test
    fun givenServiceMock_whenCallingOriginalMethod_thenCorrectlyVerified() {
        val service = mockk<TestableServiceWithUnit>()
        val myList = mutableListOf<String>()

        every { service.addHelloWorld(any()) } answers { callOriginal() }
        service.addHelloWorld(myList)

        assertEquals(1, myList.size)
        assertEquals("Hello World!", myList.first())
    }
}
```

#### 10.3. Combinar varios escenarios

El verdadero interés de `callOriginal()` aparece cuando no quieres el mismo comportamiento en todas las llamadas.

```kotlin
import io.mockk.answers
import io.mockk.every
import io.mockk.just
import io.mockk.match
import io.mockk.mockk
import io.mockk.runs
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertTrue

class TwoScenariosTest {
    @Test
    fun givenServiceMock_whenStubbingTwoScenarios_thenCorrectlyVerified() {
        val service = mockk<TestableServiceWithUnit>()
        val kaiList = mutableListOf("Kai")
        val emptyList = mutableListOf<String>()

        every { service.addHelloWorld(any()) } just runs
        every { service.addHelloWorld(match { "Kai" in it }) } answers { callOriginal() }

        service.addHelloWorld(kaiList)
        service.addHelloWorld(emptyList)

        assertEquals(listOf("Kai", "Hello World!"), kaiList)
        assertTrue(emptyList.isEmpty())
    }
}
```

En la práctica, esto te permite adaptar la simulación a distintos contextos sin renunciar al comportamiento real cuando realmente te interesa.

### 11. Cuándo conviene usar MockK y cuándo no

MockK es útil, pero también es fácil abusar de él. Como regla general:

- úsalo cuando una dependencia hace costosa o inestable la prueba;
- úsalo cuando necesitas verificar una interacción concreta;
- evita mockear clases triviales que podrías sustituir por objetos reales simples;
- no conviertas el test en una copia exacta de la implementación interna.

Si un test depende de demasiados mocks, muchas veces no es que falte MockK, sino que **sobra acoplamiento en el diseño**.

### 12. Conclusión

MockK es una herramienta muy práctica para escribir pruebas unitarias en Kotlin cuando necesitamos aislar colaboraciones, controlar respuestas y verificar interacciones. Bien usado, hace que los tests sean más precisos y más fáciles de mantener.

La idea clave con la que conviene quedarse es esta: **mockear no consiste en falsear todo, sino en sustituir solo aquellas dependencias que impiden probar con claridad la unidad que te interesa**.

## Fuentes y referencias

- [Qué es un stub](https://es.wikipedia.org/wiki/Stub)
- [Mock object](https://en.wikipedia.org/wiki/Mock_object)
- [Diferencias entre stub, spy y mock](https://gabimoreno.soy/que-diferencias-hay-entre-un-stub-un-spy-y-un-mock)
- [Documentación oficial de MockK](https://mockk.io/)
- [MockK: A Mocking Library for Kotlin](https://www.baeldung.com/kotlin/mockk)
- [MockK Guidebook](https://notwoods.github.io/mockk-guidebook/)
