---
title: "UD 7 - 7.5 Interfaces de usuario: Compose"
description: Interfaces de usuario: Compose
summary: Interfaces de usuario: Compose
authors:
    - Eduardo Fdez
date: 2023-03-13
icon: material/software
permalink: /prog/unidad7/7.5
categories:
    - PROG
tags:
    - Software
    - gui
    - compose
---
## Interface gráfica de usuario vs CLI

La Interfaz gráfica de usuario o GUI (Graphic User Interface) es el entorno visual de imágenes y objetos mediante el cual una máquina y un usuario interactúan. A mediados de los setentas las GUI comenzaron a sustituir a las interfaces de línea de comando (CLI), y esto permitió que la interacción con las computadoras fuera más sencilla e intuitiva.


### ¿Para qué sirven las Interfaces gráficas de usuario?

Su función principal es simplificar la comunicación entre una máquina o un sistema operativo y un usuario. Antes de que se desarrollaran y popularizaron las GUI, solo las personas con conocimientos profundos de informática podían usar un computador, pero las interfaces gráficas sustituyeron la complejidad de los comandos por acciones predeterminadas simbolizadas por elementos visuales muy sencillos de comprender.
A mediados de los ochentas, Mac se convirtió en el referente de las interfaces gráficas amigables desarrollando equipos con funciones muy complejas pero “tan fáciles de usar como una tostadora”, y por esas mismas fechas Microsoft lanzó  Windows 1.0, un sistema operativo que se caracterizaba por tener una interfaz gráfica similar, lo que le valió una demanda millonaria de parte de Apple.
Una buena GUI no solo es importante para los programas, sistemas operativos y aplicaciones. Se estima que el 68% de los visitantes que abandonan un sitio web lo hacen debido a que la experiencia de usuario, incluyendo la Interfaz, no está optimizada para sus necesidades y expectativas.

### ¿Cuáles son los elementos de la Interfaz gráfica de usuario?

Las interfaces gráficas de usuario integraron en sus inicios una novedad que hoy en día es de uso corriente: el mouse o ratón, que fungía como puntero para señalar y seleccionar los diferentes elementos de la GUI, que tradicionalmente se categorizaron como ventanas, iconos o carpetas.
Hoy en día los elementos visuales (widgets) de una interfaz son muy similares en esencia, sólo que cada día los diseñadores tratan de hacerlos más amigables e intuitivos. Además, los dispositivos móviles no requieren de ratón o puntero pues cuentan con pantallas táctiles.
![](assets/PRO-GUI.png)

### ¿Cómo crear una buena Interfaz gráfica de usuario?

Una buena GUI se caracteriza por:

* Ser sencilla de comprender y usar
* La curva de aprendizaje es acelerada y es fácil recordar su funcionamiento
* Los elementos principales son muy identificables
* Facilitar y predecir las acciones más comunes del usuario
* La información está adecuadamente ordenada mediante menús, iconos, barras, etc.
* Las operaciones son rápidas, intuitivas y reversibles
* La interfaz expresa claramente el estado del sistema o las operaciones, y brinda elementos de ayuda.
* La navegabilidad y la usabilidad son óptimas.

### Características generales de la GUI:

* Facilidad
* Diseño ergonómico mediante el uso de menús, barras de acciones o íconos
* Operaciones rápidas, reversibles; que sea de cambios inmediatos
* Contiene herramientas de ayuda que orientan al usuario.

Para la realización de un buen desarrollo GUI, se debe tener en cuenta:

* Consistencia:  Todos los elementos de la GUI se deben regir por las mismas normas
* Palabras y legibilidad:  Uso de colores y fuentes adecuadas, uso correcto de mayúsculas y minúsculas
* Color: Tener en cuenta el significado de los colores, que éstos permitan la legibilidad y que den una buena apariencia en la pantalla
* Accesibilidad:  Debe ser accesible en lo posible a todos teniendo en cuenta discapacidades
* Necesidades de los usuarios:  Los usuarios deben encontrar lo que buscan
* Contenidos:  Deben ser fiables
* Funcionalidad:  Debe reducir los pasos para la realización de una acción
* Sistema de búsqueda: Debe contar con diferentes maneras de realizar la búsqueda

### ¿Quiénes son responsables de la Interfaz gráfica de usuario?

Detrás de cualquier Interfaz gráfica de usuario existe un programa, sistema operativo o aplicación. Por eso, la GUI suele ser un trabajo en conjunto entre desarrolladores y diseñadores que buscan la mejor manera de que el usuario pueda interactuar con el programa mediante elementos visuales fáciles de comprender.

### Entornos gráficos 

#### Aplicaciones multiplataforma
Las aplicaciones multiplataforma son aquellas destinadas a dispositivos móviles,  aplicaciones de escritorio u otro tipos de sistemas embebidos.

Para programar los entornos gráficos de estas aplicaciones es necesario un Software Development Kit o SDK, que es un conjunto de herramientas que, entre otras cosas, hacen posible la creación de los elementos necesarios para una interfaz. Estos SDK pueden ser:   
* Oficiales: los proporcionan los fabricantes, como por ejemplo iOS SDK de Apple.   
* Alternativos: desarrollados por terceros, como GTK+ o Qt.    
* Multiplataforma: también desarrollado por terceros, algunos disponen de bindings para que se usen en varios sistemas como GTK+ o Qt o nativos al lenguajes como Swing de Java.   

En los siguientes apartados destacaremos algunos de los lenguajes y librerías que se utilizan actualmente en estas plataformas.

##### Aplicaciones móviles
Android tiene como lenguaje oficial para crear sus aplicaciones Java (JVM), lo que hace que este sea uno de los lenguajes más utilizados para el desarrollo en este sistema. Aunque Kotlin, creado por JetBrains es 100% compatible con la JVM y todas las librerías, ha sido nombrado por google lenguaje cooficial aportando además simplicidad en el código.

Por otro lado, las aplicaciones desarrolladas para iOS pueden utilizar Objetive-C o Swift, una alternativa al primero creado por Apple, con mejor rendimiento y totalmente compatible con todos los dispositivos de Apple.

##### Aplicaciones de escritorio y sistemas embebidos
Este tipo de aplicaciones se suelen desarrollar con Java o C++ generalmente.

Java junto con la librería gráfica Swing que ya viene incluida en su JDK, forman un combo con el que podemos desarrollar este tipo de aplicaciones.

C++ junto con Qt también son utilizados de forma nativa para crear interfaces gráficas en varias plataformas, además destacar que es utilizado por el entorno de escritorio GNU/Linux: KDE.

Python es un lenguaje emergente que se está imponiendo en muchos ámbitos de la programación, entre ellos las aplicaciones de escritorio y sistemas embebidos. Este lenguaje dispone de una comunidad muy grande y activa que desarrolla binding para poder utilizar las librerías gráficas como GTK, Qt y Swing.

#### Videojuegos   
Los videojuegos son un tipo de aplicación muy demandada en la actualidad, con suficiente entidad como para distinguirlos de los tipos de aplicaciones anteriores.

Uno de los lenguajes más utilizados en este sector es C# junto con la herramienta Unity, que proporciona un editor, un motor para la física 2D y la física 3D, renderizado, animación, audio, etc. Esta potente herramienta no solo se utiliza para el desarrollo de videojuegos, sino para crear experiencias en realidad virtual y cortos animados. Unity además permite la exportación del trabajo a multitud de plataformas, como móviles, videoconsolas, ordenadores, etc.

Otro de los lenguajes más utilizados para este propósito es Java junto con frameworks como LibGDX o JMonkeyEngine y Python con el framework Pygame.

