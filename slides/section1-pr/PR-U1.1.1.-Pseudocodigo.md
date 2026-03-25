# UD 1 - 1.1.1 Pseudocódigo

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice 1

- Introducción al Pseudocódigo
    - Definición
- 1. Características del Pseudocódigo
    - Rasgos principales
- 2. Elementos del Pseudocódigo
    - Instrucciones básicas


## Índice 2

- 2. Elementos del Pseudocódigo
    - Más instrucciones
- 2.1 Inicio y Fin
    - Estructura básica
- 2.2 Variables
    - Concepto y uso


## Índice 3

- 2.2 Variables
    - Ejemplo con variables
- 2.3 Estructuras de Control
    - Tipos principales
- 2.3.1 Secuenciales
    - Definición


## Índice 4

- 2.3.2 Condicionales
    - Condicional simple
    - Condicional doble
    - Condicional múltiple
    - Condicionales anidados


## Índice 5

- 2.3.3 Iterativas
    - Bucle Mientras
    - Ejemplo Mientras
    - Bucle Para
    - Ejemplo Para
- Actividades y Ejercicios


## Índice 6

- Actividades y Ejercicios
    - Actividad 1 - Comparar dos números
    - Actividad 2 - Relación entre dos números
    - Actividad 3 - Serie descendente
    - Actividad 4 - Serie descendente con Para
    - Ejercicio 1 - Validar rango


## Índice 7

- Actividades y Ejercicios
    - Solución
    - Ejercicio 2 - Serie entre dos números
    - Ejercicio 3 - Ordenar tres números
- ¡Gracias por su atención!

---

## Introducción al Pseudocódigo


### Definición

* Forma de representar algoritmos de forma simple.  
* Fácilmente entendible por cualquier persona.  
* No depende de la formación en programación.  
* Lenguaje simplificado, con estructuras básicas.  
* Se basa en la programación estructurada.  

Note: Explica que el pseudocódigo es un puente entre el lenguaje humano y la codificación real. 
No es estándar ni ejecutable, pero sirve para planificar y comunicar algoritmos.

---

## 1. Características del Pseudocódigo


### Rasgos principales

* Lenguaje cercano a la programación.  
* Objetivo: algoritmos fáciles de entender.  
* Independiente del lenguaje que se usará después.  
* Usa expresiones limitadas, sin sintaxis rígida.  
* Debe comenzar en un único punto y terminar.  
* Siempre debe tener solución finita.  

Note: Recalca la importancia de la claridad y simplicidad. 
El pseudocódigo no tiene un estándar universal, pero sigue convenciones comunes.

---

## 2. Elementos del Pseudocódigo


### Instrucciones básicas

* Inicio  
* Fin  
* Escribe "texto"  
* Lee variable  
* Si … entonces …  
* Si … entonces … Sino …  
* Según valor … opciones …  

Note: Presenta los bloques básicos. Son equivalentes a lo que luego encontraremos 
en Kotlin, Python, etc. Sirven para estructurar algoritmos de forma clara.


### Más instrucciones

* Mientras (condición) hacer …  
* Para X en (1…N) hacer …  
* Operadores matemáticos: +, -, *, /, //, %  
* Operadores relacionales: ==, >, <, >=, <=, !=  
* Operadores lógicos: and, or, not  
* Asignación con el símbolo =  

Note: Explica cómo estas instrucciones permiten expresar cálculos, decisiones y bucles. 
Son la base de cualquier programa.

---

## 2.1 Inicio y Fin


### Estructura básica

* Todo algoritmo empieza con `Inicio`.  
* Todo algoritmo termina con `Fin`.  
* Delimita el bloque principal de ejecución.  
* Facilita la lectura y comprensión.  

```text
Inicio
    Escribe "¿Cómo te llamas?"
    Lee nombre
    Escribe "Hola, " + nombre
Fin
````

Note: Enseña que cualquier pseudocódigo tiene un inicio y un fin.
En medio se escriben las instrucciones. Ejemplo sencillo: un saludo personalizado.

---

## 2.2 Variables


### Concepto y uso

* Contenedores de información con nombre.
* Tipos: cadenas ("texto"), números (5, 3.2), lógicos (verdadero/falso).
* Su valor puede cambiar en el algoritmo.
* El tipo se define implícitamente al asignar.
* Concatenación con `+` para unir textos y valores.

Note: Explica que no hace falta declarar tipo. La simplicidad es clave en pseudocódigo.
Luego en programación real sí habrá que declarar o inferir tipos.


### Ejemplo con variables

```text
Inicio
    num1 = 10
    Escribe "Introduce un número: "
    Lee num2

    suma = num1 + num2
    Escribe "La suma es " + suma

    iva = 0.21
    Escribe "Introduce un precio: "
    Lee precio

    Escribe "Precio con IVA: " + (precio * iva)
Fin
```

Note: Muestra operaciones básicas. Incluye suma, lectura de datos y cálculo con IVA.
Es un ejemplo práctico y fácil de seguir.

---

## 2.3 Estructuras de Control


### Tipos principales

* Secuenciales: instrucciones en orden.  
* Condicionales: permiten tomar decisiones.  
* Iterativas: repiten un bloque de código.  
* Basadas en programación estructurada.  
* Simples y claras en pseudocódigo.  

Note: Introduce los tres tipos de estructuras de control. 
Son los bloques básicos para construir algoritmos más complejos.

---

## 2.3.1 Secuenciales


### Definición

* Ejecutan instrucciones en orden de aparición.  
* Cada instrucción ocurre tras la anterior.  
* Delimitadas entre `Inicio` y `Fin`.  
* Base de cualquier programa.  

```text
Inicio
    Instrucción1
    Instrucción2
    Instrucción3
Fin
````

Note: Explica que lo secuencial es lo más básico.
Los programas siguen pasos como una receta, de arriba abajo.

---

## 2.3.2 Condicionales


### Condicional simple

* Ejecuta un bloque solo si se cumple una condición.
* Si no se cumple, no ejecuta nada.

```text
Si (condición) entonces
    Instrucción1
    Instrucción2
Fin
```

Note: Explica que es la forma más simple de decisión.
Ejemplo: si la nota ≥ 5 entonces aprobar.


### Condicional doble

* Añade bloque alternativo si la condición no se cumple.
* Permite elegir entre dos caminos.

```text
Si (condición) entonces
    Instrucción1
Sino
    Instrucción2
```

Note: Ejemplo práctico: si llueve → llevar paraguas, sino → ir sin paraguas.


### Condicional múltiple

* Evalúa un valor con varias opciones.
* Cada opción tiene sus instrucciones.

```text
Según valor entonces
    opcion1: Instrucciones
    opcion2: Instrucciones
```

Note: Útil cuando hay varias alternativas posibles.
Ejemplo: menú con varias elecciones.


### Condicionales anidados

* Condiciones dentro de otras condiciones.
* Permiten mayor detalle y control.

```text
Si (condición1) entonces
    Instrucciones1
Sino
    Si (condición2) entonces
        Instrucciones2
```

Note: Explica que se combinan para casos complejos.
Ejemplo: clasificación según edad (niño, adulto, anciano).

---

## 2.3.3 Iterativas


### Bucle Mientras

* Repite mientras la condición sea verdadera.
* Evalúa condición antes de ejecutar.
* Riesgo de bucles infinitos si no cambia la condición.

```text
Mientras (condición) hacer
    Instrucción1
    Instrucción2
Fin
```

Note: Ejemplo: cuenta atrás mientras el contador > 0.
Insiste en la importancia de modificar la variable de control.


### Ejemplo Mientras

```text
Mientras (cont > 0) hacer
    Escribe cont
    cont = cont - 1
```

Note: Este ejemplo imprime una cuenta atrás.
Pregunta a los alumnos qué resultado creen que dará.


### Bucle Para

* Ejecuta bloque un número fijo de veces.
* Usa variable de control (i).
* Puede ser ascendente o descendente.

```text
Para i en (1…N) hacer
    Instrucciones
```

Note: Explica que es ideal cuando se conoce el número de repeticiones.
Ejemplo: sumar los primeros 10 números.


### Ejemplo Para

```text
Inicio
    suma = 0
    Para i en (1…10) hacer
        suma = suma + i
    Escribe "La suma es " + suma
Fin
```

Note: Ejemplo típico para calcular sumas.
Pregunta: ¿cuál será el resultado de sumar 1 a 10?

---

## Actividades y Ejercicios


### Actividad 1 - Comparar dos números

* Leer dos números.  
* Mostrar cuál de los dos es mayor.  

```text
Inicio
    Lee num1
    Lee num2
    Si (num1 > num2) entonces
        Escribe num1 + " es mayor que " + num2
    Sino
        Escribe num2 + " es mayor que " + num1
Fin
````

Note: Ejemplo sencillo para practicar condiciones dobles.
Pide a los alumnos probar con diferentes valores.


### Actividad 2 - Relación entre dos números

* Leer dos números.
* Mostrar si son iguales, mayor o menor.

```text
Inicio
    Lee num1
    Lee num2
    Si (num1 == num2) entonces
        Escribe "Son iguales"
    Sino
        Si (num1 > num2) entonces
            Escribe num1 + " es mayor"
        Sino
            Escribe num2 + " es mayor"
Fin
```

Note: Actividad para practicar condiciones anidadas.
Resalta la importancia de la indentación.


### Actividad 3 - Serie descendente

* Leer un número mayor que 0.
* Mostrar la serie decreciendo hasta 0.

```text
Inicio
    Lee num
    Si (num > 0) entonces
        Mientras (num >= 0) hacer
            Escribe num
            num = num - 1
Fin
```

Note: Actividad con bucle `Mientras`.
Pregunta: ¿Qué pasa si no restamos el valor de `num`?


### Actividad 4 - Serie descendente con Para

* Repetir el ejercicio anterior.
* Usar el bucle `Para`.

```text
Inicio
    Lee num
    Si (num > 0) entonces
        Para i en (num…0) hacer
            Escribe i
Fin
```

Note: Comparar este ejemplo con el bucle `Mientras`.
Resalta que `Para` es más cómodo cuando conocemos el rango.


### Ejercicio 1 - Validar rango

* Leer un número entre 1 y 10.
* Repetir hasta que sea válido.


### Solución
```text
Inicio
    Lee num
    Mientras (num < 1 or num > 10) hacer
        Escribe "Inténtalo otra vez!"
        Lee num
Escribe "Correcto!"
Fin
```

Note: Ejercicio de validación de entrada.
Introduce el concepto de *bucles de control de errores*.


### Ejercicio 2 - Serie entre dos números

* Leer dos números.
* Crear la serie que los une.

Ejemplo:

```
4 y 8 → 4 5 6 7 8
12 y 3 → 3 4 5 … 12
```

Note: Buen ejercicio para usar condicionales y bucles.
Permite pensar si el segundo número es mayor o menor.

### Ejercicio 3 - Ordenar tres números

* Leer tres números.
* Mostrar en orden ascendente.

Ejemplo:

```
Entrada: 14, 7, 10
Salida: 7 10 14
```

Note: Problema clásico de ordenación.
Introduce a los alumnos en el razonamiento algorítmico.

---

# Dudas
![](./assets/IS-U011-Presentacion4.png)

Note: Abre el espacio para preguntas. Anima a los alumnos a expresar dudas o compartir ideas.

---

## ¡Gracias por su atención!

![](./assets/Fin.png) <!-- .element height="50%" width="50%" -->

Note: Finaliza la presentación invitando a preguntas y aclaraciones. Refuerza que la relación entre hardware y software es fundamental para comprender cómo funciona un ordenador y que este conocimiento será la base de temas más avanzados en programación y sistemas.

---

