---
title: "UD 3 - P0: Cadenas"
summary: Cadenas
description: Cadenas
authors:
    - Eduardo Fdez
date: 2022-10-01
icon: "material/file-document-edit"
permalink: /prog/unidad3/p3.0
categories:
    - PROG
tags:
    - Software
    - Ejercicios
    - Cadenas
---
## P3.0 - Ejercicios

#### **Ejercicio 3.0.1**

Escribe un bucle `while` que comience con el último carácter en la cadena y haga un recorrido hacia atrás hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.

<!--
-->

#### **Ejercicio 3.0.2**

Dado que `fruta` es una variable de tipo cadena, ¿qué significa `fruta[:]`?

<!--

-->

#### **Ejercicio 3.0.3**

Tienes este código:
```Python
palabra = 'banana'
contador = 0
for letra in palabra:
    if letra == 'a':
        contador = contador + 1
print(contador)
```
Encapsúlalo en una función llamada `cuenta`, y hazla genérica de tal modo que pueda aceptar una cadena y una letra como argumentos. De tal forma que pueda hacer la siguiente llamada:

```
numero_de_os = cuenta("consuelo","o") # Resultado debe ser 2

```

<!--

-->

#### **Ejercicio 3.0.4**

Hay un método de cadenas llamado `find`, que es similar a `count`. Lee la documentación de este método en:     

* [Métodos en ingles](https://docs.python.org/library/stdtypes.html#string-methods)
* [Métodos en castellano](https://docs.python.org/es/3/library/stdtypes.html#string-methods)

Escribe el código necesario para invocar a este método `find` y contar el número de veces que una letra aparece en “banana”.

<!--

-->