#### Aplicaciones web   
Aunque en el mundo web los primeros navegadores eran en modo texto y aún siguen existiendo (como Lynx), la web en sí es gráfica. Se suele emplear el término front-end para la parte del cliente, es decir, el entorno gráfico de una aplicación web y back-end para la parte del servidor con la que se gestionan todos los datos. Centrándonos en el front-end, podremos distinguir tres pilares básicos que pasamos a definir a continuación:   

##### Contenido: HTML   
HTML (Hypertext Markup Languaje) es un lenguaje de marcado o etiquetado, el cual sirve para definir estructuras y contenido en la web. La diferencia con un lenguaje de programación es que no dispone de las variables ni estructuras que afectan al comportamiento como condicionales, bucles etc.

Al igual que otros lenguajes, HTML también ha evolucionado con el paso del tiempo, siendo la versión actual HTML5, que incorpora algunos elementos respecto a su versión anterior que hace que las aplicaciones web sean más diversas y funcionales, añadiendo también semántica a algunos de sus elementos.

Por ejemplo, en HTML5 algunas de las estructuras para definir los elementos gráficos del entorno son:   
* Radio button: `<input type=”radio”>`   
* Listas desplegables: `<select><option>...</option>...</select>`   
* Botón: `<button></button>`    

##### Estilos: CSS   
CSS (Cascading Style Sheets) es un lenguaje de diseño gráfico que permite personalizar la presentación de un documento escrito en un lenguaje de marcado, como HTML, al cual está muy ligado.

Estos dos lenguajes se almacenan en ficheros alojados en un servidor. Cuando algún cliente como un navegador hace una consulta a una página web, el servidor devuelve estos ficheros y es el navegador, cuando los recibe, el que se encarga de interpretar el contenido de ambos lenguajes para mostrar la página tal y como la vemos.

La versión actual es CSS3, la cual destaca respecto de su versión anterior en incorporar algunos estilos muy demandados por la comunidad como el redondeo de esquinas en los elementos, gradiente, transiciones, animaciones y las Media-Queries, muy populares actualmente para satisfacer la cantidad de tamaños y resoluciones de pantallas en las que una aplicación web puede cargarse (móviles, tablets, pcs, etc) y conseguir un diseño responsivo.

Por último, destacamos Bootstrap, un framework front-end para CSS utilizado en las empresas que se dedican al desarrollo web con el que poder construir interfaces responsivas.   

##### Lógica: JavaScript   
JavaScript es un lenguaje de alto nivel que aporta lógica y dinamismo a la parte front-end de las aplicaciones web, por ejemplo, las acciones que se desencadenan en la aplicación cuando un usuario utiliza un buscador, un formulario, un calendario, etc. Además, juega un papel muy importante a la hora de validar datos antes de enviarlos al servidor, evitando la carga excesiva de este.

La librería jQuery es ámpliamente utilizada en el mundo web ya que a través de ella se simplifica mucho el código nativo que escribimos con JavaScript, por lo que escribiendo el mismo código en jQuery conseguimos el mismo resultado.

Por otro lado, encontramos la librería React, creada por Facebook, que se centra en la creación de interfaces de usuario interactivas de forma sencilla.

## Compose: Introducción

Jetpack Compose es la nueva forma de programar interfaces de usuario propuesta por Google en 2019.

Google liberó su versión Beta en Febrero de 2021. Podemos empezar ya a incluir Jetpack Compose en nuestras apps ya que Google ha anunciado que la especificación del API no variará.

Esta tecnología sigue la misma dirección que *Swift UI* o *Flutter* usando un paradigma declarativo. Esto es un buen síntoma, ya que diferentes plataformas siguen una misma dirección.

Jetpack Compose se convertirá en el nuevo estándar de desarrollo de interfaces de usuario en Android. Jetbrains ha trabajado para traer este mismo estándar:

