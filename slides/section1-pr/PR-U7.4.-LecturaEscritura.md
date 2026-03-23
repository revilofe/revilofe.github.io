# PR-U7.4 - Lectura y escritura de archivos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

Note: En esta presentación damos el paso desde las rutas a los **contenidos**.
El objetivo es entender cómo leer y escribir información persistente en
ficheros, diferenciando texto, binario y buenas prácticas básicas.


### Índice I

- 1. Por qué leer y escribir archivos
- 2. Texto y binario
- 3. Acceso secuencial
- 4. Leer ficheros de texto
- 5. Escribir ficheros de texto

Note: La primera mitad explica el problema general: por qué se necesitan los
ficheros, qué formatos hay y qué operaciones de lectura aparecen con más
frecuencia en Kotlin.


### Índice II

- 6. Leer y escribir no es lo mismo
- 7. Errores frecuentes al trabajar con texto
- 8. Introducción a los ficheros binarios
- 9. Ejemplo integrador
- 10. Relación con `7.4.1` y resumen

Note: La segunda mitad baja a decisiones prácticas: coherencia entre escritura
y lectura, errores típicos y un primer vistazo al trabajo binario.

---

## 1. ¿Por que leer y escribir archivos?

Note: Empezamos conectando el tema con la persistencia. La memoria no basta si
queremos conservar datos entre ejecuciones del programa.


### 1.1. Almacenar y recuperar informacion

- Los ficheros permiten conservar datos entre sesiones
- También permiten compartir datos con otros programas
- Leer significa traer datos al programa
- Escribir significa enviarlos al fichero

Note: Conviene presentar lectura y escritura como dos direcciones opuestas del
flujo de datos. Esto aclara mucho el resto del tema.


### 1.2. Casos de uso habituales

- Guardar notas o pedidos
- Registrar eventos y errores
- Cargar configuraciones al arrancar
- Exportar resultados a un informe

Note: Estos ejemplos conectan la teoría con aplicaciones reales y justifican
por qué el criterio RA5 pide trabajar con ficheros.

---

## 2. Texto y binario

Note: Antes de hablar de métodos concretos, hay que distinguir qué tipo de
contenido estamos almacenando.


### 2.1. Ficheros de texto

- Guardan caracteres legibles con un editor
- Son comunes en configuraciones, CSV, logs e informes

```text
Ana,8.5
Luis,7.25
Marta,9.0
```

Note: El texto es muy didáctico porque permite ver directamente qué se ha
guardado. Por eso será el caso más trabajado en el aula.


### 2.2. Ficheros binarios

- Guardan bytes no legibles a simple vista
- Son frecuentes en imágenes, audio o datos compactos
- No son peores ni mejores: responden a otra necesidad

Note: La idea importante es evitar el juicio "texto bueno, binario malo". Cada
formato tiene su contexto y sus ventajas.

---

## 3. Acceso secuencial

Note: El acceso secuencial es el modelo principal de la unidad y conecta muy
bien con la intuición que ya tenemos de leer línea a línea.


### 3.1. Procesar en orden

- Se trabaja desde el principio hasta el final
- Es parecido a leer líneas en consola
- Es el caso más habitual en esta unidad

Note: Esta slide prepara el terreno para métodos como `readLines()` o
`useLines()`, que encajan justamente en ese modelo secuencial.

---

## 4. Leer ficheros de texto

Note: Kotlin ofrece varias opciones cómodas. La elección depende del tamaño del
fichero y del tipo de procesamiento que queremos hacer.


### 4.1. `readText()` y `readLines()`

- `readText()` devuelve todo el contenido como una cadena
- `readLines()` devuelve una lista de líneas

```kotlin
val contenido = File("datos/notas.txt").readText()
val lineas = File("datos/notas.txt").readLines()
```

Note: La diferencia clave es el formato del resultado: una única cadena o una
colección de líneas listas para recorrer.


### 4.2. `useLines()` para procesar mejor

- Permite trabajar línea a línea
- Evita cargar todo en memoria de golpe
- Es útil cuando el fichero puede ser grande

```kotlin
File("datos/notas.txt").useLines { lineas ->
    lineas.forEach { println(it) }
}
```

Note: Aquí es importante explicar que "más eficiente" no siempre significa
"mejor en todos los casos". Depende del tamaño del fichero y de la tarea.

---

## 5. Escribir ficheros de texto

Note: La escritura requiere una decisión clave: sobrescribir lo existente o
añadir contenido al final.


### 5.1. `writeText()` y `appendText()`

- `writeText()` reemplaza el contenido previo
- `appendText()` añade al final

```kotlin
File("salida.txt").writeText("Hola desde Kotlin\n")
File("log.txt").appendText("Nueva entrada\n")
```

Note: Este contraste es uno de los puntos más importantes del tema. Muchísimos
errores vienen de usar `writeText()` cuando en realidad se quería conservar lo
anterior.


### 5.2. Escritura con `bufferedWriter()`

- Permite escribir varias líneas con un escritor explícito
- `use()` ayuda a cerrar correctamente el recurso

```kotlin
File("salida.txt").bufferedWriter().use { writer ->
    writer.write("Primera linea\n")
    writer.write("Segunda linea\n")
}
```

Note: Aquí conviene introducir la idea de gestionar bien los recursos. Aunque
Kotlin facilite mucho la E/S, cerrar correctamente sigue siendo importante.

---

## 6. Leer y escribir no es lo mismo

Note: Esta sección parece obvia, pero didácticamente es fundamental: guardar un
formato y luego leer otro distinto rompe el programa.


### 6.1. Coherencia entre escritura y lectura

- Al escribir decides cómo se organiza la información
- Al leer debes respetar ese formato
- Si no hay coherencia, los datos se interpretan mal

```text
Ana,8.5
Luis,7.25
```

Note: Este ejemplo simple de CSV ayuda a visualizar que una coma o un salto de
línea también forman parte del formato que luego habrá que interpretar.

---

## 7. Errores frecuentes al trabajar con texto

Note: Enumerar errores típicos ayuda a que el alumnado anticipe fallos antes de
verlos en ejecución.


### 7.1. Lista de fallos habituales

- Intentar leer un fichero que no existe
- Sobrescribir datos sin querer
- No respetar el formato esperado
- Cargar en memoria más de lo necesario
- Suponer que el contenido siempre es válido

Note: Aquí conviene insistir en que trabajar con ficheros implica una cierta
desconfianza saludable: rutas, formato y contenido deben comprobarse.

---

## 8. Introduccion a los ficheros binarios

Note: No es el foco principal del aula, pero el alumnado debe reconocer que la
JVM también ofrece herramientas para escribir y leer datos binarios.


### 8.1. `DataOutputStream` y `DataInputStream`

- Sirven para escribir y leer datos binarios tipados
- Hay que mantener el mismo orden y los mismos tipos

```kotlin
DataOutputStream(FileOutputStream("datos.bin")).use { salida ->
    salida.writeInt(25)
    salida.writeBoolean(true)
}
```

Note: Este ejemplo abre la puerta al binario, pero lo importante es la regla:
si escribes un `Int` y luego un `Boolean`, deberás leer exactamente eso mismo.


### 8.2. Regla esencial del binario

- Cambiar el orden rompe la interpretación
- Cambiar el tipo también la rompe
- El contrato de lectura y escritura debe coincidir

Note: Esta slide merece enfatizarse. En binario hay menos pistas visuales, así
que la disciplina con el formato es aún más importante que en texto.

---

## 9. Ejemplo integrador

Note: Cerramos con un caso de fichero de texto que escribe y luego vuelve a
leer. Resume muy bien el núcleo práctico del tema.


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

Note: Este tipo de ejemplo deja claro que la E/S no es un mundo aparte:
teclado, consola y archivos pueden colaborar dentro del mismo programa.

---

## 10. Relacion con `7.4.1` y resumen

Note: Cerramos marcando continuidad. Este tema es la visión general; el
siguiente profundiza en el caso más habitual: los ficheros de texto.


### 10.1. Ideas clave para continuar

- `7.4` da la vista general de lectura y escritura
- `7.4.1` profundiza en ficheros de texto
- Kotlin facilita lectura con `readText()`, `readLines()` y `useLines()`
- Y facilita escritura con `writeText()` y `appendText()`

Note: Si estas ideas quedan claras, el alumnado ya puede empezar a construir
programas que guarden y recuperen información de forma persistente.
