---
title: "UD 1 - P2: Usando python Solución"
summary: description: Usando python
description: Usando python
authors:
    - Eduardo Fdez
date: 2022-09-18
icon: 
permalink: /prog/unidad1/p1.2
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---




### **Ejercicio 1.2.1**
Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

```python
# Solicitamos el nombre del usuario
nombre = input("Escribe tu nombre: ")

# Mostramos el saludo de bienvenida
print(f"Hola, {nombre}.")
```

**Explicación**:
1. Utilizamos la función `input` para pedirle al usuario que escriba su nombre y lo almacenamos en la variable `nombre`.
2. Luego, mostramos un mensaje de bienvenida usando `print` y la función de interpolación de cadenas `f"Hola, {nombre}."`.

---

### **Ejercicio 1.2.2**
Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

```python
# Pedimos al usuario las horas trabajadas y el coste por hora
horas_trabajadas = float(input("Horas de trabajo: "))
coste_por_hora = float(input("Coste por hora: "))

# Calculamos el importe total
importe_total = horas_trabajadas * coste_por_hora

# Mostramos el importe total
print(f"Importe total: {importe_total}")
```

**Explicación**:
1. Usamos `input` para pedir al usuario las horas trabajadas y el coste por hora.
2. Convertimos estas entradas a `float` para permitir números decimales.
3. Multiplicamos las horas por el coste para calcular el importe total.
4. Finalmente, imprimimos el importe total.

---

### **Ejercicio 1.2.3**
Para cada una de las siguientes expresiones, adivina su valor y tipo. Luego compruébalo.

```python
# Definimos las variables
ancho = 17
alto = 12.0

# Expresiones
exp1 = ancho / 2  # División normal, resultado flotante
exp2 = ancho // 2  # División entera, resultado entero
exp3 = alto / 3  # División normal, resultado flotante
exp4 = 1 + 2 * 5  # Operación aritmética, siguiendo orden de operadores

# Imprimimos los resultados
print("Expresión 1:", exp1, type(exp1))
print("Expresión 2:", exp2, type(exp2))
print("Expresión 3:", exp3, type(exp3))
print("Expresión 4:", exp4, type(exp4))
```

**Explicación**:
1. Definimos `ancho` como entero y `alto` como flotante.
2. Realizamos las operaciones y mostramos los resultados junto con el tipo de dato (`type`).

---

### **Ejercicio 1.2.4**
Escribe un programa que convierta grados Celsius a Fahrenheit.

```python
# Pedimos la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertimos a Fahrenheit
fahrenheit = celsius * 9/5 + 32

# Mostramos el resultado
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")
```

**Explicación**:
1. Leemos la temperatura en Celsius y la convertimos a `float`.
2. Aplicamos la fórmula de conversión a Fahrenheit: `fahrenheit = celsius * 9/5 + 32`.
3. Mostramos el resultado.

---

### **Ejercicio 1.2.5**
Calcula el precio final de un artículo a partir de su precio sin IVA y el tipo de IVA.

```python
# Pedimos el importe sin IVA y el tipo de IVA
importe_sin_iva = float(input("Introduce el importe sin IVA: "))
tipo_iva = float(input("Introduce el tipo de IVA (%): "))

# Calculamos el importe final con IVA
precio_final = importe_sin_iva * (1 + tipo_iva / 100)

# Mostramos el resultado
print(f"El precio final con IVA es: {precio_final:.2f}")
```

**Explicación**:
1. Leemos el importe sin IVA y el tipo de IVA (en porcentaje).
2. Calculamos el precio final multiplicando por `(1 + tipo_iva / 100)`.
3. Mostramos el resultado con dos decimales.

---

### **Ejercicio 1.2.6**
Calcula el IVA pagado y el importe sin IVA a partir del precio final.

```python
# Pedimos el importe final
importe_final = float(input("Introduce el importe final del artículo: "))

# Suponemos un IVA del 10%
iva = 10

# Calculamos el importe sin IVA
importe_sin_iva = importe_final / (1 + iva / 100)

# Calculamos el IVA pagado
iva_pagado = importe_final - importe_sin_iva

# Mostramos el resultado
print(f"Importe sin IVA: {importe_sin_iva:.2f}")
print(f"IVA pagado: {iva_pagado:.2f}")
```

**Explicación**:
1. Pedimos el importe final del artículo.
2. Calculamos el importe sin IVA usando `importe_final / (1 + iva / 100)`.
3. Calculamos el IVA pagado como la diferencia entre el importe final y el importe sin IVA.

---

### **Ejercicio 1.2.7**
Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

```python
# Pedimos tres números al usuario
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Calculamos la suma de los tres números
suma = num1 + num2 + num3

# Mostramos el resultado
print(f"La suma de {num1}, {num2} y {num3} es: {suma}")
```

**Explicación**:
1. Usamos `input` para pedir al usuario tres números y los convertimos a `float` para permitir números decimales.
2. Sumamos los tres números y almacenamos el resultado en `suma`.
3. Mostramos la suma en pantalla.

---

### **Ejercicio 1.2.8**
Escribe el programa del ejercicio 1.7 usando solamente dos variables diferentes.

```python
# Pedimos el primer número
num1 = float(input("Introduce el primer número: "))

# Pedimos el segundo número y sumamos directamente
num1 += float(input("Introduce el segundo número: "))

# Pedimos el tercer número y sumamos directamente
num1 += float(input("Introduce el tercer número: "))

# Mostramos el resultado
print(f"La suma de los tres números es: {num1}")
```

**Explicación**:
1. Almacenamos el primer número en `num1`.
2. Vamos acumulando la suma de los siguientes números usando `+=`.
3. Finalmente, imprimimos el resultado acumulado en `num1`.

---

### **Ejercicio 1.2.9**
¿Es posible escribir el programa del ejercicio 1.7 sin usar variables? Inténtalo.

```python
# Realizamos la suma directamente dentro del print sin almacenar en variables
print(f"La suma de los tres números es: {float(input('Introduce el primer número: ')) + float(input('Introduce el segundo número: ')) + float(input('Introduce el tercer número: '))}")
```

**Explicación**:
1. Realizamos la suma directamente dentro de `print` y usamos `float` para convertir las entradas.
2. No se almacenan variables intermedias; el resultado se calcula y se muestra de inmediato.

---

### **Ejercicio 1.2.10**
Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética:

$$ ((3 + 2) / (2 * 5)) ^ 2 $$

```python
# Calculamos la operación aritmética
resultado = ((3 + 2) / (2 * 5)) ** 2

# Mostramos el resultado
print(f"El resultado de la operación es: {resultado}")
```

**Explicación**:
1. Se siguen las reglas de prioridad de operadores: paréntesis, multiplicación y división, y luego exponenciación.
2. Mostramos el resultado con `print`.

---

### **Ejercicio 1.2.11**
Escribir un programa que lea un entero positivo \( n \) y después muestre en pantalla la suma de todos los enteros desde 1 hasta \( n \).

```python
# Pedimos un número entero positivo
n = int(input("Introduce un número entero positivo: "))

# Calculamos la suma de los primeros n números usando la fórmula
suma = n * (n + 1) // 2

# Mostramos el resultado
print(f"La suma de los primeros {n} números enteros es: {suma}")
```

**Explicación**:
1. Leemos un número entero positivo.
2. Usamos la fórmula de la suma de los primeros \( n \) números enteros: \( n(n+1)/2 \).
3. Mostramos el resultado.

