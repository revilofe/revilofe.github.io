# U1.1 - Mi primer programa

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice 1

- U1.1 - Mi primer programa
- 1. La Programación
    - Definición
    - Ciclo de Vida de un Programa
- 2. El Ordenador
    - ¿Qué es un ordenador?


## Índice 2

- 2. El Ordenador
    - Estructura de Von Neumann
- 3. ¿Qué es un Programa o Software?
    - Definición de Software
    - Tipos de Software
- 4. Relación Hardware - Software


## Índice 3

- 4. Relación Hardware - Software
    - Hardware y Software
    - Elementos principales
- 5. Algoritmos
    - Definición de Algoritmo
    - Ejemplo de Algoritmo (Pseudocódigo)


## Índice 4

- 5. Algoritmos
    - Diagramas de Flujo
- 6. Lenguajes de Programación
    - Definición
    - Clasificación y Usos


## Índice 5

- Cierre de la Unidad
    - Resumen
    - Preguntas para Reflexionar
---

## 1. La Programación


### Definición

* Proceso de crear programas para resolver problemas o automatizar tareas.
* Usa lenguajes de programación para dar instrucciones a un dispositivo.
* Requiere un traductor (compilador/intérprete) para convertir a lenguaje máquina.
* Lenguaje máquina: único que entiende la CPU.
* Microprocesadores ejecutan estas instrucciones de forma secuencial.

Note: Explica qué significa programar: transformar ideas en instrucciones ejecutables.
Recalca que necesitamos un lenguaje intermedio porque la máquina solo entiende ceros y unos.
Introduce la noción de traductor (compilador o intérprete).


### Ciclo de Vida de un Programa

* Comprender el problema.
* Recopilar requisitos.
* Planificar la solución.
* Diseñar el programa.
* Programar (codificar).
* Probar el programa.
* Desplegarlo para su uso.
* Mantener y mejorar el software.

Note: Recorre cada fase del ciclo de vida. Usa ejemplos simples: crear una calculadora
o una app de notas. Destaca que la programación no es solo "picar código".

---

## 2. El Ordenador


### ¿Qué es un ordenador?

* Máquina electrónica que procesa información.
* Puede ser digital o analógica.
* Ejecuta programas para resolver problemas lógicos o matemáticos.
* Posee memoria y métodos de tratamiento de datos.
* Realiza operaciones siguiendo instrucciones.

Note: Señala que un ordenador no es solo un PC: también un móvil, consola o tablet.
Lo importante es que ejecuta programas y procesa datos.


### Estructura de Von Neumann

* Modelo clásico de funcionamiento del ordenador.
* Partes principales: CPU, memoria, dispositivos de entrada/salida.
* CPU ejecuta instrucciones de memoria.
* Memoria RAM almacena datos e instrucciones temporalmente.
* Discos y periféricos aportan almacenamiento y comunicación.

Note: Explica con la figura de Von Neumann. Subraya que este modelo sigue vigente
hoy en día. Usa ejemplos: teclado (entrada), monitor (salida), disco duro (almacenamiento).

---

## 3. ¿Qué es un Programa o Software?


### Definición de Software

* Conjunto de programas, datos y documentación.
* Da instrucciones al hardware sobre qué hacer y cómo.
* Permite realizar tareas específicas en dispositivos.
* Incluye desde sistemas operativos hasta aplicaciones.
* IEEE: software = programas + procedimientos + datos asociados.

Note: Destaca que el software no son solo “apps”. Incluye drivers, documentación,
instrucciones para hardware. Usa ejemplos de software cotidiano (Word, Chrome, antivirus).


### Tipos de Software

* **De sistema**: sistema operativo, drivers.
* **De aplicación**: navegadores, ofimática, juegos.
* **De desarrollo**: compiladores, editores, depuradores.
* Todos cooperan entre sí.
* Los drivers permiten que el hardware funcione correctamente.

Note: Explica cada tipo con ejemplos: Windows (sistema), WhatsApp (aplicación),
IntelliJ IDEA (desarrollo). Haz hincapié en la importancia de los drivers.

---

## 4. Relación Hardware - Software


### Hardware y Software

* Hardware: parte física del ordenador.  
* Software: conjunto de instrucciones que dirigen al hardware.  
* Ambos se necesitan mutuamente.  
* Hardware sin software: máquina inerte.  
* Software sin hardware: no puede ejecutarse.  

Note: Haz ver que uno no existe sin el otro. Da ejemplos: un móvil sin apps, 
o una app sin dispositivo físico.


