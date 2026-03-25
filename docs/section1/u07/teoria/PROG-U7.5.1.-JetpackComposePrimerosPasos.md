---
title: "UD 7 - 7.5.1 Jetpack Compose, introducción y primeros componentes"
description: Introducción a Jetpack Compose en Android, paradigma declarativo y primeros componentes básicos
summary: Qué es Jetpack Compose, cómo cambia la forma de construir interfaces en Android y cómo crear los primeros componentes con Kotlin.
authors:
    - Eduardo Fdez
date: 2026-03-25
icon: "material/file-document-outline"
permalink: /prog/unidad7/7.5.1
categories:
    - PROG
tags:
    - Kotlin
    - Android
    - Compose
    - GUI
---

## 7.5.1 Jetpack Compose: introducción y primeros componentes

En [7.5 Interfaces gráficas de usuario](/prog/unidad7/7.5) hemos visto qué
problema resuelven las GUI y por qué los eventos son tan importantes. A partir
de aquí daremos un paso más: **programar interfaces gráficas en Android con
Jetpack Compose**.

Este tema se centra en la base conceptual y en los primeros bloques de código.
El siguiente apartado de la unidad se dedicará al estado, los eventos y la
actualización de la interfaz.

| Código | Descripción |
|--------|-------------|
| RA5 | Realiza operaciones de entrada y salida de información, utilizando procedimientos específicos del lenguaje y librerías de clases. |
| CE f | Se han utilizado las herramientas del entorno de desarrollo para crear interfaces gráficas de usuario simples. |
| CE g | Se han programado controladores de eventos. |
| CE h | Se han escrito programas que utilicen interfaces gráficas para la entrada y salida de información. |

!!! abstract "Qué vas a aprender en este tema"
    - Qué es Jetpack Compose y por qué se usa en Android.
    - Qué significa trabajar con un paradigma declarativo.
    - Cómo se define un componente con `@Composable`.
    - Cómo se carga una interfaz con `setContent`.
    - Cómo usar `@Preview` y los primeros componentes visuales.

### 1. Qué es Jetpack Compose

**Jetpack Compose** es el toolkit moderno de Android para crear interfaces de
usuario usando Kotlin. Su idea principal es que la interfaz se describe
directamente con código Kotlin, sin depender del enfoque clásico basado en XML
como pieza principal.

Esto no significa solo “escribir la UI en otro sitio”. Lo importante es que
Compose cambia la forma de pensar la interfaz:

- una pantalla se construye a partir de componentes;
- esos componentes reciben datos;
- la UI se actualiza cuando cambian esos datos.

Hoy Compose es una tecnología consolidada dentro del desarrollo Android. Además
existen variantes del ecosistema Compose para otras plataformas, pero en este
bloque nos centraremos en el caso más útil para empezar: **Android con
Jetpack Compose**.

### 2. Qué ventaja aporta frente al enfoque clásico

En el modelo tradicional de Android era habitual:

1. definir la interfaz en XML;
2. enlazar los controles desde Kotlin o Java;
3. modificar propiedades manualmente;
4. coordinar eventos y cambios de pantalla con bastante código de soporte.

Compose simplifica esa idea porque permite describir la interfaz directamente
con funciones Kotlin. Eso facilita:

- reutilizar componentes;
- leer mejor la relación entre datos y UI;
- reducir código repetitivo;
- iterar más rápido con las vistas previas del IDE.

!!! note "No te quedes solo con la sintaxis"
    La mejora importante de Compose no es únicamente escribir menos código. La mejora real es que la UI se piensa como una representación del estado.

### 3. Imperativo frente a declarativo

Muchas interfaces clásicas se programan con una mentalidad **imperativa**: se
indica paso a paso qué componente hay que crear, localizar o modificar.

Compose trabaja con una mentalidad **declarativa**. En lugar de dar instrucciones
manuales del tipo “cambia este texto” o “haz visible este control”, describimos
qué debería verse en pantalla según los datos actuales.

| Enfoque | Idea principal |
|--------|----------------|
| Imperativo | Indico paso a paso cómo cambiar la interfaz |
| Declarativo | Describo qué interfaz debe verse según el estado |

