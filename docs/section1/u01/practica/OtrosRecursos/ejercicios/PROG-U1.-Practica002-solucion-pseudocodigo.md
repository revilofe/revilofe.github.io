---
title: "UD 1 - P2: Usando Pseudocodigo Solución"
summary: description: Usando Pseudocodigo
description: Usando Pseudocodigo
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: "material/file-document-edit"
permalink: /prog/unidad1/p1.2
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---


## P1.2 - Ejercicios Resueltos en pseudocódigo

## 1. Aquí tienes los algoritmos en pseudocódigo para las tareas solicitadas. Los algoritmos incluyen las instrucciones necesarias y las explicaciones correspondientes para que sean fáciles de entender.


---

### Algoritmo 1 : Determinar si un número X es par o impar

**Descripción**:
Este algoritmo determina si un número es par o impar. Un número es par si al dividirlo por 2 el resto es cero, de lo contrario, es impar.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un número entero: "
    Lee X

    Si (X % 2 == 0) Entonces  // Verificar si el resto de la división entre 2 es cero
        Escribe X + " es un número par."
    Sino
        Escribe X + " es un número impar."
    FinSi
Fin
```

**Explicación**:
1. El algoritmo solicita un número entero, `X`.
2. Se verifica si `X` es divisible entre 2 (resto igual a cero).
3. Si el resto es cero, se indica que el número es par.
4. Si el resto no es cero, se indica que el número es impar.

---

### Algoritmo 2: Generar la tabla de multiplicar del número X desde 1 hasta 10

**Descripción**:
Este algoritmo genera la tabla de multiplicar de un número dado `X`, desde 1 hasta 10.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un número entero: "
    Lee X
    
    Escribe "Tabla de multiplicar del número " + X + ":"
    
    Para i en (1...10) hacer
        resultado = X * i  // Multiplicar el número X por i
        Escribe X + " x " + i + " = " + resultado
    FinPara
Fin
```

**Explicación**:
1. El algoritmo solicita un número entero, `X`.
2. Utiliza un bucle `Para` para iterar desde 1 hasta 10.
3. En cada iteración, se multiplica `X` por el valor de `i` y se imprime el resultado en formato de tabla.
4. Se genera la tabla de multiplicar completa del número `X`.

---

### Algoritmo 3: Determinar si un número X es primo

**Descripción**:
Este algoritmo determina si un número es primo o no. Un número es primo si solo es divisible por 1 y por sí mismo, es decir, no tiene divisores propios.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un número entero: "
    Lee X

    es_primo = verdadero  // Inicialmente asumimos que el número es primo
    
    Si (X <= 1) Entonces  // Los números menores o iguales a 1 no son primos
        es_primo = falso
    Sino
        Para i en (2 ... X-1) hacer
            Si (X % i == 0) Entonces  // Si X es divisible por algún número entre 2 y X-1, no es primo
                es_primo = falso
                Romper  // Salir del bucle
            FinSi
        FinPara
    FinSi

    Si (es_primo) Entonces
        Escribe X + " es un número primo."
    Sino
        Escribe X + " no es un número primo."
    FinSi
Fin
```

**Explicación**:
1. El algoritmo solicita un número entero, `X`.
2. Inicialmente se asume que el número es primo (variable `es_primo` se establece a `verdadero`).
3. Si el número es menor o igual a 1, no es primo y se establece `es_primo = falso`.
4. Luego, se recorre un bucle `Para` desde 2 hasta `X-1`. Si `X` es divisible por algún número en ese rango, se marca como no primo (`es_primo = falso`) y se interrumpe el bucle.
5. Finalmente, se imprime si el número es primo o no, dependiendo del valor de `es_primo`.


Si necesitas más detalles o ejemplos adicionales, no dudes en pedirlo.


---
## 2. Aquí tienes las soluciones de la práctica 1.2 con explicaciones detalladas.


### Ejercicio 1.2.1: Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

**Descripción**:
Este programa solicita al usuario que introduzca su nombre y luego le da la bienvenida mostrando un mensaje en pantalla.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Escribe tu nombre: "
    Lee nombre
    Escribe "Hola, " + nombre + "."
Fin
```