- Al Escritorio con [Compose for Desktop](https://www.jetbrains.com/es-es/lp/compose-desktop/), con [ejemplos de código en github](https://github.com/JetBrains/compose-multiplatform#compose-for-desktop).
- A la web, con [Compose for Web](https://compose-web.ui.pages.jetbrains.team/), con [ejemplos de código en github](https://github.com/JetBrains/compose-multiplatform#compose-for-web-html).

Las ventajas principales de Jetpack Compose son:

* Menos código para construir interfaces.
* Código mucho más intuitivo.
* Facilidad a la hora de reutilizar componentes.
* Programación de vistas en Kotlin.

### Programación Imperativa vs Declarativa

#### Imperativa:

Se define paso a paso la casuística de la aplicación, es decir, cuando se pinta algo, cuando cambia de color, etc.... Se indica a través del código lo que tiene que hacer y como tiene que hacerlo.

Manipular las vistas de forma manual

- Aumenta la probabilidad de errores:
- Es fácil olvidarse de actualizar estados de vistas.
- Es fácil crear estados ilegales (conflicto de actualizaciones)
- El mantenimiento de los estados de las vistas se hace complejo.

La mayoría de las veces usamos un paradigma imperativo a la hora de programar aplicaciones, aunque la industria está migrando a un modelo de UI declarativo:

#### Declarativa:

Con Jetpack Compose tenemos que cambiar nuestra mentalidad para empezar a utilizar un **paradigma declarativo**:

* Nuestra interfaz de usuario estará controlada por distintos **estados** que se irán actualizando.
* Cada vez que un estado cambie, la interfaz se refrescará y se producirá una **recomposición**.
* Para lidiar con la **recomposición**, tendremos que contemplar todos los posibles estados con anterioridad.
* Es costoso en términos computacionales: **Recomposición**.
* Aunque al principio parezca más complicado, este paradigma reduce la inconsistencia de estados, favorece la legibilidad del código y la reutilización de los componentes.

### Composición

La composición consiste en la reconstrucción de los componentes que forma la interface de usuario hasta reconstruir la interface completa. En Compose, las funciones que se encargan de esta reconstrucción se anotan con `@Composable`, es decir, todas las funciones que admiten composición deben ser anotadas con `@Composable`.

Las funciones *[@Composable](https://github.com/Composable "@Composable")*:

- Son funciones que reciben datos y emiten elementos de UI
- Pueden usar sentencias `for`, `if`, etc. para genera la potencia del lenguaje.
- Pueden aceptar parámetros. La lógica de la aplicación describe la UI.
- **No están ligadas** a ninguna clase, pueden ser definidas en cualquier sitio.
- **Deben empezar por letra mayúscula**, ya que estas funciones actúan como [widgets](https://en.wikipedia.org/wiki/Graphical_widget).

Por ejemplo, `Text()` es también una función que admite composición y que se encarga de crear el elemento caja de texto en la UI.

### Modo Preview

En Android existe una vista previa para los ficheros XML de Android que representan la interface gráfica. En compose también existe un modo preview para el código que construimos [`@Preview`](https://github.com/Preview "@Preview"). El funcionamiento del modo preview puede varias entre Jetpack Compose y Compose Desktop.

IntelliJ IDEA facilitará el preview de las vistas marcadas con esta anotación. Tenemos tres tipos de modo de maquetación: *Code*, *Split* (vista recomendada) y *Design*. *Split* y *Design* incorporan un modo interactivo (Interactive) que permite al desarrollador interactuar con la interfaz al igual que si estuviese interactuando con la aplicación.

Por tanto, para que nuestra interfaz aparezca en el modo interactivo tenemos que crear una función `@Composable` y anotarla con la anotación `@Preview`.

```kotlin
@Preview(showBackground = true)  
@Composable  
fun DefaultPreview() {  
    MyApplicationTheme {  
      Greeting("mates!!")
    }  
}
```

Recuerda anotar con `@Preview` el mismo código que le pasas a la función `setContent` o en la función `application`/`singleWindowApplication` dependiendo de si es Android o Desktop respectivamente. De esta forma siempre podrás ver en la previsualización el contenido final de la pantalla.

```kotlin
setContent {  
  MyApplicationTheme {  
      Surface(color = MaterialTheme.colors.background) {  
          Greeting("mates!!")  
      }  
  }
}
```

Si la pantalla de preview desaparece, recuerda cerrar la clase y volver a abrirla. El IDE realiza un análisis de código sobre la clase en busca de una función marcada con [`@Preview`](https://github.com/Preview "@Preview") para lanzar la previsualización.

<!--  Hablaremos más adelante sobre el parámetro  *showBackground* .-->

### Primeros componentes

Como hemos comentado, Jetpack Compose se basa en funciones "componibles", anotadas con `@Composable`. Estas funciones permiten definir la interfaz de usuario de tu aplicación mediante la descripción de cómo debería verse y proporcionando dependencias de datos, en lugar de centrarse en el proceso de construcción de la interfaz de usuario (inicializar un elemento, adjuntarlo a un padre, etc.).

#### Mostrar etiquetas:

Como se puede observar en el código de abajo, la función `Greeting()` contiene un elemento  `Text()`, y esta también es una función etiquetada con `@Composable`.

```kotlin
@Composable  
fun Greeting(name: String) {  
    Text(text = "Hello $name!")  
}
```

Repecto al código anterior, podemos decir:

- `Text()` es una función propia del SDK de Android que admite composición.
- `Text()` admite por parámetro argumentos como  `text`, `modifier`, `color`, `fontSize` , etc.
- Dichos parámetros pueden ser requeridos (como en el caso de  `text`) o no requeridos con valores por defecto (`color`, `modifier`). Consulta los parámetros de la función `Text()`.

Siempre que cambiemos valores de la interfaz, recuerda usar la opción *Build Refresh* para actualizar los valores en la Preview.

Se pueden incluir las funciones Compose definidas directamente en la función `setContent` y en Desktop en la función `application`/`singleWindowApplication`. El bloque `setContent`/`application`/`singleWindowApplication` define el diseño de la interface, por tanto, en este bloque, llamaremos a las funciones componibles. **Las funciones componibles solo se pueden llamar desde otras funciones componibles**.

```kotlin
class MainActivity : ComponentActivity() {  
    override fun onCreate(savedInstanceState: Bundle?) {  
        super.onCreate(savedInstanceState)  
        setContent {  
          Text(text = "Hello mates!!")  
        }  
    }  
}
```

> En Compose Desktop, el contenido tendrá que ir dentro de la función `application`, punto de entrada para la aplicación, y que a la vez recibe un componente `@Composable`, normalmente un componente `Window`. Como puedes apreciar no hay rastros de `Activity`, ni de `setContent`.

Un Ejemplo de lo anterior:

```kotlin
fun main() = application {
    Window(onCloseRequest = ::exitApplication) {
        App()
    }
}
```

y la función `App` estará definida como `@Composable`.

#### Creación de un botón y manejo de eventos

Al igual que `Text()` , `Button()` es otra función composable ofrecida por el SDK de Android.

```kotlin
@Composable  
fun GreetingButton() {  
    Button(onClick = {  
        // Do something  
    }) {

    }  
}
```

Uno de los parámetros que recibe la función `Button()` es la función bajo el argumento `onClick`, que actúa como callback, y que será notificado cada vez que se produzca un evento click sobre el botón.

Button tiene como argumento una función lambda, que admite composición, llamada `RowScope`. Mediante esta función podemos añadir textos, iconos, imágenes, etc, ya que `Button()` no tiene ningún contenido por defecto.

```kotlin
@Composable  
fun GreetingButton() {  
    Button(onClick = {  
      // Do something  
    }) {  
      GreetingText(name = "mates!")  
    }  
}
```

`RowScope` es un contenedor de elementos de forma horizontal. Si añadimos más componentes al`RowScope` del componente `Button()` éstos se alinearán consecutivamente de forma horizontal.

### Modificar componentes

#### Modifiers

Todos los elementos Composable que ofrece el SDK de Android aceptan un parámetro llamado `modifier`.

`Modifier` es una clase estática a la que se puede acceder sin necesidad de ser instanciada y desde cualquier lugar de nuestra aplicación. Tiene funciones para especificar parámetros como la anchura, altura, el tamaño total, padding, etc, de un componente.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier.width(80.dp))  
}
```

Los métodos de `Modifier()` implementan **method chaining pattern** de forma que permiten concatenar varias llamadas a métodos en la misma cadena pudiendo establecer varios parámetros en una única expresión.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .width(80.dp)  
            .height(240.dp))  
}
```

Los valores para `width()`, `height()`, y otras funciones, se establece en `DP`. Los `DP` son objetos de la inline class `DP`.

Como alternativa, usando el método `size()` podemos establecer valores para la anchura y para la altura de un componente, pasándole valores DP.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .size(width = 80.dp, height = 240.dp))  
}
```

Si no se indican los parámetros de `width()`, `height()`, el mismo valor será aplicado para ambos parámetros haciendo que el componente sea cuadrado.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .size(80.dp))  
}
```

`fillMaxSize` permite al componente ocupar todo el espacio que ocupa su componente padre.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .fillMaxSize())  
}
```

`fillMaxHeight` permite al componente ocupar todo el espacio en altura que ocupa su componente padre. La anchura se mantiene como `wrap_content`.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .fillMaxHeight())  
}
```

`fillMaxWidth` permite al componente ocupar todo el espacio en anchura que ocupa su componente padre. La altura se mantiene como `wrap_content`.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .fillMaxWidth())  
}
```

`fillMaxWidth()` y `fillMaxHeight()` aceptan como argumento fracciones (de `0` a `1`) que indican el máximo espacio que queremos que ocupe nuestro componente dentro de su componente padre.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
      modifier = Modifier  
            .fillMaxWidth(0.5f))  
}
```

#### Eventos de click, padding y orden de modificadores

La clase `Modifier` permite hacer cualquier componente Compose clickable. Al igual que en el caso del componente  `Button()` , `Modifier` acepta una función como parámetro del método `clickeable()` que se invocará cada vez que se produzca un evento de click sobre el componente.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
        modifier = Modifier  
            .width(80.dp)  
            .height(240.dp)  
            .clickable {  
              //Do something  
            })  
}
```

Recuerda que activando la opción **Interactive Mode** de la preview de Compose (en la ruta: `File -> Settings -> Experimental`, al ser experimental puede no aparecer o fallar) podrás ver cómo tu elemento ahora se resalta cuando es seleccionado indicando que se puede hacer click sobre él.

Puedes añadir padding (El padding es un espacio situado entre los bordes de la vista y su contenido) a tu componente usando el método `padding()` del `Modifier`. El valor se establece en `DP`.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
          modifier = Modifier  
            .padding(all = 20.dp)  
    )  
}
```

El método `padding()` puede ser aplicado a todos los lados del componente usando **all** o indicar el lado o los lados específicos:  **top** ,  **start** , **bottom** y **end** donde se desee aplicar.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
        modifier = Modifier  
            .width(80.dp)  
            .height(240.dp)  
            .clickable {  
              //Do something  
            })
            .padding(top = 20.dp)
}
```

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
        modifier = Modifier  
            .width(80.dp)  
            .height(240.dp)  
            .clickable {  
              //Do something  
            })
            .padding(top = 20.dp, bottom = 20.dp)
}
```

