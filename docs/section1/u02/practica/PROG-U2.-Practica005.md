---
title: "UD 2 - P5: Ejercicios Integrados (Parte 1)"
summary: Ejercicios que integran condicionales, iterativas y algoritmia básica
description: 30 ejercicios progresivos del mundo real para practicar U01 y U02
authors:
    - Eduardo Fdez
date: 2025-10-25
icon: 
permalink: /prog/unidad2/p2.5
categories:
    - PROG
tags:
    - Software
    - Ejercicios
---

# P2.5 - Ejercicios Integrados (Parte 1/3): Nivel Básico

## Descripción

Esta práctica contiene **30 ejercicios progresivos** que integran todo lo aprendido en las unidades 1 y 2:
- Variables y tipos de datos (int, float, str, bool)
- Operadores (aritméticos, relacionales, lógicos)
- Entrada/salida de datos
- Condicionales (if, elif, else)
- Bucles (for, while)
- Validación de entrada
- Algoritmia básica

Los ejercicios están contextualizados en **problemas del mundo real** para aumentar la motivación y comprensión.

**Parte 1/3: Ejercicios 1-10 (Nivel Básico)**

---

## Normas de Entrega

1. Crea un archivo `.py` para cada ejercicio: `ejercicio01.py`, `ejercicio02.py`, etc.
2. Todos los ejercicios deben incluir:
   - Especificación de tipos (type hints) en funciones
   - Docstrings en todas las funciones
   - Comentarios explicativos
   - Validación de entrada cuando sea necesario
3. No usar: `while True`, `break` (excepto en casos muy justificados), `continue`
4. Modularizar el código con funciones pequeñas y específicas
5. Probar cada ejercicio con varios casos

---

## Ejercicio 1: Calculadora de Propinas

**Contexto:** Trabajas en un restaurante y necesitas calcular automáticamente la propina según la calidad del servicio.

**Descripción:**
Crea un programa que calcule la propina y el total a pagar en un restaurante. El usuario introduce:
- El importe de la cuenta (float)
- La calidad del servicio: "excelente" (20%), "bueno" (15%), "regular" (10%)

**Especificación de la función obligatoria:**

Debes implementar obligatoriamente la siguiente función con esta firma exacta:

```python
def calcular_propina(importe: float, calidad: str) -> tuple[float, float]:
    """
    Calcula la propina y el total a pagar según el importe y la calidad del servicio.
    
    Args:
        importe: El importe de la cuenta (debe ser positivo)
        calidad: Calidad del servicio ("excelente" = 20%, "bueno" = 15%, "regular" = 10%)
        
    Returns:
        tuple[float, float]: Una tupla con (propina, total_a_pagar)
        
    Nota:
        - Si el importe es <= 0, devuelve (0.0, 0.0)
        - Si la calidad no es válida, devuelve (0.0, importe)
        - La calidad se compara en minúsculas
    """
    pass
```

**Entrada de ejemplo:**
```
Importe de la cuenta: 47.50
Calidad del servicio (excelente/bueno/regular): bueno
```

**Salida esperada:**
```
Cuenta: 47.50€
Propina (15%): 7.12€
Total a pagar: 54.62€
```

**Requisitos de implementación:**
- La función `calcular_propina` debe estar implementada exactamente como se especifica
- Validar que el importe sea positivo (> 0)
- Validar que la calidad sea una de las tres opciones válidas
- El programa principal debe solicitar los datos, llamar a la función y mostrar el desglose
- Para mostrar el desglose, calcular la propina en main: propina = total - importe
- Mostrar todos los valores con 2 decimales

**Casos de prueba que se evaluarán:**
- Servicio excelente con diferentes importes
- Servicio bueno con diferentes importes  
- Servicio regular con diferentes importes
- Manejo de importes negativos o cero
- Manejo de calidades no válidas
- Calidad en mayúsculas/minúsculas

---

