---
title: "UD 1 - P2: Usando python Solución Por Fases y tests"
summary: description: Usando python Por Fases
description: Usando python Por Fases
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

## P1.2 Usando python Solución Por Fases y tests

### Ejercicio 1.2.1: Dar la bienvenida al usuario

**Problema:** Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

```python
# Fase 1: Entrada y validación de datos
def obtener_nombre_usuario():
    """Solicita el nombre del usuario y lo devuelve como cadena."""
    return input("Escribe tu nombre: ")

# Fase 2: Procesamiento (no se requiere procesamiento en este caso)

# Fase 3: Salida o presentación de resultados
def mostrar_bienvenida(nombre):
    """Muestra un mensaje de bienvenida al usuario."""
    print(f"Hola, {nombre}.")

# Función principal
def main():
    nombre_usuario = obtener_nombre_usuario()  # Fase 1: Entrada
    mostrar_bienvenida(nombre_usuario)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_nombre_usuario()`: Se encarga de capturar el nombre del usuario.
2. `mostrar_bienvenida(nombre)`: Muestra el mensaje de bienvenida utilizando el nombre obtenido.
3. `main()`: Coordina las fases del programa.

---

### Ejercicio 1.2.2: Calcular el importe total del servicio

**Problema:** Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_trabajo():
    """Solicita las horas trabajadas y el coste por hora y los devuelve como tupla."""
    horas_trabajadas = float(input("Horas de trabajo: "))
    coste_por_hora = float(input("Coste por hora: "))
    return horas_trabajadas, coste_por_hora

# Fase 2: Procesamiento (lógica de negocio)
def calcular_importe_total(horas, coste):
    """Calcula el importe total del servicio."""
    return horas * coste

# Fase 3: Salida o presentación de resultados
def mostrar_importe_total(importe):
    """Muestra el importe total del servicio."""
    print(f"Importe total: {importe:.2f}")

# Función principal
def main():
    horas, coste = obtener_datos_trabajo()  # Fase 1: Entrada
    importe_total = calcular_importe_total(horas, coste)  # Fase 2: Procesamiento
    mostrar_importe_total(importe_total)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_trabajo()`: Captura las horas trabajadas y el coste por hora.
2. `calcular_importe_total(horas, coste)`: Realiza el cálculo del importe total.
3. `mostrar_importe_total(importe)`: Muestra el importe total con dos decimales.

---

### Ejercicio 1.2.4: Convertir grados Celsius a Fahrenheit

**Problema:** Escribe un programa que convierta grados Celsius a Fahrenheit.

```python
# Fase 1: Entrada y validación de datos
def obtener_temperatura_celsius():
    """Solicita la temperatura en grados Celsius y la devuelve como float."""
    return float(input("Introduce la temperatura en grados Celsius: "))

# Fase 2: Procesamiento (lógica de negocio)
def convertir_a_fahrenheit(celsius):
    """Convierte la temperatura de Celsius a Fahrenheit."""
    return celsius * 9/5 + 32

# Fase 3: Salida o presentación de resultados
def mostrar_conversion(celsius, fahrenheit):
    """Muestra la temperatura en grados Fahrenheit."""
    print(f"{celsius} grados Celsius son {fahrenheit:.2f} grados Fahrenheit.")

# Función principal
def main():
    celsius = obtener_temperatura_celsius()  # Fase 1: Entrada
    fahrenheit = convertir_a_fahrenheit(celsius)  # Fase 2: Procesamiento
    mostrar_conversion(celsius, fahrenheit)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_temperatura_celsius()`: Captura la temperatura en Celsius.
2. `convertir_a_fahrenheit(celsius)`: Realiza la conversión a Fahrenheit.
3. `mostrar_conversion(celsius, fahrenheit)`: Muestra la conversión en un formato legible.

---

### Ejercicio 1.2.3: Realizar operaciones matemáticas y comprobar sus resultados

**Problema:** Para cada una de las siguientes expresiones, adivina su valor y tipo. Luego compruébalo.

```python
# Fase 1: Entrada y validación de datos (no se necesita en este caso)

# Fase 2: Procesamiento (lógica de negocio)
def calcular_expresiones(ancho, alto):
    """Calcula y devuelve el resultado de varias expresiones."""
    exp1 = ancho / 2
    exp2 = ancho // 2
    exp3 = alto / 3
    exp4 = 1 + 2 * 5
    return exp1, exp2, exp3, exp4

# Fase 3: Salida o presentación de resultados
def mostrar_resultados(exp1, exp2, exp3, exp4):
    """Muestra el valor y tipo de cada expresión."""
    print("Expresión 1:", exp1, type(exp1))
    print("Expresión 2:", exp2, type(exp2))
    print("Expresión 3:", exp3, type(exp3))
    print("Expresión 4:", exp4, type(exp4))

# Función principal
def main():
    ancho = 17
    alto = 12.0
    exp1, exp2, exp3, exp4 = calcular_expresiones(ancho, alto)  # Fase 2: Procesamiento
    mostrar_resultados(exp1, exp2, exp3, exp4)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `calcular_expresiones(ancho, alto)`: Realiza las operaciones y devuelve el resultado de cada una.
2. `mostrar_resultados(exp1, exp2, exp3, exp4)`: Muestra el valor y el tipo de cada expresión.

---

### Ejercicio 1.2.5: Calcular el precio final con IVA

**Problema:** Calcula el precio final de un artículo a partir de su precio sin IVA y el tipo de IVA.

```python
# Fase 1: Entrada y validación de datos
def obtener_precio_sin_iva():
    """Solicita el precio sin IVA y el tipo de IVA y los devuelve como tupla."""
    precio = float(input("Introduce el importe sin IVA: "))
    tipo_iva = float(input("Introduce el tipo de IVA (%): "))
    return precio, tipo_iva

# Fase 2: Procesamiento (lógica de negocio)
def calcular_precio_final(precio, tipo_iva):
    """Calcula el precio final con IVA."""
    return precio * (1 + tipo_iva / 100)

# Fase 3: Salida o presentación de resultados
def mostrar_precio_final(precio_final):
    """Muestra el precio final con dos decimales."""
    print(f"El precio final con IVA es: {precio_final:.2f}")

# Función principal
def main():
    precio, tipo_iva = obtener_precio_sin_iva()  # Fase 1: Entrada
    precio_final = calcular_precio_final(precio, tipo_iva)  # Fase 2: Procesamiento
    mostrar_precio_final(precio_final)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_precio_sin_iva()`: Captura el precio sin IVA y el tipo de IVA.