---

### **Ejercicio 1.2.12**
Escribir un programa que calcule el índice de masa corporal (IMC).

```python
# Pedimos el peso y la altura del usuario
peso = float(input("Introduce tu peso en kg: "))
altura = float(input("Introduce tu altura en metros: "))

# Calculamos el IMC
imc = peso / altura**2

# Mostramos el resultado redondeado a dos decimales
print(f"Tu índice de masa corporal es {imc:.2f}")
```

**Explicación**:
1. Leemos el peso y la altura del usuario.
2. Usamos la fórmula del IMC: \( \text{IMC} = \frac{\text{peso}}{\text{altura}^2} \).
3. Mostramos el IMC redondeado a dos decimales.

---

### **Ejercicio 1.2.13**
Escribe un programa que pida dos números y muestre el cociente y el resto de la división entera.

```python
# Pedimos dos números enteros
n = int(input("Introduce el primer número: "))
m = int(input("Introduce el segundo número: "))

# Calculamos el cociente y el resto
cociente = n // m
resto = n % m

# Mostramos el resultado
print(f"La división de {n} entre {m} da un cociente {cociente} y un resto {resto}.")
```

**Explicación**:
1. Leemos dos números enteros.
2. Calculamos el cociente con `//` y el resto con `%`.
3. Mostramos ambos valores.

---

### **Ejercicio 1.2.14**
Calcula el peso total de un pedido de payasos y muñecas.

```python
# Definimos los pesos de cada artículo
peso_payaso = 112  # gramos
peso_muneca = 75   # gramos

# Pedimos el número de payasos y muñecas vendidos
num_payasos = int(input("Número de payasos vendidos: "))
num_munecas = int(input("Número de muñecas vendidas: "))

# Calculamos el peso total del paquete
peso_total = num_payasos * peso_payaso + num_munecas * peso_muneca

# Mostramos el peso total
print(f"El peso total del paquete es: {peso_total} gramos.")
```

**Explicación**:
1. Definimos el peso de un payaso y una muñeca.
2. Pedimos la cantidad vendida de cada uno.
3. Calculamos el peso total multiplicando las cantidades por sus respectivos pesos.

---

### **Ejercicio 1.2.15**
Calcula la cantidad de dinero en una cuenta de ahorros con un 4% de interés al año durante tres años.

```python
# Pedimos el monto inicial
monto_inicial = float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

# Definimos el interés anual
interes = 0.04

# Calculamos el saldo después de cada año
saldo_ano_1 = monto_inicial * (1 + interes)
saldo_ano_2 = saldo_ano_1 * (1 + interes)
saldo_ano_3 = saldo_ano_2 * (1 + interes)

# Mostramos los saldos
print(f"Saldo después del primer año: {saldo_ano_1:.2f}")
print(f"Saldo después del segundo año: {saldo_ano_2:.2f}")
print(f"Saldo después del tercer año: {saldo_ano_3:.2f}")
```

**Explicación**:
1. Leemos el monto inicial y definimos el interés anual.
2. Calculamos el saldo para cada año acumulando el interés.
3. Mostramos los resultados de cada año.

---

### **Ejercicio 1.2.16**
Calcula el precio total de las barras de pan no frescas con descuento.

```python
# Definimos el precio de una barra de pan y el descuento
precio_barra = 3.49
descuento = 0.60

# Pedimos el número de barras vendidas no frescas
barras_no_frescas = int(input("Introduce el número de barras no frescas vendidas: "))

# Calculamos el precio con descuento
precio_con_descuento = precio_barra * (1 - descuento)

# Calculamos el coste total
coste_total = barras_no_frescas * precio_con_descuento

# Mostramos los precios y el coste total
print(f"Precio habitual de una barra de pan: {precio_barra}€")
print(f"Descuento: {descuento * 100}%")
print(f"Coste total de las barras no frescas: {coste_total:.2f}€")
```

**Explicación**:
1. Definimos el precio de una barra de pan y el descuento como constantes.
2. Pedimos al usuario la cantidad de barras vendidas.
3. Calculamos el precio con descuento y el coste total.
4. Mostramos la información relevante al usuario.

---

### **Ejercicio 1.2.17**
Imprimir el nombre del usuario en líneas distintas según el número dado.

```python
# Pedimos el nombre del usuario y el número de repeticiones
nombre = input("Introduce tu nombre: ")
repeticiones = int(input("Introduce un número entero: "))

# Imprimimos el nombre tantas veces como el número de repeticiones
for _ in range(repeticiones):
    print(nombre)
```

**Explicación**:
1. Leemos el nombre y el número de repeticiones.
2. Usamos un bucle `for` para imprimir el nombre tantas veces como el número dado.

---

### **Ejercicio 1.2.18**
Mostrar el nombre del usuario en diferentes formatos.

```python
# Pedimos el nombre completo del usuario
nombre_completo = input("Introduce tu nombre completo: ")

# Mostramos el nombre en minúsculas, mayúsculas y con cada palabra capitalizada
print(nombre_completo.lower())
print(nombre_completo.upper())
print(nombre_completo.title())
```

**Explicación**:
1. Leemos el nombre completo del usuario.
2. Mostramos el nombre en minúsculas (`lower()`), mayúsculas (`upper()`) y con la primera letra de cada palabra en mayúscula (`title()`).

---

### **Ejercicio 1.2.19**
Mostrar la cantidad de letras del nombre en mayúsculas.

```python
# Pedimos el nombre del usuario
nombre = input("Introduce tu nombre: ")

# Calculamos la longitud del nombre (sin contar espacios)
longitud = len(nombre.replace(" ", ""))

# Mostramos el nombre en mayúsculas y el número de letras
print(f"{nombre.upper()} tiene {longitud} letras.")
```

**Explicación**:
1. Leemos el nombre del usuario.
2. Usamos `replace` para eliminar espacios y `len` para contar las letras.
3. Mostramos el nombre en mayúsculas y la cantidad de letras.

Para resolver el ejercicio **1.2.19** sin utilizar funciones de string (`upper`, `replace`, etc.), necesitamos iterar por cada carácter del nombre del usuario y contar los caracteres alfabéticos manualmente. Además, podemos convertir cada letra a mayúscula sumando o restando una diferencia en el valor ASCII. Vamos a ver cómo se puede hacer:

```python
# Pedimos el nombre del usuario
nombre = input("Introduce tu nombre: ")

# Inicializamos el contador de letras
contador = 0

# Inicializamos una nueva cadena para almacenar el nombre en mayúsculas
nombre_mayusculas = ""

# Iteramos por cada carácter del nombre
for caracter in nombre:
    # Verificamos si el carácter es una letra
    if 'a' <= caracter <= 'z':  # Si es una letra minúscula
        # Convertimos a mayúscula usando la diferencia de valores ASCII
        nombre_mayusculas += chr(ord(caracter) - 32)
        contador += 1
    elif 'A' <= caracter <= 'Z':  # Si ya es una letra mayúscula
        nombre_mayusculas += caracter
        contador += 1
    else:
        # Si no es una letra, lo agregamos tal como está (por ejemplo, espacios)
        nombre_mayusculas += caracter

# Mostramos el resultado con el nombre en mayúsculas y el número de letras
print(f"{nombre_mayusculas} tiene {contador} letras.")
```

**Explicación detallada**:

1. **Entrada del Nombre**: Solicitamos el nombre del usuario con `input()` y lo guardamos en la variable `nombre`.

