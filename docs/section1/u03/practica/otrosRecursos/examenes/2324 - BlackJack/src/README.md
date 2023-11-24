## ♠️♥️♦️♣️ **Ejercicio: Juguemos al blackjack** ♠️♥️♦️♣️

#### Representación del Juego:

Este programa desarrolla el juego del black jack entre dos jugadores:

- Inicialmente se reparte una carta a cada jugador.
- Posteriormente se pregunta en cada ronda si desea una carta más o se planta.
- Gana el jugador que más se acerque a 21 sin pasarse.
- El programa te permite jugar una partida tras otra hasta que tú decidas parar o se acaben las cartas de la baraja.
- El valor de las cartas es el siguiente:
    * El número de la misma en las cartas del 2 al 10.
    * As puede valer 1 u 11.
    * J, Q y K valen 10.

#### Descripción del Problema:

En esta ocasión la documentación no está completa y solo existe una descripción funcional de qué realiza cada bloque de código del juego.

Algún profe despistado ha desarrollado con prisas el juego y debéis darle solución vosotros...

* Para empezar nos falta una constante muy VALIOSA, que recoje los puntos de cada CARTA en un diccionario. El As es una carta que actúa de comodín y puede valer 1 u 11, según mejor convenga a nuestra mano. Esta carta especial debe tener un valor de una tupla de dos valores enteros y no un solo valor entero cómo el resto de cartas.

* Soluciona los errores evidentes que ya os está marcando Visual Studio.

* Al proporcionar las cartas a los jugadores, aunque parece que tiene buena pinta, cuando se acaba la baraja se produce un "problemilla" no muy controlado, está claro que el profe no jugó mucho...

* Al desarrollar el juego seguramente existan argumentos o parámetros que no se hayan pasado o definido correctamente... en fin, las prisas :-P

* En la función valor_carta se intenta controlar que si el tipo del valor de la carta es una tupla y tiene 2 elementos pueda recuperar su valor mínimo o máximo según indique su parámetro de entrada valor_minimo.

* jugar() debe tener algún problema porque no me deja JUGAR...

* Me gustaría que el programa funcionara cómo se describe al principio y poder jugar las partidas que yo quiera hasta que se acabe la baraja.

* Si ves alguna mejora posible, adelante y realizala, siempre que la documentes correctamente y no cómo ha hecho el vago del profesor.