2. `calcular_precio_final(precio, tipo_iva)`: Calcula el precio final con IVA.
3. `mostrar_precio_final(precio_final)`: Muestra el precio final con dos decimales.

---

### Ejercicio 1.2.6: Calcular el importe sin IVA y el IVA pagado

**Problema:** Calcula el IVA pagado y el importe sin IVA a partir del precio final.

```python
# Fase 1: Entrada y validación de datos
def obtener_importe_final():
    """Solicita el importe final y el tipo de IVA y los devuelve como tupla."""
    importe_final = float(input("Introduce el importe final del artículo: "))
    tipo_iva = float(input("Introduce el tipo de IVA (%): "))
    return importe_final, tipo_iva

# Fase 2: Procesamiento (lógica de negocio)
def calcular_importe_sin_iva(importe_final, tipo_iva):
    """Calcula el importe sin IVA a partir del importe final."""
    return importe_final / (1 + tipo_iva / 100)

def calcular_iva_pagado(importe_final, importe_sin_iva):
    """Calcula el IVA pagado."""
    return importe_final - importe_sin_iva

# Fase 3: Salida o presentación de resultados
def mostrar_resultados_importe(importe_sin_iva, iva_pagado):
    """Muestra el importe sin IVA y el IVA pagado con dos decimales."""
    print(f"Importe sin IVA: {importe_sin_iva:.2f}")
    print(f"IVA pagado: {iva_pagado:.2f}")

# Función principal
def main():
    importe_final, tipo_iva = obtener_importe_final()  # Fase 1: Entrada
    importe_sin_iva = calcular_importe_sin_iva(importe_final, tipo_iva)  # Fase 2: Procesamiento
    iva_pagado = calcular_iva_pagado(importe_final, importe_sin_iva)  # Fase 2: Procesamiento
    mostrar_resultados_importe(importe_sin_iva, iva_pagado)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_importe_final()`: Captura el importe final y el tipo de IVA.
2. `calcular_importe_sin_iva(importe_final, tipo_iva)`: Calcula el importe sin IVA.
3. `calcular_iva_pagado(importe_final, importe_sin_iva)`: Calcula el IVA pagado.
4. `mostrar_resultados_importe(importe_sin_iva, iva_pagado)`: Muestra ambos valores con dos decimales.

---

### Ejercicio 1.2.7: Calcular la suma de tres números

**Problema:** Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

```python
# Fase 1: Entrada y validación de datos
def obtener_tres_numeros():
    """Solicita tres números al usuario y los devuelve como tupla."""
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    num3 = float(input("Introduce el tercer número: "))
    return num1, num2, num3

# Fase 2: Procesamiento (lógica de negocio)
def calcular_suma(num1, num2, num3):
    """Calcula la suma de tres números."""
    return num1 + num2 + num3

# Fase 3: Salida o presentación de resultados
def mostrar_suma(suma):
    """Muestra la suma de los tres números."""
    print(f"La suma de los tres números es: {suma}")

# Función principal
def main():
    num1, num2, num3 = obtener_tres_numeros()  # Fase 1: Entrada
    suma = calcular_suma(num1, num2, num3)  # Fase 2: Procesamiento
    mostrar_suma(suma)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_tres_numeros()`: Captura tres números introducidos por el usuario.
2. `calcular_suma(num1, num2, num3)`: Calcula la suma de los tres números.
3. `mostrar_suma(suma)`: Muestra la suma en la consola.

---

### Ejercicio 1.2.8: Escribir un programa para calcular el área de un triángulo

**Problema:** Escribe un programa que calcule el área de un triángulo a partir de su base y altura.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_triangulo():
    """Solicita la base y altura del triángulo y las devuelve como tupla."""
    base = float(input("Introduce la base del triángulo: "))
    altura = float(input("Introduce la altura del triángulo: "))
    return base, altura

# Fase 2: Procesamiento (lógica de negocio)
def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo a partir de su base y altura."""
    return (base * altura) / 2

# Fase 3: Salida o presentación de resultados
def mostrar_area_triangulo(area):
    """Muestra el área del triángulo calculada."""
    print(f"El área del triángulo es: {area:.2f}")

# Función principal
def main():
    base, altura = obtener_datos_triangulo()  # Fase 1: Entrada
    area = calcular_area_triangulo(base, altura)  # Fase 2: Procesamiento
    mostrar_area_triangulo(area)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_triangulo()`: Captura la base y la altura del triángulo.
2. `calcular_area_triangulo(base, altura)`: Calcula el área usando la fórmula \(\frac{\text{base} \times \text{altura}}{2}\).
3. `mostrar_area_triangulo(area)`: Muestra el área con dos decimales.

---

### Ejercicio 1.2.9: Calcular el índice de masa corporal (IMC)

**Problema:** Escribe un programa que calcule el índice de masa corporal (IMC) a partir del peso y la altura.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_imc():
    """Solicita el peso y la altura del usuario y los devuelve como tupla."""
    peso = float(input("Introduce tu peso en kg: "))
    altura = float(input("Introduce tu altura en metros: "))
    return peso, altura

# Fase 2: Procesamiento (lógica de negocio)
def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC) a partir del peso y la altura."""
    return peso / (altura ** 2)

# Fase 3: Salida o presentación de resultados
def mostrar_imc(imc):
    """Muestra el índice de masa corporal con dos decimales."""
    print(f"Tu índice de masa corporal es {imc:.2f}")

# Función principal
def main():
    peso, altura = obtener_datos_imc()  # Fase 1: Entrada
    imc = calcular_imc(peso, altura)  # Fase 2: Procesamiento
    mostrar_imc(imc)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_imc()`: Captura el peso y la altura del usuario.
2. `calcular_imc(peso, altura)`: Calcula el IMC usando la fórmula \(\frac{\text{peso}}{\text{altura}^2}\).
3. `mostrar_imc(imc)`: Muestra el IMC con dos decimales.

---

### Ejercicio 1.2.10: Convertir euros a dólares

**Problema:** Escribe un programa que convierta una cantidad en euros a dólares usando un tipo de cambio dado.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_conversion():
    """Solicita la cantidad en euros y el tipo de cambio y los devuelve como tupla."""
    euros = float(input("Introduce la cantidad en euros: "))
    tipo_cambio = float(input("Introduce el tipo de cambio (1 euro a dólares): "))
    return euros, tipo_cambio

# Fase 2: Procesamiento (lógica de negocio)
def convertir_a_dolares(euros, tipo_cambio):
    """Convierte una cantidad en euros a dólares usando el tipo de cambio."""
    return euros * tipo_cambio

# Fase 3: Salida o presentación de resultados
def mostrar_conversion(euros, dolares):
    """Muestra la cantidad en euros y la conversión a dólares."""
    print(f"{euros} euros son {dolares:.2f} dólares.")

# Función principal
def main():
    euros, tipo_cambio = obtener_datos_conversion()  # Fase 1: Entrada
    dolares = convertir_a_dolares(euros, tipo_cambio)  # Fase 2: Procesamiento
    mostrar_conversion(euros, dolares)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_conversion()`: Captura la cantidad en euros y el tipo de cambio.
