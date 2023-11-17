## 🧨 **Ejercicio: El Buscaminas de la Isla Misteriosa** 🧨

#### Descripción del Problema:

¡Aventureros! Os encontráis en la Isla Misteriosa, un lugar conocido por sus enigmas y, sobre todo, por sus peligrosas minas ocultas. Vuestro objetivo es despejar la isla de minas sin detonar ninguna. ¡Cuidado! Un paso en falso y todo habrá terminado.

#### Representación del Juego:

- **Tablero**: El juego se desarrolla en un tablero de cuadrícula de 8x8.
- **Minas**: Algunas celdas del tablero contienen minas ocultas.
- **Números**: Las celdas sin minas muestran el número de minas en las celdas adyacentes.
- **Celdas Vacías**: Las celdas sin minas ni números adyacentes son "vacías".

#### Estructuras de Datos a Utilizar:

- **Matriz Bidimensional**: Representación del tablero.
- **Listas**: Para almacenar las coordenadas de las minas, números y celdas vacías.
- **Conjuntos**: Para llevar un registro de las celdas ya reveladas o marcadas.

#### Tareas para los Estudiantes:

1. **Inicialización del Tablero**: Crear una función para inicializar el tablero colocando aleatoriamente las minas y calculando los números para las celdas adyacentes a las minas.
2. **Revelar Celda**: Implementar una función que revele el contenido de una celda seleccionada por el usuario. Si la celda es una mina, el juego termina. Si es un número, se muestra. Si es vacía, se revelan las celdas adyacentes. Permite revelar celdas marcadas.
3. **Marcar Celdas**: Permitir a los usuarios marcar celdas que creen que contienen minas.
4. **Verificación de Victoria**: Verificar si el jugador ha despejado todas las celdas sin minas.
5. **Interfaz de Usuario**: Crear una interfaz simple en la consola para que el jugador pueda interactuar con el juego (por ejemplo, elegir una celda para revelar o marcar).

#### Ejemplo de Interacción:

```
  1 2 3 4 5 6 7 8
1 . . . . . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . . . . . .
5 . . . . . . . .
6 . . . . . . . .
7 . . . . . . . .
8 . . . . . . . .

Elige una acción:
1. Revelar celda
2. Marcar celda
3. Salir

Tu elección: 1
Ingresa coordenadas (fila, columna): 5,3

Revelando celda 5,3...
```

### Consideraciones Adicionales:

- Introduce errores de sintaxis y lógica en el código base que los estudiantes tendrán que corregir.
- Añade desafíos adicionales, como limitar el número de banderas que pueden colocar o implementar diferentes niveles de dificultad.

---

Este ejercicio de Buscaminas no solo les permite practicar con estructuras de datos fundamentales en Python, sino que también desafía su lógica y capacidad de pensamiento crítico. Además, al ser un juego familiar, puede resultar más atractivo y motivador para ellos.