```mermaid
flowchart LR
    A[Datos o estado] --> B[Descripcion de la UI]
    B --> C[Compose genera la interfaz]
```

#### 3.1. Qué significa esto en la práctica

Si el nombre de una persona usuaria cambia, en un enfoque declarativo no te
preocupas primero de “buscar el control y modificarlo”. Lo importante es que el
valor cambie y que la interfaz se vuelva a describir con ese nuevo dato.

Ese proceso de actualización lo veremos con más detalle en `7.5.2`, pero ya
conviene quedarse con la idea general.

### 4. Qué necesitas para seguir los ejemplos

Los ejemplos de este tema asumen un proyecto Android con Compose ya preparado
en Android Studio.

También conviene recordar tres detalles:

- muchas funciones del ejemplo pertenecen al SDK de Compose y no las escribes tú;
- algunos fragmentos omiten imports para centrar la atención en la idea principal;
- cuando aparezcan patrones como `by`, `remember` o `mutableStateOf`, los
  explicaremos con más calma en el siguiente apartado.

### 5. El concepto de `@Composable`

La base de Compose son las funciones anotadas con `@Composable`. Una función de
este tipo describe un fragmento de interfaz.

```kotlin
@Composable
fun Saludo(nombre: String) {
    Text(text = "Hola, $nombre")
}
```

En este ejemplo:

- `Saludo()` es un componente propio;
- recibe un dato mediante parámetros;
- usa `Text()` para mostrar contenido;
- puede reutilizarse en distintas pantallas.

!!! definition "Composable"
    Una función composable describe una parte de la interfaz y puede combinarse con otras para construir pantallas más complejas.

#### 5.1. Reglas prácticas

- Las composables suelen comenzar por mayúscula inicial porque actúan como componentes.
- Reciben datos mediante parámetros, igual que otras funciones Kotlin.
- Se llaman desde otras composables o desde el punto de entrada de la UI.
- Conviene que sean pequeñas y fáciles de reutilizar.

### 6. Punto de entrada: `setContent`

En Android, una pantalla Compose suele cargarse dentro de `setContent`.

```kotlin
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                Saludo(nombre = "Clase")
            }
        }
    }
}
```

Este fragmento enseña una idea importante: dentro de `setContent` describimos
la interfaz que queremos mostrar.

No necesitas memorizar cada clase del ejemplo en este momento. Lo importante es
entender el papel de cada parte:

- `ComponentActivity` es el contenedor Android;
- `setContent` es el punto donde arranca la UI Compose;
- `MaterialTheme` aplica un tema visual;
- `Saludo(...)` es nuestro componente.

### 7. Vista previa con `@Preview`

Una de las ventajas más prácticas de Compose es la posibilidad de previsualizar
componentes en Android Studio sin ejecutar toda la aplicación.

```kotlin
@Preview(showBackground = true)
@Composable
fun SaludoPreview() {
    MaterialTheme {
        Saludo(nombre = "Clase")
    }
}
```

Esto resulta muy útil para comprobar:

- si la estructura visual tiene sentido;
- si el texto cabe correctamente;
- si los espacios y tamaños son razonables;
- si una pantalla se entiende antes de ejecutarla en un dispositivo.

### 8. Primeros componentes básicos

En Compose existen muchos componentes, pero para empezar bastan unos pocos:

- `Text()` para mostrar texto;
- `Button()` para lanzar acciones;
- `TextField()` para introducir datos;
- `Row`, `Column` y `Box` para distribuir contenido.

#### 8.1. Mostrar texto

```kotlin
@Composable
fun EtiquetaModulo() {
    Text(text = "Programacion")
}
```

`Text()` es uno de los componentes más sencillos y más utilizados. Recibe, como
mínimo, el texto que debe mostrarse. Otros parámetros permiten cambiar color,
tamaño o estilo, aunque eso lo usaremos de forma progresiva.

#### 8.2. Un botón sencillo

```kotlin
@Composable
fun AccionSimple() {
    Button(onClick = { /* accion */ }) {
        Text("Aceptar")
    }
}
```