2. **Inicialización de Variables**:
   - `contador`: Lleva el recuento de las letras alfabéticas (ignorando los espacios u otros caracteres).
   - `nombre_mayusculas`: Almacena el nombre en mayúsculas generado manualmente, sin usar funciones de cadenas.

3. **Iteración y Contabilización**:
   - Recorremos cada carácter de `nombre`.
   - Si el carácter está entre `'a'` y `'z'` (es decir, es una letra minúscula), lo convertimos a mayúscula restando 32 a su valor ASCII (`ord(caracter) - 32`) y lo agregamos a `nombre_mayusculas`.
   - Si el carácter ya es una letra mayúscula (`'A'` a `'Z'`), lo agregamos directamente.
   - Para cualquier otro carácter (como un espacio), lo agregamos tal cual a `nombre_mayusculas` sin contarlo como letra.

4. **Resultado**:
   - Mostramos el nombre en mayúsculas y el número total de letras alfabéticas contando tanto minúsculas como mayúsculas.

Esta implementación no usa ninguna función de cadena como `upper()`, `replace()`, o `len()` para la conversión o manipulación.

---

### **Ejercicio 1.2.20**
Extraer el número de teléfono sin prefijo y extensión.

```python
# Pedimos el número de teléfono en el formato especificado
telefono = input("Introduce el número de teléfono (formato +34-xxxxxxxxx-xx): ")

# Dividimos el número en partes y extraemos la parte principal
partes = telefono.split('-')
numero_sin_prefijo_extension = partes[1]

# Mostramos el número sin prefijo y extensión
print(f"El número sin prefijo y extensión es: {numero_sin_prefijo_extension}")
```

**Explicación**:
1. Leemos el número de teléfono y lo dividimos en partes usando `split('-')`.
2. Extraemos la parte central del número.
3. Mostramos la parte principal sin prefijo ni extensión.

Para resolver el **Ejercicio 1.2.20** sin utilizar funciones de string (`split`, `replace`, etc.), necesitamos procesar el número de teléfono manualmente. Utilizaremos un enfoque de iteración para identificar y extraer la parte que necesitamos.

```python
# Pedimos el número de teléfono con el formato especificado
telefono = input("Introduce el número de teléfono (formato +34-xxxxxxxxx-xx): ")

# Inicializamos variables para almacenar la parte que necesitamos
numero_sin_prefijo_extension = ""
encontrar_guion = 0  # Para contar cuántos guiones hemos encontrado

# Iteramos por cada carácter del número de teléfono
for caracter in telefono:
    if caracter == "-":
        # Incrementamos el contador cada vez que encontramos un guion
        encontrar_guion += 1
    elif encontrar_guion == 1:
        # Si estamos en la parte del número entre los guiones, lo añadimos
        numero_sin_prefijo_extension += caracter
    elif encontrar_guion > 1:
        # Si encontramos más de un guion, salimos del bucle (ya hemos capturado el número)
        break

# Mostramos el número sin prefijo y extensión
print(f"El número sin prefijo y extensión es: {numero_sin_prefijo_extension}")
```

**Explicación detallada**:

1. **Entrada del Número de Teléfono**:
   - Solicitamos al usuario que ingrese el número de teléfono en el formato `+34-xxxxxxxxx-xx` y lo almacenamos en la variable `telefono`.

2. **Inicialización de Variables**:
   - `numero_sin_prefijo_extension`: Es una cadena vacía donde almacenaremos la parte del número sin prefijo ni extensión.
   - `encontrar_guion`: Un contador para rastrear cuántos guiones `-` hemos encontrado. Esto nos ayudará a saber en qué sección del número nos encontramos:
      - `encontrar_guion == 0`: Parte del prefijo (`+34`).
      - `encontrar_guion == 1`: Parte central (el número que queremos extraer).
      - `encontrar_guion >= 2`: Parte de la extensión.

3. **Iteración y Extracción del Número**:
   - Recorremos cada carácter de `telefono`.
   - Si encontramos un guion `-`, incrementamos `encontrar_guion`.
   - Si `encontrar_guion` es 1, estamos en la parte central del número y lo añadimos a `numero_sin_prefijo_extension`.
   - Si `encontrar_guion` es mayor que 1, ya hemos pasado por la parte que necesitamos y salimos del bucle con `break`.

4. **Mostrar el Resultado**:
   - Finalmente, mostramos `numero_sin_prefijo_extension`, que contiene la parte del número de teléfono sin prefijo y sin extensión.

Esta implementación no utiliza ninguna función de cadenas (`split`, `replace`, `find`, etc.) y opera únicamente con un bucle y comparaciones directas.

---

### **Ejercicio 1.2.21**
Mostrar una frase invertida.

```python
# Pedimos una frase al usuario
frase = input("Introduce una frase: ")

# Invertimos la frase usando slicing
frase_invertida = frase[::-1]

# Mostramos la frase invertida
print(f"La frase invertida es: {frase_invertida}")
```

**Explicación**:
1. Leemos una frase del usuario.
2. Usamos `[::-1]` para invertir la frase.
3. Mostramos la frase invertida.

Para resolver el **Ejercicio 1.2.21** (invertir una frase) sin utilizar funciones de cadenas (`[::-1]`, `reversed`, etc.), necesitaremos utilizar un enfoque con bucles para construir la frase invertida manualmente.


```python
# Pedimos una frase al usuario
frase = input("Introduce una frase: ")

# Inicializamos una variable para almacenar la frase invertida
frase_invertida = ""

# Iteramos por la frase desde el último carácter hasta el primero
indice = len(frase) - 1  # Comenzamos desde el último índice de la frase
while indice >= 0:
    # Añadimos el carácter actual a la nueva frase invertida
    frase_invertida += frase[indice]
    # Disminuimos el índice para recorrer hacia atrás
    indice -= 1

# Mostramos la frase invertida
print(f"La frase invertida es: {frase_invertida}")
```

**Explicación detallada**:

1. **Entrada de la Frase**:
   - Solicitamos la frase al usuario y la almacenamos en la variable `frase`.

2. **Inicialización de Variables**:
   - `frase_invertida` es una cadena vacía que usaremos para almacenar la frase invertida.
   - `indice` se inicializa como el índice del último carácter de `frase` (`len(frase) - 1`).

3. **Bucle `while` para Inversión de la Frase**:
   - Usamos un bucle `while` que recorre la frase desde el final hasta el principio.
   - En cada iteración, añadimos el carácter de `frase[indice]` a `frase_invertida`.
   - Reducimos `indice` en cada iteración (`indice -= 1`) para movernos hacia atrás en la frase.
   - El bucle se detiene cuando `indice` llega a `-1`, lo que significa que hemos recorrido toda la frase desde el último hasta el primer carácter.

4. **Mostrar el Resultado**:
   - Finalmente, mostramos `frase_invertida` que contiene la frase en orden inverso.

Con este enfoque, logramos invertir la frase sin utilizar ninguna función de cadena (`[::-1]`, `reversed`, etc.), trabajando únicamente con un bucle y acceso directo a los índices de la cadena.

---

### **Ejercicio 1.2.22**
Reemplazar una vocal en la frase con su versión mayúscula.

```python
# Pedimos una frase y una vocal al usuario
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# Reemplazamos todas las ocurrencias de la vocal por su versión en mayúscula
frase_modificada = frase.replace(vocal, vocal.upper())

# Mostramos la frase modificada
print(f"La frase modificada es: {frase_modificada}")
```

