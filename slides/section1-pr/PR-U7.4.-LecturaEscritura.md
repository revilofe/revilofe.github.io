# PR-U7.4 - Lectura y escritura de archivos

Note: En esta presentación damos el salto desde las **rutas** al **contenido** de los ficheros, que es donde la persistencia empieza a verse de verdad en un programa. Quiero que el alumnado entienda cómo leer y escribir datos de forma consciente, diferenciando **texto**, **binario**, acceso **secuencial** y varias decisiones prácticas que afectan al diseño del programa.

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

Note: Este tema es el núcleo práctico de la unidad 7 porque aquí el programa empieza a **guardar** y **recuperar información** de verdad. Todo lo que veamos va a servir después para construir logs, cargar configuraciones, escribir informes y, en general, tratar la **persistencia** como una parte natural del desarrollo.

---

## Índice

Note: En esta presentación damos el paso desde las **rutas** hasta los **contenidos** de los ficheros. La idea central es que ya no basta con saber dónde está un archivo: ahora necesitamos entender cómo se **lee**, cómo se **escribe** y qué decisiones conviene tomar según el tipo de dato y el formato elegido.


### Índice I

- 1. Por qué leer y escribir archivos
- 2. Texto y binario
- 3. Acceso secuencial
- 4. Leer ficheros de texto
- 5. Escribir ficheros de texto

Note: La primera mitad del tema explica el problema general: por qué necesitamos **persistencia**, qué diferencia hay entre **texto** y **binario** y qué operaciones de **lectura** aparecen con más frecuencia en Kotlin. Es la parte que construye el mapa mental antes de ir a métodos concretos.


### Índice II

- 6. Leer y escribir no es lo mismo
- 7. Errores frecuentes al trabajar con texto
- 8. Introducción a los ficheros binarios
- 9. Ejemplo integrador
- 10. Relación con `7.4.1` y resumen

Note: La segunda mitad baja a decisiones mucho más prácticas: mantener coherencia entre **cómo se escribe** y **cómo se lee**, anticipar errores frecuentes y entender por qué el trabajo en **binario** exige todavía más disciplina con el formato.

---

## 1. ¿Por que leer y escribir archivos?

Note: Empezamos conectando el tema con la **persistencia**. La memoria sirve mientras el programa se está ejecutando, pero si queremos conservar datos entre ejecuciones necesitamos un soporte externo, y ahí es donde entran los **ficheros** como mecanismo básico de almacenamiento.


### 1.1. Almacenar y recuperar informacion

- Los ficheros permiten conservar datos entre sesiones
- También permiten compartir datos con otros programas
- Leer significa traer datos al programa
- Escribir significa enviarlos al fichero

Note: Conviene presentar **lectura** y **escritura** como dos direcciones opuestas de un mismo **flujo de datos**. Leer significa traer información al programa, y escribir significa enviarla fuera; si esta idea queda clara, luego se entienden mejor los métodos concretos de Kotlin.


### 1.2. Casos de uso habituales

- Guardar notas o pedidos
- Registrar eventos y errores
- Cargar configuraciones al arrancar
- Exportar resultados a un informe

Note: Estos ejemplos son importantes porque conectan la teoría con usos reales: **guardar pedidos**, **registrar eventos**, **cargar configuraciones** o **exportar informes**. Así el alumnado ve que trabajar con ficheros no es un tema artificial, sino una necesidad muy habitual en programas reales.

---

## 2. Texto y binario

Note: Antes de hablar de métodos concretos, hay que distinguir muy bien qué tipo de **contenido** estamos almacenando. No es lo mismo guardar **texto legible** que guardar **bytes** de una imagen, y esa diferencia condiciona tanto la API como la forma de pensar el problema.


### 2.1. Ficheros de texto

- Guardan caracteres legibles con un editor
- Son comunes en configuraciones, CSV, logs e informes

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

Note: El **texto** es muy didáctico porque permite ver directamente qué se ha guardado y comprobar el resultado con un editor sencillo. Por eso será el caso más trabajado en el aula: hace visible la persistencia y facilita que el alumnado conecte código y resultado.


### 2.2. Ficheros binarios

- Guardan bytes no legibles a simple vista
- Son frecuentes en imágenes, audio o datos compactos
- No son peores ni mejores: responden a otra necesidad