## Ejercicio 2: Clasificador de Temperaturas

**Contexto:** Eres meteorólogo y necesitas clasificar temperaturas para informes diarios.

**Descripción:**
Crea un programa que clasifique una temperatura según estos rangos:
- Menos de 0°C: "Helada"
- 0°C a 10°C: "Frío"
- 11°C a 20°C: "Templado"
- 21°C a 30°C: "Cálido"
- Más de 30°C: "Caluroso"

Además, debe indicar si es una temperatura "extrema" (menor a -10°C o mayor a 40°C).

**Especificación de la función obligatoria:**

```python
def clasificar_temperatura(temperatura: float) -> int:
    """
    Clasifica una temperatura y devuelve un código de clasificación.
    
    Args:
        temperatura: La temperatura en grados Celsius
        
    Returns:
        int: Código de clasificación:
            * 0: Temperatura inválida (fuera del rango -50 a 60)
            * 1: Helada (temp < 0)
            * 2: Frío (0 <= temp <= 10)
            * 3: Templado (11 <= temp <= 20)
            * 4: Cálido (21 <= temp <= 30)
            * 5: Caluroso (temp > 30)
            * 10: Extrema fría (temp < -10)
            * 20: Extrema calurosa (temp > 40)
        
    Nota:
        - Si la temperatura está fuera del rango válido (-50 a 60), devolver 0
        - Las temperaturas extremas (< -10 o > 40) devuelven códigos especiales (10 o 20)
        - Prioridad: primero verificar extremas, luego las normales
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce la temperatura en °C: 35
```

**Salida esperada:**
```
Temperatura: 35°C
Clasificación: Caluroso
Estado: Temperatura normal (no extrema)
```

**Requisitos de implementación:**
- La función `clasificar_temperatura` debe estar implementada exactamente como se especifica
- Validar que la temperatura esté en un rango razonable (-50 a 60)
- El programa debe mapear el código devuelto a mensajes legibles:
  - Código 0: "Inválida"
  - Código 1: "Helada"
  - Código 2: "Frío"
  - Código 3: "Templado"
  - Código 4: "Cálido"
  - Código 5: "Caluroso"
  - Código 10: "Helada (EXTREMA)"
  - Código 20: "Caluroso (EXTREMA)"
- Formatear la salida de manera clara

**Casos de prueba que se evaluarán:**
- Todas las clasificaciones normales (1-5)
- Temperaturas extremas (códigos 10 y 20)
- Temperaturas en límites de rangos (0, 10, 11, 20, 21, 30, -10, 40)
- Temperaturas fuera del rango válido (código 0)

---

## Ejercicio 3: Contador de Dígitos Pares e Impares

**Contexto:** En criptografía básica necesitas analizar propiedades de números.

**Descripción:**
Crea un programa que cuente cuántos dígitos pares e impares tiene un número entero.

**Especificación de la función obligatoria:**

```python
def contar_digitos_pares(numero: int) -> int:
    """
    Cuenta la cantidad de dígitos pares en un número.
    
    Args:
        numero: Un número entero (puede ser positivo o negativo)
        
    Returns:
        int: Cantidad de dígitos pares encontrados
        
    Nota:
        - El 0 se considera par
        - Si el número es negativo, se trabaja con su valor absoluto
        - Si el número es 0, devolver 1
        - Trabajar SOLO con operaciones matemáticas (NO usar str())
        - Usar % 10 para obtener el último dígito
        - Usar // 10 para eliminar el último dígito
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce un número entero: 1234567890
```

**Salida esperada:**
```
Número analizado: 1234567890
Total de dígitos: 10
Dígitos pares: 5 (0, 2, 4, 6, 8)
Dígitos impares: 5 (1, 3, 5, 7, 9)
```

**Requisitos de implementación:**
- La función `contar_digitos_pares` debe estar implementada exactamente como se especifica
- NO usar conversión a cadena (str()) - trabajar solo con operaciones matemáticas (%, //)
- Usar bucles para extraer dígitos uno a uno
- El programa principal debe calcular también los impares: total_digitos - pares
- Mostrar opcionalmente qué dígitos son pares y cuáles impares

**Casos de prueba que se evaluarán:**
- Números con solo dígitos pares
- Números con solo dígitos impares
- Números mixtos
- Número 0
- Números negativos
- Números de un solo dígito

---

## Ejercicio 4: Calculadora de Índice de Masa Corporal (IMC)

**Contexto:** Eres desarrollador de una app de salud y necesitas calcular el IMC.

**Descripción:**
Crea un programa que calcule el IMC y determine la categoría de peso:
- Fórmula: IMC = peso (kg) / altura² (m)
- Bajo peso: IMC < 18.5
- Normal: 18.5 ≤ IMC < 25
- Sobrepeso: 25 ≤ IMC < 30
- Obesidad: IMC ≥ 30

**Especificación de la función obligatoria:**

```python
def calcular_imc(peso: float, altura: float) -> int:
    """
    Calcula el IMC y devuelve un código de categoría.
    
    Args:
        peso: Peso en kilogramos
        altura: Altura en metros
        
    Returns:
        int: Código de categoría:
            * -3: Peso fuera de rango (< 20 o > 300)
            * -2: Altura fuera de rango (< 0.5 o > 2.5)
            * -1: Datos inválidos (peso <= 0 o altura <= 0)
            * 1: Bajo peso (IMC < 18.5)
            * 2: Normal (18.5 <= IMC < 25)
            * 3: Sobrepeso (25 <= IMC < 30)
            * 4: Obesidad (IMC >= 30)
        
    Nota:
        - Fórmula: IMC = peso / (altura * altura)
        - Validar primero datos inválidos, luego rangos, finalmente calcular
    """
    pass
```

**Entrada de ejemplo:**
```
Peso en kg: 70
Altura en metros: 1.75
```

**Salida esperada:**
```
Peso: 70.0 kg
Altura: 1.75 m
IMC: 22.86
Categoría: Peso Normal
```

**Requisitos de implementación:**
- La función `calcular_imc` debe estar implementada exactamente como se especifica
- Validar que peso y altura sean positivos
- Validar rangos razonables (peso: 20-300 kg, altura: 0.5-2.5 m)
- El programa principal debe:
  - Calcular el IMC real: peso / (altura * altura)
  - Mapear el código a mensajes:
    * -3: "Error: Peso fuera de rango"
    * -2: "Error: Altura fuera de rango"
    * -1: "Error: Datos inválidos"
    * 1: "Bajo peso"
    * 2: "Peso Normal"
    * 3: "Sobrepeso"
    * 4: "Obesidad"
- Mostrar IMC con 2 decimales

**Casos de prueba que se evaluarán:**
- Todas las categorías (Bajo peso, Normal, Sobrepeso, Obesidad)
- Límites de categorías (18.5, 25, 30)
- Validación de rangos
- Datos inválidos

---

## Ejercicio 5: Conversor de Tiempo

**Contexto:** Estás desarrollando una app de productividad que registra tiempo en segundos.

**Descripción:**
Crea un programa que convierta una cantidad de segundos a formato "X días, Y horas, Z minutos, W segundos".

**Especificación de la función obligatoria:**

```python
def validar_segundos(segundos_totales: int) -> int:
    """
    Valida que los segundos sean un valor válido.
    
    Args:
        segundos_totales: Cantidad total de segundos a validar
        
    Returns:
        int: El mismo valor si es válido (>= 0), o -1 si es inválido (< 0)
        
    Nota:
        - Los segundos deben ser >= 0
        - Si son negativos, devolver -1
        - Si son válidos, devolver el mismo valor
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce el número de segundos: 100000
```

**Salida esperada:**
```
100000 segundos equivalen a:
1 día(s), 3 hora(s), 46 minuto(s), 40 segundo(s)
```

**Requisitos de implementación:**
- La función `validar_segundos` debe estar implementada exactamente como se especifica
- El programa principal debe:
  - Llamar a `validar_segundos` para verificar el input
  - Si es válido, hacer la conversión en main usando operaciones // y %:
    * dias = segundos // 86400
    * resto = segundos % 86400
    * horas = resto // 3600
    * resto = resto % 3600
    * minutos = resto // 60
    * segundos = resto % 60
- Validar que los segundos sean positivos o cero
- Usar plurales correctamente en la salida (opcional)

**Casos de prueba que se evaluarán:**
- Conversiones completas (días + horas + minutos + segundos)
- Solo algunos componentes (ej: solo horas y minutos)
- Casos límite (0 segundos, 1 día exacto, etc.)
- Números negativos

---

## Ejercicio 6: Detector de Años Bisiestos

**Contexto:** Desarrollas un calendario digital que necesita detectar años bisiestos.

**Descripción:**
Un año es bisiesto si:
- Es divisible por 4 Y
- Si es divisible por 100, también debe ser divisible por 400

Ejemplos: 2000 (sí), 1900 (no), 2024 (sí), 2023 (no)

**Especificación de la función obligatoria:**

```python
def es_bisiesto(anio: int) -> tuple[bool, int]:
    """
    Determina si un año es bisiesto y devuelve un código de razón.
    
    Args:
        anio: El año a verificar
        
    Returns:
        tuple[bool, int]: (es_bisiesto, codigo_razon)
            - es_bisiesto: True si es bisiesto, False si no
            - codigo_razon: Código que indica la razón:
                * 0: Año fuera de rango (< 1582 o > 3000)
                * 1: Es bisiesto - divisible por 400
                * 2: No es bisiesto - divisible por 100 pero no por 400
                * 3: Es bisiesto - divisible por 4 pero no por 100
                * 4: No es bisiesto - no divisible por 4
        
    Nota:
        - Si año < 1582 o año > 3000, devolver (False, 0)
        - 1582 es el año de adopción del calendario gregoriano
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce un año: 2024
```

**Salida esperada:**
```
El año 2024 SÍ es bisiesto
Razón: Es divisible por 4 y no es un año secular (no es divisible por 100)
Tendrá 366 días (febrero con 29 días)
```

**Requisitos de implementación:**
- La función `es_bisiesto` debe estar implementada exactamente como se especifica
- Implementar la lógica correcta de año bisiesto
- Validar que el año esté entre 1582 y 3000
- Mostrar el mensaje correspondiente al código de razón
- Indicar días totales del año y días de febrero

**Casos de prueba que se evaluarán:**
- Años bisiestos normales (divisibles por 4)
- Años seculares no bisiestos (1900)
- Años seculares bisiestos (2000)
- Años no bisiestos normales
- Validación de rangos

---

## Ejercicio 7: Calculadora de Descuentos Progresivos

**Contexto:** Gestionas una tienda online con descuentos por volumen de compra.

**Descripción:**
Calcula el precio final aplicando descuentos progresivos:
- Compra menor a 100€: sin descuento
- Compra entre 100€ y 200€: 10% de descuento
- Compra entre 200€ y 500€: 15% de descuento
- Compra mayor a 500€: 20% de descuento

Además, si el cliente es "premium", añadir un 5% extra de descuento sobre el precio ya descontado.

**Especificación de la función obligatoria:**

```python
def calcular_precio_final(importe: float, es_premium: bool) -> float:
    """
    Calcula el precio final aplicando descuentos por volumen y premium.
    
    Args:
        importe: Importe original de la compra (debe ser > 0)
        es_premium: True si el cliente es premium, False si no
        
    Returns:
        float: Precio final a pagar después de aplicar todos los descuentos
        
    Nota:
        - Si importe <= 0, devolver 0.0
        - El descuento premium se aplica DESPUÉS del descuento por volumen
        - Descuentos por volumen:
            * < 100€: 0%
            * 100-199.99€: 10%
            * 200-499.99€: 15%
            * >= 500€: 20%
        - Descuento premium: 5% adicional sobre el precio ya descontado
        - Proceso:
            1. Calcular descuento por volumen
            2. Aplicar descuento: subtotal = importe - descuento_volumen
            3. Si es premium: descuento_premium = subtotal * 0.05
            4. precio_final = subtotal - descuento_premium
    """
    pass
```

**Entrada de ejemplo:**
```
Importe de la compra: 250.00
¿Cliente premium? (si/no): si
```

**Salida esperada:**
```
Importe original: 250.00€
Descuento por volumen (15%): -37.50€
Subtotal: 212.50€
Descuento premium (5%): -10.63€
Total a pagar: 201.87€
Ahorro total: 48.13€ (19.25%)
```

**Requisitos de implementación:**
- La función `calcular_precio_final` debe estar implementada exactamente como se especifica
- Validar que el importe sea positivo
- Calcular descuentos correctamente en orden (primero volumen, luego premium sobre el subtotal)
- El programa principal debe:
  - Llamar a la función para obtener el precio final
  - Para mostrar el desglose, recalcular los descuentos:
    * Determinar el porcentaje de descuento por volumen
    * descuento_volumen = importe * porcentaje
    * subtotal = importe - descuento_volumen
    * Si premium: descuento_premium = subtotal * 0.05
    * Verificar que precio_final coincida
- Mostrar desglose completo de descuentos
- Calcular porcentaje de ahorro total

**Casos de prueba que se evaluarán:**
- Todos los rangos de descuento por volumen
- Con y sin cliente premium
- Límites de rangos exactos (100, 200, 500)
- Cálculo de descuentos acumulados
- Importe inválido (0 o negativo)

---

## Ejercicio 8: Validador de Contraseñas Seguras

**Contexto:** Creas una herramienta que valida si una contraseña es segura.

**Descripción:**
Verifica si una contraseña cumple estos requisitos de seguridad:
1. Longitud mínima de 8 caracteres
2. Contiene al menos una letra mayúscula
3. Contiene al menos una letra minúscula
4. Contiene al menos un dígito
5. Contiene al menos un carácter especial (!@#$%&*)

**Especificación de la función obligatoria:**

```python
def validar_contrasena(contrasena: str) -> tuple[bool, int, int, int, int, int]:
    """
    Valida si una contraseña cumple los requisitos de seguridad.
    
    Args:
        contrasena: La contraseña a validar
        
    Returns:
        tuple[bool, int, int, int, int, int]: 
            (es_valida, tiene_longitud, tiene_mayuscula, tiene_minuscula, tiene_digito, tiene_especial)
            donde cada componente booleana se representa como int (1 = True, 0 = False)
        
    Nota:
        - Longitud mínima: 8 caracteres
        - Debe contener al menos: 1 mayúscula, 1 minúscula, 1 dígito, 1 carácter especial (!@#$%&*)
        - Usar bucles para revisar cada carácter
        - Comparar caracteres: 'A' <= c <= 'Z', 'a' <= c <= 'z', '0' <= c <= '9'
        - es_valida es True solo si todos los demás valores son 1
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce una contraseña: MiPass123!
```

**Salida esperada:**
```
Analizando contraseña: MiPass123!

✓ Longitud adecuada (10 caracteres)
✓ Contiene mayúsculas
✓ Contiene minúsculas
✓ Contiene números
✓ Contiene caracteres especiales

Resultado: CONTRASEÑA SEGURA
```

**Requisitos de implementación:**
- La función `validar_contrasena` debe estar implementada exactamente como se especifica
- NO usar métodos como .isupper(), .islower(), .isdigit()
- Usar bucles y comparaciones de caracteres (ej: 'A' <= c <= 'Z')
- El programa principal debe mostrar cada requisito con ✓ o ✗:
  - Si tiene_longitud == 1: "✓ Longitud adecuada", sino "✗ Longitud insuficiente"
  - Si tiene_mayuscula == 1: "✓ Contiene mayúsculas", sino "✗ No contiene mayúsculas"
  - Si tiene_minuscula == 1: "✓ Contiene minúsculas", sino "✗ No contiene minúsculas"
  - Si tiene_digito == 1: "✓ Contiene números", sino "✗ No contiene números"
  - Si tiene_especial == 1: "✓ Contiene caracteres especiales", sino "✗ No contiene caracteres especiales"
  - Si es_valida == True: "CONTRASEÑA SEGURA", sino "CONTRASEÑA INSEGURA"
- Caracteres especiales válidos: !@#$%&*

**Casos de prueba que se evaluarán:**
- Contraseñas que cumplen todos los requisitos
- Contraseñas que fallan en cada requisito individual
- Contraseña vacía
- Contraseñas en límites (7, 8 caracteres)
- Combinaciones de requisitos faltantes

---

## Ejercicio 9: Simulador de Carrera de Caracoles

**Contexto:** Estás creando un juego educativo sobre carreras de caracoles.

**Descripción:**
Simula una carrera entre 3 caracoles. Cada caracol tiene una velocidad diferente (cm/turno).
En cada turno, todos los caracoles avanzan simultáneamente según su velocidad.
Gana el primero en llegar a la meta.

**Especificación de la función obligatoria:**

```python
def simular_carrera(velocidad1: int, velocidad2: int, velocidad3: int, distancia_meta: int) -> tuple[int, int]:
    """
    Simula una carrera de 3 caracoles y determina el ganador y turnos necesarios.
    
    Args:
        velocidad1: Velocidad del caracol 1 (cm/turno, 1-10)
        velocidad2: Velocidad del caracol 2 (cm/turno, 1-10)
        velocidad3: Velocidad del caracol 3 (cm/turno, 1-10)
        distancia_meta: Distancia de la meta en cm (debe ser > 0)
        
    Returns:
        tuple[int, int]: (ganador, turnos_necesarios)
            - ganador: Número del caracol ganador (1, 2 o 3), o 0 si hay error
            - turnos_necesarios: Número de turnos que duró la carrera
        
    Nota:
        - Si alguna velocidad < 1 o > 10, devolver (0, 0)
        - Si distancia_meta <= 0, devolver (0, 0)
        - Si hay empate, gana el caracol con número más bajo
        - Todos los caracoles avanzan simultáneamente cada turno
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce las velocidades de los caracoles (1-10 cm/turno):
Velocidad caracol 1: 5
Velocidad caracol 2: 3
Velocidad caracol 3: 7
Distancia de la meta (cm): 100
```

**Salida esperada:**
```
🐌 RESULTADO DE LA CARRERA 🐌

Distancia de la meta: 100 cm
Turnos necesarios: 15

Velocidades:
  🐌 Caracol 1: 5 cm/turno
  🐌 Caracol 2: 3 cm/turno
  🐌 Caracol 3: 7 cm/turno

Distancias alcanzadas:
  Caracol 1: 75 cm
  Caracol 2: 45 cm
  Caracol 3: 105 cm

🏆 ¡GANADOR: Caracol 3!
```

**Requisitos de implementación:**
- La función `simular_carrera` debe estar implementada exactamente como se especifica
- Validar que las velocidades estén en el rango [1-10]
- Validar que la distancia sea positiva
- Usar un bucle para simular turnos
- En cada turno, todos avanzan simultáneamente
- En caso de empate, gana el de menor número
- El programa principal puede calcular y mostrar:
  - Los turnos necesarios: distancia_meta // velocidad_ganador (aproximado)
  - Las distancias alcanzadas por cada caracol
  - Información detallada de la carrera

**Casos de prueba que se evaluarán:**
- Diferentes combinaciones de velocidades
- Empates entre caracoles
- Validación de rangos (velocidades y distancia)
- Distancias cortas y largas
- Identificación correcta del ganador

---

## Ejercicio 10: Calculadora de Estadísticas Básicas

**Contexto:** Desarrollas una herramienta para analizar conjuntos de números.

**Descripción:**
Solicita números positivos al usuario hasta que ingrese 0.
Luego calcula y muestra:
- Cantidad de números
- Suma total
- Promedio
- Número máximo
- Número mínimo
- Rango (máximo - mínimo)

**Especificación de la función obligatoria:**

```python
def calcular_promedio(suma_total: int, cantidad: int) -> float:
    """
    Calcula el promedio a partir de la suma y cantidad.
    
    Args:
        suma_total: Suma total de todos los números
        cantidad: Cantidad de números procesados
        
    Returns:
        float: Promedio (suma / cantidad), o 0.0 si hay error
        
    Nota:
        - Si cantidad <= 0, devolver 0.0
        - Si suma_total < 0, devolver 0.0
        - El promedio debe tener precisión de float
    """
    pass
```

**Entrada de ejemplo:**
```
Introduce números positivos (0 para terminar):
Número 1: 10
Número 2: 20
Número 3: 15
Número 4: 25
Número 5: 30
Número 6: 0
```

**Salida esperada:**
```
📊 ESTADÍSTICAS DE LOS NÚMEROS INTRODUCIDOS 📊

Cantidad de números: 5
Suma total: 100
Promedio: 20.00
Número máximo: 30
Número mínimo: 10
Rango (máx - mín): 20
```

**Requisitos de implementación:**
- La función `calcular_promedio` debe estar implementada exactamente como se especifica
- Solicitar números en un bucle hasta que se ingrese 0
- Validar que los números sean positivos (rechazar negativos)
- El programa principal debe:
  - Ir acumulando: cantidad, suma_total, máximo y mínimo
  - Calcular máximo y mínimo usando bucles (NO usar max() o min())
  - Llamar a `calcular_promedio` para obtener el promedio
  - Calcular el rango: maximo - minimo
- Mostrar promedio con 2 decimales
- Mostrar todas las estadísticas

**Casos de prueba que se evaluarán:**
- Conjunto normal de números
- Un solo número
- Números iguales
- Validación de datos (cantidad y suma negativos)
- Cálculo correcto del promedio
- Casos con cantidad = 0

---

## Parte 2/3 y 3/3

**Los ejercicios 11-20 y 21-30 se publicarán en las siguientes entregas.**

Estos ejercicios incrementarán la dificultad progresivamente, integrando:
- Validaciones más complejas
- Algoritmos de búsqueda y ordenación básicos
- Simulaciones más elaboradas
- Problemas del mundo real más desafiantes

---

## Evaluación

Cada ejercicio se evaluará mediante:
1. **Tests automáticos** (60%): Tu código debe pasar todos los tests
2. **Estilo y documentación** (20%): Docstrings, comentarios, tipos
3. **Eficiencia** (20%): Uso correcto de estructuras de control

**Recuerda:** La función especificada en cada ejercicio es **obligatoria** y se evaluará automáticamente.

---

## Recursos de Ayuda

- Documentación de Python: [docs.python.org](https://docs.python.org)
- Guía de type hints: PEP 484
- Estilo de código: PEP 8

**¡Buena suerte! 🚀**

--- Turno 1 ---
Ana avanza 2 metros (2/20)
Luis avanza 3 metros (3/20)

--- Turno 2 ---
Ana avanza 3 metros (5/20)
Luis avanza 1 metro (4/20)

[...]

--- Turno 8 ---
Ana avanza 2 metros (20/20)
¡Ana gana la carrera en 8 turnos!
```

**Requisitos de implementación:**
- Usar import random para generar avances aleatorios
- Mostrar progreso en cada turno
- Detectar ganador correctamente
- Si hay empate en el turno, gana el corredor 1

**Casos de prueba que se evaluarán:**
- Victoria del corredor 1
- Victoria del corredor 2
- Empate (ambos llegan en el mismo turno)
- Carreras con seed fija (reproducibles)

---

## Ejercicio 10: Estadísticas de Lista de Números

**Contexto:** Analizas datos de sensores que miden temperatura durante el día.

**Descripción:**
Pide al usuario N números (temperaturas) y calcula:
1. La cantidad de números introducidos
2. La suma total
3. La media (promedio)
4. El número mayor y menor
5. Cuántos números están por encima de la media

**Especificación de la función obligatoria:**

```python
def calcular_estadisticas(cantidad: int) -> tuple[float, float, float, float, int]:
    """
    Solicita números al usuario y calcula estadísticas.
    
    IMPORTANTE: Esta función debe solicitar los números dentro de ella usando input().
    
    Args:
        cantidad: Cuántos números solicitar (debe ser > 0)
        
    Returns:
        tuple[float, float, float, float, int]: (suma, media, maximo, minimo, cantidad_sobre_media)
            - suma: Suma de todos los números
            - media: Promedio de los números
            - maximo: El número mayor
            - minimo: El número menor
            - cantidad_sobre_media: Cuántos números están por encima de la media
        
    Nota:
        - Si cantidad <= 0, devolver (0.0, 0.0, 0.0, 0.0, 0)
        - NO usar listas, trabajar con variables acumuladoras
        - Pedir los números dentro de la función usando bucles
    """
    pass
```

**Entrada de ejemplo:**
```
¿Cuántos números vas a introducir? 5
Número 1: 23.5
Número 2: 19.0
Número 3: 25.8
Número 4: 21.3
Número 5: 24.1
```

**Salida esperada:**
```
--- ESTADÍSTICAS ---
Cantidad de valores: 5
Suma total: 113.70
Media: 22.74
Valor máximo: 25.80
Valor mínimo: 19.00
Valores por encima de la media: 3
```

**Requisitos de implementación:**
- NO usar listas ni arrays
- Usar variables acumuladoras y bucles
- Calcular el máximo y mínimo durante la lectura
- Para contar valores sobre la media: hacer dos pasadas (primera para calcular media, segunda para contar)
- Validar que cantidad sea positiva

**Casos de prueba que se evaluarán:**
- Diferentes cantidades de números
- Todos los números iguales
- Números en orden creciente/decreciente
- Un solo número
- Cantidad inválida (0 o negativa)

---

## Entrega

**Estructura de carpetas:**
```
practica005/
├── ejercicio01.py
├── ejercicio02.py
├── ejercicio03.py
├── ejercicio04.py
├── ejercicio05.py
├── ejercicio06.py
├── ejercicio07.py
├── ejercicio08.py
├── ejercicio09.py
├── ejercicio10.py
└── README.md  (con tu nombre y observaciones)
```

**Fecha de entrega:** [A definir por el profesor]

**Evaluación:**
- Corrección funcional: 40%
- Calidad del código (funciones, nombres, comentarios): 30%
- Validaciones de entrada: 20%
- Documentación (docstrings, type hints): 10%

---

## Consejos

1. **Lee bien el enunciado** antes de programar
2. **Planifica con pseudocódigo** para ejercicios complejos
3. **Prueba con varios casos**, incluyendo casos extremos
4. **Modulariza**: divide problemas grandes en funciones pequeñas
5. **Nombra bien**: usa nombres descriptivos para variables y funciones
6. **Comenta**: explica la lógica compleja, no lo obvio
7. **Valida siempre**: asegura que las entradas sean correctas

¡Buena suerte! 🚀
