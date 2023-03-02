---
title: "UD 3 - 3.4 Mockk"
description: Mockk
summary: Mockk
authors:
  - Eduardo Fdez
date: 2023-01-30
icon: material/security
permalink: /edes/unidad3/3.4
categories:
  - EDES
tags:
  - EDES
  - Software
  - Mock
---

## MockK: una biblioteca burlona para Kotlin

### 1. Información general

Vamos a revisar algunas de las funciones básicas de la biblioteca  [MockK](https://mockk.io/).

### 2. MockK

En Kotlin, todas las clases y métodos son finales.  Si bien esto nos ayuda a escribir código inmutable, también causa algunos problemas durante las pruebas.

La mayoría de las bibliotecas que simulan objetos (mock) que se usan en JVM tienen problemas con las clases finales usadas para mocking or stubbing. Por supuesto, podemos agregar la palabra clave `open` a las clases y métodos que queremos "mockear" (simular). Pero cambiar el código solo para poder mockearla no parece el mejor enfoque.

La biblioteca MockK ofrece compatibilidad con las características y construcciones del lenguaje Kotlin.  MockK construye proxies para las clases mockeadas. Esto provoca cierta degradación del rendimiento, pero los beneficios generales que nos brinda MockK valen la pena.

### 3. Instalación

La configuración del proyecto consiste en añadir las dependencias de [mockk](https://search.maven.org/search?q=g:io.mockk%20a:mockk) al fichero `build.gradle.kts`


```kotlin
var mockKVersion = "1.13.4"

dependencies {
    testImplementation("io.mockk:mockk:$mockKVersion")
}
```

Ten en cuenta que estamos estableciendo la version `1.13.4`, en el [repositorio Maven ](https://mvnrepository.com/artifact/io.mockk/mockk) puedes consultar cuál es la última versión.


### 4. Ejemplo básico

Vamos a crear un servicio que podremos usar como ejemplo para "mockear" (simular) su funcionamiento:

```Kotlin
class TestableService {
    fun getDataFromDb(testParameter: String): String {
        // query database and return matching value
    }

    fun doSomethingElse(testParameter: String): String {
        return "I don't want to!"
    }
}
```

Aquí hay un test de ejemplo que mockea `TestableService`:

```kotlin
@Test
fun givenServiceMock_whenCallingMockedMethod_thenCorrectlyVerified() {
    // given
    val service = mockk<TestableService>()
    every { service.getDataFromDb("Expected Param") } returns "Expected Output"
 
    // when
    val result = service.getDataFromDb("Expected Param")
 
    // then
    verify { service.getDataFromDb("Expected Param") }
    assertEquals("Expected Output", result)
}
```
Revisando las partes mas importantes del código anterior:
- Para definir el objeto mockeado, hemos usado el método `mockk<…>()`.
- En el siguiente paso, definimos el comportamiento de nuestro objeto mockeado. Para este propósito, hemos creado un bloque `every` que describe qué respuesta debe devolverse `returns "Expected"` para qué llamada, es decir, la llamada a un método `service.getDataFromDb` y con un argumento concreto `("Expected Param")`
- Finalmente, usamos el bloque de `verify` para verificar si el simulacro se invocó como esperábamos, indicando que al menos se ha tenido que invocar una vez el método `service.getDataFromDb("Expected Param")`.

### 5. Ejemplo de uso de las anotaciones

Es posible usar las anotaciones MockK `@MockK` para crear todo tipo de objetos mocks. Vamos a crear un servicio que requiera de dos instancias de nuestro `TestableService`:

```kotlin
class InjectTestService {
    lateinit var service1: TestableService
    lateinit var service2: TestableService

    fun invokeService1(): String {
        return service1.getDataFromDb("Test Param")
    }
}
```

El servicio que hemos creado, `InjectTestService`, contiene dos variables de instancia del mismo tipo. Esto no será un problema para MockK, ya que MockK intenta hacer coincidir las propiedades por nombre y luego por clase o superclase. Además, tampoco **tiene problema con la inyección de objetos en campos privados**.

Vamos a mockear el servicio `InjectTestService` en el siguiente test haciendo uso de las anotaciones:

```kotlin
class AnnotationMockKUnitTest {

    @MockK
    lateinit var service1: TestableService

    @MockK
    lateinit var service2: TestableService

    @InjectMockKs
    var objectUnderTest = InjectTestService()

    @BeforeEach
    fun setUp() = MockKAnnotations.init(this)

    // Tests here
    ...
}
```

Revisemos lo más importante del código anterior:
- Con la anotación `@MoockK`, hemos definido (marcado para crear) los objetos mocks `service1` y `service2` que vamos a inyectar en el servicio `objectUnderTest`.
- Hemos usado la anotación `@InjectMockKs` para especificar el objeto `objectUnderTest` donde se deben inyectar los objetos mocks definidos.  
- Por defecto, los objetos mocks se inyectan en variables que aún no están asignadas. Aunque, podemos usar `@OverrideMockKs` para anular campos que ya tienen un valor.
- Por último, MockK requiere que se llame a `MockKAnnotations.init(…)` en el objeto que declara variables con anotaciones. Para Junit5, se puede reemplazar con `@ExtendWith(MockKExtension::class)`.

### 6. Spy

`Spy` permite en un objeto mezclar el comportamiento de objetos reales y mockeados, es decir, mockear solo una parte particular de alguna clase. Por ejemplo, se puede usar para simular un método específico del servicio  `TestableService`, el resto del servicio funcionará como se definió. Si no se define un comportamiento nuevo, el objeto entero funcionara como se definió en su clases, pero podremos usar sobre él verificaciones haciendo uso de `verify`. Veamos el ejemplo:

```kotlin
@Test
fun givenServiceSpy_whenMockingOnlyOneMethod_thenOtherMethodsShouldBehaveAsOriginalObject() {
    // given
    val service = spyk<TestableService>()
    every { service.getDataFromDb(any()) } returns "Mocked Output"
 
    // when checking mocked method
    val firstResult = service.getDataFromDb("Any Param")
 
    // then
    assertEquals("Mocked Output", firstResult)
 
    // when checking not mocked method
    val secondResult = service.doSomethingElse("Any Param")
 
    // then
    assertEquals("I don't want to!", secondResult)
}
```

Revisemos lo más importante del código anterior:
- Hemos usado el método `spyk` para crear un objeto spyk (espía) de la clase `TestableService`.  
- También hemos usado `every` para definir el comportamiento del método que nos interesa, en concreto `service.getDataFromDb(any())`, como vimos en ejemplos anteriores.

También podemos haber usado la anotación `@SpyK` para lograr lo mismo que hicimos con la anotación `@MockK`. Veamos un ejemplo:

```Kotlin
class SpyKUnitTest {

    @SpyK
    lateinit var service: TestableService

    // Tests here
}
```

### 7. Mockeado relajado

Un objeto mock típico lanzará la excepción `MockKException` si intentamos llamar a un método donde no se ha especificado el valor de retorno, es decir, en donde no hayamos definido un comportamiento simulado.
 
Si no queremos describir el comportamiento de cada método, podemos usar un proceso de mockeado relajado. Este tipo de mockeado proporciona valores predeterminados para cada función. Por ejemplo, el tipo de retorno `String` devolverá un `String` vacío. He aquí un breve ejemplo:

```Kotlin
@Test
fun givenRelaxedMock_whenCallingNotMockedMethod_thenReturnDefaultValue() {
    // given
    val service = mockk<TestableService>(relaxed = true)
 
    // when
    val result = service.getDataFromDb("Any Param")
 
    // then
    assertEquals("", result)
}
```

En el ejemplo, hemos usado el método `mockk` con el argumento `relaxed = True` para crear un objeto mockeado relajado. También podríamos haber usado la anotación `@RelaxedMockK`:

```kotlin
class RelaxedMockKUnitTest {

    @RelaxedMockK
    lateinit var service: TestableService

    // Tests here
}
```

### 8. Mockeado de objetos

Kotlin proporciona una manera fácil de declarar un singleton usando la palabra clave `object`:

```Kotlin
object TestableService {
    fun getDataFromDb(testParameter: String): String {
        // query database and return matching value
    }
}
```

La mayoría de las bibliotecas para crear objetos mocks tienen un problema con el mockeado las instancias de objetos singleton de Kotlin. Para resolver esto, MockK proporciona el método `mockkObject`.  Un ejemplo de uso:

```Kotlin
@Test
fun givenObject_whenMockingIt_thenMockedMethodShouldReturnProperValue(){
    // given
    mockkObject(TestableService)
 
    // when calling not mocked method
    val firstResult = service.getDataFromDb("Any Param")
 
    // then return real response
    assertEquals(/* DB result */, firstResult)

    // when calling mocked method
    every { service.getDataFromDb(any()) } returns "Mocked Output"
    val secondResult = service.getDataFromDb("Any Param")
 
    // then return mocked response
    assertEquals("Mocked Output", secondResult)
}
```

### 9. Mockeado jerárquico

Otra característica útil de MockK es la capacidad de mockear objetos jerárquicos. Parar entenderlo, primero, creemos una estructura de objeto jerárquica:

```Kotlin
class Foo {
    lateinit var name: String
    lateinit var bar: Bar
}

class Bar {
    lateinit var nickname: String
}
```

La clase `Foo` contiene un campo de tipo `Bar`. Ahora, podemos mockear la estructura en un solo paso. Vamos a mockear los campos `name` y `bar`:

```Kotlin
@Test
fun givenHierarchicalClass_whenMockingIt_thenReturnProperValue() {
    // given
    val foo = mockk<Foo> {
        every { name } returns "Karol"
        every { bar } returns mockk {
            every { nickname } returns "Tomato"
        }
    }
 
    // when
    val name = foo.name 
    val nickname = foo.bar.nickname
 
    // then
    assertEquals("Karol", name)
    assertEquals("Tomato", nickname)
}
```

### 10. Captura de argumentos

Si necesitamos capturar los valores de los parámetros pasados a un método, podemos usar `CapturingSlot` o `MutableList`. Es útil cuando queremos tener alguna lógica personalizada en un bloque `answers` o simplemente necesitamos verificar el valor de los parámetros pasados. Aquí hay un ejemplo de `CapturingSlot`:

```Kotlin
@Test
fun givenMock_whenCapturingParamValue_thenProperValueShouldBeCaptured() {
    // given
    val service = mockk<TestableService>()
    val slot = slot<String>()
    every { service.getDataFromDb(capture(slot)) } returns "Expected Output"
 
    // when
    service.getDataFromDb("Expected Param")
 
    // then
    assertEquals("Expected Param", slot.captured)
}Copiar
```

`MutableList` se puede usar para capturar y almacenar todos los valores tomados por el parámetro en las distintas invocaciones del método:

```Kotlin
@Test
fun givenMock_whenCapturingParamsValues_thenProperValuesShouldBeCaptured() {
    // given
    val service = mockk<TestableService>()
    val list = mutableListOf<String>()
    every { service.getDataFromDb(capture(list)) } returns "Expected Output"
 
    // when
    service.getDataFromDb("Expected Param 1")
    service.getDataFromDb("Expected Param 2")
 
    // then
    assertEquals(2, list.size)
    assertEquals("Expected Param 1", list[0])
    assertEquals("Expected Param 2", list[1])
}
```

### 11. Funciones Stubbing que retornan Unit
Un stub es, en el contexto del testeo del software, un trozo de código usado como sustituto de alguna otra funcionalidad. Un stub puede simular el comportamiento de código existente (tal como un procedimiento en una máquina remota) o ser el sustituto temporal para un código aún no desarrollado. Los stubs son, por tanto, muy útiles para porting, computación distribuida así como en el desarrollo y pruebas de software en general.

En Kotlin, si el tipo de retorno de una función es `Unit`, significa que la función no devuelve nada. Es bastante similar al método `void` de Java.

Para ejemplificarlo, agreguemos una función que retorna `Unit` a la clase `TestableService`:

```kotlin
fun addHelloWorld(strList: MutableList<String>) {
    println("addHelloWorld() is called")
    strList += "Hello World!"
}
```

Como muestra el código anterior, cuando se llama a la función `addHelloWorld()`, imprime una línea en la consola.  Luego, el `String` `"Hello World"` se agrega al objeto `MutableList<String>` recibido por parámetro.

En esta sección, vamos a ver cómo hacer un [stub](https://es.wikipedia.org/wiki/Stub) de una función que devuelve `Unit`. Por lo general, dependiendo de diferentes circunstancias, queremos controlar un stub de una función que retorna `Unit` de dos maneras:

* hacer que la llamada a la función no haga nada, o en otras palabras, omitir la ejecución de la función
* llamando a la función real

A continuación, usaremos la función `addHelloWorld()` como ejemplo y veremos cómo lograrlo usando MockK.

#### 11.1. Hacer que la función no haga nada

Hay varias formas de omitir la ejecución de una función que retorna `Unit` usando MockK:

```kotlin
every { addHelloWorld(any()) } returns Unit
every { addHelloWorld(any()) } answers { Unit }
every { addHelloWorld(any()) } just runs
```

Algunas de ellas no son nuevas para nosotros
- `returns …` 
- `answers {…}`, 
- y el último, `every {... } just runs` es fácil de entender.

Entonces, primero probemos si se puede omitir la ejecución de la función original y luego entendamos cómo funciona `just runs`:

```kotlin
@Test
fun givenServiceMock_whenCallingMethodReturnsUnit_thenCorrectlyVerified() {
    // given
    val service = mockk<TestableService>()
    val myList = mutableListOf<String>()
                                                                         
    // when
    every { service.addHelloWorld(any()) } just runs
    service.addHelloWorld(myList)
                                                                         
    // then
    assertTrue(myList.isEmpty())
}
```

Como muestra el código anterior, 
- Agregamos la función `addHelloWorld()` usando `just runs`. 
- Luego, llamamos a la función y le pasamos una `MutableList` vacía.
- Por último, si omitimos la ejecución de la función con éxito, `“Hello World!”` no debe aparecer en la lista, pasada como parámetro, después de la invocación. 
El test es ok tras de ejecutarlo.

Ahora entendamos cómo `just runs` omite la llamada de la función real. Primero, echemos un vistazo a la implementación de la función `just()`:

```kotlin
infix fun MockKStubScope<Unit, Unit>.just(runs: Runs) = answers(ConstantAnswer(Unit))
```

Como podemos ver, `just` es una función `infix` (infija). Por lo tanto, podemos escribir `just(runs)` como una forma mas fácil de leer:`just runs`. Además, `Runs` es un objeto dummy, y `runs` es simplemente un `typealias` de `Runs`:

```kotlin
object Runs
typealias runs = Runs
```

Por último, si creamos un stub de una función que retorna `Unit` como  `just runs`, se llama a la función `answers()`  y retorna una constante: `Unit`.

#### 11.2. Llamar a la función original

Ahora, veamos cómo crear un stub de una función que retorna `Unit` para hacer que llame a la función real.  Para llamar a la función original, podemos usar este enfoque:  `every { … } answers { callOriginal() }`

A continuación, veamos cómo se usa en una prueba real:

```kotlin
@Test
fun givenServiceMock_whenCallingOriginalMethod_thenCorrectlyVerified() {
    // given
    val service = mockk<TestableService>()
    val myList = mutableListOf<String>()
                                                                      
    // when
    every { service.addHelloWorld(any()) } answers { callOriginal() }
    service.addHelloWorld(myList)
                                                                      
    // then
    assertEquals(1, myList.size)
    assertEquals("Hello World!", myList.first())
}
```

El test es ok tras de ejecutarlo. Entonces, `“Hello World!”`  se agrega a `myList` después de llamar a la función.  Sin embargo, podemos preguntarnos: si creamos un stub de una función y le pedimos que llame a la implementación original, ¿por qué nos molestamos en crear el stub?

A continuación, veamos un ejemplo de cuándo es útil.

#### 11.3. ¿Cuándo necesitamos `callOriginal()`?

Digamos que en nuestra prueba, queremos llamar a la función `addHelloWorld()` con diferentes parámetros. Si la lista que se le pasa a la función contiene la cadena `"Kai"`, queremos llamar a la función real.  De lo contrario, nos gustaría omitir la llamada a la función:

```kotlin
@Test
fun givenServiceMock_whenStubbingTwoScenarios_thenCorrectlyVerified() {
    // given
    val service = mockk<TestableService>()
    val kaiList = mutableListOf("Kai")
    val emptyList = mutableListOf<String>()
                                                                                   
    // when
    every { service.addHelloWorld(any()) } just runs
    every { service.addHelloWorld(match { "Kai" in it }) } answers { callOriginal() }
                                                                                   
    service.addHelloWorld(kaiList)
    service.addHelloWorld(emptyList)
                                                                                   
    // then
    assertEquals(listOf("Kai", "Hello World!"), kaiList)
    assertTrue(emptyList.isEmpty())
}
```

Como podemos ver en el código anterior, agregamos la función `addHelloWorld()` dos veces, según nuestros requisitos.  Por lo tanto, `callOriginal()` nos permite decidir el comportamiento de los stubings de forma flexible.


### 12. Conclusión

Se han visto algunas de las características más importantes de MockK. MockK es una poderosa biblioteca para el lenguaje Kotlin y proporciona muchas características útiles. Para más información sobre MockK, podemos consultar la  [documentación en la web de MockK](https://mockk.io/).


## Recursos
* [¿Que es un Stub?](https://es.wikipedia.org/wiki/Stub)
* [Mock Object](https://en.wikipedia.org/wiki/Mock_object)
* [Stub, Spy, Mock](https://gabimoreno.soy/que-diferencias-hay-entre-un-stub-un-spy-y-un-mock)
* [¿Qué es TDD?](https://www.digite.com/es/agile/desarrollo-dirigido-por-pruebas-tdd/)
* [¿Cómo elaborar casos de prueba?](https://surprograma.github.io/libro-disenio-oop/docs/pruebas-automatizadas/elaborar-casos-prueba/)
* [Test unitario avanzado](http://wiki.uqbar.org/wiki/articles/testeo-unitario-avanzado.html)
* [Diseño de Software](https://surprograma.github.io/libro-disenio-oop/docs/intro/)
* 
## Fuente
* [MockK: A Mocking Library for Kotlin](https://www.baeldung.com/kotlin/mockk)
* [MockK Guidebook](https://notwoods.github.io/mockk-guidebook/)