2. `convertir_a_dolares(euros, tipo_cambio)`: Realiza la conversión de euros a dólares.
3. `mostrar_conversion(euros, dolares)`: Muestra el resultado de la conversión.

---

### Ejercicio 1.2.11: Determinar si un número es par o impar

**Problema:** Escribe un programa que determine si un número introducido es par o impar.

```python
# Fase 1: Entrada y validación de datos
def obtener_numero():
    """Solicita un número entero al usuario."""
    return int(input("Introduce un número entero: "))

# Fase 2: Procesamiento (lógica de negocio)
def es_par(numero):
    """Devuelve True si el número es par, False si es impar."""
    return numero % 2 == 0

# Fase 3: Salida o presentación de resultados
def mostrar_paridad(numero, par):
    """Muestra si el número es par o impar."""
    tipo = "par" if par else "impar"
    print(f"El número {numero} es {tipo}.")

# Función principal
def main():
    numero = obtener_numero()  # Fase 1: Entrada
    par = es_par(numero)  # Fase 2: Procesamiento
    mostrar_paridad(numero, par)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_numero()`: Captura un número entero.
2. `es_par(numero)`: Devuelve `True` si el número es par, `False` si es impar.
3. `mostrar_paridad(numero, par)`: Muestra si el número es par o impar.

---

### Ejercicio 1.2.12: Convertir de Celsius a Kelvin

**Problema:** Escribe un programa que convierta una temperatura en grados Celsius a Kelvin.

```python
# Fase 1: Entrada y validación de datos
def obtener_temperatura_celsius():
    """Solicita la temperatura en grados Celsius y la devuelve como float."""
    return float(input("Introduce la temperatura en grados Celsius: "))

# Fase 2: Procesamiento (lógica de negocio)
def convertir_a_kelvin(celsius):
    """Convierte la temperatura de Celsius a Kelvin."""
    return celsius + 273.15

# Fase 3: Salida o presentación de resultados
def mostrar_conversion(celsius, kelvin):
    """Muestra la temperatura en Celsius y su conversión a Kelvin."""
    print(f"{celsius} grados Celsius son {kelvin:.2f} grados Kelvin.")

# Función principal
def main():
    celsius = obtener_temperatura_celsius()  # Fase 1: Entrada
    kelvin = convertir_a_kelvin(celsius)  # Fase 2: Procesamiento
    mostrar_conversion(celsius, kelvin)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_temperatura_celsius()`: Captura la temperatura en Celsius.
2. `convertir_a_kelvin(celsius)`: Realiza la conversión de Celsius a Kelvin.
3. `mostrar_conversion(celsius, kelvin)`: Muestra la conversión.

---

### Ejercicio 1.2.13: Calcular la hipotenusa de un triángulo rectángulo

**Problema:** Escribe un programa que calcule la hipotenusa de un triángulo rectángulo a partir de sus dos catetos.

```python
import math

# Fase 1: Entrada y validación de datos
def obtener_datos_triangulo_rectangulo():
    """Solicita los dos catetos del triángulo y los devuelve como tupla."""
    cateto_a = float(input("Introduce el valor del primer cateto: "))
    cateto_b = float(input("Introduce el valor del segundo cateto: "))
    return cateto_a, cateto_b

# Fase 2: Procesamiento (lógica de negocio)
def calcular_hipotenusa(cateto_a, cateto_b):
    """Calcula la hipotenusa

 de un triángulo rectángulo usando la fórmula de Pitágoras."""
    return math.sqrt(cateto_a**2 + cateto_b**2)

# Fase 3: Salida o presentación de resultados
def mostrar_hipotenusa(hipotenusa):
    """Muestra la hipotenusa con dos decimales."""
    print(f"La hipotenusa del triángulo es: {hipotenusa:.2f}")

# Función principal
def main():
    cateto_a, cateto_b = obtener_datos_triangulo_rectangulo()  # Fase 1: Entrada
    hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)  # Fase 2: Procesamiento
    mostrar_hipotenusa(hipotenusa)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_triangulo_rectangulo()`: Captura los dos catetos del triángulo.
2. `calcular_hipotenusa(cateto_a, cateto_b)`: Calcula la hipotenusa usando la fórmula de Pitágoras.
3. `mostrar_hipotenusa(hipotenusa)`: Muestra la hipotenusa calculada.

---

### Ejercicio 1.2.14: Calcular el precio total de un pedido de payasos y muñecas

**Problema:** Calcula el peso total de un pedido de payasos y muñecas.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_pedido():
    """Solicita el número de payasos y muñecas vendidos y los devuelve como tupla."""
    num_payasos = int(input("Número de payasos vendidos: "))
    num_munecas = int(input("Número de muñecas vendidas: "))
    return num_payasos, num_munecas

# Fase 2: Procesamiento (lógica de negocio)
def calcular_peso_total(num_payasos, num_munecas, peso_payaso=112, peso_muneca=75):
    """Calcula el peso total del pedido de payasos y muñecas."""
    return num_payasos * peso_payaso + num_munecas * peso_muneca

# Fase 3: Salida o presentación de resultados
def mostrar_peso_total(peso_total):
    """Muestra el peso total del pedido."""
    print(f"El peso total del paquete es: {peso_total} gramos.")

# Función principal
def main():
    num_payasos, num_munecas = obtener_datos_pedido()  # Fase 1: Entrada
    peso_total = calcular_peso_total(num_payasos, num_munecas)  # Fase 2: Procesamiento
    mostrar_peso_total(peso_total)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_pedido()`: Captura el número de payasos y muñecas vendidos.
2. `calcular_peso_total(num_payasos, num_munecas)`: Calcula el peso total del pedido basado en el peso de cada artículo.
3. `mostrar_peso_total(peso_total)`: Muestra el peso total.

---

### Ejercicio 1.2.15: Calcular el saldo de una cuenta con un 4% de interés anual

**Problema:** Calcula la cantidad de dinero en una cuenta de ahorros con un 4% de interés anual durante tres años.

```python
# Fase 1: Entrada y validación de datos
def obtener_monto_inicial():
    """Solicita el monto inicial en la cuenta de ahorros."""
    return float(input("Introduce la cantidad de dinero depositada en la cuenta de ahorros: "))

