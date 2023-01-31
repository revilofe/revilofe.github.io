---
title: "UD 3 - 3.4 Mockk"
description: Mockk
summary: Mockk
authors:
- Eduardo Fdez
date: 2022-09-18
icon: material/security
permalink: /edes/unidad3/3.4
categories:
  - EDES
tags:
  - EDES
  - Software
  - Hardware
---
## MockK: una biblioteca burlona para Kotlin

### 1. Información general

Vamos a revisar algunas de las funciones básicas de la biblioteca  [MockK](https://mockk.io/).

### 2. MockK

En Kotlin, todas las clases y métodos son finales.  Si bien esto nos ayuda a escribir código inmutable, también causa algunos problemas durante las pruebas.

La mayoría de las bibliotecas que simulan objetos (mock) que se usan en JVM tienen problemas con las clases finales usadas para mocking or stubbing. Por supuesto, podemos agregar la palabra clave `open` a las clases y métodos que queremos "mockear" (simular). Pero cambiar el código solo para poder mockearla no parece el mejor enfoque.

La biblioteca MockK ofrece compatibilidad con las características y construcciones del lenguaje Kotlin.  MockK construye proxies para clases mockeadas. Esto provoca cierta degradación del rendimiento, pero los beneficios generales que nos brinda MockK valen la pena.

### 3. Instalación

La configuración del proyecto consiste en añadir las dependencias de [mockk](https://search.maven.org/search?q=g:io.mockk%20a:mockk) dentro del fichero `build.gradle.kts`


```kotlin
var mockKVersion = "1.13.4"

dependencies {
    testImplementation("io.mockk:mockk:$mockKVersion")
}
```

### 4. Ejemplo básico

Vamos a crear un servicio que nos gustaría simular:

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

Para definir el objeto mockeado, hemos usado el método `mockk<…>()`.

En el siguiente paso, definimos el comportamiento de nuestro objeto mockeado.  Para este propósito, hemos creado un bloque `every` que describe qué respuesta debe devolverse para qué llamada, es decir, la llamada a un método y con un argumento concreto.

Finalmente, usamos el bloque de `verify` para verificar si el simulacro se invocó como esperábamos.

## **5. Ejemplo de anotación**

Es posible usar anotaciones MockK para crear todo tipo de simulacros.  Vamos a crear un servicio que requiera dos instancias de nuestro  *TestableService*  :

```java
class InjectTestService {
    lateinit var service1: TestableService
    lateinit var service2: TestableService

    fun invokeService1(): String {
        return service1.getDataFromDb("Test Param")
    }
}Copiar
```

*InjectTestService*  contiene dos campos con el mismo tipo.  No será un problema para MockK.  MockK intenta hacer coincidir las propiedades por nombre, luego por clase o superclase.  Tampoco  **tiene problema con la inyección de objetos en campos privados**  .

Vamos a burlarnos de  *InjectTestService*  en una prueba usando anotaciones:

```java
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
}Copiar
```

En el ejemplo anterior, hemos usado la  anotación  *@InjectMockKs  **.  * Esto especifica un objeto donde se deben inyectar los simulacros definidos.  Por defecto, inyecta variables que aún no están asignadas.  Podemos usar  *@OverrideMockKs*  para anular campos que ya tienen un valor.

**MockK requiere que se llame a  *MockKAnnotations.init(…)*  en un objeto que declara una variable con anotaciones.  ** Para  [Junit5](https://www.baeldung.com/junit-5)  , se puede reemplazar con  *@ExtendWith(MockKExtension::class)*  .

## **6. Espía**

**Spy permite burlarse solo de una parte particular de alguna clase.  ** Por ejemplo, se puede usar para simular un método específico en  *TestableService:*

```java
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
}Copiar
```

En el ejemplo, hemos usado el método  *spyk*  para crear un objeto espía.  También podríamos haber usado la anotación  *@SpyK*  para lograr lo mismo:

```java
class SpyKUnitTest {

    @SpyK
    lateinit var service: TestableService

    // Tests here
}Copiar
```

## **7. Simulacro relajado**

Un objeto simulado típico lanzará  *MockKException*  si intentamos llamar a un método donde no se ha especificado el valor de retorno.

**Si no queremos describir el comportamiento de cada método, podemos usar un simulacro relajado.  ** Este tipo de simulacro proporciona valores predeterminados para cada función.  Por ejemplo, el tipo de retorno  *String*  devolverá un  *String*  vacío .  He aquí un breve ejemplo:

```java
@Test
fun givenRelaxedMock_whenCallingNotMockedMethod_thenReturnDefaultValue() {
    // given
    val service = mockk<TestableService>(relaxed = true)
 
    // when
    val result = service.getDataFromDb("Any Param")
 
    // then
    assertEquals("", result)
}Copiar
```

En el ejemplo, hemos usado el método  *mockk*  con el atributo  *relajado*  para crear un objeto simulado relajado.  También podríamos haber usado la anotación  *@RelaxedMockK*  :

```java
class RelaxedMockKUnitTest {

    @RelaxedMockK
    lateinit var service: TestableService

    // Tests here
}Copiar
```

## **8. Simulacro de objeto**

Kotlin proporciona una manera fácil de declarar un singleton usando la palabra clave  *object*  :

```java
object TestableService {
    fun getDataFromDb(testParameter: String): String {
        // query database and return matching value
    }
}Copiar
```

Sin embargo, la mayoría de las bibliotecas de simulación tienen un problema con la simulación de instancias únicas de Kotlin.  Debido a esto, MockK proporciona el método  *mockkObject*  .  Vamos a ver:

```java
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
}Copiar
```

## **9. Burla jerárquica**

Otra característica útil de MockK es la capacidad de simular objetos jerárquicos.  Primero, creemos una estructura de objeto jerárquica:

```java
class Foo {
    lateinit var name: String
    lateinit var bar: Bar
}

class Bar {
    lateinit var nickname: String
}Copiar
```

La clase  *Foo*  contiene un campo de tipo  *Bar.  * Ahora, podemos simular la estructura en un solo paso.  Vamos a burlarnos de los  campos de  *nombre*  y  *apodo :*

```java
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
}Copiar
```

## **10. Captura de parámetros**

Si necesitamos capturar los parámetros pasados a un método, podemos usar  *CapturingSlot*  o  *MutableList.  * Es útil cuando queremos tener alguna lógica personalizada en un bloque de  *respuesta*  o simplemente necesitamos verificar el valor de los argumentos pasados.  Aquí hay un ejemplo de  *CapturingSlot:*

```java
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

*MutableList*  se puede usar para capturar y almacenar valores de argumentos específicos para todas las invocaciones de métodos:

```java
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
}Copiar
```

## 11. Unidad  de retorno de funciones de creación de apéndices

**En Kotlin, si el tipo de devolución de una función es  [*Unit*](https://www.baeldung.com/kotlin/void-type#unit_in_kotlin)  , significa que la función no devuelve nada.  ** Es bastante similar al  método  *void de Java.*

Agreguemos una  función  *Unit a la clase  **TestableService*  :

```kotlin
fun addHelloWorld(strList: MutableList<String>) {
    println("addHelloWorld() is called")
    strList += "Hello World!"
}Copiar
```

Como muestra el código anterior, cuando se llama a la función  *addHelloWorld()*  , imprime una línea en la consola.  Luego, la  *cadena "Hello World"*  se agrega al objeto  *MutableList<String>*  dado .

En esta sección, veamos cómo convertir una función que devuelve  *Unit*  .  Por lo general, dependiendo de diferentes circunstancias, queremos controlar un stub de función de  *unidad*  de dos maneras:

* hacer que la llamada a la función no haga nada, o en otras palabras, omitir la ejecución de la función
* llamando a la función real

A continuación, tomaremos la función  *addHelloWorld()*  como ejemplo y abordaremos cómo lograrlos usando MockK.

### 11.1.  Hacer que la función no haga nada

Hay varias formas de omitir una función de  *Unidad*  usando MockK:

```kotlin
every { addHelloWorld(any()) } returns Unit
every { addHelloWorld(any()) } answers { Unit }
every { addHelloWorld(any()) } just runsCopiar
```

Algunas de ellas no son nuevas para nosotros, como las  *devoluciones…*  y las  *respuestas {…}*  .  Sin embargo, el último, "  *cada {... } simplemente se ejecuta*  " es fácil de entender.

Entonces, primero probemos si puede omitir la ejecución de la función original y luego entendamos cómo funciona "  *simplemente se ejecuta*  ":

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
}Copiar
```

Como muestra la prueba anterior, agregamos la función  *addHelloWorld()*  usando "  *simplemente se ejecuta*  ".  Y luego, llamamos a la función y le pasamos una  *MutableList*  vacía .

Si omitimos la ejecución de la función con éxito,  *"¡Hola mundo!"  * no debe agregarse a la lista dada después de la invocación.

La prueba pasa si le damos una ejecución.

Ahora entendamos cómo "  *simplemente  * *se ejecuta*  " omite la llamada de función real.  Primero, echemos un vistazo a la implementación de la función  *just()*  :

```kotlin
infix fun MockKStubScope<Unit, Unit>.just(runs: Runs) = answers(ConstantAnswer(Unit))
Copiar
```

Como podemos ver,  **es una función  [*infija*](https://www.baeldung.com/kotlin/infix-functions)  .  Por lo tanto, podemos escribir    *just(runs)*  en una forma mejor legible:  *just runs*  .  ** Además,    *Runs es un  *[objeto](https://www.baeldung.com/kotlin/objects#objects-in-kotlin)  ficticio    , y    *Runs*  es simplemente un  [*alias tipográfico*](https://www.baeldung.com/kotlin/type-aliases)  de  *Runs*  :

```kotlin
object Runs
typealias runs = Runs
Copiar
```

Además, si agregamos una función  *Unit*  como  *ejecuta*  , llama a la función  *answers()*  y  *devuelve*  una respuesta constante:  *Unit.*

### 11.2.  Llamar a la función original

Ahora, veamos cómo convertir una función Unit para hacer que llame a la función real.  **Para llamar a la función original, podemos usar este enfoque:  *cada {... } responde { callOriginal() }*  .**

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
}Copiar
```

La prueba pasa cuando la ejecutamos.  Entonces,  *"¡Hola mundo!"  * se agrega a    *myList*  después de llamar a la función.  Sin embargo, podemos preguntar, si aplicamos stub a una función y le pedimos que llame a la implementación original, ¿por qué nos molestamos en stub?

A continuación, veamos un ejemplo de cuándo es útil.

### 11.3.  ¿Cuándo necesitamos  *callOriginal()*  ?

Digamos que en nuestra prueba, queremos llamar a la función  *addHelloWorld()*  con diferentes parámetros.  Si la lista que pasa a la función contiene la cadena  *"Kai"*  , queremos llamar a la función real.  De lo contrario, nos gustaría omitir la llamada a la función:

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
}Copiar
```

Como podemos ver, agregamos la función  *addHelloWorld()*  dos veces, según nuestros requisitos.  Por lo tanto,  *callOriginal()*  nos permite decidir el comportamiento de los stubings de forma flexible.

<iframe id="google_ads_iframe_/15184186,7114245/baeldung_incontent_4_0" name="google_ads_iframe_/15184186,7114245/baeldung_incontent_4_0" title="contenido de anuncios de terceros" width="1086" height="280" scrolling="no" marginwidth="0" marginheight="0" frameborder="0" role="region" aria-label="Anuncio" tabindex="0" data-google-container-id="9" data-load-complete="true"></iframe>

[![estrella libre](https://a.pub.network/core/imgs/fslogo-green.svg)](https://freestar.com/?utm_campaign=branding&utm_medium=banner&utm_source=baeldung.com&utm_content=baeldung_incontent_4)

## **12. Conclusión**

En este artículo, hemos discutido las características más importantes de MockK.  MockK es una poderosa biblioteca para el lenguaje Kotlin y proporciona muchas características útiles.  Para más información sobre MockK, podemos consultar la  [documentación en la web de MockK](https://mockk.io/)  .



12. Conclusión

Se han visto varias funcionalidades básicas proporcionadas por el marco Kotest. y los ejemplos de código se pueden encontrar [en GitHub](https://github.com/Baeldung/kotlin-tutorials/tree/master/kotlin-testing) .

## Recursos

* [¿Qué es TDD?](https://www.digite.com/es/agile/desarrollo-dirigido-por-pruebas-tdd/)
* [¿Cómo elaborar casos de prueba?](https://surprograma.github.io/libro-disenio-oop/docs/pruebas-automatizadas/elaborar-casos-prueba/)
* [Test unitario avanzado](http://wiki.uqbar.org/wiki/articles/testeo-unitario-avanzado.html)
* [Diseño de Software](https://surprograma.github.io/libro-disenio-oop/docs/intro/)

## Fuente

* [TDD Veloz](https://www.youtube.com/watch?v=8MGtLPFtbQ8)