Note: La idea importante aquí es evitar el juicio simplista de que **texto** es bueno y **binario** es malo. Cada formato responde a necesidades distintas, y lo que queremos es que el alumnado aprenda a elegir según el **contexto**, no por costumbre.

---

## 3. Acceso secuencial

Note: El **acceso secuencial** es el modelo principal de esta unidad porque conecta muy bien con la intuición de leer línea a línea o dato a dato desde el principio hasta el final. Es un modelo muy natural para empezar y el que mejor prepara el trabajo con ficheros de texto.


### 3.1. Procesar en orden

- Se trabaja desde el principio hasta el final
- Es parecido a leer líneas en consola
- Es el caso más habitual en esta unidad

Note: Esta slide prepara el terreno para métodos como **`readLines()`** o **`useLines()`**, que encajan precisamente en ese enfoque **secuencial**. Quiero que el alumnado vea que la teoría del acceso no está separada de la API, sino que explica por qué ciertos métodos tienen sentido.

---

## 4. Leer ficheros de texto

Note: Kotlin ofrece varias opciones muy cómodas para leer ficheros, pero no conviene enseñarlas como si fueran intercambiables sin más. La elección depende del **tamaño del fichero**, del tipo de **procesamiento** y de si necesitamos todo el contenido de golpe o preferimos ir línea a línea.


### 4.1. `readText()` y `readLines()`

- `readText()` devuelve todo el contenido como una cadena
- `readLines()` devuelve una lista de líneas

```kotlin
val contenido = File("datos/notas.txt").readText()
val lineas = File("datos/notas.txt").readLines()
```

Note: La diferencia clave aquí está en el **formato del resultado**: una única **cadena** completa o una **colección de líneas** lista para recorrer. Esa diferencia parece pequeña, pero cambia bastante la manera en la que luego procesamos la información.


### 4.2. `useLines()` para procesar mejor

- Permite trabajar línea a línea
- Evita cargar todo en memoria de golpe
- Es útil cuando el fichero puede ser grande

```kotlin
File("datos/notas.txt").useLines { lineas ->
    lineas.forEach { println(it) }
}
```

Note: Aquí conviene explicar que "más **eficiente**" no significa automáticamente "mejor" en todos los casos. **`useLines()`** es muy útil cuando no queremos cargarlo todo en memoria, pero la decisión correcta depende siempre del tamaño del fichero y de la tarea concreta que queramos resolver.

---

## 5. Escribir ficheros de texto

Note: La **escritura** obliga a tomar una decisión muy importante desde el principio: si vamos a **sobrescribir** lo que ya había o si vamos a **añadir** contenido al final. Muchísimos errores vienen precisamente de no pensar esta diferencia antes de elegir el método.


### 5.1. `writeText()` y `appendText()`

- `writeText()` reemplaza el contenido previo
- `appendText()` añade al final

```kotlin
File("salida.txt").writeText("Hola desde Kotlin\n")
File("log.txt").appendText("Nueva entrada\n")
```

Note: Este contraste es uno de los puntos más importantes de todo el tema. Si usamos **`writeText()`** cuando en realidad queríamos conservar lo anterior, perderemos datos; por eso es importante remarcar muy bien cuándo conviene **reemplazar** y cuándo conviene **acumular** con **`appendText()`**.


### 5.2. Escritura con `bufferedWriter()`

- Permite escribir varias líneas con un escritor explícito
- `use()` ayuda a cerrar correctamente el recurso

```kotlin
File("salida.txt").bufferedWriter().use { writer ->
    writer.write("Primera linea\n")
    writer.write("Segunda linea\n")
}
```

Note: Aquí conviene introducir la idea de **gestionar recursos** con cuidado. Aunque Kotlin simplifique mucho la **E/S**, sigue siendo importante cerrar bien los flujos y escritores, y por eso **`use()`** es una herramienta tan valiosa: evita olvidos y hace el código más seguro.

---

## 6. Leer y escribir no es lo mismo

Note: Esta sección parece obvia, pero didácticamente es fundamental. Guardar información con un **formato** y luego intentar leerla con otro distinto rompe el programa, así que aquí quiero insistir mucho en la idea de **coherencia** entre escritura y lectura.


### 6.1. Coherencia entre escritura y lectura

- Al escribir decides cómo se organiza la información
- Al leer debes respetar ese formato
- Si no hay coherencia, los datos se interpretan mal