# Fase 2: Procesamiento (lógica de negocio)
def calcular_saldo_final(monto_inicial, interes=0.04, años=3):
    """Calcula el saldo final en la cuenta de ahorros después de un número de años."""
    saldo = monto_inicial
    for _ in range(años):
        saldo += saldo * interes
    return saldo

# Fase 3: Salida o presentación de resultados
def mostrar_saldo_final(saldo, años):
    """Muestra el saldo final después de un número de años."""
    print(f"El saldo después de {años} años es: {saldo:.2f}")

# Función principal
def main():
    monto_inicial = obtener_monto_inicial()  # Fase 1: Entrada
    saldo_final = calcular_saldo_final(monto_inicial)  # Fase 2: Procesamiento
    mostrar_saldo_final(saldo_final, 3)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_monto_inicial()`: Captura el monto inicial en la cuenta.
2. `calcular_saldo_final(monto_inicial, interes, años)`: Calcula el saldo final después de un número de años aplicando el interés anual.
3. `mostrar_saldo_final(saldo, años)`: Muestra el saldo final con dos decimales.

---

### Ejercicio 1.2.16: Calcular el precio con descuento de barras de pan no frescas

**Problema:** Calcula el precio total de las barras de pan no frescas con descuento.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_barras():
    """Solicita el número de barras de pan no frescas vendidas."""
    return int(input("Introduce el número de barras no frescas vendidas: "))

# Fase 2: Procesamiento (lógica de negocio)
def calcular_precio_total_barras(barras_no_frescas, precio_barra=3.49, descuento=0.60):
    """Calcula el precio total con descuento de las barras no frescas."""
    precio_con_descuento = precio_barra * (1 - descuento)
    return barras_no_frescas * precio_con_descuento

# Fase 3: Salida o presentación de resultados
def mostrar_precio_total(coste_total):
    """Muestra el precio total con descuento."""
    print(f"Coste total de las barras no frescas: {coste_total:.2f}€")

# Función principal
def main():
    barras_no_frescas = obtener_datos_barras()  # Fase 1: Entrada
    coste_total = calcular_precio_total_barras(barras_no_frescas)  # Fase 2: Procesamiento
    mostrar_precio_total(coste_total)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_barras()`: Captura el número de barras no frescas vendidas.
2. `calcular_precio_total_barras(barras_no_frescas)`: Calcula el precio total aplicando el descuento a las barras no frescas.
3. `mostrar_precio_total(coste_total)`: Muestra el precio total con dos decimales.

---

### Ejercicio 1.2.17: Repetir el nombre del usuario

**Problema:** Escribe un programa que repita el nombre del usuario una cantidad de veces especificada.

```python
# Fase 1: Entrada y validación de datos
def obtener_nombre_y_repeticiones():
    """Solicita el nombre del usuario y el número de repeticiones."""
    nombre = input("Introduce tu nombre: ")
    repeticiones = int(input("Introduce el número de repeticiones: "))
    return nombre, repeticiones

# Fase 2: Procesamiento (lógica de negocio)
def repetir_nombre(nombre, repeticiones):
    """Genera una lista con el nombre repetido la cantidad de veces especificada."""
    return [nombre] * repeticiones

# Fase 3: Salida o presentación de resultados
def mostrar_repeticiones(lista_nombres):
    """Muestra el nombre repetido."""
    for nombre in lista_nombres:
        print(nombre)

# Función principal
def main():
    nombre, repeticiones = obtener_nombre_y_repeticiones()  # Fase 1: Entrada
    lista_nombres = repetir_nombre(nombre, repeticiones)  # Fase 2: Procesamiento
    mostrar_repeticiones(lista_nombres)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_nombre_y_repeticiones()`: Captura el nombre del usuario y la cantidad de repeticiones.
2. `repetir_nombre(nombre, repeticiones)`: Genera una lista con el nombre repetido.
3. `mostrar_repeticiones(lista_nombres)`: Muestra el nombre repetido en líneas separadas.

---

### Ejercicio 1.2.18: Formatear el nombre del usuario en distintos formatos

**Problema:** Mostrar el nombre del usuario en minúsculas, mayúsculas y con cada palabra capitalizada.

```python
# Fase 1: Entrada y validación de datos
def obtener_nombre():
    """Solicita el nombre completo del usuario."""
    return input("Introduce tu nombre completo: ")

# Fase 2: Procesamiento (lógica de negocio)
def formatear_nombre(nombre):
    """Devuelve el nombre en minúsculas, mayúsculas y con capitalización de cada palabra."""
    return nombre.lower(), nombre.upper(), nombre.title()

# Fase 3: Salida o presentación de resultados
def mostrar_formatos_nombre(minusculas, mayusculas, capitalizado):
    """Muestra el nombre en minúsculas, mayúsculas y con capitalización."""
    print(minusculas)
    print(mayusculas)
    print(capitalizado)

# Función principal
def main():
    nombre = obtener_nombre()  # Fase 1: Entrada
    minusculas, mayusculas, capitalizado = formatear_nombre(nombre)  # Fase 2: Procesamiento
    mostrar_formatos_nombre(minusculas, mayusculas, capitalizado)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_nombre()`: Captura el nombre completo del usuario.
2. `formatear_nombre(nombre)`: Devuelve el nombre en minúsculas, mayúsculas y capitalizado.
3. `mostrar_formatos_nombre(minusculas, mayusculas, capitalizado)`: Muestra el nombre en cada formato.

---

### Ejercicio 1.2.19: Contar las letras de un nombre

**Problema:** Escribe un programa que muestre la cantidad de letras del nombre en mayúsculas.

```python
# Fase 1: Entrada y validación de datos
def obtener_nombre_usuario():
    """Solicita el nombre del usuario."""
    return input("Introduce tu nombre: ")

# Fase 2: Procesamiento (lógica de negocio)
def contar_letras(nombre):
    """Cuenta las letras de un nombre, ignorando los espacios."""
    nombre_sin_espacios = nombre.replace(" ", "")
    return len(nombre_sin_espacios), nombre.upper()

# Fase 3: Salida o presentación de resultados
def mostrar_contador(nombre_mayusculas, cantidad_letras):
    """Muestra el nombre en mayúsculas y la cantidad de letras."""
    print(f"{nombre_mayusculas} tiene {cantidad_letras} letras.")

# Función principal
def main():
    nombre = obtener_nombre_usuario()  # Fase 1: Entrada
    cantidad_letras, nombre_mayusculas = contar_letras(nombre)  # Fase 2: Procesamiento
    mostrar_contador(nombre_mayusculas, cantidad_letras)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_nombre_usuario()`: Captura el nombre del usuario.
