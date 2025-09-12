# U1.2 - Código Fuente, Objeto y Ejecutable

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice 1

- Relación entre el Software y el Hardware
- Introducción
    - De la idea al programa
- Código Fuente
    - Definición
    - Ejemplo de Código Fuente en C


## Índice 2

- Código Objeto
    - Definición
    - Importancia del Código Objeto
- Código Ejecutable
    - Definición
    - Características del Ejecutable


## Índice 3

- Ejemplo Visual
    - Proceso Comparado con una Receta
    - Ilustración del Proceso
- Proceso de Conversión
    - Etapas
- Conclusión


## Índice 4

- Conclusión
    - Resumen Final
- ¡Gracias por su atención!
---

## Relación entre el Software y el Hardware


## Introducción


### De la idea al programa

* El desarrollo de un programa tiene varias etapas.
* Se parte de un **código fuente** escrito por humanos.
* Se transforma en **código objeto** mediante compilación.
* Finalmente se obtiene un **ejecutable**.
* Metáfora: plano → piezas → mesa terminada.

Note: Explica la metáfora de la mesa: el plano es el código fuente, las piezas cortadas son el código objeto y la mesa terminada es el ejecutable. Esto permite introducir la importancia de entender cada etapa.

---

## Código Fuente


### Definición

* Conjunto de instrucciones escritas por el programador.
* Utiliza un lenguaje comprensible para humanos.
* No es ejecutable directamente por el ordenador.
* Ejemplos: Python, C, Java, C++, JavaScript.

Note: El código fuente es el punto de partida. Aclara que los ordenadores no entienden directamente estos lenguajes, sino que requieren traducción a lenguaje de máquina.


### Ejemplo de Código Fuente en C

```c
#include <stdio.h>
int main() {
    printf("Hola, mundo!\n");
    return 0;
}
```

* Muestra un mensaje en pantalla.
* Es legible para humanos, no para la CPU.

Note: Revisa el ejemplo clásico “Hola, mundo”. Explica que es fácil de entender para un programador pero ilegible para la máquina.

---

## Código Objeto


### Definición

* Versión intermedia del código fuente.
* Generado por el compilador a partir del código fuente.
* Contiene instrucciones en lenguaje de máquina parcial.
* No es aún un programa ejecutable completo.

Note: El código objeto es un paso intermedio: ya está traducido parcialmente, pero aún necesita enlazarse con librerías y otros módulos para ser ejecutable.


### Importancia del Código Objeto

* Permite dividir un programa en partes (módulos).
* Cada módulo se compila por separado.
* Luego se enlazan para crear el ejecutable.
* Hace más eficiente el proceso de desarrollo.

Note: Explica que en proyectos grandes se compilan módulos independientes para luego unirlos. Así se evita recompilar todo el proyecto cada vez.

---

## Código Ejecutable


### Definición

* Es la versión final del programa.
* Contiene instrucciones en lenguaje de máquina.
* El procesador puede ejecutarlo directamente.
* Ejemplos: `hola.exe` en Windows, `./hola` en Linux.

Note: Aclara que el ejecutable ya no es legible por humanos, pero es lo que necesita el ordenador para funcionar.


### Características del Ejecutable

* Incluye todos los módulos enlazados.
* Contiene librerías necesarias para su ejecución.
* Puede ejecutarse con doble clic o desde terminal.
* Representado en binario (unos y ceros).

Note: Recalca que el ejecutable integra todo lo necesario para que el sistema operativo pueda cargarlo y el procesador ejecutarlo.

---

## Ejemplo Visual


### Proceso Comparado con una Receta

* **Fuente**: receta en español, clara para humanos.
* **Objeto**: traducción parcial, entendible en parte.
* **Ejecutable**: instrucciones finales que entiende el robot.
* Cada paso acerca el programa a ser utilizable.

Note: Usa la metáfora de la receta: fuente es la receta escrita, objeto es la traducción parcial y ejecutable es la versión lista para que el robot (ordenador) la ejecute.


### Ilustración del Proceso

* Fuente: `printf("Hola, mundo!\n");`
* Objeto: traducción parcial en binario.
* Ejecutable: binario completo, listo para CPU.
* Secuencia: escribir → compilar → enlazar → ejecutar.

Note: Refuerza la idea del paso a paso, mostrando cómo un simple “Hola, mundo” atraviesa estas etapas.

---

## Proceso de Conversión


### Etapas

1. Escribir el código fuente.
2. Compilar → se obtiene el código objeto.
3. Enlazar → se genera el ejecutable.
4. Ejecutar → el programa corre en el ordenador.

Note: Resume la secuencia clásica en lenguajes compilados, especialmente el caso de C, que es el ejemplo más ilustrativo.

---

## Conclusión


### Resumen Final

* **Fuente**: lo que escriben los programadores.
* **Objeto**: traducción intermedia que requiere enlace.
* **Ejecutable**: el programa final que corre en el ordenador.
* Comprender las etapas ayuda a usar compiladores y enlazadores.
* Base para entender el ciclo de vida de un programa.

Note: Cierra el tema subrayando la importancia de distinguir entre los tres tipos de código. Este conocimiento es esencial para el desarrollo eficiente de software.

---

## ¡Gracias por su atención!

Note: Finaliza la presentación invitando a preguntas. Recalca que entender estas fases facilita el trabajo con herramientas de programación y la optimización de proyectos.