**Explicación**:
1. El programa comienza pidiendo el nombre del usuario con la instrucción `Escribe`.
2. Se lee el nombre del usuario y se almacena en la variable `nombre`.
3. Finalmente, se imprime un mensaje de bienvenida concatenando el texto "Hola, " con el valor de la variable `nombre`, seguido de un punto.

---

### Ejercicio 1.2.2: Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

**Descripción**:
Este programa solicita al usuario dos datos: las horas trabajadas y el precio por hora, y calcula el importe total multiplicando ambos valores.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce las horas de trabajo: "
    Lee horas
    Escribe "Introduce el coste por hora: "
    Lee coste_por_hora
    
    total = horas * coste_por_hora
    
    Escribe "El importe total es: " + total
Fin
```

**Explicación**:
1. Se solicitan al usuario las horas trabajadas y el coste por hora.
2. Se multiplican las horas por el coste por hora y se almacena el resultado en la variable `total`.
3. El programa muestra el importe total del servicio.

---

### Ejercicio 1.2.3: Adivina el resultado de las siguientes expresiones y su tipo

**Descripción**:
En este ejercicio, el alumno debe predecir el resultado de ciertas expresiones aritméticas y luego verificar si su predicción fue correcta.

1. `ancho / 2`
2. `ancho // 2`
3. `alto / 3`
4. `1 + 2 * 5`

**Resultados**:
1. `ancho / 2` → Resultado: 8.5, tipo: float (porque es una división que genera decimales).
2. `ancho // 2` → Resultado: 8, tipo: entero (división entera).
3. `alto / 3` → Resultado: 4.0, tipo: float (ya que la variable `alto` es de tipo float).
4. `1 + 2 * 5` → Resultado: 11, tipo: entero (por la precedencia de los operadores: primero se multiplica 2 * 5 y luego se suma 1).

---

### Ejercicio 1.2.4: Conversión de grados Celsius a Fahrenheit

**Descripción**:
Este programa convierte una temperatura dada en grados Celsius a grados Fahrenheit usando la fórmula:

\[ F = (C \times 9/5) + 32 \]

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce la temperatura en grados Celsius: "
    Lee celsius
    
    fahrenheit = (celsius * 9/5) + 32
    
    Escribe "La temperatura en grados Fahrenheit es: " + fahrenheit
Fin
```

**Explicación**:
1. Se pide la temperatura en grados Celsius al usuario.
2. Se utiliza la fórmula de conversión de Celsius a Fahrenheit.
3. El programa muestra la temperatura en grados Fahrenheit.

---

### Ejercicio 1.2.5: Cálculo del precio final de un artículo con IVA

**Descripción**:
Este programa calcula el precio final de un artículo sumándole el IVA. El usuario introduce el precio sin IVA y el tipo de IVA a aplicar.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el importe sin IVA: "
    Lee precio_sin_iva
    Escribe "Introduce el tipo de IVA (en porcentaje): "
    Lee iva
    
    precio_final = precio_sin_iva + (precio_sin_iva * iva / 100)
    
    Escribe "El precio final del artículo es: " + precio_final
Fin
```

**Explicación**:
1. El usuario introduce el precio del artículo sin IVA y el porcentaje del IVA.
2. El programa calcula el importe del IVA multiplicando el precio por el porcentaje de IVA y luego suma el resultado al precio original.
3. Finalmente, el programa muestra el precio final.

---

### Ejercicio 1.2.6: Cálculo del IVA pagado y el importe sin IVA