Aquí aparece por primera vez `onClick`, que es el bloque de código que se
ejecutará cuando se pulse el botón. En este tema lo importante es reconocer la
estructura; en `7.5.2` veremos cómo conectar ese evento con el estado de la
pantalla.

### 9. `Modifier`: tamaño, espacio y comportamiento

Muchos componentes de Compose aceptan un parámetro llamado `modifier`. Este
parámetro sirve para ajustar cómo se representa o se comporta el componente.

```kotlin
@Composable
fun EtiquetaDestacada() {
    Text(
        text = "Kotlin + Compose",
        modifier = Modifier
            .fillMaxWidth()
            .padding(16.dp)
    )
}
```

Con `Modifier` es habitual encadenar operaciones como estas:

- `padding(...)` para añadir espacio interior o separación aplicada al contenido;
- `fillMaxWidth()` para ocupar el ancho disponible;
- `fillMaxSize()` para ocupar todo el espacio disponible;
- `size(...)` para fijar tamaño;
- `clickable { ... }` para reaccionar a pulsaciones.

!!! warning "Precisión importante"
    En Compose, `padding` no debe explicarse como si fuera exactamente el mismo concepto que el margen en CSS. Sirve para gestionar espacio, pero no conviene mezclar modelos mentales sin matices.

#### 9.1. El orden importa

El orden de los modificadores puede cambiar el resultado final. Por eso no se
trata de “añadir adornos” al final del componente, sino de construir su
comportamiento visual paso a paso.

### 10. Contenedores básicos

Además de controles sueltos, una interfaz necesita organizar contenido.

#### 10.1. `Column`

Coloca los elementos en vertical.

```kotlin
@Composable
fun PanelVertical() {
    Column(modifier = Modifier.padding(16.dp)) {
        Text("Nombre")
        TextField(value = "", onValueChange = {})
        Button(onClick = {}) {
            Text("Guardar")
        }
    }
}
```

#### 10.2. `Row`

Coloca los elementos en horizontal.

```kotlin
@Composable
fun AccionesFila() {
    Row {
        Button(onClick = {}) { Text("Aceptar") }
        Button(onClick = {}) { Text("Cancelar") }
    }
}
```

#### 10.3. `Box`

`Box` actúa como un contenedor flexible. Puede usarse para superponer contenido
o para posicionarlo dentro de una zona concreta.

```kotlin
@Composable
fun CajaSimple() {
    Box(modifier = Modifier.size(120.dp)) {
        Text("Contenido")
    }
}
```

Este ejemplo **no centra automáticamente** el texto. Si quisiéramos centrarlo,
haría falta indicarlo de forma explícita. Lo importante ahora es entender que
`Box` sirve como contenedor libre, no como centrador automático.

### 11. Qué debes saber antes de pasar al siguiente apartado

Si has entendido este tema, ya deberías poder explicar con tus palabras:

- qué es Jetpack Compose;
- qué significa programar una UI de forma declarativa;
- qué hace una función `@Composable`;
- para qué sirven `setContent`, `@Preview` y `Modifier`;
- cómo se organizan componentes básicos en una pantalla.

### 12. Mini actividad

Como práctica rápida, intenta diseñar una pantalla sencilla con:

- un título;
- un `TextField`;
- dos botones en la misma fila;
- un bloque de texto final.

De momento no hace falta que funcione del todo. El objetivo es reconocer la
estructura y practicar con `Column`, `Row`, `Text`, `TextField`, `Button` y
`Modifier`.

### 13. Conclusión

Jetpack Compose permite construir interfaces gráficas en Android con una forma
de trabajo más directa y más coherente con Kotlin. Pero la idea realmente
importante no es memorizar nombres de componentes, sino entender que la
interfaz se expresa como código declarativo y se compone a partir de bloques
reutilizables.

En el siguiente apartado daremos el paso clave: conectar esos componentes con
**estado** y **eventos** para que la interfaz responda de verdad a la persona
usuaria.

### 14. Siguiente paso

Continúa con [7.5.2 Jetpack Compose: estado, eventos y maquetación](/prog/unidad7/7.5.2).