```text
Ana,8.5
Luis,7.25
```

Note: Este ejemplo simple de **CSV** ayuda mucho a visualizar que una coma, un separador o un salto de línea también forman parte del **formato**. No son "decoración": son la estructura que después el programa tendrá que interpretar correctamente al leer.

---

## 7. Errores frecuentes al trabajar con texto

Note: Enumerar **errores frecuentes** ayuda a que el alumnado anticipe fallos antes de encontrárselos por sorpresa en ejecución. Es una parte muy útil del aprendizaje porque enseña a pensar con más prudencia y a desconfiar sanamente de rutas, formatos y contenidos.


### 7.1. Lista de fallos habituales

- Intentar leer un fichero que no existe
- Sobrescribir datos sin querer
- No respetar el formato esperado
- Cargar en memoria más de lo necesario
- Suponer que el contenido siempre es válido

Note: Aquí conviene insistir en una idea de calidad muy importante: trabajar con ficheros implica una **desconfianza saludable**. Debemos comprobar **rutas**, validar **formatos** y no suponer que el **contenido** siempre es correcto o está en el estado esperado.

---

## 8. Introduccion a los ficheros binarios

Note: Aunque el foco principal del aula va a ser el **texto**, el alumnado debe reconocer que la JVM también ofrece herramientas para trabajar con **binario**. No lo veremos con tanto detalle, pero sí conviene que entiendan que existe otro nivel de persistencia más estricto con el formato.


### 8.1. `DataOutputStream` y `DataInputStream`

- Sirven para escribir y leer datos binarios tipados
- Hay que mantener el mismo orden y los mismos tipos

```kotlin
DataOutputStream(FileOutputStream("datos.bin")).use { salida ->
    salida.writeInt(25)
    salida.writeBoolean(true)
}
```

Note: Este ejemplo abre la puerta al trabajo en **binario**, pero lo importante no es memorizar la clase sino la **regla**: si escribes primero un **`Int`** y luego un **`Boolean`**, deberás leer exactamente en ese mismo orden y con esos mismos tipos para no romper la interpretación.


### 8.2. Regla esencial del binario

- Cambiar el orden rompe la interpretación
- Cambiar el tipo también la rompe
- El contrato de lectura y escritura debe coincidir

Note: Esta slide merece enfatizarse especialmente porque en **binario** hay muchas menos pistas visuales que en **texto**. Precisamente por eso la disciplina con el **formato**, el **orden** y los **tipos** es todavía más importante y hay menos margen para improvisar.

---

## 9. Ejemplo integrador

Note: Cerramos con un caso integrador que escribe en un fichero de **texto** y luego vuelve a leerlo. Es un ejemplo muy útil porque resume el núcleo práctico del tema y hace visible la idea de ida y vuelta entre **programa**, **fichero** y **consola**.


### 9.1. Escribir y volver a leer

```kotlin
val fichero = File("pedidos.txt")
fichero.appendText("Portatil,2\n")
fichero.appendText("Raton,5\n")

val lineas = fichero.readLines()
for (linea in lineas) {
    println(linea)
}
```

- Usa `appendText()` para conservar lo anterior
- Recupera el contenido con `readLines()`
- Muestra el puente entre persistencia y consola

Note: Este tipo de ejemplo deja claro que la **E/S** no es un mundo aparte ni una colección de trucos sueltos. **Teclado**, **consola** y **archivos** pueden colaborar dentro del mismo programa, y esa visión unificada es justo la que interesa que el alumnado consolide.

---

## 10. Relacion con `7.4.1` y resumen

Note: Cerramos marcando continuidad entre temas. Este bloque ofrece la visión general de la **lectura** y la **escritura**, y el siguiente profundiza en el caso más habitual y más didáctico: el trabajo con **ficheros de texto**.


### 10.1. Ideas clave para continuar

- `7.4` da la vista general de lectura y escritura
- `7.4.1` profundiza en ficheros de texto
- Kotlin facilita lectura con `readText()`, `readLines()` y `useLines()`
- Y facilita escritura con `writeText()` y `appendText()`

Note: Si estas ideas quedan claras, el alumnado ya puede empezar a construir programas que **guarden** y **recuperen información** de forma persistente. La idea final que debe quedar es mantener siempre la coherencia entre **cómo se escribe** un fichero, **qué formato se elige** y **cómo se vuelve a leer** después.