**Descripción**:
Este programa solicita el precio final de un artículo (incluyendo IVA) y calcula cuánto se ha pagado de IVA y el importe sin IVA. Se asume un tipo de IVA del 10%.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el importe final: "
    Lee precio_final
    
    precio_sin_iva = precio_final / 1.10
    iva_pagado = precio_final - precio_sin_iva
    
    Escribe "El importe sin IVA es: " + precio_sin_iva
    Escribe "El IVA pagado es: " + iva_pagado
Fin
```

**Explicación**:
1. El usuario introduce el precio final, que incluye el IVA.
2. Se divide el precio final entre 1.10 para obtener el precio sin IVA (dado que el 10% de IVA es equivalente a multiplicar por 1.10).
3. El IVA pagado se obtiene restando el precio sin IVA del precio final.
4. Se muestran ambos valores en pantalla.

---

### Ejercicio 1.2.7: Suma de tres números

**Descripción**:
Este programa pide al usuario que introduzca tres números y luego calcula su suma.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el primer número: "
    Lee num1
    Escribe "Introduce el segundo número: "
    Lee num2
    Escribe "Introduce el tercer número: "
    Lee num3
    
    suma = num1 + num2 + num3
    
    Escribe "La suma es: " + suma
Fin
```

**Explicación**:
1. El programa solicita tres números al usuario.
2. Suma los tres números y almacena el resultado en la variable `suma`.
3. Muestra la suma de los números en pantalla.

---

### Ejercicio 1.2.8: Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes

**Descripción**:
Este programa repite la suma de tres números pero usando solo dos variables, lo cual se puede hacer reutilizando las variables en el proceso de cálculo.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el primer número: "
    Lee num1
    Escribe "Introduce el segundo número: "
    Lee num2

    num1 = num1 + num2  // Reutilizamos la variable num1 para almacenar la suma de los dos primeros números

    Escribe "Introduce el tercer número: "
    Lee num2  // Reutilizamos la variable num2 para el tercer número

    num1 = num1 + num2  // Sumamos el tercer número a la variable num1 que ya contiene la suma de los dos primeros
    
    Escribe "La suma es: " + num1
Fin
```

**Explicación**:
1. Se solicitan los dos primeros números y se suman en la variable `num1`.
2. Luego, se lee el tercer número, reutilizando `num2` para almacenar este nuevo valor.
3. Se suma el valor de `num2` (el tercer número) al `num1` (que ya contiene la suma de los dos primeros).
4. Finalmente, el resultado de la suma se imprime.

---

### Ejercicio 1.2.9: Es posible escribir el programa del ejercicio 1.7 sin usar variables

**Descripción**:
El desafío aquí es realizar la suma de tres números sin usar ninguna variable. Aunque se puede hacer sin variables, en pseudocódigo se deben usar variables para manejar los datos temporalmente, pero aquí intentamos reducirlas al mínimo.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el primer número: "
    Lee num1
    Escribe "Introduce el segundo número: "
    Lee num2
    Escribe "Introduce el tercer número: "
    Lee num3
    
    Escribe "La suma es: " + (num1 + num2 + num3)
Fin
```

**Explicación**:
1. Los tres números se leen y se suman directamente en la operación `Escribe` sin la necesidad de variables adicionales para almacenar el resultado de la suma.
2. Se imprime directamente el resultado de la suma de los tres números.

---

### Ejercicio 1.2.10: Mostrar el resultado de una operación aritmética compleja

**Descripción**:
El ejercicio requiere escribir un programa que muestre una operación aritmética dada. Por ejemplo, si se quiere calcular \( (5 + 3) * 2 \), el resultado debería mostrarse directamente.

**Pseudocódigo**:

```plaintext
Inicio
    resultado = (5 + 3) * 2
    Escribe "El resultado es: " + resultado
Fin
```

**Explicación**:
1. Se realiza la operación directamente en una línea y se almacena el resultado en la variable `resultado`.
2. Luego, se muestra el valor de la variable `resultado`.

---