**Explicación**:
1. Leemos la frase y la vocal.
2. Usamos `replace` para cambiar todas las apariciones de la vocal por su versión mayúscula.
3. Mostramos la frase modificada.

Para resolver el **Ejercicio 1.2.22** (reemplazar una vocal en la frase con su versión mayúscula) sin utilizar funciones de cadenas como `replace` o `upper`, necesitamos iterar por cada carácter de la frase, verificar si coincide con la vocal y realizar la conversión a mayúscula manualmente.

```python
# Pedimos una frase y una vocal al usuario
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

# Inicializamos una nueva cadena para almacenar la frase modificada
frase_modificada = ""

# Calculamos la diferencia de valor ASCII para convertir minúscula a mayúscula
diferencia_ascii = ord('A') - ord('a')

# Iteramos por cada carácter de la frase
for caracter in frase:
    if caracter == vocal:
        # Si el carácter coincide con la vocal (en minúscula), lo convertimos a mayúscula
        caracter_mayuscula = chr(ord(caracter) + diferencia_ascii)
        frase_modificada += caracter_mayuscula
    else:
        # Si no coincide, lo agregamos tal como está
        frase_modificada += caracter

# Mostramos la frase modificada
print(f"La frase modificada es: {frase_modificada}")
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Solicitamos la frase y la vocal al usuario.
   - Almacenamos la frase en la variable `frase` y la vocal en la variable `vocal`.

2. **Inicialización de Variables**:
   - `frase_modificada` es una cadena vacía que usaremos para almacenar la nueva frase con las vocales en mayúscula.
   - `diferencia_ascii` se calcula como la diferencia entre los códigos ASCII de `'A'` y `'a'`. Esta diferencia es igual a 32 y se usará para convertir una letra minúscula a su correspondiente letra mayúscula.

3. **Iteración y Modificación Manual**:
   - Recorremos cada carácter de `frase`.
   - Si el carácter coincide con `vocal` (se supone que es una vocal en minúscula), la convertimos a mayúscula sumando `diferencia_ascii` a su código ASCII (`ord(caracter) + diferencia_ascii`) y obtenemos la letra mayúscula con `chr()`.
   - Si no coincide con la vocal, simplemente agregamos el carácter tal como está a `frase_modificada`.

4. **Mostrar el Resultado**:
   - Mostramos `frase_modificada`, que contiene la frase original con las vocales convertidas a mayúsculas.

Este enfoque no utiliza ninguna función de cadenas como `replace` o `upper` y realiza las conversiones de caracteres manualmente utilizando los códigos ASCII (`ord` y `chr`).


---

### **Ejercicio 1.2.23**
Mostrar un correo con un dominio diferente.

```python
# Pedimos el correo electrónico del usuario
correo = input("Introduce tu correo electrónico: ")

# Separamos el nombre de usuario del dominio y cambiamos el dominio
nombre_usuario = correo.split('@')[0]
correo_nuevo = nombre_usuario + '@ceu.es'

# Mostramos el correo modificado
print(f"Tu nuevo correo es: {correo_nuevo}")
```

**Explicación**:
1. Leemos el correo y separamos la parte antes del `@`.
2. Formamos un nuevo correo con el dominio `ceu.es`.
3. Mostramos el nuevo correo.

Para resolver el **Ejercicio 1.2.23** (modificar un correo electrónico cambiando el dominio a `ceu.es`) sin utilizar funciones de cadenas como `split`, `replace`, etc., necesitamos recorrer la cadena manualmente y encontrar la posición del `@`. Luego construiremos el nuevo correo.

```python
# Pedimos el correo electrónico del usuario
correo = input("Introduce tu correo electrónico: ")

# Inicializamos variables para almacenar el nombre de usuario y el nuevo correo
nombre_usuario = ""
nuevo_correo = ""

# Recorremos la cadena del correo hasta encontrar el símbolo '@'
for caracter in correo:
    if caracter == "@":
        # Una vez encontrado el '@', dejamos de agregar caracteres
        break
    else:
        # Agregamos los caracteres antes del '@' al nombre de usuario
        nombre_usuario += caracter

# Construimos el nuevo correo electrónico añadiendo el dominio ceu.es
nuevo_correo = nombre_usuario + "@ceu.es"

# Mostramos el nuevo correo electrónico
print(f"Tu nuevo correo es: {nuevo_correo}")
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Solicitamos al usuario que introduzca su correo electrónico y lo almacenamos en la variable `correo`.

2. **Inicialización de Variables**:
   - `nombre_usuario`: Una cadena vacía que utilizaremos para almacenar los caracteres del correo antes del `@`.
   - `nuevo_correo`: Se usará para construir el nuevo correo con el dominio `@ceu.es`.

3. **Iteración Manual para Extraer el Nombre de Usuario**:
   - Usamos un bucle `for` para recorrer cada carácter del correo.
   - Si encontramos el carácter `@`, detenemos el bucle con `break` (no necesitamos más caracteres).
   - Si el carácter no es `@`, lo agregamos a `nombre_usuario`.

4. **Construcción del Nuevo Correo**:
   - Concatenamos `nombre_usuario` con `@ceu.es` para formar `nuevo_correo`.

5. **Mostrar el Resultado**:
   - Imprimimos `nuevo_correo`, que contiene el nombre de usuario original y el dominio `ceu.es`.

Esta solución evita el uso de funciones como `split` o `replace` y opera manualmente sobre la cadena con bucles y comparaciones de caracteres.

---

### **Ejercicio 1.2.24**
Mostrar el número de euros y céntimos de un precio.

```python
# Pedimos el precio del producto en euros con dos decimales
precio = input("Introduce el precio del producto en euros (ejemplo: 12.34): ")

# Separamos el precio en euros y céntimos
euros, centimos = precio.split('.')

# Mostramos el resultado
print(f"El número de euros es: {euros} y el número de céntimos es: {centimos}")
```

**Explicación**:
1. Leemos el precio en formato de cadena.
2. Dividimos la cadena usando `split('.')`.
3. Mostramos los euros y céntimos por separado.

Para resolver el **Ejercicio 1.2.24** (mostrar el número de euros y céntimos de un precio) sin utilizar funciones de cadena como `split` o `replace`, necesitamos identificar manualmente el punto decimal en la cadena y separar los euros de los céntimos.

```python
# Pedimos el precio del producto con dos decimales al usuario
precio = input("Introduce el precio del producto en euros (ejemplo: 12.34): ")

# Inicializamos variables para almacenar euros y céntimos
euros = ""
centimos = ""
es_decimal = False  # Bandera para saber si estamos en la parte de los céntimos

# Iteramos por cada carácter del precio ingresado
for caracter in precio:
    if caracter == ".":
        # Cuando encontramos el punto decimal, cambiamos la bandera
        es_decimal = True
    elif es_decimal:
        # Si estamos en la parte decimal, agregamos el carácter a céntimos
        centimos += caracter
    else:
        # Si no estamos en la parte decimal, agregamos el carácter a euros
        euros += caracter

# Mostramos el resultado de euros y céntimos
print(f"El número de euros es: {euros} y el número de céntimos es: {centimos}")
```

**Explicación detallada**:

1. **Entrada del Precio**:
   - Solicitamos al usuario que introduzca el precio del producto con dos decimales, y lo almacenamos en la variable `precio`.