2. `contar_letras(nombre)`: Cuenta las letras del nombre ignorando espacios y convierte el nombre a mayúsculas.
3. `mostrar_contador(nombre_mayusculas, cantidad_letras)`: Muestra el nombre en mayúsculas y el número de letras.

---

### Ejercicio 1.2.20: Extraer el número de teléfono sin prefijo y extensión

**Problema:** Escribe un programa que muestre el número de teléfono sin el prefijo y la extensión en un formato específico.

```python
# Fase 1: Entrada y validación de datos
def obtener_telefono():
    """Solicita el número de teléfono en el formato +34-xxxxxxxxx-xx y lo devuelve como cadena."""
    return input("Introduce el número de teléfono (formato +34-xxxxxxxxx-xx): ")

# Fase 2: Procesamiento (lógica de negocio)
def extraer_numero_sin_prefijo_extension(telefono):
    """Extrae la parte central del número de teléfono, sin el prefijo y la extensión."""
    partes = telefono.split('-')
    return partes[1] if len(partes) == 3 else ""

# Fase 3: Salida o presentación de resultados
def mostrar_numero_sin_prefijo_extension(numero):
    """Muestra el número sin prefijo ni extensión."""
    print(f"El número sin prefijo y extensión es: {numero}")

# Función principal
def main():
    telefono = obtener_telefono()  # Fase 1: Entrada
    numero_sin_prefijo_extension = extraer_numero_sin_prefijo_extension(telefono)  # Fase 2: Procesamiento
    mostrar_numero_sin_prefijo_extension(numero_sin_prefijo_extension)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_telefono()`: Captura el número de teléfono en el formato especificado.
2. `extraer_numero_sin_prefijo_extension(telefono)`: Extrae la parte central del número, sin prefijo y sin extensión.
3. `mostrar_numero_sin_prefijo_extension(numero)`: Muestra el número sin prefijo ni extensión.

---

### Ejercicio 1.2.21: Invertir una frase

**Problema:** Escribe un programa que invierta una frase introducida por el usuario.

```python
# Fase 1: Entrada y validación de datos
def obtener_frase():
    """Solicita una frase al usuario."""
    return input("Introduce una frase: ")

# Fase 2: Procesamiento (lógica de negocio)
def invertir_frase(frase):
    """Invierte la frase."""
    return frase[::-1]

# Fase 3: Salida o presentación de resultados
def mostrar_frase_invertida(frase_invertida):
    """Muestra la frase invertida."""
    print(f"La frase invertida es: {frase_invertida}")

# Función principal
def main():
    frase = obtener_frase()  # Fase 1: Entrada
    frase_invertida = invertir_frase(frase)  # Fase 2: Procesamiento
    mostrar_frase_invertida(frase_invertida)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_frase()`: Captura la frase introducida por el usuario.
2. `invertir_frase(frase)`: Invierte la frase.
3. `mostrar_frase_invertida(frase_invertida)`: Muestra la frase invertida.

---

### Ejercicio 1.2.22: Reemplazar una vocal en la frase con su versión mayúscula

**Problema:** Escribe un programa que reemplace todas las ocurrencias de una vocal específica en una frase por su versión en mayúscula.

```python
# Fase 1: Entrada y validación de datos
def obtener_frase_y_vocal():
    """Solicita una frase y una vocal para reemplazarla."""
    frase = input("Introduce una frase: ")
    vocal = input("Introduce una vocal: ")
    return frase, vocal

# Fase 2: Procesamiento (lógica de negocio)
def reemplazar_vocal(frase, vocal):
    """Reemplaza todas las ocurrencias de la vocal por su versión en mayúscula."""
    return frase.replace(vocal, vocal.upper())

# Fase 3: Salida o presentación de resultados
def mostrar_frase_modificada(frase_modificada):
    """Muestra la frase con la vocal reemplazada por su versión en mayúscula."""
    print(f"La frase modificada es: {frase_modificada}")

# Función principal
def main():
    frase, vocal = obtener_frase_y_vocal()  # Fase 1: Entrada
    frase_modificada = reemplazar_vocal(frase, vocal)  # Fase 2: Procesamiento
    mostrar_frase_modificada(frase_modificada)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_frase_y_vocal()`: Captura la frase y la vocal que se desea reemplazar.
2. `reemplazar_vocal(frase, vocal)`: Reemplaza todas las ocurrencias de la vocal por su versión en mayúscula.
3. `mostrar_frase_modificada(frase_modificada)`: Muestra la frase modificada.

---

### Ejercicio 1.2.23: Mostrar un correo con un dominio diferente

**Problema:** Escribe un programa que reciba un correo y lo modifique para mostrarlo con un dominio diferente.

```python
# Fase 1: Entrada y validación de datos
def obtener_correo():
    """Solicita el correo electrónico del usuario."""
    return input("Introduce tu correo electrónico: ")

# Fase 2: Procesamiento (lógica de negocio)
def cambiar_dominio(correo, nuevo_dominio="ceu.es"):
    """Cambia el dominio de un correo electrónico al nuevo dominio."""
    nombre_usuario = correo.split('@')[0]
    return f"{nombre_usuario}@{nuevo_dominio}"

# Fase 3: Salida o presentación de resultados
def mostrar_correo_modificado(correo_modificado):
    """Muestra el correo con el nuevo dominio."""
    print(f"Tu nuevo correo es: {correo_modificado}")

# Función principal
def main():
    correo = obtener_correo()  # Fase 1: Entrada
    correo_modificado = cambiar_dominio(correo)  # Fase 2: Procesamiento
    mostrar_correo_modificado(correo_modificado)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_correo()`: Captura el correo electrónico del usuario.
2. `cambiar_dominio(correo, nuevo_dominio)`: Cambia el dominio del correo al nuevo dominio.
3. `mostrar_correo_modificado(correo_modificado)`: Muestra el correo con el nuevo dominio.

---

### Ejercicio 1.2.24: Mostrar el número de euros y céntimos de un precio

**Problema:** Escribe un programa que muestre la parte entera y la parte decimal de un precio en euros.