### Ejercicio 1.2.11: Suma de los n primeros números enteros

**Descripción**:
El programa solicita un número entero positivo, n, y luego calcula la suma de todos los números enteros desde 1 hasta n.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un entero positivo: "
    Lee n
    
    suma = n * (n + 1) / 2  // Fórmula para la suma de los n primeros enteros

    Escribe "La suma de los primeros " + n + " enteros es: " + suma
Fin
```

**Explicación**:
1. Se utiliza la fórmula matemática \( \text{suma} = \frac{n(n+1)}{2} \), que permite calcular la suma de los n primeros números enteros.
2. La fórmula se evalúa directamente y se muestra el resultado en pantalla.

---

### Ejercicio 1.2.12: Cálculo del índice de masa corporal (IMC)

**Descripción**:
Este programa calcula el índice de masa corporal (IMC) usando la fórmula:

\[ IMC = \frac{peso}{altura^2} \]

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu peso en kg: "
    Lee peso
    Escribe "Introduce tu estatura en metros: "
    Lee estatura
    
    imc = peso / (estatura * estatura)  // Cálculo del IMC
    Escribe "Tu índice de masa corporal es: " + imc
Fin
```

**Explicación**:
1. Se solicitan al usuario su peso y altura.
2. El IMC se calcula dividiendo el peso por el cuadrado de la altura.
3. El resultado se muestra al usuario.

---

### Ejercicio 1.2.13: Cociente y resto de una división

**Descripción**:
Este programa pide al usuario dos números enteros y muestra el cociente y el resto de la división entera entre ambos números.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el primer número: "
    Lee n
    Escribe "Introduce el segundo número: "
    Lee m
    
    cociente = n // m  // División entera
    resto = n % m  // Resto de la división
    
    Escribe "La división de " + n + " entre " + m + " da un cociente de " + cociente + " y un resto de " + resto
Fin
```

**Explicación**:
1. Se leen dos números enteros.
2. Se realiza la división entera con el operador `//` para obtener el cociente.
3. El operador `%` se utiliza para calcular el resto de la división.
4. El cociente y el resto se imprimen en pantalla.

---

### Ejercicio 1.2.14: Cálculo del peso total de un pedido de payasos y muñecas

**Descripción**:
Este programa calcula el peso total de un pedido de payasos y muñecas. Cada payaso pesa 112 g y cada muñeca pesa 75 g.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el número de payasos vendidos: "
    Lee payasos
    Escribe "Introduce el número de muñecas vendidas: "
    Lee muñecas
    
    peso_total = (payasos * 112) + (muñecas * 75)  // Cálculo del peso total

    Escribe "El peso total del paquete es: " + peso_total + " gramos"
Fin
```

**Explicación**:
1. Se solicitan la cantidad de payasos y muñecas vendidas.
2. Se calcula el peso total multiplicando el número de payasos por su peso y el número de muñecas por su peso, y luego sumando ambos resultados.
3. El peso total del paquete se imprime en gramos.

---

### Ejercicio 1.2.15: Cálculo de ahorros con interés compuesto

**Descripción**:
Este programa calcula el crecimiento de los ahorros de una cuenta bancaria durante tres años con un interés anual del 4%.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce la cantidad depositada en la cuenta de ahorros: "
    Lee capital
    
    interes = 0.04
    ahorro_ano1 = capital * (1 + interes)
    ahorro_ano2 = ahorro_ano1 * (1 + interes)
    ahorro_ano3 = ahorro_ano2 * (1 + interes)
    
    Escribe "Ahorros tras el primer año: " + ahorro_ano1
    Escribe "Ahorros tras el segundo año: " + ahorro_ano2
    Escribe "Ahorros tras el tercer año: " + ahorro_ano3
Fin
```

**Explicación**:
1. Se introduce el capital inicial y se establece un interés del 4%.
2. Se calculan los ahorros al final de cada año sumando el interés al saldo del año anterior.
3. El saldo se muestra al final de cada año.