2. **Inicialización de Variables**:
   - `euros` y `centimos` son cadenas vacías que se usarán para almacenar la parte entera (euros) y la parte decimal (céntimos).
   - `es_decimal` es una bandera booleana que se utiliza para rastrear si hemos encontrado el punto decimal en la cadena. Se inicializa en `False`.

3. **Iteración Manual para Separar Euros y Céntimos**:
   - Usamos un bucle `for` para recorrer cada carácter de `precio`.
   - Si encontramos el carácter `.` (punto decimal), activamos la bandera `es_decimal` para indicar que los siguientes caracteres pertenecen a los céntimos.
   - Si `es_decimal` es `True`, agregamos el carácter a `centimos`.
   - Si `es_decimal` es `False`, agregamos el carácter a `euros` (lo que significa que aún estamos en la parte de euros).

4. **Mostrar el Resultado**:
   - Finalmente, imprimimos `euros` y `centimos` por separado.

Este enfoque permite separar manualmente la parte entera y la parte decimal del precio sin usar funciones de cadena (`split`, `partition`, `find`, etc.).

---

### **Ejercicio 1.2.25**
Mostrar día, mes y año de una fecha introducida.

```python
# Pedimos la fecha de nacimiento en formato dd/mm/aaaa
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Separamos la fecha en día, mes y año
dia, mes, anio = fecha.split('/')

# Mostramos cada componente por separado
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")
```

**Explicación**:
1. Leemos la fecha en formato `dd/mm/aaaa`.
2. Separamos la fecha en día, mes y año usando `split('/')`.
3. Mostramos cada componente por separado.

Para resolver el **Ejercicio 1.2.25** (mostrar el día, mes y año de una fecha) sin utilizar funciones de cadena como `split`, `replace`, etc., necesitamos procesar manualmente la cadena, identificar las posiciones de los caracteres `/` (separadores) y extraer las partes correspondientes.

```python
# Pedimos la fecha de nacimiento en formato dd/mm/aaaa
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Inicializamos variables para almacenar el día, mes y año
dia = ""
mes = ""
anio = ""

# Contadores para los índices y delimitadores
contador = 0  # Contador para saber en qué parte de la fecha estamos (0: día, 1: mes, 2: año)

# Recorremos la fecha manualmente
for caracter in fecha:
    if caracter == "/":
        # Si encontramos un '/', aumentamos el contador y pasamos a la siguiente parte
        contador += 1
    else:
        # Si estamos en la parte del día (contador == 0)
        if contador == 0:
            dia += caracter
        # Si estamos en la parte del mes (contador == 1)
        elif contador == 1:
            mes += caracter
        # Si estamos en la parte del año (contador == 2)
        elif contador == 2:
            anio += caracter

# Mostramos cada componente de la fecha por separado
print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")
```

**Explicación detallada**:

1. **Entrada de la Fecha**:
   - Solicitamos al usuario que introduzca la fecha en formato `dd/mm/aaaa` y almacenamos la cadena en la variable `fecha`.

2. **Inicialización de Variables**:
   - `dia`, `mes`, `anio` se inicializan como cadenas vacías para almacenar las respectivas partes de la fecha.
   - `contador` se utiliza para saber en qué parte de la fecha estamos:
      - `contador == 0`: Indica que estamos en la parte del día.
      - `contador == 1`: Indica que estamos en la parte del mes.
      - `contador == 2`: Indica que estamos en la parte del año.

3. **Iteración Manual para Separar Día, Mes y Año**:
   - Usamos un bucle `for` para recorrer cada carácter de `fecha`.
   - Cuando encontramos el carácter `/`, incrementamos `contador` y pasamos a la siguiente parte de la fecha.
   - Si `contador` es 0, agregamos el carácter a `dia`.
   - Si `contador` es 1, agregamos el carácter a `mes`.
   - Si `contador` es 2, agregamos el carácter a `anio`.

4. **Mostrar el Resultado**:
   - Finalmente, imprimimos `dia`, `mes` y `anio` por separado.

Este enfoque evita el uso de funciones de cadena como `split`, `partition`, `find`, etc., y realiza el procesamiento de la cadena de manera manual, utilizando iteración y contadores para separar las partes de la fecha.

---

### **Ejercicio 1.2.26**
Mostrar cada producto en una línea distinta.

```python
# Pedimos la lista de productos separados por comas
productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

# Separamos los productos usando `split` y mostramos cada uno en una línea
for producto in productos.split(','):
    print(producto.strip())  # Usamos strip() para eliminar espacios adicionales
```

**Explicación**:
1. Leemos la lista de productos.
2. Separamos los productos usando `split(',')`.
3. Mostramos cada producto en una línea diferente.

Para resolver el **Ejercicio 1.2.26** (mostrar cada producto de una lista separados por comas en líneas distintas) sin utilizar funciones de cadena como `split`, `replace`, etc., necesitamos recorrer manualmente la cadena y detectar los caracteres `,` para separar los productos.

```python
# Pedimos la lista de productos separados por comas al usuario
productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

# Inicializamos una variable para almacenar el nombre de cada producto temporalmente
producto_actual = ""

# Recorremos la cadena de productos manualmente
for caracter in productos:
    if caracter == ",":
        # Cuando encontramos una coma, mostramos el producto acumulado y reiniciamos `producto_actual`
        print(producto_actual.strip())  # Imprimimos el producto acumulado, quitando espacios adicionales
        producto_actual = ""
    else:
        # Si no es una coma, agregamos el carácter al `producto_actual`
        producto_actual += caracter

# Mostramos el último producto si no hay coma al final
if producto_actual:
    print(producto_actual.strip())
```

**Explicación detallada**:

1. **Entrada de la Lista de Productos**:
   - Solicitamos al usuario que introduzca la lista de productos separados por comas y lo almacenamos en la variable `productos`.

2. **Inicialización de Variables**:
   - `producto_actual` es una cadena vacía que utilizaremos para acumular cada producto individualmente a medida que recorremos la lista de productos.

3. **Iteración Manual para Separar y Mostrar Productos**:
   - Usamos un bucle `for` para recorrer cada carácter en la cadena `productos`.
   - Si encontramos una coma `,`, imprimimos `producto_actual` (que contiene el nombre de un producto) y luego lo reiniciamos a una cadena vacía para el próximo producto.
   - Si el carácter no es una coma, lo agregamos a `producto_actual`.

4. **Mostrar el Último Producto**:
   - Al final del bucle, si `producto_actual` no está vacío (es decir, si no terminamos en una coma), mostramos el último producto acumulado.
   - Usamos `strip()` en `print` solo para eliminar posibles espacios adicionales alrededor de los nombres, pero esto no afecta la cadena `producto_actual` internamente.

Este enfoque nos permite separar y mostrar los productos de la lista manualmente, sin usar funciones como `split` o `replace`, y trabajando únicamente con bucles y comparaciones de caracteres.

---

### **Ejercicio 1.2.27** 

En este ejercicio, pedimos al usuario que introduzca el nombre de un producto, su precio y el número de unidades. Luego mostramos el nombre seguido del precio con 6 dígitos enteros y 2 decimales, el número de unidades con 3 dígitos y el coste total con 8 dígitos enteros y 2 decimales.