**El orden de los modificadores importa**. Si se aplica el método `padding()` como último elemento de la cadena el componente `Text()`* será clickable en su totalidad, incluyendo las dimensiones del padding. Si el método es aplicado antes que el método `clickeable()` la zona clickable del componente excluirá el padding indicado.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello $name!",  
        modifier = Modifier  
            .width(80.dp)  
            .height(240.dp)
            .padding(top = 20.dp, bottom = 20.dp)  
            .clickable {  
                  //Do something  
                })
}
```

# Customizar un componente

## TextStyle

La clase `TextStyle` permite customizar aspectos de un componente Composable:

* Color del texto.
* Tamaño del texto.
* Tipografía.
* Espacio entre letras.
* Indentación.
* etc.

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello: $name",  
        style = TextStyle(  
            color = Color.Red,  
            fontWeight = FontWeight.SemiBold,  
            fontSize = 18.sp)  
    )  
}
```

Jetpack Compose ya provee de estilos, llamados [Material Design](https://material.io/design) (consulta la URL), y como hemos comentado ya están predefinidos para poder usar en nuestros componentes a través de la clase `MatherialTheme`. Los siguientes estilos son de la clase `TextStyle`:

* `h1`.
* `h2`.
* `button`.
* `caption`.
* `body`.
* etc.

Podemos aplicar un `style` de tipo `TextStyle` predefinido como por ejemplo `MaterialTheme.typography.h5` y sobrescribir algún parámetro concreto por ejemplo el `fontWeight` haciendo uso de los valores ya predefinidos como `FontWeight.SemiBold`

```kotlin
@Composable  
fun GreetingText(name: String) {  
    Text(text = "Hello: $name",  
        style = MaterialTheme.typography.h5,  
        fontWeight = FontWeight.SemiBold  
    )  
}
```

`FontWeight` y `MatherialTheme` son una clase companion object de Kotlin, en las que todos sus componentes son estáticos y accesible desde los componentes.

# Contenedores

## Layouts: El componente `Surface`

El componente `Surface()` es un componente `@Componsable` que representa un bloque de UI que podemos añadir a nuestra interfaz y que puede tener color, modificadores, etc. y contener otros componentes, en concreto uno, a través de una lamda.
Si no le aplicamos modificadores no tendrá dimensiones y no podrá verse en la pantalla, por tanto aplicamos `fillMaxWidth()`.
Este componente puede formar nuestro componente principal `MainScreen` `@Composable` en la que ir colocando otros componentes.

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {
        //Aquí un componente
    }  
}
```

Podemos añadir otros componentes dentro de `Surface()`.

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Text(  
            text = "Hi mates!!",  
            style = MaterialTheme.typography.h5,  
            modifier = Modifier.wrapContentSize()  
        )  
    }  
}
```

`Text()` utiliza el método `wrapContentSize()` como modificador que indica que use solo el espacio necesario para pintar su contenido, en este caso `Hi mates!`. `wrapContentSize()` aplicará una alineación automática en `Surface()`, `Alignment.Center`, y situará el componente `Text()`en el centro del componente. Aunque esto se puede cambiar haciendo uso de la clase `Alignment`, ya que tiene multitud de valores para posicionar un componente dentro de su componente padre.

También podemos anidar componentes `Surface()`.

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
          Surface(  
              color = Color.Green,  
              modifier = Modifier.wrapContentSize(Alignment.TopEnd)  
          ) {  
              Text(  
                  text = "Hi mates!!",  
                  style = MaterialTheme.typography.h5,
                  modifier = Modifier.padding(20.dp)
              )  
          }  
    }
}
```

Anidando componentes de esta forma se puede establecer un background para el componente `Text()`. El modificador `wrapContentSize()` puede moverse ahora al componente padre `Surface()`, y por tanto, este componente `Surface()` ocupará solo lo que ocupe el componente `Text()` que contiene.

Recordamos que el componente `Surface()` acepta **un solo** componente hijo. Más adelante veremos cómo añadir varios componentes dentro de un componente padre.

## Otros contenedores

Para situaciones en las que se tengan más de un componente hijo, Jetpack Compose ofrece los componentes: **Row**, **Column** y **Box** :

* **Row**: Componente que puede albergar contenido de forma horizontal.
* **Column**: Componente que puede albergar contenido de forma vertical.
* **Box**: Componente que permite tener componentes encima o debajo de otros componentes de forma sencilla.

### Row

Al igual que  **Button**, **Row** contiene un **RowScope** que nos indica que podemos añadir componentes que admiten composición en su interior. Como indicamos anteriormente, dichos componentes se alinearán de forma horizontal.

A continuación, se muestra un ejemplo de componente **Row** con dos componentes **Surface** cuadrados que se alinean horizontalmente:

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
      Row {  
        Surface(  
            color = Color.Green,  
            modifier = Modifier.size(60.dp)  
        ) {}  
        Surface(  
            color = Color.Black,  
            modifier = Modifier.size(60.dp)  
        ) {}  
 } }}
```

Si vemos los argumentos que acepta el componente **Row** podemos observar dos muy interesantes: **verticalAlignment** y **horizontalArrangement** .

#### verticalAlignment

Mediante este argumento podemos indicar cómo queremos posicionar los hijos de nuestro componente **Row** con respecto a la línea vertical. Este argumento solo acepta parámetros del tipo **Alignment.Vertical** (valores como: **Top**, **CenterVertically** y **Bottom** ).

En el código que se muestra a continuación los hijos de posicionan centrados verticalmente con **CenterVertically** :

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Row(verticalAlignment = Alignment.CenterVertically) {  
            Surface(  
                color = Color.Green,  
                modifier = Modifier.size(60.dp)  
            ) {}  
            Surface(  
                color = Color.Black,  
                modifier = Modifier.size(60.dp)  
            ) {}  
        }
    }
}
```

#### `horizontalArrangement`

Este argumento nos permite indicar cómo disponer los elementos hijos en la línea horizontal. Acepta valores de la clase `Arrangement.Horizontal` (valores como: `Start`, `End` o `Center`).

En el código que se muestra a continuación los hijos se posicionan centrados verticalmente y horizontalmente con `Arrangement.Center`:

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Row(  
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.Center  
        ) {  
            Surface(  
                color = Color.Green,  
                modifier = Modifier.size(60.dp)  
            ) {}  
            Surface(  
                color = Color.Black,  
                modifier = Modifier.size(60.dp)  
            ) {}  
        }
    }
}
```

### `Column`

Como indicamos anteriormente, el componente `Column` alberga hijos de forma vertical.

A continuación, se muestra un ejemplo de componente `Column` con dos componentes `Surface` cuadrados que se alinean verticalmente:

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Column {  
            Surface(  
                color = Color.Green,  
                modifier = Modifier.size(60.dp)  
            ) {}  
            Surface(  
                color = Color.Black,  
                modifier = Modifier.size(60.dp)  
            ) {}  
        } 
    }
}
```

De forma similar al componente `Row`, `Column` acepta los siguientes argumentos: `horizontalAlignment` y `verticalArrangement`.

#### `horizontalAlignment`

Mediante este argumento podemos indicar cómo queremos posicionar los hijos de nuestro componente `Column` con respecto a la línea horizontal. Este argumento solo acepta parámetros del tipo `Alignment.Horizontal` (valores como: `Start`, `CenterHorizontally` y `End`).

En el código que se muestra a continuación los hijos se posicionan centrados horizontalmente con `CenterHorizontally`:

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Column(  
            horizontalAlignment = Alignment.CenterHorizontally  
        ) {  
            Surface(  
                color = Color.Green,  
                modifier = Modifier.size(60.dp)  
            ) {}  
            Surface(  
                color = Color.Black,  
                modifier = Modifier.size(60.dp)  
            ) {}  
         } 
    }
}
```

#### `verticalArrangement`