---

### Ejercicio 1.2.16: Panadería con descuento en barras de pan no frescas

**Descripción**:
Este programa calcula el precio de barras de pan no frescas, que tienen un descuento del 60%. El precio normal de una barra es de 3.49€, y el programa calcula el precio final con descuento.

**Pseudocódigo**:

```plaintext
Inicio
    precio_normal = 3.49  // Precio de una barra de pan
    descuento = 0.60  // Descuento por no ser fresca
    
    Escribe "Introduce el número de barras no frescas vendidas: "
    Lee barras_no_frescas
    
    precio_descuento = precio_normal * (1 - descuento)
    coste_total = precio_descuento * barras_no_frescas
    
    Escribe "Precio habitual de una barra de pan: " + precio_normal + "€"
    Escribe "Descuento aplicado: " + (descuento * 100) + "%"
    Escribe "Coste total por las barras no frescas: " + coste_total + "€"
Fin
```

**Explicación**:
1. Se fija el precio normal de una barra de pan (3.49€) y el descuento (60%).
2. Se calcula el precio con descuento multiplicando el precio normal por (1 - descuento).
3. Se solicita al usuario el número de barras no frescas y se multiplica por el precio con descuento para obtener el coste total.
4. Finalmente, se imprime el precio habitual, el descuento aplicado y el coste total.

---

### Ejercicio 1.2.17: Repetir el nombre del usuario

**Descripción**:
El programa solicita el nombre del usuario y un número entero. Luego imprime el nombre tantas veces como el número indicado, en líneas separadas.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu nombre: "
    Lee nombre
    Escribe "Introduce un número entero: "
    Lee n
    
    Para i en (1...n) hacer
        Escribe nombre
Fin
```

**Explicación**:
1. Se solicita al usuario su nombre y un número entero.
2. Se usa un bucle `Para` que itera desde 1 hasta `n`, imprimiendo el nombre del usuario en cada iteración.
3. Esto asegura que el nombre se imprima tantas veces como se haya solicitado.

---

### Ejercicio 1.2.18: Mostrar el nombre en minúsculas, mayúsculas y con mayúsculas iniciales

**Descripción**:
Este programa solicita el nombre completo del usuario y lo muestra de tres formas diferentes: todo en minúsculas, todo en mayúsculas y con la primera letra de cada palabra en mayúscula.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu nombre completo: "
    Lee nombre_completo
    
    Escribe "En minúsculas: " + minusculas(nombre_completo)
    Escribe "En mayúsculas: " + mayusculas(nombre_completo)
    Escribe "Con mayúsculas iniciales: " + capitalizar(nombre_completo)
Fin
```

**Explicación**:
1. Se lee el nombre completo del usuario.
2. Se utilizan tres funciones diferentes:
    - `minusculas()` convierte todas las letras a minúsculas.
    - `mayusculas()` convierte todas las letras a mayúsculas.
    - `capitalizar()` convierte la primera letra de cada palabra a mayúscula y el resto a minúsculas.
3. Cada versión del nombre se imprime en pantalla.

---

### Ejercicio 1.2.19: Mostrar el nombre del usuario y contar las letras

**Descripción**:
El programa solicita el nombre del usuario, lo convierte a mayúsculas y luego cuenta cuántas letras tiene.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu nombre: "
    Lee nombre
    
    nombre_mayusculas = mayusculas(nombre)
    num_letras = longitud(nombre)
    
    Escribe nombre_mayusculas + " tiene " + num_letras + " letras."