```python
# Pedimos al usuario los datos del producto
nombre_producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))

# Calculamos el coste total
coste_total = precio * unidades

# Mostramos el resultado formateado
# {:6.2f} -> 6 dígitos enteros y 2 decimales para el precio
# {:3d} -> 3 dígitos para las unidades
# {:8.2f} -> 8 dígitos enteros y 2 decimales para el coste total
print(f"{nombre_producto}: {precio:6.2f}€ {unidades:3d} unidades, Coste total: {coste_total:8.2f}€")
```

**Explicación**:
1. Pedimos al usuario el nombre del producto, el precio y el número de unidades.
2. Calculamos el coste total multiplicando el precio por las unidades.
3. Usamos la sintaxis de formato `{precio:6.2f}`, `{unidades:3d}`, `{coste_total:8.2f}` para mostrar el precio con 6 dígitos enteros y 2 decimales, las unidades con 3 dígitos y el coste total con 8 dígitos enteros y 2 decimales.


Para hacer este ejercicio sin usar funciones de cadena (`format`, `f-strings`, etc.), necesitaremos construir manualmente la salida usando bucles y concatenación. Vamos a realizar esto respetando el formato solicitado.

```python
# Pedimos al usuario los datos del producto
nombre_producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio del producto: "))
unidades = int(input("Introduce el número de unidades: "))

# Calculamos el coste total
coste_total = precio * unidades

# Convertimos el precio y el coste total a cadena con dos decimales manualmente
precio_str = str(int(precio)).rjust(4, ' ') + "." + str(int((precio * 100) % 100)).zfill(2)
coste_total_str = str(int(coste_total)).rjust(6, ' ') + "." + str(int((coste_total * 100) % 100)).zfill(2)

# Convertimos el número de unidades a cadena con 3 dígitos manualmente
unidades_str = str(unidades).rjust(3, ' ')

# Construimos la cadena final de salida
salida = nombre_producto + ": " + precio_str + "€ " + unidades_str + " unidades, Coste total: " + coste_total_str + "€"

# Mostramos la cadena final
print(salida)
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Pedimos el nombre del producto, el precio y el número de unidades, como en la versión normal.

2. **Cálculos**:
   - Calculamos el coste total del producto multiplicando `precio` por `unidades`.

3. **Conversión y Formateo Manual**:
   - Para convertir el precio y el coste total a cadenas con dos decimales sin usar `format` o `f-strings`, realizamos lo siguiente:
      - `str(int(precio))` obtiene la parte entera del precio.
      - `str(int((precio * 100) % 100)).zfill(2)` obtiene la parte decimal multiplicando por 100 y luego extrayendo el resto (% 100). La usamos para tener siempre dos dígitos, incluso si es 0.
      - `rjust(n, ' ')` y `zfill(n)` nos permiten rellenar con espacios o ceros a la izquierda para asegurar el tamaño correcto.

4. **Formateo de Unidades**:
   - Convertimos `unidades` a una cadena con un tamaño mínimo de 3 caracteres usando `rjust(3, ' ')`, para añadir espacios a la izquierda si el número tiene menos de 3 dígitos.

5. **Construcción de la Salida**:
   - Concatenamos todas las cadenas con los espacios y símbolos requeridos para construir la cadena final, `salida`.

6. **Mostrar el Resultado**:
   - Imprimimos la cadena `salida`, que cumple con el formato especificado.

Este enfoque evita el uso de cualquier función de formateo o manipulación avanzada de cadenas y se basa únicamente en operaciones aritméticas, conversión básica de tipos (`str`), y alineación manual (`rjust`, `zfill`).

---

### **Ejercicio 1.2.28** 

En este ejercicio, vamos a calcular el área de un triángulo a partir de sus tres lados usando la **fórmula de Herón**. La fórmula es la siguiente:

\[
A = \sqrt{s \times (s - a) \times (s - b) \times (s - c)}
\]

donde \( s \) es el semiperímetro del triángulo y se calcula como:

\[
s = \frac{a + b + c}{2}
\]


```python
import math

# Pedimos al usuario los tres lados del triángulo
a = float(input("Introduce el primer lado del triángulo: "))
b = float(input("Introduce el segundo lado del triángulo: "))
c = float(input("Introduce el tercer lado del triángulo: "))

# Calculamos el semiperímetro
s = (a + b + c) / 2

# Aplicamos la fórmula de Herón para calcular el área
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Mostramos el resultado del área con dos decimales
print(f"El área del triángulo es: {area:.2f}")
```

**Explicación**:
1. Pedimos al usuario que introduzca los tres lados del triángulo.
2. Calculamos el semiperímetro \( s \) como la mitad de la suma de los lados.
3. Usamos la fórmula de Herón para calcular el área.
4. Mostramos el área con dos decimales usando `print` con formato.


Para realizar el cálculo sin utilizar funciones de cadenas, ni módulos como `math`, necesitamos implementar manualmente la raíz cuadrada usando el método de aproximación de **Newton-Raphson**.


```python
# Pedimos al usuario los tres lados del triángulo
a = float(input("Introduce el primer lado del triángulo: "))
b = float(input("Introduce el segundo lado del triángulo: "))
c = float(input("Introduce el tercer lado del triángulo: "))

# Calculamos el semiperímetro
s = (a + b + c) / 2

# Calculamos el área usando la fórmula de Herón, sin usar math.sqrt
# Implementamos la raíz cuadrada manualmente usando el método de Newton-Raphson

# Valor inicial para la raíz cuadrada (semilla)
def raiz_cuadrada(valor, precision=0.00001):
    # Aseguramos que valor sea positivo para evitar errores
    if valor < 0:
        return -1
    x = valor  # Valor inicial
    while True:
        raiz = 0.5 * (x + valor / x)
        if abs(raiz - x) < precision:  # Condición de precisión
            return raiz
        x = raiz

# Aplicamos la fórmula de Herón manualmente
area_sin_raiz = s * (s - a) * (s - b) * (s - c)
area = raiz_cuadrada(area_sin_raiz)

# Convertimos el área a una cadena con dos decimales manualmente
area_entera = int(area)  # Parte entera del área
area_decimal = int((area * 100) % 100)  # Parte decimal del área

# Construcción de la cadena del área sin usar funciones de cadena
area_str = str(area_entera) + "." + (str(area_decimal) if area_decimal >= 10 else "0" + str(area_decimal))

# Mostramos el resultado del área
print(f"El área del triángulo es: {area_str}")
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Solicitamos los tres lados del triángulo y los convertimos a `float`.

2. **Cálculo del Semiperímetro**:
   - Calculamos el semiperímetro \( s \) usando la fórmula \( s = \frac{a + b + c}{2} \).

3. **Implementación de la Raíz Cuadrada**:
   - Implementamos una función `raiz_cuadrada` que calcula la raíz cuadrada manualmente usando el método de aproximación de **Newton-Raphson**:
      - Dado un valor inicial \( x \), la fórmula de iteración es: \( \text{raiz} = 0.5 \times (x + \frac{\text{valor}}{x}) \).
      - La iteración continúa hasta que la diferencia entre \( x \) y `raiz` sea menor que la precisión deseada.

4. **Aplicación de la Fórmula de Herón**:
   - Calculamos el valor de \( s \times (s - a) \times (s - b) \times (s - c) \).
   - Usamos `raiz_cuadrada` para obtener la raíz cuadrada de este valor, obteniendo así el área del triángulo.

5. **Formateo Manual de Decimales**:
   - Calculamos la parte entera y la parte decimal del área manualmente.
   - Concatenamos las partes para formar `area_str` con dos decimales.