Este argumento permite indicar cómo disponer los elementos hijos en la línea vertical. Acepta valores de la clase `Arrangement.Vertical` (valores como: `Top`, `Bottom`o`Center`).

En el código que se muestra a continuación los hijos se posicionan centrados verticalmente y horizontalmente con `Arrangement.Center`

```kotlin
@Composable  
fun MainScreen() {  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        Column(  
            horizontalAlignment = Alignment.CenterHorizontally,  
            verticalArrangement = Arrangement.Center  
        ) {  
            Surface(  
                color = Color.Green,  
                modifier = Modifier.size(60.dp)  
            ) {}  
            Surface(   
                color = Color.Black,  
                modifier = Modifier.size(60.dp)  
            ) {}  
        }
    }
}
```

# Reusar componentes

Tomando como ejemplo uno de los códigos vistos anteriormente, podemos observar que los hijos de `Column` son dos cuadrados representados con un componte `Surface` que son iguales y estamos añadiendo código repetitivo.

```kotlin
@Composable
fun MainScreen() {
    Surface(
        color = Color.LightGray,
        modifier = Modifier.fillMaxSize()
    ) {
      Column {
          Surface(
              color = Color.Green,
              modifier = Modifier.size(60.dp)
          ) {}
          Surface(
              color = Color.Black,
              modifier = Modifier.size(60.dp)
          ) {}
        }
    }
}
```

El componente `Surface` puede abstraerse en una función de composición específica y ser reutilizado de una forma mucho más sencilla.

Abstracción en componente `MySquare`:

```kotlin
 @Composable
fun MySquare() {
    Surface(
        color = Color.Green,
        modifier = Modifier.size(60.dp)
    ) {}
}
```

Utilización de componente `MySquare`:

```kotlin
@Composable
fun MainScreen() {
    Surface(
        color = Color.LightGray,
        modifier = Modifier.fillMaxSize()
    ) {
        Column {
            MySquare()
            MySquare()
            MySquare()
        }
 }}
```

Podemos parametrizar nuestro nuevo componente `MySquare` pasándole como argumento el color.

```kotlin
@Composable
fun MySquare(color: Color) {
    Surface(
        color = color,
        modifier = Modifier.size(60.dp)
    ) {}
}

@Composable
fun MainScreen() {
    Surface(
        color = Color.LightGray,
        modifier = Modifier.fillMaxSize()
    ) {
        Column {
            MySquare(Color.Red)
            MySquare(Color.Yellow)
            MySquare(Color.Green)
        }
    }
 }
```

# Cómo funciona State

## Recomposición

La recomposición es el proceso que se encarga de actualizar la pantalla, en concreto, los componentes que admiten composición.

Para lanzar la recomposición es indispensable tener una implementación de `State`  para cada componente composable, al menos para los que tienen un estado que cambia o puede cambiar a lo largo del tiempo.

## State

El `State` de una aplicación se puede definir como **cualquier valor o dato que puede cambiar a lo largo del tiempo**, ya sea por un evento click en una lista, una entrada de datos en un formulario de texto, etc.

En Jetpack Compose `State` es un componente más del propio componente composable.

## Flujo de datos unidireccional

El flujo de UI en Jetpack Compose puede pensarse como un bucle en el que se dispara un evento que actualiza un `State`, por ejemplo, un click a un botón que desencadena la actualización de una lista. Este nuevo valor de `State` pasa por todo el árbol de la UI de elementos composables vinculados a ese `State`, es decir, que deben tener en cuenta los posibles valores de dicho `State` y actualizar la UI.

.![image.png](assets/image.png)

Este flujo de **`Event` - `State`** es unidireccional lo que proporciona ciertas ventajas como:

* **Mayor testeabilidad** : `State` está desacoplado de la UI, es muy fácil hacer tests de ambas partes de forma aislada.
* **Mayor consistencia en la UI** : Este flujo obliga a que todos los `State` sean reflejados en la UI de forma continua eliminando las posibles inconsistencias entre los componentes visuales y los estados.

## Controlar State en una lista

Partimos de un componente `MainScreen` que contiene una lista `StudentList` de componentes `StudentText` y un `Button` que añade nuevos elementos a la lista de estudiantes.

**`MainScreen`**

```kotlin
@Composable
fun MainScreen() {
    Surface(
        color = Color.LightGray,
        modifier = Modifier.fillMaxSize()
    ) {
        StudentList()
    }
}
```

**`StudentList`**

```kotlin
@Composable
fun StudentList() {
    val students = mutableListOf("Juan", "Victor", "Esther", "Jaime")
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        for (student in students) {
            StudentText(name = student)
        }
        Button(
            onClick = { students.add("Miguel") },
        ) {
            Text(text = "Add new student")
        }
    }
}
```

**`StudentText`**

```kotlin
@Composable
fun StudentText(name: String) {
    Text(
        text = name,
        style = MaterialTheme.typography.h5,
        modifier = Modifier.padding(10.dp)
    )
}
```

Si activamos el modo interactivo y pulsamos el botón añadir podemos observar cómo la lista no añade el nuevo valor aunque modifiquemos la lista de estudiantes. Esto es debido a que no se ha implementado ningún `State` a la lista de datos que dispare la recomposición.

Para añadir `State` a la lista es necesario crear la lista del tipo `SnapshotStateList` a través del método `mutableStateListOf`

```kotlin
val studentsState = mutableStateListOf("Juan", "Victor", "Esther", "Jaime")
```

Observamos que el compilador nos obliga a utilizar el bloque `remember`. Este bloque permite que el estado sea recordado durante la recomposición y que no desaparezca después.

```kotlin
val studentsState = remember { mutableStateListOf("Juan", "Victor", "Esther", "Jaime") }
```

Finalmente, la función StudentList queda de esta forma:

```kotlin
@Composable
fun StudentList() {
    val studentsState = remember { mutableStateListOf("Juan", "Victor", "Esther", "Jaime") }
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        for (student in studentsState) {
            StudentText(name = student)
        }
        Button(
            onClick = { studentsState.add("Miguel") },
        ) {
            Text(text = "Add new student")
        }
    }
}
```

Si activamos ahora el modo interactivo y pulsamos el botón añadir vemos cómo el nuevo elemento se añade de forma satisfactoria al final de la lista.

# El patrón State Hoisting

El patrón **State Hosting** consiste en mover los estados al componente padre de tal forma que los hijos nunca tengan que manejarlos.

El principal objetivo es reemplazar la variable de estado por dos argumentos en cada función composable hija:

* `value: T` El valor para mostrar.
* `onValueChange: (T) -> Unit` Evento (lambda) que dispara la modificación del `State`.

El patrón **State Hosting** ofrece las siguientes ventajas:

* Manejar los estados de forma única y centralizada.
* Solo las funciones que manejan estados pueden modificarlos.
* Funciones composable hijas no tienen que preocuparse por manejar estados, solo:
  * pintar información: Los datos tiene un flujo top-down
  * elevar eventos: Los eventos tiene un flujo bottom-up.