Fin
```

**Explicación**:
1. Se solicita el nombre del usuario.
2. Se convierte el nombre a mayúsculas con `mayusculas()` y se almacena en `nombre_mayusculas`.
3. Se cuenta la longitud del nombre con `longitud()` y se almacena en `num_letras`.
4. El programa imprime el nombre en mayúsculas y el número de letras.

---

### Ejercicio 1.2.20: Mostrar el número de teléfono sin prefijo ni extensión

**Descripción**:
El programa solicita un número de teléfono en formato `+34-número-extensión` y luego muestra el número de teléfono sin el prefijo ni la extensión.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el número de teléfono (formato: +34-número-extensión): "
    Lee telefono
    
    partes = dividir(telefono, "-")  // Separa el prefijo, número y extensión
    
    Escribe "El número sin prefijo ni extensión es: " + partes[1]  // Muestra solo la parte central
Fin
```

**Explicación**:
1. El programa solicita un número de teléfono en formato con prefijo y extensión.
2. Se usa la función `dividir()` para separar el teléfono en tres partes: prefijo, número y extensión.
3. Se imprime la parte central (el número sin el prefijo ni la extensión).

---

### Ejercicio 1.2.21: Invertir una frase

**Descripción**:
El programa solicita una frase y muestra la frase invertida.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce una frase: "
    Lee frase
    
    frase_invertida = invertir(frase)  // Invierte la cadena de caracteres
    
    Escribe "La frase invertida es: " + frase_invertida
Fin
```

**Explicación**:
1. El programa solicita una frase al usuario.
2. La función `invertir()` invierte el orden de los caracteres de la frase.
3. Se imprime la frase invertida.

---

### Ejercicio 1.2.22: Reemplazar una vocal en una frase por su versión mayúscula

**Descripción**:
Este programa solicita una frase y una vocal, luego reemplaza todas las ocurrencias de la vocal en la frase con su versión en mayúsculas.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce una frase: "
    Lee frase
    Escribe "Introduce una vocal: "
    Lee vocal
    
    frase_modificada = reemplazar(frase, vocal, mayusculas(vocal))  // Reemplaza la vocal por mayúsculas
    
    Escribe "La frase modificada es: " + frase_modificada
Fin
```

**Explicación**:
1. El programa solicita una frase y una vocal.
2. La función `reemplazar()` busca todas las ocurrencias de la vocal en la frase y las reemplaza por la vocal en mayúsculas.
3. Se muestra la frase modificada.

---

### Ejercicio 1.2.23: Cambiar el dominio de un correo electrónico

**Descripción**:
Este programa solicita un correo electrónico y cambia su dominio por `ceu.es`.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu correo electrónico: "
    Lee correo
    
    partes = dividir(correo, "@")  // Separa el nombre y el dominio
    nuevo_correo = partes[0] + "@ceu.es"
    
    Escribe "Tu nuevo correo es: " + nuevo_correo
Fin
```

**Explicación**:
1. El programa solicita el correo electrónico del usuario.
2. Se separa el nombre y el dominio usando `dividir()`.
3. Se reemplaza el dominio por `ceu.es` y se muestra el nuevo correo.

---

### Ejercicio 1.2.24: Separar los euros y céntimos de un precio

**Descripción**:
El programa solicita el precio de un producto con dos decimales y separa la parte de los euros y los céntimos.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el precio del producto (con dos decimales): "
    Lee precio
    
    euros = parte_entera(precio)
    centimos = (precio * 100) % 100  // Extrae los céntimos
    
    Escribe "Euros: " + euros + ", Céntimos: " + centimos
Fin
```

**Explicación**:
1. Se solicita el precio del producto.
2. `parte_entera()` extrae la parte de los euros.
3. Se calcula el valor de los céntimos multiplicando el precio por 100 y tomando el resto con 100.
4. Se muestran los euros y los céntimos.

---

### Ejercicio 1.2.25: Mostrar el día, mes y año de una fecha de nacimiento

**Descripción**:
El programa solicita una fecha de nacimiento en formato `dd/mm/aaaa` y muestra el día, mes y año por separado.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce tu fecha de nacimiento (dd/mm/aaaa): "
    Lee fecha
    
    partes = dividir(fecha, "/")
    
    Escribe "Día: " + partes[0]
    Es