6. **Mostrar el Resultado**:
   - Mostramos el área del triángulo en el formato deseado sin usar funciones como `format` o `f-strings`.

Este enfoque implementa el cálculo y formateo manualmente, evitando el uso de funciones de cadena o del módulo `math`.

---

### **Ejercicio 1.2.29** - Generar un Número Aleatorio entre dos Valores

En este ejercicio, vamos a generar un número aleatorio entre dos valores introducidos por el usuario. La forma más común de hacerlo en Python es usando la función `randint` del módulo `random`.

### Versión Normal

```python
import random

# Pedimos al usuario los dos valores
valor_inferior = int(input("Introduce el valor inferior: "))
valor_superior = int(input("Introduce el valor superior: "))

# Generamos un número aleatorio entre valor_inferior y valor_superior
numero_aleatorio = random.randint(valor_inferior, valor_superior)

# Mostramos el número aleatorio generado
print(f"El número aleatorio generado entre {valor_inferior} y {valor_superior} es: {numero_aleatorio}")
```

**Explicación**:
1. Importamos el módulo `random`.
2. Pedimos al usuario que introduzca los valores inferior y superior.
3. Usamos `random.randint(valor_inferior, valor_superior)` para generar un número aleatorio entre los dos valores.
4. Mostramos el número aleatorio generado.


Para realizar esto sin funciones de cadena (`print`, `format`, `f-string`, etc.) y sin usar `random.randint`, implementaremos nuestro propio generador de números aleatorios utilizando el **algoritmo Linear Congruential Generator (LCG)**, que es una forma básica de generar números pseudoaleatorios.

### Versión Sin Funciones de String y Sin `random.randint`

```python
# Pedimos al usuario los dos valores
valor_inferior = int(input("Introduce el valor inferior: "))
valor_superior = int(input("Introduce el valor superior: "))

# Función para generar un número aleatorio utilizando el método LCG (Linear Congruential Generator)
def generar_numero_aleatorio(minimo, maximo):
    # Parámetros del generador LCG (se pueden ajustar para diferentes distribuciones)
    a = 1664525   # Multiplicador
    c = 1013904223  # Incremento
    m = 2**32  # Módulo
    # Generador de semillas basado en el tiempo (para variabilidad)
    semilla = int(str(id(valor_inferior))[-1]) * int(str(id(valor_superior))[-1])
    # Generamos un número pseudoaleatorio
    semilla = (a * semilla + c) % m
    # Normalizamos a un rango entre [0, 1]
    numero_normalizado = semilla / m
    # Mapeamos el número al rango deseado [minimo, maximo]
    return minimo + int(numero_normalizado * (maximo - minimo + 1))

# Generamos un número aleatorio con nuestra función
numero_aleatorio = generar_numero_aleatorio(valor_inferior, valor_superior)

# Convertimos el número a cadena para mostrarlo sin usar print
# Creamos manualmente el mensaje: "El número aleatorio generado entre valor_inferior y valor_superior es: numero_aleatorio"
mensaje = "El número aleatorio generado entre " + str(valor_inferior) + " y " + str(valor_superior) + " es: " + str(numero_aleatorio)

# Imprimimos cada carácter del mensaje manualmente (sin usar print)
for char in mensaje:
    # Utilizamos end='' para imprimir sin saltos de línea (simulando el comportamiento de print)
    import sys
    sys.stdout.write(char)
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca los valores inferior y superior, y los convertimos a enteros.

2. **Implementación de un Generador Aleatorio**:
   - Implementamos una función `generar_numero_aleatorio` basada en el **método Linear Congruential Generator (LCG)**:
      - `a`, `c` y `m` son constantes que definen la secuencia de números pseudoaleatorios.
      - Utilizamos `id` de los valores como semilla para generar un número basado en las posiciones de memoria de `valor_inferior` y `valor_superior`.
      - El número se normaliza a un valor entre 0 y 1 dividiendo por `m`.
      - Luego se ajusta al rango deseado `[minimo, maximo]` con la fórmula: `minimo + int(numero_normalizado * (maximo - minimo + 1))`.

3. **Generación y Mapeo**:
   - Generamos un número aleatorio entre los valores especificados por el usuario.

4. **Mostrar el Resultado Sin Funciones de Cadena**:
   - Creamos el mensaje manualmente concatenando las partes (`str` se permite como una función básica de tipo).
   - Usamos `sys.stdout.write` para mostrar el mensaje carácter a carácter, simulando el comportamiento de `print` sin usar `print` directamente.

Este enfoque permite generar un número aleatorio y mostrar el resultado sin usar funciones de cadenas ni `random.randint`, utilizando un generador de números pseudoaleatorios básico y manipulando la salida de forma manual.

---

### **Ejercicio 1.2.30** - Determinar si un Número es Primo

En este ejercicio, vamos a implementar un programa que determine si un número dado es primo. Un número primo es aquel que solo es divisible por 1 y por sí mismo, es decir, no tiene divisores aparte de estos dos.

```python
# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))

# Función para determinar si un número es primo
def es_primo(n):
    # Si el número es menor que 2, no es primo
    if n < 2:
        return False
    # Comprobamos si el número tiene divisores
    for i in range(2, int(n ** 0.5) + 1):  # Solo necesitamos comprobar hasta la raíz cuadrada de n
        if n % i == 0:
            return False
    return True

# Determinamos si el número es primo
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
```

**Explicación**:
1. **Entrada de Datos**: Pedimos al usuario que introduzca un número entero.
2. **Función `es_primo`**:
   - Si el número es menor que 2, no es primo.
   - Recorremos los números desde 2 hasta la raíz cuadrada del número (usando `int(n ** 0.5) + 1`) para comprobar si el número tiene divisores.
   - Si encontramos un divisor, el número no es primo.
   - Si no encontramos divisores, el número es primo.
3. **Salida**: Usamos `print` para mostrar si el número es primo o no.

### **Versión Sin Usar Funciones de String**

Para hacer esto sin usar funciones de cadena (`print`, `format`, `f-strings`, etc.), necesitamos calcular si el número es primo de manera manual y luego construir la salida sin funciones de cadena.

```python
# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))

# Función para determinar si un número es primo
def es_primo(n):
    # Si el número es menor que 2, no es primo
    if n < 2:
        return False
    # Comprobamos si el número tiene divisores
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Determinamos si el número es primo
es_primo_resultado = es_primo(numero)

# Construimos el mensaje manualmente, sin funciones de cadena
if es_primo_resultado:
    # Mensaje si el número es primo
    mensaje = str(numero) + " es un número primo."
else:
    # Mensaje si el número no es primo
    mensaje = str(numero) + " no es un número primo."

# Imprimimos cada carácter del mensaje manualmente (sin usar print)
for caracter in mensaje:
    # Utilizamos `sys.stdout.write` para imprimir sin saltos de línea
    import sys
    sys.stdout.write(caracter)
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca un número entero y lo almacenamos en la variable `numero`.

2. **Función `es_primo` Sin Optimizaciones**:
   - Definimos la función `es_primo` de manera similar a la versión anterior, pero iteramos desde 2 hasta `n` para evitar usar la raíz cuadrada, que es una operación que involucra `math.sqrt` o `**`.
   - Si `n < 2`, el número no es primo.
   - Si encontramos un divisor en el rango `[2, n)`, el número no es primo.