### Elementos principales

* **Disco duro**: guarda programas y datos de forma permanente.  
* **Memoria RAM**: almacén temporal de programas y datos en uso.  
* **CPU**: ejecuta instrucciones y coordina el sistema.  
* **Entrada/Salida (E/S)**: teclado, ratón, pantalla, impresora.  
* Disco duro también se considera periférico de E/S.  

Note: Usa la analogía de una oficina: disco duro como archivo, RAM como mesa de trabajo, 
CPU como trabajador y periféricos como comunicación con el exterior.

---

## 5. Algoritmos


### Definición de Algoritmo

* Secuencia de pasos lógicos para resolver un problema.  
* Es independiente del lenguaje de programación.  
* Primero se diseña el algoritmo, luego se codifica.  
* Todo algoritmo debe ser: preciso, definido y finito.  
* Base fundamental de la programación.  

Note: Insiste en que programar no es solo escribir en Kotlin, 
sino aprender a pensar en algoritmos. Usa ejemplos cotidianos: 
receta de cocina, instrucciones para armar un mueble.


### Ejemplo de Algoritmo (Pseudocódigo)

```text
Si la lámpara funciona entonces
    fin. # programa termina
Si no
    Si NO está enchufada entonces
        Enchufar.
    Si el foco está quemado entonces
        Reemplazar foco.
    Si sigue sin funcionar entonces
        Comprar nueva lámpara.
fin.
````

Note: Explica qué significa cada condición. Señala que el pseudocódigo
se parece a lenguaje humano, pero estructurado.


### Diagramas de Flujo

* Representación gráfica de un algoritmo.
* Óvalos: inicio y fin.
* Rectángulos: acciones o procesos.
* Rombos: decisiones (sí/no).
* Flechas: orden de ejecución.
* Claros y visuales para entender procesos.

Note: Muestra el diagrama de flujo de la lámpara.
Explica que ayuda a visualizar decisiones y caminos alternativos.

---

## 6. Lenguajes de Programación


### Definición

* Lenguajes formales con reglas estrictas.
* Permiten expresar algoritmos en código ejecutable.
* Controlan flujo de ejecución y manipulan datos.
* Ejemplos: Python, Java, C, Kotlin, JavaScript.
* Traducidos a lenguaje máquina mediante compiladores o intérpretes.

Note: Diferencia entre lenguaje natural y lenguaje formal.
Da ejemplos de sintaxis: Python vs Kotlin.


### Clasificación y Usos

* Multiplataforma: Kotlin, Java, C#.
* Desarrollo web: JavaScript, PHP, Python.
* Sistemas operativos: C, C++.
* Ciencia de datos: Python, R.
* Cada lenguaje tiene fortalezas y contextos ideales.

Note: Relaciona con encuestas de popularidad (TIOBE, StackOverflow).
Pregunta a los alumnos qué lenguajes conocen y cuáles les gustaría aprender.

---

## Cierre de la Unidad


### Resumen

* Programar = transformar problemas en soluciones ejecutables.
* Ordenadores siguen el modelo de Von Neumann.
* Software guía al hardware en las tareas.
* Algoritmos = base de la programación.
* Pseudocódigo y diagramas ayudan a planificar.
* Lenguajes formales convierten algoritmos en programas.

Note: Haz un repaso global. Conecta los puntos: problema → algoritmo → programa.
Resalta que esta es la base antes de escribir el primer código en Kotlin o Python.


### Preguntas para Reflexionar

* ¿Qué lenguajes de programación conoces?
* ¿Cuál te resulta más interesante y por qué?
* ¿Qué ventajas tiene escribir pseudocódigo antes de programar?
* ¿Cómo ayuda un diagrama de flujo a entender un problema?
* ¿Crees que hardware y software podrían existir uno sin otro?

Note: Lanza las preguntas al grupo. Promueve debate abierto.
El objetivo es comprobar comprensión y motivar curiosidad.
Invita a que los alumnos compartan ejemplos cotidianos de algoritmos.

---

# Dudas
![](./assets/IS-U011-Presentacion4.png)

Note: Abre el espacio para preguntas. Anima a los alumnos a expresar dudas o compartir ideas.

---

## ¡Gracias por su atención!

![](./assets/Fin.png) <!-- .element height="50%" width="50%" -->

Note: Finaliza la presentación invitando a preguntas y aclaraciones. Refuerza que la relación entre hardware y software es fundamental para comprender cómo funciona un ordenador y que este conocimiento será la base de temas más avanzados en programación y sistemas.

---