![Ilustración del flujo de datos en una IU de Compose, desde los objetos de nivel superior hasta sus elementos secundarios.](https://developer.android.com/images/jetpack/compose/mmodel-flow-data.png?hl=es-419)

![Ilustración de cómo responden los elementos de la IU a la interacción mediante la activación de eventos controlados por la lógica de la app.](https://developer.android.com/images/jetpack/compose/mmodel-flow-events.png?hl=es-419)[Mas informacion](https://developer.android.com/jetpack/compose/mental-model?hl=es-419#paradigm)

A continuación, vamos a aplicar el patrón **State Hosting** a la aplicación de alumnos de la lección anterior. Para ello, seguiremos los siguientes pasos:

* Mover la lista de estudiantes al punto de entrada `MainScreen`.
* Parametrizar la función `StudentList` con el valor a mostrar y la función lambda de eventos de click.

Modificamos la función:

```kotlin
@Composable
fun StudentList(students: List<String>, onButtonClick: () -> Unit) {
    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        for(student in students) {
            StudentText(name = student)
        }
        Button(
            onClick = onButtonClick,
        ) {
            Text(text = "Add new student")
        }
    }
}
```

Y modificamos el código en la que se hace uso de esta función:

```kotlin
@Composable  
fun MainScreen() {  
    val studentsState = remember { mutableStateListOf("Esther", "Jaime") }  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        StudentList(studentsState) {  
            studentsState.add("Miguel")  
        }  
    }
 }
```

Como podemos observar en el código, el componente `StudentList` ya no sabe nada sobre estados. Le hemos aplicado las dos premisas del patrón **State Hoisting** la parametrización de la lista de estudiantes y la función para elevar los eventos de click del botón añadir. Ahora es el componente `MainScreen` el encargado de manejar estados y de modificarlos.

# El componente `TextField` con State

El componente `TextField` es el equivalente al componente `EditText` de Android tradicional.

En esta lección veremos cómo manejar correctamente el estado de este componente a través de `State`.

Vamos a iterar nuestra aplicación de añadir alumnos incorporando un campo de introducción de texto `TextField` que permita al usuario escribir el nombre del alumno.

Cuando usamos `TextField`, es prácticamente obligatorio hacerlo de la mano de `State` de forma que podamos ver cómo el valor del componente cambia cada vez que se introduce texto tal y como se muestra a continuación:

```kotlin
val newStudentState = remember { mutableStateOf("")}  
TextField(  
    value = newStudentState.value,  
    onValueChange = {  
        newInput -> newStudentState.value = newInput  
    }  
)
```

Como vemos en el código anterior, se usa `mutableStateOf` para guardar el estado del componente `TextField`.

Podríamos incorporar este snippet de código en nuestro componente `StudentList` pero implementaremos **State Hoisting** para no manejar estados en componentes internos y elevarlos al componente `MainScreen`.

```kotlin
@Composable  
fun StudentList(
    students: List<String>,  
    onButtonClick: () -> Unit,  
    studentName: String,  
    onStudentNameChange: (String) -> Unit  
) {  
    Column(  
        modifier = Modifier.fillMaxSize(),  
        horizontalAlignment = Alignment.CenterHorizontally  
    ) {  
        for (student in students) {  
            StudentText(name = student)  
        }  
        TextField(  
            value = studentName,  
            onValueChange = onStudentNameChange  
        )  
        Button(  
            onClick = onButtonClick
        ) {  
            Text(text = "Add new student")  
        } 
    }
}
```

En el código anterior se puede observar como parametrizamos `StudentList` con los siguientes argumentos:

* `studentName: String` Contiene el valor del `TextField`. Como veremos en `MainScreen` a continuación, hace referencia a un `State`.
* `onStudentNameChange: (String)->Unit` lambda que eleva el valor del componente `TextField` cuando cambia.

```kotlin
@Composable  
fun MainScreen() {  
    val studentsState = remember { mutableStateListOf("Esther", "Jaime") }  
    val newStudentState = remember { mutableStateOf("") }  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        StudentList(  
            studentsState,  
            { studentsState.add(newStudentState.value) },  
            newStudentState.value,  
            { newStudent -> newStudentState.value = newStudent }  
        )  
    }  
}
```

* `newStudentState: MutableState` el valor de `TextField` es un `State` y todas las variaciones que se produzcan sobre él dispararán la recomposición.
* Vemos como en las lambdas `onButtonClick` y `onStudentNameChange` se inserta un valor en la lista de estudiantes y se modifica el valor del componente `TextField` respectivamente.

# `ViewModel` y `LiveData`

## Introducción a `ViewModel` y `LiveData`

En lecciones anteriores vimos el patrón **State Hoisting** y cómo elevar los estados lo más arriba posible dentro de la jerarquía de componentes composables.

El siguiente objetivo es evitar que nuestras vistas (`Fragments` y `Activities`) sean las encargadas de manejar estados y trasladar dicha responsabilidad al componente `ViewModel`

> `Fragments` y `Activities` son vistas usadas en **Jetpack Compose Android**.

`ViewModel` y `LiveData` son componentes de Jetpack y forman parte de la arquitectura **Model View-View Model (MVVM)** propuesta por Google para el desarrollo de aplicaciones Android.

### `ViewModel`

* Es responsable de preparar y manejar estados para la UI (`Fragments` y `Activities`). Tiene una relación directa con la vista para mostrar los datos.
* Mediante el uso de `ViewModel` seremos capaces de desacoplar la lógica de presentación de los componentes de UI.
* `ViewModel` está directamente relacionado con el modelo de los datos que se van a mostrar en la vista. Esto es debido a que `ViewModel` es parte de la arquitectura  **MVVM** .
* La vista espera un estado de UI proporcionado por `ViewModel` y, a su vez, `ViewModel` podrá actualizar dicho estado de UI si se producen eventos desde la vista.
* En resumen, la vista podrá recibir actualizaciones del estado de UI desde el `ViewModel`.
* En esta arquitectura, la vista no pregunta por el estado de la UI al `ViewModel` continuamente. Tiene la posibilidad de subscribirse al componente `LiveData` dentro de `ViewModel`

![image.png](assets646405734783-image.png)

### `LiveData`

* `LiveData` es un componente observable, permite que otros componentes se suscriban a él con el fin de ser notificados si se produce algún cambio.
* `LiveData` contiene un estado y su principal responsabilidad es avisar a sus suscriptores cuando dicho estado cambie.
* `Fragments` y `Activities` pueden suscribirse a un componente `LiveData` para ser notificados siempre que se produzca una actualización sobre un `State`.
* Si se produce un evento y el `State` relacionado con el componente `LiveData` cambia, los `Fragments` y `Activities` suscritos a él serán notificados al mismo tiempo.
* `LiveData` está pendiente del ciclo de vida de `Fragments` y `Activities`. Si estos van a un estado `onDestroy` el componente `LiveData` cierra y destruye la conexión con ellos automáticamente.

![image.png](assets646405775503-image.png)

## `State` en `ViewModel`

Partimos de una aplicación que contiene un componente `TextField()` y un componente `Text()` que refleja los cambios que se producen en `TextField()` cuando el usuario introduce texto en él.

`MainScreen`

```kotlin
@Composable  
fun MainScreen() {  
    val nameState = remember { mutableStateOf("") }  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        MainLayout(  
            nameState.value  
        ) { newName -> nameState.value = newName }  
    }
}
```

`MainLayout`

```kotlin
@Composable  
fun MainLayout(  
    name: String,  
    onTextFieldChange: (String) -> Unit  
) {  
    Column(  
        modifier = Modifier.fillMaxSize(),  
        horizontalAlignment = Alignment.CenterHorizontally  
    ) {  
        TextField(  
            value = name,  
            onValueChange = onTextFieldChange  
        )  
        Text(text = name)  
    }  
}
```

El siguiente paso será mover `nameState` a un componente `ViewModel`. Para ello, creamos una nueva clase `MainViewModel` que herede de `ViewModel` como se muestra a continuación:

```kotlin
class MainViewModel: ViewModel() {  

    val textFieldState = MutableLiveData("")  

    fun onTextChange(newText: String) {  
        textFieldState.value = newText  
    }  
}
```

`textFieldState: MutableLiveData` refleja ahora el estado del dato al cual nuestra UI tendrá que suscribirse para recibir actualizaciones.

A través del método público `onTextChange`, la UI mandará el evento de cambio de texto que genere el componente `TextField`.

Para leer los datos de nuestro nuevo `MainViewModel` desde la vista `MainScreen` tendremos que modificar el componente de la siguiente forma:

```kotlin
@Composable  
fun MainScreen(viewModel: MainViewModel = MainViewModel()) {  
    val nameState = viewModel.textFieldState.observeAsState("")  
    Surface(  
        color = Color.LightGray,  
        modifier = Modifier.fillMaxSize()  
    ) {  
        MainLayout(  
            nameState.value  
        ) { newName -> viewModel.onTextChange(newName) }  
    }
}
```

El valor de `nameState` proviene ahora del componente `LiveData` definido en nuestro nuevo `MainViewModel`.

Necesitamos que `nameState` sea un `State` y no un `LiveData`. Para conseguir esto, hay que añadir una nueva dependencia a nuestro fichero `build.gradle`, permitiendo el uso del método `observeAsState` encargado de la conversión a `State`:

```groovy
implementation "androidx.compose.runtime:runtime-livedata:$compose_version"
```

Los eventos de `TextField` recogidos en la lambda son enviados ahora a nuestro `MainViewModel` y a su vez notificados a `LiveData` a través del método `onTextChange`.

# Listas y Theming

## Listas con Lazy Composable

En lecciones anteriores vimos cómo implementar listas de elementos a través de los componentes **Column** y  **Row** .

Cuando el número de elementos a mostrar es grande, es preferible usar componentes Lazy Composable como **LazyColumn** o  **LazyRow** . Las ventajas de usar estos componentes son:

* Implementación de scroll de forma automática.
* Reciclaje de elementos de la lista.
* Mismos principios que el componente  **RecyclerView** .

La diferencia entre **LazyColumn** y **LazyRow** es la orientación en la que se integran sus elementos y se desplazan.

**LazyColumn** produce un desplazamiento vertical mientras que **LazyRow** produce un desplazamiento horizontal.

### LazyListScope

Al igual que **Column** y  **Row** , los componentes Lazy Composable ofrecen un **Scope** para añadir contenido.

En el caso de  **LazyListScope** , se ofrece un conjunto de funciones para añadir elementos a la lista.

```kotlin
LazyColumn {  
    // Add a single item  
    item {  
        Text(text = "First item")  
    }  
    // Add 3 items  
    items(3) { index ->  
        Text(text = "Item: $index")  
    }  
    // Add another single item  
    item {  
        Text(text = "Last item")  
    }  
}
```

* **item** : Agrega un solo elemento a la lista.
* **items(N)** : Agrega varios elementos a la lista.

```kotlin
@Composable  
funMessageList(messages: List<String>) {  
    LazyColumn {  
        items(messages) { message ->  
            MessageRow(message)  
        }
    }
}  

@Composable  
funMessageRow(message: String) {  
    Text(text = message)  
}
```

Como vemos en el código anterior, existen funciones de extensión que permiten agregar colecciones de elementos como  **List** .

Para agregar padding alrededor de los bordes del contenido de la lista, el componente permite añadir parámetros del tipo **PaddingValues** al parámetro **contentPadding** como se muestra a continuación:

```kotlin
LazyColumn(  
    contentPadding = PaddingValues(horizontal = 16.dp, vertical = 8.dp),  
) {  
    // ...  
}
```

En este ejemplo, se agregan 16.dp de padding a los bordes horizontales (izquierda y derecha) y 8.dp al principio y al final del contenido.

Para agregar espaciado entre elementos, puede usarse  **Arrangement.spacedBy** . En el siguiente ejemplo, se agregan 4.dp de espacio entre cada elemento:

```kotlin
LazyColumn(  
    verticalArrangement = Arrangement.spacedBy(4.dp),  
) {  
  // ...  
}
```

## Card, Image y Coil

### El componente Card

El componente **Card** es el equivalente del componente  **CardView** . Este componente sirve para mostrar contenido y acciones de un tema determinado aceptando para ello elementos como imágenes o texto. Puedes visitar la [documentación](https://material.io/components/cards#usage) de Material Design para obtener más información sobre el uso de este componente.

**Card** acepta un atributo **elevation** que hace que el componente tenga una elevación sobre el eje Z dando una sensación de profundidad y estableciendo un sombreado sobre su vista padre.

```kotlin
@Composable  
fun CardItem() {  
    Card(  
        Modifier
            .padding(10.dp)  
            .fillMaxWidth(),  
        elevation = 10.dp
    ) {  
        Column(  
            Modifier.padding(10.dp)  
        ) {  
            Text(text = "Hello OpenWebinars")  
            Text(text = "This is a card test")  
        }  
    }
}
```

### El componente Image

El componente **Image** es el equivalente de  **ImageView** . Permite cargar imágenes en Android. Recibe por parámetro:

* **painter** : Recurso gráfico que se pintará en el componente.
* **contentDescription** : Corresponde con la descripción de la imagen. Será leído por herramientas de accesibilidad.

### Coil

[Coil](https://coil-kt.github.io/coil/compose/) es una librería de carga de imágenes para Android. Está implementada usando coroutines y es muy ligera y fácil de integrar en Jetpack Compose.

Para su integración hay que incluir la dependencia: **implementation(“io.coil-kt::coil-compose::1.3.2”)**

**Como es una librería que permite la carga de imágenes de red es indispensable añadir el permiso de **INTERNET** al **fichero AndroidManifest.xml.****

<pre class="hljs applescript"><strong><code class="language-xml">  <uses-permission android:name="android.permission.INTERNET" /></code></strong></pre>

<pre class="hljs lisp"><strong><code class="language-kotlin">Image(  
    painter = rememberImagePainter("https://images.dog.ceo/breeds/bulldog-boston/n02096585_1761.jpg"),  
    contentDescription = "This is a beautiful dog",  
)</code></strong></pre>

## Theming

En esta lección se explica cómo estilizar una aplicación Android de forma sencilla usando Jetpack Compose con la ayuda de  **Material Theming** .

Tradicionalmente, para definir temas en Android, se usa el fichero **themes.xml** pero con Jetpack Compose todo se resuelve a nivel de clases Kotlin.

A continuación, se detalla cómo customizar colores, tipografías y formas de manera sencilla con solo unas pocas líneas de código.

### MaterialTheme

La clase **MaterialTheme** define estilos basándose en los principios de Material Design. En Jetpack Compose, esta clase está disponible como una función que admite composición en la cual se pueden customizar los valores por defecto.

```kotlin
@Composable
fun MaterialTheme(
    colors: Colors = MaterialTheme.colors,
    typography: Typography = MaterialTheme.typography,
    shapes: Shapes = MaterialTheme.shapes,
    content: @Composable () -> Unit
)
```

Tal y como se muestra en el código anterior, se pueden modificar los siguientes atributos:  **colors** , **typography** y  **shapes** . A continuación, se explica detalladamente cada uno de los siguientes atributos con el objetivo de entender mejor cómo modificarlos para obtener una customización específica.

### Color

Antes de explicar la clase **Colors** es importante saber cómo se utiliza la clase  **Color** . Jetpack Compose utiliza **Color** para representar un color. Hay dos formas básicas de definir un color mediante esta clase:

* Hexadecimal:

```kotlin
val red = Color(0xffff0000)
```

* RGB:

```kotlin
val red = Color(red = 1f, green = 0f, blue = 0f)
```

Es una buena práctica definir los colores de la aplicación en un fichero  **Color.kt** .

```kotlin
import androidx.compose.ui.graphics.Color  

val brown = Color(0xECE1D0)  
val yellow = Color(0xFFDAA95E)
```

Y acceder a ellos como se indica a continuación:

```kotlin
Text("Hello Openwebinars", color = brown)
```

Para soportar un estilo Material Design, es importante definir un conjunto de colores en un tema referenciándolos después desde ahí. A continuación, se muestra cómo hacerlo.

### Colors

La clase Colors es provista por Jetpack Compose y facilita la definición de dicho conjunto de colores para soportar el sistema Material Design.

```kotlin
class Colors(
    primary: Color,
    primaryVariant: Color,
    secondary: Color,
    secondaryVariant: Color,
    background: Color,
    surface: Color,
    error: Color,
    onPrimary: Color,
    onSecondary: Color,
    onBackground: Color,
    onSurface: Color,
    onError: Color,
    isLight: Boolean
)
```

El objetivo de esta lección no es definir a qué aspecto de una aplicación corresponde cada atributo de la clase  **Colors** , sin embargo, toda esta información puede consultarse en la documentación de [Material Design sobre el sistema de colores](https://material.io/design/color/the-color-system.html#color-usage-and-palettes).

Jetpack Compose cuenta por defecto con funciones de tipo builder para crear conjuntos de temas predefinidos del tipo light y dark: **lightColors** y  **darkColors** . A continuación, se muestra la función  **darkColors** .

```kotlin
fun darkColors(  
    primary: Color = Color(0xFFBB86FC),  
    primaryVariant: Color = Color(0xFF3700B3),  
    secondary: Color = Color(0xFF03DAC6),  
    secondaryVariant: Color = secondary,  
    background: Color = Color(0xFF121212),  
    surface: Color = Color(0xFF121212),  
    error: Color = Color(0xFFCF6679),  
    onPrimary: Color = Color.Black,  
    onSecondary: Color = Color.Black,  
    onBackground: Color = Color.White,  
    onSurface: Color = Color.White,  
    onError: Color = Color.Black  
): Colors = Colors(  
    primary,  
    primaryVariant,  
    secondary,  
    secondaryVariant,  
    background,  
    surface,  
    error,  
    onPrimary,  
    onSecondary,  
    onBackground,  
    onSurface,  
    onError,  
    false)
```

Se considera una buena práctica definir las paletas de colores de una aplicación, usando las funciones builder mencionadas anteriormente, en un fichero **Theme.kt** tal y como se muestra a continuación:

```kotlin
private val DarkColorPalette = darkColors(  
    primary = Purple200,  
    primaryVariant = Purple700,  
    secondary = Teal200  
)  

private val LightColorPalette = lightColors(  
    primary = Purple500,  
    primaryVariant = Purple700,  
    secondary = Teal200  
 )
```

### Typography

La clase  **Typography** , provista por Jetpack Compose, es la encargada de ayudar a crear estilos para etiquetas de texto. A través de dicha clase podemos definir el estilo de cada tipo de texto reflejado en Material Design (h1, h2, button, caption, body1, body2, etc). A continuación, se muestra el constructor por defecto de dicha clase para ayudar a comprender mejor su funcionamiento.

```kotlin
constructor(  
    defaultFontFamily: FontFamily = FontFamily.Default,  
    h1: TextStyle = TextStyle(  
        fontWeight = FontWeight.Light,  
        fontSize = 96.sp,  
        letterSpacing = (-1.5).sp  
    ),  
    h2: TextStyle = TextStyle(  
        fontWeight = FontWeight.Light,  
        fontSize = 60.sp,  
        letterSpacing = (-0.5).sp  
    ),  

    .... 

    subtitle1: TextStyle = TextStyle(  
        fontWeight = FontWeight.Normal,  
        fontSize = 16.sp,  
        letterSpacing = 0.15.sp  
    ),  
    subtitle2: TextStyle = TextStyle(  
        fontWeight = FontWeight.Medium,  
        fontSize = 14.sp,  
        letterSpacing = 0.1.sp  
    ),  
    body1: TextStyle = TextStyle(  
        fontWeight = FontWeight.Normal,  
        fontSize = 16.sp,  
        letterSpacing = 0.5.sp  
    ),  
    button: TextStyle = TextStyle(  
        fontWeight = FontWeight.Medium,  
        fontSize = 14.sp,  
        letterSpacing = 1.25.sp  
    ),

    ....

  )
```

Para conocer en detalle la escala de cada valor de cada tipo se recomienda visitar la [documentación de Material Design](https://material.io/design/typography/the-type-system.html#type-scale).

Para customizar los atributos de texto de la aplicación se recomienda como buena práctica crear un objeto de la clase **Typography** en un fichero **Type.kt** y sobrescribir los tipos de texto que se deseen tal y como se muestra en el ejemplo a continuación.

```kotlin
val Typography = Typography(  
    body1 = TextStyle(  
        fontFamily = FontFamily.Default,  
        fontWeight = FontWeight.Normal,  
        fontSize = 16.sp  
    ),  
    button = TextStyle(  
        fontFamily = FontFamily.Default,  
        fontWeight = FontWeight.W500,  
        fontSize = 14.sp  
    ),  
    caption = TextStyle(  
        fontFamily = FontFamily.Default,  
        fontWeight = FontWeight.Normal,  
        fontSize = 12.sp 
    )  
)
```

### Shapes

En muchas ocasiones, durante el desarrollo de una aplicación, es necesario definir formas que actúen como background de vistas con el objetivo de redondear bordes, establecer apariencias circulares, cuadradas, etc.

Tradicionalmente, las formas se definen en un fichero XML bajo el tag  **shape** . Crear formas con Jetpack Compose es más sencillo y, además, pueden ser provistas a la función **MaterialTheme** haciendo que los componentes nativos como **Button** o **TextField** varíen su aspecto por defecto.

### Uso de MatherialTheme

Después de describir todos los parámetros que puede recibir  **MaterialTheme** , se recomienda crear una función que admita composición y que aplique las sobrescrituras previas definidas de cada uno de ellos tal y como se muestra a continuación.

```kotlin
@Composable  
fun AppTheme(darkTheme: Boolean = isSystemInDarkTheme(), content: @Composable() () -> Unit) {  
    val colors = if (darkTheme) {  
        DarkColorPalette  
    } else {  
        LightColorPalette  
    }  
    MaterialTheme(  
        colors = colors,  
        typography = Typography,  
        shapes = Shapes,  
        content = content  
    )  
}
```

Un punto muy importante de esta función es la comprobación sobre si el sistema está en modo oscuro mediante la utilidad  **isSystemInDarkTheme** . Con el uso de esta función, pueden aplicarse paletas de colores distintas si el modo oscuro está activo o no.

# Bibliografía

- https://github.com/JetBrains/compose-jb/tree/master/tutorials - Tutorial sobre los principales componentes de **Jetpack Compose Desktop**
- https://www.tutorialesprogramacionya.com/composeya/ - Conceptos de compose
- https://www.develou.com/category/android/ - Articulos sobre compose
- https://www.develou.com/android-estado-en-compose/ - Estado en compose
- https://github.com/jamesreve/android-jetpack-compose - Ejemplos de Jetpack compose
- https://medium.com/droid-latam/jetpack-compose-i-motivaci%C3%B3n-50e085543923 - Que es Jetpack Compose
- https://medium.com/@facundomr/jetpack-compose-ii-funciones-composable-8d4d1d40ed44 - Funciones @Composables
- https://medium.com/@facundomr/jetpack-compose-iii-flujo-de-datos-y-eventos-e62d5f8bce6f - Arquitectura de la IU, flujo de informacion y eventos.
- https://plugins.jetbrains.com/plugin/10942-kotlin-fill-class - Plugin para rellenar los  argumentos de clases, muy util en Jetpack Compose

## Fuente