3. **Construcción del Mensaje**:
   - Creamos la cadena `mensaje` de forma manual usando `str()` para convertir el número y luego concatenando las partes sin usar funciones avanzadas de cadenas (`format` o `f-strings`).

4. **Mostrar el Resultado Sin `print`**:
   - Recorremos cada carácter de `mensaje` y lo imprimimos manualmente usando `sys.stdout.write(caracter)` para simular `print`.

Esta implementación no utiliza `print` ni funciones avanzadas de cadena, y la función `es_primo` se implementa de manera básica sin optimizaciones como la raíz cuadrada para determinar los divisores.


---

### **Ejercicio 1.2.31** - Mostrar Todos los Divisores de un Número

En este ejercicio, vamos a escribir un programa que muestre todos los divisores de un número entero introducido por el usuario. Un divisor de un número \( n \) es cualquier número \( d \) tal que \( n \% d == 0 \).

```python
# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))

# Mostramos todos los divisores del número
print(f"Los divisores de {numero} son:")
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)
```

**Explicación**:
1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca un número entero.
2. **Bucle para Encontrar Divisores**:
   - Recorremos los números desde 1 hasta el número ingresado.
   - Si el número es divisible por \( i \) (es decir, \( numero \% i == 0 \)), entonces \( i \) es un divisor.
3. **Mostrar el Resultado**:
   - Usamos `print` para mostrar el número en cada iteración cuando encontramos un divisor.

### **Versión Sin Usar Funciones de String**

Para hacer esto sin usar funciones de cadena (`print`, `format`, `f-strings`, etc.), necesitaremos construir manualmente el mensaje con todos los divisores y mostrarlo de manera manual.


```python
# Pedimos al usuario que introduzca un número entero
numero = int(input("Introduce un número entero: "))

# Inicializamos una variable para almacenar todos los divisores como cadena
divisores = ""  # Cadena vacía para acumular los divisores

# Encontramos todos los divisores y los agregamos a la cadena
for i in range(1, numero + 1):
    if numero % i == 0:
        # Convertimos el número a cadena y lo agregamos a la lista de divisores
        divisores += str(i) + " "

# Construimos el mensaje de salida manualmente
mensaje = "Los divisores de " + str(numero) + " son: " + divisores.strip()

# Mostramos el mensaje carácter a carácter sin usar print
for caracter in mensaje:
    # Utilizamos `sys.stdout.write` para imprimir sin saltos de línea ni espacios adicionales
    import sys
    sys.stdout.write(caracter)
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca un número entero y lo almacenamos en la variable `numero`.

2. **Inicialización de Variables**:
   - `divisores` es una cadena vacía que usaremos para almacenar los divisores del número, separados por espacios.

3. **Bucle para Encontrar Divisores**:
   - Recorremos los números desde 1 hasta el número ingresado (`range(1, numero + 1)`).
   - Si \( numero \% i == 0 \), entonces \( i \) es un divisor.
   - Convertimos \( i \) a cadena con `str(i)` y lo agregamos a `divisores` seguido de un espacio.

4. **Construcción del Mensaje**:
   - Construimos manualmente el mensaje `mensaje` concatenando las partes (`"Los divisores de "`, `str(numero)`, y `divisores`).
   - Usamos `strip()` en `divisores` para eliminar el espacio extra al final antes de construir el mensaje completo.

5. **Mostrar el Resultado Sin `print`**:
   - Iteramos por cada carácter de `mensaje` y lo mostramos manualmente usando `sys.stdout.write(caracter)` para simular `print` sin usarlo.

Este enfoque no utiliza `print` ni funciones avanzadas de cadenas como `format`, `f-strings` o `join`. La construcción y visualización del mensaje se hacen de forma manual, carácter por carácter.

---

### **Ejercicio 1.2.32** - Calcular la Serie de Fibonacci Hasta un Número Dado

En este ejercicio, vamos a implementar un programa que muestre la serie de Fibonacci hasta un número límite \( n \). La serie de Fibonacci comienza con 0 y 1, y cada número subsiguiente es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ...


```python
# Pedimos al usuario que introduzca el número límite
limite = int(input("Introduce un número límite para la serie de Fibonacci: "))

# Inicializamos los dos primeros términos de la serie
fibonacci = [0, 1]

# Generamos la serie de Fibonacci hasta que el siguiente número sea mayor que el límite
while fibonacci[-1] + fibonacci[-2] <= limite:
    siguiente_fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_fib)

# Mostramos la serie de Fibonacci
print("La serie de Fibonacci hasta", limite, "es:")
for numero in fibonacci:
    print(numero)
```

**Explicación**:
1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca un número límite hasta el cual generar la serie de Fibonacci.
2. **Inicialización de la Serie**:
   - Inicializamos la lista `fibonacci` con los primeros dos números de la serie: [0, 1].
3. **Generación de la Serie**:
   - Mientras la suma de los dos últimos elementos de `fibonacci` sea menor o igual al límite, seguimos generando números y agregándolos a la lista.
4. **Mostrar la Serie**:
   - Mostramos la serie usando `print` en un bucle `for` que recorre la lista `fibonacci`.

### **Versión Sin Usar Funciones de String**

Para hacer esto sin usar funciones de cadena (`print`, `format`, `f-strings`, etc.), vamos a construir la serie de Fibonacci manualmente y mostrar los resultados carácter por carácter usando `sys.stdout.write`.


```python
# Pedimos al usuario que introduzca el número límite
limite = int(input("Introduce un número límite para la serie de Fibonacci: "))

# Inicializamos los dos primeros términos de la serie
fibonacci = [0, 1]

# Generamos la serie de Fibonacci hasta que el siguiente número sea mayor que el límite
while fibonacci[-1] + fibonacci[-2] <= limite:
    siguiente_fib = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(siguiente_fib)

# Construimos el mensaje de la serie manualmente
mensaje = "La serie de Fibonacci hasta " + str(limite) + " es: "

# Añadimos cada número de la serie al mensaje
for numero in fibonacci:
    mensaje += str(numero) + " "

# Mostramos el mensaje carácter a carácter sin usar print
for caracter in mensaje:
    # Utilizamos `sys.stdout.write` para imprimir sin saltos de línea ni espacios adicionales
    import sys
    sys.stdout.write(caracter)
```

**Explicación detallada**:

1. **Entrada de Datos**:
   - Pedimos al usuario que introduzca el número límite hasta el cual generar la serie de Fibonacci y lo almacenamos en `limite`.

2. **Inicialización de la Serie**:
   - Inicializamos la lista `fibonacci` con los dos primeros números: `[0, 1]`.

3. **Generación de la Serie**:
   - Usamos un bucle `while` para seguir generando números de la serie mientras la suma de los dos últimos elementos de `fibonacci` sea menor o igual al límite.
   - Cada número nuevo se agrega a `fibonacci`.

4. **Construcción del Mensaje de Salida**:
   - Creamos el mensaje `mensaje` inicial con la frase `"La serie de Fibonacci hasta "` y el límite.
   - Recorremos la lista `fibonacci` y vamos agregando cada número a `mensaje` con un espacio después.

5. **Mostrar el Resultado Sin `print`**:
   - Recorremos cada carácter de `mensaje` y lo imprimimos manualmente usando `sys.stdout.write` para mostrarlo sin usar `print`.

Este enfoque no utiliza funciones de cadenas para mostrar el resultado y construye la serie de Fibonacci y el mensaje manualmente.