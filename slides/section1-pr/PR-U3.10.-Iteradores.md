# U3.10 - Iteradores y Objetos Iterables

---

![Logo Alberti](assets/logo-iesra.png) <!-- .element height="50%" width="50%" -->

---

## Índice
1. Conceptos Básicos
2. Funcionamiento y Uso
3. Ventajas y Conclusión

---

## 1. Conceptos Básicos


### 1.1. ¿Qué es un objeto iterable?

*   Un objeto que puede devolver sus elementos uno por uno.
*   Si puedes usarlo en un bucle `for`, es un iterable.
*   Ejemplos: listas, tuplas, cadenas, diccionarios, conjuntos.
*   Técnicamente, implementa el método `__iter__()`.

Note: Un objeto iterable es una colección de elementos que se pueden recorrer secuencialmente. La característica principal es que se puede obtener un iterador de ellos, lo que permite procesar sus elementos de uno en uno. Esto es fundamental para estructuras como los bucles `for`.


### 1.2. ¿Qué es un iterador?

*   Un objeto que representa un flujo de datos.
*   Lleva la cuenta del elemento actual en la secuencia.
*   Implementa el "protocolo del iterador":
    *   `__iter__()`: Devuelve el propio iterador.
    *   `__next__()`: Devuelve el siguiente elemento.
*   Lanza `StopIteration` cuando no hay más elementos.

Note: A diferencia del iterable (que es el contenedor), el iterador es el objeto que gestiona el estado de la iteración. Sabe cuál fue el último elemento devuelto y cómo obtener el siguiente. Esta separación de responsabilidades es clave para la eficiencia.

---

## 2. Funcionamiento y Uso


### 2.1. El bucle `for` y los iteradores

*   El bucle `for` usa iteradores de forma implícita.
*   Pasos internos que realiza Python:
    1.  Llama a `iter()` sobre el iterable para obtener un iterador.
    2.  En cada vuelta, llama a `next()` para obtener el siguiente elemento.
    3.  Cuando `next()` lanza `StopIteration`, el bucle termina.

Note: El bucle `for` abstrae toda la complejidad del manejo de iteradores. No tenemos que llamar a `iter()` o `next()` manualmente ni capturar la excepción `StopIteration`. Python lo hace todo por nosotros, lo que resulta en un código más limpio y legible.


### 2.2. Uso explícito de iteradores

*   Podemos controlar la iteración manualmente.
*   `iter(iterable)`: Obtiene el iterador.
*   `next(iterador)`: Obtiene el siguiente elemento.

```python
numeros = [10, 20, 30]
mi_iterador = iter(numeros)

print(next(mi_iterador)) # Salida: 10
print(next(mi_iterador)) # Salida: 20
# Al llamar a next() de nuevo, se obtiene 30.
# Una llamada más lanzaría StopIteration.
```

Note: El uso manual es útil para escenarios avanzados donde se necesita un control más fino sobre el proceso de iteración, como procesar solo una parte de una secuencia o pasar el estado de la iteración entre diferentes partes del programa.

---

## 3. Ventajas y Conclusión


### 3.1. Ventajas de usar iteradores

*   **Eficiencia de memoria (Lazy Evaluation)**:
    *   No cargan todos los datos en memoria a la vez.
    *   Generan valores "bajo demanda".
    *   Ideal para archivos grandes o flujos de datos infinitos.
*   **Código más flexible**:
    *   Permiten crear flujos de datos complejos (ej. generadores).

Note: La evaluación "perezosa" es la ventaja más significativa. Imagina procesar un archivo de logs de varios gigabytes. Cargar todo el archivo en una lista colapsaría la memoria del sistema. Un iterador, en cambio, solo mantiene una línea en memoria a la vez, haciendo el proceso viable y eficiente.


### 3.2. Conclusión

*   **Iterable**: Es el contenedor de datos (ej. una lista).
*   **Iterador**: Es el objeto que proporciona los datos uno a uno.
*   El bucle `for` es la forma más común de usar iterables.
*   Entender los iteradores es clave para escribir código Python eficiente,
    especialmente en el manejo de grandes volúmenes de datos.

Note: Dominar el concepto de iteradores y su diferencia con los iterables es un paso fundamental para pasar de un nivel básico a uno intermedio en Python. Permite comprender mejor cómo funcionan muchas de las herramientas del lenguaje y optimizar el rendimiento de nuestras aplicaciones.

---

## ¿Preguntas?