```python
# Fase 1: Entrada y validación de datos
def obtener_precio():
    """Solicita el precio del producto en euros con dos decimales."""
    return input("Introduce el precio del producto en euros (ejemplo: 12.34): ")

# Fase 2: Procesamiento (lógica de negocio)
def separar_euros_y_centimos(precio):
    """Separa el número de euros y céntimos de un precio."""
    euros, centimos = precio.split('.')
    return euros, centimos

# Fase 3: Salida o presentación de resultados
def mostrar_euros_y_centimos(euros, centimos):
    """Muestra los euros y céntimos del precio."""
    print(f"El número de euros es: {euros} y el número de céntimos es: {centimos}")

# Función principal
def main():
    precio = obtener_precio()  # Fase 1: Entrada
    euros, centimos = separar_euros_y_centimos(precio)  # Fase 2: Procesamiento
    mostrar_euros_y_centimos(euros, centimos)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_precio()`: Captura el precio del producto en euros.
2. `separar_euros_y_centimos(precio)`: Separa la parte entera y la parte decimal del precio.
3. `mostrar_euros_y_centimos(euros, centimos)`: Muestra los euros y céntimos por separado.

---

### Ejercicio 1.2.25: Mostrar día, mes y año de una fecha introducida

**Problema:** Escribe un programa que muestre el día, mes y año de una fecha introducida en formato `dd/mm/aaaa`.

```python
# Fase 1: Entrada y validación de datos
def obtener_fecha():
    """Solicita la fecha de nacimiento en formato dd/mm/aaaa."""
    return input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

# Fase 2: Procesamiento (lógica de negocio)
def separar_dia_mes_año(fecha):
    """Separa el día, mes y año de una fecha en formato dd/mm/aaaa."""
    dia, mes, anio = fecha.split('/')
    return dia, mes, anio

# Fase 3: Salida o

 presentación de resultados
def mostrar_dia_mes_año(dia, mes, anio):
    """Muestra el día, mes y año de la fecha."""
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")

# Función principal
def main():
    fecha = obtener_fecha()  # Fase 1: Entrada
    dia, mes, anio = separar_dia_mes_año(fecha)  # Fase 2: Procesamiento
    mostrar_dia_mes_año(dia, mes, anio)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_fecha()`: Captura la fecha en formato `dd/mm/aaaa`.
2. `separar_dia_mes_año(fecha)`: Separa el día, mes y año de la fecha.
3. `mostrar_dia_mes_año(dia, mes, anio)`: Muestra el día, mes y año de la fecha por separado.

---

### Ejercicio 1.2.26: Mostrar cada producto en una línea distinta

**Problema:** Escribe un programa que muestre cada producto de una lista separados por comas en líneas distintas.

```python
# Fase 1: Entrada y validación de datos
def obtener_productos():
    """Solicita una lista de productos separados por comas."""
    return input("Introduce los productos de la cesta de la compra, separados por comas: ")

# Fase 2: Procesamiento (lógica de negocio)
def separar_productos(productos):
    """Separa los productos en una lista usando la coma como delimitador."""
    return productos.split(',')

# Fase 3: Salida o presentación de resultados
def mostrar_productos(productos):
    """Muestra cada producto en una línea distinta."""
    for producto in productos:
        print(producto.strip())

# Función principal
def main():
    productos = obtener_productos()  # Fase 1: Entrada
    lista_productos = separar_productos(productos)  # Fase 2: Procesamiento
    mostrar_productos(lista_productos)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_productos()`: Captura la lista de productos introducidos por el usuario.
2. `separar_productos(productos)`: Separa los productos en una lista utilizando la coma como delimitador.
3. `mostrar_productos(productos)`: Muestra cada producto en una línea separada.

---

### Ejercicio 1.2.27: Mostrar formato de un producto

**Problema:** Escribe un programa que pida el nombre de un producto, su precio y el número de unidades, y luego muestre estos valores en un formato específico.

```python
# Fase 1: Entrada y validación de datos
def obtener_datos_producto():
    """Solicita el nombre, precio y número de unidades de un producto."""
    nombre_producto = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    unidades = int(input("Introduce el número de unidades: "))
    return nombre_producto, precio, unidades

# Fase 2: Procesamiento (lógica de negocio)
def calcular_coste_total(precio, unidades):
    """Calcula el coste total de un producto."""
    return precio * unidades

# Fase 3: Salida o presentación de resultados
def mostrar_producto(nombre_producto, precio, unidades, coste_total):
    """Muestra el nombre del producto, su precio, número de unidades y coste total."""
    print(f"{nombre_producto}: {precio:6.2f}€ {unidades:3d} unidades, Coste total: {coste_total:8.2f}€")

# Función principal
def main():
    nombre_producto, precio, unidades = obtener_datos_producto()  # Fase 1: Entrada
    coste_total = calcular_coste_total(precio, unidades)  # Fase 2: Procesamiento
    mostrar_producto(nombre_producto, precio, unidades, coste_total)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_datos_producto()`: Captura el nombre, precio y número de unidades del producto.
2. `calcular_coste_total(precio, unidades)`: Calcula el coste total del producto.
3. `mostrar_producto(nombre_producto, precio, unidades, coste_total)`: Muestra el nombre, precio, unidades y coste total en el formato deseado.

---

### Ejercicio 1.2.28: Calcular el área de un triángulo con la fórmula de Herón

**Problema:** Escribe un programa que calcule el área de un triángulo a partir de sus tres lados usando la **fórmula de Herón**.

\[
A = \sqrt{s \times (s - a) \times (s - b) \times (s - c)}
\]

donde \( s \) es el semiperímetro del triángulo y se calcula como:

\[
s = \frac{a + b + c}{2}
\]

```python
import math

# Fase 1: Entrada y validación de datos
def obtener_lados_triangulo():
    """Solicita los tres lados del triángulo y los devuelve como tupla."""
    a = float(input("Introduce el primer lado del triángulo: "))
    b = float(input("Introduce el segundo lado del triángulo: "))
    c = float(input("Introduce el tercer lado del triángulo: "))
    return a, b, c

# Fase 2: Procesamiento (lógica de negocio)
def calcular_area_triangulo_heron(a, b, c):
    """Calcula el área de un triángulo usando la fórmula de Herón."""
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Fase 3: Salida o presentación de resultados
def mostrar_area_triangulo(area):
    """Muestra el área del triángulo calculada."""
    print(f"El área del triángulo es: {area:.2f}")

# Función principal
def main():
    a, b, c = obtener_lados_triangulo()  # Fase 1: Entrada
    area = calcular_area_triangulo_heron(a, b, c)  # Fase 2: Procesamiento
    mostrar_area_triangulo(area)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_lados_triangulo()`: Captura los tres lados del triángulo.
2. `calcular_area_triangulo_heron(a, b, c)`: Calcula el área usando la fórmula de Herón.
3. `mostrar_area_triangulo(area)`: Muestra el área con dos decimales.

---

### Ejercicio 1.2.29: Generar un número aleatorio entre dos valores

**Problema:** Escribe un programa que genere un número aleatorio entre dos valores introducidos por el usuario.

```python
import random

# Fase 1: Entrada y validación de datos
def obtener_limites():
    """Solicita el valor inferior y superior para generar un número aleatorio."""
    valor_inferior = int(input("Introduce el valor inferior: "))
    valor_superior = int(input("Introduce el valor superior: "))
    return valor_inferior, valor_superior

# Fase 2: Procesamiento (lógica de negocio)
def generar_numero_aleatorio(valor_inferior, valor_superior):
    """Genera un número aleatorio entre valor_inferior y valor_superior."""
    return random.randint(valor_inferior, valor_superior)

# Fase 3: Salida o presentación de resultados
def mostrar_numero_aleatorio(numero_aleatorio, valor_inferior, valor_superior):
    """Muestra el número aleatorio generado."""
    print(f"El número aleatorio generado entre {valor_inferior} y {valor_superior} es: {numero_aleatorio}")

# Función principal
def main():
    valor_inferior, valor_superior = obtener_limites()  # Fase 1: Entrada
    numero_aleatorio = generar_numero_aleatorio(valor_inferior, valor_superior)  # Fase 2: Procesamiento
    mostrar_numero_aleatorio(numero_aleatorio, valor_inferior, valor_superior)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_limites()`: Captura el valor inferior y superior.
2. `generar_numero_aleatorio(valor_inferior, valor_superior)`: Genera un número aleatorio entre los valores introducidos.
3. `mostrar_numero_aleatorio(numero_aleatorio, valor_inferior, valor_superior)`: Muestra el número aleatorio generado.

---

### Ejercicio 1.2.30: Determinar si un número es primo

**Problema:** Escribe un programa que determine si un número dado es primo.

```python
# Fase 1: Entrada y validación de datos
def obtener_numero():
    """Solicita un número entero al usuario."""
    return int(input("Introduce un número entero: "))

# Fase 2: Procesamiento (lógica de negocio)
def es_primo(n):
    """Devuelve True si el número es primo, False en caso contrario."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fase 3: Salida o presentación de resultados
def mostrar_resultado_primo(n, primo):
    """Muestra si el número es primo o no."""
    if primo:
        print(f"{n} es un número primo.")
    else:
        print(f"{n} no es un número primo.")

# Función principal
def main():
    numero = obtener_numero()  # Fase 1: Entrada
    primo = es_primo(numero)  # Fase 2: Procesamiento
    mostrar_resultado_primo(numero, primo)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_numero()`: Captura un número entero introducido por el usuario.
2. `es_primo(n)`: Determina si el número es primo.
3. `mostrar_resultado_primo(n, primo)`: Muestra si el número es primo o no.

---

### Ejercicio 1.2.31: Mostrar todos los divisores de un número

**Problema:** Escribe un programa que muestre todos los divisores de un número entero introducido por el usuario.

```python
# Fase 1: Entrada y validación de datos
def obtener_numero():
    """Solicita un número entero al usuario."""
    return int(input("Introduce un número entero: "))

# Fase 2: Procesamiento (lógica de negocio)
def calcular_divisores(numero):
    """Calcula y devuelve una lista con todos los divisores del número."""
    divisores = [i for i in range(1, numero + 1) if numero % i == 0]
    return divisores

# Fase 3: Salida o presentación de resultados
def mostrar_divisores(divisores):
    """Muestra todos los divisores del número."""
    print(f"Los divisores del número son: {', '.join(map(str, divisores))}")

# Función principal
def main():
    numero = obtener_numero()  # Fase 1: Entrada
    divisores = calcular_divisores(numero)  # Fase 2: Procesamiento
    mostrar_divisores(divisores)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_numero()`: Captura un número entero introducido por el usuario.
2. `calcular_divisores(numero)`: Calcula todos los divisores del número.
3. `mostrar_divisores(divisores)`: Muestra los divisores separados por comas.

---

### Ejercicio 1.2.32: Calcular la serie de Fibonacci hasta un número dado

**Problema:** Escribe un programa que muestre la serie de Fibonacci hasta un número límite \( n \).

```python
# Fase 1: Entrada y validación de datos
def obtener_limite_fibonacci():
    """Solicita el número límite para la serie de Fibonacci."""
    return int(input("Introduce un número límite para la serie de Fibonacci: "))

# Fase 2: Procesamiento (lógica de negocio)
def calcular_serie_fibonacci(limite):
    """Calcula la serie de Fibonacci hasta el número límite dado."""
    fibonacci = [0, 1]
    while fibonacci[-1] + fibonacci[-2] <= limite:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Fase 3: Salida o presentación de resultados
def mostrar_serie_fibonacci(serie_fibonacci):
    """Muestra la serie de Fibonacci."""
    print(f"La serie de Fibonacci es: {', '.join(map(str, serie_fibonacci))}")

# Función principal
def main():
    limite = obtener_limite_fibonacci()  # Fase 1: Entrada
    serie_fibonacci = calcular_serie_fibonacci(limite)  # Fase 2: Procesamiento
    mostrar_serie_fibonacci(serie_fibonacci)  # Fase 3: Salida

if __name__ == "__main__":
    main()
```

**Explicación:**
1. `obtener_limite_fibonacci()`: Captura el número límite para la serie de Fibonacci.
2. `calcular_serie_fibonacci(limite)`: Calcula la serie de Fibonacci hasta el número límite.
3. `mostrar_serie_fibonacci(serie_fibonacci)`: Muestra la serie de Fibonacci hasta el límite.


---

---

## P1.2 Test de los ejercicios en python

### Creación de Pruebas Unitarias para las Funciones de Procesamiento de los Ejercicios

Este fichero debería llamarse `test_ejercicios.py` y contendría las pruebas unitarias para las funciones de procesamiento de los ejercicios, usando el framework `pytest`. Cada test verificará la funcionalidad central de cada ejercicio, y en los casos donde se necesiten datos de entrada/salida específicos, se usarán ejemplos simples para validar las funciones de lógica de negocio.

#### Archivo `test_ejercicios.py`

```python
import pytest
from math import isclose

# Importar las funciones de cada ejercicio. Asegúrate de que las funciones estén en un archivo llamado `main.py` o el nombre que desees.
from main import (
    calcular_area_triangulo,
    calcular_imc,
    convertir_a_dolares,
    es_par,
    convertir_a_kelvin,
    calcular_hipotenusa,
    calcular_peso_total,
    calcular_saldo_final,
    calcular_precio_total_barras,
    repetir_nombre,
    formatear_nombre,
    contar_letras,
    extraer_numero_sin_prefijo_extension,
    invertir_frase,
    reemplazar_vocal,
    cambiar_dominio,
    separar_euros_y_centimos,
    separar_dia_mes_año,
    separar_productos,
    calcular_coste_total,
    calcular_area_triangulo_heron,
    generar_numero_aleatorio,
    es_primo,
    calcular_divisores,
    calcular_serie_fibonacci,
)

# Pruebas para cada ejercicio
def test_calcular_area_triangulo():
    assert calcular_area_triangulo(5, 10) == 25.0
    assert calcular_area_triangulo(0, 10) == 0.0

def test_calcular_imc():
    assert isclose(calcular_imc(70, 1.75), 22.86, rel_tol=1e-2)
    assert isclose(calcular_imc(80, 1.80), 24.69, rel_tol=1e-2)

def test_convertir_a_dolares():
    assert convertir_a_dolares(100, 1.1) == 110.0
    assert convertir_a_dolares(50, 1.5) == 75.0

def test_es_par():
    assert es_par(4) == True
    assert es_par(7) == False

def test_convertir_a_kelvin():
    assert convertir_a_kelvin(0) == 273.15
    assert convertir_a_kelvin(-273.15) == 0.0

def test_calcular_hipotenusa():
    assert isclose(calcular_hipotenusa(3, 4), 5.0, rel_tol=1e-9)
    assert isclose(calcular_hipotenusa(6, 8), 10.0, rel_tol=1e-9)

def test_calcular_peso_total():
    assert calcular_peso_total(10, 5) == 10 * 112 + 5 * 75
    assert calcular_peso_total(0, 10) == 10 * 75

def test_calcular_saldo_final():
    assert isclose(calcular_saldo_final(1000), 1124.864, rel_tol=1e-3)
    assert isclose(calcular_saldo_final(500), 562.432, rel_tol=1e-3)

def test_calcular_precio_total_barras():
    assert isclose(calcular_precio_total_barras(10), 13.96, rel_tol=1e-2)
    assert isclose(calcular_precio_total_barras(0), 0.0)

def test_repetir_nombre():
    assert repetir_nombre("Juan", 3) == ["Juan", "Juan", "Juan"]
    assert repetir_nombre("Ana", 0) == []

def test_formatear_nombre():
    assert formatear_nombre("Juan Pérez") == ("juan pérez", "JUAN PÉREZ", "Juan Pérez")
    assert formatear_nombre("ANA") == ("ana", "ANA", "Ana")

def test_contar_letras():
    assert contar_letras("Ana María") == (7, "ANA MARÍA")
    assert contar_letras("Juan") == (4, "JUAN")

def test_extraer_numero_sin_prefijo_extension():
    assert extraer_numero_sin_prefijo_extension("+34-123456789-01") == "123456789"
    assert extraer_numero_sin_prefijo_extension("123-456-789") == ""

def test_invertir_frase():
    assert invertir_frase("Hola Mundo") == "odnuM aloH"
    assert invertir_frase("Python") == "nohtyP"

def test_reemplazar_vocal():
    assert reemplazar_vocal("hola mundo", "o") == "hOla mundO"
    assert reemplazar_vocal("banana", "a") == "bAnAnA"

def test_cambiar_dominio():
    assert cambiar_dominio("usuario@dominio.com") == "usuario@ceu.es"
    assert cambiar_dominio("test@prueba.org") == "test@ceu.es"

def test_separar_euros_y_centimos():
    assert separar_euros_y_centimos("12.34") == ("12", "34")
    assert separar_euros_y_centimos("100.00") == ("100", "00")

def test_separar_dia_mes_año():
    assert separar_dia_mes_año("01/12/2021") == ("01", "12", "2021")
    assert separar_dia_mes_año("15/07/1995") == ("15", "07", "1995")

def test_separar_productos():
    assert separar_productos("pan, leche, huevos") == ["pan", "leche", "huevos"]
    assert separar_productos("manzana, plátano") == ["manzana", "plátano"]

def test_calcular_coste_total():
    assert calcular_coste_total(10, 5) == 50.0
    assert calcular_coste_total(3.49, 10) == 34.9

def test_calcular_area_triangulo_heron():
    assert isclose(calcular_area_triangulo_heron(3, 4, 5), 6.0, rel_tol=1e-9)
    assert isclose(calcular_area_triangulo_heron(7, 10, 5), 16.25, rel_tol=1e-9)

def test_generar_numero_aleatorio():
    valor_inferior = 1
    valor_superior = 10
    numero_aleatorio = generar_numero_aleatorio(valor_inferior, valor_superior)
    assert valor_inferior <= numero_aleatorio <= valor_superior

def test_es_primo():
    assert es_primo(7) == True
    assert es_primo(9) == False

def test_calcular_divisores():
    assert calcular_divisores(6) == [1, 2, 3, 6]
    assert calcular_divisores(13) == [1, 13]

def test_calcular_serie_fibonacci():
    assert calcular_serie_fibonacci(10) == [0, 1, 1, 2, 3, 5, 8]
    assert calcular_serie_fibonacci(1) == [0, 1, 1]
```

#### Explicación de las pruebas

Cada función de procesamiento tiene su correspondiente prueba en `pytest`. Vamos a explicar algunas de ellas:

1. **Pruebas con `assert`**: Utilizamos `assert` para comparar los resultados de las funciones con los resultados esperados.
2. **Tolerancia (`rel_tol`)**: Para pruebas con números decimales (por ejemplo, `calcular_area_triangulo`), utilizamos `isclose` con una tolerancia relativa (`rel_tol`) para evitar problemas de precisión.
3. **Verificación de listas y cadenas**: Para funciones que devuelven listas (`calcular_divisores`, `calcular_serie_fibonacci`) o cadenas (`reemplazar_vocal`), comparamos las listas completas o las cadenas resultantes.

#### Ejecución de pruebas

Para ejecutar las pruebas, asegúrate de tener `pytest` instalado y ejecuta el siguiente comando en la terminal:

```bash
> pytest -v test_ejercicios.py
```

Si tienes las funciones en un archivo llamado `main.py`, verifica que las rutas de importación en el archivo de pruebas sean correctas (por ejemplo, `from main import calcular_area_triangulo`).