cribe "Mes: " + partes[1]
    Escribe "Año: " + partes[2]
Fin
```

**Explicación**:
1. El programa solicita la fecha de nacimiento.
2. Se divide la fecha en tres partes (día, mes, año) usando `dividir()`.
3. Se muestra cada parte por separado.

---

### Ejercicio 1.2.26: Mostrar productos de una cesta de la compra en líneas separadas

**Descripción**:
Este programa solicita al usuario una lista de productos separados por comas y luego muestra cada producto en una línea distinta.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce los productos de la cesta de la compra separados por comas: "
    Lee productos
    
    lista_productos = dividir(productos, ",")  // Divide la cadena de productos en una lista
    
    Para cada producto en lista_productos hacer
        Escribe producto
Fin
```

**Explicación**:
1. Se solicita al usuario que introduzca una lista de productos separados por comas.
2. Se usa la función `dividir()` para separar los productos en una lista.
3. Un bucle `Para cada` recorre la lista e imprime cada producto en una línea separada.

---

### Ejercicio 1.2.27: Mostrar el nombre de un producto, su precio y el número de unidades

**Descripción**:
El programa solicita el nombre de un producto, su precio unitario y el número de unidades, y luego muestra un formato específico con estos datos.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el nombre del producto: "
    Lee nombre_producto
    Escribe "Introduce el precio unitario del producto: "
    Lee precio
    Escribe "Introduce el número de unidades: "
    Lee unidades
    
    coste_total = precio * unidades
    
    // Mostrar el formato solicitado
    Escribe "Producto: " + nombre_producto
    Escribe "Precio unitario: " + formatear(precio, 6, 2)  // Formato de 6 dígitos enteros y 2 decimales
    Escribe "Unidades: " + formatear(unidades, 3)  // Formato de 3 dígitos enteros
    Escribe "Coste total: " + formatear(coste_total, 8, 2)  // Formato de 8 dígitos enteros y 2 decimales
Fin
```

**Explicación**:
1. Se solicitan el nombre del producto, su precio unitario y la cantidad de unidades.
2. Se calcula el coste total multiplicando el precio por el número de unidades.
3. Se utiliza la función `formatear()` para mostrar el precio unitario, el número de unidades y el coste total con el formato solicitado:
    - El precio se muestra con 6 dígitos enteros y 2 decimales.
    - El número de unidades se muestra con 3 dígitos enteros.
    - El coste total se muestra con 8 dígitos enteros y 2 decimales.

---

### Ejercicio 1.2.28: Calcular el área de un triángulo a partir de tres lados

**Descripción**:
Este programa calcula el área de un triángulo utilizando la fórmula de Herón, a partir de las longitudes de los tres lados del triángulo.

La fórmula de Herón es:

\[
s = \frac{a + b + c}{2}
\]

\[
\text{Área} = \sqrt{s(s - a)(s - b)(s - c)}
\]

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce la longitud del primer lado: "
    Lee a
    Escribe "Introduce la longitud del segundo lado: "
    Lee b
    Escribe "Introduce la longitud del tercer lado: "
    Lee c
    
    s = (a + b + c) / 2  // Semiperímetro
    
    area = raiz(s * (s - a) * (s - b) * (s - c))  // Cálculo del área usando la fórmula de Herón
    
    Escribe "El área del triángulo es: " + area
Fin
```

**Explicación**:
1. El programa solicita las longitudes de los tres lados del triángulo.
2. Se calcula el semiperímetro \( s \) sumando los tres lados y dividiendo entre 2.
3. Se calcula el área utilizando la fórmula de Herón, con la función `raiz()` para obtener la raíz cuadrada.
4. Finalmente, se muestra el área del triángulo.

---

### Ejercicio 1.2.29: Cálculo de un número aleatorio entre dos valores

**Descripción**:
Este programa solicita dos números y genera un número aleatorio entre esos dos valores.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el valor mínimo: "
    Lee min
    Escribe "Introduce el valor máximo: "
    Lee max
    
    aleatorio = generar_aleatorio(min, max)  // Función que genera un número aleatorio entre min y max
    
    Escribe "El número aleatorio generado es: " + aleatorio
Fin
```

**Explicación**:
1. Se solicitan los valores mínimo y máximo.
2. Se usa la función `generar_aleatorio()` para obtener un número aleatorio entre el valor mínimo y el máximo introducido por el usuario.
3. El número aleatorio se muestra en pantalla.

---

### Ejercicio 1.2.30: Escribir un programa que determine si un número es primo

**Descripción**:
Este programa solicita un número y determina si es primo o no. Un número es primo si solo es divisible entre 1 y él mismo.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un número entero: "
    Lee num
    
    es_primo = verdadero  // Asumimos que el número es primo al inicio
    
    Si (num <= 1) Entonces
        es_primo = falso
    Sino
        Para i en (2 ... num-1) hacer
            Si (num % i == 0) Entonces
                es_primo = falso
                Romper  // Salir del bucle si encontramos un divisor
            FinSi
        FinPara
    FinSi
    
    Si (es_primo) Entonces
        Escribe num + " es un número primo."
    Sino
        Escribe num + " no es un número primo."
Fin
```

**Explicación**:
1. Se solicita un número entero al usuario.
2. Inicialmente, se asume que el número es primo.
3. Si el número es menor o igual a 1, se marca como no primo.
4. Si no, se itera desde 2 hasta `num - 1` para verificar si el número es divisible por algún valor en ese rango. Si es divisible por alguno, no es primo.
5. El programa imprime si el número es primo o no.

---

### Ejercicio 1.2.31: Mostrar todos los divisores de un número

**Descripción**:
El programa solicita un número entero y muestra todos sus divisores.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce un número entero: "
    Lee num
    
    Escribe "Los divisores de " + num + " son:"
    
    Para i en (1 ... num) hacer
        Si (num % i == 0) Entonces
            Escribe i  // Muestra el divisor
        FinSi
    FinPara
Fin
```

**Explicación**:
1. Se solicita un número entero al usuario.
2. Se utiliza un bucle `Para` que itera desde 1 hasta el valor del número.
3. En cada iteración, se verifica si el número es divisible por `i`. Si lo es, `i` es un divisor y se imprime.
4. El programa imprime todos los divisores del número.

---

### Ejercicio 1.2.32: Calcular la serie de Fibonacci hasta un número dado

**Descripción**:
El programa genera la serie de Fibonacci hasta un número dado por el usuario. La serie de Fibonacci comienza con 0 y 1, y cada número es la suma de los dos anteriores.

**Pseudocódigo**:

```plaintext
Inicio
    Escribe "Introduce el número de términos de la serie de Fibonacci: "
    Lee n
    
    a = 0
    b = 1
    
    Si (n >= 1) Entonces
        Escribe a  // Muestra el primer término
    FinSi
    
    Si (n >= 2) Entonces
        Escribe b  // Muestra el segundo término
    FinSi
    
    Para i en (3 ... n) hacer
        siguiente = a + b
        Escribe siguiente
        a = b  // Actualizamos los valores de a y b
        b = siguiente
    FinPara
Fin
```

**Explicación**:
1. El programa solicita el número de términos de la serie de Fibonacci.
2. Los dos primeros términos de la serie (0 y 1) se muestran si el número de términos es 1 o más.
3. Luego, se usa un bucle `Para` para calcular los términos siguientes de la serie, actualizando los valores de `a` y `b` en cada iteración.
4. El programa imprime cada término de la serie hasta llegar al número de términos solicitado.

---

Con esto hemos completado las soluciones a los ejercicios solicitados. 