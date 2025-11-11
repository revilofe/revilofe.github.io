# U3.1 - Estructuras de Datos

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice

---

## Introducción


### ¿Qué son las estructuras de datos?

* Modo de representar información en una computadora
* Tienen un comportamiento interno definido
* Se rigen por reglas y restricciones específicas
* Determinadas por su construcción interna
* Fundamentales en programación

Note: Las estructuras de datos son esenciales en programación. No solo permiten almacenar información, sino que definen cómo se puede acceder y manipular esa información. Cada estructura tiene sus propias reglas que determinan qué operaciones son posibles y eficientes.


### ¿Para qué sirven?

* Organizar información de manera eficiente
* Diseñar soluciones correctas para problemas específicos
* Trabajar en alto nivel de abstracción
* Acceder, modificar y manipular datos
* Mejorar la eficiencia del código

Note: Las estructuras de datos son la base para resolver problemas complejos de forma eficiente. Permiten al programador centrarse en la lógica del problema sin preocuparse por los detalles de bajo nivel del almacenamiento en memoria.


### Tipos de estructuras

**Comúnmente utilizadas:**
* Variables
* Arrays
* Conjuntos
* Clases

**Diseñadas para propósitos específicos:**
* Árboles
* Grafos
* Tablas

Note: No todas las estructuras son iguales. Algunas como las variables y arrays son fundamentales y se usan constantemente. Otras como árboles y grafos resuelven problemas específicos de manera muy eficiente, pero requieren más conocimiento para usarlas correctamente.

---

## Tipos de Datos


### Datos primitivos vs complejos

**Datos primitivos:**
* Enteros, flotantes, booleanos, caracteres
* Representan valores simples
* Tamaño fijo en memoria

**Datos complejos/estructurados:**
* Combinan múltiples valores
* Pueden contener datos primitivos u otros complejos
* Tamaño variable

Note: Los tipos primitivos son los bloques básicos de construcción. Los tipos complejos nos permiten modelar entidades más sofisticadas combinando múltiples valores. Por ejemplo, una fecha puede representarse con tres enteros (día, mes, año).

---

## Estructuras Estáticas


### Características

* Tamaño definido antes de la ejecución
* No se puede modificar el tamaño durante ejecución
* Ocupan memoria fija
* Ejemplo típico: **arrays**

Note: Las estructuras estáticas tienen ventajas en eficiencia porque el compilador puede optimizar el acceso a memoria. Sin embargo, su rigidez puede ser una limitación si no sabemos de antemano cuántos elementos necesitaremos.


### Arrays

* Dato estructurado para almacenar conjuntos
* **Homogéneo**: todos los elementos del mismo tipo
* **Ordenado**: posición identificable de cada elemento
* Acceso directo por índice

Note: Los arrays son fundamentales en programación. Su característica de acceso directo mediante índice los hace muy eficientes para lectura y escritura. Sin embargo, insertar o eliminar elementos en medio del array puede ser costoso.


### Tipos de arrays

**Vectores:**
* 1 fila x n columnas (vector fila)
* 1 columna x n filas (vector columna)

**Matrices:**
* m filas x n columnas
* Array bidimensional

Note: Los vectores son arrays unidimensionales, mientras que las matrices son bidimensionales. Esta estructura se puede extender a más dimensiones, creando arrays multidimensionales, útiles para representar espacios o datos tabulares complejos.

---

## Estructuras Dinámicas


### Características

* Tamaño modificable durante ejecución
* Colección de elementos (nodos)
* Se expanden y contraen según necesidad
* Mayor flexibilidad que arrays

Note: Las estructuras dinámicas son más flexibles que las estáticas. Pueden crecer o reducirse según las necesidades del programa, lo que las hace ideales cuando no sabemos de antemano cuántos elementos necesitaremos almacenar.


### Lineales vs No Lineales

**Estructuras lineales:**
* Elementos en posiciones sucesivas
* Cada elemento tiene un sucesor y un predecesor
* Relación uno a uno

**Estructuras no lineales:**
* Elementos pueden enlazarse a cualquiera
* Varios sucesores o predecesores
* Relaciones complejas

Note: La distinción entre lineales y no lineales es fundamental. Las lineales son más simples de entender y procesar secuencialmente. Las no lineales permiten modelar relaciones más complejas como jerarquías o redes.

---

## Estructuras Lineales


### Listas enlazadas

* Elementos en secuencia
* Cada elemento enlazado al siguiente
* Enlace contiene posición del siguiente
* Pueden ser simples o doblemente enlazadas

```
[Nodo1] -> [Nodo2] -> [Nodo3] -> NULL
```

Note: En listas enlazadas, cada nodo conoce la dirección del siguiente. Esto permite insertar o eliminar elementos fácilmente cambiando enlaces, sin necesidad de mover datos en memoria como en arrays.


### Listas doblemente enlazadas

<figure>
  <img src="../../docs/section1/u03/teoria/assets/PROG-U3.1.-ListaEnlazada.png" alt="Lista doblemente enlazada" width="70%"/>
  <figcaption>Estructura de datos: Lista doblemente enlazada</figcaption>
</figure>

* Dos enlaces por nodo
* Enlace al anterior y al siguiente
* Navegación bidireccional

Note: Las listas doblemente enlazadas permiten recorrer la estructura en ambas direcciones. Esto es útil para operaciones que requieren retroceder, aunque consume más memoria por los enlaces adicionales.


### Pilas (Stack)

* Tipo especial de lista lineal
* Acceso **LIFO** (Last In, First Out)
* Último en entrar, primero en salir
* Dos operaciones básicas:
    * **push**: añadir elemento
    * **pop**: retirar último elemento

Note: Las pilas son fundamentales en programación. Se usan en llamadas a funciones, deshacer/rehacer operaciones, evaluación de expresiones, navegación de páginas web (historial del navegador), entre muchos otros casos.


### Ejemplo de pila

<figure>
  <img src="../../docs/section1/u03/teoria/assets/PROG-U3.1.-Pila.png" alt="Pila" width="50%"/>
  <figcaption>Estructura de datos: Pila</figcaption>
</figure>

```
push(3) -> [3]
push(5) -> [3, 5]
push(7) -> [3, 5, 7]
pop()   -> [3, 5]    (retorna 7)
```

Note: Imagina una pila de platos: solo puedes añadir o quitar platos de la parte superior. Esta restricción, aunque parece limitante, es perfecta para muchos algoritmos y simplifica el manejo de estados temporales.


### Colas (Queue)

* Tipo especial de lista lineal
* Acceso **FIFO** (First In, First Out)
* Primero en entrar, primero en salir
* Operaciones básicas:
    * **enqueue**: añadir al final
    * **dequeue**: retirar del principio

Note: Las colas modelan situaciones de espera como impresoras, procesos del sistema operativo, gestión de tareas asíncronas, etc. El primer elemento que entra es el primero en ser procesado, como en una fila de supermercado.

---

## Estructuras No Lineales


### Características

* También llamadas **multienlazadas**
* Cada elemento puede enlazarse a cualquier otro
* Varios sucesores o predecesores posibles
* Modelan relaciones complejas

Note: Las estructuras no lineales son más potentes para representar relaciones jerárquicas o en red. Son esenciales en bases de datos, inteligencia artificial, redes sociales, sistemas de archivos y muchos otros dominios.


### Árboles

* Estructura jerárquica
* Cada elemento tiene un único antecesor
* Puede tener varios sucesores
* Tipos principales:
    * **Árbol general**: número ilimitado de hijos
    * **Árbol binario**: máximo dos hijos por nodo

Note: Los árboles son perfectos para representar jerarquías: estructura de carpetas, árbol genealógico, estructura de una empresa, HTML DOM. Los árboles binarios tienen propiedades especiales que los hacen muy eficientes para búsquedas.


### Ejemplo de árbol

<figure>
  <img src="../../docs/section1/u03/teoria/assets/PROG-U3.1.-Arbol.png" alt="Árbol" width="60%"/>
  <figcaption>Estructura de datos: Árbol</figcaption>
</figure>

* Nodo raíz
* Nodos internos
* Nodos hoja (sin hijos)
* Niveles y profundidad

Note: Un árbol tiene un nodo raíz del que parten todos los demás. Los nodos que no tienen hijos se llaman hojas. La distancia desde la raíz hasta un nodo determina su nivel. Los árboles balanceados garantizan operaciones eficientes.


### Grafos

* Estructura matemática de puntos y líneas
* **Vértices** o **nodos**: puntos
* **Aristas** o **arcos**: líneas que unen nodos
* Pueden ser dirigidos o no dirigidos
* Pueden tener ciclos

Note: Los grafos son la estructura más general y poderosa. Modelan cualquier tipo de relación: redes sociales, mapas de carreteras, dependencias entre tareas, circuitos eléctricos, etc. Son fundamentales en algoritmos de búsqueda de caminos y optimización.


### Ejemplo de grafo

<figure>
  <img src="../../docs/section1/u03/teoria/assets/PROG-U3.1.-Grafo.png" alt="Grafo" width="60%"/>
  <figcaption>Estructura de datos: Grafo</figcaption>
</figure>

* Nodos conectados por aristas
* Relaciones entre elementos
* Aplicaciones: redes, mapas, relaciones

Note: En un grafo, a diferencia de un árbol, puede haber ciclos y múltiples caminos entre dos nodos. Esto permite modelar situaciones más complejas como redes de transporte donde hay varias rutas posibles entre dos puntos.

---

## Resumen


### Clasificación general

**Por tamaño:**
* Estáticas (tamaño fijo)
* Dinámicas (tamaño variable)

**Por organización:**
* Lineales (secuencial)
* No lineales (jerárquica/red)

Note: Elegir la estructura correcta es crucial para la eficiencia. Las estáticas son más rápidas pero inflexibles. Las dinámicas son flexibles pero requieren más gestión. Las lineales son simples, las no lineales más potentes pero complejas.


### Importancia

* Fundamentales en programación
* Mejoran eficiencia del código
* Permiten resolver problemas complejos
* Base para algoritmos avanzados
* Esenciales en entrevistas técnicas

Note: Dominar las estructuras de datos es lo que diferencia a un programador principiante de uno experto. Permite no solo resolver problemas, sino hacerlo de la forma más eficiente posible. Son la base sobre la que se construyen todos los algoritmos importantes.


### Próximos pasos

* Profundizar en cada estructura
* Estudiar implementaciones específicas
* Analizar complejidad temporal y espacial
* Practicar con problemas reales
* Comparar estructuras para casos de uso

Note: Este es solo el comienzo. En las siguientes lecciones veremos implementaciones concretas en Python y otros lenguajes, analizaremos cuándo usar cada estructura, y practicaremos con problemas reales que requieren elegir la estructura de datos adecuada.

---

## Conclusión

Las estructuras de datos son herramientas esenciales que nos permiten organizar y manipular información de manera eficiente, siendo la base para construir soluciones elegantes a problemas complejos.

Note: Recuerda que no hay una estructura "mejor" que otra, sino estructuras más adecuadas para cada problema. La clave está en entender las características de cada una y saber cuándo aplicarlas. Con práctica, elegir la estructura correcta se vuelve intuitivo